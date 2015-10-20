import FWCore.ParameterSet.Config as cms

from RecoMuon.TrackingTools.MuonServiceProxy_cff import *
from RecoMuon.TrackingTools.MuonTrackLoader_cff import *

L2MuonCandidatesPtFromSegmentAlignment = cms.EDProducer("L2MuonCandidatePtFromSegmentAlignmentProducer",
    InputObjects = cms.InputTag("hltL2MuonCandidatesNoVtx"),
    ServiceParameters = MuonServiceProxy.ServiceParameters,
    TrackLoaderParameters = MuonTrackLoaderForL2.TrackLoaderParameters
)
