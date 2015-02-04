// system include files
#include <memory>


// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDFilter.h"

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

#include "FWCore/Framework/interface/EDFilter.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/Utilities/interface/InputTag.h"

using namespace std;

class HLT_TrkMu15_DoubleTrkMu5NoFiltersNoVtxFilter : public edm::EDFilter {
  public:
    explicit HLT_TrkMu15_DoubleTrkMu5NoFiltersNoVtxFilter(const edm::ParameterSet&);
    ~HLT_TrkMu15_DoubleTrkMu5NoFiltersNoVtxFilter();

    static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

  private:
    virtual void beginJob() ;
    virtual bool filter(edm::Event&, const edm::EventSetup&);
    virtual void endJob() ;

    virtual void beginRun(edm::Run const&, edm::EventSetup const&);
    virtual void endRun(edm::Run const&, edm::EventSetup const&);
    virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
    virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
  
  //****************************************************************************
  //          EVENT LEVEL VARIABLES, COUNTERS, BRANCHES AND SELECTORS           
  //****************************************************************************
  
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
HLT_TrkMu15_DoubleTrkMu5NoFiltersNoVtxFilter::HLT_TrkMu15_DoubleTrkMu5NoFiltersNoVtxFilter(const edm::ParameterSet& iConfig)
{
}


HLT_TrkMu15_DoubleTrkMu5NoFiltersNoVtxFilter::~HLT_TrkMu15_DoubleTrkMu5NoFiltersNoVtxFilter()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}

//
// member functions
//

// ------------ method called for each event  ------------
bool
HLT_TrkMu15_DoubleTrkMu5NoFiltersNoVtxFilter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  edm::Handle<edm::TriggerResults> trigResults; 
  edm::InputTag trigResultsTag("TriggerResults","","TEST"); //make sure have correct process on MC
  iEvent.getByLabel(trigResultsTag,trigResults);

  // check if this event was triggered by HLT_TrkMu15_DoubleTrkMu5NoVtx_v1
  const edm::TriggerNames& trigNames = iEvent.triggerNames(*trigResults);   
  auto names(trigNames.triggerNames());
  return (*trigResults).accept(trigNames.triggerIndex("HLT_TrkMu15_DoubleTrkMu5NoVtx_v1"));
}

  /*
  const edm::TriggerNames& trigNames = iEvent.triggerNames(*trigResults);   
  auto names(trigNames.triggerNames());
  auto nTriggers = names.size();
  if (false) cout << "nTriggers " << nTriggers << endl;

  bool wasTriggered=false;
  // check that at least one trigger accepted this event (exclude the protoype)
  for (auto name : names) {
    if (name=="HLT_TrkMu15_DoubleTrkMu5NoVtx_v1") continue;
    int index(trigNames.triggerIndex(name));
    if ((*trigResults).accept(index)) {
      wasTriggered = true;
      break;
    }
  }
  if (!wasTriggered) {
    int index(trigNames.triggerIndex("HLT_TrkMu15_DoubleTrkMu5NoVtx_v1"));
    if ((*trigResults).accept(index)) {
      cout << "Only accepted by HLT_TrkMu15_DoubleTrkMu5NoVtx_v1" << endl;
    }
  }

  */

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


// ------------ method called once each job just before starting event loop  ------------
void 
HLT_TrkMu15_DoubleTrkMu5NoFiltersNoVtxFilter::beginJob() {

  //****************************************************************************
  //                          EVENT LEVEL BRANCHES                              
  //****************************************************************************

  // Event info
}

// ------------ method called once each job just after ending the event loop  ------------
void 
HLT_TrkMu15_DoubleTrkMu5NoFiltersNoVtxFilter::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
void 
HLT_TrkMu15_DoubleTrkMu5NoFiltersNoVtxFilter::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
HLT_TrkMu15_DoubleTrkMu5NoFiltersNoVtxFilter::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
HLT_TrkMu15_DoubleTrkMu5NoFiltersNoVtxFilter::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
HLT_TrkMu15_DoubleTrkMu5NoFiltersNoVtxFilter::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
HLT_TrkMu15_DoubleTrkMu5NoFiltersNoVtxFilter::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(HLT_TrkMu15_DoubleTrkMu5NoFiltersNoVtxFilter);
