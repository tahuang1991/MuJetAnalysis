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
preOut = "/uscms_data/d3/dildick/work/MuonPhaseIIScopeDoc/CMSSW_6_2_0_SLHC26_patch3/src/OutputDirectoryForScopeDoc_20150819/"
ext = ".C"

inputFiles = [
      'out_anaDarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_HLT_fullScope.root',
      'out_anaDarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_HLT_fullScopeAging.root',
      'out_anaDarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_HLT_descope235MCHF.root',
      'out_anaDarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_HLT_descope235MCHFaging.root',
      'out_anaDarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_HLT_descope200MCHF.root',
      'out_anaDarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_HLT_descope200MCHFaging.root',

      'out_anaDarkSUSY_mH_125_mGammaD_20000_cT_100_14TeV_PU140_HLT_fullScope.root',
      'out_anaDarkSUSY_mH_125_mGammaD_20000_cT_100_14TeV_PU140_HLT_fullScopeAging.root',
      'out_anaDarkSUSY_mH_125_mGammaD_20000_cT_100_14TeV_PU140_HLT_descope235MCHFaging.root',
      'out_anaDarkSUSY_mH_125_mGammaD_20000_cT_100_14TeV_PU140_HLT_descope200MCHF.root',
      'out_anaDarkSUSY_mH_125_mGammaD_20000_cT_100_14TeV_PU140_HLT_descope200MCHFaging.root',
      ]

highMassExt = [
      '_DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_fullScope',
      '_DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_fullScopeAging',
      '_DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_descope235MCHF',
      '_DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_descope235MCHFaging',
      '_DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_descope200MCHF',
      '_DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_descope200MCHFaging',

      '_DarkSUSY_mH_125_mGammaD_20000_cT_100_14TeV_PU140_fullScope',
      '_DarkSUSY_mH_125_mGammaD_20000_cT_100_14TeV_PU140_fullScopeAging',
      '_DarkSUSY_mH_125_mGammaD_20000_cT_100_14TeV_PU140_descope235MCHFaging',
      '_DarkSUSY_mH_125_mGammaD_20000_cT_100_14TeV_PU140_descope200MCHF',
      '_DarkSUSY_mH_125_mGammaD_20000_cT_100_14TeV_PU140_descope200MCHFaging',
      ]

highMassCtau = [1000,1000,1000,1000,1000,1000,
                100,100,100,100,100]

highMassPU = [140,140,140,140,140,140,
              140,140,140,140,140,140]

#outputFile = TFile("output.root","NEW")
my_efficiencies_pt0 = []
my_efficiencies_pt15 = []
my_efficiencies_pt20 = []
my_efficiencies_pt25 = []

my_efficiencies = []
my_efficiencies.append([])
my_efficiencies.append([])
my_efficiencies.append([])
my_efficiencies.append([])
my_efficiencies.append([])
my_efficiencies.append([])

my_colors = [kBlue, kRed, kGreen+1, kOrange, kMagenta+1, kBlack]
pts = [0,15,20,25]

for i in range(0,6):
      class Plotter:
            def __init__(self):
                  self.inputDir = inputDir
                  self.inputFile = inputDir + inputFiles[i]
                  self.outputDir = preOut #+ outputDirs[i]
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
#                  self.outputFile = outputFile
                  
            
      ## make the plots
      plotter = Plotter()
      #genKinematics(plotter)
      #trackKinematics(plotter)
      my_efficiencies[0].append(recoTrackEfficiency_2(plotter, 0))
      my_efficiencies[1].append(recoTrackEfficiency_2(plotter, 15))
      my_efficiencies[2].append(recoTrackEfficiency_2(plotter, 20))
      my_efficiencies[3].append(recoTrackEfficiency_2(plotter, 25))
      #recoTrackEfficiency_2(plotter)
      #pTCorrelationPlots(plotter)
   
for i in range(0,4):
      c = TCanvas("c","c",800,600)
      c.Clear()
      gStyle.SetTitleStyle(0);
      gStyle.SetTitleAlign(13); ##coord in top left
      gStyle.SetTitleX(0.);
      gStyle.SetTitleY(1.);
      gStyle.SetTitleW(1);
      gStyle.SetTitleH(0.058);
#        gStyle.SetTitleXOffset(0.05)
      gStyle.SetTitleBorderSize(0);
      gStyle.SetPadLeftMargin(0.126);
      gStyle.SetPadRightMargin(0.04);
      gStyle.SetPadTopMargin(0.06);
      gStyle.SetPadBottomMargin(0.13);
      gStyle.SetOptStat(0);
      gStyle.SetMarkerStyle(1);
      gPad.SetTickx(1)
      gPad.SetTicky(1)
        #gStyle.SetStatStyle(0)
      base = TH1D("base","base", 25, 0, 2.5)
      base.SetStats(0)
      base.SetTitle("                                                                      14 TeV,  PU = %d; SimTrack #eta; Reconstruction efficiency"%(140))
      base.SetMinimum(0)
      base.SetMaximum(1.1)
      base.GetXaxis().SetLabelSize(0.05)
      base.GetYaxis().SetLabelSize(0.05)
      base.GetXaxis().SetTitleSize(0.06)
      base.GetYaxis().SetTitleSize(0.06)
#        base.GetXaxis().SetLimits(0,maxbin)
      base.Draw()
      for h in my_efficiencies[i]:
            h.SetMarkerColor(kBlue)
            h.SetLineColor(kBlue)
            h.SetLineWidth(2)
            h.SetMarkerStyle(1)
            h.SetMarkerSize(15)
            h.Draw("same")

      leg = TLegend(0.2,0.3,0.75,0.45,"","brNDC")
      leg.SetFillColor(kWhite)
      leg.SetBorderSize(0)
      leg.SetFillStyle(0)
      leg.SetTextSize(0.05)
      leg.AddEntry(h,"title","l")
      leg.Draw("same")
      #tex = drawLabel(p.ctau + ", " + p.mass,0.45,0.55,0.05)
      #tex4 = drawLabel(p.mass,0.55,0.47,0.05)
      #tex3 = drawLabel("H #rightarrow 2n_{1} #rightarrow 2n_{D}2Z_{D} #rightarrow 2n_{D}4#mu",0.45,0.65,0.05)
      tex2 = applyStupidTdrStyle()
      
      c.SaveAs("testplot_%d.png"%(pts[i]))





