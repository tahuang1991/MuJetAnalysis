from ROOT import *
from cuts import *
import math
import array
from math import log10, floor
from logic import *
import numpy as np

ptbin = [2.0,   2.5,   3.0,   3.5,   4.0, 4.5,   5.0,   6.0,   7.0,   8.0,  10.0,  12.0,  14.0, 16.0,  18.0,  20.0,  25.0,  30.0,  35.0,  40.0,  45.0, 50.0,  60.0,  70.0,  80.0,  90.0, 100.0, 120.0, 140.0, 200.0]
myptbin = np.asarray(ptbin)

#______________________________________________________________________________
def getRatecount(tree, todraw, cut):
    htemp = TH1F("htemp"," ",29,myptbin)
    tree.Draw(todraw+">>htemp",cut)
    return htemp.GetEntries()

#___________________________________________________
def getEventsNum(tree):
    eventList = []
    for k in range(0,tree.GetEntries()):
        tree.GetEntry(k)
        eventList.append(tree.event)
    return len(set(eventList))

#______________________________________________________________________________
def getRate(tree, cut):
   
    #f = ROOT.TFile(file)
    #t = f.Get(dir)
    h = TH1F("h"," ",29,myptbin)
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
    ntotalEvents = getEventsNum(tree)
    print "ntotalEvents", ntotalEvents
    h.Scale(40000./ntotalEvents/3.*0.795)
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
  header = "                                                         PU = 140, 14 TeV"
#  h.SetTitle(header)
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
