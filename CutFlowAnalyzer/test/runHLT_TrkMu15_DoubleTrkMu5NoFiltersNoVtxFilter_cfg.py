import FWCore.ParameterSet.Config as cms

process = cms.Process("HLT_TrkMu15_DoubleTrkMu5NoFiltersNoVtxFilter")

# Input source
process.source = cms.Source("PoolSource",
    secondaryFileNames = cms.untracked.vstring(),
    fileNames = cms.untracked.vstring("file:file.root")
)
process.maxEvents = cms.untracked.PSet( 
    input = cms.untracked.int32(-1) 
)

process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("MuJetAnalysis.CutFlowAnalyzer.HLT_TrkMu15_DoubleTrkMu5NoFiltersNoVtxFilter_cfi")

process.p = cms.Path(process.HLT_TrkMu15_DoubleTrkMu5NoFiltersNoVtxFilter)

# Tell the process what filename to use to save the output
process.Out = cms.OutputModule("PoolOutputModule",
         fileName = cms.untracked.string ("out_filter.root")
)

# make sure everything is hooked up
process.end = cms.EndPath(process.Out)
