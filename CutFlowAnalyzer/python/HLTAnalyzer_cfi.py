import FWCore.ParameterSet.Config as cms

from MuJetAnalysis.Configuration.Run2.hlt_Run2_QCDMuEnrichL1Mu_Rate_with_DisplacedMuHLT_CorrectedL1Prescale import process as pp
list = pp.paths.list
print list

HLTAnalyzer = cms.EDAnalyzer('HLTAnalyzer',
    analyzerDebug = cms.int32(0),
    fillGenLevel = cms.bool(True),
    hltPaths = cms.vstring(*list)
)
