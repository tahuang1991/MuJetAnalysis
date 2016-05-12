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
#include "FWCore/Utilities/interface/RandomNumberGenerator.h"
#include "CLHEP/Random/RandomEngine.h"
#include "CLHEP/Random/Randomize.h"
//#include "CLHEP/config/iostream.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Utilities/interface/Exception.h"


#include "GEMCode/GEMValidation/interface/SimTrackMatchManager.h"
#include "MuJetAnalysis/HLTBendingAngle/interface/Ptassignment.h"
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
 Float_t eta_SimTrack;
 Float_t phi_SimTrack;
 Float_t pt_SimTrack;
 Float_t vertex_x;
 Float_t vertex_y;
 Float_t vertex_z;
 Float_t dxy; 
 Int_t csc_station;
 Int_t csc_ring;
 Int_t csc_chamber;
 Int_t nlayerscsc;
 
 Int_t endcap_st1;
 Int_t endcap_st2;
 Int_t endcap_st3;
 Int_t endcap_st4;
 Float_t Lxy;
 Float_t pzvz;
 Float_t pp_SimTrack;

 Float_t p_SimTrack;
 Float_t p_c_SimTrack;
 Float_t charge;
 Float_t deltaphi_gp_12;
 Float_t bending_sh_st1;
 Float_t bending_sh_st2;
 Float_t elliptic_value;
 Float_t elliptic_value_st2;

 Float_t csc_gv_eta;
 Float_t csc_gv_phi;
 Float_t csc_gv_pt;
 Float_t csc_gp_r;
 Float_t csc_gp_x;
 Float_t csc_gp_y;
 Float_t csc_gp_z;
 Float_t csc_gp_eta;
 Float_t csc_gp_phi;
 Float_t csc_deltaphi_gp;
 Float_t csc_deltaphi;
 Int_t has_delta_y;
 Float_t delta_y_23_12;
 Float_t delta_x_23_12;
 Float_t delta_y_24_12;
 Float_t delta_x_24_12;
 Int_t has_delta_y_4;

 Float_t Reco_pT_Position;
 Float_t Reco_pT_Direction;
 Float_t Reco_pT_Direction_Smeared;


 Float_t DeltaPhi_Smeared_03_07;
 Float_t DeltaPhi_Smeared_3_7;
 Float_t DeltaPhi_Smeared_6_14;
 Float_t DeltaPhi_Smeared_30_70;


 Float_t Reco_pT_Direction_Smeared_3_7;
 Float_t Reco_pT_Direction_Smeared_6_14;
 Float_t Reco_pT_Direction_Smeared_9_21; 
 Float_t Reco_pT_Direction_Smeared_12_28; 
 Float_t Reco_pT_Direction_Smeared_15_35;
 Float_t Reco_pT_Direction_Smeared_18_42; 
 Float_t Reco_pT_Direction_Smeared_21_49;
 Float_t Reco_pT_Direction_Smeared_24_56;
 Float_t Reco_pT_Direction_Smeared_27_63;
 Float_t Reco_pT_Direction_Smeared_30_70;
 Float_t Reco_pT_Direction_Smeared_03_07;


 Int_t has_pT_Direction;
 Int_t has_pT_Position;
 Int_t csc_chamber_st4;
 Int_t csc_chamber_st3;
 Int_t csc_chamber_st2;
 Int_t nlayers_st2;
 Int_t nlayers_st3;
 Int_t nlayers_st4;
 Float_t csc_gp_second_st3;
 Float_t csc_gp_second_st2;
 Float_t csc_gp_second_st4;
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
 Int_t has_csc_12;
 Int_t has_csc_13;
 Int_t has_csc_14;
 Int_t has_csc_23;
 Int_t has_csc_24;
 Int_t has_csc_34;


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
 Int_t wheel;
 Int_t station;




};


class HLTBendingAngle : public edm::EDAnalyzer 
{
public:
  explicit HLTBendingAngle(const edm::ParameterSet&);
  ~HLTBendingAngle();
  
  virtual void analyze(const edm::Event&, const edm::EventSetup&) ;
  
  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
  
private:
  
  void analyzeTrackEfficiency(SimTrackMatchManager& match, int trk_no, const edm::Event&);
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
   for (auto& t: sim_track) {
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
     analyzeTrackEfficiency(match, trk_no, ev);
    //a, l1_particles, hlt_l2_pp, l2_track, SegmentsDT);

    trk_no = trk_no + 1;
  }
}

void 
HLTBendingAngle::analyzeTrackEfficiency(SimTrackMatchManager& match, int trk_no,  const edm::Event& ev )
{
  const SimHitMatcher& match_sh = match.simhits();
  //const TrackMatcher& match_track = match.tracks();
  const SimTrack &t = match_sh.trk();
  //const SimVertex &vtx = match_sh.vtx();
  //const CSCRecHitMatcher& match_cscrh = match.cscRecHits();
  //const HLTTrackMatcher& match_hlt_track = match.hltTracks();
  //const SimVertex& vtx = match_sh.vtx();

  for(auto st: stationscsc_to_use_)
  {
    etrk_csc_[st].init();
    etrk_csc_[st].run = match.simhits().event().id().run();
    etrk_csc_[st].lumi = match.simhits().event().id().luminosityBlock();
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
  }


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

    if (nlayers < 4) continue;
    etrk_csc_[st].nlayerscsc = nlayers;
    etrk_csc_[st].csc_station = id.station();
    etrk_csc_[1].csc_station = id.station();
    etrk_csc_[st].csc_chamber = id.chamber();
    etrk_csc_[st].csc_ring = id.ring();
    etrk_csc_[1].csc_ring = id.ring();

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


    float local_bending = match_sh.LocalBendingInChamber(d);
    etrk_csc_[st].bending_sh_st1 = local_bending;



    //std::cout<<" There's hit on ME "<<id.station()<<id.ring()<<" Chamber :"<<id.chamber()<<" with eta: "<<t.momentum().eta()<<" pT: "<<t.momentum().pt()<<std::endl;
    //std::cout<<"              This has GP eta: "<<hitGp.eta()<<" and GV eta: "<<ym.eta()<<" And phi: "<<ym.phi()<<std::endl;

    // Case ME11
    if(id.station()==1){
        etrk_csc_[1].nlayerscsc = nlayers;
        etrk_csc_[1].bending_sh_st1 = local_bending;
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
	etrk_csc_[1].csc_chamber = id.chamber();
	auto totalp = std::sqrt( t.momentum().x()*t.momentum().x() + t.momentum().y()*t.momentum().y() + t.momentum().z()*t.momentum().z());
	etrk_csc_[1].csc_p_over_cosh_eta = totalp/cosh(std::abs(hitGp.eta()));
	etrk_csc_[1].endcap_st1 = id.endcap();
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
	if(id.station() == s_id.station()) continue; // no double hits in the same station, ME11 included by default. 
	if (s_nlayers < 4) continue;

        GlobalPoint hitGp2 = match_sh.simHitsMeanPosition(match_sh.hitsInChamber(s_d));
        GlobalVector ym2 = match_sh.simHitsMeanMomentum(match_sh.hitsInChamber(s_d));


	// Calculate here the p_T from Direction 
	
	
	
        std::cout<<" Passes here second loop: "<<std::endl;

	// Special case for ME1
        if(id.station()==1 ){


            if(s_id.station()==2){

    		float local_bending_st2 = match_sh.LocalBendingInChamber(s_d);
        	etrk_csc_[1].bending_sh_st2 = local_bending_st2;
        	etrk_csc_[st].bending_sh_st2 = local_bending_st2;


		float anglea =   hitGp2.phi();
            	float newxst1 =  hitGp.x()*cos(anglea) + hitGp.y()*sin(anglea);
	        float newyst1 = -hitGp.x()*sin(anglea) + hitGp.y()*cos(anglea);
		float newxst2 =  hitGp2.x()*cos(anglea) + hitGp2.y()*sin(anglea);
                float newyst2 = -hitGp2.x()*sin(anglea) + hitGp2.y()*cos(anglea);
		



		//std::cout<<" Passed csc 12 requirement "<<std::endl;
		etrk_csc_[1].delta_x_gp_12 = newxst2 - newxst1;
		etrk_csc_[st].delta_x_gp_12 = newxst2 - newxst1;
		etrk_csc_[st].delta_y_gp_12 = newyst2 - newyst1;
		etrk_csc_[1].delta_y_gp_12 = newyst2 - newyst1;

		etrk_csc_[1].endcap_st2 = s_id.endcap();
		etrk_csc_[st].endcap_st2 = s_id.endcap();

                etrk_csc_[1].csc_bending_angle_12 = deltaPhi(ym.phi(), ym2.phi());
                etrk_csc_[st].csc_bending_angle_12 = deltaPhi(ym.phi(), ym2.phi());
                etrk_csc_[1].has_csc_12 = 1;
                etrk_csc_[st].has_csc_12 = 1;                                                     // Ask for this
                etrk_csc_[st].csc_deltaeta_12 = ym.eta() - ym2.eta();
                etrk_csc_[1].csc_deltaeta_12 = ym.eta() - ym2.eta();
		etrk_csc_[1].csc_gp_second_st2 = hitGp2.eta();
		etrk_csc_[st].csc_gp_second_st2 = hitGp2.eta();

		etrk_csc_[st].nlayers_st2 = s_nlayers;
		etrk_csc_[1].nlayers_st2 = s_nlayers;

		etrk_csc_[st].csc_chamber_st2 = s_id.chamber();
		etrk_csc_[1].csc_chamber_st2 = s_id.chamber();
		etrk_csc_[1].csc_deltaphi_gp_12 = deltaPhi(hitGp.phi(),hitGp2.phi());
		etrk_csc_[st].csc_deltaphi_gp_12 = deltaPhi(hitGp.phi(),hitGp2.phi());

		float deltaphi_global = deltaPhi(hitGp.phi(),hitGp2.phi());
		//edm::Service<edm::RandomNumberGenerator> RandGauss;
		//CLHEP::HepRandomEngine& engine = RandGauss->getEngine(ev.streamID());
	


                double first_3 = CLHEP::RandGauss::shoot(ym.phi(), .003);
                double second_7 = CLHEP::RandGauss::shoot(ym2.phi(), .007);
                double delta_phi_smeared_3_7 = deltaPhi(first_3, second_7);


                double first_6 = CLHEP::RandGauss::shoot(ym.phi(), .006);
                double second_14 = CLHEP::RandGauss::shoot(ym2.phi(), .014);
                double delta_phi_smeared_6_14 = deltaPhi(first_6, second_14);


		double first_9 = CLHEP::RandGauss::shoot(ym.phi(), .009);
		double second_21 = CLHEP::RandGauss::shoot(ym2.phi(), .021);
		double delta_phi_smeared_9_21 = deltaPhi(first_9, second_21);


                double first_12 = CLHEP::RandGauss::shoot(ym.phi(), .012);
                double second_28 = CLHEP::RandGauss::shoot(ym2.phi(), .028);
                double delta_phi_smeared_12_28 = deltaPhi(first_12, second_28);


                double first_15 = CLHEP::RandGauss::shoot(ym.phi(), .015);
                double second_35 = CLHEP::RandGauss::shoot(ym2.phi(), .035);
                double delta_phi_smeared_15_35 = deltaPhi(first_15, second_35);

                double first_18 = CLHEP::RandGauss::shoot(ym.phi(), .018);
                double second_42 = CLHEP::RandGauss::shoot(ym2.phi(), .042);
                double delta_phi_smeared_18_42 = deltaPhi(first_18, second_42);

                double first_21 = CLHEP::RandGauss::shoot(ym.phi(), .021);
                double second_49 = CLHEP::RandGauss::shoot(ym2.phi(), .049);
                double delta_phi_smeared_21_49 = deltaPhi(first_21, second_49);


                double first_24 = CLHEP::RandGauss::shoot(ym.phi(), .024);
                double second_56 = CLHEP::RandGauss::shoot(ym2.phi(), .056);
                double delta_phi_smeared_24_56 = deltaPhi(first_24, second_56);


                double first_27 = CLHEP::RandGauss::shoot(ym.phi(), .027);
                double second_63 = CLHEP::RandGauss::shoot(ym2.phi(), .063);
                double delta_phi_smeared_27_63 = deltaPhi(first_27, second_63);


                double first_30 = CLHEP::RandGauss::shoot(ym.phi(), .030);
                double second_70 = CLHEP::RandGauss::shoot(ym2.phi(), .070);
                double delta_phi_smeared_30_70 = deltaPhi(first_30, second_70);


                double first_03 = CLHEP::RandGauss::shoot(ym.phi(), .0003);
                double second_07 = CLHEP::RandGauss::shoot(ym2.phi(), .0007);
                double delta_phi_smeared_03_07 = deltaPhi(first_03, second_07);


		
		etrk_csc_[1].DeltaPhi_Smeared_03_07 = deltaPhi(first_03, second_07);
		etrk_csc_[1].DeltaPhi_Smeared_3_7 = deltaPhi(first_3, second_7);
		etrk_csc_[1].DeltaPhi_Smeared_6_14 = deltaPhi(first_6, second_14);
		etrk_csc_[1].DeltaPhi_Smeared_30_70 = deltaPhi(first_30, second_70);


		float csc_bending_angle_variable = deltaPhi(ym.phi(), ym2.phi());
		float delta_y_gp_12_variable = newyst2 - newyst1;

		std::cout<<" Initial delta phi: "<<csc_bending_angle_variable<<" smeared value: "<<delta_phi_smeared_03_07<<std::endl;

		for(auto t_d: csc_simhits)
		{
	        	CSCDetId t_id(t_d);
	        	const int t_st(detIdToMEStation(t_id.station(),t_id.ring()));
        		if (stationscsc_to_use_.count(t_st) == 0) continue;
		        int t_nlayers(match_sh.nLayersWithHitsInSuperChamber(t_d));

			if (t_nlayers < 4) continue;

			if (t_id.station()==1) continue;
			if (t_id.station()==2) continue;
			if (t_id.station()==4) continue;


			std::cout<<" Passes 123 requirement "<<std::endl;
		        GlobalPoint hitGp3 = match_sh.simHitsMeanPosition(match_sh.hitsInChamber(t_d));
			float ysst3 = -hitGp3.x()*sin(anglea) + hitGp3.y()*cos(anglea);
			float xsst3 = hitGp3.x()*cos(anglea) + hitGp3.y()*sin(anglea);
			
			etrk_csc_[st].has_delta_y = 1;
			etrk_csc_[1].has_delta_y = 1;

			etrk_csc_[1].delta_y_23_12 =  ysst3 - newyst2;
			etrk_csc_[st].delta_y_23_12 =  ysst3 - newyst2;
			etrk_csc_[st].delta_x_23_12 =  xsst3 - newxst2;
			etrk_csc_[1].delta_x_23_12 =  xsst3 - newxst2;


			float delta_y_gp_23_variable =  ysst3 - newyst2;


			int parity_case = -1;

			if (id.chamber()%2 == 1){
				if (s_id.chamber()%2==0 and t_id.chamber()%2==0) parity_case = 0;
				if (s_id.chamber()%2==1 and t_id.chamber()%2==1) parity_case = 1;

			} 
			if (id.chamber()%2 == 0) {
				if (s_id.chamber()%2==0 and t_id.chamber()%2==0) parity_case = 2;
				if (s_id.chamber()%2==1 and t_id.chamber()%2==1) parity_case = 3;

			}


			if(parity_case == -1){
				std::cout<<" Error in the parity assignment -- Continue"<<std::endl;
				continue;
			}

			float etamin = 0.0;
			int neta=-1;


			//std::cout<<" Before eta calculation "<<std::endl;

			if( fabs(hitGp2.eta())>1.6 and fabs(hitGp2.eta()<1.8)) neta = 2;
			if( fabs(hitGp2.eta())>1.8 and fabs(hitGp2.eta()<2.0)) neta = 3;
			if( fabs(hitGp2.eta())>2.0 and fabs(hitGp2.eta()<2.2)) neta = 4;
			if( fabs(hitGp2.eta())>2.2 and fabs(hitGp2.eta()<2.4)) neta = 5;
			if( fabs(hitGp2.eta())>1.6 and fabs(hitGp2.eta()<1.8)) etamin = 1.6;
			if( fabs(hitGp2.eta())>1.8 and fabs(hitGp2.eta()<2.0)) etamin = 1.8;
			if( fabs(hitGp2.eta())>2.0 and fabs(hitGp2.eta()<2.2)) etamin = 2.0;
			if( fabs(hitGp2.eta())>2.2 and fabs(hitGp2.eta()<2.4)) etamin = 2.2;

			if(neta == -1){
				std::cout<<" Error in the eta measurement -- Continue "<<std::endl;
				continue;
			}



			std::cout<<" Passes to calculation of pT with neta: "<<neta<<" and parity_case: "<<parity_case<<std::endl;
			std::cout<<" etamin "<< etamin << ((etamin==float(1.6))?" 1.6 true ":" 1.6 false ") << ((etamin==float(1.8))?" 1.8 true ":" 1.8 false ")<< ((etamin==float(2.0))?" 2.0 true ":" 2.0 false ")<< ((etamin==float(2.2))?" 2.2 true ":" 2.2 false ") << std::endl;

	                float sigma_phi = 0.0;
                	float slope_phi = 0.0;
                	float intercept_phi = 0.0;
                
			float slope_phi_03_07 = 0.;
			float intercept_phi_03_07 = 0.;
			float slope_phi_3_7 = 0.;
			float intercept_phi_3_7 = 0.;
			float slope_phi_30_70 = 0.;
			float intercept_phi_30_70 = 0.;
			float slope_phi_6_14 = 0.;
			float intercept_phi_6_14 = 0.;
                	if (parity_case ==0){
				std::cout <<" pariry_case 0 "<< "etamin "<< neta <<std::endl;
                        	if (neta == 2){
	                            sigma_phi = 0.03583;
        	                    slope_phi = 4.53;
                	            intercept_phi = 9.422;

				    slope_phi_03_07 = 8.332;
				    intercept_phi_03_07 = -18.13;
				    slope_phi_3_7 = 6.015;
				    intercept_phi_3_7 = -8.998;
				    slope_phi_6_14 = 7.003;
				    intercept_phi_6_14 = -15.09;
				    slope_phi_30_70 = 3.554;
				    intercept_phi_30_70 = -5.732;
				std::cout <<" pariry_case 0 "<< "if etamin "<< etamin <<" slope_phi "<< slope_phi<<" intercept_phi "<< intercept_phi << std::endl;

				}
	                        if (neta == 3){
        	                    slope_phi = 5.788;
                	            intercept_phi = 9.743;
                        	    sigma_phi = 0.04496;

                                    slope_phi_03_07 = 8.926;
                                    intercept_phi_03_07 =-17.72;
                                    slope_phi_3_7 = 6.777;
                                    intercept_phi_3_7 =-8.605;
                                    slope_phi_6_14 = 4.7;
                                    intercept_phi_6_14 =0.6635;
                                    slope_phi_30_70 = 2.652;
                                    intercept_phi_30_70 =0.2292;
				std::cout <<" pariry_case 0 "<< "if etamin "<< etamin <<" slope_phi "<< slope_phi<<" intercept_phi "<< intercept_phi << std::endl;


				}
	                        if (neta == 4){
        	                    sigma_phi = 0.05328;
                	            slope_phi = 8.367;
                        	    intercept_phi = 10.22;

                                    slope_phi_03_07 =10.97;
                                    intercept_phi_03_07 =-15.35;
                                    slope_phi_3_7 =7.448;
                                    intercept_phi_3_7 =1.17;
                                    slope_phi_6_14 =3.575;
                                    intercept_phi_6_14 =20.95;
                                    slope_phi_30_70 =1.509;
                                    intercept_phi_30_70 =8.654;
				std::cout <<" pariry_case 0 "<< "if etamin "<< etamin <<" slope_phi "<< slope_phi<<" intercept_phi "<< intercept_phi << std::endl;

				}
	                        if (neta == 5){
        	                    sigma_phi = 0.05832;
                	            slope_phi = 11.02;
                        	    intercept_phi = 14.84;


                                    slope_phi_03_07 = 11.65;
                                    intercept_phi_03_07 =-16.24;
                                    slope_phi_3_7 = 7.112;
                                    intercept_phi_3_7 =9.354;
                                    slope_phi_6_14 =3.293;
                                    intercept_phi_6_14 =27.21;
                                    slope_phi_30_70 =0.9409;
                                    intercept_phi_30_70 =13.37;
					
				std::cout <<" pariry_case 0 "<< "if etamin "<< etamin <<" slope_phi "<< slope_phi<<" intercept_phi "<< intercept_phi << std::endl;

				}
				std::cout <<" pariry_case 0 "<< "etamin "<< etamin <<" slope_phi "<< slope_phi<<" intercept_phi "<< intercept_phi << std::endl;

			}
	                if (parity_case ==1 ){
				std::cout <<" pariry_case 1 "<< " etamin "<< etamin << std::endl;
        	                //if (etamin == 1.6){
                        	if (neta == 2){
                	            sigma_phi = 0.03948;
                        	    slope_phi = 4.779;
	                            intercept_phi = 9.954;

                                    slope_phi_03_07 = 7.545;
                                    intercept_phi_03_07 = -15.03;
                                    slope_phi_3_7 = 5.835;
                                    intercept_phi_3_7 = - 9.2;
                                    slope_phi_6_14 = 5.639;
                                    intercept_phi_6_14 = - 9.791;
                                    slope_phi_30_70 = 4.224;
                                    intercept_phi_30_70 = -7.633;



				}
        	                //if (etamin == 1.8){
                        	if (neta == 3){
                	            sigma_phi = 0.04381;
                        	    slope_phi= 6.273;
	                            intercept_phi = 11.91;

                                    slope_phi_03_07 = 7.979;
                                    intercept_phi_03_07 =-15.14;
                                    slope_phi_3_7 = 6.509;
                                    intercept_phi_3_7 =-8.294;
                                    slope_phi_6_14 = 3.28;
                                    intercept_phi_6_14 =12.92;
                                    slope_phi_30_70 = 2.661;
                                    intercept_phi_30_70 =2.661;


				}
        	                //if (etamin == 2.0){
                        	if (neta == 4){
                	            sigma_phi = 0.0557;
                        	    slope_phi = 9.315;
	                            intercept_phi =12.21;


                                    slope_phi_03_07 = 11.;
                                    intercept_phi_03_07 =-18.05;
                                    slope_phi_3_7 =7.727;
                                    intercept_phi_3_7 =-2.885;
                                    slope_phi_6_14 =3.432;
                                    intercept_phi_6_14 =19.09;
                                    slope_phi_30_70 =2.434;
                                    intercept_phi_30_70 =4.157;

				}
        	                //if (etamin == 2.2){
                        	if (neta == 5){
                	            sigma_phi = 0.06099;
                        	    slope_phi = 10.34;
	                            intercept_phi = 11.02;

                                    slope_phi_03_07 = 11.96;
                                    intercept_phi_03_07 =-16.66;
                                    slope_phi_3_7 = 6.087;
                                    intercept_phi_3_7 =17.15;
                                    slope_phi_6_14 = 3.3;
                                    intercept_phi_6_14 =25.51;
                                    slope_phi_30_70 =1.97;
                                    intercept_phi_30_70 =8.397;


				}
				std::cout <<" pariry_case 1 "<< "etamin "<< etamin <<" slope_phi "<< slope_phi<<" intercept_phi "<< intercept_phi << std::endl;
                        }
        	        if ( parity_case ==2 ){
				std::cout <<" pariry_case 2 "<< " etamin "<< etamin <<std::endl;
                	        //if (etamin == 1.6){
                        	if (neta == 2){
                        	    sigma_phi = 0.05226;
	                            slope_phi = 7.677;
        	                    intercept_phi =16.82;




                                    slope_phi_03_07 = 4.771;
                                    intercept_phi_03_07 = -10.11;
                                    slope_phi_3_7 = 5.524;
                                    intercept_phi_3_7 = -12.05;
                                    slope_phi_6_14 = 4.735;
                                    intercept_phi_6_14 = - 10.07;
                                    slope_phi_30_70 = 2.984;
                                    intercept_phi_30_70 = - 4.306;

				}
                	        //if ( etamin == 1.8){
                        	if (neta == 3){
                        	    sigma_phi = 0.04987;
	                            slope_phi= 7.726;
        	                    intercept_phi = 13.36;


                                    slope_phi_03_07 = 6.644;
                                    intercept_phi_03_07 =-13.71;
                                    slope_phi_3_7 = 6.094;
                                    intercept_phi_3_7 = - 11.72;
                                    slope_phi_6_14 = 4.049;
                                    intercept_phi_6_14 = - 0.4039;
                                    slope_phi_30_70 = 3.188;
                                    intercept_phi_30_70 =-3.364;

				}
                	        //if (etamin == 2.0){
                        	if (neta == 4){
                        	    sigma_phi = 0.06021;
	                            slope_phi = 9.621;
        	                    intercept_phi =10.62;

                                    slope_phi_03_07 =9.387;
                                    intercept_phi_03_07 =-12.4;
                                    slope_phi_3_7 = 5.593;
                                    intercept_phi_3_7 =10.12;
                                    slope_phi_6_14 =3.409;
                                    intercept_phi_6_14 =17.62;
                                    slope_phi_30_70 =2.697;
                                    intercept_phi_30_70 =2.567;

				}
                	        //if (etamin == 2.2){
                        	if (neta == 5){
                        	    sigma_phi = 0.05825;
	                            slope_phi = 11.23;
        	                    intercept_phi = 13.44;


                                    slope_phi_03_07 = 11.12;
                                    intercept_phi_03_07 = -12.63;
                                    slope_phi_3_7 = 7.845;
                                    intercept_phi_3_7 =1.213;
                                    slope_phi_6_14 =3.277;
                                    intercept_phi_6_14 =28.02;
                                    slope_phi_30_70 = 1.451;
                                    intercept_phi_30_70 =9.471;

				}
				std::cout <<" pariry_case 2 "<< "etamin "<< etamin <<" slope_phi "<< slope_phi<<" intercept_phi "<< intercept_phi << std::endl;
			}
        	        if (parity_case ==3 ){
				std::cout <<" pariry_case 3 "<< " etamin "<< etamin <<std::endl;
                	        //if (etamin == 1.6){
                        	if (neta == 2){
                        	    sigma_phi = 0.04902;
	                            slope_phi = 7.72;
        	                    intercept_phi = 16.91;

                                    slope_phi_03_07 = 4.677;
                                    intercept_phi_03_07 = - 9.775;
                                    slope_phi_3_7 = 4.622;
                                    intercept_phi_3_7 = -9.637;
                                    slope_phi_6_14 = 4.081;
                                    intercept_phi_6_14 = -7.384;
                                    slope_phi_30_70 = 3.196;
                                    intercept_phi_30_70 =5.167;


				}
                	        //if (etamin == 1.8){
                        	if (neta == 3){
                        	    sigma_phi = 0.04995;
	                            slope_phi = 8.643;
        	                    intercept_phi = 16.45;


                                    slope_phi_03_07 = 6.257;
                                    intercept_phi_03_07 =-12.12;
                                    slope_phi_3_7 = 5.419;
                                    intercept_phi_3_7 =-7.962;
                                    slope_phi_6_14 = 3.614;
                                    intercept_phi_6_14 =1.553;
                                    slope_phi_30_70 =2.519;
                                    intercept_phi_30_70 =-0.02093;

				}
                	        //if (etamin == 2.0){
                        	if (neta == 4){
                        	    sigma_phi = 0.05696;
	                            slope_phi = 10.02;
        	                    intercept_phi =11.83;


                                    slope_phi_03_07 =8.544;
                                    intercept_phi_03_07 =-11.85;
                                    slope_phi_3_7 =5.916;
                                    intercept_phi_3_7 =1.654;
                                    slope_phi_6_14 =2.932;
                                    intercept_phi_6_14 =20.77;
                                    slope_phi_30_70 =3.137;
                                    intercept_phi_30_70 =0.7447;

				}
                	        //if (etamin == 2.2){
                        	if (neta == 5){
                        	    sigma_phi = 0.05652;
	                            slope_phi = 11.83;
        	                    intercept_phi = 17.66;


                                    slope_phi_03_07 = 10.61;
                                    intercept_phi_03_07 =-10.52;
                                    slope_phi_3_7 = 6.667;
                                    intercept_phi_3_7 =7.642;
                                    slope_phi_6_14 =3.727;
                                    intercept_phi_6_14 =19.85;
                                    slope_phi_30_70 = 1.252;
                                    intercept_phi_30_70 =10.23;

				}
				std::cout <<" pariry_case 3 "<< "etamin "<< etamin <<" slope_phi "<< slope_phi<<" intercept_phi "<< intercept_phi << std::endl;
	
			}

 	               float slope = 0.0;
 	               float intercept = 0.0;
 	               float prop = 0.0;
	               float sigma= 0.0;

		       float slope_elliptic_Tao = 0.0;
		       float slope_Tao_st2 = 0.0;
 	               if (parity_case ==0 ){
				slope_elliptic_Tao = -13.38;
				slope_Tao_st2 = -21.28;
        	                prop = 0.6484;
                	        //if (etamin == 1.6){
                        	if (neta == 2){
                        	    sigma = 0.01319;
	                            slope = 0.05527;
        	                    intercept = 0.08944;
				}
                	        //if (etamin == 1.8){
                        	if (neta == 3){
                        	    sigma = 0.02154;
	                            slope= 0.08295;
        	                    intercept = 0.1279;
				}
                	        //if (etamin == 2.0){
                        	if (neta == 4){
                        	    sigma = 0.03251;
	                            slope = 0.166;
        	                    intercept = 0.2158;
				}
                	        //if (etamin == 2.2){
                        	if (neta == 5){
                        	    sigma = 0.05515;
	                            slope = 0.4952;
        	                    intercept = 0.7103;
				}

			}
        	        if (parity_case ==1 ){
				slope_elliptic_Tao = -14.7;
				slope_Tao_st2 = -24.54;
                	        prop = 0.3542;
                        	//if (etamin == 1.6){
                        	if (neta == 2){
	                            sigma = 0.01014;
        	                    slope = 0.1067;
                	            intercept = 0.1957;
				}
                        	//if (etamin == 1.8){
                        	if (neta == 3){
	                            sigma = 0.01997;
        	                    slope= 0.1561;
                	            intercept = 0.2654;
				}
                        	//if (etamin == 2.0){
                        	if (neta == 4){
 	                           sigma = 0.03619;
        	                    slope = 0.3156;
                	            intercept = 0.4514;
				}
	                        //if (etamin == 2.2){
                        	if (neta == 5){
        	                    sigma = 0.05695;
                	            slope = 0.8242;
                        	    intercept = 1.071;
				}
			}
	                if (parity_case ==2 ){
				slope_elliptic_Tao = -14.71;
				slope_Tao_st2 = -25.56;
        	                prop = 0.5636;
                	        //if (etamin == 1.6){
                        	if (neta == 2){
                        	    sigma = 0.008583;
	                            slope = 0.05624;
        	                    intercept = 0.08417;
				}
                	        //if (etamin == 1.8){
                        	if (neta == 3){
                        	    sigma = 0.02352;
	                            slope= 0.08702;
        	                    intercept = 0.1426;
				}
                	        //if (etamin == 2.0){
                        	if (neta == 4){
                        	    sigma = 0.03006;
	                            slope = 0.1676;
        	                    intercept = 0.2198;
				}
                	        //if (etamin == 2.2){
                        	if (neta == 5){
                        	    sigma = 0.05692;
	                            slope = 0.4953;
        	                    intercept = 0.7272;
				}
                	}           
	                if (parity_case ==3 ){
				slope_elliptic_Tao = -15.73;
				slope_Tao_st2 = -29.4;
        	                prop = 0.3217;
                	        //if (etamin == 1.6){
                        	if (neta == 2){
                        	    sigma = 0.006731;
	                            slope = 0.1066;
        	                    intercept = 0.2026;
				}
                	        //if (etamin == 1.8){
                        	if (neta == 3){
                        	    sigma = 0.02152;
	                            slope= 0.1435;
        	                    intercept = 0.2118;
				}
                	        //if (etamin == 2.0){
                        	if (neta == 4){
                        	    sigma = 0.03513;
	                            slope = 0.2874;
        	                    intercept = 0.4055;
				}
                	        //if (etamin == 2.2){
                        	if (neta == 5){
	                            sigma = 0.05173;
        	                    slope = 0.7625;
                	            intercept = 1.075;
				}	

			}



		        std::cout <<"3rd loop csc_bending_angle_variable "<< csc_bending_angle_variable <<" delta_y_gp_23_variable "<< delta_y_gp_23_variable <<" delta_y_gp_12_variable "<< delta_y_gp_12_variable<<" slope_phi "<< slope_phi << " slope " << slope <<std::endl;	
			if (csc_bending_angle_variable == 0) continue;
			if (delta_y_gp_23_variable == 0 ) continue;
			if (delta_y_gp_12_variable == 0) continue;
			if (slope_phi == 0) continue;
			if (slope == 0) continue;		



			etrk_csc_[1].deltaphi_gp_12 = deltaphi_global;
			etrk_csc_[st].deltaphi_gp_12 = deltaphi_global;
 			etrk_csc_[1].elliptic_value = abs( deltaphi_global  - slope_elliptic_Tao*local_bending);
 			etrk_csc_[st].elliptic_value = abs( deltaphi_global  - slope_elliptic_Tao*local_bending);
			etrk_csc_[1].elliptic_value_st2 = abs( deltaphi_global  - slope_Tao_st2*local_bending_st2);
			etrk_csc_[st].elliptic_value_st2 = abs( deltaphi_global  - slope_Tao_st2*local_bending_st2);

			float Reco_pT_Direction_var =  (( 1/abs(csc_bending_angle_variable) + intercept_phi )/slope_phi );
			std::cout <<" sim information pt "<< t.momentum().pt()<<" eta "<< t.momentum().eta() << std::endl;
			std::cout <<" abs(csc_bending_angle_variable) "<< abs(csc_bending_angle_variable) <<" slope "<< slope_phi <<" intercept "<< intercept_phi << " reco pt (direction) "<< Reco_pT_Direction_var << std::endl;
			std::cout <<"reco pt (direction)  from function "<< Ptassign_Direction(abs(csc_bending_angle_variable), hitGp2.eta() , parity_case) <<" eta(st2) "<<hitGp2.eta() <<" npar "<< parity_case <<  std::endl;
			etrk_csc_[st].Reco_pT_Direction = Reco_pT_Direction_var;

			etrk_csc_[1].Reco_pT_Direction = Reco_pT_Direction_var;

			float Reco_pT_Dir_smeared_3_7 = (( 1/abs(delta_phi_smeared_3_7) - intercept_phi_3_7 )/slope_phi_3_7 );
			float Reco_pT_Dir_smeared_6_14 = (( 1/abs(delta_phi_smeared_6_14) - intercept_phi_6_14 )/slope_phi_6_14 );
			float Reco_pT_Dir_smeared_9_21 = (( 1/abs(delta_phi_smeared_9_21) + intercept_phi )/slope_phi );
			float Reco_pT_Dir_smeared_12_28 = (( 1/abs(delta_phi_smeared_12_28) + intercept_phi )/slope_phi );
			float Reco_pT_Dir_smeared_15_35 = (( 1/abs(delta_phi_smeared_15_35) + intercept_phi )/slope_phi );
			float Reco_pT_Dir_smeared_18_42 = (( 1/abs(delta_phi_smeared_18_42) + intercept_phi )/slope_phi );
			float Reco_pT_Dir_smeared_21_49 = (( 1/abs(delta_phi_smeared_21_49) + intercept_phi )/slope_phi );
			float Reco_pT_Dir_smeared_24_56 = (( 1/abs(delta_phi_smeared_24_56) + intercept_phi )/slope_phi );
			float Reco_pT_Dir_smeared_27_63 = (( 1/abs(delta_phi_smeared_27_63) + intercept_phi )/slope_phi );
			float Reco_pT_Dir_smeared_30_70 = (( 1/abs(delta_phi_smeared_30_70) - intercept_phi_30_70 )/slope_phi_30_70 );
			float Reco_pT_Dir_smeared_03_07 = (( 1/abs(delta_phi_smeared_03_07) - intercept_phi_03_07 )/slope_phi_03_07 );




			etrk_csc_[1].Reco_pT_Direction_Smeared_3_7 = Reco_pT_Dir_smeared_3_7;
			etrk_csc_[1].Reco_pT_Direction_Smeared_6_14 = Reco_pT_Dir_smeared_6_14;
			etrk_csc_[1].Reco_pT_Direction_Smeared_9_21 = Reco_pT_Dir_smeared_9_21;
			etrk_csc_[1].Reco_pT_Direction_Smeared_12_28 = Reco_pT_Dir_smeared_12_28;
			etrk_csc_[1].Reco_pT_Direction_Smeared_15_35 = Reco_pT_Dir_smeared_15_35;
			etrk_csc_[1].Reco_pT_Direction_Smeared_18_42 = Reco_pT_Dir_smeared_18_42;
			etrk_csc_[1].Reco_pT_Direction_Smeared_21_49 = Reco_pT_Dir_smeared_21_49;
			etrk_csc_[1].Reco_pT_Direction_Smeared_24_56 = Reco_pT_Dir_smeared_24_56;
			etrk_csc_[1].Reco_pT_Direction_Smeared_27_63 = Reco_pT_Dir_smeared_27_63;
			etrk_csc_[1].Reco_pT_Direction_Smeared_30_70 = Reco_pT_Dir_smeared_30_70;
			etrk_csc_[1].Reco_pT_Direction_Smeared_03_07 = Reco_pT_Dir_smeared_03_07;




			etrk_csc_[1].has_pT_Direction = 1;
			etrk_csc_[st].has_pT_Direction = 1;


			etrk_csc_[1].has_pT_Position = 1;
			etrk_csc_[st].has_pT_Position = 1;
			float Reco_pT_Position_var =  (( 1/abs((delta_y_gp_23_variable) - prop*(delta_y_gp_12_variable) )  + intercept )/slope);
			etrk_csc_[st].Reco_pT_Position  =  Reco_pT_Position_var;
			etrk_csc_[1].Reco_pT_Position  =  Reco_pT_Position_var;
			// Calculate here the pT for Position

			etrk_csc_[1].p_c_SimTrack = sigma + sigma_phi;

			//std::cout<<" Reco pT Direction: "<<Reco_pT_Direction_var<<" Reco pT Position: "<<Reco_pT_Position_var<<" True pT "<<t.momentum().pt()<<std::endl;
			//std::cout<<" Sigma Direction : "<<sigma_phi<<" Sigma Position: "<<sigma<<" eta: "<<t.momentum().eta()<<std::endl;
		}







                for(auto t_d: csc_simhits)
                {
                        CSCDetId t_id(t_d);
                        const int t_st(detIdToMEStation(t_id.station(),t_id.ring()));
                        if (stationscsc_to_use_.count(t_st) == 0) continue;
                        int t_nlayers(match_sh.nLayersWithHitsInSuperChamber(t_d));

                        if (t_nlayers < 4) continue;

                        if (t_id.station()==1) continue;
                        if (t_id.station()==2) continue;
                        if (t_id.station()==3) continue;

                        GlobalPoint hitGp4 = match_sh.simHitsMeanPosition(match_sh.hitsInChamber(t_d));
                        float ysst4 = -hitGp4.x()*sin(anglea) + hitGp4.y()*cos(anglea);
                        float xsst4 = hitGp4.x()*cos(anglea) + hitGp4.y()*sin(anglea);

                        etrk_csc_[st].has_delta_y_4 = 1;
                        etrk_csc_[1].has_delta_y_4 = 1;

                        etrk_csc_[1].delta_y_24_12 =  ysst4 - newyst2;
                        etrk_csc_[st].delta_y_24_12 =  ysst4 - newyst2;
                        etrk_csc_[st].delta_x_24_12 =  xsst4 - newxst2;
                        etrk_csc_[1].delta_x_24_12 =  xsst4 - newxst2;
                }



            }
        
            if(s_id.station()==3){
                etrk_csc_[st].csc_bending_angle_13 = deltaPhi(ym.phi(), ym2.phi());
                etrk_csc_[1].csc_bending_angle_13 = deltaPhi(ym.phi(), ym2.phi());
                etrk_csc_[1].has_csc_13 = 1;
                etrk_csc_[st].has_csc_13 = 1;
                etrk_csc_[1].csc_deltaeta_13 = ym.eta() - ym2.eta();
                etrk_csc_[st].csc_deltaeta_13 = ym.eta() - ym2.eta();
		etrk_csc_[1].csc_gp_second_st3 = hitGp2.eta();
		etrk_csc_[st].csc_gp_second_st3 = hitGp2.eta();
		etrk_csc_[st].nlayers_st3 = s_nlayers;
		etrk_csc_[1].nlayers_st3 = s_nlayers;

		etrk_csc_[1].endcap_st3 = s_id.endcap();
		etrk_csc_[st].endcap_st3 = s_id.endcap();
		etrk_csc_[1].csc_chamber_st3 = s_id.chamber();
		etrk_csc_[st].csc_chamber_st3 = s_id.chamber();
		etrk_csc_[1].csc_deltaphi_gp_13 = deltaPhi(hitGp.phi(),hitGp2.phi());
		etrk_csc_[st].csc_deltaphi_gp_13 = deltaPhi(hitGp.phi(),hitGp2.phi());
                

            }

            if(s_id.station()==4){
                etrk_csc_[st].has_csc_14 = 1;
                etrk_csc_[1].has_csc_14 = 1;
                etrk_csc_[1].csc_bending_angle_14 = deltaPhi(ym.phi(), ym2.phi());
                etrk_csc_[st].csc_bending_angle_14 = deltaPhi(ym.phi(), ym2.phi());
                etrk_csc_[st].csc_deltaeta_14 = ym.eta() - ym2.eta();
                etrk_csc_[1].csc_deltaeta_14 = ym.eta() - ym2.eta();
		etrk_csc_[1].csc_gp_second_st4 = hitGp2.eta();
		etrk_csc_[st].csc_gp_second_st4 = hitGp2.eta();
		etrk_csc_[st].nlayers_st4 = s_nlayers;
		etrk_csc_[1].nlayers_st4 = s_nlayers;
		etrk_csc_[1].endcap_st4 = s_id.endcap();
		etrk_csc_[st].endcap_st4 = s_id.endcap();


		etrk_csc_[st].csc_chamber_st4 = s_id.chamber();
		etrk_csc_[1].csc_chamber_st4 = s_id.chamber();
		etrk_csc_[1].csc_deltaphi_gp_14 = deltaPhi(hitGp.phi(),hitGp2.phi());
		etrk_csc_[st].csc_deltaphi_gp_14 = deltaPhi(hitGp.phi(),hitGp2.phi());


            }
        } // End of especial case for ME11



	if (id.station()==2){

		etrk_csc_[1].endcap_st2 = id.endcap();
		if(s_id.station()==3){

			float angleb =   hitGp.phi();
		        float newxst2 =  hitGp.x()*cos(angleb) + hitGp.y()*sin(angleb);
		        float newyst2 = -hitGp.x()*sin(angleb) + hitGp.y()*cos(angleb);
        		float newxst3 =  hitGp2.x()*cos(angleb) + hitGp2.y()*sin(angleb);
        		float newyst3 = -hitGp2.x()*sin(angleb) + hitGp2.y()*cos(angleb);

			etrk_csc_[1].delta_x_gp_23 = newxst3 - newxst2;
			etrk_csc_[st].delta_x_gp_23 = newxst3 - newxst2;
			etrk_csc_[st].delta_y_gp_23 = newyst3 - newyst2;
			etrk_csc_[1].delta_y_gp_23 = newyst3 - newyst2;

              		etrk_csc_[1].has_csc_23 = 1;
              		etrk_csc_[st].has_csc_23 = 1;
			etrk_csc_[st].csc_deltaphi_gp_23 = deltaPhi(hitGp.phi(),hitGp2.phi());
	              	etrk_csc_[1].csc_deltaphi_gp_23 = deltaPhi(hitGp.phi(),hitGp2.phi());

			etrk_csc_[1].endcap_st3 = s_id.endcap();
			etrk_csc_[st].endcap_st3 = s_id.endcap();


		}

		if(s_id.station()==4){
              		etrk_csc_[1].csc_deltaphi_gp_24 = deltaPhi(hitGp.phi(),hitGp2.phi());
        	      	etrk_csc_[st].csc_deltaphi_gp_24 = deltaPhi(hitGp.phi(),hitGp2.phi());
              		etrk_csc_[1].has_csc_24 = 1;
			etrk_csc_[1].endcap_st4 = s_id.endcap();
			etrk_csc_[st].endcap_st4 = s_id.endcap();
              		etrk_csc_[st].has_csc_24 = 1;
		}
		

	}


	if (id.station()==3){


		etrk_csc_[1].endcap_st3 = id.endcap();

		if (s_id.station()==4){
              	  etrk_csc_[st].csc_deltaphi_gp_34 = deltaPhi(hitGp.phi(),hitGp2.phi());
              	  etrk_csc_[1].csc_deltaphi_gp_34 = deltaPhi(hitGp.phi(),hitGp2.phi());
		  etrk_csc_[1].endcap_st4 = s_id.endcap();
		  etrk_csc_[st].endcap_st4 = s_id.endcap();
		  etrk_csc_[1].has_csc_34 = 1;
		  etrk_csc_[st].has_csc_34 = 1;

		}

	}

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
 endcap_st1 = 0;
 endcap_st2 = 0;
 endcap_st3 = 0;
 endcap_st4 = 0;
 run = - 99;
 pt_SimTrack = - 9;
 phi_SimTrack = - 9;
 eta_SimTrack= - 9;
 vertex_x = - 9;
 vertex_y = - 9;
 vertex_z = - 9;

 dxy = - 9.;
 p_SimTrack = - 9;
 charge = - 9.;
 p_c_SimTrack = - 9;
 
 Lxy = - 9999.;
 pzvz = - 999.;
 pp_SimTrack = - 99.;

 elliptic_value_st2 = - 99.;
 bending_sh_st1 = - 99.;
 bending_sh_st2 = - 99.;
 elliptic_value = - 99.;
 deltaphi_gp_12 = - 99.;

 csc_gp_y = - 9999;
 csc_gp_x = - 9999;
 csc_gp_r = - 9999;
 csc_gp_z = - 9999;
 nlayerscsc = 0;
 csc_gp_eta = - 9;
 csc_gp_phi = - 9;
 csc_chamber = - 9; 
 csc_chamber_st2 = - 9;
 csc_chamber_st3 = - 9;
 csc_chamber_st4 = - 9;
 csc_gv_eta = - 9.;
 csc_gv_phi = - 9.;
 csc_gv_pt = - 9.;


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

 csc_station = - 99;
 csc_ring = - 99;
 csc_deltaeta = - 99.;
 csc_deltaeta_14 = - 99.;
 csc_deltaeta_13 = - 99.;
 csc_deltaeta_12 = - 99.;

 has_delta_y = 0;
 delta_y_23_12 = - 9999.;
 delta_x_23_12 = - 9999.;


 Reco_pT_Direction_Smeared_3_7 = - 9.0;
 Reco_pT_Direction_Smeared_6_14 = - 9.0;
 Reco_pT_Direction_Smeared_9_21 = - 9.0;
 Reco_pT_Direction_Smeared_12_28 = - 9.0;
 Reco_pT_Direction_Smeared_15_35 = - 9.0;
 Reco_pT_Direction_Smeared_18_42 = - 9.0;
 Reco_pT_Direction_Smeared_21_49 = - 9.0;
 Reco_pT_Direction_Smeared_24_56 = - 9.0;
 Reco_pT_Direction_Smeared_27_63 = - 9.0;
 Reco_pT_Direction_Smeared_30_70 = - 9.0;
 Reco_pT_Direction_Smeared_03_07 = - 9.0;

 Reco_pT_Direction_Smeared = - 9.0;
 Reco_pT_Direction = - 9.;
 Reco_pT_Position = - 9.;

 DeltaPhi_Smeared_03_07 = - 99.;
 DeltaPhi_Smeared_3_7 = - 99.;
 DeltaPhi_Smeared_6_14 = - 99.;
 DeltaPhi_Smeared_30_70 = - 99.;


 has_pT_Direction = 0;
 has_pT_Position = 0;

 has_delta_y_4 = 0;
 delta_y_24_12 = -9999.;
 delta_x_24_12 = - 9999.;


 delta_x_24_12 = - 9999.;
 delta_y_24_12 = - 9999.;
 has_delta_y_4= 0;

 csc_deltaphi_gp_12=-99.;
 csc_deltaphi_gp_13=-99.;
 csc_deltaphi_gp_14=-99.;
 csc_deltaphi_gp_23=-99.;
 csc_deltaphi_gp_24=-99.;
 csc_deltaphi_gp_34=-99.;

 csc_gp_second_st2 = 0.;
 nlayers_st3 = 0;
 nlayers_st4 = 0;
 nlayers_st2 = 0;
 csc_gp_second_st3 = 0.;
 csc_gp_second_st4 = 0.;
 has_csc_12 = 0;
 has_csc_13 = 0;
 has_csc_14 = 0;
 has_csc_23 = 0;
 has_csc_24 = 0;
 has_csc_34 = 0;

 csc_bending_angle_12 = - 99;
 csc_bending_angle_13 = - 99;
 csc_bending_angle_14 = - 99;
 csc_deltaphi_gp = - 99;
 csc_deltaphi = - 99;

 csc_p_over_cosh_eta = - 99.; 
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
  t->Branch("pt_SimTrack", &pt_SimTrack);
  t->Branch("phi_SimTrack", &phi_SimTrack);
  t->Branch("eta_SimTrack", &eta_SimTrack); 
  t->Branch("vertex_x", &vertex_x);
  t->Branch("vertex_y", &vertex_y);
  t->Branch("vertex_z", &vertex_z);

  t->Branch("dxy", &dxy);
  t->Branch("csc_station", &csc_station);
  t->Branch("csc_ring", &csc_ring);
  t->Branch("Lxy", &Lxy);
  t->Branch("pzvz", &Lxy);
  t->Branch("pp_SimTrack", &pp_SimTrack);


  t->Branch("p_SimTrack", &p_SimTrack);
  t->Branch("charge", &charge);
  t->Branch("p_c_SimTrack", &p_c_SimTrack);
  t->Branch("endcap_st1", &endcap_st1);
  t->Branch("endcap_st2", &endcap_st2);
  t->Branch("endcap_st3", &endcap_st3);
  t->Branch("endcap_st4", &endcap_st4);

  t->Branch("elliptic_value", &elliptic_value);
  t->Branch("bending_sh_st1", &bending_sh_st1);
  t->Branch("bending_sh_st2", &bending_sh_st2);
  t->Branch("elliptic_value_st2", &elliptic_value_st2);
  t->Branch("deltaphi_gp_12", &deltaphi_gp_12);


  t->Branch("csc_gp_y", &csc_gp_y);
  t->Branch("csc_gp_x", &csc_gp_x);
  t->Branch("csc_gp_r", &csc_gp_r);
  t->Branch("csc_gp_z", &csc_gp_z);
  t->Branch("csc_gp_eta", &csc_gp_eta);
  t->Branch("csc_gp_phi", &csc_gp_phi);
  t->Branch("nlayerscsc", &nlayerscsc);


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

  t->Branch("csc_chamber_st4", &csc_chamber_st4);
  t->Branch("csc_chamber_st3", &csc_chamber_st3);
  t->Branch("csc_chamber_st2", &csc_chamber_st2);
  t->Branch("csc_chamber", &csc_chamber);
 

  t->Branch("csc_gv_eta", &csc_gv_eta);
  t->Branch("csc_gv_pt", &csc_gv_pt);
  t->Branch("csc_gv_phi", &csc_gv_phi);
  t->Branch("csc_deltaphi", &csc_deltaphi);
  t->Branch("csc_deltaphi_gp", &csc_deltaphi_gp);


  t->Branch("nlayers_st2", &nlayers_st2);
  t->Branch("nlayers_st3", &nlayers_st3);
  t->Branch("nlayers_st4", &nlayers_st4);


  t->Branch("has_delta_y", &has_delta_y);
  t->Branch("delta_x_23_from12", &delta_x_23_12);
  t->Branch("delta_y_23_from12", &delta_y_23_12);



  t->Branch("Reco_pT_Direction_Smeared_3_7", &Reco_pT_Direction_Smeared_3_7);
  t->Branch("Reco_pT_Direction_Smeared_6_14", &Reco_pT_Direction_Smeared_6_14);
  t->Branch("Reco_pT_Direction_Smeared_9_21", &Reco_pT_Direction_Smeared_9_21);
  t->Branch("Reco_pT_Direction_Smeared_12_28", &Reco_pT_Direction_Smeared_12_28);
  t->Branch("Reco_pT_Direction_Smeared_15_35", &Reco_pT_Direction_Smeared_15_35);
  t->Branch("Reco_pT_Direction_Smeared_18_42", &Reco_pT_Direction_Smeared_18_42);
  t->Branch("Reco_pT_Direction_Smeared_21_49", &Reco_pT_Direction_Smeared_21_49);
  t->Branch("Reco_pT_Direction_Smeared_24_56", &Reco_pT_Direction_Smeared_24_56);
  t->Branch("Reco_pT_Direction_Smeared_27_63", &Reco_pT_Direction_Smeared_27_63);
  t->Branch("Reco_pT_Direction_Smeared_30_70", &Reco_pT_Direction_Smeared_30_70);
  t->Branch("Reco_pT_Direction_Smeared_03_07", &Reco_pT_Direction_Smeared_03_07);


  t->Branch("DeltaPhi_Smeared_03_07", &DeltaPhi_Smeared_03_07);
  t->Branch("DeltaPhi_Smeared_3_7", &DeltaPhi_Smeared_3_7);
  t->Branch("DeltaPhi_Smeared_6_14", &DeltaPhi_Smeared_6_14);
  t->Branch("DeltaPhi_Smeared_30_70", &DeltaPhi_Smeared_30_70);


  t->Branch("Reco_pT_Direction", &Reco_pT_Direction);
  t->Branch("Reco_pT_Direction_Smeared", &Reco_pT_Direction_Smeared);
  t->Branch("has_pT_Direction", &has_pT_Direction);
  t->Branch("has_pT_Position", &has_pT_Position);
  t->Branch("Reco_pT_Position", &Reco_pT_Position);
  t->Branch("has_delta_y_4", &has_delta_y);
  t->Branch("delta_x_24_from12", &delta_x_24_12);
  t->Branch("delta_y_24_from12", &delta_y_24_12);


  t->Branch("csc_deltaphi_gp_12", &csc_deltaphi_gp_12);
  t->Branch("csc_deltaphi_gp_13", &csc_deltaphi_gp_13);
  t->Branch("csc_deltaphi_gp_14", &csc_deltaphi_gp_14);
  t->Branch("csc_deltaphi_gp_23", &csc_deltaphi_gp_23);
  t->Branch("csc_deltaphi_gp_24", &csc_deltaphi_gp_24);
  t->Branch("csc_deltaphi_gp_34", &csc_deltaphi_gp_34);



  t->Branch("csc_gp_second_st3", &csc_gp_second_st3);
  t->Branch("csc_gp_second_st2", &csc_gp_second_st2);
  t->Branch("csc_gp_second_st4", &csc_gp_second_st4);
  t->Branch("csc_bending_angle_12", &csc_bending_angle_12);
  t->Branch("csc_bending_angle_13", &csc_bending_angle_13);
  t->Branch("csc_bending_angle_14", &csc_bending_angle_14);

  t->Branch("csc_p_over_cosh_eta", &csc_p_over_cosh_eta);

  t->Branch("csc_deltaeta_14", &csc_deltaeta_14);
  t->Branch("csc_deltaeta", &csc_deltaeta);
  t->Branch("csc_deltaeta_13", &csc_deltaeta_13);
  t->Branch("csc_deltaeta_12", &csc_deltaeta_12);
  t->Branch("has_csc_12", &has_csc_12);
  t->Branch("has_csc_13", &has_csc_13);
  t->Branch("has_csc_14", &has_csc_14);
  t->Branch("has_csc_23", &has_csc_23);
  t->Branch("has_csc_24", &has_csc_24);
  t->Branch("has_csc_34", &has_csc_34);
  return t;
}

TTree*MyTrackEffDT::book(TTree *t,const std::string & name)
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
HLTBendingAngle::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(HLTBendingAngle);
