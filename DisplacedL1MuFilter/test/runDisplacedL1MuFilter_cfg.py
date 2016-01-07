import FWCore.ParameterSet.Config as cms

process = cms.Process("test")
process.load("MuJetAnalysis.DisplacedL1MuFilter.DisplacedL1MuFilter_cfi")
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'PH2_1K_FB_V3::All', '')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorOpposite_cfi')
process.load('TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorAlong_cfi')

process.load('Configuration.Geometry.GeometryExtended2023TTIReco_cff')
process.load('Geometry.TrackerGeometryBuilder.StackedTrackerGeometry_cfi')
process.load('Configuration.Geometry.GeometryExtended2023TTI_cff')

process.load('Configuration.StandardSequences.L1Reco_cff')
#process.load("SLHCUpgradeSimulations.L1TrackTrigger.L1TkMuonSequence_cfi")
#process.pMuons = cms.Path( process.l1extraParticles + process.L1TkMuons )

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100000)
)

"""
Slava's datasets:

/Neutrino_Pt2to20_gun/slava77-TTI2023Upg14D-PU140bx25-ILT_SLHC14-6a6577f18a9b70d924bea399af3ff625/USER
/SingleMuMinusFlatPt0p2To150/slava77-TTI2023Upg14D-PU140bx25-ILT_SLHC14-6a6577f18a9b70d924bea399af3ff625/USER
/SingleMuPlusFlatPt0p2To150/slava77-TTI2023Upg14D-PU140bx25-ILT_SLHC14-6a6577f18a9b70d924bea399af3ff625/USER
"""
from MuJetAnalysis.DisplacedL1MuFilter.Neutrino_Pt2to20_gun_TTI2023Upg14D_PU140bx25_ILT_SLHC14 import files
#from MuJetAnalysis.DisplacedL1MuFilter.SingleMuPlusFlatPt0p2To150_TTI2023Upg14D_PU140bx25_ILT_SLHC14 import files
from MuJetAnalysis.DisplacedL1MuFilter.DarkSUSY_mH_125_mGammaD_20000_ctau_50_14TeV import files
from MuJetAnalysis.DisplacedL1MuFilter.DarkSUSY_mH_125_mGammaD_20000_ctau_50_14TeV_PU140 import files
#from MuJetAnalysis.DisplacedL1MuFilter.DarkSUSY_mH_125_mGammaD_20000_ctau_100_14TeV import files
#from MuJetAnalysis.DisplacedL1MuFilter.DarkSUSY_mH_125_mGammaD_20000_ctau_1000_14TeV import files

process.source = cms.Source("PoolSource",
                    fileNames = cms.untracked.vstring(*files
        #'/store/user/slava77/SingleMuMinusFlatPt0p2To150/TTI2023Upg14D-PU140bx25-ILT_SLHC14/6a6577f18a9b70d924bea399af3ff625/2023TTIUpg14D_1000_1_uFi.root'
        #'/store/user/slava77/Neutrino_Pt2to20_gun/TTI2023Upg14D-PU140bx25-ILT_SLHC14/6a6577f18a9b70d924bea399af3ff625/2023TTIUpg14D_1000_2_Eiv.root'
        )
                    )


process.dump=cms.EDAnalyzer('EventContentAnalyzer')
#process.l1extraParticles + + process.dump
#process.p = cms.Path(process.l1extraParticles + process.L1TkMuons  + process.dump + process.DisplacedL1MuFilter_PhaseIIGE21)
process.TFileService = cms.Service("TFileService",
  fileName = cms.string("out_filter_ana_DarkSUSY_mH_125_mGammaD_20000_ctau_50_14TeV_PU140.test.root")
)


process.p = cms.Path(process.DisplacedL1MuFilter_PhaseIIGE21)
#process.p.remove(process.L1TkMuonsDTSequence)

process.out = cms.OutputModule("PoolOutputModule",
   fileName = cms.untracked.string('file:filter.root'),
                               SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('p')),
)

#process.endpath1 = cms.EndPath(process.out) 
