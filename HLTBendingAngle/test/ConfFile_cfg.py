import FWCore.ParameterSet.Config as cms

process = cms.Process("demo")

process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')

process.load('Configuration.StandardSequences.Services_cff')
process.load("FWCore.MessageService.MessageLogger_cfi")
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.Services_cff')
process.load("MuJetAnalysis.HLTBendingAngle.CfiFile_cfi")
process.load('TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorOpposite_cfi')
process.load('TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorAlong_cfi')

#from Geometry.CMSCommonData.cmsExtendedGeometry2023XML_cfi import *
#from Geometry.TrackerNumberingBuilder.trackerTopology2023Constants_cfi import *
#from Configuration.Geometry.GeometryExtended2023Muon_cff import *
process.load("Geometry.CMSCommonData.cmsExtendedGeometry2023XML_cfi")
process.load("Geometry.CMSCommonData.cmsIdealGeometryXML_cfi")
process.load("Geometry.DTGeometryBuilder.dtGeometry_cfi")




process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1)
)


#process.options = cms.untracked.PSet( SkipEvent = cms.untracked.vstring('ProductNotFound'))

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
   fileNames = cms.untracked.vstring(
      'file:outputA.root'
 )
)


process.TFileService = cms.Service("TFileService",
    fileName = cms.string("out_ana.root"),
	closeFileFast = cms.untracked.bool(True)
)





process.p = cms.Path(process.demo)



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
