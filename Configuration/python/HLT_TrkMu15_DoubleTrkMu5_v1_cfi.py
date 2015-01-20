# /dev/CMSSW_7_3_0/GRun/V25 (CMSSW_7_3_0_HLT1)

import FWCore.ParameterSet.Config as cms

hltL3pfL1sDoubleMu103p5L1f0L2pf0L3PreFiltered5 = cms.EDFilter( "HLTMuonL3PreFilter",
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

## custom trigger
## 2 L1 muons with pt 10-3.5 or 12-5
## 2 L3 muons with pt 15-5 or 15-7
## TrkMu:
##    3 mu with pt>5
##    1 mu with pt>17

"""
Step 1: Start from HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v1; rename to HLT_TrkMu15_DoubleTrkMu5_v1
Step 2: Remove the isolation sequence
Step 3: Add the TrkMu reconstruction sequence
Step 4: Add TriTrkMu pt5 filter (HLTMuonTrkFilter)
Step 5: Add SingleTrkMu15 filter (HLTMuonTrkFilter)
"""
process.HLT_TrkMu15_DoubleTrkMu5_v1 = cms.Path( 
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
    process.HLTTrackerMuonSequence +
    process.hltTriTrkMu5Filtered +
    process.hltSingleTrkMu15Filtered +
    process.HLTEndSequence 
)

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


## Change the seed L1_TripleMu_5_5_3 to L1_TripleMu_5_5_3_HighQ in hltL1sL1TripleMu553

