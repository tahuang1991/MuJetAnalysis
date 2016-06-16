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

inputDir = "/afs/cern.ch/user/d/dildick/work/GEM/forJose/DisplacedMuHLTStudyPtAssignment/CMSSW_7_4_4/src/"
inputDir = "/uscms_data/d3/dildick/work/MuonPhaseIIScopeDoc/CMSSW_6_2_0_SLHC26_patch3/src/"
preOut = "/uscms_data/d3/dildick/work/MuonPhaseIIScopeDoc/CMSSW_6_2_0_SLHC26_patch3/src/OutputDirectoryForScopeDoc_20150930/"
ext = ".png"
pu=140

highMassExt_ctau100 = [
      '_DarkSUSY_mH_125_mGammaD_20000_cT_100_14TeV_PU140_fullScope_v1',
      '_DarkSUSY_mH_125_mGammaD_20000_cT_100_14TeV_PU140_fullScopeAging_v1',
      '_DarkSUSY_mH_125_mGammaD_20000_cT_100_14TeV_PU140_descope235MCHF_v1',
      '_DarkSUSY_mH_125_mGammaD_20000_cT_100_14TeV_PU140_descope235MCHFaging_v1',
      '_DarkSUSY_mH_125_mGammaD_20000_cT_100_14TeV_PU140_descope200MCHF_v1',
      '_DarkSUSY_mH_125_mGammaD_20000_cT_100_14TeV_PU140_descope200MCHFaging_v1'
      ]

highMassExt_ctau1000 = [
      '_DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_fullScope_v3',
      '_DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_fullScopeAging_v3',
      '_DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_descope235MCHF_v3',
      '_DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_descope235MCHFaging_v3',
      '_DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_descope200MCHF_v3',
      '_DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_descope200MCHFaging_v3'
      ]

highMassCtau = [100,100,100,100,100,100,
                100,100,100,100,100]

highMassPU = [140,140,140,140,140,140,
              140,140,140,140,140,140]

#outputFile = TFile("output.root","NEW")

efficiencies_3st = []
efficiencies_3seg = []
efficiencies_2seg1rh = []
efficiencies_2seg1rh_gem_endcap = []
efficiencies_2seg1rh_ge21_endcap = []
efficiencies_2seg1rh_ge21_noCSCst2_endcap = []

scenarios = ["Full scope", "Full scope + CSC/RPC aging", "235MCHF", "235MCHF + CSC/RPC aging", "200MCHF", "200MCHF + CSC/RPC/DT aging"]
patterns = ["3 stations", "3seg", "2seg+1rh", "2seg+gem", "2seg+GE21", "2seg+GE21, no ME2/1"]
patterns = ["3 stations", "3seg", "2seg+1rh", "2seg+GE11", "2seg+GE11, no GE21", "2seg+GE21"]
patterns = ["3 stations", "2seg+1rh", "2seg+gem", "2seg+GE11", "2seg+GE11, no GE21", "2seg+GE21, no GE11"]
patterns = ["3 stations", "2seg+1rh", "2seg+gem", "2seg+GE11, no GE21", "2seg+GE21", "2seg+GE21, no ME21"]

my_colors = [kBlue, kBlack, kOrange+1, kGreen+1, kMagenta+1, kRed]
my_markers = [2,5,20,21,22,23]


for sc in scenarios:
      efficiencies_3st.append([])
      efficiencies_3seg.append([])
      efficiencies_2seg1rh.append([])
      efficiencies_2seg1rh_gem_endcap.append([])
      efficiencies_2seg1rh_ge21_endcap.append([])
      efficiencies_2seg1rh_ge21_noCSCst2_endcap.append([])

pts = [0,0,5,10,15, 20]
#pts = [10]
dxy_min = 0
dxy_max = 5

## loop on scenarios
for i in range(0,6):
      #if i is 2 or i is 4:
      #      continue
      class Plotter:
            def __init__(self):
                  self.inputDir = inputDir
                  self.inputFile = inputFiles_80k_pu140_ctau100[i]
                  print self.inputFile
                  #self.inputFile = "/eos/uscms/store/user/lpcgem/DarkSUSY_MH-125_MGammaD-20000_ctau100_14TeV_madgraph-pythia6-tauola/DarkSUSY_mH_125_mGammaD_20000_cT_100_14TeV_PU140_ANA_fullScope_v3/150923_031008/0000/out_ana.root"
                  # "out_ana_DarkSUSY_mH_125_mGammaD_20000_cT_100_14TeV_PU140_HLT_fullScope.root" # inputFiles_80k_pu140_ctau100[i]
                  self.outputDir = preOut #+ outputDirs[i]
                  self.ext = highMassExt_ctau100[i] + ext
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
                  
            
      ## make the plots
      plotter = Plotter()
      if False:
            for j in range(0,6):
                  reco_pt = pts[j]
                  sim_pt = reco_pt*1.2
                  if reco_pt is 0:
                        sim_pt = 7
                  print "sim_pt, reco_pt", sim_pt, reco_pt
                  efficiencies_3st[i].append(recoTrackEfficiency_2(plotter, dxy_min, dxy_max, sim_pt, 0, reco_pt))
                  efficiencies_3seg[i].append(recoTrackEfficiency_2(plotter, dxy_min, dxy_max, sim_pt, 0, reco_pt, cand_3_st_2_segments_1_rechit()))
                  efficiencies_2seg1rh[i].append(recoTrackEfficiency_2(plotter, dxy_min, dxy_max, sim_pt, 0, reco_pt, cand_3_st_2_segments_1_rechit_gem_endcap()))
                  efficiencies_2seg1rh_gem_endcap[i].append(recoTrackEfficiency_2(plotter, dxy_min, dxy_max, sim_pt, 0, reco_pt, cand_3_st_2_segments_1_rechit_GE11_no_GE21_endcap()))
                  efficiencies_2seg1rh_ge21_endcap[i].append(recoTrackEfficiency_2(plotter, dxy_min, dxy_max, sim_pt, 0, reco_pt, cand_3_st_2_segments_1_rechit_GE21_endcap()))
                  efficiencies_2seg1rh_ge21_noCSCst2_endcap[i].append(recoTrackEfficiency_2(plotter, dxy_min, dxy_max, sim_pt, 0, reco_pt, cand_3_st_2_segments_1_rechit_GE21_no_ME21_endcap()))
   
all_efficiencies = []
all_efficiencies.append(efficiencies_3st)
all_efficiencies.append(efficiencies_3seg)
all_efficiencies.append(efficiencies_2seg1rh)
all_efficiencies.append(efficiencies_2seg1rh_gem_endcap)
all_efficiencies.append(efficiencies_2seg1rh_ge21_endcap)
all_efficiencies.append(efficiencies_2seg1rh_ge21_noCSCst2_endcap)

print all_efficiencies

for i in range(0,len(pts)):
      reco_pt = pts[i]
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
            #if j is 2 or j is 4:
            #      continue
            h = all_efficiencies[j][1][i]
            h.SetMarkerColor(my_colors[j])
            h.SetLineColor(my_colors[j])
            h.SetLineWidth(2)
            h.SetMarkerStyle(my_markers[j])
            h.SetMarkerSize(0.5)
            h.Draw("same")
            #leg.AddEntry(h,scenarios[j],"lep")
            leg.AddEntry(h,patterns[j],"lep")
            
      leg.Draw("same")
      # tex55 = drawLabel("#font[41]{c#tau(Z_{D}) = 1000 mm, m(Z_{D}) = 20 GeV}",0.45,0.55,0.05)
      # tex4 = drawLabel(p.mass,0.55,0.47,0.05)
      # tex3 = drawLabel("H #rightarrow 2n_{1} #rightarrow 2n_{D}2Z_{D} #rightarrow 2n_{D}4#mu",0.45,0.65,0.05)
      tex2 = applyTdrStyle()
      if dxy_min is 0:
            tex = drawLabel("#font[41]{|d_{xy}| < %d cm}"%(dxy_max),0.7,0.35,0.04)
      else:
            tex = drawLabel("#font[41]{%d < |d_{xy}| < %d cm}"%(dxy_min, dxy_max),0.7,0.35,0.04)
      tex555 = drawLabel("#font[41]{p_{T}^{RECO} > %d GeV}"%(reco_pt), 0.7,0.28,0.04)
      sim_pt = reco_pt*1.2
      if reco_pt is 0:
            sim_pt = 7
      tex554 = drawLabel("#font[41]{p_{T}^{SIM} > %d GeV}"%(sim_pt), 0.7,0.21,0.04)
      c.SaveAs("%seff_sim_eta_1seg_pt%d_dxy%dto%d_L1Extra_fid_recoCand_pt%d_combi_DarkSUSY_mH_125_mGammaD_20000_cT_100_14TeV_PU%d_v1%s" 
               %(preOut, sim_pt, dxy_min, dxy_max, reco_pt, pu, ext))





