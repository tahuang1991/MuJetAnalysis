import FWCore.ParameterSet.Config as cms

cutFlowAnalyzer = cms.EDAnalyzer('CutFlowAnalyzer',
    analyzerDebug = cms.int32(0),
    fillGenLevel = cms.bool(True),
#    muons = cms.InputTag("cleanPatTrackerMuonsTriggerMatch"),
#    muJets = cms.InputTag("TrackerMuJetProducer05"),
    muons = cms.InputTag("cleanPatPFMuonsTriggerMatch"),
    muJets = cms.InputTag("PFMuJetProducer05"),
    DiMuons_Iso_Max = cms.double(2.0),
    nThrowsConsistentVertexesCalculator = cms.int32(100000),
    hltPaths = cms.vstring(
        'HLT_DoubleMu33NoFiltersNoVtx_v1',
        'HLT_Mu17_Mu8_DZ_v1',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v1',
        'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v1',
        'HLT_Mu30_TkMu11_v1',
        'HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v1',
        'HLT_TripleMu_12_10_5_v1',
        'HLT_TripleMu_12_10_5_onlyL1NewSeed_v1',
        'HLT_TrkMu15_DoubleTrkMu5_v1',
        'HLT_Mu17_Mu8_DZ_v1_NoDz',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v1_NoIso',
        'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v1_NoIso'
    )
)
