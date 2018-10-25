import FWCore.ParameterSet.Config as cms

demo = cms.EDAnalyzer('MyTreeMaker'
     ,tracks = cms.untracked.InputTag('ctfWithMaterialTracks')
)
