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

file1 = TFile("DisplacedL1MuTrigger_20160826_v4/DDY123_vs_deltaPhiGEM_pad2_pt20to100_eta16to22_dxy0to100_withLCTFit_hist.root")
file2 = TFile("DisplacedL1MuTrigger_20160826_v4/DDY123_vs_deltaPhiGEM_pad2_pt2to7_eta16to22_dxy0to5_withLCTFit_hist.root")

hist1 = file.Get("DDY123_vs_deltaPhiGEM_pad2_pt20to100_eta16to22_dxy0to100_withLCTFit")
hist2 = file.Get("DDY123_vs_deltaPhiGEM_pad2_pt2to7_eta16to22_dxy0to5_withLCTFit")

print hist1
print hist2

## draw an ellipse that includes 95% of the entries
totalEntries1 = hist1.GetEntries()*1.0
totalEntries2 = hist2.GetEntries()*1.0

foundRadius68 = 0 
foundRadius90 = 0 
foundRadius65 = 0 

def getEllipse(x,y,a,b):
  return x*x/(a*a) + y*y/(b*b)

def passEllipse():
    return getEllipse(x,y,a,b) <= 1

def failEllipse():
    return getEllipse(x,y,a,b) > 1



def getEllipse(fractionToKeep, a):
  foundRadius = 0
  if totalEntries>0:
    ## step in ellipse sizes
    print "Checking ellipse"
    for radius in frange(0, 10, 0.1):
      #radius = rr/100.
      entriesInEllipseSignal  = 0
      entriesOutEllipseBackground  = 0
      ## loop on entries in histogram
      for j in range(1,hist1.GetNbinsX()):
        for k in range(1,hist1.GetNbinsY()):
          ## drop bins that are too far out
          #if hist.GetXaxis().GetBinCenter(j) > radius:
          #  continue
          #if hist.GetYaxis().GetBinCenter(k) > radius:
          #  continue
          #print "radius", radius, "binx", j, "biny", k, hist.GetXaxis().GetBinCenter(j), hist.GetYaxis().GetBinCenter(k), getEllipse(hist.GetXaxis().GetBinCenter(j), hist.GetYaxis().GetBinCenter(k)), radius*radius
          ## only select points in the circle
          if getEllipse(hist1.GetXaxis().GetBinCenter(j), hist1.GetYaxis().GetBinCenter(k)) <= radius*radius: 
            entriesInEllipse += hist1.GetBinContent(j,k)
          if getEllipse(hist2.GetXaxis().GetBinCenter(j), hist2.GetYaxis().GetBinCenter(k)) > radius*radius: 
            entriesInEllipse += hist2.GetBinContent(j,k)
            #print "\tAccept"
      ## break if enough points
      #print "CheckBreak", entriesInEllipse, totalEntries, entriesInEllipse/totalEntries, fractionToKeep
      if entriesInEllipse/totalEntries > fractionToKeep:
        foundRadius = radius
        break
  ## in case no radius could be found
  if foundRadius == 0:
      return 100
  print "Found radius", foundRadius
  return foundRadius 

foundRadius68 = getRadius(.68)
foundRadius90 = getRadius(.90)
foundRadius95 = getRadius(.95)
print "foundRadius68", foundRadius68
print "foundRadius90", foundRadius90
print "foundRadius95", foundRadius95

print "drawing ellipse"

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
hist.SetTitle("Pad1, 10 < p_{T} < 20 GeV,  1.6 < eta < 1.8 ;#Delta#Delta Y_{123} [cm]; |#Delta#Phi_{dir}(GE11,GE21)|")

#f2 = TF2("f2","TMath::Sqrt(x**2 + 2500*y**2)*%f"%(foundRadius),0,5,0,0.2);
#f2.SetContour(48);
#f2.SetLineColor(kRed);
#f2.Draw("same")

el1 = TEllipse(0,0,foundRadius68,foundRadius68/50.);
el1.SetLineColor(kRed);
el1.SetLineWidth(3);
el1.SetFillStyle(4000)
el1.SetPhimin(0)
el1.SetPhimax(90)
el1.Draw("same")

el2 = TEllipse(0,0,foundRadius90,foundRadius90/50.);
el2.SetLineColor(kBlue);
el2.SetLineWidth(3);
el2.SetFillStyle(4000)
el2.SetPhimin(0)
el2.SetPhimax(90)
el2.Draw("same")

el3 = TEllipse(0,0,foundRadius95,foundRadius95/50.);
el3.SetLineColor(kGreen+1);
el3.SetLineWidth(3);
el3.SetFillStyle(4000)
el3.SetPhimin(0)
el3.SetPhimax(90)
el3.Draw("same")

## set the radius in the plot
tex = TLatex(0.15, 0.85, "Radius (0.68): %f"%(foundRadius68))
tex.SetTextSize(0.05)
tex.SetNDC()
tex.Draw("same")

tex2 = TLatex(0.15, 0.8, "Radius (0.90): %f"%(foundRadius90))
tex2.SetTextSize(0.05)
tex2.SetNDC()
tex2.Draw("same")

tex3 = TLatex(0.15, 0.75, "Radius (0.95): %f"%(foundRadius95))
tex3.SetTextSize(0.05)
tex3.SetNDC()
tex3.Draw("same")

c.SaveAs("deltaDeltaY123_vs_deltaPhiGEM_pad4_pt10to20_eta16to18_withLCTFit_ellipse.png")
