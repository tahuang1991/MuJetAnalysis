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
  std::map<std::string,int> pathCounter_;

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
HLTAnalyzer::HLTAnalyzer(const edm::ParameterSet& iConfig) : 
  hltPaths_(iConfig.getParameter<std::vector<std::string> >("hltPaths"))
{
  // initialize
  for (auto p: hltPaths_){
    pathCounter_[p] = 0;
  }
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
  if (true) cout << "nTriggers " << nTriggers << endl;

  bool triggeredByMany=false;
  // check that at least one trigger accepted this event (exclude the protoype)
  for (auto name : names) {    
    if (name=="HLT_TrkMu15_DoubleTrkMu5NoFiltersNoVtx_v1") continue;
    if (name=="HLT_Physics_v1") continue;
    if (name=="HLTriggerFinalPath") continue;
    if (name=="HLT_Random_v1") continue;
    if (name=="HLT_TrkMu15_DoubleTrkMu5_v1") continue;
    if (name=="HLT_Mu15_DoubleMu5NoVtx_v1") continue;

    int index(trigNames.triggerIndex(name));
    if ((*trigResults).accept(index)) {
      pathCounter_[name] += 1;
      //      cout << "Triggered by " << name << endl;      
      triggeredByMany=true;
    }
  }
  if (!triggeredByMany)
    //Only triggered by HLT_TrkMu15_DoubleTrkMu5NoFiltersNoVtx_v1 
    cout << "Only triggered by HLT_TrkMu15_DoubleTrkMu5NoFiltersNoVtx_v1'" << b_run << ":" << b_lumi << ":" << b_event << "',";
  cout << endl;

  // // check if this event was triggered only by HLT_TrkMu15_DoubleTrkMu5NoVtx_v1
  // if (wasTriggered) {
  //   int index(trigNames.triggerIndex("HLT_TrkMu15_DoubleTrkMu5NoVtx_v1"));
  //   if ((*trigResults).accept(index)) {
  //     cout << "Only accepted by HLT_TrkMu15_DoubleTrkMu5NoVtx_v1" << endl;
  //   }
  // }


  /*
 /// Was at least one path run?
  bool wasrun() const {return State(0);}
  /// Has at least one path accepted the event?
  bool accept() const {return State(1);}
  /// Has any path encountered an error (exception)
  bool  error() const {return State(2);}

  // get hold of individual elements, using safe indexing with "at" which throws!

  const HLTPathStatus& at (const unsigned int i)   const { return paths_.at(i); }
  HLTPathStatus& at (const unsigned int i)         { return paths_.at(i); }
  const HLTPathStatus& operator[](const unsigned int i) const { return paths_.at(i); }
  HLTPathStatus& operator[](const unsigned int i)       { return paths_.at(i); }

  /// Was ith path run?
  bool wasrun(const unsigned int i) const { return at(i).wasrun(); }
  /// Has ith path accepted the event?
  bool accept(const unsigned int i) const { return at(i).accept(); }
  /// Has ith path encountered an error (exception)?
  bool  error(const unsigned int i) const { return at(i).error() ; }
  */
  // cout << "HLT menu information " << endl;
  // cout << (*trigResults).wasrun() <<  " " << (*trigResults).accept() << " " << (*trigResults).error() << endl;

  // int index(trigNames.triggerIndex("HLT_TrkMu15_DoubleTrkMu5NoVtx_v1"));
  // cout << "HLT_TrkMu15_DoubleTrkMu5NoVtx_v1 information " << endl;
  // cout << (*trigResults).wasrun(index) <<  " " << (*trigResults).accept(index) << " " << (*trigResults).error(index) << endl;

    
  
  // if ((*trigResults).accept())
  //   cout << "passed HLT menu" << endl;    
  // bool passCustomPath = (*trigResults).accept(trigNames.triggerIndex("HLT_TrkMu15_DoubleTrkMu5NoVtx_v1")) or 
  //   (*trigResults).accept(trigNames.triggerIndex("HLT_TrkMu15_DoubleTrkMu5NoFiltersNoVtx_v1"));
  // if (passCustomPath)
  //   cout << "\tpassed HLT_TrkMu15_DoubleTrkMu5NoVtx_v1" << endl;    
  
  // for (auto p : hltPaths_){
  //   if (triggerEvent->path(p) )
  //     std::cout << p << " does not occur in pat::TriggerEvent" << std::endl;
  //   if ( triggerEvent->path(p) && triggerEvent->path(p)->wasAccept() ){
  //     b_hltPaths.push_back(p);
  //   } 
  // } 


  /*
  // was the event trigger by at least one path?
  bool passAtLeastOnePath((*trigResults).accept());
  if (passAtLeastOnePath){
    // did it fail our path?
    bool passCustomPath = (*trigResults).accept(trigNames.triggerIndex("HLT_TrkMu15_DoubleTrkMu5NoVtx_v1"));
    if (!passCustomPath) 
      cout << "Passed HLT menu, failed HLT_TrkMu15_DoubleTrkMu5NoVtx_v1" << endl;    
  }
  */
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
  std::cout << "Trigger Counts" << std::endl;
  for (auto name: hltPaths_){
    if (pathCounter_[name] != 0) std::cout << name << " " << pathCounter_[name] << std::endl;
  }
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
