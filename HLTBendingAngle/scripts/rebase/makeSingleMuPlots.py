import sys
sys.argv.append( '-b' )
import math
import array

from ROOT import *
gROOT.SetBatch(1)

from trackRecoEfficiency import *
from trackKinematics import *
from simKinematics import *
from ptCorrelation import *
from inputFiles import *

inputDir = "/uscms_data/d3/dildick/work/MuonPhaseIIScopeDoc/CMSSW_6_2_0_SLHC26_patch3/src/"
preOut = "/uscms_data/d3/dildick/work/MuonPhaseIIScopeDoc/CMSSW_6_2_0_SLHC26_patch3/src/MuJetAnalysis/HLTBendingAngle/scripts/rebase/"
ext = ".png"
pu=0


class Plotter:
    def __init__(self):
        self.inputDir = inputDir
        self.inputFile = '/eos/uscms/store/user/lpcgem/SingleMuPt2to50/SingleMuPt2to50_PU0_ANA_fullScope/151026_121406/0000/out_ana.root'
        print self.inputFile
        self.outputDir = preOut #+ outputDirs[i]
        self.ext = '_SingleMuPt0to50' + ext
        self.analyzer = "HLTBendingAngle"
        self.events = "trk_eff_MU_ALL"
        self.file = TFile.Open(self.inputFile)
        self.dirAna = (self.file).Get(self.analyzer)
        self.tree = (self.dirAna).Get(self.events)            
        self.hlt = (self.dirAna).Get("trk_hlt")            
        self.pu = 0
        self.symb = ""
        self.ctau = ""
        self.mass = ''
        self.boson = ""
        self.debug = False

plotter = Plotter()

import singleMuEfficiency
singleMuEfficiency.l1ExtraTrackEfficiency(plotter)
