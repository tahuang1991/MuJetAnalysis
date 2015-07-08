#include <memory>
#include "TTree.h"
#include <iomanip>
#include <sstream>
#include <vector>

#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "TrackingTools/TrajectoryState/interface/TrajectoryStateOnSurface.h"
#include "TrackingTools/Records/interface/TrackingComponentsRecord.h"
#include "MagneticField/Records/interface/IdealMagneticFieldRecord.h"
#include "DataFormats/GeometrySurface/interface/Plane.h"
#include "SimDataFormats/TrackingHit/interface/PSimHitContainer.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include <SimDataFormats/Track/interface/SimTrackContainer.h>
#include <SimDataFormats/Vertex/interface/SimVertexContainer.h>
#include <FWCore/Framework/interface/EventSetupRecord.h>
#include "MagneticField/Engine/interface/MagneticField.h"
#include <DataFormats/DetId/interface/DetId.h>
#include "DataFormats/MuonDetId/interface/DTWireId.h"
#include "DataFormats/MuonDetId/interface/MuonSubdetId.h"
#include "DataFormats/GeometryVector/interface/GlobalPoint.h"
#include "FWCore/Framework/interface/EventSetupRecordImplementation.h"
#include "FWCore/Framework/interface/eventsetuprecord_registration_macro.h"
#include "DataFormats/L1Trigger/interface/L1MuonParticle.h"
#include "MuonAnalysis/MuonAssociators/interface/L1MuonMatcherAlgo.h"
#include "MuonAnalysis/MuonAssociators/interface/PropagateToMuon.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "GEMCode/GEMValidation/interface/SimTrackMatchManager.h"
#include "DataFormats/MuonReco/interface/Muon.h"
#include "DataFormats/RecoCandidate/interface/RecoCandidate.h"
#include "DataFormats/RecoCandidate/interface/RecoChargedCandidate.h"
#include "DataFormats/RecoCandidate/interface/RecoChargedCandidateFwd.h"
#include <DataFormats/TrackReco/interface/TrackExtra.h>


using namespace std;

struct MyTrackEffL1
{
 void init();
 TTree*book(TTree *t, const std::string & name = "l1_particles_");

 Float_t L1_pt;
 Float_t L1_eta;
 Float_t L1_phi;
 Float_t L1_charge;
};

struct MyTrackEffCSC
{
 void init();
 TTree*book(TTree *t, const std::string & name = "trk_eff_csc_");
 
 Int_t lumi;
 Int_t run;
 Float_t eta_SimTrack_csc;
 Float_t phi_SimTrack_csc;
 Float_t pt_SimTrack_csc;
 Float_t vertex_x;
 Float_t vertex_y;
 Float_t vertex_z;
 Float_t dxy_csc; 
 Int_t csc_station;
 Int_t csc_ring;
 
 Float_t p_SimTrack_csc;
 Float_t p_c_SimTrack_csc;
 Float_t charge_csc;

 Float_t csc_gv_eta;
 Float_t csc_gv_phi;
 Float_t csc_gv_pt;
 Float_t csc_gp_r;
 Float_t csc_gp_x;
 Float_t csc_gp_y;
 Float_t csc_gp_z;
 Float_t csc_gp_eta;
 Float_t csc_gp_phi;
 Int_t nlayerscsc;
 Float_t csc_deltaphi_gp;
 Float_t csc_deltaphi;
 Float_t csc_deltaphi_second;

 Float_t csc_bending_angle;
 Float_t csc_bending_angle_12;
 Float_t csc_bending_angle_13;
 Float_t csc_bending_angle_14;
 
 Float_t csc_q_1bending_angle;
 Float_t csc_q_1bending_angle_12;
 Float_t csc_q_1bending_angle_13;
 Float_t csc_q_1bending_angle_14;
 Float_t csc_deltaeta;
 Float_t csc_deltaeta_14;
 Float_t csc_deltaeta_13;
 Float_t csc_deltaeta_12;
 Int_t has_csc_12;
 Int_t has_csc_13;
 Int_t has_csc_14;
 Float_t csc_second_gp_x;
 Float_t csc_second_gp_y;
 Float_t csc_second_gp_z;
 Float_t csc_second_gp_eta;
 Float_t csc_second_gp_phi;
 Float_t csc_second_gv_phi;
 Float_t csc_second_gv_eta;
 Float_t csc_second_gv_pt;
 Int_t csc_second_station;
 Int_t csc_second_ring;
 Int_t csc_second_nlayers;


};

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

 Double_t dtvertex_x;
 Double_t dtvertex_y;
 Double_t dtvertex_z;
 Double_t dtvertex_r;
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

 Float_t pt_SimTrack_dt;
 Float_t eta_SimTrack_dt;
 Float_t phi_SimTrack_dt;
 Char_t has_dt_sh;
 Float_t R_gv;
 Int_t nlayerdt;
 Int_t nslayerdt;
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

 Float_t Seg_dphi_sh;
 Float_t Seg_deta_sh;

 Float_t Seg_dr_sh;
 Float_t Seg_dr_st;
 Float_t Seg_dr_l2;
 Int_t has_seg_sh_matched;
 Int_t has_seg_st_matched;
 Int_t has_seg_l2_matched;
 Int_t has_DTSegments;

 Int_t Seg_second_wheel;
 Int_t Seg_second_station;
 Float_t Seg_second_gp_eta;
 Float_t Seg_second_gp_phi;
 Float_t Seg_second_gp_z;
 Float_t Seg_second_gp_y;
 Float_t Seg_second_gp_x;
 Float_t Seg_second_gv_eta;
 Float_t Seg_second_gv_phi;
 Float_t Seg_second_sh_dr;
 Int_t Seg_second_st; //1-4 depending on the station;

 Int_t has_eta_phi_dr;
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
 Int_t has_second_segment_matched;
 Int_t has_seg_13;
 Int_t has_seg_12;
 Int_t has_seg_23;
 Int_t has_seg_24;
 Int_t has_seg_34;
 Int_t has_second_dtSegment;
 Float_t Seg_deltaphi_gv;

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
  //, edm::Handle<std::vector<l1extra::L1MuonParticle> > l1p, edm::Handle<std::vector<reco::RecoChargedCandidate> > hlt_l2_pp, edm::Handle<std::vector<reco::TrackExtra> > l2_track, edm::Handle<edm::RangeMap<DTChamberId,edm::OwnVector<DTRecSegment4D,edm::ClonePolicy<DTRecSegment4D> >,edm::ClonePolicy<DTRecSegment4D> > > SegmentsDT);

  bool isSimTrackGood(const SimTrack &t);
  int detIdToMEStation(int st, int ri);
  int detIdToMBStation(int wh, int st);
  std::vector<string> dtStations_;
  std::set<int> stationsdt_to_use_;
  std::set<int> stationscsc_to_use_;
  std::set<int> l1particles_muons_;
  
  TTree *tree_eff_dt_[56];
  MyTrackEffDT etrk_dt_[56];
  
  TTree *tree_eff_csc_[56];
  MyTrackEffCSC etrk_csc_[56];

  TTree *tree_eff_l1_[6];
  MyTrackEffL1 etrk_l1_[6];
  float deltaR;
  int does_it_match;

  double vtx_dt;
  double vty_dt;
  double vtz_dt;
  
  edm::ParameterSet cfg_;
  int verbose_;
  int verboseSimTrack_;
  edm::InputTag simInputLabel_;
  double simTrackMinPt_;
  double simTrackMinEta_;
  double simTrackMaxEta_;
  double simTrackOnlyMuon_;
  std::vector<std::pair<int,int> > dtStationsCo_;
  std::vector<std::pair<int,int> > cscStationsCo_;
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


  std::vector<string> stationsCSC;
  stationsCSC.push_back("ALL");
  stationsCSC.push_back("ME11");
  stationsCSC.push_back("ME11a");
  stationsCSC.push_back("ME11b");
  stationsCSC.push_back("ME12");
  stationsCSC.push_back("ME13");
  stationsCSC.push_back("ME21");
  stationsCSC.push_back("ME22");
  stationsCSC.push_back("ME31");
  stationsCSC.push_back("ME32");
  stationsCSC.push_back("ME41");
  stationsCSC.push_back("ME42");
  stationsCSC.push_back("ME1");

  std::vector<int> CSCStationsToUse;
  CSCStationsToUse.push_back(0);  // ALL
  CSCStationsToUse.push_back(1);  // ME11
  CSCStationsToUse.push_back(2);  // ME11a
  CSCStationsToUse.push_back(3);  // ME11b
  CSCStationsToUse.push_back(4);  // ME12
  CSCStationsToUse.push_back(5);  // ME13
  CSCStationsToUse.push_back(6);  // ME21
  CSCStationsToUse.push_back(7);  // ME22
  CSCStationsToUse.push_back(8);  // ME31
  CSCStationsToUse.push_back(9);  // ME32
  CSCStationsToUse.push_back(10);  // ME41
  CSCStationsToUse.push_back(11);  // ME42
  CSCStationsToUse.push_back(12);  // ME1 only

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

  std::vector<string> L1Ppabc;
  L1Ppabc.push_back("Muon1");
  L1Ppabc.push_back("Muon2");
  L1Ppabc.push_back("Muon3");
  L1Ppabc.push_back("Muon4");
  L1Ppabc.push_back("Muon5");
  L1Ppabc.push_back("Muon6");
  L1Ppabc.push_back("Muon7");
  L1Ppabc.push_back("Muon8");
  L1Ppabc.push_back("Muon9");
  L1Ppabc.push_back("Muon10");
  
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

  std::vector<int> L1Particles;
  L1Particles.push_back(0);
  L1Particles.push_back(1);
  L1Particles.push_back(2);
  L1Particles.push_back(4);
  L1Particles.push_back(5);
  L1Particles.push_back(6);
  L1Particles.push_back(7);
  L1Particles.push_back(8);
  L1Particles.push_back(9);

  copy(L1Particles.begin(), L1Particles.end(), inserter(l1particles_muons_, l1particles_muons_.end()));
  for(auto m: l1particles_muons_)
  {
    stringstream ss;
    ss<<" trk_eff_l1_"<< L1Ppabc[m];
    tree_eff_l1_[m] = etrk_l1_[m].book(tree_eff_l1_[m], ss.str());    
  }

  copy(DtStationsToUse.begin(),DtStationsToUse.end(),inserter(stationsdt_to_use_,stationsdt_to_use_.end()));
  for (auto m: stationsdt_to_use_)
  {
    stringstream ss;
    ss<< "trk_eff_dt_" << stationsDT[m];
    tree_eff_dt_[m] = etrk_dt_[m].book(tree_eff_dt_[m], ss.str());    
  }

  copy(CSCStationsToUse.begin(),CSCStationsToUse.end(), inserter(stationscsc_to_use_, stationscsc_to_use_.end()));
  for (auto m: stationscsc_to_use_)
  {
    stringstream ss;
    ss<< "trk_eff_csc_" << stationsCSC[m];
    tree_eff_csc_[m] = etrk_csc_[m].book(tree_eff_csc_[m], ss.str());

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

};


int HLTBendingAngle::detIdToMEStation(int st, int ri)
{
  auto p(std::make_pair(st, ri));
  return std::find(cscStationsCo_.begin(), cscStationsCo_.end(), p) - cscStationsCo_.begin();
}

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

   if (verboseSimTrack_){
    // std::cout << "Total number of SimTracks in this event: " << sim_track.size() << std::endl;   
    // std::cout << "Total number of SimVertexs in this event: " << sim_vert.size() << std::endl;
   }
   
   //edm::Handle<std::vector<l1extra::L1MuonParticle> > l1_particles;
   //ev.getByLabel("hltL1extraParticles", l1_particles);


   //edm::Handle<std::vector<reco::TrackExtra> > l2_track;
   //ev.getByLabel("hltL2Muons", l2_track);


   //edm::Handle<std::vector<reco::RecoChargedCandidate> > hlt_l2_pp;
   //ev.getByLabel("hltL2MuonCandidatesNoVtx", hlt_l2_pp);


   //edm::Handle<edm::RangeMap<DTChamberId,edm::OwnVector<DTRecSegment4D,edm::ClonePolicy<DTRecSegment4D> >,edm::ClonePolicy<DTRecSegment4D> > > SegmentsDT;
   //ev.getByLabel("hltDt4DSegments", SegmentsDT);

   int trk_no=0;
   for (auto& t: *sim_tracks.product()) {
     if(!isSimTrackGood(t)) continue;
     if (verboseSimTrack_) {
      // std::cout << "Processing SimTrack " << trk_no + 1 << std::endl;      
      // std::cout << "pt(GeV/c) = " << t.momentum().pt() << ", eta = " << t.momentum().eta()  
      //           << ", phi = " << t.momentum().phi() << ", Q = " << t.charge()
      //           << ", vtxIndex = " << t.vertIndex() << std::endl;
     }

     vtx_dt = sim_vert[t.vertIndex()].position().x();
     vty_dt = sim_vert[t.vertIndex()].position().y();
     vtz_dt = sim_vert[t.vertIndex()].position().z();

     SimTrackMatchManager match(t, sim_vert[t.vertIndex()], cfg_, ev, es);
     analyzeTrackEfficiency(match, trk_no);
    //a, l1_particles, hlt_l2_pp, l2_track, SegmentsDT);

    trk_no = trk_no + 1;
  }
}

void 
HLTBendingAngle::analyzeTrackEfficiency(SimTrackMatchManager& match, int trk_no)
{
  const SimHitMatcher& match_sh = match.simhits();
  //const TrackMatcher& match_track = match.tracks();
  const SimTrack &t = match_sh.trk();
  //const SimVertex &vtx = match_sh.vtx();


  for(auto st: stationscsc_to_use_)
  {
    etrk_csc_[st].init();
    etrk_csc_[st].run = match.simhits().event().id().run();
    etrk_csc_[st].lumi = match.simhits().event().id().luminosityBlock();

    etrk_csc_[st].pt_SimTrack_csc = t.momentum().pt();
    etrk_csc_[st].phi_SimTrack_csc = t.momentum().phi();
    etrk_csc_[st].eta_SimTrack_csc = t.momentum().eta();
    etrk_csc_[st].vertex_x = vtx_dt;
    etrk_csc_[st].vertex_y = vty_dt;
    etrk_csc_[st].vertex_z = vtz_dt;
    
    auto pphi = t.momentum().phi();
    etrk_csc_[st].dxy_csc = vtx_dt*sin(pphi) - vty_dt*cos(pphi);


    auto totalp = std::sqrt( t.momentum().x()*t.momentum().x() + t.momentum().y()*t.momentum().y() + t.momentum().z()*t.momentum().z());

    etrk_csc_[st].p_SimTrack_csc = totalp;
    etrk_csc_[st].charge_csc = t.charge();
    etrk_csc_[st]. p_c_SimTrack_csc = totalp*t.charge();


    //std::cout<<" dxy value for csc: "<<vtx_dt*sin(pphi) - vty_dt*cos(pphi)<<std::endl;
    //std::cout<<" p SimTrack : "<<totalp<<" p SimTrack * charge "<<totalp*t.charge()<<std::endl;

  }


  // Station 1 case
    etrk_csc_[12].init();
    etrk_csc_[12].run = match.simhits().event().id().run();
    etrk_csc_[12].lumi = match.simhits().event().id().luminosityBlock();

    etrk_csc_[12].pt_SimTrack_csc = t.momentum().pt();
    etrk_csc_[12].phi_SimTrack_csc = t.momentum().phi();
    etrk_csc_[12].eta_SimTrack_csc = t.momentum().eta();
    etrk_csc_[12].vertex_x = vtx_dt;
    etrk_csc_[12].vertex_y = vty_dt;
    etrk_csc_[12].vertex_z = vtz_dt;

    auto pphi = t.momentum().phi();
    etrk_csc_[12].dxy_csc = vtx_dt*sin(pphi) - vty_dt*cos(pphi);


    auto totalp = std::sqrt( t.momentum().x()*t.momentum().x() + t.momentum().y()*t.momentum().y() + t.momentum().z()*t.momentum().z());

    etrk_csc_[12].p_SimTrack_csc = totalp;
    etrk_csc_[12].charge_csc = t.charge();
    etrk_csc_[12]. p_c_SimTrack_csc = totalp*t.charge();





/*
  for (auto asdt: stationsdt_to_use_)
  {

    etrk_dt_[asdt].init();
    etrk_dt_[asdt].run = match.simhits().event().id().run();
    etrk_dt_[asdt].lumi= match.simhits().event().id().luminosityBlock();
    etrk_dt_[asdt].event = match.simhits().event().id().event();
    etrk_dt_[asdt].charge_dt=t.charge();

    etrk_dt_[asdt].dtvertex_x = vtx_dt;
    etrk_dt_[asdt].dtvertex_y = vty_dt;
    etrk_dt_[asdt].dtvertex_z = vtz_dt;
    etrk_dt_[asdt].dtvertex_r = sqrt(vtx_dt*vtx_dt+vty_dt*vty_dt);

    etrk_dt_[asdt].pt_SimTrack_dt=t.momentum().pt(); //This one

    etrk_dt_[asdt].eta_SimTrack_dt=t.momentum().eta();
    etrk_dt_[asdt].phi_SimTrack_dt = t.momentum().phi();

     if (!(t.momentum().pt()==0)){
         etrk_dt_[asdt].apt_SimTrack_dt =1/ t.momentum().pt();  //This one
     }else{
         etrk_dt_[asdt].apt_SimTrack_dt = 0;
     }

    auto pphi = t.momentum().phi();
    etrk_dt_[asdt].dt_dxy = vtx_dt*sin(pphi) - vty_dt*cos(pphi);

 // float bestdRl1 = 99.;
 // int nl1tr = 0;
    for(std::vector<l1extra::L1MuonParticle>::const_iterator muon=l1p->begin(); muon!=l1p->end(); ++muon)
    {
      etrk_dt_[asdt].L1_pt = muon->pt();
      etrk_dt_[asdt].L1_eta = muon->eta();
      etrk_dt_[asdt].L1_phi_ = muon->phi();
      etrk_dt_[asdt].L1_q = muon->charge();
      float L1eta = muon->eta();
      float L1phi = muon->phi();

      float dptr = deltaPhi(L1phi, t.momentum().phi());
      float detatr = L1eta - t.momentum().eta();
      float drtr = std::sqrt(dptr*dptr + detatr*detatr);

      if (drtr < 0.5){
         nl1tr = nl1tr + 1;
      }

      if(drtr< bestdRl1){
         bestdRl1 = drtr;
      }

    }

    etrk_dt_[asdt].has_l1_st_matched = nl1tr;
    etrk_dt_[asdt].L1_st_dr = bestdRl1;


    float bestdRl2=99.;
    int nl2tr=0;
    for(std::vector<reco::RecoChargedCandidate>::const_iterator muon = hlt_l2_pp->begin(); muon!=hlt_l2_pp->end(); ++muon)
    {
      float L2eta = muon->eta();
      float L2phi = muon->phi();

      float dptr = deltaPhi(L2phi, t.momentum().phi());
      float detatr = L2eta - t.momentum().eta();
      float drtr = std::sqrt(dptr*dptr + detatr*detatr);


      if (drtr < 0.2){
          nl2tr = nl2tr + 1;
      }

      if(drtr < bestdRl2){
          bestdRl2 = drtr;
      }
    }

    etrk_dt_[asdt].has_l2_st_matched = nl2tr;
    etrk_dt_[asdt].L2_st_dr = bestdRl2;

    float bestdRltt = 99;
    int nmtt2= 0;

    for(std::vector<reco::TrackExtra>::const_iterator l2tt = l2_track->begin(); l2tt!=l2_track->end();++l2tt)
    {

     auto Xx = l2tt->innerPosition().eta();
     auto Xy = l2tt->innerPosition().phi();

     float det = Xx = t.momentum().eta();
     float dph = deltaPhi(Xy, t.momentum().phi());

     float dr = std::sqrt(det*det + dph*dph);


     if (dr< bestdRltt) bestdRltt = dr;
     if (dr< 0.7 ) nmtt2 = nmtt2 + 1;
    }

    etrk_dt_[asdt].L2t_st_dr = bestdRltt;
    etrk_dt_[asdt].has_l2t_st_matched = nmtt2;


  } 

    */


 //CSC SimHits Start here
 auto csc_simhits(match_sh.chamberIdsCSC(0));

 for(auto d: csc_simhits)
 {
    CSCDetId id(d);
    const int st(detIdToMEStation(id.station(),id.ring()));
    if (stationscsc_to_use_.count(st) == 0) continue;
    int nlayers(match_sh.nLayersWithHitsInSuperChamber(d));

    if (id.station()==1 and (id.ring()==4 or id.ring()==1)){
    int other_ring(id.ring()==4 ? 1 : 4);
    CSCDetId co_id(id.endcap(), id.station(), other_ring, id.chamber());
      auto rawId(co_id.rawId());
      if (csc_simhits.find(rawId) != csc_simhits.end()) {
        nlayers = nlayers+match_sh.nLayersWithHitsInSuperChamber(rawId);

      }
    }

    etrk_csc_[st].nlayerscsc = nlayers;
    etrk_csc_[st].csc_station = id.station();
    etrk_csc_[st].csc_ring = id.ring();

    GlobalPoint hitGp = match_sh.simHitsMeanPosition(match_sh.hitsInChamber(d));
    etrk_csc_[st].csc_gp_x = hitGp.x();
    etrk_csc_[st].csc_gp_y = hitGp.y();
    etrk_csc_[st].csc_gp_z = hitGp.z();
    etrk_csc_[st].csc_gp_r = hitGp.perp();
    etrk_csc_[st].csc_gp_eta = hitGp.eta();
    etrk_csc_[st].csc_gp_phi = hitGp.phi();
    
    GlobalVector ym = match_sh.simHitsMeanMomentum(match_sh.hitsInChamber(d));
    etrk_csc_[st].csc_gv_eta = ym.eta();
    etrk_csc_[st].csc_gv_phi = ym.phi();
    etrk_csc_[st].csc_gv_pt = ym.perp();
    etrk_csc_[st].csc_deltaphi = deltaPhi(hitGp.phi(), ym.phi());  //Bending Angle Position and Direction

    //std::cout<<"ME"<<id.station()<<id.ring()<<" Which is equal to: "<<st<<" Has "<<nlayers<<"Layers with hits"<<std::endl;

    // Case ME11
    if(id.station()==1 and (id.ring()==4 or id.ring()==1)){
        etrk_csc_[1].nlayerscsc = nlayers;
        etrk_csc_[1].csc_station = 1;
        etrk_csc_[1].csc_ring = 1;
        etrk_csc_[1].csc_gp_x = hitGp.x();
        etrk_csc_[1].csc_gp_y = hitGp.y();
        etrk_csc_[1].csc_gp_z = hitGp.z();
        etrk_csc_[1].csc_gp_r = hitGp.perp();
        etrk_csc_[1].csc_gp_eta = hitGp.eta();
        etrk_csc_[1].csc_gp_phi = hitGp.phi();
        etrk_csc_[1].csc_gv_eta = ym.eta();
        etrk_csc_[1].csc_gv_phi = ym.phi();
        etrk_csc_[1].csc_gv_pt = ym.perp();
        etrk_csc_[1].csc_deltaphi = deltaPhi(hitGp.phi(), ym.phi());  //Bending Angle Position and Direction
    }


    if(id.station()==1){
        etrk_csc_[12].nlayerscsc = nlayers;
        etrk_csc_[12].csc_station = 1;
        etrk_csc_[12].csc_ring = 1;
        etrk_csc_[12].csc_gp_x = hitGp.x();
        etrk_csc_[12].csc_gp_y = hitGp.y();
        etrk_csc_[12].csc_gp_z = hitGp.z();
        etrk_csc_[12].csc_gp_r = hitGp.perp();
        etrk_csc_[12].csc_gp_eta = hitGp.eta();
        etrk_csc_[12].csc_gp_phi = hitGp.phi();
        etrk_csc_[12].csc_gv_eta = ym.eta();
        etrk_csc_[12].csc_gv_phi = ym.phi();
        etrk_csc_[12].csc_gv_pt = ym.perp();
        etrk_csc_[12].csc_deltaphi = deltaPhi(hitGp.phi(), ym.phi()); 
    }


    //Starting look for second hit
    for(auto s_d: csc_simhits)
    {
        CSCDetId s_id(s_d);
        const int s_st(detIdToMEStation(s_id.station(),s_id.ring()));
        if (stationscsc_to_use_.count(s_st) == 0) continue;
        int d_nlayers(match_sh.nLayersWithHitsInSuperChamber(d));
        int s_nlayers(match_sh.nLayersWithHitsInSuperChamber(s_d));
        
        if(s_nlayers == 0) continue; // Check to have hits in the secondary chamber
        if(d_nlayers == 0) continue; //Check that has hits in previous one
        if(id.station() == s_id.station() and id.ring() == s_id.ring()) continue;  // No double hits in the same station (ME11 a and ME11 need changes)
    
        GlobalPoint hitGp2 = match_sh.simHitsMeanPosition(match_sh.hitsInChamber(s_d));
        GlobalVector ym2 = match_sh.simHitsMeanMomentum(match_sh.hitsInChamber(s_d));
 

        etrk_csc_[st].csc_second_nlayers = s_nlayers;
        etrk_csc_[st].csc_second_ring = s_id.ring();
        etrk_csc_[st].csc_second_station = s_id.station();
        etrk_csc_[st].csc_second_gp_x = hitGp2.x();
        etrk_csc_[st].csc_second_gp_y = hitGp2.y();
        etrk_csc_[st].csc_second_gp_z = hitGp2.z();
        etrk_csc_[st].csc_second_gp_eta = hitGp2.eta();
        etrk_csc_[st].csc_second_gp_phi = hitGp2.phi();
        etrk_csc_[st].csc_second_gv_eta = ym2.eta();
        etrk_csc_[st].csc_second_gv_phi = ym2.phi();
        etrk_csc_[st].csc_second_gv_pt = ym2.perp();
        etrk_csc_[st].csc_bending_angle = deltaPhi(ym.phi(), ym2.phi());
        etrk_csc_[st].csc_deltaphi_second = deltaPhi(hitGp2.phi(), ym2.phi());
        etrk_csc_[st].csc_deltaphi_gp = deltaPhi(hitGp2.phi(), hitGp.phi());
        etrk_csc_[st].csc_deltaeta = ym.eta() - ym2.eta();
        etrk_csc_[st].csc_q_1bending_angle = t.charge()/deltaPhi(ym.phi(), ym2.phi());



	// Special case for ME11
        if(id.station()==1 and (id.ring()==4 or id.ring()==1)){
            etrk_csc_[1].csc_second_nlayers = s_nlayers;
            etrk_csc_[1].csc_second_ring = s_id.ring();
            etrk_csc_[1].csc_second_station = s_id.station();
            etrk_csc_[1].csc_second_gp_x = hitGp2.x();
            etrk_csc_[1].csc_second_gp_y = hitGp2.y();
            etrk_csc_[1].csc_second_gp_z = hitGp2.z();
            etrk_csc_[1].csc_second_gp_eta = hitGp2.eta();
            etrk_csc_[1].csc_second_gp_phi = hitGp2.phi();
            etrk_csc_[1].csc_second_gv_eta = ym2.eta();
            etrk_csc_[1].csc_second_gv_phi = ym2.phi();
            etrk_csc_[1].csc_second_gv_pt = ym2.perp();
            etrk_csc_[1].csc_bending_angle = deltaPhi(ym.phi(), ym2.phi());  
            etrk_csc_[1].csc_deltaphi_second = deltaPhi(hitGp2.phi(), ym2.phi());
            etrk_csc_[1].csc_deltaphi_gp = deltaPhi(hitGp2.phi(), hitGp.phi());
            etrk_csc_[1].csc_deltaeta = ym.eta() - ym2.eta();
            etrk_csc_[1].csc_q_1bending_angle = t.charge()/deltaPhi(ym.phi(), ym2.phi());

            if(s_id.station()==2){
                etrk_csc_[1].csc_bending_angle_12 = deltaPhi(ym.phi(), ym2.phi());
                etrk_csc_[st].csc_bending_angle_12 = deltaPhi(ym.phi(), ym2.phi());
                etrk_csc_[1].has_csc_12 = 1;
                etrk_csc_[st].has_csc_12 = 1;                                                     // Ask for this
                etrk_csc_[st].csc_deltaeta_12 = ym.eta() - ym2.eta();
                etrk_csc_[1].csc_deltaeta_12 = ym.eta() - ym2.eta();
                etrk_csc_[st].csc_q_1bending_angle_12 = t.charge()/deltaPhi(ym.phi(), ym2.phi()); // Use this 
                etrk_csc_[1].csc_q_1bending_angle_12 = t.charge()/deltaPhi(ym.phi(), ym2.phi());
            }
        
            if(s_id.station()==3){
                etrk_csc_[st].csc_bending_angle_13 = deltaPhi(ym.phi(), ym2.phi());
                etrk_csc_[1].csc_bending_angle_13 = deltaPhi(ym.phi(), ym2.phi());
                etrk_csc_[1].has_csc_13 = 1;
                etrk_csc_[st].has_csc_13 = 1;
                etrk_csc_[1].csc_deltaeta_13 = ym.eta() - ym2.eta();
                etrk_csc_[st].csc_deltaeta_13 = ym.eta() - ym2.eta();
                etrk_csc_[1].csc_q_1bending_angle_13 = t.charge()/deltaPhi(ym.phi(), ym2.phi());
                etrk_csc_[st].csc_q_1bending_angle_13 = t.charge()/deltaPhi(ym.phi(), ym2.phi());

            }

            if(s_id.station()==4){
                etrk_csc_[st].has_csc_14 = 1;
                etrk_csc_[1].has_csc_14 = 1;
                etrk_csc_[1].csc_bending_angle_14 = deltaPhi(ym.phi(), ym2.phi());
                etrk_csc_[st].csc_bending_angle_14 = deltaPhi(ym.phi(), ym2.phi());
                etrk_csc_[st].csc_deltaeta_14 = ym.eta() - ym2.eta();
                etrk_csc_[1].csc_deltaeta_14 = ym.eta() - ym2.eta();
                etrk_csc_[1].csc_q_1bending_angle_14 = t.charge()/deltaPhi(ym.phi(), ym2.phi());
                etrk_csc_[st].csc_q_1bending_angle_14 = t.charge()/deltaPhi(ym.phi(), ym2.phi());
            }
        } // End of especial case for ME11



	// Starting Special Case for ME1
        if(id.station()==1){
            etrk_csc_[12].csc_second_nlayers = s_nlayers;
            etrk_csc_[12].csc_second_ring = s_id.ring();
            etrk_csc_[12].csc_second_station = s_id.station();
            etrk_csc_[12].csc_second_gp_x = hitGp2.x();
            etrk_csc_[12].csc_second_gp_y = hitGp2.y();
            etrk_csc_[12].csc_second_gp_z = hitGp2.z();
            etrk_csc_[12].csc_second_gp_eta = hitGp2.eta();
            etrk_csc_[12].csc_second_gp_phi = hitGp2.phi();
            etrk_csc_[12].csc_second_gv_eta = ym2.eta();
            etrk_csc_[12].csc_second_gv_phi = ym2.phi();
            etrk_csc_[12].csc_second_gv_pt = ym2.perp();
            etrk_csc_[12].csc_bending_angle = deltaPhi(ym.phi(), ym2.phi()); // Use this and ask for has_csc_1X
            etrk_csc_[12].csc_deltaphi_second = deltaPhi(hitGp2.phi(), ym2.phi());
            etrk_csc_[12].csc_deltaphi_gp = deltaPhi(hitGp2.phi(), hitGp.phi());
            etrk_csc_[12].csc_deltaeta = ym.eta() - ym2.eta();
            etrk_csc_[12].csc_q_1bending_angle = t.charge()/deltaPhi(ym.phi(), ym2.phi());

            if(s_id.station()==2){
                etrk_csc_[12].csc_bending_angle_12 = deltaPhi(ym.phi(), ym2.phi());
                etrk_csc_[st].csc_bending_angle_12 = deltaPhi(ym.phi(), ym2.phi());
                etrk_csc_[12].has_csc_12 = 1;
                etrk_csc_[st].has_csc_12 = 1;
                etrk_csc_[st].csc_deltaeta_12 = ym.eta() - ym2.eta();
                etrk_csc_[12].csc_deltaeta_12 = ym.eta() - ym2.eta();
            	etrk_csc_[12].csc_q_1bending_angle_12 = t.charge()/deltaPhi(ym.phi(), ym2.phi());
            	etrk_csc_[st].csc_q_1bending_angle_12 = t.charge()/deltaPhi(ym.phi(), ym2.phi());
            }

            if(s_id.station()==3){
                etrk_csc_[st].csc_bending_angle_13 = deltaPhi(ym.phi(), ym2.phi());
                etrk_csc_[12].csc_bending_angle_13 = deltaPhi(ym.phi(), ym2.phi());
                etrk_csc_[12].has_csc_13 = 1;
                etrk_csc_[st].has_csc_13 = 1;
                etrk_csc_[12].csc_deltaeta_13 = ym.eta() - ym2.eta();
                etrk_csc_[st].csc_deltaeta_13 = ym.eta() - ym2.eta();
            	etrk_csc_[st].csc_q_1bending_angle_13 = t.charge()/deltaPhi(ym.phi(), ym2.phi());
            	etrk_csc_[12].csc_q_1bending_angle_13 = t.charge()/deltaPhi(ym.phi(), ym2.phi());

            }

            if(s_id.station()==4){
                etrk_csc_[st].has_csc_14 = 1;
                etrk_csc_[12].has_csc_14 = 1;
                etrk_csc_[12].csc_bending_angle_14 = deltaPhi(ym.phi(), ym2.phi()); // Deprecated all *_1X;
                etrk_csc_[st].csc_bending_angle_14 = deltaPhi(ym.phi(), ym2.phi());
                etrk_csc_[st].csc_deltaeta_14 = ym.eta() - ym2.eta();
                etrk_csc_[12].csc_deltaeta_14 = ym.eta() - ym2.eta();
            	etrk_csc_[st].csc_q_1bending_angle_13 = t.charge()/deltaPhi(ym.phi(), ym2.phi());
            	etrk_csc_[12].csc_q_1bending_angle_13 = t.charge()/deltaPhi(ym.phi(), ym2.phi());
            }
        }  // End of Special Case ME1 


        //std::cout<<" Second hit in Station ME"<<s_id.station()<<s_id.ring()<<" with nlayers "<<s_nlayers<<std::endl;

    } // End of Second Hit

 } // End of CSC Sim Hits



 //Filling per station CSC

 for(auto st: stationscsc_to_use_)
 {
  tree_eff_csc_[st]->Fill();
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

void MyTrackEffL1::init()
{

 L1_pt = -99.;
 L1_eta = -9.;
 L1_phi = - 99.;
 L1_charge = - 9.;


} 

void MyTrackEffCSC::init()
{

 lumi = - 99;
 run = - 99;
 
 pt_SimTrack_csc = - 9;
 phi_SimTrack_csc = - 9;
 eta_SimTrack_csc= - 9;
 vertex_x = - 9;
 vertex_y = - 9;
 vertex_z = - 9;

 dxy_csc = - 9.;
 p_SimTrack_csc = - 9;
 charge_csc = - 9.;
 p_c_SimTrack_csc = - 9;
 


 csc_second_gp_x = - 9999.;
 csc_second_gp_y = - 9999.;
 csc_second_gp_z = - 9999.;
 csc_second_gp_eta = - 99.;
 csc_second_gp_phi = - 99.;
 csc_second_gv_phi = -99.;
 csc_second_gv_eta = - 99.;
 csc_second_gv_pt = - 9.;
 csc_second_station = - 9;
 csc_second_ring = - 9;
 csc_second_nlayers = - 9;

 csc_gp_y = - 9999;
 csc_gp_x = - 9999;
 csc_gp_r = - 9999;
 csc_gp_z = - 9999;
 nlayerscsc = 0;
 csc_gp_eta = - 9;
 csc_gp_phi = - 9;
 
 csc_gv_eta = - 9.;
 csc_gv_phi = - 9.;
 csc_gv_pt = - 9.;

 csc_station = - 99;
 csc_ring = - 99;
 csc_deltaeta = - 99.;
 csc_deltaeta_14 = - 99.;
 csc_deltaeta_13 = - 99.;
 csc_deltaeta_12 = - 99.;

 has_csc_12 = 0;
 has_csc_13 = 0;
 has_csc_14 = 0;
 csc_bending_angle = - 99;
 csc_bending_angle_12 = - 99;
 csc_bending_angle_13 = - 99;
 csc_bending_angle_14 = - 99;
 csc_deltaphi_gp = - 99;
 csc_deltaphi = - 99;
 csc_deltaphi_second = - 99;

 csc_q_1bending_angle = - 99.;
 csc_q_1bending_angle_12 = - 99.;
 csc_q_1bending_angle_13 = - 99.;
 csc_q_1bending_angle_14 = - 99.;

}
void MyTrackEffDT::init()
{
 lumi = -99;
 run= -99;
 event = -99;

 pt_SimTrack_dt = -9.;
 eta_SimTrack_dt=-9.;
 phi_SimTrack_dt=-9.;
 eta_gp = -9.;
 eta_gv = -9.;
 phi_gv= -9.;
 pt_gv= -9.;
 z_gp = -9900.;
 deltaphi_h_g = -9.;
 apt_SimTrack_dt=-999;
 charge_dt = -99;

 Seg_dphi_sh = 99;
 Seg_deta_sh = 99;

 Seg_dr_sh = -9.;
 Seg_dr_st = -9.;
 Seg_dr_l2 = -9.;
 has_seg_sh_matched = 0;
 has_seg_st_matched = 0;
 has_seg_l2_matched = 0;
 has_DTSegments = 0;

 Seg_second_wheel =  - 9;
 Seg_second_station = - 9;
 Seg_second_st = 0;
 Seg_second_gp_eta = - 99.;
 Seg_second_gp_phi = - 99.;
 Seg_second_gp_z = - 9999.;
 Seg_second_gp_y = - 9999.;
 Seg_second_gp_x = - 9999.;
 Seg_second_gv_eta = - 99.;
 Seg_second_gv_phi = - 9.;
 Seg_second_sh_dr = - 9.;
 has_eta_phi_dr = 0;
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
 has_second_segment_matched = 0;
 has_second_dtSegment  = 0;
 Seg_deltaphi_gv = - 999.;

 has_seg_13 = 0;
 has_seg_12 = 0;
 has_seg_23 = 0;
 has_seg_24 = 0;
 has_seg_34 = 0;

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
 dtvertex_x=-9999;
 dtvertex_y=-9999;
 dtvertex_z=-9999;
 dtvertex_r=-9999;
 has_dt_sh= 0;
 
 R_gv=-9999.;
 nlayerdt = 0;
 nslayerdt = 0;
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

}

TTree*MyTrackEffL1::book(TTree *t, const std::string & name)
{
  edm::Service< TFileService> fs;
  t = fs->make<TTree>(name.c_str(),name.c_str());
 
  t->Branch("L1_pt", &L1_pt);
  t->Branch("L1_eta", &L1_eta);
  t->Branch("L1_charge", &L1_charge);
  t->Branch("L1_phi", &L1_phi);

  return t;
}

TTree*MyTrackEffCSC::book(TTree *t, const std::string & name)
{

  edm::Service< TFileService > fs;
  t = fs->make<TTree>(name.c_str(),name.c_str());

  t->Branch("run", &run);
  t->Branch("lumi", &lumi);
  t->Branch("pt_SimTrack_csc", &pt_SimTrack_csc);
  t->Branch("phi_SimTrack_csc", &phi_SimTrack_csc);
  t->Branch("eta_SimTrack_csc", &eta_SimTrack_csc); 
  t->Branch("vertex_x", &vertex_x);
  t->Branch("vertex_y", &vertex_y);
  t->Branch("vertex_z", &vertex_z);

  t->Branch("dxt_csc_", &dxy_csc);
  t->Branch("csc_station", &csc_station);
  t->Branch("csc_ring", &csc_ring);

  t->Branch("p_SimTrack_csc", &p_SimTrack_csc);
  t->Branch("charge_csc", &charge_csc);
  t->Branch("p_c_SimTrack_csc", &p_c_SimTrack_csc);


  t->Branch("csc_gp_y", &csc_gp_y);
  t->Branch("csc_gp_x", &csc_gp_x);
  t->Branch("csc_gp_r", &csc_gp_r);
  t->Branch("csc_gp_z", &csc_gp_z);
  t->Branch("csc_gp_eta", &csc_gp_eta);
  t->Branch("csc_gp_phi", &csc_gp_phi);
  t->Branch("nlayerscsc", &nlayerscsc);


  t->Branch("csc_second_gp_x", &csc_second_gp_x);
  t->Branch("csc_second_gp_y", &csc_second_gp_y);
  t->Branch("csc_second_gp_z", &csc_second_gp_z);
  t->Branch("csc_second_gp_eta", &csc_second_gp_eta);
  t->Branch("csc_second_gp_phi", &csc_second_gp_phi);
  t->Branch("csc_second_gp_x", &csc_second_gp_x);
  t->Branch("csc_second_gp_x", &csc_second_gp_x);
 

  t->Branch("csc_second_gv_phi", &csc_second_gv_phi);
  t->Branch("csc_second_gv_eta", &csc_second_gv_eta);
  t->Branch("csc_second_gv_pt", &csc_second_gv_pt);
 
  t->Branch("csc_second_station", &csc_second_station);
  t->Branch("csc_second_ring", &csc_second_ring);
  t->Branch("csc_second_nlayers", &csc_second_nlayers);

  t->Branch("csc_gv_eta", &csc_gv_eta);
  t->Branch("csc_gv_pt", &csc_gv_pt);
  t->Branch("csc_gv_phi", &csc_gv_phi);
  t->Branch("csc_deltaphi", &csc_deltaphi);
  t->Branch("csc_deltaphi_gp", &csc_deltaphi_gp);
  t->Branch("csc_deltaphi_second", &csc_deltaphi_second);

  t->Branch("csc_bending_angle", &csc_bending_angle);
  t->Branch("csc_bending_angle_12", &csc_bending_angle_12);
  t->Branch("csc_bending_angle_13", &csc_bending_angle_13);
  t->Branch("csc_bending_angle_14", &csc_bending_angle_14);


  t->Branch("csc_q_1bending_angle", &csc_q_1bending_angle);
  t->Branch("csc_q_1bending_angle_12", &csc_q_1bending_angle_12);
  t->Branch("csc_q_1bending_angle_13", &csc_q_1bending_angle_13);
  t->Branch("csc_q_1bending_angle_14", &csc_q_1bending_angle_14);

  t->Branch("csc_deltaeta_14", &csc_deltaeta_14);
  t->Branch("csc_deltaeta", &csc_deltaeta);
  t->Branch("csc_deltaeta_13", &csc_deltaeta_13);
  t->Branch("csc_deltaeta_12", &csc_deltaeta_12);
  t->Branch("has_csc_12", &has_csc_12);
  t->Branch("has_csc_13", &has_csc_13);
  t->Branch("has_csc_14", &has_csc_14);
  return t;
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

  t->Branch("Seg_dphi_sh", &Seg_dphi_sh);
  t->Branch("Seg_deta_sh", &Seg_deta_sh);

  t->Branch("Seg_dr_sh", &Seg_dr_sh);
  t->Branch("Seg_dr_st", &Seg_dr_st);
  t->Branch("Seg_dr_l2", &Seg_dr_l2);
  t->Branch("has_seg_sh_matched", &has_seg_sh_matched);
  t->Branch("has_seg_st_matched", &has_seg_st_matched);
  t->Branch("has_seg_l2_matched", &has_seg_l2_matched);
  t->Branch("has_DTSegments", &has_DTSegments);

  t->Branch("Seg_second_wheel", &Seg_second_wheel);
  t->Branch("Seg_second_station", &Seg_second_station);
  t->Branch("Seg_second_st", &Seg_second_st);
  t->Branch("Seg_second_gp_eta", &Seg_second_gp_eta);
  t->Branch("Seg_second_gp_phi", &Seg_second_gp_phi);
  t->Branch("Seg_second_gp_z", &Seg_second_gp_z);
  t->Branch("Seg_second_gp_y", &Seg_second_gp_y);
  t->Branch("Seg_second_gp_x", &Seg_second_gp_x);
  t->Branch("Seg_second_gv_eta", &Seg_second_gv_eta);
  t->Branch("Seg_second_gv_phi", &Seg_second_gv_phi);
  t->Branch("Seg_second_sh_dr", &Seg_second_sh_dr);
  t->Branch("has_eta_phi_dr", &has_eta_phi_dr);
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
  t->Branch("Seg_deltaphi_gv", &Seg_deltaphi_gv);
  t->Branch("Seg_deltaphi_13_gv", &Seg_deltaphi_13_gv);
  t->Branch("Seg_deltaphi_14_gv", &Seg_deltaphi_14_gv);
  t->Branch("Seg_deltaphi_23_gv", &Seg_deltaphi_23_gv);
  t->Branch("Seg_deltaphi_24_gv", &Seg_deltaphi_24_gv);
  t->Branch("Seg_deltaphi_34_gv", &Seg_deltaphi_34_gv);
  t->Branch("has_second_segment_matched", &has_second_segment_matched);
  t->Branch("has_second_dtSegment", &has_second_dtSegment);
  t->Branch("has_seg_14", &has_seg_14);
  t->Branch("has_seg_13", &has_seg_13);
  t->Branch("has_seg_12", &has_seg_12);
  t->Branch("has_seg_23", &has_seg_23);
  t->Branch("has_seg_24", &has_seg_24);
  t->Branch("has_seg_34", &has_seg_34);

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
  t->Branch("eta_SimTrack_dt", &eta_SimTrack_dt);
  t->Branch("pt_SimTrack_dt", &pt_SimTrack_dt);
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
  t->Branch("dtvertex_x", &dtvertex_x);
  t->Branch("dtvertex_y", &dtvertex_y);
  t->Branch("dtvertex_z", &dtvertex_z);
  t->Branch("dtvertex_r", &dtvertex_r);
  t->Branch("deltaphi_h_g", &deltaphi_h_g);
  t->Branch("z_gp", &z_gp);
  t->Branch("x_gp", &x_gp);
  t->Branch("y_gp", &y_gp);
  t->Branch("r_gp", &r_gp);
  t->Branch("phi_gp", &phi_gp);
  t->Branch("phi_SimTrack_dt", &phi_SimTrack_dt);
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
