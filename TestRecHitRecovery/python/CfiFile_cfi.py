import FWCore.ParameterSet.Config as cms

demo = cms.EDAnalyzer('TestRecHitRecovery'
     ,tracks = cms.untracked.InputTag('ctfWithMaterialTracks')
)
