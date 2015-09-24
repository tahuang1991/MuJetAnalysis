import FWCore.ParameterSet.Config as cms

L2MuonCandidatesPtFromSegmentAlignment = cms.EDProducer("L2MuonCandidatePtFromSegmentAlignmentProducer",
    InputObjects = cms.InputTag("L2MuonCandidatesNoVtx")
)
