import FWCore.ParameterSet.Config as cms

from GEMCode.GEMValidation.simTrackMatching_cfi import SimTrackMatching

DisplacedMuonTriggerRateGENSIM = cms.EDAnalyzer('DisplacedMuonTriggerRateGENSIM',
    verbose = cms.untracked.int32(0),
    simTrackMatching = SimTrackMatching
)
