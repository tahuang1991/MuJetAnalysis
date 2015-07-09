import sys
sys.argv.append( '-b' )
import math
import array

from ROOT import *
gROOT.SetBatch(1)

from trackRecoEfficiency import *

inputDir = "/afs/cern.ch/user/d/dildick/work/GEM/forJose/DisplacedMuHLTStudyPtAssignment/CMSSW_7_4_4/src/"
ext = ".png"

inputFiles = [
	"/fdata/hepx/store/user/dildick/DarkSUSY_mH_125_mGammaD_20000_ctau100_14TeV_madgraph452_bridge224_LHE_pythia8_GEN_SIM_80k_v3/DarkSUSY_mH_125_mGammaD_20000_cT_0_14TeV_ANA_v1/6e45b1eb15341f30a6eb15afa02d319d/out_ana.root",
"/fdata/hepx/store/user/dildick/DarkSUSY_mH_125_mGammaD_20000_ctau100_14TeV_madgraph452_bridge224_LHE_pythia8_GEN_SIM_80k_v3/DarkSUSY_mH_125_mGammaD_20000_cT_100_14TeV_ANA_v1/6e45b1eb15341f30a6eb15afa02d319d/out_ana.root"
]

outputDirs = [
	"out_ana_mGammaD_20000_ctau0_14TeV_HLT_07092015/",
	"out_ana_mGammaD_20000_ctau100_14TeV_HLT_07092015/"
	]

highMassExt = ['_mGammaD_20000_ctau_0_14TeV_PU0',
               '_mGammaD_20000_ctau_100_14TeV_PU0']

pu = [0,0]


for i in range(0,1):
	class Plotter:
		def __init__(self):
			self.inputDir = inputDir
			self.inputFile = inputFiles[i]
			self.outputDir = outputDirs[i]
			self.ext = highMassExt[i] + ext
			self.analyzer = "HLTBendingAngle"
			self.events = "trk_eff_dt_ALL"
			self.file = TFile.Open(self.inputFile)
			self.dirAna = (self.file).Get(self.analyzer)
			self.tree = (self.dirAna).Get(self.events)            
			self.pu = pu[i]
			self.debug = False
        
	## make the plots
	plotter = Plotter()
	print plotter.inputFile
	trackKinematics(plotter)
	recoTrackExtraEfficiency(plotter)
	recoTrackEfficiency(plotter)
	recoChargedCandidateEfficiency(plotter)







