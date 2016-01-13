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

  #label = "out_filter_ana_DarkSUSY_mH_125_mGammaD_20000_ctau_1000_14TeV_PU0_L1TkdR0p4"; pu = 'PU0'; eff = True
  #label = "out_filter_ana_DarkSUSY_mH_125_mGammaD_20000_ctau_1000_14TeV_PU0_L1TkdR0p3"; pu = 'PU0'; eff = True
  #label = "out_filter_ana_DarkSUSY_mH_125_mGammaD_20000_ctau_1000_14TeV_PU0_L1TkdR0p2"; pu = 'PU0'; eff = True
  #label = "out_filter_ana_DarkSUSY_mH_125_mGammaD_20000_ctau_1000_14TeV_PU0_L1TkdR0p12"; pu = 'PU0'; eff = True

  label = "out_filter_ana_DarkSUSY_mH_125_mGammaD_20000_ctau_1000_14TeV_PU140_L1TkdR0p4"; pu = 'PU140'; eff = True
  label = "out_filter_ana_DarkSUSY_mH_125_mGammaD_20000_ctau_1000_14TeV_PU140_L1TkdR0p3"; pu = 'PU140'; eff = True
  label = "out_filter_ana_DarkSUSY_mH_125_mGammaD_20000_ctau_1000_14TeV_PU140_L1TkdR0p2"; pu = 'PU140'; eff = True
  label = "out_filter_ana_DarkSUSY_mH_125_mGammaD_20000_ctau_1000_14TeV_PU140_L1TkdR0p12"; pu = 'PU140'; eff = True

  #label = "out_filter_ana_Neutrino_Pt2to20_gun_TTI2023Upg14D_PU140bx25_ILT_SLHC14_L1TkdR0p4"; pu = 'PU140'; eff = False
  #label = "out_filter_ana_Neutrino_Pt2to20_gun_TTI2023Upg14D_PU140bx25_ILT_SLHC14_L1TkdR0p3"; pu = 'PU140'; eff = False
  #label = "out_filter_ana_Neutrino_Pt2to20_gun_TTI2023Upg14D_PU140bx25_ILT_SLHC14_L1TkdR0p2"; pu = 'PU140'; eff = False
  #label = "out_filter_ana_Neutrino_Pt2to20_gun_TTI2023Upg14D_PU140bx25_ILT_SLHC14_L1TkdR0p12"; pu = 'PU140'; eff = False

  label = "out_filter_ana_DarkSUSY_mH_125_mGammaD_20000_ctau_1000_14TeV"; pu = 'PU0'; eff = True#.root
  label = "out_filter_ana_DarkSUSY_mH_125_mGammaD_20000_ctau_1000_14TeV_PU140"; pu = 'PU140'; eff = True#.root
  inputFile = label + ".root"
  targetDir = label + "/"

  ## extension for figures - add more?
  ext = ".png"
  

  ## Trees
  analyzer = "DisplacedL1MuFilter_PhaseIIGE21"
  recHits = "L1MuTree"

  ## Style
  gStyle.SetStatStyle(0);

  ## input
  file = TFile.Open(inputFile)
  if not file: sys.exit('Input ROOT file %s is missing.' %(inputFile))

  dirAna = file.Get(analyzer)
  if not dirAna: sys.exit('Directory %s does not exist.' %(dirAna))
    
  treeHits = dirAna.Get(recHits)
  if not treeHits: sys.exit('Tree %s does not exist.' %(treeHits))
  
  print "Making the plots"

  set_style()


  def makeRateVsPtHistogram():

    h_single_L1Mu_rate = TH1F("h_single_L1Mu_rate"," ",len(myptbin)-1, myptbin)
    h_single_displaced_rate = TH1F("h_single_displaced_rate"," ",len(myptbin)-1, myptbin)
    h_single_displaced_rate_L1TkPt2 = TH1F("h_single_displaced_rate_L1TkPt2"," ",len(myptbin)-1, myptbin)
    h_single_displaced_rate_L1TkPt2p5 = TH1F("h_single_displaced_rate_L1TkPt2p5"," ",len(myptbin)-1, myptbin)
    h_single_displaced_rate_L1TkPt3 = TH1F("h_single_displaced_rate_L1TkPt3"," ",len(myptbin)-1, myptbin)
    h_single_displaced_rate_L1TkPt4 = TH1F("h_single_displaced_rate_L1TkPt4"," ",len(myptbin)-1, myptbin)
    
    for k in range(0,treeHits.GetEntries()): #
      treeHits.GetEntry(k)

      ## get the max value of the momentum
      pts = list(treeHits.L1Mu_pt)
      if len(pts)>=1:
              
        def getMaxPts():
          maxPt1, maxPt2, maxPt3, maxPt4, maxPt5 = 0., 0., 0., 0., 0., 
          for i in range(0,len(pts)):
            L1Mu_pt = treeHits.L1Mu_pt[i]
            L1Mu_bx = treeHits.L1Mu_bx[i]
            L1Mu_quality = treeHits.L1Mu_quality[i]
            L1Mu_isMatched = treeHits.L1Mu_isMatched[i]
            L1Mu_isUnMatched = treeHits.L1Mu_isUnMatched[i]
            L1Mu_isUnMatchedL1TkPt2 = treeHits.L1Mu_isUnMatchedL1TkPt2[i]
            L1Mu_isUnMatchedL1TkPt2p5 = treeHits.L1Mu_isUnMatchedL1TkPt2p5[i]
            L1Mu_isUnMatchedL1TkPt3 = treeHits.L1Mu_isUnMatchedL1TkPt3[i]
            L1Mu_isUnMatchedL1TkPt4 = treeHits.L1Mu_isUnMatchedL1TkPt4[i]

            if L1Mu_bx==0 and L1Mu_quality >= 4                                                        and L1Mu_pt>maxPt1: maxPt1 = L1Mu_pt
            if L1Mu_bx==0 and L1Mu_quality >= 0 and L1Mu_isMatched==0 and L1Mu_isUnMatchedL1TkPt2==0   and L1Mu_pt>maxPt2: maxPt2 = L1Mu_pt
            if L1Mu_bx==0 and L1Mu_quality >= 0 and L1Mu_isMatched==0 and L1Mu_isUnMatchedL1TkPt2p5==0 and L1Mu_pt>maxPt3: maxPt3 = L1Mu_pt
            if L1Mu_bx==0 and L1Mu_quality >= 0 and L1Mu_isMatched==0 and L1Mu_isUnMatchedL1TkPt3==0   and L1Mu_pt>maxPt4: maxPt4 = L1Mu_pt
            if L1Mu_bx==0 and L1Mu_quality >= 0 and L1Mu_isMatched==0 and L1Mu_isUnMatchedL1TkPt4==0   and L1Mu_pt>maxPt5: maxPt5 = L1Mu_pt

          return maxPt1, maxPt2, maxPt3, maxPt4, maxPt5
        
        maxPt1, maxPt2, maxPt3, maxPt4, maxPt5 = getMaxPts()
        if (maxPt1>0): h_single_L1Mu_rate.Fill(maxPt1)
        if (maxPt2>0): h_single_displaced_rate_L1TkPt2.Fill(maxPt2)
        if (maxPt3>0): h_single_displaced_rate_L1TkPt2p5.Fill(maxPt3)
        if (maxPt4>0): h_single_displaced_rate_L1TkPt3.Fill(maxPt4)
        if (maxPt5>0): h_single_displaced_rate_L1TkPt4.Fill(maxPt5)

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
    b1.GetYaxis().SetTitle("L1Mu Trigger Rate [kHz]")
    b1.GetXaxis().SetTitle("L1Mu p_{T} cut [GeV]")
    b1.GetXaxis().SetTitleFont(62)
    b1.GetXaxis().SetTitleOffset(1.2)
    b1.GetXaxis().SetTitleSize(0.045)
    b1.SetTitle("CMS Simulation Preliminary"+" "*26 +" " + pu + ", 14TeV")
    b1.SetStats(0)
    b1.Draw()

    h_single_L1Mu_rate = getRatePtHistogram(treeHits, h_single_L1Mu_rate)
    h_single_L1Mu_rate.SetFillColor(kRed)
    h_single_L1Mu_rate.Draw("e3same")
    
    h_single_displaced_rate_L1TkPt2 = getRatePtHistogram(treeHits, h_single_displaced_rate_L1TkPt2)
    h_single_displaced_rate_L1TkPt2.SetFillColor(kMagenta)
    h_single_displaced_rate_L1TkPt2.Draw("e3same")

    h_single_displaced_rate_L1TkPt2p5 = getRatePtHistogram(treeHits, h_single_displaced_rate_L1TkPt2p5)
    h_single_displaced_rate_L1TkPt2p5.SetFillColor(kBlue)
    h_single_displaced_rate_L1TkPt2p5.Draw("e3same")

    h_single_displaced_rate_L1TkPt3 = getRatePtHistogram(treeHits, h_single_displaced_rate_L1TkPt3)
    h_single_displaced_rate_L1TkPt3.SetFillColor(kGreen+1)
    h_single_displaced_rate_L1TkPt3.Draw("e3same")
    
    h_single_displaced_rate_L1TkPt4 = getRatePtHistogram(treeHits, h_single_displaced_rate_L1TkPt4)
    h_single_displaced_rate_L1TkPt4.SetFillColor(kOrange+1)
    h_single_displaced_rate_L1TkPt4.Draw("e3same")

    leg = TLegend(0.2,0.7,0.9,0.9,"","brNDC")
    leg.SetFillColor(kWhite)
    leg.SetBorderSize(0)
    leg.SetFillStyle(0)
    leg.SetTextSize(0.03)
    leg.AddEntry(h_single_L1Mu_rate,"Single L1Mu", "f")
    leg.AddEntry(h_single_displaced_rate_L1TkPt4,"Displaced L1Mu (p_{T} #geq 4 GeV on non-matching L1Tk)", "f")
    leg.AddEntry(h_single_displaced_rate_L1TkPt3,"Displaced L1Mu (p_{T} #geq 3 GeV on non-matching L1Tk)", "f")
    leg.AddEntry(h_single_displaced_rate_L1TkPt2p5,"Displaced L1Mu (p_{T} #geq 2.5 GeV on non-matching L1Tk)", "f")
    leg.AddEntry(h_single_displaced_rate_L1TkPt2,"Displaced L1Mu (p_{T} #geq 2 GeV on non-matching L1Tk)", "f")
    leg.Draw("same")
    c.SaveAs(targetDir + "L1Mu_trigger_rate_pt.png")



    ## ratios 
    c = TCanvas("c","c",800,600)
    c.Clear()    
    gStyle.SetTitleBorderSize(0);
    gStyle.SetPadLeftMargin(0.126);
    gStyle.SetPadRightMargin(0.04);
    gStyle.SetPadTopMargin(0.06);
    gStyle.SetPadBottomMargin(0.13);
    gPad.SetLogy(1)

    b1 = TH1F("b1","b1",29,myptbin)
    b1.GetYaxis().SetRangeUser(0.001,1)
    b1.GetYaxis().SetTitleOffset(1.2)
    b1.GetYaxis().SetNdivisions(520)
    b1.GetYaxis().SetTitle("Ratio (normalized to prompt L1Mu)")
    b1.GetXaxis().SetTitle("L1Mu p_{T} cut [GeV]")
    b1.GetXaxis().SetTitleFont(62)
    b1.GetXaxis().SetTitleOffset(1.2)
    b1.GetXaxis().SetTitleSize(0.045)
    b1.SetTitle("CMS Simulation Preliminary"+" "*26 +" " + pu + ", 14TeV")
    b1.SetStats(0)
    b1.Draw()

    h_single_displaced_rate_L1TkPt2.SetLineColor(kMagenta)
    h_single_displaced_rate_L1TkPt2.Divide(h_single_L1Mu_rate)
    h_single_displaced_rate_L1TkPt2.Draw("same")

    h_single_displaced_rate_L1TkPt2p5.SetLineColor(kBlue)
    h_single_displaced_rate_L1TkPt2p5.Divide(h_single_L1Mu_rate)
    h_single_displaced_rate_L1TkPt2p5.Draw("same")

    h_single_displaced_rate_L1TkPt3.SetLineColor(kGreen+1)
    h_single_displaced_rate_L1TkPt3.Divide(h_single_L1Mu_rate)
    h_single_displaced_rate_L1TkPt3.Draw("same")
    
    h_single_displaced_rate_L1TkPt4.SetLineColor(kOrange+1)
    h_single_displaced_rate_L1TkPt4.Divide(h_single_L1Mu_rate)
    h_single_displaced_rate_L1TkPt4.Draw("same")

    leg = TLegend(0.2,0.2,0.9,0.4,"","brNDC")
    leg.SetFillColor(kWhite)
    leg.SetBorderSize(0)
    leg.SetFillStyle(0)
    leg.SetTextSize(0.03)
    leg.AddEntry(h_single_displaced_rate_L1TkPt4,"Displaced L1Mu (p_{T} #geq 4 GeV on non-matching L1Tk)", "l")
    leg.AddEntry(h_single_displaced_rate_L1TkPt3,"Displaced L1Mu (p_{T} #geq 3 GeV on non-matching L1Tk)", "l")
    leg.AddEntry(h_single_displaced_rate_L1TkPt2p5,"Displaced L1Mu (p_{T} #geq 2.5 GeV on non-matching L1Tk)", "l")
    leg.AddEntry(h_single_displaced_rate_L1TkPt2,"Displaced L1Mu (p_{T} #geq 2 GeV on non-matching L1Tk)", "l")
    leg.Draw("same")
    c.SaveAs(targetDir + "L1Mu_trigger_rate_pt_ratio.png")

  if not eff:
    makeRateVsPtHistogram()    


  def makeRateVsEtaHistogram(ptCut):

    h_single_L1Mu_rate = TH1F("h_single_L1Mu_rate"," ",len(myetabin)-1, myetabin)
    h_single_displaced_rate_L1TkPt2 = TH1F("h_single_displaced_rate_L1TkPt2"," ",len(myetabin)-1, myetabin)
    h_single_displaced_rate_L1TkPt2p5 = TH1F("h_single_displaced_rate_L1TkPt2p5"," ",len(myetabin)-1, myetabin)
    h_single_displaced_rate_L1TkPt3 = TH1F("h_single_displaced_rate_L1TkPt3"," ",len(myetabin)-1, myetabin)
    h_single_displaced_rate_L1TkPt4 = TH1F("h_single_displaced_rate_L1TkPt4"," ",len(myetabin)-1, myetabin)

    for k in range(0,treeHits.GetEntries()): #
      treeHits.GetEntry(k)

      ## get the max value of the momentum
      pts = list(treeHits.L1Mu_pt)
      if len(pts)>=1:
      
        def getMaxPts():
          maxPt1, maxPt2, maxPt3, maxPt4, maxPt5 = 0., 0., 0., 0., 0., 
          maxPtIndex1, maxPtIndex2, maxPtIndex3, maxPtIndex4, maxPtIndex5 = -1,  -1, -1,  -1, -1 
          for i in range(0,len(pts)):

            L1Mu_pt = treeHits.L1Mu_pt[i]
            L1Mu_bx = treeHits.L1Mu_bx[i]
            L1Mu_quality = treeHits.L1Mu_quality[i]
            L1Mu_isMatched = treeHits.L1Mu_isMatched[i]
            L1Mu_isUnMatched = treeHits.L1Mu_isUnMatched[i]
            L1Mu_isUnMatchedL1TkPt2 = treeHits.L1Mu_isUnMatchedL1TkPt2[i]
            L1Mu_isUnMatchedL1TkPt2p5 = treeHits.L1Mu_isUnMatchedL1TkPt2p5[i]
            L1Mu_isUnMatchedL1TkPt3 = treeHits.L1Mu_isUnMatchedL1TkPt3[i]
            L1Mu_isUnMatchedL1TkPt4 = treeHits.L1Mu_isUnMatchedL1TkPt4[i]
            
            commonCuts = (L1Mu_pt >= ptCut and L1Mu_bx==0 and L1Mu_quality >=0)
            if L1Mu_pt >= ptCut and L1Mu_bx==0 and L1Mu_quality >=4              and L1Mu_pt > maxPt1: maxPt1 = L1Mu_pt; maxPtIndex1 = i
            if commonCuts and L1Mu_isMatched==0 and L1Mu_isUnMatchedL1TkPt2==0   and L1Mu_pt > maxPt2: maxPt2 = L1Mu_pt; maxPtIndex2 = i
            if commonCuts and L1Mu_isMatched==0 and L1Mu_isUnMatchedL1TkPt2p5==0 and L1Mu_pt > maxPt3: maxPt3 = L1Mu_pt; maxPtIndex3 = i
            if commonCuts and L1Mu_isMatched==0 and L1Mu_isUnMatchedL1TkPt3==0   and L1Mu_pt > maxPt4: maxPt4 = L1Mu_pt; maxPtIndex4 = i
            if commonCuts and L1Mu_isMatched==0 and L1Mu_isUnMatchedL1TkPt4==0   and L1Mu_pt > maxPt5: maxPt5 = L1Mu_pt; maxPtIndex5 = i

          return maxPt1, maxPt2, maxPt3, maxPt4, maxPt5, maxPtIndex1, maxPtIndex2, maxPtIndex3, maxPtIndex4, maxPtIndex5
        
        maxPt1, maxPt2, maxPt3, maxPt4, maxPt5, maxPtIndex1, maxPtIndex2, maxPtIndex3, maxPtIndex4, maxPtIndex5 = getMaxPts()
        if (maxPt1>0): h_single_L1Mu_rate.Fill(treeHits.L1Mu_eta[maxPtIndex1])
        if (maxPt2>0): h_single_displaced_rate_L1TkPt2.Fill(treeHits.L1Mu_eta[maxPtIndex2])
        if (maxPt3>0): h_single_displaced_rate_L1TkPt2p5.Fill(treeHits.L1Mu_eta[maxPtIndex3])
        if (maxPt4>0): h_single_displaced_rate_L1TkPt3.Fill(treeHits.L1Mu_eta[maxPtIndex4])
        if (maxPt5>0): h_single_displaced_rate_L1TkPt4.Fill(treeHits.L1Mu_eta[maxPtIndex5])


    c = TCanvas("c","c",800,600)
    c.Clear()    
    gStyle.SetTitleBorderSize(0);
    gStyle.SetPadLeftMargin(0.126);
    gStyle.SetPadRightMargin(0.04);
    gStyle.SetPadTopMargin(0.06);
    gStyle.SetPadBottomMargin(0.13);
    gPad.SetLogy(1)

    b1 = TH1F("b1","b1",len(myetabin)-1, myetabin)
    b1.GetYaxis().SetRangeUser(.001,100)
    b1.GetYaxis().SetTitleOffset(1.2)
    b1.GetYaxis().SetNdivisions(520)
    b1.GetYaxis().SetTitle("L1 Trigger Rate [kHz]")
    b1.GetXaxis().SetTitle("L1 muon #eta")
    b1.GetXaxis().SetTitleFont(62)
    b1.GetXaxis().SetTitleOffset(1.2)
    b1.GetXaxis().SetTitleSize(0.045)
    b1.SetTitle("CMS Simulation Preliminary"+" "*26 +" " + pu + ", 14TeV")
    b1.SetStats(0)
    b1.Draw()

    h_single_L1Mu_rate = getRateEtaHistogram(treeHits, h_single_L1Mu_rate)
    h_single_L1Mu_rate.SetLineColor(kRed)
    h_single_L1Mu_rate.Draw("same")

    h_single_displaced_rate_L1TkPt2 = getRateEtaHistogram(treeHits, h_single_displaced_rate_L1TkPt2)
    h_single_displaced_rate_L1TkPt2.SetLineColor(kMagenta)
    h_single_displaced_rate_L1TkPt2.Draw("same")

    h_single_displaced_rate_L1TkPt2p5 = getRateEtaHistogram(treeHits, h_single_displaced_rate_L1TkPt2p5)
    h_single_displaced_rate_L1TkPt2p5.SetLineColor(kBlue)
    h_single_displaced_rate_L1TkPt2p5.Draw("same")

    h_single_displaced_rate_L1TkPt3 = getRateEtaHistogram(treeHits, h_single_displaced_rate_L1TkPt3)
    h_single_displaced_rate_L1TkPt3.SetLineColor(kGreen+1)
    h_single_displaced_rate_L1TkPt3.Draw("same")

    h_single_displaced_rate_L1TkPt4 = getRateEtaHistogram(treeHits, h_single_displaced_rate_L1TkPt4)
    h_single_displaced_rate_L1TkPt4.SetLineColor(kOrange+1)
    h_single_displaced_rate_L1TkPt4.Draw("same")

    leg = TLegend(0.2,0.7,0.9,0.9,"","brNDC")
    leg.SetFillColor(kWhite)
    leg.SetBorderSize(0)
    leg.SetFillStyle(0)
    leg.SetTextSize(0.03)
    leg.AddEntry(h_single_L1Mu_rate,"Single L1Mu", "l")
    leg.AddEntry(h_single_displaced_rate_L1TkPt4,"Displaced L1Mu (p_{T} #geq 4 GeV on non-matching L1Tk)", "l")
    leg.AddEntry(h_single_displaced_rate_L1TkPt3,"Displaced L1Mu (p_{T} #geq 3 GeV on non-matching L1Tk)", "l")
    leg.AddEntry(h_single_displaced_rate_L1TkPt2p5,"Displaced L1Mu (p_{T} #geq 2.5 GeV on non-matching L1Tk)", "l")
    leg.AddEntry(h_single_displaced_rate_L1TkPt2,"Displaced L1Mu (p_{T} #geq 2 GeV on non-matching L1Tk)", "l")
    leg.Draw("same")
    c.SaveAs(targetDir + "L1Mu_trigger_rate_eta_ptCut_%d.png"%(ptCut))

    ## ratios 
    c = TCanvas("c","c",800,600)
    c.Clear()    
    gStyle.SetTitleBorderSize(0);
    gStyle.SetPadLeftMargin(0.126);
    gStyle.SetPadRightMargin(0.04);
    gStyle.SetPadTopMargin(0.06);
    gStyle.SetPadBottomMargin(0.13);
    gPad.SetLogy(1)

    b1 = TH1F("b1","b1",len(myetabin)-1, myetabin)
    b1.GetYaxis().SetRangeUser(0.0001,1)
    b1.GetYaxis().SetTitleOffset(1.2)
    b1.GetYaxis().SetNdivisions(520)
    b1.GetYaxis().SetTitle("Ratio (normalized to prompt L1Mu)")
    b1.GetXaxis().SetTitle("L1 muon #eta")
    b1.GetXaxis().SetTitleFont(62)
    b1.GetXaxis().SetTitleOffset(1.2)
    b1.GetXaxis().SetTitleSize(0.045)
    b1.SetTitle("CMS Simulation Preliminary"+" "*26 +" " + pu + ", 14TeV")
    b1.SetStats(0)
    b1.Draw()

    h_single_displaced_rate_L1TkPt2.SetLineColor(kMagenta)
    h_single_displaced_rate_L1TkPt2.Divide(h_single_L1Mu_rate)
    h_single_displaced_rate_L1TkPt2.Draw("same")

    h_single_displaced_rate_L1TkPt2p5.SetLineColor(kBlue)
    h_single_displaced_rate_L1TkPt2p5.Divide(h_single_L1Mu_rate)
    h_single_displaced_rate_L1TkPt2p5.Draw("same")

    h_single_displaced_rate_L1TkPt3.SetLineColor(kGreen+1)
    h_single_displaced_rate_L1TkPt3.Divide(h_single_L1Mu_rate)
    h_single_displaced_rate_L1TkPt3.Draw("same")
    
    h_single_displaced_rate_L1TkPt4.SetLineColor(kOrange+1)
    h_single_displaced_rate_L1TkPt4.Divide(h_single_L1Mu_rate)
    h_single_displaced_rate_L1TkPt4.Draw("same")

    leg = TLegend(0.2,0.2,0.9,0.4,"","brNDC")
    leg.SetFillColor(kWhite)
    leg.SetBorderSize(0)
    leg.SetFillStyle(0)
    leg.SetTextSize(0.03)
    leg.AddEntry(h_single_displaced_rate_L1TkPt4,"Displaced L1Mu (p_{T} #geq 4 GeV on non-matching L1Tk)", "l")
    leg.AddEntry(h_single_displaced_rate_L1TkPt3,"Displaced L1Mu (p_{T} #geq 3 GeV on non-matching L1Tk)", "l")
    leg.AddEntry(h_single_displaced_rate_L1TkPt2p5,"Displaced L1Mu (p_{T} #geq 2.5 GeV on non-matching L1Tk)", "l")
    leg.AddEntry(h_single_displaced_rate_L1TkPt2,"Displaced L1Mu (p_{T} #geq 2 GeV on non-matching L1Tk)", "l")
    leg.Draw("same")
    c.SaveAs(targetDir + "L1Mu_trigger_rate_eta_ptCut_%d_ratio.png"%(ptCut))

  if not eff:
    makeRateVsEtaHistogram(10)
    makeRateVsEtaHistogram(15)
    makeRateVsEtaHistogram(20)
    pass

  """
  nPass = 0
  for k in range(0,treeHits.GetEntries()): #
      treeHits.GetEntry(k)

      ## get the max value of the momentum
      pts = list(treeHits.L1Mu_pt)
      if len(pts)>=1:
        nGoodMu = 0
        for i in range(0,len(pts)):        
          if treeHits.L1Mu_pt[i] >= 20 and treeHits.L1Mu_quality[i]>=4 and abs(treeHits.L1Mu_bx[i])<2 and abs(treeHits.L1Mu_eta[i])>=0.:
            print k, i, treeHits.L1Mu_pt[i], treeHits.L1Mu_bx[i], treeHits.L1Mu_quality[i]
            nGoodMu += 1
        if nGoodMu>= 1:
          nPass += 1
      else:
        continue

  print "nPass", nPass
  """

  #exit()
  
  def makeEfficiencyHistogram():

    h_single_L1Mu_efficiency_L1Tk_pt0 = TH1F("h_single_L1Mu_efficiency_L1Tk_pt0"," ", 1000, 0, 20)
    h_single_L1Mu_efficiency_L1Tk_pt2 = TH1F("h_single_L1Mu_efficiency_L1Tk_pt2"," ", 1000, 0, 20)
    h_single_L1Mu_efficiency_L1Tk_pt3 = TH1F("h_single_L1Mu_efficiency_L1Tk_pt3"," ", 1000, 0, 20)
    h_single_L1Mu_efficiency_L1Tk_pt4 = TH1F("h_single_L1Mu_efficiency_L1Tk_pt4"," ", 1000, 0, 20)

    genMu_eta_dxy0to0p1_fid = TH1F("genMu_eta_dxy0to0p1_fid"," ", 25, 0, 2.5)
    genMu_eta_dxy1to5_fid = TH1F("genMu_eta_dxy1to5_fid"," ", 25, 0, 2.5)
    genMu_eta_dxy5to10_fid = TH1F("genMu_eta_dxy5to10_fid"," ", 25, 0, 2.5)
    genMu_eta_dxy10_fid = TH1F("genMu_eta_dxy10_fid"," ", 25, 0, 2.5)

    L1Mu_genMu_eta_dxy0to0p1_fid_L1TkPt0 = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_L1TkPt0"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_L1TkPt0 = TH1F("L1Mu_genMu_eta_dxy1to5_fid_L1TkPt0"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_L1TkPt0 = TH1F("L1Mu_genMu_eta_dxy5to10_fid_L1TkPt0"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_L1TkPt0 = TH1F("L1Mu_genMu_eta_dxy10_fid_L1TkPt0"," ", 25, 0, 2.5)
    

    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt2 = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt2"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt2 = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt2"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt2 = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt2"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt2 = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt2"," ", 25, 0, 2.5)

    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt2 = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt2"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt2 = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt2"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt2 = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt2"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt2 = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt2"," ", 25, 0, 2.5)

    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt2 = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt2"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt2 = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt2"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt2 = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt2"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt2 = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt2"," ", 25, 0, 2.5)

    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt2 = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt2"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt2 = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt2"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt2 = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt2"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt2 = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt2"," ", 25, 0, 2.5)


    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt2p5 = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt2p5"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt2p5 = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt2p5"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt2p5 = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt2p5"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt2p5 = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt2p5"," ", 25, 0, 2.5)

    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt2p5 = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt2p5"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt2p5 = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt2p5"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt2p5 = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt2p5"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt2p5 = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt2p5"," ", 25, 0, 2.5)

    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt2p5 = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt2p5"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt2p5 = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt2p5"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt2p5 = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt2p5"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt2p5 = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt2p5"," ", 25, 0, 2.5)

    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt2p5 = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt2p5"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt2p5 = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt2p5"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt2p5 = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt2p5"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt2p5 = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt2p5"," ", 25, 0, 2.5)


    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt3 = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt3"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt3 = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt3"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt3 = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt3"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt3 = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt3"," ", 25, 0, 2.5)

    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt3 = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt3"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt3 = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt3"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt3 = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt3"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt3 = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt3"," ", 25, 0, 2.5)

    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt3 = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt3"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt3 = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt3"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt3 = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt3"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt3 = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt3"," ", 25, 0, 2.5)

    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt3 = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt3"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt3 = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt3"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt3 = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt3"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt3 = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt3"," ", 25, 0, 2.5)


    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt4 = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt4"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt4 = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt4"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt4 = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt4"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt4 = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt4"," ", 25, 0, 2.5)

    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt4 = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt4"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt4 = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt4"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt4 = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt4"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt4 = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt4"," ", 25, 0, 2.5)

    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt4 = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt4"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt4 = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt4"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt4 = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt4"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt4 = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt4"," ", 25, 0, 2.5)

    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt4 = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt4"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt4 = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt4"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt4 = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt4"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt4 = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt4"," ", 25, 0, 2.5)


    ## pt plots
    genMu_pt_dxy0to0p1_fid = TH1F("genMu_pt_dxy0to0p1_fid"," ", 25, 0, 50)
    genMu_pt_dxy1to5_fid = TH1F("genMu_pt_dxy1to5_fid"," ", 25, 0, 50)
    genMu_pt_dxy5to10_fid = TH1F("genMu_pt_dxy5to10_fid"," ", 25, 0, 50)
    genMu_pt_dxy10_fid = TH1F("genMu_pt_dxy10_fid"," ", 25, 0, 50)

    L1Mu_genMu_pt_dxy0to0p1_fid_L1TkPt0 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_L1TkPt0"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy1to5_fid_L1TkPt0 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_L1TkPt0"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy5to10_fid_L1TkPt0 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_L1TkPt0"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy10_fid_L1TkPt0 = TH1F("L1Mu_genMu_pt_dxy10_fid_L1TkPt0"," ", 25, 0, 50)

    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt2 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_dR0p4_L1TkPt2"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt2 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt2"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt2 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt2"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt2 = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt2"," ", 25, 0, 50)

    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt2 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_dR0p3_L1TkPt2"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt2 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt2"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt2 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt2"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt2 = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt2"," ", 25, 0, 50)

    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt2 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_dR0p2_L1TkPt2"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt2 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt2"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt2 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt2"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt2 = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt2"," ", 25, 0, 50)

    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt2 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_dR0p12_L1TkPt2"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt2 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt2"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt2 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt2"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt2 = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt2"," ", 25, 0, 50)


    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt2p5 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_dR0p4_L1TkPt2p5"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt2p5 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt2p5"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt2p5 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt2p5"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt2p5 = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt2p5"," ", 25, 0, 50)

    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt2p5 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_dR0p3_L1TkPt2p5"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt2p5 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt2p5"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt2p5 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt2p5"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt2p5 = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt2p5"," ", 25, 0, 50)

    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt2p5 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_dR0p2_L1TkPt2p5"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt2p5 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt2p5"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt2p5 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt2p5"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt2p5 = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt2p5"," ", 25, 0, 50)

    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt2p5 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_dR0p12_L1TkPt2p5"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt2p5 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt2p5"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt2p5 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt2p5"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt2p5 = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt2p5"," ", 25, 0, 50)


    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt3 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_dR0p4_L1TkPt3"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt3 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt3"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt3 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt3"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt3 = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt3"," ", 25, 0, 50)

    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt3 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_dR0p3_L1TkPt3"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt3 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt3"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt3 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt3"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt3 = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt3"," ", 25, 0, 50)

    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt3 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_dR0p2_L1TkPt3"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt3 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt3"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt3 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt3"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt3 = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt3"," ", 25, 0, 50)

    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt3 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_dR0p12_L1TkPt3"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt3 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt3"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt3 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt3"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt3 = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt3"," ", 25, 0, 50)


    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt4 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_dR0p4_L1TkPt4"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt4 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt4"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt4 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt4"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt4 = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt4"," ", 25, 0, 50)

    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt4 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_dR0p3_L1TkPt4"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt4 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt4"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt4 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt4"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt4 = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt4"," ", 25, 0, 50)

    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt4 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_dR0p2_L1TkPt4"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt4 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt4"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt4 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt4"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt4 = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt4"," ", 25, 0, 50)

    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt4 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_dR0p12_L1TkPt4"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt4 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt4"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt4 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt4"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt4 = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt4"," ", 25, 0, 50)


    ## temporary check for Slava
    L1Mu_genMu_pt_dxy0to0p1_fid = TH1F("L1Mu_genMu_pt_dxy0top01_fid"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy1to5_fid = TH1F("L1Mu_genMu_pt_dxy1to5_fid"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy5to10_fid = TH1F("L1Mu_genMu_pt_dxy5to10_fid"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy10_fid = TH1F("L1Mu_genMu_pt_dxy10_fid"," ", 25, 0, 50)

    L1Mu_genMu_pt_dxy0to0p1_fid_L1MuPt10 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_L1MuPt10"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy1to5_fid_L1MuPt10 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_L1MuPt10"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy5to10_fid_L1MuPt10 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_L1MuPt10"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy10_fid_L1MuPt10 = TH1F("L1Mu_genMu_pt_dxy10_fid_L1MuPt10"," ", 25, 0, 50)

    L1Mu_genMu_pt_dxy0to0p1_fid_L1MuPt15 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_L1MuPt15"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy1to5_fid_L1MuPt15 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_L1MuPt15"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy5to10_fid_L1MuPt15 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_L1MuPt15"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy10_fid_L1MuPt15 = TH1F("L1Mu_genMu_pt_dxy10_fid_L1MuPt15"," ", 25, 0, 50)

    L1Mu_genMu_pt_dxy0to0p1_fid_L1MuPt20 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_L1MuPt20"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy1to5_fid_L1MuPt20 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_L1MuPt20"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy5to10_fid_L1MuPt20 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_L1MuPt20"," ", 25, 0, 50)
    L1Mu_genMu_pt_dxy10_fid_L1MuPt20 = TH1F("L1Mu_genMu_pt_dxy10_fid_L1MuPt20"," ", 25, 0, 50)


    L1Mu_genMu_eta_dxy0to0p1_fid = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid = TH1F("L1Mu_genMu_eta_dxy1to5_fid"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid = TH1F("L1Mu_genMu_eta_dxy5to10_fid"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid = TH1F("L1Mu_genMu_eta_dxy10_fid"," ", 25, 0, 2.5)

    L1Mu_genMu_eta_dxy0to0p1_fid_L1MuPt10 = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_L1MuPt10"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_L1MuPt10 = TH1F("L1Mu_genMu_eta_dxy1to5_fid_L1MuPt10"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_L1MuPt10 = TH1F("L1Mu_genMu_eta_dxy5to10_fid_L1MuPt10"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_L1MuPt10 = TH1F("L1Mu_genMu_eta_dxy10_fid_L1MuPt10"," ", 25, 0, 2.5)

    L1Mu_genMu_eta_dxy0to0p1_fid_L1MuPt15 = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_L1MuPt15"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_L1MuPt15 = TH1F("L1Mu_genMu_eta_dxy1to5_fid_L1MuPt15"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_L1MuPt15 = TH1F("L1Mu_genMu_eta_dxy5to10_fid_L1MuPt15"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_L1MuPt15 = TH1F("L1Mu_genMu_eta_dxy10_fid_L1MuPt15"," ", 25, 0, 2.5)

    L1Mu_genMu_eta_dxy0to0p1_fid_L1MuPt20 = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_L1MuPt20"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_L1MuPt20 = TH1F("L1Mu_genMu_eta_dxy1to5_fid_L1MuPt20"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_L1MuPt20 = TH1F("L1Mu_genMu_eta_dxy5to10_fid_L1MuPt20"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_L1MuPt20 = TH1F("L1Mu_genMu_eta_dxy10_fid_L1MuPt20"," ", 25, 0, 2.5)

    verbose = False

    nTotalMuon = 0
    nGoodMuon = 0
    for k in range(0,treeHits.GetEntries()):
      treeHits.GetEntry(k)
      if verbose:
        print "Event", k
      for i in range(0,2):
        for j in range(0,2):
          ij = i*2+j
          if verbose:
            print "\tMuon", i, j,
            print "pt", treeHits.genGdMu_pt[ij],
            print "eta", treeHits.genGdMu_eta[ij],
            print "phi", treeHits.genGdMu_phi[ij],
            print "phi_corr", treeHits.genGdMu_phi_corr[ij],
            print "index_corr", treeHits.genGdMu_L1Mu_index_corr[ij],
            print "dR", treeHits.genGdMu_L1Mu_dR_corr[ij],
            print "abs(dxy)", abs(treeHits.genGdMu_dxy[ij])
          L1Mu_index = treeHits.genGdMu_L1Mu_index_corr[ij]

          if L1Mu_index != 99:
            nTotalMuon +=1 
            L1Mu_pt = treeHits.L1Mu_pt[L1Mu_index]
            L1Mu_eta = treeHits.L1Mu_eta[L1Mu_index]
            L1Mu_phi = treeHits.L1Mu_phi[L1Mu_index]
            L1Mu_bx = treeHits.L1Mu_bx[L1Mu_index]
            L1Mu_quality = treeHits.L1Mu_quality[L1Mu_index]
            L1Mu_isMatched = treeHits.L1Mu_isMatched[L1Mu_index]
            L1Mu_isUnMatched = treeHits.L1Mu_isUnMatched[L1Mu_index]
            L1Mu_isUnMatchedL1TkPt2 = treeHits.L1Mu_isUnMatchedL1TkPt2[L1Mu_index]
            L1Mu_isUnMatchedL1TkPt2p5 = treeHits.L1Mu_isUnMatchedL1TkPt2p5[L1Mu_index]
            L1Mu_isUnMatchedL1TkPt3 = treeHits.L1Mu_isUnMatchedL1TkPt3[L1Mu_index]
            L1Mu_isUnMatchedL1TkPt4 = treeHits.L1Mu_isUnMatchedL1TkPt4[L1Mu_index]
            L1Mu_L1Tk_dR_min = treeHits.L1Mu_L1Tk_dR_min[L1Mu_index]
            L1Mu_L1Tk_pt = treeHits.L1Mu_L1Tk_pt[L1Mu_index]
            if L1Mu_quality >= 4:
              nGoodMuon += 1
            if verbose:
              print "\t\tL1Mu", "pt", L1Mu_pt, "eta", L1Mu_eta, "phi", L1Mu_phi, "Quality", L1Mu_quality,
              print "L1Mu_L1Tk_dR_min", L1Mu_L1Tk_dR_min, "L1Mu_L1Tk_pt", L1Mu_L1Tk_pt
              """
              print "Matching", L1Mu_isMatched,
              print L1Mu_isUnMatched, 
              print L1Mu_isUnMatchedL1TkPt2,
              print L1Mu_isUnMatchedL1TkPt3,
              print L1Mu_isUnMatchedL1TkPt4
              """

            matched = False
            unMatched_dR0p4_L1TkPt4 = False
            unMatched_dR0p4_L1TkPt3 = False
            unMatched_dR0p4_L1TkPt2p5 = False
            unMatched_dR0p4_L1TkPt2 = False

            unMatched_dR0p3_L1TkPt4 = False
            unMatched_dR0p3_L1TkPt3 = False
            unMatched_dR0p3_L1TkPt2p5 = False
            unMatched_dR0p3_L1TkPt2 = False

            unMatched_dR0p2_L1TkPt4 = False
            unMatched_dR0p2_L1TkPt3 = False
            unMatched_dR0p2_L1TkPt2p5 = False
            unMatched_dR0p2_L1TkPt2 = False

            unMatched_dR0p12_L1TkPt4 = False
            unMatched_dR0p12_L1TkPt3 = False
            unMatched_dR0p12_L1TkPt2p5 = False
            unMatched_dR0p12_L1TkPt2 = False

            ## matched 
            if L1Mu_L1Tk_dR_min <= 0.12 and L1Mu_quality >= 4: matched
            
            ## unmatched 
            if L1Mu_L1Tk_dR_min <= 0.4 and L1Mu_L1Tk_pt>=4: unMatched_dR0p4_L1TkPt4 = True
            if L1Mu_L1Tk_dR_min <= 0.4 and L1Mu_L1Tk_pt>=3: unMatched_dR0p4_L1TkPt3 = True
            if L1Mu_L1Tk_dR_min <= 0.4 and L1Mu_L1Tk_pt>=2.5: unMatched_dR0p4_L1TkPt2p5 = True
            if L1Mu_L1Tk_dR_min <= 0.4 and L1Mu_L1Tk_pt>=2: unMatched_dR0p4_L1TkPt2 = True

            if L1Mu_L1Tk_dR_min <= 0.3 and L1Mu_L1Tk_pt>=4: unMatched_dR0p3_L1TkPt4 = True
            if L1Mu_L1Tk_dR_min <= 0.3 and L1Mu_L1Tk_pt>=3: unMatched_dR0p3_L1TkPt3 = True
            if L1Mu_L1Tk_dR_min <= 0.3 and L1Mu_L1Tk_pt>=2.5: unMatched_dR0p3_L1TkPt2p5 = True
            if L1Mu_L1Tk_dR_min <= 0.3 and L1Mu_L1Tk_pt>=2: unMatched_dR0p3_L1TkPt2 = True

            if L1Mu_L1Tk_dR_min <= 0.2 and L1Mu_L1Tk_pt>=4: unMatched_dR0p2_L1TkPt4 = True
            if L1Mu_L1Tk_dR_min <= 0.2 and L1Mu_L1Tk_pt>=3: unMatched_dR0p2_L1TkPt3 = True
            if L1Mu_L1Tk_dR_min <= 0.2 and L1Mu_L1Tk_pt>=2.5: unMatched_dR0p2_L1TkPt2p5 = True
            if L1Mu_L1Tk_dR_min <= 0.2 and L1Mu_L1Tk_pt>=2: unMatched_dR0p2_L1TkPt2 = True

            if L1Mu_L1Tk_dR_min <= 0.12 and L1Mu_L1Tk_pt>=4: unMatched_dR0p12_L1TkPt4 = True
            if L1Mu_L1Tk_dR_min <= 0.12 and L1Mu_L1Tk_pt>=3: unMatched_dR0p12_L1TkPt3 = True
            if L1Mu_L1Tk_dR_min <= 0.12 and L1Mu_L1Tk_pt>=2.5: unMatched_dR0p12_L1TkPt2p5 = True
            if L1Mu_L1Tk_dR_min <= 0.12 and L1Mu_L1Tk_pt>=2: unMatched_dR0p12_L1TkPt2 = True

            common = (abs(L1Mu_bx) == 0) and (L1Mu_quality >= 4) and L1Mu_pt>=0
            trig_dR0p4_L1TkPt4 =   (not matched) and (not unMatched_dR0p4_L1TkPt4) and common
            trig_dR0p4_L1TkPt3 =   (not matched) and (not unMatched_dR0p4_L1TkPt3) and common
            trig_dR0p4_L1TkPt2p5 = (not matched) and (not unMatched_dR0p4_L1TkPt2p5) and common
            trig_dR0p4_L1TkPt2 =   (not matched) and (not unMatched_dR0p4_L1TkPt2) and common

            trig_dR0p3_L1TkPt4 =   (not matched) and (not unMatched_dR0p3_L1TkPt4) and common
            trig_dR0p3_L1TkPt3 =   (not matched) and (not unMatched_dR0p3_L1TkPt3) and common
            trig_dR0p3_L1TkPt2p5 = (not matched) and (not unMatched_dR0p3_L1TkPt2p5) and common
            trig_dR0p3_L1TkPt2 =   (not matched) and (not unMatched_dR0p3_L1TkPt2) and common

            trig_dR0p2_L1TkPt4 =   (not matched) and (not unMatched_dR0p2_L1TkPt4) and common
            trig_dR0p2_L1TkPt3 =   (not matched) and (not unMatched_dR0p2_L1TkPt3) and common
            trig_dR0p2_L1TkPt2p5 = (not matched) and (not unMatched_dR0p2_L1TkPt2p5) and common
            trig_dR0p2_L1TkPt2 =   (not matched) and (not unMatched_dR0p2_L1TkPt2) and common

            trig_dR0p12_L1TkPt4 =   (not matched) and (not unMatched_dR0p12_L1TkPt4) and common
            trig_dR0p12_L1TkPt3 =   (not matched) and (not unMatched_dR0p12_L1TkPt3) and common
            trig_dR0p12_L1TkPt2p5 = (not matched) and (not unMatched_dR0p12_L1TkPt2p5) and common
            trig_dR0p12_L1TkPt2 =   (not matched) and (not unMatched_dR0p12_L1TkPt2) and common
            
            trigL1Mu = False
            trigL1TkPt0 = False
            trigL1TkPt2p5 = False
            trigL1TkPt2 = False
            trigL1TkPt3 = False
            trigL1TkPt4 = False
            """
            commonCuts = (abs(L1Mu_bx) ==0 and L1Mu_quality >= 4)
            if L1Mu_isMatched != 1 and L1Mu_isUnMatched != 1          and commonCuts: trigL1TkPt0 = True
            if L1Mu_isMatched != 1 and L1Mu_isUnMatchedL1TkPt2 != 1   and commonCuts: trigL1TkPt2 = True
            if L1Mu_isMatched != 1 and L1Mu_isUnMatchedL1TkPt2p5 != 1 and commonCuts: trigL1TkPt2p5 = True
            if L1Mu_isMatched != 1 and L1Mu_isUnMatchedL1TkPt3 != 1   and commonCuts: trigL1TkPt3 = True
            if L1Mu_isMatched != 1 and L1Mu_isUnMatchedL1TkPt4 != 1   and commonCuts: trigL1TkPt4 = True
            """
            ## temporary check for slava
            if abs(L1Mu_bx) !=1: trigL1Mu = True

          eta = abs(treeHits.genGdMu_eta[ij])
          dxy = abs(treeHits.genGdMu_dxy[ij])
          pt = treeHits.genGdMu_pt[ij]
          vz = abs(treeHits.genGd_vz[i])
          lxy =  abs(treeHits.genGd_lxy[i])

          dxy_range1 = (dxy <= 0.1)
          dxy_range2 = (dxy > 1 and dxy <= 5)
          dxy_range3 = (dxy > 5 and dxy <= 10)
          dxy_range4 = (dxy > 10)

          eta_fid = eta<2.5 and vz < 600 and lxy < 300 and pt>=0
          pt_fid = pt>=5 and vz < 600 and lxy < 300


          ## pt efficiencies
          if dxy_range1 and eta_fid:
            genMu_pt_dxy0to0p1_fid.Fill(pt)
            if trigL1TkPt0:   L1Mu_genMu_pt_dxy0to0p1_fid_L1TkPt0.Fill(pt)
 #           if trigL1TkPt2:   L1Mu_genMu_pt_dxy0to0p1_fid_L1TkPt2.Fill(pt)
#            if trigL1TkPt2p5: L1Mu_genMu_pt_dxy0to0p1_fid_L1TkPt2p5.Fill(pt)
#            if trigL1TkPt3:   L1Mu_genMu_pt_dxy0to0p1_fid_L1TkPt3.Fill(pt)
 #           if trigL1TkPt4:   L1Mu_genMu_pt_dxy0to0p1_fid_L1TkPt4.Fill(pt)
            if trigL1Mu:      L1Mu_genMu_pt_dxy0to0p1_fid.Fill(pt)
            if trig_dR0p4_L1TkPt4: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt4.Fill(pt)
            if trig_dR0p4_L1TkPt3: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt3.Fill(pt)
            if trig_dR0p4_L1TkPt2p5: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt2p5.Fill(pt)
            if trig_dR0p4_L1TkPt2: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt2.Fill(pt)

            if trig_dR0p3_L1TkPt4: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt4.Fill(pt)
            if trig_dR0p3_L1TkPt3: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt3.Fill(pt)
            if trig_dR0p3_L1TkPt2p5: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt2p5.Fill(pt)
            if trig_dR0p3_L1TkPt2: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt2.Fill(pt)

            if trig_dR0p2_L1TkPt4: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt4.Fill(pt)
            if trig_dR0p2_L1TkPt3: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt3.Fill(pt)
            if trig_dR0p2_L1TkPt2p5: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt2p5.Fill(pt)
            if trig_dR0p2_L1TkPt2: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt2.Fill(pt)

            if trig_dR0p12_L1TkPt4: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt4.Fill(pt)
            if trig_dR0p12_L1TkPt3: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt3.Fill(pt)
            if trig_dR0p12_L1TkPt2p5: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt2p5.Fill(pt)
            if trig_dR0p12_L1TkPt2: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt2.Fill(pt)

          if dxy_range2 and eta_fid:
            genMu_pt_dxy1to5_fid.Fill(pt)
            if trigL1TkPt0:   L1Mu_genMu_pt_dxy1to5_fid_L1TkPt0.Fill(pt)
#            if trigL1TkPt2:   L1Mu_genMu_pt_dxy1to5_fid_L1TkPt2.Fill(pt)
#            if trigL1TkPt2p5: L1Mu_genMu_pt_dxy1to5_fid_L1TkPt2p5.Fill(pt)
#            if trigL1TkPt3:   L1Mu_genMu_pt_dxy1to5_fid_L1TkPt3.Fill(pt)
#            if trigL1TkPt4:   L1Mu_genMu_pt_dxy1to5_fid_L1TkPt4.Fill(pt)
            if trigL1Mu:      L1Mu_genMu_pt_dxy1to5_fid.Fill(pt)
            if trig_dR0p4_L1TkPt4: L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt4.Fill(pt)
            if trig_dR0p4_L1TkPt3: L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt3.Fill(pt)
            if trig_dR0p4_L1TkPt2p5: L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt2p5.Fill(pt)
            if trig_dR0p4_L1TkPt2: L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt2.Fill(pt)

            if trig_dR0p3_L1TkPt4: L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt4.Fill(pt)
            if trig_dR0p3_L1TkPt3: L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt3.Fill(pt)
            if trig_dR0p3_L1TkPt2p5: L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt2p5.Fill(pt)
            if trig_dR0p3_L1TkPt2: L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt2.Fill(pt)

            if trig_dR0p2_L1TkPt4: L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt4.Fill(pt)
            if trig_dR0p2_L1TkPt3: L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt3.Fill(pt)
            if trig_dR0p2_L1TkPt2p5: L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt2p5.Fill(pt)
            if trig_dR0p2_L1TkPt2: L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt2.Fill(pt)

            if trig_dR0p12_L1TkPt4: L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt4.Fill(pt)
            if trig_dR0p12_L1TkPt3: L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt3.Fill(pt)
            if trig_dR0p12_L1TkPt2p5: L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt2p5.Fill(pt)
            if trig_dR0p12_L1TkPt2: L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt2.Fill(pt)

          if dxy_range3 and eta_fid:
            genMu_pt_dxy5to10_fid.Fill(pt)
            if trigL1TkPt0:   L1Mu_genMu_pt_dxy5to10_fid_L1TkPt0.Fill(pt)
#            if trigL1TkPt2:   L1Mu_genMu_pt_dxy5to10_fid_L1TkPt2.Fill(pt)
#            if trigL1TkPt2p5: L1Mu_genMu_pt_dxy5to10_fid_L1TkPt2p5.Fill(pt)
#            if trigL1TkPt3:   L1Mu_genMu_pt_dxy5to10_fid_L1TkPt3.Fill(pt)
#            if trigL1TkPt4:   L1Mu_genMu_pt_dxy5to10_fid_L1TkPt4.Fill(pt)
            if trigL1Mu:      L1Mu_genMu_pt_dxy5to10_fid.Fill(pt)
            if trig_dR0p4_L1TkPt4: L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt4.Fill(pt)
            if trig_dR0p4_L1TkPt3: L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt3.Fill(pt)
            if trig_dR0p4_L1TkPt2p5: L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt2p5.Fill(pt)
            if trig_dR0p4_L1TkPt2: L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt2.Fill(pt)

            if trig_dR0p3_L1TkPt4: L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt4.Fill(pt)
            if trig_dR0p3_L1TkPt3: L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt3.Fill(pt)
            if trig_dR0p3_L1TkPt2p5: L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt2p5.Fill(pt)
            if trig_dR0p3_L1TkPt2: L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt2.Fill(pt)

            if trig_dR0p2_L1TkPt4: L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt4.Fill(pt)
            if trig_dR0p2_L1TkPt3: L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt3.Fill(pt)
            if trig_dR0p2_L1TkPt2p5: L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt2p5.Fill(pt)
            if trig_dR0p2_L1TkPt2: L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt2.Fill(pt)

            if trig_dR0p12_L1TkPt4: L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt4.Fill(pt)
            if trig_dR0p12_L1TkPt3: L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt3.Fill(pt)
            if trig_dR0p12_L1TkPt2p5: L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt2p5.Fill(pt)
            if trig_dR0p12_L1TkPt2: L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt2.Fill(pt)

          if dxy_range4 and eta_fid:
            genMu_pt_dxy10_fid.Fill(pt)
            if trigL1TkPt0:   L1Mu_genMu_pt_dxy10_fid_L1TkPt0.Fill(pt)
#            if trigL1TkPt2:   L1Mu_genMu_pt_dxy10_fid_L1TkPt2.Fill(pt)
#            if trigL1TkPt2p5: L1Mu_genMu_pt_dxy10_fid_L1TkPt2p5.Fill(pt)
#            if trigL1TkPt3:   L1Mu_genMu_pt_dxy10_fid_L1TkPt3.Fill(pt)
  #          if trigL1TkPt4:   L1Mu_genMu_pt_dxy10_fid_L1TkPt4.Fill(pt)
            if trigL1Mu:      L1Mu_genMu_pt_dxy10_fid.Fill(pt)
            if trig_dR0p4_L1TkPt4: L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt4.Fill(pt)
            if trig_dR0p4_L1TkPt3: L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt3.Fill(pt)
            if trig_dR0p4_L1TkPt2p5: L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt2p5.Fill(pt)
            if trig_dR0p4_L1TkPt2: L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt2.Fill(pt)
             
            if trig_dR0p3_L1TkPt4: L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt4.Fill(pt)
            if trig_dR0p3_L1TkPt3: L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt3.Fill(pt)
            if trig_dR0p3_L1TkPt2p5: L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt2p5.Fill(pt)
            if trig_dR0p3_L1TkPt2: L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt2.Fill(pt)

            if trig_dR0p2_L1TkPt4: L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt4.Fill(pt)
            if trig_dR0p2_L1TkPt3: L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt3.Fill(pt)
            if trig_dR0p2_L1TkPt2p5: L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt2p5.Fill(pt)
            if trig_dR0p2_L1TkPt2: L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt2.Fill(pt)

            if trig_dR0p12_L1TkPt4: L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt4.Fill(pt)
            if trig_dR0p12_L1TkPt3: L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt3.Fill(pt)
            if trig_dR0p12_L1TkPt2p5: L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt2p5.Fill(pt)
            if trig_dR0p12_L1TkPt2: L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt2.Fill(pt)
            
          ## eta efficiencies
          if dxy_range1 and pt_fid:
            genMu_eta_dxy0to0p1_fid.Fill(eta)
            if trigL1TkPt0:   L1Mu_genMu_eta_dxy0to0p1_fid_L1TkPt0.Fill(eta)
#            if trigL1TkPt2:   L1Mu_genMu_eta_dxy0to0p1_fid_L1TkPt2.Fill(eta)
#            if trigL1TkPt2p5: L1Mu_genMu_eta_dxy0to0p1_fid_L1TkPt2p5.Fill(eta)
#            if trigL1TkPt3:   L1Mu_genMu_eta_dxy0to0p1_fid_L1TkPt3.Fill(eta)
#            if trigL1TkPt4:   L1Mu_genMu_eta_dxy0to0p1_fid_L1TkPt4.Fill(eta)
            if trigL1Mu:      L1Mu_genMu_eta_dxy0to0p1_fid.Fill(eta)
            if trig_dR0p4_L1TkPt4: L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt4.Fill(eta)
            if trig_dR0p4_L1TkPt3: L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt3.Fill(eta)
            if trig_dR0p4_L1TkPt2p5: L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt2p5.Fill(eta)
            if trig_dR0p4_L1TkPt2: L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt2.Fill(eta)

            if trig_dR0p3_L1TkPt4: L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt4.Fill(eta)
            if trig_dR0p3_L1TkPt3: L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt3.Fill(eta)
            if trig_dR0p3_L1TkPt2p5: L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt2p5.Fill(eta)
            if trig_dR0p3_L1TkPt2: L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt2.Fill(eta)

            if trig_dR0p2_L1TkPt4: L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt4.Fill(eta)
            if trig_dR0p2_L1TkPt3: L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt3.Fill(eta)
            if trig_dR0p2_L1TkPt2p5: L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt2p5.Fill(eta)
            if trig_dR0p2_L1TkPt2: L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt2.Fill(eta)

            if trig_dR0p12_L1TkPt4: L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt4.Fill(eta)
            if trig_dR0p12_L1TkPt3: L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt3.Fill(eta)
            if trig_dR0p12_L1TkPt2p5: L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt2p5.Fill(eta)
            if trig_dR0p12_L1TkPt2: L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt2.Fill(eta)

          if dxy_range2 and pt_fid:
            genMu_eta_dxy1to5_fid.Fill(eta)
            if trigL1TkPt0:   L1Mu_genMu_eta_dxy1to5_fid_L1TkPt0.Fill(eta)
#            if trigL1TkPt2:   L1Mu_genMu_eta_dxy1to5_fid_L1TkPt2.Fill(eta)
#            if trigL1TkPt2p5: L1Mu_genMu_eta_dxy1to5_fid_L1TkPt2p5.Fill(eta)
#            if trigL1TkPt3:   L1Mu_genMu_eta_dxy1to5_fid_L1TkPt3.Fill(eta)
#            if trigL1TkPt4:   L1Mu_genMu_eta_dxy1to5_fid_L1TkPt4.Fill(eta)
            if trigL1Mu:      L1Mu_genMu_eta_dxy1to5_fid.Fill(eta)
            if trig_dR0p4_L1TkPt4: L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt4.Fill(eta)
            if trig_dR0p4_L1TkPt3: L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt3.Fill(eta)
            if trig_dR0p4_L1TkPt2p5: L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt2p5.Fill(eta)
            if trig_dR0p4_L1TkPt2: L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt2.Fill(eta)

            if trig_dR0p3_L1TkPt4: L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt4.Fill(eta)
            if trig_dR0p3_L1TkPt3: L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt3.Fill(eta)
            if trig_dR0p3_L1TkPt2p5: L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt2p5.Fill(eta)
            if trig_dR0p3_L1TkPt2: L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt2.Fill(eta)

            if trig_dR0p2_L1TkPt4: L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt4.Fill(eta)
            if trig_dR0p2_L1TkPt3: L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt3.Fill(eta)
            if trig_dR0p2_L1TkPt2p5: L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt2p5.Fill(eta)
            if trig_dR0p2_L1TkPt2: L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt2.Fill(eta)

            if trig_dR0p12_L1TkPt4: L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt4.Fill(eta)
            if trig_dR0p12_L1TkPt3: L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt3.Fill(eta)
            if trig_dR0p12_L1TkPt2p5: L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt2p5.Fill(eta)
            if trig_dR0p12_L1TkPt2: L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt2.Fill(eta)

          if dxy_range3 and pt_fid:
            genMu_eta_dxy5to10_fid.Fill(eta)
            if trigL1TkPt0:   L1Mu_genMu_eta_dxy5to10_fid_L1TkPt0.Fill(eta)
#            if trigL1TkPt2:   L1Mu_genMu_eta_dxy5to10_fid_L1TkPt2.Fill(eta)
#            if trigL1TkPt2p5: L1Mu_genMu_eta_dxy5to10_fid_L1TkPt2p5.Fill(eta)
#            if trigL1TkPt3:   L1Mu_genMu_eta_dxy5to10_fid_L1TkPt3.Fill(eta)
#            if trigL1TkPt4:   L1Mu_genMu_eta_dxy5to10_fid_L1TkPt4.Fill(eta)
            if trigL1Mu:      L1Mu_genMu_eta_dxy5to10_fid.Fill(eta)
            if trig_dR0p4_L1TkPt4: L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt4.Fill(eta)
            if trig_dR0p4_L1TkPt3: L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt3.Fill(eta)
            if trig_dR0p4_L1TkPt2p5: L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt2p5.Fill(eta)
            if trig_dR0p4_L1TkPt2: L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt2.Fill(eta)

            if trig_dR0p3_L1TkPt4: L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt4.Fill(eta)
            if trig_dR0p3_L1TkPt3: L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt3.Fill(eta)
            if trig_dR0p3_L1TkPt2p5: L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt2p5.Fill(eta)
            if trig_dR0p3_L1TkPt2: L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt2.Fill(eta)

            if trig_dR0p2_L1TkPt4: L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt4.Fill(eta)
            if trig_dR0p2_L1TkPt3: L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt3.Fill(eta)
            if trig_dR0p2_L1TkPt2p5: L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt2p5.Fill(eta)
            if trig_dR0p2_L1TkPt2: L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt2.Fill(eta)

            if trig_dR0p12_L1TkPt4: L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt4.Fill(eta)
            if trig_dR0p12_L1TkPt3: L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt3.Fill(eta)
            if trig_dR0p12_L1TkPt2p5: L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt2p5.Fill(eta)
            if trig_dR0p12_L1TkPt2: L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt2.Fill(eta)

          if dxy_range4 and pt_fid:
            genMu_eta_dxy10_fid.Fill(eta)
            if trigL1TkPt0:   L1Mu_genMu_eta_dxy10_fid_L1TkPt0.Fill(eta)
#            if trigL1TkPt2:   L1Mu_genMu_eta_dxy10_fid_L1TkPt2.Fill(eta)
#            if trigL1TkPt2p5: L1Mu_genMu_eta_dxy10_fid_L1TkPt2p5.Fill(eta)
#            if trigL1TkPt3:   L1Mu_genMu_eta_dxy10_fid_L1TkPt3.Fill(eta)
#            if trigL1TkPt4:   L1Mu_genMu_eta_dxy10_fid_L1TkPt4.Fill(eta)
            if trigL1Mu:      L1Mu_genMu_eta_dxy10_fid.Fill(eta)
            if trig_dR0p4_L1TkPt4: L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt4.Fill(eta)
            if trig_dR0p4_L1TkPt3: L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt3.Fill(eta)
            if trig_dR0p4_L1TkPt2p5: L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt2p5.Fill(eta)
            if trig_dR0p4_L1TkPt2: L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt2.Fill(eta)

            if trig_dR0p3_L1TkPt4: L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt4.Fill(eta)
            if trig_dR0p3_L1TkPt3: L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt3.Fill(eta)
            if trig_dR0p3_L1TkPt2p5: L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt2p5.Fill(eta)
            if trig_dR0p3_L1TkPt2: L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt2.Fill(eta)

            if trig_dR0p2_L1TkPt4: L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt4.Fill(eta)
            if trig_dR0p2_L1TkPt3: L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt3.Fill(eta)
            if trig_dR0p2_L1TkPt2p5: L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt2p5.Fill(eta)
            if trig_dR0p2_L1TkPt2: L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt2.Fill(eta)

            if trig_dR0p12_L1TkPt4: L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt4.Fill(eta)
            if trig_dR0p12_L1TkPt3: L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt3.Fill(eta)
            if trig_dR0p12_L1TkPt2p5: L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt2p5.Fill(eta)
            if trig_dR0p12_L1TkPt2: L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt2.Fill(eta)
    
    print "nTotalMuon", nTotalMuon, "nGoodMuon", nGoodMuon

    def makeEffPlot(eff1, eff2, eff3, eff4, title, doPt = True):
      
      c = TCanvas("c","c",800,600)
      c.Clear()    
      gStyle.SetTitleBorderSize(0);
      gStyle.SetPadLeftMargin(0.126);
      gStyle.SetPadRightMargin(0.04);
      gStyle.SetPadTopMargin(0.06);
      gStyle.SetPadBottomMargin(0.13);
      #gPad.SetLogx(1)
      
      if doPt: mmax = 50;  xaxisTitle = "True Muon p_{T} [GeV]"
      else:    mmax = 2.5; xaxisTitle = "True Muon #eta"

      b1 = TH1F("b1","b1", 25, 0, mmax)
      #b1.GetYaxis().SetRangeUser(.01,100)
      b1.GetYaxis().SetTitleOffset(1.2)
      b1.GetYaxis().SetNdivisions(520)
      b1.GetYaxis().SetTitle("Trigger efficiency")
      b1.GetXaxis().SetTitle(xaxisTitle)
      b1.GetXaxis().SetTitleFont(62)
      b1.GetXaxis().SetTitleOffset(1.2)
      b1.GetXaxis().SetTitleSize(0.045)
      b1.SetTitle("CMS Simulation Preliminary"+" "*26 +" " + pu + ", 14TeV")
      b1.SetStats(0)
      b1.Draw()

      eff1.SetLineColor(kRed)
      eff1.Draw("same")
      eff2.SetLineColor(kMagenta+1)
      eff2.Draw("same")
      eff3.SetLineColor(kGreen+1)
      eff3.Draw("same")
      eff4.SetLineColor(kBlue)
      eff4.Draw("same")
      
      leg = TLegend(0.7,0.4,0.9,0.6,"","brNDC")
      leg.SetFillColor(kWhite)
      leg.SetBorderSize(0)
      leg.SetFillStyle(0)
      leg.SetTextSize(0.03)
      leg.AddEntry(eff1,"|dxy| #leq 0.1", "l")
      leg.AddEntry(eff2,"1 < |dxy| #leq 5", "l")
      leg.AddEntry(eff3,"5 < |dxy| #leq 10", "l")
      leg.AddEntry(eff4,"|dxy| > 10", "l")
      leg.Draw("same")
      c.SaveAs(title)
    
    ## pt effciency plots
    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt2, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt2,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt2,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt2,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p4_L1TkPt2.png", True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt2p5, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt2p5,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt2p5,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt2p5,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p4_L1TkPt2p5.png", True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt3, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt3,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt3,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt3,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p4_L1TkPt3.png", True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt4, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt4,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt4,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt4,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p4_L1TkPt4.png", True)


    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt2, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt2,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt2,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt2,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p3_L1TkPt2.png", True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt2p5, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt2p5,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt2p5,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt2p5,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p3_L1TkPt2p5.png", True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt3, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt3,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt3,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt3,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p3_L1TkPt3.png", True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt4, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt4,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt4,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt4,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p3_L1TkPt4.png", True)


    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt2, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt2,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt2,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt2,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p2_L1TkPt2.png", True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt2p5, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt2p5,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt2p5,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt2p5,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p2_L1TkPt2p5.png", True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt3, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt3,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt3,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt3,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p2_L1TkPt3.png", True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt4, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt4,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt4,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt4,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p2_L1TkPt4.png", True)


    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt2, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt2,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt2,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt2,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p12_L1TkPt2.png", True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt2p5, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt2p5,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt2p5,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt2p5,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p12_L1TkPt2p5.png", True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt3, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt3,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt3,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt3,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p12_L1TkPt3.png", True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt4, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt4,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt4,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt4,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p12_L1TkPt4.png", True)

    ## eta effciency plots
    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt2, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt2,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt2,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt2,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p4_L1TkPt2.png", False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt2p5, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt2p5,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt2p5,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt2p5,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p4_L1TkPt2p5.png", False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt3, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt3,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt3,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt3,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p4_L1TkPt3.png", False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt4, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt4,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt4,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt4,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p4_L1TkPt4.png", False)


    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt2, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt2,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt2,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt2,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p3_L1TkPt2.png", False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt2p5, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt2p5,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt2p5,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt2p5,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p3_L1TkPt2p5.png", False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt3, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt3,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt3,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt3,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p3_L1TkPt3.png", False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt4, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt4,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt4,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt4,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p3_L1TkPt4.png", False)


    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt2, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt2,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt2,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt2,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p2_L1TkPt2.png", False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt2p5, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt2p5,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt2p5,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt2p5,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p2_L1TkPt2p5.png", False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt3, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt3,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt3,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt3,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p2_L1TkPt3.png", False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt4, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt4,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt4,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt4,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p2_L1TkPt4.png", False)


    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt2, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt2,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt2,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt2,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p12_L1TkPt2.png", False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt2p5, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt2p5,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt2p5,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt2p5,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p12_L1TkPt2p5.png", False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt3, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt3,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt3,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt3,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p12_L1TkPt3.png", False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt4, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt4,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt4,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt4,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p12_L1TkPt4.png", False)


    ## debug for slava
    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid.png", True)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid.png", False)


  if eff:
    makeEfficiencyHistogram()   

  exit()


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
          if treeHits.L1Mu_quality>=4:
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
