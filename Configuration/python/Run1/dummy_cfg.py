# Import configurations
import FWCore.ParameterSet.Config as cms

process = cms.Process("TEST")

# this inputs the input files
#process.maxEvents = cms.untracked.int32(-1)
process.source = cms.Source( "PoolSource",
    fileNames = cms.untracked.vstring(
    'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_RAW/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_RECO/d3ab0667c6cb6bf77e14d12c3b05fdd8/out_reco_1_1_zD1.root',
    'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_RAW/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_RECO/d3ab0667c6cb6bf77e14d12c3b05fdd8/out_reco_2_1_aZw.root',
    'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_RAW/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_RECO/d3ab0667c6cb6bf77e14d12c3b05fdd8/out_reco_3_2_kUn.root',
    'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_RAW/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_RECO/d3ab0667c6cb6bf77e14d12c3b05fdd8/out_reco_4_1_Uax.root',
    'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_RAW/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_RECO/d3ab0667c6cb6bf77e14d12c3b05fdd8/out_reco_5_1_L1V.root',
    'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_RAW/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_RECO/d3ab0667c6cb6bf77e14d12c3b05fdd8/out_reco_6_1_ZRD.root',
    'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_RAW/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_RECO/d3ab0667c6cb6bf77e14d12c3b05fdd8/out_reco_7_2_7Fe.root',
    'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_RAW/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_RECO/d3ab0667c6cb6bf77e14d12c3b05fdd8/out_reco_8_1_WKA.root',
    'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_RAW/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_RECO/d3ab0667c6cb6bf77e14d12c3b05fdd8/out_reco_9_1_V7J.root',
    'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_RAW/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_RECO/d3ab0667c6cb6bf77e14d12c3b05fdd8/out_reco_10_1_KgO.root',
    'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_RAW/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_RECO/d3ab0667c6cb6bf77e14d12c3b05fdd8/out_reco_11_1_xrL.root'
    ),
    eventsToProcess = cms.untracked.VEventRange('1:14:13040','1:16:15372','1:16:15709','1:17:16603','1:20:19658','1:22:21455','1:25:24573','1:26:25087','1:29:28574','1:30:29075','1:36:35515','1:37:36373','1:40:39026','1:40:39572','1:46:45360','1:46:45652','1:47:46764','1:50:49658','1:50:49850','1:51:50377','1:54:53222','1:55:54166','1:56:55116','1:60:59892','1:61:60354','1:61:60893','1:63:62246','1:64:63046','1:64:63887','1:68:67335','1:68:67690','1:68:67938','1:69:68381','1:73:72927','1:75:74852','1:79:78850','1:5:4508','1:7:6500'),
    secondaryFileNames = cms.untracked.vstring(
    ),
    inputCommands = cms.untracked.vstring(
        'keep *'
    )
)

# talk to output module
process.out = cms.OutputModule("PoolOutputModule",
                               fileName = cms.untracked.string("DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_hltL3fL1DoubleMu10MuOpenOR3p5L1f0L2f10L3Filtered17fail.root")
                               )

# define output path
process.p = cms.EndPath(process.out)
