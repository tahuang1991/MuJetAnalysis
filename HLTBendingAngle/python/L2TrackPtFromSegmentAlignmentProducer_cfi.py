import FWCore.ParameterSet.Config as cms

from RecoMuon.TrackingTools.MuonServiceProxy_cff import *
from RecoMuon.TrackingTools.MuonTrackLoader_cff import *

L2TrackPtFromSegmentAlignment = cms.EDProducer("L2TrackPtFromSegmentAlignmentProducer",
    InputObjects = cms.InputTag("hltL2Muons"),
    ServiceParameters = MuonServiceProxy.ServiceParameters,
    TrackLoaderParameters = MuonTrackLoaderForL2.TrackLoaderParameters
)
