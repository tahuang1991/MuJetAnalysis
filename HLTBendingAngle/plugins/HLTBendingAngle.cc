#include <memory>
#include "TTree.h"
#include <iomanip>
#include <sstream>
#include <vector>

#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "DataFormats/GeometryVector/interface/GlobalPoint.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "DataFormats/Math/interface/normalizedPhi.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "DataFormats/HepMCCandidate/interface/GenParticleFwd.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "GEMCode/GEMValidation/interface/SimTrackMatchManager.h"

using namespace std;

double dxy(double px, double py, double vx, double vy, double pt)
{
  //Source: https://cmssdt.cern.ch/SDT/lxr/source/DataFormats/TrackReco/interface/TrackBase.h#119
  return (- vx * py + vy * px ) / pt;
}

double phiHeavyCorr(double pt, double eta, double phi, double q)
{
  //  float resEta = eta;
  float etaProp = std::abs(eta);
  if (etaProp< 1.1) etaProp = 1.1;
  float resPhi = phi - 1.464*q*cosh(1.7)/cosh(etaProp)/pt - M_PI/144.;
  if (resPhi > M_PI) resPhi -= 2.*M_PI;
  if (resPhi < -M_PI) resPhi += 2.*M_PI;
  return resPhi;
}

double
invariantMass(const reco::Candidate* p1, const reco::Candidate* p2) 
{
  return  sqrt((p1->energy() + p2->energy())*(p1->energy() + p2->energy()) -
               (p1->px() + p2->px())*(p1->px() + p2->px()) -
               (p1->py() + p2->py())*(p1->py() + p2->py()) -
               (p1->pz() + p2->pz())*(p1->pz() + p2->pz()) );
}

struct MyHLTEff 
{
  void init();
  
  TTree*book(TTree *t, const std::string & name = "trk_hlt_");
  Float_t pt;
  Float_t eta;
  Float_t phi;
  Int_t nHits;
  Int_t nRPCHits;
  Int_t nGEMHits;
  Int_t nDTHits;
  Int_t nCSCHits;
};

struct MyTrackEff
{
  void init();
  
  TTree*book(TTree *t, const std::string & name = "trk_eff_");
  Int_t lumi;
  Int_t run;
  Int_t event;
  
  // Dark photon  
  Float_t genGd_m;
  Float_t genGd_E;
  Float_t genGd_p;
  Float_t genGd_pt;
  Float_t genGd_px;
  Float_t genGd_py;
  Float_t genGd_pz;
  Float_t genGd_eta;
  Float_t genGd_phi;
  Float_t genGd_vx;
  Float_t genGd_vy;
  Float_t genGd_vz;
  Float_t genGd_vLx;
  Float_t genGd_vLy;
  Float_t genGd_vLz;
  Float_t genGd_lxy;
  Float_t genGd_l;
  Float_t genGd_dxy;
  Float_t genGd0Gd1_dR;
  Float_t genGd0Gd1_m;

  Float_t genGdMu_dxy_max;
  Float_t genGdMu_eta_max;

  // Gen level muon
  Int_t genGd_index;
  Int_t genGdMu_index;
  Float_t genGdMu_p[2];
  Float_t genGdMu_pt[2];
  Float_t genGdMu_px[2];
  Float_t genGdMu_py[2];
  Float_t genGdMu_pz[2];
  Float_t genGdMu_eta[2];
  Float_t genGdMu_phi[2];
  Float_t genGdMu_phi_corr[2];
  Float_t genGdMu_vx[2];
  Float_t genGdMu_vy[2];
  Float_t genGdMu_vz[2];
  Float_t genGdMu_dxy[2];

  Float_t beamSpot_x;
  Float_t beamSpot_y;
  Float_t beamSpot_z;

  Double_t vtx_x;
  Double_t vtx_y;
  Double_t vtx_z;
  Double_t vtx_r;
  Float_t eta_gp;
  Float_t phi_gp;
  Float_t x_gp;
  Float_t y_gp;
  Float_t z_gp;
  Float_t deltaphi_h_g;
  Float_t deltaphi_t_h;
  Float_t deltaphi_t_g;
  Float_t pt_gv;
  Float_t phi_gv;
  Float_t eta_gv;
  Float_t r_gp;
  
  Float_t sim_pt;
  Float_t sim_pt_inv;
  Float_t sim_eta;
  Float_t sim_eta_2ndStation;
  Float_t sim_phi;
  Float_t sim_dxy;
  Float_t sim_charge;

  Char_t has_dt_sh;
  Int_t nlayerdt;
  Int_t nslayerdt;
  Float_t R_gv;
  Float_t Z_gv;
  Float_t X_gv;
  Float_t Y_gv;
  
  Int_t wheel;
  Int_t station;
  
  Int_t n_dt_seg;
  Int_t n_dt_st_sh; // number of dt stations with at least 3 layers

  Int_t n_dt_st_seg; // number of dt stations with segments
  Int_t n_csc_seg;

  Int_t n_csc_st_sh; // number of dt stations with at least 3 layers
  Int_t n_csc_st_seg; // number of csc stations with segments

  Int_t n_rpc_rh;
  Int_t n_gem_rh;
  Int_t n_rpc_st_sh;
  Int_t n_gem_st_sh;
  Int_t n_rpc_st_rh;
  Int_t n_gem_st_rh;

  Int_t has_ge11_st_sh;
  Int_t has_ge21_st_sh;

  Int_t has_ge11_st_1rh;
  Int_t has_ge21_st_1rh;
  Int_t has_ge11_st_2rh;
  Int_t has_ge21_st_2rh;

  Int_t has_l1Extra;
  Float_t l1Extra_pt;
  Float_t l1Extra_eta;
  Float_t l1Extra_phi;
  Float_t l1Extra_dR;
  Int_t has_recoTrackExtra;
  Float_t recoTrackExtra_pt_inner;
  Float_t recoTrackExtra_eta_inner;
  Float_t recoTrackExtra_phi_inner;  
  Float_t recoTrackExtra_pt_outer;
  Float_t recoTrackExtra_eta_outer;
  Float_t recoTrackExtra_phi_outer;
  Int_t has_recoTrack;
  Float_t recoTrack_pt_outer;
  Float_t recoTrack_eta_outer;
  Float_t recoTrack_phi_outer;
  Int_t has_recoChargedCandidate;
  Float_t recoChargedCandidate_pt;
  Float_t recoChargedCandidate_eta;
  Float_t recoChargedCandidate_phi;

  Int_t recoChargedCandidate_st1;
  Int_t recoChargedCandidate_st2;
  Int_t recoChargedCandidate_st3;
  Int_t recoChargedCandidate_st4;

  Int_t recoChargedCandidate_st1_Valid;
  Int_t recoChargedCandidate_st2_Valid;
  Int_t recoChargedCandidate_st3_Valid;
  Int_t recoChargedCandidate_st4_Valid;

  Int_t recoChargedCandidate_nHits;
  Int_t recoChargedCandidate_nHitsGEM;
  Int_t recoChargedCandidate_nHitsCSC;
  Int_t recoChargedCandidate_nHitsDT;
  Int_t recoChargedCandidate_nHitsRPC;

  Int_t recoChargedCandidate_nHitsValid;
  Int_t recoChargedCandidate_nHitsGEMValid;
  Int_t recoChargedCandidate_nHitsCSCValid;
  Int_t recoChargedCandidate_nHitsDTValid;
  Int_t recoChargedCandidate_nHitsRPCValid;

  // per subsystem and per station (rpcb, rpcf, gem, csc, dt)
  // 

  Char_t cand_rpcb_st_1;
  Char_t cand_rpcb_st_2;
  Char_t cand_rpcb_st_3;
  Char_t cand_rpcb_st_4;

  Char_t cand_rpcf_st_1;
  Char_t cand_rpcf_st_2;
  Char_t cand_rpcf_st_3;
  Char_t cand_rpcf_st_4;

  Char_t cand_csc_st_1;
  Char_t cand_csc_st_2;
  Char_t cand_csc_st_3;
  Char_t cand_csc_st_4;

  Char_t cand_dt_st_1;
  Char_t cand_dt_st_2;
  Char_t cand_dt_st_3;
  Char_t cand_dt_st_4;

  Char_t cand_gem_st_1;
  Char_t cand_gem_st_2;
};


class HLTBendingAngle : public edm::EDAnalyzer 
{
public:
  explicit HLTBendingAngle(const edm::ParameterSet&);
  ~HLTBendingAngle();
  
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob();
  
  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
  
private:
  
  void analyzeTrackEfficiency(SimTrackMatchManager& match, int trk_no);
  void analyzeHLTEfficiency(const reco::TrackExtraCollection& tracks);
  bool isSimTrackGood(const SimTrack &t);
  void book();
  void init();
  void fill();
  
  TTree *tree_hlt_;
  MyHLTEff ehlt_;
  
  TTree *tree_eff_[68];
  MyTrackEff etrk_[68];

  int n_sim_trk_;

  edm::ParameterSet cfg_;
  int verbose_;
  int verboseSimTrack_;
  edm::InputTag simInputLabel_;
  double simTrackMinPt_;
  double simTrackMinEta_;
  double simTrackMaxEta_;
  double simTrackOnlyMuon_;

  std::vector<string> cscStations_;
  std::vector<string> dtStations_;
  std::vector<string> rpcStations_;
  std::vector<string> gemStations_;
  std::vector<string> muonStations_;

  std::vector<int> cscStationsToUse_;
  std::vector<int> dtStationsToUse_;
  std::vector<int> rpcStationsToUse_;
  std::vector<int> gemStationsToUse_;
  std::vector<int> muonStationsToUse_;

  int nCscStationsToUse_ = cscStationsToUse_.size();
  int nRpcStationsToUse_ = rpcStationsToUse_.size();
  int nDtStationsToUse_ = dtStationsToUse_.size();
  int nGemStationsToUse_ = gemStationsToUse_.size();
};

HLTBendingAngle::HLTBendingAngle(const edm::ParameterSet& ps)
  : cfg_(ps.getParameterSet("simTrackMatching"))
  , verbose_(ps.getUntrackedParameter<int>("verbose"))
{
  cscStations_ = cfg_.getParameter<std::vector<string> >("cscStations");
  dtStations_ = cfg_.getParameter<std::vector<string> >("dtStations");
  rpcStations_ = cfg_.getParameter<std::vector<string> >("rpcStations");
  gemStations_ = cfg_.getParameter<std::vector<string> >("gemStations");

  muonStations_.clear();
  muonStations_.push_back("MU_ALL");
  muonStations_.insert(muonStations_.end(), dtStations_.begin(), dtStations_.end());
  muonStations_.insert(muonStations_.end(), cscStations_.begin(), cscStations_.end());
  muonStations_.insert(muonStations_.end(), rpcStations_.begin(), rpcStations_.end());
  muonStations_.insert(muonStations_.end(), gemStations_.begin(), gemStations_.end());

  cscStationsToUse_ = cfg_.getParameter<std::vector<int> >("cscStationsToUse");
  dtStationsToUse_ = cfg_.getParameter<std::vector<int> >("dtStationsToUse");
  rpcStationsToUse_ = cfg_.getParameter<std::vector<int> >("rpcStationsToUse");
  gemStationsToUse_ = cfg_.getParameter<std::vector<int> >("gemStationsToUse");

  nCscStationsToUse_ = cscStationsToUse_.size();
  nRpcStationsToUse_ = rpcStationsToUse_.size();
  nDtStationsToUse_ = dtStationsToUse_.size();
  nGemStationsToUse_ = gemStationsToUse_.size();

  auto simTrack = cfg_.getParameter<edm::ParameterSet>("simTrack");
  verboseSimTrack_ = simTrack.getParameter<int>("verbose");
  simInputLabel_ = edm::InputTag("g4SimHits");
  simTrackMinPt_ = simTrack.getParameter<double>("minPt");
  simTrackMinEta_ = simTrack.getParameter<double>("minEta");
  simTrackMaxEta_ = simTrack.getParameter<double>("maxEta");
  simTrackOnlyMuon_ = simTrack.getParameter<bool>("onlyMuon");

  n_sim_trk_ = 0;

  book();
};

HLTBendingAngle::~HLTBendingAngle()
{
}

void
HLTBendingAngle::book()
{
  for (unsigned int i=0; i<muonStations_.size(); ++i) {
    tree_eff_[i] = etrk_[i].book(tree_eff_[i], "trk_eff_" + muonStations_[i]);
  }
  tree_hlt_ = ehlt_.book(tree_hlt_, "trk_hlt");
}


void
HLTBendingAngle::init()
{
  for (unsigned int i=0; i<muonStations_.size(); ++i) etrk_[i].init();
}


void
HLTBendingAngle::fill() 
{
  for (unsigned int i=0; i<muonStations_.size(); ++i) tree_eff_[i]->Fill();
}


void
HLTBendingAngle::analyze(const edm::Event& ev, const edm::EventSetup& es)
{
  using namespace edm;
  

  edm::Handle<edm::SimTrackContainer> sim_tracks;
  ev.getByLabel(simInputLabel_, sim_tracks);
  const edm::SimTrackContainer & sim_track = *sim_tracks.product();
  
  edm::Handle<edm::SimVertexContainer> sim_vertices;
  ev.getByLabel(simInputLabel_, sim_vertices);
  const edm::SimVertexContainer & sim_vert = *sim_vertices.product();
  
  if (verboseSimTrack_) {
    std::cout << "Total number of SimTracks in this event: " << sim_track.size() << std::endl;   
    std::cout << "Total number of SimVertexs in this event: " << sim_vert.size() << std::endl;
  }
  
  auto recoTrackExtra = cfg_.getParameter<edm::ParameterSet>("recoTrackExtra");
  std::vector<edm::InputTag> recoTrackExtraInputLabel_ = recoTrackExtra.getParameter<std::vector<edm::InputTag>>("validInputTags");
  
  // RecoTrackExtra 
  edm::Handle<reco::TrackExtraCollection> recoTrackExtras;
  if (gemvalidation::getByLabel(recoTrackExtraInputLabel_, recoTrackExtras, ev)) 
    analyzeHLTEfficiency(*recoTrackExtras.product());

  int trk_no=0;
  for (auto& t: *sim_tracks.product()) {
    if(!isSimTrackGood(t)) continue;
    if (verboseSimTrack_) {
      std::cout << "Processing SimTrack " << trk_no + 1 << std::endl;      
      std::cout << "pt(GeV/c) = " << t.momentum().pt() << ", eta = " << t.momentum().eta()  
		<< ", phi = " << t.momentum().phi() << ", Q = " << t.charge()
		<< ", vtxIndex = " << t.vertIndex() << std::endl;
    }
    SimTrackMatchManager match(t, sim_vert[t.vertIndex()], cfg_, ev, es);
    analyzeTrackEfficiency(match, trk_no);    
    ++trk_no;
    ++n_sim_trk_;
  }
}


void 
HLTBendingAngle::analyzeHLTEfficiency(const reco::TrackExtraCollection& tracks)
{
  ehlt_.init();
  
  for(auto& track: tracks) {
    ehlt_.pt = track.outerMomentum().Rho();
    ehlt_.eta = track.outerMomentum().eta();
    ehlt_.phi = track.outerMomentum().phi();
    for(auto rh = track.recHitsBegin(); rh != track.recHitsEnd(); rh++) {
      auto id((**rh).rawId());
      if (!(**rh).isValid()) continue;      
      if (gemvalidation::is_dt(id))  ehlt_.nDTHits++;
      if (gemvalidation::is_rpc(id)) ehlt_.nRPCHits++;
      if (gemvalidation::is_gem(id)) ehlt_.nGEMHits++;
      if (gemvalidation::is_csc(id)) ehlt_.nCSCHits++;
      ehlt_.nHits++;
    }
    tree_hlt_->Fill();
  }
}


void 
HLTBendingAngle::analyzeTrackEfficiency(SimTrackMatchManager& match, int trk_no)
{
  // initialize the tree
  init();

  const DisplacedGENMuonMatcher& match_gen = match.genMuons();
  const SimHitMatcher& match_sh = match.simhits();
  const DTRecHitMatcher& match_dtrh = match.dtRecHits();
  const CSCRecHitMatcher& match_cscrh = match.cscRecHits();
  const GEMRecHitMatcher& match_gemrh = match.gemRecHits();
  const RPCRecHitMatcher& match_rpcrh = match.rpcRecHits();
  const L1GlobalMuonTriggerMatcher& match_l1_gmt = match.l1GMTCands();
  const HLTTrackMatcher& match_hlt_track = match.hltTracks();
  const SimTrack& t = match_sh.trk();
  const SimVertex& vtx = match_sh.vtx();
  
  etrk_[0].run = match_sh.event().id().run();
  etrk_[0].lumi = match_sh.event().id().luminosityBlock();
  etrk_[0].event = match_sh.event().id().event();

  //****************************************************************************
  //                              GEN LEVEL                                     
  //****************************************************************************

  auto matchedGENMuons(match_gen.getMatchedGENMuons());
  auto matchedDarkBoson(match_gen.getMatchedDarkBoson());

  // Dark photon  
  etrk_[0].genGd_m = matchedDarkBoson->mass();
  etrk_[0].genGd_E = matchedDarkBoson->energy();
  etrk_[0].genGd_p = matchedDarkBoson->p();
  etrk_[0].genGd_pt = matchedDarkBoson->pt();
  etrk_[0].genGd_px = matchedDarkBoson->px();
  etrk_[0].genGd_py = matchedDarkBoson->py();
  etrk_[0].genGd_pz = matchedDarkBoson->pz();
  etrk_[0].genGd_eta = matchedDarkBoson->eta();
  etrk_[0].genGd_phi = matchedDarkBoson->phi();
  etrk_[0].genGd_vx = matchedDarkBoson->vx();
  etrk_[0].genGd_vy = matchedDarkBoson->vy();
  etrk_[0].genGd_vz = matchedDarkBoson->vz();

  etrk_[0].genGd_index = match_gen.darkBosonIndex();
  etrk_[0].genGdMu_index = match_gen.genMuonIndex();

  for (int i=0; i<2; ++i){
    etrk_[0].genGdMu_p[i] = matchedGENMuons[i]->p();
    etrk_[0].genGdMu_pt[i] = matchedGENMuons[i]->pt();
    etrk_[0].genGdMu_px[i] = matchedGENMuons[i]->px();
    etrk_[0].genGdMu_py[i] = matchedGENMuons[i]->py();
    etrk_[0].genGdMu_pz[i] = matchedGENMuons[i]->pz();
    etrk_[0].genGdMu_eta[i] = matchedGENMuons[i]->eta();
    etrk_[0].genGdMu_phi[i] = matchedGENMuons[i]->phi();
    // etrk_[0].genGdMu_phi_corr[i] = matchedGENMuons[i]->phi();
    etrk_[0].genGdMu_vx[i] = matchedGENMuons[i]->vx();
    etrk_[0].genGdMu_vy[i] = matchedGENMuons[i]->vy();
    etrk_[0].genGdMu_vz[i] = matchedGENMuons[i]->vz();
    etrk_[0].genGdMu_dxy[i] = dxy(etrk_[0].genGdMu_px[i], etrk_[0].genGdMu_py[i], etrk_[0].genGdMu_vx[i], etrk_[0].genGdMu_vy[i], etrk_[0].genGdMu_pt[i]);
  }

  etrk_[0].genGd_vLx = etrk_[0].genGdMu_vx[0] - etrk_[0].genGd_vx;
  etrk_[0].genGd_vLy = etrk_[0].genGdMu_vy[0] - etrk_[0].genGd_vy;
  etrk_[0].genGd_vLz = etrk_[0].genGdMu_vz[0] - etrk_[0].genGd_vz;

  // std::cout << "genGd_vLx " << etrk_[0].genGd_vLx << std::endl;
  // std::cout << "genGd_vLy " << etrk_[0].genGd_vLy << std::endl;
  // std::cout << "genGd_vLz " << etrk_[0].genGd_vLz << std::endl;

  // std::cout << "genGdMu_vx0 " << etrk_[0].genGdMu0_vx << std::endl;
  // std::cout << "genGdMu_vy0 " << etrk_[0].genGdMu0_vy << std::endl;
  // std::cout << "genGdMu_vz0 " << etrk_[0].genGdMu0_vz << std::endl;

  // std::cout << "genGdMu_vx1 " << etrk_[0].genGdMu1_vx << std::endl;
  // std::cout << "genGdMu_vy1 " << etrk_[0].genGdMu1_vy << std::endl;
  // std::cout << "genGdMu_vz1 " << etrk_[0].genGdMu1_vz << std::endl;

  etrk_[0].genGdMu_dxy_max = std::max(std::abs(etrk_[0].genGdMu_dxy[0]), std::abs(etrk_[0].genGdMu_dxy[1]));
  etrk_[0].genGdMu_eta_max = std::max(std::abs(etrk_[0].genGdMu_eta[0]), std::abs(etrk_[0].genGdMu_eta[1]));
  etrk_[0].genGd_lxy = sqrt( etrk_[0].genGd_vLx * etrk_[0].genGd_vLx + etrk_[0].genGd_vLy * etrk_[0].genGd_vLy );
  etrk_[0].genGd_l = sqrt( etrk_[0].genGd_vLx * etrk_[0].genGd_vLx + etrk_[0].genGd_vLy * etrk_[0].genGd_vLy + etrk_[0].genGd_vLz * etrk_[0].genGd_vLz );

  etrk_[0].genGd0Gd1_dR = match_gen.darkBosonDeltaR();
  etrk_[0].genGd0Gd1_m = match_gen.darkBosonInvM();

  //****************************************************************************
  //                              SIM LEVEL                                     
  //****************************************************************************

  const double vtx_x = match_sh.vtx().position().x();
  const double vtx_y = match_sh.vtx().position().y();
  const double vtx_z = match_sh.vtx().position().z();
  
  etrk_[0].vtx_x = vtx_x;
  etrk_[0].vtx_y = vtx_y;
  etrk_[0].vtx_z = vtx_z;
  etrk_[0].vtx_r = sqrt(vtx_x*vtx_x + vtx_y*vtx_y);
  
  etrk_[0].sim_pt = t.momentum().pt(); 
  etrk_[0].sim_pt_inv = 1./t.momentum().pt(); 
  etrk_[0].sim_dxy = (- vtx.position().x() * t.momentum().py() + vtx.position().y() * t.momentum().px() ) / t.momentum().pt();
  etrk_[0].sim_eta = t.momentum().eta();
  etrk_[0].sim_phi = t.momentum().phi();
  etrk_[0].sim_charge = t.charge();
  
  // // simhit information
  // for(auto ddt: match_sh.chamberIdsDT()) {

  //   std::cout << "DT Simhits " << ddt << std::endl;

  //   const DTChamberId id(ddt);
  //   const int stdt(gemvalidation::toDTType(id.wheel(),id.station()));
  //   //std::cout << "DT station" << stdt << std::endl;
  //   //    if (std::find(dtStationsToUse_.begin(), dtStationsToUse_.end(), stdt)!=dtStationsToUse_.end()) continue;
    
  //   // require at least 1 superlayer
  //   const int nsl(match_sh.nSuperLayersWithHitsInChamberDT(id.rawId()));
  //   if (nsl == 0) continue; 

  //   // require at least 3 layers hit per chamber
  //   const int nl(match_sh.nLayersWithHitsInChamberDT(id.rawId()));
  //   if (nl<3) continue;

  //   etrk_[stdt+1].nslayerdt  = nsl;
  //   etrk_[stdt+1].nlayerdt  = nl;

  //   etrk_[stdt+1].wheel = id.wheel();
  //   etrk_[stdt+1].station = id.station();

  //   const GlobalPoint hitGp(match_sh.simHitsMeanPosition(match_sh.hitsInChamber(ddt)));
  //   etrk_[stdt+1].eta_gp = hitGp.eta();
  //   etrk_[stdt+1].x_gp = hitGp.x();
  //   etrk_[stdt+1].y_gp = hitGp.y();
  //   etrk_[stdt+1].z_gp = hitGp.z();
  //   etrk_[stdt+1].r_gp = hitGp.perp();
  //   etrk_[stdt+1].phi_gp = hitGp.phi();

  //   const GlobalVector ym(match_sh.simHitsMeanMomentum(match_sh.hitsInChamber(ddt)));
  //   etrk_[stdt+1].eta_gv = ym.eta();
  //   etrk_[stdt+1].pt_gv = ym.perp();
  //   etrk_[stdt+1].phi_gv = ym.phi();
  //   etrk_[stdt+1].R_gv = sqrt (ym.x()*ym.x()+ym.y()*ym.y());
  //   etrk_[stdt+1].Z_gv = ym.z();
  //   etrk_[stdt+1].X_gv = ym.x();
  //   etrk_[stdt+1].Y_gv = ym.y();
  //   etrk_[stdt+1].deltaphi_h_g = reco::deltaPhi(hitGp.phi(), ym.phi());     //This one
  //   // etrk_[stdt].pt_calculated_dt = (1/(hitGp.phi() - ym.phi()))*1.4025845 + 0.674463;
  // } 

  etrk_[0].n_dt_st_sh = match_sh.nStationsDT();
  etrk_[0].n_csc_st_sh = match_sh.nStationsCSC();
  etrk_[0].n_rpc_st_sh = match_sh.nStationsRPC();
  etrk_[0].n_gem_st_sh = match_sh.nStationsGEM();

  etrk_[0].has_ge11_st_sh = match_sh.hitStationGEM(1,1);
  etrk_[0].has_ge21_st_sh = match_sh.hitStationGEM(3,1);

  etrk_[0].n_dt_seg =  match_dtrh.nDTRecSegment4Ds();
  etrk_[0].n_dt_st_seg = match_dtrh.chamberIdsDTRecSegment4D().size();
  etrk_[0].n_csc_seg =  match_cscrh.nCSCSegments();
  etrk_[0].n_csc_st_seg = match_cscrh.chamberIdsCSCSegment().size();

  etrk_[0].n_rpc_rh =  match_rpcrh.nRecHits();
  etrk_[0].n_gem_rh =  match_gemrh.nRecHits();
  etrk_[0].n_rpc_st_rh = match_rpcrh.chamberIds().size();
  etrk_[0].n_gem_st_rh = match_gemrh.superChamberIds().size();

  etrk_[0].has_ge11_st_1rh = match_gemrh.nCoincidenceGEMChambers(1,1);
  etrk_[0].has_ge11_st_2rh = match_gemrh.nCoincidenceGEMChambers(1,2);
  etrk_[0].has_ge21_st_1rh = match_gemrh.nCoincidenceGEMChambers(3,1);
  etrk_[0].has_ge21_st_2rh = match_gemrh.nCoincidenceGEMChambers(3,2);

  if (verbose_) {
    std::cout << "n_dt_seg: " << etrk_[0].n_dt_seg << std::endl;
    std::cout << "n_dt_st_sh: " << etrk_[0].n_dt_st_sh << std::endl;
    std::cout << "n_dt_st_seg: " << etrk_[0].n_dt_st_seg << std::endl;
    std::cout << "n_csc_seg: " << etrk_[0].n_csc_seg << std::endl;
    std::cout << "n_csc_st_sh: " << etrk_[0].n_csc_st_sh << std::endl;
    std::cout << "n_csc_st_seg: " << etrk_[0].n_csc_st_seg << std::endl;
    
    std::cout << "n_rpc_rh: " << etrk_[0].n_rpc_rh << std::endl;
    std::cout << "n_gem_rh: " << etrk_[0].n_gem_rh << std::endl;
    std::cout << "n_rpc_st_sh: " << etrk_[0].n_rpc_st_sh << std::endl;
    std::cout << "n_gem_st_sh: " << etrk_[0].n_gem_st_sh << std::endl;
    std::cout << "n_rpc_st_rh: " << etrk_[0].n_rpc_st_rh << std::endl;
    std::cout << "n_gem_st_rh: " << etrk_[0].n_gem_st_rh << std::endl;

    std::cout << "has_ge11_st_1rh: " << etrk_[0].has_ge11_st_1rh << std::endl;
    std::cout << "has_ge21_st_1rh: " << etrk_[0].has_ge21_st_1rh << std::endl;
    std::cout << "has_ge11_st_2rh: " << etrk_[0].has_ge11_st_2rh << std::endl;
    std::cout << "has_ge21_st_2rh: " << etrk_[0].has_ge21_st_2rh << std::endl;
    
  }
  // L1Extra
  auto l1Extras(match_l1_gmt.getMatchedL1ExtraMuonParticles());
  if (l1Extras.size()) {
    etrk_[0].has_l1Extra = 1;

    auto l1Extra(l1Extras[0].first);
    etrk_[0].l1Extra_pt = l1Extra.pt();
    etrk_[0].l1Extra_eta = l1Extra.eta();
    etrk_[0].l1Extra_phi = l1Extra.phi();
    etrk_[0].l1Extra_dR = l1Extras[0].second;
    if (verbose_) {
      std::cout << "Number of matched L1Extras: " << l1Extras.size() << std::endl;
      std::cout << "l1Extra_pt " << etrk_[0].l1Extra_pt << std::endl;
      std::cout << "l1Extra_eta " << etrk_[0].l1Extra_eta << std::endl;
      std::cout << "l1Extra_phi " << etrk_[0].l1Extra_phi << std::endl;
      std::cout << "l1Extra_dR " << etrk_[0].l1Extra_dR << std::endl;
    }
  }

  // RecoTrackExtra
  auto recoTrackExtras(match_hlt_track.getMatchedRecoTrackExtras());
  if (recoTrackExtras.size()) {
    if (verbose_) std::cout << "Number of matched RecoTrackExtras: " << recoTrackExtras.size() << std::endl;
    etrk_[0].has_recoTrackExtra = 1;

    auto recoTrackExtra(recoTrackExtras[0]);
    etrk_[0].recoTrackExtra_pt_inner = recoTrackExtra.innerMomentum().Rho();
    etrk_[0].recoTrackExtra_eta_inner = recoTrackExtra.innerPosition().eta();
    etrk_[0].recoTrackExtra_phi_inner = recoTrackExtra.innerPosition().phi();

    etrk_[0].recoTrackExtra_pt_outer = recoTrackExtra.outerMomentum().Rho();
    etrk_[0].recoTrackExtra_eta_outer = recoTrackExtra.outerPosition().eta();
    etrk_[0].recoTrackExtra_phi_outer = recoTrackExtra.outerPosition().phi();
  }

  // RecoTrack
  auto recoTracks(match_hlt_track.getMatchedRecoTracks());
  if (match_hlt_track.getMatchedRecoTracks().size()) {
    if (verbose_) std::cout << "Number of matched RecoTracks: " << recoTracks.size() << std::endl;
    etrk_[0].has_recoTrack = 1;

    auto recoTrack(recoTracks[0]);
    etrk_[0].recoTrack_pt_outer = recoTrack.outerPt();
    etrk_[0].recoTrack_eta_outer = recoTrack.outerEta();
    etrk_[0].recoTrack_phi_outer = recoTrack.outerPhi();
  }

  // RecoChargedCandidate
  auto recoChargedCandidates(match_hlt_track.getMatchedRecoChargedCandidates());
  if (recoChargedCandidates.size()) {
    if (verbose_) std::cout << "Number of matched RecoChargedCandidates: " << recoChargedCandidates.size() << std::endl;
    etrk_[0].has_recoChargedCandidate = 1;

    auto recoChargedCandidate(recoChargedCandidates[0]);
    etrk_[0].recoChargedCandidate_pt = recoChargedCandidate.pt();
    etrk_[0].recoChargedCandidate_eta = recoChargedCandidate.eta();
    etrk_[0].recoChargedCandidate_phi = recoChargedCandidate.phi();

    // recoChargedCandidate_st1 = ;
    // recoChargedCandidate_st2 = ;
    // recoChargedCandidate_st3 = ;
    // recoChargedCandidate_st4 = ;
    auto track(*(recoChargedCandidate.track()));
    int hits_st_1 = 0;
    int hits_st_2 = 0;
    int hits_st_3 = 0;
    int hits_st_4 = 0;

    int hitsValid_st_1 = 0;
    int hitsValid_st_2 = 0;
    int hitsValid_st_3 = 0;
    int hitsValid_st_4 = 0;


    for(auto rh = track.recHitsBegin(); rh != track.recHitsEnd(); rh++) {
      auto id((**rh).rawId());
      // all hits
      etrk_[0].recoChargedCandidate_nHits++;
      if (gemvalidation::is_dt(id)) {
        etrk_[0].recoChargedCandidate_nHitsDT++;
        DTChamberId detId(id);
        if (detId.station()==1)      {
          hits_st_1++;
          etrk_[0].cand_dt_st_1 |= 1;
        }
        else if (detId.station()==2) {
          hits_st_2++;
          etrk_[0].cand_dt_st_2 |= 1;
        }
        else if (detId.station()==3) {
          hits_st_3++;
          etrk_[0].cand_dt_st_3 |= 1;
        }
        else if (detId.station()==4) {
          hits_st_4++;
          etrk_[0].cand_dt_st_4 |= 1;
        }
      }
      if (gemvalidation::is_rpc(id)) {
        etrk_[0].recoChargedCandidate_nHitsRPC++;
        RPCDetId detId(id);

        if (detId.region()==0){
          if (detId.station()==1)      etrk_[0].cand_rpcb_st_1 |= 1;
          else if (detId.station()==2) etrk_[0].cand_rpcb_st_2 |= 1;
          else if (detId.station()==3) etrk_[0].cand_rpcb_st_3 |= 1;
          else if (detId.station()==4) etrk_[0].cand_rpcb_st_4 |= 1;
        }
        else {
          if (detId.station()==1)      etrk_[0].cand_rpcf_st_1 |= 1;
          else if (detId.station()==2) etrk_[0].cand_rpcf_st_2 |= 1;
          else if (detId.station()==3) etrk_[0].cand_rpcf_st_3 |= 1;
          else if (detId.station()==4) etrk_[0].cand_rpcf_st_4 |= 1;
        }
        if (detId.station()==1)      hits_st_1++;
        else if (detId.station()==2) hits_st_2++;
        else if (detId.station()==3) hits_st_3++;
        else if (detId.station()==4) hits_st_4++;
      }
      if (gemvalidation::is_gem(id)) {
        etrk_[0].recoChargedCandidate_nHitsGEM++;
        GEMDetId detId(id);
        if (detId.station()==1) {
          hits_st_1++;
          etrk_[0].cand_gem_st_1 |= 1;
        }
        if (detId.station()==3) {
          hits_st_2++;
          etrk_[0].cand_gem_st_2 |= 1;
        }
      }
      if (gemvalidation::is_csc(id)) {
        etrk_[0].recoChargedCandidate_nHitsCSC++;
        CSCDetId detId(id);
        if (detId.station()==1) { 
          hits_st_1++;
          etrk_[0].cand_csc_st_1 |= 1;
        }
        if (detId.station()==2) {
          hits_st_2++;
          etrk_[0].cand_csc_st_2 |= 1;
        }
        if (detId.station()==3) {
          hits_st_3++;
          etrk_[0].cand_csc_st_3 |= 1;
        }
        if (detId.station()==4) {
          hits_st_4++;
          etrk_[0].cand_csc_st_4 |= 1;
        }
      }      
      // valid hits
      if ((**rh).isValid()) {
        etrk_[0].recoChargedCandidate_nHitsValid++;
        if (gemvalidation::is_dt(id)) {
          etrk_[0].recoChargedCandidate_nHitsDTValid++;
          DTChamberId detId(id);
          if (detId.station()==1)      hitsValid_st_1++;
          else if (detId.station()==2) hitsValid_st_2++;
          else if (detId.station()==3) hitsValid_st_3++;
          else if (detId.station()==4) hitsValid_st_4++;
        }
        if (gemvalidation::is_rpc(id)) {
          etrk_[0].recoChargedCandidate_nHitsRPCValid++;
          RPCDetId detId(id);
          if (detId.station()==1)      hitsValid_st_1++;
          else if (detId.station()==2) hitsValid_st_2++;
          else if (detId.station()==3) hitsValid_st_3++;
          else if (detId.station()==4) hitsValid_st_4++;
        }
        if (gemvalidation::is_gem(id)) {
          etrk_[0].recoChargedCandidate_nHitsGEMValid++;
          GEMDetId detId(id);
          if (detId.station()==1) hitsValid_st_1++;
          if (detId.station()==3) hitsValid_st_2++;
        }
        if (gemvalidation::is_csc(id)) {
          etrk_[0].recoChargedCandidate_nHitsCSCValid++;
          CSCDetId detId(id);
          if (detId.station()==1) hitsValid_st_1++;
          if (detId.station()==2) hitsValid_st_2++;
          if (detId.station()==3) hitsValid_st_3++;
          if (detId.station()==4) hitsValid_st_4++;
        }
      }
    }
    etrk_[0].recoChargedCandidate_st1 = hits_st_1;
    etrk_[0].recoChargedCandidate_st2 = hits_st_2;
    etrk_[0].recoChargedCandidate_st3 = hits_st_3;
    etrk_[0].recoChargedCandidate_st4 = hits_st_4; 
    
    etrk_[0].recoChargedCandidate_st1_Valid = hitsValid_st_1;
    etrk_[0].recoChargedCandidate_st2_Valid = hitsValid_st_2;
    etrk_[0].recoChargedCandidate_st3_Valid = hitsValid_st_3;
    etrk_[0].recoChargedCandidate_st4_Valid = hitsValid_st_4;            
  }

  // fill the tree for every simtrack 
  fill();
}

bool 
HLTBendingAngle::isSimTrackGood(const SimTrack &t)
{
  // select only muon tracks
  if (t.noVertex()) return false;
  if (t.noGenpart()) return false;
  if (std::abs(t.type()) != 13 and simTrackOnlyMuon_) return false;
  if (t.momentum().pt() < simTrackMinPt_) return false;
  //const float eta(std::abs(t.momentum().eta()));
  //if (eta > simTrackMaxEta_ || eta < simTrackMinEta_) return false; 
  return true;
}


void MyHLTEff::init() 
{
  pt = -99;
  eta = -99;
  phi = -99;
  nRPCHits = 0;
  nGEMHits = 0;
  nDTHits = 0;
  nCSCHits = 0;
  nHits = 0;
}

void MyTrackEff::init()
{
  lumi = -99;
  run= -99;
  event = -99;
  
  beamSpot_x = 0;
  beamSpot_y = 0;
  beamSpot_z = 0;

  sim_pt = -9.;
  sim_pt_inv = -9.;
  sim_eta=-9.;
  sim_phi=-9.;
  sim_dxy = -99;
  sim_charge = -99;
  eta_gp = -9.;
  eta_gv = -9.;
  phi_gv= -9.;
  pt_gv= -9.;
  z_gp = -9900.;
  deltaphi_h_g = -9.;
  
  x_gp = -9900.;
  y_gp = -9900.;
  r_gp = -9900.;
  phi_gp = -99;
  vtx_x=-9999;
  vtx_y=-9999;
  vtx_z=-9999;
  vtx_r=-9999;
  has_dt_sh= 0;
  nlayerdt = 0;
  nslayerdt = 0;
  R_gv=-9999.;
  Z_gv=-9999.;
  X_gv=-9999.;
  Y_gv=-9999.;
  
  wheel = -9;
  station = - 9;
  
  n_dt_st_sh = -99;
  n_csc_st_sh = -99;
  n_rpc_st_sh = -99;
  n_gem_st_sh = -99;

  has_ge11_st_sh = -99;
  has_ge21_st_sh = -99;

  n_dt_seg = -99;
  n_csc_seg = -99;
  n_dt_st_seg = -99;
  n_csc_st_seg = -99;

  n_rpc_rh = -99;
  n_gem_rh = -99;
  n_rpc_st_rh = -99;
  n_gem_st_rh = -99;

  has_ge11_st_1rh = 0;
  has_ge21_st_1rh = 0;
  has_ge11_st_2rh = 0;
  has_ge21_st_2rh = 0;

  has_l1Extra = 0;
  l1Extra_pt = -99;
  l1Extra_eta = -99;
  l1Extra_phi = -99;
  l1Extra_dR = -99;
  has_recoTrackExtra = 0;
  recoTrackExtra_pt_inner = - 99.;
  recoTrackExtra_eta_inner = - 99.;
  recoTrackExtra_phi_inner = - 99.;  
  recoTrackExtra_pt_outer = - 99.;
  recoTrackExtra_eta_outer = - 99.;
  recoTrackExtra_phi_outer = - 99.;
  has_recoTrack = 0;
  recoTrack_pt_outer = - 99.;
  recoTrack_eta_outer = - 99.;
  recoTrack_phi_outer = - 99.;
  has_recoChargedCandidate = 0;
  recoChargedCandidate_pt = - 99.;
  recoChargedCandidate_eta = - 99.;
  recoChargedCandidate_phi = - 99.;
  
  recoChargedCandidate_st1 = 0;
  recoChargedCandidate_st2 = 0;
  recoChargedCandidate_st3 = 0;
  recoChargedCandidate_st4 = 0;

  recoChargedCandidate_st1_Valid = 0;
  recoChargedCandidate_st2_Valid = 0;
  recoChargedCandidate_st3_Valid = 0;
  recoChargedCandidate_st4_Valid = 0;

  recoChargedCandidate_nHits = 0;
  recoChargedCandidate_nHitsGEM = 0;
  recoChargedCandidate_nHitsCSC = 0;
  recoChargedCandidate_nHitsDT = 0;
  recoChargedCandidate_nHitsRPC = 0;

  recoChargedCandidate_nHitsValid = 0;
  recoChargedCandidate_nHitsGEMValid = 0;
  recoChargedCandidate_nHitsCSCValid = 0;
  recoChargedCandidate_nHitsDTValid = 0;
  recoChargedCandidate_nHitsRPCValid = 0;

  cand_rpcb_st_1 = 0;
  cand_rpcb_st_2 = 0;
  cand_rpcb_st_3 = 0;
  cand_rpcb_st_4 = 0;

  cand_rpcf_st_1 = 0;
  cand_rpcf_st_2 = 0;
  cand_rpcf_st_3 = 0;
  cand_rpcf_st_4 = 0;

  cand_csc_st_1 = 0;
  cand_csc_st_2 = 0;
  cand_csc_st_3 = 0;
  cand_csc_st_4 = 0;

  cand_dt_st_1 = 0;
  cand_dt_st_2 = 0;
  cand_dt_st_3 = 0;
  cand_dt_st_4 = 0;

  cand_gem_st_1 = 0;
  cand_gem_st_2 = 0;
}


TTree*MyHLTEff::book(TTree *t,const std::string & name)
{
  edm::Service< TFileService > fs;
  t = fs->make<TTree>(name.c_str(),name.c_str());
  t->Branch("eta", &eta);
  t->Branch("pt", &pt);
  t->Branch("phi", &phi);
  t->Branch("nRPCHits", &nRPCHits);
  t->Branch("nGEMHits", &nGEMHits);
  t->Branch("nDTHits", &nDTHits);
  t->Branch("nCSCHits", &nCSCHits);
  t->Branch("nHits", &nHits);
  return t;
}

TTree*MyTrackEff::book(TTree *t,const std::string & name)
{
  edm::Service< TFileService > fs;
  t = fs->make<TTree>(name.c_str(),name.c_str());
  t->Branch("lumi", &lumi);
  t->Branch("run", &run);
  t->Branch("event", &event);

  // Bosons
  t->Branch("genGd_m",   &genGd_m,   "genGd_m/F");
  t->Branch("genGd_E",   &genGd_E,   "genGd_E/F");
  t->Branch("genGd_p",   &genGd_p,   "genGd_p/F");
  t->Branch("genGd_pt",  &genGd_pt,  "genGd_pt/F");
  t->Branch("genGd_px",  &genGd_px,  "genGd_px/F");
  t->Branch("genGd_py",  &genGd_py,  "genGd_py/F");
  t->Branch("genGd_pz",  &genGd_pz,  "genGd_pz/F");
  t->Branch("genGd_eta", &genGd_eta, "genGd_eta/F");
  t->Branch("genGd_phi", &genGd_phi, "genGd_phi/F");
  t->Branch("genGd_vx",  &genGd_vx,  "genGd_vx/F");
  t->Branch("genGd_vy",  &genGd_vy,  "genGd_vy/F");
  t->Branch("genGd_vz",  &genGd_vz,  "genGd_vz/F");
  t->Branch("genGd_vLx",  &genGd_vLx,  "genGd_vLx/F");
  t->Branch("genGd_vLy",  &genGd_vLy,  "genGd_vLy/F");
  t->Branch("genGd_vLz",  &genGd_vLz,  "genGd_vLz/F");
  t->Branch("genGd_lxy",  &genGd_lxy,  "genGd_lxy/F");
  t->Branch("genGd_l",  &genGd_l,  "genGd_l/F");
  t->Branch("genGd_dxy",  &genGd_dxy,  "genGd_dxy/F");
  t->Branch("genGd0Gd1_dR",  &genGd0Gd1_dR,  "genGd0Gd1_dR/F");
  t->Branch("genGd0Gd1_m",  &genGd0Gd1_m,  "genGd0Gd1_m/F");
  t->Branch("genGd_dxy",  &genGd_dxy,  "genGd_dxy/F");
  t->Branch("genGdMu_dxy_max",  &genGdMu_dxy_max,  "genGdMu_dxy_max/F");
  t->Branch("genGdMu_eta_max",  &genGdMu_eta_max,  "genGdMu_eta_max/F");

  // Dimuons
  t->Branch("genGdMu_p", genGdMu_p, "genGdMu_p[2]/F");
  t->Branch("genGdMu_pt", genGdMu_pt, "genGdMu_pt[2]/F");
  t->Branch("genGdMu_px", genGdMu_px, "genGdMu_px[2]/F");
  t->Branch("genGdMu_py", genGdMu_py, "genGdMu_py[2]/F");
  t->Branch("genGdMu_pz", genGdMu_pz, "genGdMu_pz[2]/F");
  t->Branch("genGdMu_eta", genGdMu_eta, "genGdMu_eta[2]/F");
  t->Branch("genGdMu_phi", genGdMu_phi, "genGdMu_phi[2]/F");
  t->Branch("genGdMu_phi_corr", genGdMu_phi_corr, "genGdMu_phi_corr[2]/F");
  t->Branch("genGdMu_vx", genGdMu_vx, "genGdMu_vx[2]/F");
  t->Branch("genGdMu_vy", genGdMu_vy, "genGdMu_vy[2]/F");
  t->Branch("genGdMu_vz", genGdMu_vz, "genGdMu_vz[2]/F");
  t->Branch("genGdMu_dxy", genGdMu_dxy, "genGdMu_dxy[2]/F");

  // t->Branch("genGdMu0_p", &genGdMu0_p, "genGdMu0_p/F");
  // t->Branch("genGdMu0_pt", &genGdMu0_pt, "genGdMu0_pt/F");
  // t->Branch("genGdMu0_px", &genGdMu0_px, "genGdMu0_px/F");
  // t->Branch("genGdMu0_py", &genGdMu0_py, "genGdMu0_py/F");
  // t->Branch("genGdMu0_pz", &genGdMu0_pz, "genGdMu0_pz/F");
  // t->Branch("genGdMu0_eta", &genGdMu0_eta, "genGdMu0_eta/F");
  // t->Branch("genGdMu0_phi", &genGdMu0_phi, "genGdMu0_phi/F");
  // t->Branch("genGdMu0_phi_corr", &genGdMu0_phi_corr, "genGdMu0_phi_corr/F");
  // t->Branch("genGdMu0_vx", &genGdMu0_vx, "genGdMu0_vx/F");
  // t->Branch("genGdMu0_vy", &genGdMu0_vy, "genGdMu0_vy/F");
  // t->Branch("genGdMu0_vz", &genGdMu0_vz, "genGdMu0_vz/F");
  // t->Branch("genGdMu0_dxy", &genGdMu0_dxy, "genGdMu0_dxy/F");

  // t->Branch("genGdMu1_p", &genGdMu1_p, "genGdMu1_p/F");
  // t->Branch("genGdMu1_pt", &genGdMu1_pt, "genGdMu1_pt/F");
  // t->Branch("genGdMu1_px", &genGdMu1_px, "genGdMu1_px/F");
  // t->Branch("genGdMu1_py", &genGdMu1_py, "genGdMu1_py/F");
  // t->Branch("genGdMu1_pz", &genGdMu1_pz, "genGdMu1_pz/F");
  // t->Branch("genGdMu1_eta", &genGdMu1_eta, "genGdMu1_eta/F");
  // t->Branch("genGdMu1_phi", &genGdMu1_phi, "genGdMu1_phi/F");
  // t->Branch("genGdMu1_phi_corr", &genGdMu1_phi_corr, "genGdMu1_phi_corr/F");
  // t->Branch("genGdMu1_vx", &genGdMu1_vx, "genGdMu1_vx/F");
  // t->Branch("genGdMu1_vy", &genGdMu1_vy, "genGdMu1_vy/F");
  // t->Branch("genGdMu1_vz", &genGdMu1_vz, "genGdMu1_vz/F");
  // t->Branch("genGdMu1_dxy", &genGdMu1_dxy, "genGdMu1_dxy/F");

  t->Branch("sim_eta", &sim_eta);
  t->Branch("sim_pt", &sim_pt);
  t->Branch("sim_pt_inv", &sim_pt_inv);
  t->Branch("eta_gv", &eta_gv);
  t->Branch("sim_dxy", &sim_dxy);
  t->Branch("sim_charge", &sim_charge);

  t->Branch("wheel", &wheel);
  t->Branch("station", &station);

  t->Branch("pt_gv", &pt_gv);
  t->Branch("phi_gv", &phi_gv);
  t->Branch("eta_gp", &eta_gp);
  t->Branch("vtx_x", &vtx_x);
  t->Branch("vtx_y", &vtx_y);
  t->Branch("vtx_z", &vtx_z);
  t->Branch("vtx_r", &vtx_r);
  t->Branch("deltaphi_h_g", &deltaphi_h_g);
  t->Branch("z_gp", &z_gp);
  t->Branch("x_gp", &x_gp);
  t->Branch("y_gp", &y_gp);
  t->Branch("r_gp", &r_gp);
  t->Branch("phi_gp", &phi_gp);
  t->Branch("sim_phi", &sim_phi);
  t->Branch("nlayerdt", &nlayerdt);
  t->Branch("nslayerdt", &nslayerdt);

  t->Branch("has_ge11_st_sh", &has_ge11_st_sh);
  t->Branch("has_ge21_st_sh", &has_ge21_st_sh);

  t->Branch("n_dt_st_sh", &n_dt_st_sh);
  t->Branch("n_csc_st_sh", &n_csc_st_sh);
  t->Branch("n_rpc_st_sh", &n_rpc_st_sh);
  t->Branch("n_gem_st_sh", &n_gem_st_sh);

  t->Branch("n_dt_seg", &n_dt_seg);
  t->Branch("n_dt_st_seg", &n_dt_st_seg);
  t->Branch("n_csc_seg", &n_csc_seg);
  t->Branch("n_csc_st_seg", &n_csc_st_seg);

  t->Branch("n_rpc_rh", &n_rpc_rh);
  t->Branch("n_gem_rh", &n_gem_rh);
  t->Branch("n_rpc_st_rh", &n_rpc_st_rh);
  t->Branch("n_gem_st_rh", &n_gem_st_rh);

  t->Branch("has_ge11_st_1rh", &has_ge11_st_1rh);
  t->Branch("has_ge21_st_1rh", &has_ge21_st_1rh); 
  t->Branch("has_ge11_st_2rh", &has_ge11_st_2rh);
  t->Branch("has_ge21_st_2rh", &has_ge21_st_2rh);

  t->Branch("has_l1Extra", &has_l1Extra);
  t->Branch("l1Extra_pt", &l1Extra_pt);
  t->Branch("l1Extra_eta", &l1Extra_eta);
  t->Branch("l1Extra_phi", &l1Extra_phi);
  t->Branch("l1Extra_dR", &l1Extra_dR);
  t->Branch("has_recoTrackExtra", &has_recoTrackExtra);
  t->Branch("recoTrackExtra_pt_inner", &recoTrackExtra_pt_inner);
  t->Branch("recoTrackExtra_eta_inner", &recoTrackExtra_eta_inner);
  t->Branch("recoTrackExtra_phi_inner", &recoTrackExtra_phi_inner);
  t->Branch("recoTrackExtra_pt_outer", &recoTrackExtra_pt_outer);
  t->Branch("recoTrackExtra_eta_outer", &recoTrackExtra_eta_outer);
  t->Branch("recoTrackExtra_phi_outer", &recoTrackExtra_phi_outer);
  t->Branch("has_recoTrack", &has_recoTrack);
  t->Branch("recoTrack_pt_outer", &recoTrack_pt_outer);
  t->Branch("recoTrack_eta_outer", &recoTrack_eta_outer);
  t->Branch("recoTrack_phi_outer", &recoTrack_phi_outer);
  t->Branch("has_recoChargedCandidate", &has_recoChargedCandidate);
  t->Branch("recoChargedCandidate_pt", &recoChargedCandidate_pt);
  t->Branch("recoChargedCandidate_eta", &recoChargedCandidate_eta);
  t->Branch("recoChargedCandidate_phi", &recoChargedCandidate_phi); 

  t->Branch("recoChargedCandidate_st1", &recoChargedCandidate_st1); 
  t->Branch("recoChargedCandidate_st2", &recoChargedCandidate_st2); 
  t->Branch("recoChargedCandidate_st3", &recoChargedCandidate_st3); 
  t->Branch("recoChargedCandidate_st4", &recoChargedCandidate_st4); 

  t->Branch("recoChargedCandidate_st1_Valid", &recoChargedCandidate_st1_Valid); 
  t->Branch("recoChargedCandidate_st2_Valid", &recoChargedCandidate_st2_Valid); 
  t->Branch("recoChargedCandidate_st3_Valid", &recoChargedCandidate_st3_Valid); 
  t->Branch("recoChargedCandidate_st4_Valid", &recoChargedCandidate_st4_Valid); 

  t->Branch("recoChargedCandidate_nHits", &recoChargedCandidate_nHits); 
  t->Branch("recoChargedCandidate_nHitsGEM", &recoChargedCandidate_nHitsGEM); 
  t->Branch("recoChargedCandidate_nHitsCSC", &recoChargedCandidate_nHitsCSC); 
  t->Branch("recoChargedCandidate_nHitsDT", &recoChargedCandidate_nHitsDT); 
  t->Branch("recoChargedCandidate_nHitsRPC", &recoChargedCandidate_nHitsRPC); 
  
  t->Branch("recoChargedCandidate_nHitsValid", &recoChargedCandidate_nHitsValid); 
  t->Branch("recoChargedCandidate_nHitsGEMValid", &recoChargedCandidate_nHitsGEMValid); 
  t->Branch("recoChargedCandidate_nHitsCSCValid", &recoChargedCandidate_nHitsCSCValid); 
  t->Branch("recoChargedCandidate_nHitsDTValid", &recoChargedCandidate_nHitsDTValid); 
  t->Branch("recoChargedCandidate_nHitsRPCValid", &recoChargedCandidate_nHitsRPCValid); 

  t->Branch("cand_rpcb_st_1", &cand_rpcb_st_1);
  t->Branch("cand_rpcb_st_2", &cand_rpcb_st_2);
  t->Branch("cand_rpcb_st_3", &cand_rpcb_st_3);
  t->Branch("cand_rpcb_st_4", &cand_rpcb_st_4);

  t->Branch("cand_rpcf_st_1", &cand_rpcf_st_1);
  t->Branch("cand_rpcf_st_2", &cand_rpcf_st_2);
  t->Branch("cand_rpcf_st_3", &cand_rpcf_st_3);
  t->Branch("cand_rpcf_st_4", &cand_rpcf_st_4);

  t->Branch("cand_csc_st_1", &cand_csc_st_1);
  t->Branch("cand_csc_st_2", &cand_csc_st_2);
  t->Branch("cand_csc_st_3", &cand_csc_st_3);
  t->Branch("cand_csc_st_4", &cand_csc_st_4);

  t->Branch("cand_dt_st_1", &cand_dt_st_1);
  t->Branch("cand_dt_st_2", &cand_dt_st_2);
  t->Branch("cand_dt_st_3", &cand_dt_st_3);
  t->Branch("cand_dt_st_4", &cand_dt_st_4);

  t->Branch("cand_gem_st_1", &cand_gem_st_1);
  t->Branch("cand_gem_st_2", &cand_gem_st_2);

  return t;
}


void
HLTBendingAngle::endJob()
{
  //  std::cout << "Number of simTracks " << n_sim_trk_ << std::endl;
}

void
HLTBendingAngle::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(HLTBendingAngle);
