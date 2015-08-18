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
inputDir = "/uscms_data/d3/dildick/work/MuonPhaseIIScopeDoc/CMSSW_6_2_0_SLHC26_patch3/src/"
preOut = "/uscms_data/d3/dildick/work/MuonPhaseIIScopeDoc/CMSSW_6_2_0_SLHC26_patch3/src/OutputDirectoryForScopeDoc/"
ext = ".png"

inputFiles = [
      'out_anaDarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_HLT_fullScope.root',
      'out_anaDarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_HLT_fullScopeAging.root',
      'out_anaDarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_HLT_descope235MCHFaging.root',
      'out_anaDarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_HLT_descope200MCHF.root',
      'out_anaDarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_HLT_descope200MCHFaging.root',

      'out_anaDarkSUSY_mH_125_mGammaD_20000_cT_100_14TeV_PU140_HLT_fullScope.root',
      'out_anaDarkSUSY_mH_125_mGammaD_20000_cT_100_14TeV_PU140_HLT_fullScopeAging.root',
      'out_anaDarkSUSY_mH_125_mGammaD_20000_cT_100_14TeV_PU140_HLT_descope235MCHFaging.root',
      'out_anaDarkSUSY_mH_125_mGammaD_20000_cT_100_14TeV_PU140_HLT_descope200MCHF.root',
      'out_anaDarkSUSY_mH_125_mGammaD_20000_cT_100_14TeV_PU140_HLT_descope200MCHFaging.root',
      ]

outputDirs = [
      'DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_ANA_fullScope/',
      'DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_ANA_fullScopeAging/',
      'DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_ANA_descope235MCHFaging/',
      'DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_ANA_descope200MCHF/',
      'DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_ANA_descope200MCHFaging/',

      'DarkSUSY_mH_125_mGammaD_20000_cT_100_14TeV_PU140_ANA_fullScope/',
      'DarkSUSY_mH_125_mGammaD_20000_cT_100_14TeV_PU140_ANA_fullScopeAging/',
      'DarkSUSY_mH_125_mGammaD_20000_cT_100_14TeV_PU140_ANA_descope235MCHFaging/',
      'DarkSUSY_mH_125_mGammaD_20000_cT_100_14TeV_PU140_ANA_descope200MCHF/',
      'DarkSUSY_mH_125_mGammaD_20000_cT_100_14TeV_PU140_ANA_descope200MCHFaging/',
      ]

highMassExt = [
      '_DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_fullScope',
      '_DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_fullScopeAging',
      '_DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_descope235MCHFaging',
      '_DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_descope200MCHF',
      '_DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_descope200MCHFaging',

      '_DarkSUSY_mH_125_mGammaD_20000_cT_100_14TeV_PU140_fullScope',
      '_DarkSUSY_mH_125_mGammaD_20000_cT_100_14TeV_PU140_fullScopeAging',
      '_DarkSUSY_mH_125_mGammaD_20000_cT_100_14TeV_PU140_descope235MCHFaging',
      '_DarkSUSY_mH_125_mGammaD_20000_cT_100_14TeV_PU140_descope200MCHF',
      '_DarkSUSY_mH_125_mGammaD_20000_cT_100_14TeV_PU140_descope200MCHFaging',
      ]

highMassCtau = [1000,1000,1000,1000,1000,
                100,100,100,100,100]

highMassPU = [140,140,140,140,140,140,
              140,140,140,140,140,140]

for i in range(0,10):
      class Plotter:
            def __init__(self):
                  self.inputDir = inputDir
                  self.inputFile = inputDir + inputFiles[i]
                  self.outputDir = preOut + outputDirs[i]
                  self.ext = highMassExt[i] + ext
                  self.analyzer = "HLTBendingAngle"
                  self.events = "trk_eff_MU_ALL"
                  self.file = TFile.Open(self.inputFile)
                  self.dirAna = (self.file).Get(self.analyzer)
                  self.tree = (self.dirAna).Get(self.events)            
                  self.pu = 140
                  self.symb = "Z_{D}"
                  self.ctau = "c#tau(" + self.symb + ") = %d mm"%(highMassCtau[i])
                  self.mass = 'm(' + self.symb + ') = 20 GeV'
                  self.boson = "Z boson"
                  self.debug = False
                  
      ## make the plots
      plotter = Plotter()
      #genKinematics(plotter)
      #trackKinematics(plotter)
      recoTrackEfficiency(plotter)
      #pTCorrelationPlots(plotter)
      






