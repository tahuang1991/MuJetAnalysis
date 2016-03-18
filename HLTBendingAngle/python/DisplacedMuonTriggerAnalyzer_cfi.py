import FWCore.ParameterSet.Config as cms

from GEMCode.GEMValidation.simTrackMatching_cfi import SimTrackMatching

DisplacedMuonTriggerAnalyzer = cms.EDAnalyzer('DisplacedMuonTriggerAnalyzer',
    verbose = cms.untracked.int32(0),
    simTrackMatching = SimTrackMatching
)
