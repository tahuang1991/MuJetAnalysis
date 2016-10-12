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

 1;95;0c  To estimate the rate reduction Sven will take a MinBias sample from Slava and build a 
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
#include <iostream>
#include <iomanip>
#include <ctime>
#include <sstream>

#include "TTree.h"
#include "TCanvas.h"
#include "TFile.h"
#include "TGraph.h"
#include "TF1.h"
#include "TGraphErrors.h"
#include "TDatime.h"
#include "TTimeStamp.h"

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
#include "DataFormats/RPCDigi/interface/RPCDigiL1Linkfwd.h"
#include "DataFormats/RPCDigi/interface/RPCDigiL1Link.h"
#include "DataFormats/MuonDetId/interface/RPCDetId.h"
#include "Geometry/RPCGeometry/interface/RPCGeometry.h"
#include "DataFormats/MuonDetId/interface/CSCDetId.h"
#include "Geometry/CSCGeometry/interface/CSCGeometry.h"
#include "L1Trigger/CSCCommonTrigger/interface/CSCPatternLUT.h"

#include "CondFormats/L1TObjects/interface/L1MuTriggerScales.h"
#include "CondFormats/L1TObjects/interface/L1MuTriggerPtScale.h"
#include "CondFormats/DataRecord/interface/L1MuTriggerPtScaleRcd.h"
#include "CondFormats/DataRecord/interface/L1MuTriggerScalesRcd.h"
#include <L1Trigger/CSCCommonTrigger/interface/CSCConstants.h>
#include <L1Trigger/CSCTrackFinder/interface/CSCTFPtLUT.h>
#include "GEMCode/GEMValidation/interface/SimTrackMatchManager.h"
#include "MuJetAnalysis/DisplacedL1MuFilter/plugins/CSCStubPatterns.h"

#include "DataFormats/CSCDigi/interface/CSCComparatorDigiCollection.h"
#include "DataFormats/CSCDigi/interface/CSCWireDigiCollection.h"
#include "DataFormats/CSCDigi/interface/CSCALCTDigiCollection.h"
#include "DataFormats/CSCDigi/interface/CSCCLCTDigiCollection.h"
#include "DataFormats/CSCDigi/interface/CSCCorrelatedLCTDigiCollection.h"

#include "DataFormats/GEMDigi/interface/GEMDigiCollection.h"
#include "DataFormats/GEMDigi/interface/GEMCSCPadDigiCollection.h"
#include "DataFormats/GEMDigi/interface/GEMCSCCoPadDigiCollection.h"
//
// class declaration
//

const Int_t kMaxL1Mu = 50;
const Int_t kMaxDTTF = 50;
const Int_t kMaxCSCTF = 50;
const Int_t kMaxRPCb = 50;
const Int_t kMaxRPCf = 50;
const Int_t kMaxGEM = 50;
const Int_t kMaxSIM = 50;
const Int_t kMaxL1Tk = 500;
const int nGlu = 2;
const int nGd = 2;
const int nGdMu = 2;

typedef std::vector<CSCComparatorDigi> CSCComparatorDigiContainer;
typedef std::vector<std::pair<CSCDetId, CSCComparatorDigiContainer> > CSCComparatorDigiContainerIds;

typedef std::pair<CSCDetId, CSCCorrelatedLCTDigi> CSCCorrelatedLCTDigiId;
typedef std::vector<CSCCorrelatedLCTDigi> CSCCorrelatedLCTDigiContainer;
typedef std::pair<CSCDetId, CSCCorrelatedLCTDigiContainer> CSCCorrelatedLCTDigiContainerId;
typedef std::vector<std::pair<CSCDetId, CSCCorrelatedLCTDigiContainer> > CSCCorrelatedLCTDigiContainerIds;

typedef std::pair<GEMDetId, GEMCSCCoPadDigi> GEMCSCCoPadDigiId;
typedef std::vector<GEMCSCCoPadDigi> GEMCSCCoPadDigiContainer;
typedef std::pair<GEMDetId, GEMCSCCoPadDigiContainer> GEMCSCCoPadDigiContainerId;
typedef std::vector<std::pair<GEMDetId, GEMCSCCoPadDigiContainer> > GEMCSCCoPadDigiContainerIds;

typedef std::pair<GEMDetId, GEMCSCPadDigi> GEMCSCPadDigiId;
typedef std::vector<GEMCSCPadDigi> GEMCSCPadDigiContainer;
typedef std::pair<GEMDetId, GEMCSCPadDigiContainer> GEMCSCPadDigiContainerId;
typedef std::vector<std::pair<GEMDetId, GEMCSCPadDigiContainer> > GEMCSCPadDigiContainerIds;

typedef std::vector<std::pair<L1MuDTTrack,std::vector<L1MuDTTrackSegPhi> > > L1MuDTTrackCollection;

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
  Float_t genGdMu_etav_prop_GE11[2][2];
  Float_t genGdMu_phiv_prop_GE11[2][2];
  Float_t genGdMu_etav_prop_GE21[2][2];
  Float_t genGdMu_phiv_prop_GE21[2][2];

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

  Int_t genGdMu_SIM_index[2][2];
  Float_t genGdMu_SIM_dR[2][2];
  Int_t has_sim;
  Float_t pt_sim[kMaxSIM], eta_sim[kMaxSIM], phi_sim[kMaxSIM], charge_sim[kMaxSIM];
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
  Float_t DTTF_pt[kMaxDTTF], DTTF_eta[kMaxDTTF], DTTF_phi[kMaxDTTF];
  Int_t DTTF_bx[kMaxDTTF], DTTF_nStubs[kMaxDTTF], DTTF_quality[kMaxDTTF];
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
  Float_t CSCTF_pt[kMaxCSCTF], CSCTF_eta[kMaxCSCTF], CSCTF_phi[kMaxCSCTF];
  Int_t CSCTF_bx[kMaxCSCTF], CSCTF_nStubs[kMaxCSCTF], CSCTF_quality[kMaxCSCTF];

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
  
  Int_t CSCTF_id1[kMaxCSCTF], CSCTF_id2[kMaxCSCTF], CSCTF_id3[kMaxCSCTF], CSCTF_id4[kMaxCSCTF];

  Int_t CSCTF_val1[kMaxCSCTF], CSCTF_val2[kMaxCSCTF], CSCTF_val3[kMaxCSCTF], CSCTF_val4[kMaxCSCTF];
  Float_t CSCTF_phi1[kMaxCSCTF], CSCTF_phi2[kMaxCSCTF], CSCTF_phi3[kMaxCSCTF], CSCTF_phi4[kMaxCSCTF];
  Float_t CSCTF_eta1[kMaxCSCTF], CSCTF_eta2[kMaxCSCTF], CSCTF_eta3[kMaxCSCTF], CSCTF_eta4[kMaxCSCTF];
  Float_t CSCTF_phib1[kMaxCSCTF], CSCTF_phib2[kMaxCSCTF], CSCTF_phib3[kMaxCSCTF], CSCTF_phib4[kMaxCSCTF];

  Float_t CSCTF_gemdphi1[kMaxCSCTF], CSCTF_gemdphi2[kMaxCSCTF];
  Float_t CSCTF_R1[kMaxCSCTF], CSCTF_R2[kMaxCSCTF], CSCTF_R3[kMaxCSCTF], CSCTF_R4[kMaxCSCTF];
  Float_t CSCTF_x1[kMaxCSCTF], CSCTF_x2[kMaxCSCTF], CSCTF_x3[kMaxCSCTF], CSCTF_x4[kMaxCSCTF];
  Float_t CSCTF_y1[kMaxCSCTF], CSCTF_y2[kMaxCSCTF], CSCTF_y3[kMaxCSCTF], CSCTF_y4[kMaxCSCTF];
  Float_t CSCTF_z1[kMaxCSCTF], CSCTF_z2[kMaxCSCTF], CSCTF_z3[kMaxCSCTF], CSCTF_z4[kMaxCSCTF];
  
  // recovered stubs using the SIM information (stubs not used in track building...)
  Int_t CSCTF_rec_ch1[kMaxCSCTF], CSCTF_rec_ch2[kMaxCSCTF], CSCTF_rec_ch3[kMaxCSCTF], CSCTF_rec_ch4[kMaxCSCTF];
  Float_t CSCTF_rec_phi1[kMaxCSCTF], CSCTF_rec_phi2[kMaxCSCTF], CSCTF_rec_phi3[kMaxCSCTF], CSCTF_rec_phi4[kMaxCSCTF];
  Float_t CSCTF_rec_eta1[kMaxCSCTF], CSCTF_rec_eta2[kMaxCSCTF], CSCTF_rec_eta3[kMaxCSCTF], CSCTF_rec_eta4[kMaxCSCTF];
  Float_t CSCTF_rec_phib1[kMaxCSCTF], CSCTF_rec_phib2[kMaxCSCTF], CSCTF_rec_phib3[kMaxCSCTF], CSCTF_rec_phib4[kMaxCSCTF];
  Float_t CSCTF_rec_R1[kMaxCSCTF], CSCTF_rec_R2[kMaxCSCTF], CSCTF_rec_R3[kMaxCSCTF], CSCTF_rec_R4[kMaxCSCTF];
  Float_t CSCTF_rec_x1[kMaxCSCTF], CSCTF_rec_x2[kMaxCSCTF], CSCTF_rec_x3[kMaxCSCTF], CSCTF_rec_x4[kMaxCSCTF];
  Float_t CSCTF_rec_y1[kMaxCSCTF], CSCTF_rec_y2[kMaxCSCTF], CSCTF_rec_y3[kMaxCSCTF], CSCTF_rec_y4[kMaxCSCTF];
  Float_t CSCTF_rec_z1[kMaxCSCTF], CSCTF_rec_z2[kMaxCSCTF], CSCTF_rec_z3[kMaxCSCTF], CSCTF_rec_z4[kMaxCSCTF];

  // fitted positions -- at key layer
  Float_t CSCTF_fit_phi1[kMaxCSCTF], CSCTF_fit_phi2[kMaxCSCTF], CSCTF_fit_phi3[kMaxCSCTF], CSCTF_fit_phi4[kMaxCSCTF];
  Float_t CSCTF_fit_R1[kMaxCSCTF], CSCTF_fit_R2[kMaxCSCTF], CSCTF_fit_R3[kMaxCSCTF], CSCTF_fit_R4[kMaxCSCTF];
  Float_t CSCTF_fit_x1[kMaxCSCTF], CSCTF_fit_x2[kMaxCSCTF], CSCTF_fit_x3[kMaxCSCTF], CSCTF_fit_x4[kMaxCSCTF];
  Float_t CSCTF_fit_y1[kMaxCSCTF], CSCTF_fit_y2[kMaxCSCTF], CSCTF_fit_y3[kMaxCSCTF], CSCTF_fit_y4[kMaxCSCTF];
  Float_t CSCTF_fit_z1[kMaxCSCTF], CSCTF_fit_z2[kMaxCSCTF], CSCTF_fit_z3[kMaxCSCTF], CSCTF_fit_z4[kMaxCSCTF];

  //fitted directions
  Float_t CSCTF_fit_dphi1[kMaxCSCTF], CSCTF_fit_dphi2[kMaxCSCTF], CSCTF_fit_dphi3[kMaxCSCTF], CSCTF_fit_dphi4[kMaxCSCTF];

  // sim positions - at key layer
  Float_t CSCTF_sim_phi1[kMaxCSCTF], CSCTF_sim_phi2[kMaxCSCTF], CSCTF_sim_phi3[kMaxCSCTF], CSCTF_sim_phi4[kMaxCSCTF];
  Float_t CSCTF_sim_eta1[kMaxCSCTF], CSCTF_sim_eta2[kMaxCSCTF], CSCTF_sim_eta3[kMaxCSCTF], CSCTF_sim_eta4[kMaxCSCTF];
  Float_t CSCTF_sim_R1[kMaxCSCTF], CSCTF_sim_R2[kMaxCSCTF], CSCTF_sim_R3[kMaxCSCTF], CSCTF_sim_R4[kMaxCSCTF];
  Float_t CSCTF_sim_x1[kMaxCSCTF], CSCTF_sim_x2[kMaxCSCTF], CSCTF_sim_x3[kMaxCSCTF], CSCTF_sim_x4[kMaxCSCTF];
  Float_t CSCTF_sim_y1[kMaxCSCTF], CSCTF_sim_y2[kMaxCSCTF], CSCTF_sim_y3[kMaxCSCTF], CSCTF_sim_y4[kMaxCSCTF];
  Float_t CSCTF_sim_z1[kMaxCSCTF], CSCTF_sim_z2[kMaxCSCTF], CSCTF_sim_z3[kMaxCSCTF], CSCTF_sim_z4[kMaxCSCTF];

  Float_t CSCTF_fitline_x1[kMaxCSCTF], CSCTF_fitline_x2[kMaxCSCTF], CSCTF_fitline_x3[kMaxCSCTF], CSCTF_fitline_x4[kMaxCSCTF];
  Float_t CSCTF_fitline_y1[kMaxCSCTF], CSCTF_fitline_y2[kMaxCSCTF], CSCTF_fitline_y3[kMaxCSCTF], CSCTF_fitline_y4[kMaxCSCTF];
  Float_t CSCTF_fitline_z1[kMaxCSCTF], CSCTF_fitline_z2[kMaxCSCTF], CSCTF_fitline_z3[kMaxCSCTF], CSCTF_fitline_z4[kMaxCSCTF];
  

  // Matching the L1Mu to RPCb  
  Int_t nRPCb;
  Int_t L1Mu_RPCb_index[kMaxL1Mu];
  Float_t RPCb_pt[kMaxRPCb], RPCb_eta[kMaxRPCb], RPCb_phi[kMaxRPCb];
  Int_t RPCb_bx[kMaxRPCb], RPCb_nStubs[kMaxRPCb], RPCb_quality[kMaxRPCb];

  Float_t RPCb_phi1[kMaxRPCb], RPCb_phi2[kMaxRPCb], RPCb_phi3[kMaxRPCb];
  Float_t RPCb_phi4[kMaxRPCb], RPCb_phi5[kMaxRPCb], RPCb_phi6[kMaxRPCb];

  Int_t RPCb_bx1[kMaxRPCb], RPCb_strip1[kMaxRPCb];
  Int_t RPCb_re1[kMaxRPCb], RPCb_ri1[kMaxRPCb], RPCb_st1[kMaxRPCb], RPCb_se1[kMaxRPCb];
  Int_t RPCb_la1[kMaxRPCb], RPCb_su1[kMaxRPCb], RPCb_ro1[kMaxRPCb];
 
  Int_t RPCb_bx2[kMaxRPCb], RPCb_strip2[kMaxRPCb];
  Int_t RPCb_re2[kMaxRPCb], RPCb_ri2[kMaxRPCb], RPCb_st2[kMaxRPCb], RPCb_se2[kMaxRPCb];
  Int_t RPCb_la2[kMaxRPCb], RPCb_su2[kMaxRPCb], RPCb_ro2[kMaxRPCb];

  Int_t RPCb_bx3[kMaxRPCb], RPCb_strip3[kMaxRPCb];
  Int_t RPCb_re3[kMaxRPCb], RPCb_ri3[kMaxRPCb], RPCb_st3[kMaxRPCb], RPCb_se3[kMaxRPCb];
  Int_t RPCb_la3[kMaxRPCb], RPCb_su3[kMaxRPCb], RPCb_ro3[kMaxRPCb];

  Int_t RPCb_bx4[kMaxRPCb], RPCb_strip4[kMaxRPCb];
  Int_t RPCb_re4[kMaxRPCb], RPCb_ri4[kMaxRPCb], RPCb_st4[kMaxRPCb], RPCb_se4[kMaxRPCb];
  Int_t RPCb_la4[kMaxRPCb], RPCb_su4[kMaxRPCb], RPCb_ro4[kMaxRPCb];

  Int_t RPCb_bx5[kMaxRPCb], RPCb_strip5[kMaxRPCb];
  Int_t RPCb_re5[kMaxRPCb], RPCb_ri5[kMaxRPCb], RPCb_st5[kMaxRPCb], RPCb_se5[kMaxRPCb];
  Int_t RPCb_la5[kMaxRPCb], RPCb_su5[kMaxRPCb], RPCb_ro5[kMaxRPCb];

  Int_t RPCb_bx6[kMaxRPCb], RPCb_strip6[kMaxRPCb];
  Int_t RPCb_re6[kMaxRPCb], RPCb_ri6[kMaxRPCb], RPCb_st6[kMaxRPCb], RPCb_se6[kMaxRPCb];
  Int_t RPCb_la6[kMaxRPCb], RPCb_su6[kMaxRPCb], RPCb_ro6[kMaxRPCb];


  // Matching the L1Mu to RPCf  
  Int_t nRPCf;
  Int_t L1Mu_RPCf_index[kMaxL1Mu];
  Float_t RPCf_pt[kMaxRPCf], RPCf_eta[kMaxRPCf], RPCf_phi[kMaxRPCf];
  Int_t RPCf_bx[kMaxRPCf], RPCf_nStubs[kMaxRPCf], RPCf_quality[kMaxRPCf];

  Float_t RPCf_phi1[kMaxRPCf], RPCf_phi2[kMaxRPCf], RPCf_phi3[kMaxRPCf];
  Float_t RPCf_phi4[kMaxRPCf], RPCf_phi5[kMaxRPCf], RPCf_phi6[kMaxRPCf];

  Int_t RPCf_bx1[kMaxRPCf], RPCf_strip1[kMaxRPCf];
  Int_t RPCf_re1[kMaxRPCf], RPCf_ri1[kMaxRPCf], RPCf_st1[kMaxRPCf], RPCf_se1[kMaxRPCf];
  Int_t RPCf_la1[kMaxRPCf], RPCf_su1[kMaxRPCf], RPCf_ro1[kMaxRPCf];
 
  Int_t RPCf_bx2[kMaxRPCf], RPCf_strip2[kMaxRPCf];
  Int_t RPCf_re2[kMaxRPCf], RPCf_ri2[kMaxRPCf], RPCf_st2[kMaxRPCf], RPCf_se2[kMaxRPCf];
  Int_t RPCf_la2[kMaxRPCf], RPCf_su2[kMaxRPCf], RPCf_ro2[kMaxRPCf];

  Int_t RPCf_bx3[kMaxRPCf], RPCf_strip3[kMaxRPCf];
  Int_t RPCf_re3[kMaxRPCf], RPCf_ri3[kMaxRPCf], RPCf_st3[kMaxRPCf], RPCf_se3[kMaxRPCf];
  Int_t RPCf_la3[kMaxRPCf], RPCf_su3[kMaxRPCf], RPCf_ro3[kMaxRPCf];

  Int_t RPCf_bx4[kMaxRPCf], RPCf_strip4[kMaxRPCf];
  Int_t RPCf_re4[kMaxRPCf], RPCf_ri4[kMaxRPCf], RPCf_st4[kMaxRPCf], RPCf_se4[kMaxRPCf];
  Int_t RPCf_la4[kMaxRPCf], RPCf_su4[kMaxRPCf], RPCf_ro4[kMaxRPCf];

  Int_t RPCf_bx5[kMaxRPCf], RPCf_strip5[kMaxRPCf];
  Int_t RPCf_re5[kMaxRPCf], RPCf_ri5[kMaxRPCf], RPCf_st5[kMaxRPCf], RPCf_se5[kMaxRPCf];
  Int_t RPCf_la5[kMaxRPCf], RPCf_su5[kMaxRPCf], RPCf_ro5[kMaxRPCf];

  Int_t RPCf_bx6[kMaxRPCf], RPCf_strip6[kMaxRPCf];
  Int_t RPCf_re6[kMaxRPCf], RPCf_ri6[kMaxRPCf], RPCf_st6[kMaxRPCf], RPCf_se6[kMaxRPCf];
  Int_t RPCf_la6[kMaxRPCf], RPCf_su6[kMaxRPCf], RPCf_ro6[kMaxRPCf];

  // Matching the SIM Mu to GEM pad (really no other way to do this)
  Int_t nGEM;
  Float_t GE11_phi_L1[kMaxGEM], GE11_phi_L2[kMaxGEM], GE21_phi_L1[kMaxGEM], GE21_phi_L2[kMaxGEM];
  Float_t GE21_pad2_phi_L1[kMaxGEM], GE21_pad2_phi_L2[kMaxGEM];
  Int_t   GE11_bx_L1[kMaxGEM], GE11_bx_L2[kMaxGEM], GE21_bx_L1[kMaxGEM], GE21_bx_L2[kMaxGEM];
  Int_t   GE11_ch_L1[kMaxGEM], GE11_ch_L2[kMaxGEM], GE21_ch_L1[kMaxGEM], GE21_ch_L2[kMaxGEM];
  Float_t GE11_z_L1[kMaxGEM], GE11_z_L2[kMaxGEM], GE21_z_L1[kMaxGEM], GE21_z_L2[kMaxGEM];

  Float_t GE11_sim_phi_L1[kMaxGEM], GE11_sim_phi_L2[kMaxGEM], GE21_sim_phi_L1[kMaxGEM], GE21_sim_phi_L2[kMaxGEM];
  Float_t GE11_sim_bx_L1[kMaxGEM], GE11_sim_bx_L2[kMaxGEM], GE21_sim_bx_L1[kMaxGEM], GE21_sim_bx_L2[kMaxGEM];
  Int_t   GE11_sim_ch_L1[kMaxGEM], GE11_sim_ch_L2[kMaxGEM], GE21_sim_ch_L1[kMaxGEM], GE21_sim_ch_L2[kMaxGEM];
  Float_t GE11_sim_z_L1[kMaxGEM], GE11_sim_z_L2[kMaxGEM], GE21_sim_z_L1[kMaxGEM], GE21_sim_z_L2[kMaxGEM];

  Float_t GE11_sim_pad_phi_L1[kMaxGEM], GE11_sim_pad_phi_L2[kMaxGEM], GE21_sim_pad_phi_L1[kMaxGEM], GE21_sim_pad_phi_L2[kMaxGEM];
  Float_t GE11_sim_pad_bx_L1[kMaxGEM], GE11_sim_pad_bx_L2[kMaxGEM], GE21_sim_pad_bx_L1[kMaxGEM], GE21_sim_pad_bx_L2[kMaxGEM];
  Int_t   GE11_sim_pad_ch_L1[kMaxGEM], GE11_sim_pad_ch_L2[kMaxGEM], GE21_sim_pad_ch_L1[kMaxGEM], GE21_sim_pad_ch_L2[kMaxGEM];
  Float_t GE11_sim_pad_z_L1[kMaxGEM], GE11_sim_pad_z_L2[kMaxGEM], GE21_sim_pad_z_L1[kMaxGEM], GE21_sim_pad_z_L2[kMaxGEM];

  // positions from artificial pads
  Float_t GE21_sim_pad1_phi_L1[kMaxGEM], GE21_sim_pad1_phi_L2[kMaxGEM];
  Float_t GE21_sim_pad2_phi_L1[kMaxGEM], GE21_sim_pad2_phi_L2[kMaxGEM];
  Float_t GE21_sim_pad4_phi_L1[kMaxGEM], GE21_sim_pad4_phi_L2[kMaxGEM];
  Float_t GE21_sim_pad8_phi_L1[kMaxGEM], GE21_sim_pad8_phi_L2[kMaxGEM];
};

bool 
PtOrder (const reco::GenParticle* p1, const reco::GenParticle* p2) 
{ 
  return (p1->pt() > p2->pt() ); 
}

double 
dxy(double px, double py, double vx, double vy, double pt)
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

double 
dRWeighted(double eta1, double phi1, double eta2, double phi2, double sigma_eta=2., double sigma_phi=1.)
{
  double dEta = std::abs(eta1 - eta2);
  double dPhi = reco::deltaPhi(phi1, phi2);
  double dR = std::sqrt((dEta*dEta)/(sigma_eta*sigma_eta) + (dPhi*dPhi)/(sigma_phi*sigma_phi));
  return dR;
}

double 
My_dPhi(double phi1, double phi2) {
  double dPhi = phi1 - phi2;
  if (dPhi >  M_PI) dPhi -= 2.*M_PI;
  if (dPhi < -M_PI) dPhi += 2.*M_PI;
  return dPhi;
}

double 
phiL1DTTrack(const L1MuDTTrack& track)
{
  int phi_local = track.phi_packed(); //range: 0 < phi_local < 31
  if ( phi_local > 15 ) phi_local -= 32; //range: -16 < phi_local < 15    
  double dttrk_phi_global = normalizedPhi((phi_local*(M_PI/72.))+((M_PI/6.)*track.spid().sector()));// + 12*i->scNum(); //range: -16 < phi_global < 147 
  // if(dttrk_phi_global < 0) dttrk_phi_global+=2*M_PI; //range: 0 < phi_global < 147
  // if(dttrk_phi_global > 2*M_PI) dttrk_phi_global-=2*M_PI; //range: 0 < phi_global < 143
  return dttrk_phi_global;
}

double 
phiL1CSCTrack(const csc::L1Track& track)
{
  unsigned gbl_phi(track.localPhi() + ((track.sector() - 1)*24) + 6);
  if(gbl_phi > 143) gbl_phi -= 143;
  double phi_packed = gbl_phi & 0xff;
  return phi_packed;
}

int
getHalfStrip(const CSCComparatorDigi& digi) 
{
  return (digi.getStrip() - 1) * 2 + digi.getComparator();
}

float 
getFractionalStrip(const CSCComparatorDigi&d)
{
  return d.getStrip() + d.getComparator()/2. - 3/4.;
}

void fitStraightLineErrors(const std::vector<float>& v, 
                           const std::vector<float>& w, 
                           const std::vector<float>& ev, 
                           const std::vector<float>& ew, 
                           float& alpha, float& beta, 
                           int lumi, int run, int event, int muon, int stub,
                           bool debug)
{
  //std::cout << "size of v: "<<v.size() << std::endl; 
  
  if (v.size()>=3) {
  
  float zmin;
  float zmax;
  if (v.front() < v.back()){
    zmin = v.front();
    zmax = v.back();
  }
  else{
    zmin = v.back();
    zmax = v.front();
  }

  TF1 *fit1 = new TF1("fit1","pol1",zmin,zmax); 
  //where 0 = x-axis_lowest and 48 = x_axis_highest 
  TGraphErrors* gr = new TGraphErrors(v.size(),&(v[0]),&(w[0]),&(ev[0]),&(ew[0]));
  gr->SetMinimum(w[2]-5*0.002);
  gr->SetMaximum(w[2]+5*0.002);
 
  gr->Fit(fit1,"RQ"); 
  
  alpha = fit1->GetParameter(0); //value of 0th parameter
  beta  = fit1->GetParameter(1); //value of 1st parameter

  if (debug){
    TCanvas* c1 = new TCanvas("c1","A Simple Graph with error bars",200,10,700,500);
    c1->cd();
    c1->SetFillColor(42);
    c1->SetGrid();
    // c1->GetFrame()->SetFillColor(21);
    // c1->GetFrame()->SetBorderSize(12);
    
    TString slumi;  slumi.Form("%d", lumi);
    TString srun;   srun.Form("%d", run);
    TString sevent; sevent.Form("%d", event);
    TString smuon;  smuon.Form("%d", muon);
    TString sstub;  sstub.Form("%d", stub);

    gr->SetTitle("Linear fit to ComparatorDigis for Lumi " + slumi + " Run " + srun + " Event " + sevent + " Muon " + smuon + " Stub " + sstub);
    gr->SetMarkerColor(4);
    gr->SetMarkerStyle(21);
    gr->Draw("ALP");
    
    c1->SaveAs("ComparatoDigiLinearFits/c_debug_fit_L" + slumi + "_R" + srun + "_E" + sevent + "_M" + smuon + "_S" + sstub + ".png");
    delete c1;
  }
  delete fit1;
  delete gr;
  }
  else{
    //std::cout << "ERROR: LCT without at least 3 comparator digis in the chamber!!" << std::endl;
  }
}


void fitStraightLine(const std::vector<float>& v, 
                     const std::vector<float>& w, 
                     float& alpha, float& beta, 
                     bool debug = false)
{
  if (v.size()>=2) {
    
    float zmin;
    float zmax;
    if (v.front() < v.back()){
      zmin = v.front();
      zmax = v.back();
    }
    else{
      zmin = v.back();
      zmax = v.front();
    }
    
    TF1 *fit1 = new TF1("fit1","pol1",zmin,zmax); 
    //where 0 = x-axis_lowest and 48 = x_axis_highest 
    TGraph* gr = new TGraph(v.size(),&(v[0]),&(w[0]));
    gr->Fit(fit1,"RQ"); 
    
    alpha = fit1->GetParameter(0); //value of 0th parameter
    beta  = fit1->GetParameter(1); //value of 1st parameter
    
    delete fit1;
    delete gr;
  }
  else{
    alpha = 0;
    beta = 0;
  }
}


void getPositionsStations(float alpha_x, float beta_x, float alpha_y, float beta_y, 
                          std::vector<float>& xs, std::vector<float>& ys, 
                          int sign_z,
                          float z1 = 600, float z2 = 825, float z3 = 935, float z4 = 1020)
{
  xs.push_back(alpha_x + beta_x * z1*sign_z);
  xs.push_back(alpha_x + beta_x * z2*sign_z);
  xs.push_back(alpha_x + beta_x * z3*sign_z);
  xs.push_back(alpha_x + beta_x * z4*sign_z);
  
  ys.push_back(alpha_y + beta_y * z1*sign_z);
  ys.push_back(alpha_y + beta_y * z2*sign_z);
  ys.push_back(alpha_y + beta_y * z3*sign_z);
  ys.push_back(alpha_y + beta_y * z4*sign_z);
}


bool 
isSimTrackGood(const SimTrack &t)
{
  // SimTrack selection
  //if (t.noVertex()) return false;
  //if (t.noGenpart()) return false;
  // only muons 
  if (std::abs(t.type()) != 13) return false;
  // pt selection
  if (t.momentum().pt() < 0) return false;
  // eta selection
  const float eta(std::abs(t.momentum().eta()));
  if (eta > 3.0) return false; 
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

  float getGlobalPhi(unsigned int rawid, int stripN);
  double calcCSCSpecificPhi(unsigned int rawId, const CSCCorrelatedLCTDigi& tp) const;
  GlobalPoint getGlobalPointPad(unsigned int rawId, const GEMCSCPadDigi& tp) const;;  
  GlobalPoint getCSCSpecificPoint(unsigned int rawid, const CSCCorrelatedLCTDigi& tp) const;
  GlobalPoint getCSCSpecificPoint2(unsigned int rawId, const CSCCorrelatedLCTDigi& tp) const;
  
  GlobalPoint getCSCSpecificPointStrips(const SimTrackMatchManager& tp) const;
  bool isCSCCounterClockwise(const std::unique_ptr<const CSCLayer>& layer) const;
  void fitComparatorsLCT(const CSCComparatorDigiCollection&, const CSCCorrelatedLCTDigi& tp, 
                         CSCDetId chid, int iMuon, float& fit_z, float& fit_phi, float& dphi) const;
  void getStubPositions(int index, std::vector<float>& x, 
                        std::vector<float>& y, std::vector<float>& z) const;
  std::vector<GlobalPoint> positionPad2InDetId(const GEMDigiCollection&, unsigned int ch_id, int refBX) const;
  std::vector<GlobalPoint> positionPad4InDetId(const GEMDigiCollection&, unsigned int ch_id, int refBX) const;
  
  void printCSCStubProperties(int index) const;
  

  CSCCorrelatedLCTDigiId 
  pickBestMatchingStub(float x1, float y1,
                       const CSCCorrelatedLCTDigiId& oldCoPad,
                       const CSCCorrelatedLCTDigiId& newCoPad, 
                       int refBx) const;
  
  bool stubInCSCTFTracks(const CSCCorrelatedLCTDigi& stub, const L1CSCTrackCollection& l1Tracks) const;
  bool stubInDTTFTracks(const L1MuDTTrackSegPhi& candidateStub, 
                        const L1MuDTTrackCollection& l1Tracks) const;

  GEMCSCPadDigiId
  pickBestMatchingCoPad(float x1, float y1,
                        const GEMCSCPadDigiId& oldCoPad,
                        const GEMCSCPadDigiId& newCoPad, int refBx) const;
  GEMCSCPadDigiId
  pickBestMatchingPad(float x1, float y1,
                      const GEMCSCPadDigiId& oldPad,
                      const GEMCSCPadDigiId& newPad, int refBx) const;
  void fillCSCStubProperties(const CSCDetId& ch_id,
                             const CSCCorrelatedLCTDigi& stub,
                             int index,
                             const GlobalPoint& GP,
                             float z, float phi, float dphi);

  void extrapolate(const SimTrack&tk, const SimVertex&, GlobalPoint&);
  void extrapolate(const reco::GenParticle &tk, int station, GlobalPoint&, GlobalVector&);
  void extrapolate(const TTTrack< Ref_PixelDigi_ > &tk, int station, GlobalPoint&, GlobalVector&);
  GlobalPoint extrapolateGP(const TTTrack< Ref_PixelDigi_ > &tk, int station=2);
  TrajectoryStateOnSurface propagateToZ(const GlobalPoint &, const GlobalVector &, double, double) const;
  TrajectoryStateOnSurface propagateToR(const GlobalPoint &, const GlobalVector &, double, double) const;

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
  bool produceFitPlots_;
  bool processRPCb_;
  bool processRPCf_;
  bool doSimAnalysis_;
  bool doGenAnalysis_;
  bool processTTI_;
  bool processDTTF_;
  
  const RPCGeometry* rpcGeometry_;
  const CSCGeometry* cscGeometry_;
  const GEMGeometry* gemGeometry_;
 
  edm::InputTag L1Mu_input;
  edm::InputTag L1TkMu_input;
  
  edm::ESHandle<MagneticField> magfield_;
  edm::ESHandle<Propagator> propagator_;
  edm::ESHandle<Propagator> propagatorOpposite_;
  edm::ESHandle<Propagator> propagatorAny_;
  edm::ESHandle<MuonDetLayerGeometry> muonGeometry_;
  edm::ESHandle<RPCGeometry> rpc_geom_;
  edm::ESHandle<CSCGeometry> csc_geom_;
  edm::ESHandle<GEMGeometry> gem_geom_;
  
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

  edm::ParameterSet cfg_;
};

DisplacedL1MuFilter::DisplacedL1MuFilter(const edm::ParameterSet& iConfig) : 
  useSimpleGeometry_(iConfig.getParameter<bool>("useSimpleGeometry")),
  useMB2_(iConfig.existsAs<bool>("useStation2") ? iConfig.getParameter<bool>("useStation2") : true),
  fallbackToME1_(iConfig.existsAs<bool>("fallbackToME1") ? iConfig.getParameter<bool>("fallbackToME1") : false),
  whichTrack_(None), whichState_(AtVertex),
  cosmicPropagation_(iConfig.getParameter<bool>("cosmicPropagationHypothesis")),
  cfg_(iConfig.getParameterSet("simTrackMatching"))
{
  //now do what ever initialization is needed
  min_L1Mu_Quality = iConfig.getParameter<int>("min_L1Mu_Quality");
  max_dR_L1Mu_L1Tk = iConfig.getParameter<double>("max_dR_L1Mu_L1Tk");
  max_dR_L1Mu_noL1Tk = iConfig.getParameter<double>("max_dR_L1Mu_noL1Tk");
  min_pT_L1Tk = iConfig.getParameter<double>("min_pT_L1Tk");
  max_pT_L1Tk = iConfig.getParameter<double>("max_pT_L1Tk");
  verbose = iConfig.getParameter<int>("verbose");
  produceFitPlots_ = iConfig.getParameter<bool>("produceFitPlots");
  processRPCb_ = iConfig.getParameter<bool>("processRPCb");
  processRPCf_ = iConfig.getParameter<bool>("processRPCf");
  processTTI_ = iConfig.getParameter<bool>("processTTI");
  processDTTF_ = iConfig.getParameter<bool>("processDTTF");
  doSimAnalysis_ = iConfig.getParameter<bool>("doSimAnalysis");
  doGenAnalysis_ = iConfig.getParameter<bool>("doGenAnalysis");
  
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

  iSetup.get<MuonGeometryRecord>().get(rpc_geom_);
  rpcGeometry_ = &*rpc_geom_;

  iSetup.get<MuonGeometryRecord>().get(csc_geom_);
  cscGeometry_ = &*csc_geom_;

  iSetup.get<MuonGeometryRecord>().get(gem_geom_);
  gemGeometry_ = &*gem_geom_;

  typedef std::vector<L1MuGMTCand> GMTs;
  edm::Handle<GMTs> aH;
  iEvent.getByLabel("simGmtDigis", aH);
  const GMTs& l1GmtCands(*aH.product());

  edm::Handle<L1MuDTTrackCollection > L1DTTrackPhiH;
  iEvent.getByLabel("dttfDigis","DTTF", L1DTTrackPhiH);
  const L1MuDTTrackCollection& L1DTTrackPhis(*L1DTTrackPhiH.product());

  edm::Handle<vector<L1MuDTTrackSegPhi> > DTTrackPhiH;
  iEvent.getByLabel("dttfDigis","DTTF", DTTrackPhiH);
  const vector<L1MuDTTrackSegPhi>& DTTrackPhis(*DTTrackPhiH.product());

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

  edm::Handle< std::vector<L1MuRegionalCand> > hL1MuRPCbs;
  iEvent.getByLabel("simRpcTriggerDigis", "RPCb", hL1MuRPCbs);
  const std::vector<L1MuRegionalCand>& l1MuRPCbs(*hL1MuRPCbs.product());
  
  edm::Handle< std::vector<RPCDigiL1Link> > hL1MuRPCbLinks;
  iEvent.getByLabel("simRpcTriggerDigis", "RPCb", hL1MuRPCbLinks);
  const std::vector<RPCDigiL1Link>& l1MuRPCbLinks(*hL1MuRPCbLinks.product());
  
  edm::Handle< std::vector<L1MuRegionalCand> > hL1MuRPCfs;
  iEvent.getByLabel("simRpcTriggerDigis", "RPCf", hL1MuRPCfs);
  const std::vector<L1MuRegionalCand>& l1MuRPCfs(*hL1MuRPCfs.product());
  
  edm::Handle< std::vector<RPCDigiL1Link> > hL1MuRPCfLinks;
  iEvent.getByLabel("simRpcTriggerDigis", "RPCf", hL1MuRPCfLinks);
  const std::vector<RPCDigiL1Link>& l1MuRPCfLinks(*hL1MuRPCfLinks.product());

  // comparator digis
  edm::Handle< CSCComparatorDigiCollection > hCSCComparators;
  iEvent.getByLabel("simMuonCSCDigis", "MuonCSCComparatorDigi", hCSCComparators);
  //const CSCComparatorDigiCollection& CSCComparators(*hCSCComparators.product());
  
  // LCTs
  edm::Handle< CSCCorrelatedLCTDigiCollection > hCSCCorrelatedLCTs;
  iEvent.getByLabel("simCscTriggerPrimitiveDigis", "MPCSORTED", hCSCCorrelatedLCTs);
  const CSCCorrelatedLCTDigiCollection& CSCCorrelatedLCTs(*hCSCCorrelatedLCTs.product());

  // GEM pads and copads
  edm::Handle< GEMDigiCollection > hGEMDigis;
  iEvent.getByLabel("simMuonGEMDigis", hGEMDigis);
  const GEMDigiCollection& GEMDigis(*hGEMDigis.product());

  // GEM pads and copads
  edm::Handle< GEMCSCPadDigiCollection > hGEMCSCPads;
  iEvent.getByLabel("simMuonGEMCSCPadDigis", hGEMCSCPads);
  //const GEMCSCPadDigiCollection& GEMCSCPads(*hGEMCSCPads.product());

  edm::Handle< GEMCSCPadDigiCollection > hGEMCSCCoPads;
  iEvent.getByLabel("simMuonGEMCSCPadDigis", "Coincidence", hGEMCSCCoPads);
  //const GEMCSCCoPadDigiCollection& GEMCSCCoPads(*hGEMCSCCoPads.product());

  // L1 TrackingTrigger Analysis
  edm::Handle< std::vector< TTTrack< Ref_PixelDigi_ > > > TTTrackHandle;
  iEvent.getByLabel("TTTracksFromPixelDigis", "Level1TTTracks", TTTrackHandle);
  std::vector< TTTrack< Ref_PixelDigi_ > > TTTracks;
  if (processTTI_){
    TTTracks = *TTTrackHandle.product();
  }

  edm::Handle<edm::SimTrackContainer> sim_tracks;
  iEvent.getByLabel("g4SimHits", sim_tracks);
  const edm::SimTrackContainer & sim_trks = *sim_tracks.product();
  edm::SimTrackContainer skim_sim_trks;

  // define a skimmed simtrack collection
  for (unsigned int k=0; k<sim_trks.size(); ++k) {
    auto sim_muon = sim_trks[k];
    if (!isSimTrackGood(sim_muon)) continue;
    skim_sim_trks.push_back(sim_muon);
  }        

  edm::Handle<edm::SimVertexContainer> sim_vertices;
  iEvent.getByLabel("g4SimHits", sim_vertices);
  const edm::SimVertexContainer & sim_vtxs = *sim_vertices.product();
  
  event_.lumi = iEvent.id().luminosityBlock();
  event_.run = iEvent.id().run();
  event_.event = iEvent.id().event();

  event_.nL1Mu = l1GmtCands.size();
  if (processTTI_){
    event_.nL1Tk = TTTracks.size();
  }
  event_.beamSpot_x = 0;
  event_.beamSpot_y = 0;
  event_.beamSpot_z = 0;

  //////////////////
  // GEN analysis //
  //////////////////

  // Sort muon groups to match order of genGd vector
  std::vector< std::vector<const reco::GenParticle*> > genMuonGroups;
  std::vector<const reco::Candidate*> genMuonGroupsMothers;

  if (doGenAnalysis_) {
  
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

        GlobalPoint ex_pMS2;
        GlobalVector ex_vMS2;

        GlobalPoint ex_pGE11;
        GlobalPoint ex_pGE21;
        GlobalVector ex_vGE11;
        GlobalVector ex_vGE21;
        extrapolate(*genMuonGroups[i][j], 1, ex_pMS2, ex_vMS2);
        extrapolate(*genMuonGroups[i][j], 11, ex_pGE11, ex_vGE11);
        extrapolate(*genMuonGroups[i][j], 21, ex_pGE21, ex_vGE21);

        if (!(ex_pMS2 == GlobalPoint())){
          event_.genGdMu_eta_prop[i][j] = ex_pMS2.eta();
          event_.genGdMu_phi_prop[i][j] = ex_pMS2.phi();
          event_.genGdMu_deta_prop[i][j] = std::abs(event_.genGdMu_eta[i][j] - event_.genGdMu_eta_prop[i][j]);
          event_.genGdMu_dphi_prop[i][j] = My_dPhi(event_.genGdMu_phi[i][j], event_.genGdMu_phi_prop[i][j]);
          event_.genGdMu_dR_prop[i][j] = reco::deltaR(event_.genGdMu_eta[i][j], event_.genGdMu_phi[i][j],
                                                      event_.genGdMu_eta_prop[i][j], event_.genGdMu_phi_prop[i][j]);
        }
        if (!(ex_pGE11 == GlobalPoint())){
          event_.genGdMu_etav_prop_GE11[i][j] = ex_vGE11.eta();
          event_.genGdMu_phiv_prop_GE11[i][j] = ex_vGE11.phi();
        }
        if (!(ex_pGE21 == GlobalPoint())){
          event_.genGdMu_etav_prop_GE21[i][j] = ex_vGE21.eta();
          event_.genGdMu_phiv_prop_GE21[i][j] = ex_vGE21.phi();
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

        //////////////////////
        // pre-SIM analysis //
        //////////////////////
        double GEN_SIM_min_dR = 99;
        for (unsigned int k=0; k<skim_sim_trks.size(); ++k) {
          std::cout << "Analyze SIM muon " << k << std::endl;
          auto sim_muon = skim_sim_trks[k];
          event_.pt_sim[k] = sim_muon.momentum().pt();
          event_.eta_sim[k] = sim_muon.momentum().eta();
          event_.phi_sim[k] = sim_muon.momentum().phi();
          event_.charge_sim[k] = sim_muon.charge();
          cout << "\t"<<k<<endl;
          cout << "\tSIM_pt " << event_.pt_sim[k] << endl;
          cout << "\tSIM_eta " << event_.eta_sim[k] << endl;
          cout << "\tSIM_phi " << event_.phi_sim[k] << endl;
          cout << "\tSIM_charge " << event_.charge_sim << endl;
          double deltar(reco::deltaR(event_.eta_sim[k], 
                                     event_.phi_sim[k], 
                                     event_.genGdMu_eta[i][j], 
                                     event_.genGdMu_phi[i][j]));
          if (deltar < GEN_SIM_min_dR and deltar < 0.1){
            GEN_SIM_min_dR = deltar;
            event_.genGdMu_SIM_index[i][j] = k;
            event_.genGdMu_SIM_dR[i][j] = deltar;
          }
        }
        // std::cout << "Matched SIM " << event_.genGdMu_SIM_index[i][j] << " " << event_.genGdMu_SIM_dR[i][j] << std::endl;
      }
    }
    if(verbose) { 
      std::cout << "++++ GEN Mu analysis ++++" << std::endl; 
      std::cout << std::setw(4) << std::left << "Mu"
                << std::setw(10) << std::left << "pt"
                << std::setw(10) << std::left << "eta"
                << std::setw(10) << std::left << "phi"
                << std::setw(10) << std::left << "etaProp"
                << std::setw(10) << std::left << "phiProp"
                << std::setw(10) << std::left << "dxy"
                << std::setw(10) << std::left << "SIM index"
                << std::setw(10) << std::left << "SIM dR"
                << std::setw(10) << std::left << "SIM pt"
                << std::setw(10) << std::left << "SIM eta"
                << std::setw(10) << std::left << "SIM phi"
                << std::endl;

      for (int i=0; i<2; ++i){ 
        for (int j=0; j<2; ++j){
          std::string ijs(std::to_string(i) + std::to_string(j));
          std::cout << std::setw(4) << std::left << ijs
                    << std::setw(10) << std::left << event_.genGdMu_pt[i][j]
                    << std::setw(10) << std::left << event_.genGdMu_eta[i][j]
                    << std::setw(10) << std::left << event_.genGdMu_phi[i][j]
                    << std::setw(10) << std::left << event_.genGdMu_eta_prop[i][j]
                    << std::setw(10) << std::left << event_.genGdMu_phi_prop[i][j]
                    << std::setw(10) << std::left << event_.genGdMu_dxy[i][j]
                    << std::setw(10) << std::left << event_.genGdMu_SIM_index[i][j]
                    << std::setw(10) << std::left << event_.genGdMu_SIM_dR[i][j];
          if (event_.genGdMu_SIM_index[i][j] != -99){
            std::cout << std::setw(10) << std::left << event_.pt_sim[event_.genGdMu_SIM_index[i][j]]
                      << std::setw(10) << std::left << event_.eta_sim[event_.genGdMu_SIM_index[i][j]]
                      << std::setw(10) << std::left << event_.phi_sim[event_.genGdMu_SIM_index[i][j]]
                      << std::endl;
          } else {
            std::cout << std::setw(10) << std::left << -1 
                      << std::setw(10) << std::left << -1 
                      << std::setw(10) << std::left << -1 
                      << std::endl;
          }
        }
      }
      std::cout << std::endl;
    }
  }

  }

  // // comparator digi collection in this chamber
  // for(auto cItr = hCSCComparators->begin(); cItr != hCSCComparators->end(); ++cItr){
  //   CSCDetId id = (*cItr).first;
  //   //loop over digis of given roll
  //   for (auto digiItr = (*cItr ).second.first; digiItr != (*cItr ).second.second; ++digiItr){
  //     auto stub = *digiItr;
  //     if (stub.getTimeBin() < 4 or stub.getTimeBin() > 8) continue; 
  //     // std::cout << "Comparator digi L1Mu " << id << " " << stub << " " << getHalfStrip(stub) << std::endl;
  //   }
  // }
 
  //////////////////////
  // SIM-L1  analysis //
  //////////////////////

  if (doSimAnalysis_){

    if (not doGenAnalysis_) {
      for (unsigned int k=0; k<skim_sim_trks.size(); ++k) {
        //std::cout << "Analyze SIM muon " << k << std::endl;
        auto sim_muon = skim_sim_trks[k];
        event_.pt_sim[k] = sim_muon.momentum().pt();
        event_.eta_sim[k] = sim_muon.momentum().eta();
        event_.phi_sim[k] = sim_muon.momentum().phi();
        event_.charge_sim[k] = sim_muon.charge();
      }
    }

    if(verbose) {
      cout << "++++ SIM Mu analysis ++++" << endl;
      cout << "Number of good simtracks " << skim_sim_trks.size() << endl;
    }
    for (unsigned int k=0; k<skim_sim_trks.size(); ++k) {
      
      auto sim_muon = skim_sim_trks[k];
      if(verbose) {
        cout << "Mu "<< k
             <<" pT " << sim_muon.momentum().pt() 
             <<" eta "<< sim_muon.momentum().eta()
             <<" phi "<< sim_muon.momentum().phi() << endl << endl;
      }
      auto sim_vertex = sim_vtxs[sim_muon.vertIndex()];
      SimTrackMatchManager match(sim_muon, sim_vertex, cfg_, iEvent, iSetup);
      
      const SimHitMatcher& match_sh = match.simhits();
      //const CSCDigiMatcher& match_cd = match.cscDigis();
      const CSCStubMatcher& match_csc = match.cscStubs();
      const GEMDigiMatcher& match_gd = match.gemDigis();
      
      // True position of the CSC hits in a chamber with an LCT
      if (verbose) { 
        cout << endl<<"++++ CSC SimHit analysis ++++" << endl;
      }
      for (auto d: match_csc.chamberIdsLCT(0)){
        auto detId = CSCDetId(d);
        // only analyze ME1b and ME21
        //if (detId.station()!=1 and detId.station()!=2) continue;
        //if (detId.ring()!=1) continue;
        
        edm::PSimHitContainer simhits = match_sh.hitsInChamber(d);
        auto gp_csc = match_sh.simHitPositionKeyLayer(d);
        if(verbose) std::cout << detId 
                              << " n CSC hits " << simhits.size() 
                              << " key phi " << gp_csc.phi() 
                              << " key eta " << gp_csc.eta()
                              << " GP " << gp_csc
                              << endl;
        if (detId.station()==1) {
          event_.CSCTF_sim_phi1[k] = gp_csc.phi();
          event_.CSCTF_sim_eta1[k] = gp_csc.eta();
          event_.CSCTF_sim_x1[k] = gp_csc.x();
          event_.CSCTF_sim_y1[k] = gp_csc.y();
          event_.CSCTF_sim_z1[k] = gp_csc.z();
          event_.CSCTF_sim_R1[k] = gp_csc.perp();
        }
        if (detId.station()==2) {
          event_.CSCTF_sim_phi2[k] = gp_csc.phi();
          event_.CSCTF_sim_eta2[k] = gp_csc.eta();
          event_.CSCTF_sim_x2[k] = gp_csc.x();
          event_.CSCTF_sim_y2[k] = gp_csc.y();
          event_.CSCTF_sim_z2[k] = gp_csc.z();
          event_.CSCTF_sim_R2[k] = gp_csc.perp();
        }
        if (detId.station()==3) {
          event_.CSCTF_sim_phi3[k] = gp_csc.phi();
          event_.CSCTF_sim_eta3[k] = gp_csc.eta();
          event_.CSCTF_sim_x3[k] = gp_csc.x();
          event_.CSCTF_sim_y3[k] = gp_csc.y();
          event_.CSCTF_sim_z3[k] = gp_csc.z();
          event_.CSCTF_sim_R3[k] = gp_csc.perp();
        }
        if (detId.station()==4) {
          event_.CSCTF_sim_phi4[k] = gp_csc.phi();
          event_.CSCTF_sim_eta4[k] = gp_csc.eta();
          event_.CSCTF_sim_x4[k] = gp_csc.x();
          event_.CSCTF_sim_y4[k] = gp_csc.y();
          event_.CSCTF_sim_z4[k] = gp_csc.z();
          event_.CSCTF_sim_R4[k] = gp_csc.perp();
        }
      }
      
      // GEM simhit
      auto hits = match_sh.simHitsGEM();
      if (verbose) { 
        cout << endl<<"++++ GEM SimHit analysis ++++" << endl;
        cout << "Number of GEM hits " << hits.size() << endl;
      }
      for (auto d: match_sh.detIdsGEM()){
        auto detId = GEMDetId(d);
        if(verbose) std::cout << "GEMId " << detId << std::endl;
        for (auto p: match_sh.hitsInDetId(d)){
          auto gem_gp = gemGeometry_->idToDet(p.detUnitId())->surface().toGlobal(p.entryPoint());
          double gem_phi = gem_gp.phi();
          int gem_ch = detId.chamber();
          int gem_bx = p.timeOfFlight();
          double gem_z = gem_gp.z();
          if(verbose){
            std::cout << "\tHit " << p << " Position " << gem_phi << std::endl;
          }
          if (detId.station()==1) {
            if (detId.layer()==1) {
              event_.GE11_sim_phi_L1[k] = gem_phi;
              event_.GE11_sim_bx_L1[k] = gem_bx;
              event_.GE11_sim_ch_L1[k] = gem_ch;
              event_.GE11_sim_z_L1[k] = gem_z;
            }
            if (detId.layer()==2) {
              event_.GE11_sim_phi_L2[k] = gem_phi;
              event_.GE11_sim_bx_L2[k] = gem_bx;
              event_.GE11_sim_ch_L2[k] = gem_ch;
              event_.GE11_sim_z_L2[k] = gem_z;
            }
          }
          if (detId.station()==3) {
            if (detId.layer()==1) {
              event_.GE21_sim_phi_L1[k] = gem_phi;
              event_.GE21_sim_bx_L1[k] = gem_bx;
              event_.GE21_sim_ch_L1[k] = gem_ch;
              event_.GE21_sim_z_L1[k] = gem_z;
            }
            if (detId.layer()==2) {
              event_.GE21_sim_phi_L2[k] = gem_phi;
              event_.GE21_sim_bx_L2[k] = gem_bx;
              event_.GE21_sim_ch_L2[k] = gem_ch;
              event_.GE21_sim_z_L2[k] = gem_z;
            }
          }
        } 
      }
      
      if(verbose){
      std::cout << std::endl<<"++++ GEM pad analysis ++++" <<std::endl;
      }
      for (auto d: match_gd.detIdsPad()){
        auto detId = GEMDetId(d);
        if(verbose) std::cout << "Id " << detId << std::endl;
        for (auto p: match_gd.gemPadsInDetId(d)){
          auto gem_gp = match_gd.getGlobalPointPad(d,p);
          double gem_phi = gem_gp.phi();
          //int gem_ch = detId.chamber();
          //int gem_bx = p.bx();
          //double gem_z = gem_gp.z();
          if(verbose){
            std::cout << "\tPad " << p << " Position " << gem_phi << std::endl;
          }
        }
      }
      
      // GEM digis and pads in superchambers
      if(verbose){
        std::cout << std::endl<<"++++ GEM pad analysis ++++" <<std::endl;
      }
      for (auto d: match_gd.detIdsPad()){
        auto detId = GEMDetId(d);
        if(verbose) std::cout << "Id " << detId << std::endl;
        for (auto p: match_gd.gemPadsInDetId(d)){
          auto gem_gp = match_gd.getGlobalPointPad(d,p);
          double gem_phi = gem_gp.phi();
          int gem_ch = detId.chamber();
          int gem_bx = p.bx();
          double gem_z = gem_gp.z();
          if(verbose){
            std::cout << "\tPad " << p << " Position " << gem_phi << std::endl;
          }
          if (detId.station()==1) {
            if (detId.layer()==1) {
              event_.GE11_sim_pad_phi_L1[k] = gem_phi;
              event_.GE11_sim_pad_bx_L1[k] = gem_bx;
              event_.GE11_sim_pad_ch_L1[k] = gem_ch;
              event_.GE11_sim_pad_z_L1[k] = gem_z;
            }
            if (detId.layer()==2) {
              event_.GE11_sim_pad_phi_L2[k] = gem_phi;
              event_.GE11_sim_pad_bx_L2[k] = gem_bx;
              event_.GE11_sim_pad_ch_L2[k] = gem_ch;
              event_.GE11_sim_pad_z_L2[k] = gem_z;
            }
          }
          if (detId.station()==3) {
            if (detId.layer()==1) {
              event_.GE21_sim_pad_phi_L1[k] = gem_phi;
              event_.GE21_sim_pad_bx_L1[k] = gem_bx;
              event_.GE21_sim_pad_ch_L1[k] = gem_ch;
              event_.GE21_sim_pad_z_L1[k] = gem_z;
            }
            if (detId.layer()==2) {
              event_.GE21_sim_pad_phi_L2[k] = gem_phi;
              event_.GE21_sim_pad_bx_L2[k] = gem_bx;
              event_.GE21_sim_pad_ch_L2[k] = gem_ch;
              event_.GE21_sim_pad_z_L2[k] = gem_z;
            }
          }
        } 
      }
      
      // pad positions for GE21...
      if(verbose) std::cout << "++++ GEM pad analysis: pad positions in GE21 ++++" << std::endl;
      for (auto d: match_gd.detIdsDigi(GEMType::GEM_ME21)){
        auto detId = GEMDetId(d);
        if(verbose) std::cout << "GEMId " << detId << std::endl;
        double firstPositionPad1 = match_gd.positionPad1InDetId(d).front().phi();
        double firstPositionPad2 = match_gd.positionPad2InDetId(d).front().phi();
        double firstPositionPad4 = match_gd.positionPad4InDetId(d).front().phi();
        double firstPositionPad8 = match_gd.positionPad8InDetId(d).front().phi();
        if(verbose) {
          std::cout << "firstPositionPad1 " << firstPositionPad1 << std::endl;
          std::cout << "firstPositionPad2 " << firstPositionPad2 << std::endl;
          std::cout << "firstPositionPad4 " << firstPositionPad4 << std::endl;
          std::cout << "firstPositionPad8 " << firstPositionPad8 << std::endl;  
        }
        if (detId.station()==3) {
          if (detId.layer()==1) {
            event_.GE21_sim_pad1_phi_L1[k] = firstPositionPad1; 
            event_.GE21_sim_pad2_phi_L1[k] = firstPositionPad2; 
            event_.GE21_sim_pad4_phi_L1[k] = firstPositionPad4; 
            event_.GE21_sim_pad8_phi_L1[k] = firstPositionPad8; 
          }
          if (detId.layer()==2) {
            event_.GE21_sim_pad1_phi_L2[k] = firstPositionPad1;
            event_.GE21_sim_pad2_phi_L2[k] = firstPositionPad2;
            event_.GE21_sim_pad4_phi_L2[k] = firstPositionPad4;
            event_.GE21_sim_pad8_phi_L2[k] = firstPositionPad8;
          }
        }
      }
      
      
      //SIM based analysis to get the positions - obsolete since I derive the positions using only 
      //DIGI-L1 quantities

    /*
    // CSC digis in chambers
    if(verbose) std::cout<<std::endl<<"++++ CSC digi  and stub analysis ++++"<<std::endl;
    for (auto d: match_csc.chamberIdsLCT()){
      auto detId = CSCDetId(d);
      //if (not (detId.station()!=1 or detId.station()!=2)) continue;
      //if (detId.ring()!=1) continue; // dont consider me1a for this part
      auto cscChamber = cscGeometry_->chamber(detId);
      if(verbose) std::cout << "\tNumber of matching CSC comparator strips " << match_cd.cscComparatorDigisInChamber(d).size() << std::endl;
      if(verbose) std::cout << "\tNumber of matching CSC LCTs " << match_csc.cscLctsInChamber(d).size() << std::endl;
      // if(verbose) for (auto p: match_csc.cscLctsInChamber(d)) std::cout << "\t " <<p << std::endl;
      auto bestMatchingLCT = match_csc.bestCscLctInChamber(detId);
      if(verbose) std::cout << " BEST LCT " << match_csc.bestCscLctInChamber(detId) << std::endl;
      if(verbose) std::cout << "\tNumber of matching CSC CLCTs " << match_csc.cscClctsInChamber(d).size() << std::endl;
      if(verbose) for (auto p: match_csc.cscClctsInChamber(d)) std::cout << "\t " <<p << std::endl;

      std::vector<float> phis;
      std::vector<float> zs;
      std::vector<float> ephis;
      std::vector<float> ezs;
      int keyWireGroup = bestMatchingLCT.getKeyWG();
      float localY = cscChamber->layer(3)->geometry()->yOfWireGroup(keyWireGroup);
      float radius = cscChamber->layer(3)->surface().toGlobal(LocalPoint(0,0,0)).perp() + localY;
      for (int l=1; l<=6; l++){
        CSCDetId l_id(detId.endcap(), detId.station(), detId.ring(), detId.chamber(), l);
        if(verbose) std::cout << "\tCSCId " << l_id << std::endl;
        if(verbose) std::cout << "\tPrinting available comparator strips in detId: " << match_cd.cscComparatorDigisInDetId(l_id.rawId()).size() << std::endl;
        int closestCompDigi = -1;
        double minDist = 99;
        int jj=0;
        double bestz = 99;
        double bestphi = 99;
        for (auto p: match_cd.cscComparatorDigisInDetId(l_id.rawId())){
          float fractional_strip = match_cd.getFractionalStrip(p);
          auto layer_geo = cscChamber->layer(l)->geometry();
          LocalPoint csc_intersect = layer_geo->intersectionOfStripAndWire(fractional_strip, 20);
          GlobalPoint csc_gp = cscGeometry_->idToDet(l_id)->surface().toGlobal(csc_intersect);
          double delta = reco::deltaPhi(csc_gp.phi(), match_sh.simHitsMeanPosition(match_sh.hitsInChamber(d)).phi());
          if (delta<minDist){
            minDist = delta;
            closestCompDigi = jj;
            bestz = csc_gp.z();
            bestphi = csc_gp.phi();
            if(verbose) std::cout << "minDist closestCompDigi bestz bestphi " << " " << minDist 
                                  << " " << closestCompDigi << " " << bestz << " " << bestphi << std::endl;
          }
          ++jj;
        }
        if (minDist<99){
          zs.push_back(bestz);
          ezs.push_back(0);
          phis.push_back(bestphi);
          ephis.push_back(gemvalidation::cscHalfStripWidth(detId)/sqrt(12));
        }
        
        if(verbose) std::cout << std::endl;
      }
      auto compDigis = match_csc.matchingComparatorDigisLCT(detId, bestMatchingLCT);
      if(verbose) std::cout << "Matching compDigis " << compDigis.size() << std::endl;

      float alpha = 0., beta = 0.;
      fitStraightLineErrors(zs, phis, ezs, ephis,
                            alpha, beta, 
                            event_.lumi, event_.run, event_.event, k, 0, produceFitPlots_);
      
      float z_pos_L3 = cscChamber->layer(CSCConstants::KEY_CLCT_LAYER)->centerOfStrip(20).z();
      float bestFitPhi = alpha + beta * z_pos_L3;
      if(verbose) std::cout << "best fit phi position " << z_pos_L3 << " " << bestFitPhi << std::endl;
      
      if (detId.station()==1) {
        event_.CSCTF_fit_phi1[k] = bestFitPhi;
        event_.CSCTF_fit_x1[k] = radius*cos(bestFitPhi);
        event_.CSCTF_fit_y1[k] = radius*sin(bestFitPhi);
        event_.CSCTF_fit_z1[k] = z_pos_L3;
        event_.CSCTF_fit_R1[k] = radius;
      }
      if (detId.station()==2) {
        event_.CSCTF_fit_phi2[k] = bestFitPhi;
        event_.CSCTF_fit_x2[k] = radius*cos(bestFitPhi);
        event_.CSCTF_fit_y2[k] = radius*sin(bestFitPhi);
        event_.CSCTF_fit_z2[k] = z_pos_L3;
        event_.CSCTF_fit_R2[k] = radius;
      }
      if (detId.station()==3) {
        event_.CSCTF_fit_phi3[k] = bestFitPhi;
        event_.CSCTF_fit_x3[k] = radius*cos(bestFitPhi);
        event_.CSCTF_fit_y3[k] = radius*sin(bestFitPhi);
        event_.CSCTF_fit_z3[k] = z_pos_L3;
        event_.CSCTF_fit_R3[k] = radius;
      }
      if (detId.station()==4) {
        event_.CSCTF_fit_phi4[k] = bestFitPhi;
        event_.CSCTF_fit_x4[k] = radius*cos(bestFitPhi);
        event_.CSCTF_fit_y4[k] = radius*sin(bestFitPhi);
        event_.CSCTF_fit_z4[k] = z_pos_L3;
        event_.CSCTF_fit_R4[k] = radius;
      }
    }
    */

      // recover the missing stubs in station 1 and 2... (because they were not used in the track building)
      // GEM digis and pads in superchambers
      if(verbose){
        std::cout << "Total number of matching CSC stubs to simtrack " << std::endl;
        std::cout << "Matching CSC stub Ids " << match_csc.chamberIdsLCT().size() << std::endl;
      }
      for (auto d: match_csc.chamberIdsLCT(0)){
        auto detId = CSCDetId(d);
        auto simhits = match_sh.hitsInChamber(d);
        auto csc_sh_gv = match_sh.simHitsMeanMomentum(simhits);
        if(verbose) {
          std::cout << "\tId " << d << " " << detId << std::endl;
          std::cout << "\tNumber of LCTs " << match_csc.cscLctsInChamber(d).size() << std::endl;
        }
        int nStubs = match_csc.cscLctsInChamber(d).size();
        if (nStubs==0) continue;

        // pick the best matching stub in the chamber
        auto stub = match_csc.bestCscLctInChamber(d);

        std::vector<GlobalPoint> gps;
        std::vector<float> phis;
        std::vector<float> xs;
        std::vector<float> ys;
        std::vector<float> zs;
        std::vector<float> ephis;
        std::vector<float> exs;
        std::vector<float> ezs;
        std::vector<float> status;
 
        match_csc.positionsOfComparatorInLCT(d, stub, gps);
        auto csc_gp = match_csc.getGlobalPosition(d, stub);

        if (gps.size()>=3){
          for (auto gp: gps){
            if (gp.z() > 0)
              zs.push_back(gp.z());
            else zs.push_back(-gp.z());
            xs.push_back(gp.x());
            ys.push_back(gp.y());
            ezs.push_back(0);
            float gpphi = gp.phi();
            if (phis.size()>0 and gpphi>0 and phis[0]<0 and  (gpphi-phis[0])>3.1416)
              phis.push_back(gpphi-2*3.1415926);
            else if (phis.size()>0 and gpphi<0 and phis[0]>0 and (gpphi-phis[0])<-3.1416)
              phis.push_back(gpphi+2*3.1415926);
            else     
              phis.push_back(gp.phi());
            ephis.push_back(gemvalidation::cscHalfStripWidth(detId)/sqrt(12));
            float R=0.0;
            if (detId.ring() == 1 or detId.ring() == 4) R=200;//cm
            if (detId.ring() == 2) R=400;//cm
            exs.push_back(gemvalidation::cscHalfStripWidth(detId)/sqrt(12)*R);
          }
        }else {
          //if (verbose_) std::cout <<" the size of gloabl points in this chamber is less than 3 "<< std::endl;
        }


        float alpha = 0., beta = 0.;
        fitStraightLineErrors(zs, phis, ezs, ephis,
                              alpha, beta, 1, 1, 1, 1, 1, false);
        float alphax = 0., betax = 0.;
        fitStraightLineErrors(zs, xs, ezs, exs,
                              alphax, betax, 1, 1, 1, 1, 1, false);
        float alphay = 0., betay = 0.;
        fitStraightLineErrors(zs, ys, ezs, exs,
                              alphay, betay, 1, 1, 1, 1, 1, false);
        

        double csc_phi = normalizedPhi(alpha+beta*match_csc.zpositionOfLayer(d, 3)); //csc_gp.phi();
        auto gp_new = GlobalPoint(GlobalPoint::Cylindrical(csc_gp.perp(), csc_phi, csc_gp.z()));
        double csc_eta = match_sh.simHitPositionKeyLayer(d).eta();
        double csc_z = csc_gp.z();
        double csc_R = gp_new.perp();
        double csc_x = gp_new.x();
        double csc_y = gp_new.y();
        
        if(verbose){
          std::cout << "\t\tStub " << stub << std::endl;
          std::cout << "\t\t\tPosition " << csc_phi << std::endl;
          std::cout << "\t\t\tDirection " << csc_sh_gv.phi() << std::endl;
        }
        if (detId.station()==1) {
          event_.CSCTF_rec_ch1[k] = detId.chamber();
          event_.CSCTF_rec_phi1[k] = csc_phi;
          event_.CSCTF_rec_eta1[k] = csc_eta;
          event_.CSCTF_rec_phib1[k] = csc_sh_gv.phi();
          event_.CSCTF_rec_x1[k] = csc_x;
          event_.CSCTF_rec_y1[k] = csc_y;
          event_.CSCTF_rec_z1[k] = csc_z;
          event_.CSCTF_rec_R1[k] = csc_R;
        }
        if (detId.station()==2) {
          event_.CSCTF_rec_ch2[k] = detId.chamber();
          event_.CSCTF_rec_phi2[k] = csc_phi;
          event_.CSCTF_rec_eta2[k] = csc_eta;
          event_.CSCTF_rec_phib2[k] = csc_sh_gv.phi();
          event_.CSCTF_rec_x2[k] = csc_x;
          event_.CSCTF_rec_y2[k] = csc_y;
          event_.CSCTF_rec_z2[k] = csc_z;
          event_.CSCTF_rec_R2[k] = csc_R;
        }        
        if (detId.station()==3) {
          event_.CSCTF_rec_ch3[k] = detId.chamber();
          event_.CSCTF_rec_phi3[k] = csc_phi;
          event_.CSCTF_rec_eta3[k] = csc_eta;
          event_.CSCTF_rec_phib3[k] = csc_sh_gv.phi();
          event_.CSCTF_rec_x3[k] = csc_x;
          event_.CSCTF_rec_y3[k] = csc_y;
          event_.CSCTF_rec_z3[k] = csc_z;
          event_.CSCTF_rec_R3[k] = csc_R;
        }        
        if (detId.station()==4) {
          event_.CSCTF_rec_ch4[k] = detId.chamber();
          event_.CSCTF_rec_phi4[k] = csc_phi;
          event_.CSCTF_rec_eta4[k] = csc_eta;
          event_.CSCTF_rec_phib4[k] = csc_sh_gv.phi();
          event_.CSCTF_rec_x4[k] = csc_x;
          event_.CSCTF_rec_y4[k] = csc_y;
          event_.CSCTF_rec_z4[k] = csc_z;
          event_.CSCTF_rec_R4[k] = csc_R;
        }        
      }      
    }
  }
  
  
  /////////////////
  // L1 analysis //
  /////////////////

  if (processTTI_){
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
  }

  if (processTTI_){
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
  }  
  
  if (processDTTF_){
    // store the DTTF variables
    if(verbose) std::cout << std::endl<< "Number of L1DTTrackPhis " <<L1DTTrackPhis.size() << std::endl;
    event_.nDTTF = L1DTTrackPhis.size();
    for (unsigned int j=0; j<L1DTTrackPhis.size(); ++j) { 
      auto track = L1DTTrackPhis[j].first;
      
      event_.DTTF_pt[j] = muPtScale->getPtScale()->getLowEdge(track.pt()) + 1.e-6;
      event_.DTTF_eta[j] = muScales->getRegionalEtaScale(0)->getCenter(track.eta());
      event_.DTTF_phi[j] = phiL1DTTrack(track);
      event_.DTTF_bx[j] = track.bx();
      event_.DTTF_nStubs[j] = L1DTTrackPhis[j].second.size();
      event_.DTTF_quality[j] = track.quality();
      
      if(verbose) {  
        std::cout << std::endl
                  << "pt  = " << event_.DTTF_pt[j]
                  << ", eta  = " << event_.DTTF_eta[j] 
                  << ", phi  = " << event_.DTTF_phi[j]
                  << ", bx = " << event_.DTTF_bx[j] 
                  << ", quality = " << event_.DTTF_quality[j] 
                  << ", nStubs = " << event_.DTTF_nStubs[j]
                  << std::endl;
      }
      
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
      
      // check for stub recovery
      bool stubMissingSt1 = event_.DTTF_st1[j] == 99;
      bool stubMissingSt2 = event_.DTTF_st2[j] == 99;
      bool stubMissingSt3 = event_.DTTF_st3[j] == 99;
      bool stubMissingSt4 = event_.DTTF_st4[j] == 99;
      bool atLeast1StubMissing = stubMissingSt1 or stubMissingSt2 or stubMissingSt3 or stubMissingSt4;
      
      bool doStubRecovery = true;
      if (doStubRecovery and atLeast1StubMissing){
        //std::cout << "DT stub recovery" << std::endl;
        
        int triggerSector = track.spid().sector();
        //std::cout << "trigger sector " << triggerSector << std::endl;
        
        for (auto stub: DTTrackPhis){
          int station = stub.station();
          // check if stub is missing in station
          if (not stubMissingSt1 and station==1) continue;
          if (not stubMissingSt2 and station==2) continue;
          if (not stubMissingSt3 and station==3) continue;
          if (not stubMissingSt4 and station==4) continue;
          
          // stub cannot be used in any other track
          if (stubInDTTFTracks(stub, L1DTTrackPhis)) continue;
          
          // trigger sector must be the same
          if (triggerSector != stub.sector()) continue;
          
          // BXs have to match
          int deltaBX = std::abs(stub.bx() - (event_.DTTF_bx[j]));
          if (deltaBX > 1) continue;
          
          // wheel must be valid!
          int wheel = stub.wheel();
          if (std::abs(wheel) > 2) continue;
          
          // station must be valid!
          if (station < 0 or station > 4) continue;
        
          DTChamberId chId(wheel, station, triggerSector);
          if(verbose) std::cout << chId << std::endl;
          if(verbose) std::cout<<"Candidate " << stub << std::endl;
        }
      }
    }
  }
  

  // store the CSCTF variables
  event_.nCSCTF = l1Tracks.size();
  if(verbose) std::cout << std::endl<< "Number of L1CSCTracks " <<event_.nCSCTF << std::endl;
  for (int j=0; j<event_.nCSCTF; ++j) {
    auto track = l1Tracks[j].first;
    const int sign(track.endcap()==1 ? 1 : -1);
    unsigned gpt = 0, quality = 0;
    csc::L1Track::decodeRank(track.rank(), gpt, quality);

    // calculate pt, eta and phi (don't forget to store the sign)                                                                                   
    event_.CSCTF_pt[j] = muPtScale->getPtScale()->getLowEdge(gpt & 0x1f) + 1.e-6;
    event_.CSCTF_eta[j] = muScales->getRegionalEtaScale(2)->getCenter(track.eta_packed()) * sign;
    event_.CSCTF_phi[j] = normalizedPhi(muScales->getPhiScale()->getLowEdge(phiL1CSCTrack(track)));
    event_.CSCTF_bx[j] = track.bx();
    event_.CSCTF_quality[j] = quality;
    
    if(verbose) {  
      std::cout << std::endl
                << "L1CSC pt  = " << event_.CSCTF_pt[j]
                << ", eta  = " << event_.CSCTF_eta[j] 
                << ", phi  = " << event_.CSCTF_phi[j]
                << ", bx = " << event_.CSCTF_bx[j]
                << ", quality = " << event_.CSCTF_quality[j] 
                << std::endl<< std::endl;
      std::cout << "Print CSCTF stubs:" << std::endl;
    }
    event_.CSCTF_nStubs[j] = 0;
    auto stubCollection(l1Tracks[j].second);
    for (auto detUnitIt = stubCollection.begin(); detUnitIt != stubCollection.end(); detUnitIt++) {
      const CSCDetId& ch_id = (*detUnitIt).first;
      const auto range = (*detUnitIt).second;
      for (auto digiIt = range.first; digiIt != range.second; digiIt++) {
        //if (!(*digiIt).isValid()) continue;
        event_.CSCTF_nStubs[j] += 1;
        auto stub = *digiIt;
        auto gp = getCSCSpecificPoint2(ch_id.rawId(), stub);
        if(verbose)std::cout << "\t" << ch_id << " " << stub 
                             << " GP " << gp
                             << " key eta " << gp.eta() << " key phi " << gp.phi() << std::endl;
        
        // stub position
        
        float z_pos_L3, bestFitPhi, bestFitDPhi;

        fitComparatorsLCT(*hCSCComparators.product(), stub, ch_id, int(digiIt-range.first), z_pos_L3, bestFitPhi, bestFitDPhi);

        fillCSCStubProperties(ch_id, stub, j, gp, z_pos_L3, bestFitPhi, bestFitDPhi);
      }
    }
    
    /* 
    CSCTF stub recovery per CSCTF track
    The CSC track-finder may drop certain stubs if they don't match the pattern
    First get the station numbers where stubs are not filled
    */
    bool stubMissingSt1 = event_.CSCTF_st1[j] == 99;
    bool stubMissingSt2 = event_.CSCTF_st2[j] == 99;
    bool stubMissingSt3 = event_.CSCTF_st3[j] == 99;
    bool stubMissingSt4 = event_.CSCTF_st4[j] == 99;
    bool atLeast1StubMissing = stubMissingSt1 or stubMissingSt2 or stubMissingSt3 or stubMissingSt4;
    
    bool doStubRecovery = true;
    if (doStubRecovery and atLeast1StubMissing){
      
      std::vector<float> xs;
      std::vector<float> ys;
      std::vector<float> zs;
      //std::cout << "Get stub positions" << std::endl;
      getStubPositions(j, xs, ys, zs);
      
      //std::cout << "fit stub positions with straight line" << std::endl;
      float alpha_x, beta_x, alpha_y, beta_y;
      fitStraightLine(zs, xs, alpha_x, beta_x); 
      fitStraightLine(zs, ys, alpha_y, beta_y); 
      
      //std::cout << "Get positions stations" << std::endl;
      std::vector<float> allxs;
      std::vector<float> allys;
      int sign_z = int(event_.CSCTF_eta[j]/std::abs(event_.CSCTF_eta[j]));
      getPositionsStations(alpha_x, beta_x, alpha_y, beta_y,
                           allxs, allys, sign_z);

      
      int triggerSector = track.sector();
      //std::cout << "trigger sector " << triggerSector << std::endl;
      
      for (int endcap=1; endcap<=2; endcap++){
        //do not consider stubs in the wrong endcap
        int zendcap(endcap!=1 ? -1 : +1 );
        if (zendcap * event_.CSCTF_eta[j] < 0) continue;
        for (int station=1; station<=4; station++){
          
          // ignore station where a L1Mu stub is present!
          if (not stubMissingSt1 and station==1) continue;
          if (not stubMissingSt2 and station==2) continue;
          if (not stubMissingSt3 and station==3) continue;
          if (not stubMissingSt4 and station==4) continue;
          if(verbose) std::cout << "Recovered stubs in station: " << station << std::endl;
          // temp storage of candidate stubs per station and ring
          CSCCorrelatedLCTDigiId bestMatchingStub;
          int iStub = 0;
          for (int ring=1; ring<=3; ring++){
            if (station!=1 and ring==3) continue;
            //std::cout << "Analyzing ring " << ring << std::endl;
            
            for (int chamber=1; chamber<=36; chamber++){
              // do not consider invalid detids
              if ( (station==2 or station==3 or station==4) and 
                   (ring==1) and chamber>18) continue;
              //std::cout << "Analyzing chamber " << chamber << std::endl; 
              // create the detid
              CSCDetId ch_id(endcap, station, ring, chamber);
              //std::cout << "ch_id " <<  ch_id << std::endl;
              // get the stubs in this detid
              auto range = CSCCorrelatedLCTs.get(ch_id);
              for (auto digiItr = range.first; digiItr != range.second; ++digiItr){
                iStub++; 

                auto stub(*digiItr);

                // check that this stub is not already part of a CSC TF track
                if (stubInCSCTFTracks(stub, l1Tracks)) continue;

                // trigger sector must be the same
                if (triggerSector != ch_id.triggerSector()) continue;
                
                // BXs have to match
                int deltaBX = std::abs(stub.getBX() - (6 + event_.CSCTF_bx[j]));
                if (deltaBX > 1) continue;

                if(verbose) std::cout << ch_id << std::endl;
                if(verbose) std::cout<<"Candidate " << stub << std::endl;
                bestMatchingStub = pickBestMatchingStub(allxs[ch_id.station()-1], allys[ch_id.station()-1], 
                                                        bestMatchingStub, std::make_pair(ch_id, stub), 6 + event_.CSCTF_bx[j]);
              }
              // consider the case ME1a
              if (station==1 and ring==1){
                CSCDetId me1a_id(endcap, station, 4, chamber);
                auto range = CSCCorrelatedLCTs.get(me1a_id);
                for (auto digiItr = range.first; digiItr != range.second; ++digiItr){
                  iStub++;
                  auto stub(*digiItr);

                  // check that this stub is not already part of a CSC TF track
                  if (stubInCSCTFTracks(stub, l1Tracks)) continue;
                  
                  // trigger sector must be the same
                  if (triggerSector != me1a_id.triggerSector()) continue;
                  
                  // BXs have to match
                  int deltaBX = std::abs(stub.getBX() - (6 + event_.CSCTF_bx[j]));
                  if (deltaBX > 1) continue; 

                  if(verbose) std::cout << me1a_id << std::endl;
                  if(verbose) std::cout<<"Candidate " << stub << std::endl;
                  bestMatchingStub = pickBestMatchingStub(allxs[me1a_id.station()-1], allys[me1a_id.station()-1], 
                                                          bestMatchingStub, std::make_pair(me1a_id, stub), 6 + event_.CSCTF_bx[j]);
                  
                }
              }
            }
          }
          if (bestMatchingStub.second != CSCCorrelatedLCTDigi()) {
            // stub position
            auto gp = getCSCSpecificPoint2(bestMatchingStub.first.rawId(), bestMatchingStub.second);
            if (reco::deltaR(gp.eta(), normalizedPhi(gp.phi()), 
                             event_.CSCTF_eta[j] , normalizedPhi(event_.CSCTF_phi[j])) < 0.2){ 

              if(verbose) {
                std::cout << "\tChoice:" 
                          << bestMatchingStub.first << " " 
                          << bestMatchingStub.second << " " 
                          << "key eta " << gp.eta() << " "
                          << "key phi " << gp.phi() << std::endl;
              }
              
              float z_pos_L3, bestFitPhi, bestFitDPhi;
              fitComparatorsLCT(*hCSCComparators.product(), bestMatchingStub.second, bestMatchingStub.first, j, z_pos_L3, bestFitPhi, bestFitDPhi);
              
              fillCSCStubProperties(bestMatchingStub.first, bestMatchingStub.second, j, 
                                    gp, z_pos_L3, bestFitPhi, bestFitDPhi);
            }
            else{
              if(verbose) if (iStub!=0) std::cout << "\tNone " << std::endl;
            }
          }
          else{
            if(verbose) if (iStub!=0) std::cout << "\tNone " << std::endl;
          }
        }
      } 
    }
    stubMissingSt1 = event_.CSCTF_st1[j] == 99;
    stubMissingSt2 = event_.CSCTF_st2[j] == 99;
    if(verbose) cout << "Stub missing in station 1: " << bool(stubMissingSt1) << endl; 
    if(verbose) cout << "Stub missing in station 2: " << bool(stubMissingSt2) << endl; 
    /*

    std::cout << "Matching copads" << std::endl;
    // Get matching GEM copads

    GEMCSCPadDigiId bestCoPad_GE11;
    GEMCSCPadDigiId bestCoPad_GE21;

    for(auto cItr = hGEMCSCCoPads->begin(); cItr != hGEMCSCCoPads->end(); ++cItr) {
      GEMDetId gem_id = (*cItr).first;
      if (not stubMissingSt1) {
        // get the CSCDetId of station 1
        CSCDetId csc_st1(event_.CSCTF_id1[ j ]);
        std::cout << "CSC " << csc_st1 << endl;
        // chambers need to be compatible
        if (gem_id.station() != 1 or 
            csc_st1.chamber() != gem_id.chamber() or
            (csc_st1.ring() != 4 and csc_st1.ring() != 1)) continue;
        std::cout << "Investigate GE11 chamber " << gem_id << std::endl;
        // get the copads
        auto copad_range = (*cItr).second;
        for (auto digiItr = copad_range.first; digiItr != copad_range.second; ++digiItr){
          auto copad(*digiItr);
          std::cout << "\tCandidate copad " << copad  << std::endl;
          bestCoPad_GE11 = pickBestMatchingCoPad(event_.CSCTF_fit_x1[ j ],
                                                 event_.CSCTF_fit_y1[ j ], 
                                                 bestCoPad_GE11, std::make_pair(gem_id, copad), event_.CSCTF_bx[j]);
        }
      }
      if (not stubMissingSt2) {
        // get the CSCDetId of station 1
        CSCDetId csc_st2(event_.CSCTF_id2[ j ]);
        std::cout << "CSC " << csc_st2 << endl;
        // chambers need to be compatible
        if (gem_id.station() != 3 or 
            csc_st2.chamber() != gem_id.chamber() or
            csc_st2.ring() != 1) continue;
        std::cout << "Investigate GE21 chamber " << gem_id << std::endl;
        // get the copads
        auto copad_range = (*cItr).second;
        for (auto digiItr = copad_range.first; digiItr != copad_range.second; ++digiItr){
          auto copad(*digiItr);
          std::cout << "\tCandidate copad " << copad  << std::endl;
          bestCoPad_GE21 = pickBestMatchingCoPad(event_.CSCTF_fit_x2[ j ],
                                                 event_.CSCTF_fit_y2[ j ], 
                                                 bestCoPad_GE21, std::make_pair(gem_id, copad), event_.CSCTF_bx[j]);
        }
      }
    }
    // found copad is not empty
    if (bestCoPad_GE11.second != GEMCSCPadDigi()){
      std::cout << "\tBest GE11 copad" << bestCoPad_GE11.second << std::endl;
      if (bestCoPad_GE11.first.station()==1) {
        auto gem_gp1 = getGlobalPointPad(bestCoPad_GE11.first, bestCoPad_GE11.second);
        event_.GE11_phi_L1[j] = gem_gp1.phi();
        event_.GE11_bx_L1[j] = bestCoPad_GE11.second.bx();
        event_.GE11_ch_L1[j] = bestCoPad_GE11.first.chamber();
        event_.GE11_z_L1[j] = gem_gp1.z();
      }
    } else {
      std::cout << "No best GE11 copad" << std::endl;
    }
    
    if (bestCoPad_GE21.second != GEMCSCPadDigi()){
      std::cout << "\tBest GE21 copad" << bestCoPad_GE21.second << std::endl;
      if (bestCoPad_GE21.first.station()==2) {
        auto gem_gp1 = getGlobalPointPad(bestCoPad_GE21.first, bestCoPad_GE21.second);
        event_.GE21_phi_L1[j] = gem_gp1.phi();
        event_.GE21_bx_L1[j] = bestCoPad_GE21.second.bx();
        event_.GE21_ch_L1[j] = bestCoPad_GE21.first.chamber();
        event_.GE21_z_L1[j] = gem_gp1.z();
      }
    } else {
      std::cout << "No best GE21 copad" << std::endl;
    } 
    
    

    // check copads were matched
    const bool GE11_copad_matched( event_.GE11_phi_L1[j]!=99 );
    const bool GE21_copad_matched( event_.GE21_phi_L1[j]!=99 );
    */

    if(verbose) std::cout << "Matching pads" << std::endl;
    // Get matching GEM pads
    if (true){
      //( (not GE11_copad_matched) or  (not GE21_copad_matched) )
      GEMCSCPadDigiId bestPad_GE11_L1;
      GEMCSCPadDigiId bestPad_GE11_L2;
      GEMCSCPadDigiId bestPad_GE21_L1;
      GEMCSCPadDigiId bestPad_GE21_L2;
      
      for(auto cItr = hGEMCSCPads->begin(); cItr != hGEMCSCPads->end(); ++cItr) {
        GEMDetId gem_id = (*cItr).first;
        //cout << "Check GEMDetId " << gem_id << endl;
        //float bestGEMCSCDPhi = 99;
        if (not stubMissingSt1) {// and not GE11_copad_matched
          // get the CSCDetId of station 1
          CSCDetId csc_st1(event_.CSCTF_id1[ j ]);
          
          // chambers need to be compatible
          if (gem_id.region() == csc_st1.zendcap() and 
              gem_id.station() == 1 and 
              csc_st1.chamber() == gem_id.chamber() and
              (csc_st1.ring() == 4 or csc_st1.ring() == 1)) {
            if(verbose) std::cout << "Investigate GE11 chamber " << gem_id << std::endl;
            // get the pads
            auto pad_range = (*cItr).second;
            for (auto digiItr = pad_range.first; digiItr != pad_range.second; ++digiItr){
              auto GE11_pad(*digiItr);
              int deltaBX = std::abs(GE11_pad.bx() - event_.CSCTF_bx[j]);
              if (deltaBX <= 1) {
              
                if(verbose) std::cout << "\tCandidate Pad " << GE11_pad  << " " << getGlobalPointPad(gem_id.rawId(), GE11_pad) << std::endl;
                if (gem_id.layer()==1){
                  // BXs have to match
                  
                  bestPad_GE11_L1 = pickBestMatchingPad(event_.CSCTF_fit_x1[ j ],
                                                        event_.CSCTF_fit_y1[ j ], 
                                                        bestPad_GE11_L1, std::make_pair(gem_id, GE11_pad), event_.CSCTF_bx[j]);
                }
                if (gem_id.layer()==2){
                  bestPad_GE11_L2 = pickBestMatchingPad(event_.CSCTF_fit_x1[ j ],
                                                        event_.CSCTF_fit_y1[ j ], 
                                                        bestPad_GE11_L2, std::make_pair(gem_id, GE11_pad), event_.CSCTF_bx[j]);
                }
              }
            }
          }
        }
        if (not stubMissingSt2) {// and not GE21_copad_matched
           // get the CSCDetId of station 1
          CSCDetId csc_st2(event_.CSCTF_id2[ j ]);
          //int index = i;
          // chambers need to be compatible
          if (gem_id.region() == csc_st2.zendcap() and
              gem_id.station() == 3 and 
              csc_st2.chamber() == gem_id.chamber() and
              csc_st2.ring() == 1) {
            if(verbose) std::cout << "Investigate GE21 chamber " << gem_id << std::endl;
            // get the pads
            auto pad_range = (*cItr).second;
            for (auto digiItr = pad_range.first; digiItr != pad_range.second; ++digiItr){
              auto pad(*digiItr);
              int deltaBX = std::abs(pad.bx() - event_.CSCTF_bx[j]);
              if (deltaBX <= 1) {
                if(verbose) std::cout << "\tCandidate Pad " << pad  << " " << getGlobalPointPad(gem_id.rawId(), pad)  << std::endl;
                if (gem_id.layer()==1){
                  bestPad_GE21_L1 = pickBestMatchingPad(event_.CSCTF_fit_x2[ j ],
                                                        event_.CSCTF_fit_y2[ j ], 
                                                        bestPad_GE21_L1, std::make_pair(gem_id, pad), event_.CSCTF_bx[j]);
                }
                if (gem_id.layer()==2){
                  bestPad_GE21_L2 = pickBestMatchingPad(event_.CSCTF_fit_x2[ j ],
                                                        event_.CSCTF_fit_y2[ j ], 
                                                        bestPad_GE21_L2, std::make_pair(gem_id, pad), event_.CSCTF_bx[j]);
                }     
              }
            }
          }
        }
      }
      // found pad is not empty
      if (bestPad_GE11_L1.second != GEMCSCPadDigi()){
        if(verbose) std::cout << "Best pad GE11 L1" << bestPad_GE11_L1.second << std::endl;
        if (bestPad_GE11_L1.first.station()==1 and bestPad_GE11_L1.first.layer()==1) {
          auto gem_gp1 = getGlobalPointPad(bestPad_GE11_L1.first, bestPad_GE11_L1.second);
          if(verbose) cout << "\t"<<gem_gp1<< " " << gem_gp1.phi() << endl;
          event_.GE11_phi_L1[j] = gem_gp1.phi();
          event_.GE11_bx_L1[j] = bestPad_GE11_L1.second.bx();
          event_.GE11_ch_L1[j] = bestPad_GE11_L1.first.chamber();
          event_.GE11_z_L1[j] = gem_gp1.z();              
        }
      } else {
        if(verbose) std::cout << "No best pad GE11 L1" << std::endl;
      }
      
      if (bestPad_GE11_L2.second != GEMCSCPadDigi()){
        if(verbose) std::cout << "Best pad GE11 L2" << bestPad_GE11_L2.second << std::endl;
        if (bestPad_GE11_L2.first.station()==1 and bestPad_GE11_L2.first.layer()==2) {
          auto gem_gp1 = getGlobalPointPad(bestPad_GE11_L2.first, bestPad_GE11_L2.second);
          if(verbose) cout << "\t"<<gem_gp1<<" " << gem_gp1.phi() << endl;
          event_.GE11_phi_L2[j] = gem_gp1.phi();
          event_.GE11_bx_L2[j] = bestPad_GE11_L2.second.bx();
          event_.GE11_ch_L2[j] = bestPad_GE11_L2.first.chamber();
          event_.GE11_z_L2[j] = gem_gp1.z();              
        }
      } else {
        if(verbose) std::cout << "No best pad GE11 L2" << std::endl;
      }
      // found pad is not empty
      if (bestPad_GE21_L1.second != GEMCSCPadDigi()){
        if(verbose) std::cout << "Best pad GE21 L1" << bestPad_GE21_L1.second << std::endl;
        if (bestPad_GE21_L1.first.station()==3 and bestPad_GE21_L1.first.layer()==1) {
          auto gem_gp1 = getGlobalPointPad(bestPad_GE21_L1.first, bestPad_GE21_L1.second);
          if(verbose) cout << "\t"<<gem_gp1<<" " << gem_gp1.phi() << endl;
          event_.GE21_phi_L1[j] = gem_gp1.phi();
          event_.GE21_bx_L1[j] = bestPad_GE21_L1.second.bx();
          event_.GE21_ch_L1[j] = bestPad_GE21_L1.first.chamber();
          event_.GE21_z_L1[j] = gem_gp1.z();              
        }
      } else {
        if(verbose) std::cout << "No best pad GE21 L1" << std::endl;
      }
      
      if (bestPad_GE21_L2.second != GEMCSCPadDigi()){
        if(verbose) std::cout << "Best pad GE21 L2" << bestPad_GE21_L2.second << std::endl;
        if (bestPad_GE21_L2.first.station()==3 and bestPad_GE21_L2.first.layer()==2) {
          auto gem_gp1 = getGlobalPointPad(bestPad_GE21_L2.first, bestPad_GE21_L2.second);
          if(verbose) cout << "\t"<<gem_gp1<<" " << gem_gp1.phi() << endl;
          event_.GE21_phi_L2[j] = gem_gp1.phi();
          event_.GE21_bx_L2[j] = bestPad_GE21_L2.second.bx();
          event_.GE21_ch_L2[j] = bestPad_GE21_L2.first.chamber();
          event_.GE21_z_L2[j] = gem_gp1.z();              
        }
      } else {
        if(verbose) std::cout << "No best pad GE21 L2" << std::endl;
      }

      // pads with smaller sizes in GE21
      /*
      if (not stubMissingSt1){
        std::vector<GlobalPoint> positionPadsGE11 = positionPad2InDetId(GEMDigis, event_.CSCTF_id1[j], event_.CSCTF_bx[j]);
        std::cout << "Check positions of 2-strip pads for " << CSCDetId(event_.CSCTF_id1[j]) << " in BX " << event_.CSCTF_bx[j] << std::endl;
        std::cout << "GE11: " << std::endl;
        for (auto p: positionPadsGE11) std::cout << p << " " << p.phi() << std::endl; 

        std::vector<GlobalPoint> positionPads4GE11 = positionPad4InDetId(GEMDigis, event_.CSCTF_id1[j], event_.CSCTF_bx[j]);
        std::cout << "Check positions of 4-strip pads for " << CSCDetId(event_.CSCTF_id1[j]) << " in BX " << event_.CSCTF_bx[j] << std::endl;
        std::cout << "GE11: " << std::endl;
        for (auto p: positionPads4GE11) std::cout << p << " " << p.phi() << std::endl;
      }
      */
      if (not stubMissingSt2){
        std::vector<GlobalPoint> positionPadsGE21 = positionPad2InDetId(GEMDigis, event_.CSCTF_id2[j], event_.CSCTF_bx[j]);
        //std::cout << "Check positions of 2-strip pads for " << CSCDetId(event_.CSCTF_id2[j]) << " in BX " << event_.CSCTF_bx[j] << std::endl;
        //std::cout << "GE21: " << std::endl;
        float minDPhi_L1=99, minDPhi_L2=992; 
        
        for (auto p: positionPadsGE21){
          // L1
          if ( std::abs(p.z() - 794.439) < 0.0001 or std::abs(p.z() + 794.439) < 0.0001 ) {
            float dPhiGEMCSC(std::abs(reco::deltaPhi(event_.CSCTF_fit_phi2[j], p.phi())));
            if (dPhiGEMCSC  < minDPhi_L1) {
              minDPhi_L1 = dPhiGEMCSC;
              event_.GE21_pad2_phi_L1[j] = p.phi();
            }
          } 
          // L2
          if ( std::abs(p.z() - 798.179) < 0.0001 or std::abs(p.z() + 798.179) < 0.0001 ) {
            float dPhiGEMCSC(std::abs(reco::deltaPhi(event_.CSCTF_fit_phi2[j], p.phi())));
            if (dPhiGEMCSC  < minDPhi_L2) {
              minDPhi_L2 = dPhiGEMCSC;
              event_.GE21_pad2_phi_L2[j] = p.phi();            
            }
          }
        }        
        // std::vector<GlobalPoint> positionPads4GE21 = positionPad4InDetId(GEMDigis, event_.CSCTF_id2[j], event_.CSCTF_bx[j]);
        // std::cout << "Check positions of 4-strip pads for " << CSCDetId(event_.CSCTF_id2[j]) << " in BX " << event_.CSCTF_bx[j] << std::endl;
        // std::cout << "GE21: " << std::endl;
        // for (auto p: positionPads4GE21) std::cout << p << " " << p.phi() << std::endl;
      }
    } // check if match to pads
  } // loop on csctf tracks

  // Store the RPCb variables
  if(verbose) std::cout << "Number of l1MuRPCbs: " <<l1MuRPCbs.size() << std::endl;
  event_.nRPCb = l1MuRPCbs.size();
  if (processRPCb_) {
    for (unsigned int j=0; j<l1MuRPCbs.size(); ++j) { 
      auto track = l1MuRPCbs[j];
      
      event_.RPCb_pt[j] = muPtScale->getPtScale()->getLowEdge(track.pt_packed());
      event_.RPCb_eta[j] = muScales->getRegionalEtaScale(track.type_idx())->getCenter(track.eta_packed());
      event_.RPCb_phi[j] = normalizedPhi(muScales->getPhiScale()->getLowEdge(track.phi_packed()));
      event_.RPCb_bx[j] = track.bx();
      event_.RPCb_quality[j] = track.quality();
      
      if(verbose) {  
        std::cout << "pt " << event_.RPCb_pt[j]
                  << ", eta " << event_.RPCb_eta[j]
                  << ", phi " << event_.RPCb_phi[j]
                  << ", bx " << event_.RPCb_bx[j]
                  << ", quality " << event_.RPCb_quality[j]
                  << std::endl;
      }
      
      auto link = l1MuRPCbLinks[j];
      event_.RPCb_nStubs[j] = 0;
      for (unsigned int ii=1; ii<=link.nlayer(); ++ii){
        if (link.empty(ii)) continue;
        event_.RPCb_nStubs[j] += 1;
        double phi = getGlobalPhi(link.rawdetId(ii), link.strip(ii));
        auto detId = RPCDetId(link.rawdetId(ii));
        if(verbose) {  
          std::cout << "\t" << ii 
                    << ", RPCDetId " << detId 
                    << ", strip " << link.strip(ii) 
                    << ", bx " << link.bx(ii) 
                    << ", phi " << phi
                    << std::endl;
        } 
        switch(ii) {
        case 1:
          event_.RPCb_bx1[j] = link.bx(ii); 
          event_.RPCb_strip1[j] = link.strip(ii); 
          event_.RPCb_phi1[j] = phi;
          event_.RPCb_re1[j] = detId.region(); 
          event_.RPCb_ri1[j] = detId.ring(); 
          event_.RPCb_st1[j] = detId.station(); 
          event_.RPCb_se1[j] = detId.sector();
          event_.RPCb_la1[j] = detId.layer(); 
          event_.RPCb_su1[j] = detId.subsector(); 
          event_.RPCb_ro1[j] = detId.roll();
          break;
        case 2:
          event_.RPCb_bx2[j] = link.bx(ii); 
          event_.RPCb_strip2[j] = link.strip(ii); 
          event_.RPCb_phi2[j] = phi;
          event_.RPCb_re2[j] = detId.region(); 
          event_.RPCb_ri2[j] = detId.ring(); 
          event_.RPCb_st2[j] = detId.station(); 
          event_.RPCb_se2[j] = detId.sector();
          event_.RPCb_la2[j] = detId.layer(); 
          event_.RPCb_su2[j] = detId.subsector(); 
          event_.RPCb_ro2[j] = detId.roll();
          break;
        case 3:
          event_.RPCb_bx3[j] = link.bx(ii); 
          event_.RPCb_strip3[j] = link.strip(ii); 
          event_.RPCb_phi3[j] = phi;
          event_.RPCb_re3[j] = detId.region(); 
          event_.RPCb_ri3[j] = detId.ring(); 
          event_.RPCb_st3[j] = detId.station(); 
          event_.RPCb_se3[j] = detId.sector();
          event_.RPCb_la3[j] = detId.layer(); 
          event_.RPCb_su3[j] = detId.subsector(); 
          event_.RPCb_ro3[j] = detId.roll();
          break;
        case 4:
          event_.RPCb_bx4[j] = link.bx(ii); 
          event_.RPCb_strip4[j] = link.strip(ii); 
          event_.RPCb_phi4[j] = phi;
          event_.RPCb_re4[j] = detId.region(); 
          event_.RPCb_ri4[j] = detId.ring(); 
          event_.RPCb_st4[j] = detId.station(); 
          event_.RPCb_se4[j] = detId.sector();
          event_.RPCb_la4[j] = detId.layer(); 
          event_.RPCb_su4[j] = detId.subsector(); 
          event_.RPCb_ro4[j] = detId.roll();
          break;
        case 5:
          event_.RPCb_bx5[j] = link.bx(ii); 
          event_.RPCb_strip5[j] = link.strip(ii); 
          event_.RPCb_phi5[j] = phi;
          event_.RPCb_re5[j] = detId.region(); 
          event_.RPCb_ri5[j] = detId.ring(); 
          event_.RPCb_st5[j] = detId.station(); 
          event_.RPCb_se5[j] = detId.sector();
          event_.RPCb_la5[j] = detId.layer(); 
          event_.RPCb_su5[j] = detId.subsector(); 
          event_.RPCb_ro5[j] = detId.roll();
          break;
        case 6:
          event_.RPCb_bx6[j] = link.bx(ii); 
          event_.RPCb_strip6[j] = link.strip(ii); 
          event_.RPCb_phi6[j] = phi;
          event_.RPCb_re6[j] = detId.region(); 
          event_.RPCb_ri6[j] = detId.ring(); 
          event_.RPCb_st6[j] = detId.station(); 
          event_.RPCb_se6[j] = detId.sector();
          event_.RPCb_la6[j] = detId.layer(); 
          event_.RPCb_su6[j] = detId.subsector(); 
          event_.RPCb_ro6[j] = detId.roll();
          break;
        };
      } 
    }
  }


  // Store the RPCf variables
  if(verbose) std::cout << "Number of l1MuRPCfs: " <<l1MuRPCfs.size() << std::endl;
  event_.nRPCf = l1MuRPCfs.size();
  if (processRPCf_) {
    for (unsigned int j=0; j<l1MuRPCfs.size(); ++j) { 
      auto track = l1MuRPCfs[j];
      
      event_.RPCf_pt[j] = muPtScale->getPtScale()->getLowEdge(track.pt_packed());
      event_.RPCf_eta[j] = muScales->getRegionalEtaScale(track.type_idx())->getCenter(track.eta_packed());
      event_.RPCf_phi[j] = normalizedPhi(muScales->getPhiScale()->getLowEdge(track.phi_packed()));
      event_.RPCf_bx[j] = track.bx();
      event_.RPCf_quality[j] = track.quality();
      
      if(verbose) {  
        std::cout << "pt " << event_.RPCf_pt[j]
                  << ", eta " << event_.RPCf_eta[j]
                  << ", phi " << event_.RPCf_phi[j]
                  << ", bx " << event_.RPCf_bx[j]
                  << ", quality " << event_.RPCf_quality[j]
                  << std::endl;
      }
      
      auto link = l1MuRPCfLinks[j];
      event_.RPCf_nStubs[j] = 0;
      for (unsigned int ii=1; ii<=link.nlayer(); ++ii){
        if (link.empty(ii)) continue;
        event_.RPCf_nStubs[j] += 1;
        double phi = getGlobalPhi(link.rawdetId(ii), link.strip(ii));
        auto detId = RPCDetId(link.rawdetId(ii));
        if(verbose) {  
          std::cout << "\t" << ii
                    << ", RPCDetId " << detId 
                    << ", strip " << link.strip(ii) 
                    << ", bx " << link.bx(ii) 
                    << ", phi " << phi
                    << std::endl;
        } 
        switch(ii) {
        case 1:
          event_.RPCf_bx1[j] = link.bx(ii); 
          event_.RPCf_strip1[j] = link.strip(ii); 
          event_.RPCf_phi1[j] = phi;
          event_.RPCf_re1[j] = detId.region(); 
          event_.RPCf_ri1[j] = detId.ring(); 
          event_.RPCf_st1[j] = detId.station(); 
          event_.RPCf_se1[j] = detId.sector();
          event_.RPCf_la1[j] = detId.layer(); 
          event_.RPCf_su1[j] = detId.subsector(); 
          event_.RPCf_ro1[j] = detId.roll();
          break;
        case 2:
          event_.RPCf_bx2[j] = link.bx(ii); 
          event_.RPCf_strip2[j] = link.strip(ii); 
          event_.RPCf_phi2[j] = phi;
          event_.RPCf_re2[j] = detId.region(); 
          event_.RPCf_ri2[j] = detId.ring(); 
          event_.RPCf_st2[j] = detId.station(); 
          event_.RPCf_se2[j] = detId.sector();
          event_.RPCf_la2[j] = detId.layer(); 
          event_.RPCf_su2[j] = detId.subsector(); 
          event_.RPCf_ro2[j] = detId.roll();
          break;
        case 3:
          event_.RPCf_bx3[j] = link.bx(ii); 
          event_.RPCf_strip3[j] = link.strip(ii); 
          event_.RPCf_phi3[j] = phi;
          event_.RPCf_re3[j] = detId.region(); 
          event_.RPCf_ri3[j] = detId.ring(); 
          event_.RPCf_st3[j] = detId.station(); 
          event_.RPCf_se3[j] = detId.sector();
          event_.RPCf_la3[j] = detId.layer(); 
          event_.RPCf_su3[j] = detId.subsector(); 
          event_.RPCf_ro3[j] = detId.roll();
          break;
        case 4:
          event_.RPCf_bx4[j] = link.bx(ii); 
          event_.RPCf_strip4[j] = link.strip(ii); 
          event_.RPCf_phi4[j] = phi;
          event_.RPCf_re4[j] = detId.region(); 
          event_.RPCf_ri4[j] = detId.ring(); 
          event_.RPCf_st4[j] = detId.station(); 
          event_.RPCf_se4[j] = detId.sector();
          event_.RPCf_la4[j] = detId.layer(); 
          event_.RPCf_su4[j] = detId.subsector(); 
          event_.RPCf_ro4[j] = detId.roll();
          break;
        case 5:
          event_.RPCf_bx5[j] = link.bx(ii); 
          event_.RPCf_strip5[j] = link.strip(ii); 
          event_.RPCf_phi5[j] = phi;
          event_.RPCf_re5[j] = detId.region(); 
          event_.RPCf_ri5[j] = detId.ring(); 
          event_.RPCf_st5[j] = detId.station(); 
          event_.RPCf_se5[j] = detId.sector();
          event_.RPCf_la5[j] = detId.layer(); 
          event_.RPCf_su5[j] = detId.subsector(); 
          event_.RPCf_ro5[j] = detId.roll();
          break;
        case 6:
          event_.RPCf_bx6[j] = link.bx(ii); 
          event_.RPCf_strip6[j] = link.strip(ii); 
          event_.RPCf_phi6[j] = phi;
          event_.RPCf_re6[j] = detId.region(); 
          event_.RPCf_ri6[j] = detId.ring(); 
          event_.RPCf_st6[j] = detId.station(); 
          event_.RPCf_se6[j] = detId.sector();
          event_.RPCf_la6[j] = detId.layer(); 
          event_.RPCf_su6[j] = detId.subsector(); 
          event_.RPCf_ro6[j] = detId.roll();
          break;
        };
      } 
    }
  }


  // Store the L1Mu variables
  // also check which DTTF, CSCTF, RPCf, RPCb this L1Mu corresponds to!
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
    
    if (processTTI_){
      // Matching to DTTF
      double bestDrL1MuL1DTTrack = 99;
      for (unsigned int j=0; j<L1DTTrackPhis.size(); ++j) {   
        if ( ( event_.L1Mu_quality[i] > 0 ) &&
             ( reco::deltaPhi( event_.L1Mu_phi[i], event_.DTTF_phi[j] ) < 0.001 ) &&             
             ( event_.L1Mu_bx[i] == event_.DTTF_bx[j] ) ) {
          double drL1MuL1DTTrack = reco::deltaR(l1Mu.etaValue(), 
                                                normalizedPhi(l1Mu.phiValue()), 
                                                event_.DTTF_eta[j], 
                                                event_.DTTF_phi[j]);
          if (drL1MuL1DTTrack < bestDrL1MuL1DTTrack and drL1MuL1DTTrack < 0.3) {
            bestDrL1MuL1DTTrack = drL1MuL1DTTrack;
            event_.L1Mu_DTTF_index[i] = j;
          }
        }
      }
      
      if(verbose) {  
        int tempIndex = event_.L1Mu_DTTF_index[i]; 
        if (tempIndex != -1) { // and bestDrL1MuL1DTTrack < 0.2
          // Print matching DTTF track
          std::cout << "\tMatching DTTF track" << std::endl;
          std::cout << "\tpt = "  << event_.DTTF_pt[tempIndex]
                    << ", eta = " << event_.DTTF_eta[tempIndex]
                    << ", phi = " << event_.DTTF_phi[tempIndex] 
                    << ", bx = "  << event_.DTTF_bx[tempIndex]
                    << ", quality = " << event_.DTTF_quality[tempIndex] << std::endl;
          
          // Print stubs
          std::cout << "\tNumber of stubs: " << event_.DTTF_nStubs[tempIndex] << std::endl; 
          for (auto stub: L1DTTrackPhis[tempIndex].second) {
            std::cout << "\t\t " << stub << std::endl;
            std::cout << "\t\t phiValue = " << stub.phiValue() << ", phibValue = " << stub.phibValue() << std::endl;
          }  
        }
        else {
          std::cout << "\tNo matching DTTF track" << std::endl;
        }
      }
    }
    
    // Matching to CSCTF     
    double bestDrL1MuL1CSCTrack = 99;
    for (unsigned int j=0; j<l1Tracks.size(); ++j) {
      if ( ( event_.L1Mu_quality[i] > 0 ) &&
           ( reco::deltaPhi( event_.L1Mu_phi[i], event_.CSCTF_phi[j] ) < 0.001 ) &&             
           ( event_.L1Mu_bx[i] == event_.CSCTF_bx[j] ) ) {
        double drL1MuL1CSCTrack = reco::deltaR(l1Mu.etaValue(), 
                                               normalizedPhi(l1Mu.phiValue()), 
                                               event_.CSCTF_eta[j], 
                                               event_.CSCTF_phi[j]);
        if (drL1MuL1CSCTrack < bestDrL1MuL1CSCTrack and drL1MuL1CSCTrack < 0.3) {
          bestDrL1MuL1CSCTrack = drL1MuL1CSCTrack;
          event_.L1Mu_CSCTF_index[i] = j;
        }
      }                
    }
    

    if(verbose) {  
      int tempIndex = event_.L1Mu_CSCTF_index[i]; 
      if (tempIndex != -1) { // and bestDrL1MuL1CSCTrack < 0.2
        // Print matching CSCTF track
        std::cout << "\tMatching CSCTF track" << std::endl;
        std::cout << "\tpt = "  << event_.CSCTF_pt[tempIndex]
                  << ", eta = " << event_.CSCTF_eta[tempIndex]
                  << ", phi = " << event_.CSCTF_phi[tempIndex]
                  << ", bx = "  << event_.CSCTF_bx[tempIndex]
                  << ", quality = " << event_.CSCTF_quality[tempIndex]
                  << std::endl;
        //printCSCStubProperties(tempIndex);

        // // Print stubs
        // std::cout << "\tNumber of stubs: " << event_.CSCTF_nStubs[tempIndex] << std::endl;
        // auto stubCollection(l1Tracks[tempIndex].second);
        // for (auto detUnitIt = stubCollection.begin(); detUnitIt != stubCollection.end(); detUnitIt++) {
        //   const CSCDetId& id = (*detUnitIt).first;
        //   std::cout << "\t\tDetId " << id << std::endl;
        //   const auto range = (*detUnitIt).second;
        //   for (auto digiIt = range.first; digiIt != range.second; digiIt++) {
        //     //if (!(*digiIt).isValid()) continue;
        //     GlobalPoint csc_gp = getCSCSpecificPoint2(id.rawId(), *digiIt);
        //     std::cout << "\t\tPosition " << csc_gp.eta() << " " << csc_gp.phi() << std::endl;
        //     std::cout << "\t\t" << *digiIt << std::endl;
        //   }
        // }
      }
      else {
        std::cout << "\tNo matching CSCTF track" << std::endl;
      }
    }

    /* 
       CSCTF stub recovery
       The CSC track-finder may drop certain stubs if they don't match the pattern
       First get the station numbers where stubs are not filled
    */
    // std::cout << "CSC stub recovery" << std::endl;
    if (event_.L1Mu_CSCTF_index[i] != -1 and false) {
      bool stubMissingSt1 = event_.CSCTF_st1[ event_.L1Mu_CSCTF_index[i] ] == 99;
      bool stubMissingSt2 = event_.CSCTF_st2[ event_.L1Mu_CSCTF_index[i] ] == 99;
      bool stubMissingSt3 = event_.CSCTF_st3[ event_.L1Mu_CSCTF_index[i] ] == 99;
      bool stubMissingSt4 = event_.CSCTF_st4[ event_.L1Mu_CSCTF_index[i] ] == 99;
      bool doStubRecovery = stubMissingSt1 or stubMissingSt2 or stubMissingSt3 or stubMissingSt4;
      
      std::vector<float> xs;
      std::vector<float> ys;
      std::vector<float> zs;
      std::cout << "Get stub positions" << std::endl;
      getStubPositions(event_.L1Mu_CSCTF_index[i], xs, ys, zs);
      
      std::cout << "fit stub positions with straight line" << std::endl;
      float alpha_x, beta_x, alpha_y, beta_y;
      fitStraightLine(zs, xs, alpha_x, beta_x); 
      fitStraightLine(zs, ys, alpha_y, beta_y); 

      std::cout << "Get positions stations" << std::endl;
      std::vector<float> allxs;
      std::vector<float> allys;
      int sign_z = int(event_.L1Mu_eta[i]/std::abs(event_.L1Mu_eta[i]));
      getPositionsStations(alpha_x, beta_x, alpha_y, beta_y,
                           allxs, allys, sign_z);

      event_.CSCTF_fitline_x1[ event_.L1Mu_CSCTF_index[i] ] = allxs[0];
      event_.CSCTF_fitline_x2[ event_.L1Mu_CSCTF_index[i] ] = allxs[1];
      event_.CSCTF_fitline_x3[ event_.L1Mu_CSCTF_index[i] ] = allxs[2];
      event_.CSCTF_fitline_x4[ event_.L1Mu_CSCTF_index[i] ] = allxs[3];

      event_.CSCTF_fitline_y1[ event_.L1Mu_CSCTF_index[i] ] = allys[0];
      event_.CSCTF_fitline_y2[ event_.L1Mu_CSCTF_index[i] ] = allys[1];
      event_.CSCTF_fitline_y3[ event_.L1Mu_CSCTF_index[i] ] = allys[2];
      event_.CSCTF_fitline_y4[ event_.L1Mu_CSCTF_index[i] ] = allys[3];

      if (doStubRecovery and event_.L1Mu_CSCTF_index[i] != -1) {
        int triggerSector = (l1Tracks[ event_.L1Mu_CSCTF_index[i] ].first).sector();
        std::cout << "trigger sector " << triggerSector << std::endl;
        
        for (int endcap=1; endcap<=2; endcap++){
          //do not consider stubs in the wrong endcap
          int zendcap(endcap!=1 ? -1 : +1 );
          if (zendcap * event_.L1Mu_eta[i] < 0) continue;
          for (int station=1; station<=4; station++){
            
            // ignore station where a L1Mu stub is present!
            if (not stubMissingSt1 and station==1) continue;
            if (not stubMissingSt2 and station==2) continue;
            if (not stubMissingSt3 and station==3) continue;
            if (not stubMissingSt4 and station==4) continue;
            std::cout << "Attempt recovery  in station " << station << std::endl;
            // temp storage of candidate stubs per station and ring
            CSCCorrelatedLCTDigiId bestMatchingStub;
            int iStub = 0;
            for (int ring=1; ring<=3; ring++){
              if (station!=1 and ring==3) continue;
              std::cout << "Analyzing ring " << ring << std::endl;
              
              for (int chamber=1; chamber<=36; chamber++){
                // do not consider invalid detids
                if ( (station==2 or station==3 or station==4) and 
                     (ring==1) and chamber>18) continue;
                //std::cout << "Analyzing chamber " << chamber << std::endl; 
                // create the detid
                CSCDetId ch_id(endcap, station, ring, chamber);
                //std::cout << "ch_id " <<  ch_id << std::endl;
                // get the stubs in this detid
                auto range = CSCCorrelatedLCTs.get(ch_id);
                for (auto digiItr = range.first; digiItr != range.second; ++digiItr){
                  iStub++; 
                  // trigger sector must be the same
                  if (triggerSector != ch_id.triggerSector()) continue;
                  auto stub(*digiItr);
                  int deltaBX = std::abs(stub.getBX() - (6 + event_.L1Mu_bx[i]));
                  
                  // BXs have to match
                  if (deltaBX > 1) continue;
                  std::cout << ch_id << std::endl;
                  std::cout<<"Candidate " << stub << std::endl;
                  bestMatchingStub = pickBestMatchingStub(allxs[ch_id.station()-1], allys[ch_id.station()-1], 
                                                          bestMatchingStub, std::make_pair(ch_id, stub), 6 + event_.L1Mu_bx[i]);
                }
                // consider the case ME1a
                if (station==1 and ring==1){
                  CSCDetId me1a_id(endcap, station, 4, chamber);
                  auto range = CSCCorrelatedLCTs.get(me1a_id);
                  for (auto digiItr = range.first; digiItr != range.second; ++digiItr){
                    iStub++;
                    // trigger sector must be the same
                    if (triggerSector != me1a_id.triggerSector()) continue;
                    auto stub(*digiItr);
                    int deltaBX = std::abs(stub.getBX() - (6 + event_.L1Mu_bx[i]));
                    
                    // BXs have to match
                    if (deltaBX > 1) continue; 
                    std::cout << me1a_id << std::endl;
                    std::cout<<"Candidate " << stub << std::endl;
                    bestMatchingStub = pickBestMatchingStub(allxs[me1a_id.station()-1], allys[me1a_id.station()-1], 
                                                            bestMatchingStub, std::make_pair(me1a_id, stub), 6 + event_.L1Mu_bx[i]);
                    
                  }
                }
                //std::cout << "Current best: " << bestMatchingStub.second << std::endl;
              }
              //std::cout << "Current best2: " << bestMatchingStub.second << std::endl;
            }
            if (bestMatchingStub.second != CSCCorrelatedLCTDigi()) {
              std::cout << "Best matching stub " << bestMatchingStub.first << " " << bestMatchingStub.second <<std::endl;
            
              // stub position
              auto gp = getCSCSpecificPoint2(bestMatchingStub.first.rawId(), bestMatchingStub.second);

              float z_pos_L3, bestFitPhi, bestFitDPhi;
              fitComparatorsLCT(*hCSCComparators.product(), bestMatchingStub.second, bestMatchingStub.first, 0, z_pos_L3, bestFitPhi, bestFitDPhi);
              
              fillCSCStubProperties(bestMatchingStub.first, bestMatchingStub.second, event_.L1Mu_CSCTF_index[i], 
                                    gp, z_pos_L3, bestFitPhi, bestFitDPhi);
            }
            else{
              if (iStub!=0) std::cout << "No best matching stub " << std::endl;
            }
          }
        }
      }
    }

    if (processRPCb_) {
      // Matching to RPCb cands
      double bestDrL1MuL1RPCb = 99;
      for (unsigned int j=0; j<l1MuRPCbs.size(); ++j) { 
        if ( ( event_.L1Mu_quality[i] > 0 ) &&
             ( reco::deltaPhi( event_.L1Mu_phi[i], event_.RPCb_phi[j] ) < 0.001 ) &&             
             ( event_.L1Mu_bx[i] == event_.RPCb_bx[j] ) ) {
          double drL1MuL1RPCb = reco::deltaR(l1Mu.etaValue(), 
                                             normalizedPhi(l1Mu.phiValue()), 
                                             event_.RPCb_eta[j], 
                                             event_.RPCb_phi[j]);
          if (drL1MuL1RPCb < bestDrL1MuL1RPCb and drL1MuL1RPCb < 0.3) {
            bestDrL1MuL1RPCb = drL1MuL1RPCb;
            event_.L1Mu_RPCb_index[i] = j;
          }
        }                
      }
      
      if(verbose) {  
        int tempIndex = event_.L1Mu_RPCb_index[i]; 
        if (tempIndex != -1) { // and bestDrL1MuL1CSCTrack < 0.2
          // Print matching RPCb track
          std::cout << "\tMatching RPCb track" << std::endl;
          std::cout << "\tpt = "  << event_.RPCb_pt[tempIndex]
                    << ", eta = " << event_.RPCb_eta[tempIndex]
                    << ", phi = " << event_.RPCb_phi[tempIndex]
                    << ", bx = "  << event_.RPCb_bx[tempIndex]
                    << ", quality = " << event_.RPCb_quality[tempIndex]
                    << ", nStubs = " << event_.RPCb_nStubs[tempIndex]
                    << std::endl;
        }
        else {
          std::cout << "\tNo matching RPCb track" << std::endl;
        }
      }
    }
    
    if (processRPCf_) {
      // Matching to RPCf cands
      double bestDrL1MuL1RPCf = 99;
      for (unsigned int j=0; j<l1MuRPCfs.size(); ++j) { 
        if ( ( event_.L1Mu_quality[i] > 0 ) &&
             ( reco::deltaPhi( event_.L1Mu_phi[i], event_.RPCf_phi[j] ) < 0.001 ) &&             
             ( event_.L1Mu_bx[i] == event_.RPCf_bx[j] ) ) {
          double drL1MuL1RPCf = reco::deltaR(l1Mu.etaValue(), 
                                             normalizedPhi(l1Mu.phiValue()), 
                                             event_.RPCf_eta[j], 
                                             event_.RPCf_phi[j]);
          if (drL1MuL1RPCf < bestDrL1MuL1RPCf and drL1MuL1RPCf < 0.3) {
            bestDrL1MuL1RPCf = drL1MuL1RPCf;
            event_.L1Mu_RPCf_index[i] = j;
          }
        }                
      }
      
      if(verbose) {  
        int tempIndex = event_.L1Mu_RPCf_index[i]; 
        if (tempIndex != -1) { // and bestDrL1MuL1CSCTrack < 0.2
          // Print matching RPCf track
          std::cout << "\tMatching RPCf track" << std::endl;
          std::cout << "\tpt = "  << event_.RPCf_pt[tempIndex]
                    << ", eta = " << event_.RPCf_eta[tempIndex]
                    << ", phi = " << event_.RPCf_phi[tempIndex]
                    << ", bx = "  << event_.RPCf_bx[tempIndex]
                    << ", quality = " << event_.RPCf_quality[tempIndex]
                    << ", nStubs = " << event_.RPCf_nStubs[tempIndex]
                    << std::endl;
        }
        else {
          std::cout << "\tNo matching RPCf track" << std::endl;
        }
      }
    }
    
    if (processTTI_){
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
    }
    
    if (doGenAnalysis_) {
    
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
        
        if (processTTI_){
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
    }
  }
  
  event_tree_->Fill();  
  
  return true;
}


          // get the one closest to the CSC Stub
          // auto gem_gp1 = getGlobalPointPad(gem_id,copad.first());
          
          // auto gem_gp2 = getGlobalPointPad(gem_id,copad.second());
          // float dPhi1(reco::deltaPhi(gem_gp1.phi(), event_.CSCTF_phi1[ event_.L1Mu_CSCTF_index[i] ] ));
          // float dPhi2(reco::deltaPhi(gem_gp2.phi(), event_.CSCTF_phi1[ event_.L1Mu_CSCTF_index[i] ] ));
            
          //   if (dPhi1 < bestGEMCSCDPhi or dPhi2 < bestGEMCSCDPhi) {
          //     bestGEMCSCDPhi = std::min(dPhi1, dPhi2);
          //     bestCoPad = copad;
          //   }
          // }
          
          // if(verbose){
          //   std::cout << "\tPad " << bestCoPad  << std::endl;
          // }

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

void
DisplacedL1MuFilter::getStubPositions(int index, 
                                      std::vector<float>& x, 
                                      std::vector<float>& y, 
                                      std::vector<float>& z) const
{
  x.clear();
  y.clear();
  z.clear();
  if (event_.CSCTF_st1[index] == 1){
    x.push_back(event_.CSCTF_x1[index]);
    y.push_back(event_.CSCTF_y1[index]);
    z.push_back(event_.CSCTF_z1[index]);
  }
  if (event_.CSCTF_st2[index] == 2){
    x.push_back(event_.CSCTF_x2[index]);
    y.push_back(event_.CSCTF_y2[index]);
    z.push_back(event_.CSCTF_z2[index]);
  }
  if (event_.CSCTF_st3[index] == 3){
    x.push_back(event_.CSCTF_x3[index]);
    y.push_back(event_.CSCTF_y3[index]);
    z.push_back(event_.CSCTF_z3[index]);
  }
  if (event_.CSCTF_st4[index] == 4){
    x.push_back(event_.CSCTF_x4[index]);
    y.push_back(event_.CSCTF_y4[index]);
    z.push_back(event_.CSCTF_z4[index]);
  }
} 

void 
DisplacedL1MuFilter::fitComparatorsLCT(const CSCComparatorDigiCollection& hCSCComparators,
                                       const CSCCorrelatedLCTDigi& stub, CSCDetId ch_id, 
                                       int iMuon, float& fit_z, float& fit_phi, float& fit_dphi) const
{
  bool verbose = false;
  
  auto cscChamber = cscGeometry_->chamber(ch_id);
  
  // fetch the CSC comparator digis in this chamber
  CSCComparatorDigiContainerIds compDigisIds;
  for (int iLayer=1; iLayer<=6; ++iLayer){
    CSCDetId layerId(ch_id.endcap(), ch_id.station(), ch_id.ring(), ch_id.chamber(), iLayer);
    // get the digis per layer
    auto compRange = hCSCComparators.get(layerId);
    CSCComparatorDigiContainer compDigis;
    for (auto compDigiItr = compRange.first; compDigiItr != compRange.second; compDigiItr++) {
      auto compDigi = *compDigiItr;
      //if (stub.getTimeBin() < 4 or stub.getTimeBin() > 8) continue;
      int stubHalfStrip(getHalfStrip(compDigi));
      // these comparator digis never fit the pattern anyway!
      if (std::abs(stubHalfStrip-stub.getStrip())>5) continue;
      // check if this comparator digi fits the pattern
      //if(verbose) std::cout << "Comparator digi L1Mu " << layerId << " " << compDigi << " HS " << stubHalfStrip << " stubKeyHS " << stub.getStrip() << std::endl; 
      if (comparatorInLCTPattern(stub.getStrip(), stub.getPattern(), iLayer, stubHalfStrip)) {
        //if(verbose) std::cout<<"\tACCEPT"<<std::endl;
        compDigis.push_back(compDigi);
      }
      // else{
      //   if(verbose) std::cout<<"\tDECLINE!"<<std::endl;
      // }
    }
    // if(verbose) if (compDigis.size() > 2) std::cout << ">>> INFO: " << compDigis.size() << " matched comp digis in this layer!" << std::endl;
    compDigisIds.push_back(std::make_pair(layerId, compDigis));
  }
  
  // get the z and phi positions
  std::vector<float> phis;
  std::vector<float> zs;
  std::vector<float> ephis;
  std::vector<float> ezs;
  for (auto p: compDigisIds){
    auto detId = p.first;
    for (auto hit: p.second){
      float fractional_strip = getFractionalStrip(hit);
      auto layer_geo = cscChamber->layer(detId.layer())->geometry();
      LocalPoint csc_intersect = layer_geo->intersectionOfStripAndWire(fractional_strip, 20);
      GlobalPoint csc_gp = cscGeometry_->idToDet(detId)->surface().toGlobal(csc_intersect);
      float gpphi = csc_gp.phi();
      
      if (phis.size()>0 and gpphi>0 and phis[0]<0 and  (gpphi-phis[0])>3.1416)
        phis.push_back(gpphi-2*3.1415926);
      else if (phis.size()>0 and gpphi<0 and phis[0]>0 and (gpphi-phis[0])<-3.1416)
        phis.push_back(gpphi+2*3.1415926);
      else
        phis.push_back(csc_gp.phi());


      zs.push_back(csc_gp.z());
      ezs.push_back(0);
      // phis.push_back(csc_gp.phi());
      ephis.push_back(gemvalidation::cscHalfStripWidth(detId)/sqrt(12));
    }
  }
  
  // do a fit to the comparator digis
  float alpha = 0., beta = 0.;
  fitStraightLineErrors(zs, phis, ezs, ephis,
                        alpha, beta, 
                        event_.lumi, event_.run, event_.event, iMuon, ch_id.station(), false);
  
  fit_z = cscChamber->layer(CSCConstants::KEY_CLCT_LAYER)->centerOfStrip(20).z();
  fit_phi = normalizedPhi(alpha + beta * fit_z);
  
  if(verbose) {
    std::cout << "Number of comparator digis used in the fit " << ezs.size() << std::endl;
    std::cout << "best CSC stub fit phi position (L1Only) " << fit_z << " " << fit_phi << std::endl;
  }

  // calculate the z position in L1 and L6
  float l1_z = cscChamber->layer(1)->centerOfStrip(20).z();
  float l6_z = cscChamber->layer(6)->centerOfStrip(20).z();
  // calculate the bending angle
  fit_dphi = beta*(l6_z-l1_z);
}


float 
DisplacedL1MuFilter::getGlobalPhi(unsigned int rawid, int stripN)
{  
  const RPCDetId id(rawid);
  std::unique_ptr<const RPCRoll>  roll(rpcGeometry_->roll(id));
  const uint16_t strip = stripN;
  const LocalPoint lp = roll->centreOfStrip(strip);
  const GlobalPoint gp = roll->toGlobal(lp);
  roll.release();
  return gp.phi();
}

double 
DisplacedL1MuFilter::calcCSCSpecificPhi(unsigned int rawId, const CSCCorrelatedLCTDigi& lct) const
{
  return getCSCSpecificPoint2(rawId, lct).phi();
}

GlobalPoint 
DisplacedL1MuFilter::getGlobalPointPad(unsigned int rawId, const GEMCSCPadDigi& tp) const
{
  GEMDetId gem_id(rawId);
  // cout << "old " << gem_id << endl;
  // if (gem_id.station()==2){
  //   gem_id = GEMDetId(gem_id.region(), gem_id.ring(), 3, gem_id.layer(), gem_id.chamber(), gem_id.roll());
  // }
  // cout << "new " << gem_id << endl;
  LocalPoint gem_lp = gemGeometry_->etaPartition(gem_id)->centreOfPad(tp.pad());
  GlobalPoint gem_gp = gemGeometry_->idToDet(gem_id)->surface().toGlobal(gem_lp);
  return gem_gp;
}


GlobalPoint
DisplacedL1MuFilter::getCSCSpecificPoint2(unsigned int rawId, const CSCCorrelatedLCTDigi& lct) const 
{
  // taken from https://github.com/cms-sw/cmssw/blob/dc9f78b6af4ad56c9342cf14041b6485a60b0691/L1Trigger/CSCTriggerPrimitives/src/CSCMotherboardME11GEM.cc
  CSCDetId cscId = CSCDetId(rawId);
  CSCDetId key_id(cscId.endcap(), cscId.station(), cscId.ring(), cscId.chamber(), CSCConstants::KEY_CLCT_LAYER);
  
  auto cscChamber = cscGeometry_->chamber(cscId);
  // "strip" here is actually a half-strip in geometry's terms
  // note that LCT::getStrip() starts from 0
  float fractional_strip = 0.5 * (lct.getStrip() + 1) - 0.25;
  auto layer_geo = cscChamber->layer(CSCConstants::KEY_CLCT_LAYER)->geometry();
  // LCT::getKeyWG() also starts from 0
  float wire = layer_geo->middleWireOfGroup(lct.getKeyWG() + 1);
  LocalPoint csc_intersect = layer_geo->intersectionOfStripAndWire(fractional_strip, wire);
  GlobalPoint csc_gp = cscGeometry_->idToDet(key_id)->surface().toGlobal(csc_intersect);
  //std::cout << "\t\t>>> other CSC LCT phi " << csc_gp.phi() << std::endl;
  //return getCSCSpecificPoint(rawId, lct).phi();
  return csc_gp;
}

CSCCorrelatedLCTDigiId 
DisplacedL1MuFilter::pickBestMatchingStub(float xref, float yref,
                                          const CSCCorrelatedLCTDigiId& oldStub,
                                          const CSCCorrelatedLCTDigiId& newStub, 
                                          int refBx) const
{
  bool debug=false;

  if (debug){
  std::cout << "In function pickBestMatchingStub" << std::endl;
  std::cout << "candidate 1 " << oldStub.first << " "  << oldStub.second << std::endl;
  std::cout << "candidate 2 " << newStub.first << " "  << newStub.second << std::endl;
  }

  // check for invalid/valid
  if (oldStub.second == CSCCorrelatedLCTDigi()) {
    if (debug) cout<<"Old stub invalid"<<endl;
    return newStub;
  }
  if (newStub.second == CSCCorrelatedLCTDigi()) {
    if (debug) cout<< "New stub invalid"<<endl;
    return oldStub;
  }
  
  int deltaBXOld = std::abs(oldStub.second.getBX() - refBx);
  int deltaBXNew = std::abs(newStub.second.getBX() - refBx);
  
  if (deltaBXOld==0 and deltaBXNew!=0) {
    if (debug) cout<<"Old stub in time, new stub out of time"<<endl;
    return oldStub;
  }
  if (deltaBXNew==0 and deltaBXOld!=0) {
    if (debug) cout<<"New stub in time, old stub out of time"<<endl;
    return newStub;
  }
  if ( (deltaBXOld!=0 and deltaBXNew!=0) or 
       (deltaBXOld==0 and deltaBXNew==0) ){
    if (debug) cout<<"Both stubs out of time"<<endl;
    // pick the one with the better matching wiregroup and halfstrip
    auto gpOld = getCSCSpecificPoint2(oldStub.first.rawId(), oldStub.second);
    auto gpNew = getCSCSpecificPoint2(newStub.first.rawId(), newStub.second);
    float deltaXYOld = TMath::Sqrt( (xref-gpOld.x())*(xref-gpOld.x()) + (yref-gpOld.y())*(yref-gpOld.y()) );
    float deltaXYNew = TMath::Sqrt( (xref-gpNew.x())*(xref-gpNew.x()) + (yref-gpNew.y())*(yref-gpNew.y()) );
    if (debug) {
      cout<<"xref "<< xref << " yref " << yref << endl;
      cout <<"gpOld " << gpOld << " gpNew " << gpNew << endl; 
      cout << "deltaXYOld " << deltaXYOld << " deltaXYNew " << deltaXYNew <<endl;
    }  
    if (deltaXYOld < deltaXYNew) {
      if (debug) cout<<"Old  stub better matching XY"<<endl;
      return oldStub;
    }
    else {
      if (debug) cout<<"New stub better matching XY"<<endl;
      return newStub;
    }
  }
  std::cout << "All else fails" << std::endl;
  // in case all else fails...
  return CSCCorrelatedLCTDigiId();
}

bool 
DisplacedL1MuFilter::stubInCSCTFTracks(const CSCCorrelatedLCTDigi& candidateStub, const L1CSCTrackCollection& l1Tracks) const
{
  bool isMatched = false;
  for (auto tftrack: l1Tracks){
    auto stubCollection = tftrack.second;
    for (auto detUnitIt = stubCollection.begin(); detUnitIt != stubCollection.end(); detUnitIt++) {
      const auto range = (*detUnitIt).second;
      for (auto digiIt = range.first; digiIt != range.second; digiIt++) {
        //if (!(*digiIt).isValid()) continue;
        auto stub = *digiIt;
        if (candidateStub == stub) { 
          isMatched = true;
          break;
        }
      }
    }
  }
  return isMatched;
}


bool 
DisplacedL1MuFilter::stubInDTTFTracks(const L1MuDTTrackSegPhi& candidateStub, 
                                      const L1MuDTTrackCollection& l1Tracks) const
{
  bool isMatched = false;
  for (auto tftrack: l1Tracks){
    auto stubCollection = tftrack.second;
    for (auto stub: stubCollection) {
      if (candidateStub == stub) { 
        isMatched = true;
        break;
      }
    }
  }
  return isMatched;
}


GEMCSCPadDigiId
DisplacedL1MuFilter::pickBestMatchingCoPad(float xref, float yref,
                                           const GEMCSCPadDigiId& oldCoPad,
                                           const GEMCSCPadDigiId& newCoPad, 
                                           int bxref) const
{
  bool debug = true;
  // check for invalid/valid
  if (oldCoPad.second == GEMCSCPadDigi()) {
    if (debug) cout<<"Old copad invalid"<<endl;
    return newCoPad;
  }
  if (newCoPad.second == GEMCSCPadDigi()) {
    if (debug) cout<< "New copad invalid"<<endl;
    return oldCoPad;
  }
  
  // check the timing
  bool oldCoPadInTime = oldCoPad.second.bx() - bxref==0;// and oldCoPad.second.second().bx() - bxref==0;
  bool newCoPadInTime = newCoPad.second.bx() - bxref==0;// and newCoPad.second.second().bx() - bxref==0;
  if (oldCoPadInTime and not newCoPadInTime) {
    if (debug) cout<<"Old copad in time, new copad out of time"<<endl;
    return oldCoPad;
  }
  if (newCoPadInTime and not oldCoPadInTime) {
    if (debug) cout<<"New copad in time, old copad out of time"<<endl;
    return newCoPad;
  }

  // both copads in time, check the closest matching one!
  if ((oldCoPadInTime and newCoPadInTime) or (not oldCoPadInTime and not newCoPadInTime)){
    if (debug) cout << "check better matching one in space" << endl;
    auto gpOld = getGlobalPointPad(oldCoPad.first.rawId(), oldCoPad.second);
    auto gpNew = getGlobalPointPad(newCoPad.first.rawId(), newCoPad.second);
    float deltaXYOld = TMath::Sqrt( (xref-gpOld.x())*(xref-gpOld.x()) + (yref-gpOld.y())*(yref-gpOld.y()) );
    float deltaXYNew = TMath::Sqrt( (xref-gpNew.x())*(xref-gpNew.x()) + (yref-gpNew.y())*(yref-gpNew.y()) );
    if (debug) {
      cout<<"xref "<< xref << " yref " << yref << endl;
      cout <<"gpOld " << gpOld << " gpNew " << gpNew << endl; 
      cout << "deltaXYOld " << deltaXYOld << " deltaXYNew " << deltaXYNew <<endl;
    }  
    if (deltaXYOld < deltaXYNew) {
      if (debug) cout<<"Old  copad better matching XY"<<endl;
      return oldCoPad;
    }
    else {
      if (debug) cout<<"New copad better matching XY"<<endl;
      return newCoPad;
    }
  }
  // in case all else fails...
  return GEMCSCPadDigiId();
}


GEMCSCPadDigiId
DisplacedL1MuFilter::pickBestMatchingPad(float xref, float yref,
                                         const GEMCSCPadDigiId& oldPad,
                                         const GEMCSCPadDigiId& newPad, 
                                         int bxref) const
{
  bool debug = false;
  // check for invalid/valid
  if (oldPad.second == GEMCSCPadDigi()) {
    if (debug) cout<<"Old pad invalid"<<endl;
    return newPad;
  }
  if (newPad.second == GEMCSCPadDigi()) {
    if (debug) cout<< "New pad invalid"<<endl;
    return oldPad;
  }
  
  // check the timing
  bool oldPadInTime = oldPad.second.bx() - bxref==0 and oldPad.second.bx() - bxref==0;
  bool newPadInTime = newPad.second.bx() - bxref==0 and newPad.second.bx() - bxref==0;
  if (oldPadInTime and not newPadInTime) {
    if (debug) cout<<"Old copad in time, new copad out of time"<<endl;
    return oldPad;
  }
  if (newPadInTime and not oldPadInTime) {
    if (debug) cout<<"New copad in time, old copad out of time"<<endl;
    return newPad;
  }

  // both copads in time, check the closest matching one!
  if ((oldPadInTime and newPadInTime) or (not oldPadInTime and  not newPadInTime)){
    if (debug) cout << "check better matching one in space" << endl;
    auto gpOld = getGlobalPointPad(oldPad.first.rawId(), oldPad.second);
    auto gpNew = getGlobalPointPad(newPad.first.rawId(), newPad.second);
    float deltaXYOld = TMath::Sqrt( (xref-gpOld.x())*(xref-gpOld.x()) + (yref-gpOld.y())*(yref-gpOld.y()) );
    float deltaXYNew = TMath::Sqrt( (xref-gpNew.x())*(xref-gpNew.x()) + (yref-gpNew.y())*(yref-gpNew.y()) );
    if (debug) {
      cout<<"xref "<< xref << " yref " << yref << endl;
      cout <<"gpOld " << gpOld << " gpNew " << gpNew << endl; 
      cout << "deltaXYOld " << deltaXYOld << " deltaXYNew " << deltaXYNew <<endl;
    }  
    if (deltaXYOld < deltaXYNew) {
      if (debug) cout<<"Old  copad better matching XY"<<endl;
      return oldPad;
    }
    else {
      if (debug) cout<<"New copad better matching XY"<<endl;
      return newPad;
    }
  }
  // in case all else fails...
  return GEMCSCPadDigiId();
}


std::vector<GlobalPoint> 
DisplacedL1MuFilter::positionPad2InDetId(const GEMDigiCollection& hGEMDigis, unsigned int ch_id, int refBX) const
{
  // get the digis in detid 
  std::vector<GlobalPoint> result;
  bool verbose = false;
  
  CSCDetId csc_id(ch_id);
  if (verbose) std::cout << "In function positionPad2InDetId csc_id " << csc_id << std::endl;
  
  for(auto cItr = hGEMDigis.begin(); cItr != hGEMDigis.end(); ++cItr) {
    GEMDetId gem_id = (*cItr).first;
    
    // chambers need to be compatible
    // no cut on the eta partition!
    if (gem_id.station() == 2) continue;
    if (gem_id.region() == csc_id.zendcap() and 
        (gem_id.station() == csc_id.station() or (gem_id.station( )== 3 and csc_id.station() == 2)) and 
        csc_id.chamber() == gem_id.chamber() and
        (csc_id.ring() == 4 or csc_id.ring() == 1)) {
            
      if(verbose) std::cout << "Investigate GEM chamber " << gem_id << std::endl;
      
      // get the digis
      auto digi_range = (*cItr).second;
      for (auto digiItr = digi_range.first; digiItr != digi_range.second; ++digiItr){
        auto digi(*digiItr);
    
        int deltaBX = std::abs(digi.bx() - refBX);
        if (deltaBX <= 1) {
          
          if(verbose) std::cout << "\tCandidate digi " << digi << std::endl;
          float middleStripOfPad = 0.;
          if (digi.strip()%2==0){
            middleStripOfPad = digi.strip()-1.;
          }
          else{
            middleStripOfPad = digi.strip();
          }
          LocalPoint gem_lp = gemGeometry_->etaPartition(gem_id)->centreOfStrip(middleStripOfPad);
          GlobalPoint gem_gp = gemGeometry_->idToDet(gem_id)->surface().toGlobal(gem_lp);
          if (std::find(result.begin(), result.end(), gem_gp) == result.end()) result.push_back(gem_gp);
          if (verbose) std::cout << "middle strip " << middleStripOfPad << " " <<gem_gp <<std::endl;
        }
      }
    }
  }
  return result;
}


std::vector<GlobalPoint> 
DisplacedL1MuFilter::positionPad4InDetId(const GEMDigiCollection& hGEMDigis, unsigned int ch_id, int refBX) const
{
  // get the digis in detid 
  std::vector<GlobalPoint> result;
  bool verbose = false;
  
  CSCDetId csc_id(ch_id);
  if (verbose) std::cout << "In function positionPad4InDetId csc_id " << csc_id << std::endl;
  
  for(auto cItr = hGEMDigis.begin(); cItr != hGEMDigis.end(); ++cItr) {
    GEMDetId gem_id = (*cItr).first;
    
    // chambers need to be compatible
    // no cut on the eta partition!
    if (gem_id.station() == 2) continue;
    if (gem_id.region() == csc_id.zendcap() and 
        (gem_id.station() == csc_id.station() or (gem_id.station()==3 and csc_id.station()==2)) and 
        csc_id.chamber() == gem_id.chamber() and
        (csc_id.ring() == 4 or csc_id.ring() == 1)) {
            
      if(verbose) std::cout << "Investigate GEM chamber " << gem_id << std::endl;
      
      // get the digis
      auto digi_range = (*cItr).second;
      for (auto digiItr = digi_range.first; digiItr != digi_range.second; ++digiItr){
        auto digi(*digiItr);
    
        int deltaBX = std::abs(digi.bx() - refBX);
        if (deltaBX <= 1) {
          
          if(verbose) std::cout << "\tCandidate digi " << digi  << std::endl;
          float middleStripOfPad = 0.;
          if (digi.strip()%4==0){
            middleStripOfPad = digi.strip() - 2.;
          }
          else if (digi.strip()%4==3){
            middleStripOfPad = digi.strip() - 1.;
          }
          else if (digi.strip()%4==2){
            middleStripOfPad = digi.strip() + 0.;
          }
          else{
            middleStripOfPad = digi.strip() + 1.;
          }
          LocalPoint gem_lp = gemGeometry_->etaPartition(gem_id)->centreOfStrip(middleStripOfPad);
          GlobalPoint gem_gp = gemGeometry_->idToDet(gem_id)->surface().toGlobal(gem_lp);
          if (std::find(result.begin(), result.end(), gem_gp) == result.end()) result.push_back(gem_gp);
          if (verbose) std::cout << "middle strip " << middleStripOfPad  << " " <<gem_gp << std::endl;
        }
      }
    }
  }
  return result;
}


void 
DisplacedL1MuFilter::fillCSCStubProperties(const CSCDetId& ch_id,
                                           const CSCCorrelatedLCTDigi& stub,
                                           int index,
                                           const GlobalPoint& gp,
                                           float z_pos_L3, float bestFitPhi, float bestFitDPhi)
{
  double csc_x = gp.x();
  double csc_y = gp.y();
  double csc_z = gp.z();
  double csc_R = TMath::Sqrt(gp.y()*gp.y() + gp.x()*gp.x());
  float radius = csc_R;

  // std::cout << "Printing stub properties" << std::endl 
  //           << "Id " << ch_id << " stub " << stub 
  //           << "GP " << gp << " eta " << gp.eta() << " phi " << gp.phi() << std::endl << std::endl;  

  switch(ch_id.station()) {
  case 1:
    event_.CSCTF_id1[index] = ch_id.rawId();
    event_.CSCTF_st1[index] = ch_id.station();
    event_.CSCTF_ri1[index] = ch_id.ring(); 
    event_.CSCTF_ch1[index] = ch_id.chamber();
    event_.CSCTF_en1[index] = ch_id.zendcap();
    event_.CSCTF_trk1[index] = stub.getTrknmb(); 
    event_.CSCTF_quality1[index] = stub.getQuality();
    event_.CSCTF_wg1[index] = stub.getKeyWG();
    event_.CSCTF_hs1[index] = stub.getStrip();
    event_.CSCTF_pat1[index] = stub.getPattern();
    event_.CSCTF_bend1[index] = stub.getBend();
    event_.CSCTF_bx1[index] = stub.getBX();
    event_.CSCTF_clctpat1[index] = stub.getCLCTPattern();
    event_.CSCTF_val1[index] = stub.isValid();
    event_.CSCTF_phi1[index] = gp.phi();
    event_.CSCTF_eta1[index] = gp.eta();
    event_.CSCTF_gemdphi1[index] = stub.getGEMDPhi();
    event_.CSCTF_R1[index] = csc_R;
    event_.CSCTF_x1[index] = csc_x;
    event_.CSCTF_y1[index] = csc_y;
    event_.CSCTF_z1[index] = csc_z;
    // fitted positions
    event_.CSCTF_fit_phi1[index] = bestFitPhi;
    event_.CSCTF_fit_dphi1[index] = bestFitDPhi;
    event_.CSCTF_fit_x1[index] = radius*cos(bestFitPhi);
    event_.CSCTF_fit_y1[index] = radius*sin(bestFitPhi);
    event_.CSCTF_fit_z1[index] = z_pos_L3;
    event_.CSCTF_fit_R1[index] = radius;
    break;
  case 2:
    event_.CSCTF_id2[index] = ch_id.rawId();
    event_.CSCTF_st2[index] = ch_id.station();
    event_.CSCTF_ri2[index] = ch_id.ring(); 
    event_.CSCTF_ch2[index] = ch_id.chamber();
    event_.CSCTF_en2[index] = ch_id.zendcap();
    event_.CSCTF_trk2[index] = stub.getTrknmb(); 
    event_.CSCTF_quality2[index] = stub.getQuality();
    event_.CSCTF_wg2[index] = stub.getKeyWG();
    event_.CSCTF_hs2[index] = stub.getStrip();
    event_.CSCTF_pat2[index] = stub.getPattern();
    event_.CSCTF_bend2[index] = stub.getBend();
    event_.CSCTF_bx2[index] = stub.getBX();
    event_.CSCTF_clctpat2[index] = stub.getCLCTPattern();
    event_.CSCTF_val2[index] = stub.isValid();
    event_.CSCTF_phi2[index] = gp.phi();
    event_.CSCTF_eta2[index] = gp.eta();
    event_.CSCTF_gemdphi2[index] = stub.getGEMDPhi();
    event_.CSCTF_R2[index] = csc_R;
    event_.CSCTF_x2[index] = csc_x;
    event_.CSCTF_y2[index] = csc_y;
    event_.CSCTF_z2[index] = csc_z;
    // fitted positions
    event_.CSCTF_fit_phi2[index] = bestFitPhi;
    event_.CSCTF_fit_dphi2[index] = bestFitDPhi;
    event_.CSCTF_fit_x2[index] = radius*cos(bestFitPhi);
    event_.CSCTF_fit_y2[index] = radius*sin(bestFitPhi);
    event_.CSCTF_fit_z2[index] = z_pos_L3;
    event_.CSCTF_fit_R2[index] = radius;
    break;
  case 3:
    event_.CSCTF_id3[index] = ch_id.rawId();
    event_.CSCTF_st3[index] = ch_id.station();
    event_.CSCTF_ri3[index] = ch_id.ring(); 
    event_.CSCTF_ch3[index] = ch_id.chamber();
    event_.CSCTF_en3[index] = ch_id.zendcap();
    event_.CSCTF_trk3[index] = stub.getTrknmb(); 
    event_.CSCTF_quality3[index] = stub.getQuality();
    event_.CSCTF_wg3[index] = stub.getKeyWG();
    event_.CSCTF_hs3[index] = stub.getStrip();
    event_.CSCTF_pat3[index] = stub.getPattern();
    event_.CSCTF_bend3[index] = stub.getBend();
    event_.CSCTF_bx3[index] = stub.getBX();
    event_.CSCTF_clctpat3[index] = stub.getCLCTPattern();
    event_.CSCTF_val3[index] = stub.isValid();
    event_.CSCTF_phi3[index] = gp.phi();
    event_.CSCTF_eta3[index] = gp.eta();
    event_.CSCTF_R3[index] = csc_R;
    event_.CSCTF_x3[index] = csc_x;
    event_.CSCTF_y3[index] = csc_y;
    event_.CSCTF_z3[index] = csc_z;
    // fitted positions
    event_.CSCTF_fit_phi3[index] = bestFitPhi;
    event_.CSCTF_fit_dphi3[index] = bestFitDPhi;
    event_.CSCTF_fit_x3[index] = radius*cos(bestFitPhi);
    event_.CSCTF_fit_y3[index] = radius*sin(bestFitPhi);
    event_.CSCTF_fit_z3[index] = z_pos_L3;
    event_.CSCTF_fit_R3[index] = radius;
    break;
  case 4:
    event_.CSCTF_id4[index] = ch_id.rawId();
    event_.CSCTF_st4[index] = ch_id.station();
    event_.CSCTF_ri4[index] = ch_id.ring(); 
    event_.CSCTF_ch4[index] = ch_id.chamber();
    event_.CSCTF_en4[index] = ch_id.zendcap();
    event_.CSCTF_trk4[index] = stub.getTrknmb(); 
    event_.CSCTF_quality4[index] = stub.getQuality();
    event_.CSCTF_wg4[index] = stub.getKeyWG();
    event_.CSCTF_hs4[index] = stub.getStrip();
    event_.CSCTF_pat4[index] = stub.getPattern();
    event_.CSCTF_bend4[index] = stub.getBend();
    event_.CSCTF_bx4[index] = stub.getBX();
    event_.CSCTF_clctpat4[index] = stub.getCLCTPattern();
    event_.CSCTF_val4[index] = stub.isValid();
    event_.CSCTF_phi4[index] = gp.phi();
    event_.CSCTF_eta4[index] = gp.eta();
    event_.CSCTF_R4[index] = csc_R;
    event_.CSCTF_x4[index] = csc_x;
    event_.CSCTF_y4[index] = csc_y;
    event_.CSCTF_z4[index] = csc_z;
    // fitted positions
    event_.CSCTF_fit_phi4[index] = bestFitPhi;
    event_.CSCTF_fit_dphi4[index] = bestFitDPhi;
    event_.CSCTF_fit_x4[index] = radius*cos(bestFitPhi);
    event_.CSCTF_fit_y4[index] = radius*sin(bestFitPhi);
    event_.CSCTF_fit_z4[index] = z_pos_L3;
    event_.CSCTF_fit_R4[index] = radius;
    break;
  };
}


void 
DisplacedL1MuFilter::printCSCStubProperties(int index) const
{
  
  cout << "id1 "<< event_.CSCTF_id1[index] << endl;
  cout << "st1 "<< event_.CSCTF_st1[index] << endl;
  cout << "ri1 "<< event_.CSCTF_ri1[index] << endl; 
  cout << "ch1 "<< event_.CSCTF_ch1[index] << endl;
  cout << "en1 "<< event_.CSCTF_en1[index] << endl;
  cout << "trk1 "<< event_.CSCTF_trk1[index]<< endl; 
  cout << "quality1 "<< event_.CSCTF_quality1[index] << endl;
  cout << "wg1 "<< event_.CSCTF_wg1[index] << endl;
  cout << "hs1 "<< event_.CSCTF_hs1[index] << endl;
  cout << "pat1 "<< event_.CSCTF_pat1[index] << endl;
  cout << "bend1 "<< event_.CSCTF_bend1[index]<< endl;
  cout << "bx1 "<< event_.CSCTF_bx1[index]<< endl;
  cout << "clctpat1 "<< event_.CSCTF_clctpat1[index]<< endl;
  cout << "val1 "<< event_.CSCTF_val1[index]<< endl;
  cout << "phi1 "<< event_.CSCTF_phi1[index]<< endl;
  cout << "eta1 "<< event_.CSCTF_eta1[index]<< endl;
  cout << "gemdphi1 "<< event_.CSCTF_gemdphi1[index]<< endl;
  cout << "R1 "<< event_.CSCTF_R1[index]<< endl;
  cout << "x1 "<< event_.CSCTF_x1[index]<< endl;
  cout << "y1 "<< event_.CSCTF_y1[index]<< endl;
  cout << "z1 "<< event_.CSCTF_z1[index]<< endl;
  cout << "fit phi1 "<< event_.CSCTF_fit_phi1[index]<< endl;
  cout << "fit dphi1 "<< event_.CSCTF_fit_dphi1[index]<< endl;
  cout << "fit x1 "<< event_.CSCTF_fit_x1[index]<< endl;
  cout << "fit y1 "<< event_.CSCTF_fit_y1[index]<< endl;
  cout << "fit z1 "<< event_.CSCTF_fit_z1[index]<< endl;
  cout << "fit R1 "<< event_.CSCTF_fit_R1[index]<< endl;

  cout << "id2 "<< event_.CSCTF_id2[index] << endl;
  cout << "st2 "<< event_.CSCTF_st2[index] << endl;
  cout << "ri2 "<< event_.CSCTF_ri2[index] << endl; 
  cout << "ch2 "<< event_.CSCTF_ch2[index] << endl;
  cout << "en2 "<< event_.CSCTF_en2[index] << endl;
  cout << "trk2 "<< event_.CSCTF_trk2[index]<< endl; 
  cout << "quality2 "<< event_.CSCTF_quality2[index] << endl;
  cout << "wg2 "<< event_.CSCTF_wg2[index] << endl;
  cout << "hs2 "<< event_.CSCTF_hs2[index] << endl;
  cout << "pat2 "<< event_.CSCTF_pat2[index] << endl;
  cout << "bend2 "<< event_.CSCTF_bend2[index]<< endl;
  cout << "bx2 "<< event_.CSCTF_bx2[index]<< endl;
  cout << "clctpat2 "<< event_.CSCTF_clctpat2[index]<< endl;
  cout << "val2 "<< event_.CSCTF_val2[index]<< endl;
  cout << "phi2 "<< event_.CSCTF_phi2[index]<< endl;
  cout << "eta2 "<< event_.CSCTF_eta2[index]<< endl;
  cout << "gemdphi2 "<< event_.CSCTF_gemdphi2[index]<< endl;
  cout << "R2 "<< event_.CSCTF_R2[index]<< endl;
  cout << "x2 "<< event_.CSCTF_x2[index]<< endl;
  cout << "y2 "<< event_.CSCTF_y2[index]<< endl;
  cout << "z2 "<< event_.CSCTF_z2[index]<< endl;
  cout << "fit phi2 "<< event_.CSCTF_fit_phi2[index]<< endl;
  cout << "fit dphi2 "<< event_.CSCTF_fit_dphi2[index]<< endl;
  cout << "fit x2 "<< event_.CSCTF_fit_x2[index]<< endl;
  cout << "fit y2 "<< event_.CSCTF_fit_y2[index]<< endl;
  cout << "fit z2 "<< event_.CSCTF_fit_z2[index]<< endl;
  cout << "fit R2 "<< event_.CSCTF_fit_R2[index]<< endl;

  cout << "id3 "<< event_.CSCTF_id3[index] << endl;
  cout << "st3 "<< event_.CSCTF_st3[index] << endl;
  cout << "ri3 "<< event_.CSCTF_ri3[index] << endl; 
  cout << "ch3 "<< event_.CSCTF_ch3[index] << endl;
  cout << "en3 "<< event_.CSCTF_en3[index] << endl;
  cout << "trk3 "<< event_.CSCTF_trk3[index]<< endl; 
  cout << "quality3 "<< event_.CSCTF_quality3[index] << endl;
  cout << "wg3 "<< event_.CSCTF_wg3[index] << endl;
  cout << "hs3 "<< event_.CSCTF_hs3[index] << endl;
  cout << "pat3 "<< event_.CSCTF_pat3[index] << endl;
  cout << "bend3 "<< event_.CSCTF_bend3[index]<< endl;
  cout << "bx3 "<< event_.CSCTF_bx3[index]<< endl;
  cout << "clctpat3 "<< event_.CSCTF_clctpat3[index]<< endl;
  cout << "val3 "<< event_.CSCTF_val3[index]<< endl;
  cout << "phi3 "<< event_.CSCTF_phi3[index]<< endl;
  cout << "eta3 "<< event_.CSCTF_eta3[index]<< endl;
  cout << "R3 "<< event_.CSCTF_R3[index]<< endl;
  cout << "x3 "<< event_.CSCTF_x3[index]<< endl;
  cout << "y3 "<< event_.CSCTF_y3[index]<< endl;
  cout << "z3 "<< event_.CSCTF_z3[index]<< endl;
  cout << "fit phi3 "<< event_.CSCTF_fit_phi3[index]<< endl;
  cout << "fit dphi3 "<< event_.CSCTF_fit_dphi3[index]<< endl;
  cout << "fit x3 "<< event_.CSCTF_fit_x3[index]<< endl;
  cout << "fit y3 "<< event_.CSCTF_fit_y3[index]<< endl;
  cout << "fit z3 "<< event_.CSCTF_fit_z3[index]<< endl;
  cout << "fit R3 "<< event_.CSCTF_fit_R3[index]<< endl;

  cout << "id4 "<< event_.CSCTF_id4[index] << endl;
  cout << "st4 "<< event_.CSCTF_st4[index] << endl;
  cout << "ri4 "<< event_.CSCTF_ri4[index] << endl; 
  cout << "ch4 "<< event_.CSCTF_ch4[index] << endl;
  cout << "en4 "<< event_.CSCTF_en4[index] << endl;
  cout << "trk4 "<< event_.CSCTF_trk4[index]<< endl; 
  cout << "quality4 "<< event_.CSCTF_quality4[index] << endl;
  cout << "wg4 "<< event_.CSCTF_wg4[index] << endl;
  cout << "hs4 "<< event_.CSCTF_hs4[index] << endl;
  cout << "pat4 "<< event_.CSCTF_pat4[index] << endl;
  cout << "bend4 "<< event_.CSCTF_bend4[index]<< endl;
  cout << "bx4 "<< event_.CSCTF_bx4[index]<< endl;
  cout << "clctpat4 "<< event_.CSCTF_clctpat4[index]<< endl;
  cout << "val4 "<< event_.CSCTF_val4[index]<< endl;
  cout << "phi4 "<< event_.CSCTF_phi4[index]<< endl;
  cout << "eta4 "<< event_.CSCTF_eta4[index]<< endl;
  cout << "R4 "<< event_.CSCTF_R4[index]<< endl;
  cout << "x4 "<< event_.CSCTF_x4[index]<< endl;
  cout << "y4 "<< event_.CSCTF_y4[index]<< endl;
  cout << "z4 "<< event_.CSCTF_z4[index]<< endl;
  cout << "fit phi4 "<< event_.CSCTF_fit_phi4[index]<< endl;
  cout << "fit dphi4 "<< event_.CSCTF_fit_dphi4[index]<< endl;
  cout << "fit x4 "<< event_.CSCTF_fit_x4[index]<< endl;
  cout << "fit y4 "<< event_.CSCTF_fit_y4[index]<< endl;
  cout << "fit z4 "<< event_.CSCTF_fit_z4[index]<< endl;
  cout << "fit R4 "<< event_.CSCTF_fit_R4[index]<< endl;

}


GlobalPoint 
DisplacedL1MuFilter::getCSCSpecificPoint(unsigned int rawId, const CSCCorrelatedLCTDigi& tp) const 
{
  const CSCDetId id(rawId); 
  // we should change this to weak_ptrs at some point
  // requires introducing std::shared_ptrs to geometry
  std::unique_ptr<const CSCChamber> chamb(cscGeometry_->chamber(id));
  std::unique_ptr<const CSCLayerGeometry> layer_geom(
                                                     chamb->layer(CSCConstants::KEY_ALCT_LAYER)->geometry()
                                                     );
  std::unique_ptr<const CSCLayer> layer(
                                        chamb->layer(CSCConstants::KEY_ALCT_LAYER)
                                        );
  
  const uint16_t halfstrip = tp.getStrip();
  const uint16_t pattern = tp.getPattern();
  const uint16_t keyWG = tp.getKeyWG(); 
  //const unsigned maxStrips = layer_geom->numberOfStrips();  

  // so we can extend this later 
  // assume TMB2007 half-strips only as baseline
  double offset = 0.0;
  switch(1) {
  case 1:
    offset = CSCPatternLUT::get2007Position(pattern);
  }
  const unsigned halfstrip_offs = unsigned(0.5 + halfstrip + offset);
  const unsigned strip = halfstrip_offs/2 + 1; // geom starts from 1

  // the rough location of the hit at the ALCT key layer
  // we will refine this using the half strip information
  const LocalPoint coarse_lp = 
    layer_geom->stripWireGroupIntersection(strip,keyWG);  
  const GlobalPoint coarse_gp = layer->surface().toGlobal(coarse_lp);  
  
  // the strip width/4.0 gives the offset of the half-strip
  // center with respect to the strip center
  const double hs_offset = layer_geom->stripPhiPitch()/4.0;
  
  // determine handedness of the chamber
  const bool ccw = isCSCCounterClockwise(layer);
  // we need to subtract the offset of even half strips and add the odd ones
  const double phi_offset = ( ( halfstrip_offs%2 ? 1 : -1)*
                              ( ccw ? -hs_offset : hs_offset ) );
  
  // the global eta calculation uses the middle of the strip
  // so no need to increment it
  const GlobalPoint final_gp( GlobalPoint::Polar( coarse_gp.theta(),
                                                  (coarse_gp.phi().value() + 
                                                   phi_offset),
                                                  coarse_gp.mag() ) );
    
  // We need to add in some notion of the 'error' on trigger primitives
  // like the width of the wire group by the width of the strip
  // or something similar      

  // release ownership of the pointers
  chamb.release();
  layer_geom.release();
  layer.release();
  
  return final_gp;
}

GlobalPoint 
DisplacedL1MuFilter::getCSCSpecificPointStrips(const SimTrackMatchManager& match) const
{
  // do a fit through the comparator digis in this chamber
  // for the phi resolution, use the numbers
  // ME11: 0.00020
  // ME21: 0.00036
  const CSCDigiMatcher& match_cd = match.cscDigis();
    
  for (auto d: match_cd.chamberIdsStrip()){
    auto detId = CSCDetId(d);
    std::cout << "\tNumber of matching CSC comparator strips " << match_cd.cscComparatorDigisInChamber(d).size() << std::endl;
    for (int l=1; l<=6; l++){
      CSCDetId l_id(detId.endcap(), detId.station(), detId.ring(), detId.chamber(), l);
      if(verbose) std::cout << "\tCSCId " << l_id << std::endl;
      std::cout << "\tPrinting available comparator strips in detId: " << match_cd.cscComparatorDigisInDetId(l_id.rawId()).size() << std::endl;
      for (auto p: match_cd.cscComparatorDigisInDetId(l_id.rawId())){
        float fractional_strip = 0.5 * (p.getStrip() + 1) - 0.25;
        auto cscChamber = cscGeometry_->chamber(detId);
        auto layer_geo = cscChamber->layer(l)->geometry();
        LocalPoint csc_intersect = layer_geo->intersectionOfStripAndWire(fractional_strip, 10);
        GlobalPoint csc_gp = cscGeometry_->idToDet(l_id)->surface().toGlobal(csc_intersect);
        //std::cout << "\t\t>>> other CSC LCT phi " << csc_gp.phi() << std::endl;
        //return getCSCSpecificPoint(rawId, lct).phi();
        std::cout << "\t" << l_id << " " << p << " " << csc_gp.phi() << std::endl;
      }
    }
  }
  return GlobalPoint();
}

bool 
DisplacedL1MuFilter::isCSCCounterClockwise(const std::unique_ptr<const CSCLayer>& layer) const {
  const int nStrips = layer->geometry()->numberOfStrips();
  const double phi1 = layer->centerOfStrip(1).phi();
  const double phiN = layer->centerOfStrip(nStrips).phi();
  return ( (std::abs(phi1 - phiN) < M_PI  && phi1 >= phiN) || 
           (std::abs(phi1 - phiN) >= M_PI && phi1 < phiN)     );  
}

void 
DisplacedL1MuFilter::extrapolate(const reco::GenParticle &tk, int station, GlobalPoint& gp, GlobalVector& gv)
{
  TrajectoryStateOnSurface tsos;
  GlobalPoint inner_point(tk.vx(), tk.vy(), tk.vz());
  GlobalVector inner_vec (tk.px(), tk.py(), tk.pz());
  double R, Zmin, Zmax;
  if (station == 1){
    R = 440.; Zmax = 600.; Zmin = -600.;
  }
  else if (station == 2){
    R = 523.; Zmax = 828.; Zmin = -828.;
  }
  // GE11
  else if (station == 11){
    R = 523.; Zmax = 569.; Zmin = -569.;
  }
  // GE21
  else if (station == 21){
    R = 523.; Zmax = 798.; Zmin = -798.;
  }
  else {
    R = 0.; Zmax = 0.; Zmin = 0.;
  }

  if (std::abs(tk.eta())<1.2) tsos = propagateToR(inner_point, inner_vec, tk.charge(), R);
  else if (tk.eta()>1.2)      tsos = propagateToZ(inner_point, inner_vec, tk.charge(), Zmax);
  else if (tk.eta()<-1.2)     tsos = propagateToZ(inner_point, inner_vec, tk.charge(), Zmin);
  else                        tsos = TrajectoryStateOnSurface();

  if (tsos.isValid()){
    gp = tsos.globalPosition();
    gv = tsos.globalMomentum();
    //LocalVector lv = tsos.localMomentum();
    //std::cout << "Local momentum vector: " << lv.eta() << " " << lv.phi() << std::endl;
  } else {
    gp = GlobalPoint();
    gv = GlobalVector();
  }
}

void 
DisplacedL1MuFilter::extrapolate(const TTTrack< Ref_PixelDigi_ > &tk, int station, GlobalPoint& gp, GlobalVector& gv)
{
  TrajectoryStateOnSurface tsos;
  GlobalPoint inner_point(tk.getPOCA());
  GlobalVector inner_vec (tk.getMomentum());
  double charge(tk.getRInv()>0? 1: -1);
  double R, Zmin, Zmax;
  if (station == 1){
    R = 440.; Zmax = 600.; Zmin = -600.;
  }
  else if (station == 2){
    R = 523.; Zmax = 828.; Zmin = -828.;
  }
  else {
    R = 0.; Zmax = 0.; Zmin = 0.;
  }

  if (std::abs(tk.getMomentum().eta())<1.2) tsos = propagateToR(inner_point, inner_vec, charge, R);
  else if (tk.getMomentum().eta()>1.2)      tsos = propagateToZ(inner_point, inner_vec, charge, Zmax);
  else if (tk.getMomentum().eta()<-1.2)     tsos = propagateToZ(inner_point, inner_vec, charge, Zmin);
  else                                      tsos = TrajectoryStateOnSurface();

  if (tsos.isValid()){
    gp = tsos.globalPosition();
    gv = tsos.globalMomentum();
  } else {
    gp = GlobalPoint();
    gv = GlobalVector();
  }
}

// void 
// DisplacedL1MuFilter::extrapolate(const SimTrack&tk, const SimVertex& vtx, double z, GlobalPoint& gp)
// {
//   TrajectoryStateOnSurface tsos;
//   GlobalPoint inner_point(vtx.position().vx(), vtx.position().vy(), vtx.position().vz());
//   GlobalVector inner_vec (tk.px(), tk.py(), tk.pz());
//   // double R, Zmin, Zmax;
//   // if (station == 1){
//   //   R = 440.; Zmax = 600.; Zmin = -600.;
//   // }
//   // else if (station == 2){
//   //   R = 523.; Zmax = 828.; Zmin = -828.;
//   // }
//   // // GE11
//   // else if (station == 11){
//   //   R = 523.; Zmax = 569.; Zmin = -569.;
//   // }
//   // // GE21
//   // else if (station == 21){
//   //   R = 523.; Zmax = 798.; Zmin = -798.;
//   // }
//   // else {
//   //   R = 0.; Zmax = 0.; Zmin = 0.;
//   // }
//   tsos = propagateToZ(inner_point, inner_vec, tk.charge(), z);

//   // if (std::abs(tk.eta())<1.2) tsos = propagateToR(inner_point, inner_vec, tk.charge(), R);
//   // else if (tk.eta()>1.2)      
//   // else if (tk.eta()<-1.2)     tsos = propagateToZ(inner_point, inner_vec, tk.charge(), Zmin);
//   // else                        tsos = TrajectoryStateOnSurface();

//   if (tsos.isValid()){
//     gp = tsos.globalPosition();
//     // gv = tsos.globalMomentum();
//     //LocalVector lv = tsos.localMomentum();
//     //std::cout << "Local momentum vector: " << lv.eta() << " " << lv.phi() << std::endl;
//   } else {
//     gp = GlobalPoint();
//     // gv = GlobalVector();
//   }
// }

GlobalPoint
DisplacedL1MuFilter::extrapolateGP(const TTTrack< Ref_PixelDigi_ > &tk, int station)
{
  TrajectoryStateOnSurface tsos;
  GlobalPoint inner_point(tk.getPOCA());
  GlobalVector inner_vec (tk.getMomentum());
  double charge(tk.getRInv()>0? 1: -1);
  double R, Zmin, Zmax;
  if (station == 1){
    R = 440.; Zmax = 600.; Zmin = -600.;
  }
  else if (station == 2){
    R = 523.; Zmax = 828.; Zmin = -828.;
  }
  else {
    R = 0.; Zmax = 0.; Zmin = 0.;
  }

  if (std::abs(tk.getMomentum().eta())<1.2) tsos = propagateToR(inner_point, inner_vec, charge, R);
  else if (tk.getMomentum().eta()>1.2)      tsos = propagateToZ(inner_point, inner_vec, charge, Zmax);
  else if (tk.getMomentum().eta()<-1.2)     tsos = propagateToZ(inner_point, inner_vec, charge, Zmin);
  else                                      tsos = TrajectoryStateOnSurface();
  
  if (tsos.isValid()) return tsos.globalPosition();
  else                return GlobalPoint();
}

TrajectoryStateOnSurface
DisplacedL1MuFilter::propagateToZ(const GlobalPoint &inner_point, const GlobalVector &inner_vec, double charge, double z) const
{
  Plane::PositionType pos(0.f, 0.f, z);
  Plane::RotationType rot;
  Plane::PlanePointer my_plane(Plane::build(pos, rot));

  FreeTrajectoryState state_start(inner_point, inner_vec, charge, &*magfield_);

  TrajectoryStateOnSurface tsos(propagator_->propagate(state_start, *my_plane));
  if (!tsos.isValid()) tsos = propagatorOpposite_->propagate(state_start, *my_plane);
  return tsos;
}

TrajectoryStateOnSurface
DisplacedL1MuFilter::propagateToR(const GlobalPoint &inner_point, const GlobalVector &inner_vec, double charge, double R) const
{
  Cylinder::CylinderPointer my_cyl(Cylinder::build(Surface::PositionType(0,0,0), Surface::RotationType(), R));

  FreeTrajectoryState state_start(inner_point, inner_vec, charge, &*magfield_);

  TrajectoryStateOnSurface tsos(propagator_->propagate(state_start, *my_cyl));
  if (!tsos.isValid()) tsos = propagatorOpposite_->propagate(state_start, *my_cyl);
  return tsos;
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
  event_tree_->Branch("genGdMu_q", event_.genGdMu_q, "genGdMu_q[2][2]/F");
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

  event_tree_->Branch("genGdMu_etav_prop_GE11", event_.genGdMu_etav_prop_GE11, "genGdMu_etav_prop_GE11[2][2]/F");
  event_tree_->Branch("genGdMu_phiv_prop_GE11", event_.genGdMu_phiv_prop_GE11, "genGdMu_phiv_prop_GE11[2][2]/F");
  event_tree_->Branch("genGdMu_etav_prop_GE21", event_.genGdMu_etav_prop_GE21, "genGdMu_etav_prop_GE21[2][2]/F");
  event_tree_->Branch("genGdMu_phiv_prop_GE21", event_.genGdMu_phiv_prop_GE21, "genGdMu_phiv_prop_GE21[2][2]/F");

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

  event_tree_->Branch("genGdMu_SIM_index", event_.genGdMu_SIM_index, "genGdMu_SIM_index[2][2]/I");
  event_tree_->Branch("genGdMu_SIM_dR", event_.genGdMu_SIM_dR, "genGdMu_SIM_dR[2][2]/F");

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

  event_tree_->Branch("pt_sim", event_.pt_sim, "pt_sim[4]/F");
  event_tree_->Branch("eta_sim", event_.eta_sim, "eta_sim[4]/F");
  event_tree_->Branch("phi_sim", event_.phi_sim, "phi_sim[4]/F");
  event_tree_->Branch("charge_sim", event_.charge_sim, "charge_sim[4]/F");
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
  event_tree_->Branch("DTTF_bx", event_.DTTF_bx,"DTTF_bx[nDTTF]/I");
  event_tree_->Branch("DTTF_nStubs", event_.DTTF_nStubs,"DTTF_nStubs[nDTTF]/I");

  event_tree_->Branch("DTTF_phi1", event_.DTTF_phi1,"DTTF_phi1[nDTTF]/F");
  event_tree_->Branch("DTTF_phib1", event_.DTTF_phib1,"DTTF_phib1[nDTTF]/F");
  event_tree_->Branch("DTTF_quality1", event_.DTTF_quality1,"DTTF_quality1[nDTTF]/I");
  event_tree_->Branch("DTTF_bx1", event_.DTTF_bx1,"DTTF_bx1[nDTTF]/I");
  event_tree_->Branch("DTTF_wh1", event_.DTTF_wh1,"DTTF_wh1[nDTTF]/I");
  event_tree_->Branch("DTTF_se1", event_.DTTF_se1,"DTTF_se1[nDTTF]/I");
  event_tree_->Branch("DTTF_st1", event_.DTTF_st1,"DTTF_st1[nDTTF]/I");

  event_tree_->Branch("DTTF_phi2", event_.DTTF_phi2,"DTTF_phi2[nDTTF]/F");
  event_tree_->Branch("DTTF_phib2", event_.DTTF_phib2,"DTTF_phib2[nDTTF]/F");
  event_tree_->Branch("DTTF_quality2", event_.DTTF_quality2,"DTTF_quality2[nDTTF]/I");
  event_tree_->Branch("DTTF_bx2", event_.DTTF_bx2,"DTTF_bx2[nDTTF]/I");
  event_tree_->Branch("DTTF_wh2", event_.DTTF_wh2,"DTTF_wh2[nDTTF]/I");
  event_tree_->Branch("DTTF_se2", event_.DTTF_se2,"DTTF_se2[nDTTF]/I");
  event_tree_->Branch("DTTF_st2", event_.DTTF_st2,"DTTF_st2[nDTTF]/I");

  event_tree_->Branch("DTTF_phi3", event_.DTTF_phi3,"DTTF_phi3[nDTTF]/F");
  event_tree_->Branch("DTTF_phib3", event_.DTTF_phib3,"DTTF_phib3[nDTTF]/F");
  event_tree_->Branch("DTTF_quality3", event_.DTTF_quality3,"DTTF_quality3[nDTTF]/I");
  event_tree_->Branch("DTTF_bx3", event_.DTTF_bx3,"DTTF_bx3[nDTTF]/I");
  event_tree_->Branch("DTTF_wh3", event_.DTTF_wh3,"DTTF_wh3[nDTTF]/I");
  event_tree_->Branch("DTTF_se3", event_.DTTF_se3,"DTTF_se3[nDTTF]/I");
  event_tree_->Branch("DTTF_st3", event_.DTTF_st3,"DTTF_st3[nDTTF]/I");

  event_tree_->Branch("DTTF_phi4", event_.DTTF_phi4,"DTTF_phi4[nDTTF]/F");
  event_tree_->Branch("DTTF_phib4", event_.DTTF_phib4,"DTTF_phib4[nDTTF]/F");
  event_tree_->Branch("DTTF_quality4", event_.DTTF_quality4,"DTTF_quality4[nDTTF]/I");
  event_tree_->Branch("DTTF_bx4", event_.DTTF_bx4,"DTTF_bx4[nDTTF]/I");
  event_tree_->Branch("DTTF_wh4", event_.DTTF_wh4,"DTTF_wh4[nDTTF]/I");
  event_tree_->Branch("DTTF_se4", event_.DTTF_se4,"DTTF_se4[nDTTF]/I");
  event_tree_->Branch("DTTF_st4", event_.DTTF_st4,"DTTF_st4[nDTTF]/I");


  event_tree_->Branch("nCSCTF", &event_.nCSCTF);
  event_tree_->Branch("L1Mu_CSCTF_index", event_.L1Mu_CSCTF_index,"L1Mu_CSCTF_index[nL1Mu]/I");

  event_tree_->Branch("CSCTF_pt", event_.CSCTF_pt,"CSCTF_pt[nCSCTF]/F");
  event_tree_->Branch("CSCTF_eta", event_.CSCTF_eta,"CSCTF_eta[nCSCTF]/F");
  event_tree_->Branch("CSCTF_phi", event_.CSCTF_phi,"CSCTF_phi[nCSCTF]/F");
  event_tree_->Branch("CSCTF_bx", event_.CSCTF_bx,"CSCTF_bx[nCSCTF]/I");
  event_tree_->Branch("CSCTF_nStubs", event_.CSCTF_nStubs,"CSCTF_nStubs[nCSCTF]/I");
  event_tree_->Branch("CSCTF_quality", event_.CSCTF_quality,"CSCTF_quality[nCSCTF]/I");

  event_tree_->Branch("CSCTF_st1", event_.CSCTF_st1,"CSCTF_st1[nCSCTF]/I");
  event_tree_->Branch("CSCTF_ri1", event_.CSCTF_ri1,"CSCTF_ri1[nCSCTF]/I");
  event_tree_->Branch("CSCTF_ch1", event_.CSCTF_ch1,"CSCTF_ch1[nCSCTF]/I");
  event_tree_->Branch("CSCTF_en1", event_.CSCTF_en1,"CSCTF_en1[nCSCTF]/I");
  // event_tree_->Branch("CSCTF_trk1", event_.CSCTF_trk1,"CSCTF_trk1[nCSCTF]/I");
  // event_tree_->Branch("CSCTF_quality1", event_.CSCTF_quality1,"CSCTF_quality1[nCSCTF]/I");
  // event_tree_->Branch("CSCTF_wg1", event_.CSCTF_wg1,"CSCTF_wg1[nCSCTF]/I");
  // event_tree_->Branch("CSCTF_hs1", event_.CSCTF_hs1,"CSCTF_hs1[nCSCTF]/I");
  event_tree_->Branch("CSCTF_pat1", event_.CSCTF_pat1,"CSCTF_pat1[nCSCTF]/I");
  event_tree_->Branch("CSCTF_bend1", event_.CSCTF_bend1,"CSCTF_bend1[nCSCTF]/I");
  event_tree_->Branch("CSCTF_bx1", event_.CSCTF_bx1,"CSCTF_bx1[nCSCTF]/I");
  event_tree_->Branch("CSCTF_clctpat1", event_.CSCTF_clctpat1,"CSCTF_clctpat1[nCSCTF]/I");
  event_tree_->Branch("CSCTF_val1", event_.CSCTF_val1,"CSCTF_val1[nCSCTF]/I");
  event_tree_->Branch("CSCTF_phi1", event_.CSCTF_phi1,"CSCTF_phi1[nCSCTF]/F");
  event_tree_->Branch("CSCTF_phib1", event_.CSCTF_phib1,"CSCTF_phib1[nCSCTF]/F");

  event_tree_->Branch("CSCTF_st2", event_.CSCTF_st2,"CSCTF_st2[nCSCTF]/I");
  event_tree_->Branch("CSCTF_ri2", event_.CSCTF_ri2,"CSCTF_ri2[nCSCTF]/I");
  event_tree_->Branch("CSCTF_ch2", event_.CSCTF_ch2,"CSCTF_ch2[nCSCTF]/I");
  event_tree_->Branch("CSCTF_en2", event_.CSCTF_en2,"CSCTF_en2[nCSCTF]/I");
  // event_tree_->Branch("CSCTF_trk2", event_.CSCTF_trk2,"CSCTF_trk2[nCSCTF]/I");
  // event_tree_->Branch("CSCTF_quality2", event_.CSCTF_quality2,"CSCTF_quality2[nCSCTF]/I");
  // event_tree_->Branch("CSCTF_wg2", event_.CSCTF_wg2,"CSCTF_wg2[nCSCTF]/I");
  // event_tree_->Branch("CSCTF_hs2", event_.CSCTF_hs2,"CSCTF_hs2[nCSCTF]/I");
  event_tree_->Branch("CSCTF_pat2", event_.CSCTF_pat2,"CSCTF_pat2[nCSCTF]/I");
  event_tree_->Branch("CSCTF_bend2", event_.CSCTF_bend2,"CSCTF_bend2[nCSCTF]/I");
  event_tree_->Branch("CSCTF_bx2", event_.CSCTF_bx2,"CSCTF_bx2[nCSCTF]/I");
  event_tree_->Branch("CSCTF_clctpat2", event_.CSCTF_clctpat2,"CSCTF_clctpat2[nCSCTF]/I");
  event_tree_->Branch("CSCTF_val2", event_.CSCTF_val2,"CSCTF_val2[nCSCTF]/I");
  event_tree_->Branch("CSCTF_phi2", event_.CSCTF_phi2,"CSCTF_phi2[nCSCTF]/F");
  event_tree_->Branch("CSCTF_phib2", event_.CSCTF_phib2,"CSCTF_phib2[nCSCTF]/F");

  event_tree_->Branch("CSCTF_st3", event_.CSCTF_st3,"CSCTF_st3[nCSCTF]/I");
  event_tree_->Branch("CSCTF_ri3", event_.CSCTF_ri3,"CSCTF_ri3[nCSCTF]/I");
  event_tree_->Branch("CSCTF_ch3", event_.CSCTF_ch3,"CSCTF_ch3[nCSCTF]/I");
  event_tree_->Branch("CSCTF_en3", event_.CSCTF_en3,"CSCTF_en3[nCSCTF]/I");
  // event_tree_->Branch("CSCTF_trk3", event_.CSCTF_trk3,"CSCTF_trk3[nCSCTF]/I");
  // event_tree_->Branch("CSCTF_quality3", event_.CSCTF_quality3,"CSCTF_quality3[nCSCTF]/I");
  // event_tree_->Branch("CSCTF_wg3", event_.CSCTF_wg3,"CSCTF_wg3[nCSCTF]/I");
  // event_tree_->Branch("CSCTF_hs3", event_.CSCTF_hs3,"CSCTF_hs3[nCSCTF]/I");
  event_tree_->Branch("CSCTF_pat3", event_.CSCTF_pat3,"CSCTF_pat3[nCSCTF]/I");
  event_tree_->Branch("CSCTF_bend3", event_.CSCTF_bend3,"CSCTF_bend3[nCSCTF]/I");
  event_tree_->Branch("CSCTF_bx3", event_.CSCTF_bx3,"CSCTF_bx3[nCSCTF]/I");
  event_tree_->Branch("CSCTF_clctpat3", event_.CSCTF_clctpat3,"CSCTF_clctpat3[nCSCTF]/I");
  event_tree_->Branch("CSCTF_val3", event_.CSCTF_val3,"CSCTF_val3[nCSCTF]/I");
  event_tree_->Branch("CSCTF_phi3", event_.CSCTF_phi3,"CSCTF_phi3[nCSCTF]/F");
  event_tree_->Branch("CSCTF_phib3", event_.CSCTF_phib3,"CSCTF_phib3[nCSCTF]/F");

  event_tree_->Branch("CSCTF_st4", event_.CSCTF_st4,"CSCTF_st4[nCSCTF]/I");
  event_tree_->Branch("CSCTF_ri4", event_.CSCTF_ri4,"CSCTF_ri4[nCSCTF]/I");
  event_tree_->Branch("CSCTF_ch4", event_.CSCTF_ch4,"CSCTF_ch4[nCSCTF]/I");
  event_tree_->Branch("CSCTF_en4", event_.CSCTF_en4,"CSCTF_en4[nCSCTF]/I");
  // event_tree_->Branch("CSCTF_trk4", event_.CSCTF_trk4,"CSCTF_trk4[nCSCTF]/I");
  // event_tree_->Branch("CSCTF_quality4", event_.CSCTF_quality4,"CSCTF_quality4[nCSCTF]/I");
  // event_tree_->Branch("CSCTF_wg4", event_.CSCTF_wg4,"CSCTF_wg4[nCSCTF]/I");
  // event_tree_->Branch("CSCTF_hs4", event_.CSCTF_hs4,"CSCTF_hs4[nCSCTF]/I");
  event_tree_->Branch("CSCTF_pat4", event_.CSCTF_pat4,"CSCTF_pat4[nCSCTF]/I");
  event_tree_->Branch("CSCTF_bend4", event_.CSCTF_bend4,"CSCTF_bend4[nCSCTF]/I");
  event_tree_->Branch("CSCTF_bx4", event_.CSCTF_bx4,"CSCTF_bx4[nCSCTF]/I");
  event_tree_->Branch("CSCTF_clctpat4", event_.CSCTF_clctpat4,"CSCTF_clctpat4[nCSCTF]/I");
  event_tree_->Branch("CSCTF_val4", event_.CSCTF_val4,"CSCTF_val4[nCSCTF]/I");
  event_tree_->Branch("CSCTF_phi4", event_.CSCTF_phi4,"CSCTF_phi4[nCSCTF]/F");
  event_tree_->Branch("CSCTF_phib4", event_.CSCTF_phib4,"CSCTF_phib4[nCSCTF]/F");

  event_tree_->Branch("CSCTF_eta1", event_.CSCTF_eta1,"CSCTF_eta1[nCSCTF]/F");
  event_tree_->Branch("CSCTF_eta2", event_.CSCTF_eta2,"CSCTF_eta2[nCSCTF]/F");
  event_tree_->Branch("CSCTF_eta3", event_.CSCTF_eta3,"CSCTF_eta3[nCSCTF]/F");
  event_tree_->Branch("CSCTF_eta4", event_.CSCTF_eta4,"CSCTF_eta4[nCSCTF]/F");

  event_tree_->Branch("CSCTF_gemdphi1", event_.CSCTF_gemdphi1,"CSCTF_gemdphi1[nCSCTF]/F");
  event_tree_->Branch("CSCTF_gemdphi2", event_.CSCTF_gemdphi2,"CSCTF_gemdphi2[nCSCTF]/F");

  // true positions
  event_tree_->Branch("CSCTF_R1", event_.CSCTF_R1,"CSCTF_R1[nCSCTF]/F");
  event_tree_->Branch("CSCTF_x1", event_.CSCTF_x1,"CSCTF_x1[nCSCTF]/F");
  event_tree_->Branch("CSCTF_y1", event_.CSCTF_y1,"CSCTF_y1[nCSCTF]/F");
  event_tree_->Branch("CSCTF_z1", event_.CSCTF_z1,"CSCTF_z1[nCSCTF]/F");

  event_tree_->Branch("CSCTF_R2", event_.CSCTF_R2,"CSCTF_R2[nCSCTF]/F");
  event_tree_->Branch("CSCTF_x2", event_.CSCTF_x2,"CSCTF_x2[nCSCTF]/F");
  event_tree_->Branch("CSCTF_y2", event_.CSCTF_y2,"CSCTF_y2[nCSCTF]/F");
  event_tree_->Branch("CSCTF_z2", event_.CSCTF_z2,"CSCTF_z2[nCSCTF]/F");

  event_tree_->Branch("CSCTF_R3", event_.CSCTF_R3,"CSCTF_R3[nCSCTF]/F");
  event_tree_->Branch("CSCTF_x3", event_.CSCTF_x3,"CSCTF_x3[nCSCTF]/F");
  event_tree_->Branch("CSCTF_y3", event_.CSCTF_y3,"CSCTF_y3[nCSCTF]/F");
  event_tree_->Branch("CSCTF_z3", event_.CSCTF_z3,"CSCTF_z3[nCSCTF]/F");

  event_tree_->Branch("CSCTF_R4", event_.CSCTF_R4,"CSCTF_R4[nCSCTF]/F");
  event_tree_->Branch("CSCTF_x4", event_.CSCTF_x4,"CSCTF_x4[nCSCTF]/F");
  event_tree_->Branch("CSCTF_y4", event_.CSCTF_y4,"CSCTF_y4[nCSCTF]/F");
  event_tree_->Branch("CSCTF_z4", event_.CSCTF_z4,"CSCTF_z4[nCSCTF]/F");


  event_tree_->Branch("CSCTF_rec_ch1", event_.CSCTF_rec_ch1,"CSCTF_rec_ch1[50]/I");
  event_tree_->Branch("CSCTF_rec_phi1", event_.CSCTF_rec_phi1,"CSCTF_rec_phi1[50]/F");
  event_tree_->Branch("CSCTF_rec_phib1", event_.CSCTF_rec_phib1,"CSCTF_rec_phib1[50]/F");
  event_tree_->Branch("CSCTF_rec_R1", event_.CSCTF_rec_R1,"CSCTF_rec_R1[50]/F");
  event_tree_->Branch("CSCTF_rec_x1", event_.CSCTF_rec_x1,"CSCTF_rec_x1[50]/F");
  event_tree_->Branch("CSCTF_rec_y1", event_.CSCTF_rec_y1,"CSCTF_rec_y1[50]/F");
  event_tree_->Branch("CSCTF_rec_z1", event_.CSCTF_rec_z1,"CSCTF_rec_z1[50]/F");

  event_tree_->Branch("CSCTF_rec_ch2", event_.CSCTF_rec_ch2,"CSCTF_rec_ch2[50]/I");
  event_tree_->Branch("CSCTF_rec_phi2", event_.CSCTF_rec_phi2,"CSCTF_rec_phi2[50]/F");
  event_tree_->Branch("CSCTF_rec_phib2", event_.CSCTF_rec_phib2,"CSCTF_rec_phib2[50]/F");
  event_tree_->Branch("CSCTF_rec_R2", event_.CSCTF_rec_R2,"CSCTF_rec_R2[50]/F");
  event_tree_->Branch("CSCTF_rec_x2", event_.CSCTF_rec_x2,"CSCTF_rec_x2[50]/F");
  event_tree_->Branch("CSCTF_rec_y2", event_.CSCTF_rec_y2,"CSCTF_rec_y2[50]/F");
  event_tree_->Branch("CSCTF_rec_z2", event_.CSCTF_rec_z2,"CSCTF_rec_z2[50]/F");

  event_tree_->Branch("CSCTF_rec_ch3", event_.CSCTF_rec_ch3,"CSCTF_rec_ch3[50]/I");
  event_tree_->Branch("CSCTF_rec_phi3", event_.CSCTF_rec_phi3,"CSCTF_rec_phi3[50]/F");
  event_tree_->Branch("CSCTF_rec_phib3", event_.CSCTF_rec_phib3,"CSCTF_rec_phib3[50]/F");
  event_tree_->Branch("CSCTF_rec_R3", event_.CSCTF_rec_R3,"CSCTF_rec_R3[50]/F");
  event_tree_->Branch("CSCTF_rec_x3", event_.CSCTF_rec_x3,"CSCTF_rec_x3[50]/F");
  event_tree_->Branch("CSCTF_rec_y3", event_.CSCTF_rec_y3,"CSCTF_rec_y3[50]/F");
  event_tree_->Branch("CSCTF_rec_z3", event_.CSCTF_rec_z3,"CSCTF_rec_z3[50]/F");

  event_tree_->Branch("CSCTF_rec_ch4", event_.CSCTF_rec_ch4,"CSCTF_rec_ch4[50]/I");
  event_tree_->Branch("CSCTF_rec_phi4", event_.CSCTF_rec_phi4,"CSCTF_rec_phi4[50]/F");
  event_tree_->Branch("CSCTF_rec_phib4", event_.CSCTF_rec_phib4,"CSCTF_rec_phib4[50]/F");
  event_tree_->Branch("CSCTF_rec_R4", event_.CSCTF_rec_R4,"CSCTF_rec_R4[50]/F");
  event_tree_->Branch("CSCTF_rec_x4", event_.CSCTF_rec_x4,"CSCTF_rec_x4[50]/F");
  event_tree_->Branch("CSCTF_rec_y4", event_.CSCTF_rec_y4,"CSCTF_rec_y4[50]/F");
  event_tree_->Branch("CSCTF_rec_z4", event_.CSCTF_rec_z4,"CSCTF_rec_z4[50]/F");

  event_tree_->Branch("CSCTF_rec_eta1", event_.CSCTF_rec_eta1,"CSCTF_rec_eta1[50]/F");
  event_tree_->Branch("CSCTF_rec_eta2", event_.CSCTF_rec_eta2,"CSCTF_rec_eta2[50]/F");
  event_tree_->Branch("CSCTF_rec_eta3", event_.CSCTF_rec_eta3,"CSCTF_rec_eta3[50]/F");
  event_tree_->Branch("CSCTF_rec_eta4", event_.CSCTF_rec_eta4,"CSCTF_rec_eta4[50]/F");


  event_tree_->Branch("CSCTF_fit_phi1", event_.CSCTF_fit_phi1,"CSCTF_fit_phi1[50]/F");
  event_tree_->Branch("CSCTF_fit_phi2", event_.CSCTF_fit_phi2,"CSCTF_fit_phi2[50]/F");
  event_tree_->Branch("CSCTF_fit_phi3", event_.CSCTF_fit_phi3,"CSCTF_fit_phi3[50]/F");
  event_tree_->Branch("CSCTF_fit_phi4", event_.CSCTF_fit_phi4,"CSCTF_fit_phi4[50]/F");

  event_tree_->Branch("CSCTF_fit_dphi1", event_.CSCTF_fit_dphi1,"CSCTF_fit_dphi1[50]/F");
  event_tree_->Branch("CSCTF_fit_dphi2", event_.CSCTF_fit_dphi2,"CSCTF_fit_dphi2[50]/F");
  event_tree_->Branch("CSCTF_fit_dphi3", event_.CSCTF_fit_dphi3,"CSCTF_fit_dphi3[50]/F");
  event_tree_->Branch("CSCTF_fit_dphi4", event_.CSCTF_fit_dphi4,"CSCTF_fit_dphi4[50]/F");

  event_tree_->Branch("CSCTF_fit_R1", event_.CSCTF_fit_R1,"CSCTF_fit_R1[50]/F");
  event_tree_->Branch("CSCTF_fit_R2", event_.CSCTF_fit_R2,"CSCTF_fit_R2[50]/F");
  event_tree_->Branch("CSCTF_fit_R3", event_.CSCTF_fit_R3,"CSCTF_fit_R3[50]/F");
  event_tree_->Branch("CSCTF_fit_R4", event_.CSCTF_fit_R4,"CSCTF_fit_R4[50]/F");

  event_tree_->Branch("CSCTF_fit_x1", event_.CSCTF_fit_x1,"CSCTF_fit_x1[50]/F");
  event_tree_->Branch("CSCTF_fit_x2", event_.CSCTF_fit_x2,"CSCTF_fit_x2[50]/F");
  event_tree_->Branch("CSCTF_fit_x3", event_.CSCTF_fit_x3,"CSCTF_fit_x3[50]/F");
  event_tree_->Branch("CSCTF_fit_x4", event_.CSCTF_fit_x4,"CSCTF_fit_x4[50]/F");

  event_tree_->Branch("CSCTF_fit_y1", event_.CSCTF_fit_y1,"CSCTF_fit_y1[50]/F");
  event_tree_->Branch("CSCTF_fit_y2", event_.CSCTF_fit_y2,"CSCTF_fit_y2[50]/F");
  event_tree_->Branch("CSCTF_fit_y3", event_.CSCTF_fit_y3,"CSCTF_fit_y3[50]/F");
  event_tree_->Branch("CSCTF_fit_y4", event_.CSCTF_fit_y4,"CSCTF_fit_y4[50]/F");

  event_tree_->Branch("CSCTF_fit_z1", event_.CSCTF_fit_z1,"CSCTF_fit_z1[50]/F");
  event_tree_->Branch("CSCTF_fit_z2", event_.CSCTF_fit_z2,"CSCTF_fit_z2[50]/F");
  event_tree_->Branch("CSCTF_fit_z3", event_.CSCTF_fit_z3,"CSCTF_fit_z3[50]/F");
  event_tree_->Branch("CSCTF_fit_z4", event_.CSCTF_fit_z4,"CSCTF_fit_z4[50]/F");

  event_tree_->Branch("CSCTF_fitline_x1", event_.CSCTF_fitline_x1,"CSCTF_fitline_x1[50]/F");
  event_tree_->Branch("CSCTF_fitline_x2", event_.CSCTF_fitline_x2,"CSCTF_fitline_x2[50]/F");
  event_tree_->Branch("CSCTF_fitline_x3", event_.CSCTF_fitline_x3,"CSCTF_fitline_x3[50]/F");
  event_tree_->Branch("CSCTF_fitline_x4", event_.CSCTF_fitline_x4,"CSCTF_fitline_x4[50]/F");

  event_tree_->Branch("CSCTF_fitline_y1", event_.CSCTF_fitline_y1,"CSCTF_fitline_y1[50]/F");
  event_tree_->Branch("CSCTF_fitline_y2", event_.CSCTF_fitline_y2,"CSCTF_fitline_y2[50]/F");
  event_tree_->Branch("CSCTF_fitline_y3", event_.CSCTF_fitline_y3,"CSCTF_fitline_y3[50]/F");
  event_tree_->Branch("CSCTF_fitline_y4", event_.CSCTF_fitline_y4,"CSCTF_fitline_y4[50]/F");

  event_tree_->Branch("CSCTF_sim_phi1", event_.CSCTF_sim_phi1,"CSCTF_sim_phi1[50]/F");
  event_tree_->Branch("CSCTF_sim_phi2", event_.CSCTF_sim_phi2,"CSCTF_sim_phi2[50]/F");
  event_tree_->Branch("CSCTF_sim_phi3", event_.CSCTF_sim_phi3,"CSCTF_sim_phi3[50]/F");
  event_tree_->Branch("CSCTF_sim_phi4", event_.CSCTF_sim_phi4,"CSCTF_sim_phi4[50]/F");

  event_tree_->Branch("CSCTF_sim_eta1", event_.CSCTF_sim_eta1,"CSCTF_sim_eta1[50]/F");
  event_tree_->Branch("CSCTF_sim_eta2", event_.CSCTF_sim_eta2,"CSCTF_sim_eta2[50]/F");
  event_tree_->Branch("CSCTF_sim_eta3", event_.CSCTF_sim_eta3,"CSCTF_sim_eta3[50]/F");
  event_tree_->Branch("CSCTF_sim_eta4", event_.CSCTF_sim_eta4,"CSCTF_sim_eta4[50]/F");

  event_tree_->Branch("CSCTF_sim_R1", event_.CSCTF_sim_R1,"CSCTF_sim_R1[50]/F");
  event_tree_->Branch("CSCTF_sim_R2", event_.CSCTF_sim_R2,"CSCTF_sim_R2[50]/F");
  event_tree_->Branch("CSCTF_sim_R3", event_.CSCTF_sim_R3,"CSCTF_sim_R3[50]/F");
  event_tree_->Branch("CSCTF_sim_R4", event_.CSCTF_sim_R4,"CSCTF_sim_R4[50]/F");

  event_tree_->Branch("CSCTF_sim_x1", event_.CSCTF_sim_x1,"CSCTF_sim_x1[50]/F");
  event_tree_->Branch("CSCTF_sim_x2", event_.CSCTF_sim_x2,"CSCTF_sim_x2[50]/F");
  event_tree_->Branch("CSCTF_sim_x3", event_.CSCTF_sim_x3,"CSCTF_sim_x3[50]/F");
  event_tree_->Branch("CSCTF_sim_x4", event_.CSCTF_sim_x4,"CSCTF_sim_x4[50]/F");

  event_tree_->Branch("CSCTF_sim_y1", event_.CSCTF_sim_y1,"CSCTF_sim_y1[50]/F");
  event_tree_->Branch("CSCTF_sim_y2", event_.CSCTF_sim_y2,"CSCTF_sim_y2[50]/F");
  event_tree_->Branch("CSCTF_sim_y3", event_.CSCTF_sim_y3,"CSCTF_sim_y3[50]/F");
  event_tree_->Branch("CSCTF_sim_y4", event_.CSCTF_sim_y4,"CSCTF_sim_y4[50]/F");

  event_tree_->Branch("CSCTF_sim_z1", event_.CSCTF_sim_z1,"CSCTF_sim_z1[50]/F");
  event_tree_->Branch("CSCTF_sim_z2", event_.CSCTF_sim_z2,"CSCTF_sim_z2[50]/F");
  event_tree_->Branch("CSCTF_sim_z3", event_.CSCTF_sim_z3,"CSCTF_sim_z3[50]/F");
  event_tree_->Branch("CSCTF_sim_z4", event_.CSCTF_sim_z4,"CSCTF_sim_z4[50]/F");


  if (processRPCb_) {
  event_tree_->Branch("nRPCb", &event_.nRPCb);
  event_tree_->Branch("L1Mu_RPCb_index", event_.L1Mu_RPCb_index,"L1Mu_RPCb_index[nL1Mu]/I");

  event_tree_->Branch("RPCb_pt", event_.RPCb_pt,"RPCb_pt[nRPCb]/F");
  event_tree_->Branch("RPCb_eta", event_.RPCb_eta,"RPCb_eta[nRPCb]/F");
  event_tree_->Branch("RPCb_phi", event_.RPCb_phi,"RPCb_phi[nRPCb]/F");
  event_tree_->Branch("RPCb_bx", event_.RPCb_bx,"RPCb_bx[nRPCb]/I");
  event_tree_->Branch("RPCb_nStubs", event_.RPCb_nStubs,"RPCb_nStubs[nRPCb]/I");
  event_tree_->Branch("RPCb_quality", event_.RPCb_quality,"RPCb_quality[nRPCb]/I");

  event_tree_->Branch("RPCb_bx1", event_.RPCb_bx1,"RPCb_bx1[nRPCb]/I");
  event_tree_->Branch("RPCb_strip1", event_.RPCb_strip1,"RPCb_strip1[nRPCb]/I");
  event_tree_->Branch("RPCb_phi1", event_.RPCb_phi1,"RPCb_phi1[nRPCb]/F");
  event_tree_->Branch("RPCb_re1", event_.RPCb_re1,"RPCb_re1[nRPCb]/I");
  event_tree_->Branch("RPCb_ri1", event_.RPCb_ri1,"RPCb_ri1[nRPCb]/I");
  event_tree_->Branch("RPCb_st1", event_.RPCb_st1,"RPCb_st1[nRPCb]/I");
  event_tree_->Branch("RPCb_se1", event_.RPCb_se1,"RPCb_se1[nRPCb]/I");
  event_tree_->Branch("RPCb_la1", event_.RPCb_la1,"RPCb_la1[nRPCb]/I");
  event_tree_->Branch("RPCb_su1", event_.RPCb_su1,"RPCb_su1[nRPCb]/I");
  event_tree_->Branch("RPCb_ro1", event_.RPCb_ro1,"RPCb_ro1[nRPCb]/I");
  
  event_tree_->Branch("RPCb_bx2", event_.RPCb_bx2,"RPCb_bx2[nRPCb]/I");
  event_tree_->Branch("RPCb_strip2", event_.RPCb_strip2,"RPCb_strip2[nRPCb]/I");
  event_tree_->Branch("RPCb_phi2", event_.RPCb_phi2,"RPCb_phi2[nRPCb]/F");
  event_tree_->Branch("RPCb_re2", event_.RPCb_re2,"RPCb_re2[nRPCb]/I");
  event_tree_->Branch("RPCb_ri2", event_.RPCb_ri2,"RPCb_ri2[nRPCb]/I");
  event_tree_->Branch("RPCb_st2", event_.RPCb_st2,"RPCb_st2[nRPCb]/I");
  event_tree_->Branch("RPCb_se2", event_.RPCb_se2,"RPCb_se2[nRPCb]/I");
  event_tree_->Branch("RPCb_la2", event_.RPCb_la2,"RPCb_la2[nRPCb]/I");
  event_tree_->Branch("RPCb_su2", event_.RPCb_su2,"RPCb_su2[nRPCb]/I");
  event_tree_->Branch("RPCb_ro2", event_.RPCb_ro2,"RPCb_ro2[nRPCb]/I");

  event_tree_->Branch("RPCb_bx3", event_.RPCb_bx3,"RPCb_bx3[nRPCb]/I");
  event_tree_->Branch("RPCb_strip3", event_.RPCb_strip3,"RPCb_strip3[nRPCb]/I");
  event_tree_->Branch("RPCb_phi3", event_.RPCb_phi3,"RPCb_phi3[nRPCb]/F");
  event_tree_->Branch("RPCb_re3", event_.RPCb_re3,"RPCb_re3[nRPCb]/I");
  event_tree_->Branch("RPCb_ri3", event_.RPCb_ri3,"RPCb_ri3[nRPCb]/I");
  event_tree_->Branch("RPCb_st3", event_.RPCb_st3,"RPCb_st3[nRPCb]/I");
  event_tree_->Branch("RPCb_se3", event_.RPCb_se3,"RPCb_se3[nRPCb]/I");
  event_tree_->Branch("RPCb_la3", event_.RPCb_la3,"RPCb_la3[nRPCb]/I");
  event_tree_->Branch("RPCb_su3", event_.RPCb_su3,"RPCb_su3[nRPCb]/I");
  event_tree_->Branch("RPCb_ro3", event_.RPCb_ro3,"RPCb_ro3[nRPCb]/I");

  event_tree_->Branch("RPCb_bx4", event_.RPCb_bx4,"RPCb_bx4[nRPCb]/I");
  event_tree_->Branch("RPCb_strip4", event_.RPCb_strip4,"RPCb_strip4[nRPCb]/I");
  event_tree_->Branch("RPCb_phi4", event_.RPCb_phi4,"RPCb_phi4[nRPCb]/F");
  event_tree_->Branch("RPCb_re4", event_.RPCb_re4,"RPCb_re4[nRPCb]/I");
  event_tree_->Branch("RPCb_ri4", event_.RPCb_ri4,"RPCb_ri4[nRPCb]/I");
  event_tree_->Branch("RPCb_st4", event_.RPCb_st4,"RPCb_st4[nRPCb]/I");
  event_tree_->Branch("RPCb_se4", event_.RPCb_se4,"RPCb_se4[nRPCb]/I");
  event_tree_->Branch("RPCb_la4", event_.RPCb_la4,"RPCb_la4[nRPCb]/I");
  event_tree_->Branch("RPCb_su4", event_.RPCb_su4,"RPCb_su4[nRPCb]/I");
  event_tree_->Branch("RPCb_ro4", event_.RPCb_ro4,"RPCb_ro4[nRPCb]/I");

  event_tree_->Branch("RPCb_bx5", event_.RPCb_bx5,"RPCb_bx5[nRPCb]/I");
  event_tree_->Branch("RPCb_strip5", event_.RPCb_strip5,"RPCb_strip5[nRPCb]/I");
  event_tree_->Branch("RPCb_phi5", event_.RPCb_phi5,"RPCb_phi5[nRPCb]/F");
  event_tree_->Branch("RPCb_re5", event_.RPCb_re5,"RPCb_re5[nRPCb]/I");
  event_tree_->Branch("RPCb_ri5", event_.RPCb_ri5,"RPCb_ri5[nRPCb]/I");
  event_tree_->Branch("RPCb_st5", event_.RPCb_st5,"RPCb_st5[nRPCb]/I");
  event_tree_->Branch("RPCb_se5", event_.RPCb_se5,"RPCb_se5[nRPCb]/I");
  event_tree_->Branch("RPCb_la5", event_.RPCb_la5,"RPCb_la5[nRPCb]/I");
  event_tree_->Branch("RPCb_su5", event_.RPCb_su5,"RPCb_su5[nRPCb]/I");
  event_tree_->Branch("RPCb_ro5", event_.RPCb_ro5,"RPCb_ro5[nRPCb]/I");

  event_tree_->Branch("RPCb_bx6", event_.RPCb_bx6,"RPCb_bx6[nRPCb]/I");
  event_tree_->Branch("RPCb_strip6", event_.RPCb_strip6,"RPCb_strip6[nRPCb]/I");
  event_tree_->Branch("RPCb_phi6", event_.RPCb_phi6,"RPCb_phi6[nRPCb]/F");
  event_tree_->Branch("RPCb_re6", event_.RPCb_re6,"RPCb_re6[nRPCb]/I");
  event_tree_->Branch("RPCb_ri6", event_.RPCb_ri6,"RPCb_ri6[nRPCb]/I");
  event_tree_->Branch("RPCb_st6", event_.RPCb_st6,"RPCb_st6[nRPCb]/I");
  event_tree_->Branch("RPCb_se6", event_.RPCb_se6,"RPCb_se6[nRPCb]/I");
  event_tree_->Branch("RPCb_la6", event_.RPCb_la6,"RPCb_la6[nRPCb]/I");
  event_tree_->Branch("RPCb_su6", event_.RPCb_su6,"RPCb_su6[nRPCb]/I");
  event_tree_->Branch("RPCb_ro6", event_.RPCb_ro6,"RPCb_ro6[nRPCb]/I");
  }

  if (processRPCf_) {
  event_tree_->Branch("nRPCf", &event_.nRPCf);
  event_tree_->Branch("L1Mu_RPCf_index", event_.L1Mu_RPCf_index,"L1Mu_RPCf_index[nL1Mu]/I");

  event_tree_->Branch("RPCf_pt", event_.RPCf_pt,"RPCf_pt[nRPCf]/F");
  event_tree_->Branch("RPCf_eta", event_.RPCf_eta,"RPCf_eta[nRPCf]/F");
  event_tree_->Branch("RPCf_phi", event_.RPCf_phi,"RPCf_phi[nRPCf]/F");
  event_tree_->Branch("RPCf_bx", event_.RPCf_bx,"RPCf_bx[nRPCf]/I");
  event_tree_->Branch("RPCf_nStubs", event_.RPCf_nStubs,"RPCf_nStubs[nRPCf]/I");
  event_tree_->Branch("RPCf_quality", event_.RPCf_quality,"RPCf_quality[nRPCf]/I");

  event_tree_->Branch("RPCf_bx1", event_.RPCf_bx1,"RPCf_bx1[nRPCf]/I");
  event_tree_->Branch("RPCf_strip1", event_.RPCf_strip1,"RPCf_strip1[nRPCf]/I");
  event_tree_->Branch("RPCf_phi1", event_.RPCf_phi1,"RPCf_phi1[nRPCf]/F");
  event_tree_->Branch("RPCf_re1", event_.RPCf_re1,"RPCf_re1[nRPCf]/I");
  event_tree_->Branch("RPCf_ri1", event_.RPCf_ri1,"RPCf_ri1[nRPCf]/I");
  event_tree_->Branch("RPCf_st1", event_.RPCf_st1,"RPCf_st1[nRPCf]/I");
  event_tree_->Branch("RPCf_se1", event_.RPCf_se1,"RPCf_se1[nRPCf]/I");
  event_tree_->Branch("RPCf_la1", event_.RPCf_la1,"RPCf_la1[nRPCf]/I");
  event_tree_->Branch("RPCf_su1", event_.RPCf_su1,"RPCf_su1[nRPCf]/I");
  event_tree_->Branch("RPCf_ro1", event_.RPCf_ro1,"RPCf_ro1[nRPCf]/I");
  
  event_tree_->Branch("RPCf_bx2", event_.RPCf_bx2,"RPCf_bx2[nRPCf]/I");
  event_tree_->Branch("RPCf_strip2", event_.RPCf_strip2,"RPCf_strip2[nRPCf]/I");
  event_tree_->Branch("RPCf_phi2", event_.RPCf_phi2,"RPCf_phi2[nRPCf]/F");
  event_tree_->Branch("RPCf_re2", event_.RPCf_re2,"RPCf_re2[nRPCf]/I");
  event_tree_->Branch("RPCf_ri2", event_.RPCf_ri2,"RPCf_ri2[nRPCf]/I");
  event_tree_->Branch("RPCf_st2", event_.RPCf_st2,"RPCf_st2[nRPCf]/I");
  event_tree_->Branch("RPCf_se2", event_.RPCf_se2,"RPCf_se2[nRPCf]/I");
  event_tree_->Branch("RPCf_la2", event_.RPCf_la2,"RPCf_la2[nRPCf]/I");
  event_tree_->Branch("RPCf_su2", event_.RPCf_su2,"RPCf_su2[nRPCf]/I");
  event_tree_->Branch("RPCf_ro2", event_.RPCf_ro2,"RPCf_ro2[nRPCf]/I");

  event_tree_->Branch("RPCf_bx3", event_.RPCf_bx3,"RPCf_bx3[nRPCf]/I");
  event_tree_->Branch("RPCf_strip3", event_.RPCf_strip3,"RPCf_strip3[nRPCf]/I");
  event_tree_->Branch("RPCf_phi3", event_.RPCf_phi3,"RPCf_phi3[nRPCf]/F");
  event_tree_->Branch("RPCf_re3", event_.RPCf_re3,"RPCf_re3[nRPCf]/I");
  event_tree_->Branch("RPCf_ri3", event_.RPCf_ri3,"RPCf_ri3[nRPCf]/I");
  event_tree_->Branch("RPCf_st3", event_.RPCf_st3,"RPCf_st3[nRPCf]/I");
  event_tree_->Branch("RPCf_se3", event_.RPCf_se3,"RPCf_se3[nRPCf]/I");
  event_tree_->Branch("RPCf_la3", event_.RPCf_la3,"RPCf_la3[nRPCf]/I");
  event_tree_->Branch("RPCf_su3", event_.RPCf_su3,"RPCf_su3[nRPCf]/I");
  event_tree_->Branch("RPCf_ro3", event_.RPCf_ro3,"RPCf_ro3[nRPCf]/I");

  event_tree_->Branch("RPCf_bx4", event_.RPCf_bx4,"RPCf_bx4[nRPCf]/I");
  event_tree_->Branch("RPCf_strip4", event_.RPCf_strip4,"RPCf_strip4[nRPCf]/I");
  event_tree_->Branch("RPCf_phi4", event_.RPCf_phi4,"RPCf_phi4[nRPCf]/F");
  event_tree_->Branch("RPCf_re4", event_.RPCf_re4,"RPCf_re4[nRPCf]/I");
  event_tree_->Branch("RPCf_ri4", event_.RPCf_ri4,"RPCf_ri4[nRPCf]/I");
  event_tree_->Branch("RPCf_st4", event_.RPCf_st4,"RPCf_st4[nRPCf]/I");
  event_tree_->Branch("RPCf_se4", event_.RPCf_se4,"RPCf_se4[nRPCf]/I");
  event_tree_->Branch("RPCf_la4", event_.RPCf_la4,"RPCf_la4[nRPCf]/I");
  event_tree_->Branch("RPCf_su4", event_.RPCf_su4,"RPCf_su4[nRPCf]/I");
  event_tree_->Branch("RPCf_ro4", event_.RPCf_ro4,"RPCf_ro4[nRPCf]/I");

  event_tree_->Branch("RPCf_bx5", event_.RPCf_bx5,"RPCf_bx5[nRPCf]/I");
  event_tree_->Branch("RPCf_strip5", event_.RPCf_strip5,"RPCf_strip5[nRPCf]/I");
  event_tree_->Branch("RPCf_phi5", event_.RPCf_phi5,"RPCf_phi5[nRPCf]/F");
  event_tree_->Branch("RPCf_re5", event_.RPCf_re5,"RPCf_re5[nRPCf]/I");
  event_tree_->Branch("RPCf_ri5", event_.RPCf_ri5,"RPCf_ri5[nRPCf]/I");
  event_tree_->Branch("RPCf_st5", event_.RPCf_st5,"RPCf_st5[nRPCf]/I");
  event_tree_->Branch("RPCf_se5", event_.RPCf_se5,"RPCf_se5[nRPCf]/I");
  event_tree_->Branch("RPCf_la5", event_.RPCf_la5,"RPCf_la5[nRPCf]/I");
  event_tree_->Branch("RPCf_su5", event_.RPCf_su5,"RPCf_su5[nRPCf]/I");
  event_tree_->Branch("RPCf_ro5", event_.RPCf_ro5,"RPCf_ro5[nRPCf]/I");

  event_tree_->Branch("RPCf_bx6", event_.RPCf_bx6,"RPCf_bx6[nRPCf]/I");
  event_tree_->Branch("RPCf_strip6", event_.RPCf_strip6,"RPCf_strip6[nRPCf]/I");
  event_tree_->Branch("RPCf_phi6", event_.RPCf_phi6,"RPCf_phi6[nRPCf]/F");
  event_tree_->Branch("RPCf_re6", event_.RPCf_re6,"RPCf_re6[nRPCf]/I");
  event_tree_->Branch("RPCf_ri6", event_.RPCf_ri6,"RPCf_ri6[nRPCf]/I");
  event_tree_->Branch("RPCf_st6", event_.RPCf_st6,"RPCf_st6[nRPCf]/I");
  event_tree_->Branch("RPCf_se6", event_.RPCf_se6,"RPCf_se6[nRPCf]/I");
  event_tree_->Branch("RPCf_la6", event_.RPCf_la6,"RPCf_la6[nRPCf]/I");
  event_tree_->Branch("RPCf_su6", event_.RPCf_su6,"RPCf_su6[nRPCf]/I");
  event_tree_->Branch("RPCf_ro6", event_.RPCf_ro6,"RPCf_ro6[nRPCf]/I");
  }

  event_tree_->Branch("nGEM", &event_.nGEM);
  event_tree_->Branch("GE11_phi_L1", event_.GE11_phi_L1,"GE11_phi_L1[50]/F");
  event_tree_->Branch("GE11_phi_L2", event_.GE11_phi_L2,"GE11_phi_L2[50]/F");
  event_tree_->Branch("GE21_phi_L1", event_.GE21_phi_L1,"GE21_phi_L1[50]/F");
  event_tree_->Branch("GE21_phi_L2", event_.GE21_phi_L2,"GE21_phi_L2[50]/F");
  event_tree_->Branch("GE21_pad2_phi_L1", event_.GE21_pad2_phi_L1,"GE21_pad2_phi_L1[50]/F");
  event_tree_->Branch("GE21_pad2_phi_L2", event_.GE21_pad2_phi_L2,"GE21_pad2_phi_L2[50]/F");
  event_tree_->Branch("GE11_bx_L1", event_.GE11_bx_L1,"GE11_bx_L1[50]/I");
  event_tree_->Branch("GE11_bx_L2", event_.GE11_bx_L2,"GE11_bx_L2[50]/I");
  event_tree_->Branch("GE21_bx_L1", event_.GE21_bx_L1,"GE21_bx_L1[50]/I");
  event_tree_->Branch("GE21_bx_L2", event_.GE21_bx_L2,"GE21_bx_L2[50]/I");
  event_tree_->Branch("GE11_ch_L1", event_.GE11_ch_L1,"GE11_ch_L1[50]/I");
  event_tree_->Branch("GE11_ch_L2", event_.GE11_ch_L2,"GE11_ch_L2[50]/I");
  event_tree_->Branch("GE21_ch_L1", event_.GE21_ch_L1,"GE21_ch_L1[50]/I");
  event_tree_->Branch("GE21_ch_L2", event_.GE21_ch_L2,"GE21_ch_L2[50]/I");
  event_tree_->Branch("GE11_z_L1", event_.GE11_z_L1,"GE11_z_L1[50]/F");
  event_tree_->Branch("GE11_z_L2", event_.GE11_z_L2,"GE11_z_L2[50]/F");
  event_tree_->Branch("GE21_z_L1", event_.GE21_z_L1,"GE21_z_L1[50]/F");
  event_tree_->Branch("GE21_z_L2", event_.GE21_z_L2,"GE21_z_L2[50]/F");

  event_tree_->Branch("GE11_sim_phi_L1", event_.GE11_sim_phi_L1,"GE11_sim_phi_L1[50]/F");
  event_tree_->Branch("GE11_sim_phi_L2", event_.GE11_sim_phi_L2,"GE11_sim_phi_L2[50]/F");
  event_tree_->Branch("GE21_sim_phi_L1", event_.GE21_sim_phi_L1,"GE21_sim_phi_L1[50]/F");
  event_tree_->Branch("GE21_sim_phi_L2", event_.GE21_sim_phi_L2,"GE21_sim_phi_L2[50]/F");
  event_tree_->Branch("GE11_sim_bx_L1", event_.GE11_sim_bx_L1,"GE11_sim_bx_L1[50]/F");
  event_tree_->Branch("GE11_sim_bx_L2", event_.GE11_sim_bx_L2,"GE11_sim_bx_L2[50]/F");
  event_tree_->Branch("GE21_sim_bx_L1", event_.GE21_sim_bx_L1,"GE21_sim_bx_L1[50]/F");
  event_tree_->Branch("GE21_sim_bx_L2", event_.GE21_sim_bx_L2,"GE21_sim_bx_L2[50]/F");
  event_tree_->Branch("GE11_sim_ch_L1", event_.GE11_sim_ch_L1,"GE11_sim_ch_L1[50]/I");
  event_tree_->Branch("GE11_sim_ch_L2", event_.GE11_sim_ch_L2,"GE11_sim_ch_L2[50]/I");
  event_tree_->Branch("GE21_sim_ch_L1", event_.GE21_sim_ch_L1,"GE21_sim_ch_L1[50]/I");
  event_tree_->Branch("GE21_sim_ch_L2", event_.GE21_sim_ch_L2,"GE21_sim_ch_L2[50]/I");
  event_tree_->Branch("GE11_sim_z_L1", event_.GE11_sim_z_L1,"GE11_sim_z_L1[50]/F");
  event_tree_->Branch("GE11_sim_z_L2", event_.GE11_sim_z_L2,"GE11_sim_z_L2[50]/F");
  event_tree_->Branch("GE21_sim_z_L1", event_.GE21_sim_z_L1,"GE21_sim_z_L1[50]/F");
  event_tree_->Branch("GE21_sim_z_L2", event_.GE21_sim_z_L2,"GE21_sim_z_L2[50]/F");

  event_tree_->Branch("GE11_sim_pad_phi_L1", event_.GE11_sim_pad_phi_L1,"GE11_sim_pad_phi_L1[50]/F");
  event_tree_->Branch("GE11_sim_pad_phi_L2", event_.GE11_sim_pad_phi_L2,"GE11_sim_pad_phi_L2[50]/F");
  event_tree_->Branch("GE21_sim_pad_phi_L1", event_.GE21_sim_pad_phi_L1,"GE21_sim_pad_phi_L1[50]/F");
  event_tree_->Branch("GE21_sim_pad_phi_L2", event_.GE21_sim_pad_phi_L2,"GE21_sim_pad_phi_L2[50]/F");
  event_tree_->Branch("GE11_sim_pad_bx_L1", event_.GE11_sim_pad_bx_L1,"GE11_sim_pad_bx_L1[50]/F");
  event_tree_->Branch("GE11_sim_pad_bx_L2", event_.GE11_sim_pad_bx_L2,"GE11_sim_pad_bx_L2[50]/F");
  event_tree_->Branch("GE21_sim_pad_bx_L1", event_.GE21_sim_pad_bx_L1,"GE21_sim_pad_bx_L1[50]/F");
  event_tree_->Branch("GE21_sim_pad_bx_L2", event_.GE21_sim_pad_bx_L2,"GE21_sim_pad_bx_L2[50]/F");
  event_tree_->Branch("GE11_sim_pad_ch_L1", event_.GE11_sim_pad_ch_L1,"GE11_sim_pad_ch_L1[50]/I");
  event_tree_->Branch("GE11_sim_pad_ch_L2", event_.GE11_sim_pad_ch_L2,"GE11_sim_pad_ch_L2[50]/I");
  event_tree_->Branch("GE21_sim_pad_ch_L1", event_.GE21_sim_pad_ch_L1,"GE21_sim_pad_ch_L1[50]/I");
  event_tree_->Branch("GE21_sim_pad_ch_L2", event_.GE21_sim_pad_ch_L2,"GE21_sim_pad_ch_L2[50]/I");
  event_tree_->Branch("GE11_sim_pad_z_L1", event_.GE11_sim_pad_z_L1,"GE11_sim_pad_z_L1[50]/F");
  event_tree_->Branch("GE11_sim_pad_z_L2", event_.GE11_sim_pad_z_L2,"GE11_sim_pad_z_L2[50]/F");
  event_tree_->Branch("GE21_sim_pad_z_L1", event_.GE21_sim_pad_z_L1,"GE21_sim_pad_z_L1[50]/F");
  event_tree_->Branch("GE21_sim_pad_z_L2", event_.GE21_sim_pad_z_L2,"GE21_sim_pad_z_L2[50]/F");

  event_tree_->Branch("GE21_sim_pad1_phi_L1", event_.GE21_sim_pad1_phi_L1,"GE21_sim_pad1_phi_L1[50]/F");
  event_tree_->Branch("GE21_sim_pad1_phi_L2", event_.GE21_sim_pad1_phi_L2,"GE21_sim_pad1_phi_L2[50]/F");
  event_tree_->Branch("GE21_sim_pad2_phi_L1", event_.GE21_sim_pad2_phi_L1,"GE21_sim_pad2_phi_L1[50]/F");
  event_tree_->Branch("GE21_sim_pad2_phi_L2", event_.GE21_sim_pad2_phi_L2,"GE21_sim_pad2_phi_L2[50]/F");
  event_tree_->Branch("GE21_sim_pad4_phi_L1", event_.GE21_sim_pad4_phi_L1,"GE21_sim_pad4_phi_L1[50]/F");
  event_tree_->Branch("GE21_sim_pad4_phi_L2", event_.GE21_sim_pad4_phi_L2,"GE21_sim_pad4_phi_L2[50]/F");
  event_tree_->Branch("GE21_sim_pad8_phi_L1", event_.GE21_sim_pad8_phi_L1,"GE21_sim_pad8_phi_L1[50]/F");
  event_tree_->Branch("GE21_sim_pad8_phi_L2", event_.GE21_sim_pad8_phi_L2,"GE21_sim_pad8_phi_L2[50]/F");
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
      event_.genGdMu_q[i][j] = -99;
      event_.genGdMu_p[i][j] = -99;
      event_.genGdMu_pt[i][j] = -99;
      event_.genGdMu_px[i][j] = -99;
      event_.genGdMu_py[i][j] = -99;
      event_.genGdMu_pz[i][j] = -99;
      event_.genGdMu_eta[i][j] = -99;
      event_.genGdMu_phi[i][j] = -99;

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
      event_.genGdMu_SIM_index[i][j] = -99;
      event_.genGdMu_SIM_dR[i][j] = 99.;

      event_.genGdMu_etav_prop_GE11[i][j] = -99;
      event_.genGdMu_phiv_prop_GE11[i][j] = -99;
      event_.genGdMu_etav_prop_GE21[i][j] = -99;
      event_.genGdMu_phiv_prop_GE21[i][j] = -99;

      event_.genGdMu_vx[i][j] = -99;
      event_.genGdMu_vy[i][j] = -99;
      event_.genGdMu_vz[i][j] = -99;
      event_.genGdMu_dxy[i][j] = -99;
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
    event_.L1Mu_RPCb_index[i] = -1;
    event_.L1Mu_RPCf_index[i] = -1;
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

  for (int i=0; i<50; ++i){
    event_.pt_sim[i] = -99;
    event_.eta_sim[i] = -99;
    event_.phi_sim[i] = -99;
    event_.charge_sim[i] = -99;
  }
  event_.has_sim = -99;
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
    event_.DTTF_nStubs[i] = 0;

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
    event_.CSCTF_nStubs[i] = 0;

    event_.CSCTF_st1[i] = 99; 
    event_.CSCTF_ri1[i] = 99; 
    event_.CSCTF_ch1[i] = 99; 
    event_.CSCTF_en1[i] = 99;
    event_.CSCTF_trk1[i] = 99; 
    event_.CSCTF_quality1[i] = 99; 
    event_.CSCTF_wg1[i] = 99; 
    event_.CSCTF_hs1[i] = 99; 
    event_.CSCTF_pat1[i] = 99; 
    event_.CSCTF_bend1[i] = 99; 
    event_.CSCTF_bx1[i] = 99; 
    event_.CSCTF_clctpat1[i] = 99;
    event_.CSCTF_val1[i] = 99;
    event_.CSCTF_phi1[i] = 99;
    event_.CSCTF_phib1[i] = 99;

    event_.CSCTF_st2[i] = 99; 
    event_.CSCTF_ri2[i] = 99; 
    event_.CSCTF_ch2[i] = 99; 
    event_.CSCTF_en2[i] = 99;
    event_.CSCTF_trk2[i] = 99; 
    event_.CSCTF_quality2[i] = 99; 
    event_.CSCTF_wg2[i] = 99; 
    event_.CSCTF_hs2[i] = 99; 
    event_.CSCTF_pat2[i] = 99; 
    event_.CSCTF_bend2[i] = 99; 
    event_.CSCTF_bx2[i] = 99; 
    event_.CSCTF_clctpat2[i] = 99;
    event_.CSCTF_val2[i] = 99;
    event_.CSCTF_phi2[i] = 99;
    event_.CSCTF_phib2[i] = 99;

    event_.CSCTF_st3[i] = 99; 
    event_.CSCTF_ri3[i] = 99; 
    event_.CSCTF_ch3[i] = 99; 
    event_.CSCTF_en3[i] = 99;
    event_.CSCTF_trk3[i] = 99; 
    event_.CSCTF_quality3[i] = 99; 
    event_.CSCTF_wg3[i] = 99; 
    event_.CSCTF_hs3[i] = 99; 
    event_.CSCTF_pat3[i] = 99; 
    event_.CSCTF_bend3[i] = 99; 
    event_.CSCTF_bx3[i] = 99; 
    event_.CSCTF_clctpat3[i] = 99;
    event_.CSCTF_val3[i] = 99;
    event_.CSCTF_phi3[i] = 99;
    event_.CSCTF_phib3[i] = 99;

    event_.CSCTF_st4[i] = 99; 
    event_.CSCTF_ri4[i] = 99; 
    event_.CSCTF_ch4[i] = 99; 
    event_.CSCTF_en4[i] = 99;
    event_.CSCTF_trk4[i] = 99; 
    event_.CSCTF_quality4[i] = 99; 
    event_.CSCTF_wg4[i] = 99; 
    event_.CSCTF_hs4[i] = 99; 
    event_.CSCTF_pat4[i] = 99; 
    event_.CSCTF_bend4[i] = 99; 
    event_.CSCTF_bx4[i] = 99; 
    event_.CSCTF_clctpat4[i] = 99;
    event_.CSCTF_val4[i] = 99;
    event_.CSCTF_phi4[i] = 99;
    event_.CSCTF_phib4[i] = 99;

    event_.CSCTF_eta1[i] = 99;
    event_.CSCTF_eta2[i] = 99;
    event_.CSCTF_eta3[i] = 99;
    event_.CSCTF_eta4[i] = 99;

    event_.CSCTF_gemdphi1[i] = 99;
    event_.CSCTF_gemdphi2[i] = 99;

    event_.CSCTF_R1[i] = 99;
    event_.CSCTF_x1[i] = 99;
    event_.CSCTF_y1[i] = 99;
    event_.CSCTF_z1[i] = 99;
    event_.CSCTF_R2[i] = 99;
    event_.CSCTF_x2[i] = 99;
    event_.CSCTF_y2[i] = 99;
    event_.CSCTF_z2[i] = 99;
    event_.CSCTF_R3[i] = 99;
    event_.CSCTF_x3[i] = 99;
    event_.CSCTF_y3[i] = 99;
    event_.CSCTF_z3[i] = 99;
    event_.CSCTF_R4[i] = 99;
    event_.CSCTF_x4[i] = 99;
    event_.CSCTF_y4[i] = 99;
    event_.CSCTF_z4[i] = 99;

    event_.CSCTF_fit_R1[i] = 99;
    event_.CSCTF_fit_x1[i] = 99;
    event_.CSCTF_fit_y1[i] = 99;
    event_.CSCTF_fit_z1[i] = 99;
    event_.CSCTF_fit_R2[i] = 99;
    event_.CSCTF_fit_x2[i] = 99;
    event_.CSCTF_fit_y2[i] = 99;
    event_.CSCTF_fit_z2[i] = 99;
    event_.CSCTF_fit_R3[i] = 99;
    event_.CSCTF_fit_x3[i] = 99;
    event_.CSCTF_fit_y3[i] = 99;
    event_.CSCTF_fit_z3[i] = 99;
    event_.CSCTF_fit_R4[i] = 99;
    event_.CSCTF_fit_x4[i] = 99;
    event_.CSCTF_fit_y4[i] = 99;
    event_.CSCTF_fit_z4[i] = 99;


    event_.CSCTF_fit_phi1[i] = 99;
    event_.CSCTF_fit_phi2[i] = 99;
    event_.CSCTF_fit_phi3[i] = 99;
    event_.CSCTF_fit_phi4[i] = 99;

    event_.CSCTF_fit_dphi1[i] = 99;
    event_.CSCTF_fit_dphi2[i] = 99;
    event_.CSCTF_fit_dphi3[i] = 99;
    event_.CSCTF_fit_dphi4[i] = 99;

  }

  event_.nRPCb = 0;

  for (int i=0; i<kMaxRPCb; ++i){
    event_.RPCb_pt[i] = 99;
    event_.RPCb_eta[i] = 99;
    event_.RPCb_phi[i] = 99;
    event_.RPCb_bx[i] = 99;
    event_.RPCb_nStubs[i] = 0;
    event_.RPCb_quality[i] = 99;
    
    event_.RPCb_bx1[i] = 99;
    event_.RPCb_strip1[i] = 99;
    event_.RPCb_phi1[i] = 99;
    event_.RPCb_re1[i] = 99;
    event_.RPCb_ri1[i] = 99;
    event_.RPCb_st1[i] = 99;
    event_.RPCb_se1[i] = 99;
    event_.RPCb_la1[i] = 99;
    event_.RPCb_su1[i] = 99;
    event_.RPCb_ro1[i] = 99;

    event_.RPCb_bx2[i] = 99;
    event_.RPCb_strip2[i] = 99;
    event_.RPCb_phi2[i] = 99;
    event_.RPCb_re2[i] = 99;
    event_.RPCb_ri2[i] = 99;
    event_.RPCb_st2[i] = 99;
    event_.RPCb_se2[i] = 99;
    event_.RPCb_la2[i] = 99;
    event_.RPCb_su2[i] = 99;
    event_.RPCb_ro2[i] = 99;

    event_.RPCb_bx3[i] = 99;
    event_.RPCb_strip3[i] = 99;
    event_.RPCb_phi3[i] = 99;
    event_.RPCb_re3[i] = 99;
    event_.RPCb_ri3[i] = 99;
    event_.RPCb_st3[i] = 99;
    event_.RPCb_se3[i] = 99;
    event_.RPCb_la3[i] = 99;
    event_.RPCb_su3[i] = 99;
    event_.RPCb_ro3[i] = 99;

    event_.RPCb_bx4[i] = 99;
    event_.RPCb_strip4[i] = 99;
    event_.RPCb_phi4[i] = 99;
    event_.RPCb_re4[i] = 99;
    event_.RPCb_ri4[i] = 99;
    event_.RPCb_st4[i] = 99;
    event_.RPCb_se4[i] = 99;
    event_.RPCb_la4[i] = 99;
    event_.RPCb_su4[i] = 99;
    event_.RPCb_ro4[i] = 99;

    event_.RPCb_bx5[i] = 99;
    event_.RPCb_strip5[i] = 99;
    event_.RPCb_phi5[i] = 99;
    event_.RPCb_re5[i] = 99;
    event_.RPCb_ri5[i] = 99;
    event_.RPCb_st5[i] = 99;
    event_.RPCb_se5[i] = 99;
    event_.RPCb_la5[i] = 99;
    event_.RPCb_su5[i] = 99;
    event_.RPCb_ro5[i] = 99;

    event_.RPCb_bx6[i] = 99;
    event_.RPCb_strip6[i] = 99;
    event_.RPCb_phi6[i] = 99;
    event_.RPCb_re6[i] = 99;
    event_.RPCb_ri6[i] = 99;
    event_.RPCb_st6[i] = 99;
    event_.RPCb_se6[i] = 99;
    event_.RPCb_la6[i] = 99;
    event_.RPCb_su6[i] = 99;
    event_.RPCb_ro6[i] = 99;
  }

  event_.nRPCf = 0;

  for (int i=0; i<kMaxRPCf; ++i){
    event_.RPCf_pt[i] = 99;
    event_.RPCf_eta[i] = 99;
    event_.RPCf_phi[i] = 99;
    event_.RPCf_bx[i] = 99;
    event_.RPCf_nStubs[i] = 0;
    event_.RPCf_quality[i] = 99;
    
    event_.RPCf_bx1[i] = 99;
    event_.RPCf_strip1[i] = 99;
    event_.RPCf_phi1[i] = 99;
    event_.RPCf_re1[i] = 99;
    event_.RPCf_ri1[i] = 99;
    event_.RPCf_st1[i] = 99;
    event_.RPCf_se1[i] = 99;
    event_.RPCf_la1[i] = 99;
    event_.RPCf_su1[i] = 99;
    event_.RPCf_ro1[i] = 99;

    event_.RPCf_bx2[i] = 99;
    event_.RPCf_strip2[i] = 99;
    event_.RPCf_phi2[i] = 99;
    event_.RPCf_re2[i] = 99;
    event_.RPCf_ri2[i] = 99;
    event_.RPCf_st2[i] = 99;
    event_.RPCf_se2[i] = 99;
    event_.RPCf_la2[i] = 99;
    event_.RPCf_su2[i] = 99;
    event_.RPCf_ro2[i] = 99;

    event_.RPCf_bx3[i] = 99;
    event_.RPCf_strip3[i] = 99;
    event_.RPCf_phi3[i] = 99;
    event_.RPCf_re3[i] = 99;
    event_.RPCf_ri3[i] = 99;
    event_.RPCf_st3[i] = 99;
    event_.RPCf_se3[i] = 99;
    event_.RPCf_la3[i] = 99;
    event_.RPCf_su3[i] = 99;
    event_.RPCf_ro3[i] = 99;

    event_.RPCf_bx4[i] = 99;
    event_.RPCf_strip4[i] = 99;
    event_.RPCf_phi4[i] = 99;
    event_.RPCf_re4[i] = 99;
    event_.RPCf_ri4[i] = 99;
    event_.RPCf_st4[i] = 99;
    event_.RPCf_se4[i] = 99;
    event_.RPCf_la4[i] = 99;
    event_.RPCf_su4[i] = 99;
    event_.RPCf_ro4[i] = 99;

    event_.RPCf_bx5[i] = 99;
    event_.RPCf_strip5[i] = 99;
    event_.RPCf_phi5[i] = 99;
    event_.RPCf_re5[i] = 99;
    event_.RPCf_ri5[i] = 99;
    event_.RPCf_st5[i] = 99;
    event_.RPCf_se5[i] = 99;
    event_.RPCf_la5[i] = 99;
    event_.RPCf_su5[i] = 99;
    event_.RPCf_ro5[i] = 99;

    event_.RPCf_bx6[i] = 99;
    event_.RPCf_strip6[i] = 99;
    event_.RPCf_phi6[i] = 99;
    event_.RPCf_re6[i] = 99;
    event_.RPCf_ri6[i] = 99;
    event_.RPCf_st6[i] = 99;
    event_.RPCf_se6[i] = 99;
    event_.RPCf_la6[i] = 99;
    event_.RPCf_su6[i] = 99;
    event_.RPCf_ro6[i] = 99;
  }


  event_.nGEM = 4;
  for (int i=0; i<kMaxSIM; ++i){
    event_.GE11_phi_L1[i] = 99.;
    event_.GE11_phi_L2[i] = 99.;
    event_.GE21_phi_L1[i] = 99.;
    event_.GE21_phi_L2[i] = 99.;
    event_.GE21_pad2_phi_L1[i] = 99.;
    event_.GE21_pad2_phi_L2[i] = 99.;
    event_.GE11_bx_L1[i] = 99;
    event_.GE11_bx_L2[i] = 99;
    event_.GE21_bx_L1[i] = 99;
    event_.GE21_bx_L2[i] = 99;
    event_.GE11_ch_L1[i] = 99;
    event_.GE11_ch_L2[i] = 99;
    event_.GE21_ch_L1[i] = 99;
    event_.GE21_ch_L2[i] = 99;
    event_.GE11_z_L1[i] = 99;
    event_.GE11_z_L2[i] = 99;
    event_.GE21_z_L1[i] = 99;
    event_.GE21_z_L2[i] = 99;

    event_.GE21_sim_pad1_phi_L1[i] = 99.; 
    event_.GE21_sim_pad1_phi_L2[i] = 99.;
    event_.GE21_sim_pad2_phi_L1[i] = 99.; 
    event_.GE21_sim_pad2_phi_L2[i] = 99.;
    event_.GE21_sim_pad4_phi_L1[i] = 99.; 
    event_.GE21_sim_pad4_phi_L2[i] = 99.;
    event_.GE21_sim_pad8_phi_L1[i] = 99.; 
    event_.GE21_sim_pad8_phi_L2[i] = 99.;
    
    event_.GE11_sim_phi_L1[i] = 99.;
    event_.GE11_sim_phi_L2[i] = 99.;
    event_.GE21_sim_phi_L1[i] = 99.;
    event_.GE21_sim_phi_L2[i] = 99.;
    event_.GE11_sim_bx_L1[i] = 99;
    event_.GE11_sim_bx_L2[i] = 99;
    event_.GE21_sim_bx_L1[i] = 99;
    event_.GE21_sim_bx_L2[i] = 99;
    event_.GE11_sim_ch_L1[i] = 99;
    event_.GE11_sim_ch_L2[i] = 99;
    event_.GE21_sim_ch_L1[i] = 99;
    event_.GE21_sim_ch_L2[i] = 99;
    event_.GE11_sim_z_L1[i] = 99;
    event_.GE11_sim_z_L2[i] = 99;
    event_.GE21_sim_z_L1[i] = 99;
    event_.GE21_sim_z_L2[i] = 99;
    
    event_.GE11_sim_pad_phi_L1[i] = 99.;
    event_.GE11_sim_pad_phi_L2[i] = 99.;
    event_.GE21_sim_pad_phi_L1[i] = 99.;
    event_.GE21_sim_pad_phi_L2[i] = 99.;
    event_.GE11_sim_pad_bx_L1[i] = 99;
    event_.GE11_sim_pad_bx_L2[i] = 99;
    event_.GE21_sim_pad_bx_L1[i] = 99;
    event_.GE21_sim_pad_bx_L2[i] = 99;
    event_.GE11_sim_pad_ch_L1[i] = 99;
    event_.GE11_sim_pad_ch_L2[i] = 99;
    event_.GE21_sim_pad_ch_L1[i] = 99;
    event_.GE21_sim_pad_ch_L2[i] = 99;
    event_.GE11_sim_pad_z_L1[i] = 99;
    event_.GE11_sim_pad_z_L2[i] = 99;
    event_.GE21_sim_pad_z_L1[i] = 99;
    event_.GE21_sim_pad_z_L2[i] = 99;

    event_.CSCTF_rec_ch1[i] = 99;
    event_.CSCTF_rec_phi1[i] = 99;
    event_.CSCTF_rec_phib1[i] = 99;
    event_.CSCTF_rec_R1[i] = 99;
    event_.CSCTF_rec_z1[i] = 99;
    event_.CSCTF_rec_ch2[i] = 99;
    event_.CSCTF_rec_phi2[i] = 99;
    event_.CSCTF_rec_phib2[i] = 99;
    event_.CSCTF_rec_R2[i] = 99;
    event_.CSCTF_rec_z2[i] = 99;
    event_.CSCTF_rec_ch3[i] = 99;
    event_.CSCTF_rec_phi3[i] = 99;
    event_.CSCTF_rec_phib3[i] = 99;
    event_.CSCTF_rec_R3[i] = 99;
    event_.CSCTF_rec_z3[i] = 99;
    event_.CSCTF_rec_ch4[i] = 99;
    event_.CSCTF_rec_phi4[i] = 99;
    event_.CSCTF_rec_phib4[i] = 99;
    event_.CSCTF_rec_R4[i] = 99;
    event_.CSCTF_rec_z4[i] = 99;

    event_.CSCTF_rec_eta1[i] = 99;
    event_.CSCTF_rec_eta2[i] = 99;
    event_.CSCTF_rec_eta3[i] = 99;
    event_.CSCTF_rec_eta4[i] = 99;

    event_.CSCTF_fitline_x1[i] = 99;
    event_.CSCTF_fitline_x2[i] = 99;
    event_.CSCTF_fitline_x3[i] = 99;
    event_.CSCTF_fitline_x4[i] = 99;
    
    event_.CSCTF_fitline_y1[i] = 99;
    event_.CSCTF_fitline_y2[i] = 99;
    event_.CSCTF_fitline_y3[i] = 99;
    event_.CSCTF_fitline_y4[i] = 99;
    
    event_.CSCTF_sim_phi1[i] = 99;
    event_.CSCTF_sim_phi2[i] = 99;
    event_.CSCTF_sim_phi3[i] = 99;
    event_.CSCTF_sim_phi4[i] = 99;

    event_.CSCTF_sim_x1[i] = 99;
    event_.CSCTF_sim_x2[i] = 99;
    event_.CSCTF_sim_x3[i] = 99;
    event_.CSCTF_sim_x4[i] = 99;

    event_.CSCTF_sim_y1[i] = 99;
    event_.CSCTF_sim_y2[i] = 99;
    event_.CSCTF_sim_y3[i] = 99;
    event_.CSCTF_sim_y4[i] = 99;

    event_.CSCTF_sim_z1[i] = 99;
    event_.CSCTF_sim_z2[i] = 99;
    event_.CSCTF_sim_z3[i] = 99;
    event_.CSCTF_sim_z4[i] = 99;

    event_.CSCTF_sim_eta1[i] = 99;
    event_.CSCTF_sim_eta2[i] = 99;
    event_.CSCTF_sim_eta3[i] = 99;
    event_.CSCTF_sim_eta4[i] = 99;

    event_.CSCTF_sim_R1[i] = 99;
    event_.CSCTF_sim_R2[i] = 99;
    event_.CSCTF_sim_R3[i] = 99;
    event_.CSCTF_sim_R4[i] = 99;
  }
}

//define this as a plug-in
DEFINE_FWK_MODULE(DisplacedL1MuFilter);

//  LocalWords:  kMaxCSCTF
