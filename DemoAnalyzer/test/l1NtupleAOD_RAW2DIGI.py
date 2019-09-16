# -*- coding: utf-8 -*-
# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: l1NtupleAOD -s RAW2DIGI --era=Run2_2018 --customise=L1Trigger/L1TNtuples/customiseL1Ntuple.L1NtupleAODEMU --conditions=102X_dataRun2_Prompt_v14 -n 10 --data --no_exec --no_output --filein=file:FD7A565D-60BD-DE40-9544-1933691730E0.root
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('RAW2DIGI',eras.Run2_2018)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:Filter.root'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('l1NtupleAOD nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)




# Output definition

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '102X_dataRun2_Prompt_v14', '')

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.endjob_step = cms.EndPath(process.endOfProcess)

# Schedule definition
process.schedule = cms.Schedule(process.endjob_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)


# customisation of the process.

# Automatic addition of the customisation function from L1Trigger.L1TNtuples.customiseL1Ntuple
from L1Trigger.L1TNtuples.customiseL1Ntuple import L1NtupleAODEMU 

#call to customisation function L1NtupleAODEMU imported from L1Trigger.L1TNtuples.customiseL1Ntuple
process = L1NtupleAODEMU(process)

# End of customisation functions

# Customisation from command line

#Have logErrorHarvester wait for the same EDProducers to finish as those providing data for the OutputModule
from FWCore.Modules.logErrorHarvester_cff import customiseLogErrorHarvesterUsingOutputCommands
process = customiseLogErrorHarvesterUsingOutputCommands(process)

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion

process.l1UpgradeTfMuonTree.bmtfMuonToken = cms.untracked.InputTag("gmtStage2Digis","BMTF")
process.l1UpgradeTfMuonTree.omtfMuonToken = cms.untracked.InputTag("gmtStage2Digis","OMTF")
process.l1UpgradeTfMuonTree.emtfMuonToken = cms.untracked.InputTag("gmtStage2Digis","EMTF")

process.l1UpgradeTfMuonEmuTree.bmtfMuonToken = cms.untracked.InputTag("gmtStage2Digis","BMTF")
process.l1UpgradeTfMuonEmuTree.omtfMuonToken = cms.untracked.InputTag("gmtStage2Digis","OMTF")
process.l1UpgradeTfMuonEmuTree.emtfMuonToken = cms.untracked.InputTag("gmtStage2Digis","EMTF")

process.l1UpgradeTree.muonToken = cms.untracked.InputTag("gmtStage2Digis","Muon")
process.l1UpgradeEmuTree.muonToken = cms.untracked.InputTag("gmtStage2Digis","Muon")

process.L1NtupleAOD.remove(process.l1JetRecoTree)
process.L1NtupleAOD.remove(process.l1MetFilterRecoTree)
process.L1NtupleAOD.remove(process.l1ElectronRecoTree)
process.L1NtupleAOD.remove(process.l1TauRecoTree)

process.L1NtupleEMU.remove(process.l1CaloTowerEmuTree)
process.L1NtupleEMU.remove(process.l1uGTEmuTree)
