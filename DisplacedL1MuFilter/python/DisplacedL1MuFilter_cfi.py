import FWCore.ParameterSet.Config as cms

DisplacedL1MuFilter_PhaseIIGE21 = cms.EDFilter("DisplacedL1MuFilter",
    L1MuQuality = cms.int32(4),
    dR_L1Mu_L1TkMu = cms.double(0.12),
    dR_L1Mu_noL1TkMu = cms.double(0.4),
    min_pT_L1TkMu = cms.double(4),
    max_pT_L1TkMu = cms.double(9999),
    verbose = cms.int32(0),
    L1Mu_input = cms.InputTag("simGmtDigis"),
    L1TkMu_input = cms.InputTag("L1TkMuonsMerge"),
)
