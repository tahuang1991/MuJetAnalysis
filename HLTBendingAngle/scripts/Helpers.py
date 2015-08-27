from ROOT import *
from cuts import *
import math
import array
from math import log10, floor

#_______________________________________________________________________________
def getEffObject(p, variable, binning, denom_cut, extra_num_cut):

    denom = get_1D(p, "denom", "denom", binning, variable, denom_cut)
    num = get_1D(p, "num", "num", binning, variable, AND(denom_cut, extra_num_cut))
    h = TEfficiency(num, denom)
    h = clearEmptyBinsEff(h)
    SetOwnership(h, False)
    return h

#_______________________________________________________________________________
def applyStupidTdrStyle():
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

#_______________________________________________________________________________
def draw_1D(p, to_draw, c_title, title, h_bins, cut="", opt = ""):
    gStyle.SetStatStyle(0)
    gStyle.SetOptStat(11111111)
    if not p.debug:
        gStyle.SetOptStat(0)
    c = TCanvas("c","c",800,600)
    c.Clear()
    gStyle.SetTitleBorderSize(0);    
    gStyle.SetPadLeftMargin(0.126);
    gStyle.SetPadRightMargin(0.04);
    gStyle.SetPadTopMargin(0.06);
    gStyle.SetPadBottomMargin(0.13);
    p.tree.Draw(to_draw + ">>" + "h_name" + h_bins, cut)
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
    header = "                                                         PU = 0, 14 TeV"
    h.SetTitle(header)
    h.Draw()
    tex2 = applyStupidTdrStyle()
    if opt is "massCtau":
        tex = drawLabel(p.ctau,0.55,0.38,0.05)
        tex4 = drawLabel(p.mass,0.55,0.47,0.05)
    h.SetMinimum(0.)
    h.SetMaximum(h.GetMaximum()*1.2)
    c.SaveAs(p.outputDir + c_title + p.ext)

#_______________________________________________________________________________
def get_1D(p, title, h_name, h_bins, to_draw, cut, opt = "", color = kBlue):
    gStyle.SetStatStyle(0)
    gStyle.SetOptStat(11111111)
    #nbins = len(xbins)
    #h = TH1F("h_name", "h_name", nbins, xbins);
    p.tree.Draw(to_draw + ">>" + h_name + h_bins, cut)
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
def get_1Dmod(p, title, h_name, h_bins, to_draw, cut):
    gStyle.SetStatStyle(0)
    gStyle.SetOptStat(11111111)
    nBins = len(h_bins)-1
    h  = TH1F(h_name, title, nBins, to_array(h_bins))
    p.tree.Draw(to_draw + ">>"+ h_name, cut);
    #h = TH1F(gDirectory.Get(h_name).Clone(h_name))
    if not h:
        sys.exit('%s does not exist'%(to_draw))
    h.SetTitle(title)
    h.SetLineWidth(2)
    h.SetMinimum(0.)
    SetOwnership(h, False)
    return h

#_______________________________________________________________________________
def to_array(x, fmt="d"):
    return array.array(fmt, x)

#_______________________________________________________________________________
def clearEmptyBinsEff(h):
    return h
"""
for i in range(0,h.GetTotalHistogram().GetNbinsX()+500):
if h.GetEfficiency(i) < 0.005:
h.SetPassedEvents(i,0)
h.SetTotalEvents(i,0)
"""

#_______________________________________________________________________________
def error_poisson(total, selected):
    '''Source: 'http://home.fnal.gov/~paterno/images/effic.pdf'''
    return selected/total*TMath.Sqrt((1/total)+(1/selected))

def error_binom(total, selected):
    '''Source: 'http://home.fnal.gov/~paterno/images/effic.pdf'''
    return 1/total*TMath.Sqrt(selected*(1-(selected/total)))

def calc_eff(selected, total):
    '''Calculate the efficiency and errors -- Always use binomial'''
    return selected/total, error_binom(total, selected)

#_______________________________________________________________________________
def get_1Dmod(p, title, h_name, h_bins, to_draw, cut):
    gStyle.SetStatStyle(0)
    gStyle.SetOptStat(11111111)
    nBins = len(h_bins)-1
    h  = TH1F(h_name, title, nBins, to_array(h_bins))
    p.tree.Draw(to_draw + ">>"+ h_name, cut);
    #h = TH1F(gDirectory.Get(h_name).Clone(h_name))
    if not h:
        sys.exit('%s does not exist'%(to_draw))
    h.SetTitle(title)
    h.SetLineWidth(2)
    h.SetMinimum(0.)
    SetOwnership(h, False)
    return h


#_______________________________________________________________________________
def NOT(cut):
    return TCut("!" + cut.GetTitle())

#_______________________________________________________________________________
def AddTwo(h1,h2):
    h = h2.Clone("h")
    h.Add(h1)
    h.SetName(h1.GetName().replace('0',''))
    SetOwnership(h, False)
    return h

#_______________________________________________________________________________
def Add(*arg):
    """Add an arbitrary number of histograms""" 
    length = len(arg)
    if length == 0:
        print "ERROR: invalid number of arguments"
        return
    if length == 1:
        return arg[0] 
    if length == 2:
        return AddTwo(arg[0],arg[1])
    if length > 2:
        result = arg[0]
        for i in range(1,len(arg)):
            result = AddTwo(result,arg[i])
        SetOwnership(result, False)
        return result

#_______________________________________________________________________________
def drawLabel(title, x=0.17, y=0.35, font_size=0.05):
    tex = TLatex(x, y,"#font[41]{%s}"%(title))
    tex.SetTextSize(font_size)
    tex.SetNDC()
    tex.Draw("same")
    return tex
