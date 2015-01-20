## Customization for HLT_TrkMu15_DoubleTrkMu5_v1

import FWCore.ParameterSet.Config as cms

hltL3pfL1sDoubleMu103p5L1f0L2pf0L3PreFiltered5 = cms.EDFilter( "HLTMuonL3PreFilter",
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
hltTriTrkMu5Filtered = cms.EDFilter("HLTMuonTrkFilter",
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
hltSingleTrkMu15Filtered = cms.EDFilter("HLTMuonTrkFilter",
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

def add_HLT_TrkMu15_DoubleTrkMu5_v1(process):

    """
    Step 1: Start from HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v1; rename to HLT_TrkMu15_DoubleTrkMu5_v1
    Step 2: Remove the isolation sequence
    Step 3: Add the TrkMu reconstruction sequence
    Step 4: Add TriTrkMu pt5 filter (HLTMuonTrkFilter)
    Step 5: Add SingleTrkMu15 filter (HLTMuonTrkFilter)
    Step 6: Replace the L2 and L3 RECO sequence by variants that do not have dxy cut
    Step 7: Change L3 prefilter and filter
    """
    process.hltL3pfL1sDoubleMu103p5L1f0L2pf0L3PreFiltered5 = hltL3pfL1sDoubleMu103p5L1f0L2pf0L3PreFiltered5
    process.hltL3fL1sDoubleMu103p5L1f0L2f10OneMuL3Filtered15 = hltL3fL1sDoubleMu103p5L1f0L2f10OneMuL3Filtered15
    process.hltTriTrkMu5Filtered = hltTriTrkMu5Filtered
    process.hltSingleTrkMu15Filtered = hltSingleTrkMu15Filtered

    process.HLT_TrkMu15_DoubleTrkMu5_v1 = cms.Path( 
        process.HLTBeginSequence + 
        process.hltL1sL1DoubleMu103p5ORDoubleMu125 + 
        process.hltPreMu17TrkIsoVVLMu8TrkIsoVVL + 
        process.hltL1fL1sDoubleMu103p5ORDoubleMu125L1Filtered0 + 
        process.HLTL2muonrecoSequenceNoVtx + 
        process.hltL2pfL1sDoubleMu103p5L1f0L2PreFiltered0 + 
        process.hltL2fL1sDoubleMu103p5L1f0L2Filtered10OneMu + 
        process.HLTL3NoFiltersNoVtxmuonrecoSequence + 
        process.hltL3pfL1sDoubleMu103p5L1f0L2pf0L3PreFiltered5 + 
        process.hltL3fL1sDoubleMu103p5L1f0L2f10OneMuL3Filtered15 + 
        process.HLTTrackerMuonSequence +
        process.hltTriTrkMu5Filtered +
        process.hltSingleTrkMu15Filtered +
        process.HLTEndSequence 
    )
    return process

def addFullOutputModule(process):
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
    return process

def changeL1SeedhltL1sL1TripleMu553(process):
    ## Change the seed L1_TripleMu_5_5_3 to L1_TripleMu_5_5_3_HighQ in hltL1sL1TripleMu553
    process.hltL1sL1TripleMu553.L1SeedsLogicalExpression = "L1_TripleMu_5_5_3_HighQ"
    return process

