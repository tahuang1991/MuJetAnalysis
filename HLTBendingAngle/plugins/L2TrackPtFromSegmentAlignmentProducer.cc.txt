// Framework
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/Common/interface/Handle.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "DataFormats/TrackReco/interface/TrackExtra.h"
#include "DataFormats/TrackReco/interface/TrackExtraFwd.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"

#include "DataFormats/DTRecHit/interface/DTRecSegment4DCollection.h"
#include "DataFormats/CSCRecHit/interface/CSCSegmentCollection.h"

#include "Geometry/Records/interface/MuonGeometryRecord.h"
#include "Geometry/CSCGeometry/interface/CSCGeometry.h"
#include "Geometry/DTGeometry/interface/DTGeometry.h"

#include "RecoMuon/TrackingTools/interface/MuonTrackLoader.h"
#include "RecoMuon/TrackingTools/interface/MuonServiceProxy.h"
#include "TrackingTools/PatternTools/interface/TrajTrackAssociation.h"
#include "TrackingTools/PatternTools/interface/TrajectoryBuilder.h"
#include "TrackingTools/PatternTools/interface/Trajectory.h"
#include "MuJetAnalysis/HLTBendingAngle/plugins/L2TrackPtFromSegmentAlignmentProducer.h"
#include "DataFormats/TrackReco/interface/TrackToTrackMap.h"
#include "DataFormats/MuonSeed/interface/L2MuonTrajectorySeedCollection.h"

#include <string>

using namespace edm;
using namespace std;
using namespace reco;

/// constructor with config
L2TrackPtFromSegmentAlignmentProducer::L2TrackPtFromSegmentAlignmentProducer(const ParameterSet& iConfig)
{
  LogTrace("Muon|RecoMuon|L2TrackPtFromSegmentAlignmentProducer")<<" constructor called";

  // service parameters
  ParameterSet serviceParameters = iConfig.getParameter<ParameterSet>("ServiceParameters");
  
  // TrackLoader parameters
  ParameterSet trackLoaderParameters = iConfig.getParameter<ParameterSet>("TrackLoaderParameters");

  // the services
  service_ = new MuonServiceProxy(serviceParameters);

  muonTrackLoader_ = new MuonTrackLoader(trackLoaderParameters, service_);
  
  // StandAlone Collection Label
  theL2CollectionLabel_ = iConfig.getParameter<edm::InputTag>("InputObjects");
  trackToken_ = consumes<reco::TrackCollection>(theL2CollectionLabel_);
  trajectoryToken_ = consumes<std::vector<Trajectory> >(theL2CollectionLabel_);

  produces<reco::TrackCollection>();
  produces<reco::TrackCollection>("UpdatedAtVtx");
  produces<TrackingRecHitCollection>();
  produces<reco::TrackExtraCollection>();
  produces<reco::TrackToTrackMap>();

  produces<std::vector<Trajectory> >();
  produces<TrajTrackAssociationCollection>();

  produces<edm::AssociationMap<edm::OneToMany<std::vector<L2MuonTrajectorySeed>, std::vector<L2MuonTrajectorySeed> > > >();

}
  
/// destructor
L2TrackPtFromSegmentAlignmentProducer::~L2TrackPtFromSegmentAlignmentProducer()
{
  LogTrace("Muon|RecoMuon|L2TrackPtFromSegmentAlignmentProducer")<<" L2TrackPtFromSegmentAlignmentProducer destructor called";
  delete service_;
}

void 
L2TrackPtFromSegmentAlignmentProducer::beginRun(edm::Run &run, const edm::EventSetup &eventSetup)
{
}  

/// reconstruct muons
void 
L2TrackPtFromSegmentAlignmentProducer::produce(edm::Event& event, const edm::EventSetup& eventSetup)
{
  const std::string metname = "Muon|RecoMuon|L2MuonProducer";
  
  LogTrace(metname)<<endl<<endl<<endl;
  LogTrace(metname)<<"L2 Muon Reconstruction Started"<<endl;

  // Update the services
  service_->update(eventSetup);

  // get the geometries
  try {
    eventSetup.get<MuonGeometryRecord>().get(csc_geom);
    csc_geometry_ = &*csc_geom;
  } catch (edm::eventsetup::NoProxyException<CSCGeometry>& e) {
    LogDebug("L2TrackPtFromSegmentAlignmentProducer") << "+++ Info: CSC geometry is unavailable. +++\n";
  }

  try {
    eventSetup.get<MuonGeometryRecord>().get(dt_geom);
    dt_geometry_ = &*dt_geom;
  } catch (edm::eventsetup::NoProxyException<DTGeometry>& e) {
    LogDebug("L2TrackPtFromSegmentAlignmentProducer") << "+++ Info: DT geometry is unavailable. +++\n";
  }

  // Take the SA container
  edm::Handle<reco::TrackCollection> input_tracksH; 
  event.getByToken(trackToken_, input_tracksH);
  const reco::TrackCollection& input_tracks(*input_tracksH.product());
  
  // load the trajectories
  edm::Handle<std::vector<Trajectory> > trajectoriesH;
  event.getByToken(trajectoryToken_, trajectoriesH);
  const std::vector<Trajectory>& trajectories(*trajectoriesH.product());
  
  // Loop on all tracks
  bool verbose = true;
  for (unsigned int i=0; i<input_tracks.size(); i++) {
    
    // get the associated recotrack
    auto recoTrack(input_tracks[i]);

    // get the associated recotrack extra object
    auto recoTrackExtra(*(recoTrack.extra()));
    
    // print some relevant information
    if (verbose) {
      std::cout << "RecoTrackExtra " << std::endl
                << "\tpT_inner: "<<recoTrackExtra.innerMomentum().Rho() << std::endl
                << "\teta_inner: "<<recoTrackExtra.innerPosition().eta() << std::endl
                << "\tphi_inner: "<<recoTrackExtra.innerPosition().phi() << std::endl
                << "\tpT_outer: "<<recoTrackExtra.outerMomentum().Rho() << std::endl
                << "\teta_outer: "<<recoTrackExtra.outerPosition().eta() << std::endl
                << "\tphi_outer: "<<recoTrackExtra.outerPosition().phi() <<std::endl;  
    }

    const double newPt(ptFromBending(recoTrackExtra));
    // std::cout << "Assign Pt" << std::endl;
    
    
    /* 
       Get the track's propagation direction. 
       Make a new measurement with the new pT value and replace it 
       with the old measurement
    */
    Trajectory trajectory(trajectories[i]);
    PropagationDirection direc(trajectory.direction());
    if (direc==PropagationDirection::oppositeToMomentum){
      TrajectoryMeasurement newMeas;
      updateTrajectoryMeasurement(trajectory.lastMeasurement(), newMeas, newPt);

      trajectory.pop();
      trajectory.push(newMeas);
    }
    else if (direc==PropagationDirection::alongMomentum){
      TrajectoryMeasurement newMeas;
      updateTrajectoryMeasurement(trajectory.firstMeasurement(), newMeas, newPt);

      trajectory.reverse();
      trajectory.pop();
      trajectory.push(newMeas);
      trajectory.reverse();
    }
  } // end loop on muons
  
  // make a new vector
  // std::cout << "-----------------------------------" << std::endl;
  // std::cout << "Construct a new TrajectoryContainer" << std::endl; 
  TrajectoryContainer newTrajVector;
  for (auto t: trajectories) newTrajVector.push_back(new Trajectory(t));
  
  // load the trajectories in the trackloader
  // std::cout << "load the trajectories in the trackloader" << std::endl;
  OrphanHandle<reco::TrackCollection> orphanHandleTracks(muonTrackLoader_->loadTracks(newTrajVector, event));

  LogTrace(metname)<<"Event loaded"
		   <<"================================"
		   <<endl<<endl;
}

void 
L2TrackPtFromSegmentAlignmentProducer::bookTree()
{
  edm::Service<TFileService> fs;
  track_tree_ = fs->make<TTree>("Tracks", "Tracks");
  track_tree_->Branch("x_gp_MB1",&my_track_.x_gp_MB1);
  track_tree_->Branch("y_gp_MB1",&my_track_.y_gp_MB1);
  track_tree_->Branch("z_gp_MB1",&my_track_.z_gp_MB1);
  track_tree_->Branch("x_gp_MB2",&my_track_.x_gp_MB2);
  track_tree_->Branch("y_gp_MB2",&my_track_.y_gp_MB2);
  track_tree_->Branch("z_gp_MB2",&my_track_.z_gp_MB2);
  track_tree_->Branch("x_gp_MB3",&my_track_.x_gp_MB3);
  track_tree_->Branch("y_gp_MB3",&my_track_.y_gp_MB3);
  track_tree_->Branch("z_gp_MB3",&my_track_.z_gp_MB3);

  track_tree_->Branch("x_gp_ME1",&my_track_.x_gp_ME1);
  track_tree_->Branch("y_gp_ME1",&my_track_.y_gp_ME1);
  track_tree_->Branch("z_gp_ME1",&my_track_.z_gp_ME1);
  track_tree_->Branch("x_gp_ME2",&my_track_.x_gp_ME2);
  track_tree_->Branch("y_gp_ME2",&my_track_.y_gp_ME2);
  track_tree_->Branch("z_gp_ME2",&my_track_.z_gp_ME2);
  track_tree_->Branch("x_gp_ME3",&my_track_.x_gp_ME3);
  track_tree_->Branch("y_gp_ME3",&my_track_.y_gp_ME3);
  track_tree_->Branch("z_gp_ME3",&my_track_.z_gp_ME3);

  track_tree_->Branch("phi_gp_MB1",&my_track_.phi_gp_MB1);
  track_tree_->Branch("phi_gp_MB2",&my_track_.phi_gp_MB2);
  track_tree_->Branch("phi_gp_MB3",&my_track_.phi_gp_MB3);
  track_tree_->Branch("phi_gv_MB1",&my_track_.phi_gv_MB1);
  track_tree_->Branch("phi_gv_MB2",&my_track_.phi_gv_MB2);
  track_tree_->Branch("phi_gv_MB3",&my_track_.phi_gv_MB3);
  track_tree_->Branch("phi_gv_MB4",&my_track_.phi_gv_MB4);

  track_tree_->Branch("phi_gp_ME1",&my_track_.phi_gp_ME1);
  track_tree_->Branch("phi_gp_ME2",&my_track_.phi_gp_ME2);
  track_tree_->Branch("phi_gp_ME3",&my_track_.phi_gp_ME3);
  track_tree_->Branch("phi_gv_ME1",&my_track_.phi_gv_ME1);
  track_tree_->Branch("phi_gv_ME2",&my_track_.phi_gv_ME2);
  track_tree_->Branch("phi_gv_ME3",&my_track_.phi_gv_ME3);

  track_tree_->Branch("dx_gp_MB1_MB2",&my_track_.dx_gp_MB1_MB2);
  track_tree_->Branch("dy_gp_MB1_MB2",&my_track_.dy_gp_MB1_MB2);
  track_tree_->Branch("dz_gp_MB1_MB2",&my_track_.dz_gp_MB1_MB2);
  track_tree_->Branch("dx_gp_MB2_MB3",&my_track_.dx_gp_MB2_MB3);
  track_tree_->Branch("dy_gp_MB2_MB3",&my_track_.dy_gp_MB2_MB3);
  track_tree_->Branch("dz_gp_MB2_MB3",&my_track_.dz_gp_MB2_MB3);

  track_tree_->Branch("dx_gp_ME1_ME2",&my_track_.dx_gp_ME1_ME2);
  track_tree_->Branch("dy_gp_ME1_ME2",&my_track_.dy_gp_ME1_ME2);
  track_tree_->Branch("dz_gp_ME1_ME2",&my_track_.dz_gp_ME1_ME2);
  track_tree_->Branch("dx_gp_ME2_ME3",&my_track_.dx_gp_ME2_ME3);
  track_tree_->Branch("dy_gp_ME2_ME3",&my_track_.dy_gp_ME2_ME3);
  track_tree_->Branch("dz_gp_ME2_ME3",&my_track_.dz_gp_ME2_ME3);

  track_tree_->Branch("dphi_gp_MB1_MB2",&my_track_.dphi_gp_MB1_MB2);
  track_tree_->Branch("dphi_gp_MB1_MB4",&my_track_.dphi_gp_MB1_MB4);
  track_tree_->Branch("dphi_gp_ME1_ME2",&my_track_.dphi_gp_ME1_ME2);
  track_tree_->Branch("dphi_gp_ME2_ME3",&my_track_.dphi_gp_ME2_ME3);
}


void
L2TrackPtFromSegmentAlignmentProducer::updateTrajectoryMeasurement(const TrajectoryMeasurement& oldMeas, TrajectoryMeasurement& newMeas, double newPt)
{
  /*
    The transverse momentum is in the global coordinate system. We do not wish 
    to change the other track quantities (errors, surface, charge,...). We need to 
    extract the global momentum from the old TSOS. We update the momentum and 
    create a new TSOS using that momentum.
  */
  
  // get the old TSOS 
  // std::cout << "get the old TSOS" << std::endl;
  TrajectoryStateOnSurface tsos(oldMeas.updatedState());
  
  // get the old global momentum
  // std::cout << "get the old global momentum" << std::endl;
  GlobalVector oldGlobalMomentum(tsos.globalMomentum());

  // calculate the scale factor by which we scale the pT
  // std::cout << "calculate the scale factor by which we scale the pT" << std::endl;
  double oldPt(oldGlobalMomentum.perp());
  double scaleFactor(newPt/oldPt);

  // make a new global vector with the pT scaled
  // std::cout << "make a new global vector with the pT scaled" << std::endl;
  double newPx(oldGlobalMomentum.x()*scaleFactor);
  double newPy(oldGlobalMomentum.y()*scaleFactor);
  double newPz(oldGlobalMomentum.z()*scaleFactor);
                         
  GlobalVector newGlobalMomentum(newPx, newPy, newPz);
  
  // get the old global parameters
  // std::cout << "get the old global parameters" << std::endl;
  GlobalTrajectoryParameters oldGlobalParameters(tsos.globalParameters());
  
  // make new global parameters using the new momentum
  // do not change the position, charge or magnetic field
  // std::cout << "make new global parameters using the new momentum" << std::endl;
  GlobalTrajectoryParameters newGlobalParameters(oldGlobalParameters.position(),
                                                 newGlobalMomentum,
                                                 oldGlobalParameters.charge(),
                                                 &oldGlobalParameters.magneticField());
  
  // make a new TSOS
  // do not change the error or the surface
  // std::cout << "make a new TSOS" << std::endl;
  TrajectoryStateOnSurface newTSOS(newGlobalParameters,
                                   tsos.cartesianError(),
                                   tsos.surface());
  
  // make a new measurement
  // do not change the forward state, backward state, rechit or estimate
  // std::cout << "make a new measurement" << std::endl;
  newMeas = TrajectoryMeasurement(oldMeas.forwardPredictedState(),
                                  oldMeas.backwardPredictedState(),
                                  newTSOS,
                                  oldMeas.recHit(),
                                  oldMeas.estimate());
  // std::cout << "End" << std::endl;
}


double
L2TrackPtFromSegmentAlignmentProducer::ptFromBending(const reco::TrackExtra& recoTrackExtra)
{
  double newPt = -1;
  double verbose =false;
  // load the segments
  for(auto rh = recoTrackExtra.recHitsBegin(); rh != recoTrackExtra.recHitsEnd(); rh++) {
    
      // check if rechit is valid
      if (!(**rh).isValid()) continue;
      
      auto id((**rh).rawId());
      if ((DetId(id)).subdetId() == MuonSubdetId::DT) {
        const DTRecSegment4D *seg = dynamic_cast<const DTRecSegment4D*>(rh->get());
        DTChamberId detId(id);
        
        if (verbose) {
          std::cout << "\t\tDT  :: id :: " << DTChamberId(id) << std::endl;
          std::cout << "\t\t    :: segment :: " << *seg << std::endl;
        }

	// std::cout << "Getting global directions" << std::endl;

        const LocalPoint lp_seg(seg->localPosition());
        const GlobalPoint gp_seg(dt_geom->idToDet((**rh).rawId())->surface().toGlobal(lp_seg));

        const LocalVector lv_seg(seg->localDirection());
        const GlobalVector gv_seg(dt_geom->idToDet((**rh).rawId())->surface().toGlobal(lv_seg));
        
	// std::cout << "Found global directions" << std::endl;

        if (detId.station() == 1) {
          my_track_.x_gp_MB1 = gp_seg.x(); 
          my_track_.y_gp_MB1 = gp_seg.y(); 
          my_track_.z_gp_MB1 = gp_seg.z(); 
          my_track_.phi_gp_MB1 = gp_seg.phi(); 
          my_track_.phi_gv_MB1 = gv_seg.phi(); 
          
          if (verbose) {
            std::cout << "phi_gp_MB1 " << my_track_.phi_gp_MB1 << std::endl;
            std::cout << "phi_gv_MB1 " << my_track_.phi_gv_MB1 << std::endl;
            std::cout << "x_gp_MB1 " << my_track_.x_gp_MB1 << std::endl;
            std::cout << "y_gp_MB1 " << my_track_.y_gp_MB1 << std::endl;
            std::cout << "z_gp_MB1 " << my_track_.z_gp_MB1 << std::endl;
          }
        }
        else if (detId.station() == 2) {
          my_track_.x_gp_MB2 = gp_seg.x(); 
          my_track_.y_gp_MB2 = gp_seg.y(); 
          my_track_.z_gp_MB2 = gp_seg.z(); 
          my_track_.phi_gp_MB2 = gp_seg.phi(); 
          my_track_.phi_gv_MB2 = gv_seg.phi(); 

          if (verbose) {
            std::cout << "phi_gp_MB2 " << my_track_.phi_gp_MB2 << std::endl;
            std::cout << "phi_gv_MB2 " << my_track_.phi_gv_MB2 << std::endl;
            std::cout << "x_gp_MB2 " << my_track_.x_gp_MB2 << std::endl;
            std::cout << "y_gp_MB2 " << my_track_.y_gp_MB2 << std::endl;
            std::cout << "z_gp_MB2 " << my_track_.z_gp_MB2 << std::endl;
          }
        }
        else if (detId.station() == 3) {
          my_track_.x_gp_MB3 = gp_seg.x(); 
          my_track_.y_gp_MB3 = gp_seg.y(); 
          my_track_.z_gp_MB3 = gp_seg.z(); 
          my_track_.phi_gp_MB3 = gp_seg.phi(); 
          my_track_.phi_gv_MB3 = gv_seg.phi(); 

          if (verbose) {
            std::cout << "phi_gp_MB3 " << my_track_.phi_gp_MB3 << std::endl;
            std::cout << "phi_gv_MB3 " << my_track_.phi_gv_MB3 << std::endl;
            std::cout << "x_gp_MB3 " << my_track_.x_gp_MB3 << std::endl;
            std::cout << "y_gp_MB3 " << my_track_.y_gp_MB3 << std::endl;
            std::cout << "z_gp_MB3 " << my_track_.z_gp_MB3 << std::endl;
          }
        }
        else if (detId.station() == 4) {
          // my_track_.x_gp_MB4 = gp_seg.x(); 
          // my_track_.y_gp_MB4 = gp_seg.y(); 
          // my_track_.z_gp_MB4 = gp_seg.z(); 
          // my_track_.phi_gp_MB4 = gp_seg.phi(); 
          my_track_.phi_gv_MB4 = gv_seg.phi(); 

          if (verbose) {
            // std::cout << "phi_gv_MB4 " << my_track_.phi_gv_MB4 << std::endl;
            std::cout << "phi_gv_MB4 " << my_track_.phi_gv_MB4 << std::endl;
            // std::cout << "x_gv_MB4 " << my_track_.x_gv_MB4 << std::endl;
            // std::cout << "y_gv_MB4 " << my_track_.y_gv_MB4 << std::endl;
            // std::cout << "z_gv_MB4 " << my_track_.z_gv_MB4 << std::endl;
          }
        }

      }
      if ((DetId(id)).subdetId() == MuonSubdetId::CSC) {
        const CSCSegment *seg = dynamic_cast<const CSCSegment*>(rh->get());
        CSCDetId detId(id);
        if (verbose) {
          std::cout << "\t\tCSC :: id :: " << CSCDetId(id) << std::endl;
          std::cout << "\t\t    :: segment :: " << *seg << std::endl;
        }
        
	std::cout << "Getting global directions" << std::endl;

        const LocalPoint lp_seg(seg->localPosition());
        const GlobalPoint gp_seg(csc_geom->idToDet((**rh).rawId())->surface().toGlobal(lp_seg));
        
        const LocalVector lv_seg(seg->localDirection());
        const GlobalVector gv_seg(csc_geom->idToDet((**rh).rawId())->surface().toGlobal(lv_seg));
        
	std::cout << "Found global directions" << std::endl;

        if (detId.station() == 1) {
          my_track_.x_gp_ME1 = gp_seg.x(); 
          my_track_.y_gp_ME1 = gp_seg.y(); 
          my_track_.z_gp_ME1 = gp_seg.z(); 
          my_track_.phi_gp_ME1 = gp_seg.phi(); 
          my_track_.phi_gv_ME1 = gv_seg.phi(); 
          
          if (verbose) {
            std::cout << "phi_gp_ME1 " << my_track_.phi_gp_ME1 << std::endl;
            std::cout << "phi_gv_ME1 " << my_track_.phi_gv_ME1 << std::endl;
            std::cout << "x_gp_ME1 " << my_track_.x_gp_ME1 << std::endl;
            std::cout << "y_gp_ME1 " << my_track_.y_gp_ME1 << std::endl;
            std::cout << "z_gp_ME1 " << my_track_.z_gp_ME1 << std::endl;
          }
        }
        else if (detId.station() == 2) {
          my_track_.x_gp_ME2 = gp_seg.x(); 
          my_track_.y_gp_ME2 = gp_seg.y(); 
          my_track_.z_gp_ME2 = gp_seg.z(); 
          my_track_.phi_gp_ME2 = gp_seg.phi(); 
          my_track_.phi_gv_ME2 = gv_seg.phi(); 

          if (verbose) {
            std::cout << "phi_gp_ME2 " << my_track_.phi_gp_ME2 << std::endl;
            std::cout << "phi_gv_ME2 " << my_track_.phi_gv_ME2 << std::endl;
            std::cout << "x_gp_ME2 " << my_track_.x_gp_ME2 << std::endl;
            std::cout << "y_gp_ME2 " << my_track_.y_gp_ME2 << std::endl;
            std::cout << "z_gp_ME2 " << my_track_.z_gp_ME2 << std::endl;
          }
        }
        else if (detId.station() == 3) {
          my_track_.x_gp_ME3 = gp_seg.x(); 
          my_track_.y_gp_ME3 = gp_seg.y(); 
          my_track_.z_gp_ME3 = gp_seg.z(); 
          my_track_.phi_gp_ME3 = gp_seg.phi(); 
          my_track_.phi_gv_ME3 = gv_seg.phi(); 
          
          if (verbose) {
            std::cout << "phi_gp_ME3 " << my_track_.phi_gp_ME3 << std::endl;
            std::cout << "phi_gv_ME3 " << my_track_.phi_gv_ME3 << std::endl;
            std::cout << "x_gp_ME3 " << my_track_.x_gp_ME3 << std::endl;
            std::cout << "y_gp_ME3 " << my_track_.y_gp_ME3 << std::endl;
            std::cout << "z_gp_ME3 " << my_track_.z_gp_ME3 << std::endl;
          }
        }
      }
    }// end loop on segments

    my_track_.dx_gp_MB1_MB2 = my_track_.x_gp_MB2 - my_track_.x_gp_MB1;
    my_track_.dx_gp_MB2_MB3 = my_track_.x_gp_MB3 - my_track_.x_gp_MB2;
    
    my_track_.dy_gp_MB1_MB2 = my_track_.y_gp_MB2 - my_track_.y_gp_MB1;
    my_track_.dy_gp_MB2_MB3 = my_track_.y_gp_MB3 - my_track_.y_gp_MB2;
    
    my_track_.dz_gp_MB1_MB2 = my_track_.z_gp_MB2 - my_track_.z_gp_MB1;
    my_track_.dz_gp_MB2_MB3 = my_track_.z_gp_MB3 - my_track_.z_gp_MB2;


    my_track_.dx_gp_ME1_ME2 = my_track_.x_gp_ME2 - my_track_.x_gp_ME1;
    my_track_.dx_gp_ME2_ME3 = my_track_.x_gp_ME3 - my_track_.x_gp_ME2;
    
    my_track_.dy_gp_ME1_ME2 = my_track_.y_gp_ME2 - my_track_.y_gp_ME1;
    my_track_.dy_gp_ME2_ME3 = my_track_.y_gp_ME3 - my_track_.y_gp_ME2;
    
    my_track_.dz_gp_ME1_ME2 = my_track_.z_gp_ME2 - my_track_.z_gp_ME1;
    my_track_.dz_gp_ME2_ME3 = my_track_.z_gp_ME3 - my_track_.z_gp_ME2;
    
    my_track_.dphi_gv_MB1_MB4 = my_track_.phi_gv_MB1 - my_track_.phi_gv_MB4;
    // std::cout << "dphi_gv_MB1_MB4 " << my_track_.dphi_gv_MB1_MB4 << std::endl;

    // std::cout << "Calculate Pt" << std::endl;
    // std::cout << (1./my_track_.dphi_gv_MB1_MB4 + 1.769)/1.656 << std::endl;
    
    // barrel
    if (std::abs(recoTrackExtra.innerPosition().eta())<0.9){
      newPt = (1./my_track_.dphi_gv_MB1_MB4 + 1.769)/1.656;
    }
    // endcap
    if (std::abs(recoTrackExtra.innerPosition().eta())>1.1){
    }
    // overlap
    if (std::abs(recoTrackExtra.innerPosition().eta())>0.9 and std::abs(recoTrackExtra.innerPosition().eta())<1.1){
    }
    // rescale the values in the innermost station (using a muon trackloader)
    // we don't want to change the direction of the muon, only the pT

    // std::cout << "newPt " << newPt << std::endl;
    return newPt;
}

//define this as a plug-in
#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(L2TrackPtFromSegmentAlignmentProducer);
