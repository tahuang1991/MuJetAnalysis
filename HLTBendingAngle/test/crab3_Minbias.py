from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")

config.General.workArea = 'crab_MinbiasOnly_20160204'
config.General.requestName='crab_MinbiasOnly_20160204'
config.General.transferOutputs = True

config.section_("JobType")

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'runHLTBendingAngle_cfg.py'
#config.JobType.psetName = '/home/dildick/DisplacedMuonJetAnalysis_2015/CMSSW_7_4_1_patch1/src/MuJetAnalysis/CutFlowAnalyzer/test/runCutFlowAnalyzer_cfg.py'

config.section_("Data")

config.Data.inputDBS = 'global'

config.Data.splitting = 'FileBased'

config.Data.unitsPerJob = 50

config.Data.outLFNDirBase = '/store/user/tahuang/'

config.Data.publication = False
config.Data.inputDataset='/MinBias_TuneCUETP8M1_13TeV-pythia8/RunIIWinter15GS-MCRUN2_71_V1-v1/GEN-SIM'
config.Data.outputDatasetTag='crab_MinbiasOnly_20160204'

config.section_("Site")

config.Site.storageSite = 'T3_US_TAMU'

#config.Site.whitelist = ['T3_US_TAMU']


