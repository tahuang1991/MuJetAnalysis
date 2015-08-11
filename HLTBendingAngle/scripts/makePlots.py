import sys
sys.argv.append( '-b' )
import math
import array

from ROOT import *
gROOT.SetBatch(1)

from trackRecoEfficiency import *

def tracefunc(frame, event, arg, indent=[0]):
      if event == "call":
          indent[0] += 2
          print "-" * indent[0] + "> call function", frame.f_code.co_name
      elif event == "return":
          print "<" + "-" * indent[0], "exit function", frame.f_code.co_name
          indent[0] -= 2
      return tracefunc

#sys.settrace(tracefunc)

inputDir = "/afs/cern.ch/user/d/dildick/work/GEM/forJose/DisplacedMuHLTStudyPtAssignment/CMSSW_7_4_4/src/"
ext = ".png"

inputFiles = [
      "/fdata/hepx/store/user/dildick/DarkSUSY_mH_125_mGammaD_20000_ctau0_14TeV_madgraph452_bridge224_LHE_pythia8_GEN_SIM_80k_v3/DarkSUSY_mH_125_mGammaD_20000_cT_0_14TeV_ANA_v6/0948fe059a0e71d743b3cbd79e98108d/out_ana.root",
      "/fdata/hepx/store/user/dildick/DarkSUSY_mH_125_mGammaD_20000_ctau100_14TeV_madgraph452_bridge224_LHE_pythia8_GEN_SIM_80k_v3/DarkSUSY_mH_125_mGammaD_20000_cT_100_14TeV_ANA_v6/0948fe059a0e71d743b3cbd79e98108d/out_ana.root",
      "/fdata/hepx/store/user/dildick/DarkSUSY_mH_125_mGammaD_20000_ctau1000_14TeV_madgraph452_bridge224_LHE_pythia8_GEN_SIM_80k_v3/DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_ANA_v6/0948fe059a0e71d743b3cbd79e98108d/out_ana.root"
      ]

outputDirs = [
      "out_ana_mGammaD_20000_ctau0_14TeV_HLT_08102015/",
      "out_ana_mGammaD_20000_ctau100_14TeV_HLT_08102015/",
      "out_ana_mGammaD_20000_ctau1000_14TeV_HLT_08102015/"
      ]

highMassExt = [
      '_mGammaD_20000_ctau_0_14TeV_PU0',
      '_mGammaD_20000_ctau_100_14TeV_PU0',
      '_mGammaD_20000_ctau_1000_14TeV_PU0'
      ]

highMassCtau = [0,100,1000]
highMassPU = [0,0,0]

for i in range(0,3):
      class Plotter:
            def __init__(self):
                  self.inputDir = inputDir
                  self.inputFile = inputFiles[i]
                  self.outputDir = outputDirs[i]
                  self.ext = highMassExt[i] + ext
                  self.analyzer = "HLTBendingAngle"
                  self.events = "trk_eff_MU_ALL"
                  self.file = TFile.Open(self.inputFile)
                  self.dirAna = (self.file).Get(self.analyzer)
                  self.tree = (self.dirAna).Get(self.events)            
                  self.pu = highMassPU[i]
                  self.symb = "Z_{D}"
                  self.ctau = "c#tau(" + self.symb + ") = %d mm"%(highMassCtau[i])
                  self.mass = 'm(' + self.symb + ') = 20 GeV'
                  self.boson = "Z boson"
                  self.debug = False
                  
      ## make the plots
      plotter = Plotter()
      genKinematics(plotter)
      pTCorrelationPlots(plotter)
      #trackKinematics(plotter)
      #recoTrackEfficiency(plotter)
      






