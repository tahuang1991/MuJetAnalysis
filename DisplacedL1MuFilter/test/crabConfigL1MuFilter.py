from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()
config.General.workArea = 'crab_space'
config.General.transferOutputs = True
config.General.transferLogs = True
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '/uscms/home/dildick/nobackup/work/MuonPhaseIIScopeDoc/CMSSW_6_2_0_SLHC26_patch3/src/MuJetAnalysis/DisplacedL1MuFilter/test/runDisplacedL1MuFilter_cfg.py'
config.Data.splitting = 'FileBased'
config.Data.inputDBS = 'phys03'
config.Data.unitsPerJob = 10
config.Data.outLFNDirBase = '/store/group/lpcgem/'
config.Data.publication = True
config.Site.storageSite = 'T3_US_FNALLPC'
