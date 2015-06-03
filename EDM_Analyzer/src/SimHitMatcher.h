#ifndef EDM_Analyzer_SimHitMatcher_h
#define EDM_Analyzer_SimHitMatcher_h

#include "MuJetAnalysis/EDM_Analyzer/src/BaseMatcher.h"

#include "SimDataFormats/TrackingHit/interface/PSimHitContainer.h"
#include "DataFormats/GeometryVector/interface/GlobalPoint.h"

#include <vector>
#include <map>
#include <set>

class CSCGeometry;
class GEMGeometry;
class ME0Geometry;
class RPCGeometry;
class DTGeometry;

class SimHitMatcher : public BaseMatcher
{
public:

  SimHitMatcher(const SimTrack& t, const SimVertex& v,
      const edm::ParameterSet& ps, const edm::Event& ev, const edm::EventSetup& es);
  
  ~SimHitMatcher();
  const edm::PSimHitContainer& simHitsDT() const {return dt_hits_;}


  std::set<unsigned int> detIdsDT() const;

  std::set<unsigned int> superlayerIdsDT() const;
  std::set<unsigned int> chamberIdsDT() const;
  int nLayerWithHitsInChamberDT (unsigned int) const;
  int nLayerWithHitsInSuperlayerDT (unsigned int) const;
  const edm::PSimHitContainer& hitsInDetIdDT(unsigned int) const;
  const edm::PSimHitContainer& hitsInSuperlayerDT(unsigned int) const;
  const edm::PSimHitContainer& hitsInChamberDT(unsigned int) const;

  GlobalPoint simHitsMeanPosition(const edm::PSimHitContainer& sim_hits) const;

private:

  void init();

  std::vector<unsigned int> getIdsOfSimTrackShower(unsigned  trk_id,
      const edm::SimTrackContainer& simTracks, const edm::SimVertexContainer& simVertices);

  void matchSimHitsToSimTrack(std::vector<unsigned int> track_ids,
                              const edm::PSimHitContainer& dt_hits);


  bool simMuOnlyDT_;

  bool discardEleHitsDT_;

  bool runDTSimHit_;

  std::string simInputLabel_;

  std::map<unsigned int, unsigned int> trkid_to_index_;

  edm::PSimHitContainer no_hits_;
  edm::PSimHitContainer dt_hits_;
  std::map<unsigned int, edm::PSimHitContainer > dt_detid_to_hits_;
  std::map<unsigned int, edm::PSimHitContainer > dt_superlayer_to_hits_;
  std::map<unsigned int, edm::PSimHitContainer > dt_chamber_to_hits_;
  bool verboseDT_;
  edm::InputTag dtSimHitInput_;
  edm::Handle<edm::SimTrackContainer> sim_tracks;
  edm::Handle<edm::SimVertexContainer> sim_vertices;
};

#endif
