#ifndef L2MuonCandidatePtFromSegmentAlignmentProducer_H
#define L2MuonCandidatePtFromSegmentAlignmentProducer_H

/**
   \class L2MuPtFromStubAlignment

   Description: calculation of the L2Mu pt from stub alignment
   
   Original Author:  "Sven Dildick", "Jose Dimas Valle"
*/

#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/RecoCandidate/interface/RecoChargedCandidate.h"
#include "DataFormats/RecoCandidate/interface/RecoChargedCandidateFwd.h"

#include "TTree.h"

namespace edm {
  class ParameterSet; 
  class Event; 
  class EventSetup;
}

class CSCGeometry;
class DTGeometry;

struct MyTrack
{  
  double dx_gp_ME1_ME2; 
  double dx_gp_ME2_ME3; 
  
  double dy_gp_ME1_ME2; 
  double dy_gp_ME2_ME3; 
  
  double dz_gp_ME1_ME2; 
  double dz_gp_ME2_ME3; 
    
  double dx_gp_MB1_MB2; 
  double dx_gp_MB2_MB3; 
  
  double dy_gp_MB1_MB2; 
  double dy_gp_MB2_MB3; 
  
  double dz_gp_MB1_MB2; 
  double dz_gp_MB2_MB3; 

  double phi_gp_MB1; 
  double phi_gp_MB2;
  double phi_gp_MB3;
  double phi_gp_MB4; 
  
  double phi_gv_MB1; 
  double phi_gv_MB2;
  double phi_gv_MB3;
  double phi_gv_MB4;
  
  double x_gp_MB1; 
  double x_gp_MB2;
  double x_gp_MB3;
  
  double y_gp_MB1; 
  double y_gp_MB2;
  double y_gp_MB3;
  
  double z_gp_MB1; 
  double z_gp_MB2;
  double z_gp_MB3;
    
  double phi_gp_ME1; 
  double phi_gp_ME2;
  double phi_gp_ME3;
  
  double phi_gv_ME1; 
  double phi_gv_ME2;
  double phi_gv_ME3;
  
  double x_gp_ME1; 
  double x_gp_ME2;
  double x_gp_ME3;
  
  double y_gp_ME1; 
  double y_gp_ME2;
  double y_gp_ME3;
  
  double z_gp_ME1; 
  double z_gp_ME2;
  double z_gp_ME3;

  double dphi_gp_MB1_MB2;
  double dphi_gp_MB1_MB4;
  double dphi_gp_MB2_MB3;

  double dphi_gp_ME1_ME2;
  double dphi_gp_ME2_ME3;

  double dY_gp_ME12_ME23;
  double dY_gp_MB12_MB23;
};

class L2MuonCandidatePtFromSegmentAlignmentProducer : public edm::EDProducer 
{
 public:
  /// constructor with config
  L2MuonCandidatePtFromSegmentAlignmentProducer(const edm::ParameterSet&);
  
  /// destructor
  virtual ~L2MuonCandidatePtFromSegmentAlignmentProducer(); 
  
  /// produce candidates
  virtual void beginRun(edm::Run &iRun, const edm::EventSetup &iSetup);  
  virtual void produce(edm::Event&, const edm::EventSetup&);
  float PtFromSegmentBending(float, float, float, float);
  float PtFromSegmentPosition(float, float, float, float);

 private:
  // L2 Collection Label
  edm::InputTag theL2CollectionLabel_; 
  edm::EDGetTokenT<reco::RecoChargedCandidateCollection> trackToken_;

  const CSCGeometry* csc_geometry_;
  const DTGeometry* dt_geometry_;
  
  edm::ESHandle<CSCGeometry> csc_geom;
  edm::ESHandle<DTGeometry> dt_geom;

  void bookTree();
  TTree* track_tree_;
  MyTrack my_track_;

  float pt_from_segment_alignment_;
};

#endif
