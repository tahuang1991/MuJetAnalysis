import FWCore.ParameterSet.Config as cms

L2TrackPtFromSegmentAlignment = cms.EDProducer("L2TrackPtFromSegmentAlignmentProducer",
    InputObjects = cms.InputTag("hltL2Muons"),
    ServiceParameters = cms.PSet(),
    TrackLoaderParameters = cms.PSet()
)
