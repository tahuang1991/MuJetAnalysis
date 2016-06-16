import FWCore.ParameterSet.Config as cms

process = cms.Process("HLTBending")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.load('Configuration.Geometry.GeometryExtended2023HGCalMuonReco_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.Services_cff')
process.load('TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorOpposite_cfi')
process.load('TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorAlong_cfi')
process.load("MuJetAnalysis.HLTBendingAngle.HLTBendingAngle_cfi")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'PH2_1K_FB_V6::All', '')

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10000))

"""
process.options = cms.untracked.PSet(
    SkipEvent = cms.untracked.vstring('ProductNotFound')
)
"""

process.source = cms.Source("PoolSource",
   fileNames = cms.untracked.vstring(
        'file:/eos/uscms/store/user/lpcgem/SingleMuPt2to50/SingleMuPt2to50_HLT_fullScope/151025_163726/0000/out_hlt_fullScope_1.root'
   )
)


from MuJetAnalysis.HLTBendingAngle.hltSamples744 import *
from MuJetAnalysis.HLTBendingAngle.hltSamples62XSLHCTP import *
from MuJetAnalysis.HLTBendingAngle.InputFileHelpers import *

label = "DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_HLT_fullScope_v3"
"""
label = "DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_HLT_fullScopeAging_v3"
label = "DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_HLT_descope235MCHF_v3"
label = "DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_HLT_descope235MCHFaging_v3"
label = "DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_HLT_descope200MCHF_v3"
label = "DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_HLT_descope200MCHFaging_v3"

label = "DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU200_HLT_fullScope_v3"
label = "DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU200_HLT_descope235MCHF_v3"
label = "DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU200_HLT_descope200MCHF_v3"
label = "DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU200_HLT_fullScopeAging_v3"
label = "DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU200_HLT_descope235MCHFaging_v3"
label = "DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU200_HLT_descope200MCHFaging_v3"

label = "DarkSUSY_mH_125_mGammaD_20000_cT_100_14TeV_PU140_HLT_fullScope"
label = "DarkSUSY_mH_125_mGammaD_20000_cT_100_14TeV_PU140_HLT_fullScopeAging"
label = "DarkSUSY_mH_125_mGammaD_20000_cT_100_14TeV_PU140_HLT_descope235MCHF"
label = "DarkSUSY_mH_125_mGammaD_20000_cT_100_14TeV_PU140_HLT_descope235MCHFaging"
label = "DarkSUSY_mH_125_mGammaD_20000_cT_100_14TeV_PU140_HLT_descope200MCHF"
label = "DarkSUSY_mH_125_mGammaD_20000_cT_100_14TeV_PU140_HLT_descope200MCHFaging"
"""

label = "DarkSUSY_mH_125_mGammaD_20000_cT_100_14TeV_PU140_HLT_fullScope"
dir = eosfiles[label]
dir = '/eos/uscms/store/user/lpcgem/SingleMuPt2to50/SingleMuPt2to50_HLT_fullScope/151025_163726/0000/'
process=useInputDir(process, dir, "out_hlt_")

process.TFileService = cms.Service("TFileService",
    fileName = cms.string("out_ana_prompt_hltL2MuonCandidates.root"),
    closeFileFast = cms.untracked.bool(True)
)

matching = process.HLTBendingAngle.simTrackMatching
print matching

## no aging
matching.rpcStripDigi.validInputTags = cms.VInputTag(cms.InputTag("simMuonRPCDigis"))
matching.rpcRecHit.validInputTags = cms.VInputTag(cms.InputTag("hltRpcRecHits"))
matching.cscRecHit.validInputTags = cms.VInputTag(cms.InputTag("hltCsc2DRecHits"))

## aging
"""
matching.rpcStripDigi.validInputTags = cms.VInputTag(cms.InputTag("hltMuonRPCDigis"))
matching.rpcRecHit.validInputTags = cms.VInputTag(cms.InputTag("hltRpcRecHits"))
matching.cscRecHit.validInputTags = cms.VInputTag(cms.InputTag("hltCsc2DRecHitsOverload"))
"""
process.p = cms.Path(process.HLTBendingAngle)


## messages
print
print 'Input files:'
print '----------------------------------------'
print process.source.fileNames
print
print 'Output file:'
print '----------------------------------------'
print process.TFileService.fileName
print
