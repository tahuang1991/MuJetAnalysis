// system include files
#include <memory>


// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

// user include files
#include "TTree.h"
#include "TRandom3.h"
#include "TMath.h"


#include "DataFormats/Common/interface/TriggerResults.h"
#include "FWCore/Common/interface/TriggerNames.h"
#include "DataFormats/Common/interface/HLTGlobalStatus.h"

#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/Utilities/interface/InputTag.h"

using namespace std;

class HLTAnalyzer : public edm::EDAnalyzer {
  public:
    explicit HLTAnalyzer(const edm::ParameterSet&);
    ~HLTAnalyzer();

    static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

  private:
    virtual void beginJob() ;
    virtual void analyze(const edm::Event&, const edm::EventSetup&);
    virtual void endJob() ;

    virtual void beginRun(edm::Run const&, edm::EventSetup const&);
    virtual void endRun(edm::Run const&, edm::EventSetup const&);
    virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
    virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
  
  //****************************************************************************
  //          EVENT LEVEL VARIABLES, COUNTERS, BRANCHES AND SELECTORS           
  //****************************************************************************
  
  Int_t   m_debug;  // Debug level
  TTree * m_ttree;  // Store variables in branches of this tree for later access
  Int_t   m_events; // Counter: number of analyzed events
  
  // Branches in ROOT tree (they all start with b_)
  Int_t b_run;   // run number   | these three numbers required to extract event
  Int_t b_lumi;  // lumi number  | from sample (data or MC) and examine it in   
  Int_t b_event; // event number | event display                                
  
  std::vector<std::string> hltPaths_;
  std::vector<std::string> b_hltPaths;
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
HLTAnalyzer::HLTAnalyzer(const edm::ParameterSet& iConfig)
{
}


HLTAnalyzer::~HLTAnalyzer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}

//
// member functions
//

// ------------ method called for each event  ------------
void
HLTAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  b_run   = iEvent.id().run();
  b_lumi  = iEvent.id().luminosityBlock();
  b_event = iEvent.id().event();
  
  edm::Handle<edm::TriggerResults> trigResults; //our trigger result object
  edm::InputTag trigResultsTag("TriggerResults","","TEST"); //make sure have correct process on MC
  //data process=HLT, MC depends, Spring11 is REDIGI311X
  iEvent.getByLabel(trigResultsTag,trigResults);

  const edm::TriggerNames& trigNames = iEvent.triggerNames(*trigResults);   
  auto names(trigNames.triggerNames());
  auto nTriggers = names.size();
  if (false) cout << "nTriggers " << nTriggers << endl;
  // for (auto t : names)
  //   cout << t << endl;
  
  bool failTrig = (*trigResults).accept(trigNames.triggerIndex("HLT_TrkMu15_DoubleTrkMu5NoVtx_v1"));
  if (failTrig) 
    cout << "Failed HLT_TrkMu15_DoubleTrkMu5NoVtx_v1" << endl;

  m_ttree->Fill();  
}


// ------------ method called once each job just before starting event loop  ------------
void 
HLTAnalyzer::beginJob() {
  std::cout << "BEGIN JOB" << std::endl;
  
  edm::Service<TFileService> tFileService;
  m_ttree = tFileService->make<TTree>("Events", "Events");

  //****************************************************************************
  //                          EVENT LEVEL BRANCHES                              
  //****************************************************************************

  // Event info
  m_ttree->Branch("event", &b_event, "event/I");
  m_ttree->Branch("run",   &b_run,   "run/I");
  m_ttree->Branch("lumi",  &b_lumi,  "lumi/I");

}

// ------------ method called once each job just after ending the event loop  ------------
void 
HLTAnalyzer::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
void 
HLTAnalyzer::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
HLTAnalyzer::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
HLTAnalyzer::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
HLTAnalyzer::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
HLTAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(HLTAnalyzer);
