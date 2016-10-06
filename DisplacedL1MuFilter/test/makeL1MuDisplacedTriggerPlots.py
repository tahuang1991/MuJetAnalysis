import sys
sys.argv.append( '-b' )
import ROOT 
ROOT.gROOT.SetBatch(1)
ROOT.gErrorIgnoreLevel=1001

from Helpers import *
from ROOT import *

file = TFile("out_ana.root")
treeHits = file.Get("L1MuTree")

## Style
gStyle.SetStatStyle(0)
set_style()
  
## L1Mu pT trigger turn-on curves
def makeEffPlot(eff1, eff2, eff3, plotName, plotTitle, doPt=True):
      
    c = TCanvas("c","c",800,600)
    c.Clear() 
    
    gPad.SetTickx(1)
    gPad.SetTicky(1)
    c.SetGridx()
    c.SetGridy()
    
    gStyle.SetTitleStyle( 0 )
    gStyle.SetTitleAlign(13) ##// coord in top left
    gStyle.SetTitleX(0.)
    gStyle.SetTitleY(1.)
    gStyle.SetTitleW(1)
    gStyle.SetTitleH(0.058)
    gStyle.SetTitleBorderSize( 0 )
    
    gStyle.SetPadLeftMargin(0.126)
    gStyle.SetPadRightMargin(0.04)
    gStyle.SetPadTopMargin(0.06)
    gStyle.SetPadBottomMargin(0.13)
    gStyle.SetOptStat( 0 )
    gStyle.SetMarkerStyle(1)
    
    if doPt: 
        binLow = [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,12.0,14.0,16.0,18.0,20.0,24.0,28.0,32.0,36.0,42.0,50.0]
        ptbins = np.asarray(binLow)
        xaxisTitle = "True muon p_{T} [GeV]"
        b1 = TH1F("b1","b1", 50,0,50)
    else:    
        mmax = 2.5; xaxisTitle = "True Muon #eta"
        b1 = TH1F("b1","b1", 25, 0, mmax)
        
    #b1.GetYaxis().SetRangeUser(.01,100)
    b1.GetYaxis().SetTitleOffset(1.2)
    b1.SetMaximum(1.05)
    b1.SetMinimum(0.0)
    b1.GetYaxis().SetNdivisions(520)
    b1.GetYaxis().SetTitle("Trigger efficiency")
    b1.GetXaxis().SetTitle(xaxisTitle)
    b1.GetXaxis().SetTitleOffset(1.2)
    b1.GetXaxis().SetTitleSize(0.05)
    b1.GetYaxis().SetTitleSize(0.05)
    b1.GetXaxis().SetLabelSize(0.05)
    b1.GetYaxis().SetLabelSize(0.05)
    b1.SetTitle("           #scale[1.4]{#font[61]{CMS}} #font[52]{Simulation preliminary}                                                           14 TeV, 140 PU")

    #b1.SetTitle(plotTitle)
    b1.SetStats(0)
    b1.Draw()
    
    eff1.SetLineColor(kBlue)
    eff1.SetMarkerColor(kBlue)
    eff1.SetMarkerStyle(20)
    eff1.Draw("same")

    eff2.SetLineColor(kRed)
    eff2.SetMarkerColor(kRed)
    eff2.SetMarkerStyle(21)
    eff2.Draw("same")
    if eff3 is not None:
        eff3.SetLineColor(kGreen+2)
        eff3.SetMarkerColor(kGreen+2)
        eff3.SetMarkerStyle(22)
        eff3.Draw("same")

    ## get the pT cut from the title
    len_string = len('Prompt_L1MuPt')
    index = plotName.find('Prompt_L1MuPt')
    if index == -1:
        len_string = len('Displaced_L1MuPt')
        index = plotName.find('Displaced_L1MuPt')
    ptCut = plotName[index+len_string:index+len_string+2]
    ## check if the last character is a "_"
    if ptCut[-1] is '_':
        ptCut = ptCut[:-1]
    #print len_string, ptCut

    ## Split up plotTitle in two pieces
    algoName = plotTitle.split(";")[0]
    etaRegion = plotTitle.split(";")[1]
    #"Stub alignment algorithm"
    latex3 = TLatex(0.5, 0.6, algoName)
    latex3.SetTextSize(0.05)
    latex3.SetNDC()
    latex3.Draw("same")
    #0<|#eta|<0.9
    latex2 = TLatex(0.5, 0.5, etaRegion + ", p_{T}^{L1}>" + ptCut +  " GeV")
    latex2.SetTextSize(0.05)
    latex2.SetNDC()
    latex2.Draw("same")
    
    leg = TLegend(0.5,0.2,0.9,0.45,"","brNDC")
    leg.SetFillColor(kWhite)
    leg.SetBorderSize(1)
    leg.SetFillStyle(1001)
    leg.SetTextSize(0.05)
    #leg.SetHeader("L1Mu trigger p_{T} #geq " + ptCut +  " GeV")
    #leg.SetHeader("")
    leg.AddEntry(eff1,"|d_{xy}|<5 cm", "lp")
    leg.AddEntry(eff2,"5 <|d_{xy}|<50 cm", "lp")
    if eff3 is not None:
        leg.AddEntry(eff3,"50 <|d_{xy}|<100 cm", "lp")
    leg.Draw("same")
    c.SaveAs(plotName + ".png")
    c.SaveAs(plotName + ".pdf")
    c.SaveAs(plotName + ".C")
    

## plots
targetDir = 'myTestDir/'

for ptCut in ['3','5','7','10','15','20']:
    makeEffPlot(getEfficiency(treeHits, "(50,0,50)", "gen_pt", TCut("has_L1Mu && abs(gen_eta)<2.4 && abs(gen_dxy)<5"), TCut("L1Mu_pt>=%s"%(ptCut))),
                getEfficiency(treeHits, "(50,0,50)", "gen_pt", TCut("has_L1Mu && abs(gen_eta)<2.4 && abs(gen_dxy)>5 && abs(gen_dxy)<50"), TCut("L1Mu_pt>=%s"%(ptCut))),
                getEfficiency(treeHits, "(50,0,50)", "gen_pt", TCut("has_L1Mu && abs(gen_eta)<2.4 && abs(gen_dxy)>50 && abs(gen_dxy)<100"), TCut("L1Mu_pt>=%s"%(ptCut))),
                targetDir + "Prompt_L1MuPt%s_GenMuPt_eta00to24_dxy0to100"%(ptCut), "Prompt L1Mu algorithm;|#eta|<2.4")

    stationCut = TCut('ok_CSCTF_st1 && ok_CSCTF_st2 && ok_CSCTF_st3')

    etaCut = TCut('abs(gen_eta)>1.2 && abs(gen_eta)<1.6')
    baselineCut = AND(stationCut, etaCut)
    makeEffPlot(getEfficiency(treeHits, "(50,0,50)", "gen_pt", AND(TCut("has_L1Mu && abs(gen_dxy)<5"), baselineCut), TCut("DDY123_pt>=%s"%(ptCut))),
                getEfficiency(treeHits, "(50,0,50)", "gen_pt", AND(TCut("has_L1Mu && abs(gen_dxy)>5 && abs(gen_dxy)<50"), baselineCut), TCut("DDY123_pt>=%s"%(ptCut))),
                getEfficiency(treeHits, "(50,0,50)", "gen_pt", AND(TCut("has_L1Mu && abs(gen_dxy)>50 && abs(gen_dxy)<100"), baselineCut), TCut("DDY123_pt>=%s"%(ptCut))),
                targetDir + "Displaced_L1MuPt%s_GenMuPt_ME1_ME2_ME3_eta12to16_dxy0to100"%(ptCut), "Displaced L1Mu algorithm;1.2<|#eta|<1.6")

    etaCut = TCut('abs(gen_eta)>1.6 && abs(gen_eta)<2.2')
    baselineCut = AND(stationCut, etaCut)
    makeEffPlot(getEfficiency(treeHits, "(50,0,50)", "gen_pt", AND(TCut("has_L1Mu && abs(gen_dxy)<5"), baselineCut), TCut("DDY123_pt>=%s"%(ptCut))),
                getEfficiency(treeHits, "(50,0,50)", "gen_pt", AND(TCut("has_L1Mu && abs(gen_dxy)>5 && abs(gen_dxy)<50"), baselineCut), TCut("DDY123_pt>=%s"%(ptCut))),
                getEfficiency(treeHits, "(50,0,50)", "gen_pt", AND(TCut("has_L1Mu && abs(gen_dxy)>50 && abs(gen_dxy)<100"), baselineCut), TCut("DDY123_pt>=%s"%(ptCut))),
                targetDir + "Displaced_L1MuPt%s_GenMuPt_ME1_ME2_ME3_eta16to22_dxy0to100"%(ptCut), "Displaced L1Mu algorithm;1.6<|#eta|<2.2")

    etaCut = TCut('abs(gen_eta)>1.2 && abs(gen_eta)<2.4')
    baselineCut = AND(stationCut, etaCut)
    makeEffPlot(getEfficiency(treeHits, "(50,0,50)", "gen_pt", AND(TCut("has_L1Mu && abs(gen_dxy)<5"), baselineCut), TCut("DDY123_pt>=%s"%(ptCut))),
                getEfficiency(treeHits, "(50,0,50)", "gen_pt", AND(TCut("has_L1Mu && abs(gen_dxy)>5 && abs(gen_dxy)<50"), baselineCut), TCut("DDY123_pt>=%s"%(ptCut))),
                getEfficiency(treeHits, "(50,0,50)", "gen_pt", AND(TCut("has_L1Mu && abs(gen_dxy)>50 && abs(gen_dxy)<100"), baselineCut), TCut("DDY123_pt>=%s"%(ptCut))),
                targetDir + "Displaced_L1MuPt%s_GenMuPt_ME1_ME2_ME3_eta12to24_dxy0to100"%(ptCut), "Displaced L1Mu algorithm;1.2<|#eta|<2.4")
