import FWCore.ParameterSet.Config as cms

process = cms.Process("TriggerEff")

process.load("FWCore.MessageService.MessageLogger_cfi")

#process.load('Configuration.Geometry.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
#process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.Services_cff')
process.load('TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorOpposite_cfi')
process.load('TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorAlong_cfi')
process.load("MuJetAnalysis.HLTBendingAngle.DisplacedMuonTriggerAnalyzer_cfi")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
#process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
## global tag for upgrade studies
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'PH2_1K_FB_V6::All', '')

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100))

process.source = cms.Source("PoolSource",
   fileNames = cms.untracked.vstring(
       'file:outana.root'
   )
)

from GEMCode.GEMValidation.InputFileHelpers import *
Inputdir=['/eos/uscms/store/user/tahuang/SLHC23_patch1_2023Muon_gen_sim_Pt2_50_1M/SLHC25_patch1_2023Muon_1M_L1_PU0_Pt2_50_updategemeta/1bf93df4dfbb43dc918bd6e47dedbf79/']
process = useInputDir(process, Inputdir, True)


process.TFileService = cms.Service("TFileService",
    	fileName = cms.string("out_ana.root"),
	closeFileFast = cms.untracked.bool(True)
)

process.p = cms.Path(process.DisplacedMuonTriggerAnalyzer)



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
