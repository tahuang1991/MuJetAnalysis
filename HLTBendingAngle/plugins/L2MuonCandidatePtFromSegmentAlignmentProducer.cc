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
#include "MuJetAnalysis/HLTBendingAngle/plugins/L2MuonCandidatePtFromSegmentAlignmentProducer.h"

#include <string>
#include <typeinfo>
using namespace edm;
using namespace std;
using namespace reco;

inline bool 
is_dt(unsigned int detId) 
{
  return (DetId(detId)).subdetId() == MuonSubdetId::DT;
}

inline bool 
is_csc(unsigned int detId) 
{
  return (DetId(detId)).subdetId() == MuonSubdetId::CSC;
}

/// constructor with config
L2MuonCandidatePtFromSegmentAlignmentProducer::L2MuonCandidatePtFromSegmentAlignmentProducer(const ParameterSet& iConfig)
{
  LogTrace("Muon|RecoMuon|L2MuonCandidatePtFromSegmentAlignmentProducer")<<" constructor called";

  // service parameters
  ParameterSet serviceParameters = iConfig.getParameter<ParameterSet>("ServiceParameters");
  
  // TrackLoader parameters
  ParameterSet trackLoaderParameters = iConfig.getParameter<ParameterSet>("TrackLoaderParameters");

  // the services
  service_ = new MuonServiceProxy(serviceParameters);

  muonTrackLoader_ = new MuonTrackLoader(trackLoaderParameters, service_);
  
  // StandAlone Collection Label
  theL2CollectionLabel_ = iConfig.getParameter<InputTag>("InputObjects");
  trackToken_ = consumes<reco::RecoChargedCandidateCollection>(theL2CollectionLabel_);
  produces<RecoChargedCandidateCollection>("PtFromSegmentAlignment");
}
  
/// destructor
L2MuonCandidatePtFromSegmentAlignmentProducer::~L2MuonCandidatePtFromSegmentAlignmentProducer()
{
  LogTrace("Muon|RecoMuon|L2MuonCandidatePtFromSegmentAlignmentProducer")<<" L2MuonCandidatePtFromSegmentAlignmentProducer destructor called";
}

void L2MuonCandidatePtFromSegmentAlignmentProducer::beginRun(edm::Run &run, const edm::EventSetup &eventSetup)
{
  // get the geometries
  try {
    eventSetup.get<MuonGeometryRecord>().get(csc_geom);
    csc_geometry_ = &*csc_geom;
  } catch (edm::eventsetup::NoProxyException<CSCGeometry>& e) {
    LogDebug("L2MuonCandidatePtFromSegmentAlignmentProducer") << "+++ Info: CSC geometry is unavailable. +++\n";
  }

  try {
    eventSetup.get<MuonGeometryRecord>().get(dt_geom);
    dt_geometry_ = &*dt_geom;
  } catch (edm::eventsetup::NoProxyException<DTGeometry>& e) {
    LogDebug("L2MuonCandidatePtFromSegmentAlignmentProducer") << "+++ Info: DT geometry is unavailable. +++\n";
  }
}  

/// reconstruct muons
void L2MuonCandidatePtFromSegmentAlignmentProducer::produce(edm::Event& event, const edm::EventSetup& eventSetup)
{
  const string metname = "Muon|RecoMuon|L2MuonCandidatePtFromSegmentAlignmentProducer";
  
  // Take the SA container
  LogTrace(metname)<<" Taking the StandAlone muons: "<<theL2CollectionLabel_;
  Handle<RecoChargedCandidateCollection> input_cands; 
  event.getByToken(trackToken_,input_cands);
  const reco::RecoChargedCandidateCollection& cands(*input_cands.product());

  // Create an output RecoChargedCandidate collection
  LogTrace(metname)<<" Creating the RecoChargedCandidate::PtFromSegmentAlignment collection";
  std::auto_ptr<RecoChargedCandidateCollection> candidates(new RecoChargedCandidateCollection());
  
  // load the trajectories
  edm::Handle<std::vector<Trajectory> > trajectoryCollection;
  event.getByLabel("hltL2Muons", trajectoryCollection);
  const std::vector<Trajectory>& trajectories(*trajectoryCollection.product());


  
  
  // Loop on all candidates
  bool verbose = true;
  for (unsigned int i=0; i<cands.size(); i++) {
    
    // get the associated recotrack
    auto recoTrack(*(cands[i].track()));
    
    // print some relevant information
    if (verbose) {
      std::cout << "RecoTrack p" << recoTrack.outerMomentum() << "\n" 
                << std::endl;
    }
    
    // get the associated recotrack extra object
    auto recoTrackExtra(*(recoTrack.extra()));
    std::cout << "type of recoTrackextra" << typeid(recoTrackExtra).name() << std::endl;
    
    // print some relevant information
    if (verbose) {
      std::cout << "RecoTrackExtra " << std::endl
                << "\tpT_inner: "<<recoTrackExtra.innerMomentum().Rho()
                << ", eta_inner: "<<recoTrackExtra.innerPosition().eta()
                << ", phi_inner: "<<recoTrackExtra.innerPosition().phi()
                << "\tpT_outer: "<<recoTrackExtra.outerMomentum().Rho()
                << ", eta_outer: "<<recoTrackExtra.outerPosition().eta()
                << ", phi_outer: "<<recoTrackExtra.outerPosition().phi()
                <<std::endl;  
    }

    // load the segments
    for(auto rh = recoTrackExtra.recHitsBegin(); rh != recoTrackExtra.recHitsEnd(); rh++) {
  
      auto id((**rh).rawId());
      if (is_dt(id)) {
        const DTRecSegment4D *seg = dynamic_cast<const DTRecSegment4D*>(rh->get());
        DTChamberId detId(id);
        
        if (verbose) {
          std::cout << "\t\tDT  :: id :: " << DTChamberId(id) << std::endl;
          std::cout << "\t\t    :: segment :: " << *seg << std::endl;
        }

        const LocalPoint lp_seg(seg->localPosition());
        const GlobalPoint gp_seg(dt_geom->idToDet((**rh).rawId())->surface().toGlobal(lp_seg));

        const LocalVector lv_seg(seg->localDirection());
        const GlobalVector gv_seg(dt_geom->idToDet((**rh).rawId())->surface().toGlobal(lv_seg));
        
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
          my_track_.phi_gp_MB4 = gp_seg.phi(); 

          if (verbose) {
            // std::cout << "phi_gp_MB4 " << my_track_.phi_gp_MB4 << std::endl;
            std::cout << "phi_gp_MB4 " << my_track_.phi_gp_MB4 << std::endl;
            // std::cout << "x_gp_MB4 " << my_track_.x_gp_MB4 << std::endl;
            // std::cout << "y_gp_MB4 " << my_track_.y_gp_MB4 << std::endl;
            // std::cout << "z_gp_MB4 " << my_track_.z_gp_MB4 << std::endl;
          }
        }

      }
      if (is_csc(id)) {
        const CSCSegment *seg = dynamic_cast<const CSCSegment*>(rh->get());
        CSCDetId detId(id);
        if (verbose) {
          std::cout << "\t\tCSC :: id :: " << CSCDetId(id) << std::endl;
          std::cout << "\t\t    :: segment :: " << *seg << std::endl;
        }
        
        const LocalPoint lp_seg(seg->localPosition());
        const GlobalPoint gp_seg(csc_geom->idToDet((**rh).rawId())->surface().toGlobal(lp_seg));
        
        const LocalVector lv_seg(seg->localDirection());
        const GlobalVector gv_seg(csc_geom->idToDet((**rh).rawId())->surface().toGlobal(lv_seg));
        
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

    my_track_.dphi_gp_MB1_MB4 = my_track_.phi_gp_MB1 - my_track_.phi_gp_MB4;

    // barrel
    if (std::abs(recoTrackExtra.innerPosition().eta())<0.9){
      float pt(PtFromSegmentBending(my_track_.phi_gv_MB1, my_track_.phi_gv_MB2, 
                                    my_track_.phi_gv_MB3, my_track_.phi_gv_MB4));
      std::cout << "pt" << pt << std::endl;      
      std::cout << "dphi(MB1,MB4) " << my_track_.dphi_gp_MB1_MB4 << std::endl;
      pt_from_segment_alignment_ = 1./my_track_.dphi_gp_MB1_MB4;
    }
    // endcap
    if (std::abs(recoTrackExtra.innerPosition().eta())>1.1){
    }
    // overlap
    if (std::abs(recoTrackExtra.innerPosition().eta())>0.9 and std::abs(recoTrackExtra.innerPosition().eta())<1.1){
    }
    // rescale the values in the innermost station (using a muon trackloader)
    // we don't want to change the direction of the muon, only the pT

    // get the reco::Track' PCA track    
    auto id(cands[i].track().key());
    //reco::Track pcaTrack(pcaTrackCollection[id]);
    //const reco::TrackCollection& (*orphanHandleTracks.product());
    Trajectory trajectory(trajectories[id]);
    
    // get the propagation direction
    PropagationDirection direc(trajectory.direction());
    if (direc==PropagationDirection::oppositeToMomentum){
      std::cout << "opposite" << std::endl;
      TrajectoryMeasurement oldMeas(trajectory.lastMeasurement());
      TrajectoryStateOnSurface tsos(oldMeas.updatedState());

      // get the local trajectory parameters
      LocalTrajectoryParameters oldParams(tsos.localParameters());


      // update the pT
      LocalVector oldMomentum(oldParams.momentum());
      float newPt = 5; //dummy value for now
      LocalVector newMomentum(oldMomentum.theta(), oldMomentum.phi(), newPt);

      LocalPoint oldPosition(oldParams.position());
      TrackCharge oldCharge(oldParams.charge());
      LocalTrajectoryParameters newParams(oldPosition, newMomentum, oldCharge);
      
      // update the TSOS with the new pT
      tsos.update(newParams, tsos.surface(), tsos.magneticField());

      // // make a new measurement
      TrajectoryMeasurement newMeas(oldMeas.forwardPredictedState(),
                                    oldMeas.backwardPredictedState(),
                                    tsos,
                                    oldMeas.recHit(),
                                    oldMeas.estimate());
      
      // replace the old measurment by the new measurement
      trajectory.pop();
      trajectory.push(newMeas);
    }
    else if (direc==PropagationDirection::alongMomentum){
      std::cout << "along" << std::endl;
      TrajectoryMeasurement oldMeas(trajectory.firstMeasurement());
      TrajectoryStateOnSurface tsos(oldMeas.updatedState());
      
      // get the local trajectory parameters
      LocalTrajectoryParameters oldParams(tsos.localParameters());


      // update the pT
      LocalVector oldMomentum(oldParams.momentum());
      float newPt = 5; //dummy value for now
      LocalVector newMomentum(oldMomentum.theta(), oldMomentum.phi(), newPt);

      LocalPoint oldPosition(oldParams.position());
      TrackCharge oldCharge(oldParams.charge());
      LocalTrajectoryParameters newParams(oldPosition, newMomentum, oldCharge);
      
      // update the TSOS with the new pT
      tsos.update(newParams, tsos.surface(), tsos.magneticField());

      // // make a new measurement
      TrajectoryMeasurement newMeas(oldMeas.forwardPredictedState(),
                                    oldMeas.backwardPredictedState(),
                                    tsos,
                                    oldMeas.recHit(),
                                    oldMeas.estimate());
      
      // replace the old measurment by the new measurement
      trajectory.reverse();
      trajectory.pop();
      trajectory.push(newMeas);
      trajectory.reverse();
    }
  } // end loop on muons
  
  // make a new vector
  TrajectoryContainer newTrajVector;
  for (auto t: trajectories) {       
    Trajectory* tt = new Trajectory(t);
    newTrajVector.push_back(tt);
  }

  // load the trajectories in the trackloader
  OrphanHandle<reco::TrackCollection>
    orphanHandleTracks(muonTrackLoader_->loadTracks(newTrajVector, event));
  
  // get the PCA track collection
  const reco::TrackCollection& pcaTrackCollection(*orphanHandleTracks.product());
  std::cout << "pcaTrackCollection" << pcaTrackCollection.size() << std::endl;

  // fill the output candidate collection
  for (auto track: pcaTrackCollection){
    //   TrackRef tkref(input_cands,i);
    //   Particle::Charge q = tkref->charge();
    //   Particle::LorentzVector p4(tkref->px(), tkref->py(), tkref->pz(), tkref->p());
    //   Particle::Point vtx(tkref->vx(),tkref->vy(), tkref->vz());
    //   int pid = 13;
    //   if(abs(q)==1) pid = q < 0 ? 13 : -13;
    //   else LogWarning(metname) << "L2MuonCandidate has charge = "<<q;
    // RecoChargedCandidate cand(q, p4, vtx, pid);
    // cand.setTrack(tkref);
    // candidates->push_back(cand);
  }

  event.put(candidates);
  
  LogTrace(metname)<<" Event loaded"
                   <<"================================";
}

float L2MuonCandidatePtFromSegmentAlignmentProducer::PtFromSegmentBending(float phi1, float phi2, float phi3, float phi4)
{
  return 0;
}

float L2MuonCandidatePtFromSegmentAlignmentProducer::PtFromSegmentPosition(float phi1, float phi2, float phi3, float phi4)
{  
  return 0;
}

void L2MuonCandidatePtFromSegmentAlignmentProducer::bookTree()
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
