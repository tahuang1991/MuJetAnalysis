// Framework
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/Common/interface/Handle.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "MuJetAnalysis/HLTBendingAngle/plugins/L2MuonCandidatePtFromSegmentAlignmentProducer.h"


#include "DataFormats/TrackReco/interface/TrackExtra.h"
#include "DataFormats/TrackReco/interface/TrackExtraFwd.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"

#include "DataFormats/DTRecHit/interface/DTRecSegment4DCollection.h"
#include "DataFormats/CSCRecHit/interface/CSCSegmentCollection.h"

#include "Geometry/Records/interface/MuonGeometryRecord.h"
#include "Geometry/CSCGeometry/interface/CSCGeometry.h"
#include "Geometry/DTGeometry/interface/DTGeometry.h"

#include <string>

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
L2MuonCandidatePtFromSegmentAlignmentProducer::L2MuonCandidatePtFromSegmentAlignmentProducer(const ParameterSet& parameterSet)
{
  LogTrace("Muon|RecoMuon|L2MuonCandidatePtFromSegmentAlignmentProducer")<<" constructor called";

  // StandAlone Collection Label
  theL2CollectionLabel_ = parameterSet.getParameter<InputTag>("InputObjects");
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
void L2MuonCandidatePtFromSegmentAlignmentProducer::produce(edm::Event& event, const edm::EventSetup& eventSetup) const 
{
  const string metname = "Muon|RecoMuon|L2MuonCandidatePtFromSegmentAlignmentProducer";
  
  // Take the SA container
  LogTrace(metname)<<" Taking the StandAlone muons: "<<theL2CollectionLabel_;
  Handle<RecoChargedCandidateCollection> input_cands; 
  event.getByToken(trackToken_,input_cands);
  const reco::RecoChargedCandidateCollection& cands(*input_cands.product());

  // Create an output RecoChargedCandidate collection
  LogTrace(metname)<<" Creating the RecoChargedCandidate::PtFromSegmentAlignment collection";
  auto_ptr<RecoChargedCandidateCollection> candidates( new RecoChargedCandidateCollection());

  // add here the pT assignment algorithm
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


    // double deltaPhi_gp_ME1_ME2; 
    // double deltaPhi_gp_ME2_ME3;

    // double deltaPhi_gp_ME1_ME2_oo; 
    // double deltaPhi_gp_ME2_ME3_oo;


    // load the segments
    for(auto rh = recoTrackExtra.recHitsBegin(); rh != recoTrackExtra.recHitsEnd(); rh++) {
  
      double phi_gp_MB1; 
      double phi_gp_MB2;
      double phi_gp_MB3;
      
      double x_gp_MB1; 
      double x_gp_MB2;
      double x_gp_MB3;
      
      double y_gp_MB1; 
      double y_gp_MB2;
      double y_gp_MB3;

      double z_gp_MB1; 
      double z_gp_MB2;
      double z_gp_MB3;

      
      double phi_gp_ME1; 
      double phi_gp_ME2;
      double phi_gp_ME3;
      
      double x_gp_ME1; 
      double x_gp_ME2;
      double x_gp_ME3;
      
      double y_gp_ME1; 
      double y_gp_ME2;
      double y_gp_ME3;

      double z_gp_ME1; 
      double z_gp_ME2;
      double z_gp_ME3;

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
        
        if (detId.station() == 1) {
          x_gp_MB1 = gp_seg.x(); 
          y_gp_MB1 = gp_seg.y(); 
          z_gp_MB1 = gp_seg.z(); 
          phi_gp_MB1 = gp_seg.phi(); 

          if (verbose) {
            std::cout << "phi_gp_MB1 " << phi_gp_MB1 << std::endl;
            std::cout << "x_gp_MB1 " << x_gp_MB1 << std::endl;
            std::cout << "y_gp_MB1 " << y_gp_MB1 << std::endl;
            std::cout << "z_gp_MB1 " << z_gp_MB1 << std::endl;
          }
        }
        else if (detId.station() == 2) {
          x_gp_MB2 = gp_seg.x(); 
          y_gp_MB2 = gp_seg.y(); 
          z_gp_MB2 = gp_seg.z(); 
          phi_gp_MB2 = gp_seg.phi(); 

          if (verbose) {
            std::cout << "phi_gp_MB2 " << phi_gp_MB2 << std::endl;
            std::cout << "x_gp_MB2 " << x_gp_MB2 << std::endl;
            std::cout << "y_gp_MB2 " << y_gp_MB2 << std::endl;
            std::cout << "z_gp_MB2 " << z_gp_MB2 << std::endl;
          }
        }
        else if (detId.station() == 3) {
          x_gp_MB3 = gp_seg.x(); 
          y_gp_MB3 = gp_seg.y(); 
          z_gp_MB3 = gp_seg.z(); 
          phi_gp_MB3 = gp_seg.phi(); 
        }
        
        if (verbose) {
          std::cout << "phi_gp_MB3 " << phi_gp_MB3 << std::endl;
          std::cout << "x_gp_MB3 " << x_gp_MB3 << std::endl;
          std::cout << "y_gp_MB3 " << y_gp_MB3 << std::endl;
          std::cout << "z_gp_MB3 " << z_gp_MB3 << std::endl;
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

        if (detId.station() == 1) {
          x_gp_ME1 = gp_seg.x(); 
          y_gp_ME1 = gp_seg.y(); 
          z_gp_ME1 = gp_seg.z(); 
          phi_gp_ME1 = gp_seg.phi(); 

          if (verbose) {
            std::cout << "phi_gp_ME1 " << phi_gp_ME1 << std::endl;
            std::cout << "x_gp_ME1 " << x_gp_ME1 << std::endl;
            std::cout << "y_gp_ME1 " << y_gp_ME1 << std::endl;
            std::cout << "z_gp_ME1 " << z_gp_ME1 << std::endl;
          }
        }
        else if (detId.station() == 2) {
          x_gp_ME2 = gp_seg.x(); 
          y_gp_ME2 = gp_seg.y(); 
          z_gp_ME2 = gp_seg.z(); 
          phi_gp_ME2 = gp_seg.phi(); 

          if (verbose) {
            std::cout << "phi_gp_ME2 " << phi_gp_ME2 << std::endl;
            std::cout << "x_gp_ME2 " << x_gp_ME2 << std::endl;
            std::cout << "y_gp_ME2 " << y_gp_ME2 << std::endl;
            std::cout << "z_gp_ME2 " << z_gp_ME2 << std::endl;
          }
        }
        else if (detId.station() == 3) {
          x_gp_ME3 = gp_seg.x(); 
          y_gp_ME3 = gp_seg.y(); 
          z_gp_ME3 = gp_seg.z(); 
          phi_gp_ME3 = gp_seg.phi(); 

          if (verbose) {
            std::cout << "phi_gp_ME3 " << phi_gp_ME3 << std::endl;
            std::cout << "x_gp_ME3 " << x_gp_ME3 << std::endl;
            std::cout << "y_gp_ME3 " << y_gp_ME3 << std::endl;
            std::cout << "z_gp_ME3 " << z_gp_ME3 << std::endl;
          }
        }
      }
    }
  }
  
     //     some stuff from the original L2MuonCandidateProducer
    //   TrackRef tkref(input_cands,i);
    //   Particle::Charge q = tkref->charge();
    //   Particle::LorentzVector p4(tkref->px(), tkref->py(), tkref->pz(), tkref->p());
    //   Particle::Point vtx(tkref->vx(),tkref->vy(), tkref->vz());
    //   int pid = 13;
    //   if(abs(q)==1) pid = q < 0 ? 13 : -13;
    //   else LogWarning(metname) << "L2MuonCandidate has charge = "<<q;
    //   RecoChargedCandidate cand(q, p4, vtx, pid);
    //   cand.setTrack(tkref);
    //   candidates->push_back(cand);
    // }

  event.put(candidates);
  
  LogTrace(metname)<<" Event loaded"
                   <<"================================";
}

