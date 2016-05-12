from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")

config.General.workArea = 'crab_promptMuon_20160204'
config.General.requestName='crab_promptMuon_20160208'
config.General.transferOutputs = True

config.section_("JobType")

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'runHLTBendingAngle_cfg.py'
#config.JobType.psetName = '/home/dildick/DisplacedMuonJetAnalysis_2015/CMSSW_7_4_1_patch1/src/MuJetAnalysis/CutFlowAnalyzer/test/runCutFlowAnalyzer_cfg.py'

config.section_("Data")

#config.Data.inputDBS = 'global'
config.Data.inputDBS = 'phys03'

config.Data.splitting = 'FileBased'

config.Data.unitsPerJob = 1

config.Data.outLFNDirBase = '/store/user/tahuang/'

config.Data.publication = False
#config.Data.inputDataset='/MinBias_TuneCUETP8M1_13TeV-pythia8/RunIIWinter15GS-MCRUN2_71_V1-v1/GEN-SIM'
#config.Data.inputDataset = '/SingleMuMinusFlatPt0p2To150/slava77-TTI2023Upg14D-PU140bx25-ILT_SLHC14-6a6577f18a9b70d924bea399af3ff625/USER'
#config.Data.inputDataset = '/SLHC23_patch1_2023Muon_gen_sim_Pt2_50_1M/tahuang-SLHC25_patch1_2023Muon_1M_L1_PU0_Pt2_50_updategemeta-1bf93df4dfbb43dc918bd6e47dedbf79/USER'
config.Data.inputDataset = '/DarkSUSY_mH_125_mGammaD_20000_ctau0_14TeV_madgraph452_bridge224_LHE_pythia8_GEN_SIM_80k_v3/jrdv009-DarkSUSY_mH_125_mGammaD_20000_ctau0_14TeV_madgraph452_bridge224_LHE_pythia8_GEN_SIM_80k_v3-e007db91b5aa2bed7c0fc47ce82a4274/USER'

config.Data.outputDatasetTag='crab_promptMuon_20160207'

config.section_("Site")

config.Site.storageSite = 'T3_US_TAMU'

#config.Site.whitelist = ['T3_US_TAMU']


