import FWCore.ParameterSet.Config as cms

from MuJetAnalysis.Configuration.Run2.hlt_Run2_QCDMuEnrichL1Mu_Rate_with_DisplacedMuHLT_CorrectedL1Prescale import process as pp
list = pp.paths.list

cutFlowAnalyzer = cms.EDAnalyzer('CutFlowAnalyzer',
    analyzerDebug = cms.int32(0),
    fillGenLevel = cms.bool(True),
#    muons = cms.InputTag("cleanPatTrackerMuonsTriggerMatch"),
#    muJets = cms.InputTag("TrackerMuJetProducer05"),
    muons = cms.InputTag("cleanPatPFMuonsTriggerMatch"),
    muJets = cms.InputTag("PFMuJetProducer05"),
    DiMuons_Iso_Max = cms.double(2.0),
    nThrowsConsistentVertexesCalculator = cms.int32(100000),
    hltPaths = cms.vstring(*list)
)
