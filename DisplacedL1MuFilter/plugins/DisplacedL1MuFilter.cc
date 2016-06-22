// -*- C++ -*-
//
// Package:    DisplacedL1MuFilter
// Class:      DisplacedL1MuFilter
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
#include "DataFormats/GeometrySurface/interface/BoundCylinder.h"
#include "DataFormats/GeometrySurface/interface/BoundDisk.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "SimDataFormats/Track/interface/SimTrackContainer.h"
#include "SimDataFormats/Vertex/interface/SimVertexContainer.h"
#include "DataFormats/Math/interface/normalizedPhi.h"
#include "RecoMuon/DetLayers/interface/MuonDetLayerGeometry.h"
#include "RecoMuon/Records/interface/MuonRecoGeometryRecord.h"
#include "TrackingTools/DetLayers/interface/DetLayer.h"
#include "TrackingTools/KalmanUpdators/interface/Chi2MeasurementEstimator.h"

#include "DataFormats/L1DTTrackFinder/interface/L1MuDTChambPhContainer.h"
#include "DataFormats/L1DTTrackFinder/interface/L1MuDTTrackCand.h"
#include "DataFormats/L1DTTrackFinder/interface/L1MuDTTrackContainer.h"
#include "DataFormats/L1GlobalMuonTrigger/interface/L1MuRegionalCand.h"
#include "L1Trigger/DTTrackFinder/interface/L1MuDTTrack.h"
#include "L1Trigger/DTTrackFinder/src/L1MuDTTrackSegPhi.h"
#include "DataFormats/L1CSCTrackFinder/interface/L1CSCTrackCollection.h"

#include "CondFormats/L1TObjects/interface/L1MuTriggerScales.h"
#include "CondFormats/L1TObjects/interface/L1MuTriggerPtScale.h"
#include "CondFormats/DataRecord/interface/L1MuTriggerPtScaleRcd.h"
#include "CondFormats/DataRecord/interface/L1MuTriggerScalesRcd.h"
#include <L1Trigger/CSCCommonTrigger/interface/CSCConstants.h>
#include <L1Trigger/CSCTrackFinder/interface/CSCTFPtLUT.h>

//
// class declaration
//

const Int_t kMaxL1Mu = 50;
const Int_t kMaxDTTF = 50;
const Int_t kMaxCSCTF = 50;
const Int_t kMaxL1Tk = 500;
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

  Float_t genGdMu_eta_corr[2][2];
  Float_t genGdMu_phi_corr[2][2];
  Float_t genGdMu_deta_corr[2][2];
  Float_t genGdMu_dphi_corr[2][2];
  Float_t genGdMu_dR_corr[2][2];

  Float_t genGdMu_eta_prop[2][2];
  Float_t genGdMu_phi_prop[2][2];
  Float_t genGdMu_deta_prop[2][2];
  Float_t genGdMu_dphi_prop[2][2];
  Float_t genGdMu_dR_prop[2][2];

  Float_t genGdMu_vx[2][2];
  Float_t genGdMu_vy[2][2];
  Float_t genGdMu_vz[2][2];
  Float_t genGdMu_dxy[2][2];
  Float_t genGdMu_L1Tk_dR_prop[2][2];
  Float_t genGdMu_L1Tk_index_prop[2][2];
  Float_t genGdMu_L1Tk_dR_corr[2][2];
  Float_t genGdMu_L1Tk_index_corr[2][2];

  Float_t genGd0Gd1_dR;

  Float_t genGd_genMuMu_dEta[2];
  Float_t genGd_genMuMu_dPhi[2];
  Float_t genGd_genMuMu_dR[2];

  // Matching the dark photons to GEN-level muons
  Float_t genGd_genMu_dEta[2][2];
  Float_t genGd_genMu_dPhi[2][2];
  Float_t genGd_genMu_dR[2][2];

  Int_t nL1Mu;
  Int_t nL1Tk;
  Float_t L1Mu_pt[kMaxL1Mu], L1Mu_eta[kMaxL1Mu], L1Mu_phi[kMaxL1Mu];
  Int_t L1Mu_charge[kMaxL1Mu], L1Mu_bx[kMaxL1Mu];
  Int_t L1Mu_quality[kMaxL1Mu];
  Float_t L1Mu_L1Tk_dR_corr[kMaxL1Mu];
  Float_t L1Mu_L1Tk_pt_corr[kMaxL1Mu];
  Float_t L1Mu_L1Tk_dR_prop[kMaxL1Mu];
  Float_t L1Mu_L1Tk_dR_prop_true[kMaxL1Mu];
  Float_t L1Mu_L1Tk_pt_prop[kMaxL1Mu];
  Float_t L1Tk_pt[kMaxL1Tk], L1Tk_eta[kMaxL1Tk], L1Tk_phi[kMaxL1Tk];
  Float_t L1Tk_eta_prop[kMaxL1Tk], L1Tk_phi_prop[kMaxL1Tk];
  Float_t L1Tk_deta_prop[kMaxL1Tk], L1Tk_dphi_prop[kMaxL1Tk], L1Tk_dR_prop[kMaxL1Tk];
  Float_t L1Tk_eta_corr[kMaxL1Tk], L1Tk_phi_corr[kMaxL1Tk];
  Float_t L1Tk_deta_corr[kMaxL1Tk], L1Tk_dphi_corr[kMaxL1Tk], L1Tk_dR_corr[kMaxL1Tk];

  Float_t genGdMu_L1Mu_dR[2][2];
  Float_t genGdMu_L1Mu_dR_corr[2][2];
  Int_t genGdMu_L1Mu_index_corr[2][2];
  Float_t genGdMu_L1Mu_dR_prop[2][2];
  Int_t genGdMu_L1Mu_index_prop[2][2];

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

  // Matching the L1Mu to DTTF
  Int_t nDTTF;
  Int_t L1Mu_DTTF_index[kMaxL1Mu];
  Float_t DTTF_pt[kMaxDTTF], DTTF_eta[kMaxDTTF], DTTF_phi[kMaxDTTF], DTTF_bx[kMaxDTTF], DTTF_nStubs[kMaxDTTF];
  Float_t DTTF_phi1[kMaxDTTF], DTTF_phi2[kMaxDTTF], DTTF_phi3[kMaxDTTF], DTTF_phi4[kMaxDTTF];
  Float_t DTTF_phib1[kMaxDTTF], DTTF_phib2[kMaxDTTF], DTTF_phib3[kMaxDTTF], DTTF_phib4[kMaxDTTF];
  Int_t DTTF_quality1[kMaxDTTF], DTTF_quality2[kMaxDTTF], DTTF_quality3[kMaxDTTF], DTTF_quality4[kMaxDTTF];
  Int_t DTTF_bx1[kMaxDTTF], DTTF_bx2[kMaxDTTF], DTTF_bx3[kMaxDTTF], DTTF_bx4[kMaxDTTF];
  Int_t DTTF_wh1[kMaxDTTF], DTTF_wh2[kMaxDTTF], DTTF_wh3[kMaxDTTF], DTTF_wh4[kMaxDTTF];
  Int_t DTTF_se1[kMaxDTTF], DTTF_se2[kMaxDTTF], DTTF_se3[kMaxDTTF], DTTF_se4[kMaxDTTF];
  Int_t DTTF_st1[kMaxDTTF], DTTF_st2[kMaxDTTF], DTTF_st3[kMaxDTTF], DTTF_st4[kMaxDTTF];

  // Matching the L1Mu to CSCTF  
  Int_t nCSCTF;
  Int_t L1Mu_CSCTF_index[kMaxL1Mu];
  Float_t CSCTF_pt[kMaxCSCTF], CSCTF_eta[kMaxCSCTF], CSCTF_phi[kMaxCSCTF], CSCTF_bx[kMaxCSCTF], CSCTF_nStubs[kMaxCSCTF], CSCTF_quality[kMaxCSCTF];

  Int_t CSCTF_st1[kMaxCSCTF], CSCTF_ri1[kMaxCSCTF], CSCTF_ch1[kMaxCSCTF], CSCTF_en1[kMaxCSCTF];
  Int_t CSCTF_trk1[kMaxCSCTF], CSCTF_quality1[kMaxCSCTF], CSCTF_wg1[kMaxCSCTF], CSCTF_hs1[kMaxCSCTF]; 
  Int_t CSCTF_pat1[kMaxCSCTF], CSCTF_bend1[kMaxCSCTF], CSCTF_bx1[kMaxCSCTF], CSCTF_clctpat1[kMaxCSCTF];
  
  Int_t CSCTF_st2[kMaxCSCTF], CSCTF_ri2[kMaxCSCTF], CSCTF_ch2[kMaxCSCTF], CSCTF_en2[kMaxCSCTF];
  Int_t CSCTF_trk2[kMaxCSCTF], CSCTF_quality2[kMaxCSCTF], CSCTF_wg2[kMaxCSCTF], CSCTF_hs2[kMaxCSCTF]; 
  Int_t CSCTF_pat2[kMaxCSCTF], CSCTF_bend2[kMaxCSCTF], CSCTF_bx2[kMaxCSCTF], CSCTF_clctpat2[kMaxCSCTF];

  Int_t CSCTF_st3[kMaxCSCTF], CSCTF_ri3[kMaxCSCTF], CSCTF_ch3[kMaxCSCTF], CSCTF_en3[kMaxCSCTF];
  Int_t CSCTF_trk3[kMaxCSCTF], CSCTF_quality3[kMaxCSCTF], CSCTF_wg3[kMaxCSCTF], CSCTF_hs3[kMaxCSCTF]; 
  Int_t CSCTF_pat3[kMaxCSCTF], CSCTF_bend3[kMaxCSCTF], CSCTF_bx3[kMaxCSCTF], CSCTF_clctpat3[kMaxCSCTF];

  Int_t CSCTF_st4[kMaxCSCTF], CSCTF_ri4[kMaxCSCTF], CSCTF_ch4[kMaxCSCTF], CSCTF_en4[kMaxCSCTF];
  Int_t CSCTF_trk4[kMaxCSCTF], CSCTF_quality4[kMaxCSCTF], CSCTF_wg4[kMaxCSCTF], CSCTF_hs4[kMaxCSCTF]; 
  Int_t CSCTF_pat4[kMaxCSCTF], CSCTF_bend4[kMaxCSCTF], CSCTF_bx4[kMaxCSCTF], CSCTF_clctpat4[kMaxCSCTF];
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

double My_dPhi(double phi1, double phi2) {
  double dPhi = phi1 - phi2;
  if (dPhi >  M_PI) dPhi -= 2.*M_PI;
  if (dPhi < -M_PI) dPhi += 2.*M_PI;
  return dPhi;
}

double phiL1DTTrack(const L1MuDTTrack& track)
{
  int phi_local = track.phi_packed(); //range: 0 < phi_local < 31
  if ( phi_local > 15 ) phi_local -= 32; //range: -16 < phi_local < 15    
  double dttrk_phi_global = normalizedPhi((phi_local*(M_PI/72.))+((M_PI/6.)*track.spid().sector()));// + 12*i->scNum(); //range: -16 < phi_global < 147 
  // if(dttrk_phi_global < 0) dttrk_phi_global+=2*M_PI; //range: 0 < phi_global < 147
  // if(dttrk_phi_global > 2*M_PI) dttrk_phi_global-=2*M_PI; //range: 0 < phi_global < 143
  return dttrk_phi_global;
}

double phiL1CSCTrack(const csc::L1Track& track)
{
  unsigned gbl_phi(track.localPhi() + ((track.sector() - 1)*24) + 6);
  if(gbl_phi > 143) gbl_phi -= 143;
  double phi_packed = gbl_phi & 0xff;
  return phi_packed;
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
  void clearBranches();

  virtual void beginJob() override;
  virtual bool filter(edm::Event&, const edm::EventSetup&) override;
  virtual void endJob() override;

  GlobalPoint extrapolateGP(const reco::GenParticle &tk);
  GlobalPoint extrapolateGP(const TTTrack< Ref_PixelDigi_ > &tk);
  GlobalPoint propagateToZ(const GlobalPoint &inner_point, const GlobalVector &inner_vec, double, double) const;
  GlobalPoint propagateToR(const GlobalPoint &inner_point, const GlobalVector &inner_vec, double, double) const;
  FreeTrajectoryState startingState(const reco::GenParticle &tk) const;
  FreeTrajectoryState startingState(const TTTrack< Ref_PixelDigi_ > &tk) const;

  TrajectoryStateOnSurface extrapolate(const FreeTrajectoryState &start) const;
  /// Extrapolate reco::Candidate to the muon station 2, return an invalid TSOS if it fails
  TrajectoryStateOnSurface extrapolate(const reco::GenParticle &tk) const { 
    return extrapolate(startingState(tk)); 
  }
  TrajectoryStateOnSurface extrapolate(const TTTrack< Ref_PixelDigi_ > &tk) const { 
    return extrapolate(startingState(tk)); 
  }
  
  /// Get the best TSOS on one of the chambres of this DetLayer, or an invalid TSOS if none match
  TrajectoryStateOnSurface getBestDet(const TrajectoryStateOnSurface &tsos, const DetLayer *station) const;

  
  // ----------member data ---------------------------

  enum WhichTrack { None, TrackerTk, MuonTk, GlobalTk };
  enum WhichState { AtVertex, Innermost, Outermost };

  /// Use simplified geometry (cylinders and disks, not individual chambers)
  bool useSimpleGeometry_;

  /// Propagate to MB2 (default) instead of MB1
  bool useMB2_;

  /// Fallback to ME1 if propagation to ME2 fails
  bool fallbackToME1_;

  /// Labels for input collections
  WhichTrack whichTrack_;
  WhichState whichState_;

  /// for cosmics, some things change: the along-opposite is not in-out, nor the innermost/outermost states are in-out really
  bool cosmicPropagation_;

  int min_L1Mu_Quality;
  double max_dR_L1Mu_L1Tk;
  double max_dR_L1Mu_noL1Tk;
  double min_pT_L1Tk;
  double max_pT_L1Tk;
  int verbose;

  edm::InputTag L1Mu_input;
  edm::InputTag L1TkMu_input;
  
  edm::ESHandle<MagneticField> magfield_;
  edm::ESHandle<Propagator> propagator_;
  edm::ESHandle<Propagator> propagatorOpposite_;
  edm::ESHandle<Propagator> propagatorAny_;
  edm::ESHandle<MuonDetLayerGeometry> muonGeometry_;
  const  BoundCylinder *barrelCylinder_;
  const  BoundDisk *endcapDiskPos_[3], *endcapDiskNeg_[3];
  double barrelHalfLength_;
  std::pair<float,float> endcapRadii_[3];
  MyEvent event_;
  TTree* event_tree_;

  // trigger scale
  unsigned long long  muScalesCacheID_;
  unsigned long long  muPtScaleCacheID_;

  edm::ESHandle< L1MuTriggerScales > muScales;
  edm::ESHandle< L1MuTriggerPtScale > muPtScale;
};

DisplacedL1MuFilter::DisplacedL1MuFilter(const edm::ParameterSet& iConfig) : 
  useSimpleGeometry_(iConfig.getParameter<bool>("useSimpleGeometry")),
  useMB2_(iConfig.existsAs<bool>("useStation2") ? iConfig.getParameter<bool>("useStation2") : true),
  fallbackToME1_(iConfig.existsAs<bool>("fallbackToME1") ? iConfig.getParameter<bool>("fallbackToME1") : false),
  whichTrack_(None), whichState_(AtVertex),
  cosmicPropagation_(iConfig.getParameter<bool>("cosmicPropagationHypothesis"))
{
  //now do what ever initialization is needed
  min_L1Mu_Quality = iConfig.getParameter<int>("min_L1Mu_Quality");
  max_dR_L1Mu_L1Tk = iConfig.getParameter<double>("max_dR_L1Mu_L1Tk");
  max_dR_L1Mu_noL1Tk = iConfig.getParameter<double>("max_dR_L1Mu_noL1Tk");
  min_pT_L1Tk = iConfig.getParameter<double>("min_pT_L1Tk");
  max_pT_L1Tk = iConfig.getParameter<double>("max_pT_L1Tk");
  verbose = iConfig.getParameter<int>("verbose");
  
  L1Mu_input = iConfig.getParameter<edm::InputTag>("L1Mu_input");
  L1TkMu_input = iConfig.getParameter<edm::InputTag>("L1TkMu_input");
  
  bookL1MuTree();

  muScalesCacheID_ = 0ULL ;
  muPtScaleCacheID_ = 0ULL ;

}

DisplacedL1MuFilter::~DisplacedL1MuFilter()
{
}


bool
DisplacedL1MuFilter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  double eq = 0.000001;

  clearBranches();
  
  // propagator
  iSetup.get<IdealMagneticFieldRecord>().get(magfield_);
  iSetup.get<TrackingComponentsRecord>().get("SteppingHelixPropagatorAlong", propagator_);
  iSetup.get<TrackingComponentsRecord>().get("SteppingHelixPropagatorOpposite", propagatorOpposite_);
  iSetup.get<TrackingComponentsRecord>().get("SteppingHelixPropagatorAny",      propagatorAny_);
  iSetup.get<MuonRecoGeometryRecord>().get(muonGeometry_);

  // Get the barrel cylinder
  const DetLayer * dtLay = muonGeometry_->allDTLayers()[useMB2_ ? 1 : 0];
  barrelCylinder_ = dynamic_cast<const BoundCylinder *>(&dtLay->surface());
  barrelHalfLength_ = barrelCylinder_->bounds().length()/2;;
  // std::cout << "L1MuonMatcher: barrel radius = " << barrelCylinder_->radius() << ", half length = " << barrelHalfLength_ << std::endl;

  // Get the endcap disks. Note that ME1 has two disks (ME1/1 and ME2/1-ME3/2-ME4/1), so there's one more index
  for (size_t i = 0; i <= (useMB2_ ? 2 : 1); ++i) {
    endcapDiskPos_[i] = dynamic_cast<const BoundDisk *>(& muonGeometry_->forwardCSCLayers()[i]->surface());
    endcapDiskNeg_[i] = dynamic_cast<const BoundDisk *>(& muonGeometry_->backwardCSCLayers()[i]->surface());
    endcapRadii_[i] = std::make_pair(endcapDiskPos_[i]->innerRadius(), endcapDiskPos_[i]->outerRadius());
    // std::cout << "L1MuonMatcher: endcap " << i << " Z = " << endcapDiskPos_[i]->position().z() << ", radii = " << endcapRadii_[i].first << "," << endcapRadii_[i].second << std::endl;
  }


  typedef std::vector<L1MuGMTCand> GMTs;
  edm::Handle<GMTs> aH;
  iEvent.getByLabel("simGmtDigis", aH);
  const GMTs& l1GmtCands(*aH.product());

  // edm::Handle<L1MuDTChambPhContainer> L1MuDTChambPhH;
  // iEvent.getByLabel("simDtTriggerPrimitiveDigis", L1MuDTChambPhH);
  // const L1MuDTChambPhContainer& L1MuDTChambPhs(*L1MuDTChambPhH.product());

  // edm::Handle<L1MuDTTrackContainer> L1MuDTTrackH;
  // iEvent.getByLabel("simDttfDigis", "DTTF", L1MuDTTrackH);
  // const L1MuDTTrackContainer& L1MuDTTracks(*L1MuDTTrackH.product());

  // edm::Handle<vector<L1MuRegionalCand> > L1MuDTRegTrackH;
  // iEvent.getByLabel("simDttfDigis", "DT", L1MuDTRegTrackH);
  // const vector<L1MuRegionalCand>& L1MuDTRegTracks(*L1MuDTRegTrackH.product());
  
  edm::Handle<vector<pair<L1MuDTTrack,vector<L1MuDTTrackSegPhi> > > > L1DTTrackPhiH;
  iEvent.getByLabel("dttfDigis","DTTF", L1DTTrackPhiH);
  const vector<pair<L1MuDTTrack,vector<L1MuDTTrackSegPhi> > >& L1DTTrackPhis(*L1DTTrackPhiH.product());

  // tracks produced by TF
  edm::Handle< L1CSCTrackCollection > hl1Tracks;
  iEvent.getByLabel("simCsctfTrackDigis", hl1Tracks);
  const L1CSCTrackCollection& l1Tracks(*hl1Tracks.product());

  if (iSetup.get< L1MuTriggerScalesRcd >().cacheIdentifier() != muScalesCacheID_ ||
      iSetup.get< L1MuTriggerPtScaleRcd >().cacheIdentifier() != muPtScaleCacheID_ )
    {
      iSetup.get< L1MuTriggerScalesRcd >().get( muScales );
      iSetup.get< L1MuTriggerPtScaleRcd >().get( muPtScale );

      muScalesCacheID_  = iSetup.get< L1MuTriggerScalesRcd >().cacheIdentifier();
      muPtScaleCacheID_ = iSetup.get< L1MuTriggerPtScaleRcd >().cacheIdentifier();
    }

  
  // edm::Handle<L1MuGMTReadoutCollection> hl1GmtCands;
  // iEvent.getByLabel(L1Mu_input, hl1GmtCands );
  
  //  std::vector<L1MuGMTExtendedCand> l1GmtCands;

  // Get GMT candidates from all bunch crossings
  // auto gmt_records = hl1GmtCands->getRecords();
  // for (auto rItr = gmt_records.begin(); rItr!=gmt_records.end() ; ++rItr ){
  //   if (rItr->getBxInEvent() < -1 || rItr->getBxInEvent() > 1) continue;
    
  //   auto GMTCands = rItr->getGMTCands();
  //   for (auto cItr = GMTCands.begin() ; cItr != GMTCands.end() ; ++cItr )
  //     if (!cItr->empty()) l1GmtCands.push_back(*cItr);
  // }

  // // L1 Trigger Analysis
  // edm::Handle<l1extra::L1MuonParticleCollection> muonsHandle;
  // iEvent.getByLabel("l1extraParticles", muonsHandle);
  // //const l1extra::L1MuonParticleCollection& muons = *muonsHandle.product();

  // L1 TrackingTrigger Analysis
  edm::Handle< std::vector< TTTrack< Ref_PixelDigi_ > > > TTTrackHandle;
  iEvent.getByLabel("TTTracksFromPixelDigis", "Level1TTTracks", TTTrackHandle);
  const std::vector< TTTrack< Ref_PixelDigi_ > >& TTTracks = *TTTrackHandle.product();

  // edm::Handle<edm::SimTrackContainer> sim_tracks;
  // iEvent.getByLabel("g4SimHits", sim_tracks);
  // const edm::SimTrackContainer & sim_trks = *sim_tracks.product();

  // edm::Handle<edm::SimVertexContainer> sim_vertices;
  // iEvent.getByLabel("g4SimHits", sim_vertices);
  // const edm::SimVertexContainer & sim_vtxs = *sim_vertices.product();
  
  event_.lumi = iEvent.id().luminosityBlock();
  event_.run = iEvent.id().run();
  event_.event = iEvent.id().event();

  event_.nL1Mu = l1GmtCands.size();
  event_.nL1Tk = TTTracks.size();
  
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
    //cout << counterGenParticle << " " << iGenParticle->status() << " " << iGenParticle->pdgId() << " " << iGenParticle->vx() << " " << iGenParticle->vy() << " " << iGenParticle->vz() << endl;
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

  bool sortGammaDark(false);
  if (sortGammaDark) {
    if ( genGd_unsorted.size() >= 2 ) {
      // Sort genGd by pt (leading pt first)
      std::sort (genGd_unsorted.begin(), genGd_unsorted.end(), PtOrder);
      // Remove duplicates from genGd
      //    Float_t A_pt = genGd_unsorted[0]->pt();
      //    for ( unsigned int i = 1; i < genGd_unsorted.size(); i++ ) {
      //      if ( fabs( genGd_unsorted[i]->pt() - A_pt) > eq ) {
      //        A_pt = genGd_unsorted[i]->pt();
      //        genGd.push_back( genGd_unsorted[i] );
      //      }
      //    }
    }
  }
  genGd = genGd_unsorted;
  
  // check again that the gluons are in fact the mother particles
  if ( genGlu_unsorted.size() >= 2 ) {
    // Sort genGlu by pt (leading pt first)
    std::sort (genGlu_unsorted.begin(), genGlu_unsorted.end(), PtOrder);
  }

  genGlu = genGlu_unsorted;

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
    cout << "WARNING! genH.size() != 1" << endl;
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

  // event_.genGd0Gd1_m = invariantMass(genGd[0],genGd[1]);
  event_.genGd0Gd1_dR = deltaR(event_.genGd_eta[0], 
                               event_.genGd_phi[0], 
                               event_.genGd_eta[1], 
                               event_.genGd_phi[1]);

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
        event_.genGdMu_eta_corr[i][j] = genMuonGroups[i][j]->eta();
        event_.genGdMu_phi_corr[i][j] = phiHeavyCorr(genMuonGroups[i][j]->pt(), genMuonGroups[i][j]->eta(), 
                                                     genMuonGroups[i][j]->phi(), genMuonGroups[i][j]->charge());
        event_.genGdMu_deta_corr[i][j] = std::abs(event_.genGdMu_eta[i][j] - event_.genGdMu_eta_corr[i][j]);
        event_.genGdMu_dphi_corr[i][j] = My_dPhi(event_.genGdMu_phi[i][j], event_.genGdMu_phi_corr[i][j]);
        event_.genGdMu_dR_corr[i][j] = reco::deltaR(event_.genGdMu_eta[i][j], event_.genGdMu_phi[i][j],
                                                    event_.genGdMu_eta_corr[i][j], event_.genGdMu_phi_corr[i][j]);
        
        event_.genGdMu_vx[i][j] = genMuonGroups[i][j]->vx();
        event_.genGdMu_vy[i][j] = genMuonGroups[i][j]->vy();
        event_.genGdMu_vz[i][j] = genMuonGroups[i][j]->vz();

        // TrajectoryStateOnSurface stateAtMB2 = extrapolate(*genMuonGroups[i][j]);
        // if (stateAtMB2.isValid()) {
        //   event_.genGdMu_eta_prop[i][j] = stateAtMB2.globalPosition().eta();
        //   event_.genGdMu_phi_prop[i][j] = stateAtMB2.globalPosition().phi();
        // }
        // return FreeTrajectoryState(  GlobalPoint(tk.vx(), tk.vy(), tk.vz()),
        //                              GlobalVector(tk.px(), tk.py(), tk.pz()),
        //                              int(tk.charge()),
        //                              magfield_.product());
        
        GlobalPoint ex_point(extrapolateGP(*genMuonGroups[i][j]));
        if (!(ex_point == GlobalPoint())){
          event_.genGdMu_eta_prop[i][j] = ex_point.eta();
          event_.genGdMu_phi_prop[i][j] = ex_point.phi();
          event_.genGdMu_deta_prop[i][j] = std::abs(event_.genGdMu_eta[i][j] - event_.genGdMu_eta_prop[i][j]);
          event_.genGdMu_dphi_prop[i][j] = My_dPhi(event_.genGdMu_phi[i][j], event_.genGdMu_phi_prop[i][j]);
          event_.genGdMu_dR_prop[i][j] = reco::deltaR(event_.genGdMu_eta[i][j], event_.genGdMu_phi[i][j],
                                                      event_.genGdMu_eta_prop[i][j], event_.genGdMu_phi_prop[i][j]);
        }
      }
    }
    
    if (fabs(event_.genGdMu_vx[0][0] - event_.genGdMu_vx[0][1]) < eq and
        fabs(event_.genGdMu_vx[1][0] - event_.genGdMu_vx[1][1]) < eq and
        fabs(event_.genGdMu_vy[0][0] - event_.genGdMu_vy[0][1]) < eq and
        fabs(event_.genGdMu_vy[1][0] - event_.genGdMu_vy[1][1]) < eq and
        fabs(event_.genGdMu_vz[0][0] - event_.genGdMu_vz[0][1]) < eq and
        fabs(event_.genGdMu_vz[1][0] - event_.genGdMu_vz[1][1]) < eq) {
      
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
    for (int i=0; i<2; ++i){         
      event_.genGd_genMuMu_dEta[i] = My_dPhi(genMuonGroups[i][0]->eta(), genMuonGroups[i][1]->eta());
      event_.genGd_genMuMu_dPhi[i] = My_dPhi(genMuonGroups[i][0]->phi(), genMuonGroups[i][1]->phi());
      event_.genGd_genMuMu_dR[i]   = sqrt(event_.genGd_genMuMu_dEta[i]*event_.genGd_genMuMu_dEta[i] + 
                                          event_.genGd_genMuMu_dPhi[i]*event_.genGd_genMuMu_dPhi[i]);
      for (int j=0; j<2; ++j){
        event_.genGd_genMu_dEta[i][j] = event_.genGd_eta[i] - event_.genGdMu_eta[i][j];
        event_.genGd_genMu_dPhi[i][j] = event_.genGd_phi[i] - event_.genGdMu_phi[i][j];
        event_.genGd_genMu_dR[i][j]   = deltaR(event_.genGd_eta[i], event_.genGd_phi[i], 
                                               event_.genGdMu_eta[i][j], event_.genGdMu_phi[i][j]);
      }
    }
    if(verbose) { 
      for (int i=0; i<2; ++i){ 
        for (int j=0; j<2; ++j){
          cout << "genGd"<<i<<"Mu"<<j<<"_pt " << event_.genGdMu_pt[i][j] << endl;
          cout << "genGd"<<i<<"Mu"<<j<<"_eta " << event_.genGdMu_eta[i][j] << endl;
          cout << "genGd"<<i<<"Mu"<<j<<"_phi " << event_.genGdMu_phi[i][j] << endl;
          cout << "genGd"<<i<<"Mu"<<j<<"_phi_corr " << event_.genGdMu_phi_corr[i][j] << endl;
          cout << "genGd"<<i<<"Mu"<<j<<"_eta_prop " << event_.genGdMu_eta_prop[i][j] << endl;
          cout << "genGd"<<i<<"Mu"<<j<<"_phi_prop " << event_.genGdMu_phi_prop[i][j] << endl;
          cout << "genGd"<<i<<"Mu"<<j<<"_dxy " << event_.genGdMu_dxy[i][j] << endl;
        }
      }
    }
  }

  for (int i=0; i<2; ++i){         
    for (int j=0; j<2; ++j){
      for (unsigned int k=0; k<TTTracks.size(); ++k) {
        auto l1Tk = TTTracks[k];
        const double l1Tk_eta = l1Tk.getMomentum().eta();
        const double l1Tk_phi = normalizedPhi(l1Tk.getMomentum().phi());
        double deltar(reco::deltaR(l1Tk_eta, l1Tk_phi, event_.genGdMu_eta[i][j], event_.genGdMu_phi[i][j]));
        if (deltar < event_.genGdMu_L1Tk_dR_prop[i][j]) {
          event_.genGdMu_L1Tk_dR_prop[i][j] = deltar;
          event_.genGdMu_L1Tk_index_prop[i][j] = k;
        }
      }
    }
  }

  // store the L1Tk variables
  for (unsigned int j=0; j<TTTracks.size(); ++j) {
    auto l1Tk = TTTracks[j];
    const double l1Tk_pt = l1Tk.getMomentum().perp();
    const double l1Tk_eta = l1Tk.getMomentum().eta();
    const double l1Tk_phi = normalizedPhi(l1Tk.getMomentum().phi());
    const double l1Tk_charge = l1Tk.getRInv()>0? 1: -1;
    const double l1Tk_eta_corr = l1Tk_eta;
    const double l1Tk_phi_corr = phiHeavyCorr(l1Tk_pt, l1Tk_eta, l1Tk_phi, l1Tk_charge);

    if(verbose and false) {
      cout << "l1Tk " << j << endl; 
      cout << "l1Tk_pt " << l1Tk_pt << endl;
      cout << "l1Tk_eta " << l1Tk_eta << endl;
      cout << "l1Tk_phi " << l1Tk_phi << endl;
      cout << "l1Tk_phi_corr " << l1Tk_phi_corr << endl;
      cout << "l1Tk_charge " << l1Tk_charge << endl;
    }
      
    double l1Tk_eta_prop = -99;
    double l1Tk_phi_prop = -99;
    GlobalPoint ex_point(extrapolateGP(l1Tk));
    if (!(ex_point == GlobalPoint())) {
      l1Tk_eta_prop = ex_point.eta();
      l1Tk_phi_prop = ex_point.phi();
      if(verbose and false) {
        cout << "l1Tk_eta_prop " << l1Tk_eta_prop << endl;
        cout << "l1Tk_phi_prop " << l1Tk_phi_prop << endl;
      }
    }
    
    event_.L1Tk_pt[j] = l1Tk_pt;
    event_.L1Tk_eta[j] = l1Tk_eta;
    event_.L1Tk_phi[j] = l1Tk_phi;
    
    event_.L1Tk_eta_prop[j] = l1Tk_eta_prop;
    event_.L1Tk_phi_prop[j] = l1Tk_phi_prop;
    event_.L1Tk_deta_prop[j] = std::abs(event_.L1Tk_eta_prop[j] - event_.L1Tk_eta[j]);
    event_.L1Tk_dphi_prop[j] = My_dPhi(event_.L1Tk_phi_prop[j], event_.L1Tk_phi[j]); 
    event_.L1Tk_dR_prop[j] = reco::deltaR(event_.L1Tk_eta_prop[j], event_.L1Tk_phi_prop[j], event_.L1Tk_eta[j], event_.L1Tk_phi[j]);
    
    event_.L1Tk_eta_corr[j] = l1Tk_eta_corr;
    event_.L1Tk_phi_corr[j] = l1Tk_phi_corr;
    event_.L1Tk_deta_corr[j] = std::abs(event_.L1Tk_eta_corr[j] - event_.L1Tk_eta[j]);
    event_.L1Tk_dphi_corr[j] = My_dPhi(event_.L1Tk_phi_corr[j], event_.L1Tk_phi[j]); 
    event_.L1Tk_dR_corr[j] = reco::deltaR(event_.L1Tk_eta_corr[j], event_.L1Tk_phi_corr[j], event_.L1Tk_eta[j], event_.L1Tk_phi[j]);
  } // end of loop on TTTracks
  
  
  /////////////////
  // L1 analysis //
  /////////////////
  
  if(verbose) std::cout << "Number of L1Mu candidates before selections " << event_.nL1Mu << std::endl; 

  for (unsigned int i=0; i<l1GmtCands.size(); ++i) {
    auto l1Mu = l1GmtCands[i];
    event_.L1Mu_pt[i] = l1Mu.ptValue();
    event_.L1Mu_eta[i] = l1Mu.etaValue();
    event_.L1Mu_phi[i] = normalizedPhi(l1Mu.phiValue());
    event_.L1Mu_charge[i] = l1Mu.charge();
    event_.L1Mu_quality[i] = l1Mu.quality();
    event_.L1Mu_bx[i] = l1Mu.bx();
  
    if(verbose) {
      cout << "l1Mu " << i << endl; 
      cout << "l1Mu_pt " << event_.L1Mu_pt[i] << endl;
      cout << "l1Mu_eta " << event_.L1Mu_eta[i] << endl;
      cout << "l1Mu_phi " << event_.L1Mu_phi[i] << endl;
      cout << "l1Mu_quality " << event_.L1Mu_quality[i] << endl;
      cout << "l1Mu_charge " << event_.L1Mu_charge[i] << endl;
      cout << "l1Mu_bx " << event_.L1Mu_bx[i] << endl;
    }

    // find the matching DT
    // auto L1MuDTPhiStubs = *L1MuDTChambPhs.getContainer();
    // std::cout << "Number of L1MuDTPhiStubs " << L1MuDTPhiStubs.size() << std::endl;
    // for (unsigned int j=0; j<L1MuDTPhiStubs.size(); ++j) {
    //   std::cout << "bxNum " << L1MuDTPhiStubs[j].bxNum() << std::endl;
    //   std::cout << "whNum " << L1MuDTPhiStubs[j].whNum() << std::endl;
    //   std::cout << "scNum " << L1MuDTPhiStubs[j].scNum() << std::endl;
    //   std::cout << "stNum " << L1MuDTPhiStubs[j].stNum() << std::endl;
    //   std::cout << "phi " << L1MuDTPhiStubs[j].phi() << std::endl;
    //   std::cout << "phiB " << L1MuDTPhiStubs[j].phiB() << std::endl;
    //   std::cout << "code " << L1MuDTPhiStubs[j].code() << std::endl;
    //   std::cout << "Ts2Tag " << L1MuDTPhiStubs[j].Ts2Tag() << std::endl;
    //   std::cout << "BxCnt " << L1MuDTPhiStubs[j].BxCnt() << std::endl;
    // }

    // find the matching DT tracks
    // auto L1MuDTCands = *L1MuDTTracks.getContainer();
    // std::cout << "Number of L1MuDTCands " <<L1MuDTCands.size() << std::endl;
    // for (unsigned int j=0; j<L1MuDTCands.size(); ++j) {
    //   std::cout << "whNum " << L1MuDTCands[j].whNum() << std::endl;
    //   std::cout << "scNum " << L1MuDTCands[j].scNum() << std::endl;
    //   //      std::cout << "stNum " << L1MuDTCands[j].stNum() << std::endl;
    //   std::cout << "TCNum " << L1MuDTCands[j].TCNum() << std::endl;
    //   std::cout << "TrkTag " << L1MuDTCands[j].TrkTag() << std::endl;
    // }
    
    // std::cout << "Number of L1MuDTRegTracks " <<L1MuDTRegTracks.size() << std::endl;
    // for (unsigned int j=0; j<L1MuDTRegTracks.size(); ++j) {
    //   L1MuDTRegTracks[j].print();
    //   std::cout << "pt " << L1MuDTRegTracks[j].ptValue()
    //             << "eta " << L1MuDTRegTracks[j].etaValue()
    //             << "phi " << L1MuDTRegTracks[j].phiValue() << std::endl;
    // }

    // Matching to DTTF
    if(verbose) std::cout << "Number of L1DTTrackPhis " <<L1DTTrackPhis.size() << std::endl;
    event_.nDTTF = L1DTTrackPhis.size();
    double bestDrL1MuL1DTTrack = 99;
    for (unsigned int j=0; j<L1DTTrackPhis.size(); ++j) {
      auto track = L1DTTrackPhis[j].first;

      double DTTF_pt = muPtScale->getPtScale()->getLowEdge(track.pt()) + 1.e-6;;
      double DTTF_eta = muScales->getRegionalEtaScale(0)->getCenter(track.eta());
      double DTTF_phi = phiL1DTTrack(track);
      double DTTF_bx = track.bx();
      double DTTF_quality = track.quality();
    
      if(verbose) {  
        std::cout << "pt  = " << DTTF_pt
                  << ", eta  = " << DTTF_eta 
                  << ", phi  = " << DTTF_phi 
                  << ", bx " << DTTF_bx 
                  << ", quality " << DTTF_quality << std::endl;
      }

      event_.DTTF_pt[j] = DTTF_pt;
      event_.DTTF_eta[j] = DTTF_eta;
      event_.DTTF_phi[j] = DTTF_phi;
      event_.DTTF_bx[j] = DTTF_bx;
      event_.DTTF_nStubs[j] = L1DTTrackPhis[j].second.size();
      
      // std::cout << "stubs: " << std::endl;
      for (auto stub: L1DTTrackPhis[j].second) {
        // std::cout << "\t " << stub << std::endl;
        // std::cout << "\t phiValue = " << stub.phiValue() << ", phibValue = " << stub.phibValue() << std::endl;
        int station = stub.station();
        switch(station) {
        case 1:
          event_.DTTF_phi1[j] = stub.phiValue();
          event_.DTTF_phib1[j] = stub.phibValue();
          event_.DTTF_quality1[j] = stub.quality();
          event_.DTTF_bx1[j] = stub.bx();
          event_.DTTF_wh1[j] = stub.wheel();
          event_.DTTF_se1[j] = stub.sector();
          event_.DTTF_st1[j] = stub.station();
          break;
        case 2:
          event_.DTTF_phi2[j] = stub.phiValue();
          event_.DTTF_phib2[j] = stub.phibValue();
          event_.DTTF_quality2[j] = stub.quality();
          event_.DTTF_bx2[j] = stub.bx();
          event_.DTTF_wh2[j] = stub.wheel();
          event_.DTTF_se2[j] = stub.sector();
          event_.DTTF_st2[j] = stub.station();
          break;
        case 3:
          event_.DTTF_phi3[j] = stub.phiValue();
          event_.DTTF_phib3[j] = stub.phibValue();
          event_.DTTF_quality3[j] = stub.quality();
          event_.DTTF_bx3[j] = stub.bx();
          event_.DTTF_wh3[j] = stub.wheel();
          event_.DTTF_se3[j] = stub.sector();
          event_.DTTF_st3[j] = stub.station();
          break;
        case 4:
          event_.DTTF_phi4[j] = stub.phiValue();
          event_.DTTF_phib4[j] = stub.phibValue();
          event_.DTTF_quality4[j] = stub.quality();
          event_.DTTF_bx4[j] = stub.bx();
          event_.DTTF_wh4[j] = stub.wheel();
          event_.DTTF_se4[j] = stub.sector();
          event_.DTTF_st4[j] = stub.station();
          break;
        };
      }
      
      if ( ( event_.L1Mu_quality[i] > 0 ) &&
           ( fabs( event_.L1Mu_phi[i] - DTTF_phi ) < 0.001 ) &&             
           ( event_.L1Mu_bx[i] == DTTF_bx ) ) {
        double drL1MuL1DTTrack = reco::deltaR(l1Mu.etaValue(), 
                                              normalizedPhi(l1Mu.phiValue()), 
                                              DTTF_eta, 
                                              DTTF_phi);
        if (drL1MuL1DTTrack < bestDrL1MuL1DTTrack) {
          bestDrL1MuL1DTTrack = drL1MuL1DTTrack;
          event_.L1Mu_DTTF_index[i] = j;
        }
      }                
    }
    
    /*
    if(verbose) {  
      int tempIndex = event_.L1Mu_DTTF_index[i]; 
      if (tempIndex != -1) { // and bestDrL1MuL1DTTrack < 0.2
        // Print matching DTTF track
        auto track = L1DTTrackPhis[tempIndex].first;
        std::cout << "\tMatching DTTF track" << std::endl;
        std::cout << "\tpt "  << muPtScale->getPtScale()->getLowEdge(track.pt() + 1.e-6)
                  << "\teta " << muScales->getRegionalEtaScale(0)->getCenter(track.eta())
                  << "\tphi " << phiL1DTTrack(track) 
                  << "\tbx "  << track.bx()
                  << "\tquality " << track.quality() << std::endl;
        
        // Print stubs
        std::cout << "\tstubs: " << std::endl; 
        for (auto stub: L1DTTrackPhis[tempIndex].second) {
          std::cout << "\t\t " << stub << std::endl;
          std::cout << "\t\t phiValue = " << stub.phiValue() << ", phibValue = " << stub.phibValue() << std::endl;
        }  
      }
      else {
        std::cout << "\tNo matching DTTF track" << std::endl;
      }
    }
    */
    
    // Matching to DTTF     
    event_.nCSCTF = l1Tracks.size();
    if(verbose) std::cout << "Number of L1CSCTracks " <<event_.nCSCTF << std::endl;
    //double bestDrL1MuL1CSCTrack = 99;
    for (int j=0; j<event_.nCSCTF; ++j) {
      auto track = l1Tracks[j].first;
      const int sign(track.endcap()==1 ? 1 : -1);
      const unsigned eta_sign(track.endcap() == 1 ? 0 : 1);
      const int gbl_eta(track.eta_packed() | eta_sign << (L1MuRegionalCand::ETA_LENGTH - 1));
      unsigned gpt = 0, quality = 0;
      csc::L1Track::decodeRank(track.rank(), gpt, quality);
      double pt_packed = gpt & 0x1f;

      // calculate pt, eta and phi (don't forget to store the sign)                                                                                   
      event_.CSCTF_pt[j] = muPtScale->getPtScale()->getLowEdge(pt_packed) + 1.e-6;
      event_.CSCTF_eta[j] = muScales->getRegionalEtaScale(2)->getCenter(track.eta_packed()) * sign;
      event_.CSCTF_phi[j] = normalizedPhi(muScales->getPhiScale()->getLowEdge(phiL1CSCTrack(track)));
      event_.CSCTF_bx[j] = track.bx();
      event_.CSCTF_quality[j] = quality;

      if(verbose) {  
        std::cout << "pt  = " << event_.CSCTF_pt[j]
                  << ", eta  = " << event_.CSCTF_eta[j] 
                  << ", phi  = " << event_.CSCTF_phi[j]
                  << ", bx " << event_.CSCTF_bx[j]
                  << ", quality " << event_.CSCTF_quality[j] << std::endl;
      }


      std::cout << "stubs: " << std::endl;
      auto stubCollection(l1Tracks[j].second);
      for (auto detUnitIt = stubCollection->begin(); detUnitIt != stubCollection->end(); detUnitIt++) {
        const CSCDetId& id = (*detUnitIt).first;
        //std::cout << "DetId " << id << std::endl;
        const auto range = (*detUnitIt).second;
        for (auto digiIt = range.first; digiIt != range.second; digiIt++) {
          if (!(*digiIt).isValid()) continue;
          std::cout << "\t" << *digiIt << std::endl;
        }
      }

      // /// return track number
      // int getTrknmb()  const { return trknmb; }

      // /// return valid pattern bit
      // bool isValid()   const { return valid; }

      // /// return the 4 bit Correlated LCT Quality
      // int getQuality() const { return quality; }

      // /// return the key wire group
      // int getKeyWG()   const { return keywire; }

      // /// return the key halfstrip from 0,159
      // int getStrip()   const { return strip; }

      // /// return pattern
      // int getPattern() const { return pattern; }

      // /// return bend
      // int getBend()    const { return bend; }

      // /// return BX
      // int getBX()      const { return bx; }

      // /// return CLCT pattern number (in use again Feb 2011)
      // int getCLCTPattern() const { return (pattern & 0xF); }

      /*
      // std::cout << "stubs: " << std::endl;
      for (auto stub: l1Tracks[j].second) {
        // std::cout << "\t " << stub << std::endl;
        // std::cout << "\t phiValue = " << stub.phiValue() << ", phibValue = " << stub.phibValue() << std::endl;
        int station = stub.station();
        switch(station) {
        case 1:
          event_.CSCTF_phi1[j] = stub.phiValue();
          event_.CSCTF_phib1[j] = stub.phibValue();
          event_.CSCTF_quality1[j] = stub.quality();
          event_.CSCTF_bx1[j] = stub.bx();
          event_.CSCTF_wh1[j] = stub.wheel();
          event_.CSCTF_se1[j] = stub.sector();
          event_.CSCTF_st1[j] = stub.station();
          break;
        case 2:
          event_.CSCTF_phi2[j] = stub.phiValue();
          event_.CSCTF_phib2[j] = stub.phibValue();
          event_.CSCTF_quality2[j] = stub.quality();
          event_.CSCTF_bx2[j] = stub.bx();
          event_.CSCTF_wh2[j] = stub.wheel();
          event_.CSCTF_se2[j] = stub.sector();
          event_.CSCTF_st2[j] = stub.station();
          break;
        case 3:
          event_.CSCTF_phi3[j] = stub.phiValue();
          event_.CSCTF_phib3[j] = stub.phibValue();
          event_.CSCTF_quality3[j] = stub.quality();
          event_.CSCTF_bx3[j] = stub.bx();
          event_.CSCTF_wh3[j] = stub.wheel();
          event_.CSCTF_se3[j] = stub.sector();
          event_.CSCTF_st3[j] = stub.station();
          break;
        case 4:
          event_.CSCTF_phi4[j] = stub.phiValue();
          event_.CSCTF_phib4[j] = stub.phibValue();
          event_.CSCTF_quality4[j] = stub.quality();
          event_.CSCTF_bx4[j] = stub.bx();
          event_.CSCTF_wh4[j] = stub.wheel();
          event_.CSCTF_se4[j] = stub.sector();
          event_.CSCTF_st4[j] = stub.station();
          break;
        };
      }
      */
    }


    // calculate the number of L1Tk within 0.12
    for (unsigned int j=0; j<TTTracks.size(); ++j) {
      auto l1Tk = TTTracks[j];
      const double l1Tk_pt = l1Tk.getMomentum().perp();
      const double l1Tk_eta = l1Tk.getMomentum().eta();
      const double l1Tk_phi = normalizedPhi(l1Tk.getMomentum().phi());
      const double l1Tk_charge = l1Tk.getRInv()>0? 1: -1;
      const double l1Tk_eta_corr = l1Tk_eta;
      const double l1Tk_phi_corr = phiHeavyCorr(l1Tk_pt, l1Tk_eta, l1Tk_phi, l1Tk_charge);

      if(verbose and false) {
        cout << "l1Tk " << j << endl; 
        cout << "l1Tk_pt " << l1Tk_pt << endl;
        cout << "l1Tk_eta " << l1Tk_eta << endl;
        cout << "l1Tk_phi " << l1Tk_phi << endl;
        cout << "l1Tk_phi_corr " << l1Tk_phi_corr << endl;
        cout << "l1Tk_charge " << l1Tk_charge << endl;
      }
      
      double l1Tk_eta_prop = -99;
      double l1Tk_phi_prop = -99;
      GlobalPoint ex_point(extrapolateGP(l1Tk));
      if (!(ex_point == GlobalPoint())) {
        l1Tk_eta_prop = ex_point.eta();
        l1Tk_phi_prop = ex_point.phi();
        if(verbose and false) {
          cout << "l1Tk_eta_prop " << l1Tk_eta_prop << endl;
          cout << "l1Tk_phi_prop " << l1Tk_phi_prop << endl;
        }
        const double dR_l1Mu_l1Tk_prop = reco::deltaR(l1Tk_eta_prop, l1Tk_phi_prop, event_.L1Mu_eta[i], event_.L1Mu_phi[i]);
        if (dR_l1Mu_l1Tk_prop < event_.L1Mu_L1Tk_dR_prop[i]) {
          event_.L1Mu_L1Tk_dR_prop[i] = dR_l1Mu_l1Tk_prop;
          event_.L1Mu_L1Tk_pt_prop[i] = l1Tk_pt;
        }
      }

      // TrajectoryStateOnSurface stateAtMB2 = extrapolate(l1Tk);
      // if (stateAtMB2.isValid()) {
      //   // std::cout << ">>>Final State is valid" << std::endl;
      //   l1Tk_eta_prop = stateAtMB2.globalPosition().eta();
      //   l1Tk_phi_prop = stateAtMB2.globalPosition().phi();
      //   if(verbose) {
      //     cout << "l1Tk_eta_prop " << l1Tk_eta_prop << endl;
      //     cout << "l1Tk_phi_prop " << l1Tk_phi_prop << endl;
      //   }
      //   // cout << endl;
      //   const double dR_l1Mu_l1Tk_prop = reco::deltaR(l1Tk_eta_prop, l1Tk_phi_prop, event_.L1Mu_eta[i], event_.L1Mu_phi[i]);
      //   if (dR_l1Mu_l1Tk_prop < event_.L1Mu_L1Tk_dR_prop[i]) {
      //     event_.L1Mu_L1Tk_dR_prop[i] = dR_l1Mu_l1Tk_prop;
      //     event_.L1Mu_L1Tk_pt_prop[i] = l1Tk_pt;
      //   }
      // }
      
      const double dR_l1Mu_l1Tk_corr = reco::deltaR(l1Tk_eta_corr, l1Tk_phi_corr, event_.L1Mu_eta[i], event_.L1Mu_phi[i]);
      if (dR_l1Mu_l1Tk_corr < event_.L1Mu_L1Tk_dR_corr[i]) {
        event_.L1Mu_L1Tk_dR_corr[i] = dR_l1Mu_l1Tk_corr;
        event_.L1Mu_L1Tk_pt_corr[i] = l1Tk_pt;
      }
    } // end of loop on TTTracks
    
    // match the L1Mu to GEN
    if (genMuonGroups.size() == 2 and genMuonGroups[0].size() == 2 and genMuonGroups[1].size() == 2) {
      double newDR[2][2];
      for (int k=0; k<2; ++k){ 
        for (int j=0; j<2; ++j){
          newDR[k][j] = deltaR(event_.genGdMu_eta[k][j], event_.genGdMu_phi_corr[k][j], event_.L1Mu_eta[i], event_.L1Mu_phi[i]);        
          if(verbose) cout << "newDR " << k <<  j << " " << newDR[k][j] << " pt " << event_.genGdMu_pt[k][j]
                           << " eta_corr " << event_.genGdMu_eta[k][j] << " phi_corr " << event_.genGdMu_phi_corr[k][j] 
                           << " Q " << event_.genGdMu_q[k][j] << endl;
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
        if(verbose) cout << "Muon[0][0] was matched within " << event_.genGdMu_L1Mu_dR_corr[0][0] <<" to L1Mu "<<i<<std::endl;
        }
        break;
      case 1:
        if (newDR[0][1] < event_.genGdMu_L1Mu_dR_corr[0][1]) { 
          event_.genGdMu_L1Mu_index_corr[0][1] = i;
          event_.genGdMu_L1Mu_dR_corr[0][1] = newDR[0][1];
          if(verbose) cout << "Muon[0][1] was matched within " << event_.genGdMu_L1Mu_dR_corr[0][1] <<" to L1Mu "<<i<< std::endl;
        }
        break;
      case 2:
        if (newDR[1][0] < event_.genGdMu_L1Mu_dR_corr[1][0]) { 
          event_.genGdMu_L1Mu_index_corr[1][0] = i;
          event_.genGdMu_L1Mu_dR_corr[1][0] = newDR[1][0];
          if(verbose) cout << "Muon[1][0] was matched within " << event_.genGdMu_L1Mu_dR_corr[1][0] <<" to L1Mu "<<i<< std::endl;
        }
        break;
      case 3:
        if (newDR[1][1] < event_.genGdMu_L1Mu_dR_corr[1][1]) { 
          event_.genGdMu_L1Mu_index_corr[1][1] = i;
          event_.genGdMu_L1Mu_dR_corr[1][1] = newDR[1][1];
          if(verbose) cout << "Muon[1][1] was matched within " << event_.genGdMu_L1Mu_dR_corr[1][1] <<" to L1Mu "<<i<< std::endl;
        }
        break;
      };
    }
    
    // match the L1Mu to GEN    (propagated)
    if (genMuonGroups.size() == 2 and genMuonGroups[0].size() == 2 and genMuonGroups[1].size() == 2) {
      double newDR[2][2];
      for (int k=0; k<2; ++k){ 
        for (int j=0; j<2; ++j){
          newDR[k][j] = deltaR(event_.genGdMu_eta_prop[k][j], event_.genGdMu_phi_prop[k][j], event_.L1Mu_eta[i], event_.L1Mu_phi[i]);        
          if(verbose) cout << "newDR " << k <<  j << " " << newDR[k][j] << " pt " << event_.genGdMu_pt[k][j]
                           << " eta_prop " << event_.genGdMu_eta_prop[k][j] << " phi_prop " << event_.genGdMu_phi_prop[k][j] 
                           << " Q " << event_.genGdMu_q[k][j] << endl;
        }
      }
      
      const std::vector<double> v{newDR[0][0], newDR[0][1], newDR[1][0], newDR[1][1]};
      auto result(std::min_element(std::begin(v), std::end(v)));
      auto dis(std::distance(std::begin(v), result));
      
      switch (dis){
      case 0: 
        if (newDR[0][0] < event_.genGdMu_L1Mu_dR_prop[0][0]) { 
          event_.genGdMu_L1Mu_index_prop[0][0] = i;
          event_.genGdMu_L1Mu_dR_prop[0][0] = newDR[0][0];
          if(verbose) cout << "Muon[0][0] was matched within " << event_.genGdMu_L1Mu_dR_prop[0][0] <<" to L1Mu "<<i<<std::endl;
        }
        break;
      case 1:
        if (newDR[0][1] < event_.genGdMu_L1Mu_dR_prop[0][1]) { 
          event_.genGdMu_L1Mu_index_prop[0][1] = i;
          event_.genGdMu_L1Mu_dR_prop[0][1] = newDR[0][1];
          if(verbose) cout << "Muon[0][1] was matched within " << event_.genGdMu_L1Mu_dR_prop[0][1] <<" to L1Mu "<<i<< std::endl;
        }
        break;
      case 2:
        if (newDR[1][0] < event_.genGdMu_L1Mu_dR_prop[1][0]) { 
          event_.genGdMu_L1Mu_index_prop[1][0] = i;
          event_.genGdMu_L1Mu_dR_prop[1][0] = newDR[1][0];
          if(verbose) cout << "Muon[1][0] was matched within " << event_.genGdMu_L1Mu_dR_prop[1][0] <<" to L1Mu "<<i<< std::endl;
        }
        break;
      case 3:
        if (newDR[1][1] < event_.genGdMu_L1Mu_dR_prop[1][1]) { 
          event_.genGdMu_L1Mu_index_prop[1][1] = i;
          event_.genGdMu_L1Mu_dR_prop[1][1] = newDR[1][1];
          if(verbose) cout << "Muon[1][1] was matched within " << event_.genGdMu_L1Mu_dR_prop[1][1] <<" to L1Mu "<<i<< std::endl;
        }
        break;
      };
      
      for (int k=0; k<2; ++k){ 
        for (int j=0; j<2; ++j){
          if (event_.genGdMu_L1Tk_index_prop[k][j] != -99) {
            double deltaRL1MuTrueL1Tk(reco::deltaR(TTTracks[event_.genGdMu_L1Tk_index_prop[k][j]].getMomentum().eta(), 
                                                   normalizedPhi(TTTracks[event_.genGdMu_L1Tk_index_prop[k][j]].getMomentum().phi()), 
                                                   event_.L1Mu_eta[i], event_.L1Mu_phi[i]));
            if (deltaRL1MuTrueL1Tk < event_.L1Mu_L1Tk_dR_prop_true[i]) {
              event_.L1Mu_L1Tk_dR_prop_true[i] = deltaRL1MuTrueL1Tk;
            }
          }
        }
      }
    }
    }
  
  event_tree_->Fill();  
  
  return true;
}
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

// ------------ method called once each job just before starting event loop  ------------
void 
DisplacedL1MuFilter::beginJob()
{
}
 
// ------------ method called once each job just after ending the event loop  ------------
 void 
   DisplacedL1MuFilter::endJob()
{
}
 
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
DisplacedL1MuFilter::extrapolateGP(const reco::GenParticle &tk)
{
  GlobalPoint inner_point(tk.vx(), tk.vy(), tk.vz());
  GlobalVector inner_vec (tk.px(), tk.py(), tk.pz());
  if (std::abs(tk.eta())<1.2) {
    GlobalPoint loc_barrel(propagateToR(inner_point, inner_vec, tk.charge(), 523.));
    return loc_barrel;
  } 
  else if (tk.eta()>1.2) {
    GlobalPoint loc_endcap_pos(propagateToZ(inner_point, inner_vec, tk.charge(), 828));
    return loc_endcap_pos;
  } 
  else if (tk.eta()<-1.2) {
    GlobalPoint loc_endcap_neg(propagateToZ(inner_point, inner_vec, tk.charge(), -828));
    return loc_endcap_neg;
  }
  return GlobalPoint();
}

GlobalPoint 
DisplacedL1MuFilter::extrapolateGP(const TTTrack< Ref_PixelDigi_ > &tk)
{
  GlobalPoint inner_point(tk.getPOCA());
  GlobalVector inner_vec (tk.getMomentum());
  double charge(tk.getRInv()>0? 1: -1);
  if (std::abs(tk.getMomentum().eta())<1.2) {
    GlobalPoint loc_barrel(propagateToR(inner_point, inner_vec, charge, 523.));
    return loc_barrel;
  } 
  else if (tk.getMomentum().eta()>1.2) {
    GlobalPoint loc_endcap_pos(propagateToZ(inner_point, inner_vec, charge, 828));
    return loc_endcap_pos;
  } 
  else if (tk.getMomentum().eta()<-1.2){
    GlobalPoint loc_endcap_neg(propagateToZ(inner_point, inner_vec, charge, -828));
    return loc_endcap_neg;
  }
  return GlobalPoint();
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

FreeTrajectoryState 
DisplacedL1MuFilter::startingState(const reco::GenParticle &tk) const {
  if (!magfield_.isValid()) throw cms::Exception("NotInitialized") << "PropagateToMuon: You must call init(const edm::EventSetup &iSetup) before using this object.\n"; 
  return FreeTrajectoryState(  GlobalPoint(tk.vx(), tk.vy(), tk.vz()),
                               GlobalVector(tk.px(), tk.py(), tk.pz()),
                               int(tk.charge()),
                               magfield_.product());
}

FreeTrajectoryState 
DisplacedL1MuFilter::startingState(const TTTrack< Ref_PixelDigi_ > &tk) const {
  if (!magfield_.isValid()) throw cms::Exception("NotInitialized") << "PropagateToMuon: You must call init(const edm::EventSetup &iSetup) before using this object.\n"; 
  const double l1Tk_charge = tk.getRInv()>0? 1: -1;
  return FreeTrajectoryState(  tk.getPOCA(),
                               tk.getMomentum(),      
                               int(l1Tk_charge),
                               magfield_.product());
}

TrajectoryStateOnSurface
DisplacedL1MuFilter::extrapolate(const FreeTrajectoryState &start) const {
  if (!magfield_.isValid() || barrelCylinder_ == 0) {
    throw cms::Exception("NotInitialized") << "PropagateToMuon: You must call init(const edm::EventSetup &iSetup) before using this object.\n"; 
  }

  TrajectoryStateOnSurface final;
  if (start.momentum().mag() == 0) return final;
  double eta = start.momentum().eta();

  const Propagator * propagatorBarrel  = &*propagator_;
  const Propagator * propagatorEndcaps = &*propagator_;
  if (whichState_ != AtVertex) { 
    if (start.position().perp()    > barrelCylinder_->radius())         propagatorBarrel  = &*propagatorOpposite_;
    if (fabs(start.position().z()) > endcapDiskPos_[useMB2_?2:1]->position().z()) propagatorEndcaps = &*propagatorOpposite_;
  }
  if (cosmicPropagation_) {
    if (start.momentum().dot(GlobalVector(start.position().x(), start.position().y(), start.position().z())) < 0) {
      // must flip the propagations
      propagatorBarrel  = (propagatorBarrel  == &*propagator_ ? &*propagatorOpposite_ : &*propagator_);
      propagatorEndcaps = (propagatorEndcaps == &*propagator_ ? &*propagatorOpposite_ : &*propagator_);
    }
  }

  TrajectoryStateOnSurface tsos = propagatorBarrel->propagate(start, *barrelCylinder_);
  if (tsos.isValid()) {
    //    std::cout << "TSOS is valid" << std::endl;
    if (useSimpleGeometry_) {
      //std::cout << "  propagated to barrel, z = " << tsos.globalPosition().z() << ", bound = " << barrelHalfLength_ << std::endl;
      if (fabs(tsos.globalPosition().z()) <= barrelHalfLength_){
        //std::cout << "    acquired final position from TSOS" << std::endl;
        final = tsos;
      }
    } else {
      final = getBestDet(tsos, muonGeometry_->allDTLayers()[1]);
      //std::cout << "  obtained final position using DT layer geometry" << std::endl;
    }
  }
  // at this point we have a final state
  // if valid, return if
  // if not, check the endcap
  if (final.isValid()) {
    //std::cout << "Valid barrel TSOS" << std::endl;
    return final;
  }
 
  if (!final.isValid()) {
    //std::cout << "final position is invalid" << std::endl;
    for (int ie = (useMB2_ ? 2 : 1); ie >= 0; --ie) {
      tsos = propagatorEndcaps->propagate(start, (eta > 0 ? *endcapDiskPos_[ie] : *endcapDiskNeg_[ie]));
      if (tsos.isValid()) {
        //std::cout << "TSOS is invalid" << std::endl;
        if (useSimpleGeometry_) {
          float rho = tsos.globalPosition().perp();
          //std::cout << "  propagated to endcap " << ie << ", rho = " << rho << ", bounds [ " << endcapRadii_[ie].first << ", " << endcapRadii_[ie].second << "]" << std::endl;
          if ((rho >= endcapRadii_[ie].first) && (rho <= endcapRadii_[ie].second)) {
            //std::cout << "    acquired final position from TSOS" << std::endl;
            final = tsos;
          }
        } else {
          final = getBestDet(tsos, (eta > 0 ? muonGeometry_->forwardCSCLayers()[ie] : muonGeometry_->backwardCSCLayers()[ie]));
        }
      } 
      // else 
      //   std::cout << "  failed to propagated to endcap " << ie  << std::endl;
      if (final.isValid()) {
        //std::cout << "Valid endcap TSOS" <<std::endl;
        break;
      }
      if (ie == 2 && !fallbackToME1_) break;
    }
  }
  return final;
}

TrajectoryStateOnSurface 
DisplacedL1MuFilter::getBestDet(const TrajectoryStateOnSurface &tsos, const DetLayer *layer) const {
  TrajectoryStateOnSurface ret; // start as null
  Chi2MeasurementEstimator estimator(1e10, 3.); // require compatibility at 3 sigma
  std::vector<GeometricSearchDet::DetWithState> dets = layer->compatibleDets(tsos, *propagatorAny_, estimator);
  if (!dets.empty()) {
    ret = dets.front().second;
  }
  return ret;
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

  event_tree_->Branch("genGd_vLx", event_.genGd_vLx, "genGd_vLx[2]/F");
  event_tree_->Branch("genGd_vLy", event_.genGd_vLy, "genGd_vLy[2]/F");
  event_tree_->Branch("genGd_vLz", event_.genGd_vLz, "genGd_vLz[2]/F");
  event_tree_->Branch("genGd_lxy", event_.genGd_lxy, "genGd_lxy[2]/F");
  event_tree_->Branch("genGd_l", event_.genGd_l, "genGd_l[2]/F");
  event_tree_->Branch("genGdMu_dxy_max", event_.genGdMu_dxy_max, "genGdMu_dxy_max[2]/F");

  // Dimuons
  event_tree_->Branch("genGdMu_p", event_.genGdMu_p, "genGdMu_p[2][2]/F");
  event_tree_->Branch("genGdMu_pt", event_.genGdMu_pt, "genGdMu_pt[2][2]/F");
  event_tree_->Branch("genGdMu_px", event_.genGdMu_px, "genGdMu_px[2][2]/F");
  event_tree_->Branch("genGdMu_py", event_.genGdMu_py, "genGdMu_py[2][2]/F");
  event_tree_->Branch("genGdMu_pz", event_.genGdMu_pz, "genGdMu_pz[2][2]/F");
  event_tree_->Branch("genGdMu_eta", event_.genGdMu_eta, "genGdMu_eta[2][2]/F");
  event_tree_->Branch("genGdMu_phi", event_.genGdMu_phi, "genGdMu_phi[2][2]/F");

  event_tree_->Branch("genGdMu_eta_corr", event_.genGdMu_eta_corr, "genGdMu_eta_corr[2][2]/F");
  event_tree_->Branch("genGdMu_phi_corr", event_.genGdMu_phi_corr, "genGdMu_phi_corr[2][2]/F");
  event_tree_->Branch("genGdMu_deta_corr", event_.genGdMu_deta_corr, "genGdMu_deta_corr[2][2]/F");
  event_tree_->Branch("genGdMu_dphi_corr", event_.genGdMu_dphi_corr, "genGdMu_dphi_corr[2][2]/F");
  event_tree_->Branch("genGdMu_dR_corr", event_.genGdMu_dR_corr, "genGdMu_dR_corr[2][2]/F");

  event_tree_->Branch("genGdMu_eta_prop", event_.genGdMu_eta_prop, "genGdMu_eta_prop[2][2]/F");
  event_tree_->Branch("genGdMu_phi_prop", event_.genGdMu_phi_prop, "genGdMu_phi_prop[2][2]/F");
  event_tree_->Branch("genGdMu_deta_prop", event_.genGdMu_deta_prop, "genGdMu_deta_prop[2][2]/F");
  event_tree_->Branch("genGdMu_dphi_prop", event_.genGdMu_dphi_prop, "genGdMu_dphi_prop[2][2]/F");
  event_tree_->Branch("genGdMu_dR_prop", event_.genGdMu_dR_prop, "genGdMu_dR_prop[2][2]/F");

  event_tree_->Branch("genGdMu_vx", event_.genGdMu_vx, "genGdMu_vx[2][2]/F");
  event_tree_->Branch("genGdMu_vy", event_.genGdMu_vy, "genGdMu_vy[2][2]/F");
  event_tree_->Branch("genGdMu_vz", event_.genGdMu_vz, "genGdMu_vz[2][2]/F");
  event_tree_->Branch("genGdMu_dxy", event_.genGdMu_dxy, "genGdMu_dxy[2][2]/F");
  
  event_tree_->Branch("genGdMu_L1Tk_dR_prop", event_.genGdMu_L1Tk_dR_prop, "genGdMu_L1Tk_dR_prop[2][2]/F");
  event_tree_->Branch("genGdMu_L1Tk_index_prop", event_.genGdMu_L1Tk_index_prop, "genGdMu_L1Tk_index_prop[2][2]/F");
  event_tree_->Branch("genGdMu_L1Tk_dR_corr", event_.genGdMu_L1Tk_dR_corr, "genGdMu_L1Tk_dR_corr[2][2]/F");
  event_tree_->Branch("genGdMu_L1Tk_index_corr", event_.genGdMu_L1Tk_index_corr, "genGdMu_L1Tk_index_corr[2][2]/F");

  event_tree_->Branch("genGd0Gd1_dR",   &event_.genGd0Gd1_dR,   "genGd0Gd1_dR/F");
  event_tree_->Branch("genGd_genMuMu_dEta",   event_.genGd_genMuMu_dEta,   "genGd_genMuMu_dEta[2]/F");
  event_tree_->Branch("genGd_genMuMu_dPhi",   event_.genGd_genMuMu_dPhi,   "genGd_genMuMu_dPhi[2]/F");
  event_tree_->Branch("genGd_genMuMu_dR",   event_.genGd_genMuMu_dR,   "genGd_genMuMu_dR[2]/F");
  event_tree_->Branch("genGd_genMu_dEta",   event_.genGd_genMu_dEta,   "genGd_genMu_dEta[2][2]/F");
  event_tree_->Branch("genGd_genMu_dPhi",   event_.genGd_genMu_dPhi,   "genGd_genMu_dPhi[2][2]/F");
  event_tree_->Branch("genGd_genMu_dR",   event_.genGd_genMu_dR,   "genGd_genMu_dR[2][2]/F");

  event_tree_->Branch("nL1Mu", &event_.nL1Mu);
  event_tree_->Branch("nL1Tk", &event_.nL1Tk);

  event_tree_->Branch("L1Mu_pt",event_.L1Mu_pt,"L1Mu_pt[nL1Mu]/F");
  event_tree_->Branch("L1Mu_eta", event_.L1Mu_eta,"L1Mu_eta[nL1Mu]/F");
  event_tree_->Branch("L1Mu_phi", event_.L1Mu_phi,"L1Mu_phi[nL1Mu]/F");
  event_tree_->Branch("L1Mu_bx", event_.L1Mu_bx,"L1Mu_bx[nL1Mu]/I");
  event_tree_->Branch("L1Mu_charge", event_.L1Mu_charge,"L1Mu_charge[nL1Mu]/I");
  event_tree_->Branch("L1Mu_quality", event_.L1Mu_quality,"L1Mu_quality[nL1Mu]/I");
  event_tree_->Branch("L1Mu_L1Tk_dR_corr", event_.L1Mu_L1Tk_dR_corr,"L1Mu_L1Tk_dR_corr[nL1Mu]/F");
  event_tree_->Branch("L1Mu_L1Tk_pt_corr", event_.L1Mu_L1Tk_pt_corr,"L1Mu_L1Tk_pt_corr[nL1Mu]/F");
  event_tree_->Branch("L1Mu_L1Tk_dR_prop", event_.L1Mu_L1Tk_dR_prop,"L1Mu_L1Tk_dR_prop[nL1Mu]/F");
  event_tree_->Branch("L1Mu_L1Tk_dR_prop_true", event_.L1Mu_L1Tk_dR_prop_true,"L1Mu_L1Tk_dR_prop_true[nL1Mu]/F");
  event_tree_->Branch("L1Mu_L1Tk_pt_prop", event_.L1Mu_L1Tk_pt_prop,"L1Mu_L1Tk_pt_prop[nL1Mu]/F");

  event_tree_->Branch("L1Tk_pt",event_.L1Tk_pt,"L1Tk_pt[nL1Tk]/F");
  event_tree_->Branch("L1Tk_eta", event_.L1Tk_eta,"L1Tk_eta[nL1Tk]/F");
  event_tree_->Branch("L1Tk_phi", event_.L1Tk_phi,"L1Tk_phi[nL1Tk]/F");

  event_tree_->Branch("L1Tk_eta_prop", event_.L1Tk_eta_prop,"L1Tk_eta_prop[nL1Tk]/F");
  event_tree_->Branch("L1Tk_phi_prop", event_.L1Tk_phi_prop,"L1Tk_phi_prop[nL1Tk]/F");
  event_tree_->Branch("L1Tk_deta_prop", event_.L1Tk_deta_prop,"L1Tk_deta_prop[nL1Tk]/F");
  event_tree_->Branch("L1Tk_dphi_prop", event_.L1Tk_dphi_prop,"L1Tk_dphi_prop[nL1Tk]/F");
  event_tree_->Branch("L1Tk_dR_prop", event_.L1Tk_dR_prop,"L1Tk_dR_prop[nL1Tk]/F");

  event_tree_->Branch("L1Tk_eta_corr", event_.L1Tk_eta_corr,"L1Tk_eta_corr[nL1Tk]/F");
  event_tree_->Branch("L1Tk_phi_corr", event_.L1Tk_phi_corr,"L1Tk_phi_corr[nL1Tk]/F");
  event_tree_->Branch("L1Tk_deta_corr", event_.L1Tk_deta_corr,"L1Tk_deta_corr[nL1Tk]/F");
  event_tree_->Branch("L1Tk_dphi_corr", event_.L1Tk_dphi_corr,"L1Tk_dphi_corr[nL1Tk]/F");
  event_tree_->Branch("L1Tk_dR_corr", event_.L1Tk_dR_corr,"L1Tk_dR_corr[nL1Tk]/F");

  event_tree_->Branch("genGdMu_L1Mu_dR",    event_.genGdMu_L1Mu_dR,    "genGdMu_L1Mu_dR[2][2]/F");
  event_tree_->Branch("genGdMu_L1Mu_dR_corr",    event_.genGdMu_L1Mu_dR_corr,    "genGdMu_L1Mu_dR_corr[2][2]/F");
  event_tree_->Branch("genGdMu_L1Mu_index_corr", event_.genGdMu_L1Mu_index_corr, "genGdMu_L1Mu_index_corr[2][2]/I");
  event_tree_->Branch("genGdMu_L1Mu_dR_prop",    event_.genGdMu_L1Mu_dR_prop,    "genGdMu_L1Mu_dR_prop[2][2]/F");
  event_tree_->Branch("genGdMu_L1Mu_index_prop", event_.genGdMu_L1Mu_index_prop, "genGdMu_L1Mu_index_prop[2][2]/I");

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

  event_tree_->Branch("nDTTF", &event_.nDTTF);
  event_tree_->Branch("L1Mu_DTTF_index", event_.L1Mu_DTTF_index,"L1Mu_DTTF_index[nL1Mu]/I");

  event_tree_->Branch("DTTF_pt", event_.DTTF_pt,"DTTF_pt[nDTTF]/F");
  event_tree_->Branch("DTTF_eta", event_.DTTF_eta,"DTTF_eta[nDTTF]/F");
  event_tree_->Branch("DTTF_phi", event_.DTTF_phi,"DTTF_phi[nDTTF]/F");
  event_tree_->Branch("DTTF_bx", event_.DTTF_bx,"DTTF_bx[nDTTF]/F");
  event_tree_->Branch("DTTF_nStubs", event_.DTTF_nStubs,"DTTF_nStubs[nDTTF]/F");

  event_tree_->Branch("DTTF_phi1", event_.DTTF_phi1,"DTTF_phi1[nDTTF]/F");
  event_tree_->Branch("DTTF_phib1", event_.DTTF_phib1,"DTTF_phib1[nDTTF]/F");
  event_tree_->Branch("DTTF_quality1", event_.DTTF_quality1,"DTTF_quality1[nDTTF]/F");
  event_tree_->Branch("DTTF_bx1", event_.DTTF_bx1,"DTTF_bx1[nDTTF]/F");
  event_tree_->Branch("DTTF_wh1", event_.DTTF_wh1,"DTTF_wh1[nDTTF]/F");
  event_tree_->Branch("DTTF_se1", event_.DTTF_se1,"DTTF_se1[nDTTF]/F");
  event_tree_->Branch("DTTF_st1", event_.DTTF_st1,"DTTF_st1[nDTTF]/F");

  event_tree_->Branch("DTTF_phi2", event_.DTTF_phi2,"DTTF_phi2[nDTTF]/F");
  event_tree_->Branch("DTTF_phib2", event_.DTTF_phib2,"DTTF_phib2[nDTTF]/F");
  event_tree_->Branch("DTTF_quality2", event_.DTTF_quality2,"DTTF_quality2[nDTTF]/F");
  event_tree_->Branch("DTTF_bx2", event_.DTTF_bx2,"DTTF_bx2[nDTTF]/F");
  event_tree_->Branch("DTTF_wh2", event_.DTTF_wh2,"DTTF_wh2[nDTTF]/F");
  event_tree_->Branch("DTTF_se2", event_.DTTF_se2,"DTTF_se2[nDTTF]/F");
  event_tree_->Branch("DTTF_st2", event_.DTTF_st2,"DTTF_st2[nDTTF]/F");

  event_tree_->Branch("DTTF_phi3", event_.DTTF_phi3,"DTTF_phi3[nDTTF]/F");
  event_tree_->Branch("DTTF_phib3", event_.DTTF_phib3,"DTTF_phib3[nDTTF]/F");
  event_tree_->Branch("DTTF_quality3", event_.DTTF_quality3,"DTTF_quality3[nDTTF]/F");
  event_tree_->Branch("DTTF_bx3", event_.DTTF_bx3,"DTTF_bx3[nDTTF]/F");
  event_tree_->Branch("DTTF_wh3", event_.DTTF_wh3,"DTTF_wh3[nDTTF]/F");
  event_tree_->Branch("DTTF_se3", event_.DTTF_se3,"DTTF_se3[nDTTF]/F");
  event_tree_->Branch("DTTF_st3", event_.DTTF_st3,"DTTF_st3[nDTTF]/F");

  event_tree_->Branch("DTTF_phi4", event_.DTTF_phi4,"DTTF_phi4[nDTTF]/F");
  event_tree_->Branch("DTTF_phib4", event_.DTTF_phib4,"DTTF_phib4[nDTTF]/F");
  event_tree_->Branch("DTTF_quality4", event_.DTTF_quality4,"DTTF_quality4[nDTTF]/F");
  event_tree_->Branch("DTTF_bx4", event_.DTTF_bx4,"DTTF_bx4[nDTTF]/F");
  event_tree_->Branch("DTTF_wh4", event_.DTTF_wh4,"DTTF_wh4[nDTTF]/F");
  event_tree_->Branch("DTTF_se4", event_.DTTF_se4,"DTTF_se4[nDTTF]/F");
  event_tree_->Branch("DTTF_st4", event_.DTTF_st4,"DTTF_st4[nDTTF]/F");


  event_tree_->Branch("nCSCTF", &event_.nCSCTF);
  event_tree_->Branch("L1Mu_CSCTF_index", event_.L1Mu_CSCTF_index,"L1Mu_CSCTF_index[nL1Mu]/I");

  event_tree_->Branch("CSCTF_pt", event_.CSCTF_pt,"CSCTF_pt[nCSCTF]/F");
  event_tree_->Branch("CSCTF_eta", event_.CSCTF_eta,"CSCTF_eta[nCSCTF]/F");
  event_tree_->Branch("CSCTF_phi", event_.CSCTF_phi,"CSCTF_phi[nCSCTF]/F");
  event_tree_->Branch("CSCTF_bx", event_.CSCTF_bx,"CSCTF_bx[nCSCTF]/F");
  event_tree_->Branch("CSCTF_nStubs", event_.CSCTF_nStubs,"CSCTF_nStubs[nCSCTF]/F");

    // event_.CSCTF_st1[i] = 99; 
    // event_.CSCTF_ri1[i] = 99; 
    // event_.CSCTF_ch1[i] = 99; 
    // event_.CSCTF_en1[i] = 99;;
    // event_.CSCTF_trk1[i] = 99; 
    // event_.CSCTF_quality1[i] = 99; 
    // event_.CSCTF_wg1[i] = 99; 
    // event_.CSCTF_hs1[i] = 99;; 
    // event_.CSCTF_pat1[i] = 99; 
    // event_.CSCTF_bend1[i] = 99; 
    // event_.CSCTF_bx1[i] = 99; 
    // event_.CSCTF_clctpat1[i] = 99;;

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

    event_.genGd_vLx[i] = -99;
    event_.genGd_vLy[i] = -99;
    event_.genGd_vLz[i] = -99;
    event_.genGd_lxy[i] = -99;
    event_.genGd_l[i] = -99;
    event_.genGdMu_dxy_max[i] = -99;
 
    event_.genGd_genMuMu_dEta[i] = 99;
    event_.genGd_genMuMu_dPhi[i] = 99;
    event_.genGd_genMuMu_dR[i] = 99;

  }

  event_.genGd0Gd1_dR = -99;
    
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

      event_.genGdMu_eta_corr[i][j] = -99;
      event_.genGdMu_phi_corr[i][j] = -99;
      event_.genGdMu_deta_corr[i][j] = 99;
      event_.genGdMu_dphi_corr[i][j] = 99;
      event_.genGdMu_dR_corr[i][j] = 99;
      
      event_.genGdMu_eta_prop[i][j] = -99;
      event_.genGdMu_phi_prop[i][j] = -99;
      event_.genGdMu_deta_prop[i][j] = 99;
      event_.genGdMu_dphi_prop[i][j] = 99;
      event_.genGdMu_dR_prop[i][j] = 99;

      event_.genGdMu_vx[i][j] = -99;;
      event_.genGdMu_vy[i][j] = -99;;
      event_.genGdMu_vz[i][j] = -99;;
      event_.genGdMu_dxy[i][j] = -99;;
      event_.genGdMu_L1Tk_dR_prop[i][j] = 99;
      event_.genGdMu_L1Tk_index_prop[i][j] = -99;
      event_.genGdMu_L1Tk_dR_corr[i][j] = 99;
      event_.genGdMu_L1Tk_index_corr[i][j] = -99;

      event_.genGdMu_L1Mu_dR[i][j] = 99.;
      event_.genGdMu_L1Mu_dR_corr[i][j] = 99.;
      event_.genGdMu_L1Mu_index_corr[i][j] = 99;
      event_.genGdMu_L1Mu_dR_prop[i][j] = 99.;
      event_.genGdMu_L1Mu_index_prop[i][j] = 99;

      event_.genGd_genMu_dEta[i][j] = 99;
      event_.genGd_genMu_dPhi[i][j] = 99;
      event_.genGd_genMu_dR[i][j] = 99;
    }
  }
  event_.nL1Mu = 0;
  event_.nL1Tk = 0;


  for (int i=0; i<kMaxL1Mu; ++i){
    event_.L1Mu_pt[i] = -99;
    event_.L1Mu_eta[i] = -99;
    event_.L1Mu_phi[i] = -99;
    event_.L1Mu_charge[i] = -99;
    event_.L1Mu_bx[i] = -99;
    event_.L1Mu_quality[i] = -99;
    event_.L1Mu_L1Tk_dR_corr[i] = 999.;
    event_.L1Mu_L1Tk_pt_corr[i] = -99.;
    event_.L1Mu_L1Tk_dR_prop[i] = 999.;
    event_.L1Mu_L1Tk_dR_prop_true[i] = 999.;
    event_.L1Mu_L1Tk_pt_prop[i] = -99.;
    event_.L1Mu_DTTF_index[i] = -1;
    event_.L1Mu_CSCTF_index[i] = -1;
  }

  for (int i=0; i<kMaxL1Tk; ++i){
    event_.L1Tk_pt[i] = -99;
    event_.L1Tk_eta[i] = -99; 
    event_.L1Tk_phi[i] = -99;

    event_.L1Tk_eta_prop[i] = -99;
    event_.L1Tk_phi_prop[i] = -99;
    event_.L1Tk_deta_prop[i] = -99;
    event_.L1Tk_dphi_prop[i] = -99;
    event_.L1Tk_dR_prop[i] = -99;

    event_.L1Tk_eta_corr[i] = -99;
    event_.L1Tk_phi_corr[i] = -99;
    event_.L1Tk_deta_corr[i] = -99;
    event_.L1Tk_dphi_corr[i]  = -99;
    event_.L1Tk_dR_corr[i] = -99;    
  }

  event_.has_sim = -99;
  event_.pt_sim = -99;
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


  event_.nDTTF = 0;

  for (int i=0; i<kMaxDTTF; ++i){
    event_.DTTF_pt[i] = 99;
    event_.DTTF_eta[i] = 99;
    event_.DTTF_phi[i] = 99;
    event_.DTTF_nStubs[i] = 99;

    event_.DTTF_phi1[i] = 99;
    event_.DTTF_phib1[i] = 99;
    event_.DTTF_quality1[i] = 99;
    event_.DTTF_bx1[i] = 99;
    event_.DTTF_wh1[i] = 99;
    event_.DTTF_se1[i] = 99;
    event_.DTTF_st1[i] = 99;

    event_.DTTF_phi2[i] = 99;
    event_.DTTF_phib2[i] = 99;
    event_.DTTF_quality2[i] = 99;
    event_.DTTF_bx2[i] = 99;
    event_.DTTF_wh2[i] = 99;
    event_.DTTF_se2[i] = 99;
    event_.DTTF_st2[i] = 99;

    event_.DTTF_phi3[i] = 99;
    event_.DTTF_phib3[i] = 99;
    event_.DTTF_quality3[i] = 99;
    event_.DTTF_bx3[i] = 99;
    event_.DTTF_wh3[i] = 99;
    event_.DTTF_se3[i] = 99;
    event_.DTTF_st3[i] = 99;

    event_.DTTF_phi4[i] = 99;
    event_.DTTF_phib4[i] = 99;
    event_.DTTF_quality4[i] = 99;
    event_.DTTF_bx4[i] = 99;
    event_.DTTF_wh4[i] = 99;
    event_.DTTF_se4[i] = 99;
    event_.DTTF_st4[i] = 99;
  }


  event_.nCSCTF = 0;

  for (int i=0; i<kMaxCSCTF; ++i){
    event_.CSCTF_pt[i] = 99;
    event_.CSCTF_eta[i] = 99;
    event_.CSCTF_phi[i] = 99;
    event_.CSCTF_nStubs[i] = 99;

    event_.CSCTF_st1[i] = 99; 
    event_.CSCTF_ri1[i] = 99; 
    event_.CSCTF_ch1[i] = 99; 
    event_.CSCTF_en1[i] = 99;;
    event_.CSCTF_trk1[i] = 99; 
    event_.CSCTF_quality1[i] = 99; 
    event_.CSCTF_wg1[i] = 99; 
    event_.CSCTF_hs1[i] = 99;; 
    event_.CSCTF_pat1[i] = 99; 
    event_.CSCTF_bend1[i] = 99; 
    event_.CSCTF_bx1[i] = 99; 
    event_.CSCTF_clctpat1[i] = 99;;

    event_.CSCTF_st2[i] = 99; 
    event_.CSCTF_ri2[i] = 99; 
    event_.CSCTF_ch2[i] = 99; 
    event_.CSCTF_en2[i] = 99;;
    event_.CSCTF_trk2[i] = 99; 
    event_.CSCTF_quality2[i] = 99; 
    event_.CSCTF_wg2[i] = 99; 
    event_.CSCTF_hs2[i] = 99;; 
    event_.CSCTF_pat2[i] = 99; 
    event_.CSCTF_bend2[i] = 99; 
    event_.CSCTF_bx2[i] = 99; 
    event_.CSCTF_clctpat2[i] = 99;;

    event_.CSCTF_st3[i] = 99; 
    event_.CSCTF_ri3[i] = 99; 
    event_.CSCTF_ch3[i] = 99; 
    event_.CSCTF_en3[i] = 99;;
    event_.CSCTF_trk3[i] = 99; 
    event_.CSCTF_quality3[i] = 99; 
    event_.CSCTF_wg3[i] = 99; 
    event_.CSCTF_hs3[i] = 99;; 
    event_.CSCTF_pat3[i] = 99; 
    event_.CSCTF_bend3[i] = 99; 
    event_.CSCTF_bx3[i] = 99; 
    event_.CSCTF_clctpat3[i] = 99;;

    event_.CSCTF_st4[i] = 99; 
    event_.CSCTF_ri4[i] = 99; 
    event_.CSCTF_ch4[i] = 99; 
    event_.CSCTF_en4[i] = 99;;
    event_.CSCTF_trk4[i] = 99; 
    event_.CSCTF_quality4[i] = 99; 
    event_.CSCTF_wg4[i] = 99; 
    event_.CSCTF_hs4[i] = 99;; 
    event_.CSCTF_pat4[i] = 99; 
    event_.CSCTF_bend4[i] = 99; 
    event_.CSCTF_bx4[i] = 99; 
    event_.CSCTF_clctpat4[i] = 99;;
  }
}

//define this as a plug-in
DEFINE_FWK_MODULE(DisplacedL1MuFilter);

//  LocalWords:  kMaxCSCTF
