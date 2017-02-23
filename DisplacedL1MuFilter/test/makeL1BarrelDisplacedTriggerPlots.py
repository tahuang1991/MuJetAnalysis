import sys
sys.argv.append( '-b' )
import ROOT
ROOT.gROOT.SetBatch(1)
#ROOT.gErrorIgnoreLevel=1001

from Helpers import *
from ROOT import *

file = TFile("out_ana_pu140_displaced_L1Mu_DDY123_StubRec_20170223.root")
treeHits = file.Get("L1MuTree")

## plots
targetDir = 'DisplacedL1MuTrigger_20170223_PU140_StubRecovery/'

## Style
gStyle.SetStatStyle(0)
set_style()

## copy index file
import shutil
shutil.copy2('index.php', targetDir + 'index.php')

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
    b1.SetTitle("           #scale[1.4]{#font[61]{CMS}} #font[52]{Simulation preliminary}                                                       14 TeV, 140 PU")

    #b1.SetTitle(plotTitle)
    b1.SetStats(0)
    b1.Draw()

    eff1.SetLineColor(kBlue)
    eff1.SetMarkerColor(kBlue)
    eff1.SetMarkerStyle(20)
    eff1.Draw("same")

    if eff2 is not None:
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
    if 'Veto' in plotName:
        leg.AddEntry(eff1,"5<|d_{xy}|<10 cm", "lp")
    else:
        leg.AddEntry(eff1,"|d_{xy}|<5 cm", "lp")
    if eff2 is not None:
        leg.AddEntry(eff2,"10<|d_{xy}|<50 cm", "lp")
    if eff3 is not None:
        leg.AddEntry(eff3,"50<|d_{xy}|<100 cm", "lp")
    leg.Draw("same")
    c.SaveAs(plotName + ".png")
    c.SaveAs(plotName + ".pdf")
    c.SaveAs(plotName + ".C")

## L1Mu pT trigger turn-on curves
def makeEffPlot2(eff1, eff2, eff3, plotName, plotTitle, doPt=True):

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
    b1.SetTitle("           #scale[1.4]{#font[61]{CMS}} #font[52]{Simulation preliminary}                                                         14 TeV, 0 PU")

    #b1.SetTitle(plotTitle)
    b1.SetStats(0)
    b1.Draw()

    eff1.SetLineColor(kBlue)
    eff1.SetMarkerColor(kBlue)
    eff1.SetMarkerStyle(20)
    eff1.Draw("same")

    if eff2 is not None:
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
    latex2 = TLatex(0.5, 0.5, etaRegion)
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
    if eff2 is not None:
        leg.AddEntry(eff2,"10<|d_{xy}|<50 cm", "lp")
    if eff3 is not None:
        leg.AddEntry(eff3,"50<|d_{xy}|<100 cm", "lp")
    leg.Draw("same")
    c.SaveAs(plotName + ".png")
    c.SaveAs(plotName + ".pdf")
    c.SaveAs(plotName + ".C")


## L1Mu pT trigger turn-on curves
def makeEffPlot3(eff1, legend1,
                 eff2, legend2,
                 eff3, legend3,
                 eff4, legend4,
                 plotName, plotTitle, doPt=True):

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
    b1.SetTitle("           #scale[1.4]{#font[61]{CMS}} #font[52]{Simulation preliminary}                                                     14 TeV, 140 PU")

    #b1.SetTitle(plotTitle)
    b1.SetStats(0)
    b1.Draw()

    eff1.SetLineColor(kRed)
    eff1.SetMarkerColor(kRed)
    eff1.SetMarkerStyle(20)
    eff1.Draw("same")

    if eff2 is not None:
        eff2.SetLineColor(kGreen+2)
        eff2.SetMarkerColor(kGreen+2)
        eff2.SetMarkerStyle(21)
        eff2.Draw("same")
    if eff3 is not None:
        eff3.SetLineColor(kBlue)
        eff3.SetMarkerColor(kBlue)
        eff3.SetMarkerStyle(22)
        eff3.Draw("same")
    if eff4 is not None:
        eff4.SetLineColor(kOrange+1)
        eff4.SetMarkerColor(kOrange+1)
        eff4.SetMarkerStyle(23)
        eff4.Draw("same")

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
    try:
        float(ptCut)
        latex2 = TLatex(0.5, 0.5, etaRegion + ", p_{T}^{L1}>" + ptCut +  " GeV")
        latex2.SetTextSize(0.05)
        latex2.SetNDC()
        latex2.Draw("same")
    except ValueError:
        latex2 = TLatex(0.5, 0.5, etaRegion)
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
    leg.AddEntry(eff1,legend1, "lp")
    if eff2 is not None:
        leg.AddEntry(eff2,legend2, "lp")
    if eff3 is not None:
        leg.AddEntry(eff3,legend3, "lp")
    if eff4 is not None:
        leg.AddEntry(eff4,legend4, "lp")
    leg.Draw("same")
    c.SaveAs(plotName + ".png")
    c.SaveAs(plotName + ".pdf")
    c.SaveAs(plotName + ".C")




def makeSimplePlot(hist, cTitle, title, option = ''):
    c = TCanvas("c","c",800,600)
    c.Clear()
    gStyle.SetTitleBorderSize(0);
    gStyle.SetPadLeftMargin(0.126);
    gStyle.SetPadRightMargin(0.04);
    gStyle.SetPadTopMargin(0.06);
    gStyle.SetPadBottomMargin(0.13);
    gPad.SetTickx(1)
    gPad.SetTicky(1)
    hist.Draw("colz")
    hist.SetTitle(title)
    hist2 = get1DHistogramFractionY(hist, fraction=.9)[2]
    gPad.Update()
    hist2.Draw("p same")
    gPad.Update()
    c.SaveAs(cTitle)



## comparison of prompt trigger efficiency for various trigger models (7)
def MuonTDR2017_BarrelTriggerEfficiency():
     
    preTitle = "L1"

    vetoCut = TCut("");                     postTitle=""

    stationCut = TCut("ok_DTTF_st1==1 && ok_DTTF_st4==1")
    ## prompt muon
    prompt_dxy5to10_pt = getEfficiency(treeHits, "sim_pt", AND(TCut("abs(gen_dxy)>0 && abs(gen_dxy)<5"), stationCut), TCut("L1Mu_pt>=15"))
    prompt_dxy10to50_pt = getEfficiency(treeHits, "sim_pt", AND(TCut("abs(gen_dxy)>10 && abs(gen_dxy)<50"), stationCut), TCut("L1Mu_pt>=10"))
    
    ptCut = TCut("sim_pt>=5")
    prompt_dxy5to10_eta = getEfficiency(treeHits, "sim_eta", AND(TCut("abs(gen_dxy)>5  && abs(gen_dxy)<10"), ptCut, stationCut), TCut("L1Mu_pt>=10"))
    prompt_dxy10to50_eta = getEfficiency(treeHits, "sim_eta", AND(TCut("abs(gen_dxy)>10  && abs(gen_dxy)<50"), ptCut, stationCut), TCut("L1Mu_pt>=10"))

    direction_dxy5to10_pt = getEfficiency(treeHits, "sim_pt", AND(TCut("abs(gen_dxy)>5  && abs(gen_dxy)<10"), stationCut), TCut("abs_DTTF_phib1_phib4<=0.07617314487632515"))
    direction_dxy10to50_pt = getEfficiency(treeHits, "sim_pt", AND(TCut("abs(gen_dxy)>10 && abs(gen_dxy)<50"), stationCut), TCut("abs_DTTF_phib1_phib4<=0.07617314487632515"))

    ptCut = TCut("sim_pt>=5")#DTTF_DT1_DT4_pt>=10
    direction_dxy5to10_eta = getEfficiencyEta(treeHits, "sim_eta", AND(TCut("abs(gen_dxy)>5  && abs(gen_dxy)<10"), stationCut, ptCut), TCut("abs_DTTF_phib1_phib4<=0.11520627802690593"))
    direction_dxy10to50_eta = getEfficiencyEta(treeHits, "sim_eta", AND(TCut("abs(gen_dxy)>10 && abs(gen_dxy)<50"), stationCut, ptCut), TCut("abs_DTTF_phib1_phib4<=0.11520627802690593"))

    """
    binLow = [4.0,5.0,6.0,7.0,8.0,9.0,10.0,12.0,14.0,16.0,18.0,20.0,24.0,28.0,32.0,36.0,42.0,50.0]
    Pt_dict['DT1_DT4'] =  [4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 11.0, 13.0, 15.0, 17.0, 19.0, 22.0, 26.0, 30.0, 34.0, 39.0, 46.0, 55.0]
    DPhi_dict['DT1_DT4'] =  [0.6350000000000002, 0.3602142857142858*1.3, 0.27009677419354844*1.15, 0.20673076923076922*1.15, 0.17068571428571422*1.1, 0.13912663755458526*0.8, 0.11520627802690593*1.14, 0.09131972789115654*1.1, 0.07617314487632515, 0.06748120300751885, 0.057713754646840185, 0.05274870017331027, 0.04392118226600989, 0.03952000000000001, 0.037006993006993026, 0.0378913043478261, 0.035904761904761925, 0.02742857142857146]

    """
    
    makeEffPlot3(prompt_dxy5to10_pt, "L1Mu (constrained)",
                 direction_dxy5to10_pt, "L1Mu (unconstrained)",
                 direction_dxy10to50_pt, "L1Mu (unconstrained)",
                 None, None,
                 targetDir + preTitle + "MuonTDR2017Displaced_L1MuPt10_SimMuPt_DT1_DT4_eta0to0p9_dxy5to50" + postTitle, "Displaced L1Mu algorithm;0<|#eta|<0.9")

MuonTDR2017_BarrelTriggerEfficiency()

## comparison of prompt trigger efficiency for various trigger models (7) + track veto

## acceptance of triggers for prompt muons
## compare the acceptance of barrel L1Mu trigger with 2 stations
def MuonTDR2017_BarrelTriggerAcceptance(station1, station2):
     
    preTitle = "L1"

    vetoCut = TCut("");                     postTitle=""

    stationCut = TCut("ok_DTTF_st%d==1 && ok_DTTF_st%d==1"%(station1, station2))
    extraCut = TCut("abs(sim_eta) < 0.9")

    dxy0to5_pt = getEfficiency(treeHits, "sim_pt", AND(extraCut, TCut("abs(gen_dxy)<5")), stationCut)
    dxy5to10_pt = getEfficiency(treeHits, "sim_pt", AND(extraCut, TCut("abs(gen_dxy)>5  && abs(gen_dxy)<10")), stationCut)
    dxy10to50_pt = getEfficiency(treeHits, "sim_pt", AND(extraCut, TCut("abs(gen_dxy)>10 && abs(gen_dxy)<50")), stationCut)

    makeEffPlot3(dxy0to5_pt, "|dxy| < 5",
                 dxy5to10_pt, "5 < |dxy| < 10",
                 dxy10to50_pt, "10 < |dxy| < 50",
                 None, None,
                 targetDir + preTitle + "MuonTDR2017Displaced_Acceptance_SimMuPt_DT%d_DT%d_eta0to0p9_dxy5to50"%(station1, station2) + postTitle, "hit in DT%d and DT%d;0<|#eta|<0.9"%(station1, station2))

MuonTDR2017_BarrelTriggerAcceptance(1,2)
MuonTDR2017_BarrelTriggerAcceptance(1,3)
MuonTDR2017_BarrelTriggerAcceptance(1,4)
MuonTDR2017_BarrelTriggerAcceptance(2,3)
MuonTDR2017_BarrelTriggerAcceptance(2,4)
MuonTDR2017_BarrelTriggerAcceptance(3,4)


def MuonTDR2017_BarrelTriggerAcceptanceAll():
     
    preTitle = "L1"

    vetoCut = TCut("");                     postTitle=""

    stationCut = TCut("ok_DTTF_st1==1 && ok_DTTF_st2==1")
    stationCut = OR(stationCut, TCut("ok_DTTF_st1==1 && ok_DTTF_st3==1"))
    stationCut = OR(stationCut, TCut("ok_DTTF_st1==1 && ok_DTTF_st4==1"))
    stationCut = OR(stationCut, TCut("ok_DTTF_st2==1 && ok_DTTF_st3==1"))
    stationCut = OR(stationCut, TCut("ok_DTTF_st2==1 && ok_DTTF_st4==1"))
    stationCut = OR(stationCut, TCut("ok_DTTF_st3==1 && ok_DTTF_st4==1"))
    extraCut = TCut("abs(sim_eta) < 0.9")

    dxy0to5_pt = getEfficiency(treeHits, "sim_pt", AND(extraCut, TCut("abs(gen_dxy)<5")), stationCut)
    dxy5to10_pt = getEfficiency(treeHits, "sim_pt", AND(extraCut, TCut("abs(gen_dxy)>5  && abs(gen_dxy)<10")), stationCut)
    dxy10to50_pt = getEfficiency(treeHits, "sim_pt", AND(extraCut, TCut("abs(gen_dxy)>10 && abs(gen_dxy)<50")), stationCut)

    makeEffPlot3(dxy0to5_pt, "|dxy| < 5",
                 dxy5to10_pt, "5 < |dxy| < 10",
                 dxy10to50_pt, "10 < |dxy| < 50",
                 None, None,
                 targetDir + preTitle + "MuonTDR2017Displaced_Acceptance_SimMuPt_DTX_DTY_eta0to0p9_dxy5to50" + postTitle, "hit in 2 DT stations;0<|#eta|<0.9")

MuonTDR2017_BarrelTriggerAcceptanceAll()
