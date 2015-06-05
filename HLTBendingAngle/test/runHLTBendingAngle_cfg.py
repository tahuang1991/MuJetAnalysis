import FWCore.ParameterSet.Config as cms

process = cms.Process("HLTBending")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.Services_cff')
process.load('TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorOpposite_cfi')
process.load('TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorAlong_cfi')
process.load("MuJetAnalysis.HLTBendingAngle.HLTBendingAngle_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100))

process.source = cms.Source("PoolSource",
   fileNames = cms.untracked.vstring(
      'file:outputA.root'
 )
)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string("out_ana.root"),
	closeFileFast = cms.untracked.bool(True)
)

process.p = cms.Path(process.HLTBendingAngle)



## messages
print
#print 'Input files:'
print '----------------------------------------'
print process.source.fileNames
print
print 'Output file:'
print '----------------------------------------'
print process.TFileService.fileName
print
