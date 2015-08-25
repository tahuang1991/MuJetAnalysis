from ROOT import *
import math
import array
from math import log10, floor

#_______________________________________________________________________________
def nocut():
    return TCut("")

#_______________________________________________________________________________
def Gd_lxy(lxy_max = 20, lxy_min = 0.):
    return TCut("genGd_lxy > %f && genGd_lxy < %f"%(lxy_min,lxy_max))

#_______________________________________________________________________________
def GdMu_vz(vz_max=500):
    """
    To prevent losses in the endcap
    """
    return TCut("abs(genGdMu_vz[0]) < %f"%(vz_max))    

#_______________________________________________________________________________
def Gd_vz(vz_max = 30):
    return TCut("abs(genGd_vz) < %f"%(vz_max))

#_______________________________________________________________________________
def Gd_dR(dRmin = 2):
    return TCut("genGd0Gd1_dR > %f"%(dRmin))

#_______________________________________________________________________________
def Gd_fid(pt1=5, pt2=5, eta_min1=0, eta_max1=2.4, eta_min2=0, eta_max2=2.4):
    pt_cut1 = TCut("genGdMu_pt[0] > %f"%(pt1))
    pt_cut2 = TCut("genGdMu_pt[1] > %f"%(pt2))

    eta_min_cut1 = TCut("abs(genGdMu_eta[0]) > %f"%(eta_min1))
    eta_min_cut2 = TCut("abs(genGdMu_eta[1]) > %f"%(eta_min2))

    eta_max_cut1 = TCut("abs(genGdMu_eta[0]) < %f"%(eta_max1))
    eta_max_cut2 = TCut("abs(genGdMu_eta[1]) < %f"%(eta_max2))

    total_cut1 = AND(pt_cut1, eta_min_cut1, eta_max_cut1)
    total_cut2 = AND(pt_cut2, eta_min_cut2, eta_max_cut2)

    """
    Make sure the dark photons are reasonably far apart in eta,phi
    """
    extra_cut1 = Gd_dR()

    """
    I think the fiduciality requirement should be updated to have
    |vz| < 5 m so that for any given lxy the decay vertex is still inside
    the muon stations with at least two stations available beyond the vertex
    to be able to make a muon.
    """
    extra_cut2 = GdMu_vz(500)
    extra_cut3 = Gd_lxy(300, 0.)

    return AND(total_cut1)
#    return AND(total_cut1, total_cut2, extra_cut1, extra_cut2, extra_cut3)

#_______________________________________________________________________________
def pt_cut(pt=10):
    return TCut("sim_pt>%f"%(pt))

#_______________________________________________________________________________
def sim_lxy(lxy_max = 20, lxy_min = 0.):
    return TCut("sim_lxy > %f && sim_lxy < %f"%(lxy_min,lxy_max))

#_______________________________________________________________________________
def sim_vz(vz_max = 30):
    return TCut("sim_vz < %f"%(vz_max))

#_______________________________________________________________________________
def cms_eta():
    return OR(barrel_eta_cut(), endcap_eta_cut())
#_______________________________________________________________________________
def barrel_eta_cut():
    return TCut("abs(sim_eta)<1.1")

#_______________________________________________________________________________
def overlap_eta_cut():
    return TCut("0.9 < abs(sim_eta) && abs(sim_eta) < 1.2")

#_______________________________________________________________________________
def endcap_eta_cut():
    return TCut("1.1 < abs(sim_eta) && abs(sim_eta) < 2.4")

#_______________________________________________________________________________
def ge11_eta_cut():
    return TCut("1.6 < abs(sim_eta) && abs(sim_eta) < 2.2")

#_______________________________________________________________________________
def ge21_eta_cut():
    return TCut("1.6 < abs(sim_eta) && abs(sim_eta) < 2.4")

#_______________________________________________________________________________
def ring1endcap_eta_cut():
    return TCut("1.6 < abs(sim_eta) && abs(sim_eta) < 2.4")

#_______________________________________________________________________________
def n_dt_st_sh(n=2):
    return TCut("n_dt_st_sh>=%d"%(n))

#_______________________________________________________________________________
def n_csc_st_sh(n=2):
    return TCut("n_csc_st_sh>=%d"%(n))

#_______________________________________________________________________________
def n_gem_st_sh(n=2):
    return TCut("n_gem_st_sh>=%d"%(n))

#_______________________________________________________________________________
def n_rpc_st_sh(n=2):
    return TCut("n_rpc_st_sh>=%d"%(n))

#_______________________________________________________________________________
def n_dt_csc_st_sh(n=2):
    return OR(TCut("n_dt_st_sh>=%d"%(n)), TCut("n_csc_st_sh>=%d"%(n)))

#_______________________________________________________________________________
def n_dt_seg(n=2):
    return TCut("n_dt_seg>=%d"%(n))

#_______________________________________________________________________________
def n_csc_seg(n=2):
    return TCut("n_csc_seg>=%d"%(n))

#_______________________________________________________________________________
def n_dt_csc_seg(n):
    return TCut("n_dt_seg + n_csc_seg>=%d"%(n))
    
#_______________________________________________________________________________
def n_dt_csc_gem_seg(n):
    return TCut("n_dt_st_seg + n_csc_st_seg + n_gem_st_rh >=%d"%(n))

#_______________________________________________________________________________
def n_rpc_st_rh(n):
    return TCut("n_rpc_st_rh>=%d"%(n))

#_______________________________________________________________________________
def has_ge11_sh():
    return TCut("has_ge11_st_sh==1")

#_______________________________________________________________________________
def has_ge21_sh():
    return TCut("has_ge21_st_sh==1")

#_______________________________________________________________________________
def has_ge11_rh(n):
    if n==1:
        return TCut("has_ge11_st_1rh==1")
    elif n==2:
        return TCut("has_ge11_st_2rh==1")

#_______________________________________________________________________________
def has_ge21_rh(n):
    if n==1:
        return TCut("has_ge21_st_1rh==1")
    elif n==2:
        return TCut("has_ge21_st_2rh==1")

#_______________________________________________________________________________
def has_L1Extra(l1_pt=0):
    deltaR = 0.1
    return AND(TCut("has_l1Extra>=1"), TCut("l1Extra_dR<%f"%(deltaR)), TCut("l1Extra_pt>%f"%(l1_pt)))

#_______________________________________________________________________________
def has_trackExtra(pt=0):
    return AND(TCut("has_recoTrackExtra>=1"), TCut("recoTrackExtra_pt_outer>%f"%(pt)))

#_______________________________________________________________________________
def has_track(pt=0):
    return AND(TCut("has_recoTrack>=1"), TCut("recoTrack_pt_outer>%f"%(pt)))

#_______________________________________________________________________________
def has_cand(pt=0):
    return AND(TCut("has_recoChargedCandidate>=1"), TCut("recoChargedCandidate_pt>%f"%(pt)))
"""
#_______________________________________________________________________________
def cand_st(n):
    return TCut("recoChargedCandidate_st%d>0"%(n))
    
#_______________________________________________________________________________
def cand_st_valid(n):
    return TCut("recoChargedCandidate_st%d_valid>0"%(n))
"""

"""
#_______________________________________________________________________________
def cand_n_st(n):
    if n==4:
        return AND(cand_st(1), cand_st(2), cand_st(3), cand_st(4))
    elif n==3:
        return OR(AND(cand_st(1), cand_st(2), cand_st(3)),           
                  AND(cand_st(1), cand_st(2), cand_st(4)),
                  AND(cand_st(1), cand_st(3), cand_st(4)),
                  AND(cand_st(2), cand_st(3), cand_st(4))
                  )
    elif n==2:
        return OR(AND(cand_st(1), cand_st(2)),
                  AND(cand_st(1), cand_st(4)),
                  AND(cand_st(1), cand_st(3)),
                  AND(cand_st(2), cand_st(3)),
                  AND(cand_st(2), cand_st(4)),
                  AND(cand_st(3), cand_st(4))
                  )        
    elif n==1:
        return OR(cand_st(1), cand_st(2), cand_st(3), cand_st(4))
"""

#_______________________________________________________________________________
def cand_rpcb_st(n):
    return TCut("cand_rpcb_st_%d>0"%(n))

#_______________________________________________________________________________
def cand_rpcb_n_st(n):
    if n==4:
        return AND(cand_rpcb_st(1), cand_rpcb_st(2), cand_rpcb_st(3), cand_rpcb_st(4))
    elif n==3:
        return OR(AND(cand_rpcb_st(1), cand_rpcb_st(2), cand_rpcb_st(3)),           
                  AND(cand_rpcb_st(1), cand_rpcb_st(2), cand_rpcb_st(4)),
                  AND(cand_rpcb_st(1), cand_rpcb_st(3), cand_rpcb_st(4)),
                  AND(cand_rpcb_st(2), cand_rpcb_st(3), cand_rpcb_st(4)))
    elif n==2:
        return OR(AND(cand_rpcb_st(1), cand_rpcb_st(2)),
                  AND(cand_rpcb_st(1), cand_rpcb_st(4)),
                  AND(cand_rpcb_st(1), cand_rpcb_st(3)),
                  AND(cand_rpcb_st(2), cand_rpcb_st(3)),
                  AND(cand_rpcb_st(2), cand_rpcb_st(4)),
                  AND(cand_rpcb_st(3), cand_rpcb_st(4)))        
    elif n==1:
        return OR(cand_rpcb_st(1), cand_rpcb_st(2), cand_rpcb_st(3), cand_rpcb_st(4))

#_______________________________________________________________________________
def cand_rpcf_st(n):
    return TCut("cand_rpcf_st_%d>0"%(n))

#_______________________________________________________________________________
def cand_rpcf_n_st(n):
    if n==4:
        return AND(cand_rpcf_st(1), cand_rpcf_st(2), cand_rpcf_st(3), cand_rpcf_st(4))
    elif n==3:
        return OR(AND(cand_rpcf_st(1), cand_rpcf_st(2), cand_rpcf_st(3)),           
                  AND(cand_rpcf_st(1), cand_rpcf_st(2), cand_rpcf_st(4)),
                  AND(cand_rpcf_st(1), cand_rpcf_st(3), cand_rpcf_st(4)),
                  AND(cand_rpcf_st(2), cand_rpcf_st(3), cand_rpcf_st(4)))
    elif n==2:
        return OR(AND(cand_rpcf_st(1), cand_rpcf_st(2)),
                  AND(cand_rpcf_st(1), cand_rpcf_st(4)),
                  AND(cand_rpcf_st(1), cand_rpcf_st(3)),
                  AND(cand_rpcf_st(2), cand_rpcf_st(3)),
                  AND(cand_rpcf_st(2), cand_rpcf_st(4)),
                  AND(cand_rpcf_st(3), cand_rpcf_st(4)))        
    elif n==1:
        return OR(cand_rpcf_st(1), cand_rpcf_st(2), cand_rpcf_st(3), cand_rpcf_st(4))

#_______________________________________________________________________________
def cand_csc_st(n):
    return TCut("cand_csc_st_%d>0"%(n))

#_______________________________________________________________________________
def cand_csc_n_st(n):
    if n==4:
        return AND(cand_csc_st(1), cand_csc_st(2), cand_csc_st(3), cand_csc_st(4))
    elif n==3:
        return OR(AND(cand_csc_st(1), cand_csc_st(2), cand_csc_st(3)),           
                  AND(cand_csc_st(1), cand_csc_st(2), cand_csc_st(4)),
                  AND(cand_csc_st(1), cand_csc_st(3), cand_csc_st(4)),
                  AND(cand_csc_st(2), cand_csc_st(3), cand_csc_st(4)))
    elif n==2:
        return OR(AND(cand_csc_st(1), cand_csc_st(2)),
                  AND(cand_csc_st(1), cand_csc_st(4)),
                  AND(cand_csc_st(1), cand_csc_st(3)),
                  AND(cand_csc_st(2), cand_csc_st(3)),
                  AND(cand_csc_st(2), cand_csc_st(4)),
                  AND(cand_csc_st(3), cand_csc_st(4)))
    elif n==1:
        return OR(cand_csc_st(1), cand_csc_st(2), cand_csc_st(3), cand_csc_st(4))

#_______________________________________________________________________________
def cand_dt_st(n):
    return TCut("cand_dt_st_%d>0"%(n))

#_______________________________________________________________________________
def cand_dt_n_st(n):
    if n==4:
        return AND(cand_dt_st(1), cand_dt_st(2), cand_dt_st(3), cand_dt_st(4))
    elif n==3:
        return OR(AND(cand_dt_st(1), cand_dt_st(2), cand_dt_st(3)),           
                  AND(cand_dt_st(1), cand_dt_st(2), cand_dt_st(4)),
                  AND(cand_dt_st(1), cand_dt_st(3), cand_dt_st(4)),
                  AND(cand_dt_st(2), cand_dt_st(3), cand_dt_st(4)))
    elif n==2:
        return OR(AND(cand_dt_st(1), cand_dt_st(2)),
                  AND(cand_dt_st(1), cand_dt_st(4)),
                  AND(cand_dt_st(1), cand_dt_st(3)),
                  AND(cand_dt_st(2), cand_dt_st(3)),
                  AND(cand_dt_st(2), cand_dt_st(4)),
                  AND(cand_dt_st(3), cand_dt_st(4)))        
    elif n==1:
        return OR(cand_dt_st(1), cand_dt_st(2), cand_dt_st(3), cand_dt_st(4))

#_______________________________________________________________________________
def cand_gem_st(n):
    if n==3 or n==4:
        return nocut()
    return TCut("cand_gem_st_%d>0"%(n))

#_______________________________________________________________________________
def cand_gem_n_st(n):
    if n==2:
        return AND(cand_gem_st(1), cand_gem_st(2))
    elif n==1:
        return OR(cand_gem_st(1), cand_gem_st(2))          

#_______________________________________________________________________________
def cand_barrel_st(n):
    return OR(cand_dt_st(n), cand_rpcb_st(n))

#_______________________________________________________________________________
def cand_endcap_st(n):
    return OR(cand_csc_st(n), cand_rpcf_st(n), cand_gem_st(n))

#_______________________________________________________________________________
def cand_overlap_st(n):
    return OR(cand_dt_st(n), cand_rpcb_st(n), cand_csc_st(n), cand_rpcf_st(n))

#_______________________________________________________________________________
def cand_n_st(n):
    ## case for n=3
    cut = OR(AND(cand_barrel_st(1), cand_barrel_st(2), cand_barrel_st(3)),
             AND(cand_barrel_st(1), cand_barrel_st(2), cand_barrel_st(4)),
             AND(cand_barrel_st(1), cand_barrel_st(3), cand_barrel_st(4)),
             AND(cand_barrel_st(2), cand_barrel_st(3), cand_barrel_st(4)),
             
             AND(cand_endcap_st(1), cand_endcap_st(2), cand_endcap_st(3)),
             AND(cand_endcap_st(1), cand_endcap_st(2), cand_endcap_st(4)),
             AND(cand_endcap_st(1), cand_endcap_st(3), cand_endcap_st(4)),
             AND(cand_endcap_st(2), cand_endcap_st(3), cand_endcap_st(4)),
             
             AND(cand_barrel_st(1), cand_barrel_st(2),cand_endcap_st(1)),
             AND(cand_barrel_st(1), cand_barrel_st(2),cand_endcap_st(2)),

             AND(cand_barrel_st(1), cand_endcap_st(1),cand_endcap_st(2)),
             AND(cand_barrel_st(1), cand_endcap_st(1),cand_endcap_st(3)),
             AND(cand_barrel_st(1), cand_endcap_st(1),cand_endcap_st(4)),

             AND(cand_barrel_st(1), cand_endcap_st(2),cand_endcap_st(3)),
             AND(cand_barrel_st(1), cand_endcap_st(2),cand_endcap_st(4)),

             AND(cand_barrel_st(1), cand_endcap_st(3),cand_endcap_st(4)),

             AND(cand_barrel_st(2), cand_endcap_st(1),cand_endcap_st(2))
             )
    return cut

#_______________________________________________________________________________
def dxy(min_dxy, max_dxy=999):
    return TCut("%f < abs(sim_dxy) && abs(sim_dxy) < %f"%(min_dxy, max_dxy))

#_______________________________________________________________________________
def getEffObject(p, variable, binning, denom_cut, extra_num_cut):

    denom = get_1D(p, "denom", "denom", binning, variable, denom_cut)
    num = get_1D(p, "num", "num", binning, variable, AND(denom_cut, extra_num_cut))
    h = TEfficiency(num, denom)
    h = clearEmptyBinsEff(h)
    h1 = h.GetPaintedGraph()
#    p.outputFile = TFile("output.root","update")
#    p.outputFile.WriteTObject(h1)
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
def AND(*arg):
    """AND of any number of TCuts in PyROOT"""
    length = len(arg)
    if length == 0:
        print "ERROR: invalid number of arguments"
        return
    if length == 1:
        return arg[0] 
    if length==2:
        return ANDtwo(arg[0],arg[1])
    if length>2:
        result = arg[0]
        for i in range(1,len(arg)):
            result = ANDtwo(result,arg[i])
        return result

#_______________________________________________________________________________
def OR(*arg):
    """OR of any number of TCuts in PyROOT"""
    length = len(arg)
    if length == 0:
        print "ERROR: invalid number of arguments"
        return
    if length == 1:
        return arg[0] 
    if length==2:
        return ORtwo(arg[0],arg[1])
    if length>2:
        result = arg[0]
        for i in range(1,len(arg)):
            result = ORtwo(result,arg[i])
        return result

#_______________________________________________________________________________
def ANDtwo(cut1,cut2):
    """AND of two TCuts in PyROOT"""
    if cut1.GetTitle() == "":
        return cut2
    if cut2.GetTitle() == "":
        return cut1
    return TCut("(%s) && (%s)"%(cut1.GetTitle(),cut2.GetTitle()))


#_______________________________________________________________________________
def ORtwo(cut1,cut2):
    """OR of two TCuts in PyROOT"""
    if cut1.GetTitle() == "":
        return cut2
    if cut2.GetTitle() == "":
        return cut1
    return TCut("(%s) || (%s)"%(cut1.GetTitle(),cut2.GetTitle()))


#_______________________________________________________________________________
def drawLabel(title, x=0.17, y=0.35, font_size=0.05):
    tex = TLatex(x, y,"#font[41]{%s}"%(title))
    tex.SetTextSize(font_size)
    tex.SetNDC()
    tex.Draw("same")
    return tex
