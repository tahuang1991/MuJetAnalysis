import FWCore.ParameterSet.Config as cms

process = cms.Process("HLTAnalyzer")

# Input source
process.source = cms.Source("PoolSource",
    secondaryFileNames = cms.untracked.vstring(),
        fileNames = cms.untracked.vstring(
#        'file:/eos/uscms/store/user/lpcgem/dildick/CMSSW_73/dildick/QCD_Pt-30to50_MuEnrichedPt5_PionKaonDecay_Tune4C_13TeV_pythia8/QCD_Pt-30to50_MuEnrichedPt5_PionKaonDecay_Tune4C_13TeV_pythia8_DisplacedMuHLT_fixedPreScale/56dfcc76a898de06d8aa21a996d4b8c7/out_hlt_total.root',
        "file:/uscms/home/dildick/nobackup/work/DisplacedMuHLT/CMSSW_7_3_1_patch2/src/out_hlt_QCDMuEnrich_DisplacedMuHLT_AddTrkCollections.root"
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
    fileName = cms.string("out_hltAna.root")
)
