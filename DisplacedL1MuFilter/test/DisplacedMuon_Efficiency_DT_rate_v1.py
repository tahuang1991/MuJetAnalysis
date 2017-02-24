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
  x1 = x*cos(alpha)+y*sin(alpha)-x0
  y1 = x*sin(alpha)-y*cos(alpha)-y0
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
            

def get2dHisto(tree, to_draw, cut, nBinsX, minBinX, maxBinX, nBinsY, minBinY, maxBinY):

    histo = TH2F("histo", "", nBinsX, minBinX, maxBinX, nBinsY, minBinY, maxBinY)
    tree.Draw(to_draw + ">>histo",cut)

    SetOwnership(histo, False)
    return histo

def drawEllipse(signalHist1, 
                signalHist2, 
                signalHist3, 
                rateHist, xtitle, ytitle, cTitle): #a, b, alpha, x0, y0, 
    """takes 2 histograms, puts them on the same canvas and draws 2 ellipses"""
    gStyle.SetTitleBorderSize(0);
    gStyle.SetPadLeftMargin(0.126);
    gStyle.SetPadRightMargin(0.08);
    gStyle.SetPadTopMargin(0.06);
    gStyle.SetPadBottomMargin(0.13);
    gPad.SetTickx(1)
    gPad.SetTicky(1)

    a_axis = 0.02*4
    b_axis = 0.02*4
    alpha = -20
    x0 = 0
    y0 = 0

    el1 = TEllipse(x0,y0,a_axis,b_axis,0,360, alpha*180.0/pi);
    el1.SetLineColor(kRed);
    #el2.SetLineWidth(2);
    el1.SetFillStyle(0)
    
    c = TCanvas(cTitle,"",1000,1000)
    c.Divide(2,2)
    c.cd(1)
    signalHist1.Draw("colz")
    signalHist1.GetXaxis().SetTitle(xtitle)
    signalHist1.GetYaxis().SetTitle(ytitle)
    signalHist1.SetTitle("Signal, p_{T} > 10 GeV, dxy < 10 cm")
    el1.Draw('same')

    c.cd(2)
    signalHist2.Draw("colz")
    signalHist2.GetXaxis().SetTitle(xtitle)
    signalHist2.GetYaxis().SetTitle(ytitle)
    signalHist2.SetTitle("Signal, p_{T} > 10 GeV, 10 < dxy < 20 cm")
    el1.Draw('same')

    c.cd(3)
    signalHist3.Draw("colz")
    signalHist3.GetXaxis().SetTitle(xtitle)
    signalHist3.GetYaxis().SetTitle(ytitle)
    signalHist3.SetTitle("Signal, p_{T} > 10 GeV, 20 < dxy < 10 cm")
    el1.Draw('same')

    c.cd(4)
    rateHist.Draw("colz")
    rateHist.GetXaxis().SetTitle(xtitle)
    rateHist.GetYaxis().SetTitle(ytitle)
    rateHist.SetTitle("Background")
    el1.Draw('same')

    c.cd()
    c.SaveAs("BarrelEllipses_20170224/" + cTitle + ".C")
    c.SaveAs("BarrelEllipses_20170224/" + cTitle + ".pdf")

    for a in range(50,200):
        a_axis = a/1000.
        b_axis = a/1000.
        signalAcceptanceFactor, backgroundRejectionFactor = getBackgroundRejectionEllipse(a_axis, b_axis, alpha, x0, y0, signalHist1, rateHist) 
        if signalAcceptanceFactor>0.90: 
            print a_axis, b_axis, signalAcceptanceFactor, backgroundRejectionFactor
            print ">>DONE"
            break


def drawEllipseTree(signalTree, rateTree, to_draw, cut, signalPtCut, signalBinning, rateBinning, xtitle, ytitle, cTitle): #a, b, alpha, x0, y0, 

    [nBinsX, minBinX, maxBinX, nBinsY, minBinY, maxBinY] = signalBinning
    signalHist1 = get2dHisto(signalTree, to_draw, TCut("%s"%cut + "&& sim_pt > %f"%signalPtCut), nBinsX, minBinX, maxBinX, nBinsY, minBinY, maxBinY)

    [nBinsX, minBinX, maxBinX, nBinsY, minBinY, maxBinY] = signalBinning
    signalHist2 = get2dHisto(signalTree, to_draw, TCut("%s"%cut + "&& sim_pt > %f && abs(gen_dxy)>10 && abs(gen_dxy) < 20"%signalPtCut), nBinsX, minBinX, maxBinX, nBinsY, minBinY, maxBinY)

    [nBinsX, minBinX, maxBinX, nBinsY, minBinY, maxBinY] = signalBinning
    signalHist3 = get2dHisto(signalTree, to_draw, TCut("%s"%cut + "&& sim_pt > %f && abs(gen_dxy)>20 && abs(gen_dxy) < 50"%signalPtCut), nBinsX, minBinX, maxBinX, nBinsY, minBinY, maxBinY)

    [nBinsX, minBinX, maxBinX, nBinsY, minBinY, maxBinY] = rateBinning
    rateHist = get2dHisto(rateTree, to_draw, cut, nBinsX, minBinX, maxBinX, nBinsY, minBinY, maxBinY)

    drawEllipse(signalHist1, signalHist2, signalHist3, rateHist, xtitle, ytitle, cTitle)


def drawEllipseTreeSimple(signalTree, rateTree, st11, st12, st21, st22, signalPtCut):    
    to_draw = "DTTF_phib%d_phib%d:DTTF_phib%d_phib%d"%(st11,st12,st21,st22)
    stationCut = "ok_DTTF_st%d && ok_DTTF_st%d && ok_DTTF_st%d && ok_DTTF_st%d"%(st11,st12,st21,st22)
    xTitle = "d#Phi_{b}(MB%d,MB%d)"%(st11, st12)
    yTitle = "d#Phi_{b}(MB%d,MB%d)"%(st21, st22)
    cTitle = "DPhib_MB%d_MB%d__DPhib_MB%d_MB%d"%(st11,st12,st21,st22)
    signalBinning = [250, -0.5, 0.5, 250, -0.5, 0.5]
    rateBinning = [200, -1, 1, 200, -1, 1]
    drawEllipseTree(signalTree, rateTree, to_draw, stationCut, signalPtCut, signalBinning, rateBinning, xTitle, yTitle, cTitle)

    
def drawEllipseTreeSimpleAbs(signalTree, rateTree, st11, st12, st21, st22):    
    to_draw = "abs(DTTF_phib%d_phib%d):abs(DTTF_phib%d_phib%d)"%(st11,st12,st21,st22)
    stationCut = "ok_DTTF_st%d && ok_DTTF_st%d && ok_DTTF_st%d && ok_DTTF_st%d"%(st11,st12,st21,st22)
    xTitle = "d#Phi_{b}(MB%d,MB%d)"%(st11, st12)
    yTitle = "d#Phi_{b}(MB%d,MB%d)"%(st21, st22)
    cTitle = "DPhib_MB%d_MB%d__DPhib_MB%d_MB%d__abs"%(st11,st12,st21,st22)
    signalBinning = [250, -0.5, 0.5, 250, -0.5, 0.5]
    rateBinning = [200, -1, 1, 200, -1, 1]
    drawEllipseTree(signalTree, rateTree, to_draw, stationCut, signalBinning, rateBinning, xTitle, yTitle, cTitle)


def getEllipseCut(signalTree, rateTree, st11, st12, st21, st22, signalPtCut, a_axis, b_axis, alpha, x0=0, y0=0):
    to_draw = "abs(DTTF_phib%d_phib%d):abs(DTTF_phib%d_phib%d)"%(st11,st12,st21,st22)
    stationCut = "ok_DTTF_st%d && ok_DTTF_st%d && ok_DTTF_st%d && ok_DTTF_st%d"%(st11,st12,st21,st22)
    signalBinning = [250, -0.5, 0.5, 250, -0.5, 0.5]
    rateBinning = [200, -1, 1, 200, -1, 1]
    [nBinsX, minBinX, maxBinX, nBinsY, minBinY, maxBinY] = signalBinning
    signalHist1 = get2dHisto(signalTree, to_draw, TCut("%s"%stationCut + "&& sim_pt > %f"%signalPtCut), nBinsX, minBinX, maxBinX, nBinsY, minBinY, maxBinY)

    [nBinsX, minBinX, maxBinX, nBinsY, minBinY, maxBinY] = rateBinning
    rateHist = get2dHisto(rateTree, to_draw, stationCut, nBinsX, minBinX, maxBinX, nBinsY, minBinY, maxBinY)

    signalAcceptanceFactor, backgroundRejectionFactor = getBackgroundRejectionEllipse(a_axis, b_axis, alpha, x0, y0, signalHist1, rateHist) 
    return signalAcceptanceFactor, backgroundRejectionFactor


def getEllipseCutManyCombinations(signalTree, rateTree, signalPtCut, a_axis, b_axis, alpha):
    print "Pt cut", signalPtCut
    pairs = [(1,2), (1,3), (1,4), (2,3), (2,4), (3,4)]
    for p in range(0,len(pairs)):
        for q in range(p,len(pairs)):
            first = pairs[p]
            second = pairs[q]
            if first == second: 
                continue
            print "\tCombination", first, second, "a=", a_axis, "b=", b_axis, "alpha=", alpha, "A,R=", 
            print getEllipseCut(signalTree, rateTree, first[0], first[1], second[0], second[1], signalPtCut, a_axis, b_axis, alpha)        
        print
            #drawEllipseTreeSimpleAbs(signalTree, rateTree, p[0], p[1], q[0], q[1])        


signalFile = TFile.Open("out_ana_pu140_displaced_L1Mu_DDY123_StubRec_20170223_v2.root")
rateFile = TFile.Open("target.root")

signalTree = signalFile.Get("L1MuTree")
rateTree = rateFile.Get("L1MuTriggerRate")

signalAcceptance = 0.90

#drawEllipseTreeSimple(signalTree, rateTree, 1, 2, 2, 3)        
getEllipseCutManyCombinations(signalTree, rateTree, 10, 0.07, 0.07, 20)
