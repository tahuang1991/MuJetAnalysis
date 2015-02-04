import FWCore.ParameterSet.Config as cms

HLTAnalyzer = cms.EDAnalyzer('HLTAnalyzer',
    analyzerDebug = cms.int32(0),
    fillGenLevel = cms.bool(True),
    hltPaths = cms.vstring(
        'HLT_DoubleMu33NoFiltersNoVtx_v1',
        'HLT_Mu17_Mu8_DZ_v1',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v1',
        'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v1',
        'HLT_Mu30_TkMu11_v1',
        'HLT_TripleMu_12_10_5_v1',
        'HLT_TripleMu_12_10_5_onlyL1NewSeed_v1',
        'HLT_TrkMu15_DoubleTrkMu5_v1',
        'HLT_Mu15_DoubleMu5NoVtx_v1',
        'HLT_TrkMu15_DoubleTrkMu5NoFiltersNoVtx_v1',
        'HLT_Mu17_Mu8_DZ_v1_NoDz',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v1_NoIso',
        'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v1_NoIso',
    )
)

