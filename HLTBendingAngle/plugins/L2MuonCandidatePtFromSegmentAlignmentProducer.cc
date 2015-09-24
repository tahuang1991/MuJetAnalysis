// Framework
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/Common/interface/Handle.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "MuJetAnalysis/HLTBendingAngle/plugins/L2MuonCandidatePtFromSegmentAlignmentProducer.h"


#include "DataFormats/TrackReco/interface/TrackExtra.h"
#include "DataFormats/TrackReco/interface/TrackExtraFwd.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"

#include "DataFormats/DTRecHit/interface/DTRecSegment4DCollection.h"
#include "DataFormats/CSCRecHit/interface/CSCSegmentCollection.h"

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
L2MuonCandidatePtFromSegmentAlignmentProducer::L2MuonCandidatePtFromSegmentAlignmentProducer(const ParameterSet& parameterSet){
  LogTrace("Muon|RecoMuon|L2MuonCandidatePtFromSegmentAlignmentProducer")<<" constructor called";

  // StandAlone Collection Label
  theL2CollectionLabel_ = parameterSet.getParameter<InputTag>("InputObjects");
  trackToken_ = consumes<reco::RecoChargedCandidateCollection>(theL2CollectionLabel_);
  produces<RecoChargedCandidateCollection>("PtFromSegmentAlignment");
}
  
/// destructor
L2MuonCandidatePtFromSegmentAlignmentProducer::~L2MuonCandidatePtFromSegmentAlignmentProducer(){
  LogTrace("Muon|RecoMuon|L2MuonCandidatePtFromSegmentAlignmentProducer")<<" L2MuonCandidatePtFromSegmentAlignmentProducer destructor called";
}

/// reconstruct muons
void L2MuonCandidatePtFromSegmentAlignmentProducer::produce(Event& event, const EventSetup& eventSetup) const {
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
    // load the segments
    for(auto rh = recoTrackExtra.recHitsBegin(); rh != recoTrackExtra.recHitsEnd(); rh++) {
    
      auto id((**rh).rawId());
      if (is_dt(id)) {
        const DTRecSegment4D *seg = dynamic_cast<const DTRecSegment4D*>(rh->get());
        if (verbose) {
          std::cout << "\t\tDT  :: id :: " << DTChamberId(id) << std::endl;
          std::cout << "\t\t    :: segment :: " << *seg << std::endl;
        }
      }
      if (is_csc(id)) {
        const CSCSegment *seg = dynamic_cast<const CSCSegment*>(rh->get());
        if (verbose) {
          std::cout << "\t\tCSC :: id :: " << CSCDetId(id) << std::endl;
          std::cout << "\t\t    :: segment :: " << *seg << std::endl;
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

