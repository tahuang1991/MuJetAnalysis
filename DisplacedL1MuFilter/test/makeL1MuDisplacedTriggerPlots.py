import sys
sys.argv.append( '-b' )
import ROOT 
ROOT.gROOT.SetBatch(1)
ROOT.gErrorIgnoreLevel=1001

from Helpers import *
from ROOT import *

file = TFile("out_ana_pu140_displaced_L1Mu.root")
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
        leg.AddEntry(eff2,"5<|d_{xy}|<50 cm", "lp")
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

## plots
targetDir = 'DisplacedL1MuTrigger_20161006/'

def generateEfficiencyPlots():

    ptbin_ = {}
    ddy123cut_ = {}

    ptbin_["12to14_oee"] =  [3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0, 36.0, 42.0]
    ddy123cut_["12to14_oee"] =  [21.76, 19.240000000000002, 12.44, 8.16, 7.6000000000000005, 6.240000000000001, 4.220000000000001, 4.133333333333334, 3.3733333333333335, 2.6000000000000005, 2.4600000000000004, 2.3000000000000003, 1.7200000000000002, 1.8533333333333335, 1.7200000000000002, 1.1900000000000002, 39.080000000000005, 1.1600000000000001]
    ptbin_["12to14_ooo"] =  [2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0, 36.0, 42.0]
    ddy123cut_["12to14_ooo"] =  [12.64, 17.48, 10.013333333333334, 6.030769230769231, 4.7225, 3.68, 3.18139534883721, 2.7275000000000005, 2.272982456140351, 1.8803809523809525, 1.6095652173913046, 1.4596078431372552, 1.3575000000000002, 1.1600000000000001, 1.1032835820895524, 1.0320000000000003, 0.8950000000000004, 0.7888888888888889, 0.8560000000000003]
    ptbin_["12to14_eee"] =  [2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0, 36.0, 42.0]
    ddy123cut_["12to14_eee"] =  [25.84, 31.82, 21.400000000000006, 13.280000000000001, 9.625714285714288, 7.680000000000001, 6.201739130434783, 5.4, 4.510204081632653, 3.560373831775701, 3.107012987012987, 2.743783783783784, 2.4053333333333335, 2.0717948717948715, 1.9043902439024392, 1.581818181818182, 1.4609523809523812, 1.1978260869565218, 1.1440000000000001]
    ptbin_["12to14_eoo"] =  [3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0, 36.0, 42.0]
    ddy123cut_["12to14_eoo"] =  [22.24, 11.920000000000002, 8.280000000000001, 5.28, 4.48, 5.320000000000001, 4.0, 2.626666666666667, 2.146666666666667, 2.04, 1.6400000000000003, 1.86, 2.0800000000000005, 1.1533333333333333, 1.09, 0.7200000000000001, 0.56, 8.6]
    
    ptbin_["14to16_oee"] =  [2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0, 36.0, 42.0]
    ddy123cut_["14to16_oee"] =  [15.5, 15.02, 10.48, 8.73, 7.15, 8.300000000000002, 5.12, 5.140000000000001, 3.4600000000000004, 2.7640000000000002, 2.685, 3.6800000000000006, 1.7200000000000002, 1.6400000000000003, 4.6000000000000005, 1.1600000000000001, 13.260000000000002, 1.08, 0.5800000000000001]
    ptbin_["14to16_ooo"] =  [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0, 36.0, 42.0]
    ddy123cut_["14to16_ooo"] =  [9.16, 15.940000000000001, 11.266666666666667, 6.440000000000001, 4.546666666666667, 3.574117647058824, 3.0842857142857145, 2.5664285714285717, 2.2962500000000006, 1.9355555555555557, 1.6248648648648651, 1.390857142857143, 1.2088235294117649, 1.1543478260869564, 1.051219512195122, 0.9247368421052633, 0.8, 0.7659259259259261, 0.7437500000000001, 0.6400000000000002]
    ptbin_["14to16_eee"] =  [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0, 36.0, 42.0]
    ddy123cut_["14to16_eee"] =  [17.16, 19.14, 17.556, 12.140000000000002, 9.230000000000002, 7.335555555555556, 5.960000000000002, 5.286666666666667, 4.2690909090909095, 3.7783333333333333, 3.137777777777778, 2.5671794871794877, 2.4146666666666676, 2.210909090909091, 1.837931034482759, 1.5916279069767445, 1.3845454545454547, 1.3472727272727276, 1.2400000000000002, 1.08]
    ptbin_["14to16_eoo"] =  [2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0, 36.0, 42.0]
    ddy123cut_["14to16_eoo"] =  [11.660000000000002, 10.040000000000001, 9.360000000000001, 5.19, 5.6800000000000015, 5.42, 3.9400000000000004, 3.22, 4.58, 3.940000000000001, 3.18, 1.7000000000000002, 3.4600000000000004, 1.17, 0.9950000000000001, 5.6000000000000005, 0.7400000000000001, 0.7800000000000001, 0.56]
    
    ptbin_["16to18_oee"] =  [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0, 36.0, 42.0]
    ddy123cut_["16to18_oee"] =  [9.9, 6.08, 8.53, 8.81, 7.622000000000001, 5.720000000000001, 5.2675, 4.53, 4.39, 3.5766666666666667, 2.690000000000001, 2.55, 2.2, 2.1, 1.86, 1.54, 1.6400000000000003, 1.33, 2.25, 0.57]
    ptbin_["16to18_ooo"] =  [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0, 36.0, 42.0]
    ddy123cut_["16to18_ooo"] =  [9.9, 3.08, 9.64, 9.335, 6.880000000000001, 5.05, 3.41, 2.9000000000000004, 2.5566666666666666, 2.2150000000000003, 2.2600000000000002, 1.5539999999999998, 1.4725000000000001, 1.3325, 1.2733333333333334, 1.61, 1.0200000000000002, 0.9833333333333335, 0.7866666666666667, 1.2500000000000002, 0.6100000000000001]
    ptbin_["16to18_eee"] =  [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0, 36.0, 42.0]
    ddy123cut_["16to18_eee"] =  [9.9, 6.99, 9.095, 9.740000000000002, 7.870000000000002, 6.186666666666667, 5.57, 4.733333333333333, 3.6825, 3.636, 2.9166666666666674, 2.723333333333334, 2.3233333333333337, 2.08, 1.7722222222222226, 1.525, 1.7000000000000002, 1.4300000000000002, 1.52, 1.2400000000000002]
    ptbin_["16to18_eoo"] =  [0.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0, 36.0, 42.0]
    ddy123cut_["16to18_eoo"] =  [0.59, 9.97, 9.270000000000001, 6.46, 4.826666666666667, 3.97, 2.694, 3.18, 2.1199999999999997, 1.9240000000000002, 1.665, 1.8, 1.6700000000000008, 2.0900000000000003, 1.1949999999999998, 0.8233333333333335, 1.08, 1.0733333333333335, 1.3400000000000003, 0.7400000000000001]
    
    ptbin_["18to20_oee"] =  [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0, 36.0, 42.0]
    ddy123cut_["18to20_oee"] =  [0.6900000000000001, 9.440000000000001, 9.139999999999999, 7.15, 5.4, 4.506666666666667, 3.7950000000000004, 3.2450000000000006, 2.7433333333333336, 2.424000000000001, 2.1422222222222222, 1.7642857142857145, 1.61, 1.4375000000000002, 1.3814285714285717, 1.1928571428571428, 1.0025, 0.7866666666666667, 0.89, 0.7925000000000001]
    ptbin_["18to20_ooo"] =  [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0, 36.0, 42.0]
    ddy123cut_["18to20_ooo"] =  [9.9, 8.785000000000002, 7.94, 4.569999999999999, 3.6725000000000003, 2.6800000000000006, 2.2520000000000002, 2.0275000000000003, 1.6540000000000001, 1.5812500000000005, 1.4066666666666667, 1.1681818181818184, 1.0425000000000002, 0.9825, 0.7829166666666667, 0.8725000000000005, 0.892, 0.7000000000000001, 0.5519999999999999, 0.7500000000000002]
    ptbin_["18to20_eee"] =  [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0, 36.0, 42.0]
    ddy123cut_["18to20_eee"] =  [9.9, 9.260000000000002, 8.293333333333335, 7.330000000000001, 5.430000000000001, 4.470000000000001, 3.4300000000000006, 3.131666666666667, 2.664, 2.4725, 1.9555555555555557, 1.7327272727272731, 1.5566666666666673, 1.3583333333333334, 1.3775000000000006, 1.2828571428571431, 1.4400000000000002, 1.1600000000000001, 1.52, 0.7700000000000002]
    ptbin_["18to20_eoo"] =  [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0, 36.0, 42.0]
    ddy123cut_["18to20_eoo"] =  [9.9, 8.370000000000001, 7.385000000000001, 4.05, 3.4080000000000004, 2.54, 2.0600000000000005, 2.0116666666666667, 1.7300000000000002, 1.5077777777777779, 1.2625000000000002, 1.1981818181818185, 1.041666666666667, 0.8964705882352942, 0.9244444444444445, 0.9033333333333333, 0.7550000000000001, 0.7440000000000002, 0.7450000000000003, 0.6166666666666668]
    
    ptbin_["20to22_oee"] =  [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0, 36.0, 42.0]
    ddy123cut_["20to22_oee"] =  [3.4450000000000003, 3.285, 4.555, 4.535, 3.9625000000000004, 2.9000000000000004, 2.5399999999999996, 1.9366666666666668, 1.598888888888889, 1.6350000000000002, 1.53375, 1.1475, 1.2108333333333337, 1.0850000000000002, 1.0433333333333334, 0.7808333333333334, 0.66125, 0.7425, 0.77, 0.5875000000000001, 0.5800000000000001]
    ptbin_["20to22_ooo"] =  [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0, 36.0, 42.0]
    ddy123cut_["20to22_ooo"] =  [1.895, 3.875, 4.36, 3.6008333333333336, 2.52, 1.8550000000000006, 1.4800000000000002, 1.4233333333333333, 1.1380000000000001, 1.0125, 0.8796153846153848, 0.7391666666666669, 0.7337500000000001, 1.0233333333333334, 0.755, 0.5783333333333335, 0.6266666666666667, 0.6050000000000001, 0.5016666666666667, 0.6549999999999999, 0.6350000000000001]
    ptbin_["20to22_eee"] =  [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0, 36.0, 42.0]
    ddy123cut_["20to22_eee"] =  [4.95, 1.195, 4.605, 4.245, 3.7, 3.1633333333333336, 2.305000000000001, 1.9200000000000002, 1.6650000000000003, 1.63375, 1.4150000000000003, 1.2175000000000002, 1.165, 1.04, 0.8766666666666668, 0.9262500000000002, 0.6950000000000003, 0.8099999999999999, 0.6900000000000001, 0.5850000000000002, 1.08]
    ptbin_["20to22_eoo"] =  [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0, 36.0, 42.0]
    ddy123cut_["20to22_eoo"] =  [2.08, 4.53, 3.3533333333333335, 2.4350000000000005, 1.9212500000000001, 1.4533333333333336, 1.3907142857142858, 1.0383333333333333, 1.01, 1.0025, 0.8500000000000001, 0.7418750000000002, 0.8737500000000002, 0.5792857142857144, 0.607857142857143, 0.50625, 0.5650000000000001, 0.445, 0.8300000000000001, 0.5750000000000001]
    
    ptbin_["22to24_oee"] =  [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0, 36.0, 42.0]
    ddy123cut_["22to24_oee"] =  [4.9, 4.3149999999999995, 2.7950000000000004, 1.9950000000000006, 2.115, 1.465, 1.4050000000000002, 1.1362500000000002, 0.90625, 0.8725, 0.7383333333333335, 0.7310000000000001, 0.6616666666666667, 0.6850000000000003, 0.70125, 0.6100000000000002, 0.55, 0.7250000000000001, 0.7300000000000001, 0.42500000000000004]
    ptbin_["22to24_ooo"] =  [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0, 36.0, 42.0]
    ddy123cut_["22to24_ooo"] =  [4.485, 3.49, 2.02, 1.221666666666667, 1.11, 0.9625, 0.835, 0.6741666666666667, 0.7250000000000006, 0.6400000000000001, 0.637857142857143, 0.5283333333333335, 0.6066666666666668, 0.6420000000000001, 0.4658333333333333, 0.414, 0.8500000000000001, 0.4940000000000001, 1.04, 0.3650000000000001]
    ptbin_["22to24_eee"] =  [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0, 36.0, 42.0]
    ddy123cut_["22to24_eee"] =  [4.605, 3.7350000000000003, 2.7350000000000003, 1.833, 1.8, 1.3610000000000002, 1.3, 1.1450000000000002, 1.0266666666666666, 1.0266666666666666, 0.8375000000000001, 0.6391666666666669, 0.7925, 0.6566666666666668, 0.5675000000000001, 0.4783333333333334, 0.5266666666666667, 0.5275000000000001, 0.655, 1.4000000000000001]
    ptbin_["22to24_eoo"] =  [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0, 36.0, 42.0]
    ddy123cut_["22to24_eoo"] =  [4.95, 4.01, 3.21, 1.84, 1.2850000000000001, 1.195, 1.0975, 0.6980000000000001, 0.9590000000000001, 0.7025, 0.5306250000000001, 0.5610000000000003, 0.45249999999999996, 0.46250000000000013, 0.4975, 0.44722222222222224, 0.50625, 0.4, 0.5750000000000001, 0.66, 0.5750000000000001]


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


    stationCut = TCut('has_CSCTF==1 && ok_CSCTF_st1==1 && ok_CSCTF_st2==1 && ok_CSCTF_st3==1')
    hasL1Mu = TCut("has_L1Mu==1")

    
    ## 12 to 14
    etaCut = TCut('abs(L1Mu_eta)>1.2 && abs(L1Mu_eta)<1.4')
    baselineCut = AND(stationCut, etaCut)

    eff0 = getEfficiency(treeHits, "gen_pt", AND(TCut("has_L1Mu==1 && abs(gen_dxy)<5 && parity==0"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(0,0,10))))
    eff1 = getEfficiency(treeHits, "gen_pt", AND(TCut("has_L1Mu==1 && abs(gen_dxy)<5 && parity==1"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(1,0,10))))
    eff2 = getEfficiency(treeHits, "gen_pt", AND(TCut("has_L1Mu==1 && abs(gen_dxy)<5 && parity==2"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(2,0,10))))
    eff3 = getEfficiency(treeHits, "gen_pt", AND(TCut("has_L1Mu==1 && abs(gen_dxy)<5 && parity==3"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(3,0,10))))

    eff0 += eff1
    eff0 += eff2
    eff0 += eff3

    eff10 = getEfficiency(treeHits,  "gen_pt", AND(TCut("has_L1Mu==1 && abs(gen_dxy)>5 && abs(gen_dxy)<50 && parity==0"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(0,0,10))))
    eff11 = getEfficiency(treeHits,  "gen_pt", AND(TCut("has_L1Mu==1 && abs(gen_dxy)>5 && abs(gen_dxy)<50 && parity==1"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(1,0,10))))
    eff12 = getEfficiency(treeHits,  "gen_pt", AND(TCut("has_L1Mu==1 && abs(gen_dxy)>5 && abs(gen_dxy)<50 && parity==2"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(2,0,10))))
    eff13 = getEfficiency(treeHits,  "gen_pt", AND(TCut("has_L1Mu==1 && abs(gen_dxy)>5 && abs(gen_dxy)<50 && parity==3"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(3,0,10))))

    eff10 += eff11
    eff10 += eff12
    eff10 += eff13

    makeEffPlot(eff0, eff10, None,
                targetDir + "Displaced_L1MuPt10_GenMuPt_ME1_ME2_ME3_eta12to14_dxy0to50", "Displaced L1Mu algorithm;1.2<|#eta|<1.4")

    ## 14 to 16
    etaCut = TCut('abs(L1Mu_eta)>1.4 && abs(L1Mu_eta)<1.6')
    baselineCut = AND(stationCut, etaCut)

    eff0 = getEfficiency(treeHits, "gen_pt", AND(TCut("has_L1Mu==1 && abs(gen_dxy)<5 && parity==0"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(0,1,10))))
    eff1 = getEfficiency(treeHits, "gen_pt", AND(TCut("has_L1Mu==1 && abs(gen_dxy)<5 && parity==1"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(1,1,10))))
    eff2 = getEfficiency(treeHits, "gen_pt", AND(TCut("has_L1Mu==1 && abs(gen_dxy)<5 && parity==2"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(2,1,10))))
    eff3 = getEfficiency(treeHits, "gen_pt", AND(TCut("has_L1Mu==1 && abs(gen_dxy)<5 && parity==3"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(3,1,10))))

    eff0 += eff1
    eff0 += eff2
    eff0 += eff3

    eff10 = getEfficiency(treeHits,  "gen_pt", AND(TCut("has_L1Mu==1 && abs(gen_dxy)>5 && abs(gen_dxy)<50 && parity==0"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(0,1,10))))
    eff11 = getEfficiency(treeHits,  "gen_pt", AND(TCut("has_L1Mu==1 && abs(gen_dxy)>5 && abs(gen_dxy)<50 && parity==1"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(1,1,10))))
    eff12 = getEfficiency(treeHits,  "gen_pt", AND(TCut("has_L1Mu==1 && abs(gen_dxy)>5 && abs(gen_dxy)<50 && parity==2"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(2,1,10))))
    eff13 = getEfficiency(treeHits,  "gen_pt", AND(TCut("has_L1Mu==1 && abs(gen_dxy)>5 && abs(gen_dxy)<50 && parity==3"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(3,1,10))))

    eff10 += eff11
    eff10 += eff12
    eff10 += eff13

    makeEffPlot(eff0, eff10, None,
                targetDir + "Displaced_L1MuPt10_GenMuPt_ME1_ME2_ME3_eta14to16_dxy0to50", "Displaced L1Mu algorithm;1.4<|#eta|<1.6")


    ## 16 to 18
    etaCut = TCut('abs(L1Mu_eta)>1.6 && abs(L1Mu_eta)<1.8')
    baselineCut = AND(stationCut, etaCut)

    eff0 = getEfficiency(treeHits, "gen_pt", AND(TCut("has_L1Mu==1 && abs(gen_dxy)<5 && parity==0"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(0,2,10))))
    eff1 = getEfficiency(treeHits, "gen_pt", AND(TCut("has_L1Mu==1 && abs(gen_dxy)<5 && parity==1"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(1,2,10))))
    eff2 = getEfficiency(treeHits, "gen_pt", AND(TCut("has_L1Mu==1 && abs(gen_dxy)<5 && parity==2"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(2,2,10))))
    eff3 = getEfficiency(treeHits, "gen_pt", AND(TCut("has_L1Mu==1 && abs(gen_dxy)<5 && parity==3"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(3,2,10))))

    eff0 += eff1
    eff0 += eff2
    eff0 += eff3

    eff10 = getEfficiency(treeHits,  "gen_pt", AND(TCut("has_L1Mu==1 && abs(gen_dxy)>5 && abs(gen_dxy)<50 && parity==0"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(0,2,10))))
    eff11 = getEfficiency(treeHits,  "gen_pt", AND(TCut("has_L1Mu==1 && abs(gen_dxy)>5 && abs(gen_dxy)<50 && parity==1"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(1,2,10))))
    eff12 = getEfficiency(treeHits,  "gen_pt", AND(TCut("has_L1Mu==1 && abs(gen_dxy)>5 && abs(gen_dxy)<50 && parity==2"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(2,2,10))))
    eff13 = getEfficiency(treeHits,  "gen_pt", AND(TCut("has_L1Mu==1 && abs(gen_dxy)>5 && abs(gen_dxy)<50 && parity==3"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(3,2,10))))

    eff10 += eff11
    eff10 += eff12
    eff10 += eff13

    makeEffPlot(eff0, eff10, None,
                targetDir + "Displaced_L1MuPt10_GenMuPt_ME1_ME2_ME3_eta16to18_dxy0to50", "Displaced L1Mu algorithm;1.6<|#eta|<1.8")


    ## 18 to 20
    etaCut = TCut('abs(L1Mu_eta)>1.8 && abs(L1Mu_eta)<2.0')
    baselineCut = AND(stationCut, etaCut)

    eff0 = getEfficiency(treeHits, "gen_pt", AND(TCut("has_L1Mu==1 && abs(gen_dxy)<5 && parity==0"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(0,3,10))))
    eff1 = getEfficiency(treeHits, "gen_pt", AND(TCut("has_L1Mu==1 && abs(gen_dxy)<5 && parity==1"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(1,3,10))))
    eff2 = getEfficiency(treeHits, "gen_pt", AND(TCut("has_L1Mu==1 && abs(gen_dxy)<5 && parity==2"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(2,3,10))))
    eff3 = getEfficiency(treeHits, "gen_pt", AND(TCut("has_L1Mu==1 && abs(gen_dxy)<5 && parity==3"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(3,3,10))))

    eff0 += eff1
    eff0 += eff2
    eff0 += eff3

    eff10 = getEfficiency(treeHits,  "gen_pt", AND(TCut("has_L1Mu==1 && abs(gen_dxy)>5 && abs(gen_dxy)<50 && parity==0"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(0,3,10))))
    eff11 = getEfficiency(treeHits,  "gen_pt", AND(TCut("has_L1Mu==1 && abs(gen_dxy)>5 && abs(gen_dxy)<50 && parity==1"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(1,3,10))))
    eff12 = getEfficiency(treeHits,  "gen_pt", AND(TCut("has_L1Mu==1 && abs(gen_dxy)>5 && abs(gen_dxy)<50 && parity==2"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(2,3,10))))
    eff13 = getEfficiency(treeHits,  "gen_pt", AND(TCut("has_L1Mu==1 && abs(gen_dxy)>5 && abs(gen_dxy)<50 && parity==3"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(3,3,10))))

    eff10 += eff11
    eff10 += eff12
    eff10 += eff13

    makeEffPlot(eff0, eff10, None,
                targetDir + "Displaced_L1MuPt10_GenMuPt_ME1_ME2_ME3_eta18to20_dxy0to50", "Displaced L1Mu algorithm;1.8<|#eta|<2.0")
        

    ## 20 to 22
    etaCut = TCut('abs(L1Mu_eta)>2.0 && abs(L1Mu_eta)<2.2')
    baselineCut = AND(stationCut, etaCut)

    eff0 = getEfficiency(treeHits, "gen_pt", AND(TCut("has_L1Mu==1 && abs(gen_dxy)<5 && parity==0"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(0,4,10))))
    eff1 = getEfficiency(treeHits, "gen_pt", AND(TCut("has_L1Mu==1 && abs(gen_dxy)<5 && parity==1"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(1,4,10))))
    eff2 = getEfficiency(treeHits, "gen_pt", AND(TCut("has_L1Mu==1 && abs(gen_dxy)<5 && parity==2"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(2,4,10))))
    eff3 = getEfficiency(treeHits, "gen_pt", AND(TCut("has_L1Mu==1 && abs(gen_dxy)<5 && parity==3"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(3,4,10))))

    eff0 += eff1
    eff0 += eff2
    eff0 += eff3

    eff10 = getEfficiency(treeHits,  "gen_pt", AND(TCut("has_L1Mu==1 && abs(gen_dxy)>5 && abs(gen_dxy)<50 && parity==0"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(0,4,10))))
    eff11 = getEfficiency(treeHits,  "gen_pt", AND(TCut("has_L1Mu==1 && abs(gen_dxy)>5 && abs(gen_dxy)<50 && parity==1"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(1,4,10))))
    eff12 = getEfficiency(treeHits,  "gen_pt", AND(TCut("has_L1Mu==1 && abs(gen_dxy)>5 && abs(gen_dxy)<50 && parity==2"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(2,4,10))))
    eff13 = getEfficiency(treeHits,  "gen_pt", AND(TCut("has_L1Mu==1 && abs(gen_dxy)>5 && abs(gen_dxy)<50 && parity==3"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(3,4,10))))

    eff10 += eff11
    eff10 += eff12
    eff10 += eff13

    makeEffPlot(eff0, eff10, None,
                targetDir + "Displaced_L1MuPt10_GenMuPt_ME1_ME2_ME3_eta20to22_dxy0to50", "Displaced L1Mu algorithm;2.0<|#eta|<2.2")


    ## 22 to 24
    etaCut = TCut('abs(L1Mu_eta)>2.2 && abs(L1Mu_eta)<2.4')
    baselineCut = AND(stationCut, etaCut)
    
    eff0 = getEfficiency(treeHits, "gen_pt", AND(TCut("has_L1Mu==1 && abs(gen_dxy)<5 && parity==0"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(0,5,10))))
    eff1 = getEfficiency(treeHits, "gen_pt", AND(TCut("has_L1Mu==1 && abs(gen_dxy)<5 && parity==1"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(1,5,10))))
    eff2 = getEfficiency(treeHits, "gen_pt", AND(TCut("has_L1Mu==1 && abs(gen_dxy)<5 && parity==2"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(2,5,10))))
    eff3 = getEfficiency(treeHits, "gen_pt", AND(TCut("has_L1Mu==1 && abs(gen_dxy)<5 && parity==3"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(3,5,10))))

    eff0 += eff1
    eff0 += eff2
    eff0 += eff3

    eff10 = getEfficiency(treeHits,  "gen_pt", AND(TCut("has_L1Mu==1 && abs(gen_dxy)>5 && abs(gen_dxy)<50 && parity==0"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(0,5,10))))
    eff11 = getEfficiency(treeHits,  "gen_pt", AND(TCut("has_L1Mu==1 && abs(gen_dxy)>5 && abs(gen_dxy)<50 && parity==1"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(1,5,10))))
    eff12 = getEfficiency(treeHits,  "gen_pt", AND(TCut("has_L1Mu==1 && abs(gen_dxy)>5 && abs(gen_dxy)<50 && parity==2"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(2,5,10))))
    eff13 = getEfficiency(treeHits,  "gen_pt", AND(TCut("has_L1Mu==1 && abs(gen_dxy)>5 && abs(gen_dxy)<50 && parity==3"), baselineCut), TCut("DDY123_withLCTFit<=%f"%(getDDY123Cut(3,5,10))))

    eff10 += eff11
    eff10 += eff12
    eff10 += eff13

    makeEffPlot(eff0, eff10, None,
                targetDir + "Displaced_L1MuPt10_GenMuPt_ME1_ME2_ME3_eta22to24_dxy0to50", "Displaced L1Mu algorithm;2.2<|#eta|<2.4")


    """
    
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

    etaCut = TCut("has_L1Mu==1 && has_CSCTF==1 && ok_CSCTF_st1==1 && ok_CSCTF_st2==1 && ok_CSCTF_st3==1")
    binLow = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 
              7.0, 8.0, 9.0, 10.0, 12.0, 14.0, 
              16.0, 18.0, 20.0, 24.0, 28.0, 32.0,
              36.0, 42.0, 50.0]
    ptbins = np.asarray(binLow)
    
    for pp in range(0,6):
        
        #  ME1ME2ME3ParityCases = ['oee','ooo','eee','eoo']
        etaRanges = ['12to14','14to16','16to18','18to20','20to22','22to24']
        yBinning = ["(100,0.,40)", "(100,0.,20)", "(100,0.,10)", "(100,0.,10)", "(100,0.,5)", "(100,0.,5)"]
        
        makeSimplePlot(get_2D(treeHits, ptbins, yBinning[pp], "DDY123_withLCTFit:gen_pt", AND(TCut("partition==%d && parity==0"%(pp)), etaCut)), targetDir + "GenMuPt_vs_DDY123_withLCTFit_eta%s_oee.png"%(etaRanges[pp]),"","COLZ")
        makeSimplePlot(get_2D(treeHits, ptbins, yBinning[pp], "DDY123_withLCTFit:gen_pt", AND(TCut("partition==%d && parity==1"%(pp)), etaCut)), targetDir + "GenMuPt_vs_DDY123_withLCTFit_eta%s_ooo.png"%(etaRanges[pp]),"","COLZ")
        makeSimplePlot(get_2D(treeHits, ptbins, yBinning[pp], "DDY123_withLCTFit:gen_pt", AND(TCut("partition==%d && parity==2"%(pp)), etaCut)), targetDir + "GenMuPt_vs_DDY123_withLCTFit_eta%s_eee.png"%(etaRanges[pp]),"","COLZ")
        makeSimplePlot(get_2D(treeHits, ptbins, yBinning[pp], "DDY123_withLCTFit:gen_pt", AND(TCut("partition==%d && parity==3"%(pp)), etaCut)), targetDir + "GenMuPt_vs_DDY123_withLCTFit_eta%s_eoo.png"%(etaRanges[pp]),"","COLZ")

        """
        makeSimplePlot(get_2D(treeHits, ptbins, yBinning[pp], "DDY123_withoutLCTFit:gen_pt", AND(TCut("partition==%d && parity==0"%(pp)), etaCut)), targetDir + "GenMuPt_vs_DDY123_withoutLCTFit_eta%s_oee.png"%(etaRanges[pp]),"","COLZ")
        makeSimplePlot(get_2D(treeHits, ptbins, yBinning[pp], "DDY123_withoutLCTFit:gen_pt", AND(TCut("partition==%d && parity==2"%(pp)), etaCut)), targetDir + "GenMuPt_vs_DDY123_withoutLCTFit_eta%s_eee.png"%(etaRanges[pp]),"","COLZ")
        makeSimplePlot(get_2D(treeHits, ptbins, yBinning[pp], "DDY123_withoutLCTFit:gen_pt", AND(TCut("partition==%d && parity==3"%(pp)), etaCut)), targetDir + "GenMuPt_vs_DDY123_withoutLCTFit_eta%s_eoo.png"%(etaRanges[pp]),"","COLZ")
        makeSimplePlot(get_2D(treeHits, ptbins, yBinning[pp], "DDY123_withoutLCTFit:gen_pt", AND(TCut("partition==%d && parity==1"%(pp)), etaCut)), targetDir + "GenMuPt_vs_DDY123_withoutLCTFit_eta%s_ooo.png"%(etaRanges[pp]),"","COLZ")
        """

        lut1 = get1DHistogramFractionY(get_2D(treeHits, ptbins, yBinning[pp], "DDY123_withLCTFit:gen_pt", AND(TCut("partition==%d && parity==0"%(pp)), etaCut)), .90)
        print '    ptbin_["' + etaRanges[pp] + '_oee"] = ', lut1[0]
        print '    ddy123cut_["' + etaRanges[pp] + '_oee"] = ', lut1[1]
        lut1 = get1DHistogramFractionY(get_2D(treeHits, ptbins, yBinning[pp], "DDY123_withLCTFit:gen_pt", AND(TCut("partition==%d && parity==1"%(pp)), etaCut)), .90)
        print '    ptbin_["' + etaRanges[pp] + '_ooo"] = ', lut1[0]
        print '    ddy123cut_["' + etaRanges[pp] + '_ooo"] = ', lut1[1]
        lut1 = get1DHistogramFractionY(get_2D(treeHits, ptbins, yBinning[pp], "DDY123_withLCTFit:gen_pt", AND(TCut("partition==%d && parity==2"%(pp)), etaCut)), .90)
        print '    ptbin_["' + etaRanges[pp] + '_eee"] = ', lut1[0]
        print '    ddy123cut_["' + etaRanges[pp] + '_eee"] = ', lut1[1]
        lut1 = get1DHistogramFractionY(get_2D(treeHits, ptbins, yBinning[pp], "DDY123_withLCTFit:gen_pt", AND(TCut("partition==%d && parity==3"%(pp)), etaCut)), .90)
        print '    ptbin_["' + etaRanges[pp] + '_eoo"] = ', lut1[0]
        print '    ddy123cut_["' + etaRanges[pp] + '_eoo"] = ', lut1[1]
        print 
 
#generateEfficiencyPlots()

#goldenL1MuPtPlots()
pt_vs_ddy123Plots()
