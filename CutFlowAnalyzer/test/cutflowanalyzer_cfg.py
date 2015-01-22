import FWCore.ParameterSet.Config as cms

process = cms.Process("CutFlowAnalyzer")

# Input source
process.source = cms.Source("PoolSource",
    secondaryFileNames = cms.untracked.vstring(),
    fileNames = cms.untracked.vstring(
        #'file:/eos/uscms/store/user/lpcgem/dildick/CMSSW_73/dildick/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_RAW/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_HLT_4/3f3291e696aa213db7125f5241d82f87/out_hlt_1_1_lpI.root'
        'file:out_pat.root'
        #'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctauExp_0_8TeV_madgraph452_bridge224_LHE_pythia6_RAW/DarkSUSY_mH_125_mGammaD_0400_ctauExp_0_8TeV_madgraph452_bridge224_LHE_pythia6_RECO/d3ab0667c6cb6bf77e14d12c3b05fdd8/out_reco_1_1_r0Y.root')
        #'file:/eos/uscms/store/user/lpcgem/dildick/CMSSW_73/dildick/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_RAW/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_PAT_4/85162c32c2e4f20b1b158ff80ab75376/out_pat_44_1_UUE.root'
    )
)

process.maxEvents = cms.untracked.PSet( 
    input = cms.untracked.int32(100) 
)

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger = cms.Service("MessageLogger", 
    destinations = cms.untracked.vstring("cout"), 
    cout = cms.untracked.PSet(threshold = cms.untracked.string("ERROR"))
)

process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = "MCRUN2_72_V3::All"

process.load("MuJetAnalysis.MuJetProducer.MuJetProducer_cff")
process.load("MuJetAnalysis.CutFlowAnalyzer.CutFlowAnalyzer_cfi")

process.p = cms.Path(
    process.TrackerMuJetProducer05 *
    process.PFMuJetProducer05 *
    process.cutFlowAnalyzer
)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string("out_ana.root")
)
