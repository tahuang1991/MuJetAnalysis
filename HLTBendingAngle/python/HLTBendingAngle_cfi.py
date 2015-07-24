import FWCore.ParameterSet.Config as cms

from GEMCode.GEMValidation.simTrackMatching_cfi import SimTrackMatching
HLTBendingAngle = cms.EDAnalyzer('HLTBendingAngle',
    verbose = cms.untracked.int32(1),
    simTrackMatching = SimTrackMatching
)
