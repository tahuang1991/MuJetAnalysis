#ifndef EDM_Analyzer_BaseMatcher_h
#define EDM_Analyzer_BaseMatcher_h


#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include <SimDataFormats/Track/interface/SimTrackContainer.h>
#include <SimDataFormats/Vertex/interface/SimVertexContainer.h>

#include "MagneticField/Engine/interface/MagneticField.h"
#include "TrackingTools/GeomPropagators/interface/Propagator.h"

#include "Geometry/Records/interface/MuonGeometryRecord.h"
#include "Geometry/GEMGeometry/interface/GEMGeometry.h"


#include "Geometry/DTGeometry/interface/DTGeometry.h"
#include "DataFormats/MuonDetId/interface/DTWireId.h"

inline bool is_dt(unsigned int detId) {
  return (DetId(detId)).subdetId() == MuonSubdetId::DT;
}



class BaseMatcher
{
public:

  enum DTType { DT_ALL = 0, DT_MB10, DT_MB11, DT_MB12, DT_MB20, DT_MB21, 
		DT_MB22, DT_MB30, DT_MB31, DT_MB32, DT_MB40, DT_MB41, DT_MB42};

  BaseMatcher(const SimTrack& t, const SimVertex& v,
      const edm::ParameterSet& ps, const edm::Event& ev, const edm::EventSetup& es);

  ~BaseMatcher();


  BaseMatcher(const BaseMatcher&) = delete;
  BaseMatcher& operator=(const BaseMatcher&) = delete;

  const SimTrack& trk() const {return trk_;}
  const SimVertex& vtx() const {return vtx_;}

  const edm::ParameterSet& conf() const {return conf_;}

  const edm::Event& event() const {return ev_;}
  const edm::EventSetup& eventSetup() const {return es_;}


  GlobalPoint propagateToZ(GlobalPoint &inner_point, GlobalVector &inner_vector, float z) const;
  GlobalPoint propagateToZ(float z) const;
  void setDTGeometry(const DTGeometry *geom) {dtGeometry_ = geom;}
  const DTGeometry* getDTGeometry() const {return dtGeometry_;}

 protected:
  
  const DTGeometry* dtGeometry_;

  bool hasDTGeometry_; 
  
 private:

  const SimTrack& trk_;
  const SimVertex& vtx_;

  const edm::ParameterSet& conf_;

  const edm::Event& ev_;
  const edm::EventSetup& es_;

  int verbose_;


  edm::ESHandle<MagneticField> magfield_;
  edm::ESHandle<Propagator> propagator_;
  edm::ESHandle<Propagator> propagatorOpposite_;
  edm::ESHandle<DTGeometry> dt_geom;
};

#endif
