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

def recoTrackExtraEfficiency(p):

    sim_pt = get_1D(p, "title", "sim_pt", "(50,0,100)", "sim_pt", nocut())
    sim_pt_dtsh = get_1D(p, "title", "sim_pt_dtsh", "(50,0,100)", "sim_pt", AND(n_dt_st_sh(2)))
    sim_pt_dtseg = get_1D(p, "title", "sim_pt_dtseg", "(50,0,100)", "sim_pt", AND(n_dt_seg(2)))
    sim_pt_recoTrackExtra = get_1D(p, "title", "sim_pt_recoTrackExtra", "(50,0,100)", "sim_pt", AND(has_trackExtra()))
    sim_pt_recoTrack = get_1D(p, "title", "sim_pt_recoTrack", "(50,0,100)", "sim_pt", AND(has_track()))
    sim_pt_recoChargedCandidate = get_1D(p, "title", "sim_pt_recoChargedCandidate", "(50,0,100)", "sim_pt", AND(has_cand()))
    sim_pt_dtseg_recoTrackExtra = get_1D(p, "title", "sim_pt_dtseg_recoTrackExtra", "(50,0,100)", "sim_pt", AND(n_dt_seg(2),has_trackExtra()))
    sim_pt_dtseg_recoTrack = get_1D(p, "title", "sim_pt_dtseg_recoTrack", "(50,0,100)", "sim_pt", AND(n_dt_seg(2),has_track()))
    sim_pt_dtseg_recoChargedCandidate = get_1D(p, "title", "sim_pt_dtseg_recoChargedCandidate", "(50,0,100)", "sim_pt", AND(n_dt_seg(2),has_cand()))

    sim_pt_barrel = get_1D(p, "title", "sim_pt_barrel", "(50,0,100)", "sim_pt", barrel_eta_cut())
    sim_pt_dtsh_barrel = get_1D(p, "title", "sim_pt_dtsh_barrel", "(50,0,100)", "sim_pt", AND(n_dt_st_sh(2), barrel_eta_cut()))
    sim_pt_dtseg_barrel = get_1D(p, "title", "sim_pt_dtseg_barrel", "(50,0,100)", "sim_pt", AND(n_dt_seg(2), barrel_eta_cut()))
    sim_pt_recoTrackExtra_barrel = get_1D(p, "title", "sim_pt_recoTrackExtra_barrel", "(50,0,100)", "sim_pt", AND(has_trackExtra(), barrel_eta_cut()))
    sim_pt_recoTrack_barrel = get_1D(p, "title", "sim_pt_recoTrack_barrel", "(50,0,100)", "sim_pt", AND(has_track(), barrel_eta_cut()))
    sim_pt_recoChargedCandidate_barrel = get_1D(p, "title", "sim_pt_recoChargedCandidate_barrel", "(50,0,100)", "sim_pt", AND(has_cand(), barrel_eta_cut()))
    sim_pt_dtseg_recoTrackExtra_barrel = get_1D(p, "title", "sim_pt_dtseg_recoTrackExtra_barrel", "(50,0,100)", "sim_pt", AND(n_dt_seg(2),has_trackExtra(), barrel_eta_cut()))
    sim_pt_dtseg_recoTrack_barrel = get_1D(p, "title", "sim_pt_dtseg_recoTrack_barrel", "(50,0,100)", "sim_pt", AND(n_dt_seg(2),has_track(), barrel_eta_cut()))
    sim_pt_dtseg_recoChargedCandidate_barrel = get_1D(p, "title", "sim_pt_dtseg_recoChargedCandidate_barrel", "(50,0,100)", "sim_pt", AND(n_dt_seg(2),has_cand(), barrel_eta_cut()))

    sim_pt_endcap = get_1D(p, "title", "sim_pt_endcap", "(50,0,100)", "sim_pt", endcap_eta_cut())
    sim_pt_dtsh_endcap = get_1D(p, "title", "sim_pt_dtsh_endcap", "(50,0,100)", "sim_pt", AND(n_dt_st_sh(2), endcap_eta_cut()))
    sim_pt_dtseg_endcap = get_1D(p, "title", "sim_pt_dtseg_endcap", "(50,0,100)", "sim_pt", AND(n_dt_seg(2), endcap_eta_cut()))
    sim_pt_recoTrackExtra_endcap = get_1D(p, "title", "sim_pt_recoTrackExtra_endcap", "(50,0,100)", "sim_pt", AND(has_trackExtra(), endcap_eta_cut()))
    sim_pt_recoTrack_endcap = get_1D(p, "title", "sim_pt_recoTrack_endcap", "(50,0,100)", "sim_pt", AND(has_track(), endcap_eta_cut()))
    sim_pt_recoChargedCandidate_endcap = get_1D(p, "title", "sim_pt_recoChargedCandidate_endcap", "(50,0,100)", "sim_pt", AND(has_cand(), endcap_eta_cut()))
    sim_pt_dtseg_recoTrackExtra_endcap = get_1D(p, "title", "sim_pt_dtseg_recoTrackExtra_endcap", "(50,0,100)", "sim_pt", AND(n_dt_seg(2),has_trackExtra(), endcap_eta_cut()))
    sim_pt_dtseg_recoTrack_endcap = get_1D(p, "title", "sim_pt_dtseg_recoTrack_endcap", "(50,0,100)", "sim_pt", AND(n_dt_seg(2),has_track(), endcap_eta_cut()))
    sim_pt_dtseg_recoChargedCandidate_endcap = get_1D(p, "title", "sim_pt_dtseg_recoChargedCandidate_endcap", "(50,0,100)", "sim_pt", AND(n_dt_seg(2),has_cand(), endcap_eta_cut()))


    sim_pt_dxy = get_1D(p, "title", "sim_pt_dxy", "(50,0,100)", "sim_pt", dxy(20,999))
    sim_pt_dxy_dtsh = get_1D(p, "title", "sim_pt_dxy_dtsh", "(50,0,100)", "sim_pt", AND(dxy(20,999),n_dt_st_sh(2)))
    sim_pt_dxy_dtseg = get_1D(p, "title", "sim_pt_dxy_dtseg", "(50,0,100)", "sim_pt", AND(dxy(20,999),n_dt_seg(2)))
    sim_pt_dxy_recoTrackExtra = get_1D(p, "title", "sim_pt_dxy_recoTrackExtra", "(50,0,100)", "sim_pt", AND(dxy(20,999),has_trackExtra()))
    sim_pt_dxy_recoTrack = get_1D(p, "title", "sim_pt_dxy_recoTrack", "(50,0,100)", "sim_pt", AND(dxy(20,999),has_track()))
    sim_pt_dxy_recoChargedCandidate = get_1D(p, "title", "sim_pt_dxy_recoChargedCandidate", "(50,0,100)", "sim_pt", AND(dxy(20,999),has_cand()))
    sim_pt_dxy_dtseg_recoTrackExtra = get_1D(p, "title", "sim_pt_dxy_dtseg_recoTrackExtra", "(50,0,100)", "sim_pt", AND(dxy(20,999),n_dt_seg(2),has_trackExtra()))
    sim_pt_dxy_dtseg_recoTrack = get_1D(p, "title", "sim_pt_dxy_dtseg_recoTrack", "(50,0,100)", "sim_pt", AND(dxy(20,999),n_dt_seg(2),has_track()))
    sim_pt_dxy_dtseg_recoChargedCandidate = get_1D(p, "title", "sim_pt_dxy_dtseg_recoChargedCandidate", "(50,0,100)", "sim_pt", AND(dxy(20,999),n_dt_seg(2),has_cand()))

    sim_eta = get_1D(p, "title", "sim_eta", "(60,-3.1416,3.1416)", "sim_eta", nocut())
    sim_eta_dxy = get_1D(p, "title", "sim_eta_dxy", "(60,-3.1416,3.1416)", "sim_eta", dxy(20,999))
    sim_eta_dxy_dtsh = get_1D(p, "title", "sim_eta_dxy_dtsh", "(60,-3.1416,3.1416)", "sim_eta", AND(dxy(20,999),n_dt_st_sh()))
    sim_eta_dxy_dtseg = get_1D(p, "title", "sim_eta_dxy_dtseg", "(60,-3.1416,3.1416)", "sim_eta", AND(dxy(20,999),n_dt_seg(2)))
    sim_eta_dxy_dtseg_recoTrackExtra = get_1D(p, "title", "sim_eta_dxy_dtseg_recoTrackExtra", "(60,-3.1416,3.1416)", "sim_eta", AND(dxy(20,999),n_dt_seg(2),has_trackExtra()))
    sim_eta_dxy_dtseg_recoTrack = get_1D(p, "title", "sim_eta_dxy_dtseg_recoTrack", "(60,-3.1416,3.1416)", "sim_eta", AND(dxy(20,999),n_dt_seg(2),has_track()))
    sim_eta_dxy_dtseg_recoChargedCandidate = get_1D(p, "title", "sim_eta_dxy_dtseg_recoChargedCandidate", "(60,-3.1416,3.1416)", "sim_eta", AND(dxy(20,999),n_dt_seg(2),has_cand()))

    ## efficiencies

    eff_sim_pt_recoTrackExtra = clearEmptyBinsEff(TEfficiency(sim_pt_recoTrackExtra, sim_pt))
    eff_sim_pt_recoTrack = clearEmptyBinsEff(TEfficiency(sim_pt_recoTrack, sim_pt))
    eff_sim_pt_recoChargedCandidate = clearEmptyBinsEff(TEfficiency(sim_pt_recoChargedCandidate, sim_pt))

    eff_sim_pt_dtseg_recoTrackExtra = clearEmptyBinsEff(TEfficiency(sim_pt_dtseg_recoTrackExtra, sim_pt_dtseg))
    eff_sim_pt_dtseg_recoTrack = clearEmptyBinsEff(TEfficiency(sim_pt_dtseg_recoTrack, sim_pt_dtseg))
    eff_sim_pt_dtseg_recoChargedCandidate = clearEmptyBinsEff(TEfficiency(sim_pt_dtseg_recoChargedCandidate, sim_pt_dtseg))

    eff_sim_pt_recoTrackExtra_barrel = clearEmptyBinsEff(TEfficiency(sim_pt_recoTrackExtra_barrel, sim_pt_barrel))
    eff_sim_pt_recoTrack_barrel = clearEmptyBinsEff(TEfficiency(sim_pt_recoTrack_barrel, sim_pt_barrel))
    eff_sim_pt_recoChargedCandidate_barrel = clearEmptyBinsEff(TEfficiency(sim_pt_recoChargedCandidate_barrel, sim_pt_barrel))

    eff_sim_pt_dtseg_recoTrackExtra_endcap = clearEmptyBinsEff(TEfficiency(sim_pt_dtseg_recoTrackExtra_endcap, sim_pt_dtseg_endcap))
    eff_sim_pt_dtseg_recoTrack_endcap = clearEmptyBinsEff(TEfficiency(sim_pt_dtseg_recoTrack, sim_pt_dtseg_endcap))
    eff_sim_pt_dtseg_recoChargedCandidate_endcap = clearEmptyBinsEff(TEfficiency(sim_pt_dtseg_recoChargedCandidate, sim_pt_dtseg_endcap))

    eff_sim_pt_recoTrackExtra_endcap = clearEmptyBinsEff(TEfficiency(sim_pt_recoTrackExtra_endcap, sim_pt_endcap))
    eff_sim_pt_recoTrack_endcap = clearEmptyBinsEff(TEfficiency(sim_pt_recoTrack_endcap, sim_pt_endcap))
    eff_sim_pt_recoChargedCandidate_endcap = clearEmptyBinsEff(TEfficiency(sim_pt_recoChargedCandidate_endcap, sim_pt_endcap))

    eff_sim_pt_dtseg_recoTrackExtra_barrel = clearEmptyBinsEff(TEfficiency(sim_pt_dtseg_recoTrackExtra_barrel, sim_pt_dtseg_barrel))
    eff_sim_pt_dtseg_recoTrack_barrel = clearEmptyBinsEff(TEfficiency(sim_pt_dtseg_recoTrack, sim_pt_dtseg_barrel))
    eff_sim_pt_dtseg_recoChargedCandidate_barrel = clearEmptyBinsEff(TEfficiency(sim_pt_dtseg_recoChargedCandidate, sim_pt_dtseg_barrel))

    eff_sim_pt_dxy_recoTrackExtra = clearEmptyBinsEff(TEfficiency(sim_pt_dxy_recoTrackExtra, sim_pt_dxy))
    eff_sim_pt_dxy_recoTrack = clearEmptyBinsEff(TEfficiency(sim_pt_dxy_recoTrack, sim_pt_dxy))
    eff_sim_pt_dxy_recoChargedCandidate = clearEmptyBinsEff(TEfficiency(sim_pt_dxy_recoChargedCandidate, sim_pt_dxy))

    eff_sim_pt_dxy_dtseg_recoTrackExtra = clearEmptyBinsEff(TEfficiency(sim_pt_dxy_dtseg_recoTrackExtra, sim_pt_dxy_dtseg))
    eff_sim_pt_dxy_dtseg_recoTrack = clearEmptyBinsEff(TEfficiency(sim_pt_dxy_dtseg_recoTrack, sim_pt_dxy_dtseg))
    eff_sim_pt_dxy_dtseg_recoChargedCandidate = clearEmptyBinsEff(TEfficiency(sim_pt_dxy_dtseg_recoChargedCandidate, sim_pt_dxy_dtseg))

    """
    eff_sim_eta_dxy_recoTrackExtra = clearEmptyBinsEff(TEfficiency(sim_eta_dxy_recoTrackExtra, sim_eta_dxy))
    eff_sim_eta_dxy_recoTrack = clearEmptyBinsEff(TEfficiency(sim_eta_dxy_recoTrack, sim_eta_dxy))
    eff_sim_eta_dxy_recoChargedCandidate = clearEmptyBinsEff(TEfficiency(sim_eta_dxy_recoChargedCandidate, sim_eta_dxy))

    eff_sim_eta_dxy_dtseg_recoTrackExtra = clearEmptyBinsEff(TEfficiency(sim_eta_dxy_dtseg_recoTrackExtra, sim_eta_dxy_dtseg))
    eff_sim_eta_dxy_dtseg_recoTrack = clearEmptyBinsEff(TEfficiency(sim_eta_dxy_dtseg_recoTrack, sim_eta_dxy_dtseg))
    eff_sim_eta_dxy_dtseg_recoChargedCandidate = clearEmptyBinsEff(TEfficiency(sim_eta_dxy_dtseg_recoChargedCandidate, sim_eta_dxy_dtseg))
	"""

    ## plotmaker
    def makeEffPlot(h, plotTitle, legTitle):
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
        base.SetTitle("                                                                      14 TeV,  PU = %d; Track p_{T} [GeV]; Track reconstruction efficiency"%(p.pu))
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
        leg = TLegend(0.5,0.3,0.75,0.45,"","brNDC")
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

    makeEffPlot(eff_sim_pt_recoTrackExtra, "eff_sim_pt_recoTrackExtra", "L2 TrackExtra")
    makeEffPlot(eff_sim_pt_recoTrack, "eff_sim_pt_recoTrack", "L2 Track")
    makeEffPlot(eff_sim_pt_recoChargedCandidate, "eff_sim_pt_recoChargedCandidate", "L2 ChargedCandidate")

    makeEffPlot(eff_sim_pt_dtseg_recoTrackExtra, "eff_sim_pt_dtseg_recoTrackExtra", "L2 TrackExtra")
    makeEffPlot(eff_sim_pt_dtseg_recoTrack, "eff_sim_pt_dtseg_recoTrack", "L2 Track")
    makeEffPlot(eff_sim_pt_dtseg_recoChargedCandidate, "eff_sim_pt_dtseg_recoChargedCandidate", "L2 ChargedCandidate")

    makeEffPlot(eff_sim_pt_recoTrackExtra_barrel, "eff_sim_pt_recoTrackExtra_barrel", "L2 TrackExtra")
    makeEffPlot(eff_sim_pt_recoTrack, "eff_sim_pt_recoTrack_barrel", "L2 Track")
    makeEffPlot(eff_sim_pt_recoChargedCandidate, "eff_sim_pt_recoChargedCandidate_barrel", "L2 ChargedCandidate")

    makeEffPlot(eff_sim_pt_dtseg_recoTrackExtra_barrel, "eff_sim_pt_dtseg_recoTrackExtra_barrel", "L2 TrackExtra")
    makeEffPlot(eff_sim_pt_dtseg_recoTrack_barrel, "eff_sim_pt_dtseg_recoTrack_barrel", "L2 Track")
    makeEffPlot(eff_sim_pt_dtseg_recoChargedCandidate_barrel, "eff_sim_pt_dtseg_recoChargedCandidate_barrel", "L2 ChargedCandidate")

    makeEffPlot(eff_sim_pt_recoTrackExtra_endcap, "eff_sim_pt_recoTrackExtra_endcap", "L2 TrackExtra")
    makeEffPlot(eff_sim_pt_recoTrack, "eff_sim_pt_recoTrack_endcap", "L2 Track")
    makeEffPlot(eff_sim_pt_recoChargedCandidate, "eff_sim_pt_recoChargedCandidate_endcap", "L2 ChargedCandidate")

    makeEffPlot(eff_sim_pt_dtseg_recoTrackExtra_endcap, "eff_sim_pt_dtseg_recoTrackExtra_endcap", "L2 TrackExtra")
    makeEffPlot(eff_sim_pt_dtseg_recoTrack_endcap, "eff_sim_pt_dtseg_recoTrack_endcap", "L2 Track")
    makeEffPlot(eff_sim_pt_dtseg_recoChargedCandidate_endcap, "eff_sim_pt_dtseg_recoChargedCandidate_endcap", "L2 ChargedCandidate")

def recoTrackEfficiency(p):
    pass

def recoChargedCandidateEfficiency(p):
    pass
