// -*- C++ -*-
//
// Package:    DisplacedL1MuFilter
// Class:      DisplacedL1MuFilter
// 
/**\class DisplacedL1MuFilter DisplacedL1MuFilter.cc MuJetAnalysis/DisplacedL1MuFilter/plugins/DisplacedL1MuFilter.cc

   We assume that the displacement is reasonable (What is reasonable here? $d_{xy} < 10$ cm) 
   We require the L1Mu to be of good quality (Q>=4). L1Tk matching to L1Mu within dR<0.12 
   are vetoed. Most muons in minbias events stem from kaon decay and b-quark decay and are 
   sufficiently prompt. The (eta,phi) coordinates of L1Mu used in the dR calculation are 
   those of the second station. In addition, we veto L1Tk with pT>4 GeV (somewhat ad-hoc 
   number) within dR<0.4. This cut is effectively an isolation cut. For studies with highly 
   parallel muons, coming from e.g. low mass dark photon decay, this may cut significantly 
   on the signal. To suppress the fake rate, one might set an upper cut, e.g. pT<10 GeV.

   To estimate the rate reduction Sven will take a MinBias sample from Slava and build a 
   filter. We reject all events that have at least one muon that pass the requirements 
   for a prompt muon: (1) Q>=4 and matched to L1Tk within dR<0.12 or (2) unmatched to 
   L1Tk but with at least one L1Tk within  dR<0.4. 

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  sven dildick
//         Created:  Fri, 20 Nov 2015 12:22:11 GMT
// $Id$
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDFilter.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "L1Trigger/CSCTrackFinder/test/src/TFTrack.h"
#include "DataFormats/L1Trigger/interface/L1MuonParticleFwd.h"
#include "DataFormats/L1Trigger/interface/L1MuonParticle.h"
#include "DataFormats/L1GlobalMuonTrigger/interface/L1MuGMTReadoutCollection.h"
#include "DataFormats/L1TrackTrigger/interface/L1TkMuonParticle.h"
#include "DataFormats/L1TrackTrigger/interface/L1TkMuonParticleFwd.h"


#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Utilities/interface/InputTag.h"

#include "CondFormats/L1TObjects/interface/L1MuTriggerScales.h"
#include "CondFormats/DataRecord/interface/L1MuTriggerScalesRcd.h"
#include "CondFormats/L1TObjects/interface/L1MuTriggerPtScale.h"
#include "CondFormats/DataRecord/interface/L1MuTriggerPtScaleRcd.h"

//
// class declaration
//

class DisplacedL1MuFilter : public edm::EDFilter {
   public:
      explicit DisplacedL1MuFilter(const edm::ParameterSet&);
      ~DisplacedL1MuFilter();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

   private:
      virtual void beginJob() override;
      virtual bool filter(edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;
      
      //virtual void beginRun(edm::Run const&, edm::EventSetup const&) override;
      //virtual void endRun(edm::Run const&, edm::EventSetup const&) override;
      //virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
      //virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;

  edm::InputTag L1Mu_input;
  edm::InputTag L1TkMu_input;
  
      // ----------member data ---------------------------
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
DisplacedL1MuFilter::DisplacedL1MuFilter(const edm::ParameterSet& iConfig)
{
   //now do what ever initialization is needed
  
  L1Mu_input = iConfig.getParameter<edm::InputTag>("L1Mu_input");
  L1TkMu_input = iConfig.getParameter<edm::InputTag>("L1TkMu_input");
}


DisplacedL1MuFilter::~DisplacedL1MuFilter()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called on each new Event  ------------
bool
DisplacedL1MuFilter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  edm::Handle<L1MuGMTReadoutCollection> hl1GmtCands;
  iEvent.getByLabel(L1Mu_input, hl1GmtCands );
  std::vector<L1MuGMTExtendedCand> l1GmtCands;

  // Get GMT candidates from all bunch crossings
  auto gmt_records = hl1GmtCands->getRecords();
  for (auto rItr = gmt_records.begin(); rItr!=gmt_records.end() ; ++rItr ){
    if (rItr->getBxInEvent() < -1 || rItr->getBxInEvent() > 1) continue;
    
    auto GMTCands = rItr->getGMTCands();
    for (auto cItr = GMTCands.begin() ; cItr != GMTCands.end() ; ++cItr )
      if (!cItr->empty()) l1GmtCands.push_back(*cItr);
  }

  // L1 TrackingTrigger Analysis
  edm::Handle<l1extra::L1TkMuonParticleCollection> tkMuonsHandle;
  // use both barrel+endcap muons
  iEvent.getByLabel(L1TkMu_input, tkMuonsHandle);
  const l1extra::L1TkMuonParticleCollection& tkMuons = *tkMuonsHandle.product();

  // 1) count the number of muons with 
  int nMuons = 0;
  for (auto& cand: l1GmtCands){
    
  }
}

// ------------ method called once each job just before starting event loop  ------------
void 
DisplacedL1MuFilter::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
DisplacedL1MuFilter::endJob() {
}

// ------------ method called when starting to processes a run  ------------
/*
void
DisplacedL1MuFilter::beginRun(edm::Run const&, edm::EventSetup const&)
{ 
}
*/
 
// ------------ method called when ending the processing of a run  ------------
/*
void
DisplacedL1MuFilter::endRun(edm::Run const&, edm::EventSetup const&)
{
}
*/
 
// ------------ method called when starting to processes a luminosity block  ------------
/*
void
DisplacedL1MuFilter::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/
 
// ------------ method called when ending the processing of a luminosity block  ------------
/*
void
DisplacedL1MuFilter::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/
 
// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
DisplacedL1MuFilter::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}
//define this as a plug-in
DEFINE_FWK_MODULE(DisplacedL1MuFilter);
