## import skeleton process
from PhysicsTools.PatAlgos.patTemplate_cfg import *

# verbose flags for the PF2PAT modules
process.options.allowUnscheduled = cms.untracked.bool(True)

### Add MuJet Dataformats
from MuJetAnalysis.DataFormats.EventContent_version9_cff import *
process = customizePatOutput(process)

process.load("MuJetAnalysis.DataFormats.RECOtoPAT_cff")
process.patMuons.addGenMatch = cms.bool(True)
process.patMuons.embedGenMatch = cms.bool(True)

## pick latest HLT process
process.patTrigger.processName = cms.string( "*" )
process.patTriggerEvent.processName = cms.string( "*" )

process.source = cms.Source("PoolSource",
  fileNames = cms.untracked.vstring(
        #"file:/eos/uscms/store/user/lpcgem/dildick/CMSSW_73/dildick/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_RAW/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_RECO/ee2b69195f87ad6497ae607e47718adf/out_reco_1_1_XNE.root"
#      "file:CrabJobs/out_reco.root"
        #"file:/eos/uscms/store/user/lpcgem/dildick/CMSSW_73/dildick/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_RAW/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_HLT_4/3f3291e696aa213db7125f5241d82f87/out_hlt_1_1_lpI.root"
        #'file:out_hlt.root'
        #"file:/eos/uscms/store/user/lpcgem/dildick/CMSSW_73/dildick/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_RAW/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_HLT_5/d0ea915ba74d1796f8439692a0e72586/out_hlt_1_1_Hif.root"
        #"file:/eos/uscms/store/user/lpcgem/dildick/CMSSW_73/dildick/DarkSUSY_mH_125_mGammaD_2000_ctauExp_5_8TeV_madgraph452_bridge224_LHE_pythia6_RAW/DarkSUSY_mH_125_mGammaD_2000_ctauExp_5_8TeV_madgraph452_bridge224_LHE_pythia6_HLT/d0ea915ba74d1796f8439692a0e72586/out_hlt_1_1_uuP.root"
        "file:/eos/uscms/store/user/lpcgem/dildick/CMSSW_73/dildick/DarkSUSY_mH_125_mGammaD_2000_ctauExp_5_8TeV_madgraph452_bridge224_LHE_pythia6_RAW/DarkSUSY_mH_125_mGammaD_2000_ctauExp_5_8TeV_madgraph452_bridge224_LHE_pythia6_RECO/ee2b69195f87ad6497ae607e47718adf/out_reco_1_1_9Sf.root"
  )
)

process.maxEvents.input = -1

process.load("MuJetAnalysis.MuJetProducer.MuJetProducer_cff")
process.load("MuJetAnalysis.CutFlowAnalyzer.CutFlowAnalyzer_cfi")

process.p = cms.Path(
    process.TrackerMuJetProducer05 *
    process.PFMuJetProducer05 *
    process.cutFlowAnalyzer
)

process.outpath = cms.EndPath(process.out)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string("out_ana.root")
)
