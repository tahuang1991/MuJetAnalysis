# Run quiet mode
import sys
sys.argv.append( '-b' )
import ROOT 
ROOT.gROOT.SetBatch(1)
#from Helpers import *
ROOT.gErrorIgnoreLevel=1001
from ROOT import * 
import random
import os
import numpy as np
from math import *

ROOT.gROOT.SetBatch(1)
#ROOT.gStyle.SetStatW(0.07)
#ROOT.gStyle.SetStatH(0.06)

ROOT.gStyle.SetOptStat(11110)

#ROOT.gStyle.SetErrorX(0)
#ROOT.gStyle.SetErrorY(0)

ROOT.gStyle.SetTitleStyle(0)
ROOT.gStyle.SetTitleAlign(13) ## coord in top left
ROOT.gStyle.SetTitleX(0.)
ROOT.gStyle.SetTitleY(1.)
ROOT.gStyle.SetTitleW(1)
ROOT.gStyle.SetTitleH(0.058)
ROOT.gStyle.SetTitleBorderSize(0)

ROOT.gStyle.SetPadLeftMargin(0.126)
ROOT.gStyle.SetPadRightMargin(0.10)
ROOT.gStyle.SetPadTopMargin(0.06)
ROOT.gStyle.SetPadBottomMargin(0.13)

ROOT.gStyle.SetMarkerStyle(1)

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

    L = [None] * (count+1)

    L[0] = end
    for i in (xrange(1,count)):
        L[i] = L[i-1] + inc
    L[count] = start
    return L

def addFilesToChain(ch, filedir):
    if os.path.isdir(filedir):
    	  ls = os.listdir(filedir)
    	  for x in ls:
	      	if not(x.endswith(".root")):
			#print "x.endswith(.root) ", x.endswith(".root")
			continue
		x = filedir[:]+x
    		if os.path.isdir(x):
			continue
		ch.Add(x)
    elif os.path.isfile(filedir):
	  ch.Add(filedir)
    else:
	  print " it is not file or dir ", filedir

## draw an ellipse that includes 95% of the entries

def getEllipse(x,y,a,b, alpha=0, x0=0, y0=0):
  rad_alpha = alpha/180*2*pi
  x1 = x*cos(rad_alpha)+y*sin(rad_alpha)-x0
  y1 = x*sin(rad_alpha)-y*cos(rad_alpha)-y0
  #print "x ",x," y ",y," a ",a," b ",b," alpha ",alpha*180/pi," x1 ",x1," y1 ",y1
  return x1*x1/(a*a) + y1*y1/(b*b)

def passEllipse(x,y,a,b,alpha, x0=0, y0=0):
    return getEllipse(x,y,a,b,alpha, x0, y0) <= 1.0

def failEllipse(x,y,a,b,alpha, x0=0, y0=0):
    return getEllipse(x,y,a,b,alpha,x0, y0) > 1.0

def getBackgroundRejectionEllipse(a_axis, b_axis, alpha, x0, y0, signalHist, backgroundHist):
    if signalHist.GetEntries()==0 or backgroundHist.GetEntries()==0:
    	print "warning!!! entries (S and B) ",signalHist.GetEntries(),backgroundHist.GetEntries()
    	return (1.0,0)
    #print "signal and bg, integral/entris ", signalHist.Integral() / signalHist.GetEntries(), backgroundHist.Integral() / backgroundHist.GetEntries()
    signalEntriesTotal = signalHist.GetEntries()*1.0
    backgroundEntriesTotal = backgroundHist.GetEntries()*1.0
    #backgroundIntegral = backgroundHist.Integral()
    #backgroundoverunderflow = backgroundEntriesTotal - backgroundIntegral

    entriesInEllipseSignal  = 0.0
    entriesOutEllipseBackground  = 0.0
    entriesInEllipseBackground  = 0.0

    signalAcceptanceFactor = 0.0
    background = 0.0
    
    ## loop on entries in histogram
    for j in range(1,signalHist.GetNbinsX()+1):
        for k in range(1,signalHist.GetNbinsY()+1):
            
            ## get the bin centers
            signal_x = signalHist.GetXaxis().GetBinCenter(j)
            signal_y = signalHist.GetYaxis().GetBinCenter(k)

            background_x = backgroundHist.GetXaxis().GetBinCenter(j)
            background_y = backgroundHist.GetYaxis().GetBinCenter(k)

            ## signal passes
            if passEllipse(signal_x, signal_y, a_axis, b_axis, alpha, x0, y0):
                entriesInEllipseSignal += signalHist.GetBinContent(j,k)

            ## background passes
            if passEllipse(background_x, background_y, a_axis, b_axis, alpha, x0, y0):
                entriesInEllipseBackground += backgroundHist.GetBinContent(j,k)
		#print "background event in j ",j," k ",k," : ",backgroundHist.GetBinContent(j,k)," total outellipse ",entriesOutEllipseBackground," backgroundEntriesTotal  ",backgroundEntriesTotal

    ## current signal acceptance
    signalAcceptanceFactor = entriesInEllipseSignal / signalEntriesTotal

    ## current background rejection, overflow and underflow should be excluded
    #background = (entriesOutEllipseBackground + backgroundoverunderflow) / backgroundEntriesTotal
    background = 1 - entriesInEllipseBackground/backgroundEntriesTotal
    #print "Signal in Ellipse ",entriesInEllipseSignal," entries ",signalEntriesTotal," BG in Ellipse ",entriesOutEllipseBackground," entries ",backgroundEntriesTotal," backgroundoverunderflow ",backgroundoverunderflow
            #if background<0.50:
            #    break
            #print j,k,signalAcceptanceFactor,background

    return signalAcceptanceFactor, background


def getEvents(ch, cut, nBinsX, minBinX, maxBinX, nBinsY, minBinY, maxBinY):
    hist = TH2F("hist","hist", nBinsX, minBinX, maxBinX, nBinsY, minBinY, maxBinY)
    ch.Draw("1:1>>hist",cut)
    return hist.GetEntries()


def getEffandRateFromEllipse(signalChain, backgroundChain, cuts, signalPtCut, signalX, signalY, backgroundX, backgroundY, a_axis, b_axis, alpha, x0, y0):
    newSignalX = "(%s*TMath::Cos(%f)+%s*TMath::Sin(%f)-%f)"%(signalX, alpha, signalY, alpha, x0)
    newSignalY = "(%s*TMath::Sin(%f)-%s*TMath::Cos(%f)-%f)"%(signalX, alpha, signalY, alpha, y0)
    signalEllipse = "(%s*%s/(%f*%f)+%s*%s/(%f*%f))<=1.0"%(newSignalX, newSignalX, a_axis, a_axis, newSignalY, newSignalY, b_axis, b_axis)

    newBackgroundX = "(%s*TMath::Cos(%f)+%s*TMath::Sin(%f)-%f)"%(backgroundX, alpha, backgroundY, alpha, x0)
    newBackgroundY = "(%s*TMath::Sin(%f)-%s*TMath::Cos(%f)-%f)"%(backgroundX, alpha, backgroundY, alpha, y0)
    backgroundEllipse = "(%s*%s/(%f*%f)+%s*%s/(%f*%f))<=1.0"%(newBackgroundX, newBackgroundX, a_axis, a_axis, newBackgroundY, newBackgroundY, b_axis, b_axis)

    signalCut = "%s"%cuts + "&& sim_pt > %f"%signalPtCut 
    totSignal = getEvents(signalChain, signalCut, 100, -1, 1, 100, -1, 1)
    nsignal = getEvents(signalChain, signalCut + "&&" + signalEllipse, 100, -1, 1, 100, -1, 1)
    acceptance = float(nsignal) / float(totSignal)
    
    backgroundCut = cuts
    totBackground = getEvents(backgroundChain, backgroundCut, 100, -1, 1, 100, -1, 1)
    rejection = 1 - getEvents(backgroundChain, backgroundCut + "&&" + backgroundEllipse, 100, -1, 1, 100, -1, 1)/float(totBackground)
    return acceptance, rejection


def get2dHisto(tree, to_draw, cut, nBinsX, minBinX, maxBinX, nBinsY, minBinY, maxBinY):
    histo = TH2F("histo", "", nBinsX, minBinX, maxBinX, nBinsY, minBinY, maxBinY)
    tree.Draw(to_draw + ">>histo",cut)
    SetOwnership(histo, False)
    return histo


def addLatexText(x, y, text):
    print "Call addlatex"
    tex = ROOT.TLatex(x,y,"%s"%text)
    tex.SetTextSize(0.05)
    tex.SetTextFont(62)
    tex.SetNDC()
    tex.Draw("same")
    return tex
 
def drawEllipse(signalHist1, 
                signalHist2, 
                signalHist3, 
                rateHist, xtitle, ytitle, cTitle, a_axis, b_axis, alpha, x0, y0, acc, rej, pt):
    """takes 2 histograms, puts them on the same canvas and draws 2 ellipses"""
    gStyle.SetTitleBorderSize(0);
    gStyle.SetPadLeftMargin(0.126);
    gStyle.SetPadRightMargin(0.08);
    gStyle.SetPadTopMargin(0.06);
    gStyle.SetPadBottomMargin(0.13);
    gPad.SetTickx(1)
    gPad.SetTicky(1)

    el1 = TEllipse(x0,y0,a_axis,b_axis,0, 360, alpha);
    el1.SetLineColor(kRed);
    #el2.SetLineWidth(2);
    el1.SetFillStyle(0)
    
    c = TCanvas(cTitle,"",1000,1000)
    c.Divide(2,2)
    c.cd(1)
    signalHist1.Draw("colz")
    signalHist1.GetXaxis().SetTitle(xtitle)
    signalHist1.GetYaxis().SetTitle(ytitle)
    signalHist1.SetTitle("Signal, p_{T} > %d GeV"%pt)
    el1.Draw('same')
    tex1 = addLatexText(0.2, 0.87, "Acceptance: %f %%"%(acc))
    tex2 = addLatexText(0.2, 0.82, "a: %f"%a_axis)
    tex3 = addLatexText(0.2, 0.77, "b: %f"%b_axis)
    tex4 = addLatexText(0.2, 0.72, "#alpha: %f"%alpha)

    c.cd(2)
    signalHist2.Draw("colz")
    signalHist2.GetXaxis().SetTitle(xtitle)
    signalHist2.GetYaxis().SetTitle(ytitle)
    signalHist2.SetTitle("Signal, p_{T} > %d GeV, 10 < dxy < 20 cm"%pt)
    el1.Draw('same')
    tex11 = addLatexText(0.2, 0.82, "a: %f"%a_axis)
    tex12 = addLatexText(0.2, 0.77, "b: %f"%b_axis)
    tex13 = addLatexText(0.2, 0.72, "#alpha: %f"%alpha)

    c.cd(3)
    signalHist3.Draw("colz")
    signalHist3.GetXaxis().SetTitle(xtitle)
    signalHist3.GetYaxis().SetTitle(ytitle)
    signalHist3.SetTitle("Signal, p_{T} > %d GeV, 20 < dxy < 10 cm"%pt)
    el1.Draw('same')
    tex21 = addLatexText(0.2, 0.82, "a: %f"%a_axis)
    tex22 = addLatexText(0.2, 0.77, "b: %f"%b_axis)
    tex23 = addLatexText(0.2, 0.72, "#alpha: %f"%alpha)

    c.cd(4)
    rateHist.Draw("colz")
    rateHist.GetXaxis().SetTitle(xtitle)
    rateHist.GetYaxis().SetTitle(ytitle)
    rateHist.SetTitle("Background")
    el1.Draw('same')
    tex41 = addLatexText(0.2, 0.87, "Rejection: %f %%"%(rej))
    tex42 = addLatexText(0.2, 0.82, "a: %f"%a_axis)
    tex43 = addLatexText(0.2, 0.77, "b: %f"%b_axis)
    tex44 = addLatexText(0.2, 0.72, "#alpha: %f"%alpha)

    c.cd()
    c.SaveAs("BarrelEllipses_20170226/" + cTitle + ".C")
    c.SaveAs("BarrelEllipses_20170226/" + cTitle + ".pdf")


def drawEllipseTree(signalTree, rateTree, to_draw, cut, signalPtCut, signalBinning, rateBinning, xtitle, ytitle, cTitle, a_axis, b_axis, alpha, x0, y0, acc, rej, pt): #a, b, alpha, x0, y0, 

    [nBinsX, minBinX, maxBinX, nBinsY, minBinY, maxBinY] = signalBinning
    signalHist1 = get2dHisto(signalTree, to_draw, TCut("%s"%cut + "&& sim_pt > %f"%signalPtCut), nBinsX, minBinX, maxBinX, nBinsY, minBinY, maxBinY)

    [nBinsX, minBinX, maxBinX, nBinsY, minBinY, maxBinY] = signalBinning
    signalHist2 = get2dHisto(signalTree, to_draw, TCut("%s"%cut + "&& sim_pt > %f && abs(gen_dxy)>10 && abs(gen_dxy) < 20"%signalPtCut), nBinsX, minBinX, maxBinX, nBinsY, minBinY, maxBinY)

    [nBinsX, minBinX, maxBinX, nBinsY, minBinY, maxBinY] = signalBinning
    signalHist3 = get2dHisto(signalTree, to_draw, TCut("%s"%cut + "&& sim_pt > %f && abs(gen_dxy)>20 && abs(gen_dxy) < 50"%signalPtCut), nBinsX, minBinX, maxBinX, nBinsY, minBinY, maxBinY)

    [nBinsX, minBinX, maxBinX, nBinsY, minBinY, maxBinY] = rateBinning
    rateHist = get2dHisto(rateTree, to_draw, cut, nBinsX, minBinX, maxBinX, nBinsY, minBinY, maxBinY)

    drawEllipse(signalHist1, signalHist2, signalHist3, rateHist, xtitle, ytitle, cTitle, a_axis, b_axis, alpha, x0, y0, acc, rej, pt)


def drawEllipseTreeSimple(signalTree, rateTree, st11, st12, st21, st22, signalPtCut, a_axis, b_axis, alpha, x0, y0, acc, rej):    
    to_draw = "DTTF_phib%d_phib%d:DTTF_phib%d_phib%d"%(st11,st12,st21,st22)
    stationCut = "ok_DTTF_st%d && ok_DTTF_st%d && ok_DTTF_st%d && ok_DTTF_st%d"%(st11,st12,st21,st22)
    xTitle = "#Delta#Phi_{b}(MB%d,MB%d)"%(st11, st12)
    yTitle = "#Delta#Phi_{b}(MB%d,MB%d)"%(st21, st22)
    cTitle = "DPhib_MB%d_MB%d__DPhib_MB%d_MB%d__Pt%d"%(st11,st12,st21,st22,signalPtCut)
    signalBinning = [250, -0.5, 0.5, 250, -0.5, 0.5]
    rateBinning = [200, -1, 1, 200, -1, 1]
    drawEllipseTree(signalTree, rateTree, to_draw, stationCut, signalPtCut, signalBinning, rateBinning, xTitle, yTitle, cTitle, a_axis, b_axis, alpha, x0, y0, acc, rej, signalPtCut)

    
def drawEllipseTreeSimple2(signalTree, rateTree, combination, signalPtCut, a_axis, b_axis, alpha, x0, y0, acc, rej):
    st11 = combination[0][0]
    st12 = combination[0][1]
    st21 = combination[1][0]
    st22 = combination[1][1]
    drawEllipseTreeSimple(signalTree, rateTree, st11, st12, st21, st22, signalPtCut, a_axis, b_axis, alpha, x0, y0, acc, rej)


def drawEllipseTreeSimpleAbs(signalTree, rateTree, st11, st12, st21, st22, a_axis, b_axis, alpha):    
    to_draw = "abs(DTTF_phib%d_phib%d):abs(DTTF_phib%d_phib%d)"%(st11,st12,st21,st22)
    stationCut = "ok_DTTF_st%d && ok_DTTF_st%d && ok_DTTF_st%d && ok_DTTF_st%d"%(st11,st12,st21,st22)
    xTitle = "#Delta#Phi_{b}(MB%d,MB%d)"%(st11, st12)
    yTitle = "#Delta#Phi_{b}(MB%d,MB%d)"%(st21, st22)
    cTitle = "DPhib_MB%d_MB%d__DPhib_MB%d_MB%d__abs"%(st11,st12,st21,st22)
    signalBinning = [250, -0.5, 0.5, 250, -0.5, 0.5]
    rateBinning = [200, -1, 1, 200, -1, 1]
    drawEllipseTree(signalTree, rateTree, to_draw, stationCut, signalBinning, rateBinning, xTitle, yTitle, cTitle, a_axis, b_axis, alpha)


def getEllipseCut(signalTree, rateTree, st11, st12, st21, st22, signalPtCut, a_axis, b_axis, alpha, x0, y0):
    to_draw = "abs(DTTF_phib%d_phib%d):abs(DTTF_phib%d_phib%d)"%(st11,st12,st21,st22)
    stationCut = "ok_DTTF_st%d && ok_DTTF_st%d && ok_DTTF_st%d && ok_DTTF_st%d"%(st11,st12,st21,st22)
    signalBinning = [250, -0.5, 0.5, 250, -0.5, 0.5]
    rateBinning = [200, -1, 1, 200, -1, 1]
    ### OLDER CODE BELOW 
    #[nBinsX, minBinX, maxBinX, nBinsY, minBinY, maxBinY] = signalBinning
    #signalHist1 = get2dHisto(signalTree, to_draw, TCut("%s"%stationCut + "&& sim_pt > %f"%signalPtCut), nBinsX, minBinX, maxBinX, nBinsY, minBinY, maxBinY)

    #[nBinsX, minBinX, maxBinX, nBinsY, minBinY, maxBinY] = rateBinning
    #rateHist = get2dHisto(rateTree, to_draw, stationCut, nBinsX, minBinX, maxBinX, nBinsY, minBinY, maxBinY)

    #signalAcceptanceFactor, backgroundRejectionFactor = getBackgroundRejectionEllipse(a_axis, b_axis, alpha, x0, y0, signalHist1, rateHist)
    signalX =  "DTTF_phib%d_phib%d"%(st11,st12)
    signalY =  "DTTF_phib%d_phib%d"%(st21,st22)
    backgroundX = signalX
    backgroundY = signalY
    acceptance, rejection = getEffandRateFromEllipse(signalTree, rateTree, stationCut, signalPtCut, signalX, signalY, backgroundX, backgroundY, a_axis, b_axis, alpha, x0, y0)
    return acceptance, rejection


def getEllipseCutTuple(signalTree, rateTree, signalPtCut, combination, a_axis, b_axis, alpha, x0, y0):
    first = combination[0]
    second = combination[1] 
    acceptance, rejection = getEllipseCut(signalTree, rateTree, first[0], first[1], second[0], second[1], signalPtCut, a_axis, b_axis, alpha, x0, y0)
    return acceptance, rejection 


DT_dPhi_combinations = [
        ((1, 2),(1, 3)),
        ((1, 2),(1, 4)),
        ((1, 2),(2, 3)),
        ((1, 2),(2, 4)),
        ((1, 2),(3, 4)),
        ((1, 3),(1, 4)),
        ((1, 3),(2, 3)),
        ((1, 3),(2, 4)),
        ((1, 3),(3, 4)),
        ((1, 4),(2, 3)),
        ((1, 4),(2, 4)),
        ((1, 4),(3, 4)),
        ((2, 3),(2, 4)),
        ((2, 3),(3, 4)),
        ((2, 4),(3, 4)),
        ]


def getNominalAlpha(combination):
    nominal_alphas = {
        ((1, 2),(1, 3)) : 25.,
        ((1, 2),(1, 4)) : 10.,
        ((1, 2),(2, 3)) : 30.,
        ((1, 2),(2, 4)) : 15.,
        ((1, 2),(3, 4)) : 30.,
        
        ((1, 3),(1, 4)) : 30.,
        ((1, 3),(2, 3)) : 50.,
        ((1, 3),(2, 4)) : 40.,
        ((1, 3),(3, 4)) : 50.,
        
        ((1, 4),(2, 3)) : 70.,
        ((1, 4),(2, 4)) : 40.,
        ((1, 4),(3, 4)) : 70.,
        
        ((2, 3),(2, 4)) : 35.,
        ((2, 3),(3, 4)) : 40.,
        
        ((2, 4),(3, 4)) : 60.,
        }
    return nominal_alphas[combination]


############################################################################################################################################
############################################################################################################################################
############################################################ E X E C U T I O N ############################################################ 
############################################################################################################################################
############################################################################################################################################


signalFile = TFile.Open("out_ana_pu140_displaced_L1Mu_DDY123_StubRec_20170224.root")
rateFile = TFile.Open("Neutrino_Pt2to20_gun_TTI2023Upg14D_PU140bx25_ILT_SLHC14_20170224_BarrelTree.root")

signalTree = signalFile.Get("L1MuTree")
rateTree = rateFile.Get("L1MuTriggerRate")

nSignalEvents = signalTree.GetEntries()
nRateEvents = rateTree.GetEntries()

print "nSignalEvents", nSignalEvents, "nRateEvents", nRateEvents
signalAcceptance = 0.90

"""
## get the nominal alphas
## dot not remove!!!
#(1, 2) (1, 3)
drawEllipseTreeSimple(signalTree, rateTree, 1, 2, 1, 3, 10, 0.15, 0.04, 25)
#(1, 2) (1, 4)
drawEllipseTreeSimple(signalTree, rateTree, 1, 2, 1, 4, 10, 0.15, 0.04, 10)        
#(1, 2) (2, 3)
drawEllipseTreeSimple(signalTree, rateTree, 1, 2, 2, 3, 10, 0.15, 0.04, 30)        
#(1, 2) (2, 4)
drawEllipseTreeSimple(signalTree, rateTree, 1, 2, 2, 4, 10, 0.15, 0.04, 15)        
#(1, 2) (3, 4)
drawEllipseTreeSimple(signalTree, rateTree, 1, 2, 3, 4, 10, 0.15, 0.04, 30)        

#(1, 3) (1, 4)
drawEllipseTreeSimple(signalTree, rateTree, 1, 3, 1, 4, 10, 0.15, 0.04, 30)        
#(1, 3) (2, 3)
drawEllipseTreeSimple(signalTree, rateTree, 1, 3, 2, 3, 10, 0.15, 0.04, 50)        
#(1, 3) (2, 4)
drawEllipseTreeSimple(signalTree, rateTree, 1, 3, 2, 4, 10, 0.15, 0.04, 40)        
#(1, 3) (3, 4)
drawEllipseTreeSimple(signalTree, rateTree, 1, 3, 3, 4, 10, 0.15, 0.04, 50)        

#(1, 4) (2, 3)
drawEllipseTreeSimple(signalTree, rateTree, 1, 4, 2, 3, 10, 0.15, 0.04, 70)        
#(1, 4) (2, 4)
drawEllipseTreeSimple(signalTree, rateTree, 1, 4, 2, 4, 10, 0.15, 0.04, 50)        
#(1, 4) (3, 4)
drawEllipseTreeSimple(signalTree, rateTree, 1, 4, 3, 4, 10, 0.15, 0.04, 70)        

#(2, 3) (2, 4)
drawEllipseTreeSimple(signalTree, rateTree, 2, 3, 2, 4, 10, 0.15, 0.04, 30)        
#(2, 3) (3, 4)
drawEllipseTreeSimple(signalTree, rateTree, 2, 3, 3, 4, 10, 0.15, 0.04, 40)        

#(2, 4) (3, 4)
drawEllipseTreeSimple(signalTree, rateTree, 2, 4, 3, 4, 10, 0.15, 0.04, 60)        
"""

#getEllipseCutManyCombinations(signalTree, rateTree, 10, 0.07, 0.07)
#getEllipseCutTupleMany(signalTree, rateTree, 10, 0.07, 0.07)

bestAcceptance = 0
bestRejection = 0
bestA = 0
bestB = 0
bestAngle = 0

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)
arguments = sys.argv

ptCut = arguments[1]
print ptCut

combination = DT_dPhi_combinations[int(arguments[2])]
print combination

#combination = ((2, 4),(3, 4))
nIter=0
for a in np.arange(0.01,0.5,0.02):
    for b in np.arange(0.01,0.5,0.02):
        for c in range(-5,11):
            nIter += 1
            if nIter%1000==0:
                print "Processing", nIter
            a_axis = a
            b_axis = b
            alpha = getNominalAlpha(combination) + c
            print "a ", a_axis, "b", b_axis, "alpha", alpha
            acceptance, rejection = getEllipseCutTuple(signalTree, rateTree, int(ptCut), combination, a_axis, b_axis, alpha, 0, 0)
            #print "a ", a_axis, "b", b_axis, "alpha", alpha, "acceptance", acceptance, "rejection", rejection
            
            ## check if this combination is good
            if acceptance > 0.90:
                if rejection > bestRejection:
                    bestAcceptance = acceptance
                    bestRejection = rejection
                    bestA = a_axis
                    bestB = b_axis
                    bestAngle = alpha
                    #print "current best", bestAcceptance, bestRejection, bestA, bestB, bestAngle
print "nIter", nIter 
print "Combination", combination
print "Optimal values:"
print "CombinationNumber", int(arguments[2]), "ptCut", ptCut, "Acceptance", bestAcceptance, "Rejection", bestRejection, "bestA", bestA, "bestB", bestB, "bestAngle", bestAngle

drawEllipseTreeSimple2(signalTree, rateTree, combination, int(ptCut), bestA, bestB, bestAngle, 0, 0, bestAcceptance, bestRejection)
