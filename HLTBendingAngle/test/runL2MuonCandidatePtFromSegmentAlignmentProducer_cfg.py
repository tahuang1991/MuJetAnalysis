import FWCore.ParameterSet.Config as cms

process = cms.Process("L2MuonPtFromSegmentAlignment")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.load('Configuration.Geometry.GeometryExtended2023HGCalMuonReco_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.Services_cff')
process.load('TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorOpposite_cfi')
process.load('TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorAlong_cfi')
process.load('MuJetAnalysis.HLTBendingAngle.L2MuonCandidatePtFromSegmentAlignmentProducer_cfi')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'PH2_1K_FB_V6::All', '')

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10))

process.source = cms.Source("PoolSource",
   fileNames = cms.untracked.vstring(
        'file:out_hlt_fullScope.root'
   )
)

process.p = cms.Path(process.L2MuonCandidatePtFromSegmentAlignmentProducer)


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
