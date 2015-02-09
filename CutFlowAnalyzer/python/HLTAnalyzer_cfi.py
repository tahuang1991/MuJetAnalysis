import FWCore.ParameterSet.Config as cms

HLTAnalyzer = cms.EDAnalyzer('HLTAnalyzer',
    analyzerDebug = cms.int32(0),
    fillGenLevel = cms.bool(True),
)
