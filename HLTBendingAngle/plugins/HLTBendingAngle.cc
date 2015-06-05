// -*- C++ -*-
//
// Package:    MuJetAnalysis/HLTBendingAngle
// Class:      HLTBendingAngle
// 
/**\class HLTBendingAngle HLTBendingAngle.cc MuJetAnalysis/HLTBendingAngle/plugins/HLTBendingAngle.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Jose Dimas
//         Created:  Wed, 03 Jun 2015 20:34:56 GMT
//
//


// system include files
#include <memory>
#include "TTree.h"
#include <iomanip>
#include <sstream>
#include <vector>
using namespace std;
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
#include <Geometry/CommonDetUnit/interface/GeomDet.h>
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
#include "TrackingTools/GeomPropagators/interface/Propagator.h"
#include <Geometry/Records/interface/MuonGeometryRecord.h>
#include "Geometry/Records/interface/MuonGeometryRecord.h"
#include "Geometry/DTGeometry/interface/DTGeometry.h"
#include <DataFormats/DetId/interface/DetId.h>
#include "DataFormats/MuonDetId/interface/DTWireId.h"
#include "DataFormats/MuonDetId/interface/MuonSubdetId.h"
#include <Geometry/CommonDetUnit/interface/GeomDet.h>
#include "DataFormats/GeometryVector/interface/GlobalPoint.h"
#include "Geometry/Records/interface/DTRecoGeometryRcd.h"
#include "Geometry/DTGeometryBuilder/plugins/DTGeometryESModule.h"
#include "FWCore/Framework/interface/EventSetupRecordImplementation.h"
#include "Geometry/Records/interface/DTRecoGeometryRcd.h"
#include "FWCore/Framework/interface/eventsetuprecord_registration_macro.h"

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
 Char_t nlayerdt;
 Float_t R_gv;
 Float_t Z_gv;
 Float_t X_gv;
 Float_t Y_gv;
};

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
 has_dt_sh=0;
 nlayerdt = 0;
 R_gv=-9999.;
 Z_gv=-9999.;
 X_gv=-9999.;
 Y_gv=-9999.;

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


int chamber(const DetId& id);

std::vector<std::pair<int,int> > dtStationsCo_;

//
// class declaration
//

class HLTBendingAngle : public edm::EDAnalyzer {
   public:
      explicit HLTBendingAngle(const edm::ParameterSet&);
      ~HLTBendingAngle();

      //Originally from Base Matcher
      enum DTType { DT_ALL = 0, DT_MB10, DT_MB11, DT_MB12, DT_MB20, DT_MB21,
                DT_MB22, DT_MB30, DT_MB31, DT_MB32, DT_MB40, DT_MB41, DT_MB42};


      virtual void beginJob() ;

      int check_is_dt(unsigned int detId) const;

      GlobalPoint propagateToZ(GlobalPoint &inner_point, GlobalVector &inner_vector, float z) const;
      GlobalPoint propagateToZ(float z) const;

      edm::ESHandle<DTGeometry> dt_geom;
      const DTGeometry* dtGeometry_;
      bool hasDTGeometry_;

      std::set<unsigned int> detIdsDT() const;
      std::set<unsigned int> layerIdsDT() const;
      std::set<unsigned int> chamberIdsDT() const;

      int nLayerWithHitsInChamberDT (unsigned int) const;
      int nLayerWithHitsInSuperlayerDT (unsigned int) const;
      const edm::PSimHitContainer& hitsInDetIdDT(unsigned int) const;
      const edm::PSimHitContainer& hitsInSuperlayerDT(unsigned int) const;
      const edm::PSimHitContainer& hitsInChamberDT(unsigned int) const;

      edm::ESHandle<MagneticField> magfield_;
      edm::ESHandle<Propagator> propagator_;
      edm::ESHandle<Propagator> propagatorOpposite_;

      GlobalPoint simHitsMeanPosition(const edm::PSimHitContainer& sim_hits) const;
      GlobalPoint detidToGlobalDT(const edm::PSimHitContainer& sim_hits) const;
      GlobalVector detDTGlobalPT(const edm::PSimHitContainer& sim_hits) const;
      const edm::PSimHitContainer& hitsInLayerDT(unsigned int) const;
      virtual void beginRun(edm::Run const& run, edm::EventSetup const& es) ;
      virtual void analyze(const edm::Event&, const edm::EventSetup&) ;

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

      void matchSimHitsToSimTrack(std::vector<unsigned int> track_ids, const edm::PSimHitContainer& hits_dt);
      int nLayerWithHitsInLayerDT (unsigned int) const;

      virtual void endJob() ;
   private:

      void analyzeTrackEfficiency(const SimTrack& t, const SimVertex& v, const edm::Event& ev, const edm::EventSetup& es, int trk_no);

      std::vector<unsigned int> getIdsOfSimTrackShower(unsigned  trk_id,
           		      const edm::SimTrackContainer& simTracks, const edm::SimVertexContainer& simVertices);


      bool simMuOnlyDT_;
      bool discardEleHitsDT;
      bool runDTSimHit_;

      std::map<unsigned int, unsigned int> trkid_to_index_;
      bool isSimTrackGood(const SimTrack &t);
      edm::PSimHitContainer no_hits_;

      edm::PSimHitContainer dt_hits_;
      std::map<unsigned int, edm::PSimHitContainer > dt_detid_to_hits_;
      std::map<unsigned int, edm::PSimHitContainer > dt_layer_to_hits_;
      std::map<unsigned int, edm::PSimHitContainer > dt_chamber_to_hits_;

      //edm::InputTag dtSimHitInput_;

      edm::Handle<edm::PSimHitContainer> dt_hits;
      edm::Handle<edm::SimTrackContainer> sim_tracks;
      edm::Handle<edm::SimVertexContainer> sim_vertices;


      int detIdToMBStation(int wh, int st);
      std::vector<string> dtStations_;
      std::set<int> stationsdt_to_use_;
      TTree *tree_eff_dt_[26];
      MyTrackEffDT etrk_dt_[26];
      double vtx_dt;
      double vty_dt;
      double vtz_dt; 
      double simTrackMinEta_;
      double simTrackMaxEta_;
      double simTrackOnlyMuon_;
      int verbose_;


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
HLTBendingAngle::HLTBendingAngle(const edm::ParameterSet& iConfig)
{
   //now do what ever initialization is needed

  // auto input = cms.InputTag("g4SimHits","MuonDTHits");
  std::vector<string> stationsDT; 
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



void
HLTBendingAngle::beginRun(edm::Run const& run, edm::EventSetup const& es)
{

  try {
    es.get<MuonGeometryRecord>().get(dt_geom);
    dtGeometry_ = &*dt_geom;
    } catch (edm::eventsetup::NoProxyException<DTGeometry>& e){
      hasDTGeometry_ = false;
      LogDebug("MuonSimHitAnalyzer") <<" +++ Informatione: DT geometry is unavailable. ++++ \n";

    }




};

bool HLTBendingAngle::isSimTrackGood(const SimTrack &t)
{

  bool simTrackOnlyMuon_ = true;
  
  if (t.noVertex()) return false;
  if (t.noGenpart()) return false;
  if (std::abs(t.type()) != 13 and simTrackOnlyMuon_) return false;
  if (t.momentum().pt() < 0) return false;

  return true;
}

HLTBendingAngle::~HLTBendingAngle()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
HLTBendingAngle::analyze(const edm::Event& ev, const edm::EventSetup& es)
{
   using namespace edm;


 /*
  
  event().getByLabel(mInputLabel_, sim_tracks);
  event().getByLabel(simInputLabel_, sim_vertices);
  event().getByLabel(dtSimHitInput_, dt_hits);
*/

 // auto simInputLabel_ = "hltL1extraParticles";
 //
 //
  auto simInputLabel_ = "g4SimHits";
  edm::Handle<edm::SimTrackContainer> sim_tracks;
  edm::Handle<edm::SimVertexContainer> sim_vertices;

  ev.getByLabel(simInputLabel_, sim_tracks);
  ev.getByLabel(simInputLabel_, sim_vertices);
  const edm::SimVertexContainer & sim_vert = *sim_vertices.product();
  const edm::SimTrackContainer & sim_track = *sim_tracks.product();

  //std::cout << "Total number of SimTrack in this event: " << sim_track.size() << std::endl;
  int trk_no=0;
  for (auto& t: *sim_tracks.product())
  {

    if(!isSimTrackGood(t)) continue;
    vtx_dt = sim_vert[t.vertIndex()].position().x();
    vty_dt = sim_vert[t.vertIndex()].position().y();
    vtz_dt = sim_vert[t.vertIndex()].position().z();


    int no = 0;
    trkid_to_index_.clear();
    for (auto& t2: *sim_tracks.product())
    {
      trkid_to_index_[t2.trackId()] = no;
      no++;
    }

    vector<unsigned> track_ids = getIdsOfSimTrackShower(t.trackId(), *sim_tracks.product(), *sim_vertices.product());

    //edm::InputTag dtSimHitInput_ = ("g4SimHits","MuonDTHits");
    ev.getByLabel("g4SimHits","MuonDTHits", dt_hits);
  
    const edm::PSimHitContainer & hits_dt = *dt_hits.product();


    std::cout<<"Size of track: "<<track_ids.size()<<" , size of simhits: "<<hits_dt.size()<<std::endl;
    matchSimHitsToSimTrack(track_ids, hits_dt);

    analyzeTrackEfficiency(t, sim_vert[t.vertIndex()], ev, es , trk_no);
  
    //trk_no = trk_no + 1;
  } 
	

}




void 
HLTBendingAngle::analyzeTrackEfficiency(const SimTrack& t, const SimVertex& v, const edm::Event& ev, const edm::EventSetup& es, int trk_no)
{

  for (auto asdt: stationsdt_to_use_)
    {
    etrk_dt_[asdt].init();
    etrk_dt_[asdt].run = ev.id().run();
    etrk_dt_[asdt].lumi= ev.id().luminosityBlock();
    etrk_dt_[asdt].event = ev.id().event();
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
     
    } 


   auto dt_simhits = layerIdsDT();


   std::cout<<" Size of dt sh: "<<dt_simhits.size()<<std::endl;
   for (auto ddt: dt_simhits)
   {

    if (check_is_dt(ddt) == 0) continue;
    DTWireId iddt(ddt);
    const int stdt(detIdToMBStation(iddt.wheel(),iddt.station()));
    if (stationsdt_to_use_.count(stdt) == 0) continue;

    int nlayersdtch = nLayerWithHitsInLayerDT(iddt);
    
    if (nlayersdtch == 0) continue;

     etrk_dt_[stdt].has_dt_sh |= 1;
     etrk_dt_[stdt].nlayerdt  = nlayersdtch;

    GlobalPoint hitGp = detidToGlobalDT(hitsInLayerDT(ddt));


    etrk_dt_[stdt].eta_gp = hitGp.eta();
/*    etrk_dt_[stdt].x_gp = hitGp.x();
    etrk_dt_[stdt].y_gp = hitGp.y();
    etrk_dt_[stdt].z_gp = hitGp.z();
    etrk_dt_[stdt].r_gp = hitGp.perp();
    etrk_dt_[stdt].phi_gp = hitGp.phi();

    GlobalVector ym = detDTGlobalPT(hitsInLayerDT(ddt));

    etrk_dt_[stdt].eta_gv = ym.eta();
    etrk_dt_[stdt].pt_gv = ym.perp();
    etrk_dt_[stdt].phi_gv = ym.phi();
    etrk_dt_[stdt].R_gv = sqrt (ym.x()*ym.x()+ym.y()*ym.y());
    etrk_dt_[stdt].Z_gv = ym.z();
    etrk_dt_[stdt].X_gv = ym.x();
    etrk_dt_[stdt].Y_gv = ym.y();
    //etrk_dt_[stdt].deltaphi_h_g = hitGp.phi() - ym.phi();     //This one

    //etrk_dt_[stdt].pt_calculated_dt = (1/(hitGp.phi() - ym.phi()))*1.4025845 + 0.674463;


    for (auto s_ddt: dt_simhits) // Looking for a second hit in DT stations 
    {
      DTWireId s_iddt(s_ddt);
      const int s_stdt(detIdToMBStation(s_iddt.wheel(),s_iddt.station()));
      if (stationsdt_to_use_.count(s_stdt) == 0) continue;
      int s_nlayersdtch = nLayerWithHitsInLayerDT(s_ddt);
      int d_nlayersdtch = nLayerWithHitsInLayerDT(ddt);

      if(s_nlayersdtch == 0) continue; // Check to have hits in the secondary chamber
      if(d_nlayersdtch == 0) continue; //Check that has hits in previous one
      if(iddt.wheel()==s_iddt.wheel() and iddt.station()==s_iddt.station()) continue; //Not to count double hits in the same chamber

      if(s_iddt.station() == 2){
            GlobalPoint s_hitGp = detidToGlobalDT(hitsInLayerDT(s_ddt));
            GlobalVector s_ym = detDTGlobalPT(hitsInLayerDT(s_ddt));
            etrk_dt_[stdt].has_second_dtst_hit = 1;
            etrk_dt_[stdt].deltaphi_first_second_gv= -s_ym.phi() + ym.phi();
            etrk_dt_[stdt].deltaphi_first_second_gp=  hitGp.phi() - s_hitGp.phi();
            etrk_dt_[stdt].pt_calculated_dt_12 = (1/( -s_ym.phi() + ym.phi()))*0.160453 + 3.174856;
            etrk_dt_[stdt].wheel_second = s_iddt.wheel();
            etrk_dt_[stdt].phi_gp_second = s_hitGp.phi();
            etrk_dt_[stdt].eta_gp_second = s_hitGp.eta();
            etrk_dt_[stdt].phi_gv_second = s_ym.phi();
            etrk_dt_[stdt].eta_gv_second = s_ym.eta();
        }

      if(s_iddt.station() == 3){
            GlobalPoint t_hitGp = detidToGlobalDT(hitsInLayerDT(s_ddt));
            GlobalVector t_ym = detDTGlobalPT(hitsInLayerDT(s_ddt));
            etrk_dt_[stdt].has_third_dtst_hit = 1;
            etrk_dt_[stdt].deltaphi_first_third_gv= -t_ym.phi() + ym.phi();
            etrk_dt_[stdt].deltaphi_first_third_gp=  hitGp.phi() - t_hitGp.phi();
            etrk_dt_[stdt].pt_calculated_dt_13 = (1/( -t_ym.phi() + ym.phi()))*0.4112057 + 3.599571;
            etrk_dt_[stdt].wheel_third = s_iddt.wheel();
            etrk_dt_[stdt].phi_gp_third = t_hitGp.phi();
            etrk_dt_[stdt].eta_gp_third = t_hitGp.eta();
            etrk_dt_[stdt].phi_gv_third = t_ym.phi();
            etrk_dt_[stdt].eta_gv_third = t_ym.eta();
        }

      if(s_iddt.station() == 4){
            GlobalPoint f_hitGp = detidToGlobalDT(hitsInLayerDT(s_ddt));
            GlobalVector f_ym = detDTGlobalPT(hitsInLayerDT(s_ddt));
            etrk_dt_[stdt].has_fourth_dtst_hit = 1;
            etrk_dt_[stdt].deltaphi_first_fourth_gv= -f_ym.phi() + ym.phi();
            etrk_dt_[stdt].deltaphi_first_fourth_gp=  hitGp.phi() - f_hitGp.phi();
            etrk_dt_[stdt].pt_calculated_dt_14 = (1/( -f_ym.phi() + ym.phi()))*0.656863 + 4.1039583;
            etrk_dt_[stdt].wheel_fourth = s_iddt.wheel();
            etrk_dt_[stdt].phi_gp_fourth = f_hitGp.phi();
            etrk_dt_[stdt].eta_gp_fourth = f_hitGp.eta();
            etrk_dt_[stdt].phi_gv_fourth = f_ym.phi();
            etrk_dt_[stdt].eta_gv_fourth = f_ym.eta();
        }


     }

*/




   }




 for (auto sdt: stationsdt_to_use_)
    {
    tree_eff_dt_[sdt]->Fill();

    }


}




int HLTBendingAngle::check_is_dt(unsigned int detId) const
{
  if( (DetId(detId)).subdetId() == MuonSubdetId::DT) return 1;
  else return 0;
}


GlobalPoint
HLTBendingAngle::detidToGlobalDT(const edm::PSimHitContainer& sim_hits) const
{
  if (sim_hits.empty()) return GlobalPoint();
  GlobalPoint GP;
  float sumx, sumy, sumz;
  sumx = sumy = sumz = 0.;
  size_t n = 0;

  for(auto& h: sim_hits) {

    if (check_is_dt(h.detUnitId())==0) continue;
    LocalPoint lp = h.localPosition();
        
    GP =dtGeometry_->idToDet(h.detUnitId())->surface().toGlobal(lp);

    sumx += GP.x();
    sumy += GP.y();
    sumz += GP.z();
    ++n;

  }

 if (n == 0) return GlobalPoint();

 return GlobalPoint(sumx/n, sumy/n, sumz/n);


}

GlobalVector
HLTBendingAngle::detDTGlobalPT(const edm::PSimHitContainer& sim_hits) const
{

if (sim_hits.empty()) return GlobalVector();;

for(auto& h: sim_hits) {

    if (check_is_dt(h.detUnitId())==0) continue;
    GlobalVector globalMomentum = dtGeometry_->idToDet(h.detUnitId())->surface().toGlobal(h.momentumAtEntry());
    return globalMomentum;
}

return GlobalVector();

}




int
HLTBendingAngle::nLayerWithHitsInLayerDT(unsigned int detid) const
{
    set<int> DT_layers_with_hits;
    auto hits=hitsInLayerDT(detid);
    for (auto& h: hits)
    {
    
    DTWireId idd(h.detUnitId());
    DT_layers_with_hits.insert(idd.layerId());
    }
    return DT_layers_with_hits.size();

}


const edm::PSimHitContainer&
HLTBendingAngle::hitsInLayerDT(unsigned int detid) const
{

    int test = check_is_dt(detid);

    if (test==1)
    {
        DTWireId id(detid);
        if (dt_layer_to_hits_.find(id.layerId().rawId()) == dt_layer_to_hits_.end()) return no_hits_;
        return dt_layer_to_hits_.at(id.layerId().rawId());
    }

    return no_hits_;
}



std::set<unsigned int>
HLTBendingAngle::layerIdsDT() const
{
    std::set<unsigned int> result;
    for (auto& p: dt_layer_to_hits_) result.insert(p.first);
    return result;

}


void
HLTBendingAngle::matchSimHitsToSimTrack(std::vector<unsigned int> track_ids,
                                      const edm::PSimHitContainer& hits_dt)
{

  bool discardEleHitsDT_ = true;
  bool simMuOnlyDT_ = true;

  for (auto& track_id: track_ids)
  {

   

    for (auto& hs: hits_dt)
    {

      if (hs.trackId() != track_id) continue;

      int DTonly = check_is_dt(hs.detUnitId());
      if (DTonly == 0) continue;


      int pdgid = hs.particleType();
      if (simMuOnlyDT_ && !(std::abs(pdgid) == 13)) continue;

      if (discardEleHitsDT_ && pdgid == 11) continue; 

      dt_detid_to_hits_[ hs.detUnitId() ].push_back(hs);
      DTWireId layer_id( hs.detUnitId() );
      dt_hits_.push_back(hs);
      dt_layer_to_hits_ [ layer_id.layerId().rawId() ].push_back(hs);
      dt_chamber_to_hits_[ layer_id.chamberId().rawId() ].push_back(hs);
    }

  }

}

std::vector<unsigned int>
HLTBendingAngle::getIdsOfSimTrackShower(unsigned int initial_trk_id,
    const edm::SimTrackContainer & sim_tracks, const edm::SimVertexContainer & sim_vertices)
{
  vector<unsigned int> result;
  result.push_back(initial_trk_id);

  for (auto& t: sim_tracks)
  {
    SimTrack last_trk = t;
    bool is_child = 0;
    while (1)
    {
      if ( last_trk.noVertex() ) break;
      if ( sim_vertices[last_trk.vertIndex()].noParent() ) break;
      
      unsigned parentId = sim_vertices[last_trk.vertIndex()].parentIndex();
      if ( parentId == initial_trk_id )
      {
        is_child = 1;
        break;
      }
      
      auto association = trkid_to_index_.find( parentId );
      if ( association == trkid_to_index_.end() ) break;

      last_trk = sim_tracks[ association->second ];
    }
    if (is_child)
    {
      result.push_back(t.trackId());
    }
  }
  return result;
}






// ------------ method called once each job just before starting event loop  ------------
void 
HLTBendingAngle::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
HLTBendingAngle::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
/*
void 
HLTBendingAngle::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

*/
// ------------ method called when ending the processing of a run  ------------
/*
void 
HLTBendingAngle::endRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when starting to processes a luminosity block  ------------
/*
void 
HLTBendingAngle::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a luminosity block  ------------
/*
void 
HLTBendingAngle::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
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
