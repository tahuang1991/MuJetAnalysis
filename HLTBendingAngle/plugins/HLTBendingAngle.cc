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
#include "GEMCode/GEMValidation/interface/SimTrackMatchManager.h"


using namespace std;

struct MyTrackEff
{
  void init();
  
  TTree*book(TTree *t, const std::string & name = "trk_eff_dt_");
  Int_t lumi;
  Int_t run;
  Int_t event;
  Char_t charge_dt;
  
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
  Char_t has_dt_sh;
  Int_t nlayerdt;
  Int_t nslayerdt;
  Float_t R_gv;
  Float_t Z_gv;
  Float_t X_gv;
  Float_t Y_gv;
  
  Int_t wheel;
  Int_t station;
  
  Int_t n_dt_rh;
  Int_t n_dt_seg;
  Int_t n_dt_st_sh; // number of dt stations with at least 3 layers
  Int_t n_dt_st_rh; // number of dt stations with at least 3 layers
  Int_t n_dt_st_seg; // number of dt stations with segments
  Int_t n_csc_seg;
  Int_t n_csc_st_seg; // number of csc stations with segments

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
  
  int detIdToMBStation(int wh, int st);
  int detIdToMEStation(int st, int ri);

  TTree *tree_eff_[56];
  MyTrackEff etrk_[56];
  
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

  std::set<int> stationscsc_to_use_;
  std::set<int> stationsdt_to_use_;

  std::vector<std::pair<int,int> > cscStationsCo_;
  std::vector<std::pair<int,int> > dtStationsCo_;
};

HLTBendingAngle::HLTBendingAngle(const edm::ParameterSet& ps)
  : cfg_(ps.getParameterSet("simTrackMatching"))
  , verbose_(ps.getUntrackedParameter<int>("verbose", 0))
{
  cscStations_ = cfg_.getParameter<std::vector<string> >("cscStations");
  dtStations_ = cfg_.getParameter<std::vector<string> >("dtStations");

  auto simTrack = cfg_.getParameter<edm::ParameterSet>("simTrack");
  verboseSimTrack_ = simTrack.getParameter<int>("verbose");
  simInputLabel_ = edm::InputTag("g4SimHits");
  simTrackMinPt_ = simTrack.getParameter<double>("minPt");
  simTrackMinEta_ = simTrack.getParameter<double>("minEta");
  simTrackMaxEta_ = simTrack.getParameter<double>("maxEta");
  simTrackOnlyMuon_ = simTrack.getParameter<bool>("onlyMuon");

  vector<int> cscStations = ps.getParameter<vector<int> >("cscStations");
  copy(cscStations.begin(), cscStations.end(), inserter(stationscsc_to_use_, stationscsc_to_use_.end()));

  vector<int> dtStations = ps.getParameter<vector<int> >("dtStations");
  copy(dtStations.begin(), dtStations.end(),inserter(stationsdt_to_use_,stationsdt_to_use_.end()));

  for(auto s: stationscsc_to_use_) {
    stringstream ss;
    ss << "trk_eff_"<< cscStations_[s];
    tree_eff_[s] = etrk_[s].book(tree_eff_[s], ss.str());
  }

  for (auto m: stationsdt_to_use_) {
    stringstream ss;
    ss<< "trk_eff_" << dtStations_[m];
    tree_eff_[m] = etrk_[m].book(tree_eff_[m], ss.str());    
  }
  
  cscStationsCo_.push_back(std::make_pair(-99,-99));
  cscStationsCo_.push_back(std::make_pair(1,-99));
  cscStationsCo_.push_back(std::make_pair(1,4));
  cscStationsCo_.push_back(std::make_pair(1,1));
  cscStationsCo_.push_back(std::make_pair(1,2));
  cscStationsCo_.push_back(std::make_pair(1,3));
  cscStationsCo_.push_back(std::make_pair(2,1));
  cscStationsCo_.push_back(std::make_pair(2,2));
  cscStationsCo_.push_back(std::make_pair(3,1));
  cscStationsCo_.push_back(std::make_pair(3,2));
  cscStationsCo_.push_back(std::make_pair(4,1));
  cscStationsCo_.push_back(std::make_pair(4,2));

  dtStationsCo_.push_back(std::make_pair(-99,-99));
  dtStationsCo_.push_back(std::make_pair(0,1));
  dtStationsCo_.push_back(std::make_pair(0,2));
  dtStationsCo_.push_back(std::make_pair(0,3));
  dtStationsCo_.push_back(std::make_pair(0,4));
  dtStationsCo_.push_back(std::make_pair(1,1));
  dtStationsCo_.push_back(std::make_pair(1,3));
  dtStationsCo_.push_back(std::make_pair(1,4));
  dtStationsCo_.push_back(std::make_pair(1,2));
  dtStationsCo_.push_back(std::make_pair(2,1));
  dtStationsCo_.push_back(std::make_pair(2,2));
  dtStationsCo_.push_back(std::make_pair(2,3));
  dtStationsCo_.push_back(std::make_pair(2,4));
  dtStationsCo_.push_back(std::make_pair(-1,1));
  dtStationsCo_.push_back(std::make_pair(-1,2));
  dtStationsCo_.push_back(std::make_pair(-1,3));
  dtStationsCo_.push_back(std::make_pair(-1,4));
  dtStationsCo_.push_back(std::make_pair(-2,1));
  dtStationsCo_.push_back(std::make_pair(-2,2));
  dtStationsCo_.push_back(std::make_pair(-2,3));
  dtStationsCo_.push_back(std::make_pair(-2,4));

  n_sim_trk_ = 0;
};

HLTBendingAngle::~HLTBendingAngle()
{
}

int 
HLTBendingAngle::detIdToMBStation(int wh,  int st)
{
  auto p(std::make_pair(wh, st));
  return std::find(dtStationsCo_.begin(), dtStationsCo_.end(),p) - dtStationsCo_.begin();
}

int 
HLTBendingAngle::detIdToMEStation(int st, int ri)
{
  auto p(std::make_pair(st, ri));
  return std::find(cscStationsCo_.begin(), cscStationsCo_.end(), p) - cscStationsCo_.begin();
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
  const SimHitMatcher& match_sh = match.simhits();
  const DTRecHitMatcher& match_dtrh = match.dtRecHits();
  const CSCRecHitMatcher& match_cscrh = match.cscRecHits();
  const HLTTrackMatcher& match_hlt_track = match.hltTracks();
  const SimTrack& t = match_sh.trk();
  const SimVertex& vtx = match_sh.vtx();

  // information for each chamber
  for (auto st: stationsdt_to_use_)
  {
    etrk_[st].init();
    etrk_[st].run = match_sh.event().id().run();
    etrk_[st].lumi = match_sh.event().id().luminosityBlock();
    etrk_[st].event = match_sh.event().id().event();
    etrk_[st].charge_dt = t.charge();

    const double vtx_x = match_sh.vtx().position().x();
    const double vtx_y = match_sh.vtx().position().y();
    const double vtx_z = match_sh.vtx().position().z();
  
    etrk_[st].vtx_x = vtx_x;
    etrk_[st].vtx_y = vtx_y;
    etrk_[st].vtx_z = vtx_z;
    etrk_[st].vtx_r = sqrt(vtx_x*vtx_x + vtx_y*vtx_y);

    etrk_[st].sim_pt = t.momentum().pt(); 
    etrk_[st].sim_pt_inv = 1./t.momentum().pt(); 
    etrk_[st].sim_dxy = (- vtx.position().x() * t.momentum().py() + vtx.position().y() * t.momentum().px() ) / t.momentum().pt();
    etrk_[st].sim_eta = t.momentum().eta();
    etrk_[st].sim_phi = t.momentum().phi();
  }

  // simhit information
  for(auto ddt: match_sh.chamberIdsDT())
  {
    const DTChamberId id(ddt);
    const int stdt(detIdToMBStation(id.wheel(),id.station()));
    if (stationsdt_to_use_.count(stdt) == 0) continue;

    // require at least 1 superlayer
    const int nsl(match_sh.nSuperLayersWithHitsInChamberDT(id.rawId()));
    if (nsl == 0) continue; 

    // require at least 3 layers hit per chamber
    const int nl(match_sh.nLayersWithHitsInChamberDT(id.rawId()));
    if (nl<3) continue;

    etrk_[stdt].nslayerdt  = nsl;
    etrk_[stdt].nlayerdt  = nl;
    etrk_[0].n_dt_st_sh = match_sh.chamberIdsDT().size();

    etrk_[stdt].wheel = id.wheel();
    etrk_[stdt].station = id.station();

    const GlobalPoint hitGp(match_sh.simHitsMeanPosition(match_sh.hitsInChamber(ddt)));
    etrk_[stdt].eta_gp = hitGp.eta();
    etrk_[stdt].x_gp = hitGp.x();
    etrk_[stdt].y_gp = hitGp.y();
    etrk_[stdt].z_gp = hitGp.z();
    etrk_[stdt].r_gp = hitGp.perp();
    etrk_[stdt].phi_gp = hitGp.phi();

    const GlobalVector ym(match_sh.simHitsMeanMomentum(match_sh.hitsInChamber(ddt)));
    etrk_[stdt].eta_gv = ym.eta();
    etrk_[stdt].pt_gv = ym.perp();
    etrk_[stdt].phi_gv = ym.phi();
    etrk_[stdt].R_gv = sqrt (ym.x()*ym.x()+ym.y()*ym.y());
    etrk_[stdt].Z_gv = ym.z();
    etrk_[stdt].X_gv = ym.x();
    etrk_[stdt].Y_gv = ym.y();
    etrk_[stdt].deltaphi_h_g = reco::deltaPhi(hitGp.phi(), ym.phi());     //This one
    // etrk_[stdt].pt_calculated_dt = (1/(hitGp.phi() - ym.phi()))*1.4025845 + 0.674463;
  } 

  // rechits
  for(auto ddt: match_dtrh.chamberIdsDTRecHit1DPair())
  {
    const DTChamberId id(ddt);
    const int stdt(detIdToMBStation(id.wheel(),id.station()));
    if (stationsdt_to_use_.count(stdt) == 0) continue;

    // require at least 3 layers hit per chamber
    const int nl(match_sh.nLayersWithHitsInChamberDT(id.rawId()));
    if (nl<3) continue;

    etrk_[0].n_dt_rh =  match_dtrh.nDTRecHit1DPairs();
    etrk_[0].n_dt_st_rh = match_dtrh.chamberIdsDTRecHit1DPair().size();
  }  

  // DT segments
  for(auto ddt: match_dtrh.chamberIdsDTRecSegment4D())
  {
    const DTChamberId id(ddt);
    const int stdt(detIdToMBStation(id.wheel(),id.station()));
    if (stationsdt_to_use_.count(stdt) == 0) continue;

    // require at least 3 layers hit per chamber
    const int nl(match_sh.nLayersWithHitsInChamberDT(id.rawId()));
    if (nl<3) continue;

    etrk_[0].n_dt_seg =  match_dtrh.nDTRecSegment4Ds();
    etrk_[0].n_dt_st_seg = match_dtrh.chamberIdsDTRecSegment4D().size();
  }  

  // CSC segments
  for(auto ddt: match_cscrh.chamberIdsCSCSegment())
  {
    const CSCDetId id(ddt);
    const int st(detIdToMEStation(id.station(),id.ring()));
    if (stationscsc_to_use_.count(st) == 0) continue;

    etrk_[0].n_csc_seg =  match_cscrh.nCSCSegments();
    etrk_[0].n_csc_st_seg = match_cscrh.chamberIdsCSCSegment().size();
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
 for (auto stdt: stationsdt_to_use_)
 {
   tree_eff_[stdt]->Fill();
 }
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
  
  sim_pt = -9.;
  sim_pt_inv = -9.;
  sim_eta=-9.;
  sim_phi=-9.;
  sim_dxy = -99;
  eta_gp = -9.;
  eta_gv = -9.;
  phi_gv= -9.;
  pt_gv= -9.;
  z_gp = -9900.;
  deltaphi_h_g = -9.;
  charge_dt = -99;
  
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
  n_dt_seg = -99;
  n_dt_st_sh = -99;
  n_dt_st_seg = -99;
  n_csc_seg = -99;
  n_csc_st_seg = -99;
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

  t->Branch("wheel", &wheel);
  t->Branch("station", &station);

  t->Branch("pt_gv", &pt_gv);
  t->Branch("phi_gv", &phi_gv);
  t->Branch("eta_gp", &eta_gp);
  t->Branch("charge_dt", &charge_dt);
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
  t->Branch("n_csc_st_seg", &n_csc_st_seg);

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
