## Customization for HLT_TrkMu15_DoubleTrkMu5_v1

import FWCore.ParameterSet.Config as cms

hltTripleTrkMuFiltered5 = cms.EDFilter("HLTMuonTrkFilter",
    maxNormalizedChi2 = cms.double( 1.0E99 ),
    saveTags = cms.bool( False ),
    maxAbsEta = cms.double( 2.5 ),
    previousCandTag = cms.InputTag( "" ),
    minPt = cms.double( 5.0 ),
    minN = cms.uint32( 3 ),
    inputCandCollection = cms.InputTag( "hltGlbTrkMuonCands" ),
    minMuonStations = cms.int32( 2 ),
    trkMuonId = cms.uint32( 0 ),
    requiredTypeMask = cms.uint32( 0 ),
    minMuonHits = cms.int32( -1 ),
    minTrkHits = cms.int32( -1 ),
    inputMuonCollection = cms.InputTag( "hltGlbTrkMuons" ),
    allowedTypeMask = cms.uint32( 255 )
)
hltSingleTrkMuFiltered15 = cms.EDFilter("HLTMuonTrkFilter",
    maxNormalizedChi2 = cms.double( 1.0E99 ),
    saveTags = cms.bool( False ),
    maxAbsEta = cms.double( 2.5 ),
    previousCandTag = cms.InputTag( "" ),
    minPt = cms.double( 15.0 ),
    minN = cms.uint32( 1 ),
    inputCandCollection = cms.InputTag( "hltGlbTrkMuonCands" ),
    minMuonStations = cms.int32( 2 ),
    trkMuonId = cms.uint32( 0 ),
    requiredTypeMask = cms.uint32( 0 ),
    minMuonHits = cms.int32( -1 ),
    minTrkHits = cms.int32( -1 ),
    inputMuonCollection = cms.InputTag( "hltGlbTrkMuons" ),
    allowedTypeMask = cms.uint32( 255 )
)
hltTripleTrkMuFiltered5NoVtx = cms.EDFilter("HLTMuonTrkFilter",
    maxNormalizedChi2 = cms.double( 1.0E99 ),
    saveTags = cms.bool( False ),
    maxAbsEta = cms.double( 2.5 ),
    previousCandTag = cms.InputTag( "" ),
    minPt = cms.double( 5.0 ),
    minN = cms.uint32( 3 ),
    inputCandCollection = cms.InputTag( "hltGlbTrkMuonCandsNoVtx" ),
    minMuonStations = cms.int32( 2 ),
    trkMuonId = cms.uint32( 0 ),
    requiredTypeMask = cms.uint32( 0 ),
    minMuonHits = cms.int32( -1 ),
    minTrkHits = cms.int32( -1 ),
    inputMuonCollection = cms.InputTag( "hltGlbTrkMuonsNoVtx" ),
    allowedTypeMask = cms.uint32( 255 )
)
hltSingleTrkMuFiltered15NoVtx = cms.EDFilter("HLTMuonTrkFilter",
    maxNormalizedChi2 = cms.double( 1.0E99 ),
    saveTags = cms.bool( False ),
    maxAbsEta = cms.double( 2.5 ),
    previousCandTag = cms.InputTag( "" ),
    minPt = cms.double( 15.0 ),
    minN = cms.uint32( 1 ),
    inputCandCollection = cms.InputTag( "hltGlbTrkMuonCandsNoVtx" ),
    minMuonStations = cms.int32( 2 ),
    trkMuonId = cms.uint32( 0 ),
    requiredTypeMask = cms.uint32( 0 ),
    minMuonHits = cms.int32( -1 ),
    minTrkHits = cms.int32( -1 ),
    inputMuonCollection = cms.InputTag( "hltGlbTrkMuonsNoVtx" ),
    allowedTypeMask = cms.uint32( 255 )
)
hltL3pfL1sDoubleMu103p5L1f0L2pf0TwoMuL3PreFiltered5 = cms.EDFilter( "HLTMuonL3PreFilter",
    MaxNormalizedChi2 = cms.double( 9999.0 ),
    saveTags = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2pfL1sDoubleMu103p5L1f0L2PreFiltered0" ),
    MinNmuonHits = cms.int32( 0 ),
    MinN = cms.int32( 2 ),
    MinTrackPt = cms.double( 0.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxDXYBeamSpot = cms.double( 9999.0 ),
    MinNhits = cms.int32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MaxDz = cms.double( 9999.0 ),
    MaxPtDifference = cms.double( 9999.0 ),
    MaxDr = cms.double( 2.0 ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    MinDXYBeamSpot = cms.double( -1.0 ),
    MinDr = cms.double( -1.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinPt = cms.double( 5.0 )
)
hltL3pfL1sDoubleMu103p5L1f0L2pf0ThreeMuL3PreFiltered5 = cms.EDFilter( "HLTMuonL3PreFilter",
    MaxNormalizedChi2 = cms.double( 9999.0 ),
    saveTags = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2pfL1sDoubleMu103p5L1f0L2PreFiltered0" ),
    MinNmuonHits = cms.int32( 0 ),
    MinN = cms.int32( 3 ),
    MinTrackPt = cms.double( 0.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxDXYBeamSpot = cms.double( 9999.0 ),
    MinNhits = cms.int32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MaxDz = cms.double( 9999.0 ),
    MaxPtDifference = cms.double( 9999.0 ),
    MaxDr = cms.double( 2.0 ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    MinDXYBeamSpot = cms.double( -1.0 ),
    MinDr = cms.double( -1.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinPt = cms.double( 5.0 )
)
hltL3fL1sDoubleMu103p5L1f0L2f10OneMuL3Filtered15 = cms.EDFilter( "HLTMuonL3PreFilter",
    MaxNormalizedChi2 = cms.double( 9999.0 ),
    saveTags = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu103p5L1f0L2Filtered10OneMu" ),
    MinNmuonHits = cms.int32( 0 ),
    MinN = cms.int32( 1 ),
    MinTrackPt = cms.double( 0.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxDXYBeamSpot = cms.double( 9999.0 ),
    MinNhits = cms.int32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MaxDz = cms.double( 9999.0 ),
    MaxPtDifference = cms.double( 9999.0 ),
    MaxDr = cms.double( 2.0 ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    MinDXYBeamSpot = cms.double( -1.0 ),
    MinDr = cms.double( -1.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinPt = cms.double( 15.0 )
)

def addHLT_Mu17_Mu8_v1_NoDz(process):
    ## drop the dz filter at the end
    process.HLT_Mu17_Mu8_DZ_v1_NoDz = cms.Path( 
        process.HLTBeginSequence + 
        process.hltL1sL1DoubleMu103p5ORDoubleMu125 + 
        process.hltPreMu17Mu8DZ + 
        process.hltL1fL1sDoubleMu103p5ORDoubleMu125L1Filtered0 + 
        process.HLTL2muonrecoSequence + 
        process.hltL2pfL1sDoubleMu103p5L1f0L2PreFiltered0 + 
        process.hltL2fL1sDoubleMu103p5L1f0L2Filtered10OneMu + 
        process.HLTL3muonrecoSequence + 
        process.hltL3pfL1sDoubleMu103p5L1f0L2pf0L3PreFiltered8 + 
        process.hltL3fL1sDoubleMu103p5L1f0L2f10OneMuL3Filtered17 + 
        process.HLTEndSequence 
    )
    return process

def addHLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v1_NoIso(process):
    ## drop the isolation filter at the end
    process.HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v1_NoIso = cms.Path( 
        process.HLTBeginSequence + 
        process.hltL1sL1DoubleMu103p5ORDoubleMu125 + 
        process.hltPreMu17TrkIsoVVLMu8TrkIsoVVL + 
        process.hltL1fL1sDoubleMu103p5ORDoubleMu125L1Filtered0 + 
        process.HLTL2muonrecoSequence + 
        process.hltL2pfL1sDoubleMu103p5L1f0L2PreFiltered0 + 
        process.hltL2fL1sDoubleMu103p5L1f0L2Filtered10OneMu + 
        process.HLTL3muonrecoSequence + 
        process.hltL3pfL1sDoubleMu103p5L1f0L2pf0L3PreFiltered8 + 
        process.hltL3fL1sDoubleMu103p5L1f0L2f10OneMuL3Filtered17 + 
        process.HLTL3muontrkisovvlSequence + 
        process.HLTEndSequence 
    )
    return process

def addHLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v1_NoIso(process):
    ## drop the isolation filter at the end
    process.HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v1_NoIso = cms.Path( 
        process.HLTBeginSequence + 
        process.hltL1sL1DoubleMu103p5ORDoubleMu125 + 
        process.hltPreMu17TrkIsoVVLTkMu8TrkIsoVVL + 
        process.hltL1fL1sDoubleMu103p5L1OneMuFiltered0 + 
        process.HLTL2muonrecoSequence + 
        process.hltL2fL1sDoubleMu103p5L1f0OneMuL2Filtered10 + 
        process.HLTL3muonrecoSequence + 
        process.hltL3fL1sDoubleMu103p5L1f0L2f10L3Filtered17 + 
        process.HLTTrackerMuonSequence + 
        process.hltDiMuonGlbFiltered17TrkFiltered8 + 
        process.HLTGlbtrkmuontrkisovvlSequence + 
        process.HLTEndSequence 
    )
    return process

def addHLT_TrkMu15_DoubleTrkMu5_v1(process):
    """
    Step 1: Start from HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v1
    Step 2: Remove the isolation sequence
    Step 3: Add the TrkMu reconstruction sequence
    Step 4: Add TripleTrkMu pt5 filter (HLTMuonTrkFilter)
    Step 5: Add SingleTrkMu15 filter (HLTMuonTrkFilter)
    Step 6: Change L3 prefilter and filter
    """
    
    process.hltL3pfL1sDoubleMu103p5L1f0L2pf0TwoMuL3PreFiltered5 = hltL3pfL1sDoubleMu103p5L1f0L2pf0TwoMuL3PreFiltered5
    process.hltL3fL1sDoubleMu103p5L1f0L2f10OneMuL3Filtered15 = hltL3fL1sDoubleMu103p5L1f0L2f10OneMuL3Filtered15
    process.hltTripleTrkMuFiltered5 = hltTripleTrkMuFiltered5
    process.hltSingleTrkMuFiltered15 = hltSingleTrkMuFiltered15

    process.HLT_TrkMu15_DoubleTrkMu5_v1_hltL1sL1DoubleMu103p5ORDoubleMu125 = cms.Path( 
        process.HLTBeginSequence + 
        process.hltL1sL1DoubleMu103p5ORDoubleMu125 + 
        process.HLTEndSequence 
    )

    process.HLT_TrkMu15_DoubleTrkMu5_v1_hltL1fL1sDoubleMu103p5ORDoubleMu125L1Filtered0 = cms.Path( 
        process.HLTBeginSequence + 
        process.hltL1sL1DoubleMu103p5ORDoubleMu125 + 
        process.hltPreMu17TrkIsoVVLMu8TrkIsoVVL + 
        process.hltL1fL1sDoubleMu103p5ORDoubleMu125L1Filtered0 + 
        process.HLTEndSequence 
    )

    process.HLT_TrkMu15_DoubleTrkMu5_v1_hltL2pfL1sDoubleMu103p5L1f0L2PreFiltered0 = cms.Path( 
        process.HLTBeginSequence + 
        process.hltL1sL1DoubleMu103p5ORDoubleMu125 + 
        process.hltPreMu17TrkIsoVVLMu8TrkIsoVVL + 
        process.hltL1fL1sDoubleMu103p5ORDoubleMu125L1Filtered0 + 
        process.HLTL2muonrecoSequence + 
        process.hltL2pfL1sDoubleMu103p5L1f0L2PreFiltered0 + 
        process.HLTEndSequence 
    )

    process.HLT_TrkMu15_DoubleTrkMu5_v1_hltL2fL1sDoubleMu103p5L1f0L2Filtered10OneMu = cms.Path( 
        process.HLTBeginSequence + 
        process.hltL1sL1DoubleMu103p5ORDoubleMu125 + 
        process.hltPreMu17TrkIsoVVLMu8TrkIsoVVL + 
        process.hltL1fL1sDoubleMu103p5ORDoubleMu125L1Filtered0 + 
        process.HLTL2muonrecoSequence + 
        process.hltL2pfL1sDoubleMu103p5L1f0L2PreFiltered0 + 
        process.hltL2fL1sDoubleMu103p5L1f0L2Filtered10OneMu + 
        process.HLTEndSequence 
    )

    process.HLT_TrkMu15_DoubleTrkMu5_v1_hltL3pfL1sDoubleMu103p5L1f0L2pf0TwoMuL3PreFiltered5 = cms.Path( 
        process.HLTBeginSequence + 
        process.hltL1sL1DoubleMu103p5ORDoubleMu125 + 
        process.hltPreMu17TrkIsoVVLMu8TrkIsoVVL + 
        process.hltL1fL1sDoubleMu103p5ORDoubleMu125L1Filtered0 + 
        process.HLTL2muonrecoSequence + 
        process.hltL2pfL1sDoubleMu103p5L1f0L2PreFiltered0 + 
        process.hltL2fL1sDoubleMu103p5L1f0L2Filtered10OneMu + 
        process.HLTL3muonrecoSequence + 
        process.hltL3pfL1sDoubleMu103p5L1f0L2pf0TwoMuL3PreFiltered5 + 
        process.HLTEndSequence 
    )

    process.HLT_TrkMu15_DoubleTrkMu5_v1_hltL3fL1sDoubleMu103p5L1f0L2f10OneMuL3Filtered15 = cms.Path( 
        process.HLTBeginSequence + 
        process.hltL1sL1DoubleMu103p5ORDoubleMu125 + 
        process.hltPreMu17TrkIsoVVLMu8TrkIsoVVL + 
        process.hltL1fL1sDoubleMu103p5ORDoubleMu125L1Filtered0 + 
        process.HLTL2muonrecoSequence + 
        process.hltL2pfL1sDoubleMu103p5L1f0L2PreFiltered0 + 
        process.hltL2fL1sDoubleMu103p5L1f0L2Filtered10OneMu + 
        process.HLTL3muonrecoSequence + 
        process.hltL3pfL1sDoubleMu103p5L1f0L2pf0TwoMuL3PreFiltered5 + 
        process.hltL3fL1sDoubleMu103p5L1f0L2f10OneMuL3Filtered15 + 
        process.HLTEndSequence 
    )

    process.HLT_TrkMu15_DoubleTrkMu5_v1_hltTripleTrkMuFiltered5 = cms.Path( 
        process.HLTBeginSequence + 
        process.hltL1sL1DoubleMu103p5ORDoubleMu125 + 
        process.hltPreMu17TrkIsoVVLMu8TrkIsoVVL + 
        process.hltL1fL1sDoubleMu103p5ORDoubleMu125L1Filtered0 + 
        process.HLTL2muonrecoSequence + 
        process.hltL2pfL1sDoubleMu103p5L1f0L2PreFiltered0 + 
        process.hltL2fL1sDoubleMu103p5L1f0L2Filtered10OneMu + 
        process.HLTL3muonrecoSequence + 
        process.hltL3pfL1sDoubleMu103p5L1f0L2pf0TwoMuL3PreFiltered5 + 
        process.hltL3fL1sDoubleMu103p5L1f0L2f10OneMuL3Filtered15 + 
        process.HLTTrackerMuonSequence +
        process.hltTripleTrkMuFiltered5 +
        process.HLTEndSequence 
    )

    process.HLT_TrkMu15_DoubleTrkMu5_v1 = cms.Path( 
        process.HLTBeginSequence + 
        process.hltL1sL1DoubleMu103p5ORDoubleMu125 + 
        process.hltPreMu17TrkIsoVVLMu8TrkIsoVVL + 
        process.hltL1fL1sDoubleMu103p5ORDoubleMu125L1Filtered0 + 
        process.HLTL2muonrecoSequence + 
        process.hltL2pfL1sDoubleMu103p5L1f0L2PreFiltered0 + 
        process.hltL2fL1sDoubleMu103p5L1f0L2Filtered10OneMu + 
        process.HLTL3muonrecoSequence + 
        process.hltL3pfL1sDoubleMu103p5L1f0L2pf0TwoMuL3PreFiltered5 + 
        process.hltL3fL1sDoubleMu103p5L1f0L2f10OneMuL3Filtered15 + 
        process.HLTTrackerMuonSequence +
        process.hltTripleTrkMuFiltered5 +
        process.hltSingleTrkMuFiltered15 +
        process.HLTEndSequence 
    )
    return process

def addHLT_Mu15_DoubleMu5NoVtx_v1(process):
    """
    Step 1: Start from HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v1
    Step 2: Remove the isolation sequence
    Step 3: Replace the L2 and L3 RECO sequence by variants that do not have Vtx cut
    Step 4: Change L3 prefilter and filter cuts
    """

    process.hltL3pfL1sDoubleMu103p5L1f0L2pf0ThreeMuL3PreFiltered5 = hltL3pfL1sDoubleMu103p5L1f0L2pf0ThreeMuL3PreFiltered5
    process.hltL3pfL1sDoubleMu103p5L1f0L2pf0TwoMuL3PreFiltered5 = hltL3pfL1sDoubleMu103p5L1f0L2pf0TwoMuL3PreFiltered5
    process.hltL3fL1sDoubleMu103p5L1f0L2f10OneMuL3Filtered15 = hltL3fL1sDoubleMu103p5L1f0L2f10OneMuL3Filtered15

    process.HLT_Mu15_DoubleMu5NoVtx_v1_hltL1fL1sDoubleMu103p5ORDoubleMu125L1Filtered0 = cms.Path( 
        process.HLTBeginSequence + 
        process.hltL1sL1DoubleMu103p5ORDoubleMu125 + 
        process.hltPreMu17TrkIsoVVLMu8TrkIsoVVL + 
        process.hltL1fL1sDoubleMu103p5ORDoubleMu125L1Filtered0 + 
        process.HLTEndSequence 
    )

    process.HLT_Mu15_DoubleMu5NoVtx_v1_hltL2pfL1sDoubleMu103p5L1f0L2PreFiltered0 = cms.Path( 
        process.HLTBeginSequence + 
        process.hltL1sL1DoubleMu103p5ORDoubleMu125 + 
        process.hltPreMu17TrkIsoVVLMu8TrkIsoVVL + 
        process.hltL1fL1sDoubleMu103p5ORDoubleMu125L1Filtered0 + 
        process.HLTL2muonrecoSequenceNoVtx + 
        process.hltL2pfL1sDoubleMu103p5L1f0L2PreFiltered0 + 
        process.HLTEndSequence 
    )

    process.HLT_Mu15_DoubleMu5NoVtx_v1_hltL2fL1sDoubleMu103p5L1f0L2Filtered10OneMu = cms.Path( 
        process.HLTBeginSequence + 
        process.hltL1sL1DoubleMu103p5ORDoubleMu125 + 
        process.hltPreMu17TrkIsoVVLMu8TrkIsoVVL + 
        process.hltL1fL1sDoubleMu103p5ORDoubleMu125L1Filtered0 + 
        process.HLTL2muonrecoSequenceNoVtx + 
        process.hltL2pfL1sDoubleMu103p5L1f0L2PreFiltered0 + 
        process.hltL2fL1sDoubleMu103p5L1f0L2Filtered10OneMu + 
        process.HLTEndSequence 
    )

    process.HLT_Mu15_DoubleMu5NoVtx_v1_hltL3pfL1sDoubleMu103p5L1f0L2pf0ThreeMuL3PreFiltered5 = cms.Path( 
        process.HLTBeginSequence + 
        process.hltL1sL1DoubleMu103p5ORDoubleMu125 + 
        process.hltPreMu17TrkIsoVVLMu8TrkIsoVVL + 
        process.hltL1fL1sDoubleMu103p5ORDoubleMu125L1Filtered0 + 
        process.HLTL2muonrecoSequenceNoVtx + 
        process.hltL2pfL1sDoubleMu103p5L1f0L2PreFiltered0 + 
        process.hltL2fL1sDoubleMu103p5L1f0L2Filtered10OneMu + 
        process.HLTL3NoFiltersNoVtxmuonrecoSequence + 
        process.hltL3pfL1sDoubleMu103p5L1f0L2pf0ThreeMuL3PreFiltered5 +
        process.HLTEndSequence 
    )

    process.HLT_Mu15_DoubleMu5NoVtx_v1_TwoMuL3PreFiltered5 = cms.Path( 
        process.HLTBeginSequence + 
        process.hltL1sL1DoubleMu103p5ORDoubleMu125 + 
        process.hltPreMu17TrkIsoVVLMu8TrkIsoVVL + 
        process.hltL1fL1sDoubleMu103p5ORDoubleMu125L1Filtered0 + 
        process.HLTL2muonrecoSequenceNoVtx +  ## take from HLT_DoubleMu33NoFiltersNoVtx_v
        process.hltL2pfL1sDoubleMu103p5L1f0L2PreFiltered0 + 
        process.hltL2fL1sDoubleMu103p5L1f0L2Filtered10OneMu + 
        process.HLTL3NoFiltersNoVtxmuonrecoSequence +  ## take from HLT_DoubleMu33NoFiltersNoVtx_v
        process.hltL3pfL1sDoubleMu103p5L1f0L2pf0TwoMuL3PreFiltered5 +
        process.hltL3fL1sDoubleMu103p5L1f0L2f10OneMuL3Filtered15 +
        process.HLTEndSequence 
    )

    process.HLT_Mu15_DoubleMu5NoVtx_v1 = cms.Path( 
        process.HLTBeginSequence + 
        process.hltL1sL1DoubleMu103p5ORDoubleMu125 + 
        process.hltPreMu17TrkIsoVVLMu8TrkIsoVVL + 
        process.hltL1fL1sDoubleMu103p5ORDoubleMu125L1Filtered0 + 
        process.HLTL2muonrecoSequenceNoVtx +  ## take from HLT_DoubleMu33NoFiltersNoVtx_v
        process.hltL2pfL1sDoubleMu103p5L1f0L2PreFiltered0 + 
        process.hltL2fL1sDoubleMu103p5L1f0L2Filtered10OneMu + 
        process.HLTL3NoFiltersNoVtxmuonrecoSequence +  ## take from HLT_DoubleMu33NoFiltersNoVtx_v
        process.hltL3pfL1sDoubleMu103p5L1f0L2pf0ThreeMuL3PreFiltered5 +
        process.hltL3fL1sDoubleMu103p5L1f0L2f10OneMuL3Filtered15 +
        process.HLTEndSequence 
    )
    return process

def addHLT_TrkMu15_DoubleTrkMu5NoVtx_v1(process):
    """
    Step 1: Start from HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v1
    Step 2: Remove the isolation sequence
    Step 3: Replace the L2 and L3 RECO sequence by variants that do not have Vtx cut
    Step 4: Change L3 prefilter and filter cuts
    Step 5: Add the TrkMu reconstruction sequence (need to redefine it as well HLTTrackerMuonSequenceNoVtx)
    Step 6: Add TripleTrkMu pt5 filter (HLTMuonTrkFilter)
    Step 7: Add SingleTrkMu15 filter (HLTMuonTrkFilter)
    """

    process.hltL3pfL1sDoubleMu103p5L1f0L2pf0ThreeMuL3PreFiltered5 = hltL3pfL1sDoubleMu103p5L1f0L2pf0ThreeMuL3PreFiltered5
    process.hltL3fL1sDoubleMu103p5L1f0L2f10OneMuL3Filtered15 = hltL3fL1sDoubleMu103p5L1f0L2f10OneMuL3Filtered15
    process.hltTripleTrkMuFiltered5NoVtx = hltTripleTrkMuFiltered5NoVtx
    process.hltSingleTrkMuFiltered15NoVtx = hltSingleTrkMuFiltered15NoVtx

    ## define new NoVtx modules by cloning updatedAtVtx ones
    process.hltL3MuonsOIStateNoVtx = process.hltL3MuonsOIState.clone(
        MuonCollectionLabel = cms.InputTag( 'hltL2Muons' )
    ) 
    hltL3TrajSeedOIHitNoVtx_TkSeedGenerator = process.hltL3TrajSeedOIHit.TkSeedGenerator.clone(
        L3TkCollectionA = cms.InputTag( "hltL3MuonsOIStateNoVtx" )       
    )
    process.hltL3TrajSeedOIHitNoVtx = process.hltL3TrajSeedOIHit.clone(
        TkSeedGenerator = hltL3TrajSeedOIHitNoVtx_TkSeedGenerator,
        MuonCollectionLabel = cms.InputTag( 'hltL2Muons' )
    )
    process.hltL3TrackCandidateFromL2OIHitNoVtx = process.hltL3TrackCandidateFromL2OIHit.clone(
        src = cms.InputTag( "hltL3TrajSeedOIHitNoVtx" ),
    )
    process.hltL3TkTracksFromL2OIHitNoVtx = process.hltL3TkTracksFromL2OIHit.clone(
        src = cms.InputTag( "hltL3TrackCandidateFromL2OIHitNoVtx" ),
    )
    process.hltL3MuonsOIHitNoVtx = process.hltL3MuonsOIHit.clone(
        MuonCollectionLabel = cms.InputTag( 'hltL2Muons' )
    )
    process.hltL3TkFromL2OICombinationNoVtx = process.hltL3TkFromL2OICombination.clone(
        labels = cms.VInputTag( 'hltL3MuonsOIStateNoVtx','hltL3MuonsOIHitNoVtx' )
    )    
    hltL3TrajSeedIOHitNoVtx_TkSeedGenerator = process.hltL3TrajSeedIOHit.TkSeedGenerator.clone(
        L3TkCollectionA = cms.InputTag( "hltL3TkFromL2OICombinationNoVtx" )       
    )
    process.hltL3TrajSeedIOHitNoVtx = process.hltL3TrajSeedIOHit.clone(
        TkSeedGenerator = hltL3TrajSeedIOHitNoVtx_TkSeedGenerator,
        MuonCollectionLabel = cms.InputTag( 'hltL2Muons' )
    )
    process.hltL3TrackCandidateFromL2IOHitNoVtx = process.hltL3TrackCandidateFromL2IOHit.clone(
        src = cms.InputTag( "hltL3TrajSeedIOHitNoVtx" ),
    )
    process.hltL3TkTracksFromL2IOHitNoVtx = process.hltL3TkTracksFromL2IOHit.clone(
        src = cms.InputTag( "hltL3TrackCandidateFromL2IOHitNoVtx" ),        
    )
    process.hltL3MuonsIOHitNoVtx = process.hltL3MuonsIOHit.clone(
        MuonCollectionLabel = cms.InputTag( 'hltL2Muons' )
    )    
    process.hltL3TrajectorySeedNoVtx = process.hltL3TrajectorySeed.clone(
        labels = cms.VInputTag( 'hltL3TrajSeedIOHitNoVtx',
                                'hltL3TrajSeedOIStateNoVtx',
                                'hltL3TrajSeedOIHitNoVtx' )
    )
    process.hltL3TrackCandidateFromL2NoVtx = process.hltL3TrackCandidateFromL2.clone(
        labels = cms.VInputTag( 'hltL3TrackCandidateFromL2IOHitNoVtx',
                                'hltL3TrackCandidateFromL2OIHitNoVtx',
                                'hltL3TrackCandidateFromL2OIStateNoVtx' )
    )

    ## need noVtx inputs for this sequence
    process.HLTL3muonTkCandidateSequenceNoVtx = cms.Sequence( 
        process.HLTDoLocalPixelSequence + 
        process.HLTDoLocalStripSequence + 

        process.hltL3TrajSeedOIStateNoVtx + ## already defined
        process.hltL3TrackCandidateFromL2OIStateNoVtx + ## already defined
        process.hltL3TkTracksFromL2OIStateNoVtx + ## already defined
        process.hltL3MuonsOIStateNoVtx + ## need to redefine this one

        process.hltL3TrajSeedOIHitNoVtx + ## need to redefine this one
        process.hltL3TrackCandidateFromL2OIHitNoVtx + ## need to redefine this one
        process.hltL3TkTracksFromL2OIHitNoVtx + ## need to redefine this one
        process.hltL3MuonsOIHitNoVtx + ## need to redefine this one

        process.hltL3TkFromL2OICombinationNoVtx + ## need to redefine this one

        process.hltPixelLayerTriplets + 
        process.hltPixelLayerPairs + 
        process.hltMixedLayerPairs + 

        process.hltL3TrajSeedIOHitNoVtx + ## need to redefine this one
        process.hltL3TrackCandidateFromL2IOHitNoVtx + ## need to redefine this one
        process.hltL3TkTracksFromL2IOHitNoVtx + ## need to redefine this one
        process.hltL3MuonsIOHitNoVtx + ## need to redefine this one

        process.hltL3TrajectorySeedNoVtx + ## need to redefine this one
        process.hltL3TrackCandidateFromL2NoVtx ## need to redefine this one
    )
    process.hltL3TkTracksMergeStep1NoVtx = process.hltL3TkTracksMergeStep1.clone(
        selectedTrackQuals = cms.VInputTag( 'hltL3TkTracksFromL2OIStateNoVtx','hltL3TkTracksFromL2OIHitNoVtx' ),
        TrackProducers = cms.VInputTag( 'hltL3TkTracksFromL2OIStateNoVtx','hltL3TkTracksFromL2OIHitNoVtx' ),
    )
    process.hltL3TkTracksFromL2NoVtx = process.hltL3TkTracksFromL2.clone(
        src = cms.InputTag( "hltL3TrackCandidateFromL2OIStateNoVtx" ),
    )        
    process.hltL3MuonsLinksCombinationNoVtx = process.hltL3MuonsLinksCombination.clone(
        labels = cms.VInputTag( 'hltL3MuonsOIStateNoVtx','hltL3MuonsOIHitNoVtx','hltL3MuonsIOHitNoVtx' )        
    )    
    process.hltL3MuonsNoVtx = process.hltL3Muons.clone(
        labels = cms.VInputTag( 'hltL3MuonsOIStateNoVtx','hltL3MuonsOIHitNoVtx','hltL3MuonsIOHitNoVtx' )
    )
    
    ## need noVtx inputs for this sequence
    process.HLTL3muonrecoNocandSequenceNoVtx = cms.Sequence( 
        process.HLTL3muonTkCandidateSequenceNoVtx + ## need to redefine this one
        process.hltL3TkTracksMergeStep1NoVtx + ## need to redefine this one
        process.hltL3TkTracksFromL2NoVtx + ## need to redefine this one
        process.hltL3MuonsLinksCombinationNoVtx + ## need to redefine this one
        process.hltL3MuonsNoVtx ## need to redefine this one
    )

    """
    Take inputs from 
    HLTL3NoFiltersNoVtxmuonrecoNocandSequence = cms.Sequence(
                                          HLTL3NoFiltersNoVtxmuonTkCandidateSequence +
                                          hltL3NoFiltersNoVtxTkTracksMergeStep1 +
                                          hltL3NoFiltersTkTracksFromL2Novtx +
                                          hltL3NoFiltersNoVtxMuonsLinksCombination +
                                          hltL3NoFiltersNoVtxMuons
                                          )
    """

    process.hltDiMuonMergingNoVtx = process.hltDiMuonMerging.clone(
        #selectedTrackQuals = cms.VInputTag( 'hltL3TkTracksFromL2NoVtx','hltMuCtfTracks' ),
        #TrackProducers = cms.VInputTag(     'hltL3TkTracksFromL2NoVtx','hltMuCtfTracks' ),
        selectedTrackQuals = cms.VInputTag( 'hltL3NoFiltersTkTracksFromL2Novtx','hltMuCtfTracks' ),
        TrackProducers = cms.VInputTag( 'hltL3NoFiltersTkTracksFromL2Novtx','hltMuCtfTracks' ),
    )
    process.hltDiMuonLinksNoVtx = process.hltDiMuonLinks.clone(
        InclusiveTrackerTrackCollection = cms.InputTag( "hltDiMuonMergingNoVtx" ),
        LinkCollection = cms.InputTag( "hltL3NoFiltersNoVtxMuonsLinksCombination" ),
    )
    process.hltGlbTrkMuonsNoVtx = process.hltGlbTrkMuons.clone(
        inputCollectionLabels = cms.VInputTag( 'hltDiMuonMergingNoVtx','hltDiMuonLinksNoVtx' ),
    )
    process.hltGlbTrkMuonCandsNoVtx = process.hltGlbTrkMuonCands.clone(
        InputObjects = cms.InputTag( "hltGlbTrkMuonsNoVtx" )
    )

    ## redefine the tracker muon sequence
    ## need to check the inputs
    process.HLTTrackerMuonSequenceNoVtx = cms.Sequence( 
        process.HLTDoLocalPixelSequence + 
        process.hltPixelLayerTriplets + 
        process.hltPixelTracks + 
        process.HLTDoLocalStripSequence + 
        process.hltMuTrackSeeds + 
        process.hltMuCkfTrackCandidates + 
        process.hltMuCtfTracks + 
        process.HLTL3NoFiltersNoVtxmuonrecoNocandSequence + 
#        process.HLTL3muonrecoNocandSequenceNoVtx + ## need to redefine this one
        process.hltDiMuonMergingNoVtx + ## need to redefine this one
        process.hltDiMuonLinksNoVtx + ## need to redefine this one
        process.hltGlbTrkMuonsNoVtx + ## need to redefine this one
        process.hltGlbTrkMuonCandsNoVtx ## need to redefine this one
    )

    process.HLT_TrkMu15_DoubleTrkMu5NoVtx_v1_hltL3pfL1sDoubleMu103p5L1f0L2pf0ThreeMuL3PreFiltered5 = cms.Path( 
        process.HLTBeginSequence + 
        process.hltL1sL1DoubleMu103p5ORDoubleMu125 + 
        process.hltPreMu17TrkIsoVVLMu8TrkIsoVVL + 
        process.hltL1fL1sDoubleMu103p5ORDoubleMu125L1Filtered0 + 
        process.HLTL2muonrecoSequenceNoVtx + 
        process.hltL2pfL1sDoubleMu103p5L1f0L2PreFiltered0 + 
        process.hltL2fL1sDoubleMu103p5L1f0L2Filtered10OneMu + 
        process.HLTL3NoFiltersNoVtxmuonrecoSequence +
        process.hltL3pfL1sDoubleMu103p5L1f0L2pf0ThreeMuL3PreFiltered5 + 
        process.HLTEndSequence 
    )

    process.HLT_TrkMu15_DoubleTrkMu5NoVtx_v1_hltL3fL1sDoubleMu103p5L1f0L2f10OneMuL3Filtered15 = cms.Path( 
        process.HLTBeginSequence + 
        process.hltL1sL1DoubleMu103p5ORDoubleMu125 + 
        process.hltPreMu17TrkIsoVVLMu8TrkIsoVVL + 
        process.hltL1fL1sDoubleMu103p5ORDoubleMu125L1Filtered0 + 
        process.HLTL2muonrecoSequenceNoVtx + 
        process.hltL2pfL1sDoubleMu103p5L1f0L2PreFiltered0 + 
        process.hltL2fL1sDoubleMu103p5L1f0L2Filtered10OneMu + 
        process.HLTL3NoFiltersNoVtxmuonrecoSequence +
        process.hltL3pfL1sDoubleMu103p5L1f0L2pf0ThreeMuL3PreFiltered5 + 
        process.hltL3fL1sDoubleMu103p5L1f0L2f10OneMuL3Filtered15 + 
        process.HLTEndSequence 
    )

    process.HLT_TrkMu15_DoubleTrkMu5NoVtx_v1_hltTripleTrkMuFiltered5NoVtx = cms.Path( 
        process.HLTBeginSequence + 
        process.hltL1sL1DoubleMu103p5ORDoubleMu125 + 
        process.hltPreMu17TrkIsoVVLMu8TrkIsoVVL + 
        process.hltL1fL1sDoubleMu103p5ORDoubleMu125L1Filtered0 + 
        process.HLTL2muonrecoSequenceNoVtx +  
        process.hltL2pfL1sDoubleMu103p5L1f0L2PreFiltered0 + 
        process.hltL2fL1sDoubleMu103p5L1f0L2Filtered10OneMu + 
        process.HLTL3NoFiltersNoVtxmuonrecoSequence +  
        process.hltL3pfL1sDoubleMu103p5L1f0L2pf0ThreeMuL3PreFiltered5 + 
        process.hltL3fL1sDoubleMu103p5L1f0L2f10OneMuL3Filtered15 + 
        process.HLTTrackerMuonSequenceNoVtx + 
        process.hltTripleTrkMuFiltered5NoVtx +
        process.HLTEndSequence 
    )

    process.HLT_TrkMu15_DoubleTrkMu5NoVtx_v1 = cms.Path( 
        process.HLTBeginSequence + 
        process.hltL1sL1DoubleMu103p5ORDoubleMu125 + 
        process.hltPreMu17TrkIsoVVLMu8TrkIsoVVL + 
        process.hltL1fL1sDoubleMu103p5ORDoubleMu125L1Filtered0 + 
        process.HLTL2muonrecoSequenceNoVtx +  ## take from HLT_DoubleMu33NoFiltersNoVtx_v
        process.hltL2pfL1sDoubleMu103p5L1f0L2PreFiltered0 + 
        process.hltL2fL1sDoubleMu103p5L1f0L2Filtered10OneMu + 
        process.HLTL3NoFiltersNoVtxmuonrecoSequence +  ## take from HLT_DoubleMu33NoFiltersNoVtx_v
        process.hltL3pfL1sDoubleMu103p5L1f0L2pf0ThreeMuL3PreFiltered5 + 
        process.hltL3fL1sDoubleMu103p5L1f0L2f10OneMuL3Filtered15 + 
        process.HLTTrackerMuonSequenceNoVtx + 
        process.hltTripleTrkMuFiltered5NoVtx +
        process.hltSingleTrkMuFiltered15NoVtx +
        process.HLTEndSequence 
    )
    return process

def addHLT_TripleMu_12_10_5_onlyL1OldSeed_v1(process):
    process.HLT_TripleMu_12_10_5_onlyL1OldSeed_v1 = cms.Path( 
        process.HLTBeginSequence + 
        process.hltL1sL1TripleMu553 + 
        process.HLTEndSequence 
    )
    return process

def addHLT_TripleMu_12_10_5_onlyL1NewSeed_v1(process):
    process.hltL1sL1TripleMu553NewSeed = process.hltL1sL1TripleMu553.clone(
        L1SeedsLogicalExpression = "L1_TripleMu_5_5_3_HighQ"
    )
    process.HLT_TripleMu_12_10_5_onlyL1NewSeed_v1 = cms.Path( 
        process.HLTBeginSequence + 
        process.hltL1sL1TripleMu553NewSeed + 
        process.HLTEndSequence 
    )
    return process

def customizeOutputModule(process):
    ## remove previous trigger results
#    process.source.inputCommands.append('drop *_*_*_TEST')

    ## drop existing output modules
    if hasattr(process,"AOutput"):
        delattr(process,"AOutput")
    if hasattr(process,"DQMOutput"):
        delattr(process,"DQMOutput")

    ## add custom output module
    process.hltOutputFULL = cms.OutputModule( "PoolOutputModule",
        fileName = cms.untracked.string( "out_hlt.root" ),
        fastCloning = cms.untracked.bool( False ),
        dataset = cms.untracked.PSet(
            dataTier = cms.untracked.string( 'RECO' ),
            filterName = cms.untracked.string( '' )
        ),
        SelectEvents = cms.untracked.PSet(  
            SelectEvents = cms.vstring('*') 
        ),
        outputCommands = cms.untracked.vstring( 'keep *' )
    )
    process.FULLOutput = cms.EndPath( process.hltOutputFULL )
    process.source.fileNames = cms.untracked.vstring(
        #'file:/eos/uscms/store/user/lpcgem/dildick/CMSSW_73/dildick/DarkSUSY_mH_125_mGammaD_0400_ctauExp_0_8TeV_madgraph452_bridge224_LHE_pythia6_RAW/DarkSUSY_mH_125_mGammaD_0400_ctauExp_0_8TeV_madgraph452_bridge224_LHE_pythia6_RECO/ee2b69195f87ad6497ae607e47718adf/out_reco_2_1_IDw.root'
        'file:/eos/uscms/store/user/lpcgem/dildick/CMSSW_73/dildick/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_RAW/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_RECO/ee2b69195f87ad6497ae607e47718adf/out_reco_1_1_XNE.root',
        'file:/eos/uscms/store/user/lpcgem/dildick/CMSSW_73/dildick/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_RAW/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_RECO/ee2b69195f87ad6497ae607e47718adf/out_reco_2_1_DU4.root',
        'file:/eos/uscms/store/user/lpcgem/dildick/CMSSW_73/dildick/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_RAW/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_RECO/ee2b69195f87ad6497ae607e47718adf/out_reco_3_1_E3r.root',
        'file:/eos/uscms/store/user/lpcgem/dildick/CMSSW_73/dildick/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_RAW/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_RECO/ee2b69195f87ad6497ae607e47718adf/out_reco_4_1_7nq.root', 
        'file:/eos/uscms/store/user/lpcgem/dildick/CMSSW_73/dildick/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_RAW/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_RECO/ee2b69195f87ad6497ae607e47718adf/out_reco_5_1_brb.root',
        'file:/eos/uscms/store/user/lpcgem/dildick/CMSSW_73/dildick/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_RAW/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_RECO/ee2b69195f87ad6497ae607e47718adf/out_reco_6_1_8VH.root', 
        'file:/eos/uscms/store/user/lpcgem/dildick/CMSSW_73/dildick/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_RAW/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_RECO/ee2b69195f87ad6497ae607e47718adf/out_reco_7_1_oKs.root', 
        'file:/eos/uscms/store/user/lpcgem/dildick/CMSSW_73/dildick/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_RAW/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_RECO/ee2b69195f87ad6497ae607e47718adf/out_reco_8_1_ryo.root'
        'file:/eos/uscms/store/user/lpcgem/dildick/CMSSW_73/dildick/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_RAW/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_RECO/ee2b69195f87ad6497ae607e47718adf/out_reco_9_1_S4w.root',
        'file:/eos/uscms/store/user/lpcgem/dildick/CMSSW_73/dildick/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_RAW/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_RECO/ee2b69195f87ad6497ae607e47718adf/out_reco_10_1_ZRu.root',
        'file:/eos/uscms/store/user/lpcgem/dildick/CMSSW_73/dildick/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_RAW/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_RECO/ee2b69195f87ad6497ae607e47718adf/out_reco_11_1_nqV.root',  
        #'file:/eos/uscms/store/user/lpcgem/dildick/CMSSW_73/dildick/DarkSUSY_mH_125_mGammaD_2000_ctauExp_5_8TeV_madgraph452_bridge224_LHE_pythia6_RAW/DarkSUSY_mH_125_mGammaD_2000_ctauExp_5_8TeV_madgraph452_bridge224_LHE_pythia6_RECO/ee2b69195f87ad6497ae607e47718adf/out_reco_1_1_9Sf.root',
#        'file:/eos/uscms/store/user/lpcgem/dildick/CMSSW_73/dildick/DarkSUSY_mH_125_mGammaD_2000_ctauExp_5_8TeV_madgraph452_bridge224_LHE_pythia6_RAW/DarkSUSY_mH_125_mGammaD_2000_ctauExp_5_8TeV_madgraph452_bridge224_LHE_pythia6_RECO/ee2b69195f87ad6497ae607e47718adf/out_reco_2_1_VDD.root',
#        'file:/eos/uscms/store/user/lpcgem/dildick/CMSSW_73/dildick/DarkSUSY_mH_125_mGammaD_2000_ctauExp_5_8TeV_madgraph452_bridge224_LHE_pythia6_RAW/DarkSUSY_mH_125_mGammaD_2000_ctauExp_5_8TeV_madgraph452_bridge224_LHE_pythia6_RECO/ee2b69195f87ad6497ae607e47718adf/out_reco_3_1_nZ8.root',
#        'file:/eos/uscms/store/user/lpcgem/dildick/CMSSW_73/dildick/DarkSUSY_mH_125_mGammaD_2000_ctauExp_5_8TeV_madgraph452_bridge224_LHE_pythia6_RAW/DarkSUSY_mH_125_mGammaD_2000_ctauExp_5_8TeV_madgraph452_bridge224_LHE_pythia6_RECO/ee2b69195f87ad6497ae607e47718adf/out_reco_3_1_nZ8.root',
    )
    return process

def customizeL1SeedhltL1sL1TripleMu553(process):
    ## Change the seed L1_TripleMu_5_5_3 to L1_TripleMu_5_5_3_HighQ in hltL1sL1TripleMu553
    process.hltL1sL1TripleMu553.L1SeedsLogicalExpression = "L1_TripleMu_5_5_3_HighQ"
    return process

def customizeHLT_TrkMu15_DoubleTrkMu5_v1(process):
    process = customizeL1SeedhltL1sL1TripleMu553(process)
    process = addHLT_TripleMu_12_10_5_onlyL1NewSeed_v1(process)
    process = addHLT_TrkMu15_DoubleTrkMu5_v1(process)
    process = addHLT_Mu15_DoubleMu5NoVtx_v1(process)
    process = addHLT_TrkMu15_DoubleTrkMu5NoVtx_v1(process) #-- need to fix trackrecosequence first
    process = addHLT_Mu17_Mu8_v1_NoDz(process)
    process = addHLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v1_NoIso(process)
    process = addHLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v1_NoIso(process)
    return process

