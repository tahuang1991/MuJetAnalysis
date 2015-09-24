// Framework
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/Common/interface/Handle.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "MuJetAnalysis/HLTBendingAngle/plugins/L2MuonCandidatePtFromSegmentAlignmentProducer.h"

#include <string>

using namespace edm;
using namespace std;
using namespace reco;

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
void L2MuonCandidatePtFromSegmentAlignmentProducer::produce(edm::StreamID sid, Event& event, const EventSetup& eventSetup) const {
  const string metname = "Muon|RecoMuon|L2MuonCandidatePtFromSegmentAlignmentProducer";
  
  // Take the SA container
  LogTrace(metname)<<" Taking the StandAlone muons: "<<theL2CollectionLabel_;
  Handle<RecoChargedCandidateCollection> input_cands; 
  event.getByToken(trackToken_,input_cands);

  // Create an output RecoChargedCandidate collection
  LogTrace(metname)<<" Creating the RecoChargedCandidate::PtFromSegmentAlignment collection";
  auto_ptr<RecoChargedCandidateCollection> candidates( new RecoChargedCandidateCollection());

  // add here the pT assignment algorithm

  // for (unsigned int i=0; i<input_cands->size(); i++) {
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

