import FWCore.ParameterSet.Config as cms

process = cms.Process("HLTAnalyzer")

# Input source
process.source = cms.Source("PoolSource",
    secondaryFileNames = cms.untracked.vstring(),
    fileNames = cms.untracked.vstring(
        'file:/eos/uscms/store/user/dildick/CMSSW_73/dildick/QCD_Pt-30to50_MuEnrichedPt5_PionKaonDecay_Tune4C_13TeV_pythia8/QCD_Pt-30to50_MuEnrichedPt5_PionKaonDecay_Tune4C_13TeV_pythia8_with_HLT_TrkMu15_DoubleTrkMu5NoVtx_v1/80b6d5516b4feee18c53d65d83163c63/outputA_265_1_uMP.root'
    )
)

process.maxEvents = cms.untracked.PSet( 
    input = cms.untracked.int32(-1) 
)

process.load("FWCore.MessageService.MessageLogger_cfi")
"""
process.MessageLogger = cms.Service("MessageLogger", 
    destinations = cms.untracked.vstring("cout"), 
    cout = cms.untracked.PSet(threshold = cms.untracked.string("ERROR"))
)
"""
process.load("MuJetAnalysis.CutFlowAnalyzer.HLTAnalyzer_cfi")

process.p = cms.Path(process.HLTAnalyzer)


process.TFileService = cms.Service("TFileService",
    fileName = cms.string("out_ana.root")
)
