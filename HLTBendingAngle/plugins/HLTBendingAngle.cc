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
#include "GEMCode/GEMValidation/interface/SimTrackMatchManager.h"


using namespace std;

struct MyTrackEff
{
  void init();
  
  TTree*book(TTree *t, const std::string & name = "trk_eff_");
  Int_t lumi;
  Int_t run;
  Int_t event;
  
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

  bool isSimTrackGood(const SimTrack &t);
  void book();
  void init();
  void fill();
  
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
  , verbose_(ps.getUntrackedParameter<int>("verbose", 0))
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
  
  //****************************************************************************
  //                              GEN LEVEL                                     
  //****************************************************************************

  // needs a secion about gen level matching + gen muon matching to sim muon matching

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
HLTBendingAngle::analyzeTrackEfficiency(SimTrackMatchManager& match, int trk_no)
{
  // initialize the tree
  init();

  const SimHitMatcher& match_sh = match.simhits();
  const DTRecHitMatcher& match_dtrh = match.dtRecHits();
  const CSCRecHitMatcher& match_cscrh = match.cscRecHits();
  const L1GlobalMuonTriggerMatcher& match_l1_gmt = match.l1GMTCands();
  const HLTTrackMatcher& match_hlt_track = match.hltTracks();
  const SimTrack& t = match_sh.trk();
  const SimVertex& vtx = match_sh.vtx();

  etrk_[0].run = match_sh.event().id().run();
  etrk_[0].lumi = match_sh.event().id().luminosityBlock();
  etrk_[0].event = match_sh.event().id().event();
  
  // edm::Handle<reco::BeamSpot> beamSpot;
  // match_sh.event().getByLabel("offlineBeamSpot",beamSpot);
  etrk_[0].beamSpot_x = 0;//beamSpot->position().x();
  etrk_[0].beamSpot_y = 0;//beamSpot->position().y();
  etrk_[0].beamSpot_z = 0;//beamSpot->position().z();

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
  etrk_[0].n_dt_seg =  match_dtrh.nDTRecSegment4Ds();
  etrk_[0].n_dt_st_seg = match_dtrh.chamberIdsDTRecSegment4D().size();
  etrk_[0].n_csc_st_sh = match_sh.nStationsCSC();
  etrk_[0].n_csc_seg =  match_cscrh.nCSCSegments();
  etrk_[0].n_csc_st_seg = match_cscrh.chamberIdsCSCSegment().size();

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
  
  n_dt_seg = -99;
  n_dt_st_sh = -99;
  n_dt_st_seg = -99;
  n_csc_seg = -99;
  n_csc_st_sh = -99;
  n_csc_st_seg = -99;

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
}

TTree*MyTrackEff::book(TTree *t,const std::string & name)
{
  edm::Service< TFileService > fs;
  t = fs->make<TTree>(name.c_str(),name.c_str());
  t->Branch("lumi", &lumi);
  t->Branch("run", &run);
  t->Branch("event", &event);
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

  t->Branch("n_dt_seg", &n_dt_seg);
  t->Branch("n_dt_st_sh", &n_dt_st_sh);
  t->Branch("n_dt_st_seg", &n_dt_st_seg);
  t->Branch("n_csc_seg", &n_csc_seg);
  t->Branch("n_csc_st_sh", &n_csc_st_sh);
  t->Branch("n_csc_st_seg", &n_csc_st_seg);

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

  return t;
}


void
HLTBendingAngle::endJob()
{
  std::cout << "Number of simTracks " << n_sim_trk_ << std::endl;
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
