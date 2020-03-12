# -*- coding: utf-8 -*-
from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'Run2017C-17Nov2017-v1'
config.General.transferLogs = True

config.JobType.maxMemoryMB = 2500
config.JobType.pluginName = 'Analysis'
# Name of the CMSSW configuration file
config.JobType.psetName = 'runFilterSample2RecoMu_cfg.py'
config.JobType.allowUndistributedCMSSW = True

config.Data.inputDataset = '/SingleMuon/Run2017C-17Nov2017-v1/AOD'

config.Data.useParent = True
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 100
config.Data.publication = True
config.Data.outputDatasetTag = 'SingleMuon_Run2017C-17Nov2017-v1'

#    Select input data based on a lumi mask
config.Data.lumiMask = 'Cert_299337-302029_13TeV_PromptReco_Collisions17_JSON_eraC.txt'

#    Select input data based on run-ranges
config.Data.runRange = '299368-302029'

# Where the output files will be transmitted to
config.Site.storageSite = 'T3_US_FNALLPC'
