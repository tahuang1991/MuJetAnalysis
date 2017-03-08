# Run quiet mode
import sys
sys.argv.append( '-b' )
import ROOT
ROOT.gROOT.SetBatch(1)
from Helpers import *
ROOT.gErrorIgnoreLevel=1001
from ROOT import *
import random
import re

#______________________________________________________________________________
if __name__ == "__main__":

  label = "Neutrino_Pt2to20_gun_TTI2023Upg14D_PU140bx25_ILT_SLHC14_20170219_v2"; pu = 'PU140'; eff = False
  label = "Neutrino_Pt2to20_gun_TTI2023Upg14D_PU140bx25_ILT_SLHC14_Barrel20170306"; pu = 'PU140'; eff = False

  inputFile = TFile.Open(label + ".root")

  ## extension for figures - add more?
  ext = ".png"

  ## Style
  gStyle.SetStatStyle(0)

  print "Making the plots"

  set_style()

  doTest = False

  #label = "Neutrino_Pt2to20_gun_TTI2023Upg14D_PU140bx25_ILT_SLHC14_20170223"; pu = 'PU140'; eff = False
  targetDir = label + "/"

  verbose = False

  ## copy index file
  import shutil
  shutil.copy2('index.php', targetDir + 'index.php')

  #nEvents = 30000
  #nEvents = 100000
  #nEvents = 273100
  #nEvents = 282300
  nEvents = 283600
  #nEvents = 10000
 
  def displacedL1MuHybridTriggerRatePlots():

    ## make plots
    def makeDPhiPlot(h, title):
      c = TCanvas("c","c",800,600)
      c.Clear()
      gStyle.SetTitleBorderSize(0);
      #gStyle.SetPadLeftMargin(0.126);
      #gStyle.SetPadRightMargin(0.00);
      gStyle.SetPadTopMargin(0.06);
      gStyle.SetPadBottomMargin(0.13);
      gPad.SetTickx(1)
      gPad.SetTicky(1)
      gPad.SetLogx(0);
      gPad.SetLogy(1)
      gPad.SetGridx(1);
      gPad.SetGridy(1);

      gStyle.SetTitleStyle(0)
      gStyle.SetTitleAlign(13) ##// coord in top left
      gStyle.SetTitleX(0.)
      gStyle.SetTitleY(1.)
      gStyle.SetTitleW(1)
      gStyle.SetTitleH(0.058)
      gStyle.SetTitleBorderSize(0)

      gStyle.SetPadLeftMargin(0.126)
      gStyle.SetPadRightMargin(0.04)
      gStyle.SetPadTopMargin(0.06)
      gStyle.SetPadBottomMargin(0.13)
      gStyle.SetOptStat(0)
      gStyle.SetMarkerStyle(1)

      hh = inputFile.Get(h);

      hh.GetXaxis().SetTitleSize(0.05)
      hh.GetYaxis().SetTitleSize(0.05)
      hh.GetXaxis().SetLabelSize(0.05)
      hh.GetYaxis().SetLabelSize(0.05)

      gStyle.SetTitleFontSize(0.065)

      hh.SetTitle("           #scale[1.4]{#font[61]{CMS}} #font[52]{Simulation preliminary}                                                           14 TeV, 140 PU")
      hh.SetStats(0)
      hh.GetYaxis().SetTitle("charge*#Delta#Phi(GE1/1-ME1/1)")
      hh.GetXaxis().SetTitle("charge*#Delta#Phi(GE2/1-ME2/1)")
      hh.Draw("COLZ")

      c.SaveAs(targetDir + title + ".png")
      c.SaveAs(targetDir + title + ".pdf")
      c.SaveAs(targetDir + title + ".C")

    """
    makeDPhiPlot("h_dphi_ME11_ME21", "dphi_ME11_ME21")
    makeDPhiPlot("h_dphi_ME11_ME21_charge_Pt0to5", "dphi_ME11_ME21_charge_Pt0to5")
    makeDPhiPlot("h_dphi_ME11_ME21_charge_Pt7to140", "dphi_ME11_ME21_charge_Pt7to140")
    makeDPhiPlot("h_dphi_ME11_ME21_charge_Pt10to140", "dphi_ME11_ME21_charge_Pt10to140")
    makeDPhiPlot("h_dphi_ME11_ME21_charge_Pt15to140", "dphi_ME11_ME21_charge_Pt15to140")
    makeDPhiPlot("h_dphi_ME11_ME21_charge_Pt20to140", "dphi_ME11_ME21_charge_Pt20to140")
    makeDPhiPlot("h_dphi_ME11_ME21_charge_Pt30to140", "dphi_ME11_ME21_charge_Pt30to140")
    """

    def makeEtaPlot(title,
                     legendTitle,
                     h1, h1Legend,
                     h2=None, h2Legend=None,
                     h3=None, h3Legend=None,
                     h4=None, h4Legend=None):
      makePlot(title, 
                legendTitle,
                h1, h1Legend,
                h2, h2Legend,
                h3, h3Legend,
                h4, h4Legend,
                True)

    def makePlot(title, 
                  legendTitle,
                  h1, h1Legend,
                  h2=None, h2Legend=None,
                  h3=None, h3Legend=None,
                  h4=None, h4Legend=None,
                  doEta=False):

      if h1 is not None:
        h1 = inputFile.Get(h1)
      if h2 is not None:
        h2 = inputFile.Get(h2)
      if h3 is not None:
        h3 = inputFile.Get(h3)
      if h4 is not None:
        h4 = inputFile.Get(h4)

      c = TCanvas("c","c",800,600)
      c.Clear()
      gStyle.SetTitleBorderSize(0);
      gStyle.SetPadLeftMargin(0.126);
      gStyle.SetPadRightMargin(0.04);
      gStyle.SetPadTopMargin(0.06);
      gStyle.SetPadBottomMargin(0.13);
      gPad.SetTickx(1)
      gPad.SetTicky(1)
      gPad.SetLogy(1)
      #gPad.SetLogx(1);
      if doEta:
        gPad.SetLogx(0);
        gPad.SetLogy(0)
      gPad.SetGridx(1);
      gPad.SetGridy(1);
      gStyle.SetErrorX(0)
      gStyle.SetTitleStyle(0)
      gStyle.SetTitleAlign(13) ##// coord in top left
      gStyle.SetTitleX(0.)
      gStyle.SetTitleY(1.)
      gStyle.SetTitleW(1)
      gStyle.SetTitleH(0.058)
      gStyle.SetTitleBorderSize(0)
      gStyle.SetOptStat(0)
      gStyle.SetMarkerStyle(1)

      etabin = [
        0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95,
        1.0, 1.05, 1.1, 1.15, 1.2, 1.25, 1.3, 1.35, 1.4, 1.45, 1.5, 1.55, 1.6, 1.65, 1.7, 1.75, 1.8, 1.85, 1.9, 1.95,
        2.0, 2.05, 2.1, 2.15, 2.2, 2.25, 2.3, 2.35, 2.4, 2.45, 2.5]
      myetabin = np.asarray(etabin)
      nmyetabin = len(myetabin) - 1

      b1 = TH1F("b1","b1",100,0,100)
      if doEta:
        b1 = TH1F("b1","b1",nmyetabin,myetabin)
      b1.GetYaxis().SetTitleOffset(1.2)
      if doEta:
        legendTitleSplit = re.split('<', legendTitle)
        print legendTitleSplit
        minEta, maxEta = float(legendTitleSplit[0]), float(legendTitleSplit[2])
        print minEta, maxEta
        b1.GetXaxis().SetRangeUser(minEta,maxEta)
      else:  
        b1.GetXaxis().SetRangeUser(2,50)

      if not doEta:
        b1.GetYaxis().SetNdivisions(520)
      b1.GetYaxis().SetTitle("Trigger rate [kHz]")
      b1.GetXaxis().SetTitle("Muon trigger p_{T} threshold [GeV]")
      if doEta:
        b1.GetXaxis().SetTitle("Muon trigger #eta")
        
      b1.GetXaxis().SetTitleSize(0.05)
      b1.GetYaxis().SetTitleSize(0.05)
      b1.GetXaxis().SetLabelSize(0.05)
      b1.GetYaxis().SetLabelSize(0.05)
      gStyle.SetTitleFontSize(0.065)
      b1.SetTitle("           #scale[1.4]{#font[61]{CMS}} #font[52]{Simulation preliminary}                                                           14 TeV, 140 PU")
      b1.SetStats(0)
      b1.Draw()

      h11 = h1.Clone(h1.GetTitle() + "_clone")
      if h2 is not None:
        h21 = h2.Clone(h2.GetTitle() + "_clone")
      if h3 is not None:
        h31 = h3.Clone(h3.GetTitle() + "_clone")
      if h4 is not None:
        h41 = h4.Clone(h4.GetTitle() + "_clone")

      if doEta:
        h11 = getRateEtaHistogram(nEvents, h11)
        if h2 is not None:
          h21 = getRateEtaHistogram(nEvents, h21)
        if h3 is not None:
          h31 = getRateEtaHistogram(nEvents, h31)
        if h4 is not None:
          h41 = getRateEtaHistogram(nEvents, h41)
      else:
        h11 = getRatePtHistogram(nEvents, h11)
        if h2 is not None:
          h21 = getRatePtHistogram(nEvents, h21)
        if h3 is not None:
          h31 = getRatePtHistogram(nEvents, h31)
        if h4 is not None:
          h41 = getRatePtHistogram(nEvents, h41)

      ## set the xy-range user
      if h1 is not None: histogramMax = h11.GetMaximum()
      if h2 is not None: histogramMax = max(h11.GetMaximum(), h21.GetMaximum())
      if h3 is not None: histogramMax = max(h11.GetMaximum(), h21.GetMaximum(), h31.GetMaximum())
      if h4 is not None: histogramMax = max(h11.GetMaximum(), h21.GetMaximum(), h31.GetMaximum(), h41.GetMaximum())

      if h1 is not None: histogramMin = h11.GetMinimum()
      if h2 is not None: histogramMin = min(h11.GetMinimum(), h21.GetMinimum())
      if h3 is not None: histogramMin = min(h11.GetMinimum(), h21.GetMinimum(), h31.GetMinimum())
      if h4 is not None: histogramMin = min(h11.GetMinimum(), h21.GetMinimum(), h31.GetMinimum(), h41.GetMinimum())

      if doEta:
        ## calculate the maximum of the histograms, then add 20% to the scale
        b1.GetYaxis().SetRangeUser(0.1,histogramMax*2)
      else:
        b1.GetYaxis().SetRangeUser(0.8,histogramMax*10.)

      ## set empty bins for displaced trigger histograms!
      def setEmptyBins(h):
        #hnew = h.Clone(h.GetName() + "_clone2");
        #h.SetBinContent(1,0)
        #h.SetBinContent(2,0)
        #h.SetBinContent(3,0)
        #h.SetBinContent(4,0)
        #h.SetBinContent(5,0)
        #h.SetBinContent(6,0)
        #h.SetBinContent(8,0)
        #h.SetBinContent(10,0)
        #h.SetBinContent(12,0)
        #h.SetBinContent(14,0)
        #h.SetBinContent(15,0)
        #SetOwnership( h, False )
        return h

      if doEta:
        h11.SetLineColor(kRed)
        #h11.SetFillColor(kRed)
        h11.SetMarkerStyle(20)
        h11.SetMarkerColor(kRed)
        h11.Draw("E1X0 same")

        if h2 is not None:
          h21.SetLineColor(kGreen+2)
          #h21.SetFillColor(kViolet)
          h21.SetMarkerColor(kGreen+2)
          h21.SetMarkerStyle(21)
          h21.Draw("E1X0 same")
          
        if h3 is not None:
          h31.SetLineColor(kBlue)
          #h31.SetFillColor(kBlue)
          h31.SetMarkerColor(kBlue)
          h31.SetMarkerStyle(22)
          h31.Draw("E1X0 same")

        if h4 is not None:
          h41.SetLineColor(kOrange+1)
          #h41.SetFillColor(kBlue)
          h41.SetMarkerColor(kOrange+1)
          h41.SetMarkerStyle(22)
          h41.Draw("E1X0 same")

        ## get the pT cut
        if 'L1Pt7' in title:
          tex = TLatex(0.2, 0.85,"p_{T}^{Trigger} #geq 7 GeV")
        else:
          tex = TLatex(0.2, 0.85,"p_{T}^{Trigger} #geq 10 GeV")
        tex.SetTextSize(0.04)
        tex.SetNDC()
        tex.Draw("same")
      else:
        if True: 
          if 'hybrid' in h1Legend:
            setEmptyBins(h11)
        #h11.SetFillColor(kRed)
        h11.SetLineColor(kRed)
        h11.SetMarkerColor(kRed)
        h11.SetMarkerStyle(20)
        h11.Draw("E1X0 same")

        if h2 is not None: 
          if 'hybrid' in h2Legend:
            setEmptyBins(h21)
          #h21.SetFillColor(kViolet)
          h21.SetLineColor(kGreen+2)
          h21.SetMarkerColor(kGreen+2)
          h21.SetMarkerStyle(21)
          h21.Draw("E1X0 same")

        if h3 is not None:
          if 'hybrid' in h3Legend:
            tex = drawLabel("Note: p_{T,min}^{hybrid} = 5 GeV", 0.6,0.8)
            setEmptyBins(h31)

          #h31.SetFillColor(kBlue)
          h31.SetLineColor(kBlue)
          h31.SetMarkerColor(kBlue)
          h31.SetMarkerStyle(22)
          h31.Draw("E1X0 same")

        if h4 is not None:
          if 'hybrid' in h4Legend:
            tex = drawLabel("Note: p_{T,min}^{hybrid} = 5 GeV", 0.6,0.8)
            setEmptyBins(h41)

          #h31.SetFillColor(kBlue)
          h41.SetLineColor(kOrange+1)
          h41.SetMarkerColor(kOrange+1)
          h41.SetMarkerStyle(22)
          h41.Draw("E1X0 same")

      #latex = applyTdrStyle()

      if doEta:
        leg = TLegend(0.15,0.6,0.5,0.8,"","brNDC")
        leg.SetFillColor(kWhite)
        leg.SetBorderSize(0)
        leg.SetFillStyle(1001)
        leg.SetTextSize(0.04)
        leg.AddEntry(h11, h1Legend + " (" + str("%.1f"%h11.Integral()) + " kHz)", "p")
        if h2 is not None:
          leg.AddEntry(h21, h2Legend + " (" + str("%.1f"%h21.Integral()) + " kHz)", "p")
        if h3 is not None:
          leg.AddEntry(h31, h3Legend + " (" + str("%.1f"%h31.Integral()) + " kHz)", "p")
        if h4 is not None:
          leg.AddEntry(h41, h4Legend + " (" + str("%.1f"%h41.Integral()) + " kHz)", "p")
        leg.Draw("same")
      else:
        leg = TLegend(0.15,0.75,0.8,0.9,legendTitle,"brNDC")
        #leg.SetHeader(legendTitle)
        leg.SetFillColor(kWhite)
        leg.SetBorderSize(0)
        leg.SetFillStyle(1001)
        leg.SetTextSize(0.04)
        leg.AddEntry(h11, h1Legend, "p")
        if h2 is not None:
          leg.AddEntry(h21, h2Legend, "p")
        if h3 is not None:
          leg.AddEntry(h31, h3Legend, "p")
        if h4 is not None:
          leg.AddEntry(h41, h4Legend, "p")
        leg.Draw("same")

      if doEta:
        title.replace("_rate_pt_", "_rate_eta_")

      c.SaveAs(targetDir + title + ext)
      c.SaveAs(targetDir + title + ".pdf")
      c.SaveAs(targetDir + title + ".C")

      if False: return

      ## ratios
      c = TCanvas("c","c",800,600)
      c.Clear()
      gStyle.SetTitleBorderSize(0);
      gStyle.SetPadLeftMargin(0.126);
      gStyle.SetPadRightMargin(0.04);
      gStyle.SetPadTopMargin(0.06);
      gStyle.SetPadBottomMargin(0.13);
      gPad.SetTickx(1)
      gPad.SetTicky(1)
      gPad.SetLogy(1)
      #gPad.SetLogx(1);
      if doEta:
        gPad.SetLogx(0);
      gPad.SetLogy(1)
      gPad.SetGridx(1);
      gPad.SetGridy(1);
      gStyle.SetErrorX(0)
      gStyle.SetTitleStyle(0)
      gStyle.SetTitleAlign(13) ##// coord in top left
      gStyle.SetTitleX(0.)
      gStyle.SetTitleY(1.)
      gStyle.SetTitleW(1)
      gStyle.SetTitleH(0.058)
      gStyle.SetTitleBorderSize(0)
      gStyle.SetOptStat(0)
      gStyle.SetMarkerStyle(1)

      b1 = TH1F("b1","b1",100,0,100)
      if doEta:
        b1 = TH1F("b1","b1",nmyetabin,myetabin)
      b1.GetYaxis().SetRangeUser(0.01,100)
      b1.GetXaxis().SetRangeUser(2,50)
      if doEta:
        b1.GetXaxis().SetRangeUser(1,2.5)
      b1.GetYaxis().SetTitleOffset(1.2)
      if not doEta:
        b1.GetYaxis().SetNdivisions(520)
      b1.GetYaxis().SetTitle("Ratio")
      b1.GetXaxis().SetTitle("Muon trigger p_{T} threshold [GeV]")
      if doEta:
        b1.GetXaxis().SetTitle("Muon trigger #eta")
        
      b1.GetXaxis().SetTitleSize(0.05)
      b1.GetYaxis().SetTitleSize(0.05)
      b1.GetXaxis().SetLabelSize(0.05)
      b1.GetYaxis().SetLabelSize(0.05)
      gStyle.SetTitleFontSize(0.065)
      b1.SetTitle("           #scale[1.4]{#font[61]{CMS}} #font[52]{Simulation preliminary}                                                           14 TeV, 140 PU")
      b1.SetStats(0)
      b1.Draw()

      if h2 is not None:
        h21.SetLineColor(kRed)
        h21.SetMarkerColor(kRed)
        h21.SetMarkerStyle(20)
        h21.Divide(h11)
        h21.Draw("E1X0 same")

      if h3 is not None:
        h31.SetLineColor(kGreen+2)
        h31.SetMarkerColor(kGreen+2)
        h21.SetMarkerStyle(21)
        h31.Divide(h11)
        h31.Draw("E1X0 same")

      if h4 is not None:
        h41.SetLineColor(kBlue)
        h41.SetMarkerColor(kBlue)  
        h41.SetMarkerStyle(22)
        h41.Divide(h11)
        h41.Draw("E1X0 same")

      """
      leg = TLegend(0.2,0.2,0.9,0.4,"","brNDC")
      leg.SetFillColor(kWhite)
      leg.SetBorderSize(0)
      leg.SetFillStyle(0)
      leg.SetTextSize(0.03)
      leg.AddEntry(h1,"Prompt L1Mu", "l")
      leg.AddEntry(None,"Displaced L1Mu", "")
      leg.AddEntry(None,"Veto Matching L1Tk #DeltaR#leq0.12 with p_{T}#geq%.0f"%(MatchingL1TkMinPt), "")
      leg.AddEntry(None,"Veto Non-matching L1Tk #DeltaR#leq%.1f:"%(isolation_cone), "")
      leg.AddEntry(h5,"p_{T} #geq 4 GeV", "l")
      leg.AddEntry(h4,"p_{T} #geq 3 GeV", "l")
      leg.AddEntry(h3,"p_{T} #geq 2.5 GeV", "l")
      leg.AddEntry(h2,"p_{T} #geq 2 GeV", "l")
      leg.Draw("same")
      """

      c.SaveAs(targetDir + title + "_ratio" + ext)
      c.SaveAs(targetDir + title + "_ratio.C")
      c.SaveAs(targetDir + title + "_ratio.pdf")


    ## basic trigger rate plots
    makePlot("Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu2st__L1Mu3st_eta0to2p4",
              "0.0<|#eta|<2.4",
              "h_single_prompt_L1Mu_rate_pt_eta0to2p4", "Prompt L1Mu",
              "h_single_prompt_L1Mu_rate_pt_2_stubs_eta0to2p4", "Prompt L1Mu, 2 stubs",
              "h_single_prompt_L1Mu_rate_pt_3_stubs_eta0to2p4", "Prompt L1Mu, 3 stubs")
    makeEtaPlot("Prompt_L1Mu_trigger_rate_eta_L1Pt7__L1Mu__L1Mu2st__L1Mu3st_eta0to2p4",
                 "0.0<|#eta|<2.4",
                 "h_single_prompt_L1Mu_rate_eta_L1Pt7_eta0to2p4", "Prompt L1Mu",
                 "h_single_prompt_L1Mu_rate_eta_L1Pt7_2_stubs_eta0to2p4", "Prompt L1Mu, 2 stubs",
                 "h_single_prompt_L1Mu_rate_eta_L1Pt7_3_stubs_eta0to2p4", "Prompt L1Mu, 3 stubs")
    makeEtaPlot("Prompt_L1Mu_trigger_rate_eta_L1Pt10__L1Mu__L1Mu2st__L1Mu3st_eta0to2p4",
                 "0.0<|#eta|<2.4",
                 "h_single_prompt_L1Mu_rate_eta_L1Pt10_eta0to2p4", "Prompt L1Mu",
                 "h_single_prompt_L1Mu_rate_eta_L1Pt10_2_stubs_eta0to2p4", "Prompt L1Mu, 2 stubs",
                 "h_single_prompt_L1Mu_rate_eta_L1Pt10_3_stubs_eta0to2p4", "Prompt L1Mu, 3 stubs")











    ## barrel trigger
    makePlot("Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu2st__DisplacedL1MuDirectionBased_MB1_MB2_MB3_MB4_combined_eta0to0p9",
              "0<|#eta|<0.9",
              "h_single_prompt_L1Mu_rate_pt_eta0to0p9", "Prompt L1Mu",
              "h_single_displaced_L1Mu_rate_pt_direction_MB1_MB2_MB3_MB4_combined_eta0to0p9", "Direction based",
              "h_single_displaced_L1Mu_rate_pt_direction_MB1_MB2_MB3_MB4_combined_eta0to0p9_mediumVeto", "Direction based, medium veto",
             )
    makeEtaPlot("Prompt_L1Mu_trigger_rate_eta_L1Pt7__L1Mu__L1Mu2st__DisplacedL1MuDirectionBased_MB1_MB2_MB3_MB4_combined_eta0to0p9",
                "0<|#eta|<0.9",
                "h_single_prompt_L1Mu_rate_eta_L1Pt7_eta0to0p9", "Prompt L1Mu",
                "h_single_displaced_L1Mu_rate_eta_L1Pt7_direction_MB1_MB2_MB3_MB4_combined_eta0to0p9", "Direction based",
                "h_single_displaced_L1Mu_rate_eta_L1Pt7_direction_MB1_MB2_MB3_MB4_combined_eta0to0p9_mediumVeto", "Direction based, medium veto",
                )
    makeEtaPlot("Prompt_L1Mu_trigger_rate_eta_L1Pt10__L1Mu__L1Mu2st__DisplacedL1MuDirectionBased_MB1_MB2_MB3_MB4_combined_eta0to0p9",
                "0<|#eta|<0.9",
                "h_single_prompt_L1Mu_rate_eta_L1Pt10_eta0to0p9", "Prompt L1Mu",
                "h_single_displaced_L1Mu_rate_eta_L1Pt10_direction_MB1_MB2_MB3_MB4_combined_eta0to0p9", "Direction based",
                "h_single_displaced_L1Mu_rate_eta_L1Pt10_direction_MB1_MB2_MB3_MB4_combined_eta0to0p9_mediumVeto", "Direction based, medium veto",
                )


    twoBarrelStubCombinations = ["MB1_MB2", "MB1_MB3", "MB1_MB4", 
                                 "MB2_MB3", "MB2_MB4", "MB3_MB4",
                                 "MB1_MB2_MB3", "MB1_MB2_MB4", "MB1_MB3_MB4", "MB2_MB2_MB4",
                                 "MB1_MB2_MB3_MB4"]
    twoBarrelStubCombinationsLegend = ["MB1-MB2", "MB1-MB3", "MB1-MB4", 
                                       "MB2-MB3", "MB2-MB4", "MB3-MB4",
                                       "MB1-MB2-MB3",  "MB1-MB2-MB4",  "MB1-MB3-MB4",  "MB2-MB2-MB4", 
                                       "MB1-MB2-MB3-MB4"]

    for p,q in zip(twoBarrelStubCombinations, twoBarrelStubCombinationsLegend):
      
      print p, q
      print "h_single_displaced_L1Mu_rate_pt_direction_" + p + "_eta0to0p9"
      makePlot("Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu2st__DisplacedL1MuDirectionBased_" + p + "_eta0to0p9",
               "0<|#eta|<0.9",
               "h_single_prompt_L1Mu_rate_pt_eta0to0p9", "Prompt L1Mu",
               "h_single_prompt_L1Mu_rate_pt_" + p + "_eta0to0p9", "Prompt L1Mu, hit in " + q,
               "h_single_displaced_L1Mu_rate_pt_direction_" + p + "_eta0to0p9", "Displaced L1Mu, hit in " + q + ", direction based")
      makeEtaPlot("Prompt_L1Mu_trigger_rate_eta_L1Pt7__L1Mu__L1Mu2st__DisplacedL1MuDirectionBased_" + p + "_eta0to0p9",
                  "0<|#eta|<0.9",
                  "h_single_prompt_L1Mu_rate_eta_L1Pt7_eta0to0p9", "Prompt L1Mu",
                  "h_single_prompt_L1Mu_rate_eta_L1Pt7_" + p + "_eta0to0p9", "Prompt L1Mu, hit in " + q,
                  "h_single_displaced_L1Mu_rate_eta_L1Pt7_direction_" + p + "_eta0to0p9", "Displaced L1Mu, hit in " + q + " direction based")
      makeEtaPlot("Prompt_L1Mu_trigger_rate_eta_L1Pt10__L1Mu__L1Mu2st__DisplacedL1MuDirectionBased_" + p + "_eta0to0p9",
                  "0<|#eta|<0.9",
                  "h_single_prompt_L1Mu_rate_eta_L1Pt10_eta0to0p9", "Prompt L1Mu",
                  "h_single_prompt_L1Mu_rate_eta_L1Pt10_" + p + "_eta0to0p9", "Prompt L1Mu, hit in " + q,
                  "h_single_displaced_L1Mu_rate_eta_L1Pt10_direction_" + p + "_eta0to0p9", "Displaced L1Mu, hit in " + q + " direction based")


      makePlot("Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu2st__DisplacedL1MuDirectionBased_" + p + "_eta0to0p9_looseVeto",
               "0<|#eta|<0.9",
               "h_single_prompt_L1Mu_rate_pt_" + p + "_eta0to0p9", "Prompt L1Mu, hit in " + q,
               "h_single_displaced_L1Mu_rate_pt_direction_" + p + "_eta0to0p9", "Direction based, hit in " + q,
               "h_single_displaced_L1Mu_rate_pt_direction_" + p + "_eta0to0p9_looseVeto", "Direction based, hit in " + q + " + loose veto",
               "h_single_displaced_L1Mu_rate_pt_direction_" + p + "_eta0to0p9_mediumVeto", "Direction based, hit in " + q + " + medium veto")
      makeEtaPlot("Prompt_L1Mu_trigger_rate_eta_L1Pt7__L1Mu__L1Mu2st__DisplacedL1MuDirectionBased_" + p + "_eta0to0p9_looseVeto",
                  "0<|#eta|<0.9",
                  "h_single_prompt_L1Mu_rate_eta_L1Pt7_" + p + "_eta0to0p9", "Prompt L1Mu, hit in " + q,
                  "h_single_displaced_L1Mu_rate_eta_L1Pt7_direction_" + p + "_eta0to0p9", "Direction based, hit in " + q,
                  "h_single_displaced_L1Mu_rate_eta_L1Pt7_direction_" + p + "_eta0to0p9_looseVeto", "Direction based, hit in " + q + " + loose veto",
                  "h_single_displaced_L1Mu_rate_eta_L1Pt7_direction_" + p + "_eta0to0p9_mediumVeto", "Direction based, hit in " + q + " + medium veto")
      makeEtaPlot("Prompt_L1Mu_trigger_rate_eta_L1Pt10__L1Mu__L1Mu2st__DisplacedL1MuDirectionBased_" + p + "_eta0to0p9_looseVeto",
                  "0<|#eta|<0.9",
                  "h_single_prompt_L1Mu_rate_eta_L1Pt10_" + p + "_eta0to0p9", "Prompt L1Mu, hit in " + q,
                  "h_single_displaced_L1Mu_rate_eta_L1Pt10_direction_" + p + "_eta0to0p9", "Direction based, hit in " + q,
                  "h_single_displaced_L1Mu_rate_eta_L1Pt10_direction_" + p + "_eta0to0p9_looseVeto", "Direction based, hit in " + q + " + loose veto",
                  "h_single_displaced_L1Mu_rate_eta_L1Pt10_direction_" + p + "_eta0to0p9_mediumVeto", "Direction based, hit in " + q + " + medium veto")


  displacedL1MuHybridTriggerRatePlots()

