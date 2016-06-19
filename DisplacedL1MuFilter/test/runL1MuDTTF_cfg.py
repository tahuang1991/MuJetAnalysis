import FWCore.ParameterSet.Config as cms

process = cms.Process("L1MuDTTF")

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'PH2_1K_FB_V3::All', '')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorOpposite_cfi')
process.load('TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorAlong_cfi')
process.load('TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorAny_cfi')
process.load('Configuration.Geometry.GeometryExtended2023TTIReco_cff')
process.load('Geometry.TrackerGeometryBuilder.StackedTrackerGeometry_cfi')
process.load('Configuration.Geometry.GeometryExtended2023TTI_cff')

process.load('Configuration.StandardSequences.L1Reco_cff')
process.load("SLHCUpgradeSimulations.L1TrackTrigger.L1TkMuonSequence_cfi")
#process.pMuons = cms.Path( process.L1TkMuons ) #process.l1extraParticles + 
process.load("L1Trigger.TrackTrigger.TrackTrigger_cff")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)

"""
Slava's datasets:

/Neutrino_Pt2to20_gun/slava77-TTI2023Upg14D-PU140bx25-ILT_SLHC14-6a6577f18a9b70d924bea399af3ff625/USER
/SingleMuMinusFlatPt0p2To150/slava77-TTI2023Upg14D-PU140bx25-ILT_SLHC14-6a6577f18a9b70d924bea399af3ff625/USER
/SingleMuPlusFlatPt0p2To150/slava77-TTI2023Upg14D-PU140bx25-ILT_SLHC14-6a6577f18a9b70d924bea399af3ff625/USER
"""
from MuJetAnalysis.DisplacedL1MuFilter.Neutrino_Pt2to20_gun_TTI2023Upg14D_PU140bx25_ILT_SLHC14 import files
#from MuJetAnalysis.DisplacedL1MuFilter.SingleMuPlusFlatPt0p2To150_TTI2023Upg14D_PU140bx25_ILT_SLHC14 import files
#from MuJetAnalysis.DisplacedL1MuFilter.DarkSUSY_mH_125_mGammaD_20000_ctau_50_14TeV import files
#from MuJetAnalysis.DisplacedL1MuFilter.DarkSUSY_mH_125_mGammaD_20000_ctau_100_14TeV import files
from MuJetAnalysis.DisplacedL1MuFilter.DarkSUSY_mH_125_mGammaD_20000_ctau_1000_14TeV import files
#from MuJetAnalysis.DisplacedL1MuFilter.DarkSUSY_mH_125_mGammaD_20000_ctau_10_14TeV import files
#from MuJetAnalysis.DisplacedL1MuFilter.DarkSUSY_mH_125_mGammaD_20000_ctau_50_14TeV_PU140 import files
#from MuJetAnalysis.DisplacedL1MuFilter.DarkSUSY_mH_125_mGammaD_20000_ctau_100_14TeV_PU140 import files
from MuJetAnalysis.DisplacedL1MuFilter.DarkSUSY_mH_125_mGammaD_20000_ctau_1000_14TeV_PU140 import files
#from MuJetAnalysis.DisplacedL1MuFilter.DarkSUSY_mH_125_mGammaD_0400_ctau_0_14TeV import files

process.source = cms.Source(
    "PoolSource",
    fileNames = cms.untracked.vstring(*files)
    #fileNames = cms.untracked.vstring('/store/mc/TP2023HGCALDR/DarkSUSY_MH-125_MGammaD-20000_ctau1000_14TeV_madgraph-pythia6-tauola/GEN-SIM-DIGI-RAW/HGCALForMUO_PU140BX25_newsplit_PH2_1K_FB_V6-v2/40000/0097F2D6-523D-E511-BA2B-0025907254C8.root')
    #fileNames = cms.untracked.vstring("file:filter.root")
)


process.dump=cms.EDAnalyzer('EventContentAnalyzer')
#process.l1extraParticles + + process.dump
#process.p = cms.Path(process.l1extraParticles + process.L1TkMuons  + process.dump + process.DisplacedL1MuFilter_PhaseIIGE21)

process.TFileService = cms.Service(
    "TFileService",
    #fileName = cms.string("out_filter_ana_Neutrino_Pt2to20_gun_TTI2023Upg14D_PU140bx25_ILT_SLHC14.root")
#    fileName = cms.string("out_filter_ana_DarkSUSY_mH_125_mGammaD_20000_ctau_1000_14TeV_PU140_L1TkdR0p12.root")
#    fileName = cms.string("out_filter_ana_DarkSUSY_mH_125_mGammaD_20000_ctau_1000_14TeV_PU140.test.root")
    #fileName = cms.string("out_filter_ana_DarkSUSY_mH_125_mGammaD_20000_ctau_1000_14TeV_PU0.root")
    #fileName = cms.string("out_filter_ana_DarkSUSY_mH_125_mGammaD_20000_ctau_1000_14TeV_PU140.root")
    fileName = cms.string("out_ana.root")
)


#process.p = cms.Path(process.TrackTriggerClustersStubs * process.TrackTriggerTTTracks)
process.load('L1Trigger.DTTrackFinder.dttfDigis_cfi')
process.dttfDigis.DTDigi_Source = "simDtTriggerPrimitiveDigis"
process.dttfDigis.CSCStub_Source = "simCsctfTrackDigis"
process.p = cms.Path(process.dttfDigis)
# * process.dump * process.DisplacedL1MuFilter_PhaseIIGE21
#process.p.remove(process.L1TkMuonsDTSequence)

process.out = cms.OutputModule("PoolOutputModule",
   fileName = cms.untracked.string('file:out_DTTF.root'),
#                               SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('p')),
)

process.endpath1 = cms.EndPath(process.out)
