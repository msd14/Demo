# -*- coding: utf-8 -*-
import FWCore.ParameterSet.Config as cms
		
process = cms.Process("SKIM")
#initialize MessageLogger 
process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("EventFilter.L1TRawToDigi.emtfStage2Digis_cfi")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

	
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag.globaltag   = '102X_dataRun2_Prompt_v14'

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring("file:F76E0FE7-AA7B-2949-8045-EF7637086554.root")
)
process.maxEvents = cms.untracked.PSet ( input = cms.untracked.int32 ( -1 ) )

process.myfilter = cms.EDFilter("FilterSample2RecoMu")

process.filterPath = cms.Path(process.emtfStage2Digis * process.myfilter)


process.output = cms.OutputModule(
    "PoolOutputModule",
    fileName = cms.untracked.string( "Filter.root" ),
    SelectEvents = cms.untracked.PSet(
	SelectEvents = cms.vstring("filterPath")
    )
)

process.out = cms.EndPath( process.output )
