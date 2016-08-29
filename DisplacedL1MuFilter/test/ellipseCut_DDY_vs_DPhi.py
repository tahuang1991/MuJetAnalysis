# Run quiet mode
import sys
sys.argv.append( '-b' )
import ROOT 
ROOT.gROOT.SetBatch(1)
from Helpers import *
ROOT.gErrorIgnoreLevel=1001
from ROOT import * 
import random

def frange(end,start=0,inc=0,precision=1):
    """A range function that accepts float increments."""
    import math

    if not start:
        start = end + 0.0
        end = 0.0
    else: end += 0.0

    if not inc:
        inc = 1.0
    count = int(math.ceil((start - end) / inc))

    L = [None] * count

    L[0] = end
    for i in (xrange(1,count)):
        L[i] = L[i-1] + inc
    return L

DisplacedL1MuTrigger_20160827_v3/DDY123_vs_deltaPhiGEM_pad2_pt20to100_eta16to22_dxy0to50_eee_withLCTFit_hist.root     DisplacedL1MuTrigger_20160827_v3/DDY123_vs_deltaPhiGEM_pad2_pt2to7_eta16to22_dxy0to5_eee_withLCTFit_hist.root
DisplacedL1MuTrigger_20160827_v3/DDY123_vs_deltaPhiGEM_pad2_pt20to100_eta16to22_dxy0to50_eee_withoutLCTFit_hist.root  DisplacedL1MuTrigger_20160827_v3/DDY123_vs_deltaPhiGEM_pad2_pt2to7_eta16to22_dxy0to5_eee_withoutLCTFit_hist.root
DisplacedL1MuTrigger_20160827_v3/DDY123_vs_deltaPhiGEM_pad2_pt20to100_eta16to22_dxy0to50_eoo_withLCTFit_hist.root     DisplacedL1MuTrigger_20160827_v3/DDY123_vs_deltaPhiGEM_pad2_pt2to7_eta16to22_dxy0to5_eoo_withLCTFit_hist.root
DisplacedL1MuTrigger_20160827_v3/DDY123_vs_deltaPhiGEM_pad2_pt20to100_eta16to22_dxy0to50_eoo_withoutLCTFit_hist.root  DisplacedL1MuTrigger_20160827_v3/DDY123_vs_deltaPhiGEM_pad2_pt2to7_eta16to22_dxy0to5_eoo_withoutLCTFit_hist.root
DisplacedL1MuTrigger_20160827_v3/DDY123_vs_deltaPhiGEM_pad2_pt20to100_eta16to22_dxy0to50_oee_withLCTFit_hist.root     DisplacedL1MuTrigger_20160827_v3/DDY123_vs_deltaPhiGEM_pad2_pt2to7_eta16to22_dxy0to5_oee_withLCTFit_hist.root
DisplacedL1MuTrigger_20160827_v3/DDY123_vs_deltaPhiGEM_pad2_pt20to100_eta16to22_dxy0to50_oee_withoutLCTFit_hist.root  DisplacedL1MuTrigger_20160827_v3/DDY123_vs_deltaPhiGEM_pad2_pt2to7_eta16to22_dxy0to5_oee_withoutLCTFit_hist.root
DisplacedL1MuTrigger_20160827_v3/DDY123_vs_deltaPhiGEM_pad2_pt20to100_eta16to22_dxy0to50_ooo_withLCTFit_hist.root     DisplacedL1MuTrigger_20160827_v3/DDY123_vs_deltaPhiGEM_pad2_pt2to7_eta16to22_dxy0to5_ooo_withLCTFit_hist.root
DisplacedL1MuTrigger_20160827_v3/DDY123_vs_deltaPhiGEM_pad2_pt20to100_eta16to22_dxy0to50_ooo_withoutLCTFit_hist.root  DisplacedL1MuTrigger_20160827_v3/DDY123_vs_deltaPhiGEM_pad2_pt2to7_eta16to22_dxy0to5_ooo_withoutLCTFit_hist.root

signalFile = TFile("DisplacedL1MuTrigger_20160826_v5/DDY123_vs_deltaPhiGEM_pad2_pt20to100_eta16to22_dxy0to100_withLCTFit_hist.root")
backgroundFile = TFile("DisplacedL1MuTrigger_20160826_v5/DDY123_vs_deltaPhiGEM_pad2_pt2to7_eta16to22_dxy0to5_withLCTFit_hist.root")

signalHist = signalFile.Get("DDY123_vs_deltaPhiGEM_pad2_pt20to100_eta16to22_dxy0to100_withLCTFit")
backgroundHist = backgroundFile.Get("DDY123_vs_deltaPhiGEM_pad2_pt2to7_eta16to22_dxy0to5_withLCTFit")

print signalHist
print backgroundHist

## draw an ellipse that includes 95% of the entries

signalAcceptance = 0.90

def getEllipse(x,y,a,b):
  return x*x/(a*a) + y*y/(b*b)

def passEllipse(x,y,a,b):
    return getEllipse(x,y,a,b) <= 1

def failEllipse(x,y,a,b):
    return getEllipse(x,y,a,b) > 1

def getBackgroundRejectionEllipse(a_axis, b_axis, signalHist, backgroundHist):
    signalEntriesTotal = signalHist.Integral()*1.0
    backgroundEntriesTotal = backgroundHist.Integral()*1.0

    entriesInEllipseSignal  = 0
    entriesOutEllipseBackground  = 0

    signalAcceptanceFactor = 0
    backgroundRejectionFactor = 0
    
    ## loop on entries in histogram
    for j in range(1,signalHist.GetNbinsX()+1):
        for k in range(1,signalHist.GetNbinsY()+1):
            
            ## get the bin centers
            signal_x = signalHist.GetXaxis().GetBinCenter(j)
            signal_y = signalHist.GetYaxis().GetBinCenter(k)

            background_x = backgroundHist.GetXaxis().GetBinCenter(j)
            background_y = backgroundHist.GetYaxis().GetBinCenter(k)

            ## signal passes
            if passEllipse(signal_x, signal_y, a_axis, b_axis):
                entriesInEllipseSignal += signalHist.GetBinContent(j,k)

            ## background fails
            if failEllipse(background_x, background_y, a_axis, b_axis):
                entriesOutEllipseBackground += backgroundHist.GetBinContent(j,k)

            ## current signal acceptance
            signalAcceptanceFactor = entriesInEllipseSignal / signalEntriesTotal

            ## current background rejection
            backgroundRejectionFactor = entriesOutEllipseBackground / backgroundEntriesTotal
            #if backgroundRejectionFactor<0.50:
            #    break
            #print j,k,signalAcceptanceFactor,backgroundRejectionFactor

    return signalAcceptanceFactor, backgroundRejectionFactor
            

## loop on a and b
a_range = frange(1, 2, 0.01)
b_range = frange(0.05, 0.1, 0.001)

preselected_axes_signalAcc_backRej = []

print signalHist.Integral() / signalHist.GetEntries(), backgroundHist.Integral() / backgroundHist.GetEntries()
    
if False: 
    for a_axis in a_range:
        for b_axis in b_range:
            signalAcceptanceFactor, backgroundRejectionFactor = getBackgroundRejectionEllipse(a_axis, b_axis, signalHist, backgroundHist)
            print "a", a_axis, "b", b_axis, signalAcceptanceFactor, backgroundRejectionFactor
            if signalAcceptanceFactor > .9:
                preselected_axes_signalAcc_backRej.append([a_axis, b_axis, signalAcceptanceFactor, backgroundRejectionFactor])
            
## preselection
#print preselected_axes_signalAcc_backRej
bestBackgroundRejectionFactor = 0
pbest = [0,0,0,0]  
for pp in preselected_axes_signalAcc_backRej:
    print pp
    if preselected_axes_signalAcc_backRej[2] > 0.9 and preselected_axes_signalAcc_backRej[3] > bestBackgroundRejectionFactor:
        bestBackgroundRejectionFactor = preselected_axes_signalAcc_backRej[3]
        pbest = pp

print "best", pbest
## get the a and b for which the signal acceptance > 0.90 with highest background rejection
#print np.argmax(np.max(preselected_axes_signalAcc_backRej, axis=2))
#preselected_axes_signalAcc_backRej = np.array(preselected_axes_signalAcc_backRej)
#print preselected_axes_signalAcc_backRej.argmax(axis=3)    

"""
bestBackgroundRejectionFactor = 0
pbest = [0,0,0,0]
for p in preselected_axes_signalAcc_backRej:
    print p
    if preselected_axes_signalAcc_backRej[3] > bestBackgroundRejectionFactor:
        bestBackgroundRejectionFactor = preselected_axes_signalAcc_backRej[3]
        p
"""

#print preselected_axes_signalAcc_backRej.max(axis=1)


#best [1.4600000000000004, 0.09900000000000005, 0.9009687836383208, 0.7896341463414634]


print "drawing ellipse"


def drawEllipse(hist, a, b, plotTitle, caption, doAcceptance=True):
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
    hist.SetTitle(caption)

    el2 = TEllipse(0,0,1.4600000000000004,0.09900000000000005);
    el2.SetLineColor(kGreen+1);
    el2.SetLineWidth(3);
    el2.SetFillStyle(4000)
    el2.SetPhimin(0)
    el2.SetPhimax(90)
    el2.Draw("same")

    if doAcceptance:
        tex2 = TLatex(0.15, 0.85, "Ellipse: acceptance=0.90")
        tex2.SetTextSize(0.05)
        tex2.SetNDC()
        tex2.Draw("same")
    else:
        tex2 = TLatex(0.15, 0.85, "Ellipse: rejection=0.79")
        tex2.SetTextSize(0.05)
        tex2.SetNDC()
        tex2.Draw("same")
        
    tex3 = TLatex(0.15, 0.8, "a=%.3f, b=%.3f"%(1.4600000000000004,0.09900000000000005))
    tex3.SetTextSize(0.05)
    tex3.SetNDC()
    tex3.Draw("same")
    
    c.SaveAs(plotTitle + "_ellipse.png")


a = 1.4600000000000004,
b = 0.09900000000000005

drawEllipse(signalHist, a, b, "DDY123_vs_deltaPhiGEM_pad2_pt20to100_eta16to22_dxy0to100_withLCTFit", 
            "Ellipse cut for Pad2, p_{T} > 20 GeV,  1.6 < eta < 1.8, |dxy|<100 ;#Delta#Delta Y_{123} [cm]; |#Delta#Phi_{dir}(GE11,GE21)|",
            doAcceptance=True)

drawEllipse(backgroundHist, a, b, "DDY123_vs_deltaPhiGEM_pad2_pt2to7_eta16to22_dxy0to5_withLCTFit", 
            "Ellipse cut for Pad2, 2 < p_{T} < 7 GeV,  1.6 < eta < 1.8, |dxy|<5 ;#Delta#Delta Y_{123} [cm]; |#Delta#Phi_{dir}(GE11,GE21)|", 
            doAcceptance=False)
