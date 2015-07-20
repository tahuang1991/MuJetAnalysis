from ROOT import *

from Helpers import *
from ROOT import SetOwnership

def trackKinematics(p):

    draw_1D(p,"sim_pt", "sim_pt",  "SimTrack p_{T}; SimTrack p_{T} [GeV/c]; Entries", "(50,0,100)")
    draw_1D(p,"sim_eta", "sim_eta", "SimTrack #eta; SimTrack #eta; Entries", "(50,-2.5,2.5)")
    draw_1D(p,"sim_phi", "sim_phi", "SimTrack #phi; SimTrack #phi; Entries", "(60,-3.1416,3.1416)")
    draw_1D(p,"abs(sim_dxy)", "sim_abs_dxy", "SimTrack d_{xy}; SimTrack d_{xy} [cm]; Entries", "(100,0,20")

    draw_1D(p,"recoTrackExtra_pt_outer",  "recoTrackExtra_pt_outer",  "TrackExtra outer p_{T}; TrackExtra p_{T}^{outer} [GeV/c]; Entries", "(50,0,100)")
    draw_1D(p,"recoTrackExtra_eta_outer", "recoTrackExtra_eta_outer", "TrackExtra outer #eta; TrackExtra #eta^{outer}; Entries", "(50,-2.5,2.5)")
    draw_1D(p,"recoTrackExtra_phi_outer", "recoTrackExtra_phi_outer", "TrackExtra outer #phi; TrackExtra #phi^{outer}; Entries", "(60,-3.1416,3.1416)")

    draw_1D(p,"recoTrackExtra_pt_inner",  "recoTrackExtra_pt_inner",  "TrackExtra inner p_{T}; TrackExtra p_{T}^{inner} [GeV/c]; Entries", "(50,0,100)")
    draw_1D(p,"recoTrackExtra_eta_inner", "recoTrackExtra_eta_inner", "TrackExtra inner #eta; TrackExtra #eta^{inner}; Entries", "(50,-2.5,2.5)")
    draw_1D(p,"recoTrackExtra_phi_inner", "recoTrackExtra_phi_inner", "TrackExtra inner #phi; TrackExtra #phi^{inner}; Entries", "(60,-3.1416,3.1416)")

    draw_1D(p,"recoTrack_pt_outer",  "recoTrack_pt_outer",  "Track outer p_{T}; Track p_{T}^{outer} [GeV/c]; Entries", "(50,0,100)")
    draw_1D(p,"recoTrack_eta_outer", "recoTrack_eta_outer", "Track outer #eta; Track #eta^{outer}; Entries", "(50,-2.5,2.5)")
    draw_1D(p,"recoTrack_phi_outer", "recoTrack_phi_outer", "Track outer #phi; Track #phi^{outer}; Entries", "(60,-3.1416,3.1416)")

    draw_1D(p,"recoChargedCandidate_pt",  "recoChargedCandidate_pt",  "Charged Candidate p_{T}; Charged Candidate p_{T} [GeV/c]; Entries", "(50,0,100)")
    draw_1D(p,"recoChargedCandidate_eta", "recoChargedCandidate_eta", "Charged Candidate #eta; Charged Candidate #eta; Entries", "(50,-2.5,2.5)")
    draw_1D(p,"recoChargedCandidate_phi", "recoChargedCandidate_phi", "Charged Candidate #phi; Charged Candidate #phi; Entries", "(60,-3.1416,3.1416)")

def recoTrackEfficiency(p):

    ptBinning = "(50,0,100)"
    sim_pt = get_1D(p, "title", "sim_pt", ptBinning, "sim_pt", nocut())
    sim_pt_barrel = get_1D(p, "title", "sim_pt_barrel", ptBinning, "sim_pt", barrel_eta_cut())
    sim_pt_endcap = get_1D(p, "title", "sim_pt_endcap", ptBinning, "sim_pt", endcap_eta_cut())
    sim_pt_seg = get_1D(p, "title", "sim_pt_dtseg", ptBinning, "sim_pt", AND(n_dt_csc_seg(2)))

    sim_pt_recoTrackExtra = get_1D(p, "title", "sim_pt_recoTrackExtra", ptBinning, "sim_pt", AND(has_trackExtra()))
    sim_pt_recoTrack = get_1D(p, "title", "sim_pt_recoTrack", ptBinning, "sim_pt", AND(has_track()))
    sim_pt_recoChargedCandidate = get_1D(p, "title", "sim_pt_recoChargedCandidate", ptBinning, "sim_pt", AND(has_cand()))

    sim_pt_recoTrackExtra_barrel = get_1D(p, "title", "sim_pt_recoTrackExtra_barrel", ptBinning, "sim_pt", AND(has_trackExtra(), barrel_eta_cut()))
    sim_pt_recoTrack_barrel = get_1D(p, "title", "sim_pt_recoTrack_barrel", ptBinning, "sim_pt", AND(has_track(), barrel_eta_cut()))
    sim_pt_recoChargedCandidate_barrel = get_1D(p, "title", "sim_pt_recoChargedCandidate_barrel", ptBinning, "sim_pt", AND(has_cand(), barrel_eta_cut()))

    sim_pt_recoTrackExtra_endcap = get_1D(p, "title", "sim_pt_recoTrackExtra_endcap", ptBinning, "sim_pt", AND(has_trackExtra(), endcap_eta_cut()))
    sim_pt_recoTrack_endcap = get_1D(p, "title", "sim_pt_recoTrack_endcap", ptBinning, "sim_pt", AND(has_track(), endcap_eta_cut()))
    sim_pt_recoChargedCandidate_endcap = get_1D(p, "title", "sim_pt_recoChargedCandidate_endcap", ptBinning, "sim_pt", AND(has_cand(), endcap_eta_cut()))

    ## no eta cut
    def sim_pt_sh(n=2):
        return get_1D(p, "title", "sim_pt_%dsh"%(n), ptBinning, "sim_pt", AND(n_dt_csc_st_sh(n)))
    def sim_pt_seg(n=2):
        return get_1D(p, "title", "sim_pt_%dseg"%(n), ptBinning, "sim_pt", AND(n_dt_csc_seg(n)))
    def sim_pt_sh_seg(n=2,m=2):
        return get_1D(p, "title", "sim_pt_%dsh_%dseg"%(n,m), ptBinning, "sim_pt", AND(n_dt_csc_st_sh(n), n_dt_csc_seg(m)))
    def sim_pt_seg_recoTrackExtra(n=2):
        return get_1D(p, "title", "sim_pt_%dseg_recoTrackExtra"%(n), ptBinning, "sim_pt", AND(n_dt_csc_seg(n),has_trackExtra()))
    def sim_pt_seg_recoTrack(n=2):
        return get_1D(p, "title", "sim_pt_%dseg_recoTrack"%(n), ptBinning, "sim_pt", AND(n_dt_csc_seg(n),has_track()))
    def sim_pt_seg_recoChargedCandidate(n=2):
        return get_1D(p, "title", "sim_pt_%dseg_recoChargedCandidate"%(n), ptBinning, "sim_pt", AND(n_dt_csc_seg(n),has_cand()))

    ## DT only
    def sim_pt_sh_barrel(n=2):
        return get_1D(p, "title", "sim_pt_%dsh_barrel"%(n), ptBinning, "sim_pt", AND(n_dt_csc_st_sh(n), barrel_eta_cut()))
    def sim_pt_seg_barrel(n=2):
        return get_1D(p, "title", "sim_pt_%dseg_barrel"%(n), ptBinning, "sim_pt", AND(n_dt_csc_seg(n), barrel_eta_cut()))
    def sim_pt_sh_seg_barrel(n=2,m=2):
        return get_1D(p, "title", "sim_pt_%dsh_%dseg_barrel"%(n,m), ptBinning, "sim_pt", AND(n_dt_csc_st_sh(n), n_dt_csc_seg(m), barrel_eta_cut()))
    def sim_pt_seg_recoTrackExtra_barrel(n=2):
        return get_1D(p, "title", "sim_pt_%dseg_recoTrackExtra_barrel"%(n), ptBinning, "sim_pt", AND(n_dt_csc_seg(n),has_trackExtra(), barrel_eta_cut()))
    def sim_pt_seg_recoTrack_barrel(n=2):
        return get_1D(p, "title", "sim_pt_%dseg_recoTrack_barrel"%(n), ptBinning, "sim_pt", AND(n_dt_csc_seg(n),has_track(), barrel_eta_cut()))
    def sim_pt_seg_recoChargedCandidate_barrel(n=2):
        return get_1D(p, "title", "sim_pt_%dseg_recoChargedCandidate_barrel"%(n), ptBinning, "sim_pt", AND(n_dt_csc_seg(n),has_cand(), barrel_eta_cut()))

    ## CSC only
    def sim_pt_sh_endcap(n=2):
        return get_1D(p, "title", "sim_pt_%dcscsh_endcap"%(n), ptBinning, "sim_pt", AND(n_dt_csc_st_sh(n), endcap_eta_cut()))
    def sim_pt_cscseg_endcap(n=2):
        return get_1D(p, "title", "sim_pt_%dcscseg_endcap"%(n), ptBinning, "sim_pt", AND(n_dt_csc_seg(n), endcap_eta_cut()))
    def sim_pt_cscsh_cscseg_endcap(n=2,m=2):
        return get_1D(p, "title", "sim_pt_%dcscsh_%dcscseg_endcap"%(n,m), ptBinning, "sim_pt", AND(n_dt_csc_st_sh(n), n_dt_csc_seg(m), endcap_eta_cut()))
    def sim_pt_cscseg_recoTrackExtra_endcap(n=2):
        return get_1D(p, "title", "sim_pt_%dcscseg_recoTrackExtra_endcap"%(n), ptBinning, "sim_pt", AND(n_dt_csc_seg(n),has_trackExtra(), endcap_eta_cut()))
    def sim_pt_cscseg_recoTrack_endcap(n=2):
        return get_1D(p, "title", "sim_pt_%dcscseg_recoTrack_endcap"%(n), ptBinning, "sim_pt", AND(n_dt_csc_seg(n),has_track(), endcap_eta_cut()))
    def sim_pt_cscseg_recoChargedCandidate_endcap(n=2):
        return get_1D(p, "title", "sim_pt_%dcscseg_recoChargedCandidate_endcap"%(n), ptBinning, "sim_pt", AND(n_dt_csc_seg(n),has_cand(), endcap_eta_cut()))


    sim_pt_dxy = get_1D(p, "title", "sim_pt_dxy", ptBinning, "sim_pt", dxy(20,999))
    sim_pt_dxy_sh = get_1D(p, "title", "sim_pt_dxy_sh", ptBinning, "sim_pt", AND(dxy(20,999),n_dt_csc_st_sh(2)))
    sim_pt_dxy_seg = get_1D(p, "title", "sim_pt_dxy_seg", ptBinning, "sim_pt", AND(dxy(20,999),n_dt_csc_seg(2)))
    sim_pt_dxy_recoTrackExtra = get_1D(p, "title", "sim_pt_dxy_recoTrackExtra", ptBinning, "sim_pt", AND(dxy(20,999),has_trackExtra()))
    sim_pt_dxy_recoTrack = get_1D(p, "title", "sim_pt_dxy_recoTrack", ptBinning, "sim_pt", AND(dxy(20,999),has_track()))
    sim_pt_dxy_recoChargedCandidate = get_1D(p, "title", "sim_pt_dxy_recoChargedCandidate", ptBinning, "sim_pt", AND(dxy(20,999),has_cand()))
    sim_pt_dxy_seg_recoTrackExtra = get_1D(p, "title", "sim_pt_dxy_seg_recoTrackExtra", ptBinning, "sim_pt", AND(dxy(20,999),n_dt_csc_seg(2),has_trackExtra()))
    sim_pt_dxy_seg_recoTrack = get_1D(p, "title", "sim_pt_dxy_seg_recoTrack", ptBinning, "sim_pt", AND(dxy(20,999),n_dt_csc_seg(2),has_track()))
    sim_pt_dxy_seg_recoChargedCandidate = get_1D(p, "title", "sim_pt_dxy_seg_recoChargedCandidate", ptBinning, "sim_pt", AND(dxy(20,999),n_dt_csc_seg(2),has_cand()))


    ## CSC + DT
    def sim_eta():
        return get_1D(p, "title", "sim_eta", "(100,-2.5.,2.5.)", "sim_eta", "")
    def sim_eta_pt(pt=10):
        return get_1D(p, "title", "sim_eta", "(100,-2.5.,2.5.)", "sim_eta", pt_cut(pt))
    def sim_eta_sh(n=2):
        return get_1D(p, "title", "sim_eta_%dsh"%(n), "(100,-2.5.,2.5.)", "sim_eta", AND(n_dt_csc_st_sh(n)))
    def sim_eta_sh_pt(n=2, pt=10):
        return get_1D(p, "title", "sim_eta_%dsh_pt"%(n), "(100,-2.5.,2.5.)", "sim_eta", AND(n_dt_csc_st_sh(n), pt_cut(pt)))
    def sim_eta_seg(n=2):
        return get_1D(p, "title", "sim_eta_%dseg"%(n), "(100,-2.5.,2.5.)", "sim_eta", AND(n_dt_csc_seg(n)))
    def sim_eta_seg_pt(n=2):
        return get_1D(p, "title", "sim_eta_%dseg_pt"%(n), "(100,-2.5.,2.5.)", "sim_eta", AND(n_dt_csc_seg(n), pt_cut(pt)))
    def sim_eta_sh_seg(n=2,m=2):
        return get_1D(p, "title", "sim_eta_%dsh_%dseg"%(n,m), "(100,-2.5.,2.5.)", "sim_eta", AND(n_dt_csc_st_sh(n), n_dt_csc_seg(m)))
    def sim_eta_sh_seg_pt(n=2,m=2,pt=10):
        return get_1D(p, "title", "sim_eta_%dsh_%dseg"%(n,m), "(100,-2.5.,2.5.)", "sim_eta", AND(n_dt_csc_st_sh(n), n_dt_csc_seg(m), pt_cut(pt)))

    def sim_eta_recoTrackExtra(n=2):
        return get_1D(p, "title", "sim_eta_%dseg_recoTrackExtra"%(n), "(100,-2.5.,2.5.)", "sim_eta", AND(has_trackExtra()))
    def sim_eta_recoTrack(n=2):
        return get_1D(p, "title", "sim_eta_%dseg_recoTrack"%(n), "(100,-2.5.,2.5.)", "sim_eta", AND(has_track()))
    def sim_eta_recoChargedCandidate(n=2):
        return get_1D(p, "title", "sim_eta_%dseg_recoChargedCandidate"%(n), "(100,-2.5.,2.5.)", "sim_eta", AND(has_cand()))

    def sim_eta_seg_recoTrackExtra(n=2):
        return get_1D(p, "title", "sim_eta_%dseg_recoTrackExtra"%(n), "(100,-2.5.,2.5.)", "sim_eta", AND(n_dt_csc_seg(n),has_trackExtra()))
    def sim_eta_seg_recoTrack(n=2):
        return get_1D(p, "title", "sim_eta_%dseg_recoTrack"%(n), "(100,-2.5.,2.5.)", "sim_eta", AND(n_dt_csc_seg(n),has_track()))
    def sim_eta_seg_recoChargedCandidate(n=2):
        return get_1D(p, "title", "sim_eta_%dseg_recoChargedCandidate"%(n), "(100,-2.5.,2.5.)", "sim_eta", AND(n_dt_csc_seg(n),has_cand()))

    sim_eta_dxy = get_1D(p, "title", "sim_eta_dxy", "(100,-2.5.,2.5.)", "sim_eta", dxy(20,999))
    sim_eta_dxy_sh = get_1D(p, "title", "sim_eta_dxy_sh", "(100,-2.5.,2.5.)", "sim_eta", AND(dxy(20,999),n_dt_csc_st_sh()))
    sim_eta_dxy_seg = get_1D(p, "title", "sim_eta_dxy_seg", "(100,-2.5.,2.5.)", "sim_eta", AND(dxy(20,999),n_dt_csc_seg(2)))
    sim_eta_dxy_seg_recoTrackExtra = get_1D(p, "title", "sim_eta_dxy_seg_recoTrackExtra", "(100,-2.5.,2.5.)", "sim_eta", AND(dxy(20,999),n_dt_csc_seg(2),has_trackExtra()))
    sim_eta_dxy_seg_recoTrack = get_1D(p, "title", "sim_eta_dxy_seg_recoTrack", "(100,-2.5.,2.5.)", "sim_eta", AND(dxy(20,999),n_dt_csc_seg(2),has_track()))
    sim_eta_dxy_seg_recoChargedCandidate = get_1D(p, "title", "sim_eta_dxy_seg_recoChargedCandidate", "(100,-2.5.,2.5.)", "sim_eta", AND(dxy(20,999),n_dt_csc_seg(2),has_cand()))

    ## simhit efficiencies
    def eff_sim_pt_sh(n):
        return clearEmptyBinsEff(TEfficiency(sim_pt_sh(n), sim_pt))
    def eff_sim_pt_sh_seg(n,m):
        return clearEmptyBinsEff(TEfficiency(sim_pt_sh_seg(n,m), sim_pt_sh(n))) 
    def eff_sim_pt_sh_barrel(n):
        return clearEmptyBinsEff(TEfficiency(sim_pt_sh_barrel(n), sim_pt_barrel))
    def eff_sim_pt_sh_seg_barrel(n,m):
        return clearEmptyBinsEff(TEfficiency(sim_pt_sh_seg_barrel(n,m), sim_pt_sh_barrel(n))) 
    def eff_sim_pt_sh_seg_endcap(n,m):
        return clearEmptyBinsEff(TEfficiency(sim_pt_sh_seg_endcap(n,m), sim_pt_sh_endcap(n))) 
		
    def eff_sim_eta_sh(n, pt=10):
        return clearEmptyBinsEff(TEfficiency(sim_eta_sh_pt(n,pt), sim_eta_pt(pt)))
    def eff_sim_eta_sh_seg(n,m, pt=10):
        return clearEmptyBinsEff(TEfficiency(sim_eta_sh_seg_pt(n,m,pt), sim_eta_sh_pt(n,pt))) 

    ## track efficiencies
    eff_sim_pt_recoTrackExtra = clearEmptyBinsEff(TEfficiency(sim_pt_recoTrackExtra, sim_pt))
    eff_sim_pt_recoTrack = clearEmptyBinsEff(TEfficiency(sim_pt_recoTrack, sim_pt))
    eff_sim_pt_recoChargedCandidate = clearEmptyBinsEff(TEfficiency(sim_pt_recoChargedCandidate, sim_pt))

    eff_sim_pt_recoTrackExtra_barrel = clearEmptyBinsEff(TEfficiency(sim_pt_recoTrackExtra_barrel, sim_pt_barrel))
    eff_sim_pt_recoTrack_barrel = clearEmptyBinsEff(TEfficiency(sim_pt_recoTrack_barrel, sim_pt_barrel))
    eff_sim_pt_recoChargedCandidate_barrel = clearEmptyBinsEff(TEfficiency(sim_pt_recoChargedCandidate_barrel, sim_pt_barrel))

    eff_sim_pt_recoTrackExtra_endcap = clearEmptyBinsEff(TEfficiency(sim_pt_recoTrackExtra_endcap, sim_pt_endcap))
    eff_sim_pt_recoTrack_endcap = clearEmptyBinsEff(TEfficiency(sim_pt_recoTrack_endcap, sim_pt_endcap))
    eff_sim_pt_recoChargedCandidate_endcap = clearEmptyBinsEff(TEfficiency(sim_pt_recoChargedCandidate_endcap, sim_pt_endcap))

    def eff_sim_pt_seg_recoTrackExtra(n):
        return clearEmptyBinsEff(TEfficiency(sim_pt_seg_recoTrackExtra(n), sim_pt_seg(n)))
    def eff_sim_pt_seg_recoTrack(n):
        return clearEmptyBinsEff(TEfficiency(sim_pt_seg_recoTrack(n), sim_pt_seg(n)))
    def eff_sim_pt_seg_recoChargedCandidate(n):
        return clearEmptyBinsEff(TEfficiency(sim_pt_seg_recoChargedCandidate(n), sim_pt_seg(n)))
    def eff_sim_pt_seg_recoTrackExtra_barrel(n):
        return clearEmptyBinsEff(TEfficiency(sim_pt_seg_recoTrackExtra_barrel(n), sim_pt_seg_barrel(n)))
    def eff_sim_pt_seg_recoTrack_barrel(n):
        return clearEmptyBinsEff(TEfficiency(sim_pt_seg_recoTrack_barrel(n), sim_pt_seg_barrel(n)))
    def eff_sim_pt_seg_recoChargedCandidate_barrel(n):
        return clearEmptyBinsEff(TEfficiency(sim_pt_seg_recoChargedCandidate_barrel(n), sim_pt_seg_barrel(n)))

    def eff_sim_eta_seg_recoTrackExtra(n, pt=10):
        return clearEmptyBinsEff(TEfficiency(sim_eta_seg_recoTrackExtra(n), sim_eta_seg(n)))
    def eff_sim_eta_seg_recoTrack(n, pt=10):
        return clearEmptyBinsEff(TEfficiency(sim_eta_seg_recoTrack(n), sim_eta_seg(n)))
    def eff_sim_eta_seg_recoChargedCandidate(n, pt=10):
        return clearEmptyBinsEff(TEfficiency(sim_eta_seg_recoChargedCandidate(n), sim_eta_seg(n)))
    """
    eff_sim_pt_dxy_recoTrackExtra = clearEmptyBinsEff(TEfficiency(sim_pt_dxy_recoTrackExtra, sim_pt_dxy))
    eff_sim_pt_dxy_recoTrack = clearEmptyBinsEff(TEfficiency(sim_pt_dxy_recoTrack, sim_pt_dxy))
    eff_sim_pt_dxy_recoChargedCandidate = clearEmptyBinsEff(TEfficiency(sim_pt_dxy_recoChargedCandidate, sim_pt_dxy))

    eff_sim_pt_dxy_seg_recoTrackExtra = clearEmptyBinsEff(TEfficiency(sim_pt_dxy_seg_recoTrackExtra, sim_pt_dxy_seg))
    eff_sim_pt_dxy_seg_recoTrack = clearEmptyBinsEff(TEfficiency(sim_pt_dxy_seg_recoTrack, sim_pt_dxy_seg))
    eff_sim_pt_dxy_seg_recoChargedCandidate = clearEmptyBinsEff(TEfficiency(sim_pt_dxy_seg_recoChargedCandidate, sim_pt_dxy_seg))
    """

    """
    eff_sim_eta_dxy_recoTrackExtra = clearEmptyBinsEff(TEfficiency(sim_eta_dxy_recoTrackExtra, sim_eta_dxy))
    eff_sim_eta_dxy_recoTrack = clearEmptyBinsEff(TEfficiency(sim_eta_dxy_recoTrack, sim_eta_dxy))
    eff_sim_eta_dxy_recoChargedCandidate = clearEmptyBinsEff(TEfficiency(sim_eta_dxy_recoChargedCandidate, sim_eta_dxy))

    eff_sim_eta_dxy_seg_recoTrackExtra = clearEmptyBinsEff(TEfficiency(sim_eta_dxy_seg_recoTrackExtra, sim_eta_dxy_seg))
    eff_sim_eta_dxy_seg_recoTrack = clearEmptyBinsEff(TEfficiency(sim_eta_dxy_seg_recoTrack, sim_eta_dxy_seg))
    eff_sim_eta_dxy_seg_recoChargedCandidate = clearEmptyBinsEff(TEfficiency(sim_eta_dxy_seg_recoChargedCandidate, sim_eta_dxy_seg))
	"""

    ## plotmaker
    def makePtEffPlot(h, plotTitle, legTitle):
        c = TCanvas("c","c",800,600)
        c.Clear()
        gStyle.SetTitleStyle(0);
        gStyle.SetTitleAlign(13); ##coord in top left
        gStyle.SetTitleX(0.);
        gStyle.SetTitleY(1.);
        gStyle.SetTitleW(1);
        gStyle.SetTitleH(0.058);
#        gStyle.SetTitleXOffset(0.05)
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
        base = TH1D("base","base", 50, 0, 100)
        base.SetStats(0)
        base.SetTitle("                                                                      14 TeV,  PU = %d; SimTrack p_{T} [GeV]; Reconstruction efficiency"%(p.pu))
        base.SetMinimum(0)
        base.SetMaximum(1.1)
        base.GetXaxis().SetLabelSize(0.05)
        base.GetYaxis().SetLabelSize(0.05)
        base.GetXaxis().SetTitleSize(0.06)
        base.GetYaxis().SetTitleSize(0.06)
#        base.GetXaxis().SetLimits(0,maxbin)
        base.Draw()
        h.SetMarkerColor(kBlue)
        h.SetLineColor(kBlue)
        h.SetLineWidth(2)
        h.SetMarkerStyle(1)
        h.SetMarkerSize(15)
        h.Draw("same")
        leg = TLegend(0.2,0.3,0.75,0.45,"","brNDC")
        leg.SetFillColor(kWhite)
        leg.SetBorderSize(0)
        leg.SetFillStyle(0)
        leg.SetTextSize(0.05)
        leg.AddEntry(h,legTitle,"l")
        leg.Draw("same")
        #tex = drawLabel(p.ctau + ", " + p.mass,0.45,0.55,0.05)
        #tex4 = drawLabel(p.mass,0.55,0.47,0.05)
        #tex3 = drawLabel("H #rightarrow 2n_{1} #rightarrow 2n_{D}2Z_{D} #rightarrow 2n_{D}4#mu",0.45,0.65,0.05)
        #tex2 = applyStupidTdrStyle()

        c.SaveAs(p.outputDir + plotTitle + p.ext)


    ## plotmaker
    def makeEtaEffPlot(h, plotTitle, legTitle):
        c = TCanvas("c","c",800,600)
        c.Clear()
        gStyle.SetTitleStyle(0);
        gStyle.SetTitleAlign(13); ##coord in top left
        gStyle.SetTitleX(0.);
        gStyle.SetTitleY(1.);
        gStyle.SetTitleW(1);
        gStyle.SetTitleH(0.058);
#        gStyle.SetTitleXOffset(0.05)
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
        base = TH1D("base","base", 30, -1.5, 1.5)
        base.SetStats(0)
        base.SetTitle("                                                                      14 TeV,  PU = %d; SimTrack p_{T} [GeV]; Reconstruction efficiency"%(p.pu))
        base.SetMinimum(0)
        base.SetMaximum(1.1)
        base.GetXaxis().SetLabelSize(0.05)
        base.GetYaxis().SetLabelSize(0.05)
        base.GetXaxis().SetTitleSize(0.06)
        base.GetYaxis().SetTitleSize(0.06)
#        base.GetXaxis().SetLimits(0,maxbin)
        base.Draw()
        h.SetMarkerColor(kBlue)
        h.SetLineColor(kBlue)
        h.SetLineWidth(2)
        h.SetMarkerStyle(1)
        h.SetMarkerSize(15)
        h.Draw("same")
        leg = TLegend(0.2,0.3,0.75,0.45,"","brNDC")
        leg.SetFillColor(kWhite)
        leg.SetBorderSize(0)
        leg.SetFillStyle(0)
        leg.SetTextSize(0.05)
        leg.AddEntry(h,legTitle,"l")
        leg.Draw("same")
        #tex = drawLabel(p.ctau + ", " + p.mass,0.45,0.55,0.05)
        #tex4 = drawLabel(p.mass,0.55,0.47,0.05)
        #tex3 = drawLabel("H #rightarrow 2n_{1} #rightarrow 2n_{D}2Z_{D} #rightarrow 2n_{D}4#mu",0.45,0.65,0.05)
        #tex2 = applyStupidTdrStyle()

        c.SaveAs(p.outputDir + plotTitle + p.ext)



    ## simhits
    makePtEffPlot(eff_sim_pt_dtsh_barrel(1), "eff_sim_pt_1dtsh_barrel", "1 DT Station with SimHits")
    makePtEffPlot(eff_sim_pt_dtsh_barrel(2), "eff_sim_pt_2dtsh_barrel", "2 DT Station with SimHits")
    makePtEffPlot(eff_sim_pt_dtsh_barrel(3), "eff_sim_pt_3dtsh_barrel", "3 DT Station with SimHits")
    makePtEffPlot(eff_sim_pt_dtsh_barrel(4), "eff_sim_pt_4dtsh_barrel", "4 DT Station with SimHits")

    makePtEffPlot(eff_sim_pt_dtsh_seg_barrel(1,1), "eff_sim_pt_1dtsh_1seg_barrel", "1 DT Station with Segments")
    makePtEffPlot(eff_sim_pt_dtsh_seg_barrel(2,2), "eff_sim_pt_2dtsh_2seg_barrel", "2 DT Station with Segments")
    makePtEffPlot(eff_sim_pt_dtsh_seg_barrel(3,3), "eff_sim_pt_3dtsh_3seg_barrel", "3 DT Station with Segments")
    makePtEffPlot(eff_sim_pt_dtsh_seg_barrel(4,4), "eff_sim_pt_4dtsh_4seg_barrel", "4 DT Station with Segments")

    ## simhits
    makeEtaEffPlot(eff_sim_eta_dtsh(1), "eff_sim_eta_1dtsh", "1 DT Station with SimHits")
    makeEtaEffPlot(eff_sim_eta_dtsh(2), "eff_sim_eta_2dtsh", "2 DT Station with SimHits")
    makeEtaEffPlot(eff_sim_eta_dtsh(3), "eff_sim_eta_3dtsh", "3 DT Station with SimHits")
    makeEtaEffPlot(eff_sim_eta_dtsh(4), "eff_sim_eta_4dtsh", "4 DT Station with SimHits")

    makeEtaEffPlot(eff_sim_eta_dtsh_seg(1,1), "eff_sim_eta_1dtsh_1seg", "1 DT Station with Segments")
    makeEtaEffPlot(eff_sim_eta_dtsh_seg(2,2), "eff_sim_eta_2dtsh_2seg", "2 DT Station with Segments")
    makeEtaEffPlot(eff_sim_eta_dtsh_seg(3,3), "eff_sim_eta_3dtsh_3seg", "3 DT Station with Segments")
    makeEtaEffPlot(eff_sim_eta_dtsh_seg(4,4), "eff_sim_eta_4dtsh_4seg", "4 DT Station with Segments")

	## tracks
    for n in range(2,5):
		makePtEffPlot(eff_sim_pt_seg_recoTrackExtra(n), "eff_sim_pt_%dseg_recoTrackExtra"%(n), "L2 TrackExtra with %d segments"%(n))
		makePtEffPlot(eff_sim_pt_seg_recoTrack(n), "eff_sim_pt_%dseg_recoTrack"%(n), "L2 Track with %d segments"%(n))
		makePtEffPlot(eff_sim_pt_seg_recoChargedCandidate(n), "eff_sim_pt_%dseg_recoChargedCandidate"%(n), "L2 ChargedCandidate with %d segments"%(n))
		makePtEffPlot(eff_sim_pt_seg_recoTrackExtra_barrel(n), "eff_sim_pt_%dseg_recoTrackExtra_barrel"%(n), "L2 TrackExtra with %d segments (barrel)"%(n))
		makePtEffPlot(eff_sim_pt_seg_recoTrack_barrel(n), "eff_sim_pt_%dseg_recoTrack_barrel"%(n), "L2 Track with %d segments (barrel)"%(n))
		makePtEffPlot(eff_sim_pt_seg_recoChargedCandidate_barrel(n), "eff_sim_pt_%dseg_recoChargedCandidate_barrel"%(n), "L2 ChargedCandidate with %d segments (barrel)"%(n))

		makeEtaEffPlot(eff_sim_eta_seg_recoTrackExtra(n), "eff_sim_eta_%dseg_recoTrackExtra"%(n), "L2 TrackExtra with %d segments"%(n))
		makeEtaEffPlot(eff_sim_eta_seg_recoTrack(n), "eff_sim_eta_%dseg_recoTrack"%(n), "L2 Track with %d segments"%(n))
		makeEtaEffPlot(eff_sim_eta_seg_recoChargedCandidate(n), "eff_sim_eta_%dseg_recoChargedCandidate"%(n), "L2 ChargedCandidate with %d segments"%(n))

    """
    ## tracks
    makePtEffPlot(eff_sim_pt_recoTrackExtra, "eff_sim_pt_recoTrackExtra", "L2 TrackExtra")
    makePtEffPlot(eff_sim_pt_recoTrack, "eff_sim_pt_recoTrack", "L2 Track")
    makePtEffPlot(eff_sim_pt_recoChargedCandidate, "eff_sim_pt_recoChargedCandidate", "L2 ChargedCandidate")

    makePtEffPlot(eff_sim_pt_seg_recoTrackExtra, "eff_sim_pt_seg_recoTrackExtra", "L2 TrackExtra")
    makePtEffPlot(eff_sim_pt_seg_recoTrack, "eff_sim_pt_seg_recoTrack", "L2 Track")
    makePtEffPlot(eff_sim_pt_seg_recoChargedCandidate, "eff_sim_pt_seg_recoChargedCandidate", "L2 ChargedCandidate")

    makePtEffPlot(eff_sim_pt_recoTrackExtra_barrel, "eff_sim_pt_recoTrackExtra_barrel", "L2 TrackExtra")
    makePtEffPlot(eff_sim_pt_recoTrack, "eff_sim_pt_recoTrack_barrel", "L2 Track")
    makePtEffPlot(eff_sim_pt_recoChargedCandidate, "eff_sim_pt_recoChargedCandidate_barrel", "L2 ChargedCandidate")

    makePtEffPlot(eff_sim_pt_seg_recoTrackExtra_barrel, "eff_sim_pt_seg_recoTrackExtra_barrel", "L2 TrackExtra")
    makePtEffPlot(eff_sim_pt_seg_recoTrack_barrel, "eff_sim_pt_seg_recoTrack_barrel", "L2 Track")
    makePtEffPlot(eff_sim_pt_seg_recoChargedCandidate_barrel, "eff_sim_pt_seg_recoChargedCandidate_barrel", "L2 ChargedCandidate")

    makePtEffPlot(eff_sim_pt_recoTrackExtra_endcap, "eff_sim_pt_recoTrackExtra_endcap", "L2 TrackExtra")
    makePtEffPlot(eff_sim_pt_recoTrack, "eff_sim_pt_recoTrack_endcap", "L2 Track")
    makePtEffPlot(eff_sim_pt_recoChargedCandidate, "eff_sim_pt_recoChargedCandidate_endcap", "L2 ChargedCandidate")
    """
