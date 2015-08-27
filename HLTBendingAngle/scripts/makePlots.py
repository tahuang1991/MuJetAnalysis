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
ext = ".png"
pu=140

inputFiles = [
      'out_ana_DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_HLT_fullScope_v3.root',
      'out_ana_DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_HLT_fullScopeAging_v3.root',
      'out_ana_DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_HLT_descope235MCHF_v3.root',
      'out_ana_DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_HLT_descope235MCHFaging_v3.root',
      'out_ana_DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_HLT_descope200MCHF_v3.root',
      'out_ana_DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_HLT_descope200MCHFaging_v3.root',

      'out_ana_DarkSUSY_mH_125_mGammaD_20000_cT_100_14TeV_PU140_HLT_fullScope.root',
      'out_ana_DarkSUSY_mH_125_mGammaD_20000_cT_100_14TeV_PU140_HLT_fullScopeAging.root',
      'out_ana_DarkSUSY_mH_125_mGammaD_20000_cT_100_14TeV_PU140_HLT_descope235MCHFaging.root',
      'out_ana_DarkSUSY_mH_125_mGammaD_20000_cT_100_14TeV_PU140_HLT_descope200MCHF.root',
      'out_ana_DarkSUSY_mH_125_mGammaD_20000_cT_100_14TeV_PU140_HLT_descope200MCHFaging.root',
      ]

inputFiles_80k_pu140 = [
      '/eos/uscms/store/user/lpcgem/DarkSUSY_MH-125_MGammaD-20000_ctau1000_14TeV_madgraph-pythia6-tauola/DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_ANA_fullScope_v3/150825_133549/0000/out_ana.root',
      '/eos/uscms/store/user/lpcgem/DarkSUSY_MH-125_MGammaD-20000_ctau1000_14TeV_madgraph-pythia6-tauola/DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_ANA_fullScopeAging_v3/150825_134302/0000/out_ana.root',
      '/eos/uscms/store/user/lpcgem/DarkSUSY_MH-125_MGammaD-20000_ctau1000_14TeV_madgraph-pythia6-tauola/DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_ANA_descope235MCHF_v3/150825_133955/0000/out_ana.root',
      '/eos/uscms/store/user/lpcgem/DarkSUSY_MH-125_MGammaD-20000_ctau1000_14TeV_madgraph-pythia6-tauola/DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_ANA_descope235MCHFaging_v3/150825_134339/0000/out_ana.root',
      '/eos/uscms/store/user/lpcgem/DarkSUSY_MH-125_MGammaD-20000_ctau1000_14TeV_madgraph-pythia6-tauola/DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_ANA_descope200MCHF_v3/150825_133623/0000/out_ana.root',
      '/eos/uscms/store/user/lpcgem/DarkSUSY_MH-125_MGammaD-20000_ctau1000_14TeV_madgraph-pythia6-tauola/DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_ANA_descope200MCHFaging_v3/150825_134321/0000/out_ana.root',
      ]

inputFiles_80k_pu200 = [
      '/eos/uscms/store/user/lpcgem/DarkSUSY_MH-125_MGammaD-20000_ctau1000_14TeV_madgraph-pythia6-tauola/DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU200_ANA_fullScope_v3/150825_134011/0000/out_ana.root',
      '/eos/uscms/store/user/lpcgem/DarkSUSY_MH-125_MGammaD-20000_ctau1000_14TeV_madgraph-pythia6-tauola/DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU200_ANA_fullScopeAging_v3/150825_134358/0000/out_ana.root',
      '/eos/uscms/store/user/lpcgem/DarkSUSY_MH-125_MGammaD-20000_ctau1000_14TeV_madgraph-pythia6-tauola/DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU200_ANA_descope235MCHF_v3/150825_134044/0000/out_ana.root',
      '/eos/uscms/store/user/lpcgem/DarkSUSY_MH-125_MGammaD-20000_ctau1000_14TeV_madgraph-pythia6-tauola/DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU200_ANA_descope235MCHFaging_v3/150825_134430/0000/out_ana.root',
      '/eos/uscms/store/user/lpcgem/DarkSUSY_MH-125_MGammaD-20000_ctau1000_14TeV_madgraph-pythia6-tauola/DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU200_ANA_descope200MCHF_v3/150825_134028/0000/out_ana.root',
      '/eos/uscms/store/user/lpcgem/DarkSUSY_MH-125_MGammaD-20000_ctau1000_14TeV_madgraph-pythia6-tauola/DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU200_ANA_descope200MCHFaging_v3/150825_134414/0000/out_ana.root',
      ]

highMassExt = [
      '_DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_fullScope_v3',
      '_DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_fullScopeAging_v3',
      '_DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_descope235MCHF_v3',
      '_DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_descope235MCHFaging_v3',
      '_DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_descope200MCHF_v3',
      '_DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_descope200MCHFaging_v3',

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

my_colors = [kBlue, kBlack, kOrange+1, kGreen+1, kMagenta+1, kRed]
my_markers = [2,5,20,21,22,23]
pts = [0,0,15,17,20,25]
my_titles = ["Full scope", "Full scope + CSC/RPC aging", "235MCHF", "235MCHF + CSC/RPC aging", "200MCHF", "200MCHF + CSC/RPC/DT aging"]
dxy_min = 0
dxy_max = 10
for i in range(0,6):
      if i is 2 or i is 4:
            pass
      class Plotter:
            def __init__(self):
                  self.inputDir = inputDir
                  #self.inputFile = inputDir + inputFiles[i]
                  self.inputFile = inputFiles_80k_pu140[i]
                  self.outputDir = preOut #+ outputDirs[i]
                  self.ext = highMassExt[i] + ext
                  self.analyzer = "HLTBendingAngle"
                  self.events = "trk_eff_MU_ALL"
                  self.file = TFile.Open(self.inputFile)
                  self.dirAna = (self.file).Get(self.analyzer)
                  self.tree = (self.dirAna).Get(self.events)            
                  self.hlt = (self.dirAna).Get("trk_hlt")            
                  self.pu = 140
                  self.symb = "Z_{D}"
                  self.ctau = "c#tau(" + self.symb + ") = %d mm"%(highMassCtau[i])
                  self.mass = 'm(' + self.symb + ') = 20 GeV'
                  self.boson = "Z boson"
                  self.debug = False
#                  self.outputFile = outputFile
                  
            
      ## make the plots
      plotter = Plotter()
      #recoHits(plotter)
      #genKinematics(plotter)
      #trackKinematics(plotter)
      if True:
            for i in range(0,len(pts)):
                  sim_pt = pts[i]*1.3
                  if pts[i] is 0:
                        sim_pt = 7
                  my_efficiencies[i].append(recoTrackEfficiency_2(plotter, dxy_min, dxy_max, sim_pt, 0, pts[i]))
      #recoTrackEfficiency(plotter)
      #pTCorrelationPlots(plotter)
   
if True:
      for i in range(0,len(pts)):
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
            base.SetTitle("                                                                      14 TeV,  PU = %d; SimTrack #eta; L2Mu reconstruction efficiency"%(pu))
            base.SetMinimum(0)
            base.SetMaximum(1.1)
            base.GetXaxis().SetLabelSize(0.05)
            base.GetYaxis().SetLabelSize(0.05)
            base.GetXaxis().SetTitleSize(0.06)
            base.GetYaxis().SetTitleSize(0.06)
      #        base.GetXaxis().SetLimits(0,maxbin)
            base.Draw()
            
            leg = TLegend(0.15,0.15,0.55,0.45,"","brNDC")
            leg.SetFillColor(kWhite)
            leg.SetBorderSize(0)
            leg.SetFillStyle(0)
            leg.SetTextSize(0.04)

            for j in range(0,6):
                  if j is 2 or j is 4:
                      continue
                  h = my_efficiencies[i][j]
                  h.SetMarkerColor(my_colors[j])
                  h.SetLineColor(my_colors[j])
                  h.SetLineWidth(2)
                  h.SetMarkerStyle(my_markers[j])
                  h.SetMarkerSize(0.5)
                  h.Draw("same")
                  leg.AddEntry(h,my_titles[j],"lep")


            leg.Draw("same")
            # tex55 = drawLabel("#font[41]{c#tau(Z_{D}) = 1000 mm, m(Z_{D}) = 20 GeV}",0.45,0.55,0.05)
            #tex4 = drawLabel(p.mass,0.55,0.47,0.05)
            # tex3 = drawLabel("H #rightarrow 2n_{1} #rightarrow 2n_{D}2Z_{D} #rightarrow 2n_{D}4#mu",0.45,0.65,0.05)
            tex2 = applyStupidTdrStyle()
            if dxy_min is 0:
                  tex = drawLabel("#font[41]{|d_{xy}| < %d cm}"%(dxy_max),0.7,0.35,0.04)
            else:
                  tex = drawLabel("#font[41]{%d < |d_{xy}| < %d cm}"%(dxy_min, dxy_max),0.7,0.35,0.04)
            tex555 = drawLabel("#font[41]{p_{T}^{RECO} > %d GeV}"%(pts[i]), 0.7,0.28,0.04)
            sim_pt = pts[i]*1.3
            if pts[i] is 0:
                  sim_pt = 7
            tex554 = drawLabel("#font[41]{p_{T}^{SIM} > %d GeV}"%(sim_pt), 0.7,0.21,0.04)
            c.SaveAs("eff_sim_eta_1seg_pt_dxy%dto%d_L1Extra_fid_recoCand_pt%d_combi_DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU%d_v5.png"%(dxy_min, dxy_max, pts[i], pu))





