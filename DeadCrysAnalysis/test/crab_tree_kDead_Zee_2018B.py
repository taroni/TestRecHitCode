#from CRABClient.UserUtilities import config
#config = config()
#the two following lines are due to https://hypernews.cern.ch/HyperNews/CMS/get/computing-tools/3731/1/1/1/1/1/2/1/4.html
from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'tree_kDead_Zee_2018B'
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
# Name of the CMSSW configuration file
config.JobType.psetName = 'deadCrysAnalysis_TrainOnData_LargeStat_cfg_2.py'
config.JobType.maxMemoryMB=2500
##config.JobType.inputFiles=['ZeeIntEvents.txt']

config.section_("Data")
config.Data.inputDataset = '/EGamma/Run2018B-ZElectron-PromptReco-v1/RAW-RECO'
config.Data.splitting = 'Automatic'
#config.Data.unitsPerJob=5
#config.Data.totalUnits=-1
config.Data.publication = True
#config.Data.outLFNDirBase='/store/group/dpg_ecal/comm_ecal/taroni/'

# This string is used to construct the output dataset name
config.Data.outputDatasetTag = 'tree_kDead_Zee_2018B'

# These values only make sense for processing data
#    Select input data based on a lumi mask

##ADD THE DCS ONLY LUMIMASK
#    Select input data based on run-ranges
#config.Data.runRange = '300742-302029'

# Where the output files will be transmitted to
config.section_("Site")
config.Site.storageSite = 'T2_CH_CERN'

config.section_("User")
config.section_("Debug")
