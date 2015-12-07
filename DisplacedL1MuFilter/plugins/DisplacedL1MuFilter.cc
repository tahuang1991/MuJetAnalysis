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
   L1Tk but with at least one L1Tk within  dR<0.4 with pt>4

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

#include "TTree.h"
#include "TFile.h"

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDFilter.h"
#include "FWCore/Framework/interface/ESHandle.h"
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
#include "DataFormats/L1TrackTrigger/interface/TTTrack.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "MagneticField/Engine/interface/MagneticField.h"
#include "TrackingTools/GeomPropagators/interface/Propagator.h"
#include "TrackingTools/TrajectoryState/interface/TrajectoryStateOnSurface.h"
#include "TrackingTools/Records/interface/TrackingComponentsRecord.h"
#include "MagneticField/Records/interface/IdealMagneticFieldRecord.h"
#include "DataFormats/GeometrySurface/interface/Plane.h"
#include "DataFormats/GeometrySurface/interface/Cylinder.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "SimDataFormats/Track/interface/SimTrackContainer.h"
#include "SimDataFormats/Vertex/interface/SimVertex.h"
#include "DataFormats/Math/interface/normalizedPhi.h"

//
// class declaration
//

struct MyL1Mu
{
  Float_t pt, eta, phi;
  Int_t charge;
  Int_t endcap;
  Int_t has_sim;
  Int_t quality;
  Float_t dEta_sim_corr, dPhi_sim_corr, dR_sim_corr;
  Float_t dEta_sim_prop, dPhi_sim_prop, dR_sim_prop;
  Int_t isMatched;
  Int_t isUnMatched;
  Float_t pt_L1Tk, eta_L1Tk, phi_L1Tk;
  Float_t dEta_L1Tk, dPhi_L1Tk, dR_L1Tk;
  Float_t dPhi_L1Tk_corr, dR_L1Tk_corr;
};

double 
phiHeavyCorr(double pt, double eta, double phi, double q)
{
  //  float resEta = eta;
  float etaProp = std::abs(eta);
  if (etaProp< 1.1) etaProp = 1.1;
  float resPhi = phi - 1.464*q*cosh(1.7)/cosh(etaProp)/pt - M_PI/144.;
  if (resPhi > M_PI) resPhi -= 2.*M_PI;
  if (resPhi < -M_PI) resPhi += 2.*M_PI;
  return resPhi;
}


bool 
isSimTrackGood(const SimTrack &t)
{
  // SimTrack selection
  if (t.noVertex()) return false;
  if (t.noGenpart()) return false;
  // only muons 
  if (std::abs(t.type()) != 13) return false;
  // pt selection
  //if (t.momentum().pt() < simTrackMinPt_) return false;
  // eta selection
  const float eta(std::abs(t.momentum().eta()));
  if (eta > 2.5) return false; 
  return true;
}

using namespace std;

class DisplacedL1MuFilter : public edm::EDFilter 
{
public:
  explicit DisplacedL1MuFilter(const edm::ParameterSet&);
  ~DisplacedL1MuFilter();
  
  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
  
private:
  void bookL1MuTree();
  virtual void beginJob() override;
  virtual bool filter(edm::Event&, const edm::EventSetup&) override;
  virtual void endJob() override;
  GlobalPoint propagateToZ(const GlobalPoint &inner_point, const GlobalVector &inner_vec, double, double) const;
  GlobalPoint propagateToR(const GlobalPoint &inner_point, const GlobalVector &inner_vec, double, double) const;
  void clearBranches();
  //virtual void beginRun(edm::Run const&, edm::EventSetup const&) override;
  //virtual void endRun(edm::Run const&, edm::EventSetup const&) override;
  //virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
  //virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
  
  int min_L1Mu_Quality;
  double dR_L1Mu_L1Tk;
  double dR_L1Mu_noL1Tk;
  double min_pT_L1Tk;
  double max_pT_L1Tk;
  int nTotalMuons = 0;
  int nPromptMuons = 0;
  int verbose;

  edm::InputTag L1Mu_input;
  edm::InputTag L1TkMu_input;
  
  edm::ESHandle<MagneticField> magfield_;
  edm::ESHandle<Propagator> propagator_;
  edm::ESHandle<Propagator> propagatorOpposite_;
  MyL1Mu track_;
  TTree* track_tree_;
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
  min_L1Mu_Quality = iConfig.getParameter<int>("L1MuQuality");
  dR_L1Mu_L1Tk = iConfig.getParameter<double>("dR_L1Mu_L1Tk");
  dR_L1Mu_noL1Tk = iConfig.getParameter<double>("dR_L1Mu_noL1Tk");
  min_pT_L1Tk = iConfig.getParameter<double>("min_pT_L1Tk");
  max_pT_L1Tk = iConfig.getParameter<double>("max_pT_L1Tk");
  verbose = iConfig.getParameter<int>("verbose");
  
  L1Mu_input = iConfig.getParameter<edm::InputTag>("L1Mu_input");
  L1TkMu_input = iConfig.getParameter<edm::InputTag>("L1TkMu_input");
  
  bookL1MuTree();
}

void DisplacedL1MuFilter::bookL1MuTree()
{
  edm::Service< TFileService > fs;
  track_tree_ = fs->make<TTree>("L1MuTree", "L1MuTree");
  track_tree_->Branch("pt", &track_.pt);
  track_tree_->Branch("eta", &track_.eta);
  track_tree_->Branch("phi", &track_.phi);
  track_tree_->Branch("charge", &track_.charge);
  track_tree_->Branch("has_sim", &track_.has_sim);
  track_tree_->Branch("quality", &track_.quality);
  track_tree_->Branch("dEta_sim_corr", &track_.dEta_sim_corr);
  track_tree_->Branch("dPhi_sim_corr", &track_.dPhi_sim_corr);
  track_tree_->Branch("dR_sim_corr", &track_.dR_sim_corr);
  track_tree_->Branch("dEta_sim_prop", &track_.dEta_sim_prop);
  track_tree_->Branch("dPhi_sim_prop", &track_.dPhi_sim_prop);
  track_tree_->Branch("dR_sim_prop", &track_.dR_sim_prop);
  track_tree_->Branch("isMatched", &track_.isMatched);
  track_tree_->Branch("isUnMatched", &track_.isUnMatched);
  track_tree_->Branch("pt_L1Tk", &track_.pt_L1Tk);
  track_tree_->Branch("eta_L1Tk", &track_.eta_L1Tk);
  track_tree_->Branch("phi_L1Tk", &track_.phi_L1Tk);
  track_tree_->Branch("dEta_L1Tk", &track_.dEta_L1Tk);
  track_tree_->Branch("dPhi_L1Tk", &track_.dPhi_L1Tk);
  track_tree_->Branch("dR_L1Tk", &track_.dR_L1Tk);
  track_tree_->Branch("dPhi_L1Tk_corr", &track_.dPhi_L1Tk_corr);
  track_tree_->Branch("dR_L1Tk_corr", &track_.dR_L1Tk_corr);
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
  clearBranches();
  
  // propagator
  iSetup.get<IdealMagneticFieldRecord>().get(magfield_);
  iSetup.get<TrackingComponentsRecord>().get("SteppingHelixPropagatorAlong", propagator_);
  iSetup.get<TrackingComponentsRecord>().get("SteppingHelixPropagatorOpposite", propagatorOpposite_);

  edm::Handle<L1MuGMTReadoutCollection> hl1GmtCands;
  iEvent.getByLabel(L1Mu_input, hl1GmtCands );
  std::vector<L1MuGMTExtendedCand> l1GmtCands;

  // Get GMT candidates from all bunch crossings
  auto gmt_records = hl1GmtCands->getRecords();
  for (auto rItr = gmt_records.begin(); rItr!=gmt_records.end() ; ++rItr ){
    if (rItr->getBxInEvent() < 0 || rItr->getBxInEvent() > 0) continue;
    
    auto GMTCands = rItr->getGMTCands();
    for (auto cItr = GMTCands.begin() ; cItr != GMTCands.end() ; ++cItr )
      if (!cItr->empty()) l1GmtCands.push_back(*cItr);
  }

  // // L1 Trigger Analysis
  // edm::Handle<l1extra::L1MuonParticleCollection> muonsHandle;
  // iEvent.getByLabel("l1extraParticles", muonsHandle);
  // //const l1extra::L1MuonParticleCollection& muons = *muonsHandle.product();

  // L1 TrackingTrigger Analysis
  edm::Handle< std::vector< TTTrack< Ref_PixelDigi_ > > > TTTrackHandle;
  iEvent.getByLabel("TTTracksFromPixelDigis", "Level1TTTracks", TTTrackHandle);
  const std::vector< TTTrack< Ref_PixelDigi_ > >& TTTracks = *TTTrackHandle.product();

  edm::Handle<l1extra::L1TkMuonParticleCollection> tkMuonsHandle;
  // use both barrel+endcap muons
  iEvent.getByLabel(L1TkMu_input, tkMuonsHandle);
  //const l1extra::L1TkMuonParticleCollection& tkMuons = *tkMuonsHandle.product();

  edm::Handle<edm::SimTrackContainer> sim_tracks;
  iEvent.getByLabel("g4SimHits", sim_tracks);
  const edm::SimTrackContainer & sim_trks = *sim_tracks.product();

  edm::Handle<edm::SimVertexContainer> sim_vertices;
  iEvent.getByLabel("g4SimHits", sim_vertices);
  const edm::SimVertexContainer & sim_vtxs = *sim_vertices.product();
  
  // 1) count the number of muons with 
  int nL1MuL1TkdR012 = 0;
  int nL1MuQuality4 = 0;
  int nL1MuMatched = 0;
  int nL1MuUnMatched = 0;
  int nL1Mu = l1GmtCands.size();
  int nL1Tk = TTTracks.size();
  
  bool verbose = true;
  if(verbose) std::cout << "Number of L1Mu candidates before selections " << nL1Mu << std::endl; 

  nTotalMuons= nTotalMuons + nL1Mu;
  
  for (unsigned int i=0; i<l1GmtCands.size(); ++i){
    auto l1Mu = l1GmtCands[i];
    const double l1Mu_pt = l1Mu.ptValue();
    const double l1Mu_eta = l1Mu.etaValue();
    const double l1Mu_phi =  normalizedPhi(l1Mu.phiValue());
    const double l1Mu_quality = l1Mu.quality();

    // pt cut
    //    if (l1Mu_pt<15) continue;

    // eta cut
    //    if (std::abs(l1Mu_eta) > 2.5) continue;

    if(verbose) std::cout << "l1Mu " << i << std::endl; 
    if(verbose) std::cout << "l1Mu_pt " << l1Mu_pt << std::endl;
    if(verbose) std::cout << "l1Mu_eta " << l1Mu_eta << std::endl;
    if(verbose) std::cout << "l1Mu_phi " << l1Mu_phi << std::endl;
    if(verbose) std::cout << "l1Mu_quality " << l1Mu_quality << std::endl;
    if(verbose) std::cout << "Number of L1Tk candidates " << nL1Tk << std::endl;


    track_.pt = l1Mu_pt;
    track_.eta = l1Mu_eta;
    track_.phi = l1Mu_phi;
    track_.charge = l1Mu.charge();
    track_.quality = l1Mu_quality;


    // propagate the sim track using Slava's formula
    // calculate the deltaR
    std::cout << "Number of simtracks in this bx " << sim_trks.size() << std::endl;

    int nSimMu = 0;
    int index;
    int indexFound = 0;
    for (auto& t: sim_trks) {
      index++;
      if (!isSimTrackGood(t)) continue;
      nSimMu++;
      indexFound = index;
    }
    auto sim_muon = sim_trks[indexFound];
    auto sim_vertex = sim_vtxs[sim_muon.vertIndex()];
    std::cout << "Number of sim muons in this bx " << nSimMu << std::endl;

    double sim_muon_eta_prop;
    double sim_muon_phi_prop;

    // propagate the sim muon 
    if (std::abs(sim_muon.momentum().eta())<1.1){
      GlobalPoint loc_barrel(propagateToR(sim_vertex, sim_muon.momentum().pt(), sim_muon.charge(), 500.));
      sim_muon_eta_prop = loc_barrel.eta();
      sim_muon_phi_prop = loc_barrel.phi();
    } 
    else if (1.1 < sim_muon.momentum().eta() and sim_muon.momentum().eta() < 2.5) {
      GlobalPoint loc_endcap_pos(propagateToZ(sim_vertex, sim_muon.momentum().pt(), sim_muon.charge(), 850.));
      sim_muon_eta_prop = loc_endcap_pos.eta();
      sim_muon_phi_prop = loc_endcap_pos.phi();
    }
    else if (-1.1 > sim_muon.momentum().eta() and sim_muon.momentum().eta() > -2.5) {
      GlobalPoint loc_endcap_neg(propagateToZ(sim_vertex, sim_muon.momentum().pt(), sim_muon.charge(), -850.));
      sim_muon_eta_prop = loc_endcap_neg.eta();
      sim_muon_phi_prop = loc_endcap_neg.phi();
    }
    else{
      sim_muon_eta_prop = 99.;
      sim_muon_phi_prop = 99.;
    }
    
    
    double sim_phi_corrected = phiHeavyCorr(sim_muon.momentum().pt(), 
                                            sim_muon.momentum().eta(), 
                                            sim_muon.momentum().phi(), 
                                            sim_muon.charge() );
    
    track_.dEta_sim_corr = std::abs(sim_muon.momentum().eta() - l1Mu_eta);
    track_.dPhi_sim_corr = reco::deltaPhi(sim_phi_corrected, l1Mu_phi);
    track_.dR_sim_corr = reco::deltaR(sim_muon.momentum().eta(), sim_phi_corrected, l1Mu_eta, l1Mu_phi);
    std::cout << "track_.dEta_sim_corr " << track_.dEta_sim_corr << " track_.dPhi_sim_corr " << track_.dPhi_sim_corr << " track_.dR_sim_corr " << track_.dR_sim_corr << std::endl;
      
    track_.dEta_sim_prop = std::abs(sim_muon_eta_prop - l1Mu_eta);
    track_.dPhi_sim_prop = reco::deltaPhi(sim_muon_phi_prop, l1Mu_phi);
    track_.dR_sim_prop = reco::deltaR(sim_muon_eta_prop, sim_muon_phi_prop, l1Mu_eta, l1Mu_phi);
    std::cout << "track_.dEta_sim_prop " << track_.dEta_sim_prop << " track_.dPhi_sim_prop " << track_.dPhi_sim_prop << " track_.dR_sim_prop " << track_.dR_sim_prop << std::endl;


    bool isMatched = false;
    bool isUnMatched = false;

    for (unsigned int j=0; j<TTTracks.size(); ++j){
      auto l1Tk = TTTracks[j];
      const double l1Tk_pt = l1Tk.getMomentum().perp();
      const double l1Tk_eta = l1Tk.getMomentum().eta();
      const double l1Tk_phi = l1Tk.getMomentum().phi();
      double l1Tk_charge = l1Tk.getRInv()>0? 1: -1;
      const double l1Tk_phi_corr = phiHeavyCorr(l1Tk_pt, 
                                                l1Tk_eta, 
                                                l1Tk_phi, 
                                                l1Tk_charge);

      // propagate the L1Tk to the second station
      
      double l1Tk_eta_prop;
      double l1Tk_phi_prop;
      
      if (std::abs(l1Tk_eta)<1.1){
        GlobalPoint loc_barrel(propagateToR(l1Tk.getPOCA(), l1Tk.getMomentum(), l1Tk_charge, 500.));
        l1Tk_eta_prop = loc_barrel.eta();
        l1Tk_phi_prop = loc_barrel.phi();
      } 
      else if (1.1 < l1Tk_eta and l1Tk_eta < 2.5) {
        GlobalPoint loc_endcap_pos(propagateToZ(l1Tk.getPOCA(), l1Tk.getMomentum(), l1Tk_charge, 850.));
        l1Tk_eta_prop = loc_endcap_pos.eta();
        l1Tk_phi_prop = loc_endcap_pos.phi();
      }
      else if (-1.1 > l1Tk_eta and l1Tk_eta > -2.5) {
        GlobalPoint loc_endcap_neg(propagateToZ(l1Tk.getPOCA(), l1Tk.getMomentum(), l1Tk_charge, -850.));
        l1Tk_eta_prop = loc_endcap_neg.eta();
        l1Tk_phi_prop = loc_endcap_neg.phi();
      }
      else{
        l1Tk_eta_prop = 99.;
        l1Tk_phi_prop = 99.;
      }

      std::cout << "pt L1Tk " << l1Tk_pt << std::endl;
      std::cout << "eta L1Tk " << l1Tk_eta << " eta L1Tk prop " << l1Tk_eta_prop << std::endl;
      std::cout << "phi L1Tk " << l1Tk_phi << " phi L1Tk prop " << l1Tk_phi_prop << " phi L1Tk corr " << l1Tk_phi_corr << std::endl;
      std::cout << "dEta L1Tk prop " << std::abs(l1Tk_eta - l1Tk_eta_prop) << std::endl;
      std::cout << "dPhi L1Tk prop " << reco::deltaPhi(l1Tk_phi_prop, l1Tk_phi) << std::endl;
      std::cout << "dPhi L1Tk corr " << reco::deltaPhi(l1Tk_phi_corr, l1Tk_phi) << std::endl;
  
      // calculate the dR between the two L1Mus
      // const double dRL1Mu(reco::deltaR(l1Mu_eta, l1Mu_phi, L1Mu_of_L1TkMu.etaValue(), L1Mu_of_L1TkMu.phiValue()));

      // const double l1TkMu_phi_corr = phiHeavyCorr(l1TkMu_pt, l1TkMu_eta, l1TkMu_phi, l1TkMu_charge);
      
      //if(verbose) std::cout << "\tl1Tk_phi_corr " << l1Tk_phi_corr << std::endl;
      
      // calculate dR
      const double dR(reco::deltaR(l1Mu_eta, l1Mu_phi, l1Tk_eta_prop, l1Tk_phi_prop));
      const double dR_corr(reco::deltaR(l1Mu_eta, l1Mu_phi, l1Tk_eta, l1Tk_phi_corr));
      std::cout << "dR prop " << dR << " dR corr " << dR_corr << std::endl;

      track_.pt_L1Tk = l1Tk_pt;
      track_.eta_L1Tk = l1Tk_eta_prop;
      track_.phi_L1Tk = l1Tk_phi_prop;
      track_.dEta_L1Tk = std::abs(l1Tk_eta_prop - l1Mu_eta);
      track_.dPhi_L1Tk = reco::deltaPhi(l1Tk_phi_prop, l1Mu_phi);
      track_.dR_L1Tk = dR;
      track_.dPhi_L1Tk_corr = reco::deltaPhi(l1Tk_phi_corr, l1Tk_phi);
      track_.dR_L1Tk_corr = dR_corr;
      

      // if(verbose) std::cout << "\tdRL1Mu " << dRL1Mu << std::endl;
      
      // if (dR < dR_L1Mu_L1Tk){
      //   nL1MuL1TkdR012++;
      //   if(verbose) std::cout << "\t-- L1Mu matched to L1Tk" << std::endl;
      //   continue;
      // }
      // if (l1Mu_quality >= min_L1Mu_Quality){
      //   nL1MuQuality4++;
      //   std::cout << "\t-- L1Mu Q>=4" << std::endl;
      // }
      if (dR < dR_L1Mu_L1Tk and l1Mu_quality >= min_L1Mu_Quality) {
        track_.isMatched = 1;
        ++nL1MuMatched;
        std::cout << "\t-- L1Mu Q>=4 matched to L1Tk" << std::endl;
        if(verbose) std::cout << "\tl1Tk " << i << std::endl;
        if(verbose) std::cout << "\tl1Tk_pt " << l1Tk_pt << std::endl;
        if(verbose) std::cout << "\tl1Tk_eta " << l1Tk_eta << std::endl;
        if(verbose) std::cout << "\tl1Tk_phi " << l1Tk_phi << std::endl;
        if(verbose) std::cout << "\tl1Tk_charge " << l1Tk_charge << std::endl;
        
        if(verbose) std::cout << "\tl1Tk_eta_prop " << l1Tk_eta_prop << std::endl;
        if(verbose) std::cout << "\tl1Tk_phi_prop " << l1Tk_phi_prop << std::endl;
        if(verbose) std::cout << "\tdR " << dR << std::endl;
        isMatched = true;
        break;
      } 
      if (dR < dR_L1Mu_noL1Tk and l1Tk_pt>4) {        
        track_.isUnMatched = 1;
        ++nL1MuUnMatched;
        std::cout << "\t-- L1Mu not matched to L1Tk" << std::endl;
        if(verbose) std::cout << "\tl1Tk " << i << std::endl;
        if(verbose) std::cout << "\tl1Tk_pt " << l1Tk_pt << std::endl;
        if(verbose) std::cout << "\tl1Tk_eta " << l1Tk_eta << std::endl;
        if(verbose) std::cout << "\tl1Tk_phi " << l1Tk_phi << std::endl;
        if(verbose) std::cout << "\tl1Tk_charge " << l1Tk_charge << std::endl;
        
        if(verbose) std::cout << "\tl1Tk_eta_prop " << l1Tk_eta_prop << std::endl;
        if(verbose) std::cout << "\tl1Tk_phi_prop " << l1Tk_phi_prop << std::endl;
        if(verbose) std::cout << "\tdR " << dR << std::endl;
        isUnMatched = true;
        break;
      }
      std::cout << std::endl;
    }
    if (isUnMatched or isMatched) {
      nPromptMuons++;
    }

    track_tree_->Fill();  
  }
  std::cout << endl << "--------------------------------" << endl;
  std::cout << "event report" << endl;
  std::cout << "nL1MuL1TkdR012 " << nL1MuL1TkdR012 << endl;
  std::cout << "nL1MuQuality4 " << nL1MuQuality4 << endl;
  std::cout << "nL1MuMatched " << nL1MuMatched << endl;
  std::cout << "nL1MuUnMatched " << nL1MuUnMatched << endl;
  std::cout << "nL1Mu " << nL1Mu << endl;
  std::cout << "nL1Tk " << nL1Tk << endl;
  std::cout << "Filter " << nL1MuMatched + nL1MuUnMatched << endl;
  
  return(nL1MuMatched + nL1MuUnMatched)==0;

  // match l1 mu to simulated mu check that the delta R is less than 0.2 after propagation
  // impose selection on the L1Mu 
  // use the central bunch crossing instead of +- 1
  
  // use pt>20, plot the dEta, dPhi for the (SIM,L1) mapping
  
}

// ------------ method called once each job just before starting event loop  ------------
void 
DisplacedL1MuFilter::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
DisplacedL1MuFilter::endJob()
 {
   cout << "Total number of total muons " << nTotalMuons << endl;
   cout << "Total number of prompt muons " << nPromptMuons << endl;
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


GlobalPoint
DisplacedL1MuFilter::propagateToZ(const GlobalPoint &inner_point, const GlobalVector &inner_vec, double charge, double z) const
{
  Plane::PositionType pos(0.f, 0.f, z);
  Plane::RotationType rot;
  Plane::PlanePointer my_plane(Plane::build(pos, rot));

  FreeTrajectoryState state_start(inner_point, inner_vec, charge, &*magfield_);

  TrajectoryStateOnSurface tsos(propagator_->propagate(state_start, *my_plane));
  if (!tsos.isValid()) tsos = propagatorOpposite_->propagate(state_start, *my_plane);
  if (tsos.isValid()) return tsos.globalPosition();

  return GlobalPoint();
}

GlobalPoint
DisplacedL1MuFilter::propagateToR(const GlobalPoint &inner_point, const GlobalVector &inner_vec, double charge, double R) const
{
  Cylinder::CylinderPointer my_cyl(Cylinder::build(Surface::PositionType(0,0,0), Surface::RotationType(), R));

  FreeTrajectoryState state_start(inner_point, inner_vec, charge, &*magfield_);

  TrajectoryStateOnSurface tsos(propagator_->propagate(state_start, *my_cyl));
  if (!tsos.isValid()) tsos = propagatorOpposite_->propagate(state_start, *my_cyl);
  if (tsos.isValid()) return tsos.globalPosition();

  return GlobalPoint();
}

void 
DisplacedL1MuFilter::clearBranches()
{
  track_.pt = -10;
  track_.eta = -10;
  track_.phi = -10;
  track_.charge = -10;
  track_.has_sim = -10;
  track_.quality = -10;
  track_.dEta_sim_corr = -10;
  track_.dPhi_sim_corr = -10;
  track_.dR_sim_corr = -10;
  track_.dEta_sim_prop = -10;
  track_.dPhi_sim_prop = -10;
  track_.dR_sim_prop = -10;
  track_.isMatched = -10;
  track_.isUnMatched = -10;
  track_.pt_L1Tk = -10;
  track_.eta_L1Tk = -10;
  track_.phi_L1Tk = -10;
  track_.dEta_L1Tk = -10;
  track_.dPhi_L1Tk = -10;
  track_.dR_L1Tk = -10;
  track_.dPhi_L1Tk_corr = -10;
  track_.dR_L1Tk_corr = -10;

}

//define this as a plug-in
DEFINE_FWK_MODULE(DisplacedL1MuFilter);
