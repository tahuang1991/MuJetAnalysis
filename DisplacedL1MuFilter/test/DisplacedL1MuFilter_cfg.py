import FWCore.ParameterSet.Config as cms

process = cms.Process("test")
process.load("MuJetAnalysis.DisplacedL1MuFilter.DisplacedL1MuFilter_cfi")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(750)
)
process.source = cms.Source("EmptySource")

process.p = cms.Path(process.DisplacedL1MuFilter_PhaseIIGE21)
