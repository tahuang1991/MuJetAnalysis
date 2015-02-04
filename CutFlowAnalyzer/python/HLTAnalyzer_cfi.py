import FWCore.ParameterSet.Config as cms

from MuJetAnalysis.Configuration.Run2.hlt_Run2_QCDMuEnrichL1Mu_Rate_With_HLT_TrkMu15_DoubleTrkMu5NoVtx_v1 import process as pp

print pp.paths.list
mylist = pp.paths.list

HLTAnalyzer = cms.EDAnalyzer('HLTAnalyzer',
    analyzerDebug = cms.int32(0),
    fillGenLevel = cms.bool(True),
    hltPaths = cms.vstring(*mylist
    )
)
