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
#include "DataFormats/MuonReco/interface/Muon.h"
#include "DataFormats/RecoCandidate/interface/RecoCandidate.h"
#include "DataFormats/RecoCandidate/interface/RecoChargedCandidate.h"
#include "DataFormats/RecoCandidate/interface/RecoChargedCandidateFwd.h"
#include <DataFormats/TrackReco/interface/TrackExtra.h>

#include "GEMCode/GEMValidation/interface/SimTrackMatchManager.h"
#include "GEMCode/GEMValidation/interface/Ptassignment.h"


using namespace std;

struct MyTrackRateL1
{
 void init();
 TTree*book(TTree *t, const std::string & name = "l1_particles_");

 Float_t L1_pt;
 Float_t L1_eta;
 Float_t L1_phi;
 Float_t L1_charge;
};

struct MyTrackRateCSC
{
 void init();
 TTree*book(TTree *t, const std::string & name = "trk_eff_csc_");
 
 Int_t lumi;
 Int_t run;
 Float_t eta_SimTrack;
 Float_t phi_SimTrack;
 Float_t pt_SimTrack;
 Float_t vertex_x;
 Float_t vertex_y;
 Float_t vertex_z;
 Float_t dxy; 
 Float_t charge;
 Int_t ntrks;

 Float_t Lxy;
 Float_t pzvz;
 Float_t pp_SimTrack;
 Float_t p_SimTrack;
 Float_t p_c_SimTrack;

 Int_t csc_st1_ring;
 Int_t csc_st1_chamber;
 Int_t csc_st1_nlayerscsc;
 Char_t csc_st1_has_csc_sh; // #layers with SimHits > minHitsChamber    bit1: in odd, bit2: even
 Float_t csc_st1_gv_eta;
 Float_t csc_st1_gv_phi;
 Float_t csc_st1_gv_pt;
 Float_t csc_st1_gp_r;
 Float_t csc_st1_gp_x;
 Float_t csc_st1_gp_y;
 Float_t csc_st1_gp_z;
 Float_t csc_st1_gp_eta;
 Float_t csc_st1_gp_phi;
 Float_t csc_st1_bending_sh;
 Float_t csc_st1_deltaphi;
 
 Int_t csc_st2_ring;
 Int_t csc_st2_chamber;
 Int_t csc_st2_nlayerscsc;
 Char_t csc_st2_has_csc_sh; // #layers with SimHits > minHitsChamber    bit1: in odd, bit2: even
 Float_t csc_st2_gv_eta;
 Float_t csc_st2_gv_phi;
 Float_t csc_st2_gv_pt;
 Float_t csc_st2_gp_r;
 Float_t csc_st2_gp_x;
 Float_t csc_st2_gp_y;
 Float_t csc_st2_gp_z;
 Float_t csc_st2_gp_eta;
 Float_t csc_st2_gp_phi;
 Float_t csc_st2_bending_sh;
 Float_t csc_st2_deltaphi;

 Int_t csc_st3_ring;
 Int_t csc_st3_chamber;
 Int_t csc_st3_nlayerscsc;
 Char_t csc_st3_has_csc_sh; // #layers with SimHits > minHitsChamber    bit1: in odd, bit2: even
 Float_t csc_st3_gv_eta;
 Float_t csc_st3_gv_phi;
 Float_t csc_st3_gv_pt;
 Float_t csc_st3_gp_r;
 Float_t csc_st3_gp_x;
 Float_t csc_st3_gp_y;
 Float_t csc_st3_gp_z;
 Float_t csc_st3_gp_eta;
 Float_t csc_st3_gp_phi;
 Float_t csc_st3_bending_sh;
 Float_t csc_st3_deltaphi;

 Int_t csc_st4_ring;
 Int_t csc_st4_chamber;
 Int_t csc_st4_nlayerscsc;
 Char_t csc_st4_has_csc_sh; // #layers with SimHits > minHitsChamber    bit1: in odd, bit2: even
 Float_t csc_st4_gv_eta;
 Float_t csc_st4_gv_phi;
 Float_t csc_st4_gv_pt;
 Float_t csc_st4_gp_r;
 Float_t csc_st4_gp_x;
 Float_t csc_st4_gp_y;
 Float_t csc_st4_gp_z;
 Float_t csc_st4_gp_eta;
 Float_t csc_st4_gp_phi;
 Float_t csc_st4_bending_sh;
 Float_t csc_st4_deltaphi;

 Float_t csc_bending_angle_12;
 Float_t csc_bending_angle_13;
 Float_t csc_bending_angle_14;
 

 Float_t delta_x_gp_12;
 Float_t delta_y_gp_12;
 Float_t delta_y_gp_13;
 Float_t delta_y_gp_14;
 Float_t delta_x_gp_13;
 Float_t delta_x_gp_14;


 Float_t delta_x_gp_23;
 Float_t delta_y_gp_23;
 Float_t delta_x_gp_24;
 Float_t delta_y_gp_24;


 Float_t delta_y_gp_34;
 Float_t delta_x_gp_34;

 
 Float_t csc_deltaphi_gp_12;
 Float_t csc_deltaphi_gp_13;
 Float_t csc_deltaphi_gp_14;
 Float_t csc_deltaphi_gp_23;
 Float_t csc_deltaphi_gp_24;
 Float_t csc_deltaphi_gp_34;


 Float_t csc_p_over_cosh_eta;

 Float_t csc_deltaeta;
 Float_t csc_deltaeta_14;
 Float_t csc_deltaeta_13;
 Float_t csc_deltaeta_12;

 Int_t npar;
 Float_t pt_position_sh,pt_direction_sh;

};

struct MyTrackRateDT
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
 Int_t wheel;
 Int_t station;




};


class DisplacedMuonTriggerRateGENSIM : public edm::EDAnalyzer 
{
public:
  explicit DisplacedMuonTriggerRateGENSIM(const edm::ParameterSet&);
  ~DisplacedMuonTriggerRateGENSIM();
  
  virtual void analyze(const edm::Event&, const edm::EventSetup&) ;
  
  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
  
private:
  
  void analyzeTrackEfficiency(SimTrackMatchManager& match, int trk_no, int st);
  //, edm::Handle<std::vector<l1extra::L1MuonParticle> > l1p, edm::Handle<std::vector<reco::RecoChargedCandidate> > hlt_l2_pp, edm::Handle<std::vector<reco::TrackExtra> > l2_track, edm::Handle<edm::RangeMap<DTChamberId,edm::OwnVector<DTRecSegment4D,edm::ClonePolicy<DTRecSegment4D> >,edm::ClonePolicy<DTRecSegment4D> > > SegmentsDT);

  bool isSimTrackGood(const SimTrack &t);
  int detIdToMEStation(int st, int ri);
  int detIdToMBStation(int wh, int st);
  std::vector<string> dtStations_;
  std::set<int> stationsdt_to_use_;
  std::set<int> stationscsc_to_use_;
  std::set<int> l1particles_muons_;
  
  TTree *tree_eff_dt_[56];
  MyTrackRateDT etrk_dt_[56];
  
  TTree *tree_eff_csc_[3];//sim, position based, direction based
  MyTrackRateCSC etrk_csc_[3];

  TTree *tree_eff_l1_[6];
  MyTrackRateL1 etrk_l1_[6];
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

DisplacedMuonTriggerRateGENSIM::DisplacedMuonTriggerRateGENSIM(const edm::ParameterSet& ps)
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

  //copy(L1Particles.begin(), L1Particles.end(), inserter(l1particles_muons_, l1particles_muons_.end()));
  //for(auto m: l1particles_muons_)
  //{
    //stringstream ss;
    //ss<<" trk_eff_l1_"<< L1Ppabc[m];
    //tree_eff_l1_[m] = etrk_l1_[m].book(tree_eff_l1_[m], ss.str());    
 // }

  //copy(DtStationsToUse.begin(),DtStationsToUse.end(),inserter(stationsdt_to_use_,stationsdt_to_use_.end()));
  //for (auto m: stationsdt_to_use_)
  //{
   // stringstream ss;
    //ss<< "trk_eff_dt_" << stationsDT[m];
    //tree_eff_dt_[m] = etrk_dt_[m].book(tree_eff_dt_[m], ss.str());    
  //}

  copy(CSCStationsToUse.begin(),CSCStationsToUse.end(), inserter(stationscsc_to_use_, stationscsc_to_use_.end()));
  //case0
  stringstream ss0;
  ss0<< "trk_rate_csc_sim";
  tree_eff_csc_[0] = etrk_csc_[0].book(tree_eff_csc_[0], ss0.str());
  //case1
  stringstream ss1;
  ss1<< "trk_rate_csc_position";
  tree_eff_csc_[1] = etrk_csc_[1].book(tree_eff_csc_[1], ss1.str());
  //case1
  stringstream ss2;
  ss2<< "trk_rate_csc_direction";
  tree_eff_csc_[2] = etrk_csc_[2].book(tree_eff_csc_[2], ss2.str());


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


int DisplacedMuonTriggerRateGENSIM::detIdToMEStation(int st, int ri)
{
  auto p(std::make_pair(st, ri));
  return std::find(cscStationsCo_.begin(), cscStationsCo_.end(), p) - cscStationsCo_.begin();
}

int DisplacedMuonTriggerRateGENSIM::detIdToMBStation(int wh,  int st)
{
  auto p(std::make_pair(wh, st));
  return std::find(dtStationsCo_.begin(), dtStationsCo_.end(),p) - dtStationsCo_.begin();
};

DisplacedMuonTriggerRateGENSIM::~DisplacedMuonTriggerRateGENSIM()
{
}

void
DisplacedMuonTriggerRateGENSIM::analyze(const edm::Event& ev, const edm::EventSetup& es)
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

  //in total three case: 1.simpt, 2 position based pt; 3 direction based pt 
 for (unsigned int k=0; k<3; k++){
   etrk_csc_[k].init();// sim
   int trk_no=0;
   for (auto& t: *sim_tracks.product()) {
     if(!isSimTrackGood(t)) continue;

     vtx_dt = sim_vert[t.vertIndex()].position().x();
     vty_dt = sim_vert[t.vertIndex()].position().y();
     vtz_dt = sim_vert[t.vertIndex()].position().z();

     SimTrackMatchManager match(t, sim_vert[t.vertIndex()], cfg_, ev, es);
     analyzeTrackEfficiency(match, trk_no, k);
    //a, l1_particles, hlt_l2_pp, l2_track, SegmentsDT);

    trk_no = trk_no + 1;
  }

  etrk_csc_[k].ntrks = trk_no;
  tree_eff_csc_[k]->Fill();
  }
  /*
   etrk_csc_[0].init();// sim
   int trk1_no=0;
   for (auto& t: *sim_tracks.product()) {
     if(!isSimTrackGood(t)) continue;

     vtx_dt = sim_vert[t.vertIndex()].position().x();
     vty_dt = sim_vert[t.vertIndex()].position().y();
     vtz_dt = sim_vert[t.vertIndex()].position().z();

     SimTrackMatchManager match(t, sim_vert[t.vertIndex()], cfg_, ev, es);
     analyzeTrackEfficiency(match, trk1_no, 1);
    //a, l1_particles, hlt_l2_pp, l2_track, SegmentsDT);

    trk1_no = trk1_no + 1;
  }
  etrk_csc_[1].ntrks = trk_no;
  tree_eff_csc_[1]->Fill();
   */

}

void 
DisplacedMuonTriggerRateGENSIM::analyzeTrackEfficiency(SimTrackMatchManager& match, int trk_no, int st)
{
  const SimHitMatcher& match_sh = match.simhits();
  //const TrackMatcher& match_track = match.tracks();
  const SimTrack &t = match_sh.trk();
  //const SimVertex &vtx = match_sh.vtx();
  const CSCRecHitMatcher& match_cscrh = match.cscRecHits();
  const HLTTrackMatcher& match_hlt_track = match.hltTracks();
  //const SimVertex& vtx = match_sh.vtx();
  auto csc_simhits(match_sh.chamberIdsCSC(0));
  //pt assignment
  float pt_position_tmp=-99;
  float pt_direction_tmp=-99;
  
 //CSC SimHits Start here
  GlobalPoint gp_sh_odd[4];
  GlobalPoint gp_sh_even[4];
  GlobalVector gv_sh_odd[4];
  GlobalVector gv_sh_even[4];
  bool has_csc_sh[4]={false,false,false,false};
  bool odd[4]={false,false,false,false};
  for(auto d: csc_simhits)
  {
    CSCDetId id(d);
    const int cscst(detIdToMEStation(id.station(),id.ring()));
    if (stationscsc_to_use_.count(cscst) == 0) continue;
    int nlayers(match_sh.nLayersWithHitsInSuperChamber(d));

    if (id.station()==1 and (id.ring()==4 or id.ring()==1)){
    int other_ring(id.ring()==4 ? 1 : 4);
    CSCDetId co_id(id.endcap(), id.station(), other_ring, id.chamber());
      auto rawId(co_id.rawId());
      if (csc_simhits.find(rawId) != csc_simhits.end()) {
        nlayers = nlayers+match_sh.nLayersWithHitsInSuperChamber(rawId);

      }
    }

    if (nlayers < 4) continue;
    
    has_csc_sh[id.station()-1]=true;
    if (id.chamber()%2==1){
	 odd[id.station()-1]=true; 
     	 gp_sh_odd[id.station()-1] = match_sh.simHitsMeanPosition(match_sh.hitsInChamber(d));
    	 gv_sh_odd[id.station()-1] = match_sh.simHitsMeanMomentum(match_sh.hitsInChamber(d));
      }else {
	 odd[id.station()-1]=false; 
     	 gp_sh_even[id.station()-1] = match_sh.simHitsMeanPosition(match_sh.hitsInChamber(d));
    	 gv_sh_even[id.station()-1] = match_sh.simHitsMeanMomentum(match_sh.hitsInChamber(d));
      }
       
  }

  int npar=-1;
  if (has_csc_sh[0] and has_csc_sh[1]){
     GlobalPoint gp1,gp2, gp3;
     GlobalVector gv1,gv2;
     if (odd[0] and not(odd[1]) and not(odd[2])){
        gp1=gp_sh_odd[0];
        gp2=gp_sh_even[1];
        gv1=gv_sh_odd[0];
        gv2=gv_sh_even[1];
	npar=0;
	if (has_csc_sh[2] and not(odd[2])) 
        	gp3=gp_sh_even[2];
     }else if (odd[0] and odd[1]) {
        gp1=gp_sh_odd[0];
        gp2=gp_sh_odd[1];
        gv1=gv_sh_odd[0];
        gv2=gv_sh_odd[1];
	npar=1;
	if (has_csc_sh[2] and odd[2]) 
        	gp3=gp_sh_odd[2];
    }else if (not(odd[0]) and not(odd[1])){
        gp1=gp_sh_even[0];
        gp2=gp_sh_even[1];
        gv1=gv_sh_even[0];
        gv2=gv_sh_even[1];
	npar=2;
	if (has_csc_sh[2] and not(odd[2])) 
        	gp3=gp_sh_even[2];
    }else if (not(odd[0]) and odd[1]){
        gp1=gp_sh_even[0];
        gp2=gp_sh_odd[1];
        gv1=gv_sh_odd[0];
        gv2=gv_sh_odd[1];
	npar=3;
	if (has_csc_sh[2] and odd[2]) 
        	gp3=gp_sh_odd[2];
     }
     float csc_bending_angle_12=deltaPhi(gv1.phi(), gv2.phi());
     if (has_csc_sh[2])
	pt_position_tmp=Ptassign_Position_gp(gp1, gp2, gp3, gp2.eta(), npar); //t.momentum().eta() 

     pt_direction_tmp=Ptassign_Direction(csc_bending_angle_12, gp2.eta(), npar);  
     std::cerr <<"case "<< st <<" eta "<< gp2.eta() <<" has csc sh st12 npar "<< npar <<" simpt "<< t.momentum().pt() <<" pt_position "<< pt_position_tmp << " pt_direction "<< pt_direction_tmp <<std::endl;
  
  } 
  etrk_csc_[st].npar = npar;
  //if (st==0 and etrk_csc_[st].pt_SimTrack>t.momentum().pt())
  if ((st==0 and etrk_csc_[st].pt_SimTrack>t.momentum().pt()) or (st==1 and etrk_csc_[st].pt_position_sh> pt_position_tmp) or (st==2 and etrk_csc_[st].pt_direction_sh>pt_direction_tmp))
	return;


   //start to record the information since it may be triggered 
    etrk_csc_[st].run = match.simhits().event().id().run();
    etrk_csc_[st].lumi = match.simhits().event().id().luminosityBlock();
    etrk_csc_[st].pt_position_sh = pt_position_tmp;
    etrk_csc_[st].pt_direction_sh = pt_direction_tmp;
    etrk_csc_[st].pt_SimTrack = t.momentum().pt();
    etrk_csc_[st].phi_SimTrack = t.momentum().phi();
    etrk_csc_[st].eta_SimTrack = t.momentum().eta();
    etrk_csc_[st].vertex_x = vtx_dt;
    etrk_csc_[st].vertex_y = vty_dt;
    etrk_csc_[st].vertex_z = vtz_dt;
    auto pphi = t.momentum().phi();
    etrk_csc_[st].dxy = vtx_dt*sin(pphi) - vty_dt*cos(pphi);
    etrk_csc_[st].pp_SimTrack= t.momentum().z();
    etrk_csc_[st].Lxy = vtx_dt*cos(pphi) + vty_dt*sin(pphi);
    etrk_csc_[st].pzvz = t.momentum().z()*vtz_dt;
    auto totalp = std::sqrt( t.momentum().x()*t.momentum().x() + t.momentum().y()*t.momentum().y() + t.momentum().z()*t.momentum().z());
    etrk_csc_[st].p_SimTrack = totalp;
    etrk_csc_[st].charge = t.charge();
    etrk_csc_[st].p_c_SimTrack = totalp*t.charge();

   

 for(auto d: csc_simhits)
 {
    CSCDetId id(d);
    const int cscst(detIdToMEStation(id.station(),id.ring()));
    if (stationscsc_to_use_.count(cscst) == 0) continue;
    int nlayers(match_sh.nLayersWithHitsInSuperChamber(d));

    if (id.station()==1 and (id.ring()==4 or id.ring()==1)){
    int other_ring(id.ring()==4 ? 1 : 4);
    CSCDetId co_id(id.endcap(), id.station(), other_ring, id.chamber());
      auto rawId(co_id.rawId());
      if (csc_simhits.find(rawId) != csc_simhits.end()) {
        nlayers = nlayers+match_sh.nLayersWithHitsInSuperChamber(rawId);

      }
    }

    if (nlayers < 4) continue;
    if (id.station() == 1){
    	etrk_csc_[st].csc_st1_nlayerscsc = nlayers;
    	etrk_csc_[st].csc_st1_ring = id.ring();
    	etrk_csc_[st].csc_st1_chamber = id.chamber();

    	GlobalPoint hitGp = match_sh.simHitsMeanPosition(match_sh.hitsInChamber(d));
    	etrk_csc_[st].csc_st1_gp_x = hitGp.x();
    	etrk_csc_[st].csc_st1_gp_y = hitGp.y();
    	etrk_csc_[st].csc_st1_gp_z = hitGp.z();
    	etrk_csc_[st].csc_st1_gp_r = hitGp.perp();
    	etrk_csc_[st].csc_st1_gp_eta = hitGp.eta();
    	etrk_csc_[st].csc_st1_gp_phi = hitGp.phi();
    	etrk_csc_[st].csc_st1_bending_sh = match_sh.LocalBendingInChamber(d);
    
    	const bool odd(id.chamber()%2==1);

    	if (odd) etrk_csc_[st].csc_st1_has_csc_sh |= 1;
    	else etrk_csc_[st].csc_st1_has_csc_sh |= 2;

    	GlobalVector ym = match_sh.simHitsMeanMomentum(match_sh.hitsInChamber(d));
    	etrk_csc_[st].csc_st1_gv_eta = ym.eta();
    	etrk_csc_[st].csc_st1_gv_phi = ym.phi();
    	etrk_csc_[st].csc_st1_gv_pt = ym.perp();
    	etrk_csc_[st].csc_st1_deltaphi = deltaPhi(hitGp.phi(), ym.phi());  //Bending Angle Position and Direction

     }

    if (id.station() == 2){
    	etrk_csc_[st].csc_st2_nlayerscsc = nlayers;
    	etrk_csc_[st].csc_st2_ring = id.ring();
    	etrk_csc_[st].csc_st2_chamber = id.chamber();

    	GlobalPoint hitGp = match_sh.simHitsMeanPosition(match_sh.hitsInChamber(d));
    	etrk_csc_[st].csc_st2_gp_x = hitGp.x();
    	etrk_csc_[st].csc_st2_gp_y = hitGp.y();
    	etrk_csc_[st].csc_st2_gp_z = hitGp.z();
    	etrk_csc_[st].csc_st2_gp_r = hitGp.perp();
    	etrk_csc_[st].csc_st2_gp_eta = hitGp.eta();
    	etrk_csc_[st].csc_st2_gp_phi = hitGp.phi();
    	etrk_csc_[st].csc_st2_bending_sh = match_sh.LocalBendingInChamber(d);
    
    	const bool odd(id.chamber()%2==1);

    	if (odd) etrk_csc_[st].csc_st2_has_csc_sh |= 1;
    	else etrk_csc_[st].csc_st2_has_csc_sh |= 2;

    	GlobalVector ym = match_sh.simHitsMeanMomentum(match_sh.hitsInChamber(d));
    	etrk_csc_[st].csc_st2_gv_eta = ym.eta();
    	etrk_csc_[st].csc_st2_gv_phi = ym.phi();
    	etrk_csc_[st].csc_st2_gv_pt = ym.perp();
    	etrk_csc_[st].csc_st2_deltaphi = deltaPhi(hitGp.phi(), ym.phi());  //Bending Angle Position and Direction

     }

     
    if (id.station() == 3){
    	etrk_csc_[st].csc_st3_nlayerscsc = nlayers;
    	etrk_csc_[st].csc_st3_ring = id.ring();
    	etrk_csc_[st].csc_st3_chamber = id.chamber();

    	GlobalPoint hitGp = match_sh.simHitsMeanPosition(match_sh.hitsInChamber(d));
    	etrk_csc_[st].csc_st3_gp_x = hitGp.x();
    	etrk_csc_[st].csc_st3_gp_y = hitGp.y();
    	etrk_csc_[st].csc_st3_gp_z = hitGp.z();
    	etrk_csc_[st].csc_st3_gp_r = hitGp.perp();
    	etrk_csc_[st].csc_st3_gp_eta = hitGp.eta();
    	etrk_csc_[st].csc_st3_gp_phi = hitGp.phi();
    	etrk_csc_[st].csc_st3_bending_sh = match_sh.LocalBendingInChamber(d);
   
    	const bool odd(id.chamber()%2==1);

    	if (odd) etrk_csc_[st].csc_st3_has_csc_sh |= 1;
    	else etrk_csc_[st].csc_st3_has_csc_sh |= 2;

    	GlobalVector ym = match_sh.simHitsMeanMomentum(match_sh.hitsInChamber(d));
    	etrk_csc_[st].csc_st3_gv_eta = ym.eta();
    	etrk_csc_[st].csc_st3_gv_phi = ym.phi();
    	etrk_csc_[st].csc_st3_gv_pt = ym.perp();
    	etrk_csc_[st].csc_st3_deltaphi = deltaPhi(hitGp.phi(), ym.phi());  //Bending Angle Position and Direction

     }

    if (id.station() == 4){
    	etrk_csc_[st].csc_st4_nlayerscsc = nlayers;
    	etrk_csc_[st].csc_st4_ring = id.ring();
    	etrk_csc_[st].csc_st4_chamber = id.chamber();

    	GlobalPoint hitGp = match_sh.simHitsMeanPosition(match_sh.hitsInChamber(d));
    	etrk_csc_[st].csc_st4_gp_x = hitGp.x();
    	etrk_csc_[st].csc_st4_gp_y = hitGp.y();
    	etrk_csc_[st].csc_st4_gp_z = hitGp.z();
    	etrk_csc_[st].csc_st4_gp_r = hitGp.perp();
    	etrk_csc_[st].csc_st4_gp_eta = hitGp.eta();
    	etrk_csc_[st].csc_st4_gp_phi = hitGp.phi();
    	etrk_csc_[st].csc_st4_bending_sh = match_sh.LocalBendingInChamber(d);
   
    	const bool odd(id.chamber()%2==1);

    	if (odd) etrk_csc_[st].csc_st4_has_csc_sh |= 1;
    	else etrk_csc_[st].csc_st4_has_csc_sh |= 2;

    	GlobalVector ym = match_sh.simHitsMeanMomentum(match_sh.hitsInChamber(d));
    	etrk_csc_[st].csc_st4_gv_eta = ym.eta();
    	etrk_csc_[st].csc_st4_gv_phi = ym.phi();
    	etrk_csc_[st].csc_st4_gv_pt = ym.perp();
    	etrk_csc_[st].csc_st4_deltaphi = deltaPhi(hitGp.phi(), ym.phi());  //Bending Angle Position and Direction

     }

 } // End of CSC Sim Hits


}

bool 
DisplacedMuonTriggerRateGENSIM::isSimTrackGood(const SimTrack &t)
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

void MyTrackRateL1::init()
{

 L1_pt = -99.;
 L1_eta = -9.;
 L1_phi = - 99.;
 L1_charge = - 9.;


} 

void MyTrackRateCSC::init()
{

 lumi = - 99;
 run = - 99;
 pt_SimTrack = - 9;
 phi_SimTrack = - 9;
 eta_SimTrack= - 9;
 vertex_x = - 9;
 vertex_y = - 9;
 vertex_z = - 9;

 dxy = - 9.;
 charge = - 9.;
 ntrks=0;
 
 Lxy = - 9999.;
 pzvz = - 999.;
 pp_SimTrack = - 99.;

 csc_st1_chamber = - 9; 
 csc_st1_ring = - 99;
 csc_st1_has_csc_sh = 0;
 csc_st1_gp_y = - 9999;
 csc_st1_gp_x = - 9999;
 csc_st1_gp_r = - 9999;
 csc_st1_gp_z = - 9999;
 csc_st1_nlayerscsc = 0;
 csc_st1_gp_eta = - 9;
 csc_st1_gp_phi = - 9;
 csc_st1_gv_eta = - 9.;
 csc_st1_gv_phi = - 9.;
 csc_st1_gv_pt = - 9.;
 csc_st1_bending_sh = -10;
 csc_st1_deltaphi = - 99;

 csc_st2_chamber = - 9; 
 csc_st2_ring = - 99;
 csc_st2_has_csc_sh = 0;
 csc_st2_gp_y = - 9999;
 csc_st2_gp_x = - 9999;
 csc_st2_gp_r = - 9999;
 csc_st2_gp_z = - 9999;
 csc_st2_nlayerscsc = 0;
 csc_st2_gp_eta = - 9;
 csc_st2_gp_phi = - 9;
 csc_st2_gv_eta = - 9.;
 csc_st2_gv_phi = - 9.;
 csc_st2_gv_pt = - 9.;
 csc_st2_bending_sh = -10;
 csc_st2_deltaphi = - 99;

 csc_st3_chamber = - 9; 
 csc_st3_ring = - 99;
 csc_st3_has_csc_sh = 0;
 csc_st3_gp_y = - 9999;
 csc_st3_gp_x = - 9999;
 csc_st3_gp_r = - 9999;
 csc_st3_gp_z = - 9999;
 csc_st3_nlayerscsc = 0;
 csc_st3_gp_eta = - 9;
 csc_st3_gp_phi = - 9;
 csc_st3_gv_eta = - 9.;
 csc_st3_gv_phi = - 9.;
 csc_st3_gv_pt = - 9.;
 csc_st3_bending_sh = -10;
 csc_st3_deltaphi = - 99;

 csc_st4_chamber = - 9; 
 csc_st4_ring = - 99;
 csc_st4_has_csc_sh = 0;
 csc_st4_gp_y = - 9999;
 csc_st4_gp_x = - 9999;
 csc_st4_gp_r = - 9999;
 csc_st4_gp_z = - 9999;
 csc_st4_nlayerscsc = 0;
 csc_st4_gp_eta = - 9;
 csc_st4_gp_phi = - 9;
 csc_st4_gv_eta = - 9.;
 csc_st4_gv_phi = - 9.;
 csc_st4_gv_pt = - 9.;
 csc_st4_bending_sh = -10;
 csc_st4_deltaphi = - 99;

 delta_x_gp_12 = - 999.;
 delta_x_gp_13 = - 999.;
 delta_x_gp_14 = - 999.;
 delta_y_gp_12 = - 999.;
 delta_y_gp_13 = - 999.;
 delta_y_gp_14 = - 999.;

 delta_x_gp_23 = - 999.;
 delta_y_gp_23 = - 999.;
 delta_x_gp_24 = - 999.;
 delta_y_gp_24 = - 999.;

 delta_x_gp_34 = - 999.;
 delta_y_gp_34 = - 999.;

 csc_deltaeta = - 99.;
 csc_deltaeta_14 = - 99.;
 csc_deltaeta_13 = - 99.;
 csc_deltaeta_12 = - 99.;



 csc_deltaphi_gp_12=-99.;
 csc_deltaphi_gp_13=-99.;
 csc_deltaphi_gp_14=-99.;
 csc_deltaphi_gp_23=-99.;
 csc_deltaphi_gp_24=-99.;
 csc_deltaphi_gp_34=-99.;


 csc_bending_angle_12 = - 99;
 csc_bending_angle_13 = - 99;
 csc_bending_angle_14 = - 99;


 npar = -1;
 pt_position_sh=-99;
 pt_direction_sh = -99;
}
void MyTrackRateDT::init()
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


}

TTree*MyTrackRateL1::book(TTree *t, const std::string & name)
{
  edm::Service< TFileService> fs;
  t = fs->make<TTree>(name.c_str(),name.c_str());
 
  t->Branch("L1_pt", &L1_pt);
  t->Branch("L1_eta", &L1_eta);
  t->Branch("L1_charge", &L1_charge);
  t->Branch("L1_phi", &L1_phi);

  return t;
}

TTree*MyTrackRateCSC::book(TTree *t, const std::string & name)
{

  edm::Service< TFileService > fs;
  t = fs->make<TTree>(name.c_str(),name.c_str());

  t->Branch("run", &run);
  t->Branch("lumi", &lumi);
  t->Branch("pt_SimTrack", &pt_SimTrack);
  t->Branch("phi_SimTrack", &phi_SimTrack);
  t->Branch("eta_SimTrack", &eta_SimTrack); 
  t->Branch("vertex_x", &vertex_x);
  t->Branch("vertex_y", &vertex_y);
  t->Branch("vertex_z", &vertex_z);

  t->Branch("dxy", &dxy);
  t->Branch("Lxy", &Lxy);
  t->Branch("pzvz", &Lxy);
  t->Branch("pp_SimTrack", &pp_SimTrack);


  t->Branch("p_SimTrack", &p_SimTrack);
  t->Branch("charge", &charge);
  t->Branch("p_c_SimTrack", &p_c_SimTrack);
  t->Branch("ntrks", &ntrks);


  t->Branch("csc_st1_ring", &csc_st1_ring);
  t->Branch("csc_st1_chamber", &csc_st1_chamber);
  t->Branch("csc_st1_gp_y", &csc_st1_gp_y);
  t->Branch("csc_st1_gp_x", &csc_st1_gp_x);
  t->Branch("csc_st1_gp_r", &csc_st1_gp_r);
  t->Branch("csc_st1_gp_z", &csc_st1_gp_z);
  t->Branch("csc_st1_gp_eta", &csc_st1_gp_eta);
  t->Branch("csc_st1_gp_phi", &csc_st1_gp_phi);
  t->Branch("csc_st1_nlayerscsc", &csc_st1_nlayerscsc);
  t->Branch("csc_st1_gv_eta", &csc_st1_gv_eta);
  t->Branch("csc_st1_gv_pt", &csc_st1_gv_pt);
  t->Branch("csc_st1_gv_phi", &csc_st1_gv_phi);
  t->Branch("csc_st1_deltaphi", &csc_st1_deltaphi);
  t->Branch("csc_st1_bending_sh", &csc_st1_bending_sh);
  t->Branch("csc_st1_has_csc_sh", &csc_st1_has_csc_sh);

  t->Branch("csc_st2_ring", &csc_st2_ring);
  t->Branch("csc_st2_chamber", &csc_st2_chamber);
  t->Branch("csc_st2_gp_y", &csc_st2_gp_y);
  t->Branch("csc_st2_gp_x", &csc_st2_gp_x);
  t->Branch("csc_st2_gp_r", &csc_st2_gp_r);
  t->Branch("csc_st2_gp_z", &csc_st2_gp_z);
  t->Branch("csc_st2_gp_eta", &csc_st2_gp_eta);
  t->Branch("csc_st2_gp_phi", &csc_st2_gp_phi);
  t->Branch("csc_st2_nlayerscsc", &csc_st2_nlayerscsc);
  t->Branch("csc_st2_gv_eta", &csc_st2_gv_eta);
  t->Branch("csc_st2_gv_pt", &csc_st2_gv_pt);
  t->Branch("csc_st2_gv_phi", &csc_st2_gv_phi);
  t->Branch("csc_st2_deltaphi", &csc_st2_deltaphi);
  t->Branch("csc_st2_bending_sh", &csc_st2_bending_sh);
  t->Branch("csc_st2_has_csc_sh", &csc_st2_has_csc_sh);

  t->Branch("csc_st3_ring", &csc_st3_ring);
  t->Branch("csc_st3_chamber", &csc_st3_chamber);
  t->Branch("csc_st3_gp_y", &csc_st3_gp_y);
  t->Branch("csc_st3_gp_x", &csc_st3_gp_x);
  t->Branch("csc_st3_gp_r", &csc_st3_gp_r);
  t->Branch("csc_st3_gp_z", &csc_st3_gp_z);
  t->Branch("csc_st3_gp_eta", &csc_st3_gp_eta);
  t->Branch("csc_st3_gp_phi", &csc_st3_gp_phi);
  t->Branch("csc_st3_nlayerscsc", &csc_st3_nlayerscsc);
  t->Branch("csc_st3_gv_eta", &csc_st3_gv_eta);
  t->Branch("csc_st3_gv_pt", &csc_st3_gv_pt);
  t->Branch("csc_st3_gv_phi", &csc_st3_gv_phi);
  t->Branch("csc_st3_deltaphi", &csc_st3_deltaphi);
  t->Branch("csc_st3_bending_sh", &csc_st3_bending_sh);
  t->Branch("csc_st3_has_csc_sh", &csc_st3_has_csc_sh);

  t->Branch("csc_st4_ring", &csc_st4_ring);
  t->Branch("csc_st4_chamber", &csc_st4_chamber);
  t->Branch("csc_st4_gp_y", &csc_st4_gp_y);
  t->Branch("csc_st4_gp_x", &csc_st4_gp_x);
  t->Branch("csc_st4_gp_r", &csc_st4_gp_r);
  t->Branch("csc_st4_gp_z", &csc_st4_gp_z);
  t->Branch("csc_st4_gp_eta", &csc_st4_gp_eta);
  t->Branch("csc_st4_gp_phi", &csc_st4_gp_phi);
  t->Branch("csc_st4_nlayerscsc", &csc_st4_nlayerscsc);
  t->Branch("csc_st4_gv_eta", &csc_st4_gv_eta);
  t->Branch("csc_st4_gv_pt", &csc_st4_gv_pt);
  t->Branch("csc_st4_gv_phi", &csc_st4_gv_phi);
  t->Branch("csc_st4_deltaphi", &csc_st4_deltaphi);
  t->Branch("csc_st4_bending_sh", &csc_st4_bending_sh);
  t->Branch("csc_st4_has_csc_sh", &csc_st4_has_csc_sh);


  t->Branch("delta_x_gp_12", &delta_x_gp_12);
  t->Branch("delta_y_gp_12", &delta_y_gp_12);
  t->Branch("delta_x_gp_13", &delta_x_gp_13);
  t->Branch("delta_y_gp_14", &delta_y_gp_14);
  t->Branch("delta_x_gp_13", &delta_x_gp_13);
  t->Branch("delta_y_gp_14", &delta_y_gp_14);

  t->Branch("delta_y_gp_23", &delta_y_gp_23);
  t->Branch("delta_x_gp_23", &delta_x_gp_23);
  t->Branch("delta_y_gp_24", &delta_y_gp_24);
  t->Branch("delta_x_gp_24", &delta_x_gp_24);

  t->Branch("delta_x_gp_34", &delta_x_gp_34);
  t->Branch("delta_y_gp_34", &delta_y_gp_34);

  t->Branch("csc_deltaphi_gp_12", &csc_deltaphi_gp_12);
  t->Branch("csc_deltaphi_gp_13", &csc_deltaphi_gp_13);
  t->Branch("csc_deltaphi_gp_14", &csc_deltaphi_gp_14);
  t->Branch("csc_deltaphi_gp_23", &csc_deltaphi_gp_23);
  t->Branch("csc_deltaphi_gp_24", &csc_deltaphi_gp_24);
  t->Branch("csc_deltaphi_gp_34", &csc_deltaphi_gp_34);



  t->Branch("csc_bending_angle_12", &csc_bending_angle_12);
  t->Branch("csc_bending_angle_13", &csc_bending_angle_13);
  t->Branch("csc_bending_angle_14", &csc_bending_angle_14);

  t->Branch("csc_p_over_cosh_eta", &csc_p_over_cosh_eta);

  t->Branch("csc_deltaeta_14", &csc_deltaeta_14);
  t->Branch("csc_deltaeta", &csc_deltaeta);
  t->Branch("csc_deltaeta_13", &csc_deltaeta_13);
  t->Branch("csc_deltaeta_12", &csc_deltaeta_12);

  t->Branch("npar", &npar);
  t->Branch("pt_position_sh", &pt_position_sh);
  t->Branch("pt_direction_sh", &pt_direction_sh);
  return t;
}

TTree*MyTrackRateDT::book(TTree *t,const std::string & name)
{
  edm::Service< TFileService > fs;
  t = fs->make<TTree>(name.c_str(),name.c_str());

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



  return t;


}


void
DisplacedMuonTriggerRateGENSIM::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(DisplacedMuonTriggerRateGENSIM);
