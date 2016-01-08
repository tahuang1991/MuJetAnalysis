// -*- C++ -*-
//
// Package:    DisplacedL1MuFilter
// Class:      DisplacedL1MuFilter
// 
/**\class DisplacedL1MuFilter DisplacedL1MuFilter.cc MuJetAnalysis/DisplacedL1MuFilter/plugins/DisplacedL1MuFilter.cc

   We assume that the displacement is reasonable (What is reasonable here? $d_{xy} < 10$ cm) 
   We require the L1Mu to be of good quality (Q>=4). L1Tk matching to L1Mu within dR<0.12 
   are vetoed. Most muons in minbias events stem from kaon decay and b-quark decay and are 
   sufficiently prompt. The (eta,phi) coordinates of L1Mu used in the dR calculation are 
   those of the second station. In addition, we veto L1Tk with pT>4 GeV (somewhat ad-hoc 
   number) within dR<0.4. This cut is effectively an isolation cut. For studies with highly 
   parallel muons, coming from e.g. low mass dark photon decay, this may cut significantly 
   on the signal. To suppress the fake rate, one might set an upper cut, e.g. pT<10 GeV.

   To estimate the rate reduction Sven will take a MinBias sample from Slava and build a 
   filter. We reject all events that have at least one muon that pass the requirements 
   for a prompt muon: (1) Q>=4 and matched to L1Tk within dR<0.12 or (2) unmatched to 
   L1Tk but with at least one L1Tk within  dR<0.4 with pt>4

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  sven dildick
//         Created:  Fri, 20 Nov 2015 12:22:11 GMT
// $Id$
//
//


// system include files
#include <memory>

#include "TTree.h"
#include "TFile.h"

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDFilter.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/HepMCCandidate/interface/GenParticleFwd.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "L1Trigger/CSCTrackFinder/test/src/TFTrack.h"
#include "DataFormats/L1Trigger/interface/L1MuonParticleFwd.h"
#include "DataFormats/L1Trigger/interface/L1MuonParticle.h"
#include "DataFormats/L1GlobalMuonTrigger/interface/L1MuGMTReadoutCollection.h"
#include "DataFormats/L1TrackTrigger/interface/L1TkMuonParticle.h"
#include "DataFormats/L1TrackTrigger/interface/L1TkMuonParticleFwd.h"
#include "DataFormats/L1TrackTrigger/interface/TTTrack.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "MagneticField/Engine/interface/MagneticField.h"
#include "TrackingTools/GeomPropagators/interface/Propagator.h"
#include "TrackingTools/TrajectoryState/interface/TrajectoryStateOnSurface.h"
#include "TrackingTools/Records/interface/TrackingComponentsRecord.h"
#include "MagneticField/Records/interface/IdealMagneticFieldRecord.h"
#include "DataFormats/GeometrySurface/interface/Plane.h"
#include "DataFormats/GeometrySurface/interface/Cylinder.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "SimDataFormats/Track/interface/SimTrackContainer.h"
#include "SimDataFormats/Vertex/interface/SimVertexContainer.h"
#include "DataFormats/Math/interface/normalizedPhi.h"

//
// class declaration
//

const Int_t kMaxL1Mu = 50;
const int nGlu = 2;
const int nGd = 2;
const int nGdMu = 2;


struct MyEvent
{
  Int_t lumi, run, event;

  Float_t beamSpot_x;
  Float_t beamSpot_y;
  Float_t beamSpot_z;

  Float_t genGlu_p[2];
  Float_t genGlu_pt[2];
  Float_t genGlu_px[2];
  Float_t genGlu_py[2];
  Float_t genGlu_pz[2];
  Float_t genGlu_eta[2];
  Float_t genGlu_phi[2];

  Float_t genH_m;
  Float_t genH_p;
  Float_t genH_pt;
  Float_t genH_px;
  Float_t genH_py;
  Float_t genH_pz;
  Float_t genH_eta;
  Float_t genH_phi;
  Float_t genH_vx;
  Float_t genH_vy;
  Float_t genH_vz;

  // Dark photon  
  Float_t genGd_m[2];
  Float_t genGd_E[2];
  Float_t genGd_p[2];
  Float_t genGd_pt[2];
  Float_t genGd_px[2];
  Float_t genGd_py[2];
  Float_t genGd_pz[2];
  Float_t genGd_eta[2];
  Float_t genGd_phi[2];
  Float_t genGd_vx[2];
  Float_t genGd_vy[2];
  Float_t genGd_vz[2];
  Float_t genGd_vLx[2];
  Float_t genGd_vLy[2];
  Float_t genGd_vLz[2];
  Float_t genGd_lxy[2];
  Float_t genGd_l[2];
  Float_t genGd_dxy[2];
  Float_t genGdMu_dxy_max[2];

  // Gen level muon
  Float_t genGdMu_q[2][2];
  Float_t genGdMu_p[2][2];
  Float_t genGdMu_pt[2][2];
  Float_t genGdMu_px[2][2];
  Float_t genGdMu_py[2][2];
  Float_t genGdMu_pz[2][2];
  Float_t genGdMu_eta[2][2];
  Float_t genGdMu_phi[2][2];
  Float_t genGdMu_phi_corr[2][2];
  Float_t genGdMu_vx[2][2];
  Float_t genGdMu_vy[2][2];
  Float_t genGdMu_vz[2][2];
  Float_t genGdMu_dxy[2][2];


  Int_t nL1Mu;
  Float_t L1Mu_pt[kMaxL1Mu], L1Mu_eta[kMaxL1Mu], L1Mu_phi[kMaxL1Mu];
  Int_t L1Mu_charge[kMaxL1Mu], L1Mu_bx[kMaxL1Mu];
  Int_t L1Mu_quality[kMaxL1Mu];
  Int_t L1Mu_isMatched[kMaxL1Mu];
  Int_t L1Mu_isUnMatched[kMaxL1Mu];
  Int_t L1Mu_isUnMatchedL1TkPt2[kMaxL1Mu];
  Int_t L1Mu_isUnMatchedL1TkPt3[kMaxL1Mu];
  Int_t L1Mu_isUnMatchedL1TkPt4[kMaxL1Mu];

  Float_t genGdMu_L1Mu_dR_corr[2][2];
  Int_t genGdMu_L1Mu_index_corr[2][2];

  Int_t has_sim;
  Float_t pt_sim, eta_sim, phi_sim, charge_sim;
  Float_t eta_sim_prop, phi_sim_prop;
  Float_t eta_sim_corr, phi_sim_corr;
  Float_t dEta_sim_corr, dPhi_sim_corr, dR_sim_corr;
  Float_t dEta_sim_prop, dPhi_sim_prop, dR_sim_prop;
  Float_t pt_L1Tk, eta_L1Tk, phi_L1Tk, charge_L1Tk;
  Float_t eta_L1Tk_corr, phi_L1Tk_corr;
  Float_t eta_L1Tk_prop, phi_L1Tk_prop;
  Float_t dEta_L1Tk_corr, dPhi_L1Tk_corr, dR_L1Tk_corr;
  Float_t dEta_L1Tk_prop, dPhi_L1Tk_prop, dR_L1Tk_prop;
  Float_t dEta_sim_L1Tk, dPhi_sim_L1Tk, dR_sim_L1Tk;
};

bool PtOrder (const reco::GenParticle* p1, const reco::GenParticle* p2) 
{ 
  return (p1->pt() > p2->pt() ); 
}

double dxy(double px, double py, double vx, double vy, double pt)
{
  //Source: https://cmssdt.cern.ch/SDT/lxr/source/DataFormats/TrackReco/interface/TrackBase.h#119
  return (- vx * py + vy * px ) / pt;
}

double 
phiHeavyCorr(double pt, double eta, double phi, double q)
{
  //  float resEta = eta;
  float etaProp = std::abs(eta);
  if (etaProp< 1.1) etaProp = 1.1;
  float resPhi = phi - 1.464*q*cosh(1.7)/cosh(etaProp)/pt - M_PI/144.;
  if (resPhi > M_PI) resPhi -= 2.*M_PI;
  if (resPhi < -M_PI) resPhi += 2.*M_PI;
  return resPhi;
}

double dRWeighted(double eta1, double phi1, double eta2, double phi2, double sigma_eta=2., double sigma_phi=1.)
{
  double dEta = std::abs(eta1 - eta2);
  double dPhi = reco::deltaPhi(phi1, phi2);
  double dR = std::sqrt((dEta*dEta)/(sigma_eta*sigma_eta) + (dPhi*dPhi)/(sigma_phi*sigma_phi));
  return dR;
}

bool 
isSimTrackGood(const SimTrack &t)
{
  // SimTrack selection
  if (t.noVertex()) return false;
  if (t.noGenpart()) return false;
  // only muons 
  if (std::abs(t.type()) != 13) return false;
  // pt selection
  //if (t.momentum().pt() < simTrackMinPt_) return false;
  // eta selection
  const float eta(std::abs(t.momentum().eta()));
  if (eta > 2.5) return false; 
  return true;
}

using namespace std;

class DisplacedL1MuFilter : public edm::EDFilter 
{
public:
  explicit DisplacedL1MuFilter(const edm::ParameterSet&);
  ~DisplacedL1MuFilter();
  
  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
  
private:
  void bookL1MuTree();
  virtual void beginJob() override;
  virtual bool filter(edm::Event&, const edm::EventSetup&) override;
  virtual void endJob() override;
  GlobalPoint propagateToZ(const GlobalPoint &inner_point, const GlobalVector &inner_vec, double, double) const;
  GlobalPoint propagateToR(const GlobalPoint &inner_point, const GlobalVector &inner_vec, double, double) const;
  void clearBranches();
  //virtual void beginRun(edm::Run const&, edm::EventSetup const&) override;
  //virtual void endRun(edm::Run const&, edm::EventSetup const&) override;
  //virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
  //virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
  
  int min_L1Mu_Quality;
  double dR_L1Mu_L1Tk;
  double dR_L1Mu_noL1Tk;
  double min_pT_L1Tk;
  double max_pT_L1Tk;
  int nTotalMuons = 0;
  // int nPromptMuons = 0;
  int eventPassing = 0;
  int verbose;
  int eventsWithMuons = 0;
  int eventsWithDisplacedMuons = 0;
  int eventsWithDisplacedMuonsPt = 0;

  edm::InputTag L1Mu_input;
  edm::InputTag L1TkMu_input;
  
  edm::ESHandle<MagneticField> magfield_;
  edm::ESHandle<Propagator> propagator_;
  edm::ESHandle<Propagator> propagatorOpposite_;
  MyEvent event_;
  TTree* event_tree_;
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
DisplacedL1MuFilter::DisplacedL1MuFilter(const edm::ParameterSet& iConfig)
{
  //now do what ever initialization is needed
  min_L1Mu_Quality = iConfig.getParameter<int>("L1MuQuality");
  dR_L1Mu_L1Tk = iConfig.getParameter<double>("dR_L1Mu_L1Tk");
  dR_L1Mu_noL1Tk = iConfig.getParameter<double>("dR_L1Mu_noL1Tk");
  min_pT_L1Tk = iConfig.getParameter<double>("min_pT_L1Tk");
  max_pT_L1Tk = iConfig.getParameter<double>("max_pT_L1Tk");
  verbose = iConfig.getParameter<int>("verbose");
  
  L1Mu_input = iConfig.getParameter<edm::InputTag>("L1Mu_input");
  L1TkMu_input = iConfig.getParameter<edm::InputTag>("L1TkMu_input");
  
  bookL1MuTree();
}

DisplacedL1MuFilter::~DisplacedL1MuFilter()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called on each new Event  ------------
bool
DisplacedL1MuFilter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  double eq = 0.000001;

  clearBranches();
  
  // propagator
  iSetup.get<IdealMagneticFieldRecord>().get(magfield_);
  iSetup.get<TrackingComponentsRecord>().get("SteppingHelixPropagatorAlong", propagator_);
  iSetup.get<TrackingComponentsRecord>().get("SteppingHelixPropagatorOpposite", propagatorOpposite_);

  edm::Handle<L1MuGMTReadoutCollection> hl1GmtCands;
  iEvent.getByLabel(L1Mu_input, hl1GmtCands );
  std::vector<L1MuGMTExtendedCand> l1GmtCands;

  // Get GMT candidates from all bunch crossings
  auto gmt_records = hl1GmtCands->getRecords();
  for (auto rItr = gmt_records.begin(); rItr!=gmt_records.end() ; ++rItr ){
    if (rItr->getBxInEvent() < -1 || rItr->getBxInEvent() > 1) continue;
    
    auto GMTCands = rItr->getGMTCands();
    for (auto cItr = GMTCands.begin() ; cItr != GMTCands.end() ; ++cItr )
      if (!cItr->empty()) l1GmtCands.push_back(*cItr);
  }

  // // L1 Trigger Analysis
  // edm::Handle<l1extra::L1MuonParticleCollection> muonsHandle;
  // iEvent.getByLabel("l1extraParticles", muonsHandle);
  // //const l1extra::L1MuonParticleCollection& muons = *muonsHandle.product();

  // L1 TrackingTrigger Analysis
  edm::Handle< std::vector< TTTrack< Ref_PixelDigi_ > > > TTTrackHandle;
  iEvent.getByLabel("TTTracksFromPixelDigis", "Level1TTTracks", TTTrackHandle);
  const std::vector< TTTrack< Ref_PixelDigi_ > >& TTTracks = *TTTrackHandle.product();

  edm::Handle<l1extra::L1TkMuonParticleCollection> tkMuonsHandle;
  // use both barrel+endcap muons
  iEvent.getByLabel(L1TkMu_input, tkMuonsHandle);
  //const l1extra::L1TkMuonParticleCollection& tkMuons = *tkMuonsHandle.product();

  // edm::Handle<edm::SimTrackContainer> sim_tracks;
  // iEvent.getByLabel("g4SimHits", sim_tracks);
  // const edm::SimTrackContainer & sim_trks = *sim_tracks.product();

  // edm::Handle<edm::SimVertexContainer> sim_vertices;
  // iEvent.getByLabel("g4SimHits", sim_vertices);
  // const edm::SimVertexContainer & sim_vtxs = *sim_vertices.product();
  
  // 1) count the number of muons with 
  // int nL1MuL1TkdR012 = 0;
  // int nL1MuQuality4 = 0;
  // int nL1MuMatched = 0;
  // int nL1MuUnMatched = 0;
  int nL1Mu = l1GmtCands.size();
  event_.lumi = iEvent.id().luminosityBlock();
  event_.run = iEvent.id().run();
  event_.event = iEvent.id().event();
  event_.nL1Mu = nL1Mu;
  // int nL1Tk = TTTracks.size();
  
  event_.beamSpot_x = 0;
  event_.beamSpot_y = 0;
  event_.beamSpot_z = 0;

  //////////////////
  // GEN analysis //
  //////////////////

  edm::Handle<reco::GenParticleCollection> genParticles;
  iEvent.getByLabel("genParticles", genParticles);
  
  // Loop over all genParticles and save prompt muons from particles with codes 36 (a1) or 3000022 (gammaD) in vector genMuons
  std::vector<const reco::GenParticle*> genGlu_unsorted;
  std::vector<const reco::GenParticle*> genGlu;
  std::vector<const reco::GenParticle*> genH;
  std::vector<const reco::GenParticle*> genGd_unsorted;
  std::vector<const reco::GenParticle*> genGd;
  std::vector<const reco::GenParticle*> genMuons;
  std::vector<const reco::Candidate*>   genMuonMothers;
  // Loop over all gen particles
  int counterGenParticle = 0;
  for(reco::GenParticleCollection::const_iterator iGenParticle = genParticles->begin();  iGenParticle != genParticles->end();  ++iGenParticle) {
    counterGenParticle++;
    //    cout << counterGenParticle << " " << iGenParticle->status() << " " << iGenParticle->pdgId() << " " << iGenParticle->vx() << " " << iGenParticle->vy() << " " << iGenParticle->vz() << endl;
    // Check if gen particle is muon (pdgId = +/-13) and stable (status = 1)
    if ( fabs( iGenParticle->pdgId() ) == 13 and iGenParticle->status() == 1 ) {
      // Mother of the muon can be muon. Find the last muon in this chain: genMuonCand
      // Example: a1 -> mu+ (status = 3) mu- (status = 3)
      //          mu- (status = 3) -> mu- (status = 2) -> mu- (status = 1)
      const reco::Candidate *genMuonCand = &(*iGenParticle);
      bool isMuonMother = true;
      while(isMuonMother) {
        isMuonMother = false;
        for ( size_t iMother = 0; iMother < genMuonCand->numberOfMothers(); iMother++ ) {
          if ( fabs( genMuonCand->mother(iMother)->pdgId() ) == 13 ) {
            isMuonMother = true;
            genMuonCand = genMuonCand->mother(iMother);
          }
        }
      }
      // Loop over all real (non-muon) mothers of the muon (here we use genMuonCand)
      for ( size_t iMother = 0; iMother < genMuonCand->numberOfMothers(); iMother++ ) {
        // Check if mother is CP-odd Higgs (PdgId = 36) or gamma_Dark (PdgId = 3000022)
        //        if ( genMuonCand->mother(iMother)->pdgId() == 36 || genMuonCand->mother(iMother)->pdgId() == 3000022 || genMuonCand->mother(iMother)->pdgId() == 443 ) {
        if ( genMuonCand->mother(iMother)->pdgId() == 36 || genMuonCand->mother(iMother)->pdgId() == 3000022 ) {
          // Store the muon (stable, first in chain) into vector
          genMuons.push_back(&(*iGenParticle));
          // Store mother of the muon into vector. We need this to group muons into dimuons later
          genMuonMothers.push_back(genMuonCand->mother(iMother));
        }
      }
    }
    // Check if gen particle is
    if (    ( iGenParticle->status() == 3 and iGenParticle->pdgId() == 25 ) // decaying (status = 3) SM Higgs (pdgId = 25)
            || ( iGenParticle->status() == 3 and iGenParticle->pdgId() == 35 ) // decaying (status = 3) CP-even Higgs (pdgId = 35)
            ) {
      genH.push_back(&(*iGenParticle)); // Store the Higgs into vector
    }
    // Check if gen particle is
    if (    ( iGenParticle->status() == 3 and iGenParticle->pdgId() == 36      ) // decaying (status = 3) CP-odd Higgs (pdgId = 36)
            || ( iGenParticle->status() == 3 and iGenParticle->pdgId() == 3000022 ) // decaying (status = 3) gamma_Dark (pdgId = 3000022)
            //         || ( iGenParticle->status() == 2 and iGenParticle->pdgId() == 443   ) // decaying (status = 2) J/psi (pdgId = 443)
            ) {
      genGd_unsorted.push_back(&(*iGenParticle));
    }
    // Check if gen particle is gluon 
    if (iGenParticle->status() == 3 and iGenParticle->pdgId() == 21){
      genGlu_unsorted.push_back(&(*iGenParticle));
    }
  }

  if ( genH.size() == 1 ) {
    event_.genH_m   = genH[0]->mass();
    event_.genH_p   = genH[0]->p();
    event_.genH_pt  = genH[0]->pt();
    event_.genH_px  = genH[0]->px();
    event_.genH_py  = genH[0]->py();
    event_.genH_pz  = genH[0]->pz();
    event_.genH_eta = genH[0]->eta();
    event_.genH_phi = genH[0]->phi();
    event_.genH_vx  = genH[0]->vx() - event_.beamSpot_x;
    event_.genH_vy  = genH[0]->vy() - event_.beamSpot_y;
    event_.genH_vz  = genH[0]->vz() - event_.beamSpot_z;
  } else {
    //    cout << "WARNING! genH.size() != 1" << endl;
  }

  if ( genGd.size() >= 2 ) {
    for (int i=0; i<2; ++i){
      event_.genGd_m[i]   = genGd[i]->mass();
      event_.genGd_E[i]   = genGd[i]->energy();
      event_.genGd_p[i]   = genGd[i]->p();
      event_.genGd_pt[i]  = genGd[i]->pt();
      event_.genGd_px[i]  = genGd[i]->px();
      event_.genGd_py[i]  = genGd[i]->py();
      event_.genGd_pz[i]  = genGd[i]->pz();
      event_.genGd_eta[i] = genGd[i]->eta();
      event_.genGd_phi[i] = genGd[i]->phi();
      event_.genGd_vx[i]  = genGd[i]->vx() - event_.beamSpot_x;
      event_.genGd_vy[i]  = genGd[i]->vy() - event_.beamSpot_y;
      event_.genGd_vz[i]  = genGd[i]->vz() - event_.beamSpot_z;
    }
  } else {
    cout << "WARNING! genGd.size() < 2" << endl;
  }

  if ( genGlu.size() >= 2 ) {    
    for (int i=0; i<2; ++i){
      event_.genGlu_p[i] = genGlu[i]->p();
      event_.genGlu_pt[i]  = genGlu[i]->pt();
      event_.genGlu_px[i]  = genGlu[i]->px();
      event_.genGlu_py[i]  = genGlu[i]->py();
      event_.genGlu_pz[i]  = genGlu[i]->pz();
      event_.genGlu_eta[i] = genGlu[i]->eta();
      event_.genGlu_phi[i] = genGlu[i]->phi();
    }
  } else {
    cout << "WARNING! genGlu.size() < 2" << endl;
  }
 
  // Group muons with the same mother
  std::vector< std::vector<const reco::GenParticle*> > genMuonGroupsUnsorted;
  std::vector<const reco::Candidate*> genMuonGroupsUnsortedMothers;
  std::vector<const reco::GenParticle*> genMuonsTMP1       = genMuons;
  std::vector<const reco::Candidate*>   genMuonMothersTMP1 = genMuonMothers;
  unsigned int nMuonGroup = 0;
  while ( genMuonsTMP1.size() > 0 ) {
    std::vector<const reco::GenParticle*> genMuonsTMP2;
    std::vector<const reco::Candidate*>   genMuonMothersTMP2;
    std::vector<const reco::GenParticle*> genMuonsSameMother;
    std::vector<const reco::Candidate*>   genMuonMothersSame;
    for ( unsigned int j = 0; j < genMuonsTMP1.size(); j++ ) {
      // Check if mothers are the same particle
      if ( fabs( genMuonMothersTMP1[0]->pt() - genMuonMothersTMP1[j]->pt() ) < eq ) {
        genMuonsSameMother.push_back( genMuonsTMP1[j] );
      } else {
        genMuonsTMP2.push_back( genMuonsTMP1[j] );
        genMuonMothersTMP2.push_back( genMuonMothersTMP1[j] );
      }
    }
    genMuonGroupsUnsorted.push_back(genMuonsSameMother);
    genMuonGroupsUnsortedMothers.push_back(genMuonMothersTMP1[0]);
    genMuonsTMP1       = genMuonsTMP2;
    genMuonMothersTMP1 = genMuonMothersTMP2;
    nMuonGroup++;
  }


  // Sort muon groups to match order of genGd vector
  std::vector< std::vector<const reco::GenParticle*> > genMuonGroups;
  std::vector<const reco::Candidate*> genMuonGroupsMothers;
  for (unsigned int iA = 0; iA < genGd.size(); iA++ ) {
    bool isMuGroupMatchedToA = false;
    int  nMuGroup = -1;
    for ( unsigned int iMuGroup = 0; iMuGroup < genMuonGroupsUnsortedMothers.size(); iMuGroup++ ) {
      if ( fabs ( genGd[iA]->pt() - genMuonGroupsUnsortedMothers[iMuGroup]->pt() ) < 0.000001 ) {
        isMuGroupMatchedToA = true;
        nMuGroup = iMuGroup;
        break;
      }
    }
    if ( isMuGroupMatchedToA and nMuGroup >= 0 ) {
      genMuonGroups.push_back( genMuonGroupsUnsorted[nMuGroup] );
      genMuonGroupsMothers.push_back( genMuonGroupsUnsortedMothers[nMuGroup] );
    } else {
      cout << "Error! Muon group has no matched boson A" << endl;
    }
  }

  if ( genMuonGroups.size() == 2 and genMuonGroups[0].size() == 2 and genMuonGroups[1].size() == 2 ) {
    std::sort( genMuonGroups[0].begin(), genMuonGroups[0].end(), PtOrder );
    std::sort( genMuonGroups[1].begin(), genMuonGroups[1].end(), PtOrder );
    
    for (int i=0; i<2; ++i){ 
      for (int j=0; j<2; ++j){
        event_.genGdMu_q[i][j] = genMuonGroups[i][j]->charge();
        event_.genGdMu_p[i][j] = genMuonGroups[i][j]->p();
        event_.genGdMu_pt[i][j] = genMuonGroups[i][j]->pt();
        event_.genGdMu_px[i][j] = genMuonGroups[i][j]->px();
        event_.genGdMu_py[i][j] = genMuonGroups[i][j]->py();
        event_.genGdMu_pz[i][j] = genMuonGroups[i][j]->pz();
        event_.genGdMu_eta[i][j] = genMuonGroups[i][j]->eta();
        event_.genGdMu_phi[i][j] = genMuonGroups[i][j]->phi();
        event_.genGdMu_phi_corr[i][j] = phiHeavyCorr(genMuonGroups[i][j]->pt(), genMuonGroups[i][j]->eta(), genMuonGroups[i][j]->phi(), genMuonGroups[i][j]->charge());
        event_.genGdMu_vx[i][j] = genMuonGroups[i][j]->vx();
        event_.genGdMu_vy[i][j] = genMuonGroups[i][j]->vy();
        event_.genGdMu_vz[i][j] = genMuonGroups[i][j]->vz();
      }
    }
    
    if (fabs(event_.genGdMu_vx[0][0] - event_.genGdMu_vx[0][1]) < eq and
        fabs(event_.genGdMu_vx[1][0] - event_.genGdMu_vx[1][1]) < eq and
        fabs(event_.genGdMu_vy[0][0] - event_.genGdMu_vy[0][1]) < eq and
        fabs(event_.genGdMu_vy[1][0] - event_.genGdMu_vy[1][1]) < eq and
        fabs(event_.genGdMu_vz[0][0] - event_.genGdMu_vz[0][1]) < eq and
        fabs(event_.genGdMu_vz[1][0] - event_.genGdMu_vz[1][1]) < eq) {
      
      // Float_t genGd0_vLx = event_.genGd0Mu0_vx - event_.genGd0_vx;
      // Float_t genGd1_vLx = event_.genGd1Mu0_vx - event_.genGd1_vx;
      
      // Float_t genGd0_vLy = event_.genGd0Mu0_vy - event_.genGd0_vy;
      // Float_t genGd1_vLy = event_.genGd1Mu0_vy - event_.genGd1_vy;
    
      // Float_t genGd0_vLz = event_.genGd0Mu0_vz - event_.genGd0_vz;
      // Float_t genGd1_vLz = event_.genGd1Mu0_vz - event_.genGd1_vz;
    
      // event_.genGd0Mu0_dxy = dxy(event_.genGd0Mu0_px, event_.genGd0Mu0_py, event_.genGd0Mu0_vx - event_.beamSpot_x, event_.genGd0Mu0_vy - event_.beamSpot_y, event_.genGd0Mu0_pt);
      // event_.genGd0Mu1_dxy = dxy(event_.genGd0Mu1_px, event_.genGd0Mu1_py, event_.genGd0Mu1_vx - event_.beamSpot_x, event_.genGd0Mu1_vy - event_.beamSpot_y, event_.genGd0Mu1_pt);
      // event_.genGd1Mu0_dxy = dxy(event_.genGd1Mu0_px, event_.genGd1Mu0_py, event_.genGd1Mu0_vx - event_.beamSpot_x, event_.genGd1Mu0_vy - event_.beamSpot_y, event_.genGd1Mu0_pt);
      // event_.genGd1Mu1_dxy = dxy(event_.genGd1Mu1_px, event_.genGd1Mu1_py, event_.genGd1Mu1_vx - event_.beamSpot_x, event_.genGd1Mu1_vy - event_.beamSpot_y, event_.genGd1Mu1_pt);

      // event_.genGd0Mu_dxy_max = std::max(event_.genGd0Mu0_dxy,event_.genGd0Mu1_dxy);
      // event_.genGd1Mu_dxy_max = std::max(event_.genGd1Mu0_dxy,event_.genGd1Mu1_dxy);

      // event_.genGd0_lxy = sqrt( genGd0_vLx * genGd0_vLx + genGd0_vLy * genGd0_vLy );
      // event_.genGd1_lxy = sqrt( genGd1_vLx * genGd1_vLx + genGd1_vLy * genGd1_vLy );
    
      // event_.genGd0_l = sqrt( genGd0_vLx * genGd0_vLx + genGd0_vLy * genGd0_vLy + genGd0_vLz * genGd0_vLz );
      // event_.genGd1_l = sqrt( genGd1_vLx * genGd1_vLx + genGd1_vLy * genGd1_vLy + genGd1_vLz * genGd1_vLz );

      for (int i=0; i<2; ++i){         
        for (int j=0; j<2; ++j){
          event_.genGdMu_dxy[i][j] = dxy(event_.genGdMu_px[i][j], 
                                         event_.genGdMu_py[i][j], 
                                         event_.genGdMu_vx[i][j] - event_.beamSpot_x, 
                                         event_.genGdMu_vy[i][j] - event_.beamSpot_y, 
                                         event_.genGdMu_pt[i][j]);
        }
        event_.genGd_vLx[i] = event_.genGdMu_vx[i][0] - event_.genGd_vx[i];
        event_.genGd_vLy[i] = event_.genGdMu_vy[i][0] - event_.genGd_vy[i];
        event_.genGd_vLz[i] = event_.genGdMu_vz[i][0] - event_.genGd_vz[i];
        event_.genGd_lxy[i] = sqrt(event_.genGd_vLx[i] * event_.genGd_vLx[i] + 
                                   event_.genGd_vLy[i] * event_.genGd_vLy[i]);
        event_.genGd_l[i]   = sqrt(event_.genGd_vLx[i] * event_.genGd_vLx[i] + 
                                   event_.genGd_vLy[i] * event_.genGd_vLy[i] + 
                                   event_.genGd_vLz[i] * event_.genGd_vLz[i]);
        event_.genGdMu_dxy_max[i] = std::max(event_.genGdMu_dxy[i][0], event_.genGdMu_dxy[i][1]);
      }     
    } else {
      cout << "WARNING! Muon vertices are different" << endl;
    }
  }
  
  
  /////////////////
  // L1 analysis //
  /////////////////

  if (nL1Mu>=1)
    eventsWithMuons++;
  
  bool verbose = false;
  if(verbose) std::cout << "Number of L1Mu candidates before selections " << nL1Mu << std::endl; 

  nTotalMuons = nTotalMuons + nL1Mu;

  int nMatchedMuons = 0;
  int nUnMatchedMuons = 0;
  int nUnMatchedMuonsPt = 0;
  for (unsigned int i=0; i<l1GmtCands.size(); ++i) {
    auto l1Mu = l1GmtCands[i];
    const double l1Mu_pt = l1Mu.ptValue();
    const double l1Mu_eta = l1Mu.etaValue();
    const double l1Mu_phi =  normalizedPhi(l1Mu.phiValue());
    const double l1Mu_quality = l1Mu.quality();
    
    event_.L1Mu_pt[i] = l1Mu_pt;
    event_.L1Mu_eta[i] = l1Mu_eta;
    event_.L1Mu_phi[i] = l1Mu_phi;
    event_.L1Mu_charge[i] = l1Mu.charge();
    event_.L1Mu_quality[i] = l1Mu_quality;
    event_.L1Mu_bx[i] = l1Mu.bx();

    if(verbose) {
      cout << "l1Mu " << i << endl; 
      cout << "l1Mu_pt " << l1Mu_pt << endl;
      cout << "l1Mu_eta " << l1Mu_eta << endl;
      cout << "l1Mu_phi " << l1Mu_phi << endl;
      cout << "l1Mu_quality " << l1Mu_quality << endl;
    }
    // calculate the number of L1Tk within 0.12
    for (unsigned int j=0; j<TTTracks.size(); ++j) {
      auto l1Tk = TTTracks[j];
      const double l1Tk_pt = l1Tk.getMomentum().perp();
      const double l1Tk_eta = l1Tk.getMomentum().eta();
      const double l1Tk_phi = l1Tk.getMomentum().phi();
      const double l1Tk_charge = l1Tk.getRInv()>0? 1: -1;
      const double l1Tk_phi_corr = phiHeavyCorr(l1Tk_pt, l1Tk_eta, l1Tk_phi, l1Tk_charge);
      const double dR_l1Mu_l1Tk = reco::deltaR(l1Tk_eta, l1Tk_phi_corr, l1Mu_eta, l1Mu_phi);
      if (dR_l1Mu_l1Tk > 0.4)
        continue;
      if(verbose) std::cout << "\tL1Tk candidate " << j << " dR " << dR_l1Mu_l1Tk << " L1Tk pt " << l1Tk_pt << std::endl;
      if (true) {
        if (dR_l1Mu_l1Tk <=0.12 and l1Mu_quality >= 4) { 
          nMatchedMuons++;
          event_.L1Mu_isMatched[i] = 1;
          if(verbose) std::cout << "\t\tMatched!!!" << std::endl;
          break;
        }
        else if (dR_l1Mu_l1Tk <=0.4) { //0.12 < dR_l1Mu_l1Tk and 
          event_.L1Mu_isUnMatched[i] = 1;
          nUnMatchedMuons++;
          if(verbose) std::cout << "\t\tUnMatched!!!" << std::endl;
          if (l1Tk_pt>=2) {
            event_.L1Mu_isUnMatchedL1TkPt2[i] = 1; 
          }
          if (l1Tk_pt>=3) {
            event_.L1Mu_isUnMatchedL1TkPt3[i] = 1; 
          }
          if (l1Tk_pt>=4) {
            nUnMatchedMuonsPt++;
            event_.L1Mu_isUnMatchedL1TkPt4[i] = 1; 
          }
          break;
        }
      }
    }
    
    // match the L1Mu to GEN    
    double newDR[2][2];
    for (int i=0; i<2; ++i){ 
      for (int j=0; j<2; ++j){
        newDR[i][j] = deltaR(event_.genGdMu_eta[i][j], event_.genGdMu_phi_corr[i][j], l1Mu_eta,l1Mu_phi);        
        cout << "newDR" << i <<  j << newDR[i][j] << " pt " << event_.genGdMu_pt[i][j]
             << " eta " << event_.genGdMu_eta[i][j] << " phi " << event_.genGdMu_phi_corr[i][j] << " Q " << event_.genGdMu_q[i][j] << endl;
      }
    }
    

    const std::vector<double> v{newDR[0][0], newDR[0][1], newDR[1][0], newDR[1][1]};
    auto result(std::min_element(std::begin(v), std::end(v)));
    auto dis(std::distance(std::begin(v), result));
    
    switch (dis){
    case 0: 
      if (newDR[0][0] < event_.genGdMu_L1Mu_dR_corr[0][0]) { 
        event_.genGdMu_L1Mu_index_corr[0][0] = i;
        event_.genGdMu_L1Mu_dR_corr[0][0] = newDR[0][0];
        //        if (m_debug>20) 
        cout << "Muon[0][0] was matched within " << event_.genGdMu_L1Mu_dR_corr[0][0] <<" to L1Mu "<<i<<std::endl;
      }
      break;
    case 1:
      if (newDR[0][1] < event_.genGdMu_L1Mu_dR_corr[0][1]) { 
        event_.genGdMu_L1Mu_index_corr[0][1] = i;
        event_.genGdMu_L1Mu_dR_corr[0][1] = newDR[0][1];
        //        if (m_debug>20) 
        cout << "Muon[0][1] was matched within " << event_.genGdMu_L1Mu_dR_corr[0][1] <<" to L1Mu "<<i<< std::endl;
      }
      break;
    case 2:
      if (newDR[1][0] < event_.genGdMu_L1Mu_dR_corr[1][0]) { 
        event_.genGdMu_L1Mu_index_corr[1][0] = i;
        event_.genGdMu_L1Mu_dR_corr[1][0] = newDR[1][0];
        //        if (m_debug>20) 
        cout << "Muon[1][0] was matched within " << event_.genGdMu_L1Mu_dR_corr[1][0] <<" to L1Mu "<<i<< std::endl;
      }
      break;
    case 3:
      if (newDR[1][1] < event_.genGdMu_L1Mu_dR_corr[1][1]) { 
        event_.genGdMu_L1Mu_index_corr[1][1] = i;
        event_.genGdMu_L1Mu_dR_corr[1][1] = newDR[1][1];
        //        if (m_debug>20) 
        cout << "Muon[1][1] was matched within " << event_.genGdMu_L1Mu_dR_corr[1][1] <<" to L1Mu "<<i<< std::endl;
      }
      break;
    };
  }  
  
  if(verbose)std::cout << "Total number of muons in this event: " << nL1Mu << std::endl;
  if(verbose)std::cout << "Number of matched muons: " << nMatchedMuons << std::endl;
  if(verbose)std::cout << "Number of unmatched muons: " << nUnMatchedMuons << std::endl;
  if(verbose)std::cout << "Number of unmatched muons pt: " << nUnMatchedMuonsPt << std::endl;
  int displacedMuons = nL1Mu - nMatchedMuons - nUnMatchedMuons;
  int displacedMuonsPt = nL1Mu - nMatchedMuons - nUnMatchedMuonsPt;
  if(verbose)std::cout << "Number of displaced muons: " << displacedMuons << std::endl;
  if(verbose)std::cout << "Number of displaced muons pt: " << displacedMuonsPt << std::endl;

  if (displacedMuons >=1) 
    eventsWithDisplacedMuons++;

  if (displacedMuonsPt >=1) 
    eventsWithDisplacedMuonsPt++;

  // no L1Mu in event, still fill with default values
  event_tree_->Fill();  

  // if (nL1Mu==0) {
  //   event_.nL1Mu = 0;
  //   event_.lumi = iEvent.id().luminosityBlock();
  //   event_.run = iEvent.id().run();
  //   event_.event = iEvent.id().event();
  //   event_tree_->Fill();    
  // }

  return true;
  /*
    // get the SIM muon in this event
    // for a muon gun there is only 1 muon
    // this needs to be adjusted in order to work
    // for a 4-muon event
    int nSimMu = 0;
    int indexFound = 0;
    for (unsigned int i=0; i<sim_trks.size(); ++i) {
      if (!isSimTrackGood(sim_trks[i])) continue;
      nSimMu++;
      indexFound = i;
    }
   
    auto sim_muon = sim_trks[indexFound];
    auto sim_vertex = sim_vtxs[sim_muon.vertIndex()];
    event_.pt_sim = sim_muon.momentum().pt();
    event_.eta_sim = sim_muon.momentum().eta();
    event_.phi_sim = sim_muon.momentum().phi();
    event_.charge_sim = sim_muon.charge();
    
    // first loop on tracker tracks to get the best matching TTTrack
    double dR_SIM_L1Tk_min = 9999;
    int i_SIM_L1Tk_min = -1;
    for (unsigned int j=0; j<TTTracks.size(); ++j){
      auto l1Tk = TTTracks[j];
      const double l1Tk_eta = l1Tk.getMomentum().eta();
      const double l1Tk_phi = l1Tk.getMomentum().phi();
      const double dR_SIM_L1Tk(reco::deltaR(event_.eta_sim, event_.phi_sim, l1Tk_eta, l1Tk_phi));
      if (dR_SIM_L1Tk < dR_SIM_L1Tk_min) {
        dR_SIM_L1Tk_min = dR_SIM_L1Tk;
        i_SIM_L1Tk_min = j;
      }
    }

    // L1Tk properties
    auto l1Tk = TTTracks[i_SIM_L1Tk_min];
    event_.pt_L1Tk = l1Tk.getMomentum().perp();
    event_.eta_L1Tk = l1Tk.getMomentum().eta();
    event_.phi_L1Tk = l1Tk.getMomentum().phi();
    event_.charge_L1Tk = l1Tk.getRInv()>0? 1: -1;
  
    // only keep the L1Mu which is associated to a SIM muon
    // propagate the SIM muon to the outer stations
    double sim_muon_eta_prop;
    double sim_muon_phi_prop;
    
    GlobalPoint inner_point(sim_vertex.position().x(), sim_vertex.position().y(), sim_vertex.position().z());
    GlobalVector inner_vec (sim_muon.momentum().x(), sim_muon.momentum().y(), sim_muon.momentum().z());
    if (std::abs(sim_muon.momentum().eta())<1.1) {
      GlobalPoint loc_barrel(propagateToR(inner_point, inner_vec, sim_muon.charge(), 500.));
       sim_muon_eta_prop = loc_barrel.eta();
       sim_muon_phi_prop = loc_barrel.phi();
     } 
     else if (1.1 < sim_muon.momentum().eta() and sim_muon.momentum().eta() < 2.5) {
       GlobalPoint loc_endcap_pos(propagateToZ(inner_point, inner_vec, sim_muon.charge(), 850.));
       sim_muon_eta_prop = loc_endcap_pos.eta();
       sim_muon_phi_prop = loc_endcap_pos.phi();
     }
     else if (-1.1 > sim_muon.momentum().eta() and sim_muon.momentum().eta() > -2.5) {
       GlobalPoint loc_endcap_neg(propagateToZ(inner_point, inner_vec, sim_muon.charge(), -850.));
       sim_muon_eta_prop = loc_endcap_neg.eta();
       sim_muon_phi_prop = loc_endcap_neg.phi();
     }
     else {
       sim_muon_eta_prop = 99.;
       sim_muon_phi_prop = 99.;
     }
    
    // propagate the muon with steppinghelixpropagators
    event_.eta_sim_prop = sim_muon_eta_prop;
    event_.phi_sim_prop = sim_muon_phi_prop -  M_PI/144.; // do a phi correction after the propagation of PI/144 as suggested by Slava

    event_.dEta_sim_prop = std::abs(event_.eta_sim_prop - l1Mu_eta);
    event_.dPhi_sim_prop = reco::deltaPhi(event_.phi_sim_prop, l1Mu_phi);
    event_.dR_sim_prop = reco::deltaR(event_.eta_sim_prop, event_.phi_sim_prop, l1Mu_eta, l1Mu_phi);

    // propagate the muon using the phi correction formula that slava provided
    event_.eta_sim_corr = event_.eta_sim;
    event_.phi_sim_corr = phiHeavyCorr(event_.pt_sim,
                                       event_.eta_sim,
                                       event_.phi_sim,
                                       event_.charge_sim);
    
    event_.dEta_sim_corr = std::abs(event_.eta_sim_corr - l1Mu_eta);
    event_.dPhi_sim_corr = reco::deltaPhi(event_.phi_sim_corr, l1Mu_phi);
    event_.dR_sim_corr = reco::deltaR(event_.eta_sim_corr, event_.phi_sim_corr, l1Mu_eta, l1Mu_phi);
    
    // propagate the L1Tk object to the muon station with steppinghelixpropagator
    double eta_L1Tk_prop;
    double phi_L1Tk_prop;    
    if (std::abs(event_.eta_L1Tk)<1.1) {
      GlobalPoint loc_barrel(propagateToR(l1Tk.getPOCA(), l1Tk.getMomentum(), event_.charge_L1Tk, 500.));
      eta_L1Tk_prop = loc_barrel.eta();
      phi_L1Tk_prop = loc_barrel.phi();
    } 
    else if (1.1 < event_.eta_L1Tk and event_.eta_L1Tk < 2.5) {
      GlobalPoint loc_endcap_pos(propagateToZ(l1Tk.getPOCA(), l1Tk.getMomentum(), event_.charge_L1Tk, 850.));
      eta_L1Tk_prop = loc_endcap_pos.eta();
      phi_L1Tk_prop = loc_endcap_pos.phi();
    }
    else if (-1.1 > event_.eta_L1Tk and event_.eta_L1Tk > -2.5) {
      GlobalPoint loc_endcap_neg(propagateToZ(l1Tk.getPOCA(), l1Tk.getMomentum(), event_.charge_L1Tk, -850.));
      eta_L1Tk_prop = loc_endcap_neg.eta();
      phi_L1Tk_prop = loc_endcap_neg.phi();
    }
    else{
      eta_L1Tk_prop = 99.;
      phi_L1Tk_prop = 99.;
    }

    // propagate the muon with steppinghelixpropagator
    event_.eta_L1Tk_prop = eta_L1Tk_prop; 
    event_.phi_L1Tk_prop = phi_L1Tk_prop - M_PI/144.;

    event_.dEta_L1Tk_prop = std::abs(event_.eta_L1Tk_prop - l1Mu_eta);
    event_.dPhi_L1Tk_prop = reco::deltaPhi(event_.phi_L1Tk_prop, l1Mu_phi);
    event_.dR_L1Tk_prop = reco::deltaR(event_.eta_L1Tk_prop, event_.phi_L1Tk_prop, l1Mu_eta, l1Mu_phi);

    // propagate the muon with the phi correction formula that slava provided
    event_.eta_L1Tk_corr = event_.eta_L1Tk;
    event_.phi_L1Tk_corr = phiHeavyCorr(event_.pt_L1Tk,
                                        event_.eta_L1Tk,
                                        event_.phi_L1Tk,
                                        event_.charge_L1Tk);

    event_.dEta_L1Tk_corr = std::abs(event_.eta_L1Tk_corr - l1Mu_eta);
    event_.dPhi_L1Tk_corr = reco::deltaPhi(event_.phi_L1Tk_corr, l1Mu_phi);
    event_.dR_L1Tk_corr = reco::deltaR(event_.eta_L1Tk_corr, event_.phi_L1Tk_corr, l1Mu_eta, l1Mu_phi);

    if(verbose) {  
      cout << "l1Mu " << i << endl; 
      cout << "l1Mu_pt " << l1Mu_pt << endl;
      cout << "l1Mu_eta " << l1Mu_eta << endl;
      cout << "l1Mu_phi " << l1Mu_phi << endl;
      cout << "l1Mu_quality " << l1Mu_quality << endl;
      
      cout << "SIM " << indexFound << endl;
      cout << "SIM_pt " << event_.pt_sim << endl;
      cout << "SIM_eta " << event_.eta_sim << endl;
      cout << "SIM_phi " << event_.phi_sim << endl;
      cout << "SIM_eta_corr " << event_.eta_sim_corr << endl;
      cout << "SIM_phi_corr " << event_.phi_sim_corr << endl;
      cout << "SIM_eta_prop " << event_.eta_sim_prop << endl;
      cout << "SIM_phi_prop " << event_.phi_sim_prop << endl;
      cout << "SIM_charge " << event_.charge_sim << endl;
    
      cout << "l1Tk " << i_SIM_L1Tk_min << endl;
      cout << "l1Tk_pt " << event_.pt_L1Tk << endl;
      cout << "l1Tk_eta " << event_.eta_L1Tk << endl;
      cout << "l1Tk_phi " << event_.phi_L1Tk << endl;
      cout << "l1Tk_charge " << event_.charge_L1Tk << endl;
      cout << "dR_SIM_L1Tk_min " << dR_SIM_L1Tk_min << endl;

      cout << "event_.dEta_sim_prop " << event_.dEta_sim_prop << endl
           << "event_.dPhi_sim_prop " << event_.dPhi_sim_prop << endl
           << "event_.dR_sim_prop " << event_.dR_sim_prop << endl;

      cout << "event_.dEta_sim_corr " << event_.dEta_sim_corr << endl
           << "event_.dPhi_sim_corr " << event_.dPhi_sim_corr << endl
           << "event_.dR_sim_corr " << event_.dR_sim_corr << endl;

      cout << "event_.dEta_L1Tk_prop " << event_.dEta_L1Tk_prop << endl
           << "event_.dPhi_L1Tk_prop " << event_.dPhi_L1Tk_prop << endl
           << "event_.dR_L1Tk_prop " << event_.dR_L1Tk_prop << endl;

      cout << "event_.dEta_L1Tk_corr " << event_.dEta_L1Tk_corr << endl
           << "event_.dPhi_L1Tk_corr " << event_.dPhi_L1Tk_corr << endl
           << "event_.dR_L1Tk_corr " << event_.dR_L1Tk_corr << endl;
    }
    

    //   // calculate the dR between the two L1Mus
    //   // const double dRL1Mu(reco::deltaR(l1Mu_eta, l1Mu_phi, L1Mu_of_L1TkMu.etaValue(), L1Mu_of_L1TkMu.phiValue()));

    //   // const double l1TkMu_phi_corr = phiHeavyCorr(l1TkMu_pt, l1TkMu_eta, l1TkMu_phi, l1TkMu_charge);
      
    //   //if(verbose) std::cout << "\tl1Tk_phi_corr " << l1Tk_phi_corr << std::endl;
      
    //   // calculate dR
    //   const double dR_prop(reco::deltaR(l1Mu_eta, l1Mu_phi, l1Tk_eta_prop, l1Tk_phi_prop));
    //   const double dR_corr(reco::deltaR(l1Mu_eta, l1Mu_phi, l1Tk_eta, l1Tk_phi_corr));
    //   const double dR_SIM_L1Tk(reco::deltaR(sim_muon.momentum().eta(), sim_muon.momentum().phi(), l1Tk_eta, l1Tk_phi));
    //   //std::cout << "dR_prop " << dR_prop << " dR_corr " << dR_corr << std::endl;
    //   if (dR_SIM_L1Tk < dR_SIM_L1Tk_min) {
    //     dR_SIM_L1Tk_min = dR_SIM_L1Tk;
    //     i_SIM_L1Tk_min = j;
    //   }
    
    //   event_.pt_L1Tk = l1Tk_pt;
    //   event_.eta_L1Tk = l1Tk_eta_prop;
    //   event_.phi_L1Tk = l1Tk_phi_prop;

    //   event_.dEta_L1Tk_prop = std::abs(l1Tk_eta_prop - l1Mu_eta);
    //   event_.dPhi_L1Tk_prop = reco::deltaPhi(l1Tk_phi_prop, l1Mu_phi);
    //   event_.dR_L1Tk_prop = dR_prop;
      
    //   event_.dEta_L1Tk_corr = std::abs(l1Tk_eta - l1Mu_eta);
    //   event_.dPhi_L1Tk_corr = reco::deltaPhi(l1Tk_phi_corr, l1Mu_phi);
    //   event_.dR_L1Tk_corr = dR_corr;

    // std::cout << "\tSIM " << i << std::endl;
    // std::cout << "\tSIM_pt " << sim_muon.momentum().pt() << std::endl;
    // std::cout << "\tSIM_eta " << sim_muon.momentum().eta() << std::endl;
    // std::cout << "\tSIM_phi " << sim_muon.momentum().phi() << std::endl;
    // std::cout << "\tSIM_charge " << sim_muon.charge() << std::endl;
    // // std::cout << "Number of sim muons in this bx " << nSimMu << std::endl;
    // // std::cout << "Pt " << event_.pt_sim << endl
    // //           << "Eta " << event_.eta_sim<< endl
    // //           << "Phi " << event_.phi_sim<< endl
    
    // double sim_muon_eta_prop;
    // double sim_muon_phi_prop;

    // GlobalPoint inner_point(sim_vertex.position().x(), sim_vertex.position().y(), sim_vertex.position().z());
    // GlobalVector inner_vec (sim_muon.momentum().x(), sim_muon.momentum().y(), sim_muon.momentum().z());
     
    // double sim_phi_corrected = phiHeavyCorr(sim_muon.momentum().pt(), 
    //                                         sim_muon.momentum().eta(), 
    //                                         sim_muon.momentum().phi(), 
    //                                         sim_muon.charge());
    
    // event_.dEta_sim_corr = std::abs(sim_muon.momentum().eta() - l1Mu_eta);
    // event_.dPhi_sim_corr = reco::deltaPhi(sim_phi_corrected, l1Mu_phi);
    // event_.dR_sim_corr = reco::deltaR(sim_muon.momentum().eta(), sim_phi_corrected, l1Mu_eta, l1Mu_phi);
    // std::cout << "event_.dEta_sim_corr " << event_.dEta_sim_corr << " event_.dPhi_sim_corr " << event_.dPhi_sim_corr << " event_.dR_sim_corr " << event_.dR_sim_corr << std::endl;
    
    // event_.dEta_sim_prop = std::abs(sim_muon_eta_prop - l1Mu_eta);
    // event_.dPhi_sim_prop = reco::deltaPhi(sim_muon_phi_prop, l1Mu_phi);
    // event_.dR_sim_prop = reco::deltaR(sim_muon_eta_prop, sim_muon_phi_prop, l1Mu_eta, l1Mu_phi);
    // std::cout << "event_.dEta_sim_prop " << event_.dEta_sim_prop << " event_.dPhi_sim_prop " << event_.dPhi_sim_prop << " event_.dR_sim_prop " << event_.dR_sim_prop << std::endl;

    // bool isMatched = false;
    // bool isUnMatched = false;

    // if(verbose) std::cout << "Number of L1Tk candidates " << nL1Tk << std::endl;
    // double dR_SIM_L1Tk_min = 9999;
    // double i_SIM_L1Tk_min = -1;

    // for (unsigned int j=0; j<TTTracks.size(); ++j){
    //   auto l1Tk = TTTracks[j];
    //   const double l1Tk_pt = l1Tk.getMomentum().perp();
    //   const double l1Tk_eta = l1Tk.getMomentum().eta();
    //   const double l1Tk_phi = l1Tk.getMomentum().phi();
    //   double l1Tk_charge = l1Tk.getRInv()>0? 1: -1;
    //   const double l1Tk_phi_corr = phiHeavyCorr(l1Tk_pt, 
    //                                             l1Tk_eta, 
    //                                             l1Tk_phi, 
    //                                             l1Tk_charge);
    //   if (std::abs(l1Tk_eta - sim_muon.momentum().eta()) < event_.dEta_sim_L1Tk)
    //     event_.dEta_sim_L1Tk = std::abs(l1Tk_eta - sim_muon.momentum().eta());

    //   if ( reco::deltaPhi(sim_muon.momentum().phi(), l1Tk_phi) < event_.dPhi_sim_L1Tk)
    //     event_.dPhi_sim_L1Tk = reco::deltaPhi(sim_muon.momentum().phi(), l1Tk_phi);

    //   if (reco::deltaR(l1Tk_eta, l1Tk_phi, sim_muon.momentum().eta(), sim_muon.momentum().phi()) < event_.dR_sim_L1Tk)
    //     event_.dR_sim_L1Tk = reco::deltaR(l1Tk_eta, l1Tk_phi, sim_muon.momentum().eta(), sim_muon.momentum().phi());      

    //   //
      
    //   // propagate the L1Tk to the second station
      
    //   double l1Tk_eta_prop;
    //   double l1Tk_phi_prop;
      
    //   if (std::abs(l1Tk_eta)<1.1){
    //     GlobalPoint loc_barrel(propagateToR(l1Tk.getPOCA(), l1Tk.getMomentum(), l1Tk_charge, 500.));
    //     l1Tk_eta_prop = loc_barrel.eta();
    //     l1Tk_phi_prop = loc_barrel.phi();
    //   } 
    //   else if (1.1 < l1Tk_eta and l1Tk_eta < 2.5) {
    //     GlobalPoint loc_endcap_pos(propagateToZ(l1Tk.getPOCA(), l1Tk.getMomentum(), l1Tk_charge, 850.));
    //     l1Tk_eta_prop = loc_endcap_pos.eta();
    //     l1Tk_phi_prop = loc_endcap_pos.phi();
    //   }
    //   else if (-1.1 > l1Tk_eta and l1Tk_eta > -2.5) {
    //     GlobalPoint loc_endcap_neg(propagateToZ(l1Tk.getPOCA(), l1Tk.getMomentum(), l1Tk_charge, -850.));
    //     l1Tk_eta_prop = loc_endcap_neg.eta();
    //     l1Tk_phi_prop = loc_endcap_neg.phi();
    //   }
    //   else{
    //     l1Tk_eta_prop = 99.;
    //     l1Tk_phi_prop = 99.;
    //   }

    //   // std::cout << "pt L1Tk " << l1Tk_pt << std::endl;
    //   // std::cout << "eta L1Tk " << l1Tk_eta << " eta L1Tk prop " << l1Tk_eta_prop << std::endl;
    //   // std::cout << "phi L1Tk " << l1Tk_phi << " phi L1Tk prop " << l1Tk_phi_prop << " phi L1Tk corr " << l1Tk_phi_corr << std::endl;

    //   // std::cout << "dEta L1Tk prop " << std::abs(l1Tk_eta - l1Tk_eta_prop) << std::endl;
    //   // std::cout << "dPhi L1Tk prop " << reco::deltaPhi(l1Tk_phi_prop, l1Tk_phi) << std::endl;
    //   // std::cout << "dPhi L1Tk corr " << reco::deltaPhi(l1Tk_phi_corr, l1Tk_phi) << std::endl;
  
    //   // calculate the dR between the two L1Mus
    //   // const double dRL1Mu(reco::deltaR(l1Mu_eta, l1Mu_phi, L1Mu_of_L1TkMu.etaValue(), L1Mu_of_L1TkMu.phiValue()));

    //   // const double l1TkMu_phi_corr = phiHeavyCorr(l1TkMu_pt, l1TkMu_eta, l1TkMu_phi, l1TkMu_charge);
      
    //   //if(verbose) std::cout << "\tl1Tk_phi_corr " << l1Tk_phi_corr << std::endl;
      
    //   // calculate dR
    //   const double dR_prop(reco::deltaR(l1Mu_eta, l1Mu_phi, l1Tk_eta_prop, l1Tk_phi_prop));
    //   const double dR_corr(reco::deltaR(l1Mu_eta, l1Mu_phi, l1Tk_eta, l1Tk_phi_corr));
    //   const double dR_SIM_L1Tk(reco::deltaR(sim_muon.momentum().eta(), sim_muon.momentum().phi(), l1Tk_eta, l1Tk_phi));
    //   //std::cout << "dR_prop " << dR_prop << " dR_corr " << dR_corr << std::endl;
    //   if (dR_SIM_L1Tk < dR_SIM_L1Tk_min) {
    //     dR_SIM_L1Tk_min = dR_SIM_L1Tk;
    //     i_SIM_L1Tk_min = j;
    //   }
    
    //   event_.pt_L1Tk = l1Tk_pt;
    //   event_.eta_L1Tk = l1Tk_eta_prop;
    //   event_.phi_L1Tk = l1Tk_phi_prop;

    //   event_.dEta_L1Tk_prop = std::abs(l1Tk_eta_prop - l1Mu_eta);
    //   event_.dPhi_L1Tk_prop = reco::deltaPhi(l1Tk_phi_prop, l1Mu_phi);
    //   event_.dR_L1Tk_prop = dR_prop;
      
    //   event_.dEta_L1Tk_corr = std::abs(l1Tk_eta - l1Mu_eta);
    //   event_.dPhi_L1Tk_corr = reco::deltaPhi(l1Tk_phi_corr, l1Mu_phi);
    //   event_.dR_L1Tk_corr = dR_corr;

    //   // if(verbose) std::cout << "\tdRL1Mu " << dRL1Mu << std::endl;
      
    //   // if (dR < dR_L1Mu_L1Tk){
    //   //   nL1MuL1TkdR012++;
    //   //   if(verbose) std::cout << "\t-- L1Mu matched to L1Tk" << std::endl;
    //   //   continue;
    //   // }
    //   // if (l1Mu_quality >= min_L1Mu_Quality){
    //   //   nL1MuQuality4++;
    //   //   std::cout << "\t-- L1Mu Q>=4" << std::endl;
    //   // }
      
      
    //   //cout << "dR_SIM_L1Tk " << dR_SIM_L1Tk << endl;
      
    //   // if (dR_prop < dR_L1Mu_L1Tk and l1Mu_quality >= min_L1Mu_Quality) {
    //   //   event_.isMatched = 1;
    //   //   ++nL1MuMatched;
    //   //   // std::cout << "\t-- L1Mu Q>=4 matched to L1Tk" << std::endl;
    //   //   if(verbose) std::cout << "\tl1Tk " << i << std::endl;
    //   //   if(verbose) std::cout << "\tl1Tk_pt " << l1Tk_pt << std::endl;
    //   //   if(verbose) std::cout << "\tl1Tk_eta " << l1Tk_eta << std::endl;
    //   //   if(verbose) std::cout << "\tl1Tk_phi " << l1Tk_phi << std::endl;
    //   //   if(verbose) std::cout << "\tl1Tk_charge " << l1Tk_charge << std::endl;
        
    //   //   if(verbose) std::cout << "\tl1Tk_eta_prop " << l1Tk_eta_prop << std::endl;
    //   //   if(verbose) std::cout << "\tl1Tk_phi_prop " << l1Tk_phi_prop << std::endl;
    //   //   if(verbose) std::cout << "\tdR_prop " << dR_prop << std::endl;
    //   //   isMatched = true;
    //   //   break;
    //   // } 
    //   // if (dR_prop < dR_L1Mu_noL1Tk and l1Tk_pt>4) {        
    //   //   event_.isUnMatched = 1;
    //   //   ++nL1MuUnMatched;
    //   //   // std::cout << "\t-- L1Mu not matched to L1Tk" << std::endl;
    //   //   if(verbose) std::cout << "\tl1Tk " << i << std::endl;
    //   //   if(verbose) std::cout << "\tl1Tk_pt " << l1Tk_pt << std::endl;
    //   //   if(verbose) std::cout << "\tl1Tk_eta " << l1Tk_eta << std::endl;
    //   //   if(verbose) std::cout << "\tl1Tk_phi " << l1Tk_phi << std::endl;
    //   //   if(verbose) std::cout << "\tl1Tk_charge " << l1Tk_charge << std::endl;
        
    //   //   if(verbose) std::cout << "\tl1Tk_eta_prop " << l1Tk_eta_prop << std::endl;
    //   //   if(verbose) std::cout << "\tl1Tk_phi_prop " << l1Tk_phi_prop << std::endl;
    //   //   if(verbose) std::cout << "\tdR_prop " << dR_prop << std::endl;
    //   //   isUnMatched = true;
    //   //   break;
    //   // }
    //   // std::cout << std::endl;
    // }
    
    // std::cout << "\tl1Tk " << i_SIM_L1Tk_min << std::endl;
    // std::cout << "\tl1Tk_pt " << TTTracks[i_SIM_L1Tk_min].getMomentum().perp() << std::endl;
    // std::cout << "\tl1Tk_eta " << TTTracks[i_SIM_L1Tk_min].getMomentum().eta() << std::endl;
    // std::cout << "\tl1Tk_phi " << TTTracks[i_SIM_L1Tk_min].getMomentum().phi() << std::endl;
    // double charge = TTTracks[i_SIM_L1Tk_min].getRInv()>0? 1: -1;
    // std::cout << "\tl1Tk_charge " << charge << std::endl;
    // std::cout << "dR_SIM_L1Tk_min " << dR_SIM_L1Tk_min << std::endl;
    
    // if (isUnMatched or isMatched) {
    //   nPromptMuons++;
    // }

    event_tree_->Fill();  
  }
  std::cout << endl << "--------------------------------" << endl;
  std::cout << "event report" << endl;
  std::cout << "nL1MuL1TkdR012 " << nL1MuL1TkdR012 << endl;
  std::cout << "nL1MuQuality4 " << nL1MuQuality4 << endl;
  std::cout << "nL1MuMatched " << nL1MuMatched << endl;
  std::cout << "nL1MuUnMatched " << nL1MuUnMatched << endl;
  std::cout << "nL1Mu " << nL1Mu << endl;
  std::cout << "nL1Tk " << nL1Tk << endl;
  std::cout << "Filter " << nL1MuMatched + nL1MuUnMatched << endl;
  
  return(nL1MuMatched + nL1MuUnMatched)==0;

  // match l1 mu to simulated mu check that the delta R is less than 0.2 after propagation
  // impose selection on the L1Mu 
  // use the central bunch crossing instead of +- 1
  
  // use pt>20, plot the dEta, dPhi for the (SIM,L1) mapping
  */  
}

// ------------ method called once each job just before starting event loop  ------------
void 
DisplacedL1MuFilter::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
DisplacedL1MuFilter::endJob()
{
  // cout << "Total number of total muons " << nTotalMuons << endl;
  // cout << "Total number of prompt muons " << nPromptMuons << endl;
  cout << "Events with at least 1 muon: " << eventsWithMuons << std::endl;
  cout << "Events with at least 1 displaced muon: " << eventsWithDisplacedMuons << std::endl;
  cout << "Events with at least 1 displaced muon Pt4: " << eventsWithDisplacedMuonsPt << std::endl;
}

// ------------ method called when starting to processes a run  ------------
/*
void
DisplacedL1MuFilter::beginRun(edm::Run const&, edm::EventSetup const&)
{ 
}
*/
 
// ------------ method called when ending the processing of a run  ------------
/*
void
DisplacedL1MuFilter::endRun(edm::Run const&, edm::EventSetup const&)
{
}
*/
 
// ------------ method called when starting to processes a luminosity block  ------------
/*
void
DisplacedL1MuFilter::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/
 
// ------------ method called when ending the processing of a luminosity block  ------------
/*
void
DisplacedL1MuFilter::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/
 
// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
DisplacedL1MuFilter::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}


GlobalPoint
DisplacedL1MuFilter::propagateToZ(const GlobalPoint &inner_point, const GlobalVector &inner_vec, double charge, double z) const
{
  Plane::PositionType pos(0.f, 0.f, z);
  Plane::RotationType rot;
  Plane::PlanePointer my_plane(Plane::build(pos, rot));

  FreeTrajectoryState state_start(inner_point, inner_vec, charge, &*magfield_);

  TrajectoryStateOnSurface tsos(propagator_->propagate(state_start, *my_plane));
  if (!tsos.isValid()) tsos = propagatorOpposite_->propagate(state_start, *my_plane);
  if (tsos.isValid()) return tsos.globalPosition();

  return GlobalPoint();
}

GlobalPoint
DisplacedL1MuFilter::propagateToR(const GlobalPoint &inner_point, const GlobalVector &inner_vec, double charge, double R) const
{
  Cylinder::CylinderPointer my_cyl(Cylinder::build(Surface::PositionType(0,0,0), Surface::RotationType(), R));

  FreeTrajectoryState state_start(inner_point, inner_vec, charge, &*magfield_);

  TrajectoryStateOnSurface tsos(propagator_->propagate(state_start, *my_cyl));
  if (!tsos.isValid()) tsos = propagatorOpposite_->propagate(state_start, *my_cyl);
  if (tsos.isValid()) return tsos.globalPosition();

  return GlobalPoint();
}

void DisplacedL1MuFilter::bookL1MuTree()
{
  edm::Service< TFileService > fs;
  event_tree_ = fs->make<TTree>("L1MuTree", "L1MuTree");
  event_tree_->Branch("lumi", &event_.lumi);
  event_tree_->Branch("run", &event_.run);
  event_tree_->Branch("event", &event_.event);

  // Beam spot
  event_tree_->Branch("beamSpot_x",    &event_.beamSpot_x,    "beamSpot_x/F");
  event_tree_->Branch("beamSpot_y",    &event_.beamSpot_y,    "beamSpot_y/F");
  event_tree_->Branch("beamSpot_z",    &event_.beamSpot_z,    "beamSpot_z/F");

  // Bosons
  event_tree_->Branch("genGlu_p",    event_.genGlu_p,    "genGlu_p[2]/F");
  event_tree_->Branch("genGlu_pt",   event_.genGlu_pt,   "genGlu_pt[2]/F");
  event_tree_->Branch("genGlu_px",   event_.genGlu_px,   "genGlu_px[2]/F");
  event_tree_->Branch("genGlu_py",   event_.genGlu_py,   "genGlu_py[2]/F");
  event_tree_->Branch("genGlu_pz",   event_.genGlu_pz,   "genGlu_pz[2]/F");
  event_tree_->Branch("genGlu_eta",  event_.genGlu_eta,  "genGlu_eta[2]/F");
  event_tree_->Branch("genGlu_phi",  event_.genGlu_phi,  "genGlu_phi[2]/F");

  event_tree_->Branch("genH_m",    &event_.genH_m,    "genH_m/F");
  event_tree_->Branch("genH_p",    &event_.genH_p,    "genH_p/F");
  event_tree_->Branch("genH_pt",   &event_.genH_pt,   "genH_pt/F");
  event_tree_->Branch("genH_eta",  &event_.genH_eta,  "genH_eta/F");
  event_tree_->Branch("genH_phi",  &event_.genH_phi,  "genH_phi/F");
  event_tree_->Branch("genH_vx",   &event_.genH_vx,   "genH_vx/F");
  event_tree_->Branch("genH_vy",   &event_.genH_vy,   "genH_vy/F");
  event_tree_->Branch("genH_vz",   &event_.genH_vz,   "genH_vz/F");
  
  event_tree_->Branch("genGd_m",   event_.genGd_m,   "genGd_m[2]/F");
  event_tree_->Branch("genGd_E",   event_.genGd_E,   "genGd_E[2]/F");
  event_tree_->Branch("genGd_p",   event_.genGd_p,   "genGd_p[2]/F");
  event_tree_->Branch("genGd_pt",  event_.genGd_pt,  "genGd_pt[2]/F");
  event_tree_->Branch("genGd_px",  event_.genGd_px,  "genGd_px[2]/F");
  event_tree_->Branch("genGd_py",  event_.genGd_py,  "genGd_py[2]/F");
  event_tree_->Branch("genGd_pz",  event_.genGd_pz,  "genGd_pz[2]/F");
  event_tree_->Branch("genGd_eta", event_.genGd_eta, "genGd_eta[2]/F");
  event_tree_->Branch("genGd_phi", event_.genGd_phi, "genGd_phi[2]/F");
  event_tree_->Branch("genGd_vx",  event_.genGd_vx,  "genGd_vx[2]/F");
  event_tree_->Branch("genGd_vy",  event_.genGd_vy,  "genGd_vy[2]/F");
  event_tree_->Branch("genGd_vz",  event_.genGd_vz,  "genGd_vz[2]/F");

  // Dimuons
  event_tree_->Branch("genGdMu_p", event_.genGdMu_p, "genGdMu_p[2][2]/F");
  event_tree_->Branch("genGdMu_pt", event_.genGdMu_pt, "genGdMu_pt[2][2]/F");
  event_tree_->Branch("genGdMu_px", event_.genGdMu_px, "genGdMu_px[2][2]/F");
  event_tree_->Branch("genGdMu_py", event_.genGdMu_py, "genGdMu_py[2][2]/F");
  event_tree_->Branch("genGdMu_pz", event_.genGdMu_pz, "genGdMu_pz[2][2]/F");
  event_tree_->Branch("genGdMu_eta", event_.genGdMu_eta, "genGdMu_eta[2][2]/F");
  event_tree_->Branch("genGdMu_phi", event_.genGdMu_phi, "genGdMu_phi[2][2]/F");
  event_tree_->Branch("genGdMu_phi_corr", event_.genGdMu_phi_corr, "genGdMu_phi_corr[2][2]/F");
  event_tree_->Branch("genGdMu_vx", event_.genGdMu_vx, "genGdMu_vx[2][2]/F");
  event_tree_->Branch("genGdMu_vy", event_.genGdMu_vy, "genGdMu_vy[2][2]/F");
  event_tree_->Branch("genGdMu_vz", event_.genGdMu_vz, "genGdMu_vz[2][2]/F");
  event_tree_->Branch("genGdMu_dxy", event_.genGdMu_dxy, "genGdMu_dxy[2][2]/F");


  event_tree_->Branch("nL1Mu", &event_.nL1Mu);

  event_tree_->Branch("L1Mu_pt",event_.L1Mu_pt,"L1Mu_pt[nL1Mu]/F");
  event_tree_->Branch("L1Mu_eta", event_.L1Mu_eta,"L1Mu_eta[nL1Mu]/F");
  event_tree_->Branch("L1Mu_phi", event_.L1Mu_phi,"L1Mu_phi[nL1Mu]/F");
  event_tree_->Branch("L1Mu_bx", event_.L1Mu_bx,"L1Mu_bx[nL1Mu]/I");
  event_tree_->Branch("L1Mu_charge", event_.L1Mu_charge,"L1Mu_charge[nL1Mu]/I");
  event_tree_->Branch("L1Mu_quality", event_.L1Mu_quality,"L1Mu_quality[nL1Mu]/I");
  event_tree_->Branch("L1Mu_isMatched", event_.L1Mu_isMatched,"L1Mu_isMatched[nL1Mu]/I");
  event_tree_->Branch("L1Mu_isUnMatched", event_.L1Mu_isUnMatched,"L1Mu_isUnMatched[nL1Mu]/I");
  event_tree_->Branch("L1Mu_isUnMatchedL1TkPt2", event_.L1Mu_isUnMatchedL1TkPt2,"L1Mu_isUnMatchedL1TkPt2[nL1Mu]/I");
  event_tree_->Branch("L1Mu_isUnMatchedL1TkPt3", event_.L1Mu_isUnMatchedL1TkPt3,"L1Mu_isUnMatchedL1TkPt3[nL1Mu]/I");
  event_tree_->Branch("L1Mu_isUnMatchedL1TkPt4", event_.L1Mu_isUnMatchedL1TkPt4,"L1Mu_isUnMatchedL1TkPt4[nL1Mu]/I");

  event_tree_->Branch("genGdMu_L1Mu_dR_corr",    event_.genGdMu_L1Mu_dR_corr,    "genGdMu_L1Mu_dR_corr[2][2]/F");
  event_tree_->Branch("genGdMu_L1Mu_index_corr", event_.genGdMu_L1Mu_index_corr, "genGdMu_L1Mu_index_corr[2][2]/F");

  event_tree_->Branch("pt_sim", &event_.pt_sim);
  event_tree_->Branch("eta_sim", &event_.eta_sim);
  event_tree_->Branch("phi_sim", &event_.phi_sim);
  event_tree_->Branch("charge_sim", &event_.charge_sim);
  event_tree_->Branch("has_sim", &event_.has_sim);
  event_tree_->Branch("eta_sim_prop", &event_.eta_sim_prop);
  event_tree_->Branch("phi_sim_prop", &event_.phi_sim_prop);
  event_tree_->Branch("eta_sim_corr", &event_.eta_sim_corr);
  event_tree_->Branch("phi_sim_corr", &event_.phi_sim_corr);
  event_tree_->Branch("dEta_sim_corr", &event_.dEta_sim_corr);
  event_tree_->Branch("dPhi_sim_corr", &event_.dPhi_sim_corr);
  event_tree_->Branch("dR_sim_corr", &event_.dR_sim_corr);
  event_tree_->Branch("dEta_sim_prop", &event_.dEta_sim_prop);
  event_tree_->Branch("dPhi_sim_prop", &event_.dPhi_sim_prop);
  event_tree_->Branch("dR_sim_prop", &event_.dR_sim_prop);
  event_tree_->Branch("pt_L1Tk", &event_.pt_L1Tk);
  event_tree_->Branch("eta_L1Tk", &event_.eta_L1Tk);
  event_tree_->Branch("phi_L1Tk", &event_.phi_L1Tk);
  event_tree_->Branch("charge_L1Tk", &event_.charge_L1Tk);
  event_tree_->Branch("eta_L1Tk_prop", &event_.eta_L1Tk_prop);
  event_tree_->Branch("phi_L1Tk_prop", &event_.phi_L1Tk_prop);
  event_tree_->Branch("eta_L1Tk_corr", &event_.eta_L1Tk_corr);
  event_tree_->Branch("phi_L1Tk_corr", &event_.phi_L1Tk_corr);
  event_tree_->Branch("dEta_L1Tk_corr", &event_.dEta_L1Tk_corr);
  event_tree_->Branch("dPhi_L1Tk_corr", &event_.dPhi_L1Tk_corr);
  event_tree_->Branch("dR_L1Tk_corr", &event_.dR_L1Tk_corr);
  event_tree_->Branch("dEta_L1Tk_prop", &event_.dEta_L1Tk_prop);
  event_tree_->Branch("dPhi_L1Tk_prop", &event_.dPhi_L1Tk_prop);
  event_tree_->Branch("dR_L1Tk_prop", &event_.dR_L1Tk_prop);
  event_tree_->Branch("dEta_sim_L1Tk", &event_.dEta_sim_L1Tk);
  event_tree_->Branch("dPhi_sim_L1Tk", &event_.dPhi_sim_L1Tk);
  event_tree_->Branch("dR_sim_L1Tk", &event_.dR_sim_L1Tk);
}



void 
DisplacedL1MuFilter::clearBranches()
{
  event_.lumi = -99;
  event_.run = -99;
  event_.event = -99;

  for (int i=0; i<2; ++i){
    event_.genGlu_p[i] = -99;
    event_.genGlu_pt[i] = -99;
    event_.genGlu_px[i] = -99;
    event_.genGlu_py[i] = -99;
    event_.genGlu_pz[i] = -99;
    event_.genGlu_eta[i] = -99;
    event_.genGlu_phi[i] = -99;    
  }

  event_.genH_m = -99;
  event_.genH_p = -99;
  event_.genH_pt = -99;
  event_.genH_px = -99;
  event_.genH_py = -99;
  event_.genH_pz = -99;
  event_.genH_eta = -99;
  event_.genH_phi = -99;
  event_.genH_vx = -99;
  event_.genH_vy = -99;
  event_.genH_vz = -99;

  for (int i=0; i<2; ++i){
    event_.genGd_m[i] = -99;
    event_.genGd_E[i] = -99;
    event_.genGd_p[i] = -99;
    event_.genGd_pt[i] = -99;
    event_.genGd_px[i] = -99;
    event_.genGd_py[i] = -99;
    event_.genGd_pz[i] = -99;
    event_.genGd_eta[i] = -99;
    event_.genGd_phi[i] = -99;
    event_.genGd_vx[i] = -99;
    event_.genGd_vy[i] = -99;
    event_.genGd_vz[i] = -99;
  }

  for (int i=0; i<2; ++i){ 
    for (int j=0; j<2; ++j){
      event_.genGdMu_q[i][j] = -99;;
      event_.genGdMu_p[i][j] = -99;;
      event_.genGdMu_pt[i][j] = -99;;
      event_.genGdMu_px[i][j] = -99;;
      event_.genGdMu_py[i][j] = -99;;
      event_.genGdMu_pz[i][j] = -99;;
      event_.genGdMu_eta[i][j] = -99;;
      event_.genGdMu_phi[i][j] = -99;;
      event_.genGdMu_phi_corr[i][j] = -99;;
      event_.genGdMu_vx[i][j] = -99;;
      event_.genGdMu_vy[i][j] = -99;;
      event_.genGdMu_vz[i][j] = -99;;
      event_.genGdMu_dxy[i][j] = -99;;

      event_.genGdMu_L1Mu_dR_corr[i][j] = 99.;
      event_.genGdMu_L1Mu_index_corr[i][j] = 99;
    }
  }
  event_.nL1Mu = 0;


  for (int i=0; i<kMaxL1Mu; ++i){
    event_.L1Mu_pt[i] = -10;
    event_.L1Mu_eta[i] = -10;
    event_.L1Mu_phi[i] = -10;
    event_.L1Mu_charge[i] = -10;
    event_.L1Mu_bx[i] = -10;
    event_.L1Mu_quality[i] = -10;
    event_.L1Mu_isMatched[i] = 0;
    event_.L1Mu_isUnMatched[i] = 0;
    event_.L1Mu_isUnMatchedL1TkPt2[i] = 0;
    event_.L1Mu_isUnMatchedL1TkPt3[i] = 0;
    event_.L1Mu_isUnMatchedL1TkPt4[i] = 0;
  }

  event_.has_sim = -10;
  event_.pt_sim = -10;
  event_.eta_sim = -99;
  event_.phi_sim = -99;
  event_.eta_sim_prop = -99;
  event_.phi_sim_prop = -99;
  event_.eta_sim_corr = -99;
  event_.phi_sim_corr = -99;
  event_.dEta_sim_corr = 99;
  event_.dPhi_sim_corr = 99;
  event_.dR_sim_corr = 99;
  event_.dEta_sim_prop = 99;
  event_.dPhi_sim_prop = 99;
  event_.dR_sim_prop = 99;
  event_.pt_L1Tk = -99;
  event_.eta_L1Tk = -99;
  event_.phi_L1Tk = -99;
  event_.dEta_L1Tk_corr = 99;
  event_.dPhi_L1Tk_corr = 99;
  event_.dR_L1Tk_corr = 99;
  event_.dEta_L1Tk_prop = 99;
  event_.dPhi_L1Tk_prop = 99;
  event_.dR_L1Tk_prop = 99;
  event_.dEta_sim_L1Tk = 99;
  event_.dPhi_sim_L1Tk = 99;
  event_.dR_sim_L1Tk = 99;
}

//define this as a plug-in
DEFINE_FWK_MODULE(DisplacedL1MuFilter);
