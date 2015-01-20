import FWCore.ParameterSet.Config as cms
import os

from TrackingTools.TransientTrack.TransientTrackBuilder_cfi import *

process = cms.Process("CutFlowAnalyzer")

# Input source
process.source = cms.Source("PoolSource",
    secondaryFileNames = cms.untracked.vstring(),
    #fileNames = cms.untracked.vstring('file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctauExp_0_8TeV_madgraph452_bridge224_LHE_pythia6_RAW/DarkSUSY_mH_125_mGammaD_0400_ctauExp_0_8TeV_madgraph452_bridge224_LHE_pythia6_HLT/0a5876aaa3054a855e150da7afbee7a7/out_hlt_1_1_Vjv.root')
    fileNames = cms.untracked.vstring(
        'file:out_pat.root')
        #'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctauExp_0_8TeV_madgraph452_bridge224_LHE_pythia6_RAW/DarkSUSY_mH_125_mGammaD_0400_ctauExp_0_8TeV_madgraph452_bridge224_LHE_pythia6_RECO/d3ab0667c6cb6bf77e14d12c3b05fdd8/out_reco_1_1_r0Y.root')
)

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1000) )

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger = cms.Service("MessageLogger", 
    destinations = cms.untracked.vstring("cout"), 
    cout = cms.untracked.PSet(threshold = cms.untracked.string("ERROR"))
)

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

process.anaHLT_Mu17_Mu8_DZ_v1 = cms.EDAnalyzer('CutFlowAnalyzer',
  analyzerDebug = cms.int32(0),
  fillGenLevel = cms.bool(True),
#  muons = cms.InputTag("cleanPatTrackerMuonsTriggerMatch"),
#  muJets = cms.InputTag("TrackerMuJetProducer05"),
  muons = cms.InputTag("cleanPatPFMuonsTriggerMatch"),
  muJets = cms.InputTag("PFMuJetProducer05"),
  DiMuons_Iso_Max = cms.double(2.0),
  nThrowsConsistentVertexesCalculator = cms.int32(100000),
  hltPath = cms.string('HLT_Mu17_Mu8_DZ_v1')
)

process.anaHLT_Mu30_TkMu11_v1 = process.anaHLT_Mu17_Mu8_DZ_v1.clone(
    hltPath = cms.string('HLT_Mu30_TkMu11_v1')
)

process.anaHLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v1 = process.anaHLT_Mu17_Mu8_DZ_v1.clone(
    hltPath = cms.string('HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v1')
)

process.anaHLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v1_NoIso = process.anaHLT_Mu17_Mu8_DZ_v1.clone(
    hltPath = cms.string('HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v1_NoIso')
)

process.anaHLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v1 = process.anaHLT_Mu17_Mu8_DZ_v1.clone(
    hltPath = cms.string('HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v1')
)

process.anaHLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v1_NoIso = process.anaHLT_Mu17_Mu8_DZ_v1.clone(
    hltPath = cms.string('HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v1_NoIso')
)

process.anaHLT_TripleMu_12_10_5_v1 = process.anaHLT_Mu17_Mu8_DZ_v1.clone(
    hltPath = cms.string('HLT_TripleMu_12_10_5_v1')
)

process.anaHLT_TrkMu15_DoubleTrkMu5_v1 = process.anaHLT_Mu17_Mu8_DZ_v1.clone(
    hltPath = cms.string('HLT_TrkMu15_DoubleTrkMu5_v1')
)

process.p = cms.Path(process.TrackerMuJetProducer05 *
                     process.PFMuJetProducer05 *
                     process.cutFlowAnalyzer)

output_file = "out_ana.root"
process.TFileService = cms.Service("TFileService", fileName = cms.string(output_file))


