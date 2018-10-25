# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step3 --conditions 101X_dataRun2_Prompt_v9 -n -1 --era Run2_2018 --eventcontent RAWRECO --data -s RAW2DIGI,RECO --datatier RAW-RECO --python testReRecoZSkimData_fromRawReco.py --filein /store/data/Run2018B/EGamma/RAW-RECO/ZElectron-PromptReco-v1/000/317/864/00000/8A838407-EC71-E811-8525-FA163E54B47A.root --fileout file:step3_2018.root --scenario pp --no_exec
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('RERECO',eras.Run2_2018)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.Reconstruction_Data_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)
process.MessageLogger.cerr.FwkReport.reportEvery = 1
# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/data/Run2018B/EGamma/RAW-RECO/ZElectron-PromptReco-v1/000/317/182/00000/08C8D1B6-7966-E811-B307-FA163EAF8008.root',
##'/store/data/Run2018B/EGamma/RAW-RECO/ZElectron-PromptReco-v1/000/317/182/00000/08C8D1B6-7966-E811-B307-FA163EAF8008.root',
##'/store/data/Run2018B/EGamma/RAW-RECO/ZElectron-PromptReco-v1/000/317/696/00000/FA5B110E-8570-E811-A137-FA163EE379D7.root',
##'/store/data/Run2018B/EGamma/RAW-RECO/ZElectron-PromptReco-v1/000/317/864/00000/8A838407-EC71-E811-8525-FA163E54B47A.root',
##'/store/data/Run2018B/EGamma/RAW-RECO/ZElectron-PromptReco-v1/000/317/861/00000/347EC1FE-BD71-E811-92CB-FA163EBBBA60.root', 
##'/store/data/Run2018B/EGamma/RAW-RECO/ZElectron-PromptReco-v1/000/317/744/00000/04CD0C57-4D70-E811-9C79-FA163E9C495B.root', 
##'/store/data/Run2018B/EGamma/RAW-RECO/ZElectron-PromptReco-v1/000/317/709/00000/B2D9465B-2270-E811-979A-FA163EA83FDB.root', 
##'/store/data/Run2018B/EGamma/RAW-RECO/ZElectron-PromptReco-v1/000/317/696/00000/FE35772A-7070-E811-8156-02163E01A086.root', 
##'/store/data/Run2018B/EGamma/RAW-RECO/ZElectron-PromptReco-v1/000/317/696/00000/FE14A383-7A70-E811-BF14-02163E01A103.root', 
##'/store/data/Run2018B/EGamma/RAW-RECO/ZElectron-PromptReco-v1/000/317/696/00000/FE11D416-7870-E811-8D8C-02163E00B04A.root', 
##'/store/data/Run2018B/EGamma/RAW-RECO/ZElectron-PromptReco-v1/000/317/696/00000/FA5B110E-8570-E811-A137-FA163EE379D7.root', 
##'/store/data/Run2018B/EGamma/RAW-RECO/ZElectron-PromptReco-v1/000/317/696/00000/F87BE9D7-9270-E811-B631-FA163E96604B.root', 
##'/store/data/Run2018B/EGamma/RAW-RECO/ZElectron-PromptReco-v1/000/317/696/00000/F864E649-9070-E811-84CC-FA163E7C8798.root', 
##'/store/data/Run2018B/EGamma/RAW-RECO/ZElectron-PromptReco-v1/000/317/696/00000/F85E2381-A470-E811-9B41-FA163EBDF294.root', 
##'/store/data/Run2018B/EGamma/RAW-RECO/ZElectron-PromptReco-v1/000/317/696/00000/F2FA39A5-8870-E811-B92C-FA163EC64BA5.root', 
##'/store/data/Run2018B/EGamma/RAW-RECO/ZElectron-PromptReco-v1/000/317/696/00000/F24C3152-7970-E811-BAF8-FA163E0BA969.root', 
##'/store/data/Run2018B/EGamma/RAW-RECO/ZElectron-PromptReco-v1/000/317/696/00000/F21F45D7-8570-E811-A71C-FA163E0C46F2.root', 
##'/store/data/Run2018B/EGamma/RAW-RECO/ZElectron-PromptReco-v1/000/317/696/00000/F0CFBB67-8A70-E811-95DD-FA163E4A4920.root', 
##'/store/data/Run2018B/EGamma/RAW-RECO/ZElectron-PromptReco-v1/000/317/696/00000/F01CCA1B-8F70-E811-9953-FA163E62F74A.root', 
##'/store/data/Run2018B/EGamma/RAW-RECO/ZElectron-PromptReco-v1/000/317/696/00000/EE15058C-0670-E811-B780-02163E01A01A.root', 
##'/store/data/Run2018B/EGamma/RAW-RECO/ZElectron-PromptReco-v1/000/317/696/00000/EC710A7B-9970-E811-9A99-FA163E7D073D.root', 
##'/store/data/Run2018B/EGamma/RAW-RECO/ZElectron-PromptReco-v1/000/317/696/00000/EC3323A7-8370-E811-B387-FA163E191EB7.root', 
##'/store/data/Run2018B/EGamma/RAW-RECO/ZElectron-PromptReco-v1/000/317/696/00000/EA2202AC-8F70-E811-AFF3-02163E015C12.root', 
##'/store/data/Run2018B/EGamma/RAW-RECO/ZElectron-PromptReco-v1/000/317/696/00000/E8F8DC47-7770-E811-90F9-FA163E20727F.root', 
##'/store/data/Run2018B/EGamma/RAW-RECO/ZElectron-PromptReco-v1/000/317/696/00000/E8C4D5A3-8370-E811-B93F-FA163E04A679.root', 
##'/store/data/Run2018B/EGamma/RAW-RECO/ZElectron-PromptReco-v1/000/317/696/00000/E8B69EA6-8E70-E811-A58E-FA163EFB8B6B.root', 
##'/store/data/Run2018B/EGamma/RAW-RECO/ZElectron-PromptReco-v1/000/317/696/00000/E88687EE-7E70-E811-A885-02163E01A098.root', 
##'/store/data/Run2018B/EGamma/RAW-RECO/ZElectron-PromptReco-v1/000/317/696/00000/E6F968C5-9170-E811-B1AE-02163E01A178.root', 
##'/store/data/Run2018B/EGamma/RAW-RECO/ZElectron-PromptReco-v1/000/317/696/00000/E6F7BF17-7770-E811-B0D4-FA163E7E1CFF.root', 
##'/store/data/Run2018B/EGamma/RAW-RECO/ZElectron-PromptReco-v1/000/317/696/00000/E4E28F69-8570-E811-BEC6-FA163EA7DB29.root', 
##'/store/data/Run2018B/EGamma/RAW-RECO/ZElectron-PromptReco-v1/000/317/696/00000/E4703D02-B670-E811-A5BF-FA163E836BB3.root'
),
    secondaryFileNames = cms.untracked.vstring()
)
#events= cms.untracked.VEventRange('317182:1415:2024944698')
events= cms.untracked.VEventRange()
for line in open('checkingIntEvt700.txt'):
    events.append(line.rstrip("\n"))
##    print line.rstrip("\n")
process.source.eventsToProcess = cms.untracked.VEventRange(events)
        
process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step3 nevts:-1'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

from Configuration.EventContent.EventContent_cff import RAWRECOEventContent
process.skimContent = process.RAWRECOEventContent.clone()
process.load("DPGAnalysis.Skims.filterRecHitsRecovery_cfi")
process.recoveryfilter = cms.Path(process.recHitRecoveryFilter)
from RecoLocalCalo.EcalRecProducers.ecalRecHit_cfi import ecalRecHit
process.ecalRecHit.singleChannelRecoveryThreshold=0.7

# Output definition

process.RAWRECOoutput = cms.OutputModule("PoolOutputModule",
                             
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('RAW-RECO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:step3_2018.root'),
    outputCommands = process.RAWRECOEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0),
    SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('recoveryfilter'))
)
process.RAWRECOoutput.outputCommands.append('drop *_*_*_RECO')

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '101X_dataRun2_Prompt_v9', '')

# Path and EndPath definitions

process.raw2digi_step = cms.Path(process.RawToDigi)
process.reconstruction_step = cms.Path(process.reconstruction)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWRECOoutput_step = cms.EndPath(process.RAWRECOoutput)

##process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.reconstruction_step, process.recoveryfilter, process.endjob_step, process.RAWRECOoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)


### Customisation from command line
##
###Have logErrorHarvester wait for the same EDProducers to finish as those providing data for the OutputModule
##from FWCore.Modules.logErrorHarvester_cff import customiseLogErrorHarvesterUsingOutputCommands
##process = customiseLogErrorHarvesterUsingOutputCommands(process)
##
### Add early deletion of temporary data products to reduce peak memory need
##from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
##process = customiseEarlyDelete(process)
### End adding early deletion
