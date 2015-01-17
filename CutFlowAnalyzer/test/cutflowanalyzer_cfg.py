import FWCore.ParameterSet.Config as cms
import os

from TrackingTools.TransientTrack.TransientTrackBuilder_cfi import *

process = cms.Process("CutFlowAnalyzer")

#sample_name = os.environ["SAMPLE_NAME"]

# NMSSM Samples

#sample_name = "MSSM_mH_090_mA_2000_Hto2Ato4mu_8TeV-pythia6_537p4_PAT_v1"
#sample_name = "MSSM_mH_100_mA_2000_Hto2Ato4mu_8TeV-pythia6_537p4_PAT_v1"
#sample_name = "MSSM_mH_110_mA_2000_Hto2Ato4mu_8TeV-pythia6_537p4_PAT_v1"
#sample_name = "MSSM_mH_125_mA_0250_Hto2Ato4mu_8TeV-pythia6_537p4_PAT_v1"
#sample_name = "MSSM_mH_125_mA_0500_Hto2Ato4mu_8TeV-pythia6_537p4_PAT_v1"
#sample_name = "MSSM_mH_125_mA_0750_Hto2Ato4mu_8TeV-pythia6_537p4_PAT_v1"
#sample_name = "MSSM_mH_125_mA_1000_Hto2Ato4mu_8TeV-pythia6_537p4_PAT_v1"
#sample_name = "MSSM_mH_125_mA_2000_Hto2Ato4mu_8TeV-pythia6_537p4_PAT_v1"
#sample_name = "MSSM_mH_125_mA_3550_Hto2Ato4mu_8TeV-pythia6_537p4_PAT_v1"
#sample_name = "MSSM_mH_150_mA_2000_Hto2Ato4mu_8TeV-pythia6_537p4_PAT_v1"

# Dark SUSY Samples
#sample_name = "DarkSUSY_mH_090_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1"
#sample_name = "DarkSUSY_mH_100_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1"
#sample_name = "DarkSUSY_mH_110_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1"
#sample_name = "DarkSUSY_mH_125_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1"
#sample_name = "DarkSUSY_mH_150_Hto2n1to2nD2gammaD_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PATv1"

#sample_name = "DarkSUSY_mH_125_mGammaD_0250_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1"
#sample_name = "DarkSUSY_mH_125_mGammaD_0400_ctauExp_02_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1"
#sample_name = "DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1"
#sample_name = "DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1"
#sample_name = "DarkSUSY_mH_125_mGammaD_0550_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1"
#sample_name = "DarkSUSY_mH_125_mGammaD_0700_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1"
#sample_name = "DarkSUSY_mH_125_mGammaD_0850_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1"
#sample_name = "DarkSUSY_mH_125_mGammaD_1000_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1"

#sample_name = "DarkSUSY_mH_125_mGammaD_0250_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1"
#sample_name = "DarkSUSY_mH_125_mGammaD_0400_ctau_02_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1"
#sample_name = "DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1"
#sample_name = "DarkSUSY_mH_125_mGammaD_0400_ctau_2_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1"
#sample_name = "DarkSUSY_mH_125_mGammaD_0550_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1"
#sample_name = "DarkSUSY_mH_125_mGammaD_0700_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1"
#sample_name = "DarkSUSY_mH_125_mGammaD_0850_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1"
#sample_name = "DarkSUSY_mH_125_mGammaD_1000_ctau_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1"

# Backgrounds
#sample_name = "DoubleJPsiDPSto4mu_pTJPsi3GeV_8TeV-pythia8_537p4_PATv3"
#sample_name = "pp4mu_8TeV-calchep34cpc_LHE_pythia6_537p4_PAT_v2"

#print "Start analyze sample:", sample_name

#file_list = "MuJetAnalysis.FileLists." + sample_name + "_cff"
#process.load(file_list)

# Input source
process.source = cms.Source("PoolSource",
    secondaryFileNames = cms.untracked.vstring(),
    #fileNames = cms.untracked.vstring('file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctauExp_0_8TeV_madgraph452_bridge224_LHE_pythia6_RAW/DarkSUSY_mH_125_mGammaD_0400_ctauExp_0_8TeV_madgraph452_bridge224_LHE_pythia6_HLT/0a5876aaa3054a855e150da7afbee7a7/out_hlt_1_1_Vjv.root')
    fileNames = cms.untracked.vstring(
        'file:out_pat.root')
        #'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctauExp_0_8TeV_madgraph452_bridge224_LHE_pythia6_RAW/DarkSUSY_mH_125_mGammaD_0400_ctauExp_0_8TeV_madgraph452_bridge224_LHE_pythia6_RECO/d3ab0667c6cb6bf77e14d12c3b05fdd8/out_reco_1_1_r0Y.root')
)

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger = cms.Service("MessageLogger", destinations = cms.untracked.vstring("cout"), cout = cms.untracked.PSet(threshold = cms.untracked.string("ERROR")))

process.load("Configuration/StandardSequences/FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = "FT_53_V6_AN3::All"

process.load("MuJetAnalysis.MuJetProducer.MuJetProducer_cff")

process.TrackerMuJetProducer05 = process.MuJetProducer.clone(
  maxMass = cms.double(5.),
  muons = cms.InputTag("cleanPatTrackerMuonsTriggerMatch"),
  selectTrackerMuons = cms.bool(True),
  selectGlobalMuons = cms.bool(False),
  groupingMode = cms.string("GroupByMassAndVertexProbOrDeltaR"),
  maxDeltaR = cms.double(0.01),
  minSegmentMatches = cms.int32(2),
  minTrackerHits = cms.int32(8),
  maxTrackerNormChi2 = cms.double(4.0)
)

process.PFMuJetProducer05 = process.MuJetProducer.clone(
  maxMass = cms.double(5.),
  muons = cms.InputTag("cleanPatPFMuonsTriggerMatch"),
  selectTrackerMuons = cms.bool(False),
  selectGlobalMuons = cms.bool(False),
  groupingMode = cms.string("GroupByMassAndVertexProbOrDeltaR"),
  maxDeltaR = cms.double(0.01),
#  minSegmentMatches = cms.int32(2),
  minSegmentMatches = cms.int32(-1),
  minTrackerHits = cms.int32(-1),
  maxTrackerNormChi2 = cms.double(-1.0)
)

process.cutFlowAnalyzer = cms.EDAnalyzer('CutFlowAnalyzer',
  analyzerDebug = cms.int32(0),
  
  fillGenLevel = cms.bool(True),

#  muons = cms.InputTag("cleanPatTrackerMuonsTriggerMatch"),
#  muJets = cms.InputTag("TrackerMuJetProducer05"),
  
  muons = cms.InputTag("cleanPatPFMuonsTriggerMatch"),
  muJets = cms.InputTag("PFMuJetProducer05"),

  DiMuons_Iso_Max = cms.double(2.0),
  
  nThrowsConsistentVertexesCalculator = cms.int32(100000),

)

process.p = cms.Path(process.TrackerMuJetProducer05 *
                     process.PFMuJetProducer05 *
                     process.cutFlowAnalyzer)

output_file = "out_cutana.root"
process.TFileService = cms.Service("TFileService", fileName = cms.string(output_file))


