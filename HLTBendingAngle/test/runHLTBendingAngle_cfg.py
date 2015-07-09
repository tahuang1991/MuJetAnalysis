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
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'MCRUN2_74_V9', '')

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10000))

"""
process.options = cms.untracked.PSet(
    SkipEvent = cms.untracked.vstring('ProductNotFound')
)
"""

process.source = cms.Source("PoolSource",
   fileNames = cms.untracked.vstring(
        #'file:outputA.root'        
        #'file:outputA_25062015.root'
        #'file:outputA_30062015.root'
        'file:outputA_744_30062015.root'
   )
)


from MuJetAnalysis.HLTBendingAngle.hltSamples import *
from MuJetAnalysis.HLTBendingAngle.InputFileHelpers import *
label = "mGammaD_20000_ctau100_14TeV_HLT"
dir = eosfiles[label]
print eosfiles[label]
process=useInputDir(process, dir, pattern="outputA")

process.TFileService = cms.Service("TFileService",
    fileName = cms.string("out_ana.root"),
#    fileName = cms.string("out_ana_mGammaD_20000_ctau100_14TeV_HLT_07092015.root"),
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
