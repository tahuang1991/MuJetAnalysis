#ifndef EDM_Analyzer_SimTrackMatchManager_h
#define EDM_Analyzer_SimTrackMatchManager_h


#include "MuJetAnalysis/EDM_Analyzer/src/BaseMatcher.h"
#include "MuJetAnalysis/EDM_Analyzer/src/SimHitMatcher.h"

class SimTrackMatchManager
{
public:
  
  SimTrackMatchManager(const SimTrack& t, const SimVertex& v,
      const edm::ParameterSet& ps, const edm::Event& ev, const edm::EventSetup& es);
  
  ~SimTrackMatchManager();

  const SimHitMatcher& simhits() const {return simhits_;}
  
private:

  SimHitMatcher simhits_;
};

#endif
