#from CRABClient.UserUtilities import config
#config = config()
#the two following lines are due to https://hypernews.cern.ch/HyperNews/CMS/get/computing-tools/3731/1/1/1/1/1/2/1/4.html
from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'filteredZEEDeadCh2018B_NewTraining700_intEvt2'
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
# Name of the CMSSW configuration file
config.JobType.psetName = 'testReRecoZSkimData_intEvt_all.py'
config.JobType.maxMemoryMB=2500
##config.JobType.inputFiles=['ZeeIntEvents.txt']

config.section_("Data")
config.Data.inputDataset = '/EGamma/Run2018B-ZElectron-PromptReco-v1/RAW-RECO'
#config.Data.splitting = 'Automatic'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob=6
config.Data.totalUnits=-1
config.Data.publication = True
#config.Data.outLFNDirBase='/store/group/dpg_ecal/comm_ecal/taroni/'

# This string is used to construct the output dataset name
config.Data.outputDatasetTag = 'ZEEDeadCh2018B_NewTraining700_intEvt2'

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
