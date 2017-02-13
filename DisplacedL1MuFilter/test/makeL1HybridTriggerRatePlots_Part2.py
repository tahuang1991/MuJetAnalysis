# Run quiet mode
import sys
sys.argv.append( '-b' )
import ROOT
ROOT.gROOT.SetBatch(1)
from Helpers import *
ROOT.gErrorIgnoreLevel=1001
from ROOT import *
import random

#______________________________________________________________________________
if __name__ == "__main__":

  label = "Neutrino_Pt2to20_gun_TTI2023Upg14D_PU140bx25_ILT_SLHC14_20170213"; pu = 'PU140'; eff = False

  inputFile = TFile.Open(label + ".root")

  ## extension for figures - add more?
  ext = ".png"

  ## Style
  gStyle.SetStatStyle(0)

  print "Making the plots"

  set_style()

  doTest = False

  targetDir = label + "/"

  verbose = False

  ## copy index file
  import shutil
  shutil.copy2('index.php', targetDir + 'index.php')

  nEvents = 10000
  
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
      gPad.SetLogy(0)
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

    makeDPhiPlot("h_dphi_ME11_ME21", "dphi_ME11_ME21")
    makeDPhiPlot("h_dphi_ME11_ME21_charge_Pt0to5", "dphi_ME11_ME21_charge_Pt0to5")
    makeDPhiPlot("h_dphi_ME11_ME21_charge_Pt7to140", "dphi_ME11_ME21_charge_Pt7to140")
    makeDPhiPlot("h_dphi_ME11_ME21_charge_Pt10to140", "dphi_ME11_ME21_charge_Pt10to140")
    makeDPhiPlot("h_dphi_ME11_ME21_charge_Pt15to140", "dphi_ME11_ME21_charge_Pt15to140")
    makeDPhiPlot("h_dphi_ME11_ME21_charge_Pt20to140", "dphi_ME11_ME21_charge_Pt20to140")
    makeDPhiPlot("h_dphi_ME11_ME21_charge_Pt30to140", "dphi_ME11_ME21_charge_Pt30to140")

    def makeEtaPlots(legendTitle,
                     h1, h1Legend,
                     h2, h2Legend,
                     h3, h3Legend,
                     title, doEta=True):
      makePlots(legendTitle,
                h1, h1Legend,
                h2, h2Legend,
                h3, h3Legend,
                title, doEta)

    def makePlots(legendTitle,
                  h1, h1Legend,
                  h2, h2Legend,
                  h3, h3Legend,
                  title, doEta=False):

      h1 = inputFile.Get(h1)
      h2 = inputFile.Get(h2)
      h3 = inputFile.Get(h3)

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
      gPad.SetLogx(1);
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

      gStyle.SetPadLeftMargin(0.126)
      gStyle.SetPadRightMargin(0.04)
      gStyle.SetPadTopMargin(0.06)
      gStyle.SetPadBottomMargin(0.13)
      gStyle.SetOptStat(0)
      gStyle.SetMarkerStyle(1)

      ptbin = [
        1, 2.0,   2.5,   3.0,   3.5,   4.0,   4.5,   5.0,   6.0,   7.0,   8.0,
        10.0,  12.0,  14.0,  16.0,  18.0,  20.0,  25.0,  30.0,  35.0,  40.0,
        45.0,  50.0,  60.0,  70.0,  80.0,  90.0, 100.0, 120.0, 140.0]
      myptbin = np.asarray(ptbin)
      nmyptbin = len(myptbin) - 1

      etabin = [
        0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95,
        1.0, 1.05, 1.1, 1.15, 1.2, 1.25, 1.3, 1.35, 1.4, 1.45, 1.5, 1.55, 1.6, 1.65, 1.7, 1.75, 1.8, 1.85, 1.9, 1.95,
        2.0, 2.05, 2.1, 2.15, 2.2, 2.25, 2.3, 2.35, 2.4, 2.45, 2.5]
      myetabin = np.asarray(etabin)
      nmyetabin = len(myetabin) - 1

      b1 = TH1F("b1","b1",nmyptbin,myptbin)
      if doEta:
        b1 = TH1F("b1","b1",nmyetabin,myetabin)
      b1.GetYaxis().SetRangeUser(0.2,10000)
      b1.GetXaxis().SetRangeUser(2,140)
      if doEta:
        b1.GetYaxis().SetRangeUser(0,50)
        b1.GetXaxis().SetRangeUser(0,2.5)
      b1.GetYaxis().SetTitleOffset(1.2)
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

      print h1, h2, h3
      h11 = h1.Clone(h1.GetTitle() + "_clone")
      h21 = h2.Clone(h2.GetTitle() + "_clone")
      h31 = h3.Clone(h3.GetTitle() + "_clone")

      print "nEvents", nEvents, "entries", h1.GetEntries(), h2.GetEntries(), h3.GetEntries()
      if doEta:
        h11 = getRateEtaHistogram(nEvents, h11)
        h21 = getRateEtaHistogram(nEvents, h21)
        h31 = getRateEtaHistogram(nEvents, h31)
      else:
        h11 = getRatePtHistogram(nEvents, h11)
        h21 = getRatePtHistogram(nEvents, h21)
        h31 = getRatePtHistogram(nEvents, h31)

      ## set empty bins for displaced trigger histograms!
      def setEmptyBins(h):
        #hnew = h.Clone(h.GetName() + "_clone2");
        h.SetBinContent(1,0)
        h.SetBinContent(2,0)
        h.SetBinContent(3,0)
        h.SetBinContent(4,0)
        h.SetBinContent(5,0)
        h.SetBinContent(6,0)
        h.SetBinContent(8,0)
        h.SetBinContent(10,0)
        h.SetBinContent(12,0)
        h.SetBinContent(14,0)
        h.SetBinContent(15,0)
        #SetOwnership( h, False )
        return h

      if doEta:
        h11.SetLineColor(kRed)
        #h11.SetFillColor(kRed)
        h11.SetMarkerStyle(20)
        h11.SetMarkerColor(kRed)
        h11.Draw("E1X0 same")

        h21.SetLineColor(kViolet)
        #h21.SetFillColor(kViolet)
        h21.SetMarkerColor(kViolet)
        h21.SetMarkerStyle(21)
        h21.Draw("E1X0 same")

        h31.SetLineColor(kBlue)
        #h31.SetFillColor(kBlue)
        h31.SetMarkerColor(kBlue)
        h31.SetMarkerStyle(22)
        h31.Draw("E1X0 same")

        tex = TLatex(0.15, 0.4,"p_{T}^{Trigger} #geq 10 GeV")
        tex.SetTextSize(0.04)
        tex.SetNDC()
        tex.Draw("same")
      else:
        if False: 
          if (('Displaced' in h1Legend) and ('hybrid' in h1Legend)) or '(hybrid)' in h1Legend:
            setEmptyBins(h11)
        #h11.SetFillColor(kRed)
        h11.SetLineColor(kRed)
        h11.SetMarkerColor(kRed)
        h11.SetMarkerStyle(20)
        h11.Draw("E1X0 same")

        if False: 
          if (('Displaced' in h2Legend) and ('hybrid' in h2Legend)) or '(hybrid)' in h2Legend:
            setEmptyBins(h21)
        #h21.SetFillColor(kViolet)
        h21.SetLineColor(kViolet)
        h21.SetMarkerColor(kViolet)
        h21.SetMarkerStyle(21)
        h21.Draw("E1X0 same")

        if False: 
          if (('Displaced' in h3Legend) and ('hybrid' in h3Legend)) or '(hybrid)' in h3Legend:
            tex = drawLabel("Note: p_{T,min}^{hybrid} = 5 GeV", 0.6,0.8)
            setEmptyBins(h31)
        #h31.SetFillColor(kBlue)
        h31.SetLineColor(kBlue)
        h31.SetMarkerColor(kBlue)
        h31.SetMarkerStyle(22)
        h31.Draw("E1X0 same")

      #latex = applyTdrStyle()

      leg = TLegend(0.15,0.2,0.5,0.35,legendTitle,"brNDC")
      leg.SetFillColor(kWhite)
      leg.SetBorderSize(0)
      leg.SetFillStyle(0)
      leg.SetTextSize(0.03)
      leg.AddEntry(h11, h1Legend, "p")
      leg.AddEntry(h21, h2Legend, "p")
      leg.AddEntry(h31, h3Legend, "p")
      leg.Draw("same")

      if doEta:
        title.replace("_rate_pt_", "_rate_eta_")

      c.SaveAs(targetDir + title + ext)
      c.SaveAs(targetDir + title + ".pdf")
      c.SaveAs(targetDir + title + ".C")

      return

      ## ratios
      c = TCanvas("c","c",800,600)
      c.Clear()
      gStyle.SetTitleBorderSize(0);
      gStyle.SetPadLeftMargin(0.126);
      gStyle.SetPadRightMargin(0.04);
      gStyle.SetPadTopMargin(0.06);
      gStyle.SetPadBottomMargin(0.13);
#      gPad.SetLogy(1)

      b1 = TH1F("b1","b1",29,myptbin)
      b1.GetYaxis().SetRangeUser(0.01,1)
      b1.GetYaxis().SetTitleOffset(1.2)
      b1.GetYaxis().SetNdivisions(520)
      b1.GetYaxis().SetTitle("Ratio (normalized to prompt L1Mu)")
      b1.GetXaxis().SetTitle("L1Mu p_{T} cut [GeV]")
      b1.GetXaxis().SetTitleFont(62)
      b1.GetXaxis().SetTitleOffset(1.2)
      b1.GetXaxis().SetTitleSize(0.05)
      b1.GetYaxis().SetTitleSize(0.05)
      b1.SetTitle("                                                                  14TeV, " + pu)
      b1.SetStats(0)
      b1.Draw()

      #if isolation_cone != 0.12:
      h2.SetLineColor(kMagenta)
      h2.SetFillColor(kWhite)
      h2.Divide(h1)
      h2.Draw("same")

      h3.SetLineColor(kBlue)
      h3.SetFillColor(kWhite)
      h3.Divide(h1)
      h3.Draw("same")

      h4.SetLineColor(kGreen+1)
      h4.SetFillColor(kWhite)
      h4.Divide(h1)
      h4.Draw("same")

      h5.SetLineColor(kOrange+1)
      h5.SetFillColor(kWhite)
      h5.Divide(h1)
      h5.Draw("same")

      latex = applyTdrStyle()

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


      c.SaveAs(targetDir + title + "_ratio" + ext)
      c.SaveAs(targetDir + title + "_ratio.C")
      c.SaveAs(targetDir + title + "_ratio.pdf")


    ## Calibration plots
    makePlots("0.0<|#eta|<2.4",
              "h_single_prompt_L1Mu_rate_pt_eta0to2p4", "Prompt L1Mu, all",
              "h_single_prompt_L1Mu_rate_pt_eta1p1to2p4", "Prompt L1Mu, endcap",
              "h_single_prompt_L1Mu_rate_pt_eta0to1p1", "Prompt L1Mu, barrel",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__CALIBRATE__eta0to2p4")
    makeEtaPlots("0.0<|#eta|<2.4",
                 "h_single_prompt_L1Mu_rate_eta_eta0to2p4", "Prompt L1Mu, all",
                 "h_single_prompt_L1Mu_rate_eta_eta1p1to2p4", "Prompt L1Mu, endcap",
                 "h_single_prompt_L1Mu_rate_eta_eta0to1p1", "Prompt L1Mu, barrel",
                 "Prompt_L1Mu_trigger_rate_eta__L1Mu__CALIBRATE__eta0to2p4")

    ## trigger rate plots
    makePlots("0.0<|#eta|<2.4",
              "h_single_prompt_L1Mu_rate_pt_eta0to2p4", "Prompt L1Mu",
              "h_single_prompt_L1Mu_rate_pt_2_stubs_eta0to2p4", "Prompt L1Mu, 2 stubs",
              "h_single_prompt_L1Mu_rate_pt_3_stubs_eta0to2p4", "Prompt L1Mu, 3 stubs",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu2st__L1Mu3st_eta0to2p4")
    makeEtaPlots("0.0<|#eta|<2.4",
              "h_single_prompt_L1Mu_rate_eta_eta0to2p4", "Prompt L1Mu",
              "h_single_prompt_L1Mu_rate_eta_2_stubs_eta0to2p4", "Prompt L1Mu, 2 stubs",
              "h_single_prompt_L1Mu_rate_eta_3_stubs_eta0to2p4", "Prompt L1Mu, 3 stubs",
              "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu2st__L1Mu3st_eta0to2p4")


    makePlots("1.2<|#eta|<2.4",
              "h_single_prompt_L1Mu_rate_pt_eta1p2to2p4", "Prompt L1Mu",
              "h_single_prompt_L1Mu_rate_pt_2_stubs_eta1p2to2p4", "Prompt L1Mu, 2 CSC stubs",
              "h_single_prompt_L1Mu_rate_pt_3_stubs_eta1p2to2p4", "Prompt L1Mu, 3 CSC stubs",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu2st__L1Mu3st_eta1p2to2p4")
    makeEtaPlots("1.2<|#eta|<2.4",
              "h_single_prompt_L1Mu_rate_eta_eta1p2to2p4", "Prompt L1Mu",
              "h_single_prompt_L1Mu_rate_eta_2_stubs_eta1p2to2p4", "Prompt L1Mu, 2 CSC stubs",
              "h_single_prompt_L1Mu_rate_eta_3_stubs_eta1p2to2p4", "Prompt L1Mu, 3 CSC stubs",
              "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu2st__L1Mu3st_eta1p2to2p4")


    makePlots("1.6<|#eta|<2.2",
              "h_single_prompt_L1Mu_rate_pt_eta1p6to2p2", "Prompt L1Mu",
              "h_single_prompt_L1Mu_rate_pt_2_stubs_eta1p6to2p2", "Prompt L1Mu, 2 CSC stubs",
              "h_single_prompt_L1Mu_rate_pt_3_stubs_eta1p6to2p2", "Prompt L1Mu, 3 CSC stubs",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu2st__L1Mu3st_eta1p6to2p2")
    makeEtaPlots("1.6<|#eta|<2.2",
              "h_single_prompt_L1Mu_rate_eta_eta1p6to2p2", "Prompt L1Mu",
              "h_single_prompt_L1Mu_rate_eta_2_stubs_eta1p6to2p2", "Prompt L1Mu, 2 CSC stubs",
              "h_single_prompt_L1Mu_rate_eta_3_stubs_eta1p6to2p2", "Prompt L1Mu, 3 CSC stubs",
              "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu2st__L1Mu3st_eta1p6to2p2")


    makePlots("1.6<|#eta|<2.15",
              "h_single_prompt_L1Mu_rate_pt_eta1p6to2p15", "Prompt L1Mu",
              "h_single_prompt_L1Mu_rate_pt_2_stubs_eta1p6to2p15", "Prompt L1Mu, 2 CSC stubs",
              "h_single_prompt_L1Mu_rate_pt_3_stubs_eta1p6to2p15", "Prompt L1Mu, 3 CSC stubs",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu2st__L1Mu3st_eta1p6to2p15")
    makeEtaPlots("1.6<|#eta|<2.15",
              "h_single_prompt_L1Mu_rate_eta_eta1p6to2p15", "Prompt L1Mu",
              "h_single_prompt_L1Mu_rate_eta_2_stubs_eta1p6to2p15", "Prompt L1Mu, 2 CSC stubs",
              "h_single_prompt_L1Mu_rate_eta_3_stubs_eta1p6to2p15", "Prompt L1Mu, 3 CSC stubs",
              "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu2st__L1Mu3st_eta1p6to2p15")


    makePlots("1.2<|#eta|<1.6",
              "h_single_prompt_L1Mu_rate_pt_eta1p2to1p6", "Prompt L1Mu",
              "h_single_prompt_L1Mu_rate_pt_2_stubs_eta1p2to1p6", "Prompt L1Mu, 2 CSC stubs",
              "h_single_prompt_L1Mu_rate_pt_3_stubs_eta1p2to1p6", "Prompt L1Mu, 3 CSC stubs",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu2st__L1Mu3st_eta1p2to1p6")
    makeEtaPlots("1.2<|#eta|<1.6",
              "h_single_prompt_L1Mu_rate_eta_eta1p2to1p6", "Prompt L1Mu",
              "h_single_prompt_L1Mu_rate_eta_2_stubs_eta1p2to1p6", "Prompt L1Mu, 2 CSC stubs",
              "h_single_prompt_L1Mu_rate_eta_3_stubs_eta1p2to1p6", "Prompt L1Mu, 3 CSC stubs",
              "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu2st__L1Mu3st_eta1p2to1p6")


    makePlots("1.6<|#eta|<2.2",
              "h_single_prompt_L1Mu_rate_pt_eta1p6to2p2", "Prompt L1Mu",
              "h_single_prompt_L1Mu_rate_pt_2_stubs_eta1p6to2p2", "Prompt L1Mu, 2 CSC stubs",
              "h_single_prompt_L1Mu_rate_pt_2_stubs_ME11_eta1p6to2p2", "Prompt L1Mu, 2 CSC stubs, ME11",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu2st__L1Mu2stME11_eta1p6to2p2")
    makeEtaPlots("1.6<|#eta|<2.2",
              "h_single_prompt_L1Mu_rate_eta_eta1p6to2p2", "Prompt L1Mu",
              "h_single_prompt_L1Mu_rate_eta_2_stubs_eta1p6to2p2", "Prompt L1Mu, 2 CSC stubs",
              "h_single_prompt_L1Mu_rate_eta_2_stubs_ME11_eta1p6to2p2", "Prompt L1Mu, 2 CSC stubs, ME11",
              "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu2st__L1Mu2stME11_eta1p6to2p2")


    makePlots("1.6<|#eta|<2.2",
              "h_single_prompt_L1Mu_rate_pt_eta1p6to2p2", "Prompt L1Mu",
              "h_single_prompt_L1Mu_rate_pt_3_stubs_eta1p6to2p2", "Prompt L1Mu, 3 CSC stubs",
              "h_single_prompt_L1Mu_rate_pt_3_stubs_ME11_eta1p6to2p2", "Prompt L1Mu, 3 CSC stubs, ME11",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu3st__L1Mu3stME11_eta1p6to2p2")
    makeEtaPlots("1.6<|#eta|<2.2",
              "h_single_prompt_L1Mu_rate_eta_eta1p6to2p2", "Prompt L1Mu",
              "h_single_prompt_L1Mu_rate_eta_3_stubs_eta1p6to2p2", "Prompt L1Mu, 3 CSC stubs",
              "h_single_prompt_L1Mu_rate_eta_3_stubs_ME11_eta1p6to2p2", "Prompt L1Mu, 3 CSC stubs, ME11",
              "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu3st__L1Mu3stME11_eta1p6to2p2")


    makePlots("1.6<|#eta|<2.15",
              "h_single_prompt_L1Mu_rate_pt_eta1p6to2p15", "Prompt L1Mu",
              "h_single_prompt_L1Mu_rate_pt_2_stubs_ME11_eta1p6to2p15", "Prompt L1Mu, 2 CSC stubs, ME11",
              "h_single_prompt_L1Mu_rate_pt_2_stubs_GE11_ME11_eta1p6to2p15", "Prompt L1Mu, 2 CSC stubs, ME11, GE11",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu2stME11__L1Mu2stME11GE11_eta1p6to2p15")
    makeEtaPlots("1.6<|#eta|<2.15",
              "h_single_prompt_L1Mu_rate_eta_eta1p6to2p15", "Prompt L1Mu",
              "h_single_prompt_L1Mu_rate_eta_2_stubs_ME11_eta1p6to2p15", "Prompt L1Mu, 2 CSC stubs, ME11",
              "h_single_prompt_L1Mu_rate_eta_2_stubs_GE11_ME11_eta1p6to2p15", "Prompt L1Mu, 2 CSC stubs, ME11, GE11",
              "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu2stME11__L1Mu2stME11GE11_eta1p6to2p15")


    makePlots("1.6<|#eta|<2.15",
              "h_single_prompt_L1Mu_rate_pt_eta1p6to2p15", "Prompt L1Mu",
              "h_single_prompt_L1Mu_rate_pt_ME1_ME2_ME3_eta1p6to2p15", "Prompt L1Mu, hit in ME1, ME2, ME3",
              "h_single_displaced_L1Mu_rate_pt_position_ME1_ME2_ME3_eta1p6to2p15", "Displaced L1Mu, hit in ME1, ME2, ME3, position based",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu3st__DisplacedL1MuPositionBased_ME1_ME2_ME3_eta1p6to2p15")
    makeEtaPlots("1.6<|#eta|<2.15",
                 "h_single_prompt_L1Mu_rate_eta_eta1p6to2p15", "Prompt L1Mu",
                 "h_single_prompt_L1Mu_rate_eta_ME1_ME2_ME3_eta1p6to2p15", "Prompt L1Mu, hit in ME1, ME2, ME3",
                 "h_single_displaced_L1Mu_rate_eta_position_ME1_ME2_ME3_eta1p6to2p15", "Displaced L1Mu, hit in ME1, ME2, ME3 position based",
                 "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu3st__DisplacedL1MuPositionBased_ME1_ME2_ME3_eta1p6to2p15", doEta=True)


    makePlots("1.2<|#eta|<2.4",
              "h_single_prompt_L1Mu_rate_pt_eta1p2to2p4", "Prompt L1Mu",
              "h_single_prompt_L1Mu_rate_pt_ME1_ME2_ME3_eta1p2to2p4", "Prompt L1Mu, hit in ME1, ME2, ME3",
              "h_single_displaced_L1Mu_rate_pt_position_ME1_ME2_ME3_eta1p2to2p4", "Displaced L1Mu, hit in ME1, ME2, ME3, position based",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu3st__DisplacedL1MuPositionBased_ME1_ME2_ME3_eta1p2to2p4")
    makeEtaPlots("1.2<|#eta|<2.4",
                 "h_single_prompt_L1Mu_rate_eta_eta1p2to2p4", "Prompt L1Mu",
                 "h_single_prompt_L1Mu_rate_eta_ME1_ME2_ME3_eta1p2to2p4", "Prompt L1Mu, hit in ME1, ME2, ME3",
                 "h_single_displaced_L1Mu_rate_eta_position_ME1_ME2_ME3_eta1p2to2p4", "Displaced L1Mu, hit in ME1, ME2, ME3 position based",
                 "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu3st__DisplacedL1MuPositionBased_ME1_ME2_ME3_eta1p2to2p4", doEta=True)


    makePlots("1.6<|#eta|<2.15",
              "h_single_prompt_L1Mu_rate_pt_eta1p6to2p15", "Prompt L1Mu",
              "h_single_prompt_L1Mu_rate_pt_GE11_ME11_GE21_ME21_ME3_eta1p6to2p15", "Prompt L1Mu, hit in GE11, ME11, GE21, ME21, ME3",
              "h_single_displaced_L1Mu_rate_pt_hybrid_GE11_ME11_GE21_ME21_ME3_eta1p6to2p15", "Displaced L1Mu, hit in GE11, ME11, GE21, ME21, ME3 hybrid based",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu3st__DisplacedL1MuHybridBased_GE11_ME11_GE21_ME21_ME3_eta1p6to2p15")
    makeEtaPlots("1.6<|#eta|<2.15",
                 "h_single_prompt_L1Mu_rate_eta_eta1p6to2p15", "Prompt L1Mu",
                 "h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_ME3_eta1p6to2p15", "Prompt L1Mu, hit in GE11, ME11, GE21, ME21, ME3",
                 "h_single_displaced_L1Mu_rate_eta_hybrid_GE11_ME11_GE21_ME21_ME3_eta1p6to2p15", "Displaced L1Mu, hit in GE11, ME11, GE21, ME21, ME3 hybrid based",
                 "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu3st__DisplacedL1MuHybridBased_GE11_ME11_GE21_ME21_ME3_eta1p6to2p15")


    makePlots("1.6<|#eta|<2.15",
              "h_single_prompt_L1Mu_rate_pt_eta1p6to2p15", "Prompt L1Mu",
              "h_single_prompt_L1Mu_rate_pt_GE11_ME11_ME21_ME3_eta1p6to2p15", "Prompt L1Mu, hit in GE11, ME11, ME21, ME3",
              "h_single_displaced_L1Mu_rate_pt_hybrid_GE11_ME11_ME21_ME3_eta1p6to2p15", "Displaced L1Mu, hit in GE11, ME11, ME21, ME3 hybrid based",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu3st__DisplacedL1MuHybridBased_GE11_ME11_ME21_ME3_eta1p6to2p15")
    makeEtaPlots("1.6<|#eta|<2.15",
                 "h_single_prompt_L1Mu_rate_eta_eta1p6to2p15", "Prompt L1Mu",
                 "h_single_prompt_L1Mu_rate_eta_GE11_ME11_ME21_ME3_eta1p6to2p15", "Prompt L1Mu, hit in GE11, ME11, ME21, ME3",
                 "h_single_displaced_L1Mu_rate_eta_hybrid_GE11_ME11_ME21_ME3_eta1p6to2p15", "Displaced L1Mu, hit in GE11, ME11, ME21, ME3 hybrid based",
                 "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu3st__DisplacedL1MuHybridBased_GE11_ME11_ME21_ME3_eta1p6to2p15")



    ### FINAL PLOTS FOR MUON TDR ###
    makePlots("1.6<|#eta|<2.15",
                 "h_single_prompt_L1Mu_rate_pt_ME1_ME2_ME3_eta1p6to2p15", "L1Mu (constrained)",
                 "h_single_displaced_L1Mu_rate_pt_position_ME1_ME2_ME3_eta1p6to2p15", "L1Mu (unconstrained)",
                 "h_single_displaced_L1Mu_rate_pt_hybrid_GE11_ME11_GE21_ME21_ME3_eta1p6to2p15", "L1Mu (hybrid)",
                 "MuonTDR2017_Prompt_L1Mu_trigger_rate_pt__L1Mu__PositionBased_HybridBased_GE11_ME11_GE21_ME21_ME3_eta1p6to2p15")

    makeEtaPlots("1.6<|#eta|<2.15",
                 "h_single_prompt_L1Mu_rate_eta_ME1_ME2_ME3_eta1p6to2p15", "L1Mu (constrained)",
                 "h_single_displaced_L1Mu_rate_eta_position_ME1_ME2_ME3_eta1p6to2p15", "L1Mu (unconstrained)",
                 "h_single_displaced_L1Mu_rate_eta_hybrid_GE11_ME11_GE21_ME21_ME3_eta1p6to2p15", "L1Mu (hybrid)",
                 "MuonTDR2017_Prompt_L1Mu_trigger_rate_eta__L1Mu__PositionBased_HybridBased_GE11_ME11_GE21_ME21_ME3_eta1p6to2p15")
    exit(1)



    makePlots("1.6<|#eta|<2.2",
              "h_single_prompt_L1Mu_rate_pt_eta1p6to2p2", "Prompt L1Mu",
              "h_single_prompt_L1Mu_rate_pt_3_stubs_ME11_eta1p6to2p2", "Prompt L1Mu, 3 CSC stubs, ME11",
              "h_single_prompt_L1Mu_rate_pt_3_stubs_GE11_ME11_eta1p6to2p2", "Prompt L1Mu, 3 CSC stubs, ME11, GE11",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu3stME11__L1Mu3stME11GE11_eta1p6to2p2")
    makeEtaPlots("1.6<|#eta|<2.2",
              "h_single_prompt_L1Mu_rate_eta_eta1p6to2p2", "Prompt L1Mu",
              "h_single_prompt_L1Mu_rate_eta_3_stubs_ME11_eta1p6to2p2", "Prompt L1Mu, 3 CSC stubs, ME11",
              "h_single_prompt_L1Mu_rate_eta_3_stubs_GE11_ME11_eta1p6to2p2", "Prompt L1Mu, 3 CSC stubs, ME11, GE11",
              "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu3stME11__L1Mu3stME11GE11_eta1p6to2p2")


    makePlots("1.6<|#eta|<2.2",
              "h_single_prompt_L1Mu_rate_pt_eta1p6to2p2", "Prompt L1Mu",
              "h_single_prompt_L1Mu_rate_pt_2_stubs_ME21_eta1p6to2p2", "Prompt L1Mu, 2 CSC stubs, ME21",
              "h_single_prompt_L1Mu_rate_pt_2_stubs_GE21_ME21_eta1p6to2p2", "Prompt L1Mu, 2 CSC stubs, ME21, GE21",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu2stME21__L1Mu2stME21GE21_eta1p6to2p2")
    makeEtaPlots("1.6<|#eta|<2.2",
              "h_single_prompt_L1Mu_rate_eta_eta1p6to2p2", "Prompt L1Mu",
              "h_single_prompt_L1Mu_rate_eta_2_stubs_ME21_eta1p6to2p2", "Prompt L1Mu, 2 CSC stubs, ME21",
              "h_single_prompt_L1Mu_rate_eta_2_stubs_GE21_ME21_eta1p6to2p2", "Prompt L1Mu, 2 CSC stubs, ME21, GE21",
              "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu2stME21__L1Mu2stME21GE21_eta1p6to2p2")


    makePlots("1.6<|#eta|<2.2",
              "h_single_prompt_L1Mu_rate_pt_eta1p6to2p2", "Prompt L1Mu",
              "h_single_prompt_L1Mu_rate_pt_3_stubs_ME21_eta1p6to2p2", "Prompt L1Mu, 3 CSC stubs, ME21",
              "h_single_prompt_L1Mu_rate_pt_3_stubs_GE21_ME21_eta1p6to2p2", "Prompt L1Mu, 3 CSC stubs, ME21, GE21",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu3stME21__L1Mu3stME21GE21_eta1p6to2p2")
    makeEtaPlots("1.6<|#eta|<2.2",
              "h_single_prompt_L1Mu_rate_eta_eta1p6to2p2", "Prompt L1Mu",
              "h_single_prompt_L1Mu_rate_eta_3_stubs_ME21_eta1p6to2p2", "Prompt L1Mu, 3 CSC stubs, ME21",
              "h_single_prompt_L1Mu_rate_eta_3_stubs_GE21_ME21_eta1p6to2p2", "Prompt L1Mu, 3 CSC stubs, ME21, GE21",
              "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu3stME21__L1Mu3stME21GE21_eta1p6to2p2")


    makePlots("1.6<|#eta|<2.2",
              "h_single_prompt_L1Mu_rate_pt_2_stubs_ME11_eta1p6to2p2", "Prompt L1Mu, 2 CSC stubs, ME11",
              "h_single_prompt_L1Mu_rate_pt_2_stubs_GE11_ME11_eta1p6to2p2", "Prompt L1Mu, 2 CSC stubs, ME11, GE11",
              "h_single_prompt_L1Mu_rate_pt_GE11_ME11_GE21_ME21_eta1p6to2p2", "Prompt L1Mu, 2 CSC stubs, ME11, GE11, ME21, GE21",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu2stME11__L1Mu2stME11GE11__L1Mu2stME11GE11GE21_eta1p6to2p2")
    makeEtaPlots("1.6<|#eta|<2.2",
              "h_single_prompt_L1Mu_rate_eta_2_stubs_ME11_eta1p6to2p2", "Prompt L1Mu, 2 CSC stubs, ME11",
              "h_single_prompt_L1Mu_rate_eta_2_stubs_GE11_ME11_eta1p6to2p2", "Prompt L1Mu, 2 CSC stubs, ME11, GE11",
              "h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta1p6to2p2", "Prompt L1Mu, 2 CSC stubs, ME11, GE11, ME21, GE21",
              "Prompt_L1Mu_trigger_rate_eta__L1Mu2stME11__L1Mu2stME11GE11__L1Mu2stME11GE11GE21_eta1p6to2p2")



    makePlots("1.6<|#eta|<2.2",
              "h_single_prompt_L1Mu_rate_pt_3_stubs_ME11_eta1p6to2p2", "Prompt L1Mu, 3 CSC stubs, ME11",
              "h_single_prompt_L1Mu_rate_pt_3_stubs_GE11_ME11_eta1p6to2p2", "Prompt L1Mu, 3 CSC stubs, ME11, GE11",
              "h_single_prompt_L1Mu_rate_pt_GE11_ME11_GE21_ME21_eta1p6to2p2", "Prompt L1Mu, 3 CSC stubs, ME11, ME21, GE11, GE21",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu3stME11__L1Mu3stME11GE11__L1Mu3stME11GE11GE21_eta1p6to2p2")
    makeEtaPlots("1.6<|#eta|<2.2",
              "h_single_prompt_L1Mu_rate_eta_3_stubs_ME11_eta1p6to2p2", "Prompt L1Mu, 3 CSC stubs, ME11",
              "h_single_prompt_L1Mu_rate_eta_3_stubs_GE11_ME11_eta1p6to2p2", "Prompt L1Mu, 3 CSC stubs, ME11, GE11",
              "h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta1p6to2p2", "Prompt L1Mu, 3 CSC stubs, ME11, ME21, GE11, GE21",
              "Prompt_L1Mu_trigger_rate_eta__L1Mu3stME11__L1Mu3stME11GE11__L1Mu3stME11GE11GE21_eta1p6to2p2")

    """
    makePlots("1.6<|#eta|<2.2",
              "h_single_prompt_L1Mu_rate_pt_2_stubs_ME11_eta1p6to2p2", "Prompt L1Mu, 2 CSC stubs, ME11",
              "h_single_prompt_L1Mu_rate_pt_2_stubs_GE11_ME11_eta1p6to2p2", "Prompt L1Mu, 2 CSC stubs, ME11, GE11",
              "h_single_prompt_L1Mu_rate_pt_2_stubs_GE11_ME11_OR_GE21_ME21_eta1p6to2p2", "Prompt L1Mu, 2 CSC stubs, GE11 or GE21",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu2stME11__L1Mu2stME11GE11__L1Mu2stGE11GE21_eta1p6to2p2")
    makeEtaPlots("1.6<|#eta|<2.2",
              "h_single_prompt_L1Mu_rate_eta_2_stubs_ME11_eta1p6to2p2", "Prompt L1Mu, 2 CSC stubs, ME11",
              "h_single_prompt_L1Mu_rate_eta_2_stubs_GE11_ME11_eta1p6to2p2", "Prompt L1Mu, 2 CSC stubs, ME11, GE11",
              "h_single_prompt_L1Mu_rate_eta_2_stubs_GE11_ME11_OR_GE21_ME21_eta1p6to2p2", "Prompt L1Mu, 2 CSC stubs, GE11 or GE21",
              "Prompt_L1Mu_trigger_rate_eta__L1Mu2stME11__L1Mu2stME11GE11__L1Mu2stGE11GE21_eta1p6to2p2")


    makePlots("1.6<|#eta|<2.2",
              "h_single_prompt_L1Mu_rate_pt_3_stubs_ME11_eta1p6to2p2", "Prompt L1Mu, 3 CSC stubs, ME11",
              "h_single_prompt_L1Mu_rate_pt_3_stubs_GE11_ME11_eta1p6to2p2", "Prompt L1Mu, 3 CSC stubs, ME11, GE11",
              "h_single_prompt_L1Mu_rate_pt_3_stubs_GE11_ME11_OR_GE21_ME21_eta1p6to2p2", "Prompt L1Mu, 3 CSC stubs, GE11 or GE21",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu3stME11__L1Mu3stME11GE11__L1Mu3stGE11GE21_eta1p6to2p2")
    makeEtaPlots("1.6<|#eta|<2.2",
              "h_single_prompt_L1Mu_rate_eta_3_stubs_ME11_eta1p6to2p2", "Prompt L1Mu, 3 CSC stubs, ME11",
              "h_single_prompt_L1Mu_rate_eta_3_stubs_GE11_ME11_eta1p6to2p2", "Prompt L1Mu, 3 CSC stubs, ME11, GE11",
              "h_single_prompt_L1Mu_rate_eta_3_stubs_GE11_ME11_OR_GE21_ME21_eta1p6to2p2", "Prompt L1Mu, 3 CSC stubs, GE11 or GE21",
              "Prompt_L1Mu_trigger_rate_eta__L1Mu3stME11__L1Mu3stME11GE11__L1Mu3stGE11GE21_eta1p6to2p2")
    """



    exit(1)
    ## displaced L1Mu trigger plots
    ## trigger rate plots vs pt



    makePlots("1.6<|#eta|<2.2",
              "h_single_prompt_L1Mu_rate_pt_eta1p6to2p2", "Prompt L1Mu",
              "h_single_prompt_L1Mu_rate_pt_GE11_ME11_GE21_ME21_eta1p6to2p2", "Prompt L1Mu, hit in GE11, ME11, GE21, ME21",
              "h_single_displaced_L1Mu_rate_pt_direction_GE11_ME11_GE21_ME21_eta1p6to2p2", "Displaced L1Mu, hit in GE11, ME11, GE21, ME21 direction based",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu3st__DisplacedL1MuDirectionBased_GE11_ME11_GE21_ME21_eta1p6to2p2")


    makePlots("1.6<|#eta|<2.2",
              "h_single_prompt_L1Mu_rate_pt_eta1p6to2p2", "Prompt L1Mu",
              "h_single_prompt_L1Mu_rate_pt_GE11_ME11_ME21_ME3_eta1p6to2p2", "Prompt L1Mu, hit in GE11, ME11, ME21, ME3",
              "h_single_displaced_L1Mu_rate_pt_hybrid_GE11_ME11_ME21_ME3_eta1p6to2p2", "Displaced L1Mu, hit in GE11, ME11, ME21, ME3 hybrid based",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu3st__DisplacedL1MuHybridBased_GE11_ME11_ME21_ME3_eta1p6to2p2")

    makePlots("1.2<|#eta|<2.2",
              "h_single_prompt_L1Mu_rate_pt_eta1p2to2p2", "Prompt L1Mu",
              "h_single_prompt_L1Mu_rate_pt_ME1_ME2_ME3_eta1p2to2p2", "Prompt L1Mu, hit in ME1, ME2, ME3",
              "h_single_displaced_L1Mu_rate_pt_hybrid_ME1_ME2_ME3_eta1p2to2p2", "Displaced L1Mu, hit in ME1, ME2, ME3 hybrid based",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu3st__DisplacedL1MuHybridBased_ME1_ME2_ME3_eta1p2to2p2")

    makePlots("0.0<|#eta|<0.9",
              "h_single_prompt_L1Mu_rate_pt_eta0to0p9", "Prompt L1Mu",
              "h_single_prompt_L1Mu_rate_pt_MB1_MB4_eta0to0p9", "Prompt L1Mu, hit in MB1, MB4",
              "h_single_displaced_L1Mu_rate_pt_direction_MB1_MB4_eta0to0p9", "Displaced L1Mu, hit in MB1, MB4, direction based",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu2st__DisplacedL1Mu2st_MB1_MB4_eta0to0p9")

    ## rates vs eta

    makeEtaPlots("1.6<|#eta|<2.2",
                 "h_single_prompt_L1Mu_rate_eta_eta1p6to2p2", "Prompt L1Mu",
                 "h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta1p6to2p2", "Prompt L1Mu, hit in GE11, ME11, GE21, ME21",
                 "h_single_displaced_L1Mu_rate_eta_direction_GE11_ME11_GE21_ME21_eta1p6to2p2", "Displaced L1Mu, hit in GE11, ME11, GE21, ME21 direction based",
                 "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu3st__DisplacedL1MuDirectionBased_GE11_ME11_GE21_ME21_eta1p6to2p2", doEta=True)

    makeEtaPlots("1.6<|#eta|<2.2",
                 "h_single_prompt_L1Mu_rate_eta_eta1p6to2p2", "Prompt L1Mu",
                 "h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_ME3_eta1p6to2p2", "Prompt L1Mu, hit in GE11, ME11, GE21, ME21, ME3",
                 "h_single_displaced_L1Mu_rate_eta_hybrid_GE11_ME11_GE21_ME21_ME3_eta1p6to2p2", "Displaced L1Mu, hit in GE11, ME11, GE21, ME21, ME3 hybrid based",
                 "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu3st__DisplacedL1MuHybridBased_GE11_ME11_GE21_ME21_ME3_eta1p6to2p2", doEta=True)

    makeEtaPlots("1.6<|#eta|<2.2",
                 "h_single_prompt_L1Mu_rate_eta_eta1p6to2p2", "Prompt L1Mu",
                 "h_single_prompt_L1Mu_rate_eta_ME1_ME2_ME3_eta1p6to2p2", "Prompt L1Mu, hit in ME1, ME2, ME3",
                 "h_single_displaced_L1Mu_rate_eta_hybrid_GE11_ME1_ME2_ME3_eta1p6to2p2", "Displaced L1Mu, hit in ME1, ME2, ME3 hybrid based",
                 "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu3st__DisplacedL1MuHybridBased_ME1_ME2_ME3_eta1p6to2p2")

    makeEtaPlots("1.2<|#eta|<2.2",
                 "h_single_prompt_L1Mu_rate_eta_eta1p2to2p2", "Prompt L1Mu",
                 "h_single_prompt_L1Mu_rate_eta_ME1_ME2_ME3_eta1p2to2p2", "Prompt L1Mu, hit in ME1, ME2, ME3",
                 "h_single_displaced_L1Mu_rate_eta_hybrid_ME1_ME2_ME3_eta1p2to2p2", "Displaced L1Mu, hit in ME1, ME2, ME3 hybrid based",
                 "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu3st__DisplacedL1MuHybridBased_ME1_ME2_ME3_eta1p2to2p2")

    makeEtaPlots("0.0<|#eta|<0.9",
                 "h_single_prompt_L1Mu_rate_eta_eta0to0p9", "Prompt L1Mu",
                 "h_single_prompt_L1Mu_rate_eta_MB1_MB4_eta0to0p9", "Prompt L1Mu, hit in MB1, MB4",
                 "h_single_displaced_L1Mu_rate_eta_direction_MB1_MB4_eta0to0p9", "Displaced L1Mu, hit in MB1, MB4, direction based",
                 "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu2st__DisplacedL1Mu2st_MB1_MB4_eta0to0p9")


    ## rates with isolation
    ## trigger rate plots vs pt
    makePlots("1.6<|#eta|<2.2",
              "h_single_prompt_L1Mu_rate_pt_ME1_ME2_ME3_eta1p6to2p2", "Prompt L1Mu, hit in ME1, ME2, ME3",
              "h_single_displaced_L1Mu_rate_pt_position_ME1_ME2_ME3_eta1p6to2p2", "Displaced L1Mu, hit in ME1, ME2, ME3, position based",
              "h_single_displaced_L1Mu_rate_pt_position_ME1_ME2_ME3_eta1p6to2p2_looseVeto", "Displaced L1Mu, hit in ME1, ME2, ME3, position based, loose veto",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu3st__DisplacedL1MuPositionBased_ME1_ME2_ME3_eta1p6to2p2_looseVeto")

    makePlots("1.2<|#eta|<2.4",
              "h_single_prompt_L1Mu_rate_pt_ME1_ME2_ME3_eta1p2to2p4", "Prompt L1Mu, hit in ME1, ME2, ME3",
              "h_single_displaced_L1Mu_rate_pt_position_ME1_ME2_ME3_eta1p2to2p4", "Displaced L1Mu, hit in ME1, ME2, ME3, position based",
              "h_single_displaced_L1Mu_rate_pt_position_ME1_ME2_ME3_eta1p2to2p4_looseVeto", "Displaced L1Mu, hit in ME1, ME2, ME3, position based, loose veto",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu3st__DisplacedL1MuPositionBased_ME1_ME2_ME3_eta1p2to2p4_looseVeto")

    makePlots("1.6<|#eta|<2.2",
              "h_single_prompt_L1Mu_rate_pt_GE11_ME11_GE21_ME21_eta1p6to2p2", "Prompt L1Mu, hit in GE11, ME11, GE21, ME21",
              "h_single_displaced_L1Mu_rate_pt_direction_GE11_ME11_GE21_ME21_eta1p6to2p2", "Displaced L1Mu, hit in GE11, ME11, GE21, ME21 direction based",
              "h_single_displaced_L1Mu_rate_pt_direction_GE11_ME11_GE21_ME21_eta1p6to2p2_looseVeto", "Displaced L1Mu, hit in GE11, ME11, GE21, ME21 direction based, loose veto",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu3st__DisplacedL1MuDirectionBased_GE11_ME11_GE21_ME21_eta1p6to2p2_looseVeto")

    makePlots("1.6<|#eta|<2.2",
              "h_single_prompt_L1Mu_rate_pt_GE11_ME11_GE21_ME21_ME3_eta1p6to2p2", "Prompt L1Mu, hit in GE11, ME11, GE21, ME21, ME3",
              "h_single_displaced_L1Mu_rate_pt_hybrid_GE11_ME11_GE21_ME21_ME3_eta1p6to2p2", "Displaced L1Mu, hit in GE11, ME11, GE21, ME21, ME3 hybrid based",
              "h_single_displaced_L1Mu_rate_pt_hybrid_GE11_ME11_GE21_ME21_ME3_eta1p6to2p2_looseVeto", "Displaced L1Mu, hit in GE11, ME11, GE21, ME21, ME3 hybrid based, loose veto",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu3st__DisplacedL1MuHybridBased_GE11_ME11_GE21_ME21_ME3_eta1p6to2p2_looseVeto")

    makePlots("1.6<|#eta|<2.2",
              "h_single_prompt_L1Mu_rate_pt_ME1_ME2_ME3_eta1p6to2p2", "Prompt L1Mu, hit in ME1, ME2, ME3",
              "h_single_displaced_L1Mu_rate_pt_hybrid_GE11_ME1_ME2_ME3_eta1p6to2p2", "Displaced L1Mu, hit in GE11, ME1, ME2, ME3 hybrid based",
              "h_single_displaced_L1Mu_rate_pt_hybrid_GE11_ME1_ME2_ME3_eta1p6to2p2_looseVeto", "Displaced L1Mu, hit in GE11, ME1, ME2, ME3 hybrid based, loose veto",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu3st__DisplacedL1MuHybridBased_ME1_ME2_ME3_eta1p6to2p2_looseVeto")

    makePlots("1.2<|#eta|<2.2",
              "h_single_prompt_L1Mu_rate_pt_ME1_ME2_ME3_eta1p2to2p2", "Prompt L1Mu, hit in ME1, ME2, ME3",
              "h_single_displaced_L1Mu_rate_pt_hybrid_ME1_ME2_ME3_eta1p2to2p2", "Displaced L1Mu, hit in ME1, ME2, ME3 hybrid based",
              "h_single_displaced_L1Mu_rate_pt_hybrid_ME1_ME2_ME3_eta1p2to2p2_looseVeto", "Displaced L1Mu, hit in ME1, ME2, ME3 hybrid based, loose veto",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu3st__DisplacedL1MuHybridBased_ME1_ME2_ME3_eta1p2to2p2_looseVeto")

    makePlots("0.0<|#eta|<0.9",
              "h_single_prompt_L1Mu_rate_pt_MB1_MB4_eta0to0p9", "Prompt L1Mu, hit in MB1, MB4",
              "h_single_displaced_L1Mu_rate_pt_direction_MB1_MB4_eta0to0p9", "Displaced L1Mu, hit in MB1, MB4, direction based",
              "h_single_displaced_L1Mu_rate_pt_direction_MB1_MB4_eta0to0p9_looseVeto", "Displaced L1Mu, hit in MB1, MB4, direction based, loose veto",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu2st__DisplacedL1Mu2st_MB1_MB4_eta0to0p9_looseVeto")

    ## rates vs eta
    makeEtaPlots("1.6<|#eta|<2.2",
                 "h_single_prompt_L1Mu_rate_eta_ME1_ME2_ME3_eta1p6to2p2", "Prompt L1Mu, hit in ME1, ME2, ME3",
                 "h_single_displaced_L1Mu_rate_eta_position_ME1_ME2_ME3_eta1p6to2p2", "Displaced L1Mu, hit in ME1, ME2, ME3 position based",
                 "h_single_displaced_L1Mu_rate_eta_position_ME1_ME2_ME3_eta1p6to2p2_looseVeto", "Displaced L1Mu, hit in ME1, ME2, ME3 position based, loose veto",
                 "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu3st__DisplacedL1MuPositionBased_ME1_ME2_ME3_eta1p6to2p2_looseVeto", doEta=True)

    makeEtaPlots("1.2<|#eta|<2.4",
                 "h_single_prompt_L1Mu_rate_eta_ME1_ME2_ME3_eta1p2to2p4", "Prompt L1Mu, hit in ME1, ME2, ME3",
                 "h_single_displaced_L1Mu_rate_eta_position_ME1_ME2_ME3_eta1p2to2p4", "Displaced L1Mu, hit in ME1, ME2, ME3 position based",
                 "h_single_displaced_L1Mu_rate_eta_position_ME1_ME2_ME3_eta1p2to2p4_looseVeto", "Displaced L1Mu, hit in ME1, ME2, ME3 position based, loose veto",
                 "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu3st__DisplacedL1MuPositionBased_ME1_ME2_ME3_eta1p2to2p4_looseVeto", doEta=True)

    makeEtaPlots("1.6<|#eta|<2.2",
                 "h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta1p6to2p2", "Prompt L1Mu, hit in GE11, ME11, GE21, ME21",
                 "h_single_displaced_L1Mu_rate_eta_direction_GE11_ME11_GE21_ME21_eta1p6to2p2", "Displaced L1Mu, hit in GE11, ME11, GE21, ME21 direction based",
                 "h_single_displaced_L1Mu_rate_eta_direction_GE11_ME11_GE21_ME21_eta1p6to2p2_looseVeto", "Displaced L1Mu, hit in GE11, ME11, GE21, ME21 direction based, loose veto",
                 "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu3st__DisplacedL1MuDirectionBased_GE11_ME11_GE21_ME21_eta1p6to2p2_looseVeto", doEta=True)

    makeEtaPlots("1.6<|#eta|<2.2",
                 "h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_ME3_eta1p6to2p2", "Prompt L1Mu, hit in GE11, ME11, GE21, ME21, ME3",
                 "h_single_displaced_L1Mu_rate_eta_hybrid_GE11_ME11_GE21_ME21_ME3_eta1p6to2p2", "Displaced L1Mu, hit in GE11, ME11, GE21, ME21, ME3 hybrid based",
                 "h_single_displaced_L1Mu_rate_eta_hybrid_GE11_ME11_GE21_ME21_ME3_eta1p6to2p2_looseVeto", "Displaced L1Mu, hit in GE11, ME11, GE21, ME21, ME3 hybrid based, loose veto",
                 "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu3st__DisplacedL1MuHybridBased_GE11_ME11_GE21_ME21_ME3_eta1p6to2p2_looseVeto", doEta=True)

    makeEtaPlots("1.6<|#eta|<2.2",
                 "h_single_prompt_L1Mu_rate_eta_ME1_ME2_ME3_eta1p6to2p2", "Prompt L1Mu, hit in ME1, ME2, ME3",
                 "h_single_displaced_L1Mu_rate_eta_hybrid_GE11_ME1_ME2_ME3_eta1p6to2p2", "Displaced L1Mu, hit in GE11, ME1, ME2, ME3 hybrid based",
                 "h_single_displaced_L1Mu_rate_eta_hybrid_GE11_ME1_ME2_ME3_eta1p6to2p2_looseVeto", "Displaced L1Mu, hit in GE11, ME1, ME2, ME3 hybrid based, loose veto",
                 "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu3st__DisplacedL1MuHybridBased_ME1_ME2_ME3_eta1p6to2p2_looseVeto")

    makeEtaPlots("1.2<|#eta|<2.2",
                 "h_single_prompt_L1Mu_rate_eta_ME1_ME2_ME3_eta1p2to2p2", "Prompt L1Mu, hit in ME1, ME2, ME3",
                 "h_single_displaced_L1Mu_rate_eta_hybrid_ME1_ME2_ME3_eta1p2to2p2", "Displaced L1Mu, hit in ME1, ME2, ME3 hybrid based",
                 "h_single_displaced_L1Mu_rate_eta_hybrid_ME1_ME2_ME3_eta1p2to2p2_looseVeto", "Displaced L1Mu, hit in ME1, ME2, ME3 hybrid based, loose veto",
                 "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu3st__DisplacedL1MuHybridBased_ME1_ME2_ME3_eta1p2to2p2_looseVeto")

    makeEtaPlots("0.0<|#eta|<0.9",
                 "h_single_prompt_L1Mu_rate_eta_MB1_MB4_eta0to0p9", "Prompt L1Mu, hit in MB1, MB4",
                 "h_single_displaced_L1Mu_rate_eta_direction_MB1_MB4_eta0to0p9", "Displaced L1Mu, hit in MB1, MB4, direction based",
                 "h_single_displaced_L1Mu_rate_eta_direction_MB1_MB4_eta0to0p9_looseVeto", "Displaced L1Mu, hit in MB1, MB4, direction based, loose veto",
                 "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu2st__DisplacedL1Mu2st_MB1_MB4_eta0to0p9_looseVeto")


    ## trigger rate plots vs pt
    makePlots("1.6<|#eta|<2.2",
              "h_single_prompt_L1Mu_rate_pt_ME1_ME2_ME3_eta1p6to2p2", "Prompt L1Mu, hit in ME1, ME2, ME3",
              "h_single_displaced_L1Mu_rate_pt_position_ME1_ME2_ME3_eta1p6to2p2", "Displaced L1Mu, hit in ME1, ME2, ME3, position based",
              "h_single_displaced_L1Mu_rate_pt_position_ME1_ME2_ME3_eta1p6to2p2_mediumVeto", "Displaced L1Mu, hit in ME1, ME2, ME3, position based, medium veto",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu3st__DisplacedL1MuPositionBased_ME1_ME2_ME3_eta1p6to2p2_mediumVeto")

    makePlots("1.2<|#eta|<2.4",
              "h_single_prompt_L1Mu_rate_pt_ME1_ME2_ME3_eta1p2to2p4", "Prompt L1Mu, hit in ME1, ME2, ME3",
              "h_single_displaced_L1Mu_rate_pt_position_ME1_ME2_ME3_eta1p2to2p4", "Displaced L1Mu, hit in ME1, ME2, ME3, position based",
              "h_single_displaced_L1Mu_rate_pt_position_ME1_ME2_ME3_eta1p2to2p4_mediumVeto", "Displaced L1Mu, hit in ME1, ME2, ME3, position based, medium veto",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu3st__DisplacedL1MuPositionBased_ME1_ME2_ME3_eta1p2to2p4_mediumVeto")

    makePlots("1.6<|#eta|<2.2",
              "h_single_prompt_L1Mu_rate_pt_GE11_ME11_GE21_ME21_eta1p6to2p2", "Prompt L1Mu, hit in GE11, ME11, GE21, ME21",
              "h_single_displaced_L1Mu_rate_pt_direction_GE11_ME11_GE21_ME21_eta1p6to2p2", "Displaced L1Mu, hit in GE11, ME11, GE21, ME21 direction based",
              "h_single_displaced_L1Mu_rate_pt_direction_GE11_ME11_GE21_ME21_eta1p6to2p2_mediumVeto", "Displaced L1Mu, hit in GE11, ME11, GE21, ME21 direction based, medium veto",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu3st__DisplacedL1MuDirectionBased_GE11_ME11_GE21_ME21_eta1p6to2p2_mediumVeto")

    makePlots("1.6<|#eta|<2.2",
              "h_single_prompt_L1Mu_rate_pt_GE11_ME11_GE21_ME21_ME3_eta1p6to2p2", "Prompt L1Mu, hit in GE11, ME11, GE21, ME21, ME3",
              "h_single_displaced_L1Mu_rate_pt_hybrid_GE11_ME11_GE21_ME21_ME3_eta1p6to2p2", "Displaced L1Mu, hit in GE11, ME11, GE21, ME21, ME3 hybrid based",
              "h_single_displaced_L1Mu_rate_pt_hybrid_GE11_ME11_GE21_ME21_ME3_eta1p6to2p2_mediumVeto", "Displaced L1Mu, hit in GE11, ME11, GE21, ME21, ME3 hybrid based, medium veto",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu3st__DisplacedL1MuHybridBased_GE11_ME11_GE21_ME21_ME3_eta1p6to2p2_mediumVeto")

    makePlots("1.6<|#eta|<2.2",
              "h_single_prompt_L1Mu_rate_pt_ME1_ME2_ME3_eta1p6to2p2", "Prompt L1Mu, hit in ME1, ME2, ME3",
              "h_single_displaced_L1Mu_rate_pt_hybrid_GE11_ME1_ME2_ME3_eta1p6to2p2", "Displaced L1Mu, hit in ME1, ME2, ME3 hybrid based",
              "h_single_displaced_L1Mu_rate_pt_hybrid_GE11_ME1_ME2_ME3_eta1p6to2p2_mediumVeto", "Displaced L1Mu, hit in ME1, ME2, ME3 hybrid based, medium veto",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu3st__DisplacedL1MuHybridBased_ME1_ME2_ME3_eta1p6to2p2_mediumVeto")

    makePlots("1.2<|#eta|<2.2",
              "h_single_prompt_L1Mu_rate_pt_ME1_ME2_ME3_eta1p2to2p2", "Prompt L1Mu, hit in ME1, ME2, ME3",
              "h_single_displaced_L1Mu_rate_pt_hybrid_ME1_ME2_ME3_eta1p2to2p2", "Displaced L1Mu, hit in ME1, ME2, ME3 hybrid based",
              "h_single_displaced_L1Mu_rate_pt_hybrid_ME1_ME2_ME3_eta1p2to2p2_mediumVeto", "Displaced L1Mu, hit in ME1, ME2, ME3 hybrid based, medium veto",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu3st__DisplacedL1MuHybridBased_ME1_ME2_ME3_eta1p2to2p2_mediumVeto")

    makePlots("0.0<|#eta|<0.9",
              "h_single_prompt_L1Mu_rate_pt_MB1_MB4_eta0to0p9", "Prompt L1Mu, hit in MB1, MB4",
              "h_single_displaced_L1Mu_rate_pt_direction_MB1_MB4_eta0to0p9", "Displaced L1Mu, hit in MB1, MB4, direction based",
              "h_single_displaced_L1Mu_rate_pt_direction_MB1_MB4_eta0to0p9_mediumVeto", "Displaced L1Mu, hit in MB1, MB4, direction based, medium veto",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu2st__DisplacedL1Mu2st_MB1_MB4_eta0to0p9_mediumVeto")

    ## rates vs eta
    makeEtaPlots("1.6<|#eta|<2.2",
                 "h_single_prompt_L1Mu_rate_eta_ME1_ME2_ME3_eta1p6to2p2", "Prompt L1Mu, hit in ME1, ME2, ME3",
                 "h_single_displaced_L1Mu_rate_eta_position_ME1_ME2_ME3_eta1p6to2p2", "Displaced L1Mu, hit in ME1, ME2, ME3 position based",
                 "h_single_displaced_L1Mu_rate_eta_position_ME1_ME2_ME3_eta1p6to2p2_mediumVeto", "Displaced L1Mu, hit in ME1, ME2, ME3 position based, medium veto",
                 "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu3st__DisplacedL1MuPositionBased_ME1_ME2_ME3_eta1p6to2p2_mediumVeto", doEta=True)

    makeEtaPlots("1.2<|#eta|<2.4",
                 "h_single_prompt_L1Mu_rate_eta_ME1_ME2_ME3_eta1p2to2p4", "Prompt L1Mu, hit in ME1, ME2, ME3",
                 "h_single_displaced_L1Mu_rate_eta_position_ME1_ME2_ME3_eta1p2to2p4", "Displaced L1Mu, hit in ME1, ME2, ME3 position based",
                 "h_single_displaced_L1Mu_rate_eta_position_ME1_ME2_ME3_eta1p2to2p4_mediumVeto", "Displaced L1Mu, hit in ME1, ME2, ME3 position based, medium veto",
                 "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu3st__DisplacedL1MuPositionBased_ME1_ME2_ME3_eta1p2to2p4_mediumVeto", doEta=True)

    makeEtaPlots("1.6<|#eta|<2.2",
                 "h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta1p6to2p2", "Prompt L1Mu, hit in GE11, ME11, GE21, ME21",
                 "h_single_displaced_L1Mu_rate_eta_direction_GE11_ME11_GE21_ME21_eta1p6to2p2", "Displaced L1Mu, hit in GE11, ME11, GE21, ME21 direction based",
                 "h_single_displaced_L1Mu_rate_eta_direction_GE11_ME11_GE21_ME21_eta1p6to2p2_mediumVeto", "Displaced L1Mu, hit in GE11, ME11, GE21, ME21 direction based, medium veto",
                 "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu3st__DisplacedL1MuDirectionBased_GE11_ME11_GE21_ME21_eta1p6to2p2_mediumVeto", doEta=True)

    makeEtaPlots("1.6<|#eta|<2.2",
                 "h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_ME3_eta1p6to2p2", "Prompt L1Mu, hit in GE11, ME11, GE21, ME21, ME3",
                 "h_single_displaced_L1Mu_rate_eta_hybrid_GE11_ME11_GE21_ME21_ME3_eta1p6to2p2", "Displaced L1Mu, hit in GE11, ME11, GE21, ME21, ME3 hybrid based",
                 "h_single_displaced_L1Mu_rate_eta_hybrid_GE11_ME11_GE21_ME21_ME3_eta1p6to2p2_mediumVeto", "Displaced L1Mu, hit in GE11, ME11, GE21, ME21, ME3 hybrid based, medium veto",
                 "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu3st__DisplacedL1MuHybridBased_GE11_ME11_GE21_ME21_ME3_eta1p6to2p2_mediumVeto", doEta=True)

    makeEtaPlots("1.6<|#eta|<2.2",
                 "h_single_prompt_L1Mu_rate_eta_ME1_ME2_ME3_eta1p6to2p2", "Prompt L1Mu, hit in ME1, ME2, ME3",
                 "h_single_displaced_L1Mu_rate_eta_hybrid_GE11_ME1_ME2_ME3_eta1p6to2p2", "Displaced L1Mu, hit in ME1, ME2, ME3 hybrid based",
                 "h_single_displaced_L1Mu_rate_eta_hybrid_GE11_ME1_ME2_ME3_eta1p6to2p2_mediumVeto", "Displaced L1Mu, hit in ME1, ME2, ME3 hybrid based, medium veto",
                 "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu3st__DisplacedL1MuHybridBased_ME1_ME2_ME3_eta1p6to2p2_mediumVeto")

    makeEtaPlots("1.2<|#eta|<2.2",
                 "h_single_prompt_L1Mu_rate_eta_ME1_ME2_ME3_eta1p2to2p2", "Prompt L1Mu, hit in ME1, ME2, ME3",
                 "h_single_displaced_L1Mu_rate_eta_hybrid_ME1_ME2_ME3_eta1p2to2p2", "Displaced L1Mu, hit in ME1, ME2, ME3 hybrid based",
                 "h_single_displaced_L1Mu_rate_eta_hybrid_ME1_ME2_ME3_eta1p2to2p2_mediumVeto", "Displaced L1Mu, hit in ME1, ME2, ME3 hybrid based, medium veto",
                 "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu3st__DisplacedL1MuHybridBased_ME1_ME2_ME3_eta1p2to2p2_mediumVeto")

    makeEtaPlots("0.0<|#eta|<0.9",
                 "h_single_prompt_L1Mu_rate_eta_MB1_MB4_eta0to0p9", "Prompt L1Mu, hit in MB1, MB4",
                 "h_single_displaced_L1Mu_rate_eta_direction_MB1_MB4_eta0to0p9", "Displaced L1Mu, hit in MB1, MB4, direction based",
                 "h_single_displaced_L1Mu_rate_eta_direction_MB1_MB4_eta0to0p9_mediumVeto", "Displaced L1Mu, hit in MB1, MB4, direction based, medium veto",
                 "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu2st__DisplacedL1Mu2st_MB1_MB4_eta0to0p9_mediumVeto")




    makePlots("1.6<|#eta|<2.2",
                 "h_single_displaced_L1Mu_rate_pt_position_ME1_ME2_ME3_eta1p6to2p2_mediumVeto", "L1Mu (unconstrained)",
                 "h_single_displaced_L1Mu_rate_pt_hybrid_GE11_ME11_GE21_ME21_ME3_eta1p6to2p2_mediumVeto", "L1Mu (hybrid)",
                 "h_single_prompt_L1Mu_rate_pt_ME1_ME2_ME3_eta1p6to2p2", "L1Mu (hybrid)",
                 "MuonTDR2017_Prompt_L1Mu_trigger_rate_pt__L1Mu__PositionBased_HybridBased_GE11_ME11_GE21_ME21_ME3_eta1p6to2p2_mediumVeto")

    makeEtaPlots("1.6<|#eta|<2.2",
                 "h_single_displaced_L1Mu_rate_eta_position_ME1_ME2_ME3_eta1p6to2p2_mediumVeto", "L1Mu (unconstrained)",
                 "h_single_displaced_L1Mu_rate_eta_hybrid_GE11_ME11_GE21_ME21_ME3_eta1p6to2p2_mediumVeto", "L1Mu (hybrid)",
                 "h_single_prompt_L1Mu_rate_pt_ME1_ME2_ME3_eta1p6to2p2", "L1Mu (hybrid)",
                 "MuonTDR2017_Prompt_L1Mu_trigger_rate_eta__L1Mu__PositionBased_HybridBased_GE11_ME11_GE21_ME21_ME3_eta1p6to2p2_mediumVeto")


    makePlots("1.6<|#eta|<2.2",
                 "h_single_displaced_L1Mu_rate_pt_position_ME1_ME2_ME3_eta1p6to2p2_looseVeto", "L1Mu (unconstrained)",
                 "h_single_displaced_L1Mu_rate_pt_hybrid_GE11_ME11_GE21_ME21_ME3_eta1p6to2p2_looseVeto", "L1Mu (hybrid)",
                 "h_single_prompt_L1Mu_rate_pt_ME1_ME2_ME3_eta1p6to2p2", "L1Mu (hybrid)",
                 "MuonTDR2017_Prompt_L1Mu_trigger_rate_pt__L1Mu__PositionBased_HybridBased_GE11_ME11_GE21_ME21_ME3_eta1p6to2p2_looseVeto")

    makeEtaPlots("1.6<|#eta|<2.2",
                 "h_single_displaced_L1Mu_rate_eta_position_ME1_ME2_ME3_eta1p6to2p2_looseVeto", "L1Mu (unconstrained)",
                 "h_single_displaced_L1Mu_rate_eta_hybrid_GE11_ME11_GE21_ME21_ME3_eta1p6to2p2_looseVeto", "L1Mu (hybrid)",
                 "h_single_prompt_L1Mu_rate_pt_ME1_ME2_ME3_eta1p6to2p2", "L1Mu (hybrid)",
                 "MuonTDR2017_Prompt_L1Mu_trigger_rate_eta__L1Mu__PositionBased_HybridBased_GE11_ME11_GE21_ME21_ME3_eta1p6to2p2_looseVeto")

  displacedL1MuHybridTriggerRatePlots()

