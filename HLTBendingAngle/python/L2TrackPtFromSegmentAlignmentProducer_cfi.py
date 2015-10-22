import FWCore.ParameterSet.Config as cms

from RecoMuon.TrackingTools.MuonServiceProxy_cff import *
from RecoMuon.TrackingTools.MuonTrackLoader_cff import *

#https://raw.githubusercontent.com/cms-sw/cmssw/CMSSW_8_0_X/HLTrigger/Configuration/python/HLT_GRun_cff.py                                                                         
TrackLoaderParameters_from_HLT_TrkMu15_DoubleTrkMu5NoFiltersNoVtx = cms.PSet(
    Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
    DoSmoothing = cms.bool( False ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MuonUpdatorAtVertexParameters = cms.PSet(
        MaxChi2 = cms.double( 1000000.0 ),
        BeamSpotPosition = cms.vdouble( 0.0, 0.0, 0.0 ),
        Propagator = cms.string( "SteppingHelixPropagatorL2Opposite" ),
        BeamSpotPositionErrors = cms.vdouble( 0.1, 0.1, 5.3 )
        ),
    VertexConstraint = cms.bool( True ), # don't produce collections at vtx                                                                                                       
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" )
    )

L2TrackPtFromSegmentAlignment = cms.EDProducer("L2TrackPtFromSegmentAlignmentProducer",
    InputObjects = cms.InputTag("hltL2Muons"),
    ServiceParameters = MuonServiceProxy.ServiceParameters,
    TrackLoaderParameters = MuonTrackLoaderForL2.TrackLoaderParameters                                                                                                            
    #TrackLoaderParameters = TrackLoaderParameters_from_HLT_TrkMu15_DoubleTrkMu5NoFiltersNoVtx
)

L2TrackPtFromSegmentAlignment.TrackLoaderParameters.beamSpot = "hltOnlineBeamSpot"
L2TrackPtFromSegmentAlignment.TrackLoaderParameters.VertexConstraint = False
L2TrackPtFromSegmentAlignment.TrackLoaderParameters.MuonUpdatorAtVertexParameters.Propagator = 'SteppingHelixPropagatorOpposite'
L2TrackPtFromSegmentAlignment.TrackLoaderParameters.MuonUpdatorAtVertexParameters.Propagator = 'hltESPFastSteppingHelixPropagatorAny'
