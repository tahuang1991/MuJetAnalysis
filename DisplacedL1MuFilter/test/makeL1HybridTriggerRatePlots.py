# Run quiet mode
import sys
sys.argv.append( '-b' )
import ROOT 
ROOT.gROOT.SetBatch(1)
from Helpers import *
from hybridAlgorithmPtAssignment import *
from TTTrackIsolation import *

ROOT.gErrorIgnoreLevel=1001
from ROOT import * 
import random
#______________________________________________________________________________ 
if __name__ == "__main__":  

  label = "Neutrino_Pt2to20_gun_TTI2023Upg14D_PU140bx25_ILT_SLHC14_20160901_v2"; pu = 'PU140'; eff = False
  label = "Neutrino_Pt2to20_gun_TTI2023Upg14D_PU140bx25_ILT_SLHC14_20160905"; pu = 'PU140'; eff = False

  ## extension for figures - add more?
  ext = ".png"

  ## Style
  gStyle.SetStatStyle(0)

  print "Making the plots"

  set_style()

  doTest = True

  ch = TChain("DisplacedL1MuFilter_PhaseIIGE21/L1MuTree")
  #location = "/uscms_data/d3/dildick/work/GEMTriggerRateStudyAugust2016/CMSSW_6_2_0_SLHC28/src/MuJetAnalysis/DisplacedL1MuFilter/test/"
  #treeHits = addfiles(ch, dirname=location, ext="out_ana_TTI_300k_TDRStudies_backup.root")
  location = '/eos/uscms/store/user/lpcgem/Neutrino_Pt2to20_gun/NeutrinoGun_14TeV_PU140_L1MuANA_v1/160905_155945/0000/'
  treeHits = addfiles(ch, dirname=location, ext=".root")

  targetDir = label + "/"
  
  verbose = False
  
  ## copy index file
  import shutil
  shutil.copy2('index.php', targetDir + 'index.php')

  def displacedL1MuHybridTriggerRate():

    mapTH1F = ROOT.std.map("string,TH1F")()
    mapTH2F = ROOT.std.map("string,TH2F")()

    def addPlotToMapTH1F(name,nBin,minBin,maxBin):
      mapTH1F[name] = TH1F(name,"",nBin,minBin,maxBin)

    def addPlotToMapTH1F_v2(name,bins):
      mapTH1F[name] = TH1F(name,"",len(bins)-1, bins)

    addPlotToMapTH1F_v2("h_single_prompt_L1Mu_rate", myptbin)
    addPlotToMapTH1F_v2("h_single_prompt_L1Mu_rate_2_stubs", myptbin)
    addPlotToMapTH1F_v2("h_single_prompt_L1Mu_rate_3_stubs", myptbin)

    addPlotToMapTH1F_v2("h_single_prompt_L1Mu_rate_2_stubs_ME11", myptbin)
    addPlotToMapTH1F_v2("h_single_prompt_L1Mu_rate_3_stubs_ME11", myptbin)

    addPlotToMapTH1F_v2("h_single_prompt_L1Mu_rate_2_stubs_ME11_GE11", myptbin)
    addPlotToMapTH1F_v2("h_single_prompt_L1Mu_rate_3_stubs_ME11_GE11", myptbin)

    addPlotToMapTH1F_v2("h_single_prompt_L1Mu_rate_2_stubs_ME11_GE11_GE21", myptbin)
    addPlotToMapTH1F_v2("h_single_prompt_L1Mu_rate_3_stubs_ME11_GE11_GE21", myptbin)

    addPlotToMapTH1F_v2("h_single_prompt_L1Mu_rate_2_stubs_GE11_GE21", myptbin)
    addPlotToMapTH1F_v2("h_single_prompt_L1Mu_rate_3_stubs_GE11_GE21", myptbin)

    ## failing stations
    addPlotToMapTH1F_v2("h_single_prompt_L1Mu_rate_2_stubs_ME11_Fail10p", myptbin)
    addPlotToMapTH1F_v2("h_single_prompt_L1Mu_rate_3_stubs_ME11_Fail10p", myptbin)

    addPlotToMapTH1F_v2("h_single_prompt_L1Mu_rate_2_stubs_ME11_Fail10p_GE11", myptbin)
    addPlotToMapTH1F_v2("h_single_prompt_L1Mu_rate_3_stubs_ME11_Fail10p_GE11", myptbin)

    addPlotToMapTH1F_v2("h_single_prompt_L1Mu_rate_2_stubs_ME11_Fail10p_GE11_GE21", myptbin)
    addPlotToMapTH1F_v2("h_single_prompt_L1Mu_rate_3_stubs_ME11_Fail10p_GE11_GE21", myptbin)

    ## displaced muons
    addPlotToMapTH1F_v2("h_single_displaced_L1Mu_rate_ME1_ME2_ME3",myptbin)

    maxEntries = ch.GetEntries()
    if doTest:
      maxEntries = 100000

    for k in range(0,maxEntries):
      if k%1000==0: print "Processing event", k

      ch.GetEntry(k)      
      treeHits = ch
      
      ## get the max value of the momentum
      pts = list(treeHits.L1Mu_pt)
 
      ## ignore events without L1Mu
      if len(pts)==0: continue

      fillPtHistogram( mapTH1F["h_single_prompt_L1Mu_rate"], treeHits, True, 1.6, 2.2, 0, 6)


      fillPtHistogram( mapTH1F["h_single_prompt_L1Mu_rate_2_stubs"], treeHits,True, 1.6, 2.2, 2, 6)
      
      fillPtHistogram( mapTH1F["h_single_prompt_L1Mu_rate_3_stubs"], treeHits,True, 1.6, 2.2, 3, 6)

      
      fillPtHistogram( mapTH1F["h_single_prompt_L1Mu_rate_2_stubs_ME11"], treeHits,True, 1.6, 2.2, 2, 6, hasME11Cut=True)
      
      fillPtHistogram( mapTH1F["h_single_prompt_L1Mu_rate_3_stubs_ME11"], treeHits,True, 1.6, 2.2, 3, 6, hasME11Cut=True)
      

      fillPtHistogram( mapTH1F["h_single_prompt_L1Mu_rate_2_stubs_ME11_Fail10p"], treeHits,True, 1.6, 2.2, 2, 6, hasME11Cut=True, ME11FailRate=0.1)
      
      fillPtHistogram( mapTH1F["h_single_prompt_L1Mu_rate_3_stubs_ME11_Fail10p"], treeHits,True, 1.6, 2.2, 3, 6, hasME11Cut=True, ME11FailRate=0.1)


      fillPtHistogram( mapTH1F["h_single_prompt_L1Mu_rate_2_stubs_ME11_GE11"], treeHits,True, 1.6, 2.2, 2, 6, hasME11Cut=True, hasGE11Cut=True)
      
      fillPtHistogram( mapTH1F["h_single_prompt_L1Mu_rate_3_stubs_ME11_GE11"], treeHits,True, 1.6, 2.2, 3, 6, hasME11Cut=True, hasGE11Cut=True)

      
      fillPtHistogram( mapTH1F["h_single_prompt_L1Mu_rate_2_stubs_ME11_Fail10p_GE11"], treeHits,True, 1.6, 2.2, 2, 6, hasME11Cut=True, hasGE11Cut=True, ME11FailRate=0.1)
      
      fillPtHistogram( mapTH1F["h_single_prompt_L1Mu_rate_3_stubs_ME11_Fail10p_GE11"], treeHits,True, 1.6, 2.2, 3, 6, hasME11Cut=True, hasGE11Cut=True, ME11FailRate=0.1)


      fillPtHistogram( mapTH1F["h_single_prompt_L1Mu_rate_2_stubs_ME11_GE11_GE21"], treeHits,True, 1.6, 2.2, 2, 6, hasME11Cut=True, hasGE11Cut=True, hasGE21Cut=True)
      
      fillPtHistogram( mapTH1F["h_single_prompt_L1Mu_rate_3_stubs_ME11_GE11_GE21"], treeHits,True, 1.6, 2.2, 3, 6, hasME11Cut=True, hasGE11Cut=True, hasGE21Cut=True)


      fillPtHistogram( mapTH1F["h_single_prompt_L1Mu_rate_2_stubs_ME11_Fail10p_GE11_GE21"], treeHits,True, 1.6, 2.2, 2, 6, hasME11Cut=True, hasGE11Cut=True, hasGE21Cut=True, ME11FailRate=0.1)
      
      fillPtHistogram( mapTH1F["h_single_prompt_L1Mu_rate_3_stubs_ME11_Fail10p_GE11_GE21"], treeHits,True, 1.6, 2.2, 3, 6, hasME11Cut=True, hasGE11Cut=True, hasGE21Cut=True, ME11FailRate=0.1)
      

    def makePlots(h1, h1Legend,
                  h2, h2Legend,
                  h3, h3Legend,
                  title):
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

      ptbin = [
        2.0,   2.5,   3.0,   3.5,   4.0,   4.5,   5.0,   6.0,   7.0,   8.0,  
        10.0,  12.0,  14.0,  16.0,  18.0,  20.0,  25.0,  30.0,  35.0,  40.0,  
        45.0,  50.0,  60.0,  70.0,  80.0,  90.0, 100.0, 120.0, 140.0]
      myptbin = np.asarray(ptbin)
      nmyptbin = len(myptbin) - 1

      b1 = TH1F("b1","b1",nmyptbin,myptbin)
      b1.GetYaxis().SetRangeUser(.01,10000)
      b1.GetYaxis().SetTitleOffset(1.2)
      b1.GetYaxis().SetNdivisions(520)
      b1.GetYaxis().SetTitle("Trigger Rate [kHz]")
      b1.GetXaxis().SetTitle("L1 muon candidate p_{T}^{cut} [GeV]")
      b1.GetXaxis().SetTitleSize(0.05)
      b1.GetYaxis().SetTitleSize(0.05)
      b1.GetXaxis().SetLabelSize(0.05)
      b1.GetYaxis().SetLabelSize(0.05)
      gStyle.SetTitleFontSize(0.065)
      b1.SetTitle("                                                                                        14TeV, " + pu)
      b1.SetStats(0)
      b1.Draw()

      h1 = getRatePtHistogram(treeHits, h1)
      h1.SetFillColor(kRed)
      h1.Draw("e3same")
      
      h2 = getRatePtHistogram(treeHits, h2)
      h2.SetFillColor(kViolet)
      h2.Draw("e3same")

      h3 = getRatePtHistogram(treeHits, h3)
      h3.SetFillColor(kBlue)
      h3.Draw("e3same")

      latex = applyTdrStyle()      

      leg = TLegend(0.15,0.2,0.5,0.35,"1.6<|#eta|<2.2","brNDC")
      leg.SetFillColor(kWhite)
      leg.SetBorderSize(0)
      leg.SetFillStyle(0)
      leg.SetTextSize(0.04)
      leg.AddEntry(h1, h1Legend, "f")
      leg.AddEntry(h2, h2Legend, "f")
      leg.AddEntry(h3, h3Legend, "f")
      leg.Draw("same")

      c.SaveAs(targetDir + title + ext)

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

    ## trigger rate plots vs pt
    makePlots(mapTH1F["h_single_prompt_L1Mu_rate"], "Prompt L1Mu",
              mapTH1F["h_single_prompt_L1Mu_rate_2_stubs"], "Prompt L1Mu, 2 CSC stubs",
              mapTH1F["h_single_prompt_L1Mu_rate_3_stubs"], "Prompt L1Mu, 3 CSC stubs",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu2st__L1Mu3st")

    makePlots(mapTH1F["h_single_prompt_L1Mu_rate"], "Prompt L1Mu",
              mapTH1F["h_single_prompt_L1Mu_rate_3_stubs"], "Prompt L1Mu, 3 CSC stubs",
              mapTH1F["h_single_prompt_L1Mu_rate_3_stubs_ME11"], "Prompt L1Mu, 3 CSC stubs, ME11",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu3st__L1Mu3stME11")

    makePlots(mapTH1F["h_single_prompt_L1Mu_rate"], "Prompt L1Mu",
              mapTH1F["h_single_prompt_L1Mu_rate_2_stubs_ME11"], "Prompt L1Mu, 2 CSC stubs, ME11",
              mapTH1F["h_single_prompt_L1Mu_rate_2_stubs_ME11_GE11"], "Prompt L1Mu, 2 CSC stubs, ME11, GE11",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu2stME11__L1Mu2stME11GE11")

    makePlots(mapTH1F["h_single_prompt_L1Mu_rate"], "Prompt L1Mu",
              mapTH1F["h_single_prompt_L1Mu_rate_3_stubs_ME11"], "Prompt L1Mu, 3 CSC stubs, ME11",
              mapTH1F["h_single_prompt_L1Mu_rate_3_stubs_ME11_GE11"], "Prompt L1Mu, 3 CSC stubs, ME11, GE11",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu3stME11__L1Mu3stME11GE11")

    makePlots(mapTH1F["h_single_prompt_L1Mu_rate_2_stubs_ME11"], "Prompt L1Mu, 2 CSC stubs, ME11",
              mapTH1F["h_single_prompt_L1Mu_rate_2_stubs_ME11_GE11"], "Prompt L1Mu, 2 CSC stubs, ME11, GE11",
              mapTH1F["h_single_prompt_L1Mu_rate_2_stubs_ME11_GE11_GE21"], "Prompt L1Mu, 2 CSC stubs, ME11, GE11, GE21",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu2stME11__L1Mu2stME11GE11__L1Mu2stME11GE11GE21")

    makePlots(mapTH1F["h_single_prompt_L1Mu_rate_3_stubs_ME11"], "Prompt L1Mu, 3 CSC stubs, ME11",
              mapTH1F["h_single_prompt_L1Mu_rate_3_stubs_ME11_GE11"], "Prompt L1Mu, 3 CSC stubs, ME11, GE11",
              mapTH1F["h_single_prompt_L1Mu_rate_3_stubs_ME11_GE11_GE21"], "Prompt L1Mu, 3 CSC stubs, ME11, GE11, GE21",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu3stME11__L1Mu3stME11GE11__L1Mu3stME11GE11GE21")


    ## prompt trigger with failing chambers

    makePlots(mapTH1F["h_single_prompt_L1Mu_rate"], "Prompt L1Mu",
              mapTH1F["h_single_prompt_L1Mu_rate_2_stubs_ME11"], "Prompt L1Mu, 2 CSC stubs, ME11",
              mapTH1F["h_single_prompt_L1Mu_rate_2_stubs_ME11_Fail10p"], "Prompt L1Mu, 2 CSC stubs, ME11 Fail",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu2stME11__L1Mu2stME11Fail")


    makePlots(mapTH1F["h_single_prompt_L1Mu_rate_2_stubs_ME11"], "Prompt L1Mu, 2 CSC stubs, ME11",
              mapTH1F["h_single_prompt_L1Mu_rate_2_stubs_ME11_Fail10p_GE11"], "Prompt L1Mu, 2 CSC stubs, ME11, GE11",
              mapTH1F["h_single_prompt_L1Mu_rate_2_stubs_ME11_Fail10p_GE11_GE21"], "Prompt L1Mu, 2 CSC stubs, ME11, GE11, GE21",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu2stME11__L1Mu2stME11FailGE11__L1Mu2stME11FailGE11GE21")

    makePlots(mapTH1F["h_single_prompt_L1Mu_rate_3_stubs_ME11"], "Prompt L1Mu, 3 CSC stubs, ME11",
              mapTH1F["h_single_prompt_L1Mu_rate_3_stubs_ME11_Fail10p_GE11"], "Prompt L1Mu, 3 CSC stubs, ME11, GE11",
              mapTH1F["h_single_prompt_L1Mu_rate_3_stubs_ME11_Fail10p_GE11_GE21"], "Prompt L1Mu, 3 CSC stubs, ME11, GE11, GE21",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu3stME11__L1Mu3stME11FailGE11__L1Mu3stME11FailGE11GE21")


    ## displaced L1Mu trigger plots
    

  displacedL1MuHybridTriggerRate()


  exit(1)

  def makeRateVsPtHistogram():

    h_single_L1Mu_rate = TH1F("h_single_L1Mu_rate"," ",len(myptbin)-1, myptbin)
    h_single_displaced_rate = TH1F("h_single_displaced_rate"," ",len(myptbin)-1, myptbin)
    h_single_displaced_rate_dR0p4_L1TkPt2 = TH1F("h_single_displaced_rate_dR0p4_L1TkPt2"," ",len(myptbin)-1, myptbin)
    h_single_displaced_rate_dR0p4_L1TkPt2p5 = TH1F("h_single_displaced_rate_dR0p4_L1TkPt2p5"," ",len(myptbin)-1, myptbin)
    h_single_displaced_rate_dR0p4_L1TkPt3 = TH1F("h_single_displaced_rate_dR0p4_L1TkPt3"," ",len(myptbin)-1, myptbin)
    h_single_displaced_rate_dR0p4_L1TkPt4 = TH1F("h_single_displaced_rate_dR0p4_L1TkPt4"," ",len(myptbin)-1, myptbin)

    h_single_displaced_rate_dR0p3_L1TkPt2 = TH1F("h_single_displaced_rate_dR0p3_L1TkPt2"," ",len(myptbin)-1, myptbin)
    h_single_displaced_rate_dR0p3_L1TkPt2p5 = TH1F("h_single_displaced_rate_dR0p3_L1TkPt2p5"," ",len(myptbin)-1, myptbin)
    h_single_displaced_rate_dR0p3_L1TkPt3 = TH1F("h_single_displaced_rate_dR0p3_L1TkPt3"," ",len(myptbin)-1, myptbin)
    h_single_displaced_rate_dR0p3_L1TkPt4 = TH1F("h_single_displaced_rate_dR0p3_L1TkPt4"," ",len(myptbin)-1, myptbin)

    h_single_displaced_rate_dR0p2_L1TkPt2 = TH1F("h_single_displaced_rate_dR0p2_L1TkPt2"," ",len(myptbin)-1, myptbin)
    h_single_displaced_rate_dR0p2_L1TkPt2p5 = TH1F("h_single_displaced_rate_dR0p2_L1TkPt2p5"," ",len(myptbin)-1, myptbin)
    h_single_displaced_rate_dR0p2_L1TkPt3 = TH1F("h_single_displaced_rate_dR0p2_L1TkPt3"," ",len(myptbin)-1, myptbin)
    h_single_displaced_rate_dR0p2_L1TkPt4 = TH1F("h_single_displaced_rate_dR0p2_L1TkPt4"," ",len(myptbin)-1, myptbin)

    h_single_displaced_rate_dR0p12_L1TkPt2 = TH1F("h_single_displaced_rate_dR0p12_L1TkPt2"," ",len(myptbin)-1, myptbin)
    h_single_displaced_rate_dR0p12_L1TkPt2p5 = TH1F("h_single_displaced_rate_dR0p12_L1TkPt2p5"," ",len(myptbin)-1, myptbin)
    h_single_displaced_rate_dR0p12_L1TkPt3 = TH1F("h_single_displaced_rate_dR0p12_L1TkPt3"," ",len(myptbin)-1, myptbin)
    h_single_displaced_rate_dR0p12_L1TkPt4 = TH1F("h_single_displaced_rate_dR0p12_L1TkPt4"," ",len(myptbin)-1, myptbin)
    
    for k in range(0,ch.GetEntries()):
      if k%1000==0: print "Processing event", k
#    for k in range(0,100):
      ch.GetEntry(k)
      
      treeHits = ch
      ## get the max value of the momentum
      pts = list(treeHits.L1Mu_pt)

      if len(pts)>=1:
              
        def getMaxPts():
          maxPt1, maxPt2, maxPt3, maxPt4, maxPt5 = 0., 0., 0., 0., 0., 

          maxPt_trig_dR0p4_L1TkPt4 = 0.
          maxPt_trig_dR0p4_L1TkPt3 = 0.
          maxPt_trig_dR0p4_L1TkPt2p5 = 0.
          maxPt_trig_dR0p4_L1TkPt2 = 0.
          
          maxPt_trig_dR0p3_L1TkPt4 = 0.
          maxPt_trig_dR0p3_L1TkPt3 = 0.
          maxPt_trig_dR0p3_L1TkPt2p5 = 0.
          maxPt_trig_dR0p3_L1TkPt2 = 0.

          maxPt_trig_dR0p2_L1TkPt4 = 0.
          maxPt_trig_dR0p2_L1TkPt3 = 0.
          maxPt_trig_dR0p2_L1TkPt2p5 = 0.
          maxPt_trig_dR0p2_L1TkPt2 = 0.
          
          maxPt_trig_dR0p12_L1TkPt4 = 0.
          maxPt_trig_dR0p12_L1TkPt3 = 0.
          maxPt_trig_dR0p12_L1TkPt2p5 = 0.
          maxPt_trig_dR0p12_L1TkPt2 = 0.

          for i in range(0,len(pts)):
            L1Mu_pt = treeHits.L1Mu_pt[i]
            L1Mu_eta = treeHits.L1Mu_eta[i]
            L1Mu_phi = treeHits.L1Mu_phi[i]
            L1Mu_bx = treeHits.L1Mu_bx[i]
            L1Mu_quality = treeHits.L1Mu_quality[i]

            L1Mu_L1Tk_dR_min = treeHits.L1Mu_L1Tk_dR_prop[i]
            L1Mu_L1Tk_pt = treeHits.L1Mu_L1Tk_pt_prop[i]

            if L1Mu_bx==0:
              print k,i, "pt", L1Mu_pt, "eta", L1Mu_eta, "phi", L1Mu_phi, "bx", L1Mu_bx, "quality", L1Mu_quality


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
            matched = L1Mu_L1Tk_dR_min <= 0.12 and L1Mu_quality >= 4
            matched = matched and L1Mu_L1Tk_pt>=MatchingL1TkMinPt
            
            ## unmatched 
            if L1Mu_L1Tk_dR_min <= 0.4 and L1Mu_L1Tk_pt>=4:   unMatched_dR0p4_L1TkPt4 = True
            if L1Mu_L1Tk_dR_min <= 0.4 and L1Mu_L1Tk_pt>=3:   unMatched_dR0p4_L1TkPt3 = True
            if L1Mu_L1Tk_dR_min <= 0.4 and L1Mu_L1Tk_pt>=2.5: unMatched_dR0p4_L1TkPt2p5 = True
            if L1Mu_L1Tk_dR_min <= 0.4 and L1Mu_L1Tk_pt>=2:   unMatched_dR0p4_L1TkPt2 = True

            if L1Mu_L1Tk_dR_min <= 0.3 and L1Mu_L1Tk_pt>=4:   unMatched_dR0p3_L1TkPt4 = True
            if L1Mu_L1Tk_dR_min <= 0.3 and L1Mu_L1Tk_pt>=3:   unMatched_dR0p3_L1TkPt3 = True
            if L1Mu_L1Tk_dR_min <= 0.3 and L1Mu_L1Tk_pt>=2.5: unMatched_dR0p3_L1TkPt2p5 = True
            if L1Mu_L1Tk_dR_min <= 0.3 and L1Mu_L1Tk_pt>=2:   unMatched_dR0p3_L1TkPt2 = True

            if L1Mu_L1Tk_dR_min <= 0.2 and L1Mu_L1Tk_pt>=4:   unMatched_dR0p2_L1TkPt4 = True
            if L1Mu_L1Tk_dR_min <= 0.2 and L1Mu_L1Tk_pt>=3:   unMatched_dR0p2_L1TkPt3 = True
            if L1Mu_L1Tk_dR_min <= 0.2 and L1Mu_L1Tk_pt>=2.5: unMatched_dR0p2_L1TkPt2p5 = True
            if L1Mu_L1Tk_dR_min <= 0.2 and L1Mu_L1Tk_pt>=2:   unMatched_dR0p2_L1TkPt2 = True

            if L1Mu_L1Tk_dR_min <= 0.12 and L1Mu_L1Tk_pt>=4:   unMatched_dR0p12_L1TkPt4 = True
            if L1Mu_L1Tk_dR_min <= 0.12 and L1Mu_L1Tk_pt>=3:   unMatched_dR0p12_L1TkPt3 = True
            if L1Mu_L1Tk_dR_min <= 0.12 and L1Mu_L1Tk_pt>=2.5: unMatched_dR0p12_L1TkPt2p5 = True
            if L1Mu_L1Tk_dR_min <= 0.12 and L1Mu_L1Tk_pt>=2:   unMatched_dR0p12_L1TkPt2 = True

            common = (abs(L1Mu_bx) == 0) and (L1Mu_quality >= 4) and L1Mu_pt>=0
            trigL1Mu = common
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


            if trigL1Mu                         and L1Mu_pt > maxPt1:                                     maxPt1 = L1Mu_pt

            if trig_dR0p4_L1TkPt4               and L1Mu_pt > maxPt_trig_dR0p4_L1TkPt4: maxPt_trig_dR0p4_L1TkPt4 = L1Mu_pt
            if trig_dR0p3_L1TkPt4               and L1Mu_pt > maxPt_trig_dR0p3_L1TkPt4: maxPt_trig_dR0p3_L1TkPt4 = L1Mu_pt
            if trig_dR0p2_L1TkPt4               and L1Mu_pt > maxPt_trig_dR0p2_L1TkPt4: maxPt_trig_dR0p2_L1TkPt4 = L1Mu_pt
            if trig_dR0p12_L1TkPt4              and L1Mu_pt > maxPt_trig_dR0p12_L1TkPt4: maxPt_trig_dR0p12_L1TkPt4 = L1Mu_pt

            if trig_dR0p4_L1TkPt3               and L1Mu_pt > maxPt_trig_dR0p4_L1TkPt3: maxPt_trig_dR0p4_L1TkPt3 = L1Mu_pt
            if trig_dR0p3_L1TkPt3               and L1Mu_pt > maxPt_trig_dR0p3_L1TkPt3: maxPt_trig_dR0p3_L1TkPt3 = L1Mu_pt
            if trig_dR0p2_L1TkPt3               and L1Mu_pt > maxPt_trig_dR0p2_L1TkPt3: maxPt_trig_dR0p2_L1TkPt3 = L1Mu_pt
            if trig_dR0p12_L1TkPt3              and L1Mu_pt > maxPt_trig_dR0p12_L1TkPt3: maxPt_trig_dR0p12_L1TkPt3 = L1Mu_pt

            if trig_dR0p4_L1TkPt2p5               and L1Mu_pt > maxPt_trig_dR0p4_L1TkPt2p5: maxPt_trig_dR0p4_L1TkPt2p5 = L1Mu_pt
            if trig_dR0p3_L1TkPt2p5               and L1Mu_pt > maxPt_trig_dR0p3_L1TkPt2p5: maxPt_trig_dR0p3_L1TkPt2p5 = L1Mu_pt
            if trig_dR0p2_L1TkPt2p5               and L1Mu_pt > maxPt_trig_dR0p2_L1TkPt2p5: maxPt_trig_dR0p2_L1TkPt2p5 = L1Mu_pt
            if trig_dR0p12_L1TkPt2p5              and L1Mu_pt > maxPt_trig_dR0p12_L1TkPt2p5: maxPt_trig_dR0p12_L1TkPt2p5 = L1Mu_pt

            if trig_dR0p4_L1TkPt2               and L1Mu_pt > maxPt_trig_dR0p4_L1TkPt2: maxPt_trig_dR0p4_L1TkPt2 = L1Mu_pt
            if trig_dR0p3_L1TkPt2               and L1Mu_pt > maxPt_trig_dR0p3_L1TkPt2: maxPt_trig_dR0p3_L1TkPt2 = L1Mu_pt
            if trig_dR0p2_L1TkPt2               and L1Mu_pt > maxPt_trig_dR0p2_L1TkPt2: maxPt_trig_dR0p2_L1TkPt2 = L1Mu_pt
            if trig_dR0p12_L1TkPt2              and L1Mu_pt > maxPt_trig_dR0p12_L1TkPt2: maxPt_trig_dR0p12_L1TkPt2 = L1Mu_pt

          return maxPt1, maxPt_trig_dR0p4_L1TkPt4, maxPt_trig_dR0p4_L1TkPt3, maxPt_trig_dR0p4_L1TkPt2p5, maxPt_trig_dR0p4_L1TkPt2, maxPt_trig_dR0p3_L1TkPt4, maxPt_trig_dR0p3_L1TkPt3, maxPt_trig_dR0p3_L1TkPt2p5, maxPt_trig_dR0p3_L1TkPt2, maxPt_trig_dR0p2_L1TkPt4, maxPt_trig_dR0p2_L1TkPt3, maxPt_trig_dR0p2_L1TkPt2p5, maxPt_trig_dR0p2_L1TkPt2, maxPt_trig_dR0p12_L1TkPt4, maxPt_trig_dR0p12_L1TkPt3, maxPt_trig_dR0p12_L1TkPt2p5, maxPt_trig_dR0p12_L1TkPt2

        
        maxPt1, maxPt_trig_dR0p4_L1TkPt4, maxPt_trig_dR0p4_L1TkPt3, maxPt_trig_dR0p4_L1TkPt2p5, maxPt_trig_dR0p4_L1TkPt2, maxPt_trig_dR0p3_L1TkPt4, maxPt_trig_dR0p3_L1TkPt3, maxPt_trig_dR0p3_L1TkPt2p5, maxPt_trig_dR0p3_L1TkPt2, maxPt_trig_dR0p2_L1TkPt4, maxPt_trig_dR0p2_L1TkPt3, maxPt_trig_dR0p2_L1TkPt2p5, maxPt_trig_dR0p2_L1TkPt2, maxPt_trig_dR0p12_L1TkPt4, maxPt_trig_dR0p12_L1TkPt3, maxPt_trig_dR0p12_L1TkPt2p5, maxPt_trig_dR0p12_L1TkPt2 = getMaxPts()
        
        if (maxPt1>0): h_single_L1Mu_rate.Fill(maxPt1)
        if (maxPt_trig_dR0p4_L1TkPt4>0): h_single_displaced_rate_dR0p4_L1TkPt4.Fill(maxPt_trig_dR0p4_L1TkPt4)
        if (maxPt_trig_dR0p4_L1TkPt3>0): h_single_displaced_rate_dR0p4_L1TkPt3.Fill(maxPt_trig_dR0p4_L1TkPt3)
        if (maxPt_trig_dR0p4_L1TkPt2p5>0): h_single_displaced_rate_dR0p4_L1TkPt2p5.Fill(maxPt_trig_dR0p4_L1TkPt2p5)
        if (maxPt_trig_dR0p4_L1TkPt2>0): h_single_displaced_rate_dR0p4_L1TkPt2.Fill(maxPt_trig_dR0p4_L1TkPt2)

        if (maxPt_trig_dR0p3_L1TkPt4>0): h_single_displaced_rate_dR0p3_L1TkPt4.Fill(maxPt_trig_dR0p3_L1TkPt4)
        if (maxPt_trig_dR0p3_L1TkPt3>0): h_single_displaced_rate_dR0p3_L1TkPt3.Fill(maxPt_trig_dR0p3_L1TkPt3)
        if (maxPt_trig_dR0p3_L1TkPt2p5>0): h_single_displaced_rate_dR0p3_L1TkPt2p5.Fill(maxPt_trig_dR0p3_L1TkPt2p5)
        if (maxPt_trig_dR0p3_L1TkPt2>0): h_single_displaced_rate_dR0p3_L1TkPt2.Fill(maxPt_trig_dR0p3_L1TkPt2)

        if (maxPt_trig_dR0p2_L1TkPt4>0): h_single_displaced_rate_dR0p2_L1TkPt4.Fill(maxPt_trig_dR0p2_L1TkPt4)
        if (maxPt_trig_dR0p2_L1TkPt3>0): h_single_displaced_rate_dR0p2_L1TkPt3.Fill(maxPt_trig_dR0p2_L1TkPt3)
        if (maxPt_trig_dR0p2_L1TkPt2p5>0): h_single_displaced_rate_dR0p2_L1TkPt2p5.Fill(maxPt_trig_dR0p2_L1TkPt2p5)
        if (maxPt_trig_dR0p2_L1TkPt2>0): h_single_displaced_rate_dR0p2_L1TkPt2.Fill(maxPt_trig_dR0p2_L1TkPt2)

        if (maxPt_trig_dR0p12_L1TkPt4>0): h_single_displaced_rate_dR0p12_L1TkPt4.Fill(maxPt_trig_dR0p12_L1TkPt4)
        if (maxPt_trig_dR0p12_L1TkPt3>0): h_single_displaced_rate_dR0p12_L1TkPt3.Fill(maxPt_trig_dR0p12_L1TkPt3)
        if (maxPt_trig_dR0p12_L1TkPt2p5>0): h_single_displaced_rate_dR0p12_L1TkPt2p5.Fill(maxPt_trig_dR0p12_L1TkPt2p5)
        if (maxPt_trig_dR0p12_L1TkPt2>0): h_single_displaced_rate_dR0p12_L1TkPt2.Fill(maxPt_trig_dR0p12_L1TkPt2)

    def makePlots(h1, h2, h3, h4, h5, isolation_cone, title):
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

      b1 = TH1F("b1","b1",29,myptbin)
      b1.GetYaxis().SetRangeUser(.1,10000)
      b1.GetYaxis().SetTitleOffset(1.2)
      b1.GetYaxis().SetNdivisions(520)
      b1.GetYaxis().SetTitle("L1Mu Trigger Rate [kHz]")
      b1.GetXaxis().SetTitle("L1Mu p_{T} cut [GeV]")
      b1.GetXaxis().SetTitleFont(62)
      b1.GetXaxis().SetTitleOffset(1.2)
      b1.GetXaxis().SetTitleSize(0.05)
      b1.GetYaxis().SetTitleSize(0.05)
      b1.SetTitle("                                                                  14TeV, " + pu)
      b1.SetStats(0)
      b1.Draw()

      h1 = getRatePtHistogram(treeHits, h1)
      h1.SetFillColor(kRed)
      h1.Draw("e3same")
      
      #if isolation_cone != 0.12:    
      h2 = getRatePtHistogram(treeHits, h2)
      h2.SetFillColor(kMagenta)
      h2.Draw("e3same")
      
      h3 = getRatePtHistogram(treeHits, h3)
      h3.SetFillColor(kBlue)
      h3.Draw("e3same")
      
      h4 = getRatePtHistogram(treeHits, h4)
      h4.SetFillColor(kGreen+1)
      h4.Draw("e3same")
      
      h5 = getRatePtHistogram(treeHits, h5)
      h5.SetFillColor(kOrange+1)
      h5.Draw("e3same")

      latex = applyTdrStyle()      

      if isolation_cone == 0.12:
        leg = TLegend(0.2,0.75,0.5,0.85,"","brNDC")
        leg.SetFillColor(kWhite)
        leg.SetBorderSize(0)
        leg.SetFillStyle(0)
        leg.SetTextSize(0.03)
        leg.AddEntry(h1,"Prompt L1Mu", "f")
        leg.AddEntry(None,"Displaced L1Mu", "")
        leg.AddEntry(h5,"Veto Matching L1Tk #DeltaR#leq0.12 with p_{T}#geq%.0f"%(MatchingL1TkMinPt), "f")
        leg.Draw("same")
      else:
        leg = TLegend(0.2,0.6,0.9,0.85,"","brNDC")
        leg.SetFillColor(kWhite)
        leg.SetBorderSize(0)
        leg.SetFillStyle(0)
        leg.SetTextSize(0.03)
        leg.AddEntry(h1,"Prompt L1Mu", "f")
        leg.AddEntry(None,"Displaced L1Mu", "")
        leg.AddEntry(None,"Veto Matching L1Tk #DeltaR#leq0.12 with p_{T}#geq%.0f"%(MatchingL1TkMinPt), "")
        leg.AddEntry(None,"Veto Non-matching L1Tk #DeltaR#leq%.1f:"%(isolation_cone), "")
        leg.AddEntry(h5,"p_{T} #geq 4 GeV", "f")        
        leg.AddEntry(h4,"p_{T} #geq 3 GeV", "f")
        leg.AddEntry(h3,"p_{T} #geq 2.5 GeV", "f")
        leg.AddEntry(h2,"p_{T} #geq 2 GeV", "f")
        leg.Draw("same")

      c.SaveAs(targetDir + title + ext)

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

      print title, "%.2f"%(1./h2.GetBinContent(11))
      print title, "%.2f"%(1./h3.GetBinContent(11))
      print title, "%.2f"%(1./h4.GetBinContent(11))
      print title, "%.2f"%(1./h5.GetBinContent(11))
      print 
      print title, "%.2f"%(2./(h2.GetBinContent(13) + h2.GetBinContent(14)))
      print title, "%.2f"%(2./(h3.GetBinContent(13) + h3.GetBinContent(14)))
      print title, "%.2f"%(2./(h4.GetBinContent(13) + h4.GetBinContent(14)))
      print title, "%.2f"%(2./(h5.GetBinContent(13) + h5.GetBinContent(14)))
      """
      print 
      print title, "%.2f"%(1./h2.GetBinContent(16))
      print title, "%.2f"%(1./h3.GetBinContent(16))
      print title, "%.2f"%(1./h4.GetBinContent(16))
      print title, "%.2f"%(1./h5.GetBinContent(16))
      """

      latex = applyTdrStyle()      

      if isolation_cone == 0.12:
        leg = TLegend(0.2,0.2,0.9,0.4,"","brNDC")
        leg.SetFillColor(kWhite)
        leg.SetBorderSize(0)
        leg.SetFillStyle(0)
        leg.SetTextSize(0.03)
        leg.AddEntry(h1,"Prompt L1Mu", "l")
        leg.AddEntry(None,"Displaced L1Mu", "")
        leg.AddEntry(h5,"Veto Matching L1Tk #DeltaR#leq0.12 with p_{T}#geq%.0f"%(MatchingL1TkMinPt), "l")
        leg.Draw("same")
      else:
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

    ## trigger rate plots vs pt
    makePlots(h_single_L1Mu_rate, 
              h_single_displaced_rate_dR0p4_L1TkPt2, 
              h_single_displaced_rate_dR0p4_L1TkPt2p5, 
              h_single_displaced_rate_dR0p4_L1TkPt3, 
              h_single_displaced_rate_dR0p4_L1TkPt4, 0.4, "L1Mu_trigger_rate_pt_dR0p4")
    makePlots(h_single_L1Mu_rate, 
              h_single_displaced_rate_dR0p3_L1TkPt2, 
              h_single_displaced_rate_dR0p3_L1TkPt2p5, 
              h_single_displaced_rate_dR0p3_L1TkPt3, 
              h_single_displaced_rate_dR0p3_L1TkPt4, 0.3, "L1Mu_trigger_rate_pt_dR0p3")
    makePlots(h_single_L1Mu_rate, 
              h_single_displaced_rate_dR0p2_L1TkPt2, 
              h_single_displaced_rate_dR0p2_L1TkPt2p5, 
              h_single_displaced_rate_dR0p2_L1TkPt3, 
              h_single_displaced_rate_dR0p2_L1TkPt4, 0.2, "L1Mu_trigger_rate_pt_dR0p2")
    makePlots(h_single_L1Mu_rate, 
              h_single_displaced_rate_dR0p12_L1TkPt2, 
              h_single_displaced_rate_dR0p12_L1TkPt2p5, 
              h_single_displaced_rate_dR0p12_L1TkPt3, 
              h_single_displaced_rate_dR0p12_L1TkPt4, 0.12, "L1Mu_trigger_rate_pt_dR0p12")

  if not eff:
    makeRateVsPtHistogram()    
    pass

  def makeRateVsEtaHistogram(ptCut):

    h_single_L1Mu_rate = TH1F("h_single_L1Mu_rate"," ",len(myetabin)-1, myetabin)

    h_single_displaced_rate_dR0p4_L1TkPt2 = TH1F("h_single_displaced_rate_dR0p4_L1TkPt2"," ",len(myetabin)-1, myetabin)
    h_single_displaced_rate_dR0p4_L1TkPt2p5 = TH1F("h_single_displaced_rate_dR0p4_L1TkPt2p5"," ",len(myetabin)-1, myetabin)
    h_single_displaced_rate_dR0p4_L1TkPt3 = TH1F("h_single_displaced_rate_dR0p4_L1TkPt3"," ",len(myetabin)-1, myetabin)
    h_single_displaced_rate_dR0p4_L1TkPt4 = TH1F("h_single_displaced_rate_dR0p4_L1TkPt4"," ",len(myetabin)-1, myetabin)

    h_single_displaced_rate_dR0p3_L1TkPt2 = TH1F("h_single_displaced_rate_dR0p3_L1TkPt2"," ",len(myetabin)-1, myetabin)
    h_single_displaced_rate_dR0p3_L1TkPt2p5 = TH1F("h_single_displaced_rate_dR0p3_L1TkPt2p5"," ",len(myetabin)-1, myetabin)
    h_single_displaced_rate_dR0p3_L1TkPt3 = TH1F("h_single_displaced_rate_dR0p3_L1TkPt3"," ",len(myetabin)-1, myetabin)
    h_single_displaced_rate_dR0p3_L1TkPt4 = TH1F("h_single_displaced_rate_dR0p3_L1TkPt4"," ",len(myetabin)-1, myetabin)

    h_single_displaced_rate_dR0p2_L1TkPt2 = TH1F("h_single_displaced_rate_dR0p2_L1TkPt2"," ",len(myetabin)-1, myetabin)
    h_single_displaced_rate_dR0p2_L1TkPt2p5 = TH1F("h_single_displaced_rate_dR0p2_L1TkPt2p5"," ",len(myetabin)-1, myetabin)
    h_single_displaced_rate_dR0p2_L1TkPt3 = TH1F("h_single_displaced_rate_dR0p2_L1TkPt3"," ",len(myetabin)-1, myetabin)
    h_single_displaced_rate_dR0p2_L1TkPt4 = TH1F("h_single_displaced_rate_dR0p2_L1TkPt4"," ",len(myetabin)-1, myetabin)

    h_single_displaced_rate_dR0p12_L1TkPt2 = TH1F("h_single_displaced_rate_dR0p12_L1TkPt2"," ",len(myetabin)-1, myetabin)
    h_single_displaced_rate_dR0p12_L1TkPt2p5 = TH1F("h_single_displaced_rate_dR0p12_L1TkPt2p5"," ",len(myetabin)-1, myetabin)
    h_single_displaced_rate_dR0p12_L1TkPt3 = TH1F("h_single_displaced_rate_dR0p12_L1TkPt3"," ",len(myetabin)-1, myetabin)
    h_single_displaced_rate_dR0p12_L1TkPt4 = TH1F("h_single_displaced_rate_dR0p12_L1TkPt4"," ",len(myetabin)-1, myetabin)

    for k in range(0,1000):#,treeHits.GetEntries()): #
      treeHits.GetEntry(k)

      ## get the max value of the momentum
      pts = list(treeHits.L1Mu_pt)
      if len(pts)>=1:
      
        def getMaxPts():
          maxPt1 = 0.
          maxPtIndex1 = -1

          maxPt_trig_dR0p4_L1TkPt4 = 0.
          maxPt_trig_dR0p4_L1TkPt3 = 0.
          maxPt_trig_dR0p4_L1TkPt2p5 = 0.
          maxPt_trig_dR0p4_L1TkPt2 = 0.
          
          maxPt_trig_dR0p3_L1TkPt4 = 0.
          maxPt_trig_dR0p3_L1TkPt3 = 0.
          maxPt_trig_dR0p3_L1TkPt2p5 = 0.
          maxPt_trig_dR0p3_L1TkPt2 = 0.

          maxPt_trig_dR0p2_L1TkPt4 = 0.
          maxPt_trig_dR0p2_L1TkPt3 = 0.
          maxPt_trig_dR0p2_L1TkPt2p5 = 0.
          maxPt_trig_dR0p2_L1TkPt2 = 0.
          
          maxPt_trig_dR0p12_L1TkPt4 = 0.
          maxPt_trig_dR0p12_L1TkPt3 = 0.
          maxPt_trig_dR0p12_L1TkPt2p5 = 0.
          maxPt_trig_dR0p12_L1TkPt2 = 0.

          
          maxPtIndex_trig_dR0p4_L1TkPt4 = -1
          maxPtIndex_trig_dR0p4_L1TkPt3 = -1
          maxPtIndex_trig_dR0p4_L1TkPt2p5 = -1
          maxPtIndex_trig_dR0p4_L1TkPt2 = -1
          
          maxPtIndex_trig_dR0p3_L1TkPt4 = -1
          maxPtIndex_trig_dR0p3_L1TkPt3 = -1
          maxPtIndex_trig_dR0p3_L1TkPt2p5 = -1
          maxPtIndex_trig_dR0p3_L1TkPt2 = -1

          maxPtIndex_trig_dR0p2_L1TkPt4 = -1
          maxPtIndex_trig_dR0p2_L1TkPt3 = -1
          maxPtIndex_trig_dR0p2_L1TkPt2p5 = -1
          maxPtIndex_trig_dR0p2_L1TkPt2 = -1
          
          maxPtIndex_trig_dR0p12_L1TkPt4 = -1
          maxPtIndex_trig_dR0p12_L1TkPt3 = -1
          maxPtIndex_trig_dR0p12_L1TkPt2p5 = -1
          maxPtIndex_trig_dR0p12_L1TkPt2 = -1

          for i in range(0,len(pts)):

            L1Mu_pt = treeHits.L1Mu_pt[i]
            L1Mu_bx = treeHits.L1Mu_bx[i]
            L1Mu_quality = treeHits.L1Mu_quality[i]
            L1Mu_L1Tk_dR_min = treeHits.L1Mu_L1Tk_dR_prop[i]
            L1Mu_L1Tk_pt = treeHits.L1Mu_L1Tk_pt_prop[i]
            
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
            matched = L1Mu_L1Tk_dR_min <= 0.12 and L1Mu_quality >= 4
            matched = matched and L1Mu_L1Tk_pt>=MatchingL1TkMinPt

            ## unmatched 
            if L1Mu_L1Tk_dR_min <= 0.4 and L1Mu_L1Tk_pt>=4:   unMatched_dR0p4_L1TkPt4 = True
            if L1Mu_L1Tk_dR_min <= 0.4 and L1Mu_L1Tk_pt>=3:   unMatched_dR0p4_L1TkPt3 = True
            if L1Mu_L1Tk_dR_min <= 0.4 and L1Mu_L1Tk_pt>=2.5: unMatched_dR0p4_L1TkPt2p5 = True
            if L1Mu_L1Tk_dR_min <= 0.4 and L1Mu_L1Tk_pt>=2:   unMatched_dR0p4_L1TkPt2 = True

            if L1Mu_L1Tk_dR_min <= 0.3 and L1Mu_L1Tk_pt>=4:   unMatched_dR0p3_L1TkPt4 = True
            if L1Mu_L1Tk_dR_min <= 0.3 and L1Mu_L1Tk_pt>=3:   unMatched_dR0p3_L1TkPt3 = True
            if L1Mu_L1Tk_dR_min <= 0.3 and L1Mu_L1Tk_pt>=2.5: unMatched_dR0p3_L1TkPt2p5 = True
            if L1Mu_L1Tk_dR_min <= 0.3 and L1Mu_L1Tk_pt>=2:   unMatched_dR0p3_L1TkPt2 = True

            if L1Mu_L1Tk_dR_min <= 0.2 and L1Mu_L1Tk_pt>=4:   unMatched_dR0p2_L1TkPt4 = True
            if L1Mu_L1Tk_dR_min <= 0.2 and L1Mu_L1Tk_pt>=3:   unMatched_dR0p2_L1TkPt3 = True
            if L1Mu_L1Tk_dR_min <= 0.2 and L1Mu_L1Tk_pt>=2.5: unMatched_dR0p2_L1TkPt2p5 = True
            if L1Mu_L1Tk_dR_min <= 0.2 and L1Mu_L1Tk_pt>=2:   unMatched_dR0p2_L1TkPt2 = True

            if L1Mu_L1Tk_dR_min <= 0.12 and L1Mu_L1Tk_pt>=4:   unMatched_dR0p12_L1TkPt4 = True
            if L1Mu_L1Tk_dR_min <= 0.12 and L1Mu_L1Tk_pt>=3:   unMatched_dR0p12_L1TkPt3 = True
            if L1Mu_L1Tk_dR_min <= 0.12 and L1Mu_L1Tk_pt>=2.5: unMatched_dR0p12_L1TkPt2p5 = True
            if L1Mu_L1Tk_dR_min <= 0.12 and L1Mu_L1Tk_pt>=2:   unMatched_dR0p12_L1TkPt2 = True

            common = (L1Mu_pt >= ptCut) and (abs(L1Mu_bx) == 0) and (L1Mu_quality >= 4)
            trig_dR0p4_L1TkPt4 =   (not matched) and (not unMatched_dR0p4_L1TkPt4)   and common
            trig_dR0p4_L1TkPt3 =   (not matched) and (not unMatched_dR0p4_L1TkPt3)   and common
            trig_dR0p4_L1TkPt2p5 = (not matched) and (not unMatched_dR0p4_L1TkPt2p5) and common
            trig_dR0p4_L1TkPt2 =   (not matched) and (not unMatched_dR0p4_L1TkPt2)   and common

            trig_dR0p3_L1TkPt4 =   (not matched) and (not unMatched_dR0p3_L1TkPt4)   and common
            trig_dR0p3_L1TkPt3 =   (not matched) and (not unMatched_dR0p3_L1TkPt3)   and common
            trig_dR0p3_L1TkPt2p5 = (not matched) and (not unMatched_dR0p3_L1TkPt2p5) and common
            trig_dR0p3_L1TkPt2 =   (not matched) and (not unMatched_dR0p3_L1TkPt2)   and common

            trig_dR0p2_L1TkPt4 =   (not matched) and (not unMatched_dR0p2_L1TkPt4)   and common
            trig_dR0p2_L1TkPt3 =   (not matched) and (not unMatched_dR0p2_L1TkPt3)   and common
            trig_dR0p2_L1TkPt2p5 = (not matched) and (not unMatched_dR0p2_L1TkPt2p5) and common
            trig_dR0p2_L1TkPt2 =   (not matched) and (not unMatched_dR0p2_L1TkPt2)   and common

            trig_dR0p12_L1TkPt4 =   (not matched) and common
            trig_dR0p12_L1TkPt3 =   (not matched) and common
            trig_dR0p12_L1TkPt2p5 = (not matched) and common
            trig_dR0p12_L1TkPt2 =   (not matched) and common



            if common             and L1Mu_pt > maxPt1: maxPt1 = L1Mu_pt; maxPtIndex1 = i

            if trig_dR0p4_L1TkPt4 and L1Mu_pt > maxPt_trig_dR0p4_L1TkPt4:     maxPt_trig_dR0p4_L1TkPt4 = L1Mu_pt;   maxPtIndex_trig_dR0p4_L1TkPt4 = i
            if trig_dR0p4_L1TkPt3 and L1Mu_pt > maxPt_trig_dR0p4_L1TkPt3:     maxPt_trig_dR0p4_L1TkPt3 = L1Mu_pt;   maxPtIndex_trig_dR0p4_L1TkPt3 = i
            if trig_dR0p4_L1TkPt2p5 and L1Mu_pt > maxPt_trig_dR0p4_L1TkPt2p5: maxPt_trig_dR0p4_L1TkPt2p5 = L1Mu_pt; maxPtIndex_trig_dR0p4_L1TkPt2p5 = i
            if trig_dR0p4_L1TkPt2 and L1Mu_pt > maxPt_trig_dR0p4_L1TkPt2:     maxPt_trig_dR0p4_L1TkPt2 = L1Mu_pt;   maxPtIndex_trig_dR0p4_L1TkPt2 = i

            if trig_dR0p3_L1TkPt4 and L1Mu_pt > maxPt_trig_dR0p3_L1TkPt4:     maxPt_trig_dR0p3_L1TkPt4 = L1Mu_pt;   maxPtIndex_trig_dR0p3_L1TkPt4 = i
            if trig_dR0p3_L1TkPt3 and L1Mu_pt > maxPt_trig_dR0p3_L1TkPt3:     maxPt_trig_dR0p3_L1TkPt3 = L1Mu_pt;   maxPtIndex_trig_dR0p3_L1TkPt3 = i
            if trig_dR0p3_L1TkPt2p5 and L1Mu_pt > maxPt_trig_dR0p3_L1TkPt2p5: maxPt_trig_dR0p3_L1TkPt2p5 = L1Mu_pt; maxPtIndex_trig_dR0p3_L1TkPt2p5 = i
            if trig_dR0p3_L1TkPt2 and L1Mu_pt > maxPt_trig_dR0p3_L1TkPt2:     maxPt_trig_dR0p3_L1TkPt2 = L1Mu_pt;   maxPtIndex_trig_dR0p3_L1TkPt2 = i

            if trig_dR0p2_L1TkPt4 and L1Mu_pt > maxPt_trig_dR0p2_L1TkPt4:     maxPt_trig_dR0p2_L1TkPt4 = L1Mu_pt;   maxPtIndex_trig_dR0p2_L1TkPt4 = i
            if trig_dR0p2_L1TkPt3 and L1Mu_pt > maxPt_trig_dR0p2_L1TkPt3:     maxPt_trig_dR0p2_L1TkPt3 = L1Mu_pt;   maxPtIndex_trig_dR0p2_L1TkPt3 = i
            if trig_dR0p2_L1TkPt2p5 and L1Mu_pt > maxPt_trig_dR0p2_L1TkPt2p5: maxPt_trig_dR0p2_L1TkPt2p5 = L1Mu_pt; maxPtIndex_trig_dR0p2_L1TkPt2p5 = i
            if trig_dR0p2_L1TkPt2 and L1Mu_pt > maxPt_trig_dR0p2_L1TkPt2:     maxPt_trig_dR0p2_L1TkPt2 = L1Mu_pt;   maxPtIndex_trig_dR0p2_L1TkPt2 = i

            if trig_dR0p12_L1TkPt4 and L1Mu_pt > maxPt_trig_dR0p12_L1TkPt4:     maxPt_trig_dR0p12_L1TkPt4 = L1Mu_pt;   maxPtIndex_trig_dR0p12_L1TkPt4 = i
            if trig_dR0p12_L1TkPt3 and L1Mu_pt > maxPt_trig_dR0p12_L1TkPt3:     maxPt_trig_dR0p12_L1TkPt3 = L1Mu_pt;   maxPtIndex_trig_dR0p12_L1TkPt3 = i
            if trig_dR0p12_L1TkPt2p5 and L1Mu_pt > maxPt_trig_dR0p12_L1TkPt2p5: maxPt_trig_dR0p12_L1TkPt2p5 = L1Mu_pt; maxPtIndex_trig_dR0p12_L1TkPt2p5 = i
            if trig_dR0p12_L1TkPt2 and L1Mu_pt > maxPt_trig_dR0p12_L1TkPt2:     maxPt_trig_dR0p12_L1TkPt2 = L1Mu_pt;   maxPtIndex_trig_dR0p12_L1TkPt2 = i

          return maxPt1, maxPtIndex1, maxPt_trig_dR0p4_L1TkPt4, maxPt_trig_dR0p4_L1TkPt3, maxPt_trig_dR0p4_L1TkPt2p5, maxPt_trig_dR0p4_L1TkPt2, maxPt_trig_dR0p3_L1TkPt4, maxPt_trig_dR0p3_L1TkPt3, maxPt_trig_dR0p3_L1TkPt2p5, maxPt_trig_dR0p3_L1TkPt2, maxPt_trig_dR0p2_L1TkPt4, maxPt_trig_dR0p2_L1TkPt3, maxPt_trig_dR0p2_L1TkPt2p5, maxPt_trig_dR0p2_L1TkPt2, maxPt_trig_dR0p12_L1TkPt4, maxPt_trig_dR0p12_L1TkPt3, maxPt_trig_dR0p12_L1TkPt2p5, maxPt_trig_dR0p12_L1TkPt2, maxPtIndex_trig_dR0p4_L1TkPt4, maxPtIndex_trig_dR0p4_L1TkPt3, maxPtIndex_trig_dR0p4_L1TkPt2p5, maxPtIndex_trig_dR0p4_L1TkPt2, maxPtIndex_trig_dR0p3_L1TkPt4, maxPtIndex_trig_dR0p3_L1TkPt3, maxPtIndex_trig_dR0p3_L1TkPt2p5, maxPtIndex_trig_dR0p3_L1TkPt2, maxPtIndex_trig_dR0p2_L1TkPt4, maxPtIndex_trig_dR0p2_L1TkPt3, maxPtIndex_trig_dR0p2_L1TkPt2p5, maxPtIndex_trig_dR0p2_L1TkPt2, maxPtIndex_trig_dR0p12_L1TkPt4, maxPtIndex_trig_dR0p12_L1TkPt3, maxPtIndex_trig_dR0p12_L1TkPt2p5, maxPtIndex_trig_dR0p12_L1TkPt2
        
        maxPt1, maxPtIndex1, maxPt_trig_dR0p4_L1TkPt4, maxPt_trig_dR0p4_L1TkPt3, maxPt_trig_dR0p4_L1TkPt2p5, maxPt_trig_dR0p4_L1TkPt2, maxPt_trig_dR0p3_L1TkPt4, maxPt_trig_dR0p3_L1TkPt3, maxPt_trig_dR0p3_L1TkPt2p5, maxPt_trig_dR0p3_L1TkPt2, maxPt_trig_dR0p2_L1TkPt4, maxPt_trig_dR0p2_L1TkPt3, maxPt_trig_dR0p2_L1TkPt2p5, maxPt_trig_dR0p2_L1TkPt2, maxPt_trig_dR0p12_L1TkPt4, maxPt_trig_dR0p12_L1TkPt3, maxPt_trig_dR0p12_L1TkPt2p5, maxPt_trig_dR0p12_L1TkPt2, maxPtIndex_trig_dR0p4_L1TkPt4, maxPtIndex_trig_dR0p4_L1TkPt3, maxPtIndex_trig_dR0p4_L1TkPt2p5, maxPtIndex_trig_dR0p4_L1TkPt2, maxPtIndex_trig_dR0p3_L1TkPt4, maxPtIndex_trig_dR0p3_L1TkPt3, maxPtIndex_trig_dR0p3_L1TkPt2p5, maxPtIndex_trig_dR0p3_L1TkPt2, maxPtIndex_trig_dR0p2_L1TkPt4, maxPtIndex_trig_dR0p2_L1TkPt3, maxPtIndex_trig_dR0p2_L1TkPt2p5, maxPtIndex_trig_dR0p2_L1TkPt2, maxPtIndex_trig_dR0p12_L1TkPt4, maxPtIndex_trig_dR0p12_L1TkPt3, maxPtIndex_trig_dR0p12_L1TkPt2p5, maxPtIndex_trig_dR0p12_L1TkPt2 = getMaxPts()

        if (maxPt1>0): h_single_L1Mu_rate.Fill(treeHits.L1Mu_eta[maxPtIndex1])

        if (maxPt_trig_dR0p4_L1TkPt4>0): h_single_displaced_rate_dR0p4_L1TkPt4.Fill(treeHits.L1Mu_eta[maxPtIndex_trig_dR0p4_L1TkPt4])
        if (maxPt_trig_dR0p4_L1TkPt3>0): h_single_displaced_rate_dR0p4_L1TkPt3.Fill(treeHits.L1Mu_eta[maxPtIndex_trig_dR0p4_L1TkPt3])
        if (maxPt_trig_dR0p4_L1TkPt2p5>0): h_single_displaced_rate_dR0p4_L1TkPt2p5.Fill(treeHits.L1Mu_eta[maxPtIndex_trig_dR0p4_L1TkPt2p5])
        if (maxPt_trig_dR0p4_L1TkPt2>0): h_single_displaced_rate_dR0p4_L1TkPt2.Fill(treeHits.L1Mu_eta[maxPtIndex_trig_dR0p4_L1TkPt2])

        if (maxPt_trig_dR0p3_L1TkPt4>0): h_single_displaced_rate_dR0p3_L1TkPt4.Fill(treeHits.L1Mu_eta[maxPtIndex_trig_dR0p3_L1TkPt4])
        if (maxPt_trig_dR0p3_L1TkPt3>0): h_single_displaced_rate_dR0p3_L1TkPt3.Fill(treeHits.L1Mu_eta[maxPtIndex_trig_dR0p3_L1TkPt3])
        if (maxPt_trig_dR0p3_L1TkPt2p5>0): h_single_displaced_rate_dR0p3_L1TkPt2p5.Fill(treeHits.L1Mu_eta[maxPtIndex_trig_dR0p3_L1TkPt2p5])
        if (maxPt_trig_dR0p3_L1TkPt2>0): h_single_displaced_rate_dR0p3_L1TkPt2.Fill(treeHits.L1Mu_eta[maxPtIndex_trig_dR0p3_L1TkPt2])

        if (maxPt_trig_dR0p2_L1TkPt4>0): h_single_displaced_rate_dR0p2_L1TkPt4.Fill(treeHits.L1Mu_eta[maxPtIndex_trig_dR0p2_L1TkPt4])
        if (maxPt_trig_dR0p2_L1TkPt3>0): h_single_displaced_rate_dR0p2_L1TkPt3.Fill(treeHits.L1Mu_eta[maxPtIndex_trig_dR0p2_L1TkPt3])
        if (maxPt_trig_dR0p2_L1TkPt2p5>0): h_single_displaced_rate_dR0p2_L1TkPt2p5.Fill(treeHits.L1Mu_eta[maxPtIndex_trig_dR0p2_L1TkPt2p5])
        if (maxPt_trig_dR0p2_L1TkPt2>0): h_single_displaced_rate_dR0p2_L1TkPt2.Fill(treeHits.L1Mu_eta[maxPtIndex_trig_dR0p2_L1TkPt2])

        if (maxPt_trig_dR0p12_L1TkPt4>0): h_single_displaced_rate_dR0p12_L1TkPt4.Fill(treeHits.L1Mu_eta[maxPtIndex_trig_dR0p12_L1TkPt4])
        if (maxPt_trig_dR0p12_L1TkPt3>0): h_single_displaced_rate_dR0p12_L1TkPt3.Fill(treeHits.L1Mu_eta[maxPtIndex_trig_dR0p12_L1TkPt3])
        if (maxPt_trig_dR0p12_L1TkPt2p5>0): h_single_displaced_rate_dR0p12_L1TkPt2p5.Fill(treeHits.L1Mu_eta[maxPtIndex_trig_dR0p12_L1TkPt2p5])
        if (maxPt_trig_dR0p12_L1TkPt2>0): h_single_displaced_rate_dR0p12_L1TkPt2.Fill(treeHits.L1Mu_eta[maxPtIndex_trig_dR0p12_L1TkPt2])

                                                                                    
    def makePlots(h1, h2, h3, h4, h5, isolation_cone, title):
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

      b1 = TH1F("b1","b1",len(myetabin)-1, myetabin)
      b1.GetYaxis().SetRangeUser(.001,100)
      b1.GetYaxis().SetTitleOffset(1.2)
      b1.GetYaxis().SetNdivisions(520)
      b1.GetYaxis().SetTitle("L1 Trigger Rate [kHz]")
      b1.GetXaxis().SetTitle("L1 muon #eta")
      b1.GetXaxis().SetTitleFont(62)
      b1.GetXaxis().SetTitleOffset(1.2)
      b1.GetXaxis().SetTitleSize(0.05)
      b1.GetYaxis().SetTitleSize(0.05)
      b1.SetTitle("                                                                  14TeV, " + pu)
      b1.SetStats(0)
      b1.Draw()

      h1 = getRateEtaHistogram(treeHits, h1)
      h1.SetLineColor(kRed)
      h1.Draw("same")
      
      if isolation_cone != 0.12:    
        h2 = getRateEtaHistogram(treeHits, h2)
        h2.SetLineColor(kMagenta)
        h2.Draw("same")

        h3 = getRateEtaHistogram(treeHits, h3)
        h3.SetLineColor(kBlue)
        h3.Draw("same")
        
        h4 = getRateEtaHistogram(treeHits, h4)
        h4.SetLineColor(kGreen+1)
        h4.Draw("same")

      h5 = getRateEtaHistogram(treeHits, h5)
      h5.SetLineColor(kOrange+1)
      h5.Draw("same")
      
      latex = applyTdrStyle()      
 
      if isolation_cone == 0.12:
        leg = TLegend(0.2,0.7,0.9,0.9,"","brNDC")
        leg.SetFillColor(kWhite)
        leg.SetBorderSize(0)
        leg.SetFillStyle(0)
        leg.SetTextSize(0.03)
        leg.AddEntry(h1,"Prompt L1Mu", "l")
        leg.AddEntry(None,"Displaced L1Mu", "")
        leg.AddEntry(h5,"Matching L1Tk #DeltaR#leq0.12 with p_{T}#geq%.0f"%(MatchingL1TkMinPt), "l")
        leg.Draw("same")
      else:
        leg = TLegend(0.2,0.7,0.9,0.9,"","brNDC")
        leg.SetFillColor(kWhite)
        leg.SetBorderSize(0)
        leg.SetFillStyle(0)
        leg.SetTextSize(0.03)
        leg.AddEntry(h1,"Prompt L1Mu", "l")
        leg.AddEntry(None,"Displaced L1Mu", "")
        leg.AddEntry(None,"Matching L1Tk #DeltaR#leq0.12 with p_{T}#geq%.0f"%(MatchingL1TkMinPt), "")
        leg.AddEntry(None,"Non-matching L1Tk #DeltaR#leq%.1f:"%(isolation_cone), "")
        leg.AddEntry(h5,"p_{T} #geq 4 GeV", "l")        
        leg.AddEntry(h4,"p_{T} #geq 3 GeV", "l")
        leg.AddEntry(h3,"p_{T} #geq 2.5 GeV", "l")
        leg.AddEntry(h2,"p_{T} #geq 2 GeV", "l")
        leg.Draw("same")

      c.SaveAs(targetDir + title + "ptCut%d.png"%(ptCut))

      ## ratios 
      c = TCanvas("c","c",800,600)
      c.Clear()    
      gStyle.SetTitleBorderSize(0);
      gStyle.SetPadLeftMargin(0.126);
      gStyle.SetPadRightMargin(0.04);
      gStyle.SetPadTopMargin(0.06);
      gStyle.SetPadBottomMargin(0.13);
#      gPad.SetLogy(1)

      b1 = TH1F("b1","b1",len(myetabin)-1, myetabin)
      b1.GetYaxis().SetRangeUser(0.0001,1)
      b1.GetYaxis().SetTitleOffset(1.2)
      b1.GetYaxis().SetNdivisions(520)
      b1.GetYaxis().SetTitle("Ratio (normalized to prompt L1Mu)")
      b1.GetXaxis().SetTitle("L1 muon #eta")
      b1.GetXaxis().SetTitleFont(62)
      b1.GetXaxis().SetTitleOffset(1.2)
      b1.GetXaxis().SetTitleSize(0.05)
      b1.GetYaxis().SetTitleSize(0.05)
      b1.SetTitle("14TeV," + pu)
      b1.SetStats(0)
      b1.Draw()

      if isolation_cone != 0.12:    
        h2.SetLineColor(kMagenta)
        h2.Divide(h1)
        h2.SetFillColor(kWhite)
        h2.Draw("same")
        
        h3.SetLineColor(kBlue)
        h3.Divide(h1)
        h2.SetFillColor(kWhite)
        h3.Draw("same")
        
        h4.SetLineColor(kGreen+1)
        h4.Divide(h1)
        h4.SetFillColor(kWhite)
        h4.Draw("same")
        
      h5.SetLineColor(kOrange+1)
      h5.Divide(h1)
      h5.SetFillColor(kWhite)
      h5.Draw("same")
      """
      print title, "%.2f"%(h2.GetBinContent(11)) #pt10
      print title, "%.2f"%(h3.GetBinContent(11))
      print title, "%.2f"%(h4.GetBinContent(11))
      print title, "%.2f"%(h5.GetBinContent(11))
      print 
      print title, "%.2f"%((h2.GetBinContent(13) + h2.GetBinContent(14))/2.) #average of pt14 and pt16
      print title, "%.2f"%((h3.GetBinContent(13) + h3.GetBinContent(14))/2.)
      print title, "%.2f"%((h4.GetBinContent(13) + h4.GetBinContent(14))/2.)
      print title, "%.2f"%((h5.GetBinContent(13) + h5.GetBinContent(14))/2.)
     """

      latex = applyTdrStyle()      

      if isolation_cone == 0.12:
        leg = TLegend(0.2,0.2,0.9,0.4,"","brNDC")
        leg.SetFillColor(kWhite)
        leg.SetBorderSize(0)
        leg.SetFillStyle(0)
        leg.SetTextSize(0.03)
        leg.AddEntry(None,"Displaced L1Mu", "")
        leg.AddEntry(h5,"Matching L1Tk #DeltaR#leq0.12 with p_{T}#geq%.0f"%(MatchingL1TkMinPt), "l")
        leg.Draw("same")
      else:
        leg = TLegend(0.2,0.2,0.9,0.4,"","brNDC")
        leg.SetFillColor(kWhite)
        leg.SetBorderSize(0)
        leg.SetFillStyle(0)
        leg.SetTextSize(0.03)
        leg.AddEntry(None,"Displaced L1Mu", "")
        leg.AddEntry(None,"Matching L1Tk #DeltaR#leq0.12 with p_{T}#geq%.0f"%(MatchingL1TkMinPt), "")
        leg.AddEntry(None,"Non-matching L1Tk #DeltaR#leq%.1f:"%(isolation_cone), "")
        leg.AddEntry(h5,"p_{T} #geq 4 GeV", "l")        
        leg.AddEntry(h4,"p_{T} #geq 3 GeV", "l")
        leg.AddEntry(h3,"p_{T} #geq 2.5 GeV", "l")
        leg.AddEntry(h2,"p_{T} #geq 2 GeV", "l")
        leg.Draw("same")

      c.SaveAs(targetDir + title + "ptCut%d_ratio"%(ptCut) + ext)

    ## trigger rate plots vs pt
    makePlots(h_single_L1Mu_rate, 
              h_single_displaced_rate_dR0p4_L1TkPt2,
              h_single_displaced_rate_dR0p4_L1TkPt2p5, 
              h_single_displaced_rate_dR0p4_L1TkPt3, 
              h_single_displaced_rate_dR0p4_L1TkPt4, 0.4,
              "L1Mu_trigger_rate_pt_dR0p4")

    makePlots(h_single_L1Mu_rate, 
              h_single_displaced_rate_dR0p3_L1TkPt2,
              h_single_displaced_rate_dR0p3_L1TkPt2p5, 
              h_single_displaced_rate_dR0p3_L1TkPt3, 
              h_single_displaced_rate_dR0p3_L1TkPt4, 0.3,
              "L1Mu_trigger_rate_pt_dR0p3")

    makePlots(h_single_L1Mu_rate, 
              h_single_displaced_rate_dR0p2_L1TkPt2,
              h_single_displaced_rate_dR0p2_L1TkPt2p5, 
              h_single_displaced_rate_dR0p2_L1TkPt3, 
              h_single_displaced_rate_dR0p2_L1TkPt4, 0.2,
              "L1Mu_trigger_rate_pt_dR0p2")

    makePlots(h_single_L1Mu_rate, 
              h_single_displaced_rate_dR0p12_L1TkPt2,
              h_single_displaced_rate_dR0p12_L1TkPt2p5, 
              h_single_displaced_rate_dR0p12_L1TkPt3, 
              h_single_displaced_rate_dR0p12_L1TkPt4, 0.12,
              "L1Mu_trigger_rate_pt_dR0p12")

  if not eff and False:
    makeRateVsEtaHistogram(10)
    makeRateVsEtaHistogram(15)
    makeRateVsEtaHistogram(20)
    pass


#  exit()
  
  def makedRL1MuL1TkHistogram():

    thisTargetDir = "dRL1MuL1TkHistogram/"

    if False:
      draw_1D(ch, "genGdMu_deta_prop", thisTargetDir + "genGdMu_deta_prop", "d#eta; d#eta; Entries", "(100,0.,1.)", cut="", opt = "")
      draw_1D(ch, "genGdMu_dphi_prop", thisTargetDir + "genGdMu_dphi_prop", "d#phi; d#phi; Entries", "(100,0.,1.)", cut="", opt = "")
      draw_1D(ch, "genGdMu_dR_prop", thisTargetDir + "genGdMu_dR_prop", "dR; dR; Entries", "(100,0.,1.)", cut="", opt = "")

      draw_1D(ch, "genGdMu_deta_prop", thisTargetDir + "genGdMu_deta_prop_pt5", "d#eta; d#eta; Entries", "(100,0.,1.)", cut="genGdMu_pt>5", opt = "")
      draw_1D(ch, "genGdMu_dphi_prop", thisTargetDir + "genGdMu_dphi_prop_pt5", "d#phi; d#phi; Entries", "(100,0.,1.)", cut="genGdMu_pt>5", opt = "")
      draw_1D(ch, "genGdMu_dR_prop", thisTargetDir + "genGdMu_dR_prop_pt5", "dR; dR; Entries", "(100,0.,1.)", cut="genGdMu_pt>5", opt = "")

      draw_1D(ch, "genGdMu_deta_prop", thisTargetDir + "genGdMu_deta_prop_pt20", "d#eta; d#eta; Entries", "(100,0.,1.)", cut="genGdMu_pt>20", opt = "")
      draw_1D(ch, "genGdMu_dphi_prop", thisTargetDir + "genGdMu_dphi_prop_pt20", "d#phi; d#phi; Entries", "(100,0.,1.)", cut="genGdMu_pt>20", opt = "")
      draw_1D(ch, "genGdMu_dR_prop", thisTargetDir + "genGdMu_dR_prop_pt20", "dR; dR; Entries", "(100,0.,1.)", cut="genGdMu_pt>20", opt = "")

      draw_1D(ch, "genGdMu_deta_prop", thisTargetDir + "genGdMu_deta_prop_pt30", "d#eta; d#eta; Entries", "(100,0.,1.)", cut="genGdMu_pt>30", opt = "")
      draw_1D(ch, "genGdMu_dphi_prop", thisTargetDir + "genGdMu_dphi_prop_pt30", "d#phi; d#phi; Entries", "(100,0.,1.)", cut="genGdMu_pt>30", opt = "")
      draw_1D(ch, "genGdMu_dR_prop", thisTargetDir + "genGdMu_dR_prop_pt30", "dR; dR; Entries", "(100,0.,1.)", cut="genGdMu_pt>30", opt = "")


      draw_1D(ch, "genGdMu_deta_prop", thisTargetDir + "genGdMu_deta_prop_dxy0to0p1_pt5", "d#eta; d#eta; Entries", "(100,0.,1.)", cut="abs(genGdMu_dxy)<0.1 && genGdMu_pt>5", opt = "")
      draw_1D(ch, "genGdMu_dphi_prop", thisTargetDir + "genGdMu_dphi_prop_dxy0to0p1_pt5", "d#phi; d#phi; Entries", "(100,0.,1.)", cut="abs(genGdMu_dxy)<0.1 && genGdMu_pt>5", opt = "")
      draw_1D(ch, "genGdMu_dR_prop", thisTargetDir + "genGdMu_dR_prop_dxy0to0p1_pt5", "dR; dR; Entries", "(100,0.,1.)", cut="abs(genGdMu_dxy)<0.1 && genGdMu_pt>5", opt = "")

      draw_1D(ch, "genGdMu_deta_prop", thisTargetDir + "genGdMu_deta_prop_dxy1to5_pt5", "d#eta; d#eta; Entries", "(100,0.,1.)", cut="1<abs(genGdMu_dxy) && abs(genGdMu_dxy)<5 && genGdMu_pt>5", opt = "")
      draw_1D(ch, "genGdMu_dphi_prop", thisTargetDir + "genGdMu_dphi_prop_dxy1to5_pt5", "d#phi; d#phi; Entries", "(100,0.,1.)", cut="1<abs(genGdMu_dxy) && abs(genGdMu_dxy)<5 && genGdMu_pt>5", opt = "")
      draw_1D(ch, "genGdMu_dR_prop", thisTargetDir + "genGdMu_dR_prop_dxy1to5_pt5", "dR; dR; Entries", "(100,0.,1.)", cut="1<abs(genGdMu_dxy) && abs(genGdMu_dxy)<5 && genGdMu_pt>5", opt = "")

      draw_1D(ch, "genGdMu_deta_prop", thisTargetDir + "genGdMu_deta_prop_dxy5to10_pt5", "d#eta; d#eta; Entries", "(100,0.,1.)", cut="5<abs(genGdMu_dxy) && abs(genGdMu_dxy)<10 && genGdMu_pt>5", opt = "")
      draw_1D(ch, "genGdMu_dphi_prop", thisTargetDir + "genGdMu_dphi_prop_dxy5to10_pt5", "d#phi; d#phi; Entries", "(100,0.,1.)", cut="5<abs(genGdMu_dxy) && abs(genGdMu_dxy)<10 && genGdMu_pt>5", opt = "")
      draw_1D(ch, "genGdMu_dR_prop", thisTargetDir + "genGdMu_dR_prop_dxy5to10_pt5", "dR; dR; Entries", "(100,0.,1.)", cut="5<abs(genGdMu_dxy) && abs(genGdMu_dxy)<10 && genGdMu_pt>5", opt = "")

      draw_1D(ch, "genGdMu_deta_prop", thisTargetDir + "genGdMu_deta_prop_dxy10to50_pt5", "d#eta; d#eta; Entries", "(100,0.,1.)", cut="10<abs(genGdMu_dxy) && abs(genGdMu_dxy)<30 && genGdMu_pt>5", opt = "")
      draw_1D(ch, "genGdMu_dphi_prop", thisTargetDir + "genGdMu_dphi_prop_dxy10to50_pt5", "d#phi; d#phi; Entries", "(100,0.,1.)", cut="10<abs(genGdMu_dxy) && abs(genGdMu_dxy)<30 && genGdMu_pt>5", opt = "")
      draw_1D(ch, "genGdMu_dR_prop", thisTargetDir + "genGdMu_dR_prop_dxy10to50_pt5", "dR; dR; Entries", "(100,0.,1.)", cut="10<abs(genGdMu_dxy) && abs(genGdMu_dxy)<30 && genGdMu_pt>5", opt = "")


      draw_1D(ch, "genGdMu_deta_prop", thisTargetDir + "genGdMu_deta_prop_dxy0to0p1_pt20", "d#eta; d#eta; Entries", "(100,0.,1.)", cut="abs(genGdMu_dxy)<0.1 && genGdMu_pt>20", opt = "")
      draw_1D(ch, "genGdMu_dphi_prop", thisTargetDir + "genGdMu_dphi_prop_dxy0to0p1_pt20", "d#phi; d#phi; Entries", "(100,0.,1.)", cut="abs(genGdMu_dxy)<0.1 && genGdMu_pt>20", opt = "")
      draw_1D(ch, "genGdMu_dR_prop", thisTargetDir + "genGdMu_dR_prop_dxy0to0p1_pt20", "dR; dR; Entries", "(100,0.,1.)", cut="abs(genGdMu_dxy)<0.1 && genGdMu_pt>20", opt = "")

      draw_1D(ch, "genGdMu_deta_prop", thisTargetDir + "genGdMu_deta_prop_dxy1to5_pt20", "d#eta; d#eta; Entries", "(100,0.,1.)", cut="1<abs(genGdMu_dxy) && abs(genGdMu_dxy)<5 && genGdMu_pt>20", opt = "")
      draw_1D(ch, "genGdMu_dphi_prop", thisTargetDir + "genGdMu_dphi_prop_dxy1to5_pt20", "d#phi; d#phi; Entries", "(100,0.,1.)", cut="1<abs(genGdMu_dxy) && abs(genGdMu_dxy)<5 && genGdMu_pt>20", opt = "")
      draw_1D(ch, "genGdMu_dR_prop", thisTargetDir + "genGdMu_dR_prop_dxy1to5_pt20", "dR; dR; Entries", "(100,0.,1.)", cut="1<abs(genGdMu_dxy) && abs(genGdMu_dxy)<5 && genGdMu_pt>20", opt = "")

      draw_1D(ch, "genGdMu_deta_prop", thisTargetDir + "genGdMu_deta_prop_dxy5to10_pt20", "d#eta; d#eta; Entries", "(100,0.,1.)", cut="5<abs(genGdMu_dxy) && abs(genGdMu_dxy)<10 && genGdMu_pt>20", opt = "")
      draw_1D(ch, "genGdMu_dphi_prop", thisTargetDir + "genGdMu_dphi_prop_dxy5to10_pt20", "d#phi; d#phi; Entries", "(100,0.,1.)", cut="5<abs(genGdMu_dxy) && abs(genGdMu_dxy)<10 && genGdMu_pt>20", opt = "")
      draw_1D(ch, "genGdMu_dR_prop", thisTargetDir + "genGdMu_dR_prop_dxy5to10_pt20", "dR; dR; Entries", "(100,0.,1.)", cut="5<abs(genGdMu_dxy) && abs(genGdMu_dxy)<10 && genGdMu_pt>20", opt = "")

      draw_1D(ch, "genGdMu_deta_prop", thisTargetDir + "genGdMu_deta_prop_dxy10to50_pt20", "d#eta; d#eta; Entries", "(100,0.,1.)", cut="10<abs(genGdMu_dxy) && abs(genGdMu_dxy)<30 && genGdMu_pt>20", opt = "")
      draw_1D(ch, "genGdMu_dphi_prop", thisTargetDir + "genGdMu_dphi_prop_dxy10to50_pt20", "d#phi; d#phi; Entries", "(100,0.,1.)", cut="10<abs(genGdMu_dxy) && abs(genGdMu_dxy)<30 && genGdMu_pt>20", opt = "")
      draw_1D(ch, "genGdMu_dR_prop", thisTargetDir + "genGdMu_dR_prop_dxy10to50_pt20", "dR; dR; Entries", "(100,0.,1.)", cut="10<abs(genGdMu_dxy) && abs(genGdMu_dxy)<30 && genGdMu_pt>20", opt = "")


      draw_1D(ch, "genGdMu_deta_corr", thisTargetDir + "genGdMu_deta_corr", "d#eta; d#eta; Entries", "(100,0.,1.)", cut="", opt = "")
      draw_1D(ch, "genGdMu_dphi_corr", thisTargetDir + "genGdMu_dphi_corr", "d#phi; d#phi; Entries", "(100,0.,1.)", cut="", opt = "")
      draw_1D(ch, "genGdMu_dR_corr", thisTargetDir + "genGdMu_dR_corr", "dR; dR; Entries", "(100,0.,1.)", cut="", opt = "")

      draw_1D(ch, "genGdMu_deta_corr", thisTargetDir + "genGdMu_deta_corr_pt5", "d#eta; d#eta; Entries", "(100,0.,1.)", cut="genGdMu_pt>5", opt = "")
      draw_1D(ch, "genGdMu_dphi_corr", thisTargetDir + "genGdMu_dphi_corr_pt5", "d#phi; d#phi; Entries", "(100,0.,1.)", cut="genGdMu_pt>5", opt = "")
      draw_1D(ch, "genGdMu_dR_corr", thisTargetDir + "genGdMu_dR_corr_pt5", "dR; dR; Entries", "(100,0.,1.)", cut="genGdMu_pt>5", opt = "")

      draw_1D(ch, "genGdMu_deta_corr", thisTargetDir + "genGdMu_deta_corr_pt20", "d#eta; d#eta; Entries", "(100,0.,1.)", cut="genGdMu_pt>20", opt = "")
      draw_1D(ch, "genGdMu_dphi_corr", thisTargetDir + "genGdMu_dphi_corr_pt20", "d#phi; d#phi; Entries", "(100,0.,1.)", cut="genGdMu_pt>20", opt = "")
      draw_1D(ch, "genGdMu_dR_corr", thisTargetDir + "genGdMu_dR_corr_pt20", "dR; dR; Entries", "(100,0.,1.)", cut="genGdMu_pt>20", opt = "")

      draw_1D(ch, "genGdMu_deta_corr", thisTargetDir + "genGdMu_deta_corr_pt30", "d#eta; d#eta; Entries", "(100,0.,1.)", cut="genGdMu_pt>30", opt = "")
      draw_1D(ch, "genGdMu_dphi_corr", thisTargetDir + "genGdMu_dphi_corr_pt30", "d#phi; d#phi; Entries", "(100,0.,1.)", cut="genGdMu_pt>30", opt = "")
      draw_1D(ch, "genGdMu_dR_corr", thisTargetDir + "genGdMu_dR_corr_pt30", "dR; dR; Entries", "(100,0.,1.)", cut="genGdMu_pt>30", opt = "")


    genGdMu_L1Mu_dR_fid = TH1F("genGdMu_L1Mu_dR_fid","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy0to0p1 = TH1F("genGdMu_L1Mu_dR_fid_dxy0to0p1","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy1to5 = TH1F("genGdMu_L1Mu_dR_fid_dxy1to5","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy5to10 = TH1F("genGdMu_L1Mu_dR_fid_dxy5to10","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy10to50 = TH1F("genGdMu_L1Mu_dR_fid_dxy10to50","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)

    genGdMu_L1Mu_dR_fid_barrel = TH1F("genGdMu_L1Mu_dR_fid_barrel","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy0to0p1_barrel = TH1F("genGdMu_L1Mu_dR_fid_dxy0to0p1_barrel","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy1to5_barrel = TH1F("genGdMu_L1Mu_dR_fid_dxy1to5_barrel","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy5to10_barrel = TH1F("genGdMu_L1Mu_dR_fid_dxy5to10_barrel","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy10to50_barrel = TH1F("genGdMu_L1Mu_dR_fid_dxy10to50_barrel","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)

    genGdMu_L1Mu_dR_fid_overlap = TH1F("genGdMu_L1Mu_dR_fid_overlap","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy0to0p1_overlap = TH1F("genGdMu_L1Mu_dR_fid_dxy0to0p1_overlap","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy1to5_overlap = TH1F("genGdMu_L1Mu_dR_fid_dxy1to5_overlap","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy5to10_overlap = TH1F("genGdMu_L1Mu_dR_fid_dxy5to10_overlap","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy10to50_overlap = TH1F("genGdMu_L1Mu_dR_fid_dxy10to50_overlap","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)

    genGdMu_L1Mu_dR_fid_endcap = TH1F("genGdMu_L1Mu_dR_fid_endcap","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap = TH1F("genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy1to5_endcap = TH1F("genGdMu_L1Mu_dR_fid_dxy1to5_endcap","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy5to10_endcap = TH1F("genGdMu_L1Mu_dR_fid_dxy5to10_endcap","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy10to50_endcap = TH1F("genGdMu_L1Mu_dR_fid_dxy10to50_endcap","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)

    genGdMu_L1Mu_dR_fid_endcap_12_14 = TH1F("genGdMu_L1Mu_dR_fid_endcap_12_14","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_12_14 = TH1F("genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_12_14","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy1to5_endcap_12_14 = TH1F("genGdMu_L1Mu_dR_fid_dxy1to5_endcap_12_14","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy5to10_endcap_12_14 = TH1F("genGdMu_L1Mu_dR_fid_dxy5to10_endcap_12_14","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy10to50_endcap_12_14 = TH1F("genGdMu_L1Mu_dR_fid_dxy10to50_endcap_12_14","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)

    genGdMu_L1Mu_dR_fid_endcap_14_16 = TH1F("genGdMu_L1Mu_dR_fid_endcap_14_16","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_14_16 = TH1F("genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_14_16","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy1to5_endcap_14_16 = TH1F("genGdMu_L1Mu_dR_fid_dxy1to5_endcap_14_16","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy5to10_endcap_14_16 = TH1F("genGdMu_L1Mu_dR_fid_dxy5to10_endcap_14_16","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy10to50_endcap_14_16 = TH1F("genGdMu_L1Mu_dR_fid_dxy10to50_endcap_14_16","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)

    genGdMu_L1Mu_dR_fid_endcap_16_18 = TH1F("genGdMu_L1Mu_dR_fid_endcap_16_18","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_16_18 = TH1F("genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_16_18","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy1to5_endcap_16_18 = TH1F("genGdMu_L1Mu_dR_fid_dxy1to5_endcap_16_18","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy5to10_endcap_16_18 = TH1F("genGdMu_L1Mu_dR_fid_dxy5to10_endcap_16_18","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy10to50_endcap_16_18 = TH1F("genGdMu_L1Mu_dR_fid_dxy10to50_endcap_16_18","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)

    genGdMu_L1Mu_dR_fid_endcap_18_20 = TH1F("genGdMu_L1Mu_dR_fid_endcap_18_20","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_18_20 = TH1F("genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_18_20","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy1to5_endcap_18_20 = TH1F("genGdMu_L1Mu_dR_fid_dxy1to5_endcap_18_20","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy5to10_endcap_18_20 = TH1F("genGdMu_L1Mu_dR_fid_dxy5to10_endcap_18_20","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy10to50_endcap_18_20 = TH1F("genGdMu_L1Mu_dR_fid_dxy10to50_endcap_18_20","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)

    genGdMu_L1Mu_dR_fid_endcap_20_22 = TH1F("genGdMu_L1Mu_dR_fid_endcap_20_22","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_20_22 = TH1F("genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_20_22","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy1to5_endcap_20_22 = TH1F("genGdMu_L1Mu_dR_fid_dxy1to5_endcap_20_22","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy5to10_endcap_20_22 = TH1F("genGdMu_L1Mu_dR_fid_dxy5to10_endcap_20_22","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy10to50_endcap_20_22 = TH1F("genGdMu_L1Mu_dR_fid_dxy10to50_endcap_20_22","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)

    genGdMu_L1Mu_dR_fid_endcap_22_24 = TH1F("genGdMu_L1Mu_dR_fid_endcap_22_24","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_22_24 = TH1F("genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_22_24","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy1to5_endcap_22_24 = TH1F("genGdMu_L1Mu_dR_fid_dxy1to5_endcap_22_24","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy5to10_endcap_22_24 = TH1F("genGdMu_L1Mu_dR_fid_dxy5to10_endcap_22_24","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy10to50_endcap_22_24 = TH1F("genGdMu_L1Mu_dR_fid_dxy10to50_endcap_22_24","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)

    L1Mu_L1Tk_dR_fid = TH1F("L1Mu_L1Tk_dR_fid","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy0to0p1 = TH1F("L1Mu_L1Tk_dR_fid_dxy0to0p1","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy0to1 = TH1F("L1Mu_L1Tk_dR_fid_dxy0to1","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy1to5 = TH1F("L1Mu_L1Tk_dR_fid_dxy1to5","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy5to10 = TH1F("L1Mu_L1Tk_dR_fid_dxy5to10","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy10to50 = TH1F("L1Mu_L1Tk_dR_fid_dxy10to50","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)

    L1Mu_L1Tk_dR_fid_barrel = TH1F("L1Mu_L1Tk_dR_fid_barrel","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy0to0p1_barrel = TH1F("L1Mu_L1Tk_dR_fid_dxy0to0p1_barrel","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy0to1_barrel = TH1F("L1Mu_L1Tk_dR_fid_dxy0to1_barrel","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy1to5_barrel = TH1F("L1Mu_L1Tk_dR_fid_dxy1to5_barrel","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy5to10_barrel = TH1F("L1Mu_L1Tk_dR_fid_dxy5to10_barrel","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy10to50_barrel = TH1F("L1Mu_L1Tk_dR_fid_dxy10to50_barrel","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)

    L1Mu_L1Tk_dR_fid_overlap = TH1F("L1Mu_L1Tk_dR_fid_overlap","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy0to0p1_overlap = TH1F("L1Mu_L1Tk_dR_fid_dxy0to0p1_overlap","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy0to1_overlap = TH1F("L1Mu_L1Tk_dR_fid_dxy0to1_overlap","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy1to5_overlap = TH1F("L1Mu_L1Tk_dR_fid_dxy1to5_overlap","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy5to10_overlap = TH1F("L1Mu_L1Tk_dR_fid_dxy5to10_overlap","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy10to50_overlap = TH1F("L1Mu_L1Tk_dR_fid_dxy10to50_overlap","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)

    L1Mu_L1Tk_dR_fid_endcap = TH1F("L1Mu_L1Tk_dR_fid_endcap","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap = TH1F("L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy0to1_endcap = TH1F("L1Mu_L1Tk_dR_fid_dxy0to1_endcap","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy1to5_endcap = TH1F("L1Mu_L1Tk_dR_fid_dxy1to5_endcap","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy5to10_endcap = TH1F("L1Mu_L1Tk_dR_fid_dxy5to10_endcap","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy10to50_endcap = TH1F("L1Mu_L1Tk_dR_fid_dxy10to50_endcap","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)

    L1Mu_L1Tk_dR_fid_endcap_12_14 = TH1F("L1Mu_L1Tk_dR_fid_endcap_12_14","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_12_14 = TH1F("L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_12_14","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy0to1_endcap_12_14 = TH1F("L1Mu_L1Tk_dR_fid_dxy0to1_endcap_12_14","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy1to5_endcap_12_14 = TH1F("L1Mu_L1Tk_dR_fid_dxy1to5_endcap_12_14","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy5to10_endcap_12_14 = TH1F("L1Mu_L1Tk_dR_fid_dxy5to10_endcap_12_14","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy10to50_endcap_12_14 = TH1F("L1Mu_L1Tk_dR_fid_dxy10to50_endcap_12_14","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)

    L1Mu_L1Tk_dR_fid_endcap_14_16 = TH1F("L1Mu_L1Tk_dR_fid_endcap_14_16","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_14_16 = TH1F("L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_14_16","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy0to1_endcap_14_16 = TH1F("L1Mu_L1Tk_dR_fid_dxy0to1_endcap_14_16","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy1to5_endcap_14_16 = TH1F("L1Mu_L1Tk_dR_fid_dxy1to5_endcap_14_16","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy5to10_endcap_14_16 = TH1F("L1Mu_L1Tk_dR_fid_dxy5to10_endcap_14_16","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy10to50_endcap_14_16 = TH1F("L1Mu_L1Tk_dR_fid_dxy10to50_endcap_14_16","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)

    L1Mu_L1Tk_dR_fid_endcap_16_18 = TH1F("L1Mu_L1Tk_dR_fid_endcap_16_18","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_16_18 = TH1F("L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_16_18","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy0to1_endcap_16_18 = TH1F("L1Mu_L1Tk_dR_fid_dxy0to1_endcap_16_18","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy1to5_endcap_16_18 = TH1F("L1Mu_L1Tk_dR_fid_dxy1to5_endcap_16_18","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy5to10_endcap_16_18 = TH1F("L1Mu_L1Tk_dR_fid_dxy5to10_endcap_16_18","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy10to50_endcap_16_18 = TH1F("L1Mu_L1Tk_dR_fid_dxy10to50_endcap_16_18","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)

    L1Mu_L1Tk_dR_fid_endcap_18_20 = TH1F("L1Mu_L1Tk_dR_fid_endcap_18_20","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_18_20 = TH1F("L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_18_20","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy0to1_endcap_18_20 = TH1F("L1Mu_L1Tk_dR_fid_dxy0to1_endcap_18_20","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy1to5_endcap_18_20 = TH1F("L1Mu_L1Tk_dR_fid_dxy1to5_endcap_18_20","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy5to10_endcap_18_20 = TH1F("L1Mu_L1Tk_dR_fid_dxy5to10_endcap_18_20","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy10to50_endcap_18_20 = TH1F("L1Mu_L1Tk_dR_fid_dxy10to50_endcap_18_20","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)

    L1Mu_L1Tk_dR_fid_endcap_20_22 = TH1F("L1Mu_L1Tk_dR_fid_endcap_20_22","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_20_22 = TH1F("L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_20_22","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy0to1_endcap_20_22 = TH1F("L1Mu_L1Tk_dR_fid_dxy0to1_endcap_20_22","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy1to5_endcap_20_22 = TH1F("L1Mu_L1Tk_dR_fid_dxy1to5_endcap_20_22","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy5to10_endcap_20_22 = TH1F("L1Mu_L1Tk_dR_fid_dxy5to10_endcap_20_22","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy10to50_endcap_20_22 = TH1F("L1Mu_L1Tk_dR_fid_dxy10to50_endcap_20_22","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)

    L1Mu_L1Tk_dR_fid_endcap_22_24 = TH1F("L1Mu_L1Tk_dR_fid_endcap_22_24","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_22_24 = TH1F("L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_22_24","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy0to1_endcap_22_24 = TH1F("L1Mu_L1Tk_dR_fid_dxy0to1_endcap_22_24","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy1to5_endcap_22_24 = TH1F("L1Mu_L1Tk_dR_fid_dxy1to5_endcap_22_24","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy5to10_endcap_22_24 = TH1F("L1Mu_L1Tk_dR_fid_dxy5to10_endcap_22_24","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy10to50_endcap_22_24 = TH1F("L1Mu_L1Tk_dR_fid_dxy10to50_endcap_22_24","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)

    L1Mu_L1Tk_dR_fid_dxy1to50 = TH1F("L1Mu_L1Tk_dR_fid_dxy1to50","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy1to50_barrel = TH1F("L1Mu_L1Tk_dR_fid_dxy1to50_barrel","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy1to50_overlap = TH1F("L1Mu_L1Tk_dR_fid_dxy1to50_overlap","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy1to50_endcap = TH1F("L1Mu_L1Tk_dR_fid_dxy1to50_endcap","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy1to50_endcap_12_14 = TH1F("L1Mu_L1Tk_dR_fid_dxy1to50_endcap_12_14","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy1to50_endcap_14_16 = TH1F("L1Mu_L1Tk_dR_fid_dxy1to50_endcap_14_16","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy1to50_endcap_16_18 = TH1F("L1Mu_L1Tk_dR_fid_dxy1to50_endcap_16_18","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy1to50_endcap_18_20 = TH1F("L1Mu_L1Tk_dR_fid_dxy1to50_endcap_18_20","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy1to50_endcap_20_22 = TH1F("L1Mu_L1Tk_dR_fid_dxy1to50_endcap_20_22","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy1to50_endcap_22_24 = TH1F("L1Mu_L1Tk_dR_fid_dxy1to50_endcap_22_24","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)

    L1Mu_L1Tk_dR_fid_barrel_pt2 = TH1F("L1Mu_L1Tk_dR_fid_barrel_pt2","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy0to0p1_barrel_pt2 = TH1F("L1Mu_L1Tk_dR_fid_dxy0to0p1_barrel_pt2","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy1to5_barrel_pt2 = TH1F("L1Mu_L1Tk_dR_fid_dxy1to5_barrel_pt2","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy5to10_barrel_pt2 = TH1F("L1Mu_L1Tk_dR_fid_dxy5to10_barrel_pt2","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy10to50_barrel_pt2 = TH1F("L1Mu_L1Tk_dR_fid_dxy10to50_barrel_pt2","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)

    L1Mu_L1Tk_dR_fid_overlap_pt2 = TH1F("L1Mu_L1Tk_dR_fid_overlap_pt2","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy0to0p1_overlap_pt2 = TH1F("L1Mu_L1Tk_dR_fid_dxy0to0p1_overlap_pt2","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy1to5_overlap_pt2 = TH1F("L1Mu_L1Tk_dR_fid_dxy1to5_overlap_pt2","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy5to10_overlap_pt2 = TH1F("L1Mu_L1Tk_dR_fid_dxy5to10_overlap_pt2","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy10to50_overlap_pt2 = TH1F("L1Mu_L1Tk_dR_fid_dxy10to50_overlap_pt2","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)

    L1Mu_L1Tk_dR_fid_endcap_pt2 = TH1F("L1Mu_L1Tk_dR_fid_endcap_pt2","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_pt2 = TH1F("L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_pt2","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy1to5_endcap_pt2 = TH1F("L1Mu_L1Tk_dR_fid_dxy1to5_endcap_pt2","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy5to10_endcap_pt2 = TH1F("L1Mu_L1Tk_dR_fid_dxy5to10_endcap_pt2","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy10to50_endcap_pt2 = TH1F("L1Mu_L1Tk_dR_fid_dxy10to50_endcap_pt2","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)


    L1Mu_L1Tk_dR_true_fid = TH1F("L1Mu_L1Tk_dR_true_fid","dR(real L1Mu,true L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_true_fid_dxy0to0p1 = TH1F("L1Mu_L1Tk_dR_true_fid_dxy0to0p1","dR(real L1Mu,true L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_true_fid_dxy1to5 = TH1F("L1Mu_L1Tk_dR_true_fid_dxy1to5","dR(real L1Mu,true L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_true_fid_dxy5to10 = TH1F("L1Mu_L1Tk_dR_true_fid_dxy5to10","dR(real L1Mu,true L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_true_fid_dxy10to50 = TH1F("L1Mu_L1Tk_dR_true_fid_dxy10to50","dR(real L1Mu,true L1Tk);dR; Entries", 100,0.,1.)

    ## pt plots
    L1Mu_L1Tk_pt_fid = TH1F("L1Mu_L1Tk_pt_fid","L1Tk p_{T};GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy0to0p1 = TH1F("L1Mu_L1Tk_pt_fid_dxy0to0p1","L1Tk p_{T};GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy0to1 = TH1F("L1Mu_L1Tk_pt_fid_dxy0to1","L1Tk p_{T};GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy1to5 = TH1F("L1Mu_L1Tk_pt_fid_dxy1to5","L1Tk p_{T};GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy5to10 = TH1F("L1Mu_L1Tk_pt_fid_dxy5to10","L1Tk p_{T};GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy10to50 = TH1F("L1Mu_L1Tk_pt_fid_dxy10to50","L1Tk p_{T};GeV; Entries", 50,0.,50.)

    L1Mu_L1Tk_pt_fid_barrel = TH1F("L1Mu_L1Tk_pt_fid_barrel","L1Tk p_{T} barrel;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy0to0p1_barrel = TH1F("L1Mu_L1Tk_pt_fid_dxy0to0p1_barrel","L1Tk p_{T} barrel;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy0to1_barrel = TH1F("L1Mu_L1Tk_pt_fid_dxy0to1_barrel","L1Tk p_{T} barrel;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy1to5_barrel = TH1F("L1Mu_L1Tk_pt_fid_dxy1to5_barrel","L1Tk p_{T} barrel;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy5to10_barrel = TH1F("L1Mu_L1Tk_pt_fid_dxy5to10_barrel","L1Tk p_{T} barrel;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy10to50_barrel = TH1F("L1Mu_L1Tk_pt_fid_dxy10to50_barrel","L1Tk p_{T} barrel;GeV; Entries", 50,0.,50.)

    L1Mu_L1Tk_pt_fid_overlap = TH1F("L1Mu_L1Tk_pt_fid_overlap","L1Tk p_{T} overlap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy0to0p1_overlap = TH1F("L1Mu_L1Tk_pt_fid_dxy0to0p1_overlap","L1Tk p_{T} overlap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy0to1_overlap = TH1F("L1Mu_L1Tk_pt_fid_dxy0to1_overlap","L1Tk p_{T} overlap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy1to5_overlap = TH1F("L1Mu_L1Tk_pt_fid_dxy1to5_overlap","L1Tk p_{T} overlap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy5to10_overlap = TH1F("L1Mu_L1Tk_pt_fid_dxy5to10_overlap","L1Tk p_{T} overlap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy10to50_overlap = TH1F("L1Mu_L1Tk_pt_fid_dxy10to50_overlap","L1Tk p_{T} overlap;GeV; Entries", 50,0.,50.)

    L1Mu_L1Tk_pt_fid_endcap = TH1F("L1Mu_L1Tk_pt_fid_endcap","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap = TH1F("L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy0to1_endcap = TH1F("L1Mu_L1Tk_pt_fid_dxy0to1_endcap","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy1to5_endcap = TH1F("L1Mu_L1Tk_pt_fid_dxy1to5_endcap","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy5to10_endcap = TH1F("L1Mu_L1Tk_pt_fid_dxy5to10_endcap","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy10to50_endcap = TH1F("L1Mu_L1Tk_pt_fid_dxy10to50_endcap","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)

    L1Mu_L1Tk_pt_fid_endcap_12_14 = TH1F("L1Mu_L1Tk_pt_fid_endcap_12_14","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_12_14 = TH1F("L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_12_14","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy0to1_endcap_12_14 = TH1F("L1Mu_L1Tk_pt_fid_dxy0to1_endcap_12_14","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy1to5_endcap_12_14 = TH1F("L1Mu_L1Tk_pt_fid_dxy1to5_endcap_12_14","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy5to10_endcap_12_14 = TH1F("L1Mu_L1Tk_pt_fid_dxy5to10_endcap_12_14","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy10to50_endcap_12_14 = TH1F("L1Mu_L1Tk_pt_fid_dxy10to50_endcap_12_14","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)

    L1Mu_L1Tk_pt_fid_endcap_14_16 = TH1F("L1Mu_L1Tk_pt_fid_endcap_14_16","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_14_16 = TH1F("L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_14_16","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy0to1_endcap_14_16 = TH1F("L1Mu_L1Tk_pt_fid_dxy0to1_endcap_14_16","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy1to5_endcap_14_16 = TH1F("L1Mu_L1Tk_pt_fid_dxy1to5_endcap_14_16","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy5to10_endcap_14_16 = TH1F("L1Mu_L1Tk_pt_fid_dxy5to10_endcap_14_16","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy10to50_endcap_14_16 = TH1F("L1Mu_L1Tk_pt_fid_dxy10to50_endcap_14_16","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)

    L1Mu_L1Tk_pt_fid_endcap_16_18 = TH1F("L1Mu_L1Tk_pt_fid_endcap_16_18","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_16_18 = TH1F("L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_16_18","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy0to1_endcap_16_18 = TH1F("L1Mu_L1Tk_pt_fid_dxy0to1_endcap_16_18","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy1to5_endcap_16_18 = TH1F("L1Mu_L1Tk_pt_fid_dxy1to5_endcap_16_18","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy5to10_endcap_16_18 = TH1F("L1Mu_L1Tk_pt_fid_dxy5to10_endcap_16_18","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy10to50_endcap_16_18 = TH1F("L1Mu_L1Tk_pt_fid_dxy10to50_endcap_16_18","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)

    L1Mu_L1Tk_pt_fid_endcap_18_20 = TH1F("L1Mu_L1Tk_pt_fid_endcap_18_20","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_18_20 = TH1F("L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_18_20","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy0to1_endcap_18_20 = TH1F("L1Mu_L1Tk_pt_fid_dxy0to1_endcap_18_20","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy1to5_endcap_18_20 = TH1F("L1Mu_L1Tk_pt_fid_dxy1to5_endcap_18_20","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy5to10_endcap_18_20 = TH1F("L1Mu_L1Tk_pt_fid_dxy5to10_endcap_18_20","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy10to50_endcap_18_20 = TH1F("L1Mu_L1Tk_pt_fid_dxy10to50_endcap_18_20","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)

    L1Mu_L1Tk_pt_fid_endcap_20_22 = TH1F("L1Mu_L1Tk_pt_fid_endcap_20_22","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_20_22 = TH1F("L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_20_22","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy0to1_endcap_20_22 = TH1F("L1Mu_L1Tk_pt_fid_dxy0to1_endcap_20_22","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy1to5_endcap_20_22 = TH1F("L1Mu_L1Tk_pt_fid_dxy1to5_endcap_20_22","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy5to10_endcap_20_22 = TH1F("L1Mu_L1Tk_pt_fid_dxy5to10_endcap_20_22","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy10to50_endcap_20_22 = TH1F("L1Mu_L1Tk_pt_fid_dxy10to50_endcap_20_22","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)

    L1Mu_L1Tk_pt_fid_endcap_22_24 = TH1F("L1Mu_L1Tk_pt_fid_endcap_22_24","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_22_24 = TH1F("L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_22_24","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy0to1_endcap_22_24 = TH1F("L1Mu_L1Tk_pt_fid_dxy0to1_endcap_22_24","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy1to5_endcap_22_24 = TH1F("L1Mu_L1Tk_pt_fid_dxy1to5_endcap_22_24","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy5to10_endcap_22_24 = TH1F("L1Mu_L1Tk_pt_fid_dxy5to10_endcap_22_24","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy10to50_endcap_22_24 = TH1F("L1Mu_L1Tk_pt_fid_dxy10to50_endcap_22_24","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)

    L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_barrel = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_barrel","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_overlap = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_overlap","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_12_14 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_12_14","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_14_16 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_14_16","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_16_18 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_16_18","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_18_20 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_18_20","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_20_22 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_20_22","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_22_24 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_22_24","", 100,0.,1.,50,0.,50.)

    L1Mu_L1Tk_dRvspt_fid_dxy1to5_barrel = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy1to5_barrel","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy1to5_overlap = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy1to5_overlap","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_12_14 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_12_14","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_14_16 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_14_16","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_16_18 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_16_18","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_18_20 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_18_20","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_20_22 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_20_22","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_22_24 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_22_24","", 100,0.,1.,50,0.,50.)

    L1Mu_L1Tk_dRvspt_fid_dxy5to10_barrel = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy5to10_barrel","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy5to10_overlap = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy5to10_overlap","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_12_14 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_12_14","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_14_16 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_14_16","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_16_18 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_16_18","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_18_20 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_18_20","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_20_22 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_20_22","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_22_24 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_22_24","", 100,0.,1.,50,0.,50.)

    L1Mu_L1Tk_dRvspt_fid_dxy10to50_barrel = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy10to50_barrel","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy10to50_overlap = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy10to50_overlap","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_12_14 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_12_14","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_14_16 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_14_16","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_16_18 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_16_18","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_18_20 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_18_20","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_20_22 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_20_22","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_22_24 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_22_24","", 100,0.,1.,50,0.,50.)

    L1Mu_L1Tk_dRvspt_fid_dxy0to1_barrel = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy0to1_barrel","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy0to1_overlap = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy0to1_overlap","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_12_14 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_12_14","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_14_16 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_14_16","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_16_18 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_16_18","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_18_20 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_18_20","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_20_22 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_20_22","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_22_24 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_22_24","", 100,0.,1.,50,0.,50.)

    L1Mu_L1Tk_dRvspt_fid_dxy1to50_barrel = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy1to50_barrel","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy1to50_overlap = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy1to50_overlap","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_12_14 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_12_14","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_14_16 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_14_16","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_16_18 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_16_18","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_18_20 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_18_20","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_20_22 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_20_22","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_22_24 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_22_24","", 100,0.,1.,50,0.,50.)

    L1Mu_dxyvslxy_fid = TH2F("L1Mu_dxyvslxy_fid","; dxy [cm]; Lxy [cm]",100,0.01,100.,300,0.,300.)
    L1Mu_dxyvslxy_fid_endcap_22_24 = TH2F("L1Mu_dxyvslxy_fid_endcap_22_24","", 100,0.,1.,300,0.,300.)
    L1Mu_dxyvslxy_fid_endcap_22_24 = TH2F("L1Mu_dxyvslxy_fid_endcap_22_24","", 100,0.,1.,300,0.,300.)
    L1Mu_dxyvslxy_fid_endcap_22_24 = TH2F("L1Mu_dxyvslxy_fid_endcap_22_24","", 100,0.,1.,300,0.,300.)
    L1Mu_dxyvslxy_fid_endcap_22_24 = TH2F("L1Mu_dxyvslxy_fid_endcap_22_24","", 100,0.,1.,300,0.,300.)

    treeHits = ch

    for k in range(0,treeHits.GetEntries()):
      treeHits.GetEntry(k)
      if k%1000==0: print "Event", k, "nL1Mu", treeHits.nL1Mu

      for i in range(0,2):
        for j in range(0,2):
          ij = i*2+j
          
          pt = abs(treeHits.genGdMu_pt[ij])
          eta = treeHits.genGdMu_eta[ij]
          phi = abs(treeHits.genGdMu_phi[ij])
          eta_prop = treeHits.genGdMu_eta_prop[ij]
          phi_prop = treeHits.genGdMu_phi_prop[ij]
          dxy = abs(treeHits.genGdMu_dxy[ij])
          vz = abs(treeHits.genGd_vz[i])
          lxy =  abs(treeHits.genGd_lxy[i])

          ## exclude all the bad muons
          if (abs(treeHits.genGdMu_eta_prop[i*2+0])>2.4): 
            continue
          if (abs(treeHits.genGdMu_eta_prop[i*2+1])>2.4): 
            continue
          if (abs(treeHits.genGdMu_pt[i*2+0])<5): 
            continue
          if (abs(treeHits.genGdMu_pt[i*2+1])<5): 
            continue
          if (abs(treeHits.genGd0Gd1_dR) < 2):
            continue
          if (abs(treeHits.genGd_genMuMu_dR[i]) < 1):
            continue
          if treeHits.genGdMu_eta_prop[ij] == -99 or treeHits.genGdMu_phi_prop[ij] == -99:
            continue
          if lxy > 300:
            continue
          if vz > 500:
            continue

          L1Mu_index = treeHits.genGdMu_L1Mu_index_prop[ij]
          L1Mu_dR_prop = treeHits.genGdMu_L1Mu_dR_prop[ij]

          if L1Mu_index != 99:
            L1Mu_pt = treeHits.L1Mu_pt[L1Mu_index]
            L1Mu_eta = treeHits.L1Mu_eta[L1Mu_index]
            L1Mu_phi = treeHits.L1Mu_phi[L1Mu_index]
            L1Mu_bx = treeHits.L1Mu_bx[L1Mu_index]
            L1Mu_quality = treeHits.L1Mu_quality[L1Mu_index]
            L1Mu_L1Tk_dR_prop = treeHits.L1Mu_L1Tk_dR_prop[L1Mu_index]
            L1Mu_L1Tk_pt_prop = treeHits.L1Mu_L1Tk_pt_prop[L1Mu_index]
            L1Mu_L1Tk_dR_prop_true = treeHits.L1Mu_L1Tk_dR_prop_true[L1Mu_index]
            
            dxy_region1 = dxy<=0.1
            dxy_region5 = dxy<=1
            dxy_region2 = 1<dxy and dxy<=5
            dxy_region3 = 5<dxy and dxy<=10
            dxy_region4 = 10<dxy and dxy<=50
            dxy_region6 = 1<dxy and dxy<=50

            eta_all = abs(eta_prop)<=2.4 
            eta_barrel = abs(eta_prop)<0.9
            eta_overlap = abs(eta_prop)<=1.2 and abs(eta_prop)>0.9
            eta_endcap = abs(eta_prop)<=2.4 and abs(eta_prop)>1.2

            eta_region1 = abs(eta_prop)<=1.4 and abs(eta_prop)>1.2 
            eta_region2 = abs(eta_prop)<=1.6 and abs(eta_prop)>1.4
            eta_region3 = abs(eta_prop)<=1.8 and abs(eta_prop)>1.6
            eta_region4 = abs(eta_prop)<=2.0 and abs(eta_prop)>1.8
            eta_region5 = abs(eta_prop)<=2.2 and abs(eta_prop)>2.0
            eta_region6 = abs(eta_prop)<=2.4 and abs(eta_prop)>2.2

            L1Mu_dxyvslxy_fid.Fill(dxy, lxy)

            if eta_all: genGdMu_L1Mu_dR_fid.Fill(L1Mu_dR_prop)
            if dxy_region1 and eta_all: genGdMu_L1Mu_dR_fid_dxy0to0p1.Fill(L1Mu_dR_prop)
            if dxy_region2 and eta_all: genGdMu_L1Mu_dR_fid_dxy1to5.Fill(L1Mu_dR_prop)
            if dxy_region3 and eta_all: genGdMu_L1Mu_dR_fid_dxy5to10.Fill(L1Mu_dR_prop)
            if dxy_region4 and eta_all: genGdMu_L1Mu_dR_fid_dxy10to50.Fill(L1Mu_dR_prop)
            
            if eta_barrel: genGdMu_L1Mu_dR_fid_barrel.Fill(L1Mu_dR_prop)
            if dxy_region1 and eta_barrel: genGdMu_L1Mu_dR_fid_dxy0to0p1_barrel.Fill(L1Mu_dR_prop)
            if dxy_region2 and eta_barrel: genGdMu_L1Mu_dR_fid_dxy1to5_barrel.Fill(L1Mu_dR_prop)
            if dxy_region3 and eta_barrel: genGdMu_L1Mu_dR_fid_dxy5to10_barrel.Fill(L1Mu_dR_prop)
            if dxy_region4 and eta_barrel: genGdMu_L1Mu_dR_fid_dxy10to50_barrel.Fill(L1Mu_dR_prop)

            if eta_overlap: genGdMu_L1Mu_dR_fid_overlap.Fill(L1Mu_dR_prop)
            if dxy_region1 and eta_overlap: genGdMu_L1Mu_dR_fid_dxy0to0p1_overlap.Fill(L1Mu_dR_prop)
            if dxy_region2 and eta_overlap: genGdMu_L1Mu_dR_fid_dxy1to5_overlap.Fill(L1Mu_dR_prop)
            if dxy_region3 and eta_overlap: genGdMu_L1Mu_dR_fid_dxy5to10_overlap.Fill(L1Mu_dR_prop)
            if dxy_region4 and eta_overlap: genGdMu_L1Mu_dR_fid_dxy10to50_overlap.Fill(L1Mu_dR_prop)

            if eta_endcap: genGdMu_L1Mu_dR_fid_endcap.Fill(L1Mu_dR_prop)
            if dxy_region1 and eta_endcap: genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap.Fill(L1Mu_dR_prop)
            if dxy_region2 and eta_endcap: genGdMu_L1Mu_dR_fid_dxy1to5_endcap.Fill(L1Mu_dR_prop)
            if dxy_region3 and eta_endcap: genGdMu_L1Mu_dR_fid_dxy5to10_endcap.Fill(L1Mu_dR_prop)
            if dxy_region4 and eta_endcap: genGdMu_L1Mu_dR_fid_dxy10to50_endcap.Fill(L1Mu_dR_prop)

            if eta_region1: genGdMu_L1Mu_dR_fid_endcap_12_14.Fill(L1Mu_dR_prop)
            if dxy_region1 and eta_region1: genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_12_14.Fill(L1Mu_dR_prop)
            if dxy_region2 and eta_region1: genGdMu_L1Mu_dR_fid_dxy1to5_endcap_12_14.Fill(L1Mu_dR_prop)
            if dxy_region3 and eta_region1: genGdMu_L1Mu_dR_fid_dxy5to10_endcap_12_14.Fill(L1Mu_dR_prop)
            if dxy_region4 and eta_region1: genGdMu_L1Mu_dR_fid_dxy10to50_endcap_12_14.Fill(L1Mu_dR_prop)

            if eta_region2: genGdMu_L1Mu_dR_fid_endcap_14_16.Fill(L1Mu_dR_prop)
            if dxy_region1 and eta_region2: genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_14_16.Fill(L1Mu_dR_prop)
            if dxy_region2 and eta_region2: genGdMu_L1Mu_dR_fid_dxy1to5_endcap_14_16.Fill(L1Mu_dR_prop)
            if dxy_region3 and eta_region2: genGdMu_L1Mu_dR_fid_dxy5to10_endcap_14_16.Fill(L1Mu_dR_prop)
            if dxy_region4 and eta_region2: genGdMu_L1Mu_dR_fid_dxy10to50_endcap_14_16.Fill(L1Mu_dR_prop)

            if eta_region3: genGdMu_L1Mu_dR_fid_endcap_16_18.Fill(L1Mu_dR_prop)
            if dxy_region1 and eta_region3: genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_16_18.Fill(L1Mu_dR_prop)
            if dxy_region2 and eta_region3: genGdMu_L1Mu_dR_fid_dxy1to5_endcap_16_18.Fill(L1Mu_dR_prop)
            if dxy_region3 and eta_region3: genGdMu_L1Mu_dR_fid_dxy5to10_endcap_16_18.Fill(L1Mu_dR_prop)
            if dxy_region4 and eta_region3: genGdMu_L1Mu_dR_fid_dxy10to50_endcap_16_18.Fill(L1Mu_dR_prop)

            if eta_region4: genGdMu_L1Mu_dR_fid_endcap_18_20.Fill(L1Mu_dR_prop)
            if dxy_region1 and eta_region4: genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_18_20.Fill(L1Mu_dR_prop)
            if dxy_region2 and eta_region4: genGdMu_L1Mu_dR_fid_dxy1to5_endcap_18_20.Fill(L1Mu_dR_prop)
            if dxy_region3 and eta_region4: genGdMu_L1Mu_dR_fid_dxy5to10_endcap_18_20.Fill(L1Mu_dR_prop)
            if dxy_region4 and eta_region4: genGdMu_L1Mu_dR_fid_dxy10to50_endcap_18_20.Fill(L1Mu_dR_prop)

            if eta_region5: genGdMu_L1Mu_dR_fid_endcap_20_22.Fill(L1Mu_dR_prop)
            if dxy_region1 and eta_region5: genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_20_22.Fill(L1Mu_dR_prop)
            if dxy_region2 and eta_region5: genGdMu_L1Mu_dR_fid_dxy1to5_endcap_20_22.Fill(L1Mu_dR_prop)
            if dxy_region3 and eta_region5: genGdMu_L1Mu_dR_fid_dxy5to10_endcap_20_22.Fill(L1Mu_dR_prop)
            if dxy_region4 and eta_region5: genGdMu_L1Mu_dR_fid_dxy10to50_endcap_20_22.Fill(L1Mu_dR_prop)

            if eta_region6: genGdMu_L1Mu_dR_fid_endcap_22_24.Fill(L1Mu_dR_prop)
            if dxy_region1 and eta_region6: genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_22_24.Fill(L1Mu_dR_prop)
            if dxy_region2 and eta_region6: genGdMu_L1Mu_dR_fid_dxy1to5_endcap_22_24.Fill(L1Mu_dR_prop)
            if dxy_region3 and eta_region6: genGdMu_L1Mu_dR_fid_dxy5to10_endcap_22_24.Fill(L1Mu_dR_prop)
            if dxy_region4 and eta_region6: genGdMu_L1Mu_dR_fid_dxy10to50_endcap_22_24.Fill(L1Mu_dR_prop)

            good_L1Mu = L1Mu_quality>=4 and abs(L1Mu_bx)==0 and L1Mu_dR_prop<=0.2

            if good_L1Mu: 
              L1Mu_L1Tk_dR_fid.Fill(L1Mu_L1Tk_dR_prop)
              if eta_barrel: L1Mu_L1Tk_dR_fid_barrel.Fill(L1Mu_L1Tk_dR_prop)
              if eta_overlap: L1Mu_L1Tk_dR_fid_overlap.Fill(L1Mu_L1Tk_dR_prop)
              if eta_endcap: L1Mu_L1Tk_dR_fid_endcap.Fill(L1Mu_L1Tk_dR_prop)
              if eta_region1: L1Mu_L1Tk_dR_fid_endcap_12_14.Fill(L1Mu_L1Tk_dR_prop)
              if eta_region2: L1Mu_L1Tk_dR_fid_endcap_14_16.Fill(L1Mu_L1Tk_dR_prop)
              if eta_region3: L1Mu_L1Tk_dR_fid_endcap_16_18.Fill(L1Mu_L1Tk_dR_prop)
              if eta_region4: L1Mu_L1Tk_dR_fid_endcap_18_20.Fill(L1Mu_L1Tk_dR_prop)
              if eta_region5: L1Mu_L1Tk_dR_fid_endcap_20_22.Fill(L1Mu_L1Tk_dR_prop)
              if eta_region6: L1Mu_L1Tk_dR_fid_endcap_22_24.Fill(L1Mu_L1Tk_dR_prop)              



              if dxy_region1: 
                L1Mu_L1Tk_dR_fid_dxy0to0p1.Fill(L1Mu_L1Tk_dR_prop)
                if eta_barrel: L1Mu_L1Tk_dR_fid_dxy0to0p1_barrel.Fill(L1Mu_L1Tk_dR_prop)
                if eta_overlap: L1Mu_L1Tk_dR_fid_dxy0to0p1_overlap.Fill(L1Mu_L1Tk_dR_prop)
                if eta_endcap: L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region1: L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_12_14.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region2: L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_14_16.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region3: L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_16_18.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region4: L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_18_20.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region5: L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_20_22.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region6: L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_22_24.Fill(L1Mu_L1Tk_dR_prop)              

              if dxy_region5: 
                L1Mu_L1Tk_dR_fid_dxy0to1.Fill(L1Mu_L1Tk_dR_prop)
                if eta_barrel: L1Mu_L1Tk_dR_fid_dxy0to1_barrel.Fill(L1Mu_L1Tk_dR_prop)
                if eta_overlap: L1Mu_L1Tk_dR_fid_dxy0to1_overlap.Fill(L1Mu_L1Tk_dR_prop)
                if eta_endcap: L1Mu_L1Tk_dR_fid_dxy0to1_endcap.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region1: L1Mu_L1Tk_dR_fid_dxy0to1_endcap_12_14.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region2: L1Mu_L1Tk_dR_fid_dxy0to1_endcap_14_16.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region3: L1Mu_L1Tk_dR_fid_dxy0to1_endcap_16_18.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region4: L1Mu_L1Tk_dR_fid_dxy0to1_endcap_18_20.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region5: L1Mu_L1Tk_dR_fid_dxy0to1_endcap_20_22.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region6: L1Mu_L1Tk_dR_fid_dxy0to1_endcap_22_24.Fill(L1Mu_L1Tk_dR_prop)              
                
              if dxy_region2: 
                L1Mu_L1Tk_dR_fid_dxy1to5.Fill(L1Mu_L1Tk_dR_prop)
                if eta_barrel: L1Mu_L1Tk_dR_fid_dxy1to5_barrel.Fill(L1Mu_L1Tk_dR_prop)
                if eta_overlap: L1Mu_L1Tk_dR_fid_dxy1to5_overlap.Fill(L1Mu_L1Tk_dR_prop)
                if eta_endcap: L1Mu_L1Tk_dR_fid_dxy1to5_endcap.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region1: L1Mu_L1Tk_dR_fid_dxy1to5_endcap_12_14.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region2: L1Mu_L1Tk_dR_fid_dxy1to5_endcap_14_16.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region3: L1Mu_L1Tk_dR_fid_dxy1to5_endcap_16_18.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region4: L1Mu_L1Tk_dR_fid_dxy1to5_endcap_18_20.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region5: L1Mu_L1Tk_dR_fid_dxy1to5_endcap_20_22.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region6: L1Mu_L1Tk_dR_fid_dxy1to5_endcap_22_24.Fill(L1Mu_L1Tk_dR_prop)              

              if dxy_region3: 
                L1Mu_L1Tk_dR_fid_dxy5to10.Fill(L1Mu_L1Tk_dR_prop)
                if eta_barrel: L1Mu_L1Tk_dR_fid_dxy5to10_barrel.Fill(L1Mu_L1Tk_dR_prop)
                if eta_overlap: L1Mu_L1Tk_dR_fid_dxy5to10_overlap.Fill(L1Mu_L1Tk_dR_prop)
                if eta_endcap: L1Mu_L1Tk_dR_fid_dxy5to10_endcap.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region1: L1Mu_L1Tk_dR_fid_dxy5to10_endcap_12_14.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region2: L1Mu_L1Tk_dR_fid_dxy5to10_endcap_14_16.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region3: L1Mu_L1Tk_dR_fid_dxy5to10_endcap_16_18.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region4: L1Mu_L1Tk_dR_fid_dxy5to10_endcap_18_20.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region5: L1Mu_L1Tk_dR_fid_dxy5to10_endcap_20_22.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region6: L1Mu_L1Tk_dR_fid_dxy5to10_endcap_22_24.Fill(L1Mu_L1Tk_dR_prop)
              
              if dxy_region4: 
                L1Mu_L1Tk_dR_fid_dxy10to50.Fill(L1Mu_L1Tk_dR_prop)
                if eta_barrel: L1Mu_L1Tk_dR_fid_dxy10to50_barrel.Fill(L1Mu_L1Tk_dR_prop)
                if eta_overlap: L1Mu_L1Tk_dR_fid_dxy10to50_overlap.Fill(L1Mu_L1Tk_dR_prop)
                if eta_endcap: L1Mu_L1Tk_dR_fid_dxy10to50_endcap.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region1: L1Mu_L1Tk_dR_fid_dxy10to50_endcap_12_14.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region2: L1Mu_L1Tk_dR_fid_dxy10to50_endcap_14_16.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region3: L1Mu_L1Tk_dR_fid_dxy10to50_endcap_16_18.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region4: L1Mu_L1Tk_dR_fid_dxy10to50_endcap_18_20.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region5: L1Mu_L1Tk_dR_fid_dxy10to50_endcap_20_22.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region6: L1Mu_L1Tk_dR_fid_dxy10to50_endcap_22_24.Fill(L1Mu_L1Tk_dR_prop)              

              if dxy_region6: 
                L1Mu_L1Tk_dR_fid_dxy1to50.Fill(L1Mu_L1Tk_dR_prop)
                if eta_barrel: L1Mu_L1Tk_dR_fid_dxy1to50_barrel.Fill(L1Mu_L1Tk_dR_prop)
                if eta_overlap: L1Mu_L1Tk_dR_fid_dxy1to50_overlap.Fill(L1Mu_L1Tk_dR_prop)
                if eta_endcap:  L1Mu_L1Tk_dR_fid_dxy1to50_endcap.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region1: L1Mu_L1Tk_dR_fid_dxy1to50_endcap_12_14.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region2: L1Mu_L1Tk_dR_fid_dxy1to50_endcap_14_16.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region3: L1Mu_L1Tk_dR_fid_dxy1to50_endcap_16_18.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region4: L1Mu_L1Tk_dR_fid_dxy1to50_endcap_18_20.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region5: L1Mu_L1Tk_dR_fid_dxy1to50_endcap_20_22.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region6: L1Mu_L1Tk_dR_fid_dxy1to50_endcap_22_24.Fill(L1Mu_L1Tk_dR_prop)              

              L1Mu_L1Tk_pt_fid.Fill(L1Mu_L1Tk_pt_prop)
              if eta_barrel: L1Mu_L1Tk_pt_fid_barrel.Fill(L1Mu_L1Tk_pt_prop)
              if eta_overlap: L1Mu_L1Tk_pt_fid_overlap.Fill(L1Mu_L1Tk_pt_prop)
              if eta_endcap: L1Mu_L1Tk_pt_fid_endcap.Fill(L1Mu_L1Tk_pt_prop)
              if eta_region1: L1Mu_L1Tk_pt_fid_endcap_12_14.Fill(L1Mu_L1Tk_pt_prop)
              if eta_region2: L1Mu_L1Tk_pt_fid_endcap_14_16.Fill(L1Mu_L1Tk_pt_prop)
              if eta_region3: L1Mu_L1Tk_pt_fid_endcap_16_18.Fill(L1Mu_L1Tk_pt_prop)
              if eta_region4: L1Mu_L1Tk_pt_fid_endcap_18_20.Fill(L1Mu_L1Tk_pt_prop)
              if eta_region5: L1Mu_L1Tk_pt_fid_endcap_20_22.Fill(L1Mu_L1Tk_pt_prop)
              if eta_region6: L1Mu_L1Tk_pt_fid_endcap_22_24.Fill(L1Mu_L1Tk_pt_prop)              

              if dxy_region1: 
                L1Mu_L1Tk_pt_fid_dxy0to0p1.Fill(L1Mu_L1Tk_pt_prop)
                if eta_barrel: L1Mu_L1Tk_pt_fid_dxy0to0p1_barrel.Fill(L1Mu_L1Tk_pt_prop)
                if eta_overlap: L1Mu_L1Tk_pt_fid_dxy0to0p1_overlap.Fill(L1Mu_L1Tk_pt_prop)
                if eta_endcap: L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region1: L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_12_14.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region2: L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_14_16.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region3: L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_16_18.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region4: L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_18_20.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region5: L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_20_22.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region6: L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_22_24.Fill(L1Mu_L1Tk_pt_prop)              

              if dxy_region5: 
                L1Mu_L1Tk_pt_fid_dxy0to1.Fill(L1Mu_L1Tk_pt_prop)
                if eta_barrel: L1Mu_L1Tk_pt_fid_dxy0to1_barrel.Fill(L1Mu_L1Tk_pt_prop)
                if eta_overlap: L1Mu_L1Tk_pt_fid_dxy0to1_overlap.Fill(L1Mu_L1Tk_pt_prop)
                if eta_endcap: L1Mu_L1Tk_pt_fid_dxy0to1_endcap.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region1: L1Mu_L1Tk_pt_fid_dxy0to1_endcap_12_14.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region2: L1Mu_L1Tk_pt_fid_dxy0to1_endcap_14_16.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region3: L1Mu_L1Tk_pt_fid_dxy0to1_endcap_16_18.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region4: L1Mu_L1Tk_pt_fid_dxy0to1_endcap_18_20.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region5: L1Mu_L1Tk_pt_fid_dxy0to1_endcap_20_22.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region6: L1Mu_L1Tk_pt_fid_dxy0to1_endcap_22_24.Fill(L1Mu_L1Tk_pt_prop)              

              if dxy_region2: 
                L1Mu_L1Tk_pt_fid_dxy1to5.Fill(L1Mu_L1Tk_pt_prop)
                if eta_barrel: L1Mu_L1Tk_pt_fid_dxy1to5_barrel.Fill(L1Mu_L1Tk_pt_prop)
                if eta_overlap: L1Mu_L1Tk_pt_fid_dxy1to5_overlap.Fill(L1Mu_L1Tk_pt_prop)
                if eta_endcap: L1Mu_L1Tk_pt_fid_dxy1to5_endcap.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region1: L1Mu_L1Tk_pt_fid_dxy1to5_endcap_12_14.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region2: L1Mu_L1Tk_pt_fid_dxy1to5_endcap_14_16.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region3: L1Mu_L1Tk_pt_fid_dxy1to5_endcap_16_18.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region4: L1Mu_L1Tk_pt_fid_dxy1to5_endcap_18_20.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region5: L1Mu_L1Tk_pt_fid_dxy1to5_endcap_20_22.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region6: L1Mu_L1Tk_pt_fid_dxy1to5_endcap_22_24.Fill(L1Mu_L1Tk_pt_prop)              

              if dxy_region3: 
                L1Mu_L1Tk_pt_fid_dxy5to10.Fill(L1Mu_L1Tk_pt_prop)
                if eta_barrel: L1Mu_L1Tk_pt_fid_dxy5to10_barrel.Fill(L1Mu_L1Tk_pt_prop)
                if eta_overlap: L1Mu_L1Tk_pt_fid_dxy5to10_overlap.Fill(L1Mu_L1Tk_pt_prop)
                if eta_endcap: L1Mu_L1Tk_pt_fid_dxy5to10_endcap.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region1: L1Mu_L1Tk_pt_fid_dxy5to10_endcap_12_14.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region2: L1Mu_L1Tk_pt_fid_dxy5to10_endcap_14_16.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region3: L1Mu_L1Tk_pt_fid_dxy5to10_endcap_16_18.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region4: L1Mu_L1Tk_pt_fid_dxy5to10_endcap_18_20.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region5: L1Mu_L1Tk_pt_fid_dxy5to10_endcap_20_22.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region6: L1Mu_L1Tk_pt_fid_dxy5to10_endcap_22_24.Fill(L1Mu_L1Tk_pt_prop)              

              if dxy_region4: 
                L1Mu_L1Tk_pt_fid_dxy10to50.Fill(L1Mu_L1Tk_pt_prop)
                if eta_barrel: L1Mu_L1Tk_pt_fid_dxy10to50_barrel.Fill(L1Mu_L1Tk_pt_prop)
                if eta_overlap: L1Mu_L1Tk_pt_fid_dxy10to50_overlap.Fill(L1Mu_L1Tk_pt_prop)
                if eta_endcap: L1Mu_L1Tk_pt_fid_dxy10to50_endcap.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region1: L1Mu_L1Tk_pt_fid_dxy10to50_endcap_12_14.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region2: L1Mu_L1Tk_pt_fid_dxy10to50_endcap_14_16.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region3: L1Mu_L1Tk_pt_fid_dxy10to50_endcap_16_18.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region4: L1Mu_L1Tk_pt_fid_dxy10to50_endcap_18_20.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region5: L1Mu_L1Tk_pt_fid_dxy10to50_endcap_20_22.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region6: L1Mu_L1Tk_pt_fid_dxy10to50_endcap_22_24.Fill(L1Mu_L1Tk_pt_prop)              
                
              ### 2D plots
              if dxy_region1: 
                if eta_barrel: L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_barrel.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_overlap: L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_overlap.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region1: L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_12_14.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region2: L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_14_16.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region3: L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_16_18.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region4: L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_18_20.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region5: L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_20_22.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region6: L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_22_24.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
              if dxy_region2: 
                if eta_barrel: L1Mu_L1Tk_dRvspt_fid_dxy1to5_barrel.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_overlap: L1Mu_L1Tk_dRvspt_fid_dxy1to5_overlap.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region1: L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_12_14.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region2: L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_14_16.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region3: L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_16_18.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region4: L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_18_20.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region5: L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_20_22.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region6: L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_22_24.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
              if dxy_region3: 
                if eta_barrel: L1Mu_L1Tk_dRvspt_fid_dxy5to10_barrel.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_overlap: L1Mu_L1Tk_dRvspt_fid_dxy5to10_overlap.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region1: L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_12_14.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region2: L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_14_16.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region3: L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_16_18.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region4: L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_18_20.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region5: L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_20_22.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region6: L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_22_24.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
              if dxy_region4: 
                if eta_barrel: L1Mu_L1Tk_dRvspt_fid_dxy10to50_barrel.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_overlap: L1Mu_L1Tk_dRvspt_fid_dxy10to50_overlap.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region1: L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_12_14.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region2: L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_14_16.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region3: L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_16_18.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region4: L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_18_20.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region5: L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_20_22.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region6: L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_22_24.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)

              if dxy<=1:
                if eta_barrel: L1Mu_L1Tk_dRvspt_fid_dxy0to1_barrel.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_overlap: L1Mu_L1Tk_dRvspt_fid_dxy0to1_overlap.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region1: L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_12_14.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region2: L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_14_16.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region3: L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_16_18.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region4: L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_18_20.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region5: L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_20_22.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region6: L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_22_24.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)              
              if 1<dxy and dxy<=50:
                if eta_barrel: L1Mu_L1Tk_dRvspt_fid_dxy1to50_barrel.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_overlap: L1Mu_L1Tk_dRvspt_fid_dxy1to50_overlap.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region1: L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_12_14.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region2: L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_14_16.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region3: L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_16_18.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region4: L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_18_20.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region5: L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_20_22.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region6: L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_22_24.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)              

            extra_cuts = L1Mu_quality>=4 and abs(L1Mu_bx)==0
            if extra_cuts: L1Mu_L1Tk_dR_true_fid.Fill(L1Mu_L1Tk_dR_prop_true)
            if dxy_region1 and extra_cuts: L1Mu_L1Tk_dR_true_fid_dxy0to0p1.Fill(L1Mu_L1Tk_dR_prop_true)
            if dxy_region2 and extra_cuts: L1Mu_L1Tk_dR_true_fid_dxy1to5.Fill(L1Mu_L1Tk_dR_prop_true)
            if dxy_region3 and extra_cuts: L1Mu_L1Tk_dR_true_fid_dxy5to10.Fill(L1Mu_L1Tk_dR_prop_true)
            if dxy_region4 and extra_cuts: L1Mu_L1Tk_dR_true_fid_dxy10to50.Fill(L1Mu_L1Tk_dR_prop_true)

            
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid, "genGdMu_L1Mu_dR_fid")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy0to0p1, "genGdMu_L1Mu_dR_fid_dxy0to0p1")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy1to5, "genGdMu_L1Mu_dR_fid_dxy1to5")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy5to10, "genGdMu_L1Mu_dR_fid_dxy5to10")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy10to50, "genGdMu_L1Mu_dR_fid_dxy10to50")

    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_barrel, "genGdMu_L1Mu_dR_fid_barrel")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy0to0p1_barrel, "genGdMu_L1Mu_dR_fid_dxy0to0p1_barrel")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy1to5_barrel, "genGdMu_L1Mu_dR_fid_dxy1to5_barrel")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy5to10_barrel, "genGdMu_L1Mu_dR_fid_dxy5to10_barrel")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy10to50_barrel, "genGdMu_L1Mu_dR_fid_dxy10to50_barrel")

    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_overlap, "genGdMu_L1Mu_dR_fid_overlap")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy0to0p1_overlap, "genGdMu_L1Mu_dR_fid_dxy0to0p1_overlap")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy1to5_overlap, "genGdMu_L1Mu_dR_fid_dxy1to5_overlap")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy5to10_overlap, "genGdMu_L1Mu_dR_fid_dxy5to10_overlap")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy10to50_overlap, "genGdMu_L1Mu_dR_fid_dxy10to50_overlap")

    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_endcap, "genGdMu_L1Mu_dR_fid_endcap")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap, "genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy1to5_endcap, "genGdMu_L1Mu_dR_fid_dxy1to5_endcap")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy5to10_endcap, "genGdMu_L1Mu_dR_fid_dxy5to10_endcap")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy10to50_endcap, "genGdMu_L1Mu_dR_fid_dxy10to50_endcap")

    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_endcap_12_14, "genGdMu_L1Mu_dR_fid_endcap_12_14")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_12_14, "genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_12_14")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy1to5_endcap_12_14, "genGdMu_L1Mu_dR_fid_dxy1to5_endcap_12_14")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy5to10_endcap_12_14, "genGdMu_L1Mu_dR_fid_dxy5to10_endcap_12_14")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy10to50_endcap_12_14, "genGdMu_L1Mu_dR_fid_dxy10to50_endcap_12_14")

    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_endcap_14_16, "genGdMu_L1Mu_dR_fid_endcap_14_16")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_14_16, "genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_14_16")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy1to5_endcap_14_16, "genGdMu_L1Mu_dR_fid_dxy1to5_endcap_14_16")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy5to10_endcap_14_16, "genGdMu_L1Mu_dR_fid_dxy5to10_endcap_14_16")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy10to50_endcap_14_16, "genGdMu_L1Mu_dR_fid_dxy10to50_endcap_14_16")

    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_endcap_16_18, "genGdMu_L1Mu_dR_fid_endcap_16_18")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_16_18, "genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_16_18")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy1to5_endcap_16_18, "genGdMu_L1Mu_dR_fid_dxy1to5_endcap_16_18")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy5to10_endcap_16_18, "genGdMu_L1Mu_dR_fid_dxy5to10_endcap_16_18")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy10to50_endcap_16_18, "genGdMu_L1Mu_dR_fid_dxy10to50_endcap_16_18")

    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_endcap_18_20, "genGdMu_L1Mu_dR_fid_endcap_18_20")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_18_20, "genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_18_20")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy1to5_endcap_18_20, "genGdMu_L1Mu_dR_fid_dxy1to5_endcap_18_20")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy5to10_endcap_18_20, "genGdMu_L1Mu_dR_fid_dxy5to10_endcap_18_20")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy10to50_endcap_18_20, "genGdMu_L1Mu_dR_fid_dxy10to50_endcap_18_20")

    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_endcap_20_22, "genGdMu_L1Mu_dR_fid_endcap_20_22")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_20_22, "genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_20_22")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy1to5_endcap_20_22, "genGdMu_L1Mu_dR_fid_dxy1to5_endcap_20_22")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy5to10_endcap_20_22, "genGdMu_L1Mu_dR_fid_dxy5to10_endcap_20_22")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy10to50_endcap_20_22, "genGdMu_L1Mu_dR_fid_dxy10to50_endcap_20_22")

    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_endcap_22_24, "genGdMu_L1Mu_dR_fid_endcap_22_24")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_22_24, "genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_22_24")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy1to5_endcap_22_24, "genGdMu_L1Mu_dR_fid_dxy1to5_endcap_22_24")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy5to10_endcap_22_24, "genGdMu_L1Mu_dR_fid_dxy5to10_endcap_22_24")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy10to50_endcap_22_24, "genGdMu_L1Mu_dR_fid_dxy10to50_endcap_22_24")

    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid, "L1Mu_L1Tk_dR_fid")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy0to0p1, "L1Mu_L1Tk_dR_fid_dxy0to0p1")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy0to1, "L1Mu_L1Tk_dR_fid_dxy0to1")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy1to5, "L1Mu_L1Tk_dR_fid_dxy1to5")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy5to10, "L1Mu_L1Tk_dR_fid_dxy5to10")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy10to50, "L1Mu_L1Tk_dR_fid_dxy10to50")

    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_barrel, "L1Mu_L1Tk_dR_fid_barrel")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy0to0p1_barrel, "L1Mu_L1Tk_dR_fid_dxy0to0p1_barrel")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy0to1_barrel, "L1Mu_L1Tk_dR_fid_dxy0to1_barrel")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy1to5_barrel, "L1Mu_L1Tk_dR_fid_dxy1to5_barrel")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy5to10_barrel, "L1Mu_L1Tk_dR_fid_dxy5to10_barrel")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy10to50_barrel, "L1Mu_L1Tk_dR_fid_dxy10to50_barrel")

    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_overlap, "L1Mu_L1Tk_dR_fid_overlap")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy0to0p1_overlap, "L1Mu_L1Tk_dR_fid_dxy0to0p1_overlap")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy0to1_overlap, "L1Mu_L1Tk_dR_fid_dxy0to1_overlap")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy1to5_overlap, "L1Mu_L1Tk_dR_fid_dxy1to5_overlap")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy5to10_overlap, "L1Mu_L1Tk_dR_fid_dxy5to10_overlap")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy10to50_overlap, "L1Mu_L1Tk_dR_fid_dxy10to50_overlap")

    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_endcap, "L1Mu_L1Tk_dR_fid_endcap")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap, "L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy0to1_endcap, "L1Mu_L1Tk_dR_fid_dxy0to1_endcap")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy1to5_endcap, "L1Mu_L1Tk_dR_fid_dxy1to5_endcap")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy5to10_endcap, "L1Mu_L1Tk_dR_fid_dxy5to10_endcap")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy10to50_endcap, "L1Mu_L1Tk_dR_fid_dxy10to50_endcap")

    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_endcap_12_14, "L1Mu_L1Tk_dR_fid_endcap_12_14")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_12_14, "L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_12_14")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy0to1_endcap_12_14, "L1Mu_L1Tk_dR_fid_dxy0to1_endcap_12_14")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy1to5_endcap_12_14, "L1Mu_L1Tk_dR_fid_dxy1to5_endcap_12_14")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy5to10_endcap_12_14, "L1Mu_L1Tk_dR_fid_dxy5to10_endcap_12_14")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy10to50_endcap_12_14, "L1Mu_L1Tk_dR_fid_dxy10to50_endcap_12_14")

    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_endcap_14_16, "L1Mu_L1Tk_dR_fid_endcap_14_16")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_14_16, "L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_14_16")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy0to1_endcap_14_16, "L1Mu_L1Tk_dR_fid_dxy0to1_endcap_14_16")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy1to5_endcap_14_16, "L1Mu_L1Tk_dR_fid_dxy1to5_endcap_14_16")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy5to10_endcap_14_16, "L1Mu_L1Tk_dR_fid_dxy5to10_endcap_14_16")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy10to50_endcap_14_16, "L1Mu_L1Tk_dR_fid_dxy10to50_endcap_14_16")

    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_endcap_16_18, "L1Mu_L1Tk_dR_fid_endcap_16_18")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_16_18, "L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_16_18")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy0to1_endcap_16_18, "L1Mu_L1Tk_dR_fid_dxy0to1_endcap_16_18")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy1to5_endcap_16_18, "L1Mu_L1Tk_dR_fid_dxy1to5_endcap_16_18")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy5to10_endcap_16_18, "L1Mu_L1Tk_dR_fid_dxy5to10_endcap_16_18")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy10to50_endcap_16_18, "L1Mu_L1Tk_dR_fid_dxy10to50_endcap_16_18")

    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_endcap_18_20, "L1Mu_L1Tk_dR_fid_endcap_18_20")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_18_20, "L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_18_20")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy0to1_endcap_18_20, "L1Mu_L1Tk_dR_fid_dxy0to1_endcap_18_20")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy1to5_endcap_18_20, "L1Mu_L1Tk_dR_fid_dxy1to5_endcap_18_20")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy5to10_endcap_18_20, "L1Mu_L1Tk_dR_fid_dxy5to10_endcap_18_20")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy10to50_endcap_18_20, "L1Mu_L1Tk_dR_fid_dxy10to50_endcap_18_20")

    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_endcap_20_22, "L1Mu_L1Tk_dR_fid_endcap_20_22")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_20_22, "L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_20_22")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy0to1_endcap_20_22, "L1Mu_L1Tk_dR_fid_dxy0to1_endcap_20_22")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy1to5_endcap_20_22, "L1Mu_L1Tk_dR_fid_dxy1to5_endcap_20_22")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy5to10_endcap_20_22, "L1Mu_L1Tk_dR_fid_dxy5to10_endcap_20_22")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy10to50_endcap_20_22, "L1Mu_L1Tk_dR_fid_dxy10to50_endcap_20_22")

    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_endcap_22_24, "L1Mu_L1Tk_dR_fid_endcap_22_24")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_22_24, "L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_22_24")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy0to1_endcap_22_24, "L1Mu_L1Tk_dR_fid_dxy0to1_endcap_22_24")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy1to5_endcap_22_24, "L1Mu_L1Tk_dR_fid_dxy1to5_endcap_22_24")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy5to10_endcap_22_24, "L1Mu_L1Tk_dR_fid_dxy5to10_endcap_22_24")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy10to50_endcap_22_24, "L1Mu_L1Tk_dR_fid_dxy10to50_endcap_22_24")

    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy1to50,"L1Mu_L1Tk_dR_fid_dxy1to50")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy1to50_barrel,"L1Mu_L1Tk_dR_fid_dxy1to50_barrel")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy1to50_overlap,"L1Mu_L1Tk_dR_fid_dxy1to50_overlap")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy1to50_endcap,"L1Mu_L1Tk_dR_fid_dxy1to50_endcap")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy1to50_endcap_12_14,"L1Mu_L1Tk_dR_fid_dxy1to50_endcap_12_14")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy1to50_endcap_14_16,"L1Mu_L1Tk_dR_fid_dxy1to50_endcap_14_16")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy1to50_endcap_16_18,"L1Mu_L1Tk_dR_fid_dxy1to50_endcap_16_18")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy1to50_endcap_18_20,"L1Mu_L1Tk_dR_fid_dxy1to50_endcap_18_20")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy1to50_endcap_20_22,"L1Mu_L1Tk_dR_fid_dxy1to50_endcap_20_22")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy1to50_endcap_22_24,"L1Mu_L1Tk_dR_fid_dxy1to50_endcap_22_24")

    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_true_fid, "L1Mu_L1Tk_dR_true_fid")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_true_fid_dxy0to0p1, "L1Mu_L1Tk_dR_true_fid_dxy0to0p1")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_true_fid_dxy1to5, "L1Mu_L1Tk_dR_true_fid_dxy1to5")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_true_fid_dxy5to10, "L1Mu_L1Tk_dR_true_fid_dxy5to10")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_true_fid_dxy10to50, "L1Mu_L1Tk_dR_true_fid_dxy10to50")

    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid, "L1Mu_L1Tk_pt_fid")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy0to0p1, "L1Mu_L1Tk_pt_fid_dxy0to0p1")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy1to5, "L1Mu_L1Tk_pt_fid_dxy1to5")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy5to10, "L1Mu_L1Tk_pt_fid_dxy5to10")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy10to50, "L1Mu_L1Tk_pt_fid_dxy10to50")

    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_barrel, "L1Mu_L1Tk_pt_fid_barrel")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy0to0p1_barrel, "L1Mu_L1Tk_pt_fid_dxy0to0p1_barrel")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy1to5_barrel, "L1Mu_L1Tk_pt_fid_dxy1to5_barrel")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy5to10_barrel, "L1Mu_L1Tk_pt_fid_dxy5to10_barrel")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy10to50_barrel, "L1Mu_L1Tk_pt_fid_dxy10to50_barrel")

    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_overlap, "L1Mu_L1Tk_pt_fid_overlap")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy0to0p1_overlap, "L1Mu_L1Tk_pt_fid_dxy0to0p1_overlap")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy1to5_overlap, "L1Mu_L1Tk_pt_fid_dxy1to5_overlap")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy5to10_overlap, "L1Mu_L1Tk_pt_fid_dxy5to10_overlap")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy10to50_overlap, "L1Mu_L1Tk_pt_fid_dxy10to50_overlap")

    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_endcap, "L1Mu_L1Tk_pt_fid_endcap")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap, "L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy1to5_endcap, "L1Mu_L1Tk_pt_fid_dxy1to5_endcap")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy5to10_endcap, "L1Mu_L1Tk_pt_fid_dxy5to10_endcap")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy10to50_endcap, "L1Mu_L1Tk_pt_fid_dxy10to50_endcap")

    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_endcap_12_14, "L1Mu_L1Tk_pt_fid_endcap_12_14")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_12_14, "L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_12_14")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy0to1_endcap_12_14, "L1Mu_L1Tk_pt_fid_dxy0to1_endcap_12_14")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy1to5_endcap_12_14, "L1Mu_L1Tk_pt_fid_dxy1to5_endcap_12_14")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy5to10_endcap_12_14, "L1Mu_L1Tk_pt_fid_dxy5to10_endcap_12_14")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy10to50_endcap_12_14, "L1Mu_L1Tk_pt_fid_dxy10to50_endcap_12_14")

    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_endcap_14_16, "L1Mu_L1Tk_pt_fid_endcap_14_16")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_14_16, "L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_14_16")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy0to1_endcap_14_16, "L1Mu_L1Tk_pt_fid_dxy0to1_endcap_14_16")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy1to5_endcap_14_16, "L1Mu_L1Tk_pt_fid_dxy1to5_endcap_14_16")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy5to10_endcap_14_16, "L1Mu_L1Tk_pt_fid_dxy5to10_endcap_14_16")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy10to50_endcap_14_16, "L1Mu_L1Tk_pt_fid_dxy10to50_endcap_14_16")

    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_endcap_16_18, "L1Mu_L1Tk_pt_fid_endcap_16_18")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_16_18, "L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_16_18")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy0to1_endcap_16_18, "L1Mu_L1Tk_pt_fid_dxy0to1_endcap_16_18")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy1to5_endcap_16_18, "L1Mu_L1Tk_pt_fid_dxy1to5_endcap_16_18")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy5to10_endcap_16_18, "L1Mu_L1Tk_pt_fid_dxy5to10_endcap_16_18")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy10to50_endcap_16_18, "L1Mu_L1Tk_pt_fid_dxy10to50_endcap_16_18")

    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_endcap_18_20, "L1Mu_L1Tk_pt_fid_endcap_18_20")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_18_20, "L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_18_20")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy0to1_endcap_18_20, "L1Mu_L1Tk_pt_fid_dxy0to1_endcap_18_20")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy1to5_endcap_18_20, "L1Mu_L1Tk_pt_fid_dxy1to5_endcap_18_20")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy5to10_endcap_18_20, "L1Mu_L1Tk_pt_fid_dxy5to10_endcap_18_20")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy10to50_endcap_18_20, "L1Mu_L1Tk_pt_fid_dxy10to50_endcap_18_20")

    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_endcap_20_22, "L1Mu_L1Tk_pt_fid_endcap_20_22")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_20_22, "L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_20_22")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy0to1_endcap_20_22, "L1Mu_L1Tk_pt_fid_dxy0to1_endcap_20_22")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy1to5_endcap_20_22, "L1Mu_L1Tk_pt_fid_dxy1to5_endcap_20_22")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy5to10_endcap_20_22, "L1Mu_L1Tk_pt_fid_dxy5to10_endcap_20_22")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy10to50_endcap_20_22, "L1Mu_L1Tk_pt_fid_dxy10to50_endcap_20_22")

    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_endcap_22_24, "L1Mu_L1Tk_pt_fid_endcap_22_24")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_22_24, "L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_22_24")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy0to1_endcap_22_24, "L1Mu_L1Tk_pt_fid_dxy0to1_endcap_22_24")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy1to5_endcap_22_24, "L1Mu_L1Tk_pt_fid_dxy1to5_endcap_22_24")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy5to10_endcap_22_24, "L1Mu_L1Tk_pt_fid_dxy5to10_endcap_22_24")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy10to50_endcap_22_24, "L1Mu_L1Tk_pt_fid_dxy10to50_endcap_22_24")

    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_barrel, "L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_barrel")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_overlap, "L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_overlap")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_12_14, "L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_12_14")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_14_16, "L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_14_16")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_16_18, "L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_16_18")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_18_20, "L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_18_20")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_20_22, "L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_20_22")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_22_24, "L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_22_24")
                 
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy1to5_barrel, "L1Mu_L1Tk_dRvspt_fid_dxy1to5_barrel")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy1to5_overlap, "L1Mu_L1Tk_dRvspt_fid_dxy1to5_overlap")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_12_14, "L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_12_14")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_14_16, "L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_14_16")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_16_18, "L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_16_18")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_18_20, "L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_18_20")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_20_22, "L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_20_22")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_22_24, "L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_22_24")

    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy5to10_barrel, "L1Mu_L1Tk_dRvspt_fid_dxy5to10_barrel")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy5to10_overlap, "L1Mu_L1Tk_dRvspt_fid_dxy5to10_overlap")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_12_14, "L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_12_14")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_14_16, "L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_14_16")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_16_18, "L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_16_18")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_18_20, "L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_18_20")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_20_22, "L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_20_22")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_22_24, "L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_22_24")

    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy10to50_barrel, "L1Mu_L1Tk_dRvspt_fid_dxy10to50_barrel")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy10to50_overlap, "L1Mu_L1Tk_dRvspt_fid_dxy10to50_overlap")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_12_14, "L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_12_14")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_14_16, "L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_14_16")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_16_18, "L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_16_18")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_18_20, "L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_18_20")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_20_22, "L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_20_22")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_22_24, "L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_22_24")

    makeSimplePlot(thisTargetDir, L1Mu_dxyvslxy_fid, "L1Mu_dxyvslxy_fid", True)    

    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy1to50_barrel, "L1Mu_L1Tk_dRvspt_fid_dxy1to50_barrel")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy1to50_overlap, "L1Mu_L1Tk_dRvspt_fid_dxy1to50_overlap")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_12_14, "L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_12_14")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_14_16, "L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_14_16")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_16_18, "L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_16_18")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_18_20, "L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_18_20")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_20_22, "L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_20_22")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_22_24, "L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_22_24")

    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy0to1_barrel, "L1Mu_L1Tk_dRvspt_fid_dxy0to1_barrel")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy0to1_overlap, "L1Mu_L1Tk_dRvspt_fid_dxy0to1_overlap")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_12_14, "L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_12_14")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_14_16, "L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_14_16")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_16_18, "L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_16_18")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_18_20, "L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_18_20")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_20_22, "L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_20_22")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_22_24, "L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_22_24")



  if eff and False:
    makedRL1MuL1TkHistogram()

  #exit()

  def makeEfficiencyHistogram():

    h_single_L1Mu_efficiency_L1Tk_pt0 = TH1F("h_single_L1Mu_efficiency_L1Tk_pt0"," ", 1000, 0, 20)
    h_single_L1Mu_efficiency_L1Tk_pt2 = TH1F("h_single_L1Mu_efficiency_L1Tk_pt2"," ", 1000, 0, 20)
    h_single_L1Mu_efficiency_L1Tk_pt3 = TH1F("h_single_L1Mu_efficiency_L1Tk_pt3"," ", 1000, 0, 20)
    h_single_L1Mu_efficiency_L1Tk_pt4 = TH1F("h_single_L1Mu_efficiency_L1Tk_pt4"," ", 1000, 0, 20)

    binning2 = [0.05, 0.07, 0.1, 0.2, 0.3, 0.5, 1, 2, 4, 6, 10, 15, 20, 30, 50, 100, 200, 250, 275, 300, 400, 500, 1000]
    nBins = len(binning2) - 1
    genMu_dxy_fid = TH1F("genMu_dxy_fid"," ", nBins, np.asarray(binning2))
    genMu_dxy_lxy_fid = TH2F("genMu_dxy_lxy_fid"," ", 100, 0, 100, 300, 0, 300)
    genMu_dxy_fidT = TH1F("genMu_dxy_fidT"," ", nBins, np.asarray(binning2))
    L1Mu_genMu_dxy_fid = TH1F("L1Mu_genMu_dxy_fid"," ", nBins, np.asarray(binning2))
    L1Mu_genMu_dxy_fidT = TH1F("L1Mu_genMu_dxy_fidT"," ", nBins, np.asarray(binning2))
    L1Mu_genMu_dxy_fid_Q = TH1F("L1Mu_genMu_dxy_fid_Q"," ", nBins, np.asarray(binning2))
    L1Mu_genMu_dxy_fid_BX_Q = TH1F("L1Mu_genMu_dxy_fid_BX_Q"," ", nBins, np.asarray(binning2))
    L1Mu_genMu_dxy_fid_BX_Q_V = TH1F("L1Mu_genMu_dxy_fid_BX_Q_V"," ", nBins, np.asarray(binning2))
    L1Mu_genMu_dxy_fid_BX_Q_V_I = TH1F("L1Mu_genMu_dxy_fid_BX_Q_V_I"," ", nBins, np.asarray(binning2))

    genMu_lxy_fid = TH1F("genMu_lxy_fid"," ", nBins, np.asarray(binning2))
    L1Mu_genMu_lxy_fid = TH1F("L1Mu_genMu_lxy_fid"," ", nBins, np.asarray(binning2))
    L1Mu_genMu_lxy_fid_Q = TH1F("L1Mu_genMu_lxy_fid_Q"," ", nBins, np.asarray(binning2))
    L1Mu_genMu_lxy_fid_BX_Q = TH1F("L1Mu_genMu_lxy_fid_BX_Q"," ", nBins, np.asarray(binning2))
    L1Mu_genMu_lxy_fid_BX_Q_V = TH1F("L1Mu_genMu_lxy_fid_BX_Q_V"," ", nBins, np.asarray(binning2))
    L1Mu_genMu_lxy_fid_BX_Q_V_I = TH1F("L1Mu_genMu_lxy_fid_BX_Q_V_I"," ", nBins, np.asarray(binning2))

    genMu_dxy_fid_barrel = TH1F("genMu_dxy_fid_barrel"," ", nBins, np.asarray(binning2))
    L1Mu_genMu_dxy_fid_barrel = TH1F("L1Mu_genMu_dxy_fid_barrel"," ", nBins, np.asarray(binning2))
    L1Mu_genMu_dxy_fid_Q_barrel = TH1F("L1Mu_genMu_dxy_fid_Q_barrel"," ", nBins, np.asarray(binning2))
    L1Mu_genMu_dxy_fid_BX_Q_barrel = TH1F("L1Mu_genMu_dxy_fid_BX_Q_barrel"," ", nBins, np.asarray(binning2))
    L1Mu_genMu_dxy_fid_BX_Q_V_barrel = TH1F("L1Mu_genMu_dxy_fid_BX_Q_V_barrel"," ", nBins, np.asarray(binning2))
    L1Mu_genMu_dxy_fid_BX_Q_V_I_barrel = TH1F("L1Mu_genMu_dxy_fid_BX_Q_V_I_barrel"," ", nBins, np.asarray(binning2))

    genMu_dxy_fid_overlap = TH1F("genMu_dxy_fid_overlap"," ", nBins, np.asarray(binning2))
    L1Mu_genMu_dxy_fid_overlap = TH1F("L1Mu_genMu_dxy_fid_overlap"," ", nBins, np.asarray(binning2))
    L1Mu_genMu_dxy_fid_Q_overlap = TH1F("L1Mu_genMu_dxy_fid_Q_overlap"," ", nBins, np.asarray(binning2))
    L1Mu_genMu_dxy_fid_BX_Q_overlap = TH1F("L1Mu_genMu_dxy_fid_BX_Q_overlap"," ", nBins, np.asarray(binning2))
    L1Mu_genMu_dxy_fid_BX_Q_V_overlap = TH1F("L1Mu_genMu_dxy_fid_BX_Q_V_overlap"," ", nBins, np.asarray(binning2))
    L1Mu_genMu_dxy_fid_BX_Q_V_I_overlap = TH1F("L1Mu_genMu_dxy_fid_BX_Q_V_I_overlap"," ", nBins, np.asarray(binning2))

    genMu_dxy_fid_endcap = TH1F("genMu_dxy_fid_endcap"," ", nBins, np.asarray(binning2))
    L1Mu_genMu_dxy_fid_endcap = TH1F("L1Mu_genMu_dxy_fid_endcap"," ", nBins, np.asarray(binning2))
    L1Mu_genMu_dxy_fid_Q_endcap = TH1F("L1Mu_genMu_dxy_fid_Q_endcap"," ", nBins, np.asarray(binning2))
    L1Mu_genMu_dxy_fid_BX_Q_endcap = TH1F("L1Mu_genMu_dxy_fid_BX_Q_endcap"," ", nBins, np.asarray(binning2))
    L1Mu_genMu_dxy_fid_BX_Q_V_endcap = TH1F("L1Mu_genMu_dxy_fid_BX_Q_V_endcap"," ", nBins, np.asarray(binning2))
    L1Mu_genMu_dxy_fid_BX_Q_V_I_endcap = TH1F("L1Mu_genMu_dxy_fid_BX_Q_V_I_endcap"," ", nBins, np.asarray(binning2))

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


    ## plots per eta section
    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt4_total = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt4_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt4_total = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt4_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt4_total = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt4_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt4_total = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt4_total"," ", 25, 0, 2.5)

    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt3_total = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt3_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt3_total = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt3_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt3_total = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt3_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt3_total = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt3_total"," ", 25, 0, 2.5)

    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt2p5_total = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt2p5_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt2p5_total = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt2p5_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt2p5_total = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt2p5_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt2p5_total = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt2p5_total"," ", 25, 0, 2.5)

    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt2_total = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt2_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt2_total = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt2_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt2_total = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt2_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt2_total = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt2_total"," ", 25, 0, 2.5)


    L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt4_total = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt4_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt4_total = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt4_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt4_total = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt4_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt4_total = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt4_total"," ", 25, 0, 2.5)

    L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt3_total = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt3_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt3_total = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt3_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt3_total = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt3_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt3_total = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt3_total"," ", 25, 0, 2.5)

    L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt2p5_total = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt2p5_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt2p5_total = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt2p5_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt2p5_total = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt2p5_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt2p5_total = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt2p5_total"," ", 25, 0, 2.5)

    L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt2_total = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt2_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt2_total = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt2_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt2_total = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt2_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt2_total = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt2_total"," ", 25, 0, 2.5)

 
    L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt4_total = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt4_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt4_total = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt4_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt4_total = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt4_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt4_total = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt4_total"," ", 25, 0, 2.5)

    L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt3_total = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt3_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt3_total = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt3_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt3_total = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt3_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt3_total = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt3_total"," ", 25, 0, 2.5)

    L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt2p5_total = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt2p5_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt2p5_total = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt2p5_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt2p5_total = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt2p5_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt2p5_total = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt2p5_total"," ", 25, 0, 2.5)

    L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt2_total = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt2_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt2_total = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt2_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt2_total = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt2_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt2_total = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt2_total"," ", 25, 0, 2.5)


    L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt4_total = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt4_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt4_total = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt4_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt4_total = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt4_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt4_total = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt4_total"," ", 25, 0, 2.5)

    L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt3_total = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt3_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt3_total = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt3_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt3_total = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt3_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt3_total = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt3_total"," ", 25, 0, 2.5)

    L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt2p5_total = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt2p5_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt2p5_total = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt2p5_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt2p5_total = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt2p5_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt2p5_total = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt2p5_total"," ", 25, 0, 2.5)

    L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt2_total = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt2_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt2_total = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt2_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt2_total = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt2_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt2_total = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt2_total"," ", 25, 0, 2.5)


    ## pt plots
    genMu_pt_dxy0to0p1_fid = TH1F("genMu_pt_dxy0to0p1_fid"," ", 25,0,50)
    genMu_pt_dxy1to5_fid = TH1F("genMu_pt_dxy1to5_fid"," ", 25,0,50)
    genMu_pt_dxy5to10_fid = TH1F("genMu_pt_dxy5to10_fid"," ", 25,0,50)
    genMu_pt_dxy10_fid = TH1F("genMu_pt_dxy10_fid"," ", 25,0,50)

    L1Mu_genMu_pt_dxy0to0p1_fid_L1TkPt0 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_L1TkPt0"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_L1TkPt0 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_L1TkPt0"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_L1TkPt0 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_L1TkPt0"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_L1TkPt0 = TH1F("L1Mu_genMu_pt_dxy10_fid_L1TkPt0"," ", 25,0,50)

    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt2 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_dR0p4_L1TkPt2"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt2 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt2"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt2 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt2"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt2 = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt2"," ", 25,0,50)

    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt2 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_dR0p3_L1TkPt2"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt2 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt2"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt2 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt2"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt2 = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt2"," ", 25,0,50)

    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt2 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_dR0p2_L1TkPt2"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt2 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt2"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt2 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt2"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt2 = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt2"," ", 25,0,50)

    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt2 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_dR0p12_L1TkPt2"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt2 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt2"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt2 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt2"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt2 = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt2"," ", 25,0,50)


    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt2p5 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_dR0p4_L1TkPt2p5"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt2p5 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt2p5"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt2p5 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt2p5"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt2p5 = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt2p5"," ", 25,0,50)

    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt2p5 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_dR0p3_L1TkPt2p5"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt2p5 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt2p5"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt2p5 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt2p5"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt2p5 = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt2p5"," ", 25,0,50)

    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt2p5 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_dR0p2_L1TkPt2p5"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt2p5 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt2p5"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt2p5 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt2p5"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt2p5 = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt2p5"," ", 25,0,50)

    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt2p5 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_dR0p12_L1TkPt2p5"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt2p5 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt2p5"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt2p5 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt2p5"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt2p5 = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt2p5"," ", 25,0,50)


    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt3 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_dR0p4_L1TkPt3"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt3 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt3"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt3 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt3"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt3 = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt3"," ", 25,0,50)

    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt3 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_dR0p3_L1TkPt3"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt3 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt3"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt3 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt3"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt3 = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt3"," ", 25,0,50)

    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt3 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_dR0p2_L1TkPt3"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt3 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt3"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt3 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt3"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt3 = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt3"," ", 25,0,50)

    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt3 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_dR0p12_L1TkPt3"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt3 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt3"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt3 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt3"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt3 = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt3"," ", 25,0,50)


    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt4 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_dR0p4_L1TkPt4"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt4 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt4"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt4 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt4"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt4 = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt4"," ", 25,0,50)

    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt4 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_dR0p3_L1TkPt4"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt4 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt4"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt4 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt4"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt4 = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt4"," ", 25,0,50)

    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt4 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_dR0p2_L1TkPt4"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt4 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt4"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt4 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt4"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt4 = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt4"," ", 25,0,50)

    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt4 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_dR0p12_L1TkPt4"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt4 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt4"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt4 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt4"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt4 = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt4"," ", 25,0,50)

    ## plots per eta section
    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt4_total = TH1F("L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt4_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt4_total = TH1F("L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt4_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt4_total = TH1F("L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt4_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt4_total = TH1F("L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt4_total"," ", 25,0,50)

    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt3_total = TH1F("L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt3_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt3_total = TH1F("L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt3_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt3_total = TH1F("L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt3_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt3_total = TH1F("L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt3_total"," ", 25,0,50)

    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt2p5_total = TH1F("L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt2p5_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt2p5_total = TH1F("L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt2p5_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt2p5_total = TH1F("L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt2p5_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt2p5_total = TH1F("L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt2p5_total"," ", 25,0,50)

    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt2_total = TH1F("L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt2_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt2_total = TH1F("L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt2_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt2_total = TH1F("L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt2_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt2_total = TH1F("L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt2_total"," ", 25,0,50)


    L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt4_total = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt4_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt4_total = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt4_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt4_total = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt4_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt4_total = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt4_total"," ", 25,0,50)

    L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt3_total = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt3_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt3_total = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt3_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt3_total = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt3_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt3_total = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt3_total"," ", 25,0,50)

    L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt2p5_total = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt2p5_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt2p5_total = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt2p5_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt2p5_total = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt2p5_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt2p5_total = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt2p5_total"," ", 25,0,50)

    L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt2_total = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt2_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt2_total = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt2_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt2_total = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt2_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt2_total = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt2_total"," ", 25,0,50)

 
    L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt4_total = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt4_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt4_total = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt4_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt4_total = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt4_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt4_total = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt4_total"," ", 25,0,50)

    L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt3_total = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt3_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt3_total = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt3_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt3_total = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt3_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt3_total = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt3_total"," ", 25,0,50)

    L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt2p5_total = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt2p5_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt2p5_total = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt2p5_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt2p5_total = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt2p5_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt2p5_total = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt2p5_total"," ", 25,0,50)

    L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt2_total = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt2_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt2_total = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt2_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt2_total = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt2_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt2_total = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt2_total"," ", 25,0,50)


    L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt4_total = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt4_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt4_total = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt4_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt4_total = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt4_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt4_total = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt4_total"," ", 25,0,50)

    L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt3_total = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt3_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt3_total = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt3_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt3_total = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt3_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt3_total = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt3_total"," ", 25,0,50)

    L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt2p5_total = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt2p5_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt2p5_total = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt2p5_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt2p5_total = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt2p5_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt2p5_total = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt2p5_total"," ", 25,0,50)

    L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt2_total = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt2_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt2_total = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt2_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt2_total = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt2_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt2_total = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt2_total"," ", 25,0,50)


    ## temporary check for Slava
    L1Mu_genMu_pt_dxy0to0p1_fid = TH1F("L1Mu_genMu_pt_dxy0top01_fid"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid = TH1F("L1Mu_genMu_pt_dxy1to5_fid"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid = TH1F("L1Mu_genMu_pt_dxy5to10_fid"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid = TH1F("L1Mu_genMu_pt_dxy10_fid"," ", 25,0,50)

    L1Mu_genMu_pt_dxy0to0p1_fid_L1MuPt10 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_L1MuPt10"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_L1MuPt10 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_L1MuPt10"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_L1MuPt10 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_L1MuPt10"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_L1MuPt10 = TH1F("L1Mu_genMu_pt_dxy10_fid_L1MuPt10"," ", 25,0,50)

    L1Mu_genMu_pt_dxy0to0p1_fid_L1MuPt15 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_L1MuPt15"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_L1MuPt15 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_L1MuPt15"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_L1MuPt15 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_L1MuPt15"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_L1MuPt15 = TH1F("L1Mu_genMu_pt_dxy10_fid_L1MuPt15"," ", 25,0,50)

    L1Mu_genMu_pt_dxy0to0p1_fid_L1MuPt20 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_L1MuPt20"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_L1MuPt20 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_L1MuPt20"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_L1MuPt20 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_L1MuPt20"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_L1MuPt20 = TH1F("L1Mu_genMu_pt_dxy10_fid_L1MuPt20"," ", 25,0,50)


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
  
    nGoodGenMu = 0
    nGoodGenMuMissingL1Mu = 0
    nGoodGenMuMatchedL1MuMatchedToL1Tk = 0
    nGoodGenMuMatchedL1MuMatchedToL1TkPt3 = 0
    nGoodGenMuMatchedL1MuMatchedToL1TkPt4 = 0
    nGoodGenMuMatchedL1MuMatchedToL1TkPt5 = 0
    nGoodGenMuMatchedL1MuMatchedToL1TkPt6 = 0
    nGoodGenMuMatchedL1MuMatchedToL1TkPt10 = 0
    nGoodGenMuMatchedL1MuNotMatchedToL1Tk = 0
    nGoodGenMuMatchedL1MuNotMatchedToL1TkL1MuQLessThan4 = 0
    nGoodGenMuMatchedL1MuNotMatchedToL1TkL1MuBXNot0 = 0
    nGoodGenMuMatchedL1MuTriggered = 0

    treeHits = ch

    for k in range(0,treeHits.GetEntries()):
      treeHits.GetEntry(k)
      print "Event", k, "nL1Mu", treeHits.nL1Mu
      #if verbose:
      for i in range(0,2):
        for j in range(0,2):
          ij = i*2+j
          
          ## exclude all the bad muons
          if (abs(treeHits.genGdMu_eta_prop[i*2+0])>2.4): 
            continue
          if (abs(treeHits.genGdMu_eta_prop[i*2+1])>2.4): 
            continue
          if (abs(treeHits.genGdMu_pt[i*2+0])<5): 
            continue
          if (abs(treeHits.genGdMu_pt[i*2+1])<5): 
            continue
          if (abs(treeHits.genGd0Gd1_dR) < 2):
            continue
          if (abs(treeHits.genGd_genMuMu_dR[i]) < 1):
            continue
          if treeHits.genGdMu_eta_prop[ij] == -99 or treeHits.genGdMu_phi_prop[ij] == -99:
            continue

          pt = abs(treeHits.genGdMu_pt[ij])
          eta = treeHits.genGdMu_eta[ij]
          phi = abs(treeHits.genGdMu_phi[ij])
          phi_corr = abs(treeHits.genGdMu_phi_corr[ij])
          eta_prop = treeHits.genGdMu_eta_prop[ij]
          phi_prop = treeHits.genGdMu_phi_prop[ij]
          dxy = treeHits.genGdMu_dxy[ij]
          vz = abs(treeHits.genGd_vz[i])
          lxy =  abs(treeHits.genGd_lxy[i])

          genMu_dxy_lxy_fid.Fill(dxy,lxy)

          if verbose or True:
            print "\tGenMu", i, j,
            print "pt", pt,
            print "eta", eta,
            print "phi", phi,
            print "eta_prop", eta_prop,
            print "phi_prop", phi_prop,
            print "phi_corr", phi_corr,
#            print "index_corr", treeHits.genGdMu_L1Mu_index_corr[ij],
            print "dR_corr", treeHits.genGdMu_L1Mu_dR_corr[ij],
#            print "index_prop", treeHits.genGdMu_L1Mu_index_prop[ij],
            print "dR_prop", treeHits.genGdMu_L1Mu_dR_prop[ij],
            print "abs(dxy)", abs(treeHits.genGdMu_dxy[ij])
          L1Mu_index = treeHits.genGdMu_L1Mu_index_prop[ij]
          L1Mu_dR_prop = treeHits.genGdMu_L1Mu_dR_prop[ij]

          trigL1Mu = False
          trig_dR0p4_L1TkPt4 = False 
          trig_dR0p4_L1TkPt3 = False 
          trig_dR0p4_L1TkPt2p5 = False
          trig_dR0p4_L1TkPt2 = False
          
          trig_dR0p3_L1TkPt4 = False 
          trig_dR0p3_L1TkPt3 = False
          trig_dR0p3_L1TkPt2p5 = False
          trig_dR0p3_L1TkPt2 = False
          
          trig_dR0p2_L1TkPt4 = False
          trig_dR0p2_L1TkPt3 = False
          trig_dR0p2_L1TkPt2p5 = False
          trig_dR0p2_L1TkPt2 = False

          trig_dR0p12_L1TkPt4 = False
          trig_dR0p12_L1TkPt3 = False
          trig_dR0p12_L1TkPt2p5 = False
          trig_dR0p12_L1TkPt2 = False

          if L1Mu_index == 99 and verbose:
            for ii in range(0,treeHits.nL1Mu):     
              if treeHits.L1Mu_bx[ii] != 0: continue
              print "\t\tNot Matched: L1Mu", ii,
              print "L1Mu_pt", treeHits.L1Mu_pt[ii],
              print "L1Mu_eta", treeHits.L1Mu_eta[ii],
              print "L1Mu_phi", treeHits.L1Mu_phi[ii],
              print "L1Mu_bx", treeHits.L1Mu_bx[ii],
              print "L1Mu_quality", treeHits.L1Mu_quality[ii],
              print "L1Mu_dR_prop", deltaR(eta_prop, phi_prop, treeHits.L1Mu_eta[ii], treeHits.L1Mu_phi[ii]),
              print "L1Mu_dR_corr", deltaR(eta, phi_corr, treeHits.L1Mu_eta[ii], treeHits.L1Mu_phi[ii]),
              print "index_prop", treeHits.genGdMu_L1Mu_index_prop[ij],
              print "dR_prop", treeHits.genGdMu_L1Mu_dR_prop[ij]

          if L1Mu_index != 99:
            nTotalMuon +=1 
            L1Mu_pt = treeHits.L1Mu_pt[L1Mu_index]
            L1Mu_eta = treeHits.L1Mu_eta[L1Mu_index]
            L1Mu_phi = treeHits.L1Mu_phi[L1Mu_index]
            L1Mu_bx = treeHits.L1Mu_bx[L1Mu_index]
            L1Mu_quality = treeHits.L1Mu_quality[L1Mu_index]
            L1Mu_L1Tk_dR_prop = treeHits.L1Mu_L1Tk_dR_prop[L1Mu_index]
            L1Mu_L1Tk_pt = treeHits.L1Mu_L1Tk_pt_prop[L1Mu_index]
            if verbose or True:
              print "\t\tMatched: L1Mu", "pt", L1Mu_pt, "eta", L1Mu_eta, "phi", L1Mu_phi, "Quality", L1Mu_quality,
              print "L1Mu_L1Tk_dR_min", L1Mu_L1Tk_dR_prop, "L1Mu_L1Tk_pt", L1Mu_L1Tk_pt
                
            matched = L1Mu_L1Tk_dR_prop <= 0.12 and L1Mu_quality >= 4
            matched = matched and L1Mu_L1Tk_pt>=MatchingL1TkMinPtEff ## optional pT cut to increase the efficiency of matched L1Mu

            common = (abs(L1Mu_bx) <= 0) and (L1Mu_quality >= 4)
            
            if (common): trigL1Mu = True
            if ((not matched) and not (L1Mu_L1Tk_dR_prop <= 0.4 and L1Mu_L1Tk_pt>=4) and common): trig_dR0p4_L1TkPt4 = True
            if ((not matched) and not (L1Mu_L1Tk_dR_prop <= 0.4 and L1Mu_L1Tk_pt>=3) and common): trig_dR0p4_L1TkPt3 = True
            if ((not matched) and not (L1Mu_L1Tk_dR_prop <= 0.4 and L1Mu_L1Tk_pt>=2.5) and common): trig_dR0p4_L1TkPt2p5 = True
            if ((not matched) and not (L1Mu_L1Tk_dR_prop <= 0.4 and L1Mu_L1Tk_pt>=2) and common): trig_dR0p4_L1TkPt2 = True

            if ((not matched) and not (L1Mu_L1Tk_dR_prop <= 0.3 and L1Mu_L1Tk_pt>=4) and common): trig_dR0p3_L1TkPt4 = True
            if ((not matched) and not (L1Mu_L1Tk_dR_prop <= 0.3 and L1Mu_L1Tk_pt>=3) and common): trig_dR0p3_L1TkPt3 = True
            if ((not matched) and not (L1Mu_L1Tk_dR_prop <= 0.3 and L1Mu_L1Tk_pt>=2.5) and common): trig_dR0p3_L1TkPt2p5 = True
            if ((not matched) and not (L1Mu_L1Tk_dR_prop <= 0.3 and L1Mu_L1Tk_pt>=2) and common): trig_dR0p3_L1TkPt2 = True
            
            if ((not matched) and not (L1Mu_L1Tk_dR_prop <= 0.2 and L1Mu_L1Tk_pt>=4) and common): trig_dR0p2_L1TkPt4 = True
            if ((not matched) and not (L1Mu_L1Tk_dR_prop <= 0.2 and L1Mu_L1Tk_pt>=3) and common): trig_dR0p2_L1TkPt3 = True
            if ((not matched) and not (L1Mu_L1Tk_dR_prop <= 0.2 and L1Mu_L1Tk_pt>=2.5) and common): trig_dR0p2_L1TkPt2p5 = True
            if ((not matched) and not (L1Mu_L1Tk_dR_prop <= 0.2 and L1Mu_L1Tk_pt>=2) and common): trig_dR0p2_L1TkPt2 = True

            if ((not matched) and not (L1Mu_L1Tk_dR_prop <= 0.12 and L1Mu_L1Tk_pt>=4) and common): trig_dR0p12_L1TkPt4 = True
            if ((not matched) and not (L1Mu_L1Tk_dR_prop <= 0.12 and L1Mu_L1Tk_pt>=3) and common): trig_dR0p12_L1TkPt3 = True
            if ((not matched) and not (L1Mu_L1Tk_dR_prop <= 0.12 and L1Mu_L1Tk_pt>=2.5) and common): trig_dR0p12_L1TkPt2p5 = True
            if ((not matched) and not (L1Mu_L1Tk_dR_prop <= 0.12 and L1Mu_L1Tk_pt>=2) and common): trig_dR0p12_L1TkPt2 = True


            L1Mu_barrel = abs(L1Mu_eta)<=0.9
            L1Mu_overlap = abs(L1Mu_eta)>0.9 and abs(L1Mu_eta)<=1.2
            L1Mu_endcap = abs(L1Mu_eta)>1.2 and abs(L1Mu_eta)<=2.4

            matched_barrel = L1Mu_L1Tk_dR_prop <= 0.12 and L1Mu_quality >= 4
            matched_barrel = matched_barrel and L1Mu_L1Tk_pt>=0 ## optional pT cut to increase the efficiency of matched L1Mu

            matched_overlap = L1Mu_L1Tk_dR_prop <= 0.10 and L1Mu_quality >= 4
            matched_overlap = matched_overlap and L1Mu_L1Tk_pt>=0 ## optional pT cut to increase the efficiency of matched L1Mu

            matched_endcap = L1Mu_L1Tk_dR_prop <= 0.09 and L1Mu_quality >= 4
            matched_endcap = matched_endcap and L1Mu_L1Tk_pt>=0 ## optional pT cut to increase the efficiency of matched L1Mu

            trig_dR0p4_L1TkPt4_barrel = L1Mu_barrel and (not matched_barrel) and not (L1Mu_L1Tk_dR_prop <= 0.4 and L1Mu_L1Tk_pt>=4) and common
            trig_dR0p4_L1TkPt3_barrel = L1Mu_barrel and (not matched_barrel) and not (L1Mu_L1Tk_dR_prop <= 0.4 and L1Mu_L1Tk_pt>=3) and common
            trig_dR0p4_L1TkPt2p5_barrel = L1Mu_barrel and (not matched_barrel) and not (L1Mu_L1Tk_dR_prop <= 0.4 and L1Mu_L1Tk_pt>=2.5) and common
            trig_dR0p4_L1TkPt2_barrel = L1Mu_barrel and (not matched_barrel) and not (L1Mu_L1Tk_dR_prop <= 0.4 and L1Mu_L1Tk_pt>=2) and common

            trig_dR0p3_L1TkPt4_barrel = L1Mu_barrel and (not matched_barrel) and not (L1Mu_L1Tk_dR_prop <= 0.3 and L1Mu_L1Tk_pt>=4) and common
            trig_dR0p3_L1TkPt3_barrel = L1Mu_barrel and (not matched_barrel) and not (L1Mu_L1Tk_dR_prop <= 0.3 and L1Mu_L1Tk_pt>=3) and common
            trig_dR0p3_L1TkPt2p5_barrel = L1Mu_barrel and (not matched_barrel) and not (L1Mu_L1Tk_dR_prop <= 0.3 and L1Mu_L1Tk_pt>=2.5) and common
            trig_dR0p3_L1TkPt2_barrel = L1Mu_barrel and (not matched_barrel) and not (L1Mu_L1Tk_dR_prop <= 0.3 and L1Mu_L1Tk_pt>=2) and common

            trig_dR0p2_L1TkPt4_barrel = L1Mu_barrel and (not matched_barrel) and not (L1Mu_L1Tk_dR_prop <= 0.2 and L1Mu_L1Tk_pt>=4) and common
            trig_dR0p2_L1TkPt3_barrel = L1Mu_barrel and (not matched_barrel) and not (L1Mu_L1Tk_dR_prop <= 0.2 and L1Mu_L1Tk_pt>=3) and common
            trig_dR0p2_L1TkPt2p5_barrel = L1Mu_barrel and (not matched_barrel) and not (L1Mu_L1Tk_dR_prop <= 0.2 and L1Mu_L1Tk_pt>=2.5) and common
            trig_dR0p2_L1TkPt2_barrel = L1Mu_barrel and (not matched_barrel) and not (L1Mu_L1Tk_dR_prop <= 0.2 and L1Mu_L1Tk_pt>=2) and common

            trig_dR0p12_L1TkPt4_barrel = L1Mu_barrel and (not matched_barrel) and not (L1Mu_L1Tk_dR_prop <= 0.12 and L1Mu_L1Tk_pt>=4) and common
            trig_dR0p12_L1TkPt3_barrel = L1Mu_barrel and (not matched_barrel) and not (L1Mu_L1Tk_dR_prop <= 0.12 and L1Mu_L1Tk_pt>=3) and common
            trig_dR0p12_L1TkPt2p5_barrel = L1Mu_barrel and (not matched_barrel) and not (L1Mu_L1Tk_dR_prop <= 0.12 and L1Mu_L1Tk_pt>=2.5) and common
            trig_dR0p12_L1TkPt2_barrel = L1Mu_barrel and (not matched_barrel) and not (L1Mu_L1Tk_dR_prop <= 0.12 and L1Mu_L1Tk_pt>=2) and common


            trig_dR0p4_L1TkPt4_overlap = L1Mu_overlap and (not matched_overlap) and not (L1Mu_L1Tk_dR_prop <= 0.4 and L1Mu_L1Tk_pt>=4) and common
            trig_dR0p4_L1TkPt3_overlap = L1Mu_overlap and (not matched_overlap) and not (L1Mu_L1Tk_dR_prop <= 0.4 and L1Mu_L1Tk_pt>=3) and common
            trig_dR0p4_L1TkPt2p5_overlap = L1Mu_overlap and (not matched_overlap) and not (L1Mu_L1Tk_dR_prop <= 0.4 and L1Mu_L1Tk_pt>=2.5) and common
            trig_dR0p4_L1TkPt2_overlap = L1Mu_overlap and (not matched_overlap) and not (L1Mu_L1Tk_dR_prop <= 0.4 and L1Mu_L1Tk_pt>=2) and common

            trig_dR0p3_L1TkPt4_overlap = L1Mu_overlap and (not matched_overlap) and not (L1Mu_L1Tk_dR_prop <= 0.3 and L1Mu_L1Tk_pt>=4) and common
            trig_dR0p3_L1TkPt3_overlap = L1Mu_overlap and (not matched_overlap) and not (L1Mu_L1Tk_dR_prop <= 0.3 and L1Mu_L1Tk_pt>=3) and common
            trig_dR0p3_L1TkPt2p5_overlap = L1Mu_overlap and (not matched_overlap) and not (L1Mu_L1Tk_dR_prop <= 0.3 and L1Mu_L1Tk_pt>=2.5) and common
            trig_dR0p3_L1TkPt2_overlap = L1Mu_overlap and (not matched_overlap) and not (L1Mu_L1Tk_dR_prop <= 0.3 and L1Mu_L1Tk_pt>=2) and common

            trig_dR0p2_L1TkPt4_overlap = L1Mu_overlap and (not matched_overlap) and not (L1Mu_L1Tk_dR_prop <= 0.2 and L1Mu_L1Tk_pt>=4) and common
            trig_dR0p2_L1TkPt3_overlap = L1Mu_overlap and (not matched_overlap) and not (L1Mu_L1Tk_dR_prop <= 0.2 and L1Mu_L1Tk_pt>=3) and common
            trig_dR0p2_L1TkPt2p5_overlap = L1Mu_overlap and (not matched_overlap) and not (L1Mu_L1Tk_dR_prop <= 0.2 and L1Mu_L1Tk_pt>=2.5) and common
            trig_dR0p2_L1TkPt2_overlap = L1Mu_overlap and (not matched_overlap) and not (L1Mu_L1Tk_dR_prop <= 0.2 and L1Mu_L1Tk_pt>=2) and common

            trig_dR0p12_L1TkPt4_overlap = L1Mu_overlap and (not matched_overlap) and not (L1Mu_L1Tk_dR_prop <= 0.12 and L1Mu_L1Tk_pt>=4) and common
            trig_dR0p12_L1TkPt3_overlap = L1Mu_overlap and (not matched_overlap) and not (L1Mu_L1Tk_dR_prop <= 0.12 and L1Mu_L1Tk_pt>=3) and common
            trig_dR0p12_L1TkPt2p5_overlap = L1Mu_overlap and (not matched_overlap) and not (L1Mu_L1Tk_dR_prop <= 0.12 and L1Mu_L1Tk_pt>=2.5) and common
            trig_dR0p12_L1TkPt2_overlap = L1Mu_overlap and (not matched_overlap) and not (L1Mu_L1Tk_dR_prop <= 0.12 and L1Mu_L1Tk_pt>=2) and common
            

            trig_dR0p4_L1TkPt4_endcap = L1Mu_endcap and (not matched_endcap) and not (L1Mu_L1Tk_dR_prop <= 0.4 and L1Mu_L1Tk_pt>=4) and common
            trig_dR0p4_L1TkPt3_endcap = L1Mu_endcap and (not matched_endcap) and not (L1Mu_L1Tk_dR_prop <= 0.4 and L1Mu_L1Tk_pt>=3) and common
            trig_dR0p4_L1TkPt2p5_endcap = L1Mu_endcap and (not matched_endcap) and not (L1Mu_L1Tk_dR_prop <= 0.4 and L1Mu_L1Tk_pt>=2.5) and common
            trig_dR0p4_L1TkPt2_endcap = L1Mu_endcap and (not matched_endcap) and not (L1Mu_L1Tk_dR_prop <= 0.4 and L1Mu_L1Tk_pt>=2) and common

            trig_dR0p3_L1TkPt4_endcap = L1Mu_endcap and (not matched_endcap) and not (L1Mu_L1Tk_dR_prop <= 0.3 and L1Mu_L1Tk_pt>=4) and common
            trig_dR0p3_L1TkPt3_endcap = L1Mu_endcap and (not matched_endcap) and not (L1Mu_L1Tk_dR_prop <= 0.3 and L1Mu_L1Tk_pt>=3) and common
            trig_dR0p3_L1TkPt2p5_endcap = L1Mu_endcap and (not matched_endcap) and not (L1Mu_L1Tk_dR_prop <= 0.3 and L1Mu_L1Tk_pt>=2.5) and common
            trig_dR0p3_L1TkPt2_endcap = L1Mu_endcap and (not matched_endcap) and not (L1Mu_L1Tk_dR_prop <= 0.3 and L1Mu_L1Tk_pt>=2) and common

            trig_dR0p2_L1TkPt4_endcap = L1Mu_endcap and (not matched_endcap) and not (L1Mu_L1Tk_dR_prop <= 0.2 and L1Mu_L1Tk_pt>=4) and common
            trig_dR0p2_L1TkPt3_endcap = L1Mu_endcap and (not matched_endcap) and not (L1Mu_L1Tk_dR_prop <= 0.2 and L1Mu_L1Tk_pt>=3) and common
            trig_dR0p2_L1TkPt2p5_endcap = L1Mu_endcap and (not matched_endcap) and not (L1Mu_L1Tk_dR_prop <= 0.2 and L1Mu_L1Tk_pt>=2.5) and common
            trig_dR0p2_L1TkPt2_endcap = L1Mu_endcap and (not matched_endcap) and not (L1Mu_L1Tk_dR_prop <= 0.2 and L1Mu_L1Tk_pt>=2) and common

            trig_dR0p12_L1TkPt4_endcap = L1Mu_endcap and (not matched_endcap) and not (L1Mu_L1Tk_dR_prop <= 0.12 and L1Mu_L1Tk_pt>=4) and common
            trig_dR0p12_L1TkPt3_endcap = L1Mu_endcap and (not matched_endcap) and not (L1Mu_L1Tk_dR_prop <= 0.12 and L1Mu_L1Tk_pt>=3) and common
            trig_dR0p12_L1TkPt2p5_endcap = L1Mu_endcap and (not matched_endcap) and not (L1Mu_L1Tk_dR_prop <= 0.12 and L1Mu_L1Tk_pt>=2.5) and common
            trig_dR0p12_L1TkPt2_endcap = L1Mu_endcap and (not matched_endcap) and not (L1Mu_L1Tk_dR_prop <= 0.12 and L1Mu_L1Tk_pt>=2) and common

            
            trig_dR0p4_L1TkPt4_total = trig_dR0p4_L1TkPt4_barrel or trig_dR0p4_L1TkPt4_overlap or trig_dR0p4_L1TkPt4_endcap
            trig_dR0p3_L1TkPt4_total = trig_dR0p3_L1TkPt4_barrel or trig_dR0p3_L1TkPt4_overlap or trig_dR0p3_L1TkPt4_endcap
            trig_dR0p2_L1TkPt4_total = trig_dR0p2_L1TkPt4_barrel or trig_dR0p2_L1TkPt4_overlap or trig_dR0p2_L1TkPt4_endcap
            trig_dR0p12_L1TkPt4_total = trig_dR0p12_L1TkPt4_barrel or trig_dR0p12_L1TkPt4_overlap or trig_dR0p12_L1TkPt4_endcap

            trig_dR0p4_L1TkPt3_total = trig_dR0p4_L1TkPt3_barrel or trig_dR0p4_L1TkPt3_overlap or trig_dR0p4_L1TkPt3_endcap
            trig_dR0p3_L1TkPt3_total = trig_dR0p3_L1TkPt3_barrel or trig_dR0p3_L1TkPt3_overlap or trig_dR0p3_L1TkPt3_endcap
            trig_dR0p2_L1TkPt3_total = trig_dR0p2_L1TkPt3_barrel or trig_dR0p2_L1TkPt3_overlap or trig_dR0p2_L1TkPt3_endcap
            trig_dR0p12_L1TkPt3_total = trig_dR0p12_L1TkPt3_barrel or trig_dR0p12_L1TkPt3_overlap or trig_dR0p12_L1TkPt3_endcap
            
            trig_dR0p4_L1TkPt2p5_total = trig_dR0p4_L1TkPt2p5_barrel or trig_dR0p4_L1TkPt2p5_overlap or trig_dR0p4_L1TkPt2p5_endcap
            trig_dR0p3_L1TkPt2p5_total = trig_dR0p3_L1TkPt2p5_barrel or trig_dR0p3_L1TkPt2p5_overlap or trig_dR0p3_L1TkPt2p5_endcap
            trig_dR0p2_L1TkPt2p5_total = trig_dR0p2_L1TkPt2p5_barrel or trig_dR0p2_L1TkPt2p5_overlap or trig_dR0p2_L1TkPt2p5_endcap
            trig_dR0p12_L1TkPt2p5_total = trig_dR0p12_L1TkPt2p5_barrel or trig_dR0p12_L1TkPt2p5_overlap or trig_dR0p12_L1TkPt2p5_endcap

            trig_dR0p4_L1TkPt2_total = trig_dR0p4_L1TkPt2_barrel or trig_dR0p4_L1TkPt2_overlap or trig_dR0p4_L1TkPt2_endcap
            trig_dR0p3_L1TkPt2_total = trig_dR0p3_L1TkPt2_barrel or trig_dR0p3_L1TkPt2_overlap or trig_dR0p3_L1TkPt2_endcap
            trig_dR0p2_L1TkPt2_total = trig_dR0p2_L1TkPt2_barrel or trig_dR0p2_L1TkPt2_overlap or trig_dR0p2_L1TkPt2_endcap
            trig_dR0p12_L1TkPt2_total = trig_dR0p12_L1TkPt2_barrel or trig_dR0p12_L1TkPt2_overlap or trig_dR0p12_L1TkPt2_endcap


          dxy_range1 = (abs(dxy) <= 0.1)
          dxy_range2 = (abs(dxy) > 1 and abs(dxy) <= 5)
          dxy_range3 = (abs(dxy) > 5 and abs(dxy) <= 10)
          dxy_range4 = (abs(dxy) > 10 and abs(dxy) <= 50)

          eta_fid = abs(eta_prop)<=2.4 and vz < 500 and lxy < 300
          eta_fid_barrel = abs(eta_prop)<=0.9 and vz < 500 and lxy < 300
          eta_fid_overlap = 0.9< abs(eta_prop) and abs(eta_prop)<=1.2 and vz < 500 and lxy < 300
          eta_fid_endcap = abs(eta_prop)>1.2 and vz < 500 and lxy < 300
          eta_fid_tight = abs(eta_prop)<2.4 and vz < 300 and lxy < 300
          pt_fid = pt>=5 and vz < 500 and lxy < 300
          
          if eta_fid:
            genMu_dxy_fid.Fill(abs(dxy))
            if L1Mu_index != 99 and L1Mu_dR_prop < 0.2: 
              L1Mu_genMu_dxy_fid.Fill(abs(dxy))
              if (L1Mu_quality >= 4):
                L1Mu_genMu_dxy_fid_Q.Fill(abs(dxy))
                if (abs(L1Mu_bx) <= 0):
                  L1Mu_genMu_dxy_fid_BX_Q.Fill(abs(dxy))
                  if not matched:
                    L1Mu_genMu_dxy_fid_BX_Q_V.Fill(abs(dxy))
                    if trig_dR0p4_L1TkPt4:
                      L1Mu_genMu_dxy_fid_BX_Q_V_I.Fill(abs(dxy))
                      if abs(dxy)<1:
                        print "ALARM"

          if eta_fid:
            genMu_lxy_fid.Fill(abs(lxy))
            if L1Mu_index != 99 and L1Mu_dR_prop < 0.2: 
              L1Mu_genMu_lxy_fid.Fill(abs(lxy))
              if (L1Mu_quality >= 4):
                L1Mu_genMu_lxy_fid_Q.Fill(abs(lxy))
                if (abs(L1Mu_bx) <= 0):
                  L1Mu_genMu_lxy_fid_BX_Q.Fill(abs(lxy))
                  if not matched:
                    L1Mu_genMu_lxy_fid_BX_Q_V.Fill(abs(lxy))
                    if trig_dR0p4_L1TkPt4:
                      L1Mu_genMu_lxy_fid_BX_Q_V_I.Fill(abs(lxy))
                      if abs(lxy)<1:
                        print "ALARM"

          if eta_fid_barrel:
            genMu_dxy_fid_barrel.Fill(abs(dxy))
            if L1Mu_index != 99 and L1Mu_dR_prop < 0.2: 
              L1Mu_genMu_dxy_fid_barrel.Fill(abs(dxy))
              if (L1Mu_quality >= 4):
                L1Mu_genMu_dxy_fid_Q_barrel.Fill(abs(dxy))
                if (abs(L1Mu_bx) <= 0):
                  L1Mu_genMu_dxy_fid_BX_Q_barrel.Fill(abs(dxy))
                  if not matched:
                    L1Mu_genMu_dxy_fid_BX_Q_V_barrel.Fill(abs(dxy))
                    if trig_dR0p4_L1TkPt4:
                      L1Mu_genMu_dxy_fid_BX_Q_V_I_barrel.Fill(abs(dxy))
                      if abs(dxy)<1:
                        print "ALARM"

          if eta_fid_overlap:
            genMu_dxy_fid_overlap.Fill(abs(dxy))
            if L1Mu_index != 99 and L1Mu_dR_prop < 0.2: 
              L1Mu_genMu_dxy_fid_overlap.Fill(abs(dxy))
              if (L1Mu_quality >= 4):
                L1Mu_genMu_dxy_fid_Q_overlap.Fill(abs(dxy))
                if (abs(L1Mu_bx) <= 0):
                  L1Mu_genMu_dxy_fid_BX_Q_overlap.Fill(abs(dxy))
                  if not matched:
                    L1Mu_genMu_dxy_fid_BX_Q_V_overlap.Fill(abs(dxy))
                    if trig_dR0p4_L1TkPt4:
                      L1Mu_genMu_dxy_fid_BX_Q_V_I_overlap.Fill(abs(dxy))
                      if abs(dxy)<1:
                        print "ALARM"

          if eta_fid_endcap:
            genMu_dxy_fid_endcap.Fill(abs(dxy))
            if L1Mu_index != 99 and L1Mu_dR_prop < 0.2: 
              L1Mu_genMu_dxy_fid_endcap.Fill(abs(dxy))
              if (L1Mu_quality >= 4):
                L1Mu_genMu_dxy_fid_Q_endcap.Fill(abs(dxy))
                if (abs(L1Mu_bx) <= 0):
                  L1Mu_genMu_dxy_fid_BX_Q_endcap.Fill(abs(dxy))
                  if not matched:
                    L1Mu_genMu_dxy_fid_BX_Q_V_endcap.Fill(abs(dxy))
                    if trig_dR0p4_L1TkPt4:
                      L1Mu_genMu_dxy_fid_BX_Q_V_I_endcap.Fill(abs(dxy))
                      if abs(dxy)<1:
                        print "ALARM"

          if eta_fid_tight:
            genMu_dxy_fidT.Fill(abs(dxy))
            if treeHits.genGdMu_L1Mu_index_corr[ij] != 99 and L1Mu_dR_prop < 0.2: 
              L1Mu_genMu_dxy_fidT.Fill(abs(dxy))

          eta = abs(eta_prop)
          ## pt efficiencies
          if dxy_range1 and eta_fid:
            genMu_pt_dxy0to0p1_fid.Fill(pt)
            if trigL1Mu:      L1Mu_genMu_pt_dxy0to0p1_fid.Fill(pt)

            ### plots with different veto cones per eta section
            if trig_dR0p4_L1TkPt4_total:   L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt4_total.Fill(pt)
            if trig_dR0p4_L1TkPt3_total:   L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt3_total.Fill(pt)
            if trig_dR0p4_L1TkPt2p5_total: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p4_L1TkPt2_total:   L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt2_total.Fill(pt)

            if trig_dR0p3_L1TkPt4_total: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt4_total.Fill(pt)
            if trig_dR0p3_L1TkPt3_total: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt3_total.Fill(pt)
            if trig_dR0p3_L1TkPt2p5_total: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p3_L1TkPt2_total: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt2_total.Fill(pt)

            if trig_dR0p2_L1TkPt4_total: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt4_total.Fill(pt)
            if trig_dR0p2_L1TkPt3_total: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt3_total.Fill(pt)
            if trig_dR0p2_L1TkPt2p5_total: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p2_L1TkPt2_total: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt2_total.Fill(pt)

            if trig_dR0p12_L1TkPt4_total: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt4_total.Fill(pt)
            if trig_dR0p12_L1TkPt3_total: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt3_total.Fill(pt)
            if trig_dR0p12_L1TkPt2p5_total: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p12_L1TkPt2_total: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt2_total.Fill(pt)


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
            nGoodGenMu += 1
            if trigL1Mu:             L1Mu_genMu_pt_dxy1to5_fid.Fill(pt)

            ### plots with different veto cones per eta section
            if trig_dR0p4_L1TkPt4_total:   L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt4_total.Fill(pt)
            if trig_dR0p4_L1TkPt3_total:   L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt3_total.Fill(pt)
            if trig_dR0p4_L1TkPt2p5_total: L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p4_L1TkPt2_total:   L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt2_total.Fill(pt)

            if trig_dR0p3_L1TkPt4_total: L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt4_total.Fill(pt)
            if trig_dR0p3_L1TkPt3_total: L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt3_total.Fill(pt)
            if trig_dR0p3_L1TkPt2p5_total: L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p3_L1TkPt2_total: L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt2_total.Fill(pt)

            if trig_dR0p2_L1TkPt4_total: L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt4_total.Fill(pt)
            if trig_dR0p2_L1TkPt3_total: L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt3_total.Fill(pt)
            if trig_dR0p2_L1TkPt2p5_total: L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p2_L1TkPt2_total: L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt2_total.Fill(pt)

            if trig_dR0p12_L1TkPt4_total: L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt4_total.Fill(pt)
            if trig_dR0p12_L1TkPt3_total: L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt3_total.Fill(pt)
            if trig_dR0p12_L1TkPt2p5_total: L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p12_L1TkPt2_total: L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt2_total.Fill(pt)


            if trig_dR0p4_L1TkPt4:   L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt4.Fill(pt)
            if trig_dR0p4_L1TkPt3:   L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt3.Fill(pt)
            if trig_dR0p4_L1TkPt2p5: L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt2p5.Fill(pt)
            if trig_dR0p4_L1TkPt2:   L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt2.Fill(pt)

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
            if trig_dR0p12_L1TkPt2: 
              L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt2.Fill(pt)
              nGoodGenMuMatchedL1MuTriggered += 1
            else:
              print "\t\tGood GenMu with small dxy was not triggered", L1Mu_index              
              if L1Mu_index == 99:
                print "\t\t\tMissing L1Mu!"
                nGoodGenMuMissingL1Mu += 1
                print "\t\tlxy", lxy
              if L1Mu_index != 99:
                print "\t\t\tL1Mu was there!"
                L1Mu_pt = treeHits.L1Mu_pt[L1Mu_index]
                L1Mu_eta = treeHits.L1Mu_eta[L1Mu_index]
                L1Mu_phi = treeHits.L1Mu_phi[L1Mu_index]
                L1Mu_bx = treeHits.L1Mu_bx[L1Mu_index]
                L1Mu_quality = treeHits.L1Mu_quality[L1Mu_index]
                L1Mu_L1Tk_dR_prop = treeHits.L1Mu_L1Tk_dR_prop[L1Mu_index]
                L1Mu_L1Tk_pt = treeHits.L1Mu_L1Tk_pt_prop[L1Mu_index]
                matched = L1Mu_L1Tk_dR_prop <= 0.12 and L1Mu_quality >= 4
                common = (abs(L1Mu_bx) <= 0) and (L1Mu_quality >= 4)
#                print "\t\tProperties:", "pt", L1Mu_pt, "eta", L1Mu_eta, "phi", L1Mu_phi, "Quality", L1Mu_quality,
#                print "L1Tk_dR", L1Mu_L1Tk_dR_prop, "L1Tk_pt", L1Mu_L1Tk_pt, "bx", L1Mu_bx
                if (matched):
                  print "\t\t\tL1Mu was matched to a L1Tk!", L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt
                  nGoodGenMuMatchedL1MuMatchedToL1Tk += 1
                  if L1Mu_L1Tk_pt >= 3: nGoodGenMuMatchedL1MuMatchedToL1TkPt3 += 1 
                  if L1Mu_L1Tk_pt >= 4: nGoodGenMuMatchedL1MuMatchedToL1TkPt4 += 1
                  if L1Mu_L1Tk_pt >= 5: nGoodGenMuMatchedL1MuMatchedToL1TkPt5 += 1
                  if L1Mu_L1Tk_pt >= 6: nGoodGenMuMatchedL1MuMatchedToL1TkPt6 += 1
                  if L1Mu_L1Tk_pt >= 10: nGoodGenMuMatchedL1MuMatchedToL1TkPt10 += 1

                else:
                  nGoodGenMuMatchedL1MuNotMatchedToL1Tk += 1              
                  if (not abs(L1Mu_bx) <= 0):
                    print "\t\t\tL1Mu does not have bx=0!"
                    nGoodGenMuMatchedL1MuNotMatchedToL1TkL1MuBXNot0 += 1
                  else:
                    if (L1Mu_quality<4):
                      print "\t\t\tL1Mu does not have Q>=0!"
                      nGoodGenMuMatchedL1MuNotMatchedToL1TkL1MuQLessThan4 += 1

          if dxy_range3 and eta_fid:
            genMu_pt_dxy5to10_fid.Fill(pt)
            if trigL1Mu:             L1Mu_genMu_pt_dxy5to10_fid.Fill(pt)

            ### plots with different veto cones per eta section
            if trig_dR0p4_L1TkPt4_total:   L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt4_total.Fill(pt)
            if trig_dR0p4_L1TkPt3_total:   L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt3_total.Fill(pt)
            if trig_dR0p4_L1TkPt2p5_total: L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p4_L1TkPt2_total:   L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt2_total.Fill(pt)

            if trig_dR0p3_L1TkPt4_total: L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt4_total.Fill(pt)
            if trig_dR0p3_L1TkPt3_total: L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt3_total.Fill(pt)
            if trig_dR0p3_L1TkPt2p5_total: L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p3_L1TkPt2_total: L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt2_total.Fill(pt)

            if trig_dR0p2_L1TkPt4_total: L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt4_total.Fill(pt)
            if trig_dR0p2_L1TkPt3_total: L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt3_total.Fill(pt)
            if trig_dR0p2_L1TkPt2p5_total: L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p2_L1TkPt2_total: L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt2_total.Fill(pt)

            if trig_dR0p12_L1TkPt4_total: L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt4_total.Fill(pt)
            if trig_dR0p12_L1TkPt3_total: L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt3_total.Fill(pt)
            if trig_dR0p12_L1TkPt2p5_total: L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p12_L1TkPt2_total: L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt2_total.Fill(pt)


            if trig_dR0p4_L1TkPt4:   L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt4.Fill(pt)
            if trig_dR0p4_L1TkPt3:   L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt3.Fill(pt)
            if trig_dR0p4_L1TkPt2p5: L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt2p5.Fill(pt)
            if trig_dR0p4_L1TkPt2:   L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt2.Fill(pt)

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
            if trigL1Mu:             L1Mu_genMu_pt_dxy10_fid.Fill(pt)

            ### plots with different veto cones per eta section
            if trig_dR0p4_L1TkPt4_total:   L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt4_total.Fill(pt)
            if trig_dR0p4_L1TkPt3_total:   L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt3_total.Fill(pt)
            if trig_dR0p4_L1TkPt2p5_total: L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p4_L1TkPt2_total:   L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt2_total.Fill(pt)

            if trig_dR0p3_L1TkPt4_total: L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt4_total.Fill(pt)
            if trig_dR0p3_L1TkPt3_total: L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt3_total.Fill(pt)
            if trig_dR0p3_L1TkPt2p5_total: L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p3_L1TkPt2_total: L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt2_total.Fill(pt)

            if trig_dR0p2_L1TkPt4_total: L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt4_total.Fill(pt)
            if trig_dR0p2_L1TkPt3_total: L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt3_total.Fill(pt)
            if trig_dR0p2_L1TkPt2p5_total: L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p2_L1TkPt2_total: L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt2_total.Fill(pt)

            if trig_dR0p12_L1TkPt4_total: L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt4_total.Fill(pt)
            if trig_dR0p12_L1TkPt3_total: L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt3_total.Fill(pt)
            if trig_dR0p12_L1TkPt2p5_total: L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p12_L1TkPt2_total: L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt2_total.Fill(pt)


            if trig_dR0p4_L1TkPt4:   L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt4.Fill(pt)
            if trig_dR0p4_L1TkPt3:   L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt3.Fill(pt)
            if trig_dR0p4_L1TkPt2p5: L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt2p5.Fill(pt)
            if trig_dR0p4_L1TkPt2:   L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt2.Fill(pt)
             
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
            if trigL1Mu:             L1Mu_genMu_eta_dxy0to0p1_fid.Fill(eta)

            ### plots with different veto cones per eta section
            if trig_dR0p4_L1TkPt4_total:   
              L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt4_total.Fill(pt)
              print ">>>>OK!!!<<<<"
            if trig_dR0p4_L1TkPt3_total:   L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt3_total.Fill(pt)
            if trig_dR0p4_L1TkPt2p5_total: L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p4_L1TkPt2_total:   L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt2_total.Fill(pt)

            if trig_dR0p3_L1TkPt4_total: L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt4_total.Fill(pt)
            if trig_dR0p3_L1TkPt3_total: L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt3_total.Fill(pt)
            if trig_dR0p3_L1TkPt2p5_total: L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p3_L1TkPt2_total: L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt2_total.Fill(pt)

            if trig_dR0p2_L1TkPt4_total: L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt4_total.Fill(pt)
            if trig_dR0p2_L1TkPt3_total: L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt3_total.Fill(pt)
            if trig_dR0p2_L1TkPt2p5_total: L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p2_L1TkPt2_total: L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt2_total.Fill(pt)

            if trig_dR0p12_L1TkPt4_total: L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt4_total.Fill(pt)
            if trig_dR0p12_L1TkPt3_total: L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt3_total.Fill(pt)
            if trig_dR0p12_L1TkPt2p5_total: L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p12_L1TkPt2_total: L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt2_total.Fill(pt)


            if trig_dR0p4_L1TkPt4:   L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt4.Fill(eta)
            if trig_dR0p4_L1TkPt3:   L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt3.Fill(eta)
            if trig_dR0p4_L1TkPt2p5: L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt2p5.Fill(eta)
            if trig_dR0p4_L1TkPt2:   L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt2.Fill(eta)

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
            if trigL1Mu:             L1Mu_genMu_eta_dxy1to5_fid.Fill(eta)

            ### plots with different veto cones per eta section
            if trig_dR0p4_L1TkPt4_total:   L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt4_total.Fill(pt)
            if trig_dR0p4_L1TkPt3_total:   L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt3_total.Fill(pt)
            if trig_dR0p4_L1TkPt2p5_total: L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p4_L1TkPt2_total:   L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt2_total.Fill(pt)

            if trig_dR0p3_L1TkPt4_total: L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt4_total.Fill(pt)
            if trig_dR0p3_L1TkPt3_total: L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt3_total.Fill(pt)
            if trig_dR0p3_L1TkPt2p5_total: L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p3_L1TkPt2_total: L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt2_total.Fill(pt)

            if trig_dR0p2_L1TkPt4_total: L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt4_total.Fill(pt)
            if trig_dR0p2_L1TkPt3_total: L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt3_total.Fill(pt)
            if trig_dR0p2_L1TkPt2p5_total: L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p2_L1TkPt2_total: L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt2_total.Fill(pt)

            if trig_dR0p12_L1TkPt4_total: L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt4_total.Fill(pt)
            if trig_dR0p12_L1TkPt3_total: L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt3_total.Fill(pt)
            if trig_dR0p12_L1TkPt2p5_total: L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p12_L1TkPt2_total: L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt2_total.Fill(pt)


            if trig_dR0p4_L1TkPt4:   L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt4.Fill(eta)
            if trig_dR0p4_L1TkPt3:   L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt3.Fill(eta)
            if trig_dR0p4_L1TkPt2p5: L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt2p5.Fill(eta)
            if trig_dR0p4_L1TkPt2:   L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt2.Fill(eta)

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
            if trigL1Mu:             L1Mu_genMu_eta_dxy5to10_fid.Fill(eta)

            ### plots with different veto cones per eta section
            if trig_dR0p4_L1TkPt4_total:   L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt4_total.Fill(pt)
            if trig_dR0p4_L1TkPt3_total:   L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt3_total.Fill(pt)
            if trig_dR0p4_L1TkPt2p5_total: L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p4_L1TkPt2_total:   L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt2_total.Fill(pt)

            if trig_dR0p3_L1TkPt4_total: L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt4_total.Fill(pt)
            if trig_dR0p3_L1TkPt3_total: L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt3_total.Fill(pt)
            if trig_dR0p3_L1TkPt2p5_total: L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p3_L1TkPt2_total: L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt2_total.Fill(pt)

            if trig_dR0p2_L1TkPt4_total: L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt4_total.Fill(pt)
            if trig_dR0p2_L1TkPt3_total: L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt3_total.Fill(pt)
            if trig_dR0p2_L1TkPt2p5_total: L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p2_L1TkPt2_total: L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt2_total.Fill(pt)

            if trig_dR0p12_L1TkPt4_total: L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt4_total.Fill(pt)
            if trig_dR0p12_L1TkPt3_total: L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt3_total.Fill(pt)
            if trig_dR0p12_L1TkPt2p5_total: L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p12_L1TkPt2_total: L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt2_total.Fill(pt)


            if trig_dR0p4_L1TkPt4:   L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt4.Fill(eta)
            if trig_dR0p4_L1TkPt3:   L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt3.Fill(eta)
            if trig_dR0p4_L1TkPt2p5: L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt2p5.Fill(eta)
            if trig_dR0p4_L1TkPt2:   L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt2.Fill(eta)

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
            if trigL1Mu:             L1Mu_genMu_eta_dxy10_fid.Fill(eta)


            ### plots with different veto cones per eta section
            if trig_dR0p4_L1TkPt4_total:   L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt4_total.Fill(pt)
            if trig_dR0p4_L1TkPt3_total:   L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt3_total.Fill(pt)
            if trig_dR0p4_L1TkPt2p5_total: L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p4_L1TkPt2_total:   L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt2_total.Fill(pt)

            if trig_dR0p3_L1TkPt4_total: L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt4_total.Fill(pt)
            if trig_dR0p3_L1TkPt3_total: L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt3_total.Fill(pt)
            if trig_dR0p3_L1TkPt2p5_total: L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p3_L1TkPt2_total: L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt2_total.Fill(pt)

            if trig_dR0p2_L1TkPt4_total: L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt4_total.Fill(pt)
            if trig_dR0p2_L1TkPt3_total: L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt3_total.Fill(pt)
            if trig_dR0p2_L1TkPt2p5_total: L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p2_L1TkPt2_total: L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt2_total.Fill(pt)

            if trig_dR0p12_L1TkPt4_total: L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt4_total.Fill(pt)
            if trig_dR0p12_L1TkPt3_total: L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt3_total.Fill(pt)
            if trig_dR0p12_L1TkPt2p5_total: L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p12_L1TkPt2_total: L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt2_total.Fill(pt)


            if trig_dR0p4_L1TkPt4:   L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt4.Fill(eta)
            if trig_dR0p4_L1TkPt3:   L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt3.Fill(eta)
            if trig_dR0p4_L1TkPt2p5: L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt2p5.Fill(eta)
            if trig_dR0p4_L1TkPt2:   L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt2.Fill(eta)

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
    
    print "---------------------------------------------"
    print "Trigger Report"
    print "---------------------------------------------"
    print "nGoodGenMu", nGoodGenMu
    print "nGoodGenMuMatchedL1MuTriggered", nGoodGenMuMatchedL1MuTriggered
    print "nGoodGenMuMissingL1Mu", nGoodGenMuMissingL1Mu
    print "nGoodGenMuMatchedL1MuMatchedToL1Tk", nGoodGenMuMatchedL1MuMatchedToL1Tk
    print "\tnGoodGenMuMatchedL1MuMatchedToL1TkPt3", nGoodGenMuMatchedL1MuMatchedToL1TkPt3
    print "\tnGoodGenMuMatchedL1MuMatchedToL1TkPt4", nGoodGenMuMatchedL1MuMatchedToL1TkPt4
    print "\tnGoodGenMuMatchedL1MuMatchedToL1TkPt5", nGoodGenMuMatchedL1MuMatchedToL1TkPt5
    print "\tnGoodGenMuMatchedL1MuMatchedToL1TkPt6", nGoodGenMuMatchedL1MuMatchedToL1TkPt6
    print "\tnGoodGenMuMatchedL1MuMatchedToL1TkPt10", nGoodGenMuMatchedL1MuMatchedToL1TkPt10
    print "nGoodGenMuMatchedL1MuNotMatchedToL1Tk", nGoodGenMuMatchedL1MuNotMatchedToL1Tk
    print "nGoodGenMuMatchedL1MuNotMatchedToL1TkL1MuQLessThan4", nGoodGenMuMatchedL1MuNotMatchedToL1TkL1MuQLessThan4
    print "nGoodGenMuMatchedL1MuNotMatchedToL1TkL1MuBXNot0", nGoodGenMuMatchedL1MuNotMatchedToL1TkL1MuBXNot0
    print "---------------------------------------------"

    c = TCanvas("c","c",800,600)
    c.Clear()    
    gStyle.SetTitleBorderSize(0);
    gStyle.SetPadLeftMargin(0.126);
    gStyle.SetPadRightMargin(0.04);
    gStyle.SetPadTopMargin(0.06);
    gStyle.SetPadBottomMargin(0.13);
    gPad.SetTickx(1)
    gPad.SetTicky(1)
#    gStyle.SetPalette(kBlackBody)
    genMu_dxy_lxy_fid.Draw("colz")
    c.SaveAs("genMu_dxy_lxy_fid_plot.png")

    def makeEffPlot(eff1, eff2, eff3, eff4, title, doPt = True):
      
      c = TCanvas("c","c",800,600)
      c.Clear()    
      gStyle.SetTitleBorderSize(0);
      gStyle.SetPadLeftMargin(0.126);
      gStyle.SetPadRightMargin(0.04);
      gStyle.SetPadTopMargin(0.06);
      gStyle.SetPadBottomMargin(0.13);
      gPad.SetTickx(1)
      gPad.SetTicky(1)
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
      b1.SetTitle("                                                                  14TeV, " + pu)
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
      
      if doPt:
        errorAverage = sqrt(eff3.GetEfficiencyErrorUp(8)*eff3.GetEfficiencyErrorUp(8) + eff3.GetEfficiencyErrorUp(9)*eff3.GetEfficiencyErrorUp(9))/2.
        print title, "pt15", "%.2f"%((eff3.GetEfficiency(8) + eff3.GetEfficiency(9))/2.), "+/-%f"%(errorAverage)
        print title, "pt20", "%.2f"%(eff3.GetEfficiency(11)), "+/-%f"%(eff3.GetEfficiencyErrorUp(11))
        print

      latex = applyTdrStyle()      

      leg = TLegend(0.7,0.4,0.9,0.6,"","brNDC")
      leg.SetFillColor(kWhite)
      leg.SetBorderSize(0)
      leg.SetFillStyle(0)
      leg.SetTextSize(0.03)
      leg.AddEntry(eff1,"|dxy| #leq 0.1", "l")
      leg.AddEntry(eff2,"1 < |dxy| #leq 5", "l")
      leg.AddEntry(eff3,"5 < |dxy| #leq 10", "l")
      leg.AddEntry(eff4,"10 < |dxy| #leq 50", "l")
      leg.Draw("same")
      c.SaveAs(title)
    
    ## pt effciency plots
    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt2, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt2,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt2,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt2,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p4_L1TkPt2" + ext, True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt2p5, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt2p5,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt2p5,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt2p5,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p4_L1TkPt2p5" + ext, True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt3, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt3,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt3,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt3,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p4_L1TkPt3" + ext, True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt4, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt4,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt4,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt4,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p4_L1TkPt4" + ext, True)


    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt2, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt2,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt2,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt2,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p3_L1TkPt2" + ext, True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt2p5, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt2p5,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt2p5,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt2p5,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p3_L1TkPt2p5" + ext, True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt3, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt3,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt3,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt3,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p3_L1TkPt3" + ext, True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt4, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt4,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt4,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt4,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p3_L1TkPt4" + ext, True)


    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt2, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt2,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt2,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt2,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p2_L1TkPt2" + ext, True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt2p5, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt2p5,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt2p5,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt2p5,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p2_L1TkPt2p5" + ext, True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt3, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt3,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt3,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt3,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p2_L1TkPt3" + ext, True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt4, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt4,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt4,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt4,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p2_L1TkPt4" + ext, True)


    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt2, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt2,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt2,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt2,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p12_L1TkPt2" + ext, True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt2p5, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt2p5,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt2p5,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt2p5,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p12_L1TkPt2p5" + ext, True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt3, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt3,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt3,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt3,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p12_L1TkPt3" + ext, True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt4, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt4,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt4,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt4,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p12_L1TkPt4" + ext, True)

    
    ## eta effciency plots
    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt2, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt2,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt2,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt2,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p4_L1TkPt2" + ext, False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt2p5, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt2p5,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt2p5,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt2p5,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p4_L1TkPt2p5" + ext, False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt3, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt3,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt3,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt3,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p4_L1TkPt3" + ext, False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt4, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt4,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt4,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt4,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p4_L1TkPt4" + ext, False)


    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt2, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt2,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt2,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt2,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p3_L1TkPt2" + ext, False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt2p5, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt2p5,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt2p5,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt2p5,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p3_L1TkPt2p5" + ext, False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt3, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt3,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt3,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt3,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p3_L1TkPt3" + ext, False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt4, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt4,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt4,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt4,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p3_L1TkPt4" + ext, False)


    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt2, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt2,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt2,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt2,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p2_L1TkPt2" + ext, False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt2p5, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt2p5,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt2p5,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt2p5,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p2_L1TkPt2p5" + ext, False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt3, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt3,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt3,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt3,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p2_L1TkPt3" + ext, False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt4, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt4,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt4,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt4,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p2_L1TkPt4" + ext, False)


    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt2, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt2,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt2,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt2,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p12_L1TkPt2" + ext, False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt2p5, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt2p5,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt2p5,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt2p5,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p12_L1TkPt2p5" + ext, False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt3, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt3,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt3,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt3,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p12_L1TkPt3" + ext, False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt4, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt4,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt4,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt4,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p12_L1TkPt4" + ext, False)


    ## PLOTS WITH DIFFERENT CONE SIZES IN BARREL/overlap/endcap
    ## pt effciency plots
    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt2_total, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt2_total,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt2_total,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt2_total,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p4_L1TkPt2_total" + ext, True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt2p5_total, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt2p5_total,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt2p5_total,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt2p5_total,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p4_L1TkPt2p5_total" + ext, True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt3_total, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt3_total,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt3_total,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt3_total,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p4_L1TkPt3_total" + ext, True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt4_total, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt4_total,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt4_total,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt4_total,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p4_L1TkPt4_total" + ext, True)


    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt2_total, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt2_total,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt2_total,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt2_total,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p3_L1TkPt2_total" + ext, True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt2p5_total, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt2p5_total,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt2p5_total,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt2p5_total,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p3_L1TkPt2p5_total" + ext, True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt3_total, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt3_total,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt3_total,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt3_total,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p3_L1TkPt3_total" + ext, True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt4_total, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt4_total,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt4_total,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt4_total,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p3_L1TkPt4_total" + ext, True)


    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt2_total, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt2_total,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt2_total,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt2_total,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p2_L1TkPt2_total" + ext, True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt2p5_total, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt2p5_total,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt2p5_total,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt2p5_total,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p2_L1TkPt2p5_total" + ext, True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt3_total, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt3_total,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt3_total,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt3_total,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p2_L1TkPt3_total" + ext, True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt4_total, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt4_total,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt4_total,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt4_total,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p2_L1TkPt4_total" + ext, True)


    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt2_total, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt2_total,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt2_total,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt2_total,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p12_L1TkPt2_total" + ext, True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt2p5_total, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt2p5_total,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt2p5_total,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt2p5_total,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p12_L1TkPt2p5_total" + ext, True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt3_total, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt3_total,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt3_total,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt3_total,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p12_L1TkPt3_total" + ext, True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt4_total, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt4_total,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt4_total,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt4_total,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p12_L1TkPt4_total" + ext, True)

    
    ## eta effciency plots
    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt2_total, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt2_total,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt2_total,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt2_total,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p4_L1TkPt2_total" + ext, False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt2p5_total, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt2p5_total,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt2p5_total,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt2p5_total,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p4_L1TkPt2p5_total" + ext, False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt3_total, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt3_total,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt3_total,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt3_total,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p4_L1TkPt3_total" + ext, False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt4_total, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt4_total,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt4_total,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt4_total,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p4_L1TkPt4_total" + ext, False)


    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt2_total, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt2_total,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt2_total,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt2_total,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p3_L1TkPt2_total" + ext, False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt2p5_total, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt2p5_total,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt2p5_total,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt2p5_total,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p3_L1TkPt2p5_total" + ext, False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt3_total, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt3_total,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt3_total,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt3_total,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p3_L1TkPt3_total" + ext, False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt4_total, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt4_total,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt4_total,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt4_total,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p3_L1TkPt4_total" + ext, False)


    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt2_total, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt2_total,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt2_total,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt2_total,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p2_L1TkPt2_total" + ext, False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt2p5_total, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt2p5_total,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt2p5_total,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt2p5_total,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p2_L1TkPt2p5_total" + ext, False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt3_total, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt3_total,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt3_total,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt3_total,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p2_L1TkPt3_total" + ext, False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt4_total, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt4_total,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt4_total,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt4_total,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p2_L1TkPt4_total" + ext, False)


    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt2_total, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt2_total,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt2_total,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt2_total,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p12_L1TkPt2_total" + ext, False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt2p5_total, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt2p5_total,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt2p5_total,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt2p5_total,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p12_L1TkPt2p5_total" + ext, False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt3_total, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt3_total,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt3_total,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt3_total,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p12_L1TkPt3_total" + ext, False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt4_total, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt4_total,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt4_total,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt4_total,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p12_L1TkPt4_total" + ext, False)



    ## debug for slava
    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid" + ext, True)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid" + ext, False)

    def makeDxyEffPlot(eff1, eff2, eff3, eff4, eff5, title):
      
      c = TCanvas("c","c",800,600)
      c.Clear()    
      gStyle.SetTitleBorderSize(0);
      gStyle.SetPadLeftMargin(0.126);
      gStyle.SetPadRightMargin(0.04);
      gStyle.SetPadTopMargin(0.06);
      gStyle.SetPadBottomMargin(0.13);
      gPad.SetTickx(1)
      gPad.SetTicky(1)
      gPad.SetLogx(1)
      
      binning2 = [0.05, 0.07, 0.1, 0.2, 0.3, 0.5, 1, 2, 4, 6, 10, 15, 20, 30, 50, 100, 200, 250, 275, 300, 400, 500, 1000] #
      nBins = len(binning2) - 1

      #b1 = TH1F("b1","b1", 30, 0, 30)
      b1 = TH1F("b1","b1", nBins, np.asarray(binning2))
      #b1.GetYaxis().SetRangeUser(.01,100)
      b1.GetYaxis().SetTitleOffset(1.2)
      b1.GetYaxis().SetNdivisions(520)
      b1.GetYaxis().SetTitle("Trigger Reconstruction efficiency")
      b1.GetXaxis().SetTitle("True Muon d_{xy} [cm]")
      b1.GetXaxis().SetTitleFont(62)
      b1.GetXaxis().SetTitleOffset(1.2)
      b1.GetXaxis().SetTitleSize(0.045)
      b1.SetTitle("                                                                  14TeV, " + pu)
      b1.SetStats(0)
      b1.Draw()

      eff1.SetLineColor(kBlue)
      eff1.SetLineWidth(2)
      eff1.Draw("same")
      if eff2:
        eff2.SetLineColor(kOrange+1)
        eff2.SetLineWidth(2)
        eff2.Draw("same")
      if eff3:
        eff3.SetLineColor(kRed)
        eff3.SetLineWidth(2)
        eff3.Draw("same")
      if eff4:
        eff4.SetLineColor(kGreen+1)
        eff4.SetLineWidth(2)
        eff4.Draw("same")
      if eff5:
        eff5.SetLineColor(kMagenta+1)
        eff5.SetLineWidth(2)
        eff5.Draw("same")
        
      latex = applyTdrStyle()      

      leg = TLegend(0.25,0.2,0.75,0.45,"","brNDC")
      leg.SetFillColor(kWhite)
      leg.SetBorderSize(0)
      leg.SetFillStyle(0)
      leg.SetTextSize(0.03)
      leg.AddEntry(eff1,"L1Mu", "l")
      leg.AddEntry(eff2,"L1Mu (Q#geq4)", "l")
      leg.AddEntry(eff3,"L1Mu (Q#geq4, BX=0)", "l")
      leg.AddEntry(eff4,"L1Mu (Q#geq4, BX=0) + veto (dR#leq0.12)", "l")
      leg.AddEntry(eff5,"L1Mu (Q#geq4, BX=0) + veto (dR#leq0.12) + isol (dR<0.2, p_{T}^{L1Tk}#geq4)", "l")
      leg.Draw("same")
      c.SaveAs(targetDir + title)
      
    #makeDxyEffPlot(TEfficiency(firstSecondBin(L1Mu_genMu_dxy_fidT), firstSecondBin(genMu_dxy_fidT)), 
    #               "L1Mu_trigger_efficiency_dxy_fidT" + ext)
    makeDxyEffPlot(TEfficiency(firstSecondBin(L1Mu_genMu_lxy_fid), firstSecondBin(genMu_lxy_fid)),
                   TEfficiency(firstSecondBin(L1Mu_genMu_lxy_fid_Q), firstSecondBin(genMu_lxy_fid)), 
                   TEfficiency(firstSecondBin(L1Mu_genMu_lxy_fid_BX_Q), firstSecondBin(genMu_lxy_fid)),
                   TEfficiency(firstSecondBin(L1Mu_genMu_lxy_fid_BX_Q_V), firstSecondBin(genMu_lxy_fid)),
                   TEfficiency(firstSecondBin(L1Mu_genMu_lxy_fid_BX_Q_V_I), firstSecondBin(genMu_lxy_fid)),
                   "L1Mu_trigger_efficiency_lxy_fid" + ext)

    makeDxyEffPlot(TEfficiency(firstSecondBin(L1Mu_genMu_dxy_fid), firstSecondBin(genMu_dxy_fid)),
                   TEfficiency(firstSecondBin(L1Mu_genMu_dxy_fid_Q), firstSecondBin(genMu_dxy_fid)), 
                   TEfficiency(firstSecondBin(L1Mu_genMu_dxy_fid_BX_Q), firstSecondBin(genMu_dxy_fid)),
                   TEfficiency(firstSecondBin(L1Mu_genMu_dxy_fid_BX_Q_V), firstSecondBin(genMu_dxy_fid)),
                   TEfficiency(firstSecondBin(L1Mu_genMu_dxy_fid_BX_Q_V_I), firstSecondBin(genMu_dxy_fid)),
                   "L1Mu_trigger_efficiency_dxy_fid" + ext)

    makeDxyEffPlot(TEfficiency(firstSecondBin(L1Mu_genMu_dxy_fid_barrel), firstSecondBin(genMu_dxy_fid_barrel)),
                   TEfficiency(firstSecondBin(L1Mu_genMu_dxy_fid_Q_barrel), firstSecondBin(genMu_dxy_fid_barrel)), 
                   TEfficiency(firstSecondBin(L1Mu_genMu_dxy_fid_BX_Q_barrel), firstSecondBin(genMu_dxy_fid_barrel)),
                   TEfficiency(firstSecondBin(L1Mu_genMu_dxy_fid_BX_Q_V_barrel), firstSecondBin(genMu_dxy_fid_barrel)),
                   TEfficiency(firstSecondBin(L1Mu_genMu_dxy_fid_BX_Q_V_I_barrel), firstSecondBin(genMu_dxy_fid_barrel)),
                   "L1Mu_trigger_efficiency_dxy_fid_barrel" + ext)

    makeDxyEffPlot(TEfficiency(firstSecondBin(L1Mu_genMu_dxy_fid_overlap), firstSecondBin(genMu_dxy_fid_overlap)),
                   TEfficiency(firstSecondBin(L1Mu_genMu_dxy_fid_Q_overlap), firstSecondBin(genMu_dxy_fid_overlap)), 
                   TEfficiency(firstSecondBin(L1Mu_genMu_dxy_fid_BX_Q_overlap), firstSecondBin(genMu_dxy_fid_overlap)),
                   TEfficiency(firstSecondBin(L1Mu_genMu_dxy_fid_BX_Q_V_overlap), firstSecondBin(genMu_dxy_fid_overlap)),
                   TEfficiency(firstSecondBin(L1Mu_genMu_dxy_fid_BX_Q_V_I_overlap), firstSecondBin(genMu_dxy_fid_overlap)),
                   "L1Mu_trigger_efficiency_dxy_fid_overlap" + ext)
 
    makeDxyEffPlot(TEfficiency(firstSecondBin(L1Mu_genMu_dxy_fid_endcap), firstSecondBin(genMu_dxy_fid_endcap)),
                   TEfficiency(firstSecondBin(L1Mu_genMu_dxy_fid_Q_endcap), firstSecondBin(genMu_dxy_fid_endcap)), 
                   TEfficiency(firstSecondBin(L1Mu_genMu_dxy_fid_BX_Q_endcap), firstSecondBin(genMu_dxy_fid_endcap)),
                   TEfficiency(firstSecondBin(L1Mu_genMu_dxy_fid_BX_Q_V_endcap), firstSecondBin(genMu_dxy_fid_endcap)),
                   TEfficiency(firstSecondBin(L1Mu_genMu_dxy_fid_BX_Q_V_I_endcap), firstSecondBin(genMu_dxy_fid_endcap)),
                   "L1Mu_trigger_efficiency_dxy_fid_endcap" + ext)

    """
    makeDxyEffPlot(TEfficiency(firstSecondBin(L1Mu_genMu_dxy_fid_BX_Q), firstSecondBin(genMu_dxy_fid)), 
                   "L1Mu_trigger_efficiency_dxy_fid_BX_Q" + ext)
    makeDxyEffPlot(TEfficiency(firstSecondBin(L1Mu_genMu_dxy_fid_BX_Q_V), firstSecondBin(genMu_dxy_fid)), 
                   "L1Mu_trigger_efficiency_dxy_fid_BX_Q_V" + ext)
    """               
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
