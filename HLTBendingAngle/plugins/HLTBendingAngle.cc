// system include files
#include <memory>
#include "TTree.h"
#include <iomanip>
#include <sstream>
#include <vector>

// user include files
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
 Int_t nlayerdt;
 Float_t R_gv;
 Float_t Z_gv;
 Float_t X_gv;
 Float_t Y_gv;

 Float_t L1_pt;
 Float_t L1_eta;
 Float_t L1_q;
 Float_t L1_phi_;
 
 Int_t wheel;
 Int_t station;

};

void MyTrackEffL1::init()
{

 L1_pt = -99.;
 L1_eta = -9.;
 L1_phi = - 99.;
 L1_charge = - 9.;


} 

void MyTrackEffDT::init()
{
 lumi = -99;
 run= -99;
 event = -99;

 pt_SimTrack_dt = 0.;
 eta_SimTrack_dt=-9.;
 phi_SimTrack_dt=0.;
 eta_gp = -9.;
 eta_gv = -9.;
 phi_gv= -9.;
 pt_gv= -9.;
 z_gp = -9900.;
 deltaphi_h_g = -9.;
 apt_SimTrack_dt=-999;
 charge_dt = -99;
 
 deltaphi_first_second_gv=-9990.;
 deltaphi_first_second_gp=-9990.;
 deltaphi_first_third_gv=-9990.;
 deltaphi_first_third_gp=-9999.;
 deltaphi_first_fourth_gv=-9999.;
 deltaphi_first_fourth_gp=-9999.;
 has_second_dtst_hit=0;
 has_third_dtst_hit=0;
 has_fourth_dtst_hit=0;
 
 wheel_second = -99;
 phi_gp_second= - 9999.;
 eta_gp_second = - 99.;
 phi_gv_second = - 9999.;
 eta_gv_second = - 99.;

 wheel_third = -99.;
 phi_gp_third =  - 9999.;
 eta_gp_third = -99.;
 phi_gv_third = - 9999.;
 eta_gv_third = - 99.;

 wheel_fourth = -99.;
 phi_gp_fourth = - 9999.;
 eta_gp_fourth = -99.;
 phi_gv_fourth = - 9999.;
 eta_gv_fourth = -99.;

 pt_calculated_dt=0;
 pt_calculated_dt_12=0;
 pt_calculated_dt_13=0;
 pt_calculated_dt_14=0;
 x_gp = -9900.;
 y_gp = -9900.;
 r_gp = -9900.;
 phi_gp = -99;
 dt_dxy = -9999;
 dtvertex_x=-9999;
 dtvertex_y=-9999;
 dtvertex_z=-9999;
 dtvertex_r=-9999;
 has_dt_sh=-1;
 nlayerdt = -1;
 R_gv=-9999.;
 Z_gv=-9999.;
 X_gv=-9999.;
 Y_gv=-9999.;

 wheel = -9;
 station = - 9;
 L1_pt = - 99.;
 L1_eta = - 9.;
 L1_q = - 9.;
 L1_phi_ = -999.;
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

TTree*MyTrackEffDT::book(TTree *t,const std::string & name)
{
  edm::Service< TFileService > fs;
  t = fs->make<TTree>(name.c_str(),name.c_str());

  t->Branch("L1_pt", &L1_pt);
  t->Branch("L1_eta", &L1_eta);
  t->Branch("L1_q", &L1_q);
  t->Branch("L1_phi_", &L1_phi_);

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
  t->Branch("R_gv", &R_gv);
  t->Branch("Z_gv", &Z_gv);
  t->Branch("X_gv", &X_gv);
  t->Branch("Y_gv", &Y_gv);
  t->Branch("dt_dxy", &dt_dxy);

  return t;
}


std::vector<std::pair<int,int> > dtStationsCo_;

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
  
  std::set<int> l1particles_muons_;
  
  TTree *tree_eff_dt_[56];
  MyTrackEffDT etrk_dt_[56];
  
  TTree *tree_eff_l1_[6];
  MyTrackEffL1 etrk_l1_[6];
  float deltaR;
  float deltaPhi;
  int does_it_match;
  
  edm::ParameterSet cfg_;
  int verbose_;
  int verboseSimTrack_;
  edm::InputTag simInputLabel_;
  double simTrackMinPt_;
  double simTrackMinEta_;
  double simTrackMaxEta_;
  double simTrackOnlyMuon_;
};

HLTBendingAngle::HLTBendingAngle(const edm::ParameterSet& ps)
  : cfg_(ps.getParameterSet("simTrackMatching"))
  , verbose_(ps.getUntrackedParameter<int>("verbose", 0))
{
  auto simTrack = cfg_.getParameter<edm::ParameterSet>("simTrack");
  verboseSimTrack_ = simTrack.getParameter<int>("verbose");
  simInputLabel_ = simTrack.getParameter<edm::InputTag>("input");
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

  for (auto m: stationsdt_to_use_)
  {    
    etrk_dt_[m].init();
  }
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

   if (verboseSimTrack_){
     std::cout << "Total number of SimTracks in this event: " << sim_track.size() << std::endl;      
   }

  int trk_no=0;
  for (auto& t: *sim_tracks.product())
  {
    if(!isSimTrackGood(t)) continue;
    if (verboseSimTrack_){
      std::cout << "Processing SimTrack " << trk_no + 1 << std::endl;      
      std::cout << "pt(GeV/c) = " << t.momentum().pt() << ", eta = " << t.momentum().eta()  
                << ", phi = " << t.momentum().phi() << ", Q = " << t.charge() << std::endl;
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
  const TrackMatcher& match_track = match.tracks();
  const SimTrack &t = match_sh.trk();
  const SimVertex &vtx = match_sh.vtx();

  for (auto asdt: stationsdt_to_use_)
  {
    etrk_dt_[asdt].run = match_sh.event().id().run();
    etrk_dt_[asdt].lumi= match_sh.event().id().luminosityBlock();
    etrk_dt_[asdt].event = match_sh.event().id().event();
    etrk_dt_[asdt].charge_dt=t.charge();
    
    const float vtx_x = vtx.position().x();
    const float vtx_y = vtx.position().y();
    const float vtx_z = vtx.position().z();

    etrk_dt_[asdt].dtvertex_x = vtx_x;
    etrk_dt_[asdt].dtvertex_y = vtx_y;
    etrk_dt_[asdt].dtvertex_z = vtx_z;
    etrk_dt_[asdt].dtvertex_r = sqrt(vtx_x*vtx_x+vtx_y*vtx_y);
    
    etrk_dt_[asdt].pt_SimTrack_dt=t.momentum().pt(); //This one
    etrk_dt_[asdt].eta_SimTrack_dt=t.momentum().eta();
    etrk_dt_[asdt].phi_SimTrack_dt = t.momentum().phi();
    
    if (!(t.momentum().pt()==0)){
      etrk_dt_[asdt].apt_SimTrack_dt =1/ t.momentum().pt();  //This one
    }else{
      etrk_dt_[asdt].apt_SimTrack_dt = 0;
    }

    auto pphi = t.momentum().phi();
    etrk_dt_[asdt].dt_dxy = vtx_x*sin(pphi) - vtx_y*cos(pphi);

    // add a section on wheter the simtrack was matched to the L1MuonParticle
    // Define additional accessors in TrackMather.h if need be
    // for inspiration, look at GEMCSCAnalyzer
  } 
  
  auto dt_simhits(match_sh.chamberIdsDT());
  std::cout<<" Size of dt sh: "<<dt_simhits.size()<<std::endl;
  for(auto d: dt_simhits)
  {
    const DTWireId id(d);
    const int stdt(detIdToMBStation(id.wheel(),id.station()));
    if (stationsdt_to_use_.count(stdt) == 0) continue;
    const int nlayersdtch(match_sh.nLayersWithHitsInLayerDT(id.rawId()));
    
    if (nlayersdtch == 0) continue;
    etrk_dt_[stdt].has_dt_sh = 1;
    etrk_dt_[stdt].nlayerdt  = nlayersdtch;

    etrk_dt_[stdt].wheel = id.wheel();
    etrk_dt_[stdt].station = id.station();
  } 	

  /*
    TrajectoryStateOnSurface propagated123;
    bool does_it_match2 = L1MuonMatcherAlgo(pSetabc).match(t, sim_vert, l1_particles, deltaR, deltaPhi, propagated123);
    
  */

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
  const float eta(std::abs(t.momentum().eta()));
  if (eta > simTrackMaxEta_ || eta < simTrackMinEta_) return false; 
  return true;
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
