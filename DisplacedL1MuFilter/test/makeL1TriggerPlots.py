import sys
from ROOT import *
from ROOT import TH1F

# run quiet mode
import sys
sys.argv.append( '-b' )

import ROOT 
ROOT.gROOT.SetBatch(1)
from Helpers import *

def exit():
  sys.exit(0)

if __name__ == "__main__":  

  """
  inputFile = 'out_filter_ana.test.root'
  inputFile = 'out_filter_ana_SingleMuPlusFlatPt0p2To150_TTI2023Upg14D_PU140bx25_ILT_SLHC14.root'
  inputFile = 'out_filter_ana.10k.root'
  inputFile = 'out_filter_ana.test10k.root'
  inputFile = 'out_filter_ana.test10000.root'
  inputFile = 'out_filter_ana.test100000.root'
  """
  inputFile = 'out_filter_ana_Neutrino_Pt2to20_gun_TTI2023Upg14D_PU140bx25_ILT_SLHC14.root'
  targetDir = './'

  ## extension for figures - add more?
  ext = ".png"
  
  ## Trees
  analyzer = "DisplacedL1MuFilter_PhaseIIGE21"
  recHits = "L1MuTree"

  ## Style
  gStyle.SetStatStyle(0);

  ## input
  file = TFile.Open(inputFile)
  if not file:
    sys.exit('Input ROOT file %s is missing.' %(inputFile))

  dirAna = file.Get(analyzer)
  if not dirAna:
    sys.exit('Directory %s does not exist.' %(dirAna))
    
  treeHits = dirAna.Get(recHits)
  if not treeHits:
    sys.exit('Tree %s does not exist.' %(treeHits))
  
  print "Making the plots"


  set_style()


  c = TCanvas("c","c",800,600)
  c.Clear()    
  gStyle.SetTitleBorderSize(0);
  gStyle.SetPadLeftMargin(0.126);
  gStyle.SetPadRightMargin(0.04);
  gStyle.SetPadTopMargin(0.06);
  gStyle.SetPadBottomMargin(0.13);
  gPad.SetLogy(1)

  b1 = TH1F("b1","b1",29,myptbin)
  b1.GetYaxis().SetRangeUser(.1,10000)
  b1.GetYaxis().SetTitleOffset(1.2)
  b1.GetYaxis().SetNdivisions(520)
  b1.GetYaxis().SetTitle("L1 Trigger Rate [kHz]")
  b1.GetXaxis().SetTitle("L1 muon p_{T} threshold [GeV]")
  b1.GetXaxis().SetTitleFont(62)
  b1.GetXaxis().SetTitleOffset(1.2)
  b1.GetXaxis().SetTitleSize(0.045)
  b1.SetTitle("CMS Simulation Preliminary"+" "*26 +" PU140, 14TeV")
  b1.SetStats(0)
  b1.Draw()

  h_single_L1Mu_rate = TH1F("h_single_L1Mu_rate"," ",len(myptbin)-1, myptbin)
  h_single_displaced_rate = TH1F("h_single_displaced_rate"," ",len(myptbin)-1, myptbin)
  h_single_displaced_rate_L1Tk_pt3 = TH1F("h_single_displaced_rate_L1Tk_pt3"," ",len(myptbin)-1, myptbin)
  h_single_displaced_rate_L1Tk_pt4 = TH1F("h_single_displaced_rate_L1Tk_pt4"," ",len(myptbin)-1, myptbin)

  for k in range(0,treeHits.GetEntries()): #
    treeHits.GetEntry(k)

    ## get the max value of the momentum
    pts = list(treeHits.pt)
    if len(pts)>=1:
      
      ## single L1Mu trigger rate
      maxPt = 0.
      for i in range(0,len(pts)):
        if treeHits.bx[i]!=0 or treeHits.quality[i]<4:
          continue
        
        ## get the max pt for an event        
        if treeHits.pt[i]>maxPt:
          maxPt = treeHits.pt[i]

      if maxPt>0:
        h_single_L1Mu_rate.Fill(maxPt)
        
      ## displaced trigger: at least 1 muon that is not matched or unmatched 
      maxPt = 0.
      for i in range(0,len(pts)):
        if treeHits.bx[i]!=0 or treeHits.isMatched[i]==1 or treeHits.isUnMatched[i]==1 or treeHits.quality[i]<4:
          continue

        if treeHits.pt[i]>maxPt:
          maxPt = treeHits.pt[i]

      if maxPt>0:
        h_single_displaced_rate.Fill(maxPt)

      ## displaced trigger: at least 1 muon that is not matched or unmatched (Pt cut on non-matching L1Tk)
      maxPt = 0.
      for i in range(0,len(pts)):
        if treeHits.bx[i]!=0 or treeHits.isMatched[i]==1 or treeHits.isUnMatchedL1TkPt3[i]==1 or treeHits.quality[i]<4:
          continue

        if treeHits.pt[i]>maxPt:
          maxPt = treeHits.pt[i]

      if maxPt>0:
        h_single_displaced_rate_L1Tk_pt3.Fill(maxPt)

      ## displaced trigger: at least 1 muon that is not matched or unmatched (Pt cut on non-matching L1Tk)
      maxPt = 0.
      for i in range(0,len(pts)):
        if treeHits.bx[i]!=0 or treeHits.isMatched[i]==1 or treeHits.isUnMatchedL1TkPt4[i]==1 or treeHits.quality[i]<4:
          continue

        if treeHits.pt[i]>maxPt:
          maxPt = treeHits.pt[i]

      if maxPt>0:
        h_single_displaced_rate_L1Tk_pt4.Fill(maxPt)

    """
      print k, len(pts), oneL1MuNotMatchedNotUnMatched, oneL1MuNotMatchedNotUnMatchedPts, oneL1MuNotMatchedNotUnMatchedMaxPt
    else:
      print k
    """
      
  h_single_L1Mu_rate = getRatePtHistogram(treeHits, h_single_L1Mu_rate)
  h_single_L1Mu_rate.SetFillColor(kRed)
  h_single_L1Mu_rate.Draw("e3same")

  h_single_displaced_rate = getRatePtHistogram(treeHits, h_single_displaced_rate)
  h_single_displaced_rate.SetFillColor(kGreen+2)
  h_single_displaced_rate.Draw("e3same")

  h_single_displaced_rate_L1Tk_pt3 = getRatePtHistogram(treeHits, h_single_displaced_rate_L1Tk_pt3)
  h_single_displaced_rate_L1Tk_pt3.SetFillColor(kBlue)
  h_single_displaced_rate_L1Tk_pt3.Draw("e3same")

  h_single_displaced_rate_L1Tk_pt4 = getRatePtHistogram(treeHits, h_single_displaced_rate_L1Tk_pt4)
  h_single_displaced_rate_L1Tk_pt4.SetFillColor(kBlue)
  h_single_displaced_rate_L1Tk_pt4.Draw("e3same")

  leg = TLegend(0.2,0.7,0.9,0.9,"","brNDC")
  leg.SetFillColor(kWhite)
  leg.SetBorderSize(0)
  leg.SetFillStyle(0)
  leg.SetTextSize(0.03)
  leg.AddEntry(h_single_L1Mu_rate,"Single L1Mu", "f")
  leg.AddEntry(h_single_displaced_rate,"Displaced L1Mu (p_{T} #geq 0 GeV on non-matching L1Tk)", "f")
  leg.AddEntry(h_single_displaced_rate_L1Tk_pt3,"Displaced L1Mu (p_{T} #geq 3 GeV on non-matching L1Tk)", "f")
  leg.AddEntry(h_single_displaced_rate_L1Tk_pt4,"Displaced L1Mu (p_{T} #geq 4 GeV on non-matching L1Tk)", "f")
  leg.Draw("same")
  c.SaveAs("L1Mu_trigger_rate_pt_PU140_14TeV.png")
    
  exit()


  def makeRateVsEtaHistogram(ptCut):

    c = TCanvas("c","c",800,600)
    c.Clear()    
    gStyle.SetTitleBorderSize(0);
    gStyle.SetPadLeftMargin(0.126);
    gStyle.SetPadRightMargin(0.04);
    gStyle.SetPadTopMargin(0.06);
    gStyle.SetPadBottomMargin(0.13);
    gPad.SetLogy(1)

    b1 = TH1F("b1","b1",29,myptbin)
    b1.GetYaxis().SetRangeUser(.1,10000)
    b1.GetYaxis().SetTitleOffset(1.2)
    b1.GetYaxis().SetNdivisions(520)
    b1.GetYaxis().SetTitle("L1 Trigger Rate [kHz]")
    b1.GetXaxis().SetTitle("L1 muon #eta")
    b1.GetXaxis().SetTitleFont(62)
    b1.GetXaxis().SetTitleOffset(1.2)
    b1.GetXaxis().SetTitleSize(0.045)
    b1.SetTitle("CMS Simulation Preliminary"+" "*26 +" PU140, 14TeV")
    b1.SetStats(0)
    b1.Draw()

    h_single_L1Mu_rate = TH1F("h_single_L1Mu_rate"," ",len(myptbin)-1, myptbin)
    h_single_displaced_rate = TH1F("h_single_displaced_rate"," ",len(myptbin)-1, myptbin)
    h_single_displaced_rate_L1Tk_pt3 = TH1F("h_single_displaced_rate_L1Tk_pt3"," ",len(myptbin)-1, myptbin)
    h_single_displaced_rate_L1Tk_pt4 = TH1F("h_single_displaced_rate_L1Tk_pt4"," ",len(myptbin)-1, myptbin)
    

    for k in range(0,treeHits.GetEntries()): #
      treeHits.GetEntry(k)

      ## get the max value of the momentum
      pts = list(treeHits.pt)
      if len(pts)>=1:
      
        ## single L1Mu trigger rate
        maxPt = 0.
        maxPtIndex = -1
        for i in range(0,len(pts)):

          if treeHits.pt[i]<ptCut:
            continue
          
          if treeHits.bx[i]!=0 or treeHits.quality[i]<4:
            continue
        
          ## get the max pt for an event        
          if treeHits.pt[i]>maxPt:
            maxPt = treeHits.pt[i]
            maxPtIndex = i

        if maxPt>0:
          h_single_L1Mu_rate.Fill(abs(treeHits.eta[maxPtIndex]))
        
        ## displaced trigger: at least 1 muon that is not matched or unmatched 
        maxPt = 0.
        maxPtIndex = -1
        for i in range(0,len(pts)):
          if treeHits.pt[i]<ptCut:
            continue

          if treeHits.bx[i]!=0 or treeHits.isMatched[i]==1 or treeHits.isUnMatched[i]==1 or treeHits.quality[i]<4:
            continue

        if treeHits.pt[i]>maxPt:
          maxPt = treeHits.pt[i]
          maxPtIndex = i

        if maxPt>0:
          h_single_displaced_rate.Fill(abs(treeHits.eta[maxPtIndex]))

        ## displaced trigger: at least 1 muon that is not matched or unmatched (Pt cut on non-matching L1Tk)
        maxPt = 0.
        maxPtIndex = -1
        for i in range(0,len(pts)):
          if treeHits.pt[i]<ptCut:
            continue

          if treeHits.bx[i]!=0 or treeHits.isMatched[i]==1 or treeHits.isUnMatchedL1TkPt3[i]==1 or treeHits.quality[i]<4:
            continue

          if treeHits.pt[i]>maxPt:
            maxPt = treeHits.pt[i]
            maxPtIndex = i

        if maxPt>0:
          h_single_displaced_rate_L1Tk_pt3.Fill(abs(treeHits.eta[maxPtIndex]))

        ## displaced trigger: at least 1 muon that is not matched or unmatched (Pt cut on non-matching L1Tk)
        maxPt = 0.
        maxPtIndex = -1
        for i in range(0,len(pts)):
          if treeHits.pt[i]<ptCut:
            continue

          if treeHits.bx[i]!=0 or treeHits.isMatched[i]==1 or treeHits.isUnMatchedL1TkPt4[i]==1 or treeHits.quality[i]<4:
            continue

          if treeHits.pt[i]>maxPt:
            maxPt = treeHits.pt[i]
            maxPtIndex = i

        if maxPt>0:
          h_single_displaced_rate_L1Tk_pt4.Fill(abs(treeHits.eta[maxPtIndex]))


    h_single_L1Mu_rate = getRateEtaHistogram(treeHits, h_single_L1Mu_rate)
    h_single_L1Mu_rate.SetFillColor(kRed)
    h_single_L1Mu_rate.Draw("e3same")

    h_single_displaced_rate = getRateEtaHistogram(treeHits, h_single_displaced_rate)
    h_single_displaced_rate.SetFillColor(kGreen+2)
    h_single_displaced_rate.Draw("e3same")

    h_single_displaced_rate_L1Tk_pt3 = getRateEtaHistogram(treeHits, h_single_displaced_rate_L1Tk_pt3)
    h_single_displaced_rate_L1Tk_pt3.SetFillColor(kBlue)
    h_single_displaced_rate_L1Tk_pt3.Draw("e3same")

    h_single_displaced_rate_L1Tk_pt4 = getRateEtaHistogram(treeHits, h_single_displaced_rate_L1Tk_pt4)
    h_single_displaced_rate_L1Tk_pt4.SetFillColor(kBlue)
    h_single_displaced_rate_L1Tk_pt4.Draw("e3same")

    leg = TLegend(0.2,0.7,0.9,0.9,"","brNDC")
    leg.SetFillColor(kWhite)
    leg.SetBorderSize(0)
    leg.SetFillStyle(0)
    leg.SetTextSize(0.03)
    leg.AddEntry(h_single_L1Mu_rate,"Single L1Mu", "f")
    leg.AddEntry(h_single_displaced_rate,"Displaced L1Mu (p_{T} #geq 0 GeV on non-matching L1Tk)", "f")
    leg.AddEntry(h_single_displaced_rate_L1Tk_pt3,"Displaced L1Mu (p_{T} #geq 3 GeV on non-matching L1Tk)", "f")
    leg.AddEntry(h_single_displaced_rate_L1Tk_pt4,"Displaced L1Mu (p_{T} #geq 4 GeV on non-matching L1Tk)", "f")
    leg.Draw("same")
    c.SaveAs("L1Mu_trigger_rate_eta_ptCut_%d_PU140_14TeV_.png"%(ptCut))

  makeRateVsEtaHistogram(10)
  makeRateVsEtaHistogram(15)
  makeRateVsEtaHistogram(20)


def fitSigma():
    ### fits to get the sigma
    c = TCanvas("c","c",800,600)
    c.Clear()
    gStyle.SetTitleBorderSize(0);
    gStyle.SetPadLeftMargin(0.126);
    gStyle.SetPadRightMargin(0.04);
    gStyle.SetPadTopMargin(0.06);
    gStyle.SetPadBottomMargin(0.13);
    treeHits.Draw("abs(dEta_sim_corr)>>h_name(100,0,0.1)")
    h = TH1F(gDirectory.Get("h_name").Clone("h_name"))
    if not h:
      sys.exit('h does not exist')
    h.SetTitle("PU = 140, 14 TeV; |d#eta_{corr}(L1Mu,SIM)|; Entries")
    h.SetLineWidth(2)
    h.SetLineColor(kBlue)
    h.GetXaxis().SetLabelSize(0.05)
    h.GetYaxis().SetLabelSize(0.05)
    h.GetXaxis().SetTitleSize(0.06)
    h.GetYaxis().SetTitleSize(0.06)
    h.Draw()
    h.SaveAs("dEta_sim_corr_fit.root")
  
    c = TCanvas("c","c",800,600)
    c.Clear()
    gStyle.SetTitleBorderSize(0);
    gStyle.SetPadLeftMargin(0.126);
    gStyle.SetPadRightMargin(0.04);
    gStyle.SetPadTopMargin(0.06);
    gStyle.SetPadBottomMargin(0.13);
    treeHits.Draw("abs(dPhi_sim_corr)>>h_name(100,0,0.1")
    h = TH1F(gDirectory.Get("h_name").Clone("h_name"))
    if not h:
      sys.exit('h does not exist')
    h.SetTitle("PU = 140, 14 TeV; |d#phi_{corr}(L1Mu,SIM)|; Entries")
    h.SetLineWidth(2)
    h.SetLineColor(kBlue)
    h.GetXaxis().SetLabelSize(0.05)
    h.GetYaxis().SetLabelSize(0.05)
    h.GetXaxis().SetTitleSize(0.06)
    h.GetYaxis().SetTitleSize(0.06)
    h.Fit("gaus","L")
    h.Draw()
    h.SaveAs("dPhi_sim_corr_fit.root")

    c = TCanvas("c","c",800,600)
    c.Clear()
    gStyle.SetTitleBorderSize(0);
    gStyle.SetPadLeftMargin(0.126);
    gStyle.SetPadRightMargin(0.04);
    gStyle.SetPadTopMargin(0.06);
    gStyle.SetPadBottomMargin(0.13);
    treeHits.Draw("abs(dEta_L1Tk_corr)>>h_name(100,0,0.1)")
    h = TH1F(gDirectory.Get("h_name").Clone("h_name"))
    if not h:
      sys.exit('h does not exist')
    h.SetTitle("PU = 140, 14 TeV; |d#eta_{corr}(L1Mu,L1TK)|; Entries")
    h.SetLineWidth(2)
    h.SetLineColor(kBlue)
    h.GetXaxis().SetLabelSize(0.05)
    h.GetYaxis().SetLabelSize(0.05)
    h.GetXaxis().SetTitleSize(0.06)
    h.GetYaxis().SetTitleSize(0.06)
    h.Draw()
    h.SaveAs("dEta_L1Tk_corr_fit.root")
  
    c = TCanvas("c","c",800,600)
    c.Clear()
    gStyle.SetTitleBorderSize(0);
    gStyle.SetPadLeftMargin(0.126);
    gStyle.SetPadRightMargin(0.04);
    gStyle.SetPadTopMargin(0.06);
    gStyle.SetPadBottomMargin(0.13);
    treeHits.Draw("abs(dPhi_L1Tk_corr)>>h_name(100,0,0.1")
    h = TH1F(gDirectory.Get("h_name").Clone("h_name"))
    if not h:
      sys.exit('h does not exist')
    h.SetTitle("PU = 140, 14 TeV; |d#phi_{corr}(L1Mu,L1TK)|; Entries")
    h.SetLineWidth(2)
    h.SetLineColor(kBlue)
    h.GetXaxis().SetLabelSize(0.05)
    h.GetYaxis().SetLabelSize(0.05)
    h.GetXaxis().SetTitleSize(0.06)
    h.GetYaxis().SetTitleSize(0.06)
    h.Fit("gaus","L")
    h.Draw()
    h.SaveAs("dPhi_L1Tk_corr_fit.root")


  ### regular plots
  draw_1D(treeHits,"abs(dEta_sim_corr)",  "dEta_sim_corr",  "PU = 140, 14 TeV; |d#eta_{corr}(L1Mu,SIM)|; Entries", "(100,0,1)")
  draw_1D(treeHits,"abs(dPhi_sim_corr)",  "dPhi_sim_corr",  "PU = 140, 14 TeV; |d#phi_{corr}(L1Mu,SIM)|; Entries", "(100,0,1)")

  draw_1D(treeHits,"dR_sim_corr",  "dR_sim_corr",  "PU = 140, 14 TeV; |dR_{corr}(L1Mu,SIM)|; Entries", "(100,0,0.2)")
  draw_1D(treeHits,"dR_sim_corr",  "dR_sim_corr_fid",  "PU = 140, 14 TeV; |dR_{corr}(L1Mu,SIM)|; Entries", "(100,0,0.2)",TCut("abs(eta)<=2.5"))
  draw_1D(treeHits,"dR_sim_corr",  "dR_sim_corr_pt10_fid",  "PU = 140, 14 TeV; |dR_{corr}(L1Mu,SIM)|; Entries", "(100,0,0.2)",TCut("pt>=10 && abs(eta)<=2.5"))
  draw_1D(treeHits,"dR_sim_corr",  "dR_sim_corr_pt15_fid",  "PU = 140, 14 TeV; |dR_{corr}(L1Mu,SIM)|; Entries", "(100,0,0.2)",TCut("pt>=15 && abs(eta)<=2.5"))
  draw_1D(treeHits,"dR_sim_corr",  "dR_sim_corr_pt20_fid",  "PU = 140, 14 TeV; |dR_{corr}(L1Mu,SIM)|; Entries", "(100,0,0.2)",TCut("pt>=20 && abs(eta)<=2.5"))

  draw_1D(treeHits,"abs(dEta_sim_prop)",  "dEta_sim_prop",  "PU = 140, 14 TeV; |d#eta_{corr}(L1Mu,SIM)|; Entries", "(100,0,1)")
  draw_1D(treeHits,"abs(dPhi_sim_prop)",  "dPhi_sim_prop",  "PU = 140, 14 TeV; |d#phi_{corr}(L1Mu,SIM)|; Entries", "(100,0,1)")

  draw_1D(treeHits,"dR_sim_prop",  "dR_sim_prop",  "PU = 140, 14 TeV; |dR_{prop}(L1Mu,SIM)|; Entries", "(100,0,0.2)")
  draw_1D(treeHits,"dR_sim_prop",  "dR_sim_prop_fid",  "PU = 140, 14 TeV; |dR_{prop}(L1Mu,SIM)|; Entries", "(100,0,0.2)",TCut("abs(eta)<=2.5"))
  draw_1D(treeHits,"dR_sim_prop",  "dR_sim_prop_pt10_fid",  "PU = 140, 14 TeV; |dR_{prop}(L1Mu,SIM)|; Entries", "(100,0,0.2)",TCut("pt>=10 && abs(eta)<=2.5"))
  draw_1D(treeHits,"dR_sim_prop",  "dR_sim_prop_pt15_fid",  "PU = 140, 14 TeV; |dR_{prop}(L1Mu,SIM)|; Entries", "(100,0,0.2)",TCut("pt>=15 && abs(eta)<=2.5"))
  draw_1D(treeHits,"dR_sim_prop",  "dR_sim_prop_pt20_fid",  "PU = 140, 14 TeV; |dR_{prop}(L1Mu,SIM)|; Entries", "(100,0,0.2)",TCut("pt>=20 && abs(eta)<=2.5"))

  draw_1D(treeHits,"pt",  "pt_L1",  "p_{T,L1} [GeV]", "(100,0,200)")
  draw_1D(treeHits,"eta",  "eta_L1",  "#eta_{L1}", "(60,-3,3)")
  draw_1D(treeHits,"phi",  "phi_L1",  "#phi_{L1}", "(70,-3.5,3.5)")
  draw_1D(treeHits,"quality",  "quality",  "quality", "(10,0,10)")
  draw_1D(treeHits,"charge",  "charge",  "charge", "(5,-2,2)")

  draw_2D(treeHits,"dPhi_sim_corr:dEta_sim_prop",  "dEta_dPhi_sim_prop",  "PU = 140, 14 TeV; |d#eta_{corr}(L1Mu,SIM)|; |d#phi_{corr}(L1Mu,SIM)|", "(100,0,0.2,100,0,0.2)")
  draw_2D(treeHits,"dPhi_sim_prop:dEta_sim_prop",  "dEta_dPhi_sim_prop",  "PU = 140, 14 TeV; |d#eta_{prop}(L1Mu,SIM)|; |d#phi_{prop}(L1Mu,SIM)|", "(100,0,0.2,100,0,0.2)")


  draw_1D(treeHits,"dEta_L1Tk_corr",  "dEta_L1Tk_corr",  "PU = 140, 14 TeV; |d#eta_{corr}(L1Mu,L1Tk)|; Entries", "(100,0,1)")
  draw_1D(treeHits,"dPhi_L1Tk_corr",  "dPhi_L1Tk_corr",  "PU = 140, 14 TeV; |d#phi_{corr}(L1Mu,L1Tk)|; Entries", "(100,0,1)")

  draw_1D(treeHits,"dR_L1Tk_corr",  "dR_L1Tk_corr",  "PU = 140, 14 TeV; |dR_{prop}(L1Mu,L1Tk)|; Entries", "(100,0,1)")
  draw_1D(treeHits,"dR_L1Tk_corr",  "dR_L1Tk_corr_pt10_fid",  "PU = 140, 14 TeV; |dR_{prop}(L1Mu,L1Tk)|; Entries", "(100,0,1)",TCut("pt>=10 && abs(eta)<=2.5"))
  draw_1D(treeHits,"dR_L1Tk_corr",  "dR_L1Tk_corr_pt20_fid",  "PU = 140, 14 TeV; |dR_{prop}(L1Mu,L1Tk)|; Entries", "(100,0,1)",TCut("pt>=20 && abs(eta)<=2.5"))

  draw_1D(treeHits,"dEta_L1Tk_prop",  "dEta_L1Tk_prop",  "PU = 140, 14 TeV; |d#eta_{prop}(L1Mu,L1Tk)|; Entries", "(100,0,1)")
  draw_1D(treeHits,"dPhi_L1Tk_prop",  "dPhi_L1Tk_prop",  "PU = 140, 14 TeV; |d#phi_{prop}(L1Mu,L1Tk)|; Entries", "(100,0,1)")

  draw_1D(treeHits,"dR_L1Tk_prop",  "dR_L1Tk_prop",  "PU = 140, 14 TeV; |dR_{prop}(L1Mu,L1Tk)|; Entries", "(100,0,1)")
  draw_1D(treeHits,"dR_L1Tk_prop",  "dR_L1Tk_prop_pt10_fid",  "PU = 140, 14 TeV; |dR_{prop}(L1Mu,L1Tk)|; Entries", "(100,0,1)",TCut("pt>=10 && abs(eta)<=2.5"))
  draw_1D(treeHits,"dR_L1Tk_prop",  "dR_L1Tk_prop_pt20_fid",  "PU = 140, 14 TeV; |dR_{prop}(L1Mu,L1Tk)|; Entries", "(100,0,1)",TCut("pt>=20 && abs(eta)<=2.5"))

  draw_2D(treeHits,"dPhi_L1Tk_corr:dEta_L1Tk_prop",  "dEta_dPhi_L1Tk_prop",  "PU = 140, 14 TeV; |d#eta_{corr}(L1Mu,L1TK)|; |d#phi_{corr}(L1Mu,L1TK)|", "(100,0,1,100,0,1)")
  draw_2D(treeHits,"dPhi_L1Tk_prop:dEta_L1Tk_prop",  "dEta_dPhi_L1Tk_prop",  "PU = 140, 14 TeV; |d#eta_{prop}(L1Mu,L1TK)|; |d#phi_{prop}(L1Mu,L1TK)|", "(100,0,1,100,0,1)")


  draw_1D(treeHits,"dEta_sim_L1Tk",  "dEta_sim_L1Tk",  "PU = 140, 14 TeV; |d#eta(SIM,L1Tk)|; Entries", "(100,0,0.05)")
  draw_1D(treeHits,"dPhi_sim_L1Tk",  "dPhi_sim_L1Tk",  "PU = 140, 14 TeV; |d#phi(SIM,L1Tk)|; Entries", "(100,0,0.05)")


  etaBinning = "(25,0,2.5)"

  makeEtaEffPlot(getEffObject(treeHits, "abs(eta_sim)", etaBinning, TCut(""), TCut("pt_sim>=0")), "eff_sim_eta_pt0_sim", "")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta_sim)", etaBinning, TCut(""), TCut("pt_sim>=10")), "eff_sim_eta_pt10_sim", "")

  makeEtaEffPlot(getEffObject(treeHits, "abs(eta_sim)", etaBinning, AND(TCut("pt_sim>=10"), TCut("abs(dR_sim_prop)<=0.2")), TCut("abs(dR_L1Tk_prop)<=0.12") ), "eff_sim_eta_pt10_L1MuDR02_dR012_L1Tk_prop", 
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 10 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta_sim)", etaBinning, AND(TCut("pt_sim>=10"), TCut("abs(dR_sim_corr)<=0.2")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_sim_eta_pt10_L1MuDR02_dR012_L1Tk_prop", 
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 10 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta_sim)", etaBinning, AND(TCut("pt_sim>=15"), TCut("abs(dR_sim_prop)<=0.2")), TCut("abs(dR_L1Tk_prop)<=0.12") ), "eff_sim_eta_pt15_L1MuDR02_dR012_L1Tk_prop", 
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 15 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta_sim)", etaBinning, AND(TCut("pt_sim>=15"), TCut("abs(dR_sim_corr)<=0.2")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_sim_eta_pt15_L1MuDR02_dR012_L1Tk_prop", 
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 15 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta_sim)", etaBinning, AND(TCut("pt_sim>=20"), TCut("abs(dR_sim_prop)<=0.2")), TCut("abs(dR_L1Tk_prop)<=0.12") ), "eff_sim_eta_pt20_L1MuDR02_dR012_L1Tk_prop", 
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 20 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta_sim)", etaBinning, AND(TCut("pt_sim>=20"), TCut("abs(dR_sim_corr)<=0.2")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_sim_eta_pt20_L1MuDR02_dR012_L1Tk_prop", 
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 20 GeV, dR(L1Tk,L1Mu)<=0.12")

  makeEtaEffPlot(getEffObject(treeHits, "abs(eta_sim)", etaBinning, AND(TCut("pt_sim>=10"), TCut("abs(dR_sim_corr)<=0.2")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_sim_eta_pt10_L1MuDR02_dR012_L1Tk_corr", 
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 10 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta_sim)", etaBinning, AND(TCut("pt_sim>=10"), TCut("abs(dR_sim_corr)<=0.2")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_sim_eta_pt10_L1MuDR02_dR012_L1Tk_corr", 
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 10 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta_sim)", etaBinning, AND(TCut("pt_sim>=15"), TCut("abs(dR_sim_corr)<=0.2")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_sim_eta_pt15_L1MuDR02_dR012_L1Tk_corr",
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 15 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta_sim)", etaBinning, AND(TCut("pt_sim>=15"), TCut("abs(dR_sim_corr)<=0.2")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_sim_eta_pt15_L1MuDR02_dR012_L1Tk_corr", 
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 15 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta_sim)", etaBinning, AND(TCut("pt_sim>=20"), TCut("abs(dR_sim_corr)<=0.2")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_sim_eta_pt20_L1MuDR02_dR012_L1Tk_corr", 
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 20 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta_sim)", etaBinning, AND(TCut("pt_sim>=20"), TCut("abs(dR_sim_corr)<=0.2")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_sim_eta_pt20_L1MuDR02_dR012_L1Tk_corr", 
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 20 GeV, dR(L1Tk,L1Mu)<=0.12")



  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt_sim>=10"), TCut("abs(dR_sim_prop)<=0.2")), TCut("abs(dR_L1Tk_prop)<=0.12") ), "eff_L1_eta_pt10_L1MuDR02_dR012_L1Tk_prop", 
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 10 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt_sim>=10"), TCut("abs(dR_sim_corr)<=0.2")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_L1_eta_pt10_L1MuDR02_dR012_L1Tk_prop", 
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 10 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt_sim>=15"), TCut("abs(dR_sim_prop)<=0.2")), TCut("abs(dR_L1Tk_prop)<=0.12") ), "eff_L1_eta_pt15_L1MuDR02_dR012_L1Tk_prop", 
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 15 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt_sim>=15"), TCut("abs(dR_sim_corr)<=0.2")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_L1_eta_pt15_L1MuDR02_dR012_L1Tk_prop", 
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 15 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt_sim>=20"), TCut("abs(dR_sim_prop)<=0.2")), TCut("abs(dR_L1Tk_prop)<=0.12") ), "eff_L1_eta_pt20_L1MuDR02_dR012_L1Tk_prop", 
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 20 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt_sim>=20"), TCut("abs(dR_sim_corr)<=0.2")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_L1_eta_pt20_L1MuDR02_dR012_L1Tk_prop", 
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 20 GeV, dR(L1Tk,L1Mu)<=0.12")

  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt_sim>=10"), TCut("abs(dR_sim_corr)<=0.2")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_L1_eta_pt10_L1MuDR02_dR012_L1Tk_corr", 
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 10 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt_sim>=10"), TCut("abs(dR_sim_corr)<=0.2")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_L1_eta_pt10_L1MuDR02_dR012_L1Tk_corr", 
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 10 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt_sim>=15"), TCut("abs(dR_sim_corr)<=0.2")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_L1_eta_pt15_L1MuDR02_dR012_L1Tk_corr",
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 15 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt_sim>=15"), TCut("abs(dR_sim_corr)<=0.2")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_L1_eta_pt15_L1MuDR02_dR012_L1Tk_corr", 
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 15 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt_sim>=20"), TCut("abs(dR_sim_corr)<=0.2")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_L1_eta_pt20_L1MuDR02_dR012_L1Tk_corr", 
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 20 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt_sim>=20"), TCut("abs(dR_sim_corr)<=0.2")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_L1_eta_pt20_L1MuDR02_dR012_L1Tk_corr", 
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 20 GeV, dR(L1Tk,L1Mu)<=0.12")

  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt_sim>=10"), TCut("abs(dR_sim_corr)<=0.2"), TCut("quality>=4")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_L1_eta_pt10_Q4_L1MuDR02_dR012_L1Tk_corr", 
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 10 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt_sim>=10"), TCut("abs(dR_sim_corr)<=0.2"), TCut("quality>=4")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_L1_eta_pt10_Q4_L1MuDR02_dR012_L1Tk_corr", 
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 10 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt_sim>=15"), TCut("abs(dR_sim_corr)<=0.2"), TCut("quality>=4")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_L1_eta_pt15_Q4_L1MuDR02_dR012_L1Tk_corr",
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 15 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt_sim>=15"), TCut("abs(dR_sim_corr)<=0.2"), TCut("quality>=4")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_L1_eta_pt15_Q4_L1MuDR02_dR012_L1Tk_corr", 
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 15 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt_sim>=20"), TCut("abs(dR_sim_corr)<=0.2"), TCut("quality>=4")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_L1_eta_pt20_Q4_L1MuDR02_dR012_L1Tk_corr", 
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 20 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt_sim>=20"), TCut("abs(dR_sim_corr)<=0.2"), TCut("quality>=4")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_L1_eta_pt20_Q4_L1MuDR02_dR012_L1Tk_corr", 
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 20 GeV, dR(L1Tk,L1Mu)<=0.12")

  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt>=10"), TCut("quality>=4")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_L1_eta_pt10_Q4_dR012_L1Tk_corr", 
                 "p_{T} >= 10 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt>=10"), TCut("quality>=4")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_L1_eta_pt10_Q4_dR012_L1Tk_corr", 
                 "p_{T} >= 10 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt>=15"), TCut("quality>=4")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_L1_eta_pt15_Q4_dR012_L1Tk_corr",
                 "p_{T} >= 15 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt>=15"), TCut("quality>=4")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_L1_eta_pt15_Q4_dR012_L1Tk_corr", 
                 "p_{T} >= 15 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt>=20"), TCut("quality>=4")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_L1_eta_pt20_Q4_dR012_L1Tk_corr", 
                 "p_{T} >= 20 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt>=20"), TCut("quality>=4")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_L1_eta_pt20_Q4_dR012_L1Tk_corr", 
                 "p_{T} >= 20 GeV, dR(L1Tk,L1Mu)<=0.12")



  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, TCut("pt>=10"), TCut("abs(dR_sim_corr)<=0.2")), "eff_L1_eta_pt10_sim_corr", "dR(SIM,L1Mu)<=0.2, p_{T} >= 10 GeV")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, TCut("pt>=15"), TCut("abs(dR_sim_corr)<=0.2")), "eff_L1_eta_pt15_sim_corr", "dR(SIM,L1Mu)<=0.2, p_{T} >= 15 GeV")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, TCut("pt>=20"), TCut("abs(dR_sim_corr)<=0.2")), "eff_L1_eta_pt20_sim_corr", "dR(SIM,L1Mu)<=0.2, p_{T} >= 20 GeV")
  
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, TCut("pt>=10"), TCut("abs(dR_sim_prop)<=0.2")), "eff_L1_eta_pt10_sim_prop", "dR(SIM,L1Mu)<=0.2, p_{T} >= 10 GeV")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, TCut("pt>=15"), TCut("abs(dR_sim_prop)<=0.2")), "eff_L1_eta_pt15_sim_prop", "dR(SIM,L1Mu)<=0.2, p_{T} >= 15 GeV")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, TCut("pt>=20"), TCut("abs(dR_sim_prop)<=0.2")), "eff_L1_eta_pt20_sim_prop", "dR(SIM,L1Mu)<=0.2, p_{T} >= 20 GeV")

  makeEtaEffPlot(getEffObject(treeHits, "abs(eta_sim)", etaBinning, TCut("pt>=10"), TCut("abs(dR_sim_corr)<=0.2")), "eff_sim_eta_pt10_sim_corr", "dR(SIM,L1Mu)<=0.2, p_{T} >= 10 GeV")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta_sim)", etaBinning, TCut("pt>=15"), TCut("abs(dR_sim_corr)<=0.2")), "eff_sim_eta_pt15_sim_corr", "dR(SIM,L1Mu)<=0.2, p_{T} >= 15 GeV")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta_sim)", etaBinning, TCut("pt>=20"), TCut("abs(dR_sim_corr)<=0.2")), "eff_sim_eta_pt20_sim_corr", "dR(SIM,L1Mu)<=0.2, p_{T} >= 20 GeV")
  
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta_sim)", etaBinning, TCut("pt>=10"), TCut("abs(dR_sim_prop)<=0.2")), "eff_sim_eta_pt10_sim_prop", "dR(SIM,L1Mu)<=0.2, p_{T} >= 10 GeV")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta_sim)", etaBinning, TCut("pt>=15"), TCut("abs(dR_sim_prop)<=0.2")), "eff_sim_eta_pt15_sim_prop", "dR(SIM,L1Mu)<=0.2, p_{T} >= 15 GeV")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta_sim)", etaBinning, TCut("pt>=20"), TCut("abs(dR_sim_prop)<=0.2")), "eff_sim_eta_pt20_sim_prop", "dR(SIM,L1Mu)<=0.2, p_{T} >= 20 GeV")

  """
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt>=10"),TCut("abs(dR_sim_prop)<=0.2")), TCut("abs(dR_L1Tk_prop)<=0.12")), "eff_L1_eta_pt10_sim_prop_L1Tk_prop", "dR(SIM,L1Mu)<=0.2, p_{T} >= 10 GeV, dR(L1Mu,L1Tk)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt>=20"),TCut("abs(dR_sim_prop)<=0.2")), TCut("abs(dR_L1Tk_prop)<=0.12")), "eff_L1_eta_pt20_sim_prop_L1Tk_prop", "dR(SIM,L1Mu)<=0.2, p_{T} >= 20 GeV, dR(L1Mu,L1Tk)<=0.12")

  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt>=10"),TCut("abs(dR_sim_corr)<=0.2")), TCut("abs(dR_L1Tk_corr)<=0.12")), "eff_L1_eta_pt10_sim_corr_L1Tk_corr", "dR(SIM,L1Mu)<=0.2, p_{T} >= 10 GeV, dR(L1Mu,L1Tk)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt>=20"),TCut("abs(dR_sim_corr)<=0.2")), TCut("abs(dR_L1Tk_corr)<=0.12")), "eff_L1_eta_pt20_sim_corr_L1Tk_corr", "dR(SIM,L1Mu)<=0.2, p_{T} >= 20 GeV, dR(L1Mu,L1Tk)<=0.12")


  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt>=10"),TCut("abs(dR_sim_prop)<=0.2"), TCut("quality>=4")), TCut("abs(dR_L1Tk_prop)<=0.12")), "eff_L1_eta_pt10_sim_prop_L1Tk_prop_q", "dR(SIM,L1Mu)<=0.2, p_{T} >= 10 GeV, dR(L1Mu,L1Tk)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt>=20"),TCut("abs(dR_sim_prop)<=0.2"), TCut("quality>=4")), TCut("abs(dR_L1Tk_prop)<=0.12")), "eff_L1_eta_pt20_sim_prop_L1Tk_prop_q", "dR(SIM,L1Mu)<=0.2, p_{T} >= 20 GeV, dR(L1Mu,L1Tk)<=0.12")

  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt>=10"),TCut("abs(dR_sim_corr)<=0.2"), TCut("quality>=4")), TCut("abs(dR_L1Tk_corr)<=0.12")), "eff_L1_eta_pt10_sim_corr_L1Tk_corr_q", "dR(SIM,L1Mu)<=0.2, p_{T} >= 10 GeV, dR(L1Mu,L1Tk)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt>=20"),TCut("abs(dR_sim_corr)<=0.2"), TCut("quality>=4")), TCut("abs(dR_L1Tk_corr)<=0.12")), "eff_L1_eta_pt20_sim_corr_L1Tk_corr_q", "dR(SIM,L1Mu)<=0.2, p_{T} >= 20 GeV, dR(L1Mu,L1Tk)<=0.12")

  #  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, TCut("pt>=15"), TCut("abs(dR_sim_prop)<=0.2")), "eff_L1_eta_pt15_sim_prop", "dR(SIM,L1Mu)<=0.2, p_{T} >= 15 GeV")
  #  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, TCut("pt>=20"), TCut("abs(dR_sim_prop)<=0.2")), "eff_L1_eta_pt20_sim_prop", "dR(SIM,L1Mu)<=0.2, p_{T} >= 20 GeV")
   """

  denom = 0.
  n_L1_sim_corr = 0.
  n_L1_sim_corr_fid = 0.
  
  num = 0.
  num2 = 0.

  h_L1_eta_pt10 = TH1F("h_L1_eta_pt10", "title", 25,0,2.5)
  h_L1_eta_pt15 = TH1F("h_L1_eta_pt15", "title", 25,0,2.5)
  h_L1_eta_pt20 = TH1F("h_L1_eta_pt20", "title", 25,0,2.5)

  h_L1_eta_pt10_sim_corr = TH1F("h_L1_eta_pt10_sim_corr", "title", 25,0,2.5)
  h_L1_eta_pt10_sim_prop = TH1F("h_L1_eta_pt10_sim_prop", "title", 25,0,2.5)
  h_L1_eta_pt15_sim_corr = TH1F("h_L1_eta_pt15_sim_corr", "title", 25,0,2.5)
  h_L1_eta_pt15_sim_prop = TH1F("h_L1_eta_pt15_sim_prop", "title", 25,0,2.5)
  h_L1_eta_pt20_sim_corr = TH1F("h_L1_eta_pt20_sim_corr", "title", 25,0,2.5)
  h_L1_eta_pt20_sim_prop = TH1F("h_L1_eta_pt20_sim_prop", "title", 25,0,2.5)


  denom = 0.
  num = 0.
  num2 = 0.

  for k in range(0,treeHits.GetEntries()):
    treeHits.GetEntry(k)
    #print "event", k

    if (abs(treeHits.dR_sim_corr)<=0.2):
      n_L1_sim_corr = n_L1_sim_corr + 1

    if (abs(treeHits.dR_sim_corr)<=0.2 and abs(treeHits.eta)<=2.5 and treeHits.pt>=10):
      n_L1_sim_corr_fid = n_L1_sim_corr_fid + 1

    if (abs(treeHits.eta)<=2.5):

      if (treeHits.pt>=10):
        h_L1_eta_pt10.Fill(abs(treeHits.eta))
        if (abs(treeHits.dR_sim_corr)<=0.2):
          h_L1_eta_pt10_sim_corr.Fill(abs(treeHits.eta))
        if (abs(treeHits.dR_sim_prop)<=0.2):
          h_L1_eta_pt10_sim_prop.Fill(abs(treeHits.eta))

      if (treeHits.pt>=15):
        h_L1_eta_pt15.Fill(abs(treeHits.eta))
        if (abs(treeHits.dR_sim_corr)<=0.2):
          h_L1_eta_pt15_sim_corr.Fill(abs(treeHits.eta))
        if (abs(treeHits.dR_sim_prop)<=0.2):
          h_L1_eta_pt15_sim_prop.Fill(abs(treeHits.eta))

      if (treeHits.pt>=20):
        h_L1_eta_pt20.Fill(abs(treeHits.eta))
        if (abs(treeHits.dR_sim_prop)<=0.2):
          h_L1_eta_pt20_sim_prop.Fill(abs(treeHits.eta))
        if (abs(treeHits.dR_sim_corr)<=0.2): 
          h_L1_eta_pt20_sim_corr.Fill(abs(treeHits.eta))
          if treeHits.quality>=4:
            denom += 1
            if (abs(treeHits.dR_L1Tk_prop)<=0.12):
              num += 1
            if (abs(treeHits.dR_L1Tk_corr)<=0.12):
              num2 += 1


        """
        else:
        print "Did not make the cut"
        print "event", k
        print treeHits.dR_sim_corr
        print treeHits.pt, treeHits.eta, treeHits.phi
        print treeHits.pt_sim, treeHits.eta_sim, treeHits.phi_sim
        print 
        """
          
#  print "num", num, "denom", denom, "eff", num/denom
#  print "num2", num2, "denom", denom, "eff2", num2/denom

  makeEtaEffPlot(TEfficiency(h_L1_eta_pt10_sim_corr, h_L1_eta_pt10), "eff_L1_eta_pt10_sim_corr_loop", "dR(SIM,L1Mu)<=0.2, p_{T} >= 10 GeV")
  makeEtaEffPlot(TEfficiency(h_L1_eta_pt10_sim_prop, h_L1_eta_pt10), "eff_L1_eta_pt10_sim_prop_loop", "dR(SIM,L1Mu)<=0.2, p_{T} >= 10 GeV")

  makeEtaEffPlot(TEfficiency(h_L1_eta_pt15_sim_corr, h_L1_eta_pt15), "eff_L1_eta_pt15_sim_corr_loop", "dR(SIM,L1Mu)<=0.2, p_{T} >= 15 GeV")
  makeEtaEffPlot(TEfficiency(h_L1_eta_pt15_sim_prop, h_L1_eta_pt15), "eff_L1_eta_pt15_sim_prop_loop", "dR(SIM,L1Mu)<=0.2, p_{T} >= 15 GeV")

  makeEtaEffPlot(TEfficiency(h_L1_eta_pt20_sim_corr, h_L1_eta_pt20), "eff_L1_eta_pt20_sim_corr_loop", "dR(SIM,L1Mu)<=0.2, p_{T} >= 20 GeV")
  makeEtaEffPlot(TEfficiency(h_L1_eta_pt20_sim_prop, h_L1_eta_pt20), "eff_L1_eta_pt20_sim_prop_loop", "dR(SIM,L1Mu)<=0.2, p_{T} >= 20 GeV")

  
  """
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt>10"), TCut("dR_sim_corr<0.2")), TCut("dR_L1Tk<0.12")), "eff_L1_eta_pt10_sim_L1_dRL1Tk_012", "dR(SIM,L1Mu)<0.2, p_{T} > 10 GeV, L1Mu is matched")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt>10"), TCut("dR_sim_corr<0.2")), TCut("dR_L1Tk_corr<0.12")), "eff_L1_eta_pt10_sim_L1_dRL1TkCorr_012", "dR(SIM,L1Mu)<0.2, p_{T} > 10 GeV, L1Mu is matched")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt>15"), TCut("dR_sim_corr<0.2")), TCut("dR_L1Tk<0.12")), "eff_L1_eta_pt15_sim_L1_dRL1Tk_012", "dR(SIM,L1Mu)<0.2, p_{T} > 15 GeV, L1Mu is matched")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt>15"), TCut("dR_sim_corr<0.2")), TCut("dR_L1Tk_corr<0.12")), "eff_L1_eta_pt15_sim_L1_dRL1TkCorr_012", "dR(SIM,L1Mu)<0.2, p_{T} > 15 GeV, L1Mu is matched")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt>20"), TCut("dR_sim_corr<0.2")), TCut("dR_L1Tk<0.12")), "eff_L1_eta_pt20_sim_L1_dRL1Tk_012", "dR(SIM,L1Mu)<0.2, p_{T} > 20 GeV, L1Mu is matched")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt>20"), TCut("dR_sim_corr<0.2")), TCut("dR_L1Tk_corr<0.12")), "eff_L1_eta_pt20_sim_L1_dRL1TkCorr_012", "dR(SIM,L1Mu)<0.2, p_{T} > 20 GeV, L1Mu is matched")
  """
