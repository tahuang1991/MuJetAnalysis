import array
from ROOT import *
from cuts import *
import math
import array
from math import log10, floor
from logic import *
import numpy as np
import os

ptbin = [
    2.0,   2.5,   3.0,   3.5,   4.0,   4.5,   5.0,   6.0,   7.0,   8.0,  
    10.0,  12.0,  14.0,  16.0,  18.0,  20.0,  25.0,  30.0,  35.0,  40.0,  
    45.0,  50.0,  60.0,  70.0,  80.0,  90.0, 100.0, 120.0, 140.0, 200.0]
myptbin = np.asarray(ptbin)
nmyptbin = len(myptbin) - 1



etabin = [
    0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 
    1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9,
    2.0, 2.1, 2.2, 2.3, 2.4, 2.5]
myetabin = np.asarray(etabin)

#______________________________________________________________________________                                                                                                  
M_PI = 4*math.atan(1)


#______________________________________________________________________________                                                                                                  
def L1Mu_status(st1, st2, st3, st4):
  def ok(st):
    return st != 99
  def nok(st):
    return st==99

  ## should not happen!
  if nok(st1) and nok(st2) and nok(st3) and nok(st4): status = 0

  if ok(st1) and nok(st2) and nok(st3) and nok(st4):  status = 1
  if nok(st1) and ok(st2) and nok(st3) and nok(st4):  status = 2
  if nok(st1) and nok(st2) and ok(st3) and nok(st4):  status = 3
  if nok(st1) and nok(st2) and nok(st3) and ok(st4):  status = 4

  ## low quality
  if ok(st1) and ok(st2) and nok(st3) and nok(st4):  status = 5
  if ok(st1) and nok(st2) and ok(st3) and nok(st4):  status = 6
  if ok(st1) and nok(st2) and nok(st3) and ok(st4):  status = 7
  if nok(st1) and ok(st2) and ok(st3) and nok(st4):  status = 8
  if nok(st1) and ok(st2) and nok(st3) and ok(st4):  status = 9
  if nok(st1) and nok(st2) and ok(st3) and ok(st4):  status = 10

  ## high quality
  if nok(st1) and ok(st2) and ok(st3) and ok(st4):  status = 11
  if ok(st1) and nok(st2) and ok(st3) and ok(st4):  status = 12
  if ok(st1) and ok(st2) and nok(st3) and ok(st4):  status = 13
  if ok(st1) and ok(st2) and ok(st3) and nok(st4):  status = 14

  ## highest quality
  if ok(st1) and ok(st2) and ok(st3) and ok(st4):  status = 15

  return status

#______________________________________________________________________________                                                                                                  
def addfiles(ch, dirname=".", ext=".root"):
  theInputFiles = []
  if not os.path.isdir(dirname):
    print "ERROR: This is not a valid directory: ", dirname
    exit()
  ls = os.listdir(dirname)
  theInputFiles.extend([dirname[:] + x for x in ls if x.endswith(ext)])
  for pfile in theInputFiles:
    print pfile
    ch.Add(pfile)

  return ch


#______________________________________________________________________________                                                                                                  
def deltaPhi(phi1, phi2):
  result = phi1 - phi2;
  while (result > 2*M_PI): 
    result -= 4*M_PI;
  while (result <= -2*M_PI):
    result += 4*M_PI;
  return result;


#______________________________________________________________________________                                                                                                  
def deltaPhi2(phi1, phi2):
  result = phi1 - phi2;
  while (result > M_PI): 
    result -= 2*M_PI;
  while (result <= -M_PI):
    result += 2*M_PI;
  return result;

#______________________________________________________________________________                       
def normalizedPhi(phi1):
  result = phi1;
  while (result > 2*M_PI): 
    result -= 4*M_PI;
  while (result <= -2*M_PI):
    result += 4*M_PI;
  return result;

#______________________________________________________________________________                       
def normalizedPhi2(phi1):
  result = phi1;
  while (result > M_PI): 
    result -= 2*M_PI;
  while (result <= -M_PI):
    result += 2*M_PI;
  return result;

#______________________________________________________________________________                                                                                                  
def getQuantilesX(hist2d):
  probs = array.array('d', [0.025, 0.16, 0.5, 1 - 0.16, 0.975] )
  q = array.array('d', [0.0]*len(probs))
  hist1d = hist2d.QuantilesX(len(probs), q, probs)
  SetOwnership( hist1d, True )
  return hist1d


#______________________________________________________________________________                                                                                                  
def getMedian(yintegral):
  if (yintegral%2 == 1):
    return (yintegral-1)/2 + 1
  else:
    return (yintegral/2) + 0.5
  

#______________________________________________________________________________                                                                                                  
def get1DHistogramMedianY(hist2d):
    '''this function returns a 1d histogram
    for a 2d histgram using the median and the x-sigma resolution on the median'''

    xBins = hist2d.GetXaxis().GetNbins()
    yBins = hist2d.GetYaxis().GetNbins()
    xminBin = hist2d.GetXaxis().GetXmin()
    xmaxBin = hist2d.GetXaxis().GetXmax()
    yminBin = hist2d.GetYaxis().GetXmin()
    ymaxBin = hist2d.GetYaxis().GetXmax()
    """
    print "xBins", xBins
    print "yBins", yBins
    print "xminBin", xminBin
    print "xmaxBin", xmaxBin
    print "yminBin", yminBin
    print "ymaxBin", ymaxBin
    """
    
    printa = 0
    r1 = TH1F("r1","",xBins,xminBin,xmaxBin)
    for x in range(0,xBins):

        if (printa > 0):
            print "*********** For bin x: %d **********************"%x
            
        # Find the total number of frequencies
        yintegral = hist2d.Integral(x,x,0,yBins+1)
        median = getMedian(yintegral)
        
        temporal = 0
        midbin = 0
        
        for m in range (0,yBins+1):
          temporal = hist2d.Integral(x,x,0,m)

          if (temporal >= median):
            midbin = m              # Break once I get to the median
            break
          
        if (printa > 0):
          print "suma: ",yintegral
          print "Midbin: ",midbin
          print "mediana count: ",temporal
          
        # midbin is the actual value to be stored in (x, midbin) histogram.    
        # Find the error above the median
        
        sumerrup = 0                       # Sum of events up
        binerrup = 0                       # Bin which has the 34% of events
        
        for k in range (midbin, yBins+1): # Looping over the midbin up to 10000 
            sumerrup = hist2d.Integral(x,x,midbin,k)
  
            if (sumerrup >= 0.33*yintegral):
                binerrup = k
                break
        
        sumerrlow = 0
        binerrlow = 0
        
        for r in range (0, midbin):
            sumerrlow = hist2d.Integral(x,x,midbin-r,midbin)

            if (sumerrlow >= 0.33*yintegral):
                binerrlow = r 
                break
        
        # error is the difference averaged on the bin low and bin up
        errorbin = abs(binerrup - binerrlow)/2.
        if (yintegral > 0):
            errorbin = errorbin / sqrt(yintegral)
        
        if (printa > 0):
            print " X position: ",x
            print " Bin y: ",midbin
            print " Error: ",errorbin
            print " Error low: ",binerrlow
            print " Sum err low: ",sumerrlow
            print " Error high: ",binerrup
            print " Sum err high: ",sumerrup

        # Store in a histogram the values of (x, midbin) with an error given by errorbin
        if errorbin ==0:
            errorbin == yBins
            
        scale = ymaxBin / yBins

        r1.SetBinContent(x, midbin*scale)
        r1.SetBinError(x, errorbin*scale)

    SetOwnership(r1, False)
    return r1                               #Return the histogram 1D 


#_______________________________________________________________________________
def applyTdrStyle():
    cmsText     = "CMS Phase II Simulation"
    cmsTextFont   = 61  ## default is helvetic-bold

    lumiTextSize     = 0.6
    lumiTextOffset   = 0.2
    cmsTextSize      = 0.75
    cmsTextOffset    = 0.1  ## only used in outOfFrame version
    
    relPosX    = 0.045
    relPosY    = 0.035
    relExtraDY = 1.2
    
    ## ratio of "CMS" and extra text size
    extraOverCmsTextSize  = 0.76

    lumi_14TeV = "PU = 0"

    """
    H = pad.GetWh();
    W = pad.GetWw();
    l = pad.GetLeftMargin();
    b = pad.GetBottomMargin();
    e = 0.025;
    """
    t = gPad.GetTopMargin();
    r = gPad.GetRightMargin();


    latex = TLatex()
    latex.SetNDC();
    latex.SetTextAngle(0);
    latex.SetTextColor(kBlack);    
    
    extraTextSize = extraOverCmsTextSize*cmsTextSize;
    """
    latex.SetTextFont(cmsTextFont);
    latex.SetTextSize(cmsTextSize*t);
    latex.SetTextFont(42);
    latex.SetTextAlign(31); 
    latex.SetTextSize(lumiTextSize*t);    
    latex.DrawLatex(1-r,1-t+lumiTextOffset*t,lumiText);    
    """

    """
    alignY_=3;
    alignX_=2;    
    align_ = 10*alignX_ + alignY_;
    latex.SetTextAlign(align_);
    posX_ = 1-r - relPosX*(1-l-r)
    posY_ = 1-t - relPosY*(1-t-b)
    """
    latex.DrawLatex(0.52, 0.87, cmsText);
    return latex


#______________________________________________________________________________
def addfiles(ch, dirname=".", ext=".root"):
  theInputFiles = []
  if not os.path.isdir(dirname):
    print "ERROR: This is not a valid directory: ", dirname
    exit()
  ls = os.listdir(dirname)
  theInputFiles.extend([dirname[:] + x for x in ls if x.endswith(ext)])
  for pfile in theInputFiles:
    ch.Add(pfile)  

  return ch

#______________________________________________________________________________
def firstSecondBin(h):
    h.SetBinContent(1,h.GetBinContent(0) + h.GetBinContent(1))
    h.SetBinContent(0,0)
    return h
#______________________________________________________________________________
def getBackwardCumulative(h):
    htemp = TH1F("htemp"," ",len(myptbin)-1, myptbin)
    ## keep the underflow
    htemp.SetBinContent(0,h.GetBinContent(0))
    for i in range(1,len(myptbin)+1):        
        sum = 0
        for j in range(i,len(myptbin)+1):
            sum += h.GetBinContent(j)
        htemp.SetBinContent(i, sum)
    htemp.Sumw2()
    SetOwnership(htemp, False)
    return htemp

#______________________________________________________________________________
def getRatecount(tree, todraw, cut):
    htemp = TH1F("htemp"," ",len(myptbin)-1, myptbin)
    tree.Draw(todraw+">>htemp",cut)
    return htemp.GetEntries()

#___________________________________________________
def getTotalEventNumber(tree):
    eventList = []
    for k in range(0,tree.GetEntries()):
        tree.GetEntry(k)
        eventList.append(tree.event)
    return len(set(eventList))

#______________________________________________________________________________
def scaleToRate(tree, h):
    ntotalEvents = tree.GetEntries()
    averageRate = 30000. #[kHz]
    bunchCrossingWindow = 1.
    h.Scale(averageRate/bunchCrossingWindow/ntotalEvents)
    return h

#______________________________________________________________________________
def getRatePtHistogram(tree, h):
    h = getBackwardCumulative(h)
    h = scaleToRate(tree, h)
    return h
        
#______________________________________________________________________________
def getRateEtaHistogram(tree, h):
    h = scaleToRate(tree, h)
    return h

#______________________________________________________________________________
def getRate(treecut):
   
    #f = ROOT.TFile(file)
    #t = f.Get(dir)
    h = TH1F("h"," ",len(myptbin)-1, myptbin)
    n=1
    for x in ptbin:
       #print "cut ",cut+" && pt>=%f"%x
       content = getRatecount(tree,"pt",cut+"&& pt>=%f"%x)
       #content = tree.GetEntries(cut+"&& pt>=%f"%x)
       print "bin n ",n,"pt ",x ,"  content ",content
       h.SetBinContent(n, content)
       n= n+1
    h.Sumw2()
    #print "before scale "
    #h.Print("all")
    ntotalEvents = getTotalEventNumber(tree)
    averageRate = 30000. #[kHz]
    bunchCrossingWindow = 1.
#    h.Scale(40000./ntotalEvents/3.*0.795)
    h.Scale(averageRate/bunchCrossingWindow/ntotalEvents)
    SetOwnership(h, False)
    return h

#______________________________________________________________________________
def set_style():
   gStyle.SetStatStyle(0)
   gStyle.SetOptStat(11111111)
   gStyle.SetTitleBorderSize(0);
   gStyle.SetPadLeftMargin(0.126);
   gStyle.SetPadRightMargin(0.04);
   gStyle.SetPadTopMargin(0.06);
   gStyle.SetPadBottomMargin(0.13);
   
#______________________________________________________________________________
def draw_1D(p, to_draw, c_title, title, h_bins, cut="", opt = ""):
   gStyle.SetStatStyle(0)
   gStyle.SetOptStat(11111111)

   c = TCanvas("c","c",800,600)
   c.Clear()
   gStyle.SetTitleBorderSize(0);
   gStyle.SetPadLeftMargin(0.126);
   gStyle.SetPadRightMargin(0.04);
   gStyle.SetPadTopMargin(0.06);
   gStyle.SetPadBottomMargin(0.13);
   p.Draw(to_draw + ">>" + "h_name" + h_bins, cut)
   h = TH1F(gDirectory.Get("h_name").Clone("h_name"))
   if not h:
      sys.exit('h does not exist')
   h.SetTitle(title)
   h.SetLineWidth(2)
   h.SetLineColor(kBlue)
   h.GetXaxis().SetLabelSize(0.05)
   h.GetYaxis().SetLabelSize(0.05)
   h.GetXaxis().SetTitleSize(0.06)
   h.GetYaxis().SetTitleSize(0.06)
   header = "                                                         PU = 140, 14 TeV"
#   h.SetTitle(header)
   h.Draw()
   h.SetMinimum(0.)
   h.SetMaximum(h.GetMaximum()*1.2)
   c.SaveAs("" + c_title + ".png")
      

#______________________________________________________________________________
def draw_1D_root(p, to_draw, c_title, title, h_bins, cut="", opt = ""):
   p.Draw(to_draw + ">>" + "h_name" + h_bins, cut)
   h = TH1F(gDirectory.Get("h_name").Clone("h_name"))
   if not h:
      sys.exit('h does not exist')
   h.SetTitle(title)
   h.SetLineWidth(2)
   h.SetLineColor(kBlue)
   h.GetXaxis().SetLabelSize(0.05)
   h.GetYaxis().SetLabelSize(0.05)
   h.GetXaxis().SetTitleSize(0.06)
   h.GetYaxis().SetTitleSize(0.06)
   h.Draw()
   h.SetMinimum(0.)
   h.SetMaximum(h.GetMaximum()*1.2)
   h.SaveAs("" + c_title + ".root")


#_______________________________________________________________________________
def draw_2D(p, to_draw, c_title, title, h_bins, cut="", opt = ""):
  gStyle.SetStatStyle(0)
  gStyle.SetOptStat(1110)
  c = TCanvas("c","c",800,600)
  c.Clear()
  gStyle.SetPadLeftMargin(0.126);
  gStyle.SetPadRightMargin(0.04);
  gStyle.SetPadTopMargin(0.06);
  gStyle.SetPadBottomMargin(0.13);
  p.Draw(to_draw + ">>h_" + h_bins, cut)
  h = TH2F(gDirectory.Get("h_"))
  if not h:
    sys.exit('h does not exist')
  h = TH2F(h.Clone("h_"))
  h.SetTitle(title)
  h.SetLineWidth(2)
  h.SetLineColor(kBlue)
  h.Draw(opt) 
  c.SaveAs("" + c_title + ".png")


#_______________________________________________________________________________
def applyTdrStyle():
    cmsText     = "CMS PhaseII Simulation"
    cmsTextFont   = 61  ## default is helvetic-bold

    lumiTextSize     = 0.6
    lumiTextOffset   = 0.2
    cmsTextSize      = 0.75
    cmsTextOffset    = 0.1  ## only used in outOfFrame version
    
    relPosX    = 0.045
    relPosY    = 0.035
    relExtraDY = 1.2
    
    ## ratio of "CMS" and extra text size
    extraOverCmsTextSize  = 0.76

    lumi_14TeV = "PU = 140"

    """
    H = pad.GetWh();
    W = pad.GetWw();
    l = pad.GetLeftMargin();
    b = pad.GetBottomMargin();
    e = 0.025;
    """
    t = gPad.GetTopMargin();
    r = gPad.GetRightMargin();
    latex = TLatex()
    latex.SetNDC();
    latex.SetTextAngle(0);
    latex.SetTextColor(kBlack);    
    
    extraTextSize = extraOverCmsTextSize*cmsTextSize;
    """
    latex.SetTextFont(cmsTextFont);
    latex.SetTextSize(cmsTextSize*t);
    latex.SetTextFont(42);
    latex.SetTextAlign(31); 
    latex.SetTextSize(lumiTextSize*t);    
    latex.DrawLatex(1-r,1-t+lumiTextOffset*t,lumiText);    
    """

    """
    alignY_=3;
    alignX_=2;    
    align_ = 10*alignX_ + alignY_;
    latex.SetTextAlign(align_);
    posX_ = 1-r - relPosX*(1-l-r)
    posY_ = 1-t - relPosY*(1-t-b)
    """
    latex.DrawLatex(0.52, 0.87, cmsText);
    return latex


#_______________________________________________________________________________
def getEffObject(p, variable, binning, denom_cut, extra_num_cut):

    denom = get_1D(p, "denom", "denom", binning, variable, denom_cut)
    num = get_1D(p, "num", "num", binning, variable, AND(denom_cut, extra_num_cut))
    print "denom", denom.GetEntries()
    print "num", num.GetEntries()
    h = TEfficiency(num, denom)
#    h = clearEmptyBinsEff(h)
    SetOwnership(h, False)
    return h

#_______________________________________________________________________________
def makeEtaEffPlot(h, plotTitle, legTitle):
    c = TCanvas("c","c",800,600)
    c.Clear()
    gStyle.SetTitleStyle(0);
    gStyle.SetTitleAlign(13); ##coord in top left
    gStyle.SetTitleX(0.);
    gStyle.SetTitleY(1.);
    gStyle.SetTitleW(1);
    gStyle.SetTitleH(0.058);
    #gStyle.SetTitleXOffset(0.05)
    gStyle.SetTitleBorderSize(0);
    gStyle.SetPadLeftMargin(0.126);
    gStyle.SetPadRightMargin(0.04);
    gStyle.SetPadTopMargin(0.06);
    gStyle.SetPadBottomMargin(0.13);
    gStyle.SetOptStat(0);
    gStyle.SetMarkerStyle(1);
    gPad.SetTickx(1)
    gPad.SetTicky(1)
    #gStyle.SetStatStyle(0)
    base = TH1D("base","base", 25, 0, 2.5)
    base.SetStats(0)
    base.SetTitle("                                                                      14 TeV,  PU = 140; #eta; Efficiency")
    base.SetMinimum(0)
    base.SetMaximum(1.1)
    base.GetXaxis().SetLabelSize(0.05)
    base.GetYaxis().SetLabelSize(0.05)
    base.GetXaxis().SetTitleSize(0.06)
    base.GetYaxis().SetTitleSize(0.06)
    #base.GetXaxis().SetLimits(0,maxbin)
    base.Draw()
    h.SetMarkerColor(kBlue)
    h.SetLineColor(kBlue)
    h.SetLineWidth(2)
    h.SetMarkerStyle(1)
    h.SetMarkerSize(15)
    h.Draw("same")
    leg = TLegend(0.1,0.3,0.75,0.45,"","brNDC")
    leg.SetFillColor(kWhite)
    leg.SetBorderSize(0)
    leg.SetFillStyle(0)
    leg.SetTextSize(0.04)
    leg.AddEntry(h,legTitle,"l")
    leg.Draw("same")
    #tex = drawLabel(p.ctau + ", " + p.mass,0.45,0.55,0.05)
    #tex4 = drawLabel(p.mass,0.55,0.47,0.05)
    #tex3 = drawLabel("H #rightarrow 2n_{1} #rightarrow 2n_{D}2Z_{D} #rightarrow 2n_{D}4#mu",0.45,0.65,0.05)
    tex2 = applyTdrStyle()
    c.SaveAs(plotTitle + ".png")


#_______________________________________________________________________________
def makeSimplePlot(targetDir, h, plotTitle, setLogx=False):
    c = TCanvas("c","c",800,600)
    c.Clear()
    gStyle.SetTitleStyle(0);
    gStyle.SetTitleAlign(13); ##coord in top left
    gStyle.SetTitleX(0.);
    gStyle.SetTitleY(0.);
    gStyle.SetTitleW(1);
    gStyle.SetTitleH(0.058);
    #gStyle.SetTitleXOffset(0.05)
    gStyle.SetTitleBorderSize(0);
    gStyle.SetPadLeftMargin(0.126);
    gStyle.SetPadRightMargin(0.04);
    gStyle.SetPadTopMargin(0.06);
    gStyle.SetPadBottomMargin(0.13);
    gStyle.SetOptStat(0);
    gStyle.SetMarkerStyle(1);
    gPad.SetTickx(1)
    gPad.SetTicky(1)
    if setLogx:
        gPad.SetLogx()
    #gStyle.SetStatStyle(0)
    gStyle.SetOptStat(11111111)
    h.SetStats(1)
    h.GetXaxis().SetLabelSize(0.05)
    h.GetYaxis().SetLabelSize(0.05)
    h.GetXaxis().SetTitleSize(0.06)
    h.GetYaxis().SetTitleSize(0.06)
    #h.GetXaxis().SetLimits(0,maxbin)
    h.Draw()
    h.SetMarkerColor(kBlue)
    h.SetLineColor(kBlue)
    h.SetLineWidth(2)
    h.SetMarkerStyle(1)
    h.SetMarkerSize(15)
    #tex = drawLabel(p.ctau + ", " + p.mass,0.45,0.55,0.05)
    #tex4 = drawLabel(p.mass,0.55,0.47,0.05)
    #tex3 = drawLabel("H #rightarrow 2n_{1} #rightarrow 2n_{D}2Z_{D} #rightarrow 2n_{D}4#mu",0.45,0.65,0.05)
    tex2 = applyTdrStyle()
    c.SaveAs(targetDir + plotTitle + ".png")


#_______________________________________________________________________________
def get_1D(p, title, h_name, h_bins, to_draw, cut, opt = "", color = kBlue):
    gStyle.SetStatStyle(0)
    gStyle.SetOptStat(11111111)
    #nbins = len(xbins)
    #h = TH1F("h_name", "h_name", nbins, xbins);
    p.Draw(to_draw + ">>" + h_name + h_bins, cut)
    h = TH1F(gDirectory.Get(h_name).Clone(h_name))
    if not h:
        sys.exit('%s does not exist'%(to_draw))
    h.SetTitle(title)
    h.SetLineWidth(2)
    h.SetLineColor(color)    
    h.SetMinimum(0.)
    SetOwnership(h, False)
    return h

#_______________________________________________________________________________
def to_array(x, fmt="d"):
    return array.array(fmt, x)
