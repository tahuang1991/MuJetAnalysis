#ifndef L2MuonCandidatePtFromSegmentAlignmentProducer_H
#define L2MuonCandidatePtFromSegmentAlignmentProducer_H

/**
   \class L2MuPtFromStubAlignment

   Description: calculation of the L2Mu pt from stub alignment
   
   Original Author:  "Sven Dildick", "Jose Dimas Valle"
*/

#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/RecoCandidate/interface/RecoChargedCandidate.h"
#include "DataFormats/RecoCandidate/interface/RecoChargedCandidateFwd.h"

namespace edm {class ParameterSet; class Event; class EventSetup;}

class L2MuonCandidatePtFromSegmentAlignmentProducer : public edm::EDProducer 
{
 public:
  /// constructor with config
  L2MuonCandidatePtFromSegmentAlignmentProducer(const edm::ParameterSet&);
  
  /// destructor
  virtual ~L2MuonCandidatePtFromSegmentAlignmentProducer(); 
  
  /// produce candidates
  virtual void produce(edm::Event&, const edm::EventSetup&) const;
  
 private:
  // L2 Collection Label
  edm::InputTag theL2CollectionLabel_; 
  edm::EDGetTokenT<reco::RecoChargedCandidateCollection> trackToken_;
};

#endif
