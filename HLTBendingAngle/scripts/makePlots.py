import sys
sys.argv.append( '-b' )
import math
import array

from ROOT import *
gROOT.SetBatch(1)

from trackRecoEfficiency import *

inputDir = "/afs/cern.ch/user/d/dildick/work/GEM/forJose/DisplacedMuHLTStudyPtAssignment/CMSSW_7_4_4/src/"
ext = ".png"

class Plotter:
    def __init__(self):
        self.inputDir = inputDir
        self.inputFile = "out_ana_mGammaD_20000_ctau100_14TeV_HLT_07092015.root"
        self.outputDir = "out_ana_mGammaD_20000_ctau100_14TeV_HLT_07092015/"
        self.ext = ext
        self.analyzer = "HLTBendingAngle"
        self.events = "trk_eff_dt_ALL"
        self.file = TFile.Open(self.inputFile)
        self.dirAna = (self.file).Get(self.analyzer)
        self.tree = (self.dirAna).Get(self.events)            
        self.pu = 0
        self.debug = False
        
plotter = Plotter()

trackKinematics(plotter)
recoTrackExtraEfficiency(plotter)
recoTrackEfficiency(plotter)
recoChargedCandidateEfficiency(plotter)







