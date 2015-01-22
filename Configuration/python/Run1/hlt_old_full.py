import FWCore.ParameterSet.Config as cms

process = cms.Process("HLT")

process.source = cms.Source("PoolSource",
    inputCommands = cms.untracked.vstring('keep *'),
    secondaryFileNames = cms.untracked.vstring(),
    fileNames = cms.untracked.vstring('file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_1500_ctauExp_5_8TeV_madgraph452_bridge224_LHE_pythia6_RAW/DarkSUSY_mH_125_mGammaD_1500_ctauExp_5_8TeV_madgraph452_bridge224_LHE_pythia6_RAW/d7be294dffab161f3c0e82b16a790458/out_raw_1_1_UMU.root')
)
process.hltCsc2DRecHits = cms.EDProducer("CSCRecHitDProducer",
    XTasymmetry_ME1b = cms.double(0.0),
    XTasymmetry_ME1a = cms.double(0.0),
    XTasymmetry_ME41 = cms.double(0.0),
    ConstSyst_ME41 = cms.double(0.0),
    CSCStripxtalksOffset = cms.double(0.03),
    CSCUseCalibrations = cms.bool(True),
    CSCUseTimingCorrections = cms.bool(True),
    CSCNoOfTimeBinsForDynamicPedestal = cms.int32(2),
    XTasymmetry_ME22 = cms.double(0.0),
    UseFivePoleFit = cms.bool(True),
    XTasymmetry_ME21 = cms.double(0.0),
    ConstSyst_ME21 = cms.double(0.0),
    CSCDebug = cms.untracked.bool(False),
    XTasymmetry_ME32 = cms.double(0.0),
    ConstSyst_ME22 = cms.double(0.0),
    CSCUseGasGainCorrections = cms.bool(False),
    XTasymmetry_ME31 = cms.double(0.0),
    ConstSyst_ME1a = cms.double(0.022),
    readBadChambers = cms.bool(True),
    NoiseLevel_ME13 = cms.double(8.0),
    NoiseLevel_ME12 = cms.double(9.0),
    NoiseLevel_ME32 = cms.double(9.0),
    NoiseLevel_ME31 = cms.double(9.0),
    CSCStripClusterChargeCut = cms.double(25.0),
    ConstSyst_ME1b = cms.double(0.007),
    CSCStripClusterSize = cms.untracked.int32(3),
    CSCStripPeakThreshold = cms.double(10.0),
    readBadChannels = cms.bool(True),
    UseParabolaFit = cms.bool(False),
    XTasymmetry_ME13 = cms.double(0.0),
    XTasymmetry_ME12 = cms.double(0.0),
    wireDigiTag = cms.InputTag("hltMuonCSCDigis","MuonCSCWireDigi"),
    ConstSyst_ME12 = cms.double(0.0),
    ConstSyst_ME13 = cms.double(0.0),
    ConstSyst_ME32 = cms.double(0.0),
    ConstSyst_ME31 = cms.double(0.0),
    UseAverageTime = cms.bool(False),
    NoiseLevel_ME1a = cms.double(7.0),
    NoiseLevel_ME1b = cms.double(8.0),
    CSCWireClusterDeltaT = cms.int32(1),
    CSCUseStaticPedestals = cms.bool(False),
    stripDigiTag = cms.InputTag("hltMuonCSCDigis","MuonCSCStripDigi"),
    CSCstripWireDeltaTime = cms.int32(8),
    NoiseLevel_ME21 = cms.double(9.0),
    NoiseLevel_ME22 = cms.double(9.0),
    NoiseLevel_ME41 = cms.double(9.0)
)


process.hltCscSegments = cms.EDProducer("CSCSegmentProducer",
    inputObjects = cms.InputTag("hltCsc2DRecHits"),
    algo_type = cms.int32(1),
    algo_psets = cms.VPSet(cms.PSet(
        chamber_types = cms.vstring('ME1/a', 
            'ME1/b', 
            'ME1/2', 
            'ME1/3', 
            'ME2/1', 
            'ME2/2', 
            'ME3/1', 
            'ME3/2', 
            'ME4/1', 
            'ME4/2'),
        algo_name = cms.string('CSCSegAlgoST'),
        algo_psets = cms.VPSet(cms.PSet(
            maxRatioResidualPrune = cms.double(3.0),
            yweightPenalty = cms.double(1.5),
            maxRecHitsInCluster = cms.int32(20),
            dPhiFineMax = cms.double(0.025),
            preClusteringUseChaining = cms.bool(True),
            ForceCovariance = cms.bool(False),
            hitDropLimit6Hits = cms.double(0.3333),
            NormChi2Cut2D = cms.double(20.0),
            BPMinImprovement = cms.double(10000.0),
            Covariance = cms.double(0.0),
            tanPhiMax = cms.double(0.5),
            onlyBestSegment = cms.bool(False),
            SeedBig = cms.double(0.0015),
            dRPhiFineMax = cms.double(8.0),
            SeedSmall = cms.double(0.0002),
            curvePenalty = cms.double(2.0),
            dXclusBoxMax = cms.double(4.0),
            BrutePruning = cms.bool(True),
            tanThetaMax = cms.double(1.2),
            CorrectTheErrors = cms.bool(True),
            hitDropLimit4Hits = cms.double(0.6),
            useShowering = cms.bool(False),
            CSCDebug = cms.untracked.bool(False),
            curvePenaltyThreshold = cms.double(0.85),
            NormChi2Cut3D = cms.double(10.0),
            minHitsPerSegment = cms.int32(3),
            ForceCovarianceAll = cms.bool(False),
            yweightPenaltyThreshold = cms.double(1.0),
            prePrunLimit = cms.double(3.17),
            hitDropLimit5Hits = cms.double(0.8),
            preClustering = cms.bool(True),
            prePrun = cms.bool(True),
            maxDPhi = cms.double(999.0),
            maxDTheta = cms.double(999.0),
            Pruning = cms.bool(True),
            dYclusBoxMax = cms.double(8.0)
        ), 
            cms.PSet(
                maxRatioResidualPrune = cms.double(3.0),
                yweightPenalty = cms.double(1.5),
                maxRecHitsInCluster = cms.int32(24),
                dPhiFineMax = cms.double(0.025),
                preClusteringUseChaining = cms.bool(True),
                ForceCovariance = cms.bool(False),
                hitDropLimit6Hits = cms.double(0.3333),
                NormChi2Cut2D = cms.double(20.0),
                BPMinImprovement = cms.double(10000.0),
                Covariance = cms.double(0.0),
                tanPhiMax = cms.double(0.5),
                onlyBestSegment = cms.bool(False),
                SeedBig = cms.double(0.0015),
                dRPhiFineMax = cms.double(8.0),
                SeedSmall = cms.double(0.0002),
                curvePenalty = cms.double(2.0),
                dXclusBoxMax = cms.double(4.0),
                BrutePruning = cms.bool(True),
                tanThetaMax = cms.double(1.2),
                CorrectTheErrors = cms.bool(True),
                hitDropLimit4Hits = cms.double(0.6),
                useShowering = cms.bool(False),
                CSCDebug = cms.untracked.bool(False),
                curvePenaltyThreshold = cms.double(0.85),
                NormChi2Cut3D = cms.double(10.0),
                minHitsPerSegment = cms.int32(3),
                ForceCovarianceAll = cms.bool(False),
                yweightPenaltyThreshold = cms.double(1.0),
                prePrunLimit = cms.double(3.17),
                hitDropLimit5Hits = cms.double(0.8),
                preClustering = cms.bool(True),
                prePrun = cms.bool(True),
                maxDPhi = cms.double(999.0),
                maxDTheta = cms.double(999.0),
                Pruning = cms.bool(True),
                dYclusBoxMax = cms.double(8.0)
            )),
        parameters_per_chamber_type = cms.vint32(2, 1, 1, 1, 1, 
            1, 1, 1, 1, 1)
    ))
)


process.hltDt1DRecHits = cms.EDProducer("DTRecHitProducer",
    debug = cms.untracked.bool(False),
    recAlgoConfig = cms.PSet(
        tTrigMode = cms.string('DTTTrigSyncFromDB'),
        minTime = cms.double(-3.0),
        stepTwoFromDigi = cms.bool(False),
        doVdriftCorr = cms.bool(False),
        debug = cms.untracked.bool(False),
        tTrigModeConfig = cms.PSet(
            vPropWire = cms.double(24.4),
            doTOFCorrection = cms.bool(True),
            tofCorrType = cms.int32(0),
            wirePropCorrType = cms.int32(0),
            tTrigLabel = cms.string(''),
            doWirePropCorrection = cms.bool(True),
            doT0Correction = cms.bool(True),
            debug = cms.untracked.bool(False)
        ),
        maxTime = cms.double(420.0)
    ),
    dtDigiLabel = cms.InputTag("hltMuonDTDigis"),
    recAlgo = cms.string('DTLinearDriftFromDBAlgo')
)


process.hltDt4DSegments = cms.EDProducer("DTRecSegment4DProducer",
    debug = cms.untracked.bool(False),
    Reco4DAlgoName = cms.string('DTCombinatorialPatternReco4D'),
    recHits2DLabel = cms.InputTag("dt2DSegments"),
    recHits1DLabel = cms.InputTag("hltDt1DRecHits"),
    Reco4DAlgoConfig = cms.PSet(
        segmCleanerMode = cms.int32(2),
        perform_delta_rejecting = cms.bool(False),
        recAlgo = cms.string('DTLinearDriftFromDBAlgo'),
        nSharedHitsMax = cms.int32(2),
        hit_afterT0_resolution = cms.double(0.03),
        Reco2DAlgoConfig = cms.PSet(
            segmCleanerMode = cms.int32(2),
            perform_delta_rejecting = cms.bool(False),
            recAlgo = cms.string('DTLinearDriftFromDBAlgo'),
            nSharedHitsMax = cms.int32(2),
            AlphaMaxPhi = cms.double(1.0),
            hit_afterT0_resolution = cms.double(0.03),
            MaxAllowedHits = cms.uint32(50),
            performT0_vdriftSegCorrection = cms.bool(False),
            AlphaMaxTheta = cms.double(0.9),
            debug = cms.untracked.bool(False),
            recAlgoConfig = cms.PSet(
                tTrigMode = cms.string('DTTTrigSyncFromDB'),
                minTime = cms.double(-3.0),
                stepTwoFromDigi = cms.bool(False),
                doVdriftCorr = cms.bool(False),
                debug = cms.untracked.bool(False),
                tTrigModeConfig = cms.PSet(
                    vPropWire = cms.double(24.4),
                    doTOFCorrection = cms.bool(True),
                    tofCorrType = cms.int32(0),
                    wirePropCorrType = cms.int32(0),
                    tTrigLabel = cms.string(''),
                    doWirePropCorrection = cms.bool(True),
                    doT0Correction = cms.bool(True),
                    debug = cms.untracked.bool(False)
                ),
                maxTime = cms.double(420.0)
            ),
            nUnSharedHitsMin = cms.int32(2),
            performT0SegCorrection = cms.bool(False)
        ),
        performT0_vdriftSegCorrection = cms.bool(False),
        debug = cms.untracked.bool(False),
        recAlgoConfig = cms.PSet(
            tTrigMode = cms.string('DTTTrigSyncFromDB'),
            minTime = cms.double(-3.0),
            stepTwoFromDigi = cms.bool(False),
            doVdriftCorr = cms.bool(False),
            debug = cms.untracked.bool(False),
            tTrigModeConfig = cms.PSet(
                vPropWire = cms.double(24.4),
                doTOFCorrection = cms.bool(True),
                tofCorrType = cms.int32(0),
                wirePropCorrType = cms.int32(0),
                tTrigLabel = cms.string(''),
                doWirePropCorrection = cms.bool(True),
                doT0Correction = cms.bool(True),
                debug = cms.untracked.bool(False)
            ),
            maxTime = cms.double(420.0)
        ),
        nUnSharedHitsMin = cms.int32(2),
        AllDTRecHits = cms.bool(True),
        performT0SegCorrection = cms.bool(False),
        Reco2DAlgoName = cms.string('DTCombinatorialPatternReco')
    )
)


process.hltGctDigis = cms.EDProducer("GctRawToDigi",
    unpackSharedRegions = cms.bool(False),
    numberOfGctSamplesToUnpack = cms.uint32(1),
    verbose = cms.untracked.bool(False),
    numberOfRctSamplesToUnpack = cms.uint32(1),
    inputLabel = cms.InputTag("rawDataCollector"),
    unpackerVersion = cms.uint32(0),
    gctFedId = cms.untracked.int32(745),
    hltMode = cms.bool(True)
)


process.hltGtDigis = cms.EDProducer("L1GlobalTriggerRawToDigi",
    DaqGtFedId = cms.untracked.int32(813),
    DaqGtInputTag = cms.InputTag("rawDataCollector"),
    UnpackBxInEvent = cms.int32(5),
    ActiveBoardsMask = cms.uint32(65535)
)


process.hltL1GtObjectMap = cms.EDProducer("L1GlobalTrigger",
    TechnicalTriggersUnprescaled = cms.bool(True),
    ProduceL1GtObjectMapRecord = cms.bool(True),
    AlgorithmTriggersUnmasked = cms.bool(False),
    EmulateBxInEvent = cms.int32(1),
    AlgorithmTriggersUnprescaled = cms.bool(True),
    ProduceL1GtDaqRecord = cms.bool(False),
    ReadTechnicalTriggerRecords = cms.bool(True),
    RecordLength = cms.vint32(3, 0),
    TechnicalTriggersUnmasked = cms.bool(False),
    ProduceL1GtEvmRecord = cms.bool(False),
    GmtInputTag = cms.InputTag("hltGtDigis"),
    TechnicalTriggersVetoUnmasked = cms.bool(True),
    AlternativeNrBxBoardEvm = cms.uint32(0),
    TechnicalTriggersInputTags = cms.VInputTag("simBscDigis"),
    CastorInputTag = cms.InputTag("castorL1Digis"),
    GctInputTag = cms.InputTag("hltGctDigis"),
    AlternativeNrBxBoardDaq = cms.uint32(0),
    WritePsbL1GtDaqRecord = cms.bool(False),
    BstLengthBytes = cms.int32(-1)
)


process.hltL1extraParticles = cms.EDProducer("L1ExtraParticlesProd",
    centralBxOnly = cms.bool(True),
    muonSource = cms.InputTag("hltGtDigis"),
    etTotalSource = cms.InputTag("hltGctDigis"),
    etHadSource = cms.InputTag("hltGctDigis"),
    centralJetSource = cms.InputTag("hltGctDigis","cenJets"),
    etMissSource = cms.InputTag("hltGctDigis"),
    hfRingEtSumsSource = cms.InputTag("hltGctDigis"),
    produceMuonParticles = cms.bool(True),
    forwardJetSource = cms.InputTag("hltGctDigis","forJets"),
    ignoreHtMiss = cms.bool(False),
    htMissSource = cms.InputTag("hltGctDigis"),
    produceCaloParticles = cms.bool(True),
    tauJetSource = cms.InputTag("hltGctDigis","tauJets"),
    isolatedEmSource = cms.InputTag("hltGctDigis","isoEm"),
    nonIsolatedEmSource = cms.InputTag("hltGctDigis","nonIsoEm"),
    hfRingBitCountsSource = cms.InputTag("hltGctDigis")
)


process.hltL2MuonCandidates = cms.EDProducer("L2MuonCandidateProducer",
    InputObjects = cms.InputTag("hltL2Muons","UpdatedAtVtx")
)


process.hltL2MuonSeeds = cms.EDProducer("L2MuonSeedGenerator",
    L1MinPt = cms.double(0.0),
    InputObjects = cms.InputTag("hltL1extraParticles"),
    L1MaxEta = cms.double(2.5),
    OfflineSeedLabel = cms.untracked.InputTag("hltL2OfflineMuonSeeds"),
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny'),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    L1MinQuality = cms.uint32(1),
    GMTReadoutCollection = cms.InputTag("hltGtDigis"),
    UseOfflineSeed = cms.untracked.bool(True),
    Propagator = cms.string('SteppingHelixPropagatorAny')
)


process.hltL2Muons = cms.EDProducer("L2MuonProducer",
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('hltESPFastSteppingHelixPropagatorAny', 
            'hltESPFastSteppingHelixPropagatorOpposite'),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    InputObjects = cms.InputTag("hltL2MuonSeeds"),
    SeedTransformerParameters = cms.PSet(
        Fitter = cms.string('hltESPKFFittingSmootherForL2Muon'),
        MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
        Propagator = cms.string('hltESPFastSteppingHelixPropagatorAny'),
        UseSubRecHits = cms.bool(False),
        NMinRecHits = cms.uint32(2),
        RescaleError = cms.double(100.0)
    ),
    L2TrajBuilderParameters = cms.PSet(
        DoRefit = cms.bool(False),
        SeedPropagator = cms.string('hltESPFastSteppingHelixPropagatorAny'),
        FilterParameters = cms.PSet(
            NumberOfSigma = cms.double(3.0),
            FitDirection = cms.string('insideOut'),
            DTRecSegmentLabel = cms.InputTag("hltDt4DSegments"),
            MaxChi2 = cms.double(1000.0),
            MuonTrajectoryUpdatorParameters = cms.PSet(
                MaxChi2 = cms.double(25.0),
                RescaleErrorFactor = cms.double(100.0),
                Granularity = cms.int32(0),
                ExcludeRPCFromFit = cms.bool(False),
                UseInvalidHits = cms.bool(True),
                RescaleError = cms.bool(False)
            ),
            EnableRPCMeasurement = cms.bool(True),
            CSCRecSegmentLabel = cms.InputTag("hltCscSegments"),
            EnableDTMeasurement = cms.bool(True),
            RPCRecSegmentLabel = cms.InputTag("hltRpcRecHits"),
            Propagator = cms.string('hltESPFastSteppingHelixPropagatorAny'),
            EnableCSCMeasurement = cms.bool(True)
        ),
        NavigationType = cms.string('Standard'),
        SeedTransformerParameters = cms.PSet(
            Fitter = cms.string('hltESPKFFittingSmootherForL2Muon'),
            MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
            Propagator = cms.string('hltESPFastSteppingHelixPropagatorAny'),
            UseSubRecHits = cms.bool(False),
            NMinRecHits = cms.uint32(2),
            RescaleError = cms.double(100.0)
        ),
        DoBackwardFilter = cms.bool(True),
        SeedPosition = cms.string('in'),
        BWFilterParameters = cms.PSet(
            NumberOfSigma = cms.double(3.0),
            CSCRecSegmentLabel = cms.InputTag("hltCscSegments"),
            FitDirection = cms.string('outsideIn'),
            DTRecSegmentLabel = cms.InputTag("hltDt4DSegments"),
            MaxChi2 = cms.double(100.0),
            MuonTrajectoryUpdatorParameters = cms.PSet(
                MaxChi2 = cms.double(25.0),
                RescaleErrorFactor = cms.double(100.0),
                Granularity = cms.int32(2),
                ExcludeRPCFromFit = cms.bool(False),
                UseInvalidHits = cms.bool(True),
                RescaleError = cms.bool(False)
            ),
            EnableRPCMeasurement = cms.bool(True),
            BWSeedType = cms.string('fromGenerator'),
            EnableDTMeasurement = cms.bool(True),
            RPCRecSegmentLabel = cms.InputTag("hltRpcRecHits"),
            Propagator = cms.string('hltESPFastSteppingHelixPropagatorAny'),
            EnableCSCMeasurement = cms.bool(True)
        ),
        DoSeedRefit = cms.bool(False)
    ),
    DoSeedRefit = cms.bool(False),
    TrackLoaderParameters = cms.PSet(
        Smoother = cms.string('hltESPKFTrajectorySmootherForMuonTrackLoader'),
        DoSmoothing = cms.bool(False),
        beamSpot = cms.InputTag("hltOnlineBeamSpot"),
        MuonUpdatorAtVertexParameters = cms.PSet(
            MaxChi2 = cms.double(1000000.0),
            BeamSpotPosition = cms.vdouble(0.0, 0.0, 0.0),
            Propagator = cms.string('hltESPFastSteppingHelixPropagatorOpposite'),
            BeamSpotPositionErrors = cms.vdouble(0.1, 0.1, 5.3)
        ),
        VertexConstraint = cms.bool(True)
    )
)


process.hltL2OfflineMuonSeeds = cms.EDProducer("MuonSeedGenerator",
    SMB_21 = cms.vdouble(1.043, -0.124, 0.0, 0.183, 0.0, 
        0.0),
    SMB_20 = cms.vdouble(1.011, -0.052, 0.0, 0.188, 0.0, 
        0.0),
    SMB_22 = cms.vdouble(1.474, -0.758, 0.0, 0.185, 0.0, 
        0.0),
    OL_2213 = cms.vdouble(0.117, 0.0, 0.0, 0.044, 0.0, 
        0.0),
    SME_11 = cms.vdouble(3.295, -1.527, 0.112, 0.378, 0.02, 
        0.0),
    SME_13 = cms.vdouble(-1.286, 1.711, 0.0, 0.356, 0.0, 
        0.0),
    SME_12 = cms.vdouble(0.102, 0.599, 0.0, 0.38, 0.0, 
        0.0),
    DT_34_2_scale = cms.vdouble(-11.901897, 0.0),
    OL_1213_0_scale = cms.vdouble(-4.488158, 0.0),
    OL_1222_0_scale = cms.vdouble(-5.810449, 0.0),
    DT_13 = cms.vdouble(0.315, 0.068, -0.127, 0.051, -0.002, 
        0.0),
    DT_12 = cms.vdouble(0.183, 0.054, -0.087, 0.028, 0.002, 
        0.0),
    DT_14 = cms.vdouble(0.359, 0.052, -0.107, 0.072, -0.004, 
        0.0),
    CSC_13_3_scale = cms.vdouble(-1.701268, 0.0),
    CSC_23 = cms.vdouble(-0.081, 0.113, -0.029, 0.015, 0.008, 
        0.0),
    CSC_24 = cms.vdouble(0.004, 0.021, -0.002, 0.053, 0.0, 
        0.0),
    OL_2222 = cms.vdouble(0.107, 0.0, 0.0, 0.04, 0.0, 
        0.0),
    DT_14_2_scale = cms.vdouble(-4.808546, 0.0),
    SMB_10 = cms.vdouble(1.387, -0.038, 0.0, 0.19, 0.0, 
        0.0),
    SMB_11 = cms.vdouble(1.247, 0.72, -0.802, 0.229, -0.075, 
        0.0),
    SMB_12 = cms.vdouble(2.128, -0.956, 0.0, 0.199, 0.0, 
        0.0),
    SME_21 = cms.vdouble(-0.529, 1.194, -0.358, 0.472, 0.086, 
        0.0),
    SME_22 = cms.vdouble(-1.207, 1.491, -0.251, 0.189, 0.243, 
        0.0),
    DT_13_2_scale = cms.vdouble(-4.257687, 0.0),
    CSC_34 = cms.vdouble(0.062, -0.067, 0.019, 0.021, 0.003, 
        0.0),
    SME_22_0_scale = cms.vdouble(-3.457901, 0.0),
    DT_24_1_scale = cms.vdouble(-7.490909, 0.0),
    OL_1232_0_scale = cms.vdouble(-5.964634, 0.0),
    SMB_32 = cms.vdouble(0.67, -0.327, 0.0, 0.22, 0.0, 
        0.0),
    SME_13_0_scale = cms.vdouble(0.104905, 0.0),
    SMB_22_0_scale = cms.vdouble(1.346681, 0.0),
    DT_24_2_scale = cms.vdouble(-6.63094, 0.0),
    DT_34 = cms.vdouble(0.044, 0.004, -0.013, 0.029, 0.003, 
        0.0),
    SME_32 = cms.vdouble(-0.901, 1.333, -0.47, 0.41, 0.073, 
        0.0),
    SME_31 = cms.vdouble(-1.594, 1.482, -0.317, 0.487, 0.097, 
        0.0),
    CSC_13_2_scale = cms.vdouble(-6.077936, 0.0),
    crackEtas = cms.vdouble(0.2, 1.6, 1.7),
    SME_11_0_scale = cms.vdouble(1.325085, 0.0),
    SMB_20_0_scale = cms.vdouble(1.486168, 0.0),
    DT_13_1_scale = cms.vdouble(-4.520923, 0.0),
    CSC_24_1_scale = cms.vdouble(-6.055701, 0.0),
    CSC_01_1_scale = cms.vdouble(-1.915329, 0.0),
    DT_23 = cms.vdouble(0.13, 0.023, -0.057, 0.028, 0.004, 
        0.0),
    DT_24 = cms.vdouble(0.176, 0.014, -0.051, 0.051, 0.003, 
        0.0),
    SMB_12_0_scale = cms.vdouble(2.283221, 0.0),
    CSC_23_1_scale = cms.vdouble(-19.084285, 0.0),
    SME_42 = cms.vdouble(-0.003, 0.005, 0.005, 0.608, 0.076, 
        0.0),
    SME_41 = cms.vdouble(-0.003, 0.005, 0.005, 0.608, 0.076, 
        0.0),
    CSC_12_2_scale = cms.vdouble(-1.63622, 0.0),
    DT_34_1_scale = cms.vdouble(-13.783765, 0.0),
    CSC_34_1_scale = cms.vdouble(-11.520507, 0.0),
    OL_2213_0_scale = cms.vdouble(-7.239789, 0.0),
    SMB_32_0_scale = cms.vdouble(-3.054156, 0.0),
    CSC_12_3_scale = cms.vdouble(-1.63622, 0.0),
    SME_21_0_scale = cms.vdouble(-0.040862, 0.0),
    OL_1232 = cms.vdouble(0.184, 0.0, 0.0, 0.066, 0.0, 
        0.0),
    DTRecSegmentLabel = cms.InputTag("hltDt4DSegments"),
    SMB_10_0_scale = cms.vdouble(2.448566, 0.0),
    EnableDTMeasurement = cms.bool(True),
    CSCRecSegmentLabel = cms.InputTag("hltCscSegments"),
    CSC_23_2_scale = cms.vdouble(-6.079917, 0.0),
    scaleDT = cms.bool(True),
    DT_12_2_scale = cms.vdouble(-3.518165, 0.0),
    OL_1222 = cms.vdouble(0.848, -0.591, 0.0, 0.062, 0.0, 
        0.0),
    SMB_30_0_scale = cms.vdouble(-3.629838, 0.0),
    CSC_12_1_scale = cms.vdouble(-6.434242, 0.0),
    OL_1213 = cms.vdouble(0.96, -0.737, 0.0, 0.052, 0.0, 
        0.0),
    CSC_02 = cms.vdouble(0.612, -0.207, 0.0, 0.067, -0.001, 
        0.0),
    CSC_03 = cms.vdouble(0.787, -0.338, 0.029, 0.101, -0.008, 
        0.0),
    CSC_01 = cms.vdouble(0.166, 0.0, 0.0, 0.031, 0.0, 
        0.0),
    DT_23_1_scale = cms.vdouble(-5.320346, 0.0),
    SMB_30 = cms.vdouble(0.505, -0.022, 0.0, 0.215, 0.0, 
        0.0),
    SMB_31 = cms.vdouble(0.549, -0.145, 0.0, 0.207, 0.0, 
        0.0),
    crackWindow = cms.double(0.04),
    CSC_14_3_scale = cms.vdouble(-1.969563, 0.0),
    SMB_31_0_scale = cms.vdouble(-3.323768, 0.0),
    DT_12_1_scale = cms.vdouble(-3.692398, 0.0),
    SMB_21_0_scale = cms.vdouble(1.58384, 0.0),
    DT_23_2_scale = cms.vdouble(-5.117625, 0.0),
    SME_12_0_scale = cms.vdouble(2.279181, 0.0),
    DT_14_1_scale = cms.vdouble(-5.644816, 0.0),
    beamSpotTag = cms.InputTag("hltOnlineBeamSpot"),
    SMB_11_0_scale = cms.vdouble(2.56363, 0.0),
    CSC_13 = cms.vdouble(0.901, -1.302, 0.533, 0.045, 0.005, 
        0.0),
    CSC_14 = cms.vdouble(0.606, -0.181, -0.002, 0.111, -0.003, 
        0.0),
    OL_2222_0_scale = cms.vdouble(-7.667231, 0.0),
    EnableCSCMeasurement = cms.bool(True),
    CSC_12 = cms.vdouble(-0.161, 0.254, -0.047, 0.042, -0.007, 
        0.0)
)


process.hltL3MuonCandidates = cms.EDProducer("L3MuonCandidateProducer",
    InputLinksObjects = cms.InputTag("hltL3MuonsLinksCombination"),
    InputObjects = cms.InputTag("hltL3Muons"),
    MuonPtOption = cms.string('Tracker')
)


process.hltL3Muons = cms.EDProducer("L3TrackCombiner",
    labels = cms.VInputTag("hltL3MuonsOIState", "hltL3MuonsOIHit", "hltL3MuonsIOHit")
)


process.hltL3MuonsIOHit = cms.EDProducer("L3MuonProducer",
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('hltESPSmartPropagatorAny', 
            'SteppingHelixPropagatorAny', 
            'hltESPSmartPropagator', 
            'hltESPSteppingHelixPropagatorOpposite'),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    L3TrajBuilderParameters = cms.PSet(
        ScaleTECyFactor = cms.double(-1.0),
        GlbRefitterParameters = cms.PSet(
            DoPredictionsOnly = cms.bool(False),
            TrackerSkipSection = cms.int32(-1),
            Chi2CutCSC = cms.double(150.0),
            HitThreshold = cms.int32(1),
            MuonHitsOption = cms.int32(1),
            Chi2CutRPC = cms.double(1.0),
            Fitter = cms.string('hltESPL3MuKFTrajectoryFitter'),
            DTRecSegmentLabel = cms.InputTag("hltDt4DSegments"),
            TrackerRecHitBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
            MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
            RefitDirection = cms.string('insideOut'),
            CSCRecSegmentLabel = cms.InputTag("hltCscSegments"),
            DYTthrs = cms.vint32(30, 15),
            PropDirForCosmics = cms.bool(False),
            Chi2CutDT = cms.double(10.0),
            RefitRPCHits = cms.bool(True),
            SkipStation = cms.int32(-1),
            Propagator = cms.string('hltESPSmartPropagatorAny'),
            TrackerSkipSystem = cms.int32(-1)
        ),
        ScaleTECxFactor = cms.double(-1.0),
        TrackerRecHitBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
        MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
        MuonTrackingRegionBuilder = cms.PSet(
            EtaR_UpperLimit_Par1 = cms.double(0.25),
            DeltaR = cms.double(0.2),
            beamSpot = cms.InputTag("hltOnlineBeamSpot"),
            OnDemand = cms.double(-1.0),
            vertexCollection = cms.InputTag("pixelVertices"),
            Rescale_phi = cms.double(3.0),
            Eta_fixed = cms.double(0.2),
            DeltaZ_Region = cms.double(15.9),
            Rescale_eta = cms.double(3.0),
            PhiR_UpperLimit_Par2 = cms.double(0.2),
            Eta_min = cms.double(0.05),
            Phi_fixed = cms.double(0.2),
            Phi_min = cms.double(0.05),
            EscapePt = cms.double(1.5),
            UseFixedRegion = cms.bool(False),
            PhiR_UpperLimit_Par1 = cms.double(0.6),
            EtaR_UpperLimit_Par2 = cms.double(0.15),
            MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
            UseVertex = cms.bool(False),
            Rescale_Dz = cms.double(3.0)
        ),
        RefitRPCHits = cms.bool(True),
        PCut = cms.double(2.5),
        TrackTransformer = cms.PSet(
            DoPredictionsOnly = cms.bool(False),
            Fitter = cms.string('hltESPL3MuKFTrajectoryFitter'),
            TrackerRecHitBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
            Smoother = cms.string('hltESPKFTrajectorySmootherForMuonTrackLoader'),
            MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
            RefitDirection = cms.string('insideOut'),
            RefitRPCHits = cms.bool(True),
            Propagator = cms.string('hltESPSmartPropagatorAny')
        ),
        GlobalMuonTrackMatcher = cms.PSet(
            Pt_threshold1 = cms.double(0.0),
            DeltaDCut_3 = cms.double(15.0),
            MinP = cms.double(2.5),
            MinPt = cms.double(1.0),
            Chi2Cut_1 = cms.double(50.0),
            Pt_threshold2 = cms.double(999999999.0),
            LocChi2Cut = cms.double(0.001),
            Eta_threshold = cms.double(1.2),
            Quality_3 = cms.double(7.0),
            Quality_2 = cms.double(15.0),
            Chi2Cut_2 = cms.double(50.0),
            Chi2Cut_3 = cms.double(200.0),
            DeltaDCut_1 = cms.double(40.0),
            DeltaRCut_2 = cms.double(0.2),
            DeltaRCut_3 = cms.double(1.0),
            DeltaDCut_2 = cms.double(10.0),
            DeltaRCut_1 = cms.double(0.1),
            Propagator = cms.string('hltESPSmartPropagator'),
            Quality_1 = cms.double(20.0)
        ),
        PtCut = cms.double(1.0),
        TrackerPropagator = cms.string('SteppingHelixPropagatorAny'),
        tkTrajLabel = cms.InputTag("hltL3TkTracksFromL2IOHit")
    ),
    TrackLoaderParameters = cms.PSet(
        PutTkTrackIntoEvent = cms.untracked.bool(False),
        beamSpot = cms.InputTag("hltOnlineBeamSpot"),
        SmoothTkTrack = cms.untracked.bool(False),
        MuonSeededTracksInstance = cms.untracked.string('L2Seeded'),
        Smoother = cms.string('hltESPKFTrajectorySmootherForMuonTrackLoader'),
        MuonUpdatorAtVertexParameters = cms.PSet(
            MaxChi2 = cms.double(1000000.0),
            Propagator = cms.string('hltESPSteppingHelixPropagatorOpposite'),
            BeamSpotPositionErrors = cms.vdouble(0.1, 0.1, 5.3)
        ),
        VertexConstraint = cms.bool(False),
        DoSmoothing = cms.bool(True)
    ),
    MuonCollectionLabel = cms.InputTag("hltL2Muons","UpdatedAtVtx")
)


process.hltL3MuonsLinksCombination = cms.EDProducer("L3TrackLinksCombiner",
    labels = cms.VInputTag("hltL3MuonsOIState", "hltL3MuonsOIHit", "hltL3MuonsIOHit")
)


process.hltL3MuonsOIHit = cms.EDProducer("L3MuonProducer",
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('hltESPSmartPropagatorAny', 
            'SteppingHelixPropagatorAny', 
            'hltESPSmartPropagator', 
            'hltESPSteppingHelixPropagatorOpposite'),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    L3TrajBuilderParameters = cms.PSet(
        ScaleTECyFactor = cms.double(-1.0),
        GlbRefitterParameters = cms.PSet(
            DoPredictionsOnly = cms.bool(False),
            TrackerSkipSection = cms.int32(-1),
            Chi2CutCSC = cms.double(150.0),
            HitThreshold = cms.int32(1),
            MuonHitsOption = cms.int32(1),
            Chi2CutRPC = cms.double(1.0),
            Fitter = cms.string('hltESPL3MuKFTrajectoryFitter'),
            DTRecSegmentLabel = cms.InputTag("hltDt4DSegments"),
            TrackerRecHitBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
            MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
            RefitDirection = cms.string('insideOut'),
            CSCRecSegmentLabel = cms.InputTag("hltCscSegments"),
            DYTthrs = cms.vint32(30, 15),
            PropDirForCosmics = cms.bool(False),
            Chi2CutDT = cms.double(10.0),
            RefitRPCHits = cms.bool(True),
            SkipStation = cms.int32(-1),
            Propagator = cms.string('hltESPSmartPropagatorAny'),
            TrackerSkipSystem = cms.int32(-1)
        ),
        ScaleTECxFactor = cms.double(-1.0),
        TrackerRecHitBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
        MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
        MuonTrackingRegionBuilder = cms.PSet(
            EtaR_UpperLimit_Par1 = cms.double(0.25),
            DeltaR = cms.double(0.2),
            beamSpot = cms.InputTag("hltOnlineBeamSpot"),
            OnDemand = cms.double(-1.0),
            vertexCollection = cms.InputTag("pixelVertices"),
            Rescale_phi = cms.double(3.0),
            Eta_fixed = cms.double(0.2),
            DeltaZ_Region = cms.double(15.9),
            Rescale_eta = cms.double(3.0),
            PhiR_UpperLimit_Par2 = cms.double(0.2),
            Eta_min = cms.double(0.05),
            Phi_fixed = cms.double(0.2),
            Phi_min = cms.double(0.05),
            EscapePt = cms.double(1.5),
            UseFixedRegion = cms.bool(False),
            PhiR_UpperLimit_Par1 = cms.double(0.6),
            EtaR_UpperLimit_Par2 = cms.double(0.15),
            MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
            UseVertex = cms.bool(False),
            Rescale_Dz = cms.double(3.0)
        ),
        RefitRPCHits = cms.bool(True),
        PCut = cms.double(2.5),
        TrackTransformer = cms.PSet(
            DoPredictionsOnly = cms.bool(False),
            Fitter = cms.string('hltESPL3MuKFTrajectoryFitter'),
            TrackerRecHitBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
            Smoother = cms.string('hltESPKFTrajectorySmootherForMuonTrackLoader'),
            MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
            RefitDirection = cms.string('insideOut'),
            RefitRPCHits = cms.bool(True),
            Propagator = cms.string('hltESPSmartPropagatorAny')
        ),
        GlobalMuonTrackMatcher = cms.PSet(
            Pt_threshold1 = cms.double(0.0),
            DeltaDCut_3 = cms.double(15.0),
            MinP = cms.double(2.5),
            MinPt = cms.double(1.0),
            Chi2Cut_1 = cms.double(50.0),
            Pt_threshold2 = cms.double(999999999.0),
            LocChi2Cut = cms.double(0.001),
            Eta_threshold = cms.double(1.2),
            Quality_3 = cms.double(7.0),
            Quality_2 = cms.double(15.0),
            Chi2Cut_2 = cms.double(50.0),
            Chi2Cut_3 = cms.double(200.0),
            DeltaDCut_1 = cms.double(40.0),
            DeltaRCut_2 = cms.double(0.2),
            DeltaRCut_3 = cms.double(1.0),
            DeltaDCut_2 = cms.double(10.0),
            DeltaRCut_1 = cms.double(0.1),
            Propagator = cms.string('hltESPSmartPropagator'),
            Quality_1 = cms.double(20.0)
        ),
        PtCut = cms.double(1.0),
        TrackerPropagator = cms.string('SteppingHelixPropagatorAny'),
        tkTrajLabel = cms.InputTag("hltL3TkTracksFromL2OIHit")
    ),
    TrackLoaderParameters = cms.PSet(
        PutTkTrackIntoEvent = cms.untracked.bool(False),
        beamSpot = cms.InputTag("hltOnlineBeamSpot"),
        SmoothTkTrack = cms.untracked.bool(False),
        MuonSeededTracksInstance = cms.untracked.string('L2Seeded'),
        Smoother = cms.string('hltESPKFTrajectorySmootherForMuonTrackLoader'),
        MuonUpdatorAtVertexParameters = cms.PSet(
            MaxChi2 = cms.double(1000000.0),
            Propagator = cms.string('hltESPSteppingHelixPropagatorOpposite'),
            BeamSpotPositionErrors = cms.vdouble(0.1, 0.1, 5.3)
        ),
        VertexConstraint = cms.bool(False),
        DoSmoothing = cms.bool(True)
    ),
    MuonCollectionLabel = cms.InputTag("hltL2Muons","UpdatedAtVtx")
)


process.hltL3MuonsOIState = cms.EDProducer("L3MuonProducer",
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('hltESPSmartPropagatorAny', 
            'SteppingHelixPropagatorAny', 
            'hltESPSmartPropagator', 
            'hltESPSteppingHelixPropagatorOpposite'),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    L3TrajBuilderParameters = cms.PSet(
        ScaleTECyFactor = cms.double(-1.0),
        GlbRefitterParameters = cms.PSet(
            DoPredictionsOnly = cms.bool(False),
            TrackerSkipSection = cms.int32(-1),
            Chi2CutCSC = cms.double(150.0),
            HitThreshold = cms.int32(1),
            MuonHitsOption = cms.int32(1),
            Chi2CutRPC = cms.double(1.0),
            Fitter = cms.string('hltESPL3MuKFTrajectoryFitter'),
            DTRecSegmentLabel = cms.InputTag("hltDt4DSegments"),
            TrackerRecHitBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
            MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
            RefitDirection = cms.string('insideOut'),
            CSCRecSegmentLabel = cms.InputTag("hltCscSegments"),
            DYTthrs = cms.vint32(30, 15),
            PropDirForCosmics = cms.bool(False),
            Chi2CutDT = cms.double(10.0),
            RefitRPCHits = cms.bool(True),
            SkipStation = cms.int32(-1),
            Propagator = cms.string('hltESPSmartPropagatorAny'),
            TrackerSkipSystem = cms.int32(-1)
        ),
        ScaleTECxFactor = cms.double(-1.0),
        TrackerRecHitBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
        MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
        MuonTrackingRegionBuilder = cms.PSet(
            EtaR_UpperLimit_Par1 = cms.double(0.25),
            DeltaR = cms.double(0.2),
            beamSpot = cms.InputTag("hltOnlineBeamSpot"),
            OnDemand = cms.double(-1.0),
            vertexCollection = cms.InputTag("pixelVertices"),
            Rescale_phi = cms.double(3.0),
            Eta_fixed = cms.double(0.2),
            DeltaZ_Region = cms.double(15.9),
            Rescale_eta = cms.double(3.0),
            PhiR_UpperLimit_Par2 = cms.double(0.2),
            Eta_min = cms.double(0.05),
            Phi_fixed = cms.double(0.2),
            Phi_min = cms.double(0.05),
            EscapePt = cms.double(1.5),
            UseFixedRegion = cms.bool(False),
            PhiR_UpperLimit_Par1 = cms.double(0.6),
            EtaR_UpperLimit_Par2 = cms.double(0.15),
            MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
            UseVertex = cms.bool(False),
            Rescale_Dz = cms.double(3.0)
        ),
        RefitRPCHits = cms.bool(True),
        PCut = cms.double(2.5),
        TrackTransformer = cms.PSet(
            DoPredictionsOnly = cms.bool(False),
            Fitter = cms.string('hltESPL3MuKFTrajectoryFitter'),
            TrackerRecHitBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
            Smoother = cms.string('hltESPKFTrajectorySmootherForMuonTrackLoader'),
            MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
            RefitDirection = cms.string('insideOut'),
            RefitRPCHits = cms.bool(True),
            Propagator = cms.string('hltESPSmartPropagatorAny')
        ),
        GlobalMuonTrackMatcher = cms.PSet(
            Pt_threshold1 = cms.double(0.0),
            DeltaDCut_3 = cms.double(15.0),
            MinP = cms.double(2.5),
            MinPt = cms.double(1.0),
            Chi2Cut_1 = cms.double(50.0),
            Pt_threshold2 = cms.double(999999999.0),
            LocChi2Cut = cms.double(0.001),
            Eta_threshold = cms.double(1.2),
            Quality_3 = cms.double(7.0),
            Quality_2 = cms.double(15.0),
            Chi2Cut_2 = cms.double(50.0),
            Chi2Cut_3 = cms.double(200.0),
            DeltaDCut_1 = cms.double(40.0),
            DeltaRCut_2 = cms.double(0.2),
            DeltaRCut_3 = cms.double(1.0),
            DeltaDCut_2 = cms.double(10.0),
            DeltaRCut_1 = cms.double(0.1),
            Propagator = cms.string('hltESPSmartPropagator'),
            Quality_1 = cms.double(20.0)
        ),
        PtCut = cms.double(1.0),
        TrackerPropagator = cms.string('SteppingHelixPropagatorAny'),
        tkTrajLabel = cms.InputTag("hltL3TkTracksFromL2OIState")
    ),
    TrackLoaderParameters = cms.PSet(
        PutTkTrackIntoEvent = cms.untracked.bool(False),
        beamSpot = cms.InputTag("hltOnlineBeamSpot"),
        SmoothTkTrack = cms.untracked.bool(False),
        MuonSeededTracksInstance = cms.untracked.string('L2Seeded'),
        Smoother = cms.string('hltESPKFTrajectorySmootherForMuonTrackLoader'),
        MuonUpdatorAtVertexParameters = cms.PSet(
            MaxChi2 = cms.double(1000000.0),
            Propagator = cms.string('hltESPSteppingHelixPropagatorOpposite'),
            BeamSpotPositionErrors = cms.vdouble(0.1, 0.1, 5.3)
        ),
        VertexConstraint = cms.bool(False),
        DoSmoothing = cms.bool(True)
    ),
    MuonCollectionLabel = cms.InputTag("hltL2Muons","UpdatedAtVtx")
)


process.hltL3TkFromL2OICombination = cms.EDProducer("L3TrackCombiner",
    labels = cms.VInputTag("hltL3MuonsOIState", "hltL3MuonsOIHit")
)


process.hltL3TkTracksFromL2 = cms.EDProducer("L3TrackCombiner",
    labels = cms.VInputTag("hltL3TkTracksFromL2IOHit", "hltL3TkTracksFromL2OIHit", "hltL3TkTracksFromL2OIState")
)


process.hltL3TkTracksFromL2IOHit = cms.EDProducer("TrackProducer",
    src = cms.InputTag("hltL3TrackCandidateFromL2IOHit"),
    clusterRemovalInfo = cms.InputTag(""),
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    Fitter = cms.string('hltESPKFFittingSmoother'),
    useHitsSplitting = cms.bool(False),
    MeasurementTracker = cms.string(''),
    alias = cms.untracked.string(''),
    NavigationSchool = cms.string(''),
    TrajectoryInEvent = cms.bool(True),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    AlgorithmName = cms.string('undefAlgorithm'),
    Propagator = cms.string('PropagatorWithMaterial')
)


process.hltL3TkTracksFromL2OIHit = cms.EDProducer("TrackProducer",
    src = cms.InputTag("hltL3TrackCandidateFromL2OIHit"),
    clusterRemovalInfo = cms.InputTag(""),
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    Fitter = cms.string('hltESPKFFittingSmoother'),
    useHitsSplitting = cms.bool(False),
    MeasurementTracker = cms.string(''),
    alias = cms.untracked.string(''),
    NavigationSchool = cms.string(''),
    TrajectoryInEvent = cms.bool(True),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    AlgorithmName = cms.string('undefAlgorithm'),
    Propagator = cms.string('PropagatorWithMaterial')
)


process.hltL3TkTracksFromL2OIState = cms.EDProducer("TrackProducer",
    src = cms.InputTag("hltL3TrackCandidateFromL2OIState"),
    clusterRemovalInfo = cms.InputTag(""),
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    Fitter = cms.string('hltESPKFFittingSmoother'),
    useHitsSplitting = cms.bool(False),
    MeasurementTracker = cms.string(''),
    alias = cms.untracked.string(''),
    NavigationSchool = cms.string(''),
    TrajectoryInEvent = cms.bool(True),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    AlgorithmName = cms.string('undefAlgorithm'),
    Propagator = cms.string('PropagatorWithMaterial')
)


process.hltL3TrackCandidateFromL2 = cms.EDProducer("L3TrackCandCombiner",
    labels = cms.VInputTag("hltL3TrackCandidateFromL2IOHit", "hltL3TrackCandidateFromL2OIHit", "hltL3TrackCandidateFromL2OIState")
)


process.hltL3TrackCandidateFromL2IOHit = cms.EDProducer("CkfTrajectoryMaker",
    src = cms.InputTag("hltL3TrajSeedIOHit"),
    reverseTrajectories = cms.bool(False),
    TrajectoryCleaner = cms.string('hltESPTrajectoryCleanerBySharedHits'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    cleanTrajectoryAfterInOut = cms.bool(False),
    useHitsSplitting = cms.bool(False),
    doSeedingRegionRebuilding = cms.bool(False),
    trackCandidateAlso = cms.bool(True),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryBuilder = cms.string('hltESPMuonCkfTrajectoryBuilder'),
    maxNSeeds = cms.uint32(100000),
    TransientInitialStateEstimatorParameters = cms.PSet(
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        numberMeasurementsForFit = cms.int32(4),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    )
)


process.hltL3TrackCandidateFromL2OIHit = cms.EDProducer("CkfTrajectoryMaker",
    src = cms.InputTag("hltL3TrajSeedOIHit"),
    reverseTrajectories = cms.bool(True),
    TrajectoryCleaner = cms.string('hltESPTrajectoryCleanerBySharedHits'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    cleanTrajectoryAfterInOut = cms.bool(False),
    useHitsSplitting = cms.bool(False),
    doSeedingRegionRebuilding = cms.bool(False),
    trackCandidateAlso = cms.bool(True),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryBuilder = cms.string('hltESPMuonCkfTrajectoryBuilder'),
    maxNSeeds = cms.uint32(100000),
    TransientInitialStateEstimatorParameters = cms.PSet(
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        numberMeasurementsForFit = cms.int32(4),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    )
)


process.hltL3TrackCandidateFromL2OIState = cms.EDProducer("CkfTrajectoryMaker",
    src = cms.InputTag("hltL3TrajSeedOIState"),
    reverseTrajectories = cms.bool(True),
    TrajectoryCleaner = cms.string('hltESPTrajectoryCleanerBySharedHits'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    cleanTrajectoryAfterInOut = cms.bool(False),
    useHitsSplitting = cms.bool(False),
    doSeedingRegionRebuilding = cms.bool(False),
    trackCandidateAlso = cms.bool(True),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryBuilder = cms.string('hltESPMuonCkfTrajectoryBuilderSeedHit'),
    maxNSeeds = cms.uint32(100000),
    TransientInitialStateEstimatorParameters = cms.PSet(
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        numberMeasurementsForFit = cms.int32(4),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    )
)


process.hltL3TrajSeedIOHit = cms.EDProducer("TSGFromL2Muon",
    TkSeedGenerator = cms.PSet(
        ComponentName = cms.string('DualByL2TSG'),
        L3TkCollectionA = cms.InputTag("hltL3TkFromL2OICombination"),
        iterativeTSG = cms.PSet(
            firstTSG = cms.PSet(
                ComponentName = cms.string('TSGFromOrderedHits'),
                OrderedHitsFactoryPSet = cms.PSet(
                    ComponentName = cms.string('StandardHitTripletGenerator'),
                    SeedingLayers = cms.string('hltESPPixelLayerTriplets'),
                    GeneratorPSet = cms.PSet(
                        useBending = cms.bool(True),
                        useFixedPreFiltering = cms.bool(False),
                        maxElement = cms.uint32(0),
                        phiPreFiltering = cms.double(0.3),
                        extraHitRPhitolerance = cms.double(0.06),
                        useMultScattering = cms.bool(True),
                        SeedComparitorPSet = cms.PSet(
                            ComponentName = cms.string('none')
                        ),
                        extraHitRZtolerance = cms.double(0.06),
                        ComponentName = cms.string('PixelTripletHLTGenerator')
                    )
                ),
                TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle')
            ),
            PSetNames = cms.vstring('firstTSG', 
                'secondTSG'),
            ComponentName = cms.string('CombinedTSG'),
            thirdTSG = cms.PSet(
                PSetNames = cms.vstring('endcapTSG', 
                    'barrelTSG'),
                ComponentName = cms.string('DualByEtaTSG'),
                endcapTSG = cms.PSet(
                    ComponentName = cms.string('TSGFromOrderedHits'),
                    OrderedHitsFactoryPSet = cms.PSet(
                        maxElement = cms.uint32(0),
                        ComponentName = cms.string('StandardHitPairGenerator'),
                        SeedingLayers = cms.string('hltESPMixedLayerPairs'),
                        useOnDemandTracker = cms.untracked.int32(0)
                    ),
                    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle')
                ),
                etaSeparation = cms.double(2.0),
                barrelTSG = cms.PSet(

                )
            ),
            secondTSG = cms.PSet(
                ComponentName = cms.string('TSGFromOrderedHits'),
                OrderedHitsFactoryPSet = cms.PSet(
                    maxElement = cms.uint32(0),
                    ComponentName = cms.string('StandardHitPairGenerator'),
                    SeedingLayers = cms.string('hltESPPixelLayerPairs'),
                    useOnDemandTracker = cms.untracked.int32(0)
                ),
                TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle')
            )
        ),
        skipTSG = cms.PSet(

        ),
        PSetNames = cms.vstring('skipTSG', 
            'iterativeTSG')
    ),
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('PropagatorWithMaterial'),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    MuonCollectionLabel = cms.InputTag("hltL2Muons","UpdatedAtVtx"),
    MuonTrackingRegionBuilder = cms.PSet(
        EtaR_UpperLimit_Par1 = cms.double(0.25),
        DeltaR = cms.double(0.2),
        beamSpot = cms.InputTag("hltOnlineBeamSpot"),
        OnDemand = cms.double(-1.0),
        vertexCollection = cms.InputTag("pixelVertices"),
        Rescale_phi = cms.double(3.0),
        Eta_fixed = cms.double(0.2),
        DeltaZ_Region = cms.double(15.9),
        Rescale_eta = cms.double(3.0),
        PhiR_UpperLimit_Par2 = cms.double(0.2),
        Eta_min = cms.double(0.1),
        Phi_fixed = cms.double(0.2),
        Phi_min = cms.double(0.1),
        EscapePt = cms.double(1.5),
        UseFixedRegion = cms.bool(False),
        PhiR_UpperLimit_Par1 = cms.double(0.6),
        EtaR_UpperLimit_Par2 = cms.double(0.15),
        MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
        UseVertex = cms.bool(False),
        Rescale_Dz = cms.double(3.0)
    ),
    PCut = cms.double(2.5),
    TrackerSeedCleaner = cms.PSet(
        cleanerFromSharedHits = cms.bool(True),
        ptCleaner = cms.bool(True),
        TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
        beamSpot = cms.InputTag("hltOnlineBeamSpot"),
        directionCleaner = cms.bool(True)
    ),
    PtCut = cms.double(1.0)
)


process.hltL3TrajSeedOIHit = cms.EDProducer("TSGFromL2Muon",
    TkSeedGenerator = cms.PSet(
        ComponentName = cms.string('DualByL2TSG'),
        L3TkCollectionA = cms.InputTag("hltL3MuonsOIState"),
        iterativeTSG = cms.PSet(
            ErrorRescaling = cms.double(3.0),
            beamSpot = cms.InputTag("unused"),
            ComponentName = cms.string('TSGFromPropagation'),
            errorMatrixPset = cms.PSet(
                action = cms.string('use'),
                atIP = cms.bool(True),
                errorMatrixValuesPSet = cms.PSet(
                    pf3_V12 = cms.PSet(
                        action = cms.string('scale'),
                        values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0)
                    ),
                    pf3_V13 = cms.PSet(
                        action = cms.string('scale'),
                        values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0)
                    ),
                    pf3_V11 = cms.PSet(
                        action = cms.string('scale'),
                        values = cms.vdouble(3.0, 3.0, 3.0, 5.0, 4.0, 
                            5.0, 10.0, 7.0, 10.0, 10.0, 
                            10.0, 10.0)
                    ),
                    pf3_V45 = cms.PSet(
                        action = cms.string('scale'),
                        values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0)
                    ),
                    pf3_V14 = cms.PSet(
                        action = cms.string('scale'),
                        values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0)
                    ),
                    pf3_V15 = cms.PSet(
                        action = cms.string('scale'),
                        values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0)
                    ),
                    yAxis = cms.vdouble(0.0, 1.0, 1.4, 10.0),
                    pf3_V35 = cms.PSet(
                        action = cms.string('scale'),
                        values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0)
                    ),
                    zAxis = cms.vdouble(-3.14159, 3.14159),
                    pf3_V44 = cms.PSet(
                        action = cms.string('scale'),
                        values = cms.vdouble(3.0, 3.0, 3.0, 5.0, 4.0, 
                            5.0, 10.0, 7.0, 10.0, 10.0, 
                            10.0, 10.0)
                    ),
                    xAxis = cms.vdouble(0.0, 13.0, 30.0, 70.0, 1000.0),
                    pf3_V23 = cms.PSet(
                        action = cms.string('scale'),
                        values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0)
                    ),
                    pf3_V22 = cms.PSet(
                        action = cms.string('scale'),
                        values = cms.vdouble(3.0, 3.0, 3.0, 5.0, 4.0, 
                            5.0, 10.0, 7.0, 10.0, 10.0, 
                            10.0, 10.0)
                    ),
                    pf3_V55 = cms.PSet(
                        action = cms.string('scale'),
                        values = cms.vdouble(3.0, 3.0, 3.0, 5.0, 4.0, 
                            5.0, 10.0, 7.0, 10.0, 10.0, 
                            10.0, 10.0)
                    ),
                    pf3_V34 = cms.PSet(
                        action = cms.string('scale'),
                        values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0)
                    ),
                    pf3_V33 = cms.PSet(
                        action = cms.string('scale'),
                        values = cms.vdouble(3.0, 3.0, 3.0, 5.0, 4.0, 
                            5.0, 10.0, 7.0, 10.0, 10.0, 
                            10.0, 10.0)
                    ),
                    pf3_V25 = cms.PSet(
                        action = cms.string('scale'),
                        values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0)
                    ),
                    pf3_V24 = cms.PSet(
                        action = cms.string('scale'),
                        values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0, 1.0, 1.0, 1.0, 
                            1.0, 1.0)
                    )
                )
            ),
            UpdateState = cms.bool(True),
            MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
            SelectState = cms.bool(False),
            SigmaZ = cms.double(25.0),
            ResetMethod = cms.string('matrix'),
            MaxChi2 = cms.double(40.0),
            UseVertexState = cms.bool(True),
            Propagator = cms.string('hltESPSmartPropagatorAnyOpposite')
        ),
        skipTSG = cms.PSet(

        ),
        PSetNames = cms.vstring('skipTSG', 
            'iterativeTSG')
    ),
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('PropagatorWithMaterial', 
            'hltESPSmartPropagatorAnyOpposite'),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    MuonCollectionLabel = cms.InputTag("hltL2Muons","UpdatedAtVtx"),
    MuonTrackingRegionBuilder = cms.PSet(

    ),
    PCut = cms.double(2.5),
    TrackerSeedCleaner = cms.PSet(
        cleanerFromSharedHits = cms.bool(True),
        ptCleaner = cms.bool(True),
        TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
        beamSpot = cms.InputTag("hltOnlineBeamSpot"),
        directionCleaner = cms.bool(True)
    ),
    PtCut = cms.double(1.0)
)


process.hltL3TrajSeedOIState = cms.EDProducer("TSGFromL2Muon",
    TkSeedGenerator = cms.PSet(
        propagatorCompatibleName = cms.string('hltESPSteppingHelixPropagatorOpposite'),
        option = cms.uint32(3),
        ComponentName = cms.string('TSGForRoadSearch'),
        errorMatrixPset = cms.PSet(
            action = cms.string('use'),
            atIP = cms.bool(True),
            errorMatrixValuesPSet = cms.PSet(
                pf3_V12 = cms.PSet(
                    action = cms.string('scale'),
                    values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0)
                ),
                pf3_V13 = cms.PSet(
                    action = cms.string('scale'),
                    values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0)
                ),
                pf3_V11 = cms.PSet(
                    action = cms.string('scale'),
                    values = cms.vdouble(3.0, 3.0, 3.0, 5.0, 4.0, 
                        5.0, 10.0, 7.0, 10.0, 10.0, 
                        10.0, 10.0)
                ),
                pf3_V45 = cms.PSet(
                    action = cms.string('scale'),
                    values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0)
                ),
                pf3_V14 = cms.PSet(
                    action = cms.string('scale'),
                    values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0)
                ),
                pf3_V15 = cms.PSet(
                    action = cms.string('scale'),
                    values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0)
                ),
                yAxis = cms.vdouble(0.0, 1.0, 1.4, 10.0),
                pf3_V35 = cms.PSet(
                    action = cms.string('scale'),
                    values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0)
                ),
                zAxis = cms.vdouble(-3.14159, 3.14159),
                pf3_V44 = cms.PSet(
                    action = cms.string('scale'),
                    values = cms.vdouble(3.0, 3.0, 3.0, 5.0, 4.0, 
                        5.0, 10.0, 7.0, 10.0, 10.0, 
                        10.0, 10.0)
                ),
                xAxis = cms.vdouble(0.0, 13.0, 30.0, 70.0, 1000.0),
                pf3_V23 = cms.PSet(
                    action = cms.string('scale'),
                    values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0)
                ),
                pf3_V22 = cms.PSet(
                    action = cms.string('scale'),
                    values = cms.vdouble(3.0, 3.0, 3.0, 5.0, 4.0, 
                        5.0, 10.0, 7.0, 10.0, 10.0, 
                        10.0, 10.0)
                ),
                pf3_V55 = cms.PSet(
                    action = cms.string('scale'),
                    values = cms.vdouble(3.0, 3.0, 3.0, 5.0, 4.0, 
                        5.0, 10.0, 7.0, 10.0, 10.0, 
                        10.0, 10.0)
                ),
                pf3_V34 = cms.PSet(
                    action = cms.string('scale'),
                    values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0)
                ),
                pf3_V33 = cms.PSet(
                    action = cms.string('scale'),
                    values = cms.vdouble(3.0, 3.0, 3.0, 5.0, 4.0, 
                        5.0, 10.0, 7.0, 10.0, 10.0, 
                        10.0, 10.0)
                ),
                pf3_V25 = cms.PSet(
                    action = cms.string('scale'),
                    values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0)
                ),
                pf3_V24 = cms.PSet(
                    action = cms.string('scale'),
                    values = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0, 1.0, 1.0, 1.0, 
                        1.0, 1.0)
                )
            )
        ),
        propagatorName = cms.string('hltESPSteppingHelixPropagatorAlong'),
        manySeeds = cms.bool(False),
        copyMuonRecHit = cms.bool(False),
        maxChi2 = cms.double(40.0)
    ),
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('hltESPSteppingHelixPropagatorOpposite', 
            'hltESPSteppingHelixPropagatorAlong'),
        RPCLayers = cms.bool(True),
        UseMuonNavigation = cms.untracked.bool(True)
    ),
    MuonCollectionLabel = cms.InputTag("hltL2Muons","UpdatedAtVtx"),
    MuonTrackingRegionBuilder = cms.PSet(

    ),
    PCut = cms.double(2.5),
    TrackerSeedCleaner = cms.PSet(

    ),
    PtCut = cms.double(1.0)
)


process.hltL3TrajectorySeed = cms.EDProducer("L3MuonTrajectorySeedCombiner",
    labels = cms.VInputTag("hltL3TrajSeedIOHit", "hltL3TrajSeedOIState", "hltL3TrajSeedOIHit")
)


process.hltMuonCSCDigis = cms.EDProducer("CSCDCCUnpacker",
    PrintEventNumber = cms.untracked.bool(False),
    UseExaminer = cms.bool(True),
    Debug = cms.untracked.bool(False),
    ErrorMask = cms.uint32(0),
    InputObjects = cms.InputTag("rawDataCollector"),
    ExaminerMask = cms.uint32(535557110),
    UseFormatStatus = cms.bool(True),
    UnpackStatusDigis = cms.bool(False),
    VisualFEDInspect = cms.untracked.bool(False),
    FormatedEventDump = cms.untracked.bool(False),
    UseSelectiveUnpacking = cms.bool(True),
    VisualFEDShort = cms.untracked.bool(False)
)


process.hltMuonDTDigis = cms.EDProducer("DTUnpackingModule",
    dataType = cms.string('DDU'),
    inputLabel = cms.InputTag("rawDataCollector"),
    useStandardFEDid = cms.bool(True),
    fedbyType = cms.bool(False),
    readOutParameters = cms.PSet(
        debug = cms.untracked.bool(False),
        rosParameters = cms.PSet(
            writeSC = cms.untracked.bool(True),
            readingDDU = cms.untracked.bool(True),
            performDataIntegrityMonitor = cms.untracked.bool(False),
            readDDUIDfromDDU = cms.untracked.bool(True),
            debug = cms.untracked.bool(False),
            localDAQ = cms.untracked.bool(False)
        ),
        performDataIntegrityMonitor = cms.untracked.bool(False),
        localDAQ = cms.untracked.bool(False)
    ),
    dqmOnly = cms.bool(False)
)


process.hltMuonRPCDigis = cms.EDProducer("RPCUnpackingModule",
    InputLabel = cms.InputTag("rawDataCollector"),
    doSynchro = cms.bool(False)
)


process.hltOnlineBeamSpot = cms.EDProducer("BeamSpotOnlineProducer",
    maxZ = cms.double(40.0),
    src = cms.InputTag("hltScalersRawToDigi"),
    gtEvmLabel = cms.InputTag(""),
    changeToCMSCoordinates = cms.bool(False),
    setSigmaZ = cms.double(0.0),
    maxRadius = cms.double(2.0)
)


process.hltRpcRecHits = cms.EDProducer("RPCRecHitProducer",
    recAlgo = cms.string('RPCRecHitStandardAlgo'),
    deadvecfile = cms.FileInPath('RecoLocalMuon/RPCRecHit/data/RPCDeadVec.dat'),
    rpcDigiLabel = cms.InputTag("hltMuonRPCDigis"),
    maskvecfile = cms.FileInPath('RecoLocalMuon/RPCRecHit/data/RPCMaskVec.dat'),
    recAlgoConfig = cms.PSet(

    ),
    deadSource = cms.string('File'),
    maskSource = cms.string('File')
)


process.hltScalersRawToDigi = cms.EDProducer("ScalersRawToDigi",
    scalersInputTag = cms.InputTag("rawDataCollector")
)


process.hltSiPixelClusters = cms.EDProducer("SiPixelClusterProducer",
    src = cms.InputTag("hltSiPixelDigis"),
    ChannelThreshold = cms.int32(1000),
    maxNumberOfClusters = cms.int32(20000),
    VCaltoElectronGain = cms.int32(65),
    MissCalibrate = cms.untracked.bool(True),
    SplitClusters = cms.bool(False),
    VCaltoElectronOffset = cms.int32(-414),
    payloadType = cms.string('HLT'),
    SeedThreshold = cms.int32(1000),
    ClusterThreshold = cms.double(4000.0)
)


process.hltSiPixelDigis = cms.EDProducer("SiPixelRawToDigi",
    UseQualityInfo = cms.bool(False),
    CheckPixelOrder = cms.bool(False),
    IncludeErrors = cms.bool(False),
    UseCablingTree = cms.untracked.bool(True),
    InputLabel = cms.InputTag("rawDataCollector"),
    ErrorList = cms.vint32(),
    Regions = cms.PSet(

    ),
    Timing = cms.untracked.bool(False),
    UserErrorList = cms.vint32()
)


process.hltSiPixelRecHits = cms.EDProducer("SiPixelRecHitConverter",
    VerboseLevel = cms.untracked.int32(0),
    src = cms.InputTag("hltSiPixelClusters"),
    CPE = cms.string('hltESPPixelCPEGeneric')
)


process.hltSiStripClusters = cms.EDProducer("MeasurementTrackerSiStripRefGetterProducer",
    InputModuleLabel = cms.InputTag("hltSiStripRawToClustersFacility"),
    measurementTrackerName = cms.string('hltESPMeasurementTracker')
)


process.hltSiStripExcludedFEDListProducer = cms.EDProducer("SiStripExcludedFEDListProducer",
    ProductLabel = cms.InputTag("rawDataCollector")
)


process.hltSiStripRawToClustersFacility = cms.EDProducer("SiStripRawToClusters",
    ProductLabel = cms.InputTag("rawDataCollector"),
    DoAPVEmulatorCheck = cms.bool(False),
    Algorithms = cms.PSet(
        CommonModeNoiseSubtractionMode = cms.string('Median'),
        doAPVRestore = cms.bool(False),
        TruncateInSuppressor = cms.bool(True),
        useCMMeanMap = cms.bool(False),
        PedestalSubtractionFedMode = cms.bool(True),
        SiStripFedZeroSuppressionMode = cms.uint32(4)
    ),
    Clusterizer = cms.PSet(
        setDetId = cms.bool(True),
        ChannelThreshold = cms.double(2.0),
        MaxSequentialBad = cms.uint32(1),
        MaxSequentialHoles = cms.uint32(0),
        Algorithm = cms.string('ThreeThresholdAlgorithm'),
        MaxAdjacentBad = cms.uint32(0),
        QualityLabel = cms.string(''),
        SeedThreshold = cms.double(3.0),
        RemoveApvShots = cms.bool(True),
        ClusterThreshold = cms.double(5.0)
    )
)


process.hltBoolEnd = cms.EDFilter("HLTBool",
    result = cms.bool(True)
)


process.hltDiMuonGlb17Glb8DzFiltered0p2 = cms.EDFilter("HLT2MuonMuonDZ",
    saveTags = cms.bool(True),
    originTag1 = cms.InputTag("hltL3MuonCandidates"),
    originTag2 = cms.InputTag("hltL3MuonCandidates"),
    MinN = cms.int32(1),
    triggerType1 = cms.int32(83),
    triggerType2 = cms.int32(83),
    MinDR = cms.double(0.001),
    MaxDZ = cms.double(0.2),
    inputTag1 = cms.InputTag("hltL3pfL1DoubleMu10MuOpenOR3p5L1f0L2pf0L3PreFiltered8"),
    checkSC = cms.bool(False),
    inputTag2 = cms.InputTag("hltL3fL1DoubleMu10MuOpenOR3p5L1f0L2f10L3Filtered17")
)


process.hltL1DoubleMu10MuOpenOR3p5L1Filtered0 = cms.EDFilter("HLTMuonL1Filter",
    saveTags = cms.bool(False),
    CSCTFtag = cms.InputTag("unused"),
    PreviousCandTag = cms.InputTag("hltL1sL1DoubleMu10MuOpenORDoubleMu103p5"),
    MinPt = cms.double(0.0),
    MinN = cms.int32(2),
    MaxEta = cms.double(2.5),
    SelectQualities = cms.vint32(),
    CandTag = cms.InputTag("hltL1extraParticles"),
    ExcludeSingleSegmentCSC = cms.bool(False)
)


process.hltL1sL1DoubleMu10MuOpenORDoubleMu103p5 = cms.EDFilter("HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string('L1_DoubleMu_10_Open OR L1_DoubleMu_10_3p5'),
    saveTags = cms.bool(True),
    L1MuonCollectionTag = cms.InputTag("hltL1extraParticles"),
    L1UseL1TriggerObjectMaps = cms.bool(True),
    L1UseAliasesForSeeding = cms.bool(True),
    L1GtReadoutRecordTag = cms.InputTag("hltGtDigis"),
    L1CollectionsTag = cms.InputTag("hltL1extraParticles"),
    L1NrBxInEvent = cms.int32(3),
    L1GtObjectMapTag = cms.InputTag("hltL1GtObjectMap"),
    L1TechTriggerSeeding = cms.bool(False)
)


process.hltL2fL1DoubleMu10MuOpenOR3p5L1f0L2Filtered10 = cms.EDFilter("HLTMuonL2PreFilter",
    saveTags = cms.bool(True),
    CutOnChambers = cms.bool(False),
    BeamSpotTag = cms.InputTag("hltOnlineBeamSpot"),
    MinNstations = cms.vint32(0),
    MinN = cms.int32(1),
    SeedMapTag = cms.InputTag("hltL2Muons"),
    MaxEta = cms.double(2.5),
    MinNhits = cms.vint32(0),
    MinDxySig = cms.double(-1.0),
    MinNchambers = cms.vint32(0),
    AbsEtaBins = cms.vdouble(5.0),
    MaxDz = cms.double(9999.0),
    PreviousCandTag = cms.InputTag("hltL1DoubleMu10MuOpenOR3p5L1Filtered0"),
    MaxDr = cms.double(9999.0),
    CandTag = cms.InputTag("hltL2MuonCandidates"),
    MinDr = cms.double(-1.0),
    NSigmaPt = cms.double(0.0),
    MinPt = cms.double(10.0)
)


process.hltL2pfL1DoubleMu10MuOpenOR3p5L1f0L2PreFiltered0 = cms.EDFilter("HLTMuonL2PreFilter",
    saveTags = cms.bool(True),
    CutOnChambers = cms.bool(False),
    BeamSpotTag = cms.InputTag("hltOnlineBeamSpot"),
    MinNstations = cms.vint32(0),
    MinN = cms.int32(2),
    SeedMapTag = cms.InputTag("hltL2Muons"),
    MaxEta = cms.double(2.5),
    MinNhits = cms.vint32(0),
    MinDxySig = cms.double(-1.0),
    MinNchambers = cms.vint32(0),
    AbsEtaBins = cms.vdouble(5.0),
    MaxDz = cms.double(9999.0),
    PreviousCandTag = cms.InputTag("hltL1DoubleMu10MuOpenOR3p5L1Filtered0"),
    MaxDr = cms.double(9999.0),
    CandTag = cms.InputTag("hltL2MuonCandidates"),
    MinDr = cms.double(-1.0),
    NSigmaPt = cms.double(0.0),
    MinPt = cms.double(0.0)
)


process.hltL3fL1DoubleMu10MuOpenOR3p5L1f0L2f10L3Filtered17 = cms.EDFilter("HLTMuonL3PreFilter",
    saveTags = cms.bool(True),
    MaxNormalizedChi2 = cms.double(9999.0),
    BeamSpotTag = cms.InputTag("hltOnlineBeamSpot"),
    MinPt = cms.double(17.0),
    MinN = cms.int32(1),
    MinTrackPt = cms.double(0.0),
    MaxEta = cms.double(2.5),
    MaxDXYBeamSpot = cms.double(9999.0),
    MinNhits = cms.int32(0),
    MinDxySig = cms.double(-1.0),
    MinDr = cms.double(-1.0),
    MaxDz = cms.double(9999.0),
    PreviousCandTag = cms.InputTag("hltL2fL1DoubleMu10MuOpenOR3p5L1f0L2Filtered10"),
    MaxPtDifference = cms.double(9999.0),
    MaxDr = cms.double(2.0),
    CandTag = cms.InputTag("hltL3MuonCandidates"),
    NSigmaPt = cms.double(0.0),
    MinNmuonHits = cms.int32(0)
)


process.hltL3pfL1DoubleMu10MuOpenOR3p5L1f0L2pf0L3PreFiltered8 = cms.EDFilter("HLTMuonL3PreFilter",
    saveTags = cms.bool(True),
    MaxNormalizedChi2 = cms.double(9999.0),
    BeamSpotTag = cms.InputTag("hltOnlineBeamSpot"),
    MinPt = cms.double(8.0),
    MinN = cms.int32(2),
    MinTrackPt = cms.double(0.0),
    MaxEta = cms.double(2.5),
    MaxDXYBeamSpot = cms.double(9999.0),
    MinNhits = cms.int32(0),
    MinDxySig = cms.double(-1.0),
    MinDr = cms.double(-1.0),
    MaxDz = cms.double(9999.0),
    PreviousCandTag = cms.InputTag("hltL2pfL1DoubleMu10MuOpenOR3p5L1f0L2PreFiltered0"),
    MaxPtDifference = cms.double(9999.0),
    MaxDr = cms.double(2.0),
    CandTag = cms.InputTag("hltL3MuonCandidates"),
    NSigmaPt = cms.double(0.0),
    MinNmuonHits = cms.int32(0)
)


process.hltPreALCALUMIPIXELSOutput = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtDigis"),
    offset = cms.uint32(0)
)


process.hltPreALCAP0Output = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtDigis"),
    offset = cms.uint32(0)
)


process.hltPreALCAPHISYMOutput = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtDigis"),
    offset = cms.uint32(0)
)


process.hltPreAOutput = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtDigis"),
    offset = cms.uint32(0)
)


process.hltPreBOutput = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtDigis"),
    offset = cms.uint32(0)
)


process.hltPreCalibrationOutput = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtDigis"),
    offset = cms.uint32(0)
)


process.hltPreDQMOutput = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtDigis"),
    offset = cms.uint32(0)
)


process.hltPreEcalCalibrationOutput = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtDigis"),
    offset = cms.uint32(0)
)


process.hltPreExpressOutput = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtDigis"),
    offset = cms.uint32(0)
)


process.hltPreExpressOutputSmart = cms.EDFilter("TriggerResultsFilter",
    l1tIgnoreMask = cms.bool(False),
    l1tResults = cms.InputTag("hltGtDigis"),
    l1techIgnorePrescales = cms.bool(False),
    hltResults = cms.InputTag("TriggerResults"),
    triggerConditions = cms.vstring('HLT_EightJet35_eta3p0_v5', 
        'HLT_MET400_v7', 
        'HLT_Mu17_Mu8_v22 / 2', 
        'HLT_Photon300_NoHE_v5', 
        'HLT_DoublePhoton80_v7', 
        'HLT_ZeroBias_v7'),
    throw = cms.bool(True),
    daqPartitions = cms.uint32(1),
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT")
)


process.hltPreHLTDQMOutput = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtDigis"),
    offset = cms.uint32(0)
)


process.hltPreHLTDQMOutputSmart = cms.EDFilter("TriggerResultsFilter",
    l1tIgnoreMask = cms.bool(False),
    l1tResults = cms.InputTag("hltGtDigis"),
    l1techIgnorePrescales = cms.bool(False),
    hltResults = cms.InputTag("TriggerResults"),
    triggerConditions = cms.vstring('HLT_PFJet40_v8', 
        'HLT_PFJet80_v9', 
        'HLT_PFJet140_v9', 
        'HLT_PFJet200_v9', 
        'HLT_PFJet260_v9', 
        'HLT_PFJet320_v9', 
        'HLT_Jet370_NoJetID_v15', 
        'HLT_PFJet400_v9', 
        'HLT_SingleForJet25_v4', 
        'HLT_SingleForJet15_v4', 
        'HLT_DiPFJetAve40_v9', 
        'HLT_DiPFJetAve80_v10', 
        'HLT_DiPFJetAve140_v10', 
        'HLT_DiPFJetAve200_v10', 
        'HLT_DiPFJetAve260_v10', 
        'HLT_DiPFJetAve320_v10', 
        'HLT_DiPFJetAve400_v10', 
        'HLT_DiJet80_DiJet60_DiJet20_v6', 
        'HLT_Mu5_v20', 
        'HLT_Mu8_v18', 
        'HLT_Mu12_v18', 
        'HLT_Mu17_v5', 
        'HLT_Mu15_eta2p1_v5', 
        'HLT_Mu24_eta2p1_v5', 
        'HLT_Mu30_eta2p1_v5', 
        'HLT_Mu40_eta2p1_v11', 
        'HLT_RelIso1p0Mu5_v6', 
        'HLT_IsoMu20_eta2p1_v7', 
        'HLT_IsoMu24_eta2p1_v15', 
        'HLT_IsoMu30_eta2p1_v15', 
        'HLT_IsoMu34_eta2p1_v13', 
        'HLT_IsoMu40_eta2p1_v10', 
        'HLT_Mu40_eta2p1_Track50_dEdx3p6_v5', 
        'HLT_Mu40_eta2p1_Track60_dEdx3p7_v5', 
        'HLT_Ele22_CaloIdL_CaloIsoVL_v6', 
        'HLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_v11', 
        'HLT_Ele27_WP80_v11', 
        'HLT_Ele27_WP80_PFMET_MT50_v7', 
        'HLT_Ele30_CaloIdVT_TrkIdT_v6', 
        'HLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_v11', 
        'HLT_Ele80_CaloIdVT_GsfTrkIdT_v2', 
        'HLT_Ele90_CaloIdVT_GsfTrkIdT_v2'),
    throw = cms.bool(True),
    daqPartitions = cms.uint32(1),
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT")
)


process.hltPreHLTMONOutput = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtDigis"),
    offset = cms.uint32(0)
)


process.hltPreHLTMONOutputSmart = cms.EDFilter("TriggerResultsFilter",
    l1tIgnoreMask = cms.bool(False),
    l1tResults = cms.InputTag("hltGtDigis"),
    l1techIgnorePrescales = cms.bool(False),
    hltResults = cms.InputTag("TriggerResults"),
    triggerConditions = cms.vstring( ('HLT_Activity_Ecal_SC7_v13', 
        'HLT_L1SingleJet16_v7', 
        'HLT_L1SingleJet36_v7', 
        'HLT_PFJet40_v8', 
        'HLT_PFJet80_v9', 
        'HLT_PFJet140_v9', 
        'HLT_PFJet200_v9', 
        'HLT_PFJet260_v9', 
        'HLT_PFJet320_v9', 
        'HLT_Jet370_NoJetID_v15', 
        'HLT_PFJet400_v9', 
        'HLT_MonoCentralPFJet80_PFMETnoMu105_NHEF0p95_v4', 
        'HLT_SingleForJet25_v4', 
        'HLT_SingleForJet15_v4', 
        'HLT_DiPFJetAve40_v9', 
        'HLT_DiPFJetAve80_v10', 
        'HLT_DiPFJetAve140_v10', 
        'HLT_DiPFJetAve200_v10', 
        'HLT_DiPFJetAve260_v10', 
        'HLT_DiPFJetAve320_v10', 
        'HLT_DiPFJetAve400_v10', 
        'HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v10', 
        'HLT_DoubleJet20_ForwardBackward_v4', 
        'HLT_DiJet80_DiJet60_DiJet20_v6', 
        'HLT_DiPFJet40_PFMETnoMu65_MJJ800VBF_AllJets_v9', 
        'HLT_DiPFJet40_PFMETnoMu65_MJJ600VBF_LeadingJets_v9', 
        'HLT_DiJet40Eta2p6_BTagIP3DFastPV_v7', 
        'HLT_DiJet80Eta2p6_BTagIP3DFastPVLoose_v7', 
        'HLT_Jet60Eta1p7_Jet53Eta1p7_DiBTagIP3DFastPV_v7', 
        'HLT_Jet80Eta1p7_Jet70Eta1p7_DiBTagIP3DFastPV_v7', 
        'HLT_Jet160Eta2p4_Jet120Eta2p4_DiBTagIP3DFastPVLoose_v7', 
        'HLT_QuadJet45_v1', 
        'HLT_QuadJet50_v5', 
        'HLT_QuadJet60_DiJet20_v6', 
        'HLT_QuadJet70_v6', 
        'HLT_QuadJet80_v6', 
        'HLT_QuadJet90_v6', 
        'HLT_QuadJet75_55_35_20_BTagIP_VBF_v7', 
        'HLT_QuadJet75_55_38_20_BTagIP_VBF_v7', 
        'HLT_QuadJet75_55_35_20_VBF_v1', 
        'HLT_QuadPFJet78_61_44_31_BTagCSV_VBF_v6', 
        'HLT_QuadPFJet78_61_44_31_VBF_v1', 
        'HLT_QuadPFJet82_65_48_35_BTagCSV_VBF_v6', 
        'HLT_SixJet35_v6', 
        'HLT_SixJet45_v6', 
        'HLT_SixJet50_v6', 
        'HLT_EightJet30_eta3p0_v5', 
        'HLT_EightJet35_eta3p0_v5', 
        'HLT_ExclDiJet35_HFOR_v4', 
        'HLT_ExclDiJet35_HFAND_v4', 
        'HLT_ExclDiJet80_HFAND_v4', 
        'HLT_JetE30_NoBPTX_v14', 
        'HLT_JetE30_NoBPTX3BX_NoHalo_v16', 
        'HLT_JetE50_NoBPTX3BX_NoHalo_v13', 
        'HLT_JetE70_NoBPTX3BX_NoHalo_v5', 
        'HLT_HT200_AlphaT0p57_v8', 
        'HLT_HT200_v6', 
        'HLT_HT250_AlphaT0p55_v8', 
        'HLT_HT250_AlphaT0p57_v8', 
        'HLT_HT250_v7', 
        'HLT_HT300_AlphaT0p53_v8', 
        'HLT_HT300_AlphaT0p54_v14', 
        'HLT_HT300_v7', 
        'HLT_HT300_DoubleDisplacedPFJet60_v10', 
        'HLT_HT300_DoubleDisplacedPFJet60_ChgFraction10_v10', 
        'HLT_HT300_SingleDisplacedPFJet60_v10', 
        'HLT_HT300_SingleDisplacedPFJet60_ChgFraction10_v10', 
        'HLT_HT350_v7', 
        'HLT_HT350_AlphaT0p52_v8', 
        'HLT_HT350_AlphaT0p53_v19', 
        'HLT_HT400_v7', 
        'HLT_HT400_AlphaT0p51_v19', 
        'HLT_HT400_AlphaT0p52_v14', 
        'HLT_HT450_AlphaT0p51_v14', 
        'HLT_HT450_v7', 
        'HLT_HT500_v7', 
        'HLT_HT550_v7', 
        'HLT_HT650_v7', 
        'HLT_HT650_Track50_dEdx3p6_v10', 
        'HLT_HT650_Track60_dEdx3p7_v10', 
        'HLT_HT750_v7', 
        'HLT_PFNoPUHT350_v4', 
        'HLT_PFNoPUHT650_v4', 
        'HLT_PFNoPUHT650_DiCentralPFNoPUJet80_CenPFNoPUJet40_v4', 
        'HLT_PFNoPUHT700_v4', 
        'HLT_PFNoPUHT750_v4', 
        'HLT_PFMET150_v7', 
        'HLT_PFMET180_v7', 
        'HLT_DiCentralJetSumpT100_dPhi05_DiCentralPFJet60_25_PFMET100_HBHENoiseCleaned_v5', 
        'HLT_DiCentralPFJet30_PFMET80_v6', 
        'HLT_DiCentralPFNoPUJet50_PFMETORPFMETNoMu80_v4', 
        'HLT_DiCentralPFJet30_PFMET80_BTagCSV07_v5', 
        'HLT_DiPFJet80_DiPFJet30_BTagCSVd07d05d03_v5', 
        'HLT_DiPFJet80_DiPFJet30_BTagCSVd07d05d05_v5', 
        'HLT_DiPFJet80_DiPFJet30_BTagCSVd07d05_v5', 
        'HLT_MET80_v5', 
        'HLT_MET80_Parked_v5', 
        'HLT_MET80_Track50_dEdx3p6_v6', 
        'HLT_MET80_Track60_dEdx3p7_v6', 
        'HLT_MET120_v13', 
        'HLT_MET120_HBHENoiseCleaned_v6', 
        'HLT_MET200_v12', 
        'HLT_MET200_HBHENoiseCleaned_v5', 
        'HLT_MET300_v4', 
        'HLT_MET300_HBHENoiseCleaned_v5', 
        'HLT_MET400_v7', 
        'HLT_MET400_HBHENoiseCleaned_v5', 
        'HLT_L1SingleMuOpen_v7', 
        'HLT_L1SingleMu12_v2', 
        'HLT_L2Mu70_2Cha_eta2p1_PFMET55_v2', 
        'HLT_L2Mu70_2Cha_eta2p1_PFMET60_v2', 
        'HLT_L2Mu20_eta2p1_NoVertex_v2', 
        'HLT_L2Mu10_NoVertex_NoBPTX3BX_NoHalo_v4', 
        'HLT_L2Mu20_NoVertex_2Cha_NoBPTX3BX_NoHalo_v1', 
        'HLT_L2Mu30_NoVertex_2Cha_NoBPTX3BX_NoHalo_v1', 
        'HLT_L2TripleMu10_0_0_NoVertex_PFJet40Neutral_v8', 
        'HLT_DoubleDisplacedMu4_DiPFJet40Neutral_v8', 
        'HLT_Mu5_v20', 
        'HLT_Mu8_v18', 
        'HLT_Mu12_v18', 
        'HLT_Mu17_v5', 
        'HLT_Mu12_eta2p1_L1Mu10erJetC12WdEtaPhi1DiJetsC_v7', 
        'HLT_Mu15_eta2p1_L1Mu10erJetC12WdEtaPhi1DiJetsC_v3', 
        'HLT_Mu15_eta2p1_v5', 
        'HLT_Mu24_v16', 
        'HLT_Mu24_eta2p1_v5', 
        'HLT_Mu30_v16', 
        'HLT_Mu30_eta2p1_v5', 
        'HLT_Mu40_v14', 
        'HLT_Mu40_eta2p1_v11', 
        'HLT_Mu50_eta2p1_v8', 
        'HLT_RelIso1p0Mu5_v6', 
        'HLT_RelIso1p0Mu20_v3', 
        'HLT_IsoMu20_eta2p1_v7', 
        'HLT_IsoMu24_v17', 
        'HLT_IsoMu24_eta2p1_v15', 
        'HLT_IsoMu30_v11', 
        'HLT_IsoMu30_eta2p1_v15', 
        'HLT_IsoMu34_eta2p1_v13', 
        'HLT_IsoMu40_eta2p1_v10', 
        'HLT_Mu40_eta2p1_Track50_dEdx3p6_v5', 
        'HLT_Mu40_eta2p1_Track60_dEdx3p7_v5', 
        'HLT_L2DoubleMu23_NoVertex_v11', 
        'HLT_L2DoubleMu23_NoVertex_2Cha_Angle2p5_v3', 
        'HLT_L2DoubleMu38_NoVertex_2Cha_Angle2p5_v3', 
        'HLT_DoubleMu11_Acoplanarity03_v5', 
        'HLT_DoubleMu4_Jpsi_Displaced_v12', 
        'HLT_DoubleMu4_JpsiTk_Displaced_v6', 
        'HLT_DoubleMu3p5_LowMass_Displaced_v6', 
        'HLT_DoubleMu3p5_LowMassNonResonant_Displaced_v6', 
        'HLT_Dimuon0_Jpsi_v17', 
        'HLT_Dimuon0_Jpsi_NoVertexing_v14', 
        'HLT_Dimuon0_Upsilon_v17', 
        'HLT_Dimuon0_PsiPrime_v6', 
        'HLT_Dimuon5_Upsilon_v6', 
        'HLT_Dimuon5_PsiPrime_v6', 
        'HLT_Dimuon7_Upsilon_v7', 
        'HLT_Dimuon7_PsiPrime_v3', 
        'HLT_Dimuon8_Jpsi_v7', 
        'HLT_Dimuon8_Upsilon_v6', 
        'HLT_Dimuon10_Jpsi_v6', 
        'HLT_Dimuon11_Upsilon_v6', 
        'HLT_Dimuon0_Jpsi_Muon_v18', 
        'HLT_Dimuon0_Upsilon_Muon_v18', 
        'HLT_Dimuon3p5_SameSign_v6', 
        'HLT_DoubleMu4_Acoplanarity03_v5', 
        'HLT_Tau2Mu_ItTrack_v7', 
        'HLT_Mu13_Mu8_v22', 
        'HLT_Mu17_Mu8_v22', 
        'HLT_Mu13_Mu8_NoDZ_v1', 
        'HLT_Mu17_TkMu8_v14', 
        'HLT_Mu17_TkMu8_NoDZ_v1', 
        'HLT_Mu22_TkMu8_v9', 
        'HLT_Mu22_TkMu22_v9', 
        'HLT_TripleMu5_v19', 
        'HLT_DoubleMu5_IsoMu5_v20', 
        'HLT_Mu5_L2Mu3_Jpsi_v8', 
        'HLT_Mu5_Track2_Jpsi_v21', 
        'HLT_Mu5_Track3p5_Jpsi_v7', 
        'HLT_Mu7_Track7_Jpsi_v20', 
        'HLT_Mu15_TkMu5_Onia_v1', 
        'HLT_BTagMu_Jet20_Mu4_v2', 
        'HLT_BTagMu_Jet60_Mu4_v2', 
        'HLT_Photon20_CaloIdVL_IsoL_v16', 
        'HLT_Photon22_R9Id90_HE10_Iso40_EBOnly_v5', 
        'HLT_Photon26_Photon18_v12', 
        'HLT_Photon26_R9Id85_OR_CaloId10_Iso50_Photon18_R9Id85_OR_CaloId10_Iso50_Mass70_v2', 
        'HLT_Photon26_R9Id85_OR_CaloId10_Iso50_Photon18_v5', 
        'HLT_Photon30_v1', 
        'HLT_Photon30_CaloIdVL_v14', 
        'HLT_Photon30_R9Id90_CaloId_HE10_Iso40_EBOnly_v1', 
        'HLT_Photon30_R9Id90_CaloId_HE10_Iso40_EBOnly_Met25_HBHENoiseCleaned_v1', 
        'HLT_Photon36_R9Id90_HE10_Iso40_EBOnly_v5', 
        'HLT_Photon36_Photon22_v6', 
        'HLT_Photon36_R9Id85_Photon22_R9Id85_v4', 
        'HLT_Photon36_R9Id85_Photon22_CaloId10_Iso50_v6', 
        'HLT_Photon36_CaloId10_Iso50_Photon22_R9Id85_v6', 
        'HLT_Photon36_CaloId10_Iso50_Photon22_CaloId10_Iso50_v6', 
        'HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon22_R9Id85_OR_CaloId10_Iso50_v6', 
        'HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon22_v5', 
        'HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon10_R9Id85_OR_CaloId10_Iso50_Mass80_v1', 
        'HLT_Photon50_CaloIdVL_v10', 
        'HLT_Photon50_CaloIdVL_IsoL_v17', 
        'HLT_Photon50_R9Id90_HE10_Iso40_EBOnly_v5', 
        'HLT_Photon60_CaloIdL_MHT70_v11', 
        'HLT_Photon60_CaloIdL_HT300_v4', 
        'HLT_Photon70_CaloIdXL_PFNoPUHT400_v4', 
        'HLT_Photon70_CaloIdXL_PFNoPUHT500_v4', 
        'HLT_Photon70_CaloIdXL_PFMET100_v7', 
        'HLT_Photon75_CaloIdVL_v13', 
        'HLT_Photon75_R9Id90_HE10_Iso40_EBOnly_v5', 
        'HLT_Photon90_CaloIdVL_v10', 
        'HLT_Photon90_R9Id90_HE10_Iso40_EBOnly_v5', 
        'HLT_DisplacedPhoton65_CaloIdVL_IsoL_PFMET25_v4', 
        'HLT_DisplacedPhoton65EBOnly_CaloIdVL_IsoL_PFMET30_v4', 
        'HLT_Photon135_v7', 
        'HLT_Photon150_v4', 
        'HLT_Photon160_v4', 
        'HLT_Photon300_NoHE_v5', 
        'HLT_DoublePhoton48_HEVT_v8', 
        'HLT_DoublePhoton53_HEVT_v2', 
        'HLT_DoublePhoton70_v6', 
        'HLT_DoublePhoton80_v7', 
        'HLT_L1SingleEG5_v6', 
        'HLT_L1SingleEG12_v6', 
        'HLT_L1DoubleEG3_FwdVeto_v2', 
        'HLT_L1ETM30_v2', 
        'HLT_L1ETM40_v2', 
        'HLT_L1ETM70_v2', 
        'HLT_L1ETM100_v2', 
        'HLT_Ele8_CaloIdT_TrkIdVL_v5', 
        'HLT_Ele8_CaloIdT_TrkIdVL_EG7_v2', 
        'HLT_Ele8_CaloIdT_TrkIdVL_Jet30_v7', 
        'HLT_Ele8_CaloIdL_CaloIsoVL_v17', 
        'HLT_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v15', 
        'HLT_Ele17_CaloIdL_CaloIsoVL_v17', 
        'HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v6', 
        'HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v19', 
        'HLT_Ele17_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_Ele8_Mass50_v6', 
        'HLT_Ele20_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_SC4_Mass50_v7', 
        'HLT_Ele22_CaloIdL_CaloIsoVL_v6', 
        'HLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_v11', 
        'HLT_Ele27_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele15_CaloIdT_CaloIsoVL_trackless_v8', 
        'HLT_Ele27_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_HFT15_v8', 
        'HLT_Ele23_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_HFT30_v8', 
        'HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30_v4', 
        'HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet50_40_30_v4', 
        'HLT_Ele27_WP80_v11', 
        'HLT_Ele27_WP80_PFMET_MT50_v7', 
        'HLT_Ele30_CaloIdVT_TrkIdT_v6', 
        'HLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_v11', 
        'HLT_Ele32_CaloIdT_CaloIsoT_TrkIdT_TrkIsoT_SC17_Mass50_v6', 
        'HLT_Ele80_CaloIdVT_GsfTrkIdT_v2', 
        'HLT_Ele90_CaloIdVT_GsfTrkIdT_v2', 
        'HLT_DoubleEle8_CaloIdT_TrkIdVL_v12', 
        'HLT_DoubleEle33_CaloIdL_v14', 
        'HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_v7', 
        'HLT_DoubleEle33_CaloIdT_v10', 
        'HLT_Ele15_Ele8_Ele5_CaloIdL_TrkIdVL_v6', 
        'HLT_LooseIsoPFTau35_Trk20_Prong1_v10', 
        'HLT_LooseIsoPFTau35_Trk20_Prong1_MET70_v10', 
        'HLT_LooseIsoPFTau35_Trk20_Prong1_MET75_v10', 
        'HLT_IsoMu15_eta2p1_LooseIsoPFTau35_Trk20_Prong1_L1ETM20_v10', 
        'HLT_IsoMu8_eta2p1_LooseIsoPFTau20_L1ETM26_v1', 
        'HLT_IsoMu8_eta2p1_LooseIsoPFTau20_v1', 
        'HLT_Mu8_eta2p1_LooseIsoPFTau20_L1ETM26_v1', 
        'HLT_Ele13_eta2p1_WP90Rho_LooseIsoPFTau20_L1ETM36_v1', 
        'HLT_Ele13_eta2p1_WP90NoIso_LooseIsoPFTau20_L1ETM36_v1', 
        'HLT_Ele13_eta2p1_WP90Rho_LooseIsoPFTau20_v1', 
        'HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_Jet30_v5', 
        'HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_v4', 
        'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Prong1_v4', 
        'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_v4', 
        'HLT_IsoMu18_eta2p1_MediumIsoPFTau25_Trk1_eta2p1_v4', 
        'HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_Reg_Jet30_v1', 
        'HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_Reg_v1', 
        'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Prong1_Reg_v1', 
        'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Reg_v1', 
        'HLT_IsoMu18_eta2p1_MediumIsoPFTau25_Trk1_eta2p1_Reg_v1', 
        'HLT_DoubleIsoL2Tau30_eta2p1_v1', 
        'HLT_BTagMu_DiJet20_Mu5_v6', 
        'HLT_BTagMu_DiJet40_Mu5_v6', 
        'HLT_BTagMu_DiJet70_Mu5_v6', 
        'HLT_BTagMu_DiJet110_Mu5_v6', 
        'HLT_BTagMu_Jet300_Mu5_v6', 
        'HLT_Mu7_Ele7_CaloIdT_CaloIsoVL_v7', 
        'HLT_Mu8_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v9', 
        'HLT_Mu8_DiJet30_v7', 
        'HLT_Mu8_TriJet30_v7', 
        'HLT_Mu8_QuadJet30_v7', 
        'HLT_IsoMu12_DoubleCentralJet65_v4', 
        'HLT_Mu15_eta2p1_L1ETM20_v5', 
        'HLT_IsoMu18_CentralPFJet30_CentralPFJet25_v1', 
        'HLT_IsoMu18_PFJet30_PFJet25_Deta3_v1', 
        'HLT_Mu18_CentralPFJet30_CentralPFJet25_v1', 
        'HLT_Mu18_PFJet30_PFJet25_Deta3_CentralPFJet25_v1', 
        'HLT_IsoMu18_CentralPFJet30_CentralPFJet25_PFMET20_v1', 
        'HLT_IsoMu18_PFJet30_PFJet25_Deta3_CentralPFJet25_v1', 
        'HLT_Ele24_WP80_CentralPFJet35_CentralPFJet25_v1', 
        'HLT_Ele24_WP80_PFJet30_PFJet25_Deta3_v1', 
        'HLT_Ele24_WP80_PFJet30_PFJet25_Deta3_CentralPFJet30_v1', 
        'HLT_Ele24_WP80_CentralPFJet35_CentralPFJet25_PFMET20_v1', 
        'HLT_IsoMu17_eta2p1_CentralPFNoPUJet30_BTagIPIter_v4', 
        'HLT_IsoMu17_eta2p1_CentralPFNoPUJet30_v4', 
        'HLT_IsoMu17_eta2p1_DiCentralPFNoPUJet30_v4', 
        'HLT_IsoMu17_eta2p1_TriCentralPFNoPUJet30_v4', 
        'HLT_Mu17_eta2p1_CentralPFNoPUJet30_BTagIPIter_v4', 
        'HLT_Mu17_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v9', 
        'HLT_Mu12_eta2p1_DiCentral_40_20_DiBTagIP3D1stTrack_v8', 
        'HLT_Mu12_eta2p1_DiCentral_40_20_BTagIP3D1stTrack_v8', 
        'HLT_Mu12_eta2p1_DiCentral_40_20_v8', 
        'HLT_Mu12_eta2p1_DiCentral_20_v8', 
        'HLT_Mu15_eta2p1_DiCentral_40_20_v1', 
        'HLT_Mu15_eta2p1_DiCentral_20_v1', 
        'HLT_Mu15_eta2p1_TriCentral_40_20_20_DiBTagIP3D1stTrack_v8', 
        'HLT_Mu15_eta2p1_TriCentral_40_20_20_BTagIP3D1stTrack_v8', 
        'HLT_Mu15_eta2p1_TriCentral_40_20_20_v8', 
        'HLT_Mu30_Ele30_CaloIdL_v8', 
        'HLT_IsoMu17_eta2p1_DiCentralPFNoPUJet30_PFNoPUHT350_PFMHT40_v3', 
        'HLT_IsoMu20_eta2p1_CentralPFJet80_v9', 
        'HLT_DoubleRelIso1p0Mu5_Mass8_PFNoPUHT175_v4', 
        'HLT_DoubleRelIso1p0Mu5_Mass8_PFNoPUHT225_v4', 
        'HLT_DoubleMu8_Mass8_PFNoPUHT175_v4', 
        'HLT_DoubleMu8_Mass8_PFNoPUHT225_v4', 
        'HLT_RelIso1p0Mu5_Ele8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT175_v4', 
        'HLT_RelIso1p0Mu5_Ele8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT225_v4', 
        'HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT175_v4', 
        'HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT225_v4', 
        'HLT_PFNoPUHT350_Mu15_PFMET45_v4', 
        'HLT_PFNoPUHT350_Mu15_PFMET50_v4', 
        'HLT_PFNoPUHT400_Mu5_PFMET45_v4', 
        'HLT_PFNoPUHT400_Mu5_PFMET50_v4', 
        'HLT_Mu40_PFNoPUHT350_v4', 
        'HLT_Mu60_PFNoPUHT350_v4', 
        'HLT_DoubleMu5_Ele8_CaloIdT_TrkIdVL_v16', 
        'HLT_DoubleMu8_Ele8_CaloIdT_TrkIdVL_v5', 
        'HLT_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Jet30_v7', 
        'HLT_Ele8_CaloIdT_TrkIdT_DiJet30_v18', 
        'HLT_Ele8_CaloIdT_TrkIdT_TriJet30_v18', 
        'HLT_Ele8_CaloIdT_TrkIdT_QuadJet30_v18', 
        'HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Jet30_v7', 
        'HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_CentralPFNoPUJet30_v8', 
        'HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_DiCentralPFNoPUJet30_v2', 
        'HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_CentralPFNoPUJet30_BTagIPIter_v9', 
        'HLT_Ele27_WP80_CentralPFJet80_v9', 
        'HLT_Ele30_CaloIdVT_TrkIdT_PFNoPUJet100_PFNoPUJet25_v8', 
        'HLT_Ele30_CaloIdVT_TrkIdT_PFNoPUJet150_PFNoPUJet25_v8', 
        'HLT_DoubleEle8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT175_v4', 
        'HLT_DoubleEle8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT225_v4', 
        'HLT_DoubleEle10_CaloIdL_TrkIdVL_Ele10_CaloIdT_TrkIdVL_v12', 
        'HLT_TripleEle10_CaloIdL_TrkIdVL_v18', 
        'HLT_RsqMR40_Rsq0p04_v6', 
        'HLT_RsqMR45_Rsq0p09_v5', 
        'HLT_RsqMR55_Rsq0p09_MR150_v6', 
        'HLT_RsqMR60_Rsq0p09_MR150_v6', 
        'HLT_RsqMR65_Rsq0p09_MR150_v5', 
        'HLT_IsoMu12_RsqMR30_Rsq0p04_MR200_v4', 
        'HLT_IsoMu12_RsqMR40_Rsq0p04_MR200_v4', 
        'HLT_Ele12_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_RsqMR30_Rsq0p04_MR200_v4', 
        'HLT_Ele12_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_RsqMR40_Rsq0p04_MR200_v4', 
        'HLT_Ele12_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_DoubleCentralJet65_v4', 
        'HLT_Photon40_CaloIdL_RsqMR40_Rsq0p09_MR150_v6', 
        'HLT_Photon40_CaloIdL_RsqMR45_Rsq0p09_MR150_v6', 
        'HLT_Photon40_CaloIdL_RsqMR50_Rsq0p09_MR150_v6', 
        'HLT_DoublePhoton40_CaloIdL_Rsq0p035_v6', 
        'HLT_DoublePhoton40_CaloIdL_Rsq0p06_v6', 
        'HLT_Mu22_Photon22_CaloIdL_v7', 
        'HLT_Mu8_DoubleEle8_CaloIdT_TrkIdVL_v7', 
        'HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Ele8_CaloIdL_TrkIdVL_v7', 
        'HLT_DoubleMu14_Mass8_PFMET40_v8', 
        'HLT_DoubleMu14_Mass8_PFMET50_v8', 
        'HLT_DoubleEle14_CaloIdT_TrkIdVL_Mass8_PFMET40_v8', 
        'HLT_DoubleEle14_CaloIdT_TrkIdVL_Mass8_PFMET50_v8', 
        'HLT_Mu14_Ele14_CaloIdT_TrkIdVL_Mass8_PFMET40_v8', 
        'HLT_Mu14_Ele14_CaloIdT_TrkIdVL_Mass8_PFMET50_v8', 
        'HLT_PFNoPUHT350_PFMET100_v4', 
        'HLT_PFNoPUHT400_PFMET100_v4', 
        'HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v3', 
        'HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v3', 
        'HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v3', 
        'HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v3', 
        'HLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT_v3', 
        'HLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT_v3', 
        'HLT_Ele5_SC5_Jpsi_Mass2to15_v4', 
        'HLT_DiJet35_MJJ650_AllJets_DEta3p5_VBF_v5', 
        'HLT_DiJet35_MJJ700_AllJets_DEta3p5_VBF_v5', 
        'HLT_DiJet35_MJJ750_AllJets_DEta3p5_VBF_v5', 
        'HLT_Ele22_eta2p1_WP90Rho_LooseIsoPFTau20_v7', 
        'HLT_Ele22_eta2p1_WP90NoIso_LooseIsoPFTau20_v7', 
        'HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v7', 
        'HLT_Mu17_eta2p1_LooseIsoPFTau20_v7', 
        'HLT_PixelTracks_Multiplicity70_v3', 
        'HLT_PixelTracks_Multiplicity80_v12', 
        'HLT_PixelTracks_Multiplicity90_v3', 
        'DST_HT250_v4', 
        'DST_L1HTT_Or_L1MultiJet_v4', 
        'DST_Mu5_HT250_v4', 
        'DST_Ele8_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT250_v4', 
        'HLT_BeamGas_HF_Beam1_v5', 
        'HLT_BeamGas_HF_Beam2_v5', 
        'HLT_BeamHalo_v13', 
        'HLT_HcalUTCA_v1', 
        'HLT_IsoTrackHE_v15', 
        'HLT_IsoTrackHB_v14', 
        'HLT_HcalPhiSym_v11', 
        'HLT_HcalNZS_v10', 
        'HLT_GlobalRunHPDNoise_v8', 
        'HLT_L1Tech_HBHEHO_totalOR_v6', 
        'HLT_L1Tech_HCAL_HF_single_channel_v4', 
        'HLT_ZeroBias_v7', 
        'HLT_ZeroBiasPixel_DoubleTrack_v2', 
        'HLT_Physics_v5 / 500', 
        'HLT_HcalCalibration_v3', 
        'HLT_Random_v2', 
        'HLT_L1SingleMuOpen_AntiBPTX_v7', 
        'HLT_L1TrackerCosmics_v7', 
        'HLT_DTErrors_v3', 
        'HLT_L1DoubleJet36Central_v7', 
        'AlCa_EcalPi0EBonly_v6 / 100', 
        'AlCa_EcalPi0EEonly_v6 / 100', 
        'AlCa_EcalEtaEBonly_v6 / 100', 
        'AlCa_EcalEtaEEonly_v6 / 100', 
        'AlCa_EcalPhiSym_v13 / 100', 
        'AlCa_RPCMuonNoTriggers_v9 / 100', 
        'AlCa_RPCMuonNoHits_v9 / 100', 
        'AlCa_RPCMuonNormalisation_v9 / 100', 
        'AlCa_LumiPixels_v8 / 100', 
        'AlCa_LumiPixels_ZeroBias_v4 / 100', 
        'AlCa_LumiPixels_Random_v1 / 100', 
        'HLT_LogMonitor_v4' ) ),
    throw = cms.bool(True),
    daqPartitions = cms.uint32(1),
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT")
)


process.hltPreMu17Mu8 = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtDigis"),
    offset = cms.uint32(0)
)


process.hltPreNanoDSTOutput = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtDigis"),
    offset = cms.uint32(0)
)


process.hltPrePhysicsDSTOutputSmart = cms.EDFilter("TriggerResultsFilter",
    l1tIgnoreMask = cms.bool(False),
    l1tResults = cms.InputTag("hltGtDigis"),
    l1techIgnorePrescales = cms.bool(False),
    hltResults = cms.InputTag("TriggerResults"),
    triggerConditions = cms.vstring('DST_HT250_v4', 
        'DST_L1HTT_Or_L1MultiJet_v4', 
        'DST_Mu5_HT250_v4', 
        'DST_Ele8_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT250_v4'),
    throw = cms.bool(True),
    daqPartitions = cms.uint32(1)
)


process.hltPreRPCMONOutput = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtDigis"),
    offset = cms.uint32(0)
)


process.hltPreTrackerCalibrationOutput = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtDigis"),
    offset = cms.uint32(0)
)


process.hltTriggerType = cms.EDFilter("HLTTriggerTypeFilter",
    SelectedTriggerType = cms.int32(1)
)


process.hltOutputA = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('RAW')
    ),
    fileName = cms.untracked.string('outputA.root'),
    fastCloning = cms.untracked.bool(False),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring( ('HLT_Activity_Ecal_SC7_v13', 
            'HLT_BTagMu_DiJet110_Mu5_v6', 
            'HLT_BTagMu_DiJet20_Mu5_v6', 
            'HLT_BTagMu_DiJet40_Mu5_v6', 
            'HLT_BTagMu_DiJet70_Mu5_v6', 
            'HLT_BTagMu_Jet20_Mu4_v2', 
            'HLT_BTagMu_Jet300_Mu5_v6', 
            'HLT_BTagMu_Jet60_Mu4_v2', 
            'HLT_BeamGas_HF_Beam1_v5', 
            'HLT_BeamGas_HF_Beam2_v5', 
            'HLT_BeamHalo_v13', 
            'HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v3', 
            'HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v3', 
            'HLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT_v3', 
            'HLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT_v3', 
            'HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v3', 
            'HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v3', 
            'HLT_DTErrors_v3', 
            'HLT_DiCentralJetSumpT100_dPhi05_DiCentralPFJet60_25_PFMET100_HBHENoiseCleaned_v5', 
            'HLT_DiCentralPFJet30_PFMET80_BTagCSV07_v5', 
            'HLT_DiCentralPFJet30_PFMET80_v6', 
            'HLT_DiCentralPFNoPUJet50_PFMETORPFMETNoMu80_v4', 
            'HLT_DiJet20_MJJ650_AllJets_DEta3p5_HT120_VBF_v1', 
            'HLT_DiJet30_MJJ700_AllJets_DEta3p5_VBF_v1', 
            'HLT_DiJet35_MJJ650_AllJets_DEta3p5_VBF_v5', 
            'HLT_DiJet35_MJJ700_AllJets_DEta3p5_VBF_v5', 
            'HLT_DiJet35_MJJ750_AllJets_DEta3p5_VBF_v5', 
            'HLT_DiJet40Eta2p6_BTagIP3DFastPV_v7', 
            'HLT_DiJet80Eta2p6_BTagIP3DFastPVLoose_v7', 
            'HLT_DiJet80_DiJet60_DiJet20_v6', 
            'HLT_DiPFJet40_PFMETnoMu65_MJJ600VBF_LeadingJets_v9', 
            'HLT_DiPFJet40_PFMETnoMu65_MJJ800VBF_AllJets_v9', 
            'HLT_DiPFJet80_DiPFJet30_BTagCSVd07d05_v5', 
            'HLT_DiPFJet80_DiPFJet30_BTagCSVd07d05d03_v5', 
            'HLT_DiPFJet80_DiPFJet30_BTagCSVd07d05d05_v5', 
            'HLT_DiPFJetAve140_v10', 
            'HLT_DiPFJetAve200_v10', 
            'HLT_DiPFJetAve260_v10', 
            'HLT_DiPFJetAve320_v10', 
            'HLT_DiPFJetAve400_v10', 
            'HLT_DiPFJetAve40_v9', 
            'HLT_DiPFJetAve80_v10', 
            'HLT_Dimuon0_Jpsi_Muon_v18', 
            'HLT_Dimuon0_Jpsi_NoVertexing_v14', 
            'HLT_Dimuon0_Jpsi_v17', 
            'HLT_Dimuon0_PsiPrime_v6', 
            'HLT_Dimuon0_Upsilon_Muon_v18', 
            'HLT_Dimuon0_Upsilon_v17', 
            'HLT_Dimuon10_Jpsi_v6', 
            'HLT_Dimuon11_Upsilon_v6', 
            'HLT_Dimuon3p5_SameSign_v6', 
            'HLT_Dimuon5_PsiPrime_v6', 
            'HLT_Dimuon5_Upsilon_v6', 
            'HLT_Dimuon7_PsiPrime_v3', 
            'HLT_Dimuon7_Upsilon_v7', 
            'HLT_Dimuon8_Jpsi_v7', 
            'HLT_Dimuon8_Upsilon_v6', 
            'HLT_DisplacedPhoton65EBOnly_CaloIdVL_IsoL_PFMET30_v4', 
            'HLT_DisplacedPhoton65_CaloIdVL_IsoL_PFMET25_v4', 
            'HLT_DoubleDisplacedMu4_DiPFJet40Neutral_v8', 
            'HLT_DoubleEle10_CaloIdL_TrkIdVL_Ele10_CaloIdT_TrkIdVL_v12', 
            'HLT_DoubleEle14_CaloIdT_TrkIdVL_Mass8_PFMET40_v8', 
            'HLT_DoubleEle14_CaloIdT_TrkIdVL_Mass8_PFMET50_v8', 
            'HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_v7', 
            'HLT_DoubleEle33_CaloIdL_v14', 
            'HLT_DoubleEle33_CaloIdT_v10', 
            'HLT_DoubleEle8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT175_v4', 
            'HLT_DoubleEle8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT225_v4', 
            'HLT_DoubleEle8_CaloIdT_TrkIdVL_v12', 
            'HLT_DoubleIsoL2Tau30_eta2p1_v1', 
            'HLT_DoubleJet20_ForwardBackward_v4', 
            'HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_Jet30_v5', 
            'HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_Reg_Jet30_v1', 
            'HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_Reg_v1', 
            'HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_v4', 
            'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Prong1_Reg_v1', 
            'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Prong1_v4', 
            'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Reg_v1', 
            'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_v4', 
            'HLT_DoubleMu11_Acoplanarity03_v5', 
            'HLT_DoubleMu14_Mass8_PFMET40_v8', 
            'HLT_DoubleMu14_Mass8_PFMET50_v8', 
            'HLT_DoubleMu3_4_Dimuon5_Bs_Central_v5', 
            'HLT_DoubleMu3p5_4_Dimuon5_Bs_Central_v5', 
            'HLT_DoubleMu3p5_LowMassNonResonant_Displaced_v6', 
            'HLT_DoubleMu3p5_LowMass_Displaced_v6', 
            'HLT_DoubleMu4_Acoplanarity03_v5', 
            'HLT_DoubleMu4_Dimuon7_Bs_Forward_v5', 
            'HLT_DoubleMu4_JpsiTk_Displaced_v6', 
            'HLT_DoubleMu4_Jpsi_Displaced_v12', 
            'HLT_DoubleMu5_Ele8_CaloIdT_TrkIdVL_v16', 
            'HLT_DoubleMu5_IsoMu5_v20', 
            'HLT_DoubleMu8_Ele8_CaloIdT_TrkIdVL_v5', 
            'HLT_DoubleMu8_Mass8_PFNoPUHT175_v4', 
            'HLT_DoubleMu8_Mass8_PFNoPUHT225_v4', 
            'HLT_DoublePhoton40_CaloIdL_Rsq0p035_v6', 
            'HLT_DoublePhoton40_CaloIdL_Rsq0p06_v6', 
            'HLT_DoublePhoton48_HEVT_v8', 
            'HLT_DoublePhoton53_HEVT_v2', 
            'HLT_DoublePhoton70_v6', 
            'HLT_DoublePhoton80_v7', 
            'HLT_DoubleRelIso1p0Mu5_Mass8_PFNoPUHT175_v4', 
            'HLT_DoubleRelIso1p0Mu5_Mass8_PFNoPUHT225_v4', 
            'HLT_EightJet30_eta3p0_v5', 
            'HLT_EightJet35_eta3p0_v5', 
            'HLT_Ele12_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_DoubleCentralJet65_v4', 
            'HLT_Ele12_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_RsqMR30_Rsq0p04_MR200_v4', 
            'HLT_Ele12_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_RsqMR40_Rsq0p04_MR200_v4', 
            'HLT_Ele13_eta2p1_WP90NoIso_LooseIsoPFTau20_L1ETM36_v1', 
            'HLT_Ele13_eta2p1_WP90Rho_LooseIsoPFTau20_L1ETM36_v1', 
            'HLT_Ele13_eta2p1_WP90Rho_LooseIsoPFTau20_v1', 
            'HLT_Ele15_Ele8_Ele5_CaloIdL_TrkIdVL_v6', 
            'HLT_Ele17_CaloIdL_CaloIsoVL_v17', 
            'HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v19', 
            'HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Jet30_v7', 
            'HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v6', 
            'HLT_Ele17_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_Ele8_Mass50_v6', 
            'HLT_Ele20_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_SC4_Mass50_v7', 
            'HLT_Ele22_CaloIdL_CaloIsoVL_v6', 
            'HLT_Ele22_eta2p1_WP90NoIso_LooseIsoPFTau20_v7', 
            'HLT_Ele22_eta2p1_WP90Rho_LooseIsoPFTau20_v7', 
            'HLT_Ele23_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_HFT30_v8', 
            'HLT_Ele24_WP80_CentralPFJet35_CentralPFJet25_PFMET20_v1', 
            'HLT_Ele24_WP80_CentralPFJet35_CentralPFJet25_v1', 
            'HLT_Ele24_WP80_PFJet30_PFJet25_Deta3_CentralPFJet30_v1', 
            'HLT_Ele24_WP80_PFJet30_PFJet25_Deta3_v1', 
            'HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_CentralPFNoPUJet30_BTagIPIter_v9', 
            'HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_CentralPFNoPUJet30_v8', 
            'HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_DiCentralPFNoPUJet30_v2', 
            'HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30_v4', 
            'HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet45_35_25_v2', 
            'HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet50_40_30_v4', 
            'HLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_v11', 
            'HLT_Ele27_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele15_CaloIdT_CaloIsoVL_trackless_v8', 
            'HLT_Ele27_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_HFT15_v8', 
            'HLT_Ele27_WP80_CentralPFJet80_v9', 
            'HLT_Ele27_WP80_PFMET_MT50_v7', 
            'HLT_Ele27_WP80_WCandPt80_v9', 
            'HLT_Ele27_WP80_v11', 
            'HLT_Ele30_CaloIdVT_TrkIdT_PFNoPUJet100_PFNoPUJet25_v8', 
            'HLT_Ele30_CaloIdVT_TrkIdT_PFNoPUJet150_PFNoPUJet25_v8', 
            'HLT_Ele30_CaloIdVT_TrkIdT_v6', 
            'HLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_v11', 
            'HLT_Ele32_CaloIdT_CaloIsoT_TrkIdT_TrkIsoT_SC17_Mass50_v6', 
            'HLT_Ele5_SC5_Jpsi_Mass2to15_v4', 
            'HLT_Ele80_CaloIdVT_GsfTrkIdT_v2', 
            'HLT_Ele8_CaloIdL_CaloIsoVL_v17', 
            'HLT_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Jet30_v7', 
            'HLT_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v15', 
            'HLT_Ele8_CaloIdT_TrkIdT_DiJet30_v18', 
            'HLT_Ele8_CaloIdT_TrkIdT_QuadJet30_v18', 
            'HLT_Ele8_CaloIdT_TrkIdT_TriJet30_v18', 
            'HLT_Ele8_CaloIdT_TrkIdVL_EG7_v2', 
            'HLT_Ele8_CaloIdT_TrkIdVL_Jet30_v7', 
            'HLT_Ele8_CaloIdT_TrkIdVL_v5', 
            'HLT_Ele90_CaloIdVT_GsfTrkIdT_v2', 
            'HLT_ExclDiJet35_HFAND_v4', 
            'HLT_ExclDiJet35_HFOR_v4', 
            'HLT_ExclDiJet80_HFAND_v4', 
            'HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v10', 
            'HLT_GlobalRunHPDNoise_v8', 
            'HLT_HT200_AlphaT0p57_v8', 
            'HLT_HT200_v6', 
            'HLT_HT250_AlphaT0p55_v8', 
            'HLT_HT250_AlphaT0p57_v8', 
            'HLT_HT250_v7', 
            'HLT_HT300_AlphaT0p53_v8', 
            'HLT_HT300_AlphaT0p54_v14', 
            'HLT_HT300_DoubleDisplacedPFJet60_ChgFraction10_v10', 
            'HLT_HT300_DoubleDisplacedPFJet60_v10', 
            'HLT_HT300_SingleDisplacedPFJet60_ChgFraction10_v10', 
            'HLT_HT300_SingleDisplacedPFJet60_v10', 
            'HLT_HT300_v7', 
            'HLT_HT350_AlphaT0p52_v8', 
            'HLT_HT350_AlphaT0p53_v19', 
            'HLT_HT350_v7', 
            'HLT_HT400_AlphaT0p51_v19', 
            'HLT_HT400_AlphaT0p52_v14', 
            'HLT_HT400_v7', 
            'HLT_HT450_AlphaT0p51_v14', 
            'HLT_HT450_v7', 
            'HLT_HT500_v7', 
            'HLT_HT550_v7', 
            'HLT_HT650_Track50_dEdx3p6_v10', 
            'HLT_HT650_Track60_dEdx3p7_v10', 
            'HLT_HT650_v7', 
            'HLT_HT750_v7', 
            'HLT_HcalNZS_v10', 
            'HLT_HcalPhiSym_v11', 
            'HLT_HcalUTCA_v1', 
            'HLT_IsoMu12_DoubleCentralJet65_v4', 
            'HLT_IsoMu12_RsqMR30_Rsq0p04_MR200_v4', 
            'HLT_IsoMu12_RsqMR40_Rsq0p04_MR200_v4', 
            'HLT_IsoMu15_eta2p1_L1ETM20_v7', 
            'HLT_IsoMu15_eta2p1_LooseIsoPFTau35_Trk20_Prong1_L1ETM20_v10', 
            'HLT_IsoMu17_eta2p1_CentralPFNoPUJet30_BTagIPIter_v4', 
            'HLT_IsoMu17_eta2p1_CentralPFNoPUJet30_v4', 
            'HLT_IsoMu17_eta2p1_DiCentralPFNoPUJet30_PFNoPUHT350_PFMHT40_v3', 
            'HLT_IsoMu17_eta2p1_DiCentralPFNoPUJet30_v4', 
            'HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v7', 
            'HLT_IsoMu17_eta2p1_TriCentralPFNoPUJet30_v4', 
            'HLT_IsoMu17_eta2p1_TriCentralPFNoPUJet45_35_25_v2', 
            'HLT_IsoMu18_CentralPFJet30_CentralPFJet25_PFMET20_v1', 
            'HLT_IsoMu18_CentralPFJet30_CentralPFJet25_v1', 
            'HLT_IsoMu18_PFJet30_PFJet25_Deta3_CentralPFJet25_v1', 
            'HLT_IsoMu18_PFJet30_PFJet25_Deta3_v1', 
            'HLT_IsoMu18_eta2p1_MediumIsoPFTau25_Trk1_eta2p1_Reg_v1', 
            'HLT_IsoMu18_eta2p1_MediumIsoPFTau25_Trk1_eta2p1_v4', 
            'HLT_IsoMu20_WCandPt80_v4', 
            'HLT_IsoMu20_eta2p1_CentralPFJet80_v9', 
            'HLT_IsoMu20_eta2p1_v7', 
            'HLT_IsoMu24_eta2p1_v15', 
            'HLT_IsoMu24_v17', 
            'HLT_IsoMu30_eta2p1_v15', 
            'HLT_IsoMu30_v11', 
            'HLT_IsoMu34_eta2p1_v13', 
            'HLT_IsoMu40_eta2p1_v10', 
            'HLT_IsoMu8_eta2p1_LooseIsoPFTau20_L1ETM26_v1', 
            'HLT_IsoMu8_eta2p1_LooseIsoPFTau20_v1', 
            'HLT_IsoTrackHB_v14', 
            'HLT_IsoTrackHE_v15', 
            'HLT_Jet160Eta2p4_Jet120Eta2p4_DiBTagIP3DFastPVLoose_v7', 
            'HLT_Jet370_NoJetID_v15', 
            'HLT_Jet60Eta1p7_Jet53Eta1p7_DiBTagIP3DFastPV_v7', 
            'HLT_Jet80Eta1p7_Jet70Eta1p7_DiBTagIP3DFastPV_v7', 
            'HLT_JetE30_NoBPTX3BX_NoHalo_v16', 
            'HLT_JetE30_NoBPTX_v14', 
            'HLT_JetE50_NoBPTX3BX_NoHalo_v13', 
            'HLT_JetE70_NoBPTX3BX_NoHalo_v5', 
            'HLT_L1DoubleEG3_FwdVeto_v2', 
            'HLT_L1DoubleJet36Central_v7', 
            'HLT_L1ETM100_v2', 
            'HLT_L1ETM30_v2', 
            'HLT_L1ETM40_v2', 
            'HLT_L1ETM70_v2', 
            'HLT_L1SingleEG12_v6', 
            'HLT_L1SingleEG5_v6', 
            'HLT_L1SingleJet16_v7', 
            'HLT_L1SingleJet36_v7', 
            'HLT_L1SingleMu12_v2', 
            'HLT_L1SingleMuOpen_AntiBPTX_v7', 
            'HLT_L1SingleMuOpen_v7', 
            'HLT_L1Tech_HBHEHO_totalOR_v6', 
            'HLT_L1Tech_HCAL_HF_single_channel_v4', 
            'HLT_L1TrackerCosmics_v7', 
            'HLT_L2DoubleMu23_NoVertex_2Cha_Angle2p5_v3', 
            'HLT_L2DoubleMu23_NoVertex_v11', 
            'HLT_L2DoubleMu38_NoVertex_2Cha_Angle2p5_v3', 
            'HLT_L2Mu10_NoVertex_NoBPTX3BX_NoHalo_v4', 
            'HLT_L2Mu20_NoVertex_2Cha_NoBPTX3BX_NoHalo_v1', 
            'HLT_L2Mu20_eta2p1_NoVertex_v2', 
            'HLT_L2Mu30_NoVertex_2Cha_NoBPTX3BX_NoHalo_v1', 
            'HLT_L2Mu70_2Cha_eta2p1_PFMET55_v2', 
            'HLT_L2Mu70_2Cha_eta2p1_PFMET60_v2', 
            'HLT_L2TripleMu10_0_0_NoVertex_PFJet40Neutral_v8', 
            'HLT_LogMonitor_v4', 
            'HLT_LooseIsoPFTau35_Trk20_Prong1_MET70_v10', 
            'HLT_LooseIsoPFTau35_Trk20_Prong1_MET75_v10', 
            'HLT_LooseIsoPFTau35_Trk20_Prong1_v10', 
            'HLT_MET100_HBHENoiseCleaned_v1', 
            'HLT_MET120_HBHENoiseCleaned_v6', 
            'HLT_MET120_v13', 
            'HLT_MET200_HBHENoiseCleaned_v5', 
            'HLT_MET200_v12', 
            'HLT_MET300_HBHENoiseCleaned_v5', 
            'HLT_MET300_v4', 
            'HLT_MET400_HBHENoiseCleaned_v5', 
            'HLT_MET400_v7', 
            'HLT_MET80_Parked_v5', 
            'HLT_MET80_Track50_dEdx3p6_v6', 
            'HLT_MET80_Track60_dEdx3p7_v6', 
            'HLT_MET80_v5', 
            'HLT_MonoCentralPFJet80_PFMETnoMu105_NHEF0p95_v4', 
            'HLT_Mu12_eta2p1_DiCentral_20_v8', 
            'HLT_Mu12_eta2p1_DiCentral_40_20_BTagIP3D1stTrack_v8', 
            'HLT_Mu12_eta2p1_DiCentral_40_20_DiBTagIP3D1stTrack_v8', 
            'HLT_Mu12_eta2p1_DiCentral_40_20_v8', 
            'HLT_Mu12_eta2p1_L1Mu10erJetC12WdEtaPhi1DiJetsC_v7', 
            'HLT_Mu12_v18', 
            'HLT_Mu13_Mu8_NoDZ_v1', 
            'HLT_Mu13_Mu8_v22', 
            'HLT_Mu14_Ele14_CaloIdT_TrkIdVL_Mass8_PFMET40_v8', 
            'HLT_Mu14_Ele14_CaloIdT_TrkIdVL_Mass8_PFMET50_v8', 
            'HLT_Mu15_TkMu5_Onia_v1', 
            'HLT_Mu15_eta2p1_DiCentral_20_v1', 
            'HLT_Mu15_eta2p1_DiCentral_40_20_v1', 
            'HLT_Mu15_eta2p1_L1ETM20_v5', 
            'HLT_Mu15_eta2p1_L1Mu10erJetC12WdEtaPhi1DiJetsC_v3', 
            'HLT_Mu15_eta2p1_TriCentral_40_20_20_BTagIP3D1stTrack_v8', 
            'HLT_Mu15_eta2p1_TriCentral_40_20_20_DiBTagIP3D1stTrack_v8', 
            'HLT_Mu15_eta2p1_TriCentral_40_20_20_v8', 
            'HLT_Mu15_eta2p1_v5', 
            'HLT_Mu17_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v9', 
            'HLT_Mu17_Mu8_v22', 
            'HLT_Mu17_TkMu8_NoDZ_v1', 
            'HLT_Mu17_TkMu8_v14', 
            'HLT_Mu17_eta2p1_CentralPFNoPUJet30_BTagIPIter_v4', 
            'HLT_Mu17_eta2p1_LooseIsoPFTau20_v7', 
            'HLT_Mu17_eta2p1_TriCentralPFNoPUJet45_35_25_v2', 
            'HLT_Mu17_v5', 
            'HLT_Mu18_CentralPFJet30_CentralPFJet25_v1', 
            'HLT_Mu18_PFJet30_PFJet25_Deta3_CentralPFJet25_v1', 
            'HLT_Mu22_Photon22_CaloIdL_v7', 
            'HLT_Mu22_TkMu22_v9', 
            'HLT_Mu22_TkMu8_v9', 
            'HLT_Mu24_eta2p1_v5', 
            'HLT_Mu24_v16', 
            'HLT_Mu30_Ele30_CaloIdL_v8', 
            'HLT_Mu30_eta2p1_v5', 
            'HLT_Mu30_v16', 
            'HLT_Mu40_PFNoPUHT350_v4', 
            'HLT_Mu40_eta2p1_Track50_dEdx3p6_v5', 
            'HLT_Mu40_eta2p1_Track60_dEdx3p7_v5', 
            'HLT_Mu40_eta2p1_v11', 
            'HLT_Mu40_v14', 
            'HLT_Mu50_eta2p1_v8', 
            'HLT_Mu5_L2Mu3_Jpsi_v8', 
            'HLT_Mu5_Track2_Jpsi_v21', 
            'HLT_Mu5_Track3p5_Jpsi_v7', 
            'HLT_Mu5_v20', 
            'HLT_Mu60_PFNoPUHT350_v4', 
            'HLT_Mu7_Ele7_CaloIdT_CaloIsoVL_v7', 
            'HLT_Mu7_Track7_Jpsi_v20', 
            'HLT_Mu8_DiJet30_v7', 
            'HLT_Mu8_DoubleEle8_CaloIdT_TrkIdVL_v7', 
            'HLT_Mu8_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v9', 
            'HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Ele8_CaloIdL_TrkIdVL_v7', 
            'HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT175_v4', 
            'HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT225_v4', 
            'HLT_Mu8_QuadJet30_v7', 
            'HLT_Mu8_TriJet30_v7', 
            'HLT_Mu8_eta2p1_LooseIsoPFTau20_L1ETM26_v1', 
            'HLT_Mu8_v18', 
            'HLT_PFJet140_v9', 
            'HLT_PFJet200_v9', 
            'HLT_PFJet260_v9', 
            'HLT_PFJet320_v9', 
            'HLT_PFJet400_v9', 
            'HLT_PFJet40_v8', 
            'HLT_PFJet80_v9', 
            'HLT_PFMET150_v7', 
            'HLT_PFMET180_v7', 
            'HLT_PFNoPUHT350_Mu15_PFMET45_v4', 
            'HLT_PFNoPUHT350_Mu15_PFMET50_v4', 
            'HLT_PFNoPUHT350_PFMET100_v4', 
            'HLT_PFNoPUHT350_v4', 
            'HLT_PFNoPUHT400_Mu5_PFMET45_v4', 
            'HLT_PFNoPUHT400_Mu5_PFMET50_v4', 
            'HLT_PFNoPUHT400_PFMET100_v4', 
            'HLT_PFNoPUHT650_DiCentralPFNoPUJet80_CenPFNoPUJet40_v4', 
            'HLT_PFNoPUHT650_v4', 
            'HLT_PFNoPUHT700_v4', 
            'HLT_PFNoPUHT750_v4', 
            'HLT_Photon135_v7', 
            'HLT_Photon150_v4', 
            'HLT_Photon160_v4', 
            'HLT_Photon20_CaloIdVL_IsoL_v16', 
            'HLT_Photon20_CaloIdVL_v4', 
            'HLT_Photon22_R9Id90_HE10_Iso40_EBOnly_v5', 
            'HLT_Photon26_Photon18_v12', 
            'HLT_Photon26_R9Id85_OR_CaloId10_Iso50_Photon18_R9Id85_OR_CaloId10_Iso50_Mass70_v2', 
            'HLT_Photon26_R9Id85_OR_CaloId10_Iso50_Photon18_v5', 
            'HLT_Photon300_NoHE_v5', 
            'HLT_Photon30_CaloIdVL_v14', 
            'HLT_Photon30_R9Id90_CaloId_HE10_Iso40_EBOnly_Met25_HBHENoiseCleaned_v1', 
            'HLT_Photon30_R9Id90_CaloId_HE10_Iso40_EBOnly_v1', 
            'HLT_Photon30_v1', 
            'HLT_Photon36_CaloId10_Iso50_Photon22_CaloId10_Iso50_v6', 
            'HLT_Photon36_CaloId10_Iso50_Photon22_R9Id85_v6', 
            'HLT_Photon36_Photon22_v6', 
            'HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon10_R9Id85_OR_CaloId10_Iso50_Mass80_v1', 
            'HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon22_R9Id85_OR_CaloId10_Iso50_v6', 
            'HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon22_v5', 
            'HLT_Photon36_R9Id85_Photon22_CaloId10_Iso50_v6', 
            'HLT_Photon36_R9Id85_Photon22_R9Id85_v4', 
            'HLT_Photon36_R9Id90_HE10_Iso40_EBOnly_v5', 
            'HLT_Photon40_CaloIdL_RsqMR40_Rsq0p09_MR150_v6', 
            'HLT_Photon40_CaloIdL_RsqMR45_Rsq0p09_MR150_v6', 
            'HLT_Photon40_CaloIdL_RsqMR50_Rsq0p09_MR150_v6', 
            'HLT_Photon50_CaloIdVL_IsoL_v17', 
            'HLT_Photon50_CaloIdVL_v10', 
            'HLT_Photon50_R9Id90_HE10_Iso40_EBOnly_v5', 
            'HLT_Photon60_CaloIdL_HT300_v4', 
            'HLT_Photon60_CaloIdL_MHT70_v11', 
            'HLT_Photon70_CaloIdXL_PFMET100_v7', 
            'HLT_Photon70_CaloIdXL_PFNoPUHT400_v4', 
            'HLT_Photon70_CaloIdXL_PFNoPUHT500_v4', 
            'HLT_Photon75_CaloIdVL_v13', 
            'HLT_Photon75_R9Id90_HE10_Iso40_EBOnly_v5', 
            'HLT_Photon90_CaloIdVL_v10', 
            'HLT_Photon90_R9Id90_HE10_Iso40_EBOnly_v5', 
            'HLT_Physics_Parked_v1', 
            'HLT_Physics_v5', 
            'HLT_PixelTracks_Multiplicity70_v3', 
            'HLT_PixelTracks_Multiplicity80_v12', 
            'HLT_PixelTracks_Multiplicity90_v3', 
            'HLT_QuadJet45_v1', 
            'HLT_QuadJet50_v5', 
            'HLT_QuadJet60_DiJet20_v6', 
            'HLT_QuadJet70_v6', 
            'HLT_QuadJet75_55_35_20_BTagIP_VBF_v7', 
            'HLT_QuadJet75_55_35_20_VBF_v1', 
            'HLT_QuadJet75_55_38_20_BTagIP_VBF_v7', 
            'HLT_QuadJet80_v6', 
            'HLT_QuadJet90_v6', 
            'HLT_QuadPFJet78_61_44_31_BTagCSV_VBF_v6', 
            'HLT_QuadPFJet78_61_44_31_VBF_v1', 
            'HLT_QuadPFJet82_65_48_35_BTagCSV_VBF_v6', 
            'HLT_Random_v2', 
            'HLT_RelIso1p0Mu20_v3', 
            'HLT_RelIso1p0Mu5_Ele8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT175_v4', 
            'HLT_RelIso1p0Mu5_Ele8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT225_v4', 
            'HLT_RelIso1p0Mu5_v6', 
            'HLT_RsqMR40_Rsq0p04_v6', 
            'HLT_RsqMR45_Rsq0p09_v5', 
            'HLT_RsqMR55_Rsq0p09_MR150_v6', 
            'HLT_RsqMR60_Rsq0p09_MR150_v6', 
            'HLT_RsqMR65_Rsq0p09_MR150_v5', 
            'HLT_SingleForJet15_v4', 
            'HLT_SingleForJet25_v4', 
            'HLT_SixJet35_v6', 
            'HLT_SixJet45_v6', 
            'HLT_SixJet50_v6', 
            'HLT_Tau2Mu_ItTrack_v7', 
            'HLT_TripleEle10_CaloIdL_TrkIdVL_v18', 
            'HLT_TripleMu5_v19', 
            'HLT_ZeroBiasPixel_DoubleTrack_v2', 
            'HLT_ZeroBias_Parked_v1', 
            'HLT_ZeroBias_v7' ) )
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_hltL1GtObjectMap_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*')
)


process.hltOutputALCALUMIPIXELS = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('RAW')
    ),
    fileName = cms.untracked.string('outputALCALUMIPIXELS.root'),
    fastCloning = cms.untracked.bool(False),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('AlCa_LumiPixels_Random_v1', 
            'AlCa_LumiPixels_ZeroBias_v4', 
            'AlCa_LumiPixels_v8')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_hltFEDSelectorLumiPixels_*_*', 
        'keep L1GlobalTriggerReadoutRecord_hltGtDigis_*_*', 
        'keep edmTriggerResults_*_*_*')
)


process.hltOutputALCAP0 = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('RAW')
    ),
    fileName = cms.untracked.string('outputALCAP0.root'),
    fastCloning = cms.untracked.bool(False),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('AlCa_EcalEtaEBonly_v6', 
            'AlCa_EcalEtaEEonly_v6', 
            'AlCa_EcalPi0EBonly_v6', 
            'AlCa_EcalPi0EEonly_v6')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_hltAlCaEtaEBUncalibrator_*_*', 
        'keep *_hltAlCaEtaEEUncalibrator_*_*', 
        'keep *_hltAlCaEtaRecHitsFilterEEonly_etaEcalRecHitsES_*', 
        'keep *_hltAlCaPi0EBUncalibrator_*_*', 
        'keep *_hltAlCaPi0EEUncalibrator_*_*', 
        'keep *_hltAlCaPi0RecHitsFilterEEonly_pi0EcalRecHitsES_*', 
        'keep L1GlobalTriggerReadoutRecord_hltGtDigis_*_*', 
        'keep edmTriggerResults_*_*_*')
)


process.hltOutputALCAPHISYM = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('RAW')
    ),
    fileName = cms.untracked.string('outputALCAPHISYM.root'),
    fastCloning = cms.untracked.bool(False),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('AlCa_EcalPhiSym_v13')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_hltAlCaPhiSymUncalibrator_*_*', 
        'keep L1GlobalTriggerReadoutRecord_hltGtDigis_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*')
)


process.hltOutputB = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('RAW')
    ),
    fileName = cms.untracked.string('outputB.root'),
    fastCloning = cms.untracked.bool(False),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('HLT_BTagMu_Jet20_Mu4_v2', 
            'HLT_BTagMu_Jet60_Mu4_v2', 
            'HLT_DiJet20_MJJ650_AllJets_DEta3p5_HT120_VBF_v1', 
            'HLT_DiJet30_MJJ700_AllJets_DEta3p5_VBF_v1', 
            'HLT_DiJet35_MJJ650_AllJets_DEta3p5_VBF_v5', 
            'HLT_DiJet35_MJJ700_AllJets_DEta3p5_VBF_v5', 
            'HLT_DiJet35_MJJ750_AllJets_DEta3p5_VBF_v5', 
            'HLT_Dimuon10_Jpsi_v6', 
            'HLT_Dimuon5_PsiPrime_v6', 
            'HLT_Dimuon5_Upsilon_v6', 
            'HLT_Dimuon7_PsiPrime_v3', 
            'HLT_Dimuon8_Jpsi_v7', 
            'HLT_Dimuon8_Upsilon_v6', 
            'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Reg_v1', 
            'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_v4', 
            'HLT_DoubleMu3p5_LowMassNonResonant_Displaced_v6', 
            'HLT_DoubleMu3p5_LowMass_Displaced_v6', 
            'HLT_HT200_AlphaT0p57_v8', 
            'HLT_MET100_HBHENoiseCleaned_v1', 
            'HLT_MET80_Parked_v5', 
            'HLT_Mu13_Mu8_v22', 
            'HLT_Mu15_TkMu5_Onia_v1', 
            'HLT_Photon30_R9Id90_CaloId_HE10_Iso40_EBOnly_Met25_HBHENoiseCleaned_v1', 
            'HLT_Photon30_R9Id90_CaloId_HE10_Iso40_EBOnly_v1', 
            'HLT_Photon30_v1', 
            'HLT_Physics_Parked_v1', 
            'HLT_QuadJet45_v1', 
            'HLT_QuadJet50_v5', 
            'HLT_RsqMR45_Rsq0p09_v5', 
            'HLT_ZeroBias_Parked_v1')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_hltL1GtObjectMap_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*')
)


process.hltOutputCalibration = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('RAW')
    ),
    fileName = cms.untracked.string('outputCalibration.root'),
    fastCloning = cms.untracked.bool(False),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('HLT_DTCalibration_v2', 
            'HLT_EcalCalibration_v3', 
            'HLT_HcalCalibration_v3')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_hltDTCalibrationRaw_*_*', 
        'keep *_hltEcalCalibrationRaw_*_*', 
        'keep *_hltHcalCalibrationRaw_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*')
)


process.hltOutputDQM = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('RAW')
    ),
    fileName = cms.untracked.string('outputDQM.root'),
    fastCloning = cms.untracked.bool(False),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring( ('HLT_Activity_Ecal_SC7_v13', 
            'HLT_BTagMu_DiJet110_Mu5_v6', 
            'HLT_BTagMu_DiJet20_Mu5_v6', 
            'HLT_BTagMu_DiJet40_Mu5_v6', 
            'HLT_BTagMu_DiJet70_Mu5_v6', 
            'HLT_BTagMu_Jet300_Mu5_v6', 
            'HLT_BeamGas_HF_Beam1_v5', 
            'HLT_BeamGas_HF_Beam2_v5', 
            'HLT_BeamHalo_v13', 
            'HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v3', 
            'HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v3', 
            'HLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT_v3', 
            'HLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT_v3', 
            'HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v3', 
            'HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v3', 
            'HLT_DTErrors_v3', 
            'HLT_DiCentralJetSumpT100_dPhi05_DiCentralPFJet60_25_PFMET100_HBHENoiseCleaned_v5', 
            'HLT_DiCentralPFJet30_PFMET80_BTagCSV07_v5', 
            'HLT_DiCentralPFJet30_PFMET80_v6', 
            'HLT_DiCentralPFNoPUJet50_PFMETORPFMETNoMu80_v4', 
            'HLT_DiJet40Eta2p6_BTagIP3DFastPV_v7', 
            'HLT_DiJet80Eta2p6_BTagIP3DFastPVLoose_v7', 
            'HLT_DiJet80_DiJet60_DiJet20_v6', 
            'HLT_DiPFJet40_PFMETnoMu65_MJJ600VBF_LeadingJets_v9', 
            'HLT_DiPFJet40_PFMETnoMu65_MJJ800VBF_AllJets_v9', 
            'HLT_DiPFJet80_DiPFJet30_BTagCSVd07d05_v5', 
            'HLT_DiPFJet80_DiPFJet30_BTagCSVd07d05d03_v5', 
            'HLT_DiPFJet80_DiPFJet30_BTagCSVd07d05d05_v5', 
            'HLT_DiPFJetAve140_v10', 
            'HLT_DiPFJetAve200_v10', 
            'HLT_DiPFJetAve260_v10', 
            'HLT_DiPFJetAve320_v10', 
            'HLT_DiPFJetAve400_v10', 
            'HLT_DiPFJetAve40_v9', 
            'HLT_DiPFJetAve80_v10', 
            'HLT_Dimuon0_Jpsi_Muon_v18', 
            'HLT_Dimuon0_Jpsi_NoVertexing_v14', 
            'HLT_Dimuon0_Jpsi_v17', 
            'HLT_Dimuon0_PsiPrime_v6', 
            'HLT_Dimuon0_Upsilon_Muon_v18', 
            'HLT_Dimuon0_Upsilon_v17', 
            'HLT_Dimuon11_Upsilon_v6', 
            'HLT_Dimuon3p5_SameSign_v6', 
            'HLT_Dimuon7_Upsilon_v7', 
            'HLT_DisplacedPhoton65EBOnly_CaloIdVL_IsoL_PFMET30_v4', 
            'HLT_DisplacedPhoton65_CaloIdVL_IsoL_PFMET25_v4', 
            'HLT_DoubleDisplacedMu4_DiPFJet40Neutral_v8', 
            'HLT_DoubleEle10_CaloIdL_TrkIdVL_Ele10_CaloIdT_TrkIdVL_v12', 
            'HLT_DoubleEle14_CaloIdT_TrkIdVL_Mass8_PFMET40_v8', 
            'HLT_DoubleEle14_CaloIdT_TrkIdVL_Mass8_PFMET50_v8', 
            'HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_v7', 
            'HLT_DoubleEle33_CaloIdL_v14', 
            'HLT_DoubleEle33_CaloIdT_v10', 
            'HLT_DoubleEle8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT175_v4', 
            'HLT_DoubleEle8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT225_v4', 
            'HLT_DoubleEle8_CaloIdT_TrkIdVL_v12', 
            'HLT_DoubleIsoL2Tau30_eta2p1_v1', 
            'HLT_DoubleJet20_ForwardBackward_v4', 
            'HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_Jet30_v5', 
            'HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_Reg_Jet30_v1', 
            'HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_Reg_v1', 
            'HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_v4', 
            'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Prong1_Reg_v1', 
            'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Prong1_v4', 
            'HLT_DoubleMu11_Acoplanarity03_v5', 
            'HLT_DoubleMu14_Mass8_PFMET40_v8', 
            'HLT_DoubleMu14_Mass8_PFMET50_v8', 
            'HLT_DoubleMu3_4_Dimuon5_Bs_Central_v5', 
            'HLT_DoubleMu3p5_4_Dimuon5_Bs_Central_v5', 
            'HLT_DoubleMu4_Acoplanarity03_v5', 
            'HLT_DoubleMu4_Dimuon7_Bs_Forward_v5', 
            'HLT_DoubleMu4_JpsiTk_Displaced_v6', 
            'HLT_DoubleMu4_Jpsi_Displaced_v12', 
            'HLT_DoubleMu5_Ele8_CaloIdT_TrkIdVL_v16', 
            'HLT_DoubleMu5_IsoMu5_v20', 
            'HLT_DoubleMu8_Ele8_CaloIdT_TrkIdVL_v5', 
            'HLT_DoubleMu8_Mass8_PFNoPUHT175_v4', 
            'HLT_DoubleMu8_Mass8_PFNoPUHT225_v4', 
            'HLT_DoublePhoton40_CaloIdL_Rsq0p035_v6', 
            'HLT_DoublePhoton40_CaloIdL_Rsq0p06_v6', 
            'HLT_DoublePhoton48_HEVT_v8', 
            'HLT_DoublePhoton53_HEVT_v2', 
            'HLT_DoublePhoton70_v6', 
            'HLT_DoublePhoton80_v7', 
            'HLT_DoubleRelIso1p0Mu5_Mass8_PFNoPUHT175_v4', 
            'HLT_DoubleRelIso1p0Mu5_Mass8_PFNoPUHT225_v4', 
            'HLT_EightJet30_eta3p0_v5', 
            'HLT_EightJet35_eta3p0_v5', 
            'HLT_Ele12_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_DoubleCentralJet65_v4', 
            'HLT_Ele12_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_RsqMR30_Rsq0p04_MR200_v4', 
            'HLT_Ele12_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_RsqMR40_Rsq0p04_MR200_v4', 
            'HLT_Ele13_eta2p1_WP90NoIso_LooseIsoPFTau20_L1ETM36_v1', 
            'HLT_Ele13_eta2p1_WP90Rho_LooseIsoPFTau20_L1ETM36_v1', 
            'HLT_Ele13_eta2p1_WP90Rho_LooseIsoPFTau20_v1', 
            'HLT_Ele15_Ele8_Ele5_CaloIdL_TrkIdVL_v6', 
            'HLT_Ele17_CaloIdL_CaloIsoVL_v17', 
            'HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v19', 
            'HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Jet30_v7', 
            'HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v6', 
            'HLT_Ele17_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_Ele8_Mass50_v6', 
            'HLT_Ele20_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_SC4_Mass50_v7', 
            'HLT_Ele22_CaloIdL_CaloIsoVL_v6', 
            'HLT_Ele22_eta2p1_WP90NoIso_LooseIsoPFTau20_v7', 
            'HLT_Ele22_eta2p1_WP90Rho_LooseIsoPFTau20_v7', 
            'HLT_Ele23_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_HFT30_v8', 
            'HLT_Ele24_WP80_CentralPFJet35_CentralPFJet25_PFMET20_v1', 
            'HLT_Ele24_WP80_CentralPFJet35_CentralPFJet25_v1', 
            'HLT_Ele24_WP80_PFJet30_PFJet25_Deta3_CentralPFJet30_v1', 
            'HLT_Ele24_WP80_PFJet30_PFJet25_Deta3_v1', 
            'HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_CentralPFNoPUJet30_BTagIPIter_v9', 
            'HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_CentralPFNoPUJet30_v8', 
            'HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_DiCentralPFNoPUJet30_v2', 
            'HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30_v4', 
            'HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet45_35_25_v2', 
            'HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet50_40_30_v4', 
            'HLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_v11', 
            'HLT_Ele27_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele15_CaloIdT_CaloIsoVL_trackless_v8', 
            'HLT_Ele27_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_HFT15_v8', 
            'HLT_Ele27_WP80_CentralPFJet80_v9', 
            'HLT_Ele27_WP80_PFMET_MT50_v7', 
            'HLT_Ele27_WP80_WCandPt80_v9', 
            'HLT_Ele27_WP80_v11', 
            'HLT_Ele30_CaloIdVT_TrkIdT_PFNoPUJet100_PFNoPUJet25_v8', 
            'HLT_Ele30_CaloIdVT_TrkIdT_PFNoPUJet150_PFNoPUJet25_v8', 
            'HLT_Ele30_CaloIdVT_TrkIdT_v6', 
            'HLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_v11', 
            'HLT_Ele32_CaloIdT_CaloIsoT_TrkIdT_TrkIsoT_SC17_Mass50_v6', 
            'HLT_Ele5_SC5_Jpsi_Mass2to15_v4', 
            'HLT_Ele80_CaloIdVT_GsfTrkIdT_v2', 
            'HLT_Ele8_CaloIdL_CaloIsoVL_v17', 
            'HLT_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Jet30_v7', 
            'HLT_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v15', 
            'HLT_Ele8_CaloIdT_TrkIdT_DiJet30_v18', 
            'HLT_Ele8_CaloIdT_TrkIdT_QuadJet30_v18', 
            'HLT_Ele8_CaloIdT_TrkIdT_TriJet30_v18', 
            'HLT_Ele8_CaloIdT_TrkIdVL_EG7_v2', 
            'HLT_Ele8_CaloIdT_TrkIdVL_Jet30_v7', 
            'HLT_Ele8_CaloIdT_TrkIdVL_v5', 
            'HLT_Ele90_CaloIdVT_GsfTrkIdT_v2', 
            'HLT_ExclDiJet35_HFAND_v4', 
            'HLT_ExclDiJet35_HFOR_v4', 
            'HLT_ExclDiJet80_HFAND_v4', 
            'HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v10', 
            'HLT_GlobalRunHPDNoise_v8', 
            'HLT_HT200_v6', 
            'HLT_HT250_AlphaT0p55_v8', 
            'HLT_HT250_AlphaT0p57_v8', 
            'HLT_HT250_v7', 
            'HLT_HT300_AlphaT0p53_v8', 
            'HLT_HT300_AlphaT0p54_v14', 
            'HLT_HT300_DoubleDisplacedPFJet60_ChgFraction10_v10', 
            'HLT_HT300_DoubleDisplacedPFJet60_v10', 
            'HLT_HT300_SingleDisplacedPFJet60_ChgFraction10_v10', 
            'HLT_HT300_SingleDisplacedPFJet60_v10', 
            'HLT_HT300_v7', 
            'HLT_HT350_AlphaT0p52_v8', 
            'HLT_HT350_AlphaT0p53_v19', 
            'HLT_HT350_v7', 
            'HLT_HT400_AlphaT0p51_v19', 
            'HLT_HT400_AlphaT0p52_v14', 
            'HLT_HT400_v7', 
            'HLT_HT450_AlphaT0p51_v14', 
            'HLT_HT450_v7', 
            'HLT_HT500_v7', 
            'HLT_HT550_v7', 
            'HLT_HT650_Track50_dEdx3p6_v10', 
            'HLT_HT650_Track60_dEdx3p7_v10', 
            'HLT_HT650_v7', 
            'HLT_HT750_v7', 
            'HLT_HcalNZS_v10', 
            'HLT_HcalPhiSym_v11', 
            'HLT_HcalUTCA_v1', 
            'HLT_IsoMu12_DoubleCentralJet65_v4', 
            'HLT_IsoMu12_RsqMR30_Rsq0p04_MR200_v4', 
            'HLT_IsoMu12_RsqMR40_Rsq0p04_MR200_v4', 
            'HLT_IsoMu15_eta2p1_L1ETM20_v7', 
            'HLT_IsoMu15_eta2p1_LooseIsoPFTau35_Trk20_Prong1_L1ETM20_v10', 
            'HLT_IsoMu17_eta2p1_CentralPFNoPUJet30_BTagIPIter_v4', 
            'HLT_IsoMu17_eta2p1_CentralPFNoPUJet30_v4', 
            'HLT_IsoMu17_eta2p1_DiCentralPFNoPUJet30_PFNoPUHT350_PFMHT40_v3', 
            'HLT_IsoMu17_eta2p1_DiCentralPFNoPUJet30_v4', 
            'HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v7', 
            'HLT_IsoMu17_eta2p1_TriCentralPFNoPUJet30_v4', 
            'HLT_IsoMu17_eta2p1_TriCentralPFNoPUJet45_35_25_v2', 
            'HLT_IsoMu18_CentralPFJet30_CentralPFJet25_PFMET20_v1', 
            'HLT_IsoMu18_CentralPFJet30_CentralPFJet25_v1', 
            'HLT_IsoMu18_PFJet30_PFJet25_Deta3_CentralPFJet25_v1', 
            'HLT_IsoMu18_PFJet30_PFJet25_Deta3_v1', 
            'HLT_IsoMu18_eta2p1_MediumIsoPFTau25_Trk1_eta2p1_Reg_v1', 
            'HLT_IsoMu18_eta2p1_MediumIsoPFTau25_Trk1_eta2p1_v4', 
            'HLT_IsoMu20_WCandPt80_v4', 
            'HLT_IsoMu20_eta2p1_CentralPFJet80_v9', 
            'HLT_IsoMu20_eta2p1_v7', 
            'HLT_IsoMu24_eta2p1_v15', 
            'HLT_IsoMu24_v17', 
            'HLT_IsoMu30_eta2p1_v15', 
            'HLT_IsoMu30_v11', 
            'HLT_IsoMu34_eta2p1_v13', 
            'HLT_IsoMu40_eta2p1_v10', 
            'HLT_IsoMu8_eta2p1_LooseIsoPFTau20_L1ETM26_v1', 
            'HLT_IsoMu8_eta2p1_LooseIsoPFTau20_v1', 
            'HLT_IsoTrackHB_v14', 
            'HLT_IsoTrackHE_v15', 
            'HLT_Jet160Eta2p4_Jet120Eta2p4_DiBTagIP3DFastPVLoose_v7', 
            'HLT_Jet370_NoJetID_v15', 
            'HLT_Jet60Eta1p7_Jet53Eta1p7_DiBTagIP3DFastPV_v7', 
            'HLT_Jet80Eta1p7_Jet70Eta1p7_DiBTagIP3DFastPV_v7', 
            'HLT_JetE30_NoBPTX3BX_NoHalo_v16', 
            'HLT_JetE30_NoBPTX_v14', 
            'HLT_JetE50_NoBPTX3BX_NoHalo_v13', 
            'HLT_JetE70_NoBPTX3BX_NoHalo_v5', 
            'HLT_L1DoubleEG3_FwdVeto_v2', 
            'HLT_L1DoubleJet36Central_v7', 
            'HLT_L1ETM100_v2', 
            'HLT_L1ETM30_v2', 
            'HLT_L1ETM40_v2', 
            'HLT_L1ETM70_v2', 
            'HLT_L1SingleEG12_v6', 
            'HLT_L1SingleEG5_v6', 
            'HLT_L1SingleJet16_v7', 
            'HLT_L1SingleJet36_v7', 
            'HLT_L1SingleMu12_v2', 
            'HLT_L1SingleMuOpen_AntiBPTX_v7', 
            'HLT_L1SingleMuOpen_v7', 
            'HLT_L1Tech_HBHEHO_totalOR_v6', 
            'HLT_L1Tech_HCAL_HF_single_channel_v4', 
            'HLT_L1TrackerCosmics_v7', 
            'HLT_L2DoubleMu23_NoVertex_2Cha_Angle2p5_v3', 
            'HLT_L2DoubleMu23_NoVertex_v11', 
            'HLT_L2DoubleMu38_NoVertex_2Cha_Angle2p5_v3', 
            'HLT_L2Mu10_NoVertex_NoBPTX3BX_NoHalo_v4', 
            'HLT_L2Mu20_NoVertex_2Cha_NoBPTX3BX_NoHalo_v1', 
            'HLT_L2Mu20_eta2p1_NoVertex_v2', 
            'HLT_L2Mu30_NoVertex_2Cha_NoBPTX3BX_NoHalo_v1', 
            'HLT_L2Mu70_2Cha_eta2p1_PFMET55_v2', 
            'HLT_L2Mu70_2Cha_eta2p1_PFMET60_v2', 
            'HLT_L2TripleMu10_0_0_NoVertex_PFJet40Neutral_v8', 
            'HLT_LooseIsoPFTau35_Trk20_Prong1_MET70_v10', 
            'HLT_LooseIsoPFTau35_Trk20_Prong1_MET75_v10', 
            'HLT_LooseIsoPFTau35_Trk20_Prong1_v10', 
            'HLT_MET120_HBHENoiseCleaned_v6', 
            'HLT_MET120_v13', 
            'HLT_MET200_HBHENoiseCleaned_v5', 
            'HLT_MET200_v12', 
            'HLT_MET300_HBHENoiseCleaned_v5', 
            'HLT_MET300_v4', 
            'HLT_MET400_HBHENoiseCleaned_v5', 
            'HLT_MET400_v7', 
            'HLT_MET80_Track50_dEdx3p6_v6', 
            'HLT_MET80_Track60_dEdx3p7_v6', 
            'HLT_MET80_v5', 
            'HLT_MonoCentralPFJet80_PFMETnoMu105_NHEF0p95_v4', 
            'HLT_Mu12_eta2p1_DiCentral_20_v8', 
            'HLT_Mu12_eta2p1_DiCentral_40_20_BTagIP3D1stTrack_v8', 
            'HLT_Mu12_eta2p1_DiCentral_40_20_DiBTagIP3D1stTrack_v8', 
            'HLT_Mu12_eta2p1_DiCentral_40_20_v8', 
            'HLT_Mu12_eta2p1_L1Mu10erJetC12WdEtaPhi1DiJetsC_v7', 
            'HLT_Mu12_v18', 
            'HLT_Mu13_Mu8_NoDZ_v1', 
            'HLT_Mu14_Ele14_CaloIdT_TrkIdVL_Mass8_PFMET40_v8', 
            'HLT_Mu14_Ele14_CaloIdT_TrkIdVL_Mass8_PFMET50_v8', 
            'HLT_Mu15_eta2p1_DiCentral_20_v1', 
            'HLT_Mu15_eta2p1_DiCentral_40_20_v1', 
            'HLT_Mu15_eta2p1_L1ETM20_v5', 
            'HLT_Mu15_eta2p1_L1Mu10erJetC12WdEtaPhi1DiJetsC_v3', 
            'HLT_Mu15_eta2p1_TriCentral_40_20_20_BTagIP3D1stTrack_v8', 
            'HLT_Mu15_eta2p1_TriCentral_40_20_20_DiBTagIP3D1stTrack_v8', 
            'HLT_Mu15_eta2p1_TriCentral_40_20_20_v8', 
            'HLT_Mu15_eta2p1_v5', 
            'HLT_Mu17_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v9', 
            'HLT_Mu17_Mu8_v22', 
            'HLT_Mu17_TkMu8_NoDZ_v1', 
            'HLT_Mu17_TkMu8_v14', 
            'HLT_Mu17_eta2p1_CentralPFNoPUJet30_BTagIPIter_v4', 
            'HLT_Mu17_eta2p1_LooseIsoPFTau20_v7', 
            'HLT_Mu17_eta2p1_TriCentralPFNoPUJet45_35_25_v2', 
            'HLT_Mu17_v5', 
            'HLT_Mu18_CentralPFJet30_CentralPFJet25_v1', 
            'HLT_Mu18_PFJet30_PFJet25_Deta3_CentralPFJet25_v1', 
            'HLT_Mu22_Photon22_CaloIdL_v7', 
            'HLT_Mu22_TkMu22_v9', 
            'HLT_Mu22_TkMu8_v9', 
            'HLT_Mu24_eta2p1_v5', 
            'HLT_Mu24_v16', 
            'HLT_Mu30_Ele30_CaloIdL_v8', 
            'HLT_Mu30_eta2p1_v5', 
            'HLT_Mu30_v16', 
            'HLT_Mu40_PFNoPUHT350_v4', 
            'HLT_Mu40_eta2p1_Track50_dEdx3p6_v5', 
            'HLT_Mu40_eta2p1_Track60_dEdx3p7_v5', 
            'HLT_Mu40_eta2p1_v11', 
            'HLT_Mu40_v14', 
            'HLT_Mu50_eta2p1_v8', 
            'HLT_Mu5_L2Mu3_Jpsi_v8', 
            'HLT_Mu5_Track2_Jpsi_v21', 
            'HLT_Mu5_Track3p5_Jpsi_v7', 
            'HLT_Mu5_v20', 
            'HLT_Mu60_PFNoPUHT350_v4', 
            'HLT_Mu7_Ele7_CaloIdT_CaloIsoVL_v7', 
            'HLT_Mu7_Track7_Jpsi_v20', 
            'HLT_Mu8_DiJet30_v7', 
            'HLT_Mu8_DoubleEle8_CaloIdT_TrkIdVL_v7', 
            'HLT_Mu8_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v9', 
            'HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Ele8_CaloIdL_TrkIdVL_v7', 
            'HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT175_v4', 
            'HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT225_v4', 
            'HLT_Mu8_QuadJet30_v7', 
            'HLT_Mu8_TriJet30_v7', 
            'HLT_Mu8_eta2p1_LooseIsoPFTau20_L1ETM26_v1', 
            'HLT_Mu8_v18', 
            'HLT_PFJet140_v9', 
            'HLT_PFJet200_v9', 
            'HLT_PFJet260_v9', 
            'HLT_PFJet320_v9', 
            'HLT_PFJet400_v9', 
            'HLT_PFJet40_v8', 
            'HLT_PFJet80_v9', 
            'HLT_PFMET150_v7', 
            'HLT_PFMET180_v7', 
            'HLT_PFNoPUHT350_Mu15_PFMET45_v4', 
            'HLT_PFNoPUHT350_Mu15_PFMET50_v4', 
            'HLT_PFNoPUHT350_PFMET100_v4', 
            'HLT_PFNoPUHT350_v4', 
            'HLT_PFNoPUHT400_Mu5_PFMET45_v4', 
            'HLT_PFNoPUHT400_Mu5_PFMET50_v4', 
            'HLT_PFNoPUHT400_PFMET100_v4', 
            'HLT_PFNoPUHT650_DiCentralPFNoPUJet80_CenPFNoPUJet40_v4', 
            'HLT_PFNoPUHT650_v4', 
            'HLT_PFNoPUHT700_v4', 
            'HLT_PFNoPUHT750_v4', 
            'HLT_Photon135_v7', 
            'HLT_Photon150_v4', 
            'HLT_Photon160_v4', 
            'HLT_Photon20_CaloIdVL_IsoL_v16', 
            'HLT_Photon20_CaloIdVL_v4', 
            'HLT_Photon22_R9Id90_HE10_Iso40_EBOnly_v5', 
            'HLT_Photon26_Photon18_v12', 
            'HLT_Photon26_R9Id85_OR_CaloId10_Iso50_Photon18_R9Id85_OR_CaloId10_Iso50_Mass70_v2', 
            'HLT_Photon26_R9Id85_OR_CaloId10_Iso50_Photon18_v5', 
            'HLT_Photon300_NoHE_v5', 
            'HLT_Photon30_CaloIdVL_v14', 
            'HLT_Photon36_CaloId10_Iso50_Photon22_CaloId10_Iso50_v6', 
            'HLT_Photon36_CaloId10_Iso50_Photon22_R9Id85_v6', 
            'HLT_Photon36_Photon22_v6', 
            'HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon10_R9Id85_OR_CaloId10_Iso50_Mass80_v1', 
            'HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon22_R9Id85_OR_CaloId10_Iso50_v6', 
            'HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon22_v5', 
            'HLT_Photon36_R9Id85_Photon22_CaloId10_Iso50_v6', 
            'HLT_Photon36_R9Id85_Photon22_R9Id85_v4', 
            'HLT_Photon36_R9Id90_HE10_Iso40_EBOnly_v5', 
            'HLT_Photon40_CaloIdL_RsqMR40_Rsq0p09_MR150_v6', 
            'HLT_Photon40_CaloIdL_RsqMR45_Rsq0p09_MR150_v6', 
            'HLT_Photon40_CaloIdL_RsqMR50_Rsq0p09_MR150_v6', 
            'HLT_Photon50_CaloIdVL_IsoL_v17', 
            'HLT_Photon50_CaloIdVL_v10', 
            'HLT_Photon50_R9Id90_HE10_Iso40_EBOnly_v5', 
            'HLT_Photon60_CaloIdL_HT300_v4', 
            'HLT_Photon60_CaloIdL_MHT70_v11', 
            'HLT_Photon70_CaloIdXL_PFMET100_v7', 
            'HLT_Photon70_CaloIdXL_PFNoPUHT400_v4', 
            'HLT_Photon70_CaloIdXL_PFNoPUHT500_v4', 
            'HLT_Photon75_CaloIdVL_v13', 
            'HLT_Photon75_R9Id90_HE10_Iso40_EBOnly_v5', 
            'HLT_Photon90_CaloIdVL_v10', 
            'HLT_Photon90_R9Id90_HE10_Iso40_EBOnly_v5', 
            'HLT_Physics_v5', 
            'HLT_PixelTracks_Multiplicity70_v3', 
            'HLT_PixelTracks_Multiplicity80_v12', 
            'HLT_PixelTracks_Multiplicity90_v3', 
            'HLT_QuadJet60_DiJet20_v6', 
            'HLT_QuadJet70_v6', 
            'HLT_QuadJet75_55_35_20_BTagIP_VBF_v7', 
            'HLT_QuadJet75_55_35_20_VBF_v1', 
            'HLT_QuadJet75_55_38_20_BTagIP_VBF_v7', 
            'HLT_QuadJet80_v6', 
            'HLT_QuadJet90_v6', 
            'HLT_QuadPFJet78_61_44_31_BTagCSV_VBF_v6', 
            'HLT_QuadPFJet78_61_44_31_VBF_v1', 
            'HLT_QuadPFJet82_65_48_35_BTagCSV_VBF_v6', 
            'HLT_Random_v2', 
            'HLT_RelIso1p0Mu20_v3', 
            'HLT_RelIso1p0Mu5_Ele8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT175_v4', 
            'HLT_RelIso1p0Mu5_Ele8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT225_v4', 
            'HLT_RelIso1p0Mu5_v6', 
            'HLT_RsqMR40_Rsq0p04_v6', 
            'HLT_RsqMR55_Rsq0p09_MR150_v6', 
            'HLT_RsqMR60_Rsq0p09_MR150_v6', 
            'HLT_RsqMR65_Rsq0p09_MR150_v5', 
            'HLT_SingleForJet15_v4', 
            'HLT_SingleForJet25_v4', 
            'HLT_SixJet35_v6', 
            'HLT_SixJet45_v6', 
            'HLT_SixJet50_v6', 
            'HLT_Tau2Mu_ItTrack_v7', 
            'HLT_TripleEle10_CaloIdL_TrkIdVL_v18', 
            'HLT_TripleMu5_v19', 
            'HLT_ZeroBiasPixel_DoubleTrack_v2', 
            'HLT_ZeroBias_v7' ) )
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_hltL1GtObjectMap_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*')
)


process.hltOutputEcalCalibration = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('RAW')
    ),
    fileName = cms.untracked.string('outputEcalCalibration.root'),
    fastCloning = cms.untracked.bool(False),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('HLT_EcalCalibration_v3')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_hltEcalCalibrationRaw_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*')
)


process.hltOutputExpress = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('RAW')
    ),
    fileName = cms.untracked.string('outputExpress.root'),
    fastCloning = cms.untracked.bool(False),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('HLT_DoublePhoton80_v7', 
            'HLT_EightJet30_eta3p0_v5', 
            'HLT_EightJet35_eta3p0_v5', 
            'HLT_MET400_v7', 
            'HLT_Mu17_Mu8_v22', 
            'HLT_Photon300_NoHE_v5', 
            'HLT_ZeroBias_v7')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_hltL1GtObjectMap_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*')
)


process.hltOutputFULL = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('AOD')
    ),
    fileName = cms.untracked.string('out_hlt.root'),
    fastCloning = cms.untracked.bool(False),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('HLT_Mu17_Mu8_v22')
    ),
    outputCommands = cms.untracked.vstring('keep *')
)


process.hltOutputHLTDQM = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('RAW')
    ),
    fileName = cms.untracked.string('outputHLTDQM.root'),
    fastCloning = cms.untracked.bool(False),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('HLT_DiJet80_DiJet60_DiJet20_v6', 
            'HLT_DiPFJetAve140_v10', 
            'HLT_DiPFJetAve200_v10', 
            'HLT_DiPFJetAve260_v10', 
            'HLT_DiPFJetAve320_v10', 
            'HLT_DiPFJetAve400_v10', 
            'HLT_DiPFJetAve40_v9', 
            'HLT_DiPFJetAve80_v10', 
            'HLT_Ele22_CaloIdL_CaloIsoVL_v6', 
            'HLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_v11', 
            'HLT_Ele27_WP80_PFMET_MT50_v7', 
            'HLT_Ele27_WP80_v11', 
            'HLT_Ele30_CaloIdVT_TrkIdT_v6', 
            'HLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_v11', 
            'HLT_Ele80_CaloIdVT_GsfTrkIdT_v2', 
            'HLT_Ele90_CaloIdVT_GsfTrkIdT_v2', 
            'HLT_IsoMu20_eta2p1_v7', 
            'HLT_IsoMu24_eta2p1_v15', 
            'HLT_IsoMu30_eta2p1_v15', 
            'HLT_IsoMu34_eta2p1_v13', 
            'HLT_IsoMu40_eta2p1_v10', 
            'HLT_Jet370_NoJetID_v15', 
            'HLT_Mu12_v18', 
            'HLT_Mu15_eta2p1_v5', 
            'HLT_Mu17_v5', 
            'HLT_Mu24_eta2p1_v5', 
            'HLT_Mu30_eta2p1_v5', 
            'HLT_Mu40_eta2p1_Track50_dEdx3p6_v5', 
            'HLT_Mu40_eta2p1_Track60_dEdx3p7_v5', 
            'HLT_Mu40_eta2p1_v11', 
            'HLT_Mu5_v20', 
            'HLT_Mu8_v18', 
            'HLT_PFJet140_v9', 
            'HLT_PFJet200_v9', 
            'HLT_PFJet260_v9', 
            'HLT_PFJet320_v9', 
            'HLT_PFJet400_v9', 
            'HLT_PFJet40_v8', 
            'HLT_PFJet80_v9', 
            'HLT_RelIso1p0Mu20_v3', 
            'HLT_RelIso1p0Mu5_v6', 
            'HLT_SingleForJet15_v4', 
            'HLT_SingleForJet25_v4')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_hltTriggerSummaryAOD_*_*', 
        'keep DcsStatuss_hltScalersRawToDigi_*_*', 
        'keep L1GlobalTriggerReadoutRecord_hltGtDigis_*_*', 
        'keep LumiScalerss_hltScalersRawToDigi_*_*', 
        'keep edmTriggerResults_*_*_*')
)


process.hltOutputHLTMON = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('RAW')
    ),
    fileName = cms.untracked.string('outputHLTMON.root'),
    fastCloning = cms.untracked.bool(False),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring( ('AlCa_EcalEtaEBonly_v6', 
            'AlCa_EcalEtaEEonly_v6', 
            'AlCa_EcalPhiSym_v13', 
            'AlCa_EcalPi0EBonly_v6', 
            'AlCa_EcalPi0EEonly_v6', 
            'AlCa_LumiPixels_Random_v1', 
            'AlCa_LumiPixels_ZeroBias_v4', 
            'AlCa_LumiPixels_v8', 
            'AlCa_RPCMuonNoHits_v9', 
            'AlCa_RPCMuonNoTriggers_v9', 
            'AlCa_RPCMuonNormalisation_v9', 
            'DST_Ele8_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT250_v4', 
            'DST_HT250_v4', 
            'DST_L1HTT_Or_L1MultiJet_v4', 
            'DST_Mu5_HT250_v4', 
            'HLT_Activity_Ecal_SC7_v13', 
            'HLT_BTagMu_DiJet110_Mu5_v6', 
            'HLT_BTagMu_DiJet20_Mu5_v6', 
            'HLT_BTagMu_DiJet40_Mu5_v6', 
            'HLT_BTagMu_DiJet70_Mu5_v6', 
            'HLT_BTagMu_Jet20_Mu4_v2', 
            'HLT_BTagMu_Jet300_Mu5_v6', 
            'HLT_BTagMu_Jet60_Mu4_v2', 
            'HLT_BeamGas_HF_Beam1_v5', 
            'HLT_BeamGas_HF_Beam2_v5', 
            'HLT_BeamHalo_v13', 
            'HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v3', 
            'HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v3', 
            'HLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT_v3', 
            'HLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT_v3', 
            'HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v3', 
            'HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v3', 
            'HLT_DTErrors_v3', 
            'HLT_DiCentralJetSumpT100_dPhi05_DiCentralPFJet60_25_PFMET100_HBHENoiseCleaned_v5', 
            'HLT_DiCentralPFJet30_PFMET80_BTagCSV07_v5', 
            'HLT_DiCentralPFJet30_PFMET80_v6', 
            'HLT_DiCentralPFNoPUJet50_PFMETORPFMETNoMu80_v4', 
            'HLT_DiJet20_MJJ650_AllJets_DEta3p5_HT120_VBF_v1', 
            'HLT_DiJet30_MJJ700_AllJets_DEta3p5_VBF_v1', 
            'HLT_DiJet35_MJJ650_AllJets_DEta3p5_VBF_v5', 
            'HLT_DiJet35_MJJ700_AllJets_DEta3p5_VBF_v5', 
            'HLT_DiJet35_MJJ750_AllJets_DEta3p5_VBF_v5', 
            'HLT_DiJet40Eta2p6_BTagIP3DFastPV_v7', 
            'HLT_DiJet80Eta2p6_BTagIP3DFastPVLoose_v7', 
            'HLT_DiJet80_DiJet60_DiJet20_v6', 
            'HLT_DiPFJet40_PFMETnoMu65_MJJ600VBF_LeadingJets_v9', 
            'HLT_DiPFJet40_PFMETnoMu65_MJJ800VBF_AllJets_v9', 
            'HLT_DiPFJet80_DiPFJet30_BTagCSVd07d05_v5', 
            'HLT_DiPFJet80_DiPFJet30_BTagCSVd07d05d03_v5', 
            'HLT_DiPFJet80_DiPFJet30_BTagCSVd07d05d05_v5', 
            'HLT_DiPFJetAve140_v10', 
            'HLT_DiPFJetAve200_v10', 
            'HLT_DiPFJetAve260_v10', 
            'HLT_DiPFJetAve320_v10', 
            'HLT_DiPFJetAve400_v10', 
            'HLT_DiPFJetAve40_v9', 
            'HLT_DiPFJetAve80_v10', 
            'HLT_Dimuon0_Jpsi_Muon_v18', 
            'HLT_Dimuon0_Jpsi_NoVertexing_v14', 
            'HLT_Dimuon0_Jpsi_v17', 
            'HLT_Dimuon0_PsiPrime_v6', 
            'HLT_Dimuon0_Upsilon_Muon_v18', 
            'HLT_Dimuon0_Upsilon_v17', 
            'HLT_Dimuon10_Jpsi_v6', 
            'HLT_Dimuon11_Upsilon_v6', 
            'HLT_Dimuon3p5_SameSign_v6', 
            'HLT_Dimuon5_PsiPrime_v6', 
            'HLT_Dimuon5_Upsilon_v6', 
            'HLT_Dimuon7_PsiPrime_v3', 
            'HLT_Dimuon7_Upsilon_v7', 
            'HLT_Dimuon8_Jpsi_v7', 
            'HLT_Dimuon8_Upsilon_v6', 
            'HLT_DisplacedPhoton65EBOnly_CaloIdVL_IsoL_PFMET30_v4', 
            'HLT_DisplacedPhoton65_CaloIdVL_IsoL_PFMET25_v4', 
            'HLT_DoubleDisplacedMu4_DiPFJet40Neutral_v8', 
            'HLT_DoubleEle10_CaloIdL_TrkIdVL_Ele10_CaloIdT_TrkIdVL_v12', 
            'HLT_DoubleEle14_CaloIdT_TrkIdVL_Mass8_PFMET40_v8', 
            'HLT_DoubleEle14_CaloIdT_TrkIdVL_Mass8_PFMET50_v8', 
            'HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_v7', 
            'HLT_DoubleEle33_CaloIdL_v14', 
            'HLT_DoubleEle33_CaloIdT_v10', 
            'HLT_DoubleEle8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT175_v4', 
            'HLT_DoubleEle8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT225_v4', 
            'HLT_DoubleEle8_CaloIdT_TrkIdVL_v12', 
            'HLT_DoubleIsoL2Tau30_eta2p1_v1', 
            'HLT_DoubleJet20_ForwardBackward_v4', 
            'HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_Jet30_v5', 
            'HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_Reg_Jet30_v1', 
            'HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_Reg_v1', 
            'HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_v4', 
            'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Prong1_Reg_v1', 
            'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Prong1_v4', 
            'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Reg_v1', 
            'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_v4', 
            'HLT_DoubleMu11_Acoplanarity03_v5', 
            'HLT_DoubleMu14_Mass8_PFMET40_v8', 
            'HLT_DoubleMu14_Mass8_PFMET50_v8', 
            'HLT_DoubleMu3_4_Dimuon5_Bs_Central_v5', 
            'HLT_DoubleMu3p5_4_Dimuon5_Bs_Central_v5', 
            'HLT_DoubleMu3p5_LowMassNonResonant_Displaced_v6', 
            'HLT_DoubleMu3p5_LowMass_Displaced_v6', 
            'HLT_DoubleMu4_Acoplanarity03_v5', 
            'HLT_DoubleMu4_Dimuon7_Bs_Forward_v5', 
            'HLT_DoubleMu4_JpsiTk_Displaced_v6', 
            'HLT_DoubleMu4_Jpsi_Displaced_v12', 
            'HLT_DoubleMu5_Ele8_CaloIdT_TrkIdVL_v16', 
            'HLT_DoubleMu5_IsoMu5_v20', 
            'HLT_DoubleMu8_Ele8_CaloIdT_TrkIdVL_v5', 
            'HLT_DoubleMu8_Mass8_PFNoPUHT175_v4', 
            'HLT_DoubleMu8_Mass8_PFNoPUHT225_v4', 
            'HLT_DoublePhoton40_CaloIdL_Rsq0p035_v6', 
            'HLT_DoublePhoton40_CaloIdL_Rsq0p06_v6', 
            'HLT_DoublePhoton48_HEVT_v8', 
            'HLT_DoublePhoton53_HEVT_v2', 
            'HLT_DoublePhoton70_v6', 
            'HLT_DoublePhoton80_v7', 
            'HLT_DoubleRelIso1p0Mu5_Mass8_PFNoPUHT175_v4', 
            'HLT_DoubleRelIso1p0Mu5_Mass8_PFNoPUHT225_v4', 
            'HLT_EightJet30_eta3p0_v5', 
            'HLT_EightJet35_eta3p0_v5', 
            'HLT_Ele12_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_DoubleCentralJet65_v4', 
            'HLT_Ele12_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_RsqMR30_Rsq0p04_MR200_v4', 
            'HLT_Ele12_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_RsqMR40_Rsq0p04_MR200_v4', 
            'HLT_Ele13_eta2p1_WP90NoIso_LooseIsoPFTau20_L1ETM36_v1', 
            'HLT_Ele13_eta2p1_WP90Rho_LooseIsoPFTau20_L1ETM36_v1', 
            'HLT_Ele13_eta2p1_WP90Rho_LooseIsoPFTau20_v1', 
            'HLT_Ele15_Ele8_Ele5_CaloIdL_TrkIdVL_v6', 
            'HLT_Ele17_CaloIdL_CaloIsoVL_v17', 
            'HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v19', 
            'HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Jet30_v7', 
            'HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v6', 
            'HLT_Ele17_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_Ele8_Mass50_v6', 
            'HLT_Ele20_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_SC4_Mass50_v7', 
            'HLT_Ele22_CaloIdL_CaloIsoVL_v6', 
            'HLT_Ele22_eta2p1_WP90NoIso_LooseIsoPFTau20_v7', 
            'HLT_Ele22_eta2p1_WP90Rho_LooseIsoPFTau20_v7', 
            'HLT_Ele23_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_HFT30_v8', 
            'HLT_Ele24_WP80_CentralPFJet35_CentralPFJet25_PFMET20_v1', 
            'HLT_Ele24_WP80_CentralPFJet35_CentralPFJet25_v1', 
            'HLT_Ele24_WP80_PFJet30_PFJet25_Deta3_CentralPFJet30_v1', 
            'HLT_Ele24_WP80_PFJet30_PFJet25_Deta3_v1', 
            'HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_CentralPFNoPUJet30_BTagIPIter_v9', 
            'HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_CentralPFNoPUJet30_v8', 
            'HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_DiCentralPFNoPUJet30_v2', 
            'HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30_v4', 
            'HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet45_35_25_v2', 
            'HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet50_40_30_v4', 
            'HLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_v11', 
            'HLT_Ele27_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele15_CaloIdT_CaloIsoVL_trackless_v8', 
            'HLT_Ele27_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_HFT15_v8', 
            'HLT_Ele27_WP80_CentralPFJet80_v9', 
            'HLT_Ele27_WP80_PFMET_MT50_v7', 
            'HLT_Ele27_WP80_WCandPt80_v9', 
            'HLT_Ele27_WP80_v11', 
            'HLT_Ele30_CaloIdVT_TrkIdT_PFNoPUJet100_PFNoPUJet25_v8', 
            'HLT_Ele30_CaloIdVT_TrkIdT_PFNoPUJet150_PFNoPUJet25_v8', 
            'HLT_Ele30_CaloIdVT_TrkIdT_v6', 
            'HLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_v11', 
            'HLT_Ele32_CaloIdT_CaloIsoT_TrkIdT_TrkIsoT_SC17_Mass50_v6', 
            'HLT_Ele5_SC5_Jpsi_Mass2to15_v4', 
            'HLT_Ele80_CaloIdVT_GsfTrkIdT_v2', 
            'HLT_Ele8_CaloIdL_CaloIsoVL_v17', 
            'HLT_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Jet30_v7', 
            'HLT_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v15', 
            'HLT_Ele8_CaloIdT_TrkIdT_DiJet30_v18', 
            'HLT_Ele8_CaloIdT_TrkIdT_QuadJet30_v18', 
            'HLT_Ele8_CaloIdT_TrkIdT_TriJet30_v18', 
            'HLT_Ele8_CaloIdT_TrkIdVL_EG7_v2', 
            'HLT_Ele8_CaloIdT_TrkIdVL_Jet30_v7', 
            'HLT_Ele8_CaloIdT_TrkIdVL_v5', 
            'HLT_Ele90_CaloIdVT_GsfTrkIdT_v2', 
            'HLT_ExclDiJet35_HFAND_v4', 
            'HLT_ExclDiJet35_HFOR_v4', 
            'HLT_ExclDiJet80_HFAND_v4', 
            'HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v10', 
            'HLT_GlobalRunHPDNoise_v8', 
            'HLT_HT200_AlphaT0p57_v8', 
            'HLT_HT200_v6', 
            'HLT_HT250_AlphaT0p55_v8', 
            'HLT_HT250_AlphaT0p57_v8', 
            'HLT_HT250_v7', 
            'HLT_HT300_AlphaT0p53_v8', 
            'HLT_HT300_AlphaT0p54_v14', 
            'HLT_HT300_DoubleDisplacedPFJet60_ChgFraction10_v10', 
            'HLT_HT300_DoubleDisplacedPFJet60_v10', 
            'HLT_HT300_SingleDisplacedPFJet60_ChgFraction10_v10', 
            'HLT_HT300_SingleDisplacedPFJet60_v10', 
            'HLT_HT300_v7', 
            'HLT_HT350_AlphaT0p52_v8', 
            'HLT_HT350_AlphaT0p53_v19', 
            'HLT_HT350_v7', 
            'HLT_HT400_AlphaT0p51_v19', 
            'HLT_HT400_AlphaT0p52_v14', 
            'HLT_HT400_v7', 
            'HLT_HT450_AlphaT0p51_v14', 
            'HLT_HT450_v7', 
            'HLT_HT500_v7', 
            'HLT_HT550_v7', 
            'HLT_HT650_Track50_dEdx3p6_v10', 
            'HLT_HT650_Track60_dEdx3p7_v10', 
            'HLT_HT650_v7', 
            'HLT_HT750_v7', 
            'HLT_HcalCalibration_v3', 
            'HLT_HcalNZS_v10', 
            'HLT_HcalPhiSym_v11', 
            'HLT_HcalUTCA_v1', 
            'HLT_IsoMu12_DoubleCentralJet65_v4', 
            'HLT_IsoMu12_RsqMR30_Rsq0p04_MR200_v4', 
            'HLT_IsoMu12_RsqMR40_Rsq0p04_MR200_v4', 
            'HLT_IsoMu15_eta2p1_L1ETM20_v7', 
            'HLT_IsoMu15_eta2p1_LooseIsoPFTau35_Trk20_Prong1_L1ETM20_v10', 
            'HLT_IsoMu17_eta2p1_CentralPFNoPUJet30_BTagIPIter_v4', 
            'HLT_IsoMu17_eta2p1_CentralPFNoPUJet30_v4', 
            'HLT_IsoMu17_eta2p1_DiCentralPFNoPUJet30_PFNoPUHT350_PFMHT40_v3', 
            'HLT_IsoMu17_eta2p1_DiCentralPFNoPUJet30_v4', 
            'HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v7', 
            'HLT_IsoMu17_eta2p1_TriCentralPFNoPUJet30_v4', 
            'HLT_IsoMu17_eta2p1_TriCentralPFNoPUJet45_35_25_v2', 
            'HLT_IsoMu18_CentralPFJet30_CentralPFJet25_PFMET20_v1', 
            'HLT_IsoMu18_CentralPFJet30_CentralPFJet25_v1', 
            'HLT_IsoMu18_PFJet30_PFJet25_Deta3_CentralPFJet25_v1', 
            'HLT_IsoMu18_PFJet30_PFJet25_Deta3_v1', 
            'HLT_IsoMu18_eta2p1_MediumIsoPFTau25_Trk1_eta2p1_Reg_v1', 
            'HLT_IsoMu18_eta2p1_MediumIsoPFTau25_Trk1_eta2p1_v4', 
            'HLT_IsoMu20_WCandPt80_v4', 
            'HLT_IsoMu20_eta2p1_CentralPFJet80_v9', 
            'HLT_IsoMu20_eta2p1_v7', 
            'HLT_IsoMu24_eta2p1_v15', 
            'HLT_IsoMu24_v17', 
            'HLT_IsoMu30_eta2p1_v15', 
            'HLT_IsoMu30_v11', 
            'HLT_IsoMu34_eta2p1_v13', 
            'HLT_IsoMu40_eta2p1_v10', 
            'HLT_IsoMu8_eta2p1_LooseIsoPFTau20_L1ETM26_v1', 
            'HLT_IsoMu8_eta2p1_LooseIsoPFTau20_v1', 
            'HLT_IsoTrackHB_v14', 
            'HLT_IsoTrackHE_v15', 
            'HLT_Jet160Eta2p4_Jet120Eta2p4_DiBTagIP3DFastPVLoose_v7', 
            'HLT_Jet370_NoJetID_v15', 
            'HLT_Jet60Eta1p7_Jet53Eta1p7_DiBTagIP3DFastPV_v7', 
            'HLT_Jet80Eta1p7_Jet70Eta1p7_DiBTagIP3DFastPV_v7', 
            'HLT_JetE30_NoBPTX3BX_NoHalo_v16', 
            'HLT_JetE30_NoBPTX_v14', 
            'HLT_JetE50_NoBPTX3BX_NoHalo_v13', 
            'HLT_JetE70_NoBPTX3BX_NoHalo_v5', 
            'HLT_L1DoubleEG3_FwdVeto_v2', 
            'HLT_L1DoubleJet36Central_v7', 
            'HLT_L1ETM100_v2', 
            'HLT_L1ETM30_v2', 
            'HLT_L1ETM40_v2', 
            'HLT_L1ETM70_v2', 
            'HLT_L1SingleEG12_v6', 
            'HLT_L1SingleEG5_v6', 
            'HLT_L1SingleJet16_v7', 
            'HLT_L1SingleJet36_v7', 
            'HLT_L1SingleMu12_v2', 
            'HLT_L1SingleMuOpen_AntiBPTX_v7', 
            'HLT_L1SingleMuOpen_v7', 
            'HLT_L1Tech_HBHEHO_totalOR_v6', 
            'HLT_L1Tech_HCAL_HF_single_channel_v4', 
            'HLT_L1TrackerCosmics_v7', 
            'HLT_L2DoubleMu23_NoVertex_2Cha_Angle2p5_v3', 
            'HLT_L2DoubleMu23_NoVertex_v11', 
            'HLT_L2DoubleMu38_NoVertex_2Cha_Angle2p5_v3', 
            'HLT_L2Mu10_NoVertex_NoBPTX3BX_NoHalo_v4', 
            'HLT_L2Mu20_NoVertex_2Cha_NoBPTX3BX_NoHalo_v1', 
            'HLT_L2Mu20_eta2p1_NoVertex_v2', 
            'HLT_L2Mu30_NoVertex_2Cha_NoBPTX3BX_NoHalo_v1', 
            'HLT_L2Mu70_2Cha_eta2p1_PFMET55_v2', 
            'HLT_L2Mu70_2Cha_eta2p1_PFMET60_v2', 
            'HLT_L2TripleMu10_0_0_NoVertex_PFJet40Neutral_v8', 
            'HLT_LogMonitor_v4', 
            'HLT_LooseIsoPFTau35_Trk20_Prong1_MET70_v10', 
            'HLT_LooseIsoPFTau35_Trk20_Prong1_MET75_v10', 
            'HLT_LooseIsoPFTau35_Trk20_Prong1_v10', 
            'HLT_MET100_HBHENoiseCleaned_v1', 
            'HLT_MET120_HBHENoiseCleaned_v6', 
            'HLT_MET120_v13', 
            'HLT_MET200_HBHENoiseCleaned_v5', 
            'HLT_MET200_v12', 
            'HLT_MET300_HBHENoiseCleaned_v5', 
            'HLT_MET300_v4', 
            'HLT_MET400_HBHENoiseCleaned_v5', 
            'HLT_MET400_v7', 
            'HLT_MET80_Parked_v5', 
            'HLT_MET80_Track50_dEdx3p6_v6', 
            'HLT_MET80_Track60_dEdx3p7_v6', 
            'HLT_MET80_v5', 
            'HLT_MonoCentralPFJet80_PFMETnoMu105_NHEF0p95_v4', 
            'HLT_Mu12_eta2p1_DiCentral_20_v8', 
            'HLT_Mu12_eta2p1_DiCentral_40_20_BTagIP3D1stTrack_v8', 
            'HLT_Mu12_eta2p1_DiCentral_40_20_DiBTagIP3D1stTrack_v8', 
            'HLT_Mu12_eta2p1_DiCentral_40_20_v8', 
            'HLT_Mu12_eta2p1_L1Mu10erJetC12WdEtaPhi1DiJetsC_v7', 
            'HLT_Mu12_v18', 
            'HLT_Mu13_Mu8_NoDZ_v1', 
            'HLT_Mu13_Mu8_v22', 
            'HLT_Mu14_Ele14_CaloIdT_TrkIdVL_Mass8_PFMET40_v8', 
            'HLT_Mu14_Ele14_CaloIdT_TrkIdVL_Mass8_PFMET50_v8', 
            'HLT_Mu15_TkMu5_Onia_v1', 
            'HLT_Mu15_eta2p1_DiCentral_20_v1', 
            'HLT_Mu15_eta2p1_DiCentral_40_20_v1', 
            'HLT_Mu15_eta2p1_L1ETM20_v5', 
            'HLT_Mu15_eta2p1_L1Mu10erJetC12WdEtaPhi1DiJetsC_v3', 
            'HLT_Mu15_eta2p1_TriCentral_40_20_20_BTagIP3D1stTrack_v8', 
            'HLT_Mu15_eta2p1_TriCentral_40_20_20_DiBTagIP3D1stTrack_v8', 
            'HLT_Mu15_eta2p1_TriCentral_40_20_20_v8', 
            'HLT_Mu15_eta2p1_v5', 
            'HLT_Mu17_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v9', 
            'HLT_Mu17_Mu8_v22', 
            'HLT_Mu17_TkMu8_NoDZ_v1', 
            'HLT_Mu17_TkMu8_v14', 
            'HLT_Mu17_eta2p1_CentralPFNoPUJet30_BTagIPIter_v4', 
            'HLT_Mu17_eta2p1_LooseIsoPFTau20_v7', 
            'HLT_Mu17_eta2p1_TriCentralPFNoPUJet45_35_25_v2', 
            'HLT_Mu17_v5', 
            'HLT_Mu18_CentralPFJet30_CentralPFJet25_v1', 
            'HLT_Mu18_PFJet30_PFJet25_Deta3_CentralPFJet25_v1', 
            'HLT_Mu22_Photon22_CaloIdL_v7', 
            'HLT_Mu22_TkMu22_v9', 
            'HLT_Mu22_TkMu8_v9', 
            'HLT_Mu24_eta2p1_v5', 
            'HLT_Mu24_v16', 
            'HLT_Mu30_Ele30_CaloIdL_v8', 
            'HLT_Mu30_eta2p1_v5', 
            'HLT_Mu30_v16', 
            'HLT_Mu40_PFNoPUHT350_v4', 
            'HLT_Mu40_eta2p1_Track50_dEdx3p6_v5', 
            'HLT_Mu40_eta2p1_Track60_dEdx3p7_v5', 
            'HLT_Mu40_eta2p1_v11', 
            'HLT_Mu40_v14', 
            'HLT_Mu50_eta2p1_v8', 
            'HLT_Mu5_L2Mu3_Jpsi_v8', 
            'HLT_Mu5_Track2_Jpsi_v21', 
            'HLT_Mu5_Track3p5_Jpsi_v7', 
            'HLT_Mu5_v20', 
            'HLT_Mu60_PFNoPUHT350_v4', 
            'HLT_Mu7_Ele7_CaloIdT_CaloIsoVL_v7', 
            'HLT_Mu7_Track7_Jpsi_v20', 
            'HLT_Mu8_DiJet30_v7', 
            'HLT_Mu8_DoubleEle8_CaloIdT_TrkIdVL_v7', 
            'HLT_Mu8_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v9', 
            'HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Ele8_CaloIdL_TrkIdVL_v7', 
            'HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT175_v4', 
            'HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT225_v4', 
            'HLT_Mu8_QuadJet30_v7', 
            'HLT_Mu8_TriJet30_v7', 
            'HLT_Mu8_eta2p1_LooseIsoPFTau20_L1ETM26_v1', 
            'HLT_Mu8_v18', 
            'HLT_PFJet140_v9', 
            'HLT_PFJet200_v9', 
            'HLT_PFJet260_v9', 
            'HLT_PFJet320_v9', 
            'HLT_PFJet400_v9', 
            'HLT_PFJet40_v8', 
            'HLT_PFJet80_v9', 
            'HLT_PFMET150_v7', 
            'HLT_PFMET180_v7', 
            'HLT_PFNoPUHT350_Mu15_PFMET45_v4', 
            'HLT_PFNoPUHT350_Mu15_PFMET50_v4', 
            'HLT_PFNoPUHT350_PFMET100_v4', 
            'HLT_PFNoPUHT350_v4', 
            'HLT_PFNoPUHT400_Mu5_PFMET45_v4', 
            'HLT_PFNoPUHT400_Mu5_PFMET50_v4', 
            'HLT_PFNoPUHT400_PFMET100_v4', 
            'HLT_PFNoPUHT650_DiCentralPFNoPUJet80_CenPFNoPUJet40_v4', 
            'HLT_PFNoPUHT650_v4', 
            'HLT_PFNoPUHT700_v4', 
            'HLT_PFNoPUHT750_v4', 
            'HLT_Photon135_v7', 
            'HLT_Photon150_v4', 
            'HLT_Photon160_v4', 
            'HLT_Photon20_CaloIdVL_IsoL_v16', 
            'HLT_Photon20_CaloIdVL_v4', 
            'HLT_Photon22_R9Id90_HE10_Iso40_EBOnly_v5', 
            'HLT_Photon26_Photon18_v12', 
            'HLT_Photon26_R9Id85_OR_CaloId10_Iso50_Photon18_R9Id85_OR_CaloId10_Iso50_Mass70_v2', 
            'HLT_Photon26_R9Id85_OR_CaloId10_Iso50_Photon18_v5', 
            'HLT_Photon300_NoHE_v5', 
            'HLT_Photon30_CaloIdVL_v14', 
            'HLT_Photon30_R9Id90_CaloId_HE10_Iso40_EBOnly_Met25_HBHENoiseCleaned_v1', 
            'HLT_Photon30_R9Id90_CaloId_HE10_Iso40_EBOnly_v1', 
            'HLT_Photon30_v1', 
            'HLT_Photon36_CaloId10_Iso50_Photon22_CaloId10_Iso50_v6', 
            'HLT_Photon36_CaloId10_Iso50_Photon22_R9Id85_v6', 
            'HLT_Photon36_Photon22_v6', 
            'HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon10_R9Id85_OR_CaloId10_Iso50_Mass80_v1', 
            'HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon22_R9Id85_OR_CaloId10_Iso50_v6', 
            'HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon22_v5', 
            'HLT_Photon36_R9Id85_Photon22_CaloId10_Iso50_v6', 
            'HLT_Photon36_R9Id85_Photon22_R9Id85_v4', 
            'HLT_Photon36_R9Id90_HE10_Iso40_EBOnly_v5', 
            'HLT_Photon40_CaloIdL_RsqMR40_Rsq0p09_MR150_v6', 
            'HLT_Photon40_CaloIdL_RsqMR45_Rsq0p09_MR150_v6', 
            'HLT_Photon40_CaloIdL_RsqMR50_Rsq0p09_MR150_v6', 
            'HLT_Photon50_CaloIdVL_IsoL_v17', 
            'HLT_Photon50_CaloIdVL_v10', 
            'HLT_Photon50_R9Id90_HE10_Iso40_EBOnly_v5', 
            'HLT_Photon60_CaloIdL_HT300_v4', 
            'HLT_Photon60_CaloIdL_MHT70_v11', 
            'HLT_Photon70_CaloIdXL_PFMET100_v7', 
            'HLT_Photon70_CaloIdXL_PFNoPUHT400_v4', 
            'HLT_Photon70_CaloIdXL_PFNoPUHT500_v4', 
            'HLT_Photon75_CaloIdVL_v13', 
            'HLT_Photon75_R9Id90_HE10_Iso40_EBOnly_v5', 
            'HLT_Photon90_CaloIdVL_v10', 
            'HLT_Photon90_R9Id90_HE10_Iso40_EBOnly_v5', 
            'HLT_Physics_v5', 
            'HLT_PixelTracks_Multiplicity70_v3', 
            'HLT_PixelTracks_Multiplicity80_v12', 
            'HLT_PixelTracks_Multiplicity90_v3', 
            'HLT_QuadJet45_v1', 
            'HLT_QuadJet50_v5', 
            'HLT_QuadJet60_DiJet20_v6', 
            'HLT_QuadJet70_v6', 
            'HLT_QuadJet75_55_35_20_BTagIP_VBF_v7', 
            'HLT_QuadJet75_55_35_20_VBF_v1', 
            'HLT_QuadJet75_55_38_20_BTagIP_VBF_v7', 
            'HLT_QuadJet80_v6', 
            'HLT_QuadJet90_v6', 
            'HLT_QuadPFJet78_61_44_31_BTagCSV_VBF_v6', 
            'HLT_QuadPFJet78_61_44_31_VBF_v1', 
            'HLT_QuadPFJet82_65_48_35_BTagCSV_VBF_v6', 
            'HLT_Random_v2', 
            'HLT_RelIso1p0Mu20_v3', 
            'HLT_RelIso1p0Mu5_Ele8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT175_v4', 
            'HLT_RelIso1p0Mu5_Ele8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT225_v4', 
            'HLT_RelIso1p0Mu5_v6', 
            'HLT_RsqMR40_Rsq0p04_v6', 
            'HLT_RsqMR45_Rsq0p09_v5', 
            'HLT_RsqMR55_Rsq0p09_MR150_v6', 
            'HLT_RsqMR60_Rsq0p09_MR150_v6', 
            'HLT_RsqMR65_Rsq0p09_MR150_v5', 
            'HLT_SingleForJet15_v4', 
            'HLT_SingleForJet25_v4', 
            'HLT_SixJet35_v6', 
            'HLT_SixJet45_v6', 
            'HLT_SixJet50_v6', 
            'HLT_Tau2Mu_ItTrack_v7', 
            'HLT_TripleEle10_CaloIdL_TrkIdVL_v18', 
            'HLT_TripleMu5_v19', 
            'HLT_ZeroBiasPixel_DoubleTrack_v2', 
            'HLT_ZeroBias_v7' ) )
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_hltDoublePFTau25TrackPt5MediumIsolationProng4L1HLTMatched_*_*', 
        'keep *_hltDoublePFTau25TrackPt5MediumIsolationProng4_*_*', 
        'keep *_hltDoublePFTau25TrackPt5MediumIsolation_*_*', 
        'keep *_hltDoublePFTau25TrackPt5_*_*', 
        'keep *_hltDoublePFTau25_*_*', 
        'keep *_hltEle20CaloIdVTTrkIdTDphiFilter_*_*', 
        'keep *_hltIter1Merged_*_*', 
        'keep *_hltIter2Merged_*_*', 
        'keep *_hltIter3Merged_*_*', 
        'keep *_hltIter4Merged_*_*', 
        'keep *_hltL1extraParticlesCentral_*_*', 
        'keep *_hltL1extraParticlesNonIsolated_*_*', 
        'keep *_hltL1extraParticlesTau_*_*', 
        'keep *_hltL1extraParticles_*_*', 
        'keep *_hltL1sDoubleTauJet44erorDoubleJetC64_*_*', 
        'keep *_hltL1sL1EG18er_*_*', 
        'keep *_hltL1sL1ETM36ORETM40_*_*', 
        'keep *_hltL1sMu16Eta2p1_*_*', 
        'keep *_hltL3TkTracksFromL2_*_*', 
        'keep *_hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f18QL3crIsoRhoFiltered0p15_*_*', 
        'keep *_hltOverlapFilterEle20LooseIsoPFTau20OldVersion_*_*', 
        'keep *_hltOverlapFilterIsoMu18LooseIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu18PFTau25TrackPt5Prong4_*_*', 
        'keep *_hltPFTau20IsoMuVertex_*_*', 
        'keep *_hltPFTau20TrackLooseIso_*_*', 
        'keep *_hltPFTau20Track_*_*', 
        'keep *_hltPFTau20_*_*', 
        'keep *_hltPFTau25TrackPt5MediumIsolationProng4IsoMuVertex_*_*', 
        'keep *_hltPFTau25TrackPt5MediumIsolationProng4_*_*', 
        'keep *_hltPFTau25TrackPt5MediumIsolation_*_*', 
        'keep *_hltPFTau25TrackPt5_*_*', 
        'keep *_hltPFTau25_*_*', 
        'keep *_hltPFTau35TrackPt20LooseIsoProng2_*_*', 
        'keep *_hltPFTau35TrackPt20LooseIso_*_*', 
        'keep *_hltPFTau35TrackPt20_*_*', 
        'keep *_hltPFTau35Track_*_*', 
        'keep *_hltPFTau35_*_*', 
        'keep *_hltPFTauEleVertex20_*_*', 
        'keep *_hltPixelTracks_*_*', 
        'keep *_hltPixelVertices3DbbPhi_*_*', 
        'keep *_hltPixelVertices_*_*', 
        'keep *_hltTriggerSummaryAOD_*_*', 
        'keep *_hltTriggerSummaryRAW_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_rawDataRepacker_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep recoCaloJets_*_*_*', 
        'keep recoCaloMETs_*_*_*', 
        'keep recoCompositeCandidates_*_*_*', 
        'keep recoElectrons_*_*_*', 
        'keep recoIsolatedPixelTrackCandidates_*_*_*', 
        'keep recoMETs_*_*_*', 
        'keep recoPFJets_*_*_*', 
        'keep recoPFTaus_*_*_*', 
        'keep recoRecoChargedCandidates_*_*_*', 
        'keep recoRecoEcalCandidates_*_*_*', 
        'keep triggerTriggerEventWithRefs_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep triggerTriggerFilterObjectWithRefs_*_*_*')
)


process.hltOutputNanoDST = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('RAW')
    ),
    fileName = cms.untracked.string('outputNanoDST.root'),
    fastCloning = cms.untracked.bool(False),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('DST_Physics_v5')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_hltFEDSelector_*_*', 
        'keep L1GlobalTriggerReadoutRecord_hltGtDigis_*_*', 
        'keep L1MuGMTReadoutCollection_hltGtDigis_*_*', 
        'keep edmTriggerResults_*_*_*')
)


process.hltOutputPhysicsDST = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('RAW')
    ),
    fileName = cms.untracked.string('outputPhysicsDST.root'),
    fastCloning = cms.untracked.bool(False),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('DST_Ele8_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT250_v4', 
            'DST_HT250_v4', 
            'DST_L1HTT_Or_L1MultiJet_v4', 
            'DST_Mu5_HT250_v4')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_hltActivityPhotonClusterShape_*_*', 
        'keep *_hltActivityPhotonEcalIso_*_*', 
        'keep *_hltActivityPhotonHcalForHE_*_*', 
        'keep *_hltActivityPhotonHcalIso_*_*', 
        'keep *_hltCaloJetIDPassed_*_*', 
        'keep *_hltElectronActivityDetaDphi_*_*', 
        'keep *_hltHitElectronActivityTrackIsol_*_*', 
        'keep *_hltKT6CaloJets_rho*_*', 
        'keep *_hltL3MuonCandidates_*_*', 
        'keep *_hltL3MuonCombRelIsolations_*_*', 
        'keep *_hltMetClean_*_*', 
        'keep *_hltMet_*_*', 
        'keep *_hltPixelMatchElectronsActivity_*_*', 
        'keep *_hltPixelVertices_*_*', 
        'keep *_hltRecoEcalSuperClusterActivityCandidate_*_*', 
        'keep L1GlobalTriggerReadoutRecord_hltGtDigis_*_*', 
        'keep edmTriggerResults_*_*_*')
)


process.hltOutputRPCMON = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('RAW')
    ),
    fileName = cms.untracked.string('outputRPCMON.root'),
    fastCloning = cms.untracked.bool(False),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('AlCa_RPCMuonNoHits_v9', 
            'AlCa_RPCMuonNoTriggers_v9', 
            'AlCa_RPCMuonNormalisation_v9')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_hltCscSegments_*_*', 
        'keep *_hltDt4DSegments_*_*', 
        'keep *_hltMuonCSCDigis_MuonCSCStripDigi_*', 
        'keep *_hltMuonCSCDigis_MuonCSCWireDigi_*', 
        'keep *_hltMuonDTDigis_*_*', 
        'keep *_hltMuonRPCDigis_*_*', 
        'keep *_hltRpcRecHits_*_*', 
        'keep L1GlobalTriggerReadoutRecord_hltGtDigis_*_*', 
        'keep L1MuGMTCands_hltGtDigis_*_*', 
        'keep L1MuGMTReadoutCollection_hltGtDigis_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*')
)


process.hltOutputTrackerCalibration = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('RAW')
    ),
    fileName = cms.untracked.string('outputTrackerCalibration.root'),
    fastCloning = cms.untracked.bool(False),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('HLT_TrackerCalibration_v3')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_hltTrackerCalibrationRaw_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*')
)


process.HLTMuonLocalRecoSequence = cms.Sequence(process.hltMuonDTDigis+process.hltDt1DRecHits+process.hltDt4DSegments+process.hltMuonCSCDigis+process.hltCsc2DRecHits+process.hltCscSegments+process.hltMuonRPCDigis+process.hltRpcRecHits)


process.HLTDoLocalPixelSequence = cms.Sequence(process.hltSiPixelDigis+process.hltSiPixelClusters+process.hltSiPixelRecHits)


process.HLTDoLocalStripSequence = cms.Sequence(process.hltSiStripExcludedFEDListProducer+process.hltSiStripRawToClustersFacility+process.hltSiStripClusters)


process.HLTL3muonTkCandidateSequence = cms.Sequence(process.HLTDoLocalPixelSequence+process.HLTDoLocalStripSequence+process.hltL3TrajSeedOIState+process.hltL3TrackCandidateFromL2OIState+process.hltL3TkTracksFromL2OIState+process.hltL3MuonsOIState+process.hltL3TrajSeedOIHit+process.hltL3TrackCandidateFromL2OIHit+process.hltL3TkTracksFromL2OIHit+process.hltL3MuonsOIHit+process.hltL3TkFromL2OICombination+process.hltL3TrajSeedIOHit+process.hltL3TrackCandidateFromL2IOHit+process.hltL3TkTracksFromL2IOHit+process.hltL3MuonsIOHit+process.hltL3TrajectorySeed+process.hltL3TrackCandidateFromL2)


process.HLTL3muonrecoNocandSequence = cms.Sequence(process.HLTL3muonTkCandidateSequence+process.hltL3TkTracksFromL2+process.hltL3MuonsLinksCombination+process.hltL3Muons)


process.HLTBeamSpot = cms.Sequence(process.hltScalersRawToDigi+process.hltOnlineBeamSpot)


process.HLTL3muonrecoSequence = cms.Sequence(process.HLTL3muonrecoNocandSequence+process.hltL3MuonCandidates)


process.HLTL1UnpackerSequence = cms.Sequence(process.hltGtDigis+process.hltGctDigis+process.hltL1GtObjectMap+process.hltL1extraParticles)


process.HLTL2muonrecoNocandSequence = cms.Sequence(process.HLTMuonLocalRecoSequence+process.hltL2OfflineMuonSeeds+process.hltL2MuonSeeds+process.hltL2Muons)


process.HLTEndSequence = cms.Sequence(process.hltBoolEnd)


process.HLTBeginSequence = cms.Sequence(process.hltTriggerType+process.HLTL1UnpackerSequence+process.HLTBeamSpot)


process.HLTL2muonrecoSequence = cms.Sequence(process.HLTL2muonrecoNocandSequence+process.hltL2MuonCandidates)


process.HLT_Mu17_Mu8_v22 = cms.Path(process.HLTBeginSequence+process.hltL1sL1DoubleMu10MuOpenORDoubleMu103p5+process.hltPreMu17Mu8+process.hltL1DoubleMu10MuOpenOR3p5L1Filtered0+process.HLTL2muonrecoSequence+process.hltL2pfL1DoubleMu10MuOpenOR3p5L1f0L2PreFiltered0+process.hltL2fL1DoubleMu10MuOpenOR3p5L1f0L2Filtered10+process.HLTL3muonrecoSequence+process.hltL3pfL1DoubleMu10MuOpenOR3p5L1f0L2pf0L3PreFiltered8+process.hltL3fL1DoubleMu10MuOpenOR3p5L1f0L2f10L3Filtered17+process.hltDiMuonGlb17Glb8DzFiltered0p2+process.HLTEndSequence)

process.hltTriggerSummaryAOD = cms.EDProducer("TriggerSummaryProducerAOD",
                                                  processName = cms.string('@')
                                              )

process.hltTriggerSummaryRAW = cms.EDProducer("TriggerSummaryProducerRAW",
                                                  processName = cms.string('@')
                                              )

process.HLTriggerFinalPath = cms.Path(process.hltTriggerSummaryAOD+process.hltTriggerSummaryRAW)

process.FULLOutput = cms.EndPath(process.hltOutputFULL)


process.DQM = cms.Service("DQM",
    debug = cms.untracked.bool(False),
    publishFrequency = cms.untracked.double(5.0),
    collectorPort = cms.untracked.int32(0),
    collectorHost = cms.untracked.string('')
)


process.DQMStore = cms.Service("DQMStore")


process.DTDataIntegrityTask = cms.Service("DTDataIntegrityTask",
    processingMode = cms.untracked.string('HLT'),
    fedIntegrityFolder = cms.untracked.string('DT/FEDIntegrity_EvF'),
    getSCInfo = cms.untracked.bool(True)
)


process.FastTimerService = cms.Service("FastTimerService",
    dqmPath = cms.untracked.string('HLT/TimerService'),
    dqmModuleTimeRange = cms.untracked.double(40.0),
    luminosityProduct = cms.untracked.InputTag("hltScalersRawToDigi"),
    enableDQMbyLuminosity = cms.untracked.bool(True),
    enableTimingModules = cms.untracked.bool(True),
    enableDQMbyPathOverhead = cms.untracked.bool(False),
    enableDQMbyModule = cms.untracked.bool(False),
    dqmLuminosityResolution = cms.untracked.double(1e+31),
    enableTimingExclusive = cms.untracked.bool(False),
    skipFirstPath = cms.untracked.bool(False),
    enableDQMbyLumiSection = cms.untracked.bool(True),
    dqmPathTimeResolution = cms.untracked.double(0.5),
    dqmPathTimeRange = cms.untracked.double(100.0),
    enableTimingSummary = cms.untracked.bool(False),
    dqmTimeRange = cms.untracked.double(1000.0),
    dqmLumiSectionsRange = cms.untracked.uint32(2500),
    enableDQMbyProcesses = cms.untracked.bool(True),
    enableDQMSummary = cms.untracked.bool(True),
    useRealTimeClock = cms.untracked.bool(True),
    enableDQMbyPathTotal = cms.untracked.bool(False),
    enableTimingPaths = cms.untracked.bool(True),
    enableDQMbyPathExclusive = cms.untracked.bool(False),
    dqmTimeResolution = cms.untracked.double(5.0),
    supportedProcesses = cms.untracked.vuint32(8, 12, 16, 24, 32),
    dqmModuleTimeResolution = cms.untracked.double(0.2),
    dqmLuminosityRange = cms.untracked.double(1e+34),
    enableDQMbyPathActive = cms.untracked.bool(False),
    enableDQMbyPathDetails = cms.untracked.bool(False),
    enableDQM = cms.untracked.bool(True),
    enableDQMbyPathCounters = cms.untracked.bool(False)
)


process.MessageLogger = cms.Service("MessageLogger",
    suppressInfo = cms.untracked.vstring(),
    debugs = cms.untracked.PSet(
        suppressInfo = cms.untracked.vstring(),
        suppressDebug = cms.untracked.vstring(),
        suppressWarning = cms.untracked.vstring(),
        suppressError = cms.untracked.vstring(),
        threshold = cms.untracked.string('INFO'),
        placeholder = cms.untracked.bool(True)
    ),
    suppressDebug = cms.untracked.vstring(),
    cout = cms.untracked.PSet(
        suppressWarning = cms.untracked.vstring(),
        suppressInfo = cms.untracked.vstring(),
        suppressDebug = cms.untracked.vstring(),
        suppressError = cms.untracked.vstring(),
        threshold = cms.untracked.string('ERROR')
    ),
    cerr_stats = cms.untracked.PSet(
        optionalPSet = cms.untracked.bool(True),
        output = cms.untracked.string('cerr'),
        threshold = cms.untracked.string('WARNING')
    ),
    warnings = cms.untracked.PSet(
        suppressInfo = cms.untracked.vstring(),
        suppressDebug = cms.untracked.vstring(),
        suppressWarning = cms.untracked.vstring(),
        suppressError = cms.untracked.vstring(),
        threshold = cms.untracked.string('INFO'),
        placeholder = cms.untracked.bool(True)
    ),
    threshold = cms.untracked.string('INFO'),
    statistics = cms.untracked.vstring('cerr'),
    cerr = cms.untracked.PSet(
        INFO = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        suppressInfo = cms.untracked.vstring(),
        noTimeStamps = cms.untracked.bool(False),
        suppressDebug = cms.untracked.vstring(),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000)
        ),
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        suppressWarning = cms.untracked.vstring(),
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        suppressError = cms.untracked.vstring(),
        FwkSummary = cms.untracked.PSet(
            reportEvery = cms.untracked.int32(1),
            limit = cms.untracked.int32(10000000)
        ),
        threshold = cms.untracked.string('INFO'),
        FwkReport = cms.untracked.PSet(
            reportEvery = cms.untracked.int32(1),
            limit = cms.untracked.int32(0)
        )
    ),
    FrameworkJobReport = cms.untracked.PSet(
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000)
        )
    ),
    suppressWarning = cms.untracked.vstring('hltOnlineBeamSpot', 
        'hltCtf3HitL1SeededWithMaterialTracks', 
        'hltL3MuonsOIState', 
        'hltPixelTracksForHighMult', 
        'hltHITPixelTracksHE', 
        'hltHITPixelTracksHB', 
        'hltCtfL1SeededWithMaterialTracks', 
        'hltRegionalTracksForL3MuonIsolation', 
        'hltSiPixelClusters', 
        'hltActivityStartUpElectronPixelSeeds', 
        'hltLightPFTracks', 
        'hltPixelVertices3DbbPhi', 
        'hltL3MuonsIOHit', 
        'hltPixelTracks', 
        'hltSiPixelDigis', 
        'hltL3MuonsOIHit', 
        'hltL1SeededElectronGsfTracks', 
        'hltL1SeededStartUpElectronPixelSeeds', 
        'hltBLifetimeRegionalCtfWithMaterialTracksbbPhiL1FastJetFastPV', 
        'hltCtfActivityWithMaterialTracks'),
    suppressError = cms.untracked.vstring('hltOnlineBeamSpot', 
        'hltL3MuonCandidates', 
        'hltL3TkTracksFromL2OIState', 
        'hltPFJetCtfWithMaterialTracks', 
        'hltL3TkTracksFromL2IOHit', 
        'hltL3TkTracksFromL2OIHit'),
    errors = cms.untracked.PSet(
        suppressInfo = cms.untracked.vstring(),
        suppressDebug = cms.untracked.vstring(),
        suppressWarning = cms.untracked.vstring(),
        suppressError = cms.untracked.vstring(),
        threshold = cms.untracked.string('INFO'),
        placeholder = cms.untracked.bool(True)
    ),
    destinations = cms.untracked.vstring('warnings', 
        'errors', 
        'infos', 
        'debugs', 
        'cout', 
        'cerr'),
    debugModules = cms.untracked.vstring(),
    infos = cms.untracked.PSet(
        suppressInfo = cms.untracked.vstring(),
        suppressDebug = cms.untracked.vstring(),
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        suppressWarning = cms.untracked.vstring(),
        suppressError = cms.untracked.vstring(),
        threshold = cms.untracked.string('INFO'),
        placeholder = cms.untracked.bool(True)
    ),
    categories = cms.untracked.vstring('FwkJob', 
        'FwkReport', 
        'FwkSummary', 
        'Root_NoDictionary', 
        'TriggerSummaryProducerAOD', 
        'L1GtTrigReport', 
        'HLTrigReport', 
        'FastReport'),
    fwkJobReports = cms.untracked.vstring('FrameworkJobReport')
)


process.MicroStateService = cms.Service("MicroStateService")


process.ModuleWebRegistry = cms.Service("ModuleWebRegistry")


process.PrescaleService = cms.Service("PrescaleService",
    prescaleTable = cms.VPSet(),
    forceDefault = cms.bool(False),
    lvl1DefaultLabel = cms.string('0'),
    lvl1Labels = cms.vstring('0', 
        '1', 
        '2', 
        '3', 
        '4', 
        '5', 
        '6', 
        '7', 
        '8', 
        '9')
)


process.UpdaterService = cms.Service("UpdaterService")


process.AnyDirectionAnalyticalPropagator = cms.ESProducer("AnalyticalPropagatorESProducer",
    MaxDPhi = cms.double(1.6),
    ComponentName = cms.string('AnyDirectionAnalyticalPropagator'),
    PropagationDirection = cms.string('anyDirection')
)


process.AutoMagneticFieldESProducer = cms.ESProducer("AutoMagneticFieldESProducer",
    label = cms.untracked.string(''),
    nominalCurrents = cms.untracked.vint32(-1, 0, 9558, 14416, 16819, 
        18268, 19262),
    valueOverride = cms.int32(-1),
    mapLabels = cms.untracked.vstring('090322_3_8t', 
        '0t', 
        '071212_2t', 
        '071212_3t', 
        '071212_3_5t', 
        '090322_3_8t', 
        '071212_4t')
)


process.CSCGeometryESModule = cms.ESProducer("CSCGeometryESModule",
    appendToDataLabel = cms.string(''),
    useDDD = cms.bool(False),
    alignmentsLabel = cms.string(''),
    useGangedStripsInME1a = cms.bool(True),
    debugV = cms.untracked.bool(False),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True),
    useCentreTIOffsets = cms.bool(False),
    applyAlignment = cms.bool(True)
)


process.CaloGeometryBuilder = cms.ESProducer("CaloGeometryBuilder",
    SelectedCalos = cms.vstring('HCAL', 
        'ZDC', 
        'EcalBarrel', 
        'EcalEndcap', 
        'EcalPreshower', 
        'TOWER')
)


process.CaloTopologyBuilder = cms.ESProducer("CaloTopologyBuilder")


process.CaloTowerConstituentsMapBuilder = cms.ESProducer("CaloTowerConstituentsMapBuilder",
    MapFile = cms.untracked.string('Geometry/CaloTopology/data/CaloTowerEEGeometric.map.gz')
)


process.CaloTowerGeometryFromDBEP = cms.ESProducer("CaloTowerGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.CastorDbProducer = cms.ESProducer("CastorDbProducer",
    appendToDataLabel = cms.string('')
)


process.ClusterShapeHitFilterESProducer = cms.ESProducer("ClusterShapeHitFilterESProducer",
    ComponentName = cms.string('ClusterShapeHitFilter')
)


process.DTGeometryESModule = cms.ESProducer("DTGeometryESModule",
    appendToDataLabel = cms.string(''),
    fromDDD = cms.bool(False),
    applyAlignment = cms.bool(True),
    alignmentsLabel = cms.string('')
)


process.EcalBarrelGeometryFromDBEP = cms.ESProducer("EcalBarrelGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalElectronicsMappingBuilder = cms.ESProducer("EcalElectronicsMappingBuilder")


process.EcalEndcapGeometryFromDBEP = cms.ESProducer("EcalEndcapGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalLaserCorrectionService = cms.ESProducer("EcalLaserCorrectionService")


process.EcalPreshowerGeometryFromDBEP = cms.ESProducer("EcalPreshowerGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalUnpackerWorkerESProducer = cms.ESProducer("EcalUnpackerWorkerESProducer",
    ComponentName = cms.string(''),
    ElectronicsMapper = cms.PSet(
        numbXtalTSamples = cms.uint32(10),
        numbTriggerTSamples = cms.uint32(1)
    ),
    UncalibRHAlgo = cms.PSet(
        Type = cms.string('EcalUncalibRecHitWorkerWeights')
    ),
    DCCDataUnpacker = cms.PSet(
        tccUnpacking = cms.bool(False),
        orderedDCCIdList = cms.vint32(1, 2, 3, 4, 5, 
            6, 7, 8, 9, 10, 
            11, 12, 13, 14, 15, 
            16, 17, 18, 19, 20, 
            21, 22, 23, 24, 25, 
            26, 27, 28, 29, 30, 
            31, 32, 33, 34, 35, 
            36, 37, 38, 39, 40, 
            41, 42, 43, 44, 45, 
            46, 47, 48, 49, 50, 
            51, 52, 53, 54),
        srpUnpacking = cms.bool(False),
        syncCheck = cms.bool(False),
        feIdCheck = cms.bool(True),
        headerUnpacking = cms.bool(True),
        orderedFedList = cms.vint32(601, 602, 603, 604, 605, 
            606, 607, 608, 609, 610, 
            611, 612, 613, 614, 615, 
            616, 617, 618, 619, 620, 
            621, 622, 623, 624, 625, 
            626, 627, 628, 629, 630, 
            631, 632, 633, 634, 635, 
            636, 637, 638, 639, 640, 
            641, 642, 643, 644, 645, 
            646, 647, 648, 649, 650, 
            651, 652, 653, 654),
        feUnpacking = cms.bool(True),
        forceKeepFRData = cms.bool(False),
        memUnpacking = cms.bool(True)
    ),
    CalibRHAlgo = cms.PSet(
        EBLaserMAX = cms.double(2.0),
        EELaserMIN = cms.double(0.5),
        flagsMapDBReco = cms.vint32(0, 0, 0, 0, 4, 
            -1, -1, -1, 4, 4, 
            7, 7, 7, 8, 9),
        EELaserMAX = cms.double(3.0),
        ChannelStatusToBeExcluded = cms.vint32(10, 11, 12, 13, 14),
        laserCorrection = cms.bool(True),
        EBLaserMIN = cms.double(0.5),
        killDeadChannels = cms.bool(True),
        Type = cms.string('EcalRecHitWorkerSimple')
    )
)


process.HcalGeometryFromDBEP = cms.ESProducer("HcalGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.HcalTopologyIdealEP = cms.ESProducer("HcalTopologyIdealEP")


process.MaterialPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    PropagationDirection = cms.string('alongMomentum'),
    ComponentName = cms.string('PropagatorWithMaterial'),
    Mass = cms.double(0.105),
    ptMin = cms.double(-1.0),
    MaxDPhi = cms.double(1.6),
    useRungeKutta = cms.bool(False)
)


process.MaterialPropagatorForHI = cms.ESProducer("PropagatorWithMaterialESProducer",
    PropagationDirection = cms.string('alongMomentum'),
    ComponentName = cms.string('PropagatorWithMaterialForHI'),
    Mass = cms.double(0.139),
    ptMin = cms.double(-1.0),
    MaxDPhi = cms.double(1.6),
    useRungeKutta = cms.bool(False)
)


process.OppositeMaterialPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    PropagationDirection = cms.string('oppositeToMomentum'),
    ComponentName = cms.string('PropagatorWithMaterialOpposite'),
    Mass = cms.double(0.105),
    ptMin = cms.double(-1.0),
    MaxDPhi = cms.double(1.6),
    useRungeKutta = cms.bool(False)
)


process.OppositeMaterialPropagatorForHI = cms.ESProducer("PropagatorWithMaterialESProducer",
    PropagationDirection = cms.string('oppositeToMomentum'),
    ComponentName = cms.string('PropagatorWithMaterialOppositeForHI'),
    Mass = cms.double(0.139),
    ptMin = cms.double(-1.0),
    MaxDPhi = cms.double(1.6),
    useRungeKutta = cms.bool(False)
)


process.RPCGeometryESModule = cms.ESProducer("RPCGeometryESModule",
    useDDD = cms.untracked.bool(False),
    compatibiltyWith11 = cms.untracked.bool(True)
)


process.SiStripGainESProducer = cms.ESProducer("SiStripGainESProducer",
    printDebug = cms.untracked.bool(False),
    appendToDataLabel = cms.string(''),
    APVGain = cms.VPSet(cms.PSet(
        Record = cms.string('SiStripApvGainRcd'),
        NormalizationFactor = cms.untracked.double(1.0),
        Label = cms.untracked.string('')
    ), 
        cms.PSet(
            Record = cms.string('SiStripApvGain2Rcd'),
            NormalizationFactor = cms.untracked.double(1.0),
            Label = cms.untracked.string('')
        )),
    AutomaticNormalization = cms.bool(False)
)


process.SiStripQualityESProducer = cms.ESProducer("SiStripQualityESProducer",
    appendToDataLabel = cms.string(''),
    PrintDebugOutput = cms.bool(False),
    PrintDebug = cms.untracked.bool(False),
    ThresholdForReducedGranularity = cms.double(0.3),
    UseEmptyRunInfo = cms.bool(False),
    ReduceGranularity = cms.bool(False),
    ListOfRecordToMerge = cms.VPSet(cms.PSet(
        record = cms.string('SiStripDetVOffRcd'),
        tag = cms.string('')
    ), 
        cms.PSet(
            record = cms.string('SiStripDetCablingRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadChannelRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadFiberRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadModuleRcd'),
            tag = cms.string('')
        ))
)


process.SiStripRecHitMatcherESProducer = cms.ESProducer("SiStripRecHitMatcherESProducer",
    ComponentName = cms.string('StandardMatcher'),
    NSigmaInside = cms.double(3.0)
)


process.SlaveField0 = cms.ESProducer("UniformMagneticFieldESProducer",
    ZFieldInTesla = cms.double(0.0),
    label = cms.untracked.string('slave_0')
)


process.SlaveField20 = cms.ESProducer("ParametrizedMagneticFieldProducer",
    version = cms.string('OAE_1103l_071212'),
    parameters = cms.PSet(
        BValue = cms.string('2_0T')
    ),
    label = cms.untracked.string('slave_20')
)


process.SlaveField30 = cms.ESProducer("ParametrizedMagneticFieldProducer",
    version = cms.string('OAE_1103l_071212'),
    parameters = cms.PSet(
        BValue = cms.string('3_0T')
    ),
    label = cms.untracked.string('slave_30')
)


process.SlaveField35 = cms.ESProducer("ParametrizedMagneticFieldProducer",
    version = cms.string('OAE_1103l_071212'),
    parameters = cms.PSet(
        BValue = cms.string('3_5T')
    ),
    label = cms.untracked.string('slave_35')
)


process.SlaveField38 = cms.ESProducer("ParametrizedMagneticFieldProducer",
    version = cms.string('OAE_1103l_071212'),
    parameters = cms.PSet(
        BValue = cms.string('3_8T')
    ),
    label = cms.untracked.string('slave_38')
)


process.SlaveField40 = cms.ESProducer("ParametrizedMagneticFieldProducer",
    version = cms.string('OAE_1103l_071212'),
    parameters = cms.PSet(
        BValue = cms.string('4_0T')
    ),
    label = cms.untracked.string('slave_40')
)


process.SteppingHelixPropagatorAny = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ComponentName = cms.string('SteppingHelixPropagatorAny'),
    endcapShiftInZNeg = cms.double(0.0),
    PropagationDirection = cms.string('anyDirection'),
    useTuningForL2Speed = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    NoErrorPropagation = cms.bool(False),
    SetVBFPointer = cms.bool(False),
    AssumeNoMaterial = cms.bool(False),
    endcapShiftInZPos = cms.double(0.0),
    useInTeslaFromMagField = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    useEndcapShiftsInZ = cms.bool(False),
    sendLogWarning = cms.bool(False),
    useMatVolumes = cms.bool(True),
    debug = cms.bool(False),
    ApplyRadX0Correction = cms.bool(True),
    useMagVolumes = cms.bool(True),
    returnTangentPlane = cms.bool(True)
)


process.StripCPEfromTrackAngleESProducer = cms.ESProducer("StripCPEESProducer",
    TanDiffusionAngle = cms.double(0.01),
    UncertaintyScaling = cms.double(1.42),
    ThicknessRelativeUncertainty = cms.double(0.02),
    MaybeNoiseThreshold = cms.double(3.5),
    ComponentName = cms.string('StripCPEfromTrackAngle'),
    MinimumUncertainty = cms.double(0.01),
    NoiseThreshold = cms.double(2.3)
)


process.TrackerDigiGeometryESModule = cms.ESProducer("TrackerDigiGeometryESModule",
    appendToDataLabel = cms.string(''),
    fromDDD = cms.bool(False),
    applyAlignment = cms.bool(True),
    alignmentsLabel = cms.string('')
)


process.TrackerGeometricDetESModule = cms.ESProducer("TrackerGeometricDetESModule",
    fromDDD = cms.bool(False)
)


process.TransientTrackBuilderESProducer = cms.ESProducer("TransientTrackBuilderESProducer",
    ComponentName = cms.string('TransientTrackBuilder')
)


process.VBF0 = cms.ESProducer("VolumeBasedMagneticFieldESProducer",
    scalingVolumes = cms.vint32(),
    overrideMasterSector = cms.bool(True),
    useParametrizedTrackerField = cms.bool(True),
    scalingFactors = cms.vdouble(),
    label = cms.untracked.string('0t'),
    version = cms.string('grid_1103l_071212_2t'),
    debugBuilder = cms.untracked.bool(False),
    paramLabel = cms.string('slave_0'),
    cacheLastVolume = cms.untracked.bool(True)
)


process.VBF20 = cms.ESProducer("VolumeBasedMagneticFieldESProducer",
    scalingVolumes = cms.vint32(),
    overrideMasterSector = cms.bool(True),
    useParametrizedTrackerField = cms.bool(True),
    scalingFactors = cms.vdouble(),
    label = cms.untracked.string('071212_2t'),
    version = cms.string('grid_1103l_071212_2t'),
    debugBuilder = cms.untracked.bool(False),
    paramLabel = cms.string('slave_20'),
    cacheLastVolume = cms.untracked.bool(True)
)


process.VBF30 = cms.ESProducer("VolumeBasedMagneticFieldESProducer",
    scalingVolumes = cms.vint32(),
    overrideMasterSector = cms.bool(True),
    useParametrizedTrackerField = cms.bool(True),
    scalingFactors = cms.vdouble(),
    label = cms.untracked.string('071212_3t'),
    version = cms.string('grid_1103l_071212_3t'),
    debugBuilder = cms.untracked.bool(False),
    paramLabel = cms.string('slave_30'),
    cacheLastVolume = cms.untracked.bool(True)
)


process.VBF35 = cms.ESProducer("VolumeBasedMagneticFieldESProducer",
    scalingVolumes = cms.vint32(),
    overrideMasterSector = cms.bool(True),
    useParametrizedTrackerField = cms.bool(True),
    scalingFactors = cms.vdouble(),
    label = cms.untracked.string('071212_3_5t'),
    version = cms.string('grid_1103l_071212_3_5t'),
    debugBuilder = cms.untracked.bool(False),
    paramLabel = cms.string('slave_35'),
    cacheLastVolume = cms.untracked.bool(True)
)


process.VBF38 = cms.ESProducer("VolumeBasedMagneticFieldESProducer",
    scalingVolumes = cms.vint32(14100, 14200, 17600, 17800, 17900, 
        18100, 18300, 18400, 18600, 23100, 
        23300, 23400, 23600, 23800, 23900, 
        24100, 28600, 28800, 28900, 29100, 
        29300, 29400, 29600, 28609, 28809, 
        28909, 29109, 29309, 29409, 29609, 
        28610, 28810, 28910, 29110, 29310, 
        29410, 29610, 28611, 28811, 28911, 
        29111, 29311, 29411, 29611),
    overrideMasterSector = cms.bool(False),
    useParametrizedTrackerField = cms.bool(True),
    scalingFactors = cms.vdouble(1.0, 1.0, 0.994, 1.004, 1.004, 
        1.005, 1.004, 1.004, 0.994, 0.965, 
        0.958, 0.958, 0.953, 0.958, 0.958, 
        0.965, 0.918, 0.924, 0.924, 0.906, 
        0.924, 0.924, 0.918, 0.991, 0.998, 
        0.998, 0.978, 0.998, 0.998, 0.991, 
        0.991, 0.998, 0.998, 0.978, 0.998, 
        0.998, 0.991, 0.991, 0.998, 0.998, 
        0.978, 0.998, 0.998, 0.991),
    label = cms.untracked.string('090322_3_8t'),
    version = cms.string('grid_1103l_090322_3_8t'),
    debugBuilder = cms.untracked.bool(False),
    paramLabel = cms.string('slave_38'),
    cacheLastVolume = cms.untracked.bool(True)
)


process.VBF40 = cms.ESProducer("VolumeBasedMagneticFieldESProducer",
    scalingVolumes = cms.vint32(),
    overrideMasterSector = cms.bool(True),
    useParametrizedTrackerField = cms.bool(True),
    scalingFactors = cms.vdouble(),
    label = cms.untracked.string('071212_4t'),
    version = cms.string('grid_1103l_071212_4t'),
    debugBuilder = cms.untracked.bool(False),
    paramLabel = cms.string('slave_40'),
    cacheLastVolume = cms.untracked.bool(True)
)


process.ZdcGeometryFromDBEP = cms.ESProducer("ZdcGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.caloDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('CaloDetIdAssociator'),
    includeBadChambers = cms.bool(False),
    etaBinSize = cms.double(0.087),
    nEta = cms.int32(70),
    nPhi = cms.int32(72)
)


process.cosmicsNavigationSchoolESProducer = cms.ESProducer("NavigationSchoolESProducer",
    ComponentName = cms.string('CosmicNavigationSchool')
)


process.ecalDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('EcalDetIdAssociator'),
    includeBadChambers = cms.bool(False),
    etaBinSize = cms.double(0.02),
    nEta = cms.int32(300),
    nPhi = cms.int32(360)
)


process.ecalSeverityLevel = cms.ESProducer("EcalSeverityLevelESProducer",
    dbstatusMask = cms.PSet(
        kRecovered = cms.vuint32(),
        kGood = cms.vuint32(0),
        kTime = cms.vuint32(),
        kWeird = cms.vuint32(),
        kBad = cms.vuint32(11, 12, 13, 14, 15, 
            16),
        kProblematic = cms.vuint32(1, 2, 3, 4, 5, 
            6, 7, 8, 9, 10)
    ),
    timeThresh = cms.double(2.0),
    flagMask = cms.PSet(
        kRecovered = cms.vstring('kLeadingEdgeRecovered', 
            'kTowerRecovered'),
        kGood = cms.vstring('kGood'),
        kTime = cms.vstring('kOutOfTime'),
        kWeird = cms.vstring('kWeird', 
            'kDiWeird'),
        kBad = cms.vstring('kFaultyHardware', 
            'kDead', 
            'kKilled'),
        kProblematic = cms.vstring('kPoorReco', 
            'kPoorCalib', 
            'kNoisy', 
            'kSaturated')
    )
)


process.hcalDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('HcalDetIdAssociator'),
    includeBadChambers = cms.bool(False),
    etaBinSize = cms.double(0.087),
    nEta = cms.int32(70),
    nPhi = cms.int32(72)
)


process.hcalRecAlgos = cms.ESProducer("HcalRecAlgoESProducer",
    RecoveredRecHitBits = cms.vstring('TimingAddedBit', 
        'TimingSubtractedBit'),
    SeverityLevels = cms.VPSet(cms.PSet(
        RecHitFlags = cms.vstring(),
        ChannelStatus = cms.vstring(),
        Level = cms.int32(0)
    ), 
        cms.PSet(
            RecHitFlags = cms.vstring(),
            ChannelStatus = cms.vstring('HcalCellCaloTowerProb'),
            Level = cms.int32(1)
        ), 
        cms.PSet(
            RecHitFlags = cms.vstring('HSCP_R1R2', 
                'HSCP_FracLeader', 
                'HSCP_OuterEnergy', 
                'HSCP_ExpFit', 
                'ADCSaturationBit'),
            ChannelStatus = cms.vstring(),
            Level = cms.int32(5)
        ), 
        cms.PSet(
            RecHitFlags = cms.vstring('HBHEHpdHitMultiplicity', 
                'HFDigiTime', 
                'HBHEPulseShape', 
                'HOBit', 
                'HFInTimeWindow', 
                'ZDCBit', 
                'CalibrationBit', 
                'TimingErrorBit', 
                'HBHEFlatNoise', 
                'HBHESpikeNoise', 
                'HBHETriangleNoise', 
                'HBHETS4TS5Noise'),
            ChannelStatus = cms.vstring(),
            Level = cms.int32(8)
        ), 
        cms.PSet(
            RecHitFlags = cms.vstring('HFLongShort', 
                'HFS8S1Ratio', 
                'HFPET'),
            ChannelStatus = cms.vstring(),
            Level = cms.int32(11)
        ), 
        cms.PSet(
            RecHitFlags = cms.vstring(),
            ChannelStatus = cms.vstring('HcalCellCaloTowerMask'),
            Level = cms.int32(12)
        ), 
        cms.PSet(
            RecHitFlags = cms.vstring(),
            ChannelStatus = cms.vstring('HcalCellHot'),
            Level = cms.int32(15)
        ), 
        cms.PSet(
            RecHitFlags = cms.vstring(),
            ChannelStatus = cms.vstring('HcalCellOff', 
                'HcalCellDead'),
            Level = cms.int32(20)
        )),
    DropChannelStatusBits = cms.vstring('HcalCellMask', 
        'HcalCellOff', 
        'HcalCellDead')
)


process.hcal_db_producer = cms.ESProducer("HcalDbProducer")


process.hltCombinedSecondaryVertex = cms.ESProducer("CombinedSecondaryVertexESProducer",
    useTrackWeights = cms.bool(True),
    useCategories = cms.bool(True),
    pseudoMultiplicityMin = cms.uint32(2),
    correctVertexMass = cms.bool(True),
    categoryVariableName = cms.string('vertexCategory'),
    calibrationRecords = cms.vstring('CombinedSVRecoVertex', 
        'CombinedSVPseudoVertex', 
        'CombinedSVNoVertex'),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    charmCut = cms.double(1.5),
    trackFlip = cms.bool(False),
    trackSelection = cms.PSet(
        totalHitsMin = cms.uint32(0),
        jetDeltaRMax = cms.double(0.3),
        qualityClass = cms.string('any'),
        pixelHitsMin = cms.uint32(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        normChi2Max = cms.double(99999.9),
        maxDistToAxis = cms.double(0.07),
        sip2dValMax = cms.double(99999.9),
        maxDecayLen = cms.double(5.0),
        ptMin = cms.double(0.0),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dValMin = cms.double(-99999.9)
    ),
    minimumTrackWeight = cms.double(0.5),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackMultiplicityMin = cms.uint32(3),
    trackPseudoSelection = cms.PSet(
        totalHitsMin = cms.uint32(0),
        jetDeltaRMax = cms.double(0.3),
        qualityClass = cms.string('any'),
        pixelHitsMin = cms.uint32(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        normChi2Max = cms.double(99999.9),
        maxDistToAxis = cms.double(0.07),
        sip2dValMax = cms.double(99999.9),
        maxDecayLen = cms.double(5.0),
        ptMin = cms.double(0.0),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip3dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dValMin = cms.double(-99999.9)
    ),
    trackSort = cms.string('sip2dSig'),
    vertexFlip = cms.bool(False)
)


process.hltESPAK5CaloL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    appendToDataLabel = cms.string(''),
    correctors = cms.vstring('hltESPL1FastJetCorrectionESProducer', 
        'hltESPL2RelativeCorrectionESProducer', 
        'hltESPL3AbsoluteCorrectionESProducer')
)


process.hltESPAK5CaloL2L3 = cms.ESProducer("JetCorrectionESChain",
    appendToDataLabel = cms.string(''),
    correctors = cms.vstring('hltESPL2RelativeCorrectionESProducer', 
        'hltESPL3AbsoluteCorrectionESProducer')
)


process.hltESPAK5PFL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    appendToDataLabel = cms.string(''),
    correctors = cms.vstring('hltESPL1PFFastJetCorrectionESProducer', 
        'hltESPL2PFRelativeCorrectionESProducer', 
        'hltESPL3PFAbsoluteCorrectionESProducer')
)


process.hltESPAK5PFNoPUL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    appendToDataLabel = cms.string(''),
    correctors = cms.vstring('hltESPL1PFNoPUFastJetCorrectionESProducer', 
        'hltESPL2PFNoPURelativeCorrectionESProducer', 
        'hltESPL3PFNoPUAbsoluteCorrectionESProducer')
)


process.hltESPAnalyticalPropagator = cms.ESProducer("AnalyticalPropagatorESProducer",
    MaxDPhi = cms.double(1.6),
    ComponentName = cms.string('hltESPAnalyticalPropagator'),
    PropagationDirection = cms.string('alongMomentum')
)


process.hltESPBwdAnalyticalPropagator = cms.ESProducer("AnalyticalPropagatorESProducer",
    MaxDPhi = cms.double(1.6),
    ComponentName = cms.string('hltESPBwdAnalyticalPropagator'),
    PropagationDirection = cms.string('oppositeToMomentum')
)


process.hltESPBwdElectronPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    PropagationDirection = cms.string('oppositeToMomentum'),
    ComponentName = cms.string('hltESPBwdElectronPropagator'),
    Mass = cms.double(0.000511),
    ptMin = cms.double(-1.0),
    MaxDPhi = cms.double(1.6),
    useRungeKutta = cms.bool(False)
)


process.hltESPChi2EstimatorForRefit = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2EstimatorForRefit'),
    nSigma = cms.double(3.0),
    MaxChi2 = cms.double(100000.0)
)


process.hltESPChi2MeasurementEstimator = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2MeasurementEstimator'),
    nSigma = cms.double(3.0),
    MaxChi2 = cms.double(30.0)
)


process.hltESPChi2MeasurementEstimator16 = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2MeasurementEstimator16'),
    nSigma = cms.double(3.0),
    MaxChi2 = cms.double(16.0)
)


process.hltESPChi2MeasurementEstimator9 = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2MeasurementEstimator9'),
    nSigma = cms.double(3.0),
    MaxChi2 = cms.double(9.0)
)


process.hltESPCkf3HitTrajectoryBuilder = cms.ESProducer("CkfTrajectoryBuilderESProducer",
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    trajectoryFilterName = cms.string('hltESPCkf3HitTrajectoryFilter'),
    maxCand = cms.int32(5),
    ComponentName = cms.string('hltESPCkf3HitTrajectoryBuilder'),
    intermediateCleaning = cms.bool(True),
    MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
    estimator = cms.string('hltESPChi2MeasurementEstimator'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    updator = cms.string('hltESPKFUpdator'),
    alwaysUseInvalidHits = cms.bool(True),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    lostHitPenalty = cms.double(30.0)
)


process.hltESPCkf3HitTrajectoryFilter = cms.ESProducer("TrajectoryFilterESProducer",
    filterPset = cms.PSet(
        chargeSignificance = cms.double(-1.0),
        minPt = cms.double(0.9),
        minHitsMinPt = cms.int32(3),
        ComponentType = cms.string('CkfBaseTrajectoryFilter'),
        maxLostHits = cms.int32(1),
        maxNumberOfHits = cms.int32(-1),
        maxConsecLostHits = cms.int32(1),
        nSigmaMinPt = cms.double(5.0),
        minimumNumberOfHits = cms.int32(3)
    ),
    ComponentName = cms.string('hltESPCkf3HitTrajectoryFilter')
)


process.hltESPCkfTrajectoryBuilder = cms.ESProducer("CkfTrajectoryBuilderESProducer",
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    trajectoryFilterName = cms.string('hltESPCkfTrajectoryFilter'),
    maxCand = cms.int32(5),
    ComponentName = cms.string('hltESPCkfTrajectoryBuilder'),
    intermediateCleaning = cms.bool(True),
    MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
    estimator = cms.string('hltESPChi2MeasurementEstimator'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    updator = cms.string('hltESPKFUpdator'),
    alwaysUseInvalidHits = cms.bool(True),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    lostHitPenalty = cms.double(30.0)
)


process.hltESPCkfTrajectoryBuilderForHI = cms.ESProducer("CkfTrajectoryBuilderESProducer",
    propagatorAlong = cms.string('PropagatorWithMaterialForHI'),
    trajectoryFilterName = cms.string('hltESPCkfTrajectoryFilterForHI'),
    maxCand = cms.int32(5),
    ComponentName = cms.string('hltESPCkfTrajectoryBuilderForHI'),
    intermediateCleaning = cms.bool(False),
    MeasurementTrackerName = cms.string('hltESPMeasurementTrackerForHI'),
    estimator = cms.string('hltESPChi2MeasurementEstimator'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    updator = cms.string('hltESPKFUpdator'),
    alwaysUseInvalidHits = cms.bool(False),
    propagatorOpposite = cms.string('PropagatorWithMaterialOppositeForHI'),
    lostHitPenalty = cms.double(30.0)
)


process.hltESPCkfTrajectoryFilter = cms.ESProducer("TrajectoryFilterESProducer",
    filterPset = cms.PSet(
        chargeSignificance = cms.double(-1.0),
        minPt = cms.double(0.9),
        minHitsMinPt = cms.int32(3),
        ComponentType = cms.string('CkfBaseTrajectoryFilter'),
        maxLostHits = cms.int32(1),
        maxNumberOfHits = cms.int32(-1),
        maxConsecLostHits = cms.int32(1),
        nSigmaMinPt = cms.double(5.0),
        minimumNumberOfHits = cms.int32(5)
    ),
    ComponentName = cms.string('hltESPCkfTrajectoryFilter')
)


process.hltESPCkfTrajectoryFilterForHI = cms.ESProducer("TrajectoryFilterESProducer",
    filterPset = cms.PSet(
        minPt = cms.double(11.0),
        minHitsMinPt = cms.int32(3),
        ComponentType = cms.string('CkfBaseTrajectoryFilter'),
        maxLostHits = cms.int32(1),
        maxNumberOfHits = cms.int32(-1),
        maxConsecLostHits = cms.int32(1),
        minimumNumberOfHits = cms.int32(6),
        nSigmaMinPt = cms.double(5.0),
        chargeSignificance = cms.double(-1.0)
    ),
    ComponentName = cms.string('hltESPCkfTrajectoryFilterForHI')
)


process.hltESPCloseComponentsMerger5D = cms.ESProducer("CloseComponentsMergerESProducer5D",
    ComponentName = cms.string('hltESPCloseComponentsMerger5D'),
    MaxComponents = cms.int32(12),
    DistanceMeasure = cms.string('hltESPKullbackLeiblerDistance5D')
)


process.hltESPDummyDetLayerGeometry = cms.ESProducer("DetLayerGeometryESProducer",
    ComponentName = cms.string('hltESPDummyDetLayerGeometry')
)


process.hltESPESUnpackerWorker = cms.ESProducer("ESUnpackerWorkerESProducer",
    ComponentName = cms.string('hltESPESUnpackerWorker'),
    DCCDataUnpacker = cms.PSet(
        LookupTable = cms.FileInPath('EventFilter/ESDigiToRaw/data/ES_lookup_table.dat')
    ),
    RHAlgo = cms.PSet(
        ESRecoAlgo = cms.int32(0),
        Type = cms.string('ESRecHitWorker')
    )
)


process.hltESPEcalRegionCablingESProducer = cms.ESProducer("EcalRegionCablingESProducer",
    esMapping = cms.PSet(
        LookupTable = cms.FileInPath('EventFilter/ESDigiToRaw/data/ES_lookup_table.dat')
    )
)


process.hltESPEcalTrigTowerConstituentsMapBuilder = cms.ESProducer("EcalTrigTowerConstituentsMapBuilder",
    MapFile = cms.untracked.string('Geometry/EcalMapping/data/EndCap_TTMap.txt')
)


process.hltESPElectronChi2 = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPElectronChi2'),
    nSigma = cms.double(3.0),
    MaxChi2 = cms.double(2000.0)
)


process.hltESPElectronMaterialEffects = cms.ESProducer("GsfMaterialEffectsESProducer",
    BetheHeitlerParametrization = cms.string('BetheHeitler_cdfmom_nC6_O5.par'),
    EnergyLossUpdator = cms.string('GsfBetheHeitlerUpdator'),
    ComponentName = cms.string('hltESPElectronMaterialEffects'),
    MultipleScatteringUpdator = cms.string('MultipleScatteringUpdator'),
    Mass = cms.double(0.000511),
    BetheHeitlerCorrection = cms.int32(2)
)


process.hltESPFastSteppingHelixPropagatorAny = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ComponentName = cms.string('hltESPFastSteppingHelixPropagatorAny'),
    endcapShiftInZNeg = cms.double(0.0),
    PropagationDirection = cms.string('anyDirection'),
    useTuningForL2Speed = cms.bool(True),
    useIsYokeFlag = cms.bool(True),
    NoErrorPropagation = cms.bool(False),
    SetVBFPointer = cms.bool(False),
    AssumeNoMaterial = cms.bool(False),
    endcapShiftInZPos = cms.double(0.0),
    useInTeslaFromMagField = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    useEndcapShiftsInZ = cms.bool(False),
    sendLogWarning = cms.bool(False),
    useMatVolumes = cms.bool(True),
    debug = cms.bool(False),
    ApplyRadX0Correction = cms.bool(True),
    useMagVolumes = cms.bool(True),
    returnTangentPlane = cms.bool(True)
)


process.hltESPFastSteppingHelixPropagatorOpposite = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ComponentName = cms.string('hltESPFastSteppingHelixPropagatorOpposite'),
    endcapShiftInZNeg = cms.double(0.0),
    PropagationDirection = cms.string('oppositeToMomentum'),
    useTuningForL2Speed = cms.bool(True),
    useIsYokeFlag = cms.bool(True),
    NoErrorPropagation = cms.bool(False),
    SetVBFPointer = cms.bool(False),
    AssumeNoMaterial = cms.bool(False),
    endcapShiftInZPos = cms.double(0.0),
    useInTeslaFromMagField = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    useEndcapShiftsInZ = cms.bool(False),
    sendLogWarning = cms.bool(False),
    useMatVolumes = cms.bool(True),
    debug = cms.bool(False),
    ApplyRadX0Correction = cms.bool(True),
    useMagVolumes = cms.bool(True),
    returnTangentPlane = cms.bool(True)
)


process.hltESPFittingSmootherIT = cms.ESProducer("KFFittingSmootherESProducer",
    EstimateCut = cms.double(10.0),
    LogPixelProbabilityCut = cms.double(-16.0),
    Fitter = cms.string('hltESPTrajectoryFitterRK'),
    MinNumberOfHits = cms.int32(3),
    Smoother = cms.string('hltESPTrajectorySmootherRK'),
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('hltESPFittingSmootherIT'),
    NoInvalidHitsBeginEnd = cms.bool(True),
    RejectTracks = cms.bool(True)
)


process.hltESPFittingSmootherRK = cms.ESProducer("KFFittingSmootherESProducer",
    EstimateCut = cms.double(-1.0),
    LogPixelProbabilityCut = cms.double(-16.0),
    Fitter = cms.string('hltESPTrajectoryFitterRK'),
    MinNumberOfHits = cms.int32(5),
    Smoother = cms.string('hltESPTrajectorySmootherRK'),
    BreakTrajWith2ConsecutiveMissing = cms.bool(False),
    ComponentName = cms.string('hltESPFittingSmootherRK'),
    NoInvalidHitsBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True)
)


process.hltESPFwdElectronPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    PropagationDirection = cms.string('alongMomentum'),
    ComponentName = cms.string('hltESPFwdElectronPropagator'),
    Mass = cms.double(0.000511),
    ptMin = cms.double(-1.0),
    MaxDPhi = cms.double(1.6),
    useRungeKutta = cms.bool(False)
)


process.hltESPGlobalDetLayerGeometry = cms.ESProducer("GlobalDetLayerGeometryESProducer",
    ComponentName = cms.string('hltESPGlobalDetLayerGeometry')
)


process.hltESPGlobalTrackingGeometryESProducer = cms.ESProducer("GlobalTrackingGeometryESProducer")


process.hltESPGsfElectronFittingSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    EstimateCut = cms.double(-1.0),
    LogPixelProbabilityCut = cms.double(-16.0),
    Fitter = cms.string('hltESPGsfTrajectoryFitter'),
    MinNumberOfHits = cms.int32(5),
    Smoother = cms.string('hltESPGsfTrajectorySmoother'),
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('hltESPGsfElectronFittingSmoother'),
    NoInvalidHitsBeginEnd = cms.bool(True),
    RejectTracks = cms.bool(True)
)


process.hltESPGsfTrajectoryFitter = cms.ESProducer("GsfTrajectoryFitterESProducer",
    Merger = cms.string('hltESPCloseComponentsMerger5D'),
    ComponentName = cms.string('hltESPGsfTrajectoryFitter'),
    MaterialEffectsUpdator = cms.string('hltESPElectronMaterialEffects'),
    RecoGeometry = cms.string('hltESPGlobalDetLayerGeometry'),
    GeometricalPropagator = cms.string('hltESPAnalyticalPropagator')
)


process.hltESPGsfTrajectorySmoother = cms.ESProducer("GsfTrajectorySmootherESProducer",
    ErrorRescaling = cms.double(100.0),
    RecoGeometry = cms.string('hltESPGlobalDetLayerGeometry'),
    Merger = cms.string('hltESPCloseComponentsMerger5D'),
    ComponentName = cms.string('hltESPGsfTrajectorySmoother'),
    GeometricalPropagator = cms.string('hltESPBwdAnalyticalPropagator'),
    MaterialEffectsUpdator = cms.string('hltESPElectronMaterialEffects')
)


process.hltESPHIMixedLayerPairs = cms.ESProducer("SeedingLayersESProducer",
    layerList = cms.vstring('BPix1+BPix2', 
        'BPix1+BPix3', 
        'BPix2+BPix3', 
        'BPix1+FPix1_pos', 
        'BPix1+FPix1_neg', 
        'BPix1+FPix2_pos', 
        'BPix1+FPix2_neg', 
        'BPix2+FPix1_pos', 
        'BPix2+FPix1_neg', 
        'BPix2+FPix2_pos', 
        'BPix2+FPix2_neg', 
        'FPix1_pos+FPix2_pos', 
        'FPix1_neg+FPix2_neg', 
        'FPix2_pos+TEC1_pos', 
        'FPix2_pos+TEC2_pos', 
        'TEC1_pos+TEC2_pos', 
        'TEC2_pos+TEC3_pos', 
        'FPix2_neg+TEC1_neg', 
        'FPix2_neg+TEC2_neg', 
        'TEC1_neg+TEC2_neg', 
        'TEC2_neg+TEC3_neg'),
    TID = cms.PSet(

    ),
    ComponentName = cms.string('hltESPHIMixedLayerPairs'),
    TEC = cms.PSet(
        useRingSlector = cms.bool(True),
        TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
        minRing = cms.int32(1),
        maxRing = cms.int32(1)
    ),
    FPix = cms.PSet(
        useErrorsFromParam = cms.bool(True),
        hitErrorRPhi = cms.double(0.0051),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        HitProducer = cms.string('hltHISiPixelRecHits'),
        hitErrorRZ = cms.double(0.0036)
    ),
    TOB = cms.PSet(

    ),
    BPix = cms.PSet(
        useErrorsFromParam = cms.bool(True),
        hitErrorRPhi = cms.double(0.0027),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        HitProducer = cms.string('hltHISiPixelRecHits'),
        hitErrorRZ = cms.double(0.006)
    ),
    TIB = cms.PSet(

    )
)


process.hltESPHIPixelLayerPairs = cms.ESProducer("SeedingLayersESProducer",
    layerList = cms.vstring('BPix1+BPix2', 
        'BPix1+BPix3', 
        'BPix2+BPix3', 
        'BPix1+FPix1_pos', 
        'BPix1+FPix1_neg', 
        'BPix1+FPix2_pos', 
        'BPix1+FPix2_neg', 
        'BPix2+FPix1_pos', 
        'BPix2+FPix1_neg', 
        'BPix2+FPix2_pos', 
        'BPix2+FPix2_neg', 
        'FPix1_pos+FPix2_pos', 
        'FPix1_neg+FPix2_neg'),
    TID = cms.PSet(

    ),
    ComponentName = cms.string('hltESPHIPixelLayerPairs'),
    TEC = cms.PSet(

    ),
    FPix = cms.PSet(
        hitErrorRZ = cms.double(0.0036),
        hitErrorRPhi = cms.double(0.0051),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        HitProducer = cms.string('hltHISiPixelRecHits'),
        useErrorsFromParam = cms.bool(True)
    ),
    TOB = cms.PSet(

    ),
    BPix = cms.PSet(
        hitErrorRZ = cms.double(0.006),
        hitErrorRPhi = cms.double(0.0027),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        HitProducer = cms.string('hltHISiPixelRecHits'),
        useErrorsFromParam = cms.bool(True)
    ),
    TIB = cms.PSet(

    )
)


process.hltESPHIPixelLayerTriplets = cms.ESProducer("SeedingLayersESProducer",
    layerList = cms.vstring('BPix1+BPix2+BPix3', 
        'BPix1+BPix2+FPix1_pos', 
        'BPix1+BPix2+FPix1_neg', 
        'BPix1+FPix1_pos+FPix2_pos', 
        'BPix1+FPix1_neg+FPix2_neg'),
    TID = cms.PSet(

    ),
    ComponentName = cms.string('hltESPHIPixelLayerTriplets'),
    TEC = cms.PSet(

    ),
    FPix = cms.PSet(
        hitErrorRZ = cms.double(0.0036),
        hitErrorRPhi = cms.double(0.0051),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        HitProducer = cms.string('hltHISiPixelRecHits'),
        useErrorsFromParam = cms.bool(True)
    ),
    TOB = cms.PSet(

    ),
    BPix = cms.PSet(
        hitErrorRZ = cms.double(0.006),
        hitErrorRPhi = cms.double(0.0027),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        HitProducer = cms.string('hltHISiPixelRecHits'),
        useErrorsFromParam = cms.bool(True)
    ),
    TIB = cms.PSet(

    )
)


process.hltESPHITTRHBuilderWithoutRefit = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    StripCPE = cms.string('Fake'),
    ComponentName = cms.string('hltESPHITTRHBuilderWithoutRefit'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    PixelCPE = cms.string('Fake'),
    Matcher = cms.string('Fake')
)


process.hltESPKFFittingSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    EstimateCut = cms.double(-1.0),
    LogPixelProbabilityCut = cms.double(-16.0),
    Fitter = cms.string('hltESPKFTrajectoryFitter'),
    MinNumberOfHits = cms.int32(5),
    Smoother = cms.string('hltESPKFTrajectorySmoother'),
    BreakTrajWith2ConsecutiveMissing = cms.bool(False),
    ComponentName = cms.string('hltESPKFFittingSmoother'),
    NoInvalidHitsBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True)
)


process.hltESPKFFittingSmootherForL2Muon = cms.ESProducer("KFFittingSmootherESProducer",
    EstimateCut = cms.double(-1.0),
    LogPixelProbabilityCut = cms.double(-16.0),
    Fitter = cms.string('hltESPKFTrajectoryFitterForL2Muon'),
    MinNumberOfHits = cms.int32(5),
    Smoother = cms.string('hltESPKFTrajectorySmootherForL2Muon'),
    BreakTrajWith2ConsecutiveMissing = cms.bool(False),
    ComponentName = cms.string('hltESPKFFittingSmootherForL2Muon'),
    NoInvalidHitsBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True)
)


process.hltESPKFFittingSmootherWithOutliersRejectionAndRK = cms.ESProducer("KFFittingSmootherESProducer",
    EstimateCut = cms.double(20.0),
    LogPixelProbabilityCut = cms.double(-14.0),
    Fitter = cms.string('hltESPRKFitter'),
    MinNumberOfHits = cms.int32(3),
    Smoother = cms.string('hltESPRKSmoother'),
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('hltESPKFFittingSmootherWithOutliersRejectionAndRK'),
    NoInvalidHitsBeginEnd = cms.bool(True),
    RejectTracks = cms.bool(True)
)


process.hltESPKFTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    ComponentName = cms.string('hltESPKFTrajectoryFitter'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator'),
    Updator = cms.string('hltESPKFUpdator'),
    Propagator = cms.string('PropagatorWithMaterial'),
    minHits = cms.int32(3)
)


process.hltESPKFTrajectoryFitterForL2Muon = cms.ESProducer("KFTrajectoryFitterESProducer",
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    ComponentName = cms.string('hltESPKFTrajectoryFitterForL2Muon'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator'),
    Updator = cms.string('hltESPKFUpdator'),
    Propagator = cms.string('hltESPFastSteppingHelixPropagatorAny'),
    minHits = cms.int32(3)
)


process.hltESPKFTrajectorySmoother = cms.ESProducer("KFTrajectorySmootherESProducer",
    errorRescaling = cms.double(100.0),
    minHits = cms.int32(3),
    ComponentName = cms.string('hltESPKFTrajectorySmoother'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator'),
    Updator = cms.string('hltESPKFUpdator'),
    Propagator = cms.string('PropagatorWithMaterial'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry')
)


process.hltESPKFTrajectorySmootherForL2Muon = cms.ESProducer("KFTrajectorySmootherESProducer",
    errorRescaling = cms.double(100.0),
    minHits = cms.int32(3),
    ComponentName = cms.string('hltESPKFTrajectorySmootherForL2Muon'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator'),
    Updator = cms.string('hltESPKFUpdator'),
    Propagator = cms.string('hltESPFastSteppingHelixPropagatorOpposite'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry')
)


process.hltESPKFTrajectorySmootherForMuonTrackLoader = cms.ESProducer("KFTrajectorySmootherESProducer",
    errorRescaling = cms.double(10.0),
    minHits = cms.int32(3),
    ComponentName = cms.string('hltESPKFTrajectorySmootherForMuonTrackLoader'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator'),
    Updator = cms.string('hltESPKFUpdator'),
    Propagator = cms.string('hltESPSmartPropagatorAnyOpposite'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry')
)


process.hltESPKFUpdator = cms.ESProducer("KFUpdatorESProducer",
    ComponentName = cms.string('hltESPKFUpdator')
)


process.hltESPKullbackLeiblerDistance5D = cms.ESProducer("DistanceBetweenComponentsESProducer5D",
    ComponentName = cms.string('hltESPKullbackLeiblerDistance5D'),
    DistanceMeasure = cms.string('KullbackLeibler')
)


process.hltESPL1FastJetCorrectionESProducer = cms.ESProducer("L1FastjetCorrectionESProducer",
    appendToDataLabel = cms.string(''),
    srcRho = cms.InputTag("hltKT6CaloJets","rho"),
    algorithm = cms.string('AK5CaloHLT'),
    level = cms.string('L1FastJet')
)


process.hltESPL1PFFastJetCorrectionESProducer = cms.ESProducer("L1FastjetCorrectionESProducer",
    appendToDataLabel = cms.string(''),
    srcRho = cms.InputTag("hltKT6PFJets","rho"),
    algorithm = cms.string('AK5PFHLT'),
    level = cms.string('L1FastJet')
)


process.hltESPL1PFNoPUFastJetCorrectionESProducer = cms.ESProducer("L1FastjetCorrectionESProducer",
    appendToDataLabel = cms.string(''),
    srcRho = cms.InputTag("hltKT6PFJets","rho"),
    algorithm = cms.string('AK5PFchsHLT'),
    level = cms.string('L1FastJet')
)


process.hltESPL2PFNoPURelativeCorrectionESProducer = cms.ESProducer("LXXXCorrectionESProducer",
    appendToDataLabel = cms.string(''),
    algorithm = cms.string('AK5PFchsHLT'),
    level = cms.string('L2Relative')
)


process.hltESPL2PFRelativeCorrectionESProducer = cms.ESProducer("LXXXCorrectionESProducer",
    appendToDataLabel = cms.string(''),
    algorithm = cms.string('AK5PFHLT'),
    level = cms.string('L2Relative')
)


process.hltESPL2RelativeCorrectionESProducer = cms.ESProducer("LXXXCorrectionESProducer",
    appendToDataLabel = cms.string(''),
    algorithm = cms.string('AK5CaloHLT'),
    level = cms.string('L2Relative')
)


process.hltESPL3AbsoluteCorrectionESProducer = cms.ESProducer("LXXXCorrectionESProducer",
    appendToDataLabel = cms.string(''),
    algorithm = cms.string('AK5CaloHLT'),
    level = cms.string('L3Absolute')
)


process.hltESPL3MuKFTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    ComponentName = cms.string('hltESPL3MuKFTrajectoryFitter'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator'),
    Updator = cms.string('hltESPKFUpdator'),
    Propagator = cms.string('hltESPSmartPropagatorAny'),
    minHits = cms.int32(3)
)


process.hltESPL3PFAbsoluteCorrectionESProducer = cms.ESProducer("LXXXCorrectionESProducer",
    appendToDataLabel = cms.string(''),
    algorithm = cms.string('AK5PFHLT'),
    level = cms.string('L3Absolute')
)


process.hltESPL3PFNoPUAbsoluteCorrectionESProducer = cms.ESProducer("LXXXCorrectionESProducer",
    appendToDataLabel = cms.string(''),
    algorithm = cms.string('AK5PFchsHLT'),
    level = cms.string('L3Absolute')
)


process.hltESPMeasurementTracker = cms.ESProducer("MeasurementTrackerESProducer",
    StripCPE = cms.string('StripCPEfromTrackAngle'),
    inactivePixelDetectorLabels = cms.VInputTag(),
    UseStripCablingDB = cms.bool(False),
    PixelCPE = cms.string('hltESPPixelCPEGeneric'),
    stripLazyGetterProducer = cms.string('hltSiStripRawToClustersFacility'),
    OnDemand = cms.bool(True),
    Regional = cms.bool(True),
    UsePixelModuleQualityDB = cms.bool(True),
    pixelClusterProducer = cms.string('hltSiPixelClusters'),
    switchOffPixelsIfEmpty = cms.bool(True),
    inactiveStripDetectorLabels = cms.VInputTag("hltSiStripExcludedFEDListProducer"),
    MaskBadAPVFibers = cms.bool(True),
    UseStripStripQualityDB = cms.bool(True),
    UsePixelROCQualityDB = cms.bool(True),
    DebugPixelROCQualityDB = cms.untracked.bool(False),
    UseStripAPVFiberQualityDB = cms.bool(True),
    stripClusterProducer = cms.string('hltSiStripClusters'),
    DebugStripAPVFiberQualityDB = cms.untracked.bool(False),
    DebugStripStripQualityDB = cms.untracked.bool(False),
    SiStripQualityLabel = cms.string(''),
    UseStripNoiseDB = cms.bool(False),
    badStripCuts = cms.PSet(
        TID = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TOB = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TEC = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TIB = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        )
    ),
    DebugStripModuleQualityDB = cms.untracked.bool(False),
    ComponentName = cms.string('hltESPMeasurementTracker'),
    DebugPixelModuleQualityDB = cms.untracked.bool(False),
    HitMatcher = cms.string('StandardMatcher'),
    skipClusters = cms.InputTag(""),
    UseStripModuleQualityDB = cms.bool(True)
)


process.hltESPMeasurementTrackerForHI = cms.ESProducer("MeasurementTrackerESProducer",
    StripCPE = cms.string('StripCPEfromTrackAngle'),
    inactivePixelDetectorLabels = cms.VInputTag(),
    UseStripCablingDB = cms.bool(False),
    PixelCPE = cms.string('hltESPPixelCPEGeneric'),
    stripLazyGetterProducer = cms.string('hltSiStripRawToClustersFacility'),
    OnDemand = cms.bool(False),
    Regional = cms.bool(False),
    UsePixelModuleQualityDB = cms.bool(True),
    pixelClusterProducer = cms.string('hltHISiPixelClusters'),
    switchOffPixelsIfEmpty = cms.bool(True),
    inactiveStripDetectorLabels = cms.VInputTag("hltSiStripRawToDigi"),
    MaskBadAPVFibers = cms.bool(True),
    UseStripStripQualityDB = cms.bool(True),
    UsePixelROCQualityDB = cms.bool(True),
    DebugPixelROCQualityDB = cms.untracked.bool(False),
    UseStripAPVFiberQualityDB = cms.bool(True),
    stripClusterProducer = cms.string('hltHISiStripClustersNonRegional'),
    DebugStripAPVFiberQualityDB = cms.untracked.bool(False),
    DebugStripStripQualityDB = cms.untracked.bool(False),
    SiStripQualityLabel = cms.string(''),
    UseStripNoiseDB = cms.bool(False),
    badStripCuts = cms.PSet(
        TID = cms.PSet(
            maxConsecutiveBad = cms.uint32(2),
            maxBad = cms.uint32(4)
        ),
        TOB = cms.PSet(
            maxConsecutiveBad = cms.uint32(2),
            maxBad = cms.uint32(4)
        ),
        TEC = cms.PSet(
            maxConsecutiveBad = cms.uint32(2),
            maxBad = cms.uint32(4)
        ),
        TIB = cms.PSet(
            maxConsecutiveBad = cms.uint32(2),
            maxBad = cms.uint32(4)
        )
    ),
    DebugStripModuleQualityDB = cms.untracked.bool(False),
    ComponentName = cms.string('hltESPMeasurementTrackerForHI'),
    DebugPixelModuleQualityDB = cms.untracked.bool(False),
    HitMatcher = cms.string('StandardMatcher'),
    skipClusters = cms.InputTag(""),
    UseStripModuleQualityDB = cms.bool(True)
)


process.hltESPMeasurementTrackerReg = cms.ESProducer("MeasurementTrackerESProducer",
    StripCPE = cms.string('StripCPEfromTrackAngle'),
    inactivePixelDetectorLabels = cms.VInputTag(),
    UseStripCablingDB = cms.bool(False),
    PixelCPE = cms.string('hltESPPixelCPEGeneric'),
    stripLazyGetterProducer = cms.string('hltSiStripRawToClustersFacility'),
    OnDemand = cms.bool(True),
    Regional = cms.bool(True),
    UsePixelModuleQualityDB = cms.bool(True),
    pixelClusterProducer = cms.string('hltSiPixelClustersReg'),
    switchOffPixelsIfEmpty = cms.bool(True),
    inactiveStripDetectorLabels = cms.VInputTag("hltSiStripExcludedFEDListProducer"),
    MaskBadAPVFibers = cms.bool(True),
    UseStripStripQualityDB = cms.bool(True),
    UsePixelROCQualityDB = cms.bool(True),
    DebugPixelROCQualityDB = cms.untracked.bool(False),
    UseStripAPVFiberQualityDB = cms.bool(True),
    stripClusterProducer = cms.string('hltSiStripClustersReg'),
    DebugStripAPVFiberQualityDB = cms.untracked.bool(False),
    DebugStripStripQualityDB = cms.untracked.bool(False),
    SiStripQualityLabel = cms.string(''),
    UseStripNoiseDB = cms.bool(False),
    badStripCuts = cms.PSet(
        TID = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TOB = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TEC = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TIB = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        )
    ),
    DebugStripModuleQualityDB = cms.untracked.bool(False),
    ComponentName = cms.string('hltESPMeasurementTrackerReg'),
    DebugPixelModuleQualityDB = cms.untracked.bool(False),
    HitMatcher = cms.string('StandardMatcher'),
    skipClusters = cms.InputTag(""),
    UseStripModuleQualityDB = cms.bool(True)
)


process.hltESPMixedLayerPairs = cms.ESProducer("SeedingLayersESProducer",
    layerList = cms.vstring('BPix1+BPix2', 
        'BPix1+BPix3', 
        'BPix2+BPix3', 
        'BPix1+FPix1_pos', 
        'BPix1+FPix1_neg', 
        'BPix1+FPix2_pos', 
        'BPix1+FPix2_neg', 
        'BPix2+FPix1_pos', 
        'BPix2+FPix1_neg', 
        'BPix2+FPix2_pos', 
        'BPix2+FPix2_neg', 
        'FPix1_pos+FPix2_pos', 
        'FPix1_neg+FPix2_neg', 
        'FPix2_pos+TEC1_pos', 
        'FPix2_pos+TEC2_pos', 
        'TEC1_pos+TEC2_pos', 
        'TEC2_pos+TEC3_pos', 
        'FPix2_neg+TEC1_neg', 
        'FPix2_neg+TEC2_neg', 
        'TEC1_neg+TEC2_neg', 
        'TEC2_neg+TEC3_neg'),
    TID = cms.PSet(

    ),
    ComponentName = cms.string('hltESPMixedLayerPairs'),
    TEC = cms.PSet(
        useRingSlector = cms.bool(True),
        TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
        minRing = cms.int32(1),
        maxRing = cms.int32(1)
    ),
    FPix = cms.PSet(
        hitErrorRZ = cms.double(0.0036),
        hitErrorRPhi = cms.double(0.0051),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        HitProducer = cms.string('hltSiPixelRecHits'),
        useErrorsFromParam = cms.bool(True)
    ),
    TOB = cms.PSet(

    ),
    BPix = cms.PSet(
        hitErrorRZ = cms.double(0.006),
        hitErrorRPhi = cms.double(0.0027),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        HitProducer = cms.string('hltSiPixelRecHits'),
        useErrorsFromParam = cms.bool(True)
    ),
    TIB = cms.PSet(

    )
)


process.hltESPMuTrackJpsiEffTrajectoryBuilder = cms.ESProducer("CkfTrajectoryBuilderESProducer",
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    trajectoryFilterName = cms.string('hltESPMuTrackJpsiEffTrajectoryFilter'),
    maxCand = cms.int32(1),
    ComponentName = cms.string('hltESPMuTrackJpsiEffTrajectoryBuilder'),
    intermediateCleaning = cms.bool(True),
    MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
    estimator = cms.string('hltESPChi2MeasurementEstimator'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    updator = cms.string('hltESPKFUpdator'),
    alwaysUseInvalidHits = cms.bool(False),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    lostHitPenalty = cms.double(30.0)
)


process.hltESPMuTrackJpsiEffTrajectoryFilter = cms.ESProducer("TrajectoryFilterESProducer",
    filterPset = cms.PSet(
        chargeSignificance = cms.double(-1.0),
        minPt = cms.double(1.0),
        minHitsMinPt = cms.int32(3),
        ComponentType = cms.string('CkfBaseTrajectoryFilter'),
        maxLostHits = cms.int32(1),
        maxNumberOfHits = cms.int32(9),
        maxConsecLostHits = cms.int32(1),
        nSigmaMinPt = cms.double(5.0),
        minimumNumberOfHits = cms.int32(5)
    ),
    ComponentName = cms.string('hltESPMuTrackJpsiEffTrajectoryFilter')
)


process.hltESPMuTrackJpsiTrajectoryBuilder = cms.ESProducer("CkfTrajectoryBuilderESProducer",
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    trajectoryFilterName = cms.string('hltESPMuTrackJpsiTrajectoryFilter'),
    maxCand = cms.int32(1),
    ComponentName = cms.string('hltESPMuTrackJpsiTrajectoryBuilder'),
    intermediateCleaning = cms.bool(True),
    MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
    estimator = cms.string('hltESPChi2MeasurementEstimator'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    updator = cms.string('hltESPKFUpdator'),
    alwaysUseInvalidHits = cms.bool(False),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    lostHitPenalty = cms.double(30.0)
)


process.hltESPMuTrackJpsiTrajectoryFilter = cms.ESProducer("TrajectoryFilterESProducer",
    filterPset = cms.PSet(
        chargeSignificance = cms.double(-1.0),
        minPt = cms.double(1.0),
        minHitsMinPt = cms.int32(3),
        ComponentType = cms.string('CkfBaseTrajectoryFilter'),
        maxLostHits = cms.int32(1),
        maxNumberOfHits = cms.int32(8),
        maxConsecLostHits = cms.int32(1),
        nSigmaMinPt = cms.double(5.0),
        minimumNumberOfHits = cms.int32(5)
    ),
    ComponentName = cms.string('hltESPMuTrackJpsiTrajectoryFilter')
)


process.hltESPMuonCkfTrajectoryBuilder = cms.ESProducer("MuonCkfTrajectoryBuilderESProducer",
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    trajectoryFilterName = cms.string('hltESPMuonCkfTrajectoryFilter'),
    maxCand = cms.int32(5),
    ComponentName = cms.string('hltESPMuonCkfTrajectoryBuilder'),
    intermediateCleaning = cms.bool(False),
    useSeedLayer = cms.bool(False),
    deltaEta = cms.double(0.1),
    MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
    estimator = cms.string('hltESPChi2MeasurementEstimator'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    propagatorProximity = cms.string('SteppingHelixPropagatorAny'),
    updator = cms.string('hltESPKFUpdator'),
    alwaysUseInvalidHits = cms.bool(True),
    rescaleErrorIfFail = cms.double(1.0),
    deltaPhi = cms.double(0.1),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    lostHitPenalty = cms.double(30.0)
)


process.hltESPMuonCkfTrajectoryBuilderSeedHit = cms.ESProducer("MuonCkfTrajectoryBuilderESProducer",
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    trajectoryFilterName = cms.string('hltESPMuonCkfTrajectoryFilter'),
    maxCand = cms.int32(5),
    ComponentName = cms.string('hltESPMuonCkfTrajectoryBuilderSeedHit'),
    intermediateCleaning = cms.bool(False),
    useSeedLayer = cms.bool(True),
    deltaEta = cms.double(0.1),
    MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
    estimator = cms.string('hltESPChi2MeasurementEstimator'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    propagatorProximity = cms.string('SteppingHelixPropagatorAny'),
    updator = cms.string('hltESPKFUpdator'),
    alwaysUseInvalidHits = cms.bool(True),
    rescaleErrorIfFail = cms.double(1.0),
    deltaPhi = cms.double(0.1),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    lostHitPenalty = cms.double(30.0)
)


process.hltESPMuonCkfTrajectoryFilter = cms.ESProducer("TrajectoryFilterESProducer",
    filterPset = cms.PSet(
        minimumNumberOfHits = cms.int32(5),
        minPt = cms.double(0.9),
        minHitsMinPt = cms.int32(3),
        ComponentType = cms.string('CkfBaseTrajectoryFilter'),
        maxLostHits = cms.int32(1),
        maxNumberOfHits = cms.int32(-1),
        maxConsecLostHits = cms.int32(1),
        nSigmaMinPt = cms.double(5.0),
        chargeSignificance = cms.double(-1.0)
    ),
    ComponentName = cms.string('hltESPMuonCkfTrajectoryFilter')
)


process.hltESPMuonDetLayerGeometryESProducer = cms.ESProducer("MuonDetLayerGeometryESProducer")


process.hltESPMuonTransientTrackingRecHitBuilder = cms.ESProducer("MuonTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('hltESPMuonTransientTrackingRecHitBuilder')
)


process.hltESPPixelCPEGeneric = cms.ESProducer("PixelCPEGenericESProducer",
    eff_charge_cut_lowY = cms.double(0.0),
    EdgeClusterErrorY = cms.double(85.0),
    LoadTemplatesFromDB = cms.bool(True),
    eff_charge_cut_lowX = cms.double(0.0),
    eff_charge_cut_highX = cms.double(1.0),
    EdgeClusterErrorX = cms.double(50.0),
    size_cutY = cms.double(3.0),
    size_cutX = cms.double(3.0),
    eff_charge_cut_highY = cms.double(1.0),
    inflate_all_errors_no_trk_angle = cms.bool(False),
    IrradiationBiasCorrection = cms.bool(False),
    TanLorentzAnglePerTesla = cms.double(0.106),
    inflate_errors = cms.bool(False),
    Alpha2Order = cms.bool(True),
    TruncatePixelCharge = cms.bool(True),
    ClusterProbComputationFlag = cms.int32(0),
    UseErrorsFromTemplates = cms.bool(True),
    ComponentName = cms.string('hltESPPixelCPEGeneric'),
    DoCosmics = cms.bool(False),
    PixelErrorParametrization = cms.string('NOTcmsim')
)


process.hltESPPixelCPETemplateReco = cms.ESProducer("PixelCPETemplateRecoESProducer",
    DoCosmics = cms.bool(False),
    LoadTemplatesFromDB = cms.bool(True),
    ComponentName = cms.string('hltESPPixelCPETemplateReco'),
    Alpha2Order = cms.bool(True),
    ClusterProbComputationFlag = cms.int32(0),
    speed = cms.int32(-2),
    UseClusterSplitter = cms.bool(False)
)


process.hltESPPixelLayerPairs = cms.ESProducer("SeedingLayersESProducer",
    layerList = cms.vstring('BPix1+BPix2', 
        'BPix1+BPix3', 
        'BPix2+BPix3', 
        'BPix1+FPix1_pos', 
        'BPix1+FPix1_neg', 
        'BPix1+FPix2_pos', 
        'BPix1+FPix2_neg', 
        'BPix2+FPix1_pos', 
        'BPix2+FPix1_neg', 
        'BPix2+FPix2_pos', 
        'BPix2+FPix2_neg', 
        'FPix1_pos+FPix2_pos', 
        'FPix1_neg+FPix2_neg'),
    TID = cms.PSet(

    ),
    ComponentName = cms.string('hltESPPixelLayerPairs'),
    TEC = cms.PSet(

    ),
    FPix = cms.PSet(
        hitErrorRZ = cms.double(0.0036),
        hitErrorRPhi = cms.double(0.0051),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        HitProducer = cms.string('hltSiPixelRecHits'),
        useErrorsFromParam = cms.bool(True)
    ),
    TOB = cms.PSet(

    ),
    BPix = cms.PSet(
        hitErrorRZ = cms.double(0.006),
        hitErrorRPhi = cms.double(0.0027),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        HitProducer = cms.string('hltSiPixelRecHits'),
        useErrorsFromParam = cms.bool(True)
    ),
    TIB = cms.PSet(

    )
)


process.hltESPPixelLayerTriplets = cms.ESProducer("SeedingLayersESProducer",
    layerList = cms.vstring('BPix1+BPix2+BPix3', 
        'BPix1+BPix2+FPix1_pos', 
        'BPix1+BPix2+FPix1_neg', 
        'BPix1+FPix1_pos+FPix2_pos', 
        'BPix1+FPix1_neg+FPix2_neg'),
    TID = cms.PSet(

    ),
    ComponentName = cms.string('hltESPPixelLayerTriplets'),
    TEC = cms.PSet(

    ),
    FPix = cms.PSet(
        hitErrorRZ = cms.double(0.0036),
        hitErrorRPhi = cms.double(0.0051),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        HitProducer = cms.string('hltSiPixelRecHits'),
        useErrorsFromParam = cms.bool(True)
    ),
    TOB = cms.PSet(

    ),
    BPix = cms.PSet(
        hitErrorRZ = cms.double(0.006),
        hitErrorRPhi = cms.double(0.0027),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        HitProducer = cms.string('hltSiPixelRecHits'),
        useErrorsFromParam = cms.bool(True)
    ),
    TIB = cms.PSet(

    )
)


process.hltESPPixelLayerTripletsHITHB = cms.ESProducer("SeedingLayersESProducer",
    layerList = cms.vstring('BPix1+BPix2+BPix3'),
    TID = cms.PSet(

    ),
    ComponentName = cms.string('hltESPPixelLayerTripletsHITHB'),
    TEC = cms.PSet(

    ),
    FPix = cms.PSet(
        hitErrorRZ = cms.double(0.0036),
        hitErrorRPhi = cms.double(0.0051),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        HitProducer = cms.string('hltSiPixelRecHits'),
        useErrorsFromParam = cms.bool(True)
    ),
    TOB = cms.PSet(

    ),
    BPix = cms.PSet(
        hitErrorRZ = cms.double(0.006),
        hitErrorRPhi = cms.double(0.0027),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        HitProducer = cms.string('hltSiPixelRecHits'),
        useErrorsFromParam = cms.bool(True)
    ),
    TIB = cms.PSet(

    )
)


process.hltESPPixelLayerTripletsHITHE = cms.ESProducer("SeedingLayersESProducer",
    layerList = cms.vstring('BPix1+BPix2+FPix1_pos', 
        'BPix1+BPix2+FPix1_neg', 
        'BPix1+FPix1_pos+FPix2_pos', 
        'BPix1+FPix1_neg+FPix2_neg'),
    TID = cms.PSet(

    ),
    ComponentName = cms.string('hltESPPixelLayerTripletsHITHE'),
    TEC = cms.PSet(

    ),
    FPix = cms.PSet(
        hitErrorRZ = cms.double(0.0036),
        hitErrorRPhi = cms.double(0.0051),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        HitProducer = cms.string('hltSiPixelRecHits'),
        useErrorsFromParam = cms.bool(True)
    ),
    TOB = cms.PSet(

    ),
    BPix = cms.PSet(
        hitErrorRZ = cms.double(0.006),
        hitErrorRPhi = cms.double(0.0027),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        HitProducer = cms.string('hltSiPixelRecHits'),
        useErrorsFromParam = cms.bool(True)
    ),
    TIB = cms.PSet(

    )
)


process.hltESPPixelLayerTripletsReg = cms.ESProducer("SeedingLayersESProducer",
    layerList = cms.vstring('BPix1+BPix2+BPix3', 
        'BPix1+BPix2+FPix1_pos', 
        'BPix1+BPix2+FPix1_neg', 
        'BPix1+FPix1_pos+FPix2_pos', 
        'BPix1+FPix1_neg+FPix2_neg'),
    TID = cms.PSet(

    ),
    ComponentName = cms.string('hltESPPixelLayerTripletsReg'),
    TEC = cms.PSet(

    ),
    FPix = cms.PSet(
        useErrorsFromParam = cms.bool(True),
        hitErrorRPhi = cms.double(0.0051),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        HitProducer = cms.string('hltSiPixelRecHitsReg'),
        hitErrorRZ = cms.double(0.0036)
    ),
    TOB = cms.PSet(

    ),
    BPix = cms.PSet(
        useErrorsFromParam = cms.bool(True),
        hitErrorRPhi = cms.double(0.0027),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        HitProducer = cms.string('hltSiPixelRecHitsReg'),
        hitErrorRZ = cms.double(0.006)
    ),
    TIB = cms.PSet(

    )
)


process.hltESPPromptTrackCountingESProducer = cms.ESProducer("PromptTrackCountingESProducer",
    maxImpactParameterSig = cms.double(999999.0),
    deltaR = cms.double(-1.0),
    maximumDistanceToJetAxis = cms.double(999999.0),
    impactParameterType = cms.int32(0),
    trackQualityClass = cms.string('any'),
    deltaRmin = cms.double(0.0),
    maxImpactParameter = cms.double(0.03),
    maximumDecayLength = cms.double(999999.0),
    nthTrack = cms.int32(-1)
)


process.hltESPRKTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    RecoGeometry = cms.string('hltESPGlobalDetLayerGeometry'),
    ComponentName = cms.string('hltESPRKFitter'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator'),
    Updator = cms.string('hltESPKFUpdator'),
    Propagator = cms.string('hltESPRungeKuttaTrackerPropagator'),
    minHits = cms.int32(3)
)


process.hltESPRKTrajectorySmoother = cms.ESProducer("KFTrajectorySmootherESProducer",
    errorRescaling = cms.double(100.0),
    minHits = cms.int32(3),
    ComponentName = cms.string('hltESPRKSmoother'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator'),
    Updator = cms.string('hltESPKFUpdator'),
    Propagator = cms.string('hltESPRungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('hltESPGlobalDetLayerGeometry')
)


process.hltESPRungeKuttaTrackerPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    PropagationDirection = cms.string('alongMomentum'),
    ComponentName = cms.string('hltESPRungeKuttaTrackerPropagator'),
    Mass = cms.double(0.105),
    ptMin = cms.double(-1.0),
    MaxDPhi = cms.double(1.6),
    useRungeKutta = cms.bool(True)
)


process.hltESPSiStripRegionConnectivity = cms.ESProducer("SiStripRegionConnectivity",
    EtaMax = cms.untracked.double(2.5),
    PhiDivisions = cms.untracked.uint32(20),
    EtaDivisions = cms.untracked.uint32(20)
)


process.hltESPSmartPropagator = cms.ESProducer("SmartPropagatorESProducer",
    ComponentName = cms.string('hltESPSmartPropagator'),
    TrackerPropagator = cms.string('PropagatorWithMaterial'),
    MuonPropagator = cms.string('hltESPSteppingHelixPropagatorAlong'),
    PropagationDirection = cms.string('alongMomentum'),
    Epsilon = cms.double(5.0)
)


process.hltESPSmartPropagatorAny = cms.ESProducer("SmartPropagatorESProducer",
    ComponentName = cms.string('hltESPSmartPropagatorAny'),
    TrackerPropagator = cms.string('PropagatorWithMaterial'),
    MuonPropagator = cms.string('SteppingHelixPropagatorAny'),
    PropagationDirection = cms.string('alongMomentum'),
    Epsilon = cms.double(5.0)
)


process.hltESPSmartPropagatorAnyOpposite = cms.ESProducer("SmartPropagatorESProducer",
    ComponentName = cms.string('hltESPSmartPropagatorAnyOpposite'),
    TrackerPropagator = cms.string('PropagatorWithMaterialOpposite'),
    MuonPropagator = cms.string('SteppingHelixPropagatorAny'),
    PropagationDirection = cms.string('oppositeToMomentum'),
    Epsilon = cms.double(5.0)
)


process.hltESPSmartPropagatorOpposite = cms.ESProducer("SmartPropagatorESProducer",
    ComponentName = cms.string('hltESPSmartPropagatorOpposite'),
    TrackerPropagator = cms.string('PropagatorWithMaterialOpposite'),
    MuonPropagator = cms.string('hltESPSteppingHelixPropagatorOpposite'),
    PropagationDirection = cms.string('oppositeToMomentum'),
    Epsilon = cms.double(5.0)
)


process.hltESPSoftLeptonByDistance = cms.ESProducer("LeptonTaggerByDistanceESProducer",
    distance = cms.double(0.5)
)


process.hltESPSoftLeptonByPt = cms.ESProducer("LeptonTaggerByPtESProducer",
    ipSign = cms.string('any')
)


process.hltESPSteppingHelixPropagatorAlong = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ComponentName = cms.string('hltESPSteppingHelixPropagatorAlong'),
    endcapShiftInZNeg = cms.double(0.0),
    PropagationDirection = cms.string('alongMomentum'),
    useTuningForL2Speed = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    NoErrorPropagation = cms.bool(False),
    SetVBFPointer = cms.bool(False),
    AssumeNoMaterial = cms.bool(False),
    endcapShiftInZPos = cms.double(0.0),
    useInTeslaFromMagField = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    useEndcapShiftsInZ = cms.bool(False),
    sendLogWarning = cms.bool(False),
    useMatVolumes = cms.bool(True),
    debug = cms.bool(False),
    ApplyRadX0Correction = cms.bool(True),
    useMagVolumes = cms.bool(True),
    returnTangentPlane = cms.bool(True)
)


process.hltESPSteppingHelixPropagatorOpposite = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ComponentName = cms.string('hltESPSteppingHelixPropagatorOpposite'),
    endcapShiftInZNeg = cms.double(0.0),
    PropagationDirection = cms.string('oppositeToMomentum'),
    useTuningForL2Speed = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    NoErrorPropagation = cms.bool(False),
    SetVBFPointer = cms.bool(False),
    AssumeNoMaterial = cms.bool(False),
    endcapShiftInZPos = cms.double(0.0),
    useInTeslaFromMagField = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    useEndcapShiftsInZ = cms.bool(False),
    sendLogWarning = cms.bool(False),
    useMatVolumes = cms.bool(True),
    debug = cms.bool(False),
    ApplyRadX0Correction = cms.bool(True),
    useMagVolumes = cms.bool(True),
    returnTangentPlane = cms.bool(True)
)


process.hltESPStraightLinePropagator = cms.ESProducer("StraightLinePropagatorESProducer",
    ComponentName = cms.string('hltESPStraightLinePropagator'),
    PropagationDirection = cms.string('alongMomentum')
)


process.hltESPTTRHBWithTrackAngle = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    StripCPE = cms.string('StripCPEfromTrackAngle'),
    ComponentName = cms.string('hltESPTTRHBWithTrackAngle'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    PixelCPE = cms.string('hltESPPixelCPEGeneric'),
    Matcher = cms.string('StandardMatcher')
)


process.hltESPTTRHBuilderAngleAndTemplate = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    StripCPE = cms.string('StripCPEfromTrackAngle'),
    ComponentName = cms.string('hltESPTTRHBuilderAngleAndTemplate'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    PixelCPE = cms.string('hltESPPixelCPETemplateReco'),
    Matcher = cms.string('StandardMatcher')
)


process.hltESPTTRHBuilderPixelOnly = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    StripCPE = cms.string('Fake'),
    ComponentName = cms.string('hltESPTTRHBuilderPixelOnly'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    PixelCPE = cms.string('hltESPPixelCPEGeneric'),
    Matcher = cms.string('StandardMatcher')
)


process.hltESPTTRHBuilderWithoutAngle4PixelTriplets = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    StripCPE = cms.string('Fake'),
    ComponentName = cms.string('hltESPTTRHBuilderWithoutAngle4PixelTriplets'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    PixelCPE = cms.string('hltESPPixelCPEGeneric'),
    Matcher = cms.string('StandardMatcher')
)


process.hltESPTrackCounting3D1st = cms.ESProducer("TrackCountingESProducer",
    deltaR = cms.double(-1.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    impactParameterType = cms.int32(0),
    trackQualityClass = cms.string('any'),
    maximumDecayLength = cms.double(5.0),
    nthTrack = cms.int32(1)
)


process.hltESPTrackCounting3D2nd = cms.ESProducer("TrackCountingESProducer",
    deltaR = cms.double(-1.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    impactParameterType = cms.int32(0),
    trackQualityClass = cms.string('any'),
    maximumDecayLength = cms.double(5.0),
    nthTrack = cms.int32(2)
)


process.hltESPTrackerRecoGeometryESProducer = cms.ESProducer("TrackerRecoGeometryESProducer",
    trackerGeometryLabel = cms.untracked.string(''),
    appendToDataLabel = cms.string('')
)


process.hltESPTrajectoryBuilderForElectrons = cms.ESProducer("CkfTrajectoryBuilderESProducer",
    propagatorAlong = cms.string('hltESPFwdElectronPropagator'),
    trajectoryFilterName = cms.string('hltESPTrajectoryFilterForElectrons'),
    maxCand = cms.int32(5),
    ComponentName = cms.string('hltESPTrajectoryBuilderForElectrons'),
    intermediateCleaning = cms.bool(False),
    MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
    estimator = cms.string('hltESPElectronChi2'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    updator = cms.string('hltESPKFUpdator'),
    alwaysUseInvalidHits = cms.bool(True),
    propagatorOpposite = cms.string('hltESPBwdElectronPropagator'),
    lostHitPenalty = cms.double(90.0)
)


process.hltESPTrajectoryBuilderIT = cms.ESProducer("CkfTrajectoryBuilderESProducer",
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    trajectoryFilterName = cms.string('hltESPTrajectoryFilterIT'),
    maxCand = cms.int32(2),
    ComponentName = cms.string('hltESPTrajectoryBuilderIT'),
    intermediateCleaning = cms.bool(True),
    MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
    estimator = cms.string('hltESPChi2MeasurementEstimator9'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    updator = cms.string('hltESPKFUpdator'),
    alwaysUseInvalidHits = cms.bool(False),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    lostHitPenalty = cms.double(30.0)
)


process.hltESPTrajectoryBuilderITReg = cms.ESProducer("CkfTrajectoryBuilderESProducer",
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    trajectoryFilterName = cms.string('hltESPTrajectoryFilterIT'),
    maxCand = cms.int32(2),
    ComponentName = cms.string('hltESPTrajectoryBuilderITReg'),
    intermediateCleaning = cms.bool(True),
    MeasurementTrackerName = cms.string('hltESPMeasurementTrackerReg'),
    estimator = cms.string('hltESPChi2MeasurementEstimator9'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    updator = cms.string('hltESPKFUpdator'),
    alwaysUseInvalidHits = cms.bool(False),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    lostHitPenalty = cms.double(30.0)
)


process.hltESPTrajectoryBuilderL3 = cms.ESProducer("CkfTrajectoryBuilderESProducer",
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    trajectoryFilterName = cms.string('hltESPTrajectoryFilterL3'),
    maxCand = cms.int32(5),
    ComponentName = cms.string('hltESPTrajectoryBuilderL3'),
    intermediateCleaning = cms.bool(True),
    MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
    estimator = cms.string('hltESPChi2MeasurementEstimator'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    updator = cms.string('hltESPKFUpdator'),
    alwaysUseInvalidHits = cms.bool(False),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    lostHitPenalty = cms.double(30.0)
)


process.hltESPTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPTrajectoryCleanerBySharedHits'),
    fractionShared = cms.double(0.5),
    ValidHitBonus = cms.double(100.0),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(0.0),
    allowSharedFirstHit = cms.bool(False)
)


process.hltESPTrajectoryCleanerBySharedSeeds = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPTrajectoryCleanerBySharedSeeds'),
    fractionShared = cms.double(0.5),
    ValidHitBonus = cms.double(100.0),
    ComponentType = cms.string('TrajectoryCleanerBySharedSeeds'),
    MissingHitPenalty = cms.double(0.0),
    allowSharedFirstHit = cms.bool(True)
)


process.hltESPTrajectoryFilterForElectrons = cms.ESProducer("TrajectoryFilterESProducer",
    filterPset = cms.PSet(
        chargeSignificance = cms.double(-1.0),
        minPt = cms.double(2.0),
        minHitsMinPt = cms.int32(-1),
        ComponentType = cms.string('CkfBaseTrajectoryFilter'),
        maxLostHits = cms.int32(1),
        maxNumberOfHits = cms.int32(-1),
        maxConsecLostHits = cms.int32(1),
        nSigmaMinPt = cms.double(5.0),
        minimumNumberOfHits = cms.int32(5)
    ),
    ComponentName = cms.string('hltESPTrajectoryFilterForElectrons')
)


process.hltESPTrajectoryFilterIT = cms.ESProducer("TrajectoryFilterESProducer",
    filterPset = cms.PSet(
        chargeSignificance = cms.double(-1.0),
        minPt = cms.double(0.3),
        minHitsMinPt = cms.int32(3),
        ComponentType = cms.string('CkfBaseTrajectoryFilter'),
        maxLostHits = cms.int32(1),
        maxNumberOfHits = cms.int32(100),
        maxConsecLostHits = cms.int32(1),
        nSigmaMinPt = cms.double(5.0),
        minimumNumberOfHits = cms.int32(3)
    ),
    ComponentName = cms.string('hltESPTrajectoryFilterIT')
)


process.hltESPTrajectoryFilterL3 = cms.ESProducer("TrajectoryFilterESProducer",
    filterPset = cms.PSet(
        chargeSignificance = cms.double(-1.0),
        minPt = cms.double(0.5),
        minHitsMinPt = cms.int32(3),
        ComponentType = cms.string('CkfBaseTrajectoryFilter'),
        maxLostHits = cms.int32(1),
        maxNumberOfHits = cms.int32(1000000000),
        maxConsecLostHits = cms.int32(1),
        nSigmaMinPt = cms.double(5.0),
        minimumNumberOfHits = cms.int32(5)
    ),
    ComponentName = cms.string('hltESPTrajectoryFilterL3')
)


process.hltESPTrajectoryFitterRK = cms.ESProducer("KFTrajectoryFitterESProducer",
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    ComponentName = cms.string('hltESPTrajectoryFitterRK'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator'),
    Updator = cms.string('hltESPKFUpdator'),
    Propagator = cms.string('hltESPRungeKuttaTrackerPropagator'),
    minHits = cms.int32(3)
)


process.hltESPTrajectorySmootherRK = cms.ESProducer("KFTrajectorySmootherESProducer",
    errorRescaling = cms.double(100.0),
    minHits = cms.int32(3),
    ComponentName = cms.string('hltESPTrajectorySmootherRK'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator'),
    Updator = cms.string('hltESPKFUpdator'),
    Propagator = cms.string('hltESPRungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry')
)


process.hltESPbJetRegionalTrajectoryBuilder = cms.ESProducer("CkfTrajectoryBuilderESProducer",
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    trajectoryFilterName = cms.string('hltESPbJetRegionalTrajectoryFilter'),
    maxCand = cms.int32(1),
    ComponentName = cms.string('hltESPbJetRegionalTrajectoryBuilder'),
    intermediateCleaning = cms.bool(True),
    MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
    estimator = cms.string('hltESPChi2MeasurementEstimator'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    updator = cms.string('hltESPKFUpdator'),
    alwaysUseInvalidHits = cms.bool(False),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    lostHitPenalty = cms.double(30.0)
)


process.hltESPbJetRegionalTrajectoryFilter = cms.ESProducer("TrajectoryFilterESProducer",
    filterPset = cms.PSet(
        chargeSignificance = cms.double(-1.0),
        minPt = cms.double(1.0),
        minHitsMinPt = cms.int32(3),
        ComponentType = cms.string('CkfBaseTrajectoryFilter'),
        maxLostHits = cms.int32(1),
        maxNumberOfHits = cms.int32(8),
        maxConsecLostHits = cms.int32(1),
        nSigmaMinPt = cms.double(5.0),
        minimumNumberOfHits = cms.int32(5)
    ),
    ComponentName = cms.string('hltESPbJetRegionalTrajectoryFilter')
)


process.hltHIAllESPCkf3HitTrajectoryBuilder = cms.ESProducer("CkfTrajectoryBuilderESProducer",
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    trajectoryFilterName = cms.string('hltESPCkf3HitTrajectoryFilter'),
    maxCand = cms.int32(5),
    ComponentName = cms.string('hltHIAllESPCkf3HitTrajectoryBuilder'),
    intermediateCleaning = cms.bool(True),
    MeasurementTrackerName = cms.string('hltHIAllESPMeasurementTracker'),
    estimator = cms.string('hltESPChi2MeasurementEstimator'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    updator = cms.string('hltESPKFUpdator'),
    alwaysUseInvalidHits = cms.bool(True),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    lostHitPenalty = cms.double(30.0)
)


process.hltHIAllESPCkfTrajectoryBuilder = cms.ESProducer("CkfTrajectoryBuilderESProducer",
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    trajectoryFilterName = cms.string('hltESPCkfTrajectoryFilter'),
    maxCand = cms.int32(5),
    ComponentName = cms.string('hltHIAllESPCkfTrajectoryBuilder'),
    intermediateCleaning = cms.bool(True),
    MeasurementTrackerName = cms.string('hltHIAllESPMeasurementTracker'),
    estimator = cms.string('hltESPChi2MeasurementEstimator'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    updator = cms.string('hltESPKFUpdator'),
    alwaysUseInvalidHits = cms.bool(True),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    lostHitPenalty = cms.double(30.0)
)


process.hltHIAllESPMeasurementTracker = cms.ESProducer("MeasurementTrackerESProducer",
    StripCPE = cms.string('StripCPEfromTrackAngle'),
    inactivePixelDetectorLabels = cms.VInputTag(),
    UseStripCablingDB = cms.bool(False),
    PixelCPE = cms.string('hltESPPixelCPEGeneric'),
    stripLazyGetterProducer = cms.string('hltHISiStripRawToClustersFacility'),
    OnDemand = cms.bool(True),
    Regional = cms.bool(True),
    UsePixelModuleQualityDB = cms.bool(True),
    pixelClusterProducer = cms.string('hltHISiPixelClusters'),
    switchOffPixelsIfEmpty = cms.bool(True),
    inactiveStripDetectorLabels = cms.VInputTag("hltSiStripExcludedFEDListProducer"),
    MaskBadAPVFibers = cms.bool(True),
    UseStripStripQualityDB = cms.bool(True),
    UsePixelROCQualityDB = cms.bool(True),
    DebugPixelROCQualityDB = cms.untracked.bool(False),
    UseStripAPVFiberQualityDB = cms.bool(True),
    stripClusterProducer = cms.string('hltHISiStripClusters'),
    DebugStripAPVFiberQualityDB = cms.untracked.bool(False),
    DebugStripStripQualityDB = cms.untracked.bool(False),
    SiStripQualityLabel = cms.string(''),
    UseStripNoiseDB = cms.bool(False),
    badStripCuts = cms.PSet(
        TOB = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TID = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TEC = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TIB = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        )
    ),
    DebugStripModuleQualityDB = cms.untracked.bool(False),
    ComponentName = cms.string('hltHIAllESPMeasurementTracker'),
    DebugPixelModuleQualityDB = cms.untracked.bool(False),
    HitMatcher = cms.string('StandardMatcher'),
    skipClusters = cms.InputTag(""),
    UseStripModuleQualityDB = cms.bool(True)
)


process.hltHIAllESPMuonCkfTrajectoryBuilder = cms.ESProducer("MuonCkfTrajectoryBuilderESProducer",
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    trajectoryFilterName = cms.string('hltESPMuonCkfTrajectoryFilter'),
    maxCand = cms.int32(5),
    ComponentName = cms.string('hltHIAllESPMuonCkfTrajectoryBuilder'),
    intermediateCleaning = cms.bool(False),
    useSeedLayer = cms.bool(False),
    deltaEta = cms.double(0.1),
    MeasurementTrackerName = cms.string('hltHIAllESPMeasurementTracker'),
    estimator = cms.string('hltESPChi2MeasurementEstimator'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    propagatorProximity = cms.string('SteppingHelixPropagatorAny'),
    updator = cms.string('hltESPKFUpdator'),
    alwaysUseInvalidHits = cms.bool(True),
    rescaleErrorIfFail = cms.double(1.0),
    deltaPhi = cms.double(0.1),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    lostHitPenalty = cms.double(30.0)
)


process.hltHIAllESPTrajectoryBuilderIT = cms.ESProducer("CkfTrajectoryBuilderESProducer",
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    trajectoryFilterName = cms.string('hltESPTrajectoryFilterIT'),
    maxCand = cms.int32(5),
    ComponentName = cms.string('hltHIAllESPTrajectoryBuilderIT'),
    intermediateCleaning = cms.bool(True),
    MeasurementTrackerName = cms.string('hltHIAllESPMeasurementTracker'),
    estimator = cms.string('hltESPChi2MeasurementEstimator'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    updator = cms.string('hltESPKFUpdator'),
    alwaysUseInvalidHits = cms.bool(False),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    lostHitPenalty = cms.double(30.0)
)


process.hltIter1ESPMeasurementTracker = cms.ESProducer("MeasurementTrackerESProducer",
    StripCPE = cms.string('StripCPEfromTrackAngle'),
    inactivePixelDetectorLabels = cms.VInputTag(),
    UseStripCablingDB = cms.bool(False),
    PixelCPE = cms.string('hltESPPixelCPEGeneric'),
    stripLazyGetterProducer = cms.string('hltSiStripRawToClustersFacility'),
    OnDemand = cms.bool(True),
    Regional = cms.bool(True),
    UsePixelModuleQualityDB = cms.bool(True),
    pixelClusterProducer = cms.string('hltSiPixelClusters'),
    switchOffPixelsIfEmpty = cms.bool(True),
    inactiveStripDetectorLabels = cms.VInputTag("hltSiStripExcludedFEDListProducer"),
    MaskBadAPVFibers = cms.bool(True),
    UseStripStripQualityDB = cms.bool(True),
    UsePixelROCQualityDB = cms.bool(True),
    DebugPixelROCQualityDB = cms.untracked.bool(False),
    UseStripAPVFiberQualityDB = cms.bool(True),
    stripClusterProducer = cms.string('hltIter1SiStripClusters'),
    DebugStripAPVFiberQualityDB = cms.untracked.bool(False),
    DebugStripStripQualityDB = cms.untracked.bool(False),
    SiStripQualityLabel = cms.string(''),
    UseStripNoiseDB = cms.bool(False),
    badStripCuts = cms.PSet(
        TID = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TOB = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TEC = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TIB = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        )
    ),
    DebugStripModuleQualityDB = cms.untracked.bool(False),
    ComponentName = cms.string('hltIter1ESPMeasurementTracker'),
    DebugPixelModuleQualityDB = cms.untracked.bool(False),
    HitMatcher = cms.string('StandardMatcher'),
    skipClusters = cms.InputTag("hltIter1ClustersRefRemoval"),
    UseStripModuleQualityDB = cms.bool(True)
)


process.hltIter1ESPMeasurementTrackerPA = cms.ESProducer("MeasurementTrackerESProducer",
    StripCPE = cms.string('StripCPEfromTrackAngle'),
    inactivePixelDetectorLabels = cms.VInputTag(),
    UseStripCablingDB = cms.bool(False),
    PixelCPE = cms.string('hltESPPixelCPEGeneric'),
    stripLazyGetterProducer = cms.string('hltSiStripRawToClustersFacility'),
    OnDemand = cms.bool(True),
    Regional = cms.bool(True),
    UsePixelModuleQualityDB = cms.bool(True),
    pixelClusterProducer = cms.string('hltSiPixelClusters'),
    switchOffPixelsIfEmpty = cms.bool(True),
    inactiveStripDetectorLabels = cms.VInputTag("hltSiStripExcludedFEDListProducer"),
    MaskBadAPVFibers = cms.bool(True),
    UseStripStripQualityDB = cms.bool(True),
    UsePixelROCQualityDB = cms.bool(True),
    DebugPixelROCQualityDB = cms.untracked.bool(False),
    UseStripAPVFiberQualityDB = cms.bool(True),
    stripClusterProducer = cms.string('hltPAFullTrackIter1SiStripClusters'),
    DebugStripAPVFiberQualityDB = cms.untracked.bool(False),
    DebugStripStripQualityDB = cms.untracked.bool(False),
    SiStripQualityLabel = cms.string(''),
    UseStripNoiseDB = cms.bool(False),
    badStripCuts = cms.PSet(
        TID = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TOB = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TEC = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TIB = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        )
    ),
    DebugStripModuleQualityDB = cms.untracked.bool(False),
    ComponentName = cms.string('hltIter1ESPMeasurementTrackerPA'),
    DebugPixelModuleQualityDB = cms.untracked.bool(False),
    HitMatcher = cms.string('StandardMatcher'),
    skipClusters = cms.InputTag("hltPAFullTrackIter1ClustersRefRemoval"),
    UseStripModuleQualityDB = cms.bool(True)
)


process.hltIter1ESPMeasurementTrackerReg = cms.ESProducer("MeasurementTrackerESProducer",
    StripCPE = cms.string('StripCPEfromTrackAngle'),
    inactivePixelDetectorLabels = cms.VInputTag(),
    UseStripCablingDB = cms.bool(False),
    PixelCPE = cms.string('hltESPPixelCPEGeneric'),
    stripLazyGetterProducer = cms.string('hltSiStripRawToClustersFacility'),
    OnDemand = cms.bool(True),
    Regional = cms.bool(True),
    UsePixelModuleQualityDB = cms.bool(True),
    pixelClusterProducer = cms.string('hltSiPixelClustersReg'),
    switchOffPixelsIfEmpty = cms.bool(True),
    inactiveStripDetectorLabels = cms.VInputTag("hltSiStripExcludedFEDListProducer"),
    MaskBadAPVFibers = cms.bool(True),
    UseStripStripQualityDB = cms.bool(True),
    UsePixelROCQualityDB = cms.bool(True),
    DebugPixelROCQualityDB = cms.untracked.bool(False),
    UseStripAPVFiberQualityDB = cms.bool(True),
    stripClusterProducer = cms.string('hltIter1SiStripClustersReg'),
    DebugStripAPVFiberQualityDB = cms.untracked.bool(False),
    DebugStripStripQualityDB = cms.untracked.bool(False),
    SiStripQualityLabel = cms.string(''),
    UseStripNoiseDB = cms.bool(False),
    badStripCuts = cms.PSet(
        TID = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TOB = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TEC = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TIB = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        )
    ),
    DebugStripModuleQualityDB = cms.untracked.bool(False),
    ComponentName = cms.string('hltIter1ESPMeasurementTrackerReg'),
    DebugPixelModuleQualityDB = cms.untracked.bool(False),
    HitMatcher = cms.string('StandardMatcher'),
    skipClusters = cms.InputTag("hltIter1ClustersRefRemovalReg"),
    UseStripModuleQualityDB = cms.bool(True)
)


process.hltIter1ESPPixelLayerTriplets = cms.ESProducer("SeedingLayersESProducer",
    layerList = cms.vstring('BPix1+BPix2+BPix3', 
        'BPix1+BPix2+FPix1_pos', 
        'BPix1+BPix2+FPix1_neg', 
        'BPix1+FPix1_pos+FPix2_pos', 
        'BPix1+FPix1_neg+FPix2_neg'),
    TID = cms.PSet(

    ),
    ComponentName = cms.string('hltIter1ESPPixelLayerTriplets'),
    TEC = cms.PSet(

    ),
    FPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        hitErrorRZ = cms.double(0.0036),
        useErrorsFromParam = cms.bool(True),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        skipClusters = cms.InputTag("hltIter1ClustersRefRemoval"),
        hitErrorRPhi = cms.double(0.0051)
    ),
    TOB = cms.PSet(

    ),
    BPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        hitErrorRZ = cms.double(0.006),
        useErrorsFromParam = cms.bool(True),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        skipClusters = cms.InputTag("hltIter1ClustersRefRemoval"),
        hitErrorRPhi = cms.double(0.0027)
    ),
    TIB = cms.PSet(

    )
)


process.hltIter1ESPPixelLayerTripletsPA = cms.ESProducer("SeedingLayersESProducer",
    layerList = cms.vstring('BPix1+BPix2+BPix3', 
        'BPix1+BPix2+FPix1_pos', 
        'BPix1+BPix2+FPix1_neg', 
        'BPix1+FPix1_pos+FPix2_pos', 
        'BPix1+FPix1_neg+FPix2_neg'),
    TID = cms.PSet(

    ),
    ComponentName = cms.string('hltIter1ESPPixelLayerTripletsPA'),
    TEC = cms.PSet(

    ),
    FPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        hitErrorRZ = cms.double(0.0036),
        useErrorsFromParam = cms.bool(True),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        skipClusters = cms.InputTag("hltPAFullTrackIter1ClustersRefRemoval"),
        hitErrorRPhi = cms.double(0.0051)
    ),
    TOB = cms.PSet(

    ),
    BPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        hitErrorRZ = cms.double(0.006),
        useErrorsFromParam = cms.bool(True),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        skipClusters = cms.InputTag("hltPAFullTrackIter1ClustersRefRemoval"),
        hitErrorRPhi = cms.double(0.0027)
    ),
    TIB = cms.PSet(

    )
)


process.hltIter1ESPPixelLayerTripletsReg = cms.ESProducer("SeedingLayersESProducer",
    layerList = cms.vstring('BPix1+BPix2+BPix3', 
        'BPix1+BPix2+FPix1_pos', 
        'BPix1+BPix2+FPix1_neg', 
        'BPix1+FPix1_pos+FPix2_pos', 
        'BPix1+FPix1_neg+FPix2_neg'),
    TID = cms.PSet(

    ),
    ComponentName = cms.string('hltIter1ESPPixelLayerTripletsReg'),
    TEC = cms.PSet(

    ),
    FPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHitsReg'),
        hitErrorRZ = cms.double(0.0036),
        useErrorsFromParam = cms.bool(True),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        skipClusters = cms.InputTag("hltIter1ClustersRefRemovalReg"),
        hitErrorRPhi = cms.double(0.0051)
    ),
    TOB = cms.PSet(

    ),
    BPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHitsReg'),
        hitErrorRZ = cms.double(0.006),
        useErrorsFromParam = cms.bool(True),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        skipClusters = cms.InputTag("hltIter1ClustersRefRemovalReg"),
        hitErrorRPhi = cms.double(0.0027)
    ),
    TIB = cms.PSet(

    )
)


process.hltIter1ESPTrajectoryBuilderIT = cms.ESProducer("CkfTrajectoryBuilderESProducer",
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    trajectoryFilterName = cms.string('hltIter1ESPTrajectoryFilterIT'),
    maxCand = cms.int32(2),
    ComponentName = cms.string('hltIter1ESPTrajectoryBuilderIT'),
    intermediateCleaning = cms.bool(True),
    MeasurementTrackerName = cms.string('hltIter1ESPMeasurementTracker'),
    estimator = cms.string('hltESPChi2MeasurementEstimator16'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    updator = cms.string('hltESPKFUpdator'),
    alwaysUseInvalidHits = cms.bool(False),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    lostHitPenalty = cms.double(30.0)
)


process.hltIter1ESPTrajectoryBuilderITPA = cms.ESProducer("CkfTrajectoryBuilderESProducer",
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    trajectoryFilterName = cms.string('hltIter1ESPTrajectoryFilterIT'),
    maxCand = cms.int32(2),
    ComponentName = cms.string('hltIter1ESPTrajectoryBuilderITPA'),
    intermediateCleaning = cms.bool(True),
    MeasurementTrackerName = cms.string('hltIter1ESPMeasurementTrackerPA'),
    estimator = cms.string('hltESPChi2MeasurementEstimator16'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    updator = cms.string('hltESPKFUpdator'),
    alwaysUseInvalidHits = cms.bool(False),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    lostHitPenalty = cms.double(30.0)
)


process.hltIter1ESPTrajectoryBuilderITReg = cms.ESProducer("CkfTrajectoryBuilderESProducer",
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    trajectoryFilterName = cms.string('hltIter1ESPTrajectoryFilterIT'),
    maxCand = cms.int32(2),
    ComponentName = cms.string('hltIter1ESPTrajectoryBuilderITReg'),
    intermediateCleaning = cms.bool(True),
    MeasurementTrackerName = cms.string('hltIter1ESPMeasurementTrackerReg'),
    estimator = cms.string('hltESPChi2MeasurementEstimator16'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    updator = cms.string('hltESPKFUpdator'),
    alwaysUseInvalidHits = cms.bool(False),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    lostHitPenalty = cms.double(30.0)
)


process.hltIter1ESPTrajectoryFilterIT = cms.ESProducer("TrajectoryFilterESProducer",
    filterPset = cms.PSet(
        chargeSignificance = cms.double(-1.0),
        minPt = cms.double(0.2),
        minHitsMinPt = cms.int32(3),
        ComponentType = cms.string('CkfBaseTrajectoryFilter'),
        maxLostHits = cms.int32(1),
        maxNumberOfHits = cms.int32(100),
        maxConsecLostHits = cms.int32(1),
        nSigmaMinPt = cms.double(5.0),
        minimumNumberOfHits = cms.int32(3)
    ),
    ComponentName = cms.string('hltIter1ESPTrajectoryFilterIT')
)


process.hltIter1Tau3MuESPMeasurementTracker = cms.ESProducer("MeasurementTrackerESProducer",
    StripCPE = cms.string('StripCPEfromTrackAngle'),
    inactivePixelDetectorLabels = cms.VInputTag(),
    UseStripCablingDB = cms.bool(False),
    PixelCPE = cms.string('hltESPPixelCPEGeneric'),
    stripLazyGetterProducer = cms.string('hltSiStripRawToClustersFacility'),
    OnDemand = cms.bool(True),
    Regional = cms.bool(True),
    UsePixelModuleQualityDB = cms.bool(True),
    pixelClusterProducer = cms.string('hltSiPixelClusters'),
    switchOffPixelsIfEmpty = cms.bool(True),
    inactiveStripDetectorLabels = cms.VInputTag("hltSiStripExcludedFEDListProducer"),
    MaskBadAPVFibers = cms.bool(True),
    UseStripStripQualityDB = cms.bool(True),
    UsePixelROCQualityDB = cms.bool(True),
    DebugPixelROCQualityDB = cms.untracked.bool(False),
    UseStripAPVFiberQualityDB = cms.bool(True),
    stripClusterProducer = cms.string('hltIter1Tau3MuSiStripClusters'),
    DebugStripAPVFiberQualityDB = cms.untracked.bool(False),
    DebugStripStripQualityDB = cms.untracked.bool(False),
    SiStripQualityLabel = cms.string(''),
    UseStripNoiseDB = cms.bool(False),
    badStripCuts = cms.PSet(
        TOB = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TID = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TEC = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TIB = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        )
    ),
    DebugStripModuleQualityDB = cms.untracked.bool(False),
    ComponentName = cms.string('hltIter1Tau3MuESPMeasurementTracker'),
    DebugPixelModuleQualityDB = cms.untracked.bool(False),
    HitMatcher = cms.string('StandardMatcher'),
    skipClusters = cms.InputTag("hltIter1Tau3MuClustersRefRemoval"),
    UseStripModuleQualityDB = cms.bool(True)
)


process.hltIter1Tau3MuESPPixelLayerTriplets = cms.ESProducer("SeedingLayersESProducer",
    layerList = cms.vstring('BPix1+BPix2+BPix3', 
        'BPix1+BPix2+FPix1_pos', 
        'BPix1+BPix2+FPix1_neg', 
        'BPix1+FPix1_pos+FPix2_pos', 
        'BPix1+FPix1_neg+FPix2_neg'),
    TID = cms.PSet(

    ),
    ComponentName = cms.string('hltIter1Tau3MuESPPixelLayerTriplets'),
    TEC = cms.PSet(

    ),
    FPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        hitErrorRZ = cms.double(0.0036),
        useErrorsFromParam = cms.bool(True),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        skipClusters = cms.InputTag("hltIter1Tau3MuClustersRefRemoval"),
        hitErrorRPhi = cms.double(0.0051)
    ),
    TOB = cms.PSet(

    ),
    BPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        hitErrorRZ = cms.double(0.006),
        useErrorsFromParam = cms.bool(True),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        skipClusters = cms.InputTag("hltIter1Tau3MuClustersRefRemoval"),
        hitErrorRPhi = cms.double(0.0027)
    ),
    TIB = cms.PSet(

    )
)


process.hltIter1Tau3MuESPTrajectoryBuilderIT = cms.ESProducer("CkfTrajectoryBuilderESProducer",
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    trajectoryFilterName = cms.string('hltIter1ESPTrajectoryFilterIT'),
    maxCand = cms.int32(2),
    ComponentName = cms.string('hltIter1Tau3MuESPTrajectoryBuilderIT'),
    intermediateCleaning = cms.bool(True),
    MeasurementTrackerName = cms.string('hltIter1Tau3MuESPMeasurementTracker'),
    estimator = cms.string('hltESPChi2MeasurementEstimator16'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    updator = cms.string('hltESPKFUpdator'),
    alwaysUseInvalidHits = cms.bool(False),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    lostHitPenalty = cms.double(30.0)
)


process.hltIter2ESPMeasurementTracker = cms.ESProducer("MeasurementTrackerESProducer",
    StripCPE = cms.string('StripCPEfromTrackAngle'),
    inactivePixelDetectorLabels = cms.VInputTag(),
    UseStripCablingDB = cms.bool(False),
    PixelCPE = cms.string('hltESPPixelCPEGeneric'),
    stripLazyGetterProducer = cms.string('hltSiStripRawToClustersFacility'),
    OnDemand = cms.bool(True),
    Regional = cms.bool(True),
    UsePixelModuleQualityDB = cms.bool(True),
    pixelClusterProducer = cms.string('hltSiPixelClusters'),
    switchOffPixelsIfEmpty = cms.bool(True),
    inactiveStripDetectorLabels = cms.VInputTag("hltSiStripExcludedFEDListProducer"),
    MaskBadAPVFibers = cms.bool(True),
    UseStripStripQualityDB = cms.bool(True),
    UsePixelROCQualityDB = cms.bool(True),
    DebugPixelROCQualityDB = cms.untracked.bool(False),
    UseStripAPVFiberQualityDB = cms.bool(True),
    stripClusterProducer = cms.string('hltIter2SiStripClusters'),
    DebugStripAPVFiberQualityDB = cms.untracked.bool(False),
    DebugStripStripQualityDB = cms.untracked.bool(False),
    SiStripQualityLabel = cms.string(''),
    UseStripNoiseDB = cms.bool(False),
    badStripCuts = cms.PSet(
        TID = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TOB = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TEC = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TIB = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        )
    ),
    DebugStripModuleQualityDB = cms.untracked.bool(False),
    ComponentName = cms.string('hltIter2ESPMeasurementTracker'),
    DebugPixelModuleQualityDB = cms.untracked.bool(False),
    HitMatcher = cms.string('StandardMatcher'),
    skipClusters = cms.InputTag("hltIter2ClustersRefRemoval"),
    UseStripModuleQualityDB = cms.bool(True)
)


process.hltIter2ESPMeasurementTrackerPA = cms.ESProducer("MeasurementTrackerESProducer",
    StripCPE = cms.string('StripCPEfromTrackAngle'),
    inactivePixelDetectorLabels = cms.VInputTag(),
    UseStripCablingDB = cms.bool(False),
    PixelCPE = cms.string('hltESPPixelCPEGeneric'),
    stripLazyGetterProducer = cms.string('hltSiStripRawToClustersFacility'),
    OnDemand = cms.bool(True),
    Regional = cms.bool(True),
    UsePixelModuleQualityDB = cms.bool(True),
    pixelClusterProducer = cms.string('hltSiPixelClusters'),
    switchOffPixelsIfEmpty = cms.bool(True),
    inactiveStripDetectorLabels = cms.VInputTag("hltSiStripExcludedFEDListProducer"),
    MaskBadAPVFibers = cms.bool(True),
    UseStripStripQualityDB = cms.bool(True),
    UsePixelROCQualityDB = cms.bool(True),
    DebugPixelROCQualityDB = cms.untracked.bool(False),
    UseStripAPVFiberQualityDB = cms.bool(True),
    stripClusterProducer = cms.string('hltPAFullTrackIter2SiStripClusters'),
    DebugStripAPVFiberQualityDB = cms.untracked.bool(False),
    DebugStripStripQualityDB = cms.untracked.bool(False),
    SiStripQualityLabel = cms.string(''),
    UseStripNoiseDB = cms.bool(False),
    badStripCuts = cms.PSet(
        TID = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TOB = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TEC = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TIB = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        )
    ),
    DebugStripModuleQualityDB = cms.untracked.bool(False),
    ComponentName = cms.string('hltIter2ESPMeasurementTrackerPA'),
    DebugPixelModuleQualityDB = cms.untracked.bool(False),
    HitMatcher = cms.string('StandardMatcher'),
    skipClusters = cms.InputTag("hltPAFullTrackIter2ClustersRefRemoval"),
    UseStripModuleQualityDB = cms.bool(True)
)


process.hltIter2ESPMeasurementTrackerReg = cms.ESProducer("MeasurementTrackerESProducer",
    StripCPE = cms.string('StripCPEfromTrackAngle'),
    inactivePixelDetectorLabels = cms.VInputTag(),
    UseStripCablingDB = cms.bool(False),
    PixelCPE = cms.string('hltESPPixelCPEGeneric'),
    stripLazyGetterProducer = cms.string('hltSiStripRawToClustersFacility'),
    OnDemand = cms.bool(True),
    Regional = cms.bool(True),
    UsePixelModuleQualityDB = cms.bool(True),
    pixelClusterProducer = cms.string('hltSiPixelClustersReg'),
    switchOffPixelsIfEmpty = cms.bool(True),
    inactiveStripDetectorLabels = cms.VInputTag("hltSiStripExcludedFEDListProducer"),
    MaskBadAPVFibers = cms.bool(True),
    UseStripStripQualityDB = cms.bool(True),
    UsePixelROCQualityDB = cms.bool(True),
    DebugPixelROCQualityDB = cms.untracked.bool(False),
    UseStripAPVFiberQualityDB = cms.bool(True),
    stripClusterProducer = cms.string('hltIter2SiStripClustersReg'),
    DebugStripAPVFiberQualityDB = cms.untracked.bool(False),
    DebugStripStripQualityDB = cms.untracked.bool(False),
    SiStripQualityLabel = cms.string(''),
    UseStripNoiseDB = cms.bool(False),
    badStripCuts = cms.PSet(
        TID = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TOB = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TEC = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TIB = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        )
    ),
    DebugStripModuleQualityDB = cms.untracked.bool(False),
    ComponentName = cms.string('hltIter2ESPMeasurementTrackerReg'),
    DebugPixelModuleQualityDB = cms.untracked.bool(False),
    HitMatcher = cms.string('StandardMatcher'),
    skipClusters = cms.InputTag("hltIter2ClustersRefRemovalReg"),
    UseStripModuleQualityDB = cms.bool(True)
)


process.hltIter2ESPPixelLayerPairs = cms.ESProducer("SeedingLayersESProducer",
    layerList = cms.vstring('BPix1+BPix2', 
        'BPix1+BPix3', 
        'BPix2+BPix3', 
        'BPix1+FPix1_pos', 
        'BPix1+FPix1_neg', 
        'BPix1+FPix2_pos', 
        'BPix1+FPix2_neg', 
        'BPix2+FPix1_pos', 
        'BPix2+FPix1_neg', 
        'BPix2+FPix2_pos', 
        'BPix2+FPix2_neg', 
        'FPix1_pos+FPix2_pos', 
        'FPix1_neg+FPix2_neg'),
    TID = cms.PSet(

    ),
    ComponentName = cms.string('hltIter2ESPPixelLayerPairs'),
    TEC = cms.PSet(

    ),
    FPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        hitErrorRZ = cms.double(0.0036),
        useErrorsFromParam = cms.bool(True),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        skipClusters = cms.InputTag("hltIter2ClustersRefRemoval"),
        hitErrorRPhi = cms.double(0.0051)
    ),
    TOB = cms.PSet(

    ),
    BPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        hitErrorRZ = cms.double(0.006),
        useErrorsFromParam = cms.bool(True),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        skipClusters = cms.InputTag("hltIter2ClustersRefRemoval"),
        hitErrorRPhi = cms.double(0.0027)
    ),
    TIB = cms.PSet(

    )
)


process.hltIter2ESPPixelLayerPairsPA = cms.ESProducer("SeedingLayersESProducer",
    layerList = cms.vstring('BPix1+BPix2', 
        'BPix1+BPix3', 
        'BPix2+BPix3', 
        'BPix1+FPix1_pos', 
        'BPix1+FPix1_neg', 
        'BPix1+FPix2_pos', 
        'BPix1+FPix2_neg', 
        'BPix2+FPix1_pos', 
        'BPix2+FPix1_neg', 
        'BPix2+FPix2_pos', 
        'BPix2+FPix2_neg', 
        'FPix1_pos+FPix2_pos', 
        'FPix1_neg+FPix2_neg'),
    TID = cms.PSet(

    ),
    ComponentName = cms.string('hltIter2ESPPixelLayerPairsPA'),
    TEC = cms.PSet(

    ),
    FPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        hitErrorRZ = cms.double(0.0036),
        useErrorsFromParam = cms.bool(True),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        skipClusters = cms.InputTag("hltPAFullTrackIter2ClustersRefRemoval"),
        hitErrorRPhi = cms.double(0.0051)
    ),
    TOB = cms.PSet(

    ),
    BPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        hitErrorRZ = cms.double(0.006),
        useErrorsFromParam = cms.bool(True),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        skipClusters = cms.InputTag("hltPAFullTrackIter2ClustersRefRemoval"),
        hitErrorRPhi = cms.double(0.0027)
    ),
    TIB = cms.PSet(

    )
)


process.hltIter2ESPPixelLayerPairsReg = cms.ESProducer("SeedingLayersESProducer",
    layerList = cms.vstring('BPix1+BPix2', 
        'BPix1+BPix3', 
        'BPix2+BPix3', 
        'BPix1+FPix1_pos', 
        'BPix1+FPix1_neg', 
        'BPix1+FPix2_pos', 
        'BPix1+FPix2_neg', 
        'BPix2+FPix1_pos', 
        'BPix2+FPix1_neg', 
        'BPix2+FPix2_pos', 
        'BPix2+FPix2_neg', 
        'FPix1_pos+FPix2_pos', 
        'FPix1_neg+FPix2_neg'),
    TID = cms.PSet(

    ),
    ComponentName = cms.string('hltIter2ESPPixelLayerPairsReg'),
    TEC = cms.PSet(

    ),
    FPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHitsReg'),
        hitErrorRZ = cms.double(0.0036),
        useErrorsFromParam = cms.bool(True),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        skipClusters = cms.InputTag("hltIter2ClustersRefRemovalReg"),
        hitErrorRPhi = cms.double(0.0051)
    ),
    TOB = cms.PSet(

    ),
    BPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHitsReg'),
        hitErrorRZ = cms.double(0.006),
        useErrorsFromParam = cms.bool(True),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        skipClusters = cms.InputTag("hltIter2ClustersRefRemovalReg"),
        hitErrorRPhi = cms.double(0.0027)
    ),
    TIB = cms.PSet(

    )
)


process.hltIter2ESPTrajectoryBuilderIT = cms.ESProducer("CkfTrajectoryBuilderESProducer",
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    trajectoryFilterName = cms.string('hltIter2ESPTrajectoryFilterIT'),
    maxCand = cms.int32(2),
    ComponentName = cms.string('hltIter2ESPTrajectoryBuilderIT'),
    intermediateCleaning = cms.bool(True),
    MeasurementTrackerName = cms.string('hltIter2ESPMeasurementTracker'),
    estimator = cms.string('hltESPChi2MeasurementEstimator16'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    updator = cms.string('hltESPKFUpdator'),
    alwaysUseInvalidHits = cms.bool(False),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    lostHitPenalty = cms.double(30.0)
)


process.hltIter2ESPTrajectoryBuilderITPA = cms.ESProducer("CkfTrajectoryBuilderESProducer",
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    trajectoryFilterName = cms.string('hltIter2ESPTrajectoryFilterIT'),
    maxCand = cms.int32(2),
    ComponentName = cms.string('hltIter2ESPTrajectoryBuilderITPA'),
    intermediateCleaning = cms.bool(True),
    MeasurementTrackerName = cms.string('hltIter2ESPMeasurementTrackerPA'),
    estimator = cms.string('hltESPChi2MeasurementEstimator16'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    updator = cms.string('hltESPKFUpdator'),
    alwaysUseInvalidHits = cms.bool(False),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    lostHitPenalty = cms.double(30.0)
)


process.hltIter2ESPTrajectoryBuilderITReg = cms.ESProducer("CkfTrajectoryBuilderESProducer",
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    trajectoryFilterName = cms.string('hltIter2ESPTrajectoryFilterIT'),
    maxCand = cms.int32(2),
    ComponentName = cms.string('hltIter2ESPTrajectoryBuilderITReg'),
    intermediateCleaning = cms.bool(True),
    MeasurementTrackerName = cms.string('hltIter2ESPMeasurementTrackerReg'),
    estimator = cms.string('hltESPChi2MeasurementEstimator16'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    updator = cms.string('hltESPKFUpdator'),
    alwaysUseInvalidHits = cms.bool(False),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    lostHitPenalty = cms.double(30.0)
)


process.hltIter2ESPTrajectoryFilterIT = cms.ESProducer("TrajectoryFilterESProducer",
    filterPset = cms.PSet(
        chargeSignificance = cms.double(-1.0),
        minPt = cms.double(0.3),
        minHitsMinPt = cms.int32(3),
        ComponentType = cms.string('CkfBaseTrajectoryFilter'),
        maxLostHits = cms.int32(1),
        maxNumberOfHits = cms.int32(100),
        maxConsecLostHits = cms.int32(1),
        nSigmaMinPt = cms.double(5.0),
        minimumNumberOfHits = cms.int32(3)
    ),
    ComponentName = cms.string('hltIter2ESPTrajectoryFilterIT')
)


process.hltIter2Tau3MuESPMeasurementTracker = cms.ESProducer("MeasurementTrackerESProducer",
    StripCPE = cms.string('StripCPEfromTrackAngle'),
    inactivePixelDetectorLabels = cms.VInputTag(),
    UseStripCablingDB = cms.bool(False),
    PixelCPE = cms.string('hltESPPixelCPEGeneric'),
    stripLazyGetterProducer = cms.string('hltSiStripRawToClustersFacility'),
    OnDemand = cms.bool(True),
    Regional = cms.bool(True),
    UsePixelModuleQualityDB = cms.bool(True),
    pixelClusterProducer = cms.string('hltSiPixelClusters'),
    switchOffPixelsIfEmpty = cms.bool(True),
    inactiveStripDetectorLabels = cms.VInputTag("hltSiStripExcludedFEDListProducer"),
    MaskBadAPVFibers = cms.bool(True),
    UseStripStripQualityDB = cms.bool(True),
    UsePixelROCQualityDB = cms.bool(True),
    DebugPixelROCQualityDB = cms.untracked.bool(False),
    UseStripAPVFiberQualityDB = cms.bool(True),
    stripClusterProducer = cms.string('hltIter2SiStripClusters'),
    DebugStripAPVFiberQualityDB = cms.untracked.bool(False),
    DebugStripStripQualityDB = cms.untracked.bool(False),
    SiStripQualityLabel = cms.string(''),
    UseStripNoiseDB = cms.bool(False),
    badStripCuts = cms.PSet(
        TOB = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TID = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TEC = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TIB = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        )
    ),
    DebugStripModuleQualityDB = cms.untracked.bool(False),
    ComponentName = cms.string('hltIter2Tau3MuESPMeasurementTracker'),
    DebugPixelModuleQualityDB = cms.untracked.bool(False),
    HitMatcher = cms.string('StandardMatcher'),
    skipClusters = cms.InputTag("hltIter2Tau3MuClustersRefRemoval"),
    UseStripModuleQualityDB = cms.bool(True)
)


process.hltIter2Tau3MuESPPixelLayerPairs = cms.ESProducer("SeedingLayersESProducer",
    layerList = cms.vstring('BPix1+BPix2', 
        'BPix1+BPix3', 
        'BPix2+BPix3', 
        'BPix1+FPix1_pos', 
        'BPix1+FPix1_neg', 
        'BPix1+FPix2_pos', 
        'BPix1+FPix2_neg', 
        'BPix2+FPix1_pos', 
        'BPix2+FPix1_neg', 
        'BPix2+FPix2_pos', 
        'BPix2+FPix2_neg', 
        'FPix1_pos+FPix2_pos', 
        'FPix1_neg+FPix2_neg'),
    TID = cms.PSet(

    ),
    ComponentName = cms.string('hltIter2Tau3MuESPPixelLayerPairs'),
    TEC = cms.PSet(

    ),
    FPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        hitErrorRZ = cms.double(0.0036),
        useErrorsFromParam = cms.bool(True),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        skipClusters = cms.InputTag("hltIter2Tau3MuClustersRefRemoval"),
        hitErrorRPhi = cms.double(0.0051)
    ),
    TOB = cms.PSet(

    ),
    BPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        hitErrorRZ = cms.double(0.006),
        useErrorsFromParam = cms.bool(True),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        skipClusters = cms.InputTag("hltIter2Tau3MuClustersRefRemoval"),
        hitErrorRPhi = cms.double(0.0027)
    ),
    TIB = cms.PSet(

    )
)


process.hltIter2Tau3MuESPTrajectoryBuilderIT = cms.ESProducer("CkfTrajectoryBuilderESProducer",
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    trajectoryFilterName = cms.string('hltIter2ESPTrajectoryFilterIT'),
    maxCand = cms.int32(2),
    ComponentName = cms.string('hltIter2Tau3MuESPTrajectoryBuilderIT'),
    intermediateCleaning = cms.bool(True),
    MeasurementTrackerName = cms.string('hltIter2Tau3MuESPMeasurementTracker'),
    estimator = cms.string('hltESPChi2MeasurementEstimator16'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    updator = cms.string('hltESPKFUpdator'),
    alwaysUseInvalidHits = cms.bool(False),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    lostHitPenalty = cms.double(30.0)
)


process.hltIter3ESPLayerTriplets = cms.ESProducer("SeedingLayersESProducer",
    layerList = cms.vstring('BPix1+BPix2+BPix3', 
        'BPix1+BPix2+FPix1_pos', 
        'BPix1+BPix2+FPix1_neg', 
        'BPix1+FPix1_pos+FPix2_pos', 
        'BPix1+FPix1_neg+FPix2_neg', 
        'BPix2+FPix1_pos+FPix2_pos', 
        'BPix2+FPix1_neg+FPix2_neg', 
        'FPix1_pos+FPix2_pos+TEC1_pos', 
        'FPix1_neg+FPix2_neg+TEC1_neg', 
        'FPix2_pos+TEC2_pos+TEC3_pos', 
        'FPix2_neg+TEC2_neg+TEC3_neg', 
        'BPix2+BPix3+TIB1', 
        'BPix2+BPix3+TIB2', 
        'BPix1+BPix3+TIB1', 
        'BPix1+BPix3+TIB2', 
        'BPix1+BPix2+TIB1', 
        'BPix1+BPix2+TIB2'),
    TID = cms.PSet(

    ),
    ComponentName = cms.string('hltIter3ESPLayerTriplets'),
    TEC = cms.PSet(
        useRingSlector = cms.bool(True),
        TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
        minRing = cms.int32(1),
        maxRing = cms.int32(1)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        hitErrorRZ = cms.double(0.0036),
        useErrorsFromParam = cms.bool(True),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        skipClusters = cms.InputTag("hltIter3ClustersRefRemoval"),
        hitErrorRPhi = cms.double(0.0051)
    ),
    TOB = cms.PSet(

    ),
    BPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        hitErrorRZ = cms.double(0.006),
        useErrorsFromParam = cms.bool(True),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        skipClusters = cms.InputTag("hltIter3ClustersRefRemoval"),
        hitErrorRPhi = cms.double(0.0027)
    ),
    TIB = cms.PSet(
        TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle')
    )
)


process.hltIter3ESPLayerTripletsPA = cms.ESProducer("SeedingLayersESProducer",
    layerList = cms.vstring('BPix1+BPix2+BPix3', 
        'BPix1+BPix2+FPix1_pos', 
        'BPix1+BPix2+FPix1_neg', 
        'BPix1+FPix1_pos+FPix2_pos', 
        'BPix1+FPix1_neg+FPix2_neg', 
        'BPix2+FPix1_pos+FPix2_pos', 
        'BPix2+FPix1_neg+FPix2_neg', 
        'FPix1_pos+FPix2_pos+TEC1_pos', 
        'FPix1_neg+FPix2_neg+TEC1_neg', 
        'FPix2_pos+TEC2_pos+TEC3_pos', 
        'FPix2_neg+TEC2_neg+TEC3_neg', 
        'BPix2+BPix3+TIB1', 
        'BPix2+BPix3+TIB2', 
        'BPix1+BPix3+TIB1', 
        'BPix1+BPix3+TIB2', 
        'BPix1+BPix2+TIB1', 
        'BPix1+BPix2+TIB2'),
    TID = cms.PSet(

    ),
    ComponentName = cms.string('hltIter3ESPLayerTripletsPA'),
    TEC = cms.PSet(
        useRingSlector = cms.bool(True),
        TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
        minRing = cms.int32(1),
        maxRing = cms.int32(1)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        hitErrorRZ = cms.double(0.0036),
        useErrorsFromParam = cms.bool(True),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        skipClusters = cms.InputTag("hltPAFullTrackIter3ClustersRefRemoval"),
        hitErrorRPhi = cms.double(0.0051)
    ),
    TOB = cms.PSet(

    ),
    BPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        hitErrorRZ = cms.double(0.006),
        useErrorsFromParam = cms.bool(True),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        skipClusters = cms.InputTag("hltPAFullTrackIter3ClustersRefRemoval"),
        hitErrorRPhi = cms.double(0.0027)
    ),
    TIB = cms.PSet(
        TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle')
    )
)


process.hltIter3ESPLayerTripletsReg = cms.ESProducer("SeedingLayersESProducer",
    layerList = cms.vstring('BPix1+BPix2+BPix3', 
        'BPix1+BPix2+FPix1_pos', 
        'BPix1+BPix2+FPix1_neg', 
        'BPix1+FPix1_pos+FPix2_pos', 
        'BPix1+FPix1_neg+FPix2_neg', 
        'BPix2+FPix1_pos+FPix2_pos', 
        'BPix2+FPix1_neg+FPix2_neg', 
        'FPix1_pos+FPix2_pos+TEC1_pos', 
        'FPix1_neg+FPix2_neg+TEC1_neg', 
        'FPix2_pos+TEC2_pos+TEC3_pos', 
        'FPix2_neg+TEC2_neg+TEC3_neg', 
        'BPix2+BPix3+TIB1', 
        'BPix2+BPix3+TIB2', 
        'BPix1+BPix3+TIB1', 
        'BPix1+BPix3+TIB2', 
        'BPix1+BPix2+TIB1', 
        'BPix1+BPix2+TIB2'),
    TID = cms.PSet(

    ),
    ComponentName = cms.string('hltIter3ESPLayerTripletsReg'),
    TEC = cms.PSet(
        useRingSlector = cms.bool(True),
        TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
        minRing = cms.int32(1),
        maxRing = cms.int32(1)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHitsReg'),
        hitErrorRZ = cms.double(0.0036),
        useErrorsFromParam = cms.bool(True),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        skipClusters = cms.InputTag("hltIter3ClustersRefRemovalReg"),
        hitErrorRPhi = cms.double(0.0051)
    ),
    TOB = cms.PSet(

    ),
    BPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHitsReg'),
        hitErrorRZ = cms.double(0.006),
        useErrorsFromParam = cms.bool(True),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        skipClusters = cms.InputTag("hltIter3ClustersRefRemovalReg"),
        hitErrorRPhi = cms.double(0.0027)
    ),
    TIB = cms.PSet(
        TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle')
    )
)


process.hltIter3ESPMeasurementTracker = cms.ESProducer("MeasurementTrackerESProducer",
    StripCPE = cms.string('StripCPEfromTrackAngle'),
    inactivePixelDetectorLabels = cms.VInputTag(),
    UseStripCablingDB = cms.bool(False),
    PixelCPE = cms.string('hltESPPixelCPEGeneric'),
    stripLazyGetterProducer = cms.string('hltSiStripRawToClustersFacility'),
    OnDemand = cms.bool(True),
    Regional = cms.bool(True),
    UsePixelModuleQualityDB = cms.bool(True),
    pixelClusterProducer = cms.string('hltSiPixelClusters'),
    switchOffPixelsIfEmpty = cms.bool(True),
    inactiveStripDetectorLabels = cms.VInputTag("hltSiStripExcludedFEDListProducer"),
    MaskBadAPVFibers = cms.bool(True),
    UseStripStripQualityDB = cms.bool(True),
    UsePixelROCQualityDB = cms.bool(True),
    DebugPixelROCQualityDB = cms.untracked.bool(False),
    UseStripAPVFiberQualityDB = cms.bool(True),
    stripClusterProducer = cms.string('hltIter3SiStripClusters'),
    DebugStripAPVFiberQualityDB = cms.untracked.bool(False),
    DebugStripStripQualityDB = cms.untracked.bool(False),
    SiStripQualityLabel = cms.string(''),
    UseStripNoiseDB = cms.bool(False),
    badStripCuts = cms.PSet(
        TID = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TOB = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TEC = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TIB = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        )
    ),
    DebugStripModuleQualityDB = cms.untracked.bool(False),
    ComponentName = cms.string('hltIter3ESPMeasurementTracker'),
    DebugPixelModuleQualityDB = cms.untracked.bool(False),
    HitMatcher = cms.string('StandardMatcher'),
    skipClusters = cms.InputTag("hltIter3ClustersRefRemoval"),
    UseStripModuleQualityDB = cms.bool(True)
)


process.hltIter3ESPMeasurementTrackerPA = cms.ESProducer("MeasurementTrackerESProducer",
    StripCPE = cms.string('StripCPEfromTrackAngle'),
    inactivePixelDetectorLabels = cms.VInputTag(),
    UseStripCablingDB = cms.bool(False),
    PixelCPE = cms.string('hltESPPixelCPEGeneric'),
    stripLazyGetterProducer = cms.string('hltSiStripRawToClustersFacility'),
    OnDemand = cms.bool(True),
    Regional = cms.bool(True),
    UsePixelModuleQualityDB = cms.bool(True),
    pixelClusterProducer = cms.string('hltSiPixelClusters'),
    switchOffPixelsIfEmpty = cms.bool(True),
    inactiveStripDetectorLabels = cms.VInputTag("hltSiStripExcludedFEDListProducer"),
    MaskBadAPVFibers = cms.bool(True),
    UseStripStripQualityDB = cms.bool(True),
    UsePixelROCQualityDB = cms.bool(True),
    DebugPixelROCQualityDB = cms.untracked.bool(False),
    UseStripAPVFiberQualityDB = cms.bool(True),
    stripClusterProducer = cms.string('hltPAFullTrackIter3SiStripClusters'),
    DebugStripAPVFiberQualityDB = cms.untracked.bool(False),
    DebugStripStripQualityDB = cms.untracked.bool(False),
    SiStripQualityLabel = cms.string(''),
    UseStripNoiseDB = cms.bool(False),
    badStripCuts = cms.PSet(
        TID = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TOB = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TEC = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TIB = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        )
    ),
    DebugStripModuleQualityDB = cms.untracked.bool(False),
    ComponentName = cms.string('hltIter3ESPMeasurementTrackerPA'),
    DebugPixelModuleQualityDB = cms.untracked.bool(False),
    HitMatcher = cms.string('StandardMatcher'),
    skipClusters = cms.InputTag("hltPAFullTrackIter3ClustersRefRemoval"),
    UseStripModuleQualityDB = cms.bool(True)
)


process.hltIter3ESPMeasurementTrackerReg = cms.ESProducer("MeasurementTrackerESProducer",
    StripCPE = cms.string('StripCPEfromTrackAngle'),
    inactivePixelDetectorLabels = cms.VInputTag(),
    UseStripCablingDB = cms.bool(False),
    PixelCPE = cms.string('hltESPPixelCPEGeneric'),
    stripLazyGetterProducer = cms.string('hltSiStripRawToClustersFacility'),
    OnDemand = cms.bool(True),
    Regional = cms.bool(True),
    UsePixelModuleQualityDB = cms.bool(True),
    pixelClusterProducer = cms.string('hltSiPixelClustersReg'),
    switchOffPixelsIfEmpty = cms.bool(True),
    inactiveStripDetectorLabels = cms.VInputTag("hltSiStripExcludedFEDListProducer"),
    MaskBadAPVFibers = cms.bool(True),
    UseStripStripQualityDB = cms.bool(True),
    UsePixelROCQualityDB = cms.bool(True),
    DebugPixelROCQualityDB = cms.untracked.bool(False),
    UseStripAPVFiberQualityDB = cms.bool(True),
    stripClusterProducer = cms.string('hltIter3SiStripClustersReg'),
    DebugStripAPVFiberQualityDB = cms.untracked.bool(False),
    DebugStripStripQualityDB = cms.untracked.bool(False),
    SiStripQualityLabel = cms.string(''),
    UseStripNoiseDB = cms.bool(False),
    badStripCuts = cms.PSet(
        TID = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TOB = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TEC = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TIB = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        )
    ),
    DebugStripModuleQualityDB = cms.untracked.bool(False),
    ComponentName = cms.string('hltIter3ESPMeasurementTrackerReg'),
    DebugPixelModuleQualityDB = cms.untracked.bool(False),
    HitMatcher = cms.string('StandardMatcher'),
    skipClusters = cms.InputTag("hltIter3ClustersRefRemovalReg"),
    UseStripModuleQualityDB = cms.bool(True)
)


process.hltIter3ESPTrajectoryBuilderIT = cms.ESProducer("CkfTrajectoryBuilderESProducer",
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    trajectoryFilterName = cms.string('hltIter3ESPTrajectoryFilterIT'),
    maxCand = cms.int32(1),
    ComponentName = cms.string('hltIter3ESPTrajectoryBuilderIT'),
    intermediateCleaning = cms.bool(True),
    MeasurementTrackerName = cms.string('hltIter3ESPMeasurementTracker'),
    estimator = cms.string('hltESPChi2MeasurementEstimator16'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    updator = cms.string('hltESPKFUpdator'),
    alwaysUseInvalidHits = cms.bool(False),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    lostHitPenalty = cms.double(30.0)
)


process.hltIter3ESPTrajectoryBuilderITPA = cms.ESProducer("CkfTrajectoryBuilderESProducer",
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    trajectoryFilterName = cms.string('hltIter3ESPTrajectoryFilterIT'),
    maxCand = cms.int32(1),
    ComponentName = cms.string('hltIter3ESPTrajectoryBuilderITPA'),
    intermediateCleaning = cms.bool(True),
    MeasurementTrackerName = cms.string('hltIter3ESPMeasurementTrackerPA'),
    estimator = cms.string('hltESPChi2MeasurementEstimator16'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    updator = cms.string('hltESPKFUpdator'),
    alwaysUseInvalidHits = cms.bool(False),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    lostHitPenalty = cms.double(30.0)
)


process.hltIter3ESPTrajectoryBuilderITReg = cms.ESProducer("CkfTrajectoryBuilderESProducer",
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    trajectoryFilterName = cms.string('hltIter3ESPTrajectoryFilterIT'),
    maxCand = cms.int32(1),
    ComponentName = cms.string('hltIter3ESPTrajectoryBuilderITReg'),
    intermediateCleaning = cms.bool(True),
    MeasurementTrackerName = cms.string('hltIter3ESPMeasurementTrackerReg'),
    estimator = cms.string('hltESPChi2MeasurementEstimator16'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    updator = cms.string('hltESPKFUpdator'),
    alwaysUseInvalidHits = cms.bool(False),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    lostHitPenalty = cms.double(30.0)
)


process.hltIter3ESPTrajectoryFilterIT = cms.ESProducer("TrajectoryFilterESProducer",
    filterPset = cms.PSet(
        chargeSignificance = cms.double(-1.0),
        minPt = cms.double(0.3),
        minHitsMinPt = cms.int32(3),
        ComponentType = cms.string('CkfBaseTrajectoryFilter'),
        maxLostHits = cms.int32(0),
        maxNumberOfHits = cms.int32(100),
        maxConsecLostHits = cms.int32(1),
        nSigmaMinPt = cms.double(5.0),
        minimumNumberOfHits = cms.int32(3)
    ),
    ComponentName = cms.string('hltIter3ESPTrajectoryFilterIT')
)


process.hltIter3Tau3MuESPLayerTriplets = cms.ESProducer("SeedingLayersESProducer",
    layerList = cms.vstring('BPix1+BPix2+BPix3', 
        'BPix1+BPix2+FPix1_pos', 
        'BPix1+BPix2+FPix1_neg', 
        'BPix1+FPix1_pos+FPix2_pos', 
        'BPix1+FPix1_neg+FPix2_neg', 
        'BPix2+FPix1_pos+FPix2_pos', 
        'BPix2+FPix1_neg+FPix2_neg', 
        'FPix1_pos+FPix2_pos+TEC1_pos', 
        'FPix1_neg+FPix2_neg+TEC1_neg', 
        'FPix2_pos+TEC2_pos+TEC3_pos', 
        'FPix2_neg+TEC2_neg+TEC3_neg', 
        'BPix2+BPix3+TIB1', 
        'BPix2+BPix3+TIB2', 
        'BPix1+BPix3+TIB1', 
        'BPix1+BPix3+TIB2', 
        'BPix1+BPix2+TIB1', 
        'BPix1+BPix2+TIB2'),
    TID = cms.PSet(

    ),
    ComponentName = cms.string('hltIter3Tau3MuESPLayerTriplets'),
    TEC = cms.PSet(
        useRingSlector = cms.bool(True),
        TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
        minRing = cms.int32(1),
        maxRing = cms.int32(1)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        hitErrorRZ = cms.double(0.0036),
        useErrorsFromParam = cms.bool(True),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        skipClusters = cms.InputTag("hltIter3Tau3MuClustersRefRemoval"),
        hitErrorRPhi = cms.double(0.0051)
    ),
    TOB = cms.PSet(

    ),
    BPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        hitErrorRZ = cms.double(0.006),
        useErrorsFromParam = cms.bool(True),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        skipClusters = cms.InputTag("hltIter3Tau3MuClustersRefRemoval"),
        hitErrorRPhi = cms.double(0.0027)
    ),
    TIB = cms.PSet(
        TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle')
    )
)


process.hltIter3Tau3MuESPMeasurementTracker = cms.ESProducer("MeasurementTrackerESProducer",
    StripCPE = cms.string('StripCPEfromTrackAngle'),
    inactivePixelDetectorLabels = cms.VInputTag(),
    UseStripCablingDB = cms.bool(False),
    PixelCPE = cms.string('hltESPPixelCPEGeneric'),
    stripLazyGetterProducer = cms.string('hltSiStripRawToClustersFacility'),
    OnDemand = cms.bool(True),
    Regional = cms.bool(True),
    UsePixelModuleQualityDB = cms.bool(True),
    pixelClusterProducer = cms.string('hltSiPixelClusters'),
    switchOffPixelsIfEmpty = cms.bool(True),
    inactiveStripDetectorLabels = cms.VInputTag("hltSiStripExcludedFEDListProducer"),
    MaskBadAPVFibers = cms.bool(True),
    UseStripStripQualityDB = cms.bool(True),
    UsePixelROCQualityDB = cms.bool(True),
    DebugPixelROCQualityDB = cms.untracked.bool(False),
    UseStripAPVFiberQualityDB = cms.bool(True),
    stripClusterProducer = cms.string('hltIter3Tau3MuSiStripClusters'),
    DebugStripAPVFiberQualityDB = cms.untracked.bool(False),
    DebugStripStripQualityDB = cms.untracked.bool(False),
    SiStripQualityLabel = cms.string(''),
    UseStripNoiseDB = cms.bool(False),
    badStripCuts = cms.PSet(
        TOB = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TID = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TEC = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TIB = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        )
    ),
    DebugStripModuleQualityDB = cms.untracked.bool(False),
    ComponentName = cms.string('hltIter3Tau3MuESPMeasurementTracker'),
    DebugPixelModuleQualityDB = cms.untracked.bool(False),
    HitMatcher = cms.string('StandardMatcher'),
    skipClusters = cms.InputTag("hltIter3Tau3MuClustersRefRemoval"),
    UseStripModuleQualityDB = cms.bool(True)
)


process.hltIter3Tau3MuESPTrajectoryBuilderIT = cms.ESProducer("CkfTrajectoryBuilderESProducer",
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    trajectoryFilterName = cms.string('hltIter3ESPTrajectoryFilterIT'),
    maxCand = cms.int32(1),
    ComponentName = cms.string('hltIter3Tau3MuESPTrajectoryBuilderIT'),
    intermediateCleaning = cms.bool(True),
    MeasurementTrackerName = cms.string('hltIter3Tau3MuESPMeasurementTracker'),
    estimator = cms.string('hltESPChi2MeasurementEstimator16'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    updator = cms.string('hltESPKFUpdator'),
    alwaysUseInvalidHits = cms.bool(False),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    lostHitPenalty = cms.double(30.0)
)


process.hltIter4ESPMeasurementTracker = cms.ESProducer("MeasurementTrackerESProducer",
    StripCPE = cms.string('StripCPEfromTrackAngle'),
    inactivePixelDetectorLabels = cms.VInputTag(),
    UseStripCablingDB = cms.bool(False),
    PixelCPE = cms.string('hltESPPixelCPEGeneric'),
    stripLazyGetterProducer = cms.string('hltSiStripRawToClustersFacility'),
    OnDemand = cms.bool(True),
    Regional = cms.bool(True),
    UsePixelModuleQualityDB = cms.bool(True),
    pixelClusterProducer = cms.string('hltSiPixelClusters'),
    switchOffPixelsIfEmpty = cms.bool(True),
    inactiveStripDetectorLabels = cms.VInputTag("hltSiStripExcludedFEDListProducer"),
    MaskBadAPVFibers = cms.bool(True),
    UseStripStripQualityDB = cms.bool(True),
    UsePixelROCQualityDB = cms.bool(True),
    DebugPixelROCQualityDB = cms.untracked.bool(False),
    UseStripAPVFiberQualityDB = cms.bool(True),
    stripClusterProducer = cms.string('hltIter4SiStripClusters'),
    DebugStripAPVFiberQualityDB = cms.untracked.bool(False),
    DebugStripStripQualityDB = cms.untracked.bool(False),
    SiStripQualityLabel = cms.string(''),
    UseStripNoiseDB = cms.bool(False),
    badStripCuts = cms.PSet(
        TID = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TOB = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TEC = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TIB = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        )
    ),
    DebugStripModuleQualityDB = cms.untracked.bool(False),
    ComponentName = cms.string('hltIter4ESPMeasurementTracker'),
    DebugPixelModuleQualityDB = cms.untracked.bool(False),
    HitMatcher = cms.string('StandardMatcher'),
    skipClusters = cms.InputTag("hltIter4ClustersRefRemoval"),
    UseStripModuleQualityDB = cms.bool(True)
)


process.hltIter4ESPMeasurementTrackerReg = cms.ESProducer("MeasurementTrackerESProducer",
    StripCPE = cms.string('StripCPEfromTrackAngle'),
    inactivePixelDetectorLabels = cms.VInputTag(),
    UseStripCablingDB = cms.bool(False),
    PixelCPE = cms.string('hltESPPixelCPEGeneric'),
    stripLazyGetterProducer = cms.string('hltSiStripRawToClustersFacility'),
    OnDemand = cms.bool(True),
    Regional = cms.bool(True),
    UsePixelModuleQualityDB = cms.bool(True),
    pixelClusterProducer = cms.string('hltSiPixelClustersReg'),
    switchOffPixelsIfEmpty = cms.bool(True),
    inactiveStripDetectorLabels = cms.VInputTag("hltSiStripExcludedFEDListProducer"),
    MaskBadAPVFibers = cms.bool(True),
    UseStripStripQualityDB = cms.bool(True),
    UsePixelROCQualityDB = cms.bool(True),
    DebugPixelROCQualityDB = cms.untracked.bool(False),
    UseStripAPVFiberQualityDB = cms.bool(True),
    stripClusterProducer = cms.string('hltIter4SiStripClustersReg'),
    DebugStripAPVFiberQualityDB = cms.untracked.bool(False),
    DebugStripStripQualityDB = cms.untracked.bool(False),
    SiStripQualityLabel = cms.string(''),
    UseStripNoiseDB = cms.bool(False),
    badStripCuts = cms.PSet(
        TID = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TOB = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TEC = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TIB = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        )
    ),
    DebugStripModuleQualityDB = cms.untracked.bool(False),
    ComponentName = cms.string('hltIter4ESPMeasurementTrackerReg'),
    DebugPixelModuleQualityDB = cms.untracked.bool(False),
    HitMatcher = cms.string('StandardMatcher'),
    skipClusters = cms.InputTag("hltIter4ClustersRefRemovalReg"),
    UseStripModuleQualityDB = cms.bool(True)
)


process.hltIter4ESPPixelLayerPairs = cms.ESProducer("SeedingLayersESProducer",
    layerList = cms.vstring('TIB1+TIB2'),
    TID = cms.PSet(

    ),
    ComponentName = cms.string('hltIter4ESPPixelLayerPairs'),
    TEC = cms.PSet(

    ),
    FPix = cms.PSet(

    ),
    TOB = cms.PSet(

    ),
    BPix = cms.PSet(

    ),
    TIB = cms.PSet(
        TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle')
    )
)


process.hltIter4ESPTrajectoryBuilderIT = cms.ESProducer("CkfTrajectoryBuilderESProducer",
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    trajectoryFilterName = cms.string('hltIter4ESPTrajectoryFilterIT'),
    maxCand = cms.int32(1),
    ComponentName = cms.string('hltIter4ESPTrajectoryBuilderIT'),
    intermediateCleaning = cms.bool(True),
    MeasurementTrackerName = cms.string('hltIter4ESPMeasurementTracker'),
    estimator = cms.string('hltESPChi2MeasurementEstimator16'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    lostHitPenalty = cms.double(30.0),
    updator = cms.string('hltESPKFUpdator'),
    alwaysUseInvalidHits = cms.bool(False),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    minNrOfHitsForRebuild = cms.untracked.int32(4)
)


process.hltIter4ESPTrajectoryBuilderITReg = cms.ESProducer("CkfTrajectoryBuilderESProducer",
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    trajectoryFilterName = cms.string('hltIter4ESPTrajectoryFilterIT'),
    maxCand = cms.int32(1),
    ComponentName = cms.string('hltIter4ESPTrajectoryBuilderITReg'),
    intermediateCleaning = cms.bool(True),
    MeasurementTrackerName = cms.string('hltIter4ESPMeasurementTrackerReg'),
    estimator = cms.string('hltESPChi2MeasurementEstimator16'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    updator = cms.string('hltESPKFUpdator'),
    alwaysUseInvalidHits = cms.bool(False),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    lostHitPenalty = cms.double(30.0)
)


process.hltIter4ESPTrajectoryFilterIT = cms.ESProducer("TrajectoryFilterESProducer",
    filterPset = cms.PSet(
        chargeSignificance = cms.double(-1.0),
        minPt = cms.double(0.3),
        minHitsMinPt = cms.int32(3),
        ComponentType = cms.string('CkfBaseTrajectoryFilter'),
        maxLostHits = cms.int32(0),
        maxNumberOfHits = cms.int32(100),
        maxConsecLostHits = cms.int32(1),
        nSigmaMinPt = cms.double(5.0),
        minimumNumberOfHits = cms.int32(6)
    ),
    ComponentName = cms.string('hltIter4ESPTrajectoryFilterIT')
)


process.hltIter4Tau3MuESPMeasurementTracker = cms.ESProducer("MeasurementTrackerESProducer",
    StripCPE = cms.string('StripCPEfromTrackAngle'),
    inactivePixelDetectorLabels = cms.VInputTag(),
    UseStripCablingDB = cms.bool(False),
    PixelCPE = cms.string('hltESPPixelCPEGeneric'),
    stripLazyGetterProducer = cms.string('hltSiStripRawToClustersFacility'),
    OnDemand = cms.bool(True),
    Regional = cms.bool(True),
    UsePixelModuleQualityDB = cms.bool(True),
    pixelClusterProducer = cms.string('hltSiPixelClusters'),
    switchOffPixelsIfEmpty = cms.bool(True),
    inactiveStripDetectorLabels = cms.VInputTag("hltSiStripExcludedFEDListProducer"),
    MaskBadAPVFibers = cms.bool(True),
    UseStripStripQualityDB = cms.bool(True),
    UsePixelROCQualityDB = cms.bool(True),
    DebugPixelROCQualityDB = cms.untracked.bool(False),
    UseStripAPVFiberQualityDB = cms.bool(True),
    stripClusterProducer = cms.string('hltIter4Tau3MuSiStripClusters'),
    DebugStripAPVFiberQualityDB = cms.untracked.bool(False),
    DebugStripStripQualityDB = cms.untracked.bool(False),
    SiStripQualityLabel = cms.string(''),
    UseStripNoiseDB = cms.bool(False),
    badStripCuts = cms.PSet(
        TOB = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TID = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TEC = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        ),
        TIB = cms.PSet(
            maxConsecutiveBad = cms.uint32(9999),
            maxBad = cms.uint32(9999)
        )
    ),
    DebugStripModuleQualityDB = cms.untracked.bool(False),
    ComponentName = cms.string('hltIter4Tau3MuESPMeasurementTracker'),
    DebugPixelModuleQualityDB = cms.untracked.bool(False),
    HitMatcher = cms.string('StandardMatcher'),
    skipClusters = cms.InputTag("hltIter4Tau3MuClustersRefRemoval"),
    UseStripModuleQualityDB = cms.bool(True)
)


process.hltIter4Tau3MuESPTrajectoryBuilderIT = cms.ESProducer("CkfTrajectoryBuilderESProducer",
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    trajectoryFilterName = cms.string('hltIter4ESPTrajectoryFilterIT'),
    maxCand = cms.int32(1),
    ComponentName = cms.string('hltIter4Tau3MuESPTrajectoryBuilderIT'),
    intermediateCleaning = cms.bool(True),
    MeasurementTrackerName = cms.string('hltIter4Tau3MuESPMeasurementTracker'),
    estimator = cms.string('hltESPChi2MeasurementEstimator16'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    lostHitPenalty = cms.double(30.0),
    updator = cms.string('hltESPKFUpdator'),
    alwaysUseInvalidHits = cms.bool(False),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    minNrOfHitsForRebuild = cms.untracked.int32(4)
)


process.hoDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('HODetIdAssociator'),
    includeBadChambers = cms.bool(False),
    etaBinSize = cms.double(0.087),
    nEta = cms.int32(30),
    nPhi = cms.int32(72)
)


process.muonDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('MuonDetIdAssociator'),
    includeBadChambers = cms.bool(False),
    etaBinSize = cms.double(0.125),
    nEta = cms.int32(48),
    nPhi = cms.int32(48)
)


process.navigationSchoolESProducer = cms.ESProducer("NavigationSchoolESProducer",
    ComponentName = cms.string('SimpleNavigationSchool')
)


process.preshowerDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('PreshowerDetIdAssociator'),
    includeBadChambers = cms.bool(False),
    etaBinSize = cms.double(0.1),
    nEta = cms.int32(60),
    nPhi = cms.int32(30)
)


process.siPixelQualityESProducer = cms.ESProducer("SiPixelQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(cms.PSet(
        record = cms.string('SiPixelQualityFromDbRcd'),
        tag = cms.string('')
    ), 
        cms.PSet(
            record = cms.string('SiPixelDetVOffRcd'),
            tag = cms.string('')
        ))
)


process.siPixelTemplateDBObjectESProducer = cms.ESProducer("SiPixelTemplateDBObjectESProducer")


process.siStripLorentzAngleDepESProducer = cms.ESProducer("SiStripLorentzAngleDepESProducer",
    LatencyRecord = cms.PSet(
        record = cms.string('SiStripLatencyRcd'),
        label = cms.untracked.string('')
    ),
    LorentzAnglePeakMode = cms.PSet(
        record = cms.string('SiStripLorentzAngleRcd'),
        label = cms.untracked.string('peak')
    ),
    LorentzAngleDeconvMode = cms.PSet(
        record = cms.string('SiStripLorentzAngleRcd'),
        label = cms.untracked.string('deconvolution')
    )
)


process.sistripconn = cms.ESProducer("SiStripConnectivity")


process.GlobalTag = cms.ESSource("PoolDBESSource",
    globaltag = cms.string('START53_V15A::All'),
    RefreshEachRun = cms.untracked.bool(True),
    ReconnectEachRun = cms.untracked.bool(True),
    toGet = cms.VPSet(cms.PSet(
        record = cms.string('L1MuCSCPtLutRcd'),
        tag = cms.string('L1MuCSCPtLut_key-11_mc'),
        connect = cms.untracked.string('frontier://FrontierProd/CMS_COND_31X_L1T')
    ), 
        cms.PSet(
            record = cms.string('L1HtMissScaleRcd'),
            tag = cms.string('L1HtMissScale_GCTPhysics_2012_04_27_JetSeedThresh5GeV_mc'),
            connect = cms.untracked.string('frontier://FrontierProd/CMS_COND_31X_L1T')
        ), 
        cms.PSet(
            record = cms.string('L1JetEtScaleRcd'),
            tag = cms.string('L1JetEtScale_GCTPhysics_2012_04_27_JetSeedThresh5GeV_mc'),
            connect = cms.untracked.string('frontier://FrontierProd/CMS_COND_31X_L1T')
        ), 
        cms.PSet(
            record = cms.string('L1GctJetFinderParamsRcd'),
            tag = cms.string('L1GctJetFinderParams_GCTPhysics_2012_04_27_JetSeedThresh5GeV_mc'),
            connect = cms.untracked.string('frontier://FrontierProd/CMS_COND_31X_L1T')
        ), 
        cms.PSet(
            record = cms.string('L1GtTriggerMenuRcd'),
            tag = cms.string('L1GtTriggerMenu_L1Menu_Collisions2012_v3_mc'),
            connect = cms.untracked.string('frontier://FrontierProd/CMS_COND_31X_L1T')
        ), 
        cms.PSet(
            record = cms.string('L1MuDTTFParametersRcd'),
            tag = cms.string('L1MuDTTFParameters_dttf12_TSC_03_csc_col_mc'),
            connect = cms.untracked.string('frontier://FrontierProd/CMS_COND_31X_L1T')
        ), 
        cms.PSet(
            record = cms.string('L1HfRingEtScaleRcd'),
            tag = cms.string('L1HfRingEtScale_GCTPhysics_2012_04_27_JetSeedThresh5GeV_mc'),
            connect = cms.untracked.string('frontier://FrontierProd/CMS_COND_31X_L1T')
        )),
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string('.'),
        connectionRetrialPeriod = cms.untracked.int32(10),
        idleConnectionCleanupPeriod = cms.untracked.int32(10),
        messageLevel = cms.untracked.int32(0),
        enablePoolAutomaticCleanUp = cms.untracked.bool(False),
        enableConnectionSharing = cms.untracked.bool(True),
        enableReadOnlySessionOnUpdateConnection = cms.untracked.bool(False),
        connectionTimeOut = cms.untracked.int32(0),
        connectionRetrialTimeOut = cms.untracked.int32(60)
    ),
    timetype = cms.string('runnumber'),
    RefreshAlways = cms.untracked.bool(False),
    connect = cms.string('frontier://FrontierProd/CMS_COND_31X_GLOBALTAG'),
    RefreshOpenIOVs = cms.untracked.bool(False),
    BlobStreamerName = cms.untracked.string('TBufferBlobStreamingService'),
    pfnPrefix = cms.untracked.string('frontier://FrontierProd/')
)


process.HepPDTESSource = cms.ESSource("HepPDTESSource",
    pdtFileName = cms.FileInPath('SimGeneral/HepPDTESSource/data/pythiaparticle.tbl')
)


process.eegeom = cms.ESSource("EmptyESSource",
    recordName = cms.string('EcalMappingRcd'),
    iovIsRunNotTime = cms.bool(True),
    firstValid = cms.vuint32(1)
)


process.es_hardcode = cms.ESSource("HcalHardcodeCalibrations",
    fromDDD = cms.untracked.bool(False),
    toGet = cms.untracked.vstring('GainWidths')
)


process.hltESSBTagRecord = cms.ESSource("EmptyESSource",
    recordName = cms.string('JetTagComputerRecord'),
    iovIsRunNotTime = cms.bool(True),
    firstValid = cms.vuint32(1)
)


process.hltESSEcalSeverityLevel = cms.ESSource("EmptyESSource",
    recordName = cms.string('EcalSeverityLevelAlgoRcd'),
    iovIsRunNotTime = cms.bool(True),
    firstValid = cms.vuint32(1)
)


process.hltESSHcalSeverityLevel = cms.ESSource("EmptyESSource",
    recordName = cms.string('HcalSeverityLevelComputerRcd'),
    iovIsRunNotTime = cms.bool(True),
    firstValid = cms.vuint32(1)
)


process.magfield = cms.ESSource("XMLIdealGeometryESSource",
    geomXMLFiles = cms.vstring('Geometry/CMSCommonData/data/normal/cmsextent.xml', 
        'Geometry/CMSCommonData/data/cms.xml', 
        'Geometry/CMSCommonData/data/cmsMagneticField.xml', 
        'MagneticField/GeomBuilder/data/MagneticFieldVolumes_1103l.xml', 
        'MagneticField/GeomBuilder/data/MagneticFieldParameters_07_2pi.xml'),
    rootNodeName = cms.string('cmsMagneticField:MAGF')
)


process.HLTConfigVersion = cms.PSet(
    tableName = cms.string('/cdaq/physics/Run2012/8e33/v2.1/HLT/V7')
)

process.datasets = cms.PSet(
    MuOniaParked = cms.vstring('HLT_BTagMu_Jet20_Mu4_v2', 
        'HLT_BTagMu_Jet60_Mu4_v2', 
        'HLT_Dimuon10_Jpsi_v6', 
        'HLT_Dimuon5_PsiPrime_v6', 
        'HLT_Dimuon5_Upsilon_v6', 
        'HLT_Dimuon7_PsiPrime_v3', 
        'HLT_Dimuon8_Jpsi_v7', 
        'HLT_Dimuon8_Upsilon_v6', 
        'HLT_DoubleMu3p5_LowMassNonResonant_Displaced_v6', 
        'HLT_DoubleMu3p5_LowMass_Displaced_v6', 
        'HLT_Mu15_TkMu5_Onia_v1'),
    HcalHPDNoise = cms.vstring('HLT_GlobalRunHPDNoise_v8', 
        'HLT_L1Tech_HBHEHO_totalOR_v6', 
        'HLT_L1Tech_HCAL_HF_single_channel_v4'),
    JetHT = cms.vstring('HLT_DiPFJetAve320_v10', 
        'HLT_DiPFJetAve400_v10', 
        'HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v10', 
        'HLT_HT200_v6', 
        'HLT_HT250_v7', 
        'HLT_HT300_DoubleDisplacedPFJet60_ChgFraction10_v10', 
        'HLT_HT300_DoubleDisplacedPFJet60_v10', 
        'HLT_HT300_SingleDisplacedPFJet60_ChgFraction10_v10', 
        'HLT_HT300_SingleDisplacedPFJet60_v10', 
        'HLT_HT300_v7', 
        'HLT_HT350_v7', 
        'HLT_HT400_v7', 
        'HLT_HT450_v7', 
        'HLT_HT500_v7', 
        'HLT_HT550_v7', 
        'HLT_HT650_Track50_dEdx3p6_v10', 
        'HLT_HT650_Track60_dEdx3p7_v10', 
        'HLT_HT650_v7', 
        'HLT_HT750_v7', 
        'HLT_Jet370_NoJetID_v15', 
        'HLT_MET80_Track50_dEdx3p6_v6', 
        'HLT_MET80_Track60_dEdx3p7_v6', 
        'HLT_MET80_v5', 
        'HLT_PFJet320_v9', 
        'HLT_PFJet400_v9', 
        'HLT_PFNoPUHT350_v4', 
        'HLT_PFNoPUHT650_DiCentralPFNoPUJet80_CenPFNoPUJet40_v4', 
        'HLT_PFNoPUHT650_v4', 
        'HLT_PFNoPUHT700_v4', 
        'HLT_PFNoPUHT750_v4'),
    ElectronHad = cms.vstring('HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v3', 
        'HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v3', 
        'HLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT_v3', 
        'HLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT_v3', 
        'HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v3', 
        'HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v3', 
        'HLT_DoubleEle14_CaloIdT_TrkIdVL_Mass8_PFMET40_v8', 
        'HLT_DoubleEle14_CaloIdT_TrkIdVL_Mass8_PFMET50_v8', 
        'HLT_DoubleEle8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT175_v4', 
        'HLT_DoubleEle8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT225_v4', 
        'HLT_DoubleEle8_CaloIdT_TrkIdVL_v12', 
        'HLT_Ele12_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_DoubleCentralJet65_v4', 
        'HLT_Ele12_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_RsqMR30_Rsq0p04_MR200_v4', 
        'HLT_Ele12_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_RsqMR40_Rsq0p04_MR200_v4', 
        'HLT_Ele30_CaloIdVT_TrkIdT_PFNoPUJet100_PFNoPUJet25_v8', 
        'HLT_Ele30_CaloIdVT_TrkIdT_PFNoPUJet150_PFNoPUJet25_v8', 
        'HLT_Ele8_CaloIdT_TrkIdT_DiJet30_v18', 
        'HLT_Ele8_CaloIdT_TrkIdT_QuadJet30_v18', 
        'HLT_Ele8_CaloIdT_TrkIdT_TriJet30_v18'),
    HTMHT = cms.vstring('HLT_HT250_AlphaT0p55_v8', 
        'HLT_HT250_AlphaT0p57_v8', 
        'HLT_HT300_AlphaT0p53_v8', 
        'HLT_HT300_AlphaT0p54_v14', 
        'HLT_HT350_AlphaT0p52_v8', 
        'HLT_HT350_AlphaT0p53_v19', 
        'HLT_HT400_AlphaT0p51_v19', 
        'HLT_HT400_AlphaT0p52_v14', 
        'HLT_HT450_AlphaT0p51_v14', 
        'HLT_PFNoPUHT350_PFMET100_v4', 
        'HLT_PFNoPUHT400_PFMET100_v4', 
        'HLT_RsqMR40_Rsq0p04_v6', 
        'HLT_RsqMR55_Rsq0p09_MR150_v6', 
        'HLT_RsqMR60_Rsq0p09_MR150_v6', 
        'HLT_RsqMR65_Rsq0p09_MR150_v5'),
    HLTPhysicsParked = cms.vstring('HLT_Physics_Parked_v1'),
    FEDMonitor = cms.vstring('HLT_DTErrors_v3'),
    NoBPTX = cms.vstring('HLT_JetE30_NoBPTX3BX_NoHalo_v16', 
        'HLT_JetE30_NoBPTX_v14', 
        'HLT_JetE50_NoBPTX3BX_NoHalo_v13', 
        'HLT_JetE70_NoBPTX3BX_NoHalo_v5', 
        'HLT_L2Mu10_NoVertex_NoBPTX3BX_NoHalo_v4', 
        'HLT_L2Mu20_NoVertex_2Cha_NoBPTX3BX_NoHalo_v1', 
        'HLT_L2Mu20_eta2p1_NoVertex_v2', 
        'HLT_L2Mu30_NoVertex_2Cha_NoBPTX3BX_NoHalo_v1'),
    SingleMu = cms.vstring('HLT_IsoMu17_eta2p1_CentralPFNoPUJet30_BTagIPIter_v4', 
        'HLT_IsoMu17_eta2p1_CentralPFNoPUJet30_v4', 
        'HLT_IsoMu17_eta2p1_DiCentralPFNoPUJet30_v4', 
        'HLT_IsoMu17_eta2p1_TriCentralPFNoPUJet30_v4', 
        'HLT_IsoMu17_eta2p1_TriCentralPFNoPUJet45_35_25_v2', 
        'HLT_IsoMu18_CentralPFJet30_CentralPFJet25_PFMET20_v1', 
        'HLT_IsoMu18_CentralPFJet30_CentralPFJet25_v1', 
        'HLT_IsoMu18_PFJet30_PFJet25_Deta3_CentralPFJet25_v1', 
        'HLT_IsoMu18_PFJet30_PFJet25_Deta3_v1', 
        'HLT_IsoMu20_WCandPt80_v4', 
        'HLT_IsoMu20_eta2p1_CentralPFJet80_v9', 
        'HLT_IsoMu20_eta2p1_v7', 
        'HLT_IsoMu24_eta2p1_v15', 
        'HLT_IsoMu24_v17', 
        'HLT_IsoMu30_eta2p1_v15', 
        'HLT_IsoMu30_v11', 
        'HLT_IsoMu34_eta2p1_v13', 
        'HLT_IsoMu40_eta2p1_v10', 
        'HLT_L2Mu70_2Cha_eta2p1_PFMET55_v2', 
        'HLT_L2Mu70_2Cha_eta2p1_PFMET60_v2', 
        'HLT_Mu12_eta2p1_DiCentral_20_v8', 
        'HLT_Mu12_eta2p1_DiCentral_40_20_BTagIP3D1stTrack_v8', 
        'HLT_Mu12_eta2p1_DiCentral_40_20_DiBTagIP3D1stTrack_v8', 
        'HLT_Mu12_eta2p1_DiCentral_40_20_v8', 
        'HLT_Mu12_eta2p1_L1Mu10erJetC12WdEtaPhi1DiJetsC_v7', 
        'HLT_Mu12_v18', 
        'HLT_Mu15_eta2p1_DiCentral_20_v1', 
        'HLT_Mu15_eta2p1_DiCentral_40_20_v1', 
        'HLT_Mu15_eta2p1_L1Mu10erJetC12WdEtaPhi1DiJetsC_v3', 
        'HLT_Mu15_eta2p1_TriCentral_40_20_20_BTagIP3D1stTrack_v8', 
        'HLT_Mu15_eta2p1_TriCentral_40_20_20_DiBTagIP3D1stTrack_v8', 
        'HLT_Mu15_eta2p1_TriCentral_40_20_20_v8', 
        'HLT_Mu15_eta2p1_v5', 
        'HLT_Mu17_eta2p1_CentralPFNoPUJet30_BTagIPIter_v4', 
        'HLT_Mu17_eta2p1_TriCentralPFNoPUJet45_35_25_v2', 
        'HLT_Mu18_CentralPFJet30_CentralPFJet25_v1', 
        'HLT_Mu18_PFJet30_PFJet25_Deta3_CentralPFJet25_v1', 
        'HLT_Mu24_eta2p1_v5', 
        'HLT_Mu24_v16', 
        'HLT_Mu30_eta2p1_v5', 
        'HLT_Mu30_v16', 
        'HLT_Mu40_eta2p1_Track50_dEdx3p6_v5', 
        'HLT_Mu40_eta2p1_Track60_dEdx3p7_v5', 
        'HLT_Mu40_eta2p1_v11', 
        'HLT_Mu40_v14', 
        'HLT_Mu50_eta2p1_v8', 
        'HLT_Mu5_v20', 
        'HLT_RelIso1p0Mu20_v3', 
        'HLT_RelIso1p0Mu5_v6'),
    SingleElectron = cms.vstring('HLT_Ele22_CaloIdL_CaloIsoVL_v6', 
        'HLT_Ele24_WP80_CentralPFJet35_CentralPFJet25_PFMET20_v1', 
        'HLT_Ele24_WP80_CentralPFJet35_CentralPFJet25_v1', 
        'HLT_Ele24_WP80_PFJet30_PFJet25_Deta3_CentralPFJet30_v1', 
        'HLT_Ele24_WP80_PFJet30_PFJet25_Deta3_v1', 
        'HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_CentralPFNoPUJet30_BTagIPIter_v9', 
        'HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_CentralPFNoPUJet30_v8', 
        'HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_DiCentralPFNoPUJet30_v2', 
        'HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30_v4', 
        'HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet45_35_25_v2', 
        'HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet50_40_30_v4', 
        'HLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_v11', 
        'HLT_Ele27_WP80_CentralPFJet80_v9', 
        'HLT_Ele27_WP80_PFMET_MT50_v7', 
        'HLT_Ele27_WP80_WCandPt80_v9', 
        'HLT_Ele27_WP80_v11', 
        'HLT_Ele30_CaloIdVT_TrkIdT_v6', 
        'HLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_v11', 
        'HLT_Ele80_CaloIdVT_GsfTrkIdT_v2', 
        'HLT_Ele90_CaloIdVT_GsfTrkIdT_v2'),
    JetMon = cms.vstring('HLT_DiPFJetAve140_v10', 
        'HLT_DiPFJetAve200_v10', 
        'HLT_DiPFJetAve260_v10', 
        'HLT_DiPFJetAve40_v9', 
        'HLT_DiPFJetAve80_v10', 
        'HLT_PFJet140_v9', 
        'HLT_PFJet200_v9', 
        'HLT_PFJet260_v9', 
        'HLT_PFJet40_v8', 
        'HLT_PFJet80_v9', 
        'HLT_SingleForJet15_v4', 
        'HLT_SingleForJet25_v4'),
    MuOnia = cms.vstring('HLT_Dimuon0_Jpsi_Muon_v18', 
        'HLT_Dimuon0_Jpsi_NoVertexing_v14', 
        'HLT_Dimuon0_Jpsi_v17', 
        'HLT_Dimuon0_PsiPrime_v6', 
        'HLT_Dimuon0_Upsilon_Muon_v18', 
        'HLT_Dimuon0_Upsilon_v17', 
        'HLT_Dimuon11_Upsilon_v6', 
        'HLT_Dimuon3p5_SameSign_v6', 
        'HLT_Dimuon7_Upsilon_v7', 
        'HLT_DoubleMu3_4_Dimuon5_Bs_Central_v5', 
        'HLT_DoubleMu3p5_4_Dimuon5_Bs_Central_v5', 
        'HLT_DoubleMu4_Dimuon7_Bs_Forward_v5', 
        'HLT_DoubleMu4_JpsiTk_Displaced_v6', 
        'HLT_DoubleMu4_Jpsi_Displaced_v12', 
        'HLT_Mu5_L2Mu3_Jpsi_v8', 
        'HLT_Mu5_Track2_Jpsi_v21', 
        'HLT_Mu5_Track3p5_Jpsi_v7', 
        'HLT_Mu7_Track7_Jpsi_v20', 
        'HLT_Tau2Mu_ItTrack_v7'),
    MuEG = cms.vstring('HLT_DoubleMu5_Ele8_CaloIdT_TrkIdVL_v16', 
        'HLT_DoubleMu8_Ele8_CaloIdT_TrkIdVL_v5', 
        'HLT_Mu17_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v9', 
        'HLT_Mu22_Photon22_CaloIdL_v7', 
        'HLT_Mu30_Ele30_CaloIdL_v8', 
        'HLT_Mu7_Ele7_CaloIdT_CaloIsoVL_v7', 
        'HLT_Mu8_DoubleEle8_CaloIdT_TrkIdVL_v7', 
        'HLT_Mu8_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v9', 
        'HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Ele8_CaloIdL_TrkIdVL_v7'),
    RPCMonitor = cms.vstring('AlCa_RPCMuonNoHits_v9', 
        'AlCa_RPCMuonNoTriggers_v9', 
        'AlCa_RPCMuonNormalisation_v9'),
    DataScouting = cms.vstring('DST_Ele8_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT250_v4', 
        'DST_HT250_v4', 
        'DST_L1HTT_Or_L1MultiJet_v4', 
        'DST_Mu5_HT250_v4'),
    DoublePhotonHighPt = cms.vstring('HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_v7', 
        'HLT_DoubleEle33_CaloIdL_v14', 
        'HLT_DoubleEle33_CaloIdT_v10', 
        'HLT_DoublePhoton40_CaloIdL_Rsq0p035_v6', 
        'HLT_DoublePhoton40_CaloIdL_Rsq0p06_v6', 
        'HLT_DoublePhoton48_HEVT_v8', 
        'HLT_DoublePhoton53_HEVT_v2', 
        'HLT_DoublePhoton70_v6', 
        'HLT_DoublePhoton80_v7'),
    ExpressPhysics = cms.vstring('HLT_DoublePhoton80_v7', 
        'HLT_EightJet30_eta3p0_v5', 
        'HLT_EightJet35_eta3p0_v5', 
        'HLT_MET400_v7', 
        'HLT_Mu17_Mu8_v22', 
        'HLT_Photon300_NoHE_v5', 
        'HLT_ZeroBias_v7'),
    BTag = cms.vstring('HLT_BTagMu_DiJet110_Mu5_v6', 
        'HLT_BTagMu_DiJet20_Mu5_v6', 
        'HLT_BTagMu_DiJet40_Mu5_v6', 
        'HLT_BTagMu_DiJet70_Mu5_v6', 
        'HLT_BTagMu_Jet300_Mu5_v6'),
    DoubleElectron = cms.vstring('HLT_DoubleEle10_CaloIdL_TrkIdVL_Ele10_CaloIdT_TrkIdVL_v12', 
        'HLT_Ele15_Ele8_Ele5_CaloIdL_TrkIdVL_v6', 
        'HLT_Ele17_CaloIdL_CaloIsoVL_v17', 
        'HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v19', 
        'HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Jet30_v7', 
        'HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v6', 
        'HLT_Ele17_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_Ele8_Mass50_v6', 
        'HLT_Ele20_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_SC4_Mass50_v7', 
        'HLT_Ele23_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_HFT30_v8', 
        'HLT_Ele27_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele15_CaloIdT_CaloIsoVL_trackless_v8', 
        'HLT_Ele27_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_HFT15_v8', 
        'HLT_Ele32_CaloIdT_CaloIsoT_TrkIdT_TrkIsoT_SC17_Mass50_v6', 
        'HLT_Ele5_SC5_Jpsi_Mass2to15_v4', 
        'HLT_Ele8_CaloIdL_CaloIsoVL_v17', 
        'HLT_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Jet30_v7', 
        'HLT_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v15', 
        'HLT_Ele8_CaloIdT_TrkIdVL_EG7_v2', 
        'HLT_Ele8_CaloIdT_TrkIdVL_Jet30_v7', 
        'HLT_Ele8_CaloIdT_TrkIdVL_v5', 
        'HLT_Photon22_R9Id90_HE10_Iso40_EBOnly_v5', 
        'HLT_Photon36_R9Id90_HE10_Iso40_EBOnly_v5', 
        'HLT_Photon50_R9Id90_HE10_Iso40_EBOnly_v5', 
        'HLT_Photon75_R9Id90_HE10_Iso40_EBOnly_v5', 
        'HLT_Photon90_R9Id90_HE10_Iso40_EBOnly_v5', 
        'HLT_TripleEle10_CaloIdL_TrkIdVL_v18'),
    HcalNZS = cms.vstring('HLT_HcalNZS_v10', 
        'HLT_HcalPhiSym_v11', 
        'HLT_HcalUTCA_v1'),
    TestEnablesEcalHcalDT = cms.vstring('HLT_DTCalibration_v2', 
        'HLT_EcalCalibration_v3', 
        'HLT_HcalCalibration_v3'),
    TauParked = cms.vstring('HLT_DoubleIsoL2Tau30_eta2p1_v1', 
        'HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_Jet30_v5', 
        'HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_Reg_Jet30_v1', 
        'HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_Reg_v1', 
        'HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_v4', 
        'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Prong1_Reg_v1', 
        'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Prong1_v4', 
        'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Reg_v1', 
        'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_v4', 
        'HLT_LooseIsoPFTau35_Trk20_Prong1_MET70_v10', 
        'HLT_LooseIsoPFTau35_Trk20_Prong1_MET75_v10', 
        'HLT_LooseIsoPFTau35_Trk20_Prong1_v10'),
    HTMHTParked = cms.vstring('HLT_HT200_AlphaT0p57_v8', 
        'HLT_HT250_AlphaT0p55_v8', 
        'HLT_HT250_AlphaT0p57_v8', 
        'HLT_HT300_AlphaT0p53_v8', 
        'HLT_HT300_AlphaT0p54_v14', 
        'HLT_HT350_AlphaT0p52_v8', 
        'HLT_HT350_AlphaT0p53_v19', 
        'HLT_HT400_AlphaT0p51_v19', 
        'HLT_HT400_AlphaT0p52_v14', 
        'HLT_HT450_AlphaT0p51_v14', 
        'HLT_PFNoPUHT350_PFMET100_v4', 
        'HLT_PFNoPUHT400_PFMET100_v4', 
        'HLT_RsqMR40_Rsq0p04_v6', 
        'HLT_RsqMR45_Rsq0p09_v5', 
        'HLT_RsqMR55_Rsq0p09_MR150_v6', 
        'HLT_RsqMR60_Rsq0p09_MR150_v6', 
        'HLT_RsqMR65_Rsq0p09_MR150_v5'),
    MuHad = cms.vstring('HLT_DoubleDisplacedMu4_DiPFJet40Neutral_v8', 
        'HLT_DoubleMu14_Mass8_PFMET40_v8', 
        'HLT_DoubleMu14_Mass8_PFMET50_v8', 
        'HLT_DoubleMu8_Mass8_PFNoPUHT175_v4', 
        'HLT_DoubleMu8_Mass8_PFNoPUHT225_v4', 
        'HLT_DoubleRelIso1p0Mu5_Mass8_PFNoPUHT175_v4', 
        'HLT_DoubleRelIso1p0Mu5_Mass8_PFNoPUHT225_v4', 
        'HLT_IsoMu12_DoubleCentralJet65_v4', 
        'HLT_IsoMu12_RsqMR30_Rsq0p04_MR200_v4', 
        'HLT_IsoMu12_RsqMR40_Rsq0p04_MR200_v4', 
        'HLT_IsoMu17_eta2p1_DiCentralPFNoPUJet30_PFNoPUHT350_PFMHT40_v3', 
        'HLT_L2TripleMu10_0_0_NoVertex_PFJet40Neutral_v8', 
        'HLT_Mu14_Ele14_CaloIdT_TrkIdVL_Mass8_PFMET40_v8', 
        'HLT_Mu14_Ele14_CaloIdT_TrkIdVL_Mass8_PFMET50_v8', 
        'HLT_Mu40_PFNoPUHT350_v4', 
        'HLT_Mu60_PFNoPUHT350_v4', 
        'HLT_Mu8_DiJet30_v7', 
        'HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT175_v4', 
        'HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT225_v4', 
        'HLT_Mu8_QuadJet30_v7', 
        'HLT_Mu8_TriJet30_v7', 
        'HLT_PFNoPUHT350_Mu15_PFMET45_v4', 
        'HLT_PFNoPUHT350_Mu15_PFMET50_v4', 
        'HLT_PFNoPUHT400_Mu5_PFMET45_v4', 
        'HLT_PFNoPUHT400_Mu5_PFMET50_v4', 
        'HLT_RelIso1p0Mu5_Ele8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT175_v4', 
        'HLT_RelIso1p0Mu5_Ele8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT225_v4'),
    BJetPlusX = cms.vstring('HLT_DiJet40Eta2p6_BTagIP3DFastPV_v7', 
        'HLT_DiJet80Eta2p6_BTagIP3DFastPVLoose_v7', 
        'HLT_DiPFJet80_DiPFJet30_BTagCSVd07d05_v5', 
        'HLT_DiPFJet80_DiPFJet30_BTagCSVd07d05d03_v5', 
        'HLT_DiPFJet80_DiPFJet30_BTagCSVd07d05d05_v5', 
        'HLT_Jet160Eta2p4_Jet120Eta2p4_DiBTagIP3DFastPVLoose_v7', 
        'HLT_Jet60Eta1p7_Jet53Eta1p7_DiBTagIP3DFastPV_v7', 
        'HLT_Jet80Eta1p7_Jet70Eta1p7_DiBTagIP3DFastPV_v7', 
        'HLT_L1DoubleJet36Central_v7', 
        'HLT_QuadJet75_55_35_20_BTagIP_VBF_v7', 
        'HLT_QuadJet75_55_35_20_VBF_v1', 
        'HLT_QuadJet75_55_38_20_BTagIP_VBF_v7', 
        'HLT_QuadPFJet78_61_44_31_BTagCSV_VBF_v6', 
        'HLT_QuadPFJet78_61_44_31_VBF_v1', 
        'HLT_QuadPFJet82_65_48_35_BTagCSV_VBF_v6'),
    ZeroBiasParked = cms.vstring('HLT_ZeroBias_Parked_v1'),
    OnlineMonitor = cms.vstring( ('HLT_Activity_Ecal_SC7_v13', 
        'HLT_BTagMu_DiJet110_Mu5_v6', 
        'HLT_BTagMu_DiJet20_Mu5_v6', 
        'HLT_BTagMu_DiJet40_Mu5_v6', 
        'HLT_BTagMu_DiJet70_Mu5_v6', 
        'HLT_BTagMu_Jet300_Mu5_v6', 
        'HLT_BeamGas_HF_Beam1_v5', 
        'HLT_BeamGas_HF_Beam2_v5', 
        'HLT_BeamHalo_v13', 
        'HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v3', 
        'HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v3', 
        'HLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT_v3', 
        'HLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT_v3', 
        'HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v3', 
        'HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v3', 
        'HLT_DTErrors_v3', 
        'HLT_DiCentralJetSumpT100_dPhi05_DiCentralPFJet60_25_PFMET100_HBHENoiseCleaned_v5', 
        'HLT_DiCentralPFJet30_PFMET80_BTagCSV07_v5', 
        'HLT_DiCentralPFJet30_PFMET80_v6', 
        'HLT_DiCentralPFNoPUJet50_PFMETORPFMETNoMu80_v4', 
        'HLT_DiJet40Eta2p6_BTagIP3DFastPV_v7', 
        'HLT_DiJet80Eta2p6_BTagIP3DFastPVLoose_v7', 
        'HLT_DiJet80_DiJet60_DiJet20_v6', 
        'HLT_DiPFJet40_PFMETnoMu65_MJJ600VBF_LeadingJets_v9', 
        'HLT_DiPFJet40_PFMETnoMu65_MJJ800VBF_AllJets_v9', 
        'HLT_DiPFJet80_DiPFJet30_BTagCSVd07d05_v5', 
        'HLT_DiPFJet80_DiPFJet30_BTagCSVd07d05d03_v5', 
        'HLT_DiPFJet80_DiPFJet30_BTagCSVd07d05d05_v5', 
        'HLT_DiPFJetAve140_v10', 
        'HLT_DiPFJetAve200_v10', 
        'HLT_DiPFJetAve260_v10', 
        'HLT_DiPFJetAve320_v10', 
        'HLT_DiPFJetAve400_v10', 
        'HLT_DiPFJetAve40_v9', 
        'HLT_DiPFJetAve80_v10', 
        'HLT_Dimuon0_Jpsi_Muon_v18', 
        'HLT_Dimuon0_Jpsi_NoVertexing_v14', 
        'HLT_Dimuon0_Jpsi_v17', 
        'HLT_Dimuon0_PsiPrime_v6', 
        'HLT_Dimuon0_Upsilon_Muon_v18', 
        'HLT_Dimuon0_Upsilon_v17', 
        'HLT_Dimuon11_Upsilon_v6', 
        'HLT_Dimuon3p5_SameSign_v6', 
        'HLT_Dimuon7_Upsilon_v7', 
        'HLT_DisplacedPhoton65EBOnly_CaloIdVL_IsoL_PFMET30_v4', 
        'HLT_DisplacedPhoton65_CaloIdVL_IsoL_PFMET25_v4', 
        'HLT_DoubleDisplacedMu4_DiPFJet40Neutral_v8', 
        'HLT_DoubleEle10_CaloIdL_TrkIdVL_Ele10_CaloIdT_TrkIdVL_v12', 
        'HLT_DoubleEle14_CaloIdT_TrkIdVL_Mass8_PFMET40_v8', 
        'HLT_DoubleEle14_CaloIdT_TrkIdVL_Mass8_PFMET50_v8', 
        'HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_v7', 
        'HLT_DoubleEle33_CaloIdL_v14', 
        'HLT_DoubleEle33_CaloIdT_v10', 
        'HLT_DoubleEle8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT175_v4', 
        'HLT_DoubleEle8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT225_v4', 
        'HLT_DoubleEle8_CaloIdT_TrkIdVL_v12', 
        'HLT_DoubleIsoL2Tau30_eta2p1_v1', 
        'HLT_DoubleJet20_ForwardBackward_v4', 
        'HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_Jet30_v5', 
        'HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_Reg_Jet30_v1', 
        'HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_Reg_v1', 
        'HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_v4', 
        'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Prong1_Reg_v1', 
        'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Prong1_v4', 
        'HLT_DoubleMu11_Acoplanarity03_v5', 
        'HLT_DoubleMu14_Mass8_PFMET40_v8', 
        'HLT_DoubleMu14_Mass8_PFMET50_v8', 
        'HLT_DoubleMu3_4_Dimuon5_Bs_Central_v5', 
        'HLT_DoubleMu3p5_4_Dimuon5_Bs_Central_v5', 
        'HLT_DoubleMu4_Acoplanarity03_v5', 
        'HLT_DoubleMu4_Dimuon7_Bs_Forward_v5', 
        'HLT_DoubleMu4_JpsiTk_Displaced_v6', 
        'HLT_DoubleMu4_Jpsi_Displaced_v12', 
        'HLT_DoubleMu5_Ele8_CaloIdT_TrkIdVL_v16', 
        'HLT_DoubleMu5_IsoMu5_v20', 
        'HLT_DoubleMu8_Ele8_CaloIdT_TrkIdVL_v5', 
        'HLT_DoubleMu8_Mass8_PFNoPUHT175_v4', 
        'HLT_DoubleMu8_Mass8_PFNoPUHT225_v4', 
        'HLT_DoublePhoton40_CaloIdL_Rsq0p035_v6', 
        'HLT_DoublePhoton40_CaloIdL_Rsq0p06_v6', 
        'HLT_DoublePhoton48_HEVT_v8', 
        'HLT_DoublePhoton53_HEVT_v2', 
        'HLT_DoublePhoton70_v6', 
        'HLT_DoublePhoton80_v7', 
        'HLT_DoubleRelIso1p0Mu5_Mass8_PFNoPUHT175_v4', 
        'HLT_DoubleRelIso1p0Mu5_Mass8_PFNoPUHT225_v4', 
        'HLT_EightJet30_eta3p0_v5', 
        'HLT_EightJet35_eta3p0_v5', 
        'HLT_Ele12_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_DoubleCentralJet65_v4', 
        'HLT_Ele12_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_RsqMR30_Rsq0p04_MR200_v4', 
        'HLT_Ele12_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_RsqMR40_Rsq0p04_MR200_v4', 
        'HLT_Ele13_eta2p1_WP90NoIso_LooseIsoPFTau20_L1ETM36_v1', 
        'HLT_Ele13_eta2p1_WP90Rho_LooseIsoPFTau20_L1ETM36_v1', 
        'HLT_Ele13_eta2p1_WP90Rho_LooseIsoPFTau20_v1', 
        'HLT_Ele15_Ele8_Ele5_CaloIdL_TrkIdVL_v6', 
        'HLT_Ele17_CaloIdL_CaloIsoVL_v17', 
        'HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v19', 
        'HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Jet30_v7', 
        'HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v6', 
        'HLT_Ele17_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_Ele8_Mass50_v6', 
        'HLT_Ele20_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_SC4_Mass50_v7', 
        'HLT_Ele22_CaloIdL_CaloIsoVL_v6', 
        'HLT_Ele22_eta2p1_WP90NoIso_LooseIsoPFTau20_v7', 
        'HLT_Ele22_eta2p1_WP90Rho_LooseIsoPFTau20_v7', 
        'HLT_Ele23_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_HFT30_v8', 
        'HLT_Ele24_WP80_CentralPFJet35_CentralPFJet25_PFMET20_v1', 
        'HLT_Ele24_WP80_CentralPFJet35_CentralPFJet25_v1', 
        'HLT_Ele24_WP80_PFJet30_PFJet25_Deta3_CentralPFJet30_v1', 
        'HLT_Ele24_WP80_PFJet30_PFJet25_Deta3_v1', 
        'HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_CentralPFNoPUJet30_BTagIPIter_v9', 
        'HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_CentralPFNoPUJet30_v8', 
        'HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_DiCentralPFNoPUJet30_v2', 
        'HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30_v4', 
        'HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet45_35_25_v2', 
        'HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet50_40_30_v4', 
        'HLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_v11', 
        'HLT_Ele27_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele15_CaloIdT_CaloIsoVL_trackless_v8', 
        'HLT_Ele27_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_HFT15_v8', 
        'HLT_Ele27_WP80_CentralPFJet80_v9', 
        'HLT_Ele27_WP80_PFMET_MT50_v7', 
        'HLT_Ele27_WP80_WCandPt80_v9', 
        'HLT_Ele27_WP80_v11', 
        'HLT_Ele30_CaloIdVT_TrkIdT_PFNoPUJet100_PFNoPUJet25_v8', 
        'HLT_Ele30_CaloIdVT_TrkIdT_PFNoPUJet150_PFNoPUJet25_v8', 
        'HLT_Ele30_CaloIdVT_TrkIdT_v6', 
        'HLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_v11', 
        'HLT_Ele32_CaloIdT_CaloIsoT_TrkIdT_TrkIsoT_SC17_Mass50_v6', 
        'HLT_Ele5_SC5_Jpsi_Mass2to15_v4', 
        'HLT_Ele80_CaloIdVT_GsfTrkIdT_v2', 
        'HLT_Ele8_CaloIdL_CaloIsoVL_v17', 
        'HLT_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Jet30_v7', 
        'HLT_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v15', 
        'HLT_Ele8_CaloIdT_TrkIdT_DiJet30_v18', 
        'HLT_Ele8_CaloIdT_TrkIdT_QuadJet30_v18', 
        'HLT_Ele8_CaloIdT_TrkIdT_TriJet30_v18', 
        'HLT_Ele8_CaloIdT_TrkIdVL_EG7_v2', 
        'HLT_Ele8_CaloIdT_TrkIdVL_Jet30_v7', 
        'HLT_Ele8_CaloIdT_TrkIdVL_v5', 
        'HLT_Ele90_CaloIdVT_GsfTrkIdT_v2', 
        'HLT_ExclDiJet35_HFAND_v4', 
        'HLT_ExclDiJet35_HFOR_v4', 
        'HLT_ExclDiJet80_HFAND_v4', 
        'HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v10', 
        'HLT_GlobalRunHPDNoise_v8', 
        'HLT_HT200_v6', 
        'HLT_HT250_AlphaT0p55_v8', 
        'HLT_HT250_AlphaT0p57_v8', 
        'HLT_HT250_v7', 
        'HLT_HT300_AlphaT0p53_v8', 
        'HLT_HT300_AlphaT0p54_v14', 
        'HLT_HT300_DoubleDisplacedPFJet60_ChgFraction10_v10', 
        'HLT_HT300_DoubleDisplacedPFJet60_v10', 
        'HLT_HT300_SingleDisplacedPFJet60_ChgFraction10_v10', 
        'HLT_HT300_SingleDisplacedPFJet60_v10', 
        'HLT_HT300_v7', 
        'HLT_HT350_AlphaT0p52_v8', 
        'HLT_HT350_AlphaT0p53_v19', 
        'HLT_HT350_v7', 
        'HLT_HT400_AlphaT0p51_v19', 
        'HLT_HT400_AlphaT0p52_v14', 
        'HLT_HT400_v7', 
        'HLT_HT450_AlphaT0p51_v14', 
        'HLT_HT450_v7', 
        'HLT_HT500_v7', 
        'HLT_HT550_v7', 
        'HLT_HT650_Track50_dEdx3p6_v10', 
        'HLT_HT650_Track60_dEdx3p7_v10', 
        'HLT_HT650_v7', 
        'HLT_HT750_v7', 
        'HLT_HcalNZS_v10', 
        'HLT_HcalPhiSym_v11', 
        'HLT_HcalUTCA_v1', 
        'HLT_IsoMu12_DoubleCentralJet65_v4', 
        'HLT_IsoMu12_RsqMR30_Rsq0p04_MR200_v4', 
        'HLT_IsoMu12_RsqMR40_Rsq0p04_MR200_v4', 
        'HLT_IsoMu15_eta2p1_L1ETM20_v7', 
        'HLT_IsoMu15_eta2p1_LooseIsoPFTau35_Trk20_Prong1_L1ETM20_v10', 
        'HLT_IsoMu17_eta2p1_CentralPFNoPUJet30_BTagIPIter_v4', 
        'HLT_IsoMu17_eta2p1_CentralPFNoPUJet30_v4', 
        'HLT_IsoMu17_eta2p1_DiCentralPFNoPUJet30_PFNoPUHT350_PFMHT40_v3', 
        'HLT_IsoMu17_eta2p1_DiCentralPFNoPUJet30_v4', 
        'HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v7', 
        'HLT_IsoMu17_eta2p1_TriCentralPFNoPUJet30_v4', 
        'HLT_IsoMu17_eta2p1_TriCentralPFNoPUJet45_35_25_v2', 
        'HLT_IsoMu18_CentralPFJet30_CentralPFJet25_PFMET20_v1', 
        'HLT_IsoMu18_CentralPFJet30_CentralPFJet25_v1', 
        'HLT_IsoMu18_PFJet30_PFJet25_Deta3_CentralPFJet25_v1', 
        'HLT_IsoMu18_PFJet30_PFJet25_Deta3_v1', 
        'HLT_IsoMu18_eta2p1_MediumIsoPFTau25_Trk1_eta2p1_Reg_v1', 
        'HLT_IsoMu18_eta2p1_MediumIsoPFTau25_Trk1_eta2p1_v4', 
        'HLT_IsoMu20_WCandPt80_v4', 
        'HLT_IsoMu20_eta2p1_CentralPFJet80_v9', 
        'HLT_IsoMu20_eta2p1_v7', 
        'HLT_IsoMu24_eta2p1_v15', 
        'HLT_IsoMu24_v17', 
        'HLT_IsoMu30_eta2p1_v15', 
        'HLT_IsoMu30_v11', 
        'HLT_IsoMu34_eta2p1_v13', 
        'HLT_IsoMu40_eta2p1_v10', 
        'HLT_IsoMu8_eta2p1_LooseIsoPFTau20_L1ETM26_v1', 
        'HLT_IsoMu8_eta2p1_LooseIsoPFTau20_v1', 
        'HLT_IsoTrackHB_v14', 
        'HLT_IsoTrackHE_v15', 
        'HLT_Jet160Eta2p4_Jet120Eta2p4_DiBTagIP3DFastPVLoose_v7', 
        'HLT_Jet370_NoJetID_v15', 
        'HLT_Jet60Eta1p7_Jet53Eta1p7_DiBTagIP3DFastPV_v7', 
        'HLT_Jet80Eta1p7_Jet70Eta1p7_DiBTagIP3DFastPV_v7', 
        'HLT_JetE30_NoBPTX3BX_NoHalo_v16', 
        'HLT_JetE30_NoBPTX_v14', 
        'HLT_JetE50_NoBPTX3BX_NoHalo_v13', 
        'HLT_JetE70_NoBPTX3BX_NoHalo_v5', 
        'HLT_L1DoubleEG3_FwdVeto_v2', 
        'HLT_L1DoubleJet36Central_v7', 
        'HLT_L1ETM100_v2', 
        'HLT_L1ETM30_v2', 
        'HLT_L1ETM40_v2', 
        'HLT_L1ETM70_v2', 
        'HLT_L1SingleEG12_v6', 
        'HLT_L1SingleEG5_v6', 
        'HLT_L1SingleJet16_v7', 
        'HLT_L1SingleJet36_v7', 
        'HLT_L1SingleMu12_v2', 
        'HLT_L1SingleMuOpen_AntiBPTX_v7', 
        'HLT_L1SingleMuOpen_v7', 
        'HLT_L1Tech_HBHEHO_totalOR_v6', 
        'HLT_L1Tech_HCAL_HF_single_channel_v4', 
        'HLT_L1TrackerCosmics_v7', 
        'HLT_L2DoubleMu23_NoVertex_2Cha_Angle2p5_v3', 
        'HLT_L2DoubleMu23_NoVertex_v11', 
        'HLT_L2DoubleMu38_NoVertex_2Cha_Angle2p5_v3', 
        'HLT_L2Mu10_NoVertex_NoBPTX3BX_NoHalo_v4', 
        'HLT_L2Mu20_NoVertex_2Cha_NoBPTX3BX_NoHalo_v1', 
        'HLT_L2Mu20_eta2p1_NoVertex_v2', 
        'HLT_L2Mu30_NoVertex_2Cha_NoBPTX3BX_NoHalo_v1', 
        'HLT_L2Mu70_2Cha_eta2p1_PFMET55_v2', 
        'HLT_L2Mu70_2Cha_eta2p1_PFMET60_v2', 
        'HLT_L2TripleMu10_0_0_NoVertex_PFJet40Neutral_v8', 
        'HLT_LooseIsoPFTau35_Trk20_Prong1_MET70_v10', 
        'HLT_LooseIsoPFTau35_Trk20_Prong1_MET75_v10', 
        'HLT_LooseIsoPFTau35_Trk20_Prong1_v10', 
        'HLT_MET120_HBHENoiseCleaned_v6', 
        'HLT_MET120_v13', 
        'HLT_MET200_HBHENoiseCleaned_v5', 
        'HLT_MET200_v12', 
        'HLT_MET300_HBHENoiseCleaned_v5', 
        'HLT_MET300_v4', 
        'HLT_MET400_HBHENoiseCleaned_v5', 
        'HLT_MET400_v7', 
        'HLT_MET80_Track50_dEdx3p6_v6', 
        'HLT_MET80_Track60_dEdx3p7_v6', 
        'HLT_MET80_v5', 
        'HLT_MonoCentralPFJet80_PFMETnoMu105_NHEF0p95_v4', 
        'HLT_Mu12_eta2p1_DiCentral_20_v8', 
        'HLT_Mu12_eta2p1_DiCentral_40_20_BTagIP3D1stTrack_v8', 
        'HLT_Mu12_eta2p1_DiCentral_40_20_DiBTagIP3D1stTrack_v8', 
        'HLT_Mu12_eta2p1_DiCentral_40_20_v8', 
        'HLT_Mu12_eta2p1_L1Mu10erJetC12WdEtaPhi1DiJetsC_v7', 
        'HLT_Mu12_v18', 
        'HLT_Mu13_Mu8_NoDZ_v1', 
        'HLT_Mu14_Ele14_CaloIdT_TrkIdVL_Mass8_PFMET40_v8', 
        'HLT_Mu14_Ele14_CaloIdT_TrkIdVL_Mass8_PFMET50_v8', 
        'HLT_Mu15_eta2p1_DiCentral_20_v1', 
        'HLT_Mu15_eta2p1_DiCentral_40_20_v1', 
        'HLT_Mu15_eta2p1_L1ETM20_v5', 
        'HLT_Mu15_eta2p1_L1Mu10erJetC12WdEtaPhi1DiJetsC_v3', 
        'HLT_Mu15_eta2p1_TriCentral_40_20_20_BTagIP3D1stTrack_v8', 
        'HLT_Mu15_eta2p1_TriCentral_40_20_20_DiBTagIP3D1stTrack_v8', 
        'HLT_Mu15_eta2p1_TriCentral_40_20_20_v8', 
        'HLT_Mu15_eta2p1_v5', 
        'HLT_Mu17_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v9', 
        'HLT_Mu17_Mu8_v22', 
        'HLT_Mu17_TkMu8_NoDZ_v1', 
        'HLT_Mu17_TkMu8_v14', 
        'HLT_Mu17_eta2p1_CentralPFNoPUJet30_BTagIPIter_v4', 
        'HLT_Mu17_eta2p1_LooseIsoPFTau20_v7', 
        'HLT_Mu17_eta2p1_TriCentralPFNoPUJet45_35_25_v2', 
        'HLT_Mu17_v5', 
        'HLT_Mu18_CentralPFJet30_CentralPFJet25_v1', 
        'HLT_Mu18_PFJet30_PFJet25_Deta3_CentralPFJet25_v1', 
        'HLT_Mu22_Photon22_CaloIdL_v7', 
        'HLT_Mu22_TkMu22_v9', 
        'HLT_Mu22_TkMu8_v9', 
        'HLT_Mu24_eta2p1_v5', 
        'HLT_Mu24_v16', 
        'HLT_Mu30_Ele30_CaloIdL_v8', 
        'HLT_Mu30_eta2p1_v5', 
        'HLT_Mu30_v16', 
        'HLT_Mu40_PFNoPUHT350_v4', 
        'HLT_Mu40_eta2p1_Track50_dEdx3p6_v5', 
        'HLT_Mu40_eta2p1_Track60_dEdx3p7_v5', 
        'HLT_Mu40_eta2p1_v11', 
        'HLT_Mu40_v14', 
        'HLT_Mu50_eta2p1_v8', 
        'HLT_Mu5_L2Mu3_Jpsi_v8', 
        'HLT_Mu5_Track2_Jpsi_v21', 
        'HLT_Mu5_Track3p5_Jpsi_v7', 
        'HLT_Mu5_v20', 
        'HLT_Mu60_PFNoPUHT350_v4', 
        'HLT_Mu7_Ele7_CaloIdT_CaloIsoVL_v7', 
        'HLT_Mu7_Track7_Jpsi_v20', 
        'HLT_Mu8_DiJet30_v7', 
        'HLT_Mu8_DoubleEle8_CaloIdT_TrkIdVL_v7', 
        'HLT_Mu8_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v9', 
        'HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Ele8_CaloIdL_TrkIdVL_v7', 
        'HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT175_v4', 
        'HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT225_v4', 
        'HLT_Mu8_QuadJet30_v7', 
        'HLT_Mu8_TriJet30_v7', 
        'HLT_Mu8_eta2p1_LooseIsoPFTau20_L1ETM26_v1', 
        'HLT_Mu8_v18', 
        'HLT_PFJet140_v9', 
        'HLT_PFJet200_v9', 
        'HLT_PFJet260_v9', 
        'HLT_PFJet320_v9', 
        'HLT_PFJet400_v9', 
        'HLT_PFJet40_v8', 
        'HLT_PFJet80_v9', 
        'HLT_PFMET150_v7', 
        'HLT_PFMET180_v7', 
        'HLT_PFNoPUHT350_Mu15_PFMET45_v4', 
        'HLT_PFNoPUHT350_Mu15_PFMET50_v4', 
        'HLT_PFNoPUHT350_PFMET100_v4', 
        'HLT_PFNoPUHT350_v4', 
        'HLT_PFNoPUHT400_Mu5_PFMET45_v4', 
        'HLT_PFNoPUHT400_Mu5_PFMET50_v4', 
        'HLT_PFNoPUHT400_PFMET100_v4', 
        'HLT_PFNoPUHT650_DiCentralPFNoPUJet80_CenPFNoPUJet40_v4', 
        'HLT_PFNoPUHT650_v4', 
        'HLT_PFNoPUHT700_v4', 
        'HLT_PFNoPUHT750_v4', 
        'HLT_Photon135_v7', 
        'HLT_Photon150_v4', 
        'HLT_Photon160_v4', 
        'HLT_Photon20_CaloIdVL_IsoL_v16', 
        'HLT_Photon20_CaloIdVL_v4', 
        'HLT_Photon22_R9Id90_HE10_Iso40_EBOnly_v5', 
        'HLT_Photon26_Photon18_v12', 
        'HLT_Photon26_R9Id85_OR_CaloId10_Iso50_Photon18_R9Id85_OR_CaloId10_Iso50_Mass70_v2', 
        'HLT_Photon26_R9Id85_OR_CaloId10_Iso50_Photon18_v5', 
        'HLT_Photon300_NoHE_v5', 
        'HLT_Photon30_CaloIdVL_v14', 
        'HLT_Photon36_CaloId10_Iso50_Photon22_CaloId10_Iso50_v6', 
        'HLT_Photon36_CaloId10_Iso50_Photon22_R9Id85_v6', 
        'HLT_Photon36_Photon22_v6', 
        'HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon10_R9Id85_OR_CaloId10_Iso50_Mass80_v1', 
        'HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon22_R9Id85_OR_CaloId10_Iso50_v6', 
        'HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon22_v5', 
        'HLT_Photon36_R9Id85_Photon22_CaloId10_Iso50_v6', 
        'HLT_Photon36_R9Id85_Photon22_R9Id85_v4', 
        'HLT_Photon36_R9Id90_HE10_Iso40_EBOnly_v5', 
        'HLT_Photon40_CaloIdL_RsqMR40_Rsq0p09_MR150_v6', 
        'HLT_Photon40_CaloIdL_RsqMR45_Rsq0p09_MR150_v6', 
        'HLT_Photon40_CaloIdL_RsqMR50_Rsq0p09_MR150_v6', 
        'HLT_Photon50_CaloIdVL_IsoL_v17', 
        'HLT_Photon50_CaloIdVL_v10', 
        'HLT_Photon50_R9Id90_HE10_Iso40_EBOnly_v5', 
        'HLT_Photon60_CaloIdL_HT300_v4', 
        'HLT_Photon60_CaloIdL_MHT70_v11', 
        'HLT_Photon70_CaloIdXL_PFMET100_v7', 
        'HLT_Photon70_CaloIdXL_PFNoPUHT400_v4', 
        'HLT_Photon70_CaloIdXL_PFNoPUHT500_v4', 
        'HLT_Photon75_CaloIdVL_v13', 
        'HLT_Photon75_R9Id90_HE10_Iso40_EBOnly_v5', 
        'HLT_Photon90_CaloIdVL_v10', 
        'HLT_Photon90_R9Id90_HE10_Iso40_EBOnly_v5', 
        'HLT_Physics_v5', 
        'HLT_PixelTracks_Multiplicity70_v3', 
        'HLT_PixelTracks_Multiplicity80_v12', 
        'HLT_PixelTracks_Multiplicity90_v3', 
        'HLT_QuadJet60_DiJet20_v6', 
        'HLT_QuadJet70_v6', 
        'HLT_QuadJet75_55_35_20_BTagIP_VBF_v7', 
        'HLT_QuadJet75_55_35_20_VBF_v1', 
        'HLT_QuadJet75_55_38_20_BTagIP_VBF_v7', 
        'HLT_QuadJet80_v6', 
        'HLT_QuadJet90_v6', 
        'HLT_QuadPFJet78_61_44_31_BTagCSV_VBF_v6', 
        'HLT_QuadPFJet78_61_44_31_VBF_v1', 
        'HLT_QuadPFJet82_65_48_35_BTagCSV_VBF_v6', 
        'HLT_Random_v2', 
        'HLT_RelIso1p0Mu20_v3', 
        'HLT_RelIso1p0Mu5_Ele8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT175_v4', 
        'HLT_RelIso1p0Mu5_Ele8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT225_v4', 
        'HLT_RelIso1p0Mu5_v6', 
        'HLT_RsqMR40_Rsq0p04_v6', 
        'HLT_RsqMR55_Rsq0p09_MR150_v6', 
        'HLT_RsqMR60_Rsq0p09_MR150_v6', 
        'HLT_RsqMR65_Rsq0p09_MR150_v5', 
        'HLT_SingleForJet15_v4', 
        'HLT_SingleForJet25_v4', 
        'HLT_SixJet35_v6', 
        'HLT_SixJet45_v6', 
        'HLT_SixJet50_v6', 
        'HLT_Tau2Mu_ItTrack_v7', 
        'HLT_TripleEle10_CaloIdL_TrkIdVL_v18', 
        'HLT_TripleMu5_v19', 
        'HLT_ZeroBiasPixel_DoubleTrack_v2', 
        'HLT_ZeroBias_v7' ) ),
    MultiJet1Parked = cms.vstring('HLT_DiJet80_DiJet60_DiJet20_v6', 
        'HLT_DoubleJet20_ForwardBackward_v4', 
        'HLT_EightJet30_eta3p0_v5', 
        'HLT_EightJet35_eta3p0_v5', 
        'HLT_ExclDiJet35_HFAND_v4', 
        'HLT_ExclDiJet35_HFOR_v4', 
        'HLT_ExclDiJet80_HFAND_v4', 
        'HLT_QuadJet45_v1', 
        'HLT_QuadJet50_v5', 
        'HLT_QuadJet60_DiJet20_v6', 
        'HLT_QuadJet70_v6', 
        'HLT_QuadJet80_v6', 
        'HLT_QuadJet90_v6', 
        'HLT_SixJet35_v6', 
        'HLT_SixJet45_v6', 
        'HLT_SixJet50_v6'),
    L1Accept = cms.vstring('DST_Physics_v5'),
    OnlineHltMonitor = cms.vstring('HLT_DiJet80_DiJet60_DiJet20_v6', 
        'HLT_DiPFJetAve140_v10', 
        'HLT_DiPFJetAve200_v10', 
        'HLT_DiPFJetAve260_v10', 
        'HLT_DiPFJetAve320_v10', 
        'HLT_DiPFJetAve400_v10', 
        'HLT_DiPFJetAve40_v9', 
        'HLT_DiPFJetAve80_v10', 
        'HLT_Ele22_CaloIdL_CaloIsoVL_v6', 
        'HLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_v11', 
        'HLT_Ele27_WP80_PFMET_MT50_v7', 
        'HLT_Ele27_WP80_v11', 
        'HLT_Ele30_CaloIdVT_TrkIdT_v6', 
        'HLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_v11', 
        'HLT_Ele80_CaloIdVT_GsfTrkIdT_v2', 
        'HLT_Ele90_CaloIdVT_GsfTrkIdT_v2', 
        'HLT_IsoMu20_eta2p1_v7', 
        'HLT_IsoMu24_eta2p1_v15', 
        'HLT_IsoMu30_eta2p1_v15', 
        'HLT_IsoMu34_eta2p1_v13', 
        'HLT_IsoMu40_eta2p1_v10', 
        'HLT_Jet370_NoJetID_v15', 
        'HLT_Mu12_v18', 
        'HLT_Mu15_eta2p1_v5', 
        'HLT_Mu17_v5', 
        'HLT_Mu24_eta2p1_v5', 
        'HLT_Mu30_eta2p1_v5', 
        'HLT_Mu40_eta2p1_Track50_dEdx3p6_v5', 
        'HLT_Mu40_eta2p1_Track60_dEdx3p7_v5', 
        'HLT_Mu40_eta2p1_v11', 
        'HLT_Mu5_v20', 
        'HLT_Mu8_v18', 
        'HLT_PFJet140_v9', 
        'HLT_PFJet200_v9', 
        'HLT_PFJet260_v9', 
        'HLT_PFJet320_v9', 
        'HLT_PFJet400_v9', 
        'HLT_PFJet40_v8', 
        'HLT_PFJet80_v9', 
        'HLT_RelIso1p0Mu20_v3', 
        'HLT_RelIso1p0Mu5_v6', 
        'HLT_SingleForJet15_v4', 
        'HLT_SingleForJet25_v4'),
    MinimumBias = cms.vstring('HLT_Physics_v5', 
        'HLT_PixelTracks_Multiplicity70_v3', 
        'HLT_PixelTracks_Multiplicity80_v12', 
        'HLT_PixelTracks_Multiplicity90_v3', 
        'HLT_Random_v2', 
        'HLT_ZeroBiasPixel_DoubleTrack_v2', 
        'HLT_ZeroBias_v7'),
    EcalLaser = cms.vstring('HLT_EcalCalibration_v3'),
    SinglePhoton = cms.vstring('HLT_DisplacedPhoton65EBOnly_CaloIdVL_IsoL_PFMET30_v4', 
        'HLT_DisplacedPhoton65_CaloIdVL_IsoL_PFMET25_v4', 
        'HLT_L1DoubleEG3_FwdVeto_v2', 
        'HLT_Photon135_v7', 
        'HLT_Photon150_v4', 
        'HLT_Photon160_v4', 
        'HLT_Photon20_CaloIdVL_IsoL_v16', 
        'HLT_Photon20_CaloIdVL_v4', 
        'HLT_Photon300_NoHE_v5', 
        'HLT_Photon30_CaloIdVL_v14', 
        'HLT_Photon50_CaloIdVL_IsoL_v17', 
        'HLT_Photon50_CaloIdVL_v10', 
        'HLT_Photon75_CaloIdVL_v13', 
        'HLT_Photon90_CaloIdVL_v10'),
    SinglePhotonParked = cms.vstring('HLT_DisplacedPhoton65EBOnly_CaloIdVL_IsoL_PFMET30_v4', 
        'HLT_DisplacedPhoton65_CaloIdVL_IsoL_PFMET25_v4', 
        'HLT_L1DoubleEG3_FwdVeto_v2', 
        'HLT_Photon135_v7', 
        'HLT_Photon150_v4', 
        'HLT_Photon160_v4', 
        'HLT_Photon20_CaloIdVL_IsoL_v16', 
        'HLT_Photon20_CaloIdVL_v4', 
        'HLT_Photon300_NoHE_v5', 
        'HLT_Photon30_CaloIdVL_v14', 
        'HLT_Photon30_R9Id90_CaloId_HE10_Iso40_EBOnly_Met25_HBHENoiseCleaned_v1', 
        'HLT_Photon30_R9Id90_CaloId_HE10_Iso40_EBOnly_v1', 
        'HLT_Photon30_v1', 
        'HLT_Photon50_CaloIdVL_IsoL_v17', 
        'HLT_Photon50_CaloIdVL_v10', 
        'HLT_Photon75_CaloIdVL_v13', 
        'HLT_Photon90_CaloIdVL_v10'),
    MultiJet = cms.vstring('HLT_DiJet80_DiJet60_DiJet20_v6', 
        'HLT_DoubleJet20_ForwardBackward_v4', 
        'HLT_EightJet30_eta3p0_v5', 
        'HLT_EightJet35_eta3p0_v5', 
        'HLT_ExclDiJet35_HFAND_v4', 
        'HLT_ExclDiJet35_HFOR_v4', 
        'HLT_ExclDiJet80_HFAND_v4', 
        'HLT_QuadJet60_DiJet20_v6', 
        'HLT_QuadJet70_v6', 
        'HLT_QuadJet80_v6', 
        'HLT_QuadJet90_v6', 
        'HLT_SixJet35_v6', 
        'HLT_SixJet45_v6', 
        'HLT_SixJet50_v6'),
    VBF1Parked = cms.vstring('HLT_DiJet20_MJJ650_AllJets_DEta3p5_HT120_VBF_v1', 
        'HLT_DiJet30_MJJ700_AllJets_DEta3p5_VBF_v1', 
        'HLT_DiJet35_MJJ650_AllJets_DEta3p5_VBF_v5', 
        'HLT_DiJet35_MJJ700_AllJets_DEta3p5_VBF_v5', 
        'HLT_DiJet35_MJJ750_AllJets_DEta3p5_VBF_v5'),
    TauPlusX = cms.vstring('HLT_Ele13_eta2p1_WP90NoIso_LooseIsoPFTau20_L1ETM36_v1', 
        'HLT_Ele13_eta2p1_WP90Rho_LooseIsoPFTau20_L1ETM36_v1', 
        'HLT_Ele13_eta2p1_WP90Rho_LooseIsoPFTau20_v1', 
        'HLT_Ele22_eta2p1_WP90NoIso_LooseIsoPFTau20_v7', 
        'HLT_Ele22_eta2p1_WP90Rho_LooseIsoPFTau20_v7', 
        'HLT_IsoMu15_eta2p1_L1ETM20_v7', 
        'HLT_IsoMu15_eta2p1_LooseIsoPFTau35_Trk20_Prong1_L1ETM20_v10', 
        'HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v7', 
        'HLT_IsoMu18_eta2p1_MediumIsoPFTau25_Trk1_eta2p1_Reg_v1', 
        'HLT_IsoMu18_eta2p1_MediumIsoPFTau25_Trk1_eta2p1_v4', 
        'HLT_IsoMu8_eta2p1_LooseIsoPFTau20_L1ETM26_v1', 
        'HLT_IsoMu8_eta2p1_LooseIsoPFTau20_v1', 
        'HLT_Mu15_eta2p1_L1ETM20_v5', 
        'HLT_Mu17_eta2p1_LooseIsoPFTau20_v7', 
        'HLT_Mu8_eta2p1_LooseIsoPFTau20_L1ETM26_v1'),
    ParkingMonitor = cms.vstring('HLT_BTagMu_Jet20_Mu4_v2', 
        'HLT_BTagMu_Jet60_Mu4_v2', 
        'HLT_DiJet20_MJJ650_AllJets_DEta3p5_HT120_VBF_v1', 
        'HLT_DiJet30_MJJ700_AllJets_DEta3p5_VBF_v1', 
        'HLT_DiJet35_MJJ650_AllJets_DEta3p5_VBF_v5', 
        'HLT_DiJet35_MJJ700_AllJets_DEta3p5_VBF_v5', 
        'HLT_DiJet35_MJJ750_AllJets_DEta3p5_VBF_v5', 
        'HLT_Dimuon10_Jpsi_v6', 
        'HLT_Dimuon5_PsiPrime_v6', 
        'HLT_Dimuon5_Upsilon_v6', 
        'HLT_Dimuon7_PsiPrime_v3', 
        'HLT_Dimuon8_Jpsi_v7', 
        'HLT_Dimuon8_Upsilon_v6', 
        'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Reg_v1', 
        'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_v4', 
        'HLT_DoubleMu3p5_LowMassNonResonant_Displaced_v6', 
        'HLT_DoubleMu3p5_LowMass_Displaced_v6', 
        'HLT_HT200_AlphaT0p57_v8', 
        'HLT_MET100_HBHENoiseCleaned_v1', 
        'HLT_MET80_Parked_v5', 
        'HLT_Mu13_Mu8_v22', 
        'HLT_Mu15_TkMu5_Onia_v1', 
        'HLT_Photon30_R9Id90_CaloId_HE10_Iso40_EBOnly_Met25_HBHENoiseCleaned_v1', 
        'HLT_Photon30_R9Id90_CaloId_HE10_Iso40_EBOnly_v1', 
        'HLT_Photon30_v1', 
        'HLT_Physics_Parked_v1', 
        'HLT_QuadJet45_v1', 
        'HLT_QuadJet50_v5', 
        'HLT_RsqMR45_Rsq0p09_v5', 
        'HLT_ZeroBias_Parked_v1'),
    DoubleMu = cms.vstring('HLT_DoubleMu11_Acoplanarity03_v5', 
        'HLT_DoubleMu4_Acoplanarity03_v5', 
        'HLT_DoubleMu5_IsoMu5_v20', 
        'HLT_L2DoubleMu23_NoVertex_2Cha_Angle2p5_v3', 
        'HLT_L2DoubleMu23_NoVertex_v11', 
        'HLT_L2DoubleMu38_NoVertex_2Cha_Angle2p5_v3', 
        'HLT_Mu13_Mu8_NoDZ_v1', 
        'HLT_Mu17_Mu8_v22', 
        'HLT_Mu17_TkMu8_NoDZ_v1', 
        'HLT_Mu17_TkMu8_v14', 
        'HLT_Mu17_v5', 
        'HLT_Mu22_TkMu22_v9', 
        'HLT_Mu22_TkMu8_v9', 
        'HLT_Mu8_v18', 
        'HLT_TripleMu5_v19'),
    AlCaPhiSym = cms.vstring('AlCa_EcalPhiSym_v13'),
    Tau = cms.vstring('HLT_DoubleIsoL2Tau30_eta2p1_v1', 
        'HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_Jet30_v5', 
        'HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_Reg_Jet30_v1', 
        'HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_Reg_v1', 
        'HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_v4', 
        'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Prong1_Reg_v1', 
        'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Prong1_v4', 
        'HLT_LooseIsoPFTau35_Trk20_Prong1_MET70_v10', 
        'HLT_LooseIsoPFTau35_Trk20_Prong1_MET75_v10', 
        'HLT_LooseIsoPFTau35_Trk20_Prong1_v10'),
    OfflineMonitor = cms.vstring( ('AlCa_EcalEtaEBonly_v6', 
        'AlCa_EcalEtaEEonly_v6', 
        'AlCa_EcalPhiSym_v13', 
        'AlCa_EcalPi0EBonly_v6', 
        'AlCa_EcalPi0EEonly_v6', 
        'AlCa_LumiPixels_Random_v1', 
        'AlCa_LumiPixels_ZeroBias_v4', 
        'AlCa_LumiPixels_v8', 
        'AlCa_RPCMuonNoHits_v9', 
        'AlCa_RPCMuonNoTriggers_v9', 
        'AlCa_RPCMuonNormalisation_v9', 
        'DST_Ele8_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT250_v4', 
        'DST_HT250_v4', 
        'DST_L1HTT_Or_L1MultiJet_v4', 
        'DST_Mu5_HT250_v4', 
        'HLT_Activity_Ecal_SC7_v13', 
        'HLT_BTagMu_DiJet110_Mu5_v6', 
        'HLT_BTagMu_DiJet20_Mu5_v6', 
        'HLT_BTagMu_DiJet40_Mu5_v6', 
        'HLT_BTagMu_DiJet70_Mu5_v6', 
        'HLT_BTagMu_Jet20_Mu4_v2', 
        'HLT_BTagMu_Jet300_Mu5_v6', 
        'HLT_BTagMu_Jet60_Mu4_v2', 
        'HLT_BeamGas_HF_Beam1_v5', 
        'HLT_BeamGas_HF_Beam2_v5', 
        'HLT_BeamHalo_v13', 
        'HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v3', 
        'HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v3', 
        'HLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT_v3', 
        'HLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT_v3', 
        'HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v3', 
        'HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v3', 
        'HLT_DTErrors_v3', 
        'HLT_DiCentralJetSumpT100_dPhi05_DiCentralPFJet60_25_PFMET100_HBHENoiseCleaned_v5', 
        'HLT_DiCentralPFJet30_PFMET80_BTagCSV07_v5', 
        'HLT_DiCentralPFJet30_PFMET80_v6', 
        'HLT_DiCentralPFNoPUJet50_PFMETORPFMETNoMu80_v4', 
        'HLT_DiJet20_MJJ650_AllJets_DEta3p5_HT120_VBF_v1', 
        'HLT_DiJet30_MJJ700_AllJets_DEta3p5_VBF_v1', 
        'HLT_DiJet35_MJJ650_AllJets_DEta3p5_VBF_v5', 
        'HLT_DiJet35_MJJ700_AllJets_DEta3p5_VBF_v5', 
        'HLT_DiJet35_MJJ750_AllJets_DEta3p5_VBF_v5', 
        'HLT_DiJet40Eta2p6_BTagIP3DFastPV_v7', 
        'HLT_DiJet80Eta2p6_BTagIP3DFastPVLoose_v7', 
        'HLT_DiJet80_DiJet60_DiJet20_v6', 
        'HLT_DiPFJet40_PFMETnoMu65_MJJ600VBF_LeadingJets_v9', 
        'HLT_DiPFJet40_PFMETnoMu65_MJJ800VBF_AllJets_v9', 
        'HLT_DiPFJet80_DiPFJet30_BTagCSVd07d05_v5', 
        'HLT_DiPFJet80_DiPFJet30_BTagCSVd07d05d03_v5', 
        'HLT_DiPFJet80_DiPFJet30_BTagCSVd07d05d05_v5', 
        'HLT_DiPFJetAve140_v10', 
        'HLT_DiPFJetAve200_v10', 
        'HLT_DiPFJetAve260_v10', 
        'HLT_DiPFJetAve320_v10', 
        'HLT_DiPFJetAve400_v10', 
        'HLT_DiPFJetAve40_v9', 
        'HLT_DiPFJetAve80_v10', 
        'HLT_Dimuon0_Jpsi_Muon_v18', 
        'HLT_Dimuon0_Jpsi_NoVertexing_v14', 
        'HLT_Dimuon0_Jpsi_v17', 
        'HLT_Dimuon0_PsiPrime_v6', 
        'HLT_Dimuon0_Upsilon_Muon_v18', 
        'HLT_Dimuon0_Upsilon_v17', 
        'HLT_Dimuon10_Jpsi_v6', 
        'HLT_Dimuon11_Upsilon_v6', 
        'HLT_Dimuon3p5_SameSign_v6', 
        'HLT_Dimuon5_PsiPrime_v6', 
        'HLT_Dimuon5_Upsilon_v6', 
        'HLT_Dimuon7_PsiPrime_v3', 
        'HLT_Dimuon7_Upsilon_v7', 
        'HLT_Dimuon8_Jpsi_v7', 
        'HLT_Dimuon8_Upsilon_v6', 
        'HLT_DisplacedPhoton65EBOnly_CaloIdVL_IsoL_PFMET30_v4', 
        'HLT_DisplacedPhoton65_CaloIdVL_IsoL_PFMET25_v4', 
        'HLT_DoubleDisplacedMu4_DiPFJet40Neutral_v8', 
        'HLT_DoubleEle10_CaloIdL_TrkIdVL_Ele10_CaloIdT_TrkIdVL_v12', 
        'HLT_DoubleEle14_CaloIdT_TrkIdVL_Mass8_PFMET40_v8', 
        'HLT_DoubleEle14_CaloIdT_TrkIdVL_Mass8_PFMET50_v8', 
        'HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_v7', 
        'HLT_DoubleEle33_CaloIdL_v14', 
        'HLT_DoubleEle33_CaloIdT_v10', 
        'HLT_DoubleEle8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT175_v4', 
        'HLT_DoubleEle8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT225_v4', 
        'HLT_DoubleEle8_CaloIdT_TrkIdVL_v12', 
        'HLT_DoubleIsoL2Tau30_eta2p1_v1', 
        'HLT_DoubleJet20_ForwardBackward_v4', 
        'HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_Jet30_v5', 
        'HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_Reg_Jet30_v1', 
        'HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_Reg_v1', 
        'HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_v4', 
        'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Prong1_Reg_v1', 
        'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Prong1_v4', 
        'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Reg_v1', 
        'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_v4', 
        'HLT_DoubleMu11_Acoplanarity03_v5', 
        'HLT_DoubleMu14_Mass8_PFMET40_v8', 
        'HLT_DoubleMu14_Mass8_PFMET50_v8', 
        'HLT_DoubleMu3_4_Dimuon5_Bs_Central_v5', 
        'HLT_DoubleMu3p5_4_Dimuon5_Bs_Central_v5', 
        'HLT_DoubleMu3p5_LowMassNonResonant_Displaced_v6', 
        'HLT_DoubleMu3p5_LowMass_Displaced_v6', 
        'HLT_DoubleMu4_Acoplanarity03_v5', 
        'HLT_DoubleMu4_Dimuon7_Bs_Forward_v5', 
        'HLT_DoubleMu4_JpsiTk_Displaced_v6', 
        'HLT_DoubleMu4_Jpsi_Displaced_v12', 
        'HLT_DoubleMu5_Ele8_CaloIdT_TrkIdVL_v16', 
        'HLT_DoubleMu5_IsoMu5_v20', 
        'HLT_DoubleMu8_Ele8_CaloIdT_TrkIdVL_v5', 
        'HLT_DoubleMu8_Mass8_PFNoPUHT175_v4', 
        'HLT_DoubleMu8_Mass8_PFNoPUHT225_v4', 
        'HLT_DoublePhoton40_CaloIdL_Rsq0p035_v6', 
        'HLT_DoublePhoton40_CaloIdL_Rsq0p06_v6', 
        'HLT_DoublePhoton48_HEVT_v8', 
        'HLT_DoublePhoton53_HEVT_v2', 
        'HLT_DoublePhoton70_v6', 
        'HLT_DoublePhoton80_v7', 
        'HLT_DoubleRelIso1p0Mu5_Mass8_PFNoPUHT175_v4', 
        'HLT_DoubleRelIso1p0Mu5_Mass8_PFNoPUHT225_v4', 
        'HLT_EightJet30_eta3p0_v5', 
        'HLT_EightJet35_eta3p0_v5', 
        'HLT_Ele12_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_DoubleCentralJet65_v4', 
        'HLT_Ele12_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_RsqMR30_Rsq0p04_MR200_v4', 
        'HLT_Ele12_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_RsqMR40_Rsq0p04_MR200_v4', 
        'HLT_Ele13_eta2p1_WP90NoIso_LooseIsoPFTau20_L1ETM36_v1', 
        'HLT_Ele13_eta2p1_WP90Rho_LooseIsoPFTau20_L1ETM36_v1', 
        'HLT_Ele13_eta2p1_WP90Rho_LooseIsoPFTau20_v1', 
        'HLT_Ele15_Ele8_Ele5_CaloIdL_TrkIdVL_v6', 
        'HLT_Ele17_CaloIdL_CaloIsoVL_v17', 
        'HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v19', 
        'HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Jet30_v7', 
        'HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v6', 
        'HLT_Ele17_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_Ele8_Mass50_v6', 
        'HLT_Ele20_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_SC4_Mass50_v7', 
        'HLT_Ele22_CaloIdL_CaloIsoVL_v6', 
        'HLT_Ele22_eta2p1_WP90NoIso_LooseIsoPFTau20_v7', 
        'HLT_Ele22_eta2p1_WP90Rho_LooseIsoPFTau20_v7', 
        'HLT_Ele23_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_HFT30_v8', 
        'HLT_Ele24_WP80_CentralPFJet35_CentralPFJet25_PFMET20_v1', 
        'HLT_Ele24_WP80_CentralPFJet35_CentralPFJet25_v1', 
        'HLT_Ele24_WP80_PFJet30_PFJet25_Deta3_CentralPFJet30_v1', 
        'HLT_Ele24_WP80_PFJet30_PFJet25_Deta3_v1', 
        'HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_CentralPFNoPUJet30_BTagIPIter_v9', 
        'HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_CentralPFNoPUJet30_v8', 
        'HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_DiCentralPFNoPUJet30_v2', 
        'HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30_v4', 
        'HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet45_35_25_v2', 
        'HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet50_40_30_v4', 
        'HLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_v11', 
        'HLT_Ele27_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele15_CaloIdT_CaloIsoVL_trackless_v8', 
        'HLT_Ele27_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_HFT15_v8', 
        'HLT_Ele27_WP80_CentralPFJet80_v9', 
        'HLT_Ele27_WP80_PFMET_MT50_v7', 
        'HLT_Ele27_WP80_WCandPt80_v9', 
        'HLT_Ele27_WP80_v11', 
        'HLT_Ele30_CaloIdVT_TrkIdT_PFNoPUJet100_PFNoPUJet25_v8', 
        'HLT_Ele30_CaloIdVT_TrkIdT_PFNoPUJet150_PFNoPUJet25_v8', 
        'HLT_Ele30_CaloIdVT_TrkIdT_v6', 
        'HLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_v11', 
        'HLT_Ele32_CaloIdT_CaloIsoT_TrkIdT_TrkIsoT_SC17_Mass50_v6', 
        'HLT_Ele5_SC5_Jpsi_Mass2to15_v4', 
        'HLT_Ele80_CaloIdVT_GsfTrkIdT_v2', 
        'HLT_Ele8_CaloIdL_CaloIsoVL_v17', 
        'HLT_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Jet30_v7', 
        'HLT_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v15', 
        'HLT_Ele8_CaloIdT_TrkIdT_DiJet30_v18', 
        'HLT_Ele8_CaloIdT_TrkIdT_QuadJet30_v18', 
        'HLT_Ele8_CaloIdT_TrkIdT_TriJet30_v18', 
        'HLT_Ele8_CaloIdT_TrkIdVL_EG7_v2', 
        'HLT_Ele8_CaloIdT_TrkIdVL_Jet30_v7', 
        'HLT_Ele8_CaloIdT_TrkIdVL_v5', 
        'HLT_Ele90_CaloIdVT_GsfTrkIdT_v2', 
        'HLT_ExclDiJet35_HFAND_v4', 
        'HLT_ExclDiJet35_HFOR_v4', 
        'HLT_ExclDiJet80_HFAND_v4', 
        'HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v10', 
        'HLT_GlobalRunHPDNoise_v8', 
        'HLT_HT200_AlphaT0p57_v8', 
        'HLT_HT200_v6', 
        'HLT_HT250_AlphaT0p55_v8', 
        'HLT_HT250_AlphaT0p57_v8', 
        'HLT_HT250_v7', 
        'HLT_HT300_AlphaT0p53_v8', 
        'HLT_HT300_AlphaT0p54_v14', 
        'HLT_HT300_DoubleDisplacedPFJet60_ChgFraction10_v10', 
        'HLT_HT300_DoubleDisplacedPFJet60_v10', 
        'HLT_HT300_SingleDisplacedPFJet60_ChgFraction10_v10', 
        'HLT_HT300_SingleDisplacedPFJet60_v10', 
        'HLT_HT300_v7', 
        'HLT_HT350_AlphaT0p52_v8', 
        'HLT_HT350_AlphaT0p53_v19', 
        'HLT_HT350_v7', 
        'HLT_HT400_AlphaT0p51_v19', 
        'HLT_HT400_AlphaT0p52_v14', 
        'HLT_HT400_v7', 
        'HLT_HT450_AlphaT0p51_v14', 
        'HLT_HT450_v7', 
        'HLT_HT500_v7', 
        'HLT_HT550_v7', 
        'HLT_HT650_Track50_dEdx3p6_v10', 
        'HLT_HT650_Track60_dEdx3p7_v10', 
        'HLT_HT650_v7', 
        'HLT_HT750_v7', 
        'HLT_HcalCalibration_v3', 
        'HLT_HcalNZS_v10', 
        'HLT_HcalPhiSym_v11', 
        'HLT_HcalUTCA_v1', 
        'HLT_IsoMu12_DoubleCentralJet65_v4', 
        'HLT_IsoMu12_RsqMR30_Rsq0p04_MR200_v4', 
        'HLT_IsoMu12_RsqMR40_Rsq0p04_MR200_v4', 
        'HLT_IsoMu15_eta2p1_L1ETM20_v7', 
        'HLT_IsoMu15_eta2p1_LooseIsoPFTau35_Trk20_Prong1_L1ETM20_v10', 
        'HLT_IsoMu17_eta2p1_CentralPFNoPUJet30_BTagIPIter_v4', 
        'HLT_IsoMu17_eta2p1_CentralPFNoPUJet30_v4', 
        'HLT_IsoMu17_eta2p1_DiCentralPFNoPUJet30_PFNoPUHT350_PFMHT40_v3', 
        'HLT_IsoMu17_eta2p1_DiCentralPFNoPUJet30_v4', 
        'HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v7', 
        'HLT_IsoMu17_eta2p1_TriCentralPFNoPUJet30_v4', 
        'HLT_IsoMu17_eta2p1_TriCentralPFNoPUJet45_35_25_v2', 
        'HLT_IsoMu18_CentralPFJet30_CentralPFJet25_PFMET20_v1', 
        'HLT_IsoMu18_CentralPFJet30_CentralPFJet25_v1', 
        'HLT_IsoMu18_PFJet30_PFJet25_Deta3_CentralPFJet25_v1', 
        'HLT_IsoMu18_PFJet30_PFJet25_Deta3_v1', 
        'HLT_IsoMu18_eta2p1_MediumIsoPFTau25_Trk1_eta2p1_Reg_v1', 
        'HLT_IsoMu18_eta2p1_MediumIsoPFTau25_Trk1_eta2p1_v4', 
        'HLT_IsoMu20_WCandPt80_v4', 
        'HLT_IsoMu20_eta2p1_CentralPFJet80_v9', 
        'HLT_IsoMu20_eta2p1_v7', 
        'HLT_IsoMu24_eta2p1_v15', 
        'HLT_IsoMu24_v17', 
        'HLT_IsoMu30_eta2p1_v15', 
        'HLT_IsoMu30_v11', 
        'HLT_IsoMu34_eta2p1_v13', 
        'HLT_IsoMu40_eta2p1_v10', 
        'HLT_IsoMu8_eta2p1_LooseIsoPFTau20_L1ETM26_v1', 
        'HLT_IsoMu8_eta2p1_LooseIsoPFTau20_v1', 
        'HLT_IsoTrackHB_v14', 
        'HLT_IsoTrackHE_v15', 
        'HLT_Jet160Eta2p4_Jet120Eta2p4_DiBTagIP3DFastPVLoose_v7', 
        'HLT_Jet370_NoJetID_v15', 
        'HLT_Jet60Eta1p7_Jet53Eta1p7_DiBTagIP3DFastPV_v7', 
        'HLT_Jet80Eta1p7_Jet70Eta1p7_DiBTagIP3DFastPV_v7', 
        'HLT_JetE30_NoBPTX3BX_NoHalo_v16', 
        'HLT_JetE30_NoBPTX_v14', 
        'HLT_JetE50_NoBPTX3BX_NoHalo_v13', 
        'HLT_JetE70_NoBPTX3BX_NoHalo_v5', 
        'HLT_L1DoubleEG3_FwdVeto_v2', 
        'HLT_L1DoubleJet36Central_v7', 
        'HLT_L1ETM100_v2', 
        'HLT_L1ETM30_v2', 
        'HLT_L1ETM40_v2', 
        'HLT_L1ETM70_v2', 
        'HLT_L1SingleEG12_v6', 
        'HLT_L1SingleEG5_v6', 
        'HLT_L1SingleJet16_v7', 
        'HLT_L1SingleJet36_v7', 
        'HLT_L1SingleMu12_v2', 
        'HLT_L1SingleMuOpen_AntiBPTX_v7', 
        'HLT_L1SingleMuOpen_v7', 
        'HLT_L1Tech_HBHEHO_totalOR_v6', 
        'HLT_L1Tech_HCAL_HF_single_channel_v4', 
        'HLT_L1TrackerCosmics_v7', 
        'HLT_L2DoubleMu23_NoVertex_2Cha_Angle2p5_v3', 
        'HLT_L2DoubleMu23_NoVertex_v11', 
        'HLT_L2DoubleMu38_NoVertex_2Cha_Angle2p5_v3', 
        'HLT_L2Mu10_NoVertex_NoBPTX3BX_NoHalo_v4', 
        'HLT_L2Mu20_NoVertex_2Cha_NoBPTX3BX_NoHalo_v1', 
        'HLT_L2Mu20_eta2p1_NoVertex_v2', 
        'HLT_L2Mu30_NoVertex_2Cha_NoBPTX3BX_NoHalo_v1', 
        'HLT_L2Mu70_2Cha_eta2p1_PFMET55_v2', 
        'HLT_L2Mu70_2Cha_eta2p1_PFMET60_v2', 
        'HLT_L2TripleMu10_0_0_NoVertex_PFJet40Neutral_v8', 
        'HLT_LogMonitor_v4', 
        'HLT_LooseIsoPFTau35_Trk20_Prong1_MET70_v10', 
        'HLT_LooseIsoPFTau35_Trk20_Prong1_MET75_v10', 
        'HLT_LooseIsoPFTau35_Trk20_Prong1_v10', 
        'HLT_MET100_HBHENoiseCleaned_v1', 
        'HLT_MET120_HBHENoiseCleaned_v6', 
        'HLT_MET120_v13', 
        'HLT_MET200_HBHENoiseCleaned_v5', 
        'HLT_MET200_v12', 
        'HLT_MET300_HBHENoiseCleaned_v5', 
        'HLT_MET300_v4', 
        'HLT_MET400_HBHENoiseCleaned_v5', 
        'HLT_MET400_v7', 
        'HLT_MET80_Parked_v5', 
        'HLT_MET80_Track50_dEdx3p6_v6', 
        'HLT_MET80_Track60_dEdx3p7_v6', 
        'HLT_MET80_v5', 
        'HLT_MonoCentralPFJet80_PFMETnoMu105_NHEF0p95_v4', 
        'HLT_Mu12_eta2p1_DiCentral_20_v8', 
        'HLT_Mu12_eta2p1_DiCentral_40_20_BTagIP3D1stTrack_v8', 
        'HLT_Mu12_eta2p1_DiCentral_40_20_DiBTagIP3D1stTrack_v8', 
        'HLT_Mu12_eta2p1_DiCentral_40_20_v8', 
        'HLT_Mu12_eta2p1_L1Mu10erJetC12WdEtaPhi1DiJetsC_v7', 
        'HLT_Mu12_v18', 
        'HLT_Mu13_Mu8_NoDZ_v1', 
        'HLT_Mu13_Mu8_v22', 
        'HLT_Mu14_Ele14_CaloIdT_TrkIdVL_Mass8_PFMET40_v8', 
        'HLT_Mu14_Ele14_CaloIdT_TrkIdVL_Mass8_PFMET50_v8', 
        'HLT_Mu15_TkMu5_Onia_v1', 
        'HLT_Mu15_eta2p1_DiCentral_20_v1', 
        'HLT_Mu15_eta2p1_DiCentral_40_20_v1', 
        'HLT_Mu15_eta2p1_L1ETM20_v5', 
        'HLT_Mu15_eta2p1_L1Mu10erJetC12WdEtaPhi1DiJetsC_v3', 
        'HLT_Mu15_eta2p1_TriCentral_40_20_20_BTagIP3D1stTrack_v8', 
        'HLT_Mu15_eta2p1_TriCentral_40_20_20_DiBTagIP3D1stTrack_v8', 
        'HLT_Mu15_eta2p1_TriCentral_40_20_20_v8', 
        'HLT_Mu15_eta2p1_v5', 
        'HLT_Mu17_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v9', 
        'HLT_Mu17_Mu8_v22', 
        'HLT_Mu17_TkMu8_NoDZ_v1', 
        'HLT_Mu17_TkMu8_v14', 
        'HLT_Mu17_eta2p1_CentralPFNoPUJet30_BTagIPIter_v4', 
        'HLT_Mu17_eta2p1_LooseIsoPFTau20_v7', 
        'HLT_Mu17_eta2p1_TriCentralPFNoPUJet45_35_25_v2', 
        'HLT_Mu17_v5', 
        'HLT_Mu18_CentralPFJet30_CentralPFJet25_v1', 
        'HLT_Mu18_PFJet30_PFJet25_Deta3_CentralPFJet25_v1', 
        'HLT_Mu22_Photon22_CaloIdL_v7', 
        'HLT_Mu22_TkMu22_v9', 
        'HLT_Mu22_TkMu8_v9', 
        'HLT_Mu24_eta2p1_v5', 
        'HLT_Mu24_v16', 
        'HLT_Mu30_Ele30_CaloIdL_v8', 
        'HLT_Mu30_eta2p1_v5', 
        'HLT_Mu30_v16', 
        'HLT_Mu40_PFNoPUHT350_v4', 
        'HLT_Mu40_eta2p1_Track50_dEdx3p6_v5', 
        'HLT_Mu40_eta2p1_Track60_dEdx3p7_v5', 
        'HLT_Mu40_eta2p1_v11', 
        'HLT_Mu40_v14', 
        'HLT_Mu50_eta2p1_v8', 
        'HLT_Mu5_L2Mu3_Jpsi_v8', 
        'HLT_Mu5_Track2_Jpsi_v21', 
        'HLT_Mu5_Track3p5_Jpsi_v7', 
        'HLT_Mu5_v20', 
        'HLT_Mu60_PFNoPUHT350_v4', 
        'HLT_Mu7_Ele7_CaloIdT_CaloIsoVL_v7', 
        'HLT_Mu7_Track7_Jpsi_v20', 
        'HLT_Mu8_DiJet30_v7', 
        'HLT_Mu8_DoubleEle8_CaloIdT_TrkIdVL_v7', 
        'HLT_Mu8_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v9', 
        'HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Ele8_CaloIdL_TrkIdVL_v7', 
        'HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT175_v4', 
        'HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT225_v4', 
        'HLT_Mu8_QuadJet30_v7', 
        'HLT_Mu8_TriJet30_v7', 
        'HLT_Mu8_eta2p1_LooseIsoPFTau20_L1ETM26_v1', 
        'HLT_Mu8_v18', 
        'HLT_PFJet140_v9', 
        'HLT_PFJet200_v9', 
        'HLT_PFJet260_v9', 
        'HLT_PFJet320_v9', 
        'HLT_PFJet400_v9', 
        'HLT_PFJet40_v8', 
        'HLT_PFJet80_v9', 
        'HLT_PFMET150_v7', 
        'HLT_PFMET180_v7', 
        'HLT_PFNoPUHT350_Mu15_PFMET45_v4', 
        'HLT_PFNoPUHT350_Mu15_PFMET50_v4', 
        'HLT_PFNoPUHT350_PFMET100_v4', 
        'HLT_PFNoPUHT350_v4', 
        'HLT_PFNoPUHT400_Mu5_PFMET45_v4', 
        'HLT_PFNoPUHT400_Mu5_PFMET50_v4', 
        'HLT_PFNoPUHT400_PFMET100_v4', 
        'HLT_PFNoPUHT650_DiCentralPFNoPUJet80_CenPFNoPUJet40_v4', 
        'HLT_PFNoPUHT650_v4', 
        'HLT_PFNoPUHT700_v4', 
        'HLT_PFNoPUHT750_v4', 
        'HLT_Photon135_v7', 
        'HLT_Photon150_v4', 
        'HLT_Photon160_v4', 
        'HLT_Photon20_CaloIdVL_IsoL_v16', 
        'HLT_Photon20_CaloIdVL_v4', 
        'HLT_Photon22_R9Id90_HE10_Iso40_EBOnly_v5', 
        'HLT_Photon26_Photon18_v12', 
        'HLT_Photon26_R9Id85_OR_CaloId10_Iso50_Photon18_R9Id85_OR_CaloId10_Iso50_Mass70_v2', 
        'HLT_Photon26_R9Id85_OR_CaloId10_Iso50_Photon18_v5', 
        'HLT_Photon300_NoHE_v5', 
        'HLT_Photon30_CaloIdVL_v14', 
        'HLT_Photon30_R9Id90_CaloId_HE10_Iso40_EBOnly_Met25_HBHENoiseCleaned_v1', 
        'HLT_Photon30_R9Id90_CaloId_HE10_Iso40_EBOnly_v1', 
        'HLT_Photon30_v1', 
        'HLT_Photon36_CaloId10_Iso50_Photon22_CaloId10_Iso50_v6', 
        'HLT_Photon36_CaloId10_Iso50_Photon22_R9Id85_v6', 
        'HLT_Photon36_Photon22_v6', 
        'HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon10_R9Id85_OR_CaloId10_Iso50_Mass80_v1', 
        'HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon22_R9Id85_OR_CaloId10_Iso50_v6', 
        'HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon22_v5', 
        'HLT_Photon36_R9Id85_Photon22_CaloId10_Iso50_v6', 
        'HLT_Photon36_R9Id85_Photon22_R9Id85_v4', 
        'HLT_Photon36_R9Id90_HE10_Iso40_EBOnly_v5', 
        'HLT_Photon40_CaloIdL_RsqMR40_Rsq0p09_MR150_v6', 
        'HLT_Photon40_CaloIdL_RsqMR45_Rsq0p09_MR150_v6', 
        'HLT_Photon40_CaloIdL_RsqMR50_Rsq0p09_MR150_v6', 
        'HLT_Photon50_CaloIdVL_IsoL_v17', 
        'HLT_Photon50_CaloIdVL_v10', 
        'HLT_Photon50_R9Id90_HE10_Iso40_EBOnly_v5', 
        'HLT_Photon60_CaloIdL_HT300_v4', 
        'HLT_Photon60_CaloIdL_MHT70_v11', 
        'HLT_Photon70_CaloIdXL_PFMET100_v7', 
        'HLT_Photon70_CaloIdXL_PFNoPUHT400_v4', 
        'HLT_Photon70_CaloIdXL_PFNoPUHT500_v4', 
        'HLT_Photon75_CaloIdVL_v13', 
        'HLT_Photon75_R9Id90_HE10_Iso40_EBOnly_v5', 
        'HLT_Photon90_CaloIdVL_v10', 
        'HLT_Photon90_R9Id90_HE10_Iso40_EBOnly_v5', 
        'HLT_Physics_v5', 
        'HLT_PixelTracks_Multiplicity70_v3', 
        'HLT_PixelTracks_Multiplicity80_v12', 
        'HLT_PixelTracks_Multiplicity90_v3', 
        'HLT_QuadJet45_v1', 
        'HLT_QuadJet50_v5', 
        'HLT_QuadJet60_DiJet20_v6', 
        'HLT_QuadJet70_v6', 
        'HLT_QuadJet75_55_35_20_BTagIP_VBF_v7', 
        'HLT_QuadJet75_55_35_20_VBF_v1', 
        'HLT_QuadJet75_55_38_20_BTagIP_VBF_v7', 
        'HLT_QuadJet80_v6', 
        'HLT_QuadJet90_v6', 
        'HLT_QuadPFJet78_61_44_31_BTagCSV_VBF_v6', 
        'HLT_QuadPFJet78_61_44_31_VBF_v1', 
        'HLT_QuadPFJet82_65_48_35_BTagCSV_VBF_v6', 
        'HLT_Random_v2', 
        'HLT_RelIso1p0Mu20_v3', 
        'HLT_RelIso1p0Mu5_Ele8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT175_v4', 
        'HLT_RelIso1p0Mu5_Ele8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT225_v4', 
        'HLT_RelIso1p0Mu5_v6', 
        'HLT_RsqMR40_Rsq0p04_v6', 
        'HLT_RsqMR45_Rsq0p09_v5', 
        'HLT_RsqMR55_Rsq0p09_MR150_v6', 
        'HLT_RsqMR60_Rsq0p09_MR150_v6', 
        'HLT_RsqMR65_Rsq0p09_MR150_v5', 
        'HLT_SingleForJet15_v4', 
        'HLT_SingleForJet25_v4', 
        'HLT_SixJet35_v6', 
        'HLT_SixJet45_v6', 
        'HLT_SixJet50_v6', 
        'HLT_Tau2Mu_ItTrack_v7', 
        'HLT_TripleEle10_CaloIdL_TrkIdVL_v18', 
        'HLT_TripleMu5_v19', 
        'HLT_ZeroBiasPixel_DoubleTrack_v2', 
        'HLT_ZeroBias_v7' ) ),
    PhotonHad = cms.vstring('HLT_Photon40_CaloIdL_RsqMR40_Rsq0p09_MR150_v6', 
        'HLT_Photon40_CaloIdL_RsqMR45_Rsq0p09_MR150_v6', 
        'HLT_Photon40_CaloIdL_RsqMR50_Rsq0p09_MR150_v6', 
        'HLT_Photon60_CaloIdL_HT300_v4', 
        'HLT_Photon60_CaloIdL_MHT70_v11', 
        'HLT_Photon70_CaloIdXL_PFMET100_v7', 
        'HLT_Photon70_CaloIdXL_PFNoPUHT400_v4', 
        'HLT_Photon70_CaloIdXL_PFNoPUHT500_v4'),
    AlCaP0 = cms.vstring('AlCa_EcalEtaEBonly_v6', 
        'AlCa_EcalEtaEEonly_v6', 
        'AlCa_EcalPi0EBonly_v6', 
        'AlCa_EcalPi0EEonly_v6'),
    LogMonitor = cms.vstring('HLT_LogMonitor_v4'),
    METParked = cms.vstring('HLT_DiCentralJetSumpT100_dPhi05_DiCentralPFJet60_25_PFMET100_HBHENoiseCleaned_v5', 
        'HLT_DiCentralPFJet30_PFMET80_BTagCSV07_v5', 
        'HLT_DiCentralPFJet30_PFMET80_v6', 
        'HLT_DiCentralPFNoPUJet50_PFMETORPFMETNoMu80_v4', 
        'HLT_DiPFJet40_PFMETnoMu65_MJJ600VBF_LeadingJets_v9', 
        'HLT_DiPFJet40_PFMETnoMu65_MJJ800VBF_AllJets_v9', 
        'HLT_L1ETM100_v2', 
        'HLT_L1ETM30_v2', 
        'HLT_L1ETM40_v2', 
        'HLT_L1ETM70_v2', 
        'HLT_MET100_HBHENoiseCleaned_v1', 
        'HLT_MET120_HBHENoiseCleaned_v6', 
        'HLT_MET120_v13', 
        'HLT_MET200_HBHENoiseCleaned_v5', 
        'HLT_MET200_v12', 
        'HLT_MET300_HBHENoiseCleaned_v5', 
        'HLT_MET300_v4', 
        'HLT_MET400_HBHENoiseCleaned_v5', 
        'HLT_MET400_v7', 
        'HLT_MET80_Parked_v5', 
        'HLT_MonoCentralPFJet80_PFMETnoMu105_NHEF0p95_v4', 
        'HLT_PFMET150_v7', 
        'HLT_PFMET180_v7'),
    DoubleMuParked = cms.vstring('HLT_DoubleMu11_Acoplanarity03_v5', 
        'HLT_DoubleMu4_Acoplanarity03_v5', 
        'HLT_DoubleMu5_IsoMu5_v20', 
        'HLT_L2DoubleMu23_NoVertex_2Cha_Angle2p5_v3', 
        'HLT_L2DoubleMu23_NoVertex_v11', 
        'HLT_L2DoubleMu38_NoVertex_2Cha_Angle2p5_v3', 
        'HLT_Mu13_Mu8_NoDZ_v1', 
        'HLT_Mu13_Mu8_v22', 
        'HLT_Mu17_Mu8_v22', 
        'HLT_Mu17_TkMu8_NoDZ_v1', 
        'HLT_Mu17_TkMu8_v14', 
        'HLT_Mu17_v5', 
        'HLT_Mu22_TkMu22_v9', 
        'HLT_Mu22_TkMu8_v9', 
        'HLT_Mu8_v18', 
        'HLT_TripleMu5_v19'),
    AlCaLumiPixels = cms.vstring('AlCa_LumiPixels_Random_v1', 
        'AlCa_LumiPixels_ZeroBias_v4', 
        'AlCa_LumiPixels_v8'),
    MET = cms.vstring('HLT_DiCentralJetSumpT100_dPhi05_DiCentralPFJet60_25_PFMET100_HBHENoiseCleaned_v5', 
        'HLT_DiCentralPFJet30_PFMET80_BTagCSV07_v5', 
        'HLT_DiCentralPFJet30_PFMET80_v6', 
        'HLT_DiCentralPFNoPUJet50_PFMETORPFMETNoMu80_v4', 
        'HLT_DiPFJet40_PFMETnoMu65_MJJ600VBF_LeadingJets_v9', 
        'HLT_DiPFJet40_PFMETnoMu65_MJJ800VBF_AllJets_v9', 
        'HLT_L1ETM100_v2', 
        'HLT_L1ETM30_v2', 
        'HLT_L1ETM40_v2', 
        'HLT_L1ETM70_v2', 
        'HLT_MET120_HBHENoiseCleaned_v6', 
        'HLT_MET120_v13', 
        'HLT_MET200_HBHENoiseCleaned_v5', 
        'HLT_MET200_v12', 
        'HLT_MET300_HBHENoiseCleaned_v5', 
        'HLT_MET300_v4', 
        'HLT_MET400_HBHENoiseCleaned_v5', 
        'HLT_MET400_v7', 
        'HLT_MonoCentralPFJet80_PFMETnoMu105_NHEF0p95_v4', 
        'HLT_PFMET150_v7', 
        'HLT_PFMET180_v7'),
    TestEnablesTracker = cms.vstring('HLT_TrackerCalibration_v3'),
    Commissioning = cms.vstring('HLT_Activity_Ecal_SC7_v13', 
        'HLT_BeamGas_HF_Beam1_v5', 
        'HLT_BeamGas_HF_Beam2_v5', 
        'HLT_IsoTrackHB_v14', 
        'HLT_IsoTrackHE_v15', 
        'HLT_L1SingleEG12_v6', 
        'HLT_L1SingleEG5_v6', 
        'HLT_L1SingleJet16_v7', 
        'HLT_L1SingleJet36_v7', 
        'HLT_L1SingleMu12_v2', 
        'HLT_L1SingleMuOpen_v7'),
    DoublePhoton = cms.vstring('HLT_Photon26_Photon18_v12', 
        'HLT_Photon26_R9Id85_OR_CaloId10_Iso50_Photon18_R9Id85_OR_CaloId10_Iso50_Mass70_v2', 
        'HLT_Photon26_R9Id85_OR_CaloId10_Iso50_Photon18_v5', 
        'HLT_Photon36_CaloId10_Iso50_Photon22_CaloId10_Iso50_v6', 
        'HLT_Photon36_CaloId10_Iso50_Photon22_R9Id85_v6', 
        'HLT_Photon36_Photon22_v6', 
        'HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon10_R9Id85_OR_CaloId10_Iso50_Mass80_v1', 
        'HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon22_R9Id85_OR_CaloId10_Iso50_v6', 
        'HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon22_v5', 
        'HLT_Photon36_R9Id85_Photon22_CaloId10_Iso50_v6', 
        'HLT_Photon36_R9Id85_Photon22_R9Id85_v4'),
    Cosmics = cms.vstring('HLT_BeamHalo_v13', 
        'HLT_L1SingleMuOpen_AntiBPTX_v7', 
        'HLT_L1TrackerCosmics_v7')
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)

process.streams = cms.PSet(
    A = cms.vstring('BJetPlusX', 
        'BTag', 
        'Commissioning', 
        'Cosmics', 
        'DoubleElectron', 
        'DoubleMu', 
        'DoubleMuParked', 
        'DoublePhoton', 
        'DoublePhotonHighPt', 
        'ElectronHad', 
        'FEDMonitor', 
        'HLTPhysicsParked', 
        'HTMHT', 
        'HTMHTParked', 
        'HcalHPDNoise', 
        'HcalNZS', 
        'JetHT', 
        'JetMon', 
        'LogMonitor', 
        'MET', 
        'METParked', 
        'MinimumBias', 
        'MuEG', 
        'MuHad', 
        'MuOnia', 
        'MuOniaParked', 
        'MultiJet', 
        'MultiJet1Parked', 
        'NoBPTX', 
        'PhotonHad', 
        'SingleElectron', 
        'SingleMu', 
        'SinglePhoton', 
        'SinglePhotonParked', 
        'Tau', 
        'TauParked', 
        'TauPlusX', 
        'VBF1Parked', 
        'ZeroBiasParked'),
    B = cms.vstring('ParkingMonitor'),
    HLTDQM = cms.vstring('OnlineHltMonitor'),
    ALCAP0 = cms.vstring('AlCaP0'),
    Calibration = cms.vstring('TestEnablesEcalHcalDT'),
    Express = cms.vstring('ExpressPhysics'),
    NanoDST = cms.vstring('L1Accept'),
    ALCALUMIPIXELS = cms.vstring('AlCaLumiPixels'),
    RPCMON = cms.vstring('RPCMonitor'),
    HLTMON = cms.vstring('OfflineMonitor'),
    DQM = cms.vstring('OnlineMonitor'),
    TrackerCalibration = cms.vstring('TestEnablesTracker'),
    PhysicsDST = cms.vstring('DataScouting'),
    EcalCalibration = cms.vstring('EcalLaser'),
    ALCAPHISYM = cms.vstring('AlCaPhiSym')
)


