# -*- coding: utf-8 -*-
from CRABClient.UserUtilities import config
config = config()


config.General.requestName = 'SingleMuon_Run2018A-17Sep2018-v2_AOD'
config.General.transferLogs = True

config.JobType.maxMemoryMB = 10000
config.JobType.pluginName = 'Analysis'
# Name of the CMSSW configuration file
#config.JobType.psetName = 'l1NtupleAOD_RAW2DIGI.py'
config.JobType.psetName = 'runFilterSample2RecoMu_cfg.py'

config.Data.inputDataset = '/SingleMuon/Run2018A-17Sep2018-v2/AOD'  #315252-316995
#config.Data.inputDataset = '/SingleMuon/Run2018B-17Sep2018-v1/AOD' #317080-319310
#config.Data.inputDataset = '/SingleMuon/Run2018C-17Sep2018-v1/AOD' #319337-320065
#config.Data.inputDataset = '/SingleMuon/Run2018D-PromptReco-v2/AOD' #320673-325175

config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 100
config.Data.publication = True
# This string is used to construct the output dataset name
config.Data.outputDatasetTag = 'CRAB3_Analysis_SingleMuon_Run2018A-17Sep2018-v2_AOD'
# These values only make sense for processing data
#    Select input data based on a lumi mask
config.Data.lumiMask = 'Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt'
#    Select input data based on run-ranges
#config.Data.runRange = '319337-320065'
config.Data.runRange = '315252-316995'

# Where the output files will be transmitted to
config.Site.storageSite = 'T3_US_Rice'
