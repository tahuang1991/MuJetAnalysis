import FWCore.ParameterSet.Config as cms

process = cms.Process("PATIFY")

process.source = cms.Source("PoolSource",
  fileNames = cms.untracked.vstring(
    "file:/uscms_data/d3/dildick/work/DisplacedMuHLT/CMSSW_5_3_11_patch5/src/CrabJobs/out_reco.root"
  )
)

#from GEMCode.GEMValidation.InputFileHelpers import *
#process = useInputDir(process, ["/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_1500_ctauExp_5_8TeV_madgraph452_bridge224_LHE_pythia6_RAW/DarkSUSY_mH_125_mGammaD_1500_ctauExp_5_8TeV_madgraph452_bridge224_LHE_pythia6_RECO/d3ab0667c6cb6bf77e14d12c3b05fdd8/"])

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))

process.MessageLogger = cms.Service("MessageLogger",
  destinations = cms.untracked.vstring("cout"),
  cout = cms.untracked.PSet(threshold = cms.untracked.string("ERROR"))
)

process.load("Configuration/StandardSequences/FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:startup_GRun', '')

process.load("MuJetAnalysis.DataFormats.RECOtoPAT_cff")
process.patMuons.addGenMatch = cms.bool(True)
process.patMuons.embedGenMatch = cms.bool(True)
process.Path = cms.Path(process.patifyMC)

process.load("MuJetAnalysis.DataFormats.EventContent_version9_cff")
process.patOutput.fileName = cms.untracked.string("out_pat.root")
process.EndPath = cms.EndPath(process.patOutput)

process.schedule = cms.Schedule(process.Path, process.EndPath)
