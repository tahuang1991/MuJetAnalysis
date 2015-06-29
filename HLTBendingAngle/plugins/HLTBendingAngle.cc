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
  
  void analyzeTrackEfficiency(SimTrackMatchManager& match, int trk_no, edm::Handle<std::vector<l1extra::L1MuonParticle> > l1p, edm::Handle<std::vector<reco::RecoChargedCandidate> > hlt_l2_pp, edm::Handle<std::vector<reco::TrackExtra> > l2_track, edm::Handle<edm::RangeMap<DTChamberId,edm::OwnVector<DTRecSegment4D,edm::ClonePolicy<DTRecSegment4D> >,edm::ClonePolicy<DTRecSegment4D> > > SegmentsDT);

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

   if (verboseSimTrack_){
     std::cout << "Total number of SimTracks in this event: " << sim_track.size() << std::endl;   
     std::cout << "Total number of SimVertexs in this event: " << sim_vert.size() << std::endl;
   }
   
   edm::Handle<std::vector<l1extra::L1MuonParticle> > l1_particles;
   ev.getByLabel("hltL1extraParticles", l1_particles);


   edm::Handle<std::vector<reco::TrackExtra> > l2_track;
   ev.getByLabel("hltL2Muons", l2_track);


   edm::Handle<std::vector<reco::RecoChargedCandidate> > hlt_l2_pp;
   ev.getByLabel("hltL2MuonCandidatesNoVtx", hlt_l2_pp);


   edm::Handle<edm::RangeMap<DTChamberId,edm::OwnVector<DTRecSegment4D,edm::ClonePolicy<DTRecSegment4D> >,edm::ClonePolicy<DTRecSegment4D> > > SegmentsDT;
   ev.getByLabel("hltDt4DSegments", SegmentsDT);

   int trk_no=0;
   for (auto& t: *sim_tracks.product()) {
     if(!isSimTrackGood(t)) continue;
     if (verboseSimTrack_) {
       std::cout << "Processing SimTrack " << trk_no + 1 << std::endl;      
       std::cout << "pt(GeV/c) = " << t.momentum().pt() << ", eta = " << t.momentum().eta()  
                 << ", phi = " << t.momentum().phi() << ", Q = " << t.charge()
                 << ", vtxIndex = " << t.vertIndex() << std::endl;
     }

     vtx_dt = sim_vert[t.vertIndex()].position().x();
     vty_dt = sim_vert[t.vertIndex()].position().y();
     vtz_dt = sim_vert[t.vertIndex()].position().z();

     SimTrackMatchManager match(t, sim_vert[t.vertIndex()], cfg_, ev, es);
     analyzeTrackEfficiency(match, trk_no, l1_particles, hlt_l2_pp, l2_track, SegmentsDT);

    ++trk_no;
  }
}

void 
HLTBendingAngle::analyzeTrackEfficiency(SimTrackMatchManager& match, int trk_no, edm::Handle<std::vector<l1extra::L1MuonParticle> > l1p, edm::Handle<std::vector<reco::RecoChargedCandidate> > hlt_l2_pp, edm::Handle<std::vector<reco::TrackExtra> > l2_track, edm::Handle<edm::RangeMap<DTChamberId,edm::OwnVector<DTRecSegment4D,edm::ClonePolicy<DTRecSegment4D> >,edm::ClonePolicy<DTRecSegment4D> > > SegmentsDT)
{
  const SimHitMatcher& match_sh = match.simhits();
  //const TrackMatcher& match_track = match.tracks();
  const SimTrack &t = match_sh.trk();
  //const SimVertex &vtx = match_sh.vtx();

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

    float bestdRl1 = 99.;
    int nl1tr = 0;
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
  
  auto dt_chambers(match_sh.chamberIdsDT());
  for(auto ddt: dt_chambers)
  {
    const DTChamberId id(ddt);
    const int stdt(detIdToMBStation(id.wheel(),id.station()));
    if (stationsdt_to_use_.count(stdt) == 0) continue;


    const int nsl(match_sh.nSuperLayersWithHitsInChamberDT(id.rawId()));
    if (nsl == 0) continue;

    etrk_dt_[stdt].nslayerdt  = nsl;

    int nltotal(0);
    auto superLayers(match_sh.superlayerIdsDT());
    for (auto sl: superLayers) {
      const int nl(match_sh.nLayersWithHitsInSuperLayerDT(sl));
      if (nl < 3) continue;
      nltotal += nl;

    }

    etrk_dt_[stdt].nlayerdt  = nltotal;
    etrk_dt_[stdt].has_dt_sh = 1;


    etrk_dt_[stdt].wheel = id.wheel();
    etrk_dt_[stdt].station = id.station();

    GlobalPoint hitGp = match_sh.simHitsMeanPosition(match_sh.hitsInChamber(ddt));
    etrk_dt_[stdt].eta_gp = hitGp.eta();
    etrk_dt_[stdt].x_gp = hitGp.x();
    etrk_dt_[stdt].y_gp = hitGp.y();
    etrk_dt_[stdt].z_gp = hitGp.z();
    etrk_dt_[stdt].r_gp = hitGp.perp();
    etrk_dt_[stdt].phi_gp = hitGp.phi();

    GlobalVector ym = match_sh.simHitsMeanMomentum(match_sh.hitsInChamber(ddt));
    etrk_dt_[stdt].eta_gv = ym.eta();
    etrk_dt_[stdt].pt_gv = ym.perp();
    etrk_dt_[stdt].phi_gv = ym.phi();
    etrk_dt_[stdt].R_gv = sqrt (ym.x()*ym.x()+ym.y()*ym.y());
    etrk_dt_[stdt].Z_gv = ym.z();
    etrk_dt_[stdt].X_gv = ym.x();
    etrk_dt_[stdt].Y_gv = ym.y();
    etrk_dt_[stdt].deltaphi_h_g = hitGp.phi() - ym.phi();     //This one
    etrk_dt_[stdt].pt_calculated_dt = (1/(hitGp.phi() - ym.phi()))*1.4025845 + 0.674463;

    if(id.station()==2){
        int nl1=0;
        float bestdR = 99.;
        etrk_dt_[21].has_dt_sh = 1;
        etrk_dt_[21].nlayerdt  = nsl;
        etrk_dt_[21].wheel = id.wheel();
        etrk_dt_[21].station = id.station();
        etrk_dt_[21].eta_gp = hitGp.eta();
        etrk_dt_[21].x_gp = hitGp.x();
        etrk_dt_[21].y_gp = hitGp.y();
        etrk_dt_[21].z_gp = hitGp.z();
        etrk_dt_[21].r_gp = hitGp.perp();
        etrk_dt_[21].phi_gp = hitGp.phi();
        etrk_dt_[21].eta_gv = ym.eta();
        etrk_dt_[21].pt_gv = ym.perp();
        etrk_dt_[21].phi_gv = ym.phi();
        etrk_dt_[21].R_gv = sqrt (ym.x()*ym.x()+ym.y()*ym.y());
        etrk_dt_[21].Z_gv = ym.z();
        etrk_dt_[21].X_gv = ym.x();
        etrk_dt_[21].Y_gv = ym.y();
        etrk_dt_[21].deltaphi_h_g = hitGp.phi() - ym.phi();     //This one
        etrk_dt_[21].pt_calculated_dt = (1/(hitGp.phi() - ym.phi()))*1.4025845 + 0.674463;

        for(std::vector<l1extra::L1MuonParticle>::const_iterator muon=l1p->begin(); muon!=l1p->end(); ++muon)
        {
           etrk_dt_[21].L1_pt = muon->pt();
           etrk_dt_[21].L1_eta = muon->eta();
           etrk_dt_[21].L1_phi_ = muon->phi();
           etrk_dt_[21].L1_q = muon->charge();
           float L1eta = muon->eta();
           float L1phi = muon->phi();
           float dp = deltaPhi(L1phi, hitGp.phi());
           float dr = std::sqrt(dp*dp + (L1eta - hitGp.eta())*(L1eta - hitGp.eta()));
           if (dr < 0.2 ){
                  nl1 = nl1 + 1;
           }

           if (dr < bestdR){
                bestdR = dr;
           }

        }

        etrk_dt_[21].has_l1_sh_matched = nl1;
        etrk_dt_[21].L1_sh_dr = bestdR;


    }

    float bestdRl2 = 99.;
    int nl2sh = 0;
    for(std::vector<reco::RecoChargedCandidate>::const_iterator muon = hlt_l2_pp->begin(); muon!=hlt_l2_pp->end(); ++muon)
    {

           auto tracIdd = muon->track()->innerDetId();
           if(tracIdd != ddt) continue;

           float ptx = muon->track()->innerMomentum().X();
           float pty = muon->track()->innerMomentum().Y();
           float pz = muon->track()->innerMomentum().Z();

           auto Xx = muon->track()->innerPosition().eta();
           auto Xy = muon->track()->innerPosition().phi();

           etrk_dt_[stdt].L2_eta = Xx;
           etrk_dt_[stdt].L2_phi= Xy;
           etrk_dt_[stdt].has_l2 = 1;
           etrk_dt_[21].L2_eta = Xx;
           etrk_dt_[21].L2_phi= Xy;
           etrk_dt_[21].has_l2 = 1;
           etrk_dt_[stdt].L2_pp = pz;
           etrk_dt_[21].L2_pp = pz;
           etrk_dt_[stdt].L2_pt = std::sqrt(ptx*ptx+pty*pty);
           etrk_dt_[21].L2_pt = std::sqrt(ptx*ptx+pty*pty);

           float dX = Xx - hitGp.eta();
           float dY = deltaPhi(Xy, hitGp.phi());

           float dr = std::sqrt(dX*dX+dY*dY);

           if (dr < 0.2){
                  nl2sh = nl2sh + 1;
           }

           if (dr < bestdRl2){
                    bestdRl2 = dr;
           }

    }

    etrk_dt_[stdt].L2_sh_dr = bestdRl2;
    etrk_dt_[21].L2_sh_dr = bestdRl2;
    etrk_dt_[stdt].has_l2_sh_matched = nl2sh;
    etrk_dt_[21].has_l2_sh_matched = nl2sh;



    float bestl2tdR = 99;
    int nttm = 0;

    for(std::vector<reco::TrackExtra>::const_iterator l2tt = l2_track->begin(); l2tt!=l2_track->end();++l2tt)
    {
         auto detIdd = l2tt->innerDetId();
         if(detIdd != ddt) continue;
         auto Xx = l2tt->innerPosition().eta();
         auto Xy = l2tt->innerPosition().phi();
         float ptx = l2tt->innerMomentum().X();
         float pty = l2tt->innerMomentum().Y();
         float pz = l2tt->innerMomentum().Z();

         etrk_dt_[stdt].L2t_eta = Xx;
         etrk_dt_[stdt].L2t_phi = Xy;
         etrk_dt_[stdt].L2t_pp = pz;
         etrk_dt_[stdt].L2t_pt = std::sqrt(ptx*ptx+pty*pty);
         etrk_dt_[stdt].has_l2t = 1;
         etrk_dt_[21].L2t_wheel = id.wheel();
         etrk_dt_[21].L2t_station = id.station();
         etrk_dt_[21].L2t_eta = Xx;
         etrk_dt_[21].L2t_phi = Xy;
         etrk_dt_[21].L2t_pp = pz;
         etrk_dt_[21].L2t_pt = std::sqrt(ptx*ptx+pty*pty);
         etrk_dt_[21].has_l2t = 1;

         float dX = Xx - hitGp.eta();
         float dY = deltaPhi(Xy, hitGp.phi());
         float dr = std::sqrt(dX*dX+dY*dY);
         if (dr < 0.2) nttm = nttm + 1;

         if (dr < bestl2tdR) bestl2tdR = dr;
    }

    etrk_dt_[stdt].L2t_sh_dr = bestl2tdR;
    etrk_dt_[21].L2t_sh_dr = bestl2tdR;
    etrk_dt_[21].has_l2t_sh_matched = nttm;
    etrk_dt_[stdt].has_l2t_sh_matched = nttm;

    float bestSegdR = 99.;
    float bestSegdEta = 99.;
    float bestSegdPhi = 99.;
    float bestDTSegBendingAngle1 = 99.;
    int DTSegment_fist_station = 0;
    int segDTm = 0;
    int has_deta_dphi_dr = 0;
    int nDTSegments = 0;

    for(edm::RangeMap<DTChamberId,edm::OwnVector<DTRecSegment4D,edm::ClonePolicy<DTRecSegment4D> >,edm::ClonePolicy<DTRecSegment4D> >::const_iterator seg = SegmentsDT->begin();  seg!=SegmentsDT->end(); ++seg)
    {

        auto segdt = seg->chamberId();

        if(segdt.wheel()!=id.wheel()) continue;
        if(segdt.station()!=id.station()) continue;

        nDTSegments = nDTSegments  + 1;
        etrk_dt_[21].has_DTSegments = 1;
        etrk_dt_[stdt].has_DTSegments = 1;

        auto lp = seg->localPosition();
        GlobalPoint GPp = match_sh.DTSegmentsGlobalPosition(lp, DTChamberId(segdt));


        auto gvv = seg->localDirection();
        GlobalVector GVv = match_sh.DTSegmentsGlobalVector(gvv, DTChamberId(segdt));

        etrk_dt_[21].Seg_wheel = id.wheel();
        etrk_dt_[21].Seg_station = id.station();
        etrk_dt_[21].Seg_gp_eta = GPp.eta();
        etrk_dt_[21].Seg_gp_phi = GPp.phi();
        etrk_dt_[21].Seg_gp_x = GPp.x();
        etrk_dt_[21].Seg_gp_y = GPp.y();
        etrk_dt_[21].Seg_gp_z = GPp.z();
        etrk_dt_[21].Seg_gv_phi = GVv.phi();
        etrk_dt_[21].Seg_gv_eta = GVv.eta();


        etrk_dt_[stdt].Seg_wheel = id.wheel();
        etrk_dt_[stdt].Seg_station = id.station();
        etrk_dt_[stdt].Seg_gp_eta = GPp.eta();
        etrk_dt_[stdt].Seg_gp_phi = GPp.phi();
        etrk_dt_[stdt].Seg_gp_x = GPp.x();
        etrk_dt_[stdt].Seg_gp_y = GPp.y();
        etrk_dt_[stdt].Seg_gp_z = GPp.z();
        etrk_dt_[stdt].Seg_gv_phi = GVv.phi();
        etrk_dt_[stdt].Seg_gv_eta = GVv.eta();

        float deltaeta = std::sqrt( ( GPp.eta() - hitGp.eta()) * ( GPp.eta() - hitGp.eta()));
        float deltaphi = deltaPhi(GPp.phi(), hitGp.phi());
        float dr;
        int has_ddr = 0;

        if(seg->hasPhi()){
            if(seg->hasZed()){
                dr = std::sqrt ( deltaeta*deltaeta + deltaphi*deltaphi);
                std::cout<<" First has both "<<std::endl;
                has_ddr = 3;
            }else{
                dr = deltaphi;
                std::cout<<" First only has phi "<<std::endl;
                has_ddr = 2;
            }
        }else {
            if(seg->hasZed()){
                dr = deltaeta;
                has_ddr = 1;
                std::cout<<" First only has eta "<<std::endl;
            }else{
                dr = 99;
                std::cout<<" First has none "<<std::endl;
                has_ddr = 0;
            }
        }

        if (dr > 1.0) continue;

        std::cout<<"DT Segment on  MB"<<segdt.wheel()<<segdt.station()<<" with deltaR to SimHits: "<<dr<<std::endl;
        if(std::abs(dr) < std::abs(bestSegdR)){
            bestDTSegBendingAngle1= GVv.phi();
            bestSegdR = dr;
            DTSegment_fist_station = segdt.station();
            has_deta_dphi_dr = has_ddr;
        }

        if(std::abs(dr) < 0.01 ) segDTm = segDTm + 1;

        if(deltaeta < bestSegdEta) bestSegdEta = deltaeta;
        if(deltaphi < bestSegdPhi) bestSegdPhi = deltaphi;


    } // End of first loop

    std::cout<<"Best Bending Angle of the chosen DTSegment: "<<bestDTSegBendingAngle1<<" on with deltar: "<<bestSegdR<<" on station: MBX"<<DTSegment_fist_station<<" with delta: "<<has_deta_dphi_dr<<std::endl;
    etrk_dt_[21].Seg_dphi_sh = bestSegdPhi;
    etrk_dt_[stdt].Seg_dphi_sh = bestSegdPhi;
    etrk_dt_[21].Seg_deta_sh = bestSegdEta;
    etrk_dt_[stdt].Seg_deta_sh = bestSegdEta;
    etrk_dt_[21].Seg_dr_sh = bestSegdR;
    etrk_dt_[stdt].Seg_dr_sh = bestSegdR;
    etrk_dt_[stdt].has_seg_sh_matched = segDTm;
    etrk_dt_[21].has_seg_sh_matched = segDTm;
    etrk_dt_[21].has_eta_phi_dr = has_deta_dphi_dr;
    etrk_dt_[stdt].has_eta_phi_dr = has_deta_dphi_dr;



    // Looking for a second station with hits.
    //
    for(auto s_ddt: dt_chambers)
    {
      const DTChamberId s_iddt(s_ddt);
      const int s_stdt(detIdToMBStation(s_iddt.wheel(),s_iddt.station()));
      if (stationsdt_to_use_.count(s_stdt) == 0) continue;


      const int s_nlayersdtch(match_sh.nSuperLayersWithHitsInChamberDT(s_iddt.rawId()));
      const int d_nlayersdtch(match_sh.nSuperLayersWithHitsInChamberDT(id.rawId()));

      if(s_nlayersdtch == 0) continue; // Check to have hits in the secondary chamber
      if(d_nlayersdtch == 0) continue; //Check that has hits in previous one
      if(id.wheel()==s_iddt.wheel() and id.station()==s_iddt.station()) continue; //Not to count double hits in the same chamber

      GlobalVector ym2 = match_sh.simHitsMeanMomentum(match_sh.hitsInChamber(s_ddt));
      GlobalPoint hitGp2 = match_sh.simHitsMeanPosition(match_sh.hitsInChamber(s_ddt));


      if(s_iddt.station() == 2){
            etrk_dt_[stdt].has_second_dtst_hit = 1;
            etrk_dt_[stdt].deltaphi_first_second_gv= -ym2.phi() + ym.phi();
            etrk_dt_[stdt].deltaphi_first_second_gp=  hitGp.phi() - hitGp2.phi();
            etrk_dt_[stdt].pt_calculated_dt_12 = (1/( -ym2.phi() + ym.phi()))*0.160453 + 3.174856;
            etrk_dt_[stdt].wheel_second = s_iddt.wheel();
            etrk_dt_[stdt].phi_gp_second = hitGp2.phi();
            etrk_dt_[stdt].eta_gp_second = hitGp2.eta();
            etrk_dt_[stdt].phi_gv_second = ym2.phi();
            etrk_dt_[stdt].eta_gv_second = ym2.eta();
        }

      if(s_iddt.station() == 3){
            etrk_dt_[stdt].has_third_dtst_hit = 1;
            etrk_dt_[stdt].deltaphi_first_third_gv= -ym2.phi() + ym.phi();
            etrk_dt_[stdt].deltaphi_first_third_gp=  hitGp.phi() - hitGp2.phi();
            etrk_dt_[stdt].pt_calculated_dt_13 = (1/( -ym2.phi() + ym.phi()))*0.4112057 + 3.599571;
            etrk_dt_[stdt].wheel_third = s_iddt.wheel();
            etrk_dt_[stdt].phi_gp_third = hitGp2.phi();
            etrk_dt_[stdt].eta_gp_third = hitGp2.eta();
            etrk_dt_[stdt].phi_gv_third = ym2.phi();
            etrk_dt_[stdt].eta_gv_third = ym2.eta();
        }

      if(s_iddt.station() == 4){
            etrk_dt_[stdt].has_fourth_dtst_hit = 1;
            etrk_dt_[stdt].deltaphi_first_fourth_gv= -ym2.phi() + ym.phi();
            etrk_dt_[stdt].deltaphi_first_fourth_gp=  hitGp.phi() - hitGp2.phi();
            etrk_dt_[stdt].pt_calculated_dt_14 = (1/( -ym2.phi() + ym.phi()))*0.656863 + 4.1039583;
            etrk_dt_[stdt].wheel_fourth = s_iddt.wheel();
            etrk_dt_[stdt].phi_gp_fourth = hitGp2.phi();
            etrk_dt_[stdt].eta_gp_fourth = hitGp2.eta();
            etrk_dt_[stdt].phi_gv_fourth = ym2.phi();
            etrk_dt_[stdt].eta_gv_fourth = ym2.eta();
        }


       float bestDTSegment_second_BendingAngle = 99.;
       float bestDeltaRSecondST = 99.;
       int has_second_seg_matched = 0;
       int stationsasdf=0;
       for(edm::RangeMap<DTChamberId,edm::OwnVector<DTRecSegment4D,edm::ClonePolicy<DTRecSegment4D> >,edm::ClonePolicy<DTRecSegment4D> >::const_iterator seg2 = SegmentsDT->begin();  seg2!=SegmentsDT->end(); ++seg2)
       {

            auto segdt2 = seg2->chamberId();
            if(!(segdt2.wheel()== s_iddt.wheel() and segdt2.station()==s_iddt.station())) continue; // Same location as the hit.

            etrk_dt_[stdt].has_second_dtSegment = 1;
            etrk_dt_[21].has_second_dtSegment = 1;
            auto lp2 = seg2->localPosition();
            GlobalPoint GPp2 = match_sh.DTSegmentsGlobalPosition(lp2, DTChamberId(segdt2));
            auto gvv2 = seg2->localDirection();
            GlobalVector GVv2 = match_sh.DTSegmentsGlobalVector(gvv2, DTChamberId(segdt2));

            float deltaEta22 = std::abs(GPp2.eta() - hitGp2.eta());
            float deltaPhi22 = deltaPhi( GPp2.phi(), hitGp2.phi());
            float deltar2;

            if(seg2->hasPhi()){
                if(seg2->hasZed()) {
                    deltar2 = std::sqrt(deltaEta22*deltaEta22 + deltaPhi22*deltaPhi22);
                    std::cout<<"Has both deltas"<<std::endl;
                }else{
                    deltar2 = deltaPhi22;
                    std::cout<<" Only has phi "<<std::endl;
                }
            }else{
                if(seg2->hasZed()) {
                    deltar2 = deltaEta22;
                    std::cout<<" Only has eta "<<std::endl;
                }else{
                    deltar2 = 99;
                    std::cout<<" Has none "<<std::endl;
                }
            }

            if (deltar2 > 10) continue;

            if(std::abs(deltar2)<0.01) has_second_seg_matched = has_second_seg_matched + 1;
            if(std::abs(deltar2)< std::abs(bestDeltaRSecondST)) {
                bestDeltaRSecondST = deltar2;
                bestDTSegment_second_BendingAngle = GVv2.phi();
                stationsasdf = segdt2.station();
            }

            std::cout<<"Second DT Segment on Chamber MB"<<segdt2.wheel()<<segdt2.station()<<" with deltaR: "<<deltar2<<" and DeltaEta: "<<deltaEta22<<" and deltaPhi: "<<deltaPhi22<<std::endl;

            etrk_dt_[stdt].Seg_second_wheel = segdt2.wheel();
            etrk_dt_[stdt].Seg_second_station = segdt2.station();
            etrk_dt_[stdt].Seg_second_gp_eta = GPp2.eta();
            etrk_dt_[stdt].Seg_second_gp_phi = GPp2.phi();
            etrk_dt_[stdt].Seg_second_gp_z = GPp2.z();
            etrk_dt_[stdt].Seg_second_gp_y = GPp2.y();
            etrk_dt_[stdt].Seg_second_gp_x = GPp2.x();
            etrk_dt_[stdt].Seg_second_gv_eta = GVv2.eta();
            etrk_dt_[stdt].Seg_second_gv_phi = GVv2.phi();


       }

        if(has_second_seg_matched==0) continue;
        if(bestDeltaRSecondST == 99) continue;

       etrk_dt_[21].has_second_segment_matched = has_second_seg_matched;
       etrk_dt_[stdt].has_second_segment_matched = has_second_seg_matched;
       etrk_dt_[stdt].Seg_second_sh_dr = bestDeltaRSecondST;
       etrk_dt_[21].Seg_second_sh_dr = bestDeltaRSecondST;

        std::cout<<"Best Second DTSegment stored, in MBX"<<stationsasdf<<" with delta R: "<<bestDeltaRSecondST<<" and having "<<has_second_seg_matched<<" segment[s]  matched to that chamber"<<std::endl;

        etrk_dt_[21].Seg_deltaphi_gv = deltaPhi(bestDTSegment_second_BendingAngle, bestDTSegBendingAngle1);
        etrk_dt_[stdt].Seg_deltaphi_gv = deltaPhi(bestDTSegment_second_BendingAngle, bestDTSegBendingAngle1);

       if (DTSegment_fist_station == 1){

            if(stationsasdf==2){
                 etrk_dt_[21].Seg_deltaphi_12_gv= deltaPhi(bestDTSegment_second_BendingAngle, bestDTSegBendingAngle1);
                 etrk_dt_[stdt].Seg_deltaphi_12_gv= deltaPhi(bestDTSegment_second_BendingAngle, bestDTSegBendingAngle1);
                 etrk_dt_[stdt].has_seg_12 =1;
                 etrk_dt_[21].has_seg_12 =1;
            }

            if(stationsasdf==3){
                 etrk_dt_[stdt].Seg_deltaphi_13_gv= deltaPhi(bestDTSegment_second_BendingAngle, bestDTSegBendingAngle1);
                 etrk_dt_[21].Seg_deltaphi_13_gv= deltaPhi(bestDTSegment_second_BendingAngle, bestDTSegBendingAngle1);
                 etrk_dt_[stdt].has_seg_13 =1;
                 etrk_dt_[21].has_seg_13 =1;
            }

            if(stationsasdf==4){
                 etrk_dt_[stdt].Seg_deltaphi_14_gv= deltaPhi(bestDTSegment_second_BendingAngle, bestDTSegBendingAngle1);
                 etrk_dt_[21].Seg_deltaphi_14_gv= deltaPhi(bestDTSegment_second_BendingAngle, bestDTSegBendingAngle1);
                 etrk_dt_[stdt].has_seg_14 =1;
                 etrk_dt_[21].has_seg_14 =1;
                 std::cout<<"Best Bending Angle MBX1 -  MBX4: "<<bestDTSegment_second_BendingAngle<<" with deltaR: "<<bestDeltaRSecondST<<std::endl;
            }

       }



       if( DTSegment_fist_station == 2){

            if(stationsasdf==3){
                 etrk_dt_[21].Seg_deltaphi_23_gv= deltaPhi(bestDTSegment_second_BendingAngle, bestDTSegBendingAngle1);
                 etrk_dt_[stdt].Seg_deltaphi_23_gv= deltaPhi(bestDTSegment_second_BendingAngle, bestDTSegBendingAngle1);
                 etrk_dt_[stdt].has_seg_23 =1;
                 etrk_dt_[21].has_seg_23 =1;
            }

            if(stationsasdf==4){
                 etrk_dt_[21].Seg_deltaphi_24_gv= deltaPhi(bestDTSegment_second_BendingAngle, bestDTSegBendingAngle1);
                 etrk_dt_[stdt].Seg_deltaphi_24_gv= deltaPhi(bestDTSegment_second_BendingAngle, bestDTSegBendingAngle1);
                 etrk_dt_[stdt].has_seg_24 =1;
                 etrk_dt_[21].has_seg_24 =1;
                 std::cout<<"Best Bending Angle MBX2 -  MBX4: "<<bestDTSegment_second_BendingAngle<<" with deltaR: "<<bestDeltaRSecondST<<std::endl;
            }

       }

       if(DTSegment_fist_station == 3) {

            if(stationsasdf==4){
                 etrk_dt_[stdt].Seg_deltaphi_34_gv= deltaPhi(bestDTSegment_second_BendingAngle, bestDTSegBendingAngle1);
                 etrk_dt_[21].Seg_deltaphi_34_gv= deltaPhi(bestDTSegment_second_BendingAngle, bestDTSegBendingAngle1);
                 etrk_dt_[stdt].has_seg_34 =1;
                 etrk_dt_[21].has_seg_34 =1;
                 std::cout<<"Best Bending Angle MBX3 -  MBX4: "<<bestDTSegment_second_BendingAngle<<" with deltaR: "<<bestDeltaRSecondST<<std::endl;
            }
       }




    } // End of Second DT SimHIt


  } // End of DT Sim HIT


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
