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

struct MyTrackEffDT
{
  void init();
  
  TTree*book(TTree *t, const std::string & name = "trk_eff_dt_");
  Int_t lumi;
  Int_t run;
  Int_t event;
  Char_t charge_dt;
  
  Float_t deltaphi_dt_rpc_gv;
  Float_t deltaphi_dt_rpc_gp;
  Float_t deltaphi_first_second_gv;
  Float_t deltaphi_first_second_gp;
  Float_t deltaphi_first_third_gv;
  Float_t deltaphi_first_third_gp;
  Float_t deltaphi_first_fourth_gv;
  Float_t deltaphi_first_fourth_gp;
  
  Float_t wheel_second;
  Float_t eta_gv_second;
  Float_t phi_gv_second;
  Float_t eta_gp_second;
  Float_t phi_gp_second;
  
  Float_t wheel_third;
  Float_t eta_gv_third;
  Float_t phi_gv_third;
  Float_t phi_gp_third;
  Float_t eta_gp_third;
  
  Float_t wheel_fourth;
  Float_t eta_gv_fourth;
  Float_t phi_gv_fourth;
  Float_t eta_gp_fourth;
  Float_t phi_gp_fourth;
  
  Char_t has_second_dtst_hit;
  Char_t has_third_dtst_hit;
  Char_t has_fourth_dtst_hit;
  
  Float_t pt_calculated_dt;
  Float_t pt_calculated_dt_12;
  Float_t pt_calculated_dt_14;
  Float_t pt_calculated_dt_13;
  
  Double_t vtx_x;
  Double_t vtx_y;
  Double_t vtx_z;
  Double_t vtx_r;
  Float_t dt_dxy;
  Float_t eta_gp;
  Float_t x_gp;
  Float_t y_gp;
  Float_t z_gp;
  Float_t deltaphi_h_g;
  Float_t deltaphi_t_h;
  Float_t deltaphi_t_g;
  Float_t pt_gv;
  Float_t apt_SimTrack_dt;
  Float_t phi_gv;
  Float_t eta_gv;
  Float_t r_gp;
  Float_t phi_gp;
  
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
  
  Float_t L1_pt;
  Float_t L1_eta;
  Float_t L1_q;
  Float_t L1_phi_;
  Float_t L1_sh_dr;
  Int_t wheel;
  Int_t station;
  Float_t L1_st_dr;
  
  Int_t has_l1_sh_matched;
  Int_t has_l1_st_matched;
  
  Int_t has_l2;
  Float_t L2_pp;
  Float_t L2_pt;
  Float_t L2_eta;
  Float_t L2_q;
  Float_t L2_phi;
  Float_t L2_sh_dr;
  Float_t L2_st_dr;
  
  Float_t Seg_dr_sh;
  Float_t Seg_dr_st;
  Float_t Seg_dr_l2;
  Int_t has_seg_sh_matched;
  Int_t has_seg_st_matched;
  Int_t has_seg_l2_matched;
  Int_t has_DTSegments;
  
  Int_t Seg_wheel;
  Int_t Seg_station;
  Float_t Seg_gp_eta;
  Float_t Seg_gp_phi;
  Float_t Seg_gp_x;
  Float_t Seg_gp_y;
  Float_t Seg_gp_z;
  Float_t Seg_gv_phi;
  Float_t Seg_gv_eta;
  Float_t Seg_deltaphi_12_gv;
  Float_t Seg_deltaphi_14_gv;
  Float_t Seg_deltaphi_13_gv;
  Float_t Seg_deltaphi_23_gv;
  Float_t Seg_deltaphi_24_gv;
  Float_t Seg_deltaphi_34_gv;
  Int_t has_seg_14;
  
  Float_t L2t_wheel;
  Float_t L2t_station;
  Float_t L2t_eta;
  Float_t L2t_phi;
  Float_t L2t_pp;
  Float_t L2t_pt;
  Float_t L2t_q;
  Int_t has_l2t;
  Float_t L2t_st_dr;
  Float_t L2t_sh_dr;
  Int_t has_l2t_sh_matched;
  Int_t has_l2t_st_matched;
    
  Int_t has_l2_sh_matched;
  Int_t has_l2_st_matched;

  Int_t has_dt_seg;
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
  Int_t n_dt_seg;
  Int_t n_dt_st_sh; // number of dt stations with at least 3 layers
};


class HLTBendingAngle : public edm::EDAnalyzer 
{
public:
  explicit HLTBendingAngle(const edm::ParameterSet&);
  ~HLTBendingAngle();
  
  virtual void analyze(const edm::Event&, const edm::EventSetup&) ;
  
  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
  
private:
  
  void analyzeTrackEfficiency(SimTrackMatchManager& match, int trk_no);

  bool isSimTrackGood(const SimTrack &t);
  
  int detIdToMBStation(int wh, int st);
  std::vector<string> dtStations_;
  std::set<int> stationsdt_to_use_;
  
  TTree *tree_eff_dt_[56];
  MyTrackEffDT etrk_dt_[56];
  
  float deltaR;
  int does_it_match;

  edm::ParameterSet cfg_;
  int verbose_;
  int verboseSimTrack_;
  edm::InputTag simInputLabel_;
  double simTrackMinPt_;
  double simTrackMinEta_;
  double simTrackMaxEta_;
  double simTrackOnlyMuon_;
  std::vector<std::pair<int,int> > dtStationsCo_;
};

HLTBendingAngle::HLTBendingAngle(const edm::ParameterSet& ps)
  : cfg_(ps.getParameterSet("simTrackMatching"))
  , verbose_(ps.getUntrackedParameter<int>("verbose", 0))
{
  auto simTrack = cfg_.getParameter<edm::ParameterSet>("simTrack");
  verboseSimTrack_ = simTrack.getParameter<int>("verbose");
  simInputLabel_ = edm::InputTag("g4SimHits");
  simTrackMinPt_ = simTrack.getParameter<double>("minPt");
  simTrackMinEta_ = simTrack.getParameter<double>("minEta");
  simTrackMaxEta_ = simTrack.getParameter<double>("maxEta");
  simTrackOnlyMuon_ = simTrack.getParameter<bool>("onlyMuon");

  // auto input = cms.InputTag("g4SimHits","MuonDTHits");
  std::vector<string> stationsDT; 
  stationsDT.push_back("ALL");
  stationsDT.push_back("MB01");
  stationsDT.push_back("MB11");
  stationsDT.push_back("MB21");
  stationsDT.push_back("MB02");
  stationsDT.push_back("MB12");
  stationsDT.push_back("MB22");
  stationsDT.push_back("MB03");
  stationsDT.push_back("MB13");
  stationsDT.push_back("MB23");
  stationsDT.push_back("MB04");
  stationsDT.push_back("MB14");
  stationsDT.push_back("MB24");
  stationsDT.push_back("MB11n");
  stationsDT.push_back("MB21n");
  stationsDT.push_back("MB12n");
  stationsDT.push_back("MB22n");
  stationsDT.push_back("MB13n");
  stationsDT.push_back("MB23n");
  stationsDT.push_back("MB14n");
  stationsDT.push_back("MB24n");
  stationsDT.push_back("STMB2");  

  std::vector<int> DtStationsToUse;
  DtStationsToUse.push_back(0);
  DtStationsToUse.push_back(1);
  DtStationsToUse.push_back(2);
  DtStationsToUse.push_back(3);
  DtStationsToUse.push_back(4);
  DtStationsToUse.push_back(5);
  DtStationsToUse.push_back(6);
  DtStationsToUse.push_back(7);
  DtStationsToUse.push_back(8);
  DtStationsToUse.push_back(9);
  DtStationsToUse.push_back(10);
  DtStationsToUse.push_back(11);
  DtStationsToUse.push_back(12);
  DtStationsToUse.push_back(13);
  DtStationsToUse.push_back(14);
  DtStationsToUse.push_back(15);
  DtStationsToUse.push_back(16);
  DtStationsToUse.push_back(17);
  DtStationsToUse.push_back(18);
  DtStationsToUse.push_back(19);
  DtStationsToUse.push_back(20);
  DtStationsToUse.push_back(21);

  copy(DtStationsToUse.begin(),DtStationsToUse.end(),inserter(stationsdt_to_use_,stationsdt_to_use_.end()));
  for (auto m: stationsdt_to_use_)
  {
    stringstream ss;
    ss<< "trk_eff_dt_" << stationsDT[m];
    tree_eff_dt_[m] = etrk_dt_[m].book(tree_eff_dt_[m], ss.str());    
  }
  
  dtStationsCo_.push_back(std::make_pair(-99,-99));
  dtStationsCo_.push_back(std::make_pair(0,1));
  dtStationsCo_.push_back(std::make_pair(1,1));
  dtStationsCo_.push_back(std::make_pair(2,1));
  dtStationsCo_.push_back(std::make_pair(0,2));
  dtStationsCo_.push_back(std::make_pair(1,2));
  dtStationsCo_.push_back(std::make_pair(2,2));
  dtStationsCo_.push_back(std::make_pair(0,3));
  dtStationsCo_.push_back(std::make_pair(1,3));
  dtStationsCo_.push_back(std::make_pair(2,3));
  dtStationsCo_.push_back(std::make_pair(0,4));
  dtStationsCo_.push_back(std::make_pair(1,4));
  dtStationsCo_.push_back(std::make_pair(2,4));
  dtStationsCo_.push_back(std::make_pair(-1,1));
  dtStationsCo_.push_back(std::make_pair(-2,1));
  dtStationsCo_.push_back(std::make_pair(-1,2));
  dtStationsCo_.push_back(std::make_pair(-2,2));
  dtStationsCo_.push_back(std::make_pair(-1,3));
  dtStationsCo_.push_back(std::make_pair(-2,3));
  dtStationsCo_.push_back(std::make_pair(-1,4));
  dtStationsCo_.push_back(std::make_pair(-2,4));
};

int HLTBendingAngle::detIdToMBStation(int wh,  int st)
{
  auto p(std::make_pair(wh, st));
  return std::find(dtStationsCo_.begin(), dtStationsCo_.end(),p) - dtStationsCo_.begin();
};

HLTBendingAngle::~HLTBendingAngle()
{
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
  }
}

void 
HLTBendingAngle::analyzeTrackEfficiency(SimTrackMatchManager& match, int trk_no)
{
  const SimHitMatcher& match_sh = match.simhits();
  const DTRecHitMatcher& match_dt = match.dtRecHits();
  const HLTTrackMatcher& match_hlt_track = match.hltTracks();
  const SimTrack& t = match_sh.trk();
  const SimVertex& vtx = match_sh.vtx();

  // information for each chamber
  for (auto st: stationsdt_to_use_)
  {
    etrk_dt_[st].init();
    etrk_dt_[st].run = match_sh.event().id().run();
    etrk_dt_[st].lumi = match_sh.event().id().luminosityBlock();
    etrk_dt_[st].event = match_sh.event().id().event();
    etrk_dt_[st].charge_dt = t.charge();

    const double vtx_x = match_sh.vtx().position().x();
    const double vtx_y = match_sh.vtx().position().y();
    const double vtx_z = match_sh.vtx().position().z();
  
    etrk_dt_[st].vtx_x = vtx_x;
    etrk_dt_[st].vtx_y = vtx_y;
    etrk_dt_[st].vtx_z = vtx_z;
    etrk_dt_[st].vtx_r = sqrt(vtx_x*vtx_x + vtx_y*vtx_y);

    etrk_dt_[st].sim_pt = t.momentum().pt(); 
    etrk_dt_[st].sim_pt_inv = 1./t.momentum().pt(); 
    etrk_dt_[st].sim_dxy = (- vtx.position().x() * t.momentum().py() + vtx.position().y() * t.momentum().px() ) / t.momentum().pt();
    etrk_dt_[st].sim_eta = t.momentum().eta();
    etrk_dt_[st].sim_phi = t.momentum().phi();
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

    etrk_dt_[stdt].nslayerdt  = nsl;
    etrk_dt_[stdt].nlayerdt  = nl;
    etrk_dt_[stdt].has_dt_sh = 1;
    etrk_dt_[0].has_dt_sh = 1;
    etrk_dt_[0].n_dt_st_sh = match_sh.chamberIdsDT().size();

    etrk_dt_[stdt].wheel = id.wheel();
    etrk_dt_[stdt].station = id.station();

    const GlobalPoint hitGp(match_sh.simHitsMeanPosition(match_sh.hitsInChamber(ddt)));
    etrk_dt_[stdt].eta_gp = hitGp.eta();
    etrk_dt_[stdt].x_gp = hitGp.x();
    etrk_dt_[stdt].y_gp = hitGp.y();
    etrk_dt_[stdt].z_gp = hitGp.z();
    etrk_dt_[stdt].r_gp = hitGp.perp();
    etrk_dt_[stdt].phi_gp = hitGp.phi();

    const GlobalVector ym(match_sh.simHitsMeanMomentum(match_sh.hitsInChamber(ddt)));
    etrk_dt_[stdt].eta_gv = ym.eta();
    etrk_dt_[stdt].pt_gv = ym.perp();
    etrk_dt_[stdt].phi_gv = ym.phi();
    etrk_dt_[stdt].R_gv = sqrt (ym.x()*ym.x()+ym.y()*ym.y());
    etrk_dt_[stdt].Z_gv = ym.z();
    etrk_dt_[stdt].X_gv = ym.x();
    etrk_dt_[stdt].Y_gv = ym.y();
    etrk_dt_[stdt].deltaphi_h_g = reco::deltaPhi(hitGp.phi(), ym.phi());     //This one
    // etrk_dt_[stdt].pt_calculated_dt = (1/(hitGp.phi() - ym.phi()))*1.4025845 + 0.674463;
  } 

  // segments
  for(auto ddt: match_dt.chamberIdsDTRecSegment4D())
  {
    const DTChamberId id(ddt);
    const int stdt(detIdToMBStation(id.wheel(),id.station()));
    if (stationsdt_to_use_.count(stdt) == 0) continue;

    // require at least 3 layers hit per chamber
    const int nl(match_sh.nLayersWithHitsInChamberDT(id.rawId()));
    if (nl<3) continue;

    etrk_dt_[stdt].has_dt_seg = 1;
    etrk_dt_[0].has_dt_seg = 1;
    // store total number of segments
    etrk_dt_[0].n_dt_seg =  match_dt.nDTRecSegment4Ds();
  }  

  // RecoTrackExtra
  auto recoTrackExtras(match_hlt_track.getMatchedRecoTrackExtras());
  if (recoTrackExtras.size()) {
    if (verbose_) std::cout << "Number of matched RecoTrackExtras: " << recoTrackExtras.size() << std::endl;
    etrk_dt_[0].has_recoTrackExtra = 1;

    auto recoTrackExtra(recoTrackExtras[0]);
    etrk_dt_[0].recoTrackExtra_pt_inner = recoTrackExtra.innerMomentum().Rho();
    etrk_dt_[0].recoTrackExtra_eta_inner = recoTrackExtra.innerPosition().eta();
    etrk_dt_[0].recoTrackExtra_phi_inner = recoTrackExtra.innerPosition().phi();

    etrk_dt_[0].recoTrackExtra_pt_outer = recoTrackExtra.outerMomentum().Rho();
    etrk_dt_[0].recoTrackExtra_eta_outer = recoTrackExtra.outerPosition().eta();
    etrk_dt_[0].recoTrackExtra_phi_outer = recoTrackExtra.outerPosition().phi();
  }

  // RecoTrack
  auto recoTracks(match_hlt_track.getMatchedRecoTracks());
  if (match_hlt_track.getMatchedRecoTracks().size()) {
    if (verbose_) std::cout << "Number of matched RecoTracks: " << recoTracks.size() << std::endl;
    etrk_dt_[0].has_recoTrack = 1;

    auto recoTrack(recoTracks[0]);
    etrk_dt_[0].recoTrack_pt_outer = recoTrack.outerPt();
    etrk_dt_[0].recoTrack_eta_outer = recoTrack.outerEta();
    etrk_dt_[0].recoTrack_phi_outer = recoTrack.outerPhi();
  }

  // RecoChargedCandidate
  auto recoChargedCandidates(match_hlt_track.getMatchedRecoChargedCandidates());
  if (recoChargedCandidates.size()) {
    if (verbose_) std::cout << "Number of matched RecoChargedCandidates: " << recoChargedCandidates.size() << std::endl;
    etrk_dt_[0].has_recoChargedCandidate = 1;

    auto recoChargedCandidate(recoChargedCandidates[0]);
    etrk_dt_[0].recoChargedCandidate_pt = recoChargedCandidate.pt();
    etrk_dt_[0].recoChargedCandidate_eta = recoChargedCandidate.eta();
    etrk_dt_[0].recoChargedCandidate_phi = recoChargedCandidate.phi();
  }

  // fill the tree for every simtrack 
 for (auto stdt: stationsdt_to_use_)
 {
   tree_eff_dt_[stdt]->Fill();
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

void MyTrackEffDT::init()
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
  apt_SimTrack_dt=-999;
  charge_dt = -99;
  
  Seg_dr_sh = -9.;
  Seg_dr_st = -9.;
  Seg_dr_l2 = -9.;
  has_seg_sh_matched = 0;
  has_seg_st_matched = 0;
  has_seg_l2_matched = 0;
  has_DTSegments = 0;
  
  Seg_wheel = - 9;
  Seg_station = - 9;
  Seg_gp_eta = - 99.;
  Seg_gp_phi = - 99.;
  Seg_gp_x = - 9999.;
  Seg_gp_y = - 9999.;
  Seg_gp_z = - 9999.;
  Seg_gv_phi = - 99.;
  Seg_gv_eta = - 99.;
  Seg_deltaphi_12_gv = - 99.;
  Seg_deltaphi_13_gv = - 99.;
  Seg_deltaphi_14_gv = - 99.;
  Seg_deltaphi_23_gv = - 99.;
  Seg_deltaphi_24_gv = - 99.;
  Seg_deltaphi_34_gv = - 99.;
  has_seg_14 = 0;
  
  L2t_eta = -99.;
  L2t_phi = - 99.;
  L2t_pp = - 99.;
  L2t_pt = - 99.;
  L2t_q = 0;
  has_l2t = 0;
  L2t_st_dr = 99.;
  L2t_sh_dr = 99;
  has_l2t_sh_matched = 0;
  has_l2t_st_matched = 0;
  L2t_wheel = -9;
  L2t_station = -9.;
  
  deltaphi_first_second_gv=-99.;
  deltaphi_first_second_gp=-99.;
  deltaphi_first_third_gv=-99.;
  deltaphi_first_third_gp=-99.;
  deltaphi_first_fourth_gv=-99.;
  deltaphi_first_fourth_gp=-99.;
  has_second_dtst_hit=0;
  has_third_dtst_hit=0;
  has_fourth_dtst_hit=0;
  
  wheel_second = -99;
  phi_gp_second= - 99.;
  eta_gp_second = - 99.;
  phi_gv_second = - 99.;
  eta_gv_second = - 99.;
  
  wheel_third = -99.;
  phi_gp_third =  - 99.;
  eta_gp_third = -99.;
  phi_gv_third = - 99.;
  eta_gv_third = - 99.;
  
  wheel_fourth = -99.;
  phi_gp_fourth = - 9999.;
  eta_gp_fourth = -99.;
  phi_gv_fourth = - 9999.;
  eta_gv_fourth = -99.;
  
  pt_calculated_dt= -9;
  pt_calculated_dt_12=-9;
  pt_calculated_dt_13=-9;
  pt_calculated_dt_14=9;
  x_gp = -9900.;
  y_gp = -9900.;
  r_gp = -9900.;
  phi_gp = -99;
  dt_dxy = -9999;
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
  L1_pt = - 99.;
  L1_eta = - 9.;
  L1_q = - 9.;
  L1_phi_ = -99.;
  L1_sh_dr = - 99.;
  L1_st_dr = - 99.;
  has_l1_sh_matched = 0;
  has_l1_st_matched = 0;
  
  has_l2 = 0;
  L2_pp = - 99.;
  L2_pt = - 99.;
  L2_eta = - 9.;
  L2_q = - 9.;
  L2_phi = -99.;
  L2_sh_dr = - 99.;
  L2_st_dr = - 99.;
  
  has_l2_sh_matched = 0;
  has_l2_st_matched = 0;
  
  has_dt_seg = 0;
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
}

TTree*MyTrackEffDT::book(TTree *t,const std::string & name)
{
  edm::Service< TFileService > fs;
  t = fs->make<TTree>(name.c_str(),name.c_str());
  t->Branch("L1_st_dr", &L1_st_dr);
  t->Branch("L1_sh_dr", &L1_sh_dr);
  t->Branch("L1_pt", &L1_pt);
  t->Branch("L1_eta", &L1_eta);
  t->Branch("L1_q", &L1_q);
  t->Branch("L1_phi_", &L1_phi_);


  t->Branch("Seg_dr_sh", &Seg_dr_sh);
  t->Branch("Seg_dr_st", &Seg_dr_st);
  t->Branch("Seg_dr_l2", &Seg_dr_l2);
  t->Branch("has_seg_sh_matched", &has_seg_sh_matched);
  t->Branch("has_seg_st_matched", &has_seg_st_matched);
  t->Branch("has_seg_l2_matched", &has_seg_l2_matched);
  t->Branch("has_DTSegments", &has_DTSegments);

  t->Branch("Seg_wheel", &Seg_wheel);
  t->Branch("Seg_station", & Seg_station);
  t->Branch("Seg_gp_eta", &Seg_gp_eta);
  t->Branch("Seg_gp_phi", &Seg_gp_phi);
  t->Branch("Seg_gp_x", &Seg_gp_x);
  t->Branch("Seg_gp_y", &Seg_gp_y);
  t->Branch("Seg_gp_z", &Seg_gp_z);
  t->Branch("Seg_gv_phi", &Seg_gv_phi);
  t->Branch("Seg_gv_eta", &Seg_gv_eta);
  t->Branch("Seg_deltaphi_12_gv", &Seg_deltaphi_12_gv);
  t->Branch("Seg_deltaphi_13_gv", &Seg_deltaphi_13_gv);
  t->Branch("Seg_deltaphi_14_gv", &Seg_deltaphi_14_gv);
  t->Branch("Seg_deltaphi_23_gv", &Seg_deltaphi_23_gv);
  t->Branch("Seg_deltaphi_24_gv", &Seg_deltaphi_24_gv);
  t->Branch("Seg_deltaphi_34_gv", &Seg_deltaphi_34_gv);
  t->Branch("has_seg_14", &has_seg_14);

  t->Branch("has_l2", &has_l2);
  t->Branch("L2_pp", &L2_pp);
  t->Branch("L2_st_dr", &L2_st_dr);
  t->Branch("L2_sh_dr", &L2_sh_dr);
  t->Branch("L2_pt", &L2_pt);
  t->Branch("L2_eta", &L2_eta);
  t->Branch("L2_q", &L2_q);
  t->Branch("L2_phi", &L2_phi);

  t->Branch("L2t_eta", &L2t_eta);
  t->Branch("L2t_phi", &L2t_phi);
  t->Branch("L2t_pp", &L2t_pp);
  t->Branch("L2t_pt", &L2t_pt);
  t->Branch("L2t_q", &L2t_q);
  t->Branch("has_l2t", &has_l2t);
  t->Branch("L2t_st_dr", &L2t_st_dr);
  t->Branch("L2t_sh_dr", &L2t_sh_dr);
  t->Branch("has_l2t_sh_matched", &has_l2t_sh_matched);
  t->Branch("has_l2t_st_matched", &has_l2t_st_matched);
  t->Branch("L2t_wheel", &L2t_wheel);
  t->Branch("L2t_station", &L2t_station);

  t->Branch("lumi", &lumi);
  t->Branch("run", &run);
  t->Branch("event", &event);
  t->Branch("sim_eta", &sim_eta);
  t->Branch("sim_pt", &sim_pt);
  t->Branch("sim_pt_inv", &sim_pt_inv);
  t->Branch("eta_gv", &eta_gv);


  t->Branch("deltaphi_first_second_gv", &deltaphi_first_second_gv);
  t->Branch("deltaphi_first_second_gp", &deltaphi_first_second_gp);
  t->Branch("deltaphi_first_third_gv", &deltaphi_first_third_gv);
  t->Branch("deltaphi_first_third_gp", &deltaphi_first_third_gp);
  t->Branch("deltaphi_first_fourth_gv", &deltaphi_first_fourth_gv);
  t->Branch("deltaphi_first_fourth_gp", &deltaphi_first_fourth_gp);

  t->Branch("has_second_dtst_hit", &has_second_dtst_hit);
  t->Branch("has_third_dtst_hit", &has_third_dtst_hit);
  t->Branch("has_fourth_dtst_hit", &has_fourth_dtst_hit);

  t->Branch("wheel", &wheel);
  t->Branch("station", &station);
  t->Branch("wheel_second", &wheel_second);
  t->Branch("eta_gv_second", &eta_gv_second);
  t->Branch("eta_gp_second", &eta_gp_second);
  t->Branch("phi_gv_second", &phi_gv_second);
  t->Branch("eta_gv_second", &eta_gv_second);

  t->Branch("wheel_third", &wheel_third);
  t->Branch("eta_gv_third", &eta_gv_third);
  t->Branch("eta_gp_third", &eta_gp_third);
  t->Branch("phi_gv_third", &phi_gv_third);
  t->Branch("eta_gv_third", &eta_gv_third);

  t->Branch("wheel_fourth", &wheel_fourth);
  t->Branch("eta_gv_fourth", &eta_gv_fourth);
  t->Branch("eta_gp_fourth", &eta_gp_fourth);
  t->Branch("phi_gv_fourth", &phi_gv_fourth);
  t->Branch("eta_gv_fourth", &eta_gv_fourth);


  t->Branch("pt_calculated_dt", &pt_calculated_dt);
  t->Branch("pt_calculated_dt_12", &pt_calculated_dt_12);
  t->Branch("pt_calculated_dt_13", &pt_calculated_dt_13);
  t->Branch("pt_calculated_dt_14", &pt_calculated_dt_14);

  t->Branch("pt_gv", &pt_gv);
  t->Branch("phi_gv", &phi_gv);
  t->Branch("eta_gp", &eta_gp);
  t->Branch("apt_SimTrack_dt", &apt_SimTrack_dt);
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
  t->Branch("has_dt_sh", &has_dt_sh);
  t->Branch("nlayerdt", &nlayerdt);
  t->Branch("nslayerdt", &nslayerdt);
  t->Branch("R_gv", &R_gv);
  t->Branch("Z_gv", &Z_gv);
  t->Branch("X_gv", &X_gv);
  t->Branch("Y_gv", &Y_gv);
  t->Branch("dt_dxy", &dt_dxy);

  t->Branch("has_l1_st_matched", &has_l1_st_matched);
  t->Branch("has_l2_st_matched", &has_l2_st_matched);

  t->Branch("has_l1_sh_matched", &has_l1_sh_matched);
  t->Branch("has_l2_sh_matched", &has_l2_sh_matched);

  t->Branch("has_dt_seg", &has_dt_seg);
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
  t->Branch("n_dt_seg", &n_dt_seg);
  t->Branch("n_dt_st_sh", &n_dt_st_sh);

  return t;
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
