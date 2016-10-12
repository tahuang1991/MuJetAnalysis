import sys
sys.argv.append( '-b' )
import ROOT 
ROOT.gROOT.SetBatch(1)
ROOT.gErrorIgnoreLevel=1001

from Helpers import *
from ROOT import *

file = TFile("out_ana_pu0_displaced_L1Mu.root")
treeHits = file.Get("L1MuTree")

## plots
targetDir = 'DisplacedL1MuTrigger_20161012/'

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
    b1.SetTitle("           #scale[1.4]{#font[61]{CMS}} #font[52]{Simulation preliminary}                                                             14 TeV, 0 PU")

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
    leg.AddEntry(eff1,"|d_{xy}|<5 cm", "lp")
    if eff2 is not None:
        leg.AddEntry(eff2,"10<|d_{xy}|<50 cm", "lp")
    if eff3 is not None:
        leg.AddEntry(eff3,"50<|d_{xy}|<100 cm", "lp")
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

def generateEfficiencyPlots():

    ptbin_ = {}
    ddy123cut_ = {}

    ptbin_["12to14_oee"] =  [3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 11.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0, 36.0, 42.0]
    ddy123cut_["12to14_oee"] =  [15.555000000000001, 12.321, 10.038, 7.559, 5.53, 5.759, 4.263999999999999, 3.571, 2.915, 2.524, 2.461, 2.3619999999999997, 1.8090000000000002, 1.6630000000000003, 1.943, 1.31, 38.997, 1.188]
    ptbin_["12to14_ooo"] =  [2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 11.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0, 36.0, 42.0]
    ddy123cut_["12to14_ooo"] =  [12.617999999999999, 17.561999999999998, 10.072000000000001, 6.040666666666667, 4.5440000000000005, 3.629, 3.067, 2.4755000000000003, 2.0785, 1.822, 1.6145000000000003, 1.3926, 1.2873333333333334, 1.1250000000000004, 0.9985, 0.922, 0.8393333333333335, 0.7755000000000001, 0.8270000000000001]
    ptbin_["12to14_eee"] =  [2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 11.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0, 36.0, 42.0]
    ddy123cut_["12to14_eee"] =  [24.367, 30.807000000000002, 21.327, 13.045000000000002, 9.625000000000002, 7.577, 6.13, 5.029800000000001, 4.178, 3.5506666666666673, 3.0770000000000004, 2.7, 2.4233333333333333, 2.046, 1.8044, 1.5745000000000002, 1.4249999999999998, 1.1985, 1.1320000000000001]
    ptbin_["12to14_eoo"] =  [3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 11.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0, 36.0, 42.0]
    ddy123cut_["12to14_eoo"] =  [22.127000000000002, 11.668000000000001, 7.533, 5.157, 3.9405, 3.2680000000000002, 3.105, 2.242, 1.986, 1.8230000000000002, 1.6380000000000001, 1.615, 4.815, 0.964, 0.999, 0.539, 0.5640000000000001, 8.505]

    ptbin_["14to16_oee"] =  [2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 11.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0, 36.0, 42.0]
    ddy123cut_["14to16_oee"] =  [31.573, 15.142000000000001, 10.476, 8.738000000000001, 8.909, 12.936, 7.612, 3.7060000000000004, 3.0170000000000003, 2.6470000000000002, 2.729, 2.136, 1.752, 1.598, 4.841, 1.547, 30.291999999999998, 32.683, 0.41900000000000004]
    ptbin_["14to16_ooo"] =  [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 11.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0, 36.0, 42.0]
    ddy123cut_["14to16_ooo"] =  [8.829, 16.536, 12.246, 6.4639999999999995, 4.4935, 3.575, 3.0275, 2.527, 2.1275000000000004, 1.821, 1.602, 1.3696666666666668, 1.1795, 1.122, 1.0180000000000002, 0.9345, 0.8005, 0.7335, 0.6950000000000001, 0.616]
    ptbin_["14to16_eee"] =  [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 11.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0, 36.0, 42.0]
    ddy123cut_["14to16_eee"] =  [17.069, 27.317000000000004, 20.517000000000003, 13.019, 9.06, 7.281000000000001, 5.853000000000001, 5.263999999999999, 4.16, 3.4750000000000005, 3.0985, 2.5590000000000006, 2.41025, 2.233, 1.8362500000000002, 1.574, 1.3780000000000001, 1.331, 1.2209999999999999, 1.018]
    ptbin_["14to16_eoo"] =  [2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 11.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0, 36.0, 42.0]
    ddy123cut_["14to16_eoo"] =  [11.723, 10.046000000000001, 8.440999999999999, 5.003, 5.649, 5.492, 3.008, 2.4819999999999998, 4.481000000000001, 3.847, 1.365, 2.8649999999999998, 1.797, 1.022, 0.912, 2.891, 0.734, 0.736, 0.458]

    ptbin_["16to18_oee"] =  [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 11.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0, 36.0, 42.0]
    ddy123cut_["16to18_oee"] =  [32.899, 28.319000000000003, 19.297, 12.399000000000001, 10.593, 5.789000000000001, 5.908, 4.63, 4.132, 3.873, 2.886, 3.0540000000000003, 3.331, 1.766, 1.846, 2.031, 1.8130000000000002, 1.624, 2.285, 0.756]
    ptbin_["16to18_ooo"] =  [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 11.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0, 36.0, 42.0]
    ddy123cut_["16to18_ooo"] =  [21.369, 3.069, 28.824, 15.051, 7.726, 5.281000000000001, 3.435, 3.511, 2.885, 2.863, 2.06, 1.536, 1.51, 1.3065, 1.292, 1.614, 1.621, 1.124, 0.776, 1.454, 0.612]
    ptbin_["16to18_eee"] =  [2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 11.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0, 36.0, 42.0]
    ddy123cut_["16to18_eee"] =  [33.916000000000004, 24.296, 11.964, 8.105, 7.1765, 5.746, 4.8790000000000004, 3.98, 3.458, 3.004, 2.887, 2.3560000000000003, 2.2230000000000003, 1.768, 1.606, 1.879, 1.4060000000000001, 1.522, 1.274]
    ptbin_["16to18_eoo"] =  [0.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 11.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0, 36.0, 42.0]
    ddy123cut_["16to18_eoo"] =  [0.559, 25.675, 12.418000000000001, 7.037, 4.99, 4.146, 2.798, 3.209, 2.634, 1.8865, 1.729, 1.706, 1.72, 2.951, 1.8750000000000002, 0.8230000000000001, 1.0890000000000002, 1.092, 1.5730000000000002, 0.728]

    ptbin_["18to20_oee"] =  [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 11.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0, 36.0, 42.0]
    ddy123cut_["18to20_oee"] =  [31.854000000000003, 26.240000000000002, 14.273, 8.113, 5.819000000000001, 4.640499999999999, 4.137, 3.4555000000000002, 2.7590000000000003, 2.35, 2.1965, 1.818, 1.744, 1.5130000000000001, 1.532, 1.3910000000000002, 1.001, 0.772, 0.9560000000000001, 0.905]
    ptbin_["18to20_ooo"] =  [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 11.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0, 36.0, 42.0]
    ddy123cut_["18to20_ooo"] =  [11.799000000000001, 17.364, 9.19, 4.795, 4.2545, 3.056, 2.864, 2.182, 1.67, 1.665, 1.4910000000000003, 1.163, 1.234, 1.026, 0.8080000000000003, 0.9540000000000002, 2.488, 0.7490000000000001, 0.528, 0.904]
    ptbin_["18to20_eee"] =  [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 11.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0, 36.0, 42.0]
    ddy123cut_["18to20_eee"] =  [36.577, 25.178, 13.789000000000001, 8.374, 5.665, 5.256, 3.715, 3.438, 2.793, 2.438, 2.0330000000000004, 1.764, 1.6949999999999998, 1.54, 1.5250000000000004, 1.3125, 1.536, 1.48, 2.83, 0.797]
    ptbin_["18to20_eoo"] =  [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 11.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0, 36.0, 42.0]
    ddy123cut_["18to20_eoo"] =  [27.258, 16.248, 8.654, 4.259, 3.455, 2.6323333333333334, 2.212, 2.05, 1.677, 1.49, 1.314, 1.2095, 1.097, 0.9165, 1.056, 0.9795, 0.879, 0.79, 0.719, 0.654]

    ptbin_["20to22_oee"] =  [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 11.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0, 36.0, 42.0]
    ddy123cut_["20to22_oee"] =  [24.887999999999998, 14.677, 6.032500000000001, 4.785, 3.097, 3.482, 2.12, 1.9244999999999999, 2.0130000000000003, 1.838, 1.2763333333333333, 1.305, 2.265, 1.2049999999999998, 1.31, 0.776, 1.022, 1.1310000000000002, 0.624, 0.5660000000000001]
    ptbin_["20to22_ooo"] =  [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 11.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0, 36.0, 42.0]
    ddy123cut_["20to22_ooo"] =  [5.438, 21.278, 7.859000000000001, 5.0569999999999995, 3.257, 3.756, 2.347, 2.812, 1.205, 1.1515000000000002, 0.966, 0.8463333333333333, 0.8479999999999999, 1.653, 1.8900000000000001, 0.842, 0.7880000000000001, 0.77, 0.757, 0.9500000000000001, 0.627]
    ptbin_["20to22_eee"] =  [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 11.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0, 36.0, 42.0]
    ddy123cut_["20to22_eee"] =  [16.349, 22.498, 12.298000000000002, 9.24, 4.408, 3.49, 2.8040000000000003, 2.137, 1.977, 2.158, 1.47, 1.686, 1.417, 1.355, 0.96, 1.192, 0.87, 1.4275, 2.271, 1.1340000000000001, 1.066]
    ptbin_["20to22_eoo"] =  [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 11.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0, 36.0, 42.0]
    ddy123cut_["20to22_eoo"] =  [22.503, 9.357, 3.5580000000000003, 2.981, 4.0840000000000005, 2.6310000000000002, 1.5030000000000001, 1.4070000000000003, 1.7050000000000003, 1.3470000000000002, 2.82, 1.1390000000000002, 2.2359999999999998, 1.1480000000000001, 0.772, 0.562, 0.684, 0.47800000000000004, 1.1320000000000001, 0.713]

    ptbin_["22to24_oee"] =  [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 11.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0, 36.0, 42.0]
    ddy123cut_["22to24_oee"] =  [11.65, 7.131, 3.929, 2.0759999999999996, 2.81, 1.6320000000000001, 1.488, 1.253, 1.03, 2.5330000000000004, 0.894, 0.8625, 0.7565000000000001, 0.769, 0.7940000000000002, 0.8390000000000001, 0.7170000000000001, 0.764, 1.9120000000000001, 0.41500000000000004]
    ptbin_["22to24_ooo"] =  [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 11.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0, 36.0, 42.0]
    ddy123cut_["22to24_ooo"] =  [37.51, 4.186, 3.992, 1.9060000000000001, 1.303, 1.065, 1.019, 0.8560000000000001, 0.7770000000000001, 0.6950000000000002, 1.0430000000000001, 0.633, 0.642, 0.6845000000000001, 0.504, 0.45, 1.365, 0.5015000000000001, 1.028, 0.452]
    ptbin_["22to24_eee"] =  [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 11.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0, 36.0, 42.0]
    ddy123cut_["22to24_eee"] =  [12.25, 7.1530000000000005, 4.081, 2.4770000000000003, 2.0340000000000003, 1.5570000000000002, 1.5115, 1.473, 1.1815, 1.308, 0.8560000000000001, 0.658, 0.9180000000000001, 0.8770000000000001, 0.6395, 0.515, 0.632, 0.628, 0.75, 1.44]
    ptbin_["22to24_eoo"] =  [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 11.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0, 36.0, 42.0]
    ddy123cut_["22to24_eoo"] =  [39.99, 10.934, 4.067, 2.105, 1.5430000000000001, 1.622, 1.4975, 0.7675000000000001, 0.998, 0.6960000000000002, 0.6050000000000001, 0.754, 0.49450000000000005, 0.5390000000000001, 0.532, 0.5545000000000001, 0.532, 0.4045, 0.654, 0.731, 0.8240000000000001]


    def getDDY123Cut(parity, etaPart, ptCut):
        ME1ME2ME3ParityCases = ['oee','ooo','eee','eoo']
        etaRanges = ['12to14','14to16','16to18','18to20','20to22','22to24']
        #print etaRanges[etaPart] + "_" + ME1ME2ME3ParityCases[parity]
        ptbins = ptbin_[etaRanges[etaPart] + "_" + ME1ME2ME3ParityCases[parity]]
        ddy123cuts = ddy123cut_[etaRanges[etaPart] + "_" + ME1ME2ME3ParityCases[parity]]
        
        #print ptbins
        #print ddy123cuts
        pt_index = ptbins.index(ptCut)
        ddy123cut = ddy123cuts[pt_index]
        #print "10", pt_index, ddy123cut
        #print
        
        return ddy123cut


    stationCut = TCut('has_CSCTF==1 && ok_CSCTF_st1==1 && ok_CSCTF_st2==1 && ok_CSCTF_st3==1 && DDY123_withLCTFit<=40 && has_L1Mu==1')

    
    ## 12 to 14
    etaCut = TCut('partition==0')
    baselineCut = AND(stationCut, etaCut)

    eff0 = getEfficiency(treeHits, "gen_pt", AND(TCut("abs(gen_dxy)<5 && parity==0"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(0,0,9))))
    eff1 = getEfficiency(treeHits, "gen_pt", AND(TCut("abs(gen_dxy)<5 && parity==1"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(1,0,9))))
    eff2 = getEfficiency(treeHits, "gen_pt", AND(TCut("abs(gen_dxy)<5 && parity==2"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(2,0,9))))
    eff3 = getEfficiency(treeHits, "gen_pt", AND(TCut("abs(gen_dxy)<5 && parity==3"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(3,0,9))))

    eff0 += eff1
    eff0 += eff2
    eff0 += eff3

    eff10 = getEfficiency(treeHits,  "gen_pt", AND(TCut("abs(gen_dxy)>10 && abs(gen_dxy)<50 && parity==0"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(0,0,9))))
    eff11 = getEfficiency(treeHits,  "gen_pt", AND(TCut("abs(gen_dxy)>10 && abs(gen_dxy)<50 && parity==1"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(1,0,9))))
    eff12 = getEfficiency(treeHits,  "gen_pt", AND(TCut("abs(gen_dxy)>10 && abs(gen_dxy)<50 && parity==2"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(2,0,9))))
    eff13 = getEfficiency(treeHits,  "gen_pt", AND(TCut("abs(gen_dxy)>10 && abs(gen_dxy)<50 && parity==3"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(3,0,9))))

    eff10 += eff11
    eff10 += eff12
    eff10 += eff13

    makeEffPlot(eff0, eff10, None,
                targetDir + "Displaced_L1MuPt10_GenMuPt_ME1_ME2_ME3_eta12to14_dxy0to50", "Displaced L1Mu algorithm;1.2<|#eta|<1.4")

    ## 14 to 16
    etaCut = TCut('partition==1')
    baselineCut = AND(stationCut, etaCut)

    eff0 = getEfficiency(treeHits, "gen_pt", AND(TCut("abs(gen_dxy)<5 && parity==0"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(0,1,9))))
    eff1 = getEfficiency(treeHits, "gen_pt", AND(TCut("abs(gen_dxy)<5 && parity==1"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(1,1,9))))
    eff2 = getEfficiency(treeHits, "gen_pt", AND(TCut("abs(gen_dxy)<5 && parity==2"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(2,1,9))))
    eff3 = getEfficiency(treeHits, "gen_pt", AND(TCut("abs(gen_dxy)<5 && parity==3"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(3,1,9))))

    eff0 += eff1
    eff0 += eff2
    eff0 += eff3

    eff10 = getEfficiency(treeHits,  "gen_pt", AND(TCut("abs(gen_dxy)>10 && abs(gen_dxy)<50 && parity==0"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(0,1,9))))
    eff11 = getEfficiency(treeHits,  "gen_pt", AND(TCut("abs(gen_dxy)>10 && abs(gen_dxy)<50 && parity==1"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(1,1,9))))
    eff12 = getEfficiency(treeHits,  "gen_pt", AND(TCut("abs(gen_dxy)>10 && abs(gen_dxy)<50 && parity==2"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(2,1,9))))
    eff13 = getEfficiency(treeHits,  "gen_pt", AND(TCut("abs(gen_dxy)>10 && abs(gen_dxy)<50 && parity==3"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(3,1,9))))

    eff10 += eff11
    eff10 += eff12
    eff10 += eff13

    makeEffPlot(eff0, eff10, None,
                targetDir + "Displaced_L1MuPt10_GenMuPt_ME1_ME2_ME3_eta14to16_dxy0to50", "Displaced L1Mu algorithm;1.4<|#eta|<1.6")


    ## 16 to 18
    etaCut = TCut('partition==2')
    baselineCut = AND(stationCut, etaCut)

    eff0 = getEfficiency(treeHits, "gen_pt", AND(TCut("abs(gen_dxy)<5 && parity==0"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(0,2,9))))
    eff1 = getEfficiency(treeHits, "gen_pt", AND(TCut("abs(gen_dxy)<5 && parity==1"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(1,2,9))))
    eff2 = getEfficiency(treeHits, "gen_pt", AND(TCut("abs(gen_dxy)<5 && parity==2"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(2,2,9))))
    eff3 = getEfficiency(treeHits, "gen_pt", AND(TCut("abs(gen_dxy)<5 && parity==3"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(3,2,9))))

    eff0 += eff1
    eff0 += eff2
    eff0 += eff3

    eff10 = getEfficiency(treeHits,  "gen_pt", AND(TCut("abs(gen_dxy)>10 && abs(gen_dxy)<50 && parity==0"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(0,2,9))))
    eff11 = getEfficiency(treeHits,  "gen_pt", AND(TCut("abs(gen_dxy)>10 && abs(gen_dxy)<50 && parity==1"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(1,2,9))))
    eff12 = getEfficiency(treeHits,  "gen_pt", AND(TCut("abs(gen_dxy)>10 && abs(gen_dxy)<50 && parity==2"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(2,2,9))))
    eff13 = getEfficiency(treeHits,  "gen_pt", AND(TCut("abs(gen_dxy)>10 && abs(gen_dxy)<50 && parity==3"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(3,2,9))))

    eff10 += eff11
    eff10 += eff12
    eff10 += eff13

    makeEffPlot(eff0, eff10, None,
                targetDir + "Displaced_L1MuPt10_GenMuPt_ME1_ME2_ME3_eta16to18_dxy0to50", "Displaced L1Mu algorithm;1.6<|#eta|<1.8")


    ## 18 to 20
    etaCut = TCut('partition==3')
    baselineCut = AND(stationCut, etaCut)

    eff0 = getEfficiency(treeHits, "gen_pt", AND(TCut("abs(gen_dxy)<5 && parity==0"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(0,3,9))))
    eff1 = getEfficiency(treeHits, "gen_pt", AND(TCut("abs(gen_dxy)<5 && parity==1"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(1,3,9))))
    eff2 = getEfficiency(treeHits, "gen_pt", AND(TCut("abs(gen_dxy)<5 && parity==2"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(2,3,9))))
    eff3 = getEfficiency(treeHits, "gen_pt", AND(TCut("abs(gen_dxy)<5 && parity==3"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(3,3,9))))

    eff0 += eff1
    eff0 += eff2
    eff0 += eff3

    eff10 = getEfficiency(treeHits,  "gen_pt", AND(TCut("abs(gen_dxy)>10 && abs(gen_dxy)<50 && parity==0"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(0,3,9))))
    eff11 = getEfficiency(treeHits,  "gen_pt", AND(TCut("abs(gen_dxy)>10 && abs(gen_dxy)<50 && parity==1"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(1,3,9))))
    eff12 = getEfficiency(treeHits,  "gen_pt", AND(TCut("abs(gen_dxy)>10 && abs(gen_dxy)<50 && parity==2"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(2,3,9))))
    eff13 = getEfficiency(treeHits,  "gen_pt", AND(TCut("abs(gen_dxy)>10 && abs(gen_dxy)<50 && parity==3"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(3,3,9))))

    eff10 += eff11
    eff10 += eff12
    eff10 += eff13

    makeEffPlot(eff0, eff10, None,
                targetDir + "Displaced_L1MuPt10_GenMuPt_ME1_ME2_ME3_eta18to20_dxy0to50", "Displaced L1Mu algorithm;1.8<|#eta|<2.0")
        

    ## 20 to 22
    etaCut = TCut('partition==4')
    baselineCut = AND(stationCut, etaCut)

    eff0 = getEfficiency(treeHits, "gen_pt", AND(TCut("abs(gen_dxy)<5 && parity==0"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(0,4,9))))
    eff1 = getEfficiency(treeHits, "gen_pt", AND(TCut("abs(gen_dxy)<5 && parity==1"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(1,4,9))))
    eff2 = getEfficiency(treeHits, "gen_pt", AND(TCut("abs(gen_dxy)<5 && parity==2"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(2,4,9))))
    eff3 = getEfficiency(treeHits, "gen_pt", AND(TCut("abs(gen_dxy)<5 && parity==3"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(3,4,9))))

    eff0 += eff1
    eff0 += eff2
    eff0 += eff3

    eff10 = getEfficiency(treeHits,  "gen_pt", AND(TCut("abs(gen_dxy)>10 && abs(gen_dxy)<50 && parity==0"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(0,4,9))))
    eff11 = getEfficiency(treeHits,  "gen_pt", AND(TCut("abs(gen_dxy)>10 && abs(gen_dxy)<50 && parity==1"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(1,4,9))))
    eff12 = getEfficiency(treeHits,  "gen_pt", AND(TCut("abs(gen_dxy)>10 && abs(gen_dxy)<50 && parity==2"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(2,4,9))))
    eff13 = getEfficiency(treeHits,  "gen_pt", AND(TCut("abs(gen_dxy)>10 && abs(gen_dxy)<50 && parity==3"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(3,4,9))))

    eff10 += eff11
    eff10 += eff12
    eff10 += eff13

    makeEffPlot(eff0, eff10, None,
                targetDir + "Displaced_L1MuPt10_GenMuPt_ME1_ME2_ME3_eta20to22_dxy0to50", "Displaced L1Mu algorithm;2.0<|#eta|<2.2")


    ## 22 to 24
    etaCut = TCut('partition==5')
    baselineCut = AND(stationCut, etaCut)
    
    eff0 = getEfficiency(treeHits, "gen_pt", AND(TCut("abs(gen_dxy)<5 && parity==0"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(0,5,9))))
    eff1 = getEfficiency(treeHits, "gen_pt", AND(TCut("abs(gen_dxy)<5 && parity==1"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(1,5,9))))
    eff2 = getEfficiency(treeHits, "gen_pt", AND(TCut("abs(gen_dxy)<5 && parity==2"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(2,5,9))))
    eff3 = getEfficiency(treeHits, "gen_pt", AND(TCut("abs(gen_dxy)<5 && parity==3"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(3,5,9))))

    eff0 += eff1
    eff0 += eff2
    eff0 += eff3

    eff10 = getEfficiency(treeHits,  "gen_pt", AND(TCut("abs(gen_dxy)>10 && abs(gen_dxy)<50 && parity==0"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(0,5,9))))
    eff11 = getEfficiency(treeHits,  "gen_pt", AND(TCut("abs(gen_dxy)>10 && abs(gen_dxy)<50 && parity==1"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(1,5,9))))
    eff12 = getEfficiency(treeHits,  "gen_pt", AND(TCut("abs(gen_dxy)>10 && abs(gen_dxy)<50 && parity==2"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(2,5,9))))
    eff13 = getEfficiency(treeHits,  "gen_pt", AND(TCut("abs(gen_dxy)>10 && abs(gen_dxy)<50 && parity==3"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(3,5,9))))

    eff10 += eff11
    eff10 += eff12
    eff10 += eff13

    makeEffPlot(eff0, eff10, None,
                targetDir + "Displaced_L1MuPt10_GenMuPt_ME1_ME2_ME3_eta22to24_dxy0to50", "Displaced L1Mu algorithm;2.2<|#eta|<2.4")
    """
    makeEffPlot(eff1, eff11, None,
                targetDir + "Displaced_L1MuPt10_GenMuPt_ME1_ME2_ME3_eta22to24_dxy0to50_ooo", "Displaced L1Mu algorithm;2.2<|#eta|<2.4")
    makeEffPlot(eff2, eff12, None,
                targetDir + "Displaced_L1MuPt10_GenMuPt_ME1_ME2_ME3_eta22to24_dxy0to50_eee", "Displaced L1Mu algorithm;2.2<|#eta|<2.4")
    makeEffPlot(eff3, eff13, None,
                targetDir + "Displaced_L1MuPt10_GenMuPt_ME1_ME2_ME3_eta22to24_dxy0to50_eoo", "Displaced L1Mu algorithm;2.2<|#eta|<2.4")

    
    makeEffPlot(getEfficiency(treeHits, "(50,0,50)", "gen_pt", TCut("has_L1Mu==1 && abs(gen_eta)<2.4 && abs(gen_dxy)<5"), TCut("L1Mu_pt>=%s"%(ptCut))),
    getEfficiency(treeHits, "(50,0,50)", "gen_pt", TCut("has_L1Mu==1 && abs(gen_eta)<2.4 && abs(gen_dxy)>5 && abs(gen_dxy)<50"), TCut("L1Mu_pt>=%s"%(ptCut))),
    None,
    targetDir + "Prompt_L1MuPt%s_GenMuPt_eta00to24_dxy0to50"%(ptCut), "Prompt L1Mu algorithm;|#eta|<2.4")
    makeEffPlot(getEfficiency(treeHits, "(50,0,50)", "gen_pt", TCut("has_L1Mu==1 && abs(gen_eta)<2.4 && abs(gen_dxy)<5"), TCut("L1Mu_pt>=%s"%(ptCut))),
    getEfficiency(treeHits, "(50,0,50)", "gen_pt", TCut("has_L1Mu==1 && abs(gen_eta)<2.4 && abs(gen_dxy)>5 && abs(gen_dxy)<50"), TCut("L1Mu_pt>=%s"%(ptCut))),
    getEfficiency(treeHits, "(50,0,50)", "gen_pt", TCut("has_L1Mu==1 && abs(gen_eta)<2.4 && abs(gen_dxy)>50 && abs(gen_dxy)<100"), TCut("L1Mu_pt>=%s"%(ptCut))),
    targetDir + "Prompt_L1MuPt%s_GenMuPt_eta00to24_dxy0to100"%(ptCut), "Prompt L1Mu algorithm;|#eta|<2.4")
    """                 
    

def goldenL1MuPtPlots():

    ptbin = [
        2.0,   2.5,   3.0,   3.5,   4.0,   4.5,   5.0,   6.0,   7.0,   8.0,  
        10.0,  12.0,  14.0,  16.0,  18.0,  20.0,  25.0,  30.0,  35.0,  40.0,  
        45.0,  50.0,  60.0,  70.0,  80.0,  90.0, 100.0, 120.0, 140.0]
    ptbinString = [
        '2',   '2p5',   '3',   '3p5',   '4',   '4p5',   '5',   '6',   '7',   '8',  
        '10',  '12',  '14',  '16',  '18',  '20',  '25',  '30',  '35',  '40',  
        '45',  '50',  '60',  '70',  '80',  '90', '100', '120', '140']

    golden_pt_factor = {
        '12to14' : [
            '2',   '2p5',   '3',   '3p5',   '4',   '4p5',   1.,   '6',   '7',   '8',  
            '10',  '12',  '14',  '16',  '18',  1.5,  '25',  2,  '35',  '40',  
            '45',  '50',  '60',  '70',  '80',  '90', '100', '120', '140'],
        '14to16' : [
            '2',   '2p5',   '3',   '3p5',   '4',   '4p5',   '5',   '6',   '7',   '8',  
            '10',  '12',  '14',  '16',  '18',  '20',  '25',  '30',  '35',  '40',  
            '45',  '50',  '60',  '70',  '80',  '90', '100', '120', '140'],
        '16to18' : [
            '2',   '2p5',   '3',   '3p5',   '4',   '4p5',   '5',   '6',   '7',   '8',  
            '10',  '12',  '14',  '16',  '18',  '20',  '25',  '30',  '35',  '40',  
            '45',  '50',  '60',  '70',  '80',  '90', '100', '120', '140'],
        '18to20' : [
            '2',   '2p5',   '3',   '3p5',   '4',   '4p5',   '5',   '6',   '7',   '8',  
            '10',  '12',  '14',  '16',  '18',  '20',  '25',  '30',  '35',  '40',  
            '45',  '50',  '60',  '70',  '80',  '90', '100', '120', '140'],
        '20to22' : [
            '2',   '2p5',   '3',   '3p5',   '4',   '4p5',   '5',   '6',   '7',   '8',  
            '10',  '12',  '14',  '16',  '18',  '20',  '25',  '30',  '35',  '40',  
            '45',  '50',  '60',  '70',  '80',  '90', '100', '120', '140'],
        '22to24' : [
            '2',   '2p5',   '3',   '3p5',   '4',   '4p5',   '5',   '6',   '7',   '8',  
            '10',  '12',  '14',  '16',  '18',  '20',  '25',  '30',  '35',  '40',  
            '45',  '50',  '60',  '70',  '80',  '90', '100', '120', '140'],
        }

    #num =   treeHits.GetEntries("abs(L1Mu_eta)>2.2 && abs(L1Mu_eta)<2.4 && has_L1Mu==1 && abs(gen_dxy)<5 && ((L1Mu_pt*2) >=30) && gen_pt>=30 && gen_pt<35")
    #denom = treeHits.GetEntries("abs(L1Mu_eta)>2.2 && abs(L1Mu_eta)<2.4 && has_L1Mu==1 && abs(gen_dxy)<5 && gen_pt>=30 && gen_pt<35")
    #print float(num)/float(denom)

    ptbin = [
        1,   2.5,   3.0,   3.5,   4.0,   4.5,   5.0,   6.0,   7.0,   8.0,  
        10.0,  12.0,  14.0,  16.0,  18.0,  20.0,  25.0,  30.0,  35.0,  40.0,  
        45.0,  50.0,  60.0,  70.0,  80.0,  90.0, 100.0, 120.0, 140.0]

    for i in range(1,len(ptbin)-1):
        num =   treeHits.GetEntries("abs(L1Mu_eta)>1.2 && abs(L1Mu_eta)<1.4 && has_L1Mu==1 && abs(gen_dxy)<5 && ((L1Mu_pt) >=%f) && gen_pt>=%f && gen_pt<%f"%(ptbin[i], ptbin[i], ptbin[i+1]))
        denom = treeHits.GetEntries("abs(L1Mu_eta)>1.2 && abs(L1Mu_eta)<1.4 && has_L1Mu==1 && abs(gen_dxy)<5 && gen_pt>=%f && gen_pt<%f"%(ptbin[i], ptbin[i+1]))
        print ptbin[i], num, denom, float(num)/float(denom)
        
        


    return
    for ptCut, ptCutString in zip(ptbin, ptbinString):
        makeEffPlot(getEfficiency(treeHits, "(50,0,50)", "gen_pt", TCut("has_L1Mu==1 && abs(L1Mu_eta)>1.2 && abs(L1Mu_eta)<1.4 && abs(gen_dxy)<5"), TCut("L1Mu_pt>=%f"%(ptCut))),
                    None,
                    None,
                    targetDir + "Prompt_L1MuPt%s_GenMuPt_eta12to14_dxy0to5"%(ptCutString), "Prompt L1Mu algorithm;1.2<|#eta|<1.4")
        """
        makeEffPlot(getEfficiency(treeHits, "(50,0,50)", "gen_pt", TCut("has_L1Mu==1 && abs(L1Mu)>1.4 && abs(L1Mu)<1.6 && abs(gen_dxy)<5"), TCut("L1Mu_pt>=%f"%(ptCut))),
                    None,
                    None,
                    targetDir + "Prompt_L1MuPt%s_GenMuPt_eta14to16_dxy0to5"%(ptCutString), "Prompt L1Mu algorithm;1.4<|#eta|<1.6")

        makeEffPlot(getEfficiency(treeHits, "(50,0,50)", "gen_pt", TCut("has_L1Mu==1 && abs(L1Mu)>1.6 && abs(L1Mu)<1.8 && abs(gen_dxy)<5"), TCut("L1Mu_pt>=%f"%(ptCut))),
                    None,
                    None,
                    targetDir + "Prompt_L1MuPt%s_GenMuPt_eta16to18_dxy0to5"%(ptCutString), "Prompt L1Mu algorithm;1.6<|#eta|<1.8")

        makeEffPlot(getEfficiency(treeHits, "(50,0,50)", "gen_pt", TCut("has_L1Mu==1 && abs(L1Mu)>1.8 && abs(L1Mu)<2.0 && abs(gen_dxy)<5"), TCut("L1Mu_pt>=%f"%(ptCut))),
                    None,
                    None,
                    targetDir + "Prompt_L1MuPt%s_GenMuPt_eta18to20_dxy0to5"%(ptCutString), "Prompt L1Mu algorithm;1.8<|#eta|<2.0")

        makeEffPlot(getEfficiency(treeHits, "(50,0,50)", "gen_pt", TCut("has_L1Mu==1 && abs(L1Mu)>2.0 && abs(L1Mu)<2.2 && abs(gen_dxy)<5"), TCut("L1Mu_pt>=%f"%(ptCut))),
                    None,
                    None,
                    targetDir + "Prompt_L1MuPt%s_GenMuPt_eta20to22_dxy0to5"%(ptCutString), "Prompt L1Mu algorithm;2.0<|#eta|<2.2")

        makeEffPlot(getEfficiency(treeHits, "(50,0,50)", "gen_pt", TCut("has_L1Mu==1 && abs(L1Mu)>2.2 && abs(L1Mu)<2.4 && abs(gen_dxy)<5"), TCut("L1Mu_pt>=%f"%(ptCut))),
                    None,
                    None,
                    targetDir + "Prompt_L1MuPt%s_GenMuPt_eta22to24_dxy0to5"%(ptCutString), "Prompt L1Mu algorithm;2.2<|#eta|<2.4")
        """

def pt_vs_ddy123Plots():

    """
    print treeHits.GetEntries("abs(gen_eta)<2.4 && has_L1Mu==1")

    print
    print treeHits.GetEntries("abs(gen_eta)<1.2 && has_L1Mu==1")

    print
    print treeHits.GetEntries("abs(gen_eta)>1.2 && abs(gen_eta)<1.4 && has_L1Mu==1")
    print treeHits.GetEntries("abs(gen_eta)>1.4 && abs(gen_eta)<1.6 && has_L1Mu==1")
    print treeHits.GetEntries("abs(gen_eta)>1.6 && abs(gen_eta)<1.8 && has_L1Mu==1")
    print treeHits.GetEntries("abs(gen_eta)>1.8 && abs(gen_eta)<2.0 && has_L1Mu==1")
    print treeHits.GetEntries("abs(gen_eta)>2.0 && abs(gen_eta)<2.2 && has_L1Mu==1")
    print treeHits.GetEntries("abs(gen_eta)>2.2 && abs(gen_eta)<2.4 && has_L1Mu==1")

    print
    print treeHits.GetEntries("abs(gen_eta)>1.2 && abs(gen_eta)<1.4 && has_L1Mu==1 && has_CSCTF==1 && ok_CSCTF_st1==1 && ok_CSCTF_st2==1 && ok_CSCTF_st3==1")
    print treeHits.GetEntries("abs(gen_eta)>1.4 && abs(gen_eta)<1.6 && has_L1Mu==1 && has_CSCTF==1 && ok_CSCTF_st1==1 && ok_CSCTF_st2==1 && ok_CSCTF_st3==1")
    print treeHits.GetEntries("abs(gen_eta)>1.6 && abs(gen_eta)<1.8 && has_L1Mu==1 && has_CSCTF==1 && ok_CSCTF_st1==1 && ok_CSCTF_st2==1 && ok_CSCTF_st3==1")
    print treeHits.GetEntries("abs(gen_eta)>1.8 && abs(gen_eta)<2.0 && has_L1Mu==1 && has_CSCTF==1 && ok_CSCTF_st1==1 && ok_CSCTF_st2==1 && ok_CSCTF_st3==1")
    print treeHits.GetEntries("abs(gen_eta)>2.0 && abs(gen_eta)<2.2 && has_L1Mu==1 && has_CSCTF==1 && ok_CSCTF_st1==1 && ok_CSCTF_st2==1 && ok_CSCTF_st3==1")
    print treeHits.GetEntries("abs(gen_eta)>2.2 && abs(gen_eta)<2.4 && has_L1Mu==1 && has_CSCTF==1 && ok_CSCTF_st1==1 && ok_CSCTF_st2==1 && ok_CSCTF_st3==1")
    """

    binLow = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 
              7.0, 8.0, 9.0, 11.0, 12.0, 14.0, 
              16.0, 18.0, 20.0, 24.0, 28.0, 32.0,
              36.0, 42.0, 50.0]
    ptbins = np.asarray(binLow)
    
    for pp in range(0,6):
        
        #  ME1ME2ME3ParityCases = ['oee','ooo','eee','eoo']
        etaRanges = ['12to14','14to16','16to18','18to20','20to22','22to24']
        etaRangesString = ['1.2 #leq |#eta| #leq 1.4',
                           '1.4 #leq |#eta| #leq 1.6',
                           '1.6 #leq |#eta| #leq 1.8',
                           '1.8 #leq |#eta| #leq 2.0',
                           '2.0 #leq |#eta| #leq 2.2',
                           '2.2 #leq |#eta| #leq 2.4']
        
        yBinning = ["(4000,0.,40.)", "(4000,0.,40.)","(4000,0.,40.)","(4000,0.,40.)","(4000,0.,40.)","(4000,0.,40.)"]
        
        extraCut = TCut("has_L1Mu==1 && has_CSCTF==1 && ok_CSCTF_st1==1 && ok_CSCTF_st2==1 && ok_CSCTF_st3==1")
        makeSimplePlot(get_2D(treeHits, ptbins, yBinning[pp], "DDY123_withLCTFit:gen_pt", AND(TCut("abs(gen_dxy)<50 && partition==%d && parity==0"%(pp)), extraCut)), targetDir + "GenMuPt_vs_DDY123_withLCTFit_eta%s_oee.png"%(etaRanges[pp]),
                       "%s, parity: oee; True muon pT [GeV]; DDY123 [cm]"%(etaRangesString[pp]),"COLZ")
        makeSimplePlot(get_2D(treeHits, ptbins, yBinning[pp], "DDY123_withLCTFit:gen_pt", AND(TCut("abs(gen_dxy)<50 && partition==%d && parity==1"%(pp)), extraCut)), targetDir + "GenMuPt_vs_DDY123_withLCTFit_eta%s_ooo.png"%(etaRanges[pp]),"%s, parity: ooo; True muon pT [GeV]; DDY123 [cm]"%(etaRangesString[pp]),"COLZ")
        makeSimplePlot(get_2D(treeHits, ptbins, yBinning[pp], "DDY123_withLCTFit:gen_pt", AND(TCut("abs(gen_dxy)<50 && partition==%d && parity==2"%(pp)), extraCut)), targetDir + "GenMuPt_vs_DDY123_withLCTFit_eta%s_eee.png"%(etaRanges[pp]),"%s, parity: eee; True muon pT [GeV]; DDY123 [cm]"%(etaRangesString[pp]),"COLZ")
        makeSimplePlot(get_2D(treeHits, ptbins, yBinning[pp], "DDY123_withLCTFit:gen_pt", AND(TCut("abs(gen_dxy)<50 && partition==%d && parity==3"%(pp)), extraCut)), targetDir + "GenMuPt_vs_DDY123_withLCTFit_eta%s_eoo.png"%(etaRanges[pp]),"%s, parity: eoo; True muon pT [GeV]; DDY123 [cm]"%(etaRangesString[pp]),"COLZ")

        print "Cut", AND(TCut("abs(gen_dxy)<50 && partition==%d && parity==0"%(pp)), extraCut)
        lut1 = get1DHistogramFractionY(get_2D(treeHits, ptbins, yBinning[pp], "DDY123_withLCTFit:gen_pt", AND(TCut("abs(gen_dxy)<50 && partition==%d && parity==0"%(pp)), extraCut)), .90)
        print '    ptbin_["' + etaRanges[pp] + '_oee"] = ', lut1[0]
        print '    ddy123cut_["' + etaRanges[pp] + '_oee"] = ', lut1[1]

        lut1 = get1DHistogramFractionY(get_2D(treeHits, ptbins, yBinning[pp], "DDY123_withLCTFit:gen_pt", AND(TCut("abs(gen_dxy)<50 && partition==%d && parity==1"%(pp)), extraCut)), .90)
        print '    ptbin_["' + etaRanges[pp] + '_ooo"] = ', lut1[0]
        print '    ddy123cut_["' + etaRanges[pp] + '_ooo"] = ', lut1[1]

        lut1 = get1DHistogramFractionY(get_2D(treeHits, ptbins, yBinning[pp], "DDY123_withLCTFit:gen_pt", AND(TCut("abs(gen_dxy)<50 && partition==%d && parity==2"%(pp)), extraCut)), .90)
        print '    ptbin_["' + etaRanges[pp] + '_eee"] = ', lut1[0]
        print '    ddy123cut_["' + etaRanges[pp] + '_eee"] = ', lut1[1]

        lut1 = get1DHistogramFractionY(get_2D(treeHits, ptbins, yBinning[pp], "DDY123_withLCTFit:gen_pt", AND(TCut("abs(gen_dxy)<50 && partition==%d && parity==3"%(pp)), extraCut)), .90)
        print '    ptbin_["' + etaRanges[pp] + '_eoo"] = ', lut1[0]
        print '    ddy123cut_["' + etaRanges[pp] + '_eoo"] = ', lut1[1]
        print 
 
generateEfficiencyPlots()

#goldenL1MuPtPlots()
pt_vs_ddy123Plots()
