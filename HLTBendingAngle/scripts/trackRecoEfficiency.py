from ROOT import *

from Helpers import *
from ROOT import SetOwnership

def trackKinematics(p):

    draw_1D(p,"sim_pt", "sim_pt",  "SimTrack p_{T}; SimTrack p_{T} [GeV/c]; Entries", "(50,0,100)")
    draw_1D(p,"sim_eta", "sim_eta", "SimTrack #eta; SimTrack #eta; Entries", "(50,-2.5,2.5)")
    draw_1D(p,"sim_phi", "sim_phi", "SimTrack #phi; SimTrack #phi; Entries", "(60,-3.1416,3.1416)")
    draw_1D(p,"abs(sim_dxy)", "sim_abs_dxy", "SimTrack d_{xy}; SimTrack d_{xy} [cm]; Entries", "(100,0,20")

    draw_1D(p,"l1Extra_pt",  "l1Extra_pt",  "L1Extra p_{T}; L1Extra p_{T} [GeV/c]; Entries", "(50,0,100)")
    draw_1D(p,"l1Extra_eta", "l1Extra_eta", "L1Extra #eta; L1Extra #eta; Entries", "(50,-2.5,2.5)")
    draw_1D(p,"l1Extra_phi", "l1Extra_phi", "L1Extra #phi; L1Extra #phi; Entries", "(60,-3.1416,3.1416)")
    draw_1D(p,"l1Extra_dR", "l1Extra_dR", "dR(SimTrack,L1Extra); dR(SimTrack, L1Extra); Entries", "(100,0,1.0")

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
    sim_pt_seg = get_1D(p, "title", "sim_pt_dtseg", ptBinning, "sim_pt", n_dt_csc_seg(2))

    sim_pt_L1Extra = get_1D(p, "title", "sim_pt_L1Extra", ptBinning, "sim_pt", has_trackExtra())
    sim_pt_recoTrackExtra = get_1D(p, "title", "sim_pt_recoTrackExtra", ptBinning, "sim_pt", has_trackExtra())
    sim_pt_recoTrack = get_1D(p, "title", "sim_pt_recoTrack", ptBinning, "sim_pt", has_track())
    sim_pt_recoChargedCandidate = get_1D(p, "title", "sim_pt_recoChargedCandidate", ptBinning, "sim_pt", has_cand())

    sim_pt_recoTrackExtra_barrel = get_1D(p, "title", "sim_pt_recoTrackExtra_barrel", ptBinning, "sim_pt", AND(has_trackExtra(), barrel_eta_cut()))
    sim_pt_recoTrack_barrel = get_1D(p, "title", "sim_pt_recoTrack_barrel", ptBinning, "sim_pt", AND(has_track(), barrel_eta_cut()))
    sim_pt_recoChargedCandidate_barrel = get_1D(p, "title", "sim_pt_recoChargedCandidate_barrel", ptBinning, "sim_pt", AND(has_cand(), barrel_eta_cut()))

    sim_pt_recoTrackExtra_endcap = get_1D(p, "title", "sim_pt_recoTrackExtra_endcap", ptBinning, "sim_pt", AND(has_trackExtra(), endcap_eta_cut()))
    sim_pt_recoTrack_endcap = get_1D(p, "title", "sim_pt_recoTrack_endcap", ptBinning, "sim_pt", AND(has_track(), endcap_eta_cut()))
    sim_pt_recoChargedCandidate_endcap = get_1D(p, "title", "sim_pt_recoChargedCandidate_endcap", ptBinning, "sim_pt", AND(has_cand(), endcap_eta_cut()))

    ## no eta cut
    def sim_pt_sh(n=2):
        return get_1D(p, "title", "sim_pt_%dsh"%(n), ptBinning, "sim_pt", n_dt_csc_st_sh(n))
    def sim_pt_seg(n=2):
        return get_1D(p, "title", "sim_pt_%dseg"%(n), ptBinning, "sim_pt", n_dt_csc_seg(n))
    def sim_pt_sh_seg(n=2,m=2):
        return get_1D(p, "title", "sim_pt_%dsh_%dseg"%(n,m), ptBinning, "sim_pt", AND(n_dt_csc_st_sh(n), n_dt_csc_seg(m)))
    def sim_pt_seg_recoTrackExtra(n=2, l2_pt=0):
        return get_1D(p, "title", "sim_pt_%dseg_recoTrackExtra"%(n), ptBinning, "sim_pt", AND(n_dt_csc_seg(n), has_trackExtra(l2_pt)))
    def sim_pt_seg_recoTrack(n=2, l2_pt=0):
        return get_1D(p, "title", "sim_pt_%dseg_recoTrack"%(n), ptBinning, "sim_pt", AND(n_dt_csc_seg(n), has_track(l2_pt)))
    def sim_pt_seg_recoChargedCandidate(n=2, l2_pt=0):
        return get_1D(p, "title", "sim_pt_%dseg_recoChargedCandidate"%(n), ptBinning, "sim_pt", AND(n_dt_csc_seg(n), has_cand(l2_pt)))

    ## DT only
    def sim_pt_sh_barrel(n=2):
        return get_1D(p, "title", "sim_pt_%dsh_barrel"%(n), ptBinning, "sim_pt", AND(n_dt_st_sh(n), barrel_eta_cut()))
    def sim_pt_seg_barrel(n=2):
        return get_1D(p, "title", "sim_pt_%dseg_barrel"%(n), ptBinning, "sim_pt", AND(n_dt_seg(n), barrel_eta_cut()))
    def sim_pt_sh_seg_barrel(n=2,m=2):
        return get_1D(p, "title", "sim_pt_%dsh_%dseg_barrel"%(n,m), ptBinning, "sim_pt", AND(n_dt_st_sh(n), n_dt_seg(m), barrel_eta_cut()))
    def sim_pt_seg_recoTrackExtra_barrel(n=2, l2_pt=0):
        return get_1D(p, "title", "sim_pt_%dseg_recoTrackExtra_barrel"%(n), ptBinning, "sim_pt", AND(n_dt_seg(n), has_trackExtra(l2_pt), barrel_eta_cut()))
    def sim_pt_seg_recoTrack_barrel(n=2, l2_pt=0):
        return get_1D(p, "title", "sim_pt_%dseg_recoTrack_barrel"%(n), ptBinning, "sim_pt", AND(n_dt_seg(n), has_track(l2_pt), barrel_eta_cut()))
    def sim_pt_seg_recoChargedCandidate_barrel(n=2, l2_pt=0):
        return get_1D(p, "title", "sim_pt_%dseg_recoChargedCandidate_barrel"%(n), ptBinning, "sim_pt", AND(n_dt_seg(n), has_cand(l2_pt), barrel_eta_cut()))

    ## CSC only
    def sim_pt_sh_endcap(n=2):
        return get_1D(p, "title", "sim_pt_%dsh_endcap"%(n), ptBinning, "sim_pt", AND(n_csc_st_sh(n), endcap_eta_cut()))
    def sim_pt_seg_endcap(n=2):
        return get_1D(p, "title", "sim_pt_%dseg_endcap"%(n), ptBinning, "sim_pt", AND(n_csc_seg(n), endcap_eta_cut()))
    def sim_pt_sh_seg_endcap(n=2,m=2):
        return get_1D(p, "title", "sim_pt_%dsh_%dseg_endcap"%(n,m), ptBinning, "sim_pt", AND(n_csc_st_sh(n), n_csc_seg(m), endcap_eta_cut()))
    def sim_pt_seg_recoTrackExtra_endcap(n=2, l2_pt=0):
        return get_1D(p, "title", "sim_pt_%dseg_recoTrackExtra_endcap"%(n), ptBinning, "sim_pt", AND(n_csc_seg(n), has_trackExtra(l2_pt), endcap_eta_cut()))
    def sim_pt_seg_recoTrack_endcap(n=2, l2_pt=0):
        return get_1D(p, "title", "sim_pt_%dseg_recoTrack_endcap"%(n), ptBinning, "sim_pt", AND(n_csc_seg(n), has_track(l2_pt), endcap_eta_cut()))
    def sim_pt_seg_recoChargedCandidate_endcap(n=2, l2_pt=0):
        return get_1D(p, "title", "sim_pt_%dseg_recoChargedCandidate_endcap"%(n), ptBinning, "sim_pt", AND(n_csc_seg(n), has_cand(l2_pt), endcap_eta_cut()))

    ## CSC + DT
    def sim_eta():
        return get_1D(p, "title", "sim_eta", "(100,-2.5.,2.5.)", "sim_eta", nocut())
    def sim_eta_sh(n=2):
        return get_1D(p, "title", "sim_eta_%dsh"%(n), "(100,-2.5.,2.5.)", "sim_eta", n_dt_csc_st_sh(n))
    def sim_eta_seg(n=2):
        return get_1D(p, "title", "sim_eta_%dseg"%(n), "(100,-2.5.,2.5.)", "sim_eta", n_dt_csc_seg(n))
    def sim_eta_seg_dxy(n=2):
        return get_1D(p, "title", "sim_eta_%dseg_dxy"%(n), "(100,-2.5.,2.5.)", "sim_eta", AND(n_dt_csc_seg(n), dxy(20)))
    def sim_eta_sh_seg(n=2,m=2):
        return get_1D(p, "title", "sim_eta_%dsh_%dseg"%(n,m), "(100,-2.5.,2.5.)", "sim_eta", AND(n_dt_csc_st_sh(n), n_dt_csc_seg(m)))
    def sim_eta_pt(sim_pt=10):
        return get_1D(p, "title", "sim_eta_pt", "(100,-2.5.,2.5.)", "sim_eta", pt_cut(sim_pt))
    def sim_eta_sh_pt(n=2, sim_pt=10):
        return get_1D(p, "title", "sim_eta_%dsh_pt"%(n), "(100,-2.5.,2.5.)", "sim_eta", AND(n_dt_csc_st_sh(n), pt_cut(sim_pt)))
    def sim_eta_seg_pt(n=2, sim_pt=20):
        return get_1D(p, "title", "sim_eta_%dseg_pt"%(n), "(100,-2.5.,2.5.)", "sim_eta", AND(n_dt_csc_seg(n), pt_cut(sim_pt)))
    def sim_eta_seg_pt_L1Extra(n=2, sim_pt=20):
        return get_1D(p, "title", "sim_eta_%dseg_pt_L1Extra"%(n), "(100,-2.5.,2.5.)", "sim_eta", AND(n_dt_csc_seg(n), pt_cut(sim_pt), has_L1Extra()))
    def sim_eta_seg_pt_dxy(n=2, sim_pt=20):
        return get_1D(p, "title", "sim_eta_%dseg_pt_dxy"%(n), "(100,-2.5.,2.5.)", "sim_eta", AND(n_dt_csc_seg(n), pt_cut(sim_pt), dxy(20)))
    def sim_eta_seg_pt_dxy_L1Extra(n=2, sim_pt=20):
        return get_1D(p, "title", "sim_eta_%dseg_pt_dxy_L1Extra"%(n), "(100,-2.5.,2.5.)", "sim_eta", AND(n_dt_csc_seg(n), pt_cut(sim_pt), dxy(20), has_L1Extra()))
    def sim_eta_sh_seg_pt(n=2,m=2, sim_pt=10):
        return get_1D(p, "title", "sim_eta_%dsh_%dseg_pt"%(n,m), "(100,-2.5.,2.5.)", "sim_eta", AND(n_dt_csc_st_sh(n), n_dt_csc_seg(m), pt_cut(sim_pt)))

    def sim_eta_L1Extra(l1_pt=0):
        return get_1D(p, "title", "sim_eta_L1Extra", "(100,-2.5.,2.5.)", "sim_eta", has_L1Extra(l1_pt))
    def sim_eta_recoTrackExtra(l2_pt=0):
        return get_1D(p, "title", "sim_eta_recoTrackExtra", "(100,-2.5.,2.5.)", "sim_eta", has_trackExtra(l2_pt))
    def sim_eta_recoTrack(l2_pt=0):
        return get_1D(p, "title", "sim_eta_recoTrack", "(100,-2.5.,2.5.)", "sim_eta", has_track(l2_pt))
    def sim_eta_recoChargedCandidate(l2_pt=0):
        return get_1D(p, "title", "sim_eta_recoChargedCandidate", "(100,-2.5.,2.5.)", "sim_eta", has_cand(l2_pt))

    def sim_eta_seg_recoTrackExtra(n=2, l2_pt=0):
        return get_1D(p, "title", "sim_eta_%dseg_recoTrackExtra"%(n), "(100,-2.5.,2.5.)", "sim_eta", AND(n_dt_csc_seg(n), has_trackExtra(l2_pt)))
    def sim_eta_seg_recoTrack(n=2, l2_pt=0):
        return get_1D(p, "title", "sim_eta_%dseg_recoTrack"%(n), "(100,-2.5.,2.5.)", "sim_eta", AND(n_dt_csc_seg(n), has_track(l2_pt)))
    def sim_eta_seg_recoChargedCandidate(n=2, l2_pt=0):
        return get_1D(p, "title", "sim_eta_%dseg_recoChargedCandidate"%(n), "(100,-2.5.,2.5.)", "sim_eta", AND(n_dt_csc_seg(n), has_cand(l2_pt)))

    def sim_eta_seg_pt_recoTrackExtra(n=2, pt=20, l2_pt=0):
        return get_1D(p, "title", "sim_eta_%dseg_pt_recoTrackExtra"%(n), "(100,-2.5.,2.5.)", "sim_eta", AND(n_dt_csc_seg(n), pt_cut(pt), has_trackExtra(l2_pt)))
    def sim_eta_seg_pt_recoTrack(n=2, pt=20, l2_pt=0):
        return get_1D(p, "title", "sim_eta_%dseg_pt_recoTrack"%(n), "(100,-2.5.,2.5.)", "sim_eta", AND(n_dt_csc_seg(n), pt_cut(pt), has_track(l2_pt)))
    def sim_eta_seg_pt_recoChargedCandidate(n=2, pt=20, l2_pt=0):
        return get_1D(p, "title", "sim_eta_%dseg_pt_recoChargedCandidate"%(n), "(100,-2.5.,2.5.)", "sim_eta", AND(n_dt_csc_seg(n), pt_cut(pt), has_cand(l2_pt)))

    def sim_eta_seg_pt_L1Extra_recoTrackExtra(n=2, pt=20, l2_pt=0):
        return get_1D(p, "title", "sim_eta_%dseg_pt_L1Extra_recoTrackExtra"%(n), "(100,-2.5.,2.5.)", "sim_eta", AND(n_dt_csc_seg(n), pt_cut(pt), has_trackExtra(l2_pt), has_L1Extra()))
    def sim_eta_seg_pt_L1Extra_recoTrack(n=2, pt=20, l2_pt=0):
        return get_1D(p, "title", "sim_eta_%dseg_pt_L1Extra_recoTrack"%(n), "(100,-2.5.,2.5.)", "sim_eta", AND(n_dt_csc_seg(n), pt_cut(pt), has_track(l2_pt), has_L1Extra()))
    def sim_eta_seg_pt_L1Extra_recoChargedCandidate(n=2, pt=20, l2_pt=0):
        return get_1D(p, "title", "sim_eta_%dseg_pt_L1Extra_recoChargedCandidate"%(n), "(100,-2.5.,2.5.)", "sim_eta", AND(n_dt_csc_seg(n), pt_cut(pt), has_cand(l2_pt), has_L1Extra()))

    def sim_eta_seg_pt_dxy_recoTrackExtra(n=2, pt=20, l2_pt=0):
        return get_1D(p, "title", "sim_eta_%dseg_pt_dxy_recoTrackExtra"%(n), "(100,-2.5.,2.5.)", "sim_eta", AND(n_dt_csc_seg(n), pt_cut(pt), has_trackExtra(l2_pt), dxy(20)))
    def sim_eta_seg_pt_dxy_recoTrack(n=2, pt=20, l2_pt=0):
        return get_1D(p, "title", "sim_eta_%dseg_pt_dxy_recoTrack"%(n), "(100,-2.5.,2.5.)", "sim_eta", AND(n_dt_csc_seg(n), pt_cut(pt), has_track(l2_pt), dxy(20)))
    def sim_eta_seg_pt_dxy_recoChargedCandidate(n=2, pt=20, l2_pt=0):
        return get_1D(p, "title", "sim_eta_%dseg_pt_dxy_recoChargedCandidate"%(n), "(100,-2.5.,2.5.)", "sim_eta", AND(n_dt_csc_seg(n), pt_cut(pt), has_cand(l2_pt), dxy(20)))

    def sim_eta_seg_pt_dxy_L1Extra_recoTrackExtra(n=2, pt=20, l2_pt=0):
        return get_1D(p, "title", "sim_eta_%dseg_pt_dxy_L1Extra_recoTrackExtra"%(n), "(100,-2.5.,2.5.)", "sim_eta", AND(n_dt_csc_seg(n), pt_cut(pt), has_trackExtra(l2_pt), dxy(20), has_L1Extra()))
    def sim_eta_seg_pt_dxy_L1Extra_recoTrack(n=2, pt=20, l2_pt=0):
        return get_1D(p, "title", "sim_eta_%dseg_pt_dxy_L1Extra_recoTrack"%(n), "(100,-2.5.,2.5.)", "sim_eta", AND(n_dt_csc_seg(n), pt_cut(pt), has_track(l2_pt), dxy(20), has_L1Extra()))
    def sim_eta_seg_pt_dxy_L1Extra_recoChargedCandidate(n=2, pt=20, l2_pt=0):
        return get_1D(p, "title", "sim_eta_%dseg_pt_dxy_L1Extra_recoChargedCandidate"%(n), "(100,-2.5.,2.5.)", "sim_eta", AND(n_dt_csc_seg(n), pt_cut(pt), has_cand(l2_pt), dxy(20), has_L1Extra()))

    """
    sim_pt_dxy = get_1D(p, "title", "sim_pt_dxy", ptBinning, "sim_pt", dxy(20))
    sim_pt_dxy_sh = get_1D(p, "title", "sim_pt_dxy_sh", ptBinning, "sim_pt", AND(dxy(20),n_dt_csc_st_sh(2)))
    sim_pt_dxy_seg = get_1D(p, "title", "sim_pt_dxy_seg", ptBinning, "sim_pt", AND(dxy(20),n_dt_csc_seg(2)))
    sim_pt_dxy_recoTrackExtra = get_1D(p, "title", "sim_pt_dxy_recoTrackExtra", ptBinning, "sim_pt", AND(dxy(20),has_trackExtra()))
    sim_pt_dxy_recoTrack = get_1D(p, "title", "sim_pt_dxy_recoTrack", ptBinning, "sim_pt", AND(dxy(20),has_track()))
    sim_pt_dxy_recoChargedCandidate = get_1D(p, "title", "sim_pt_dxy_recoChargedCandidate", ptBinning, "sim_pt", AND(dxy(20),has_cand()))
    sim_pt_dxy_seg_recoTrackExtra = get_1D(p, "title", "sim_pt_dxy_seg_recoTrackExtra", ptBinning, "sim_pt", AND(dxy(20),n_dt_csc_seg(2),has_trackExtra()))
    sim_pt_dxy_seg_recoTrack = get_1D(p, "title", "sim_pt_dxy_seg_recoTrack", ptBinning, "sim_pt", AND(dxy(20),n_dt_csc_seg(2),has_track()))
    sim_pt_dxy_seg_recoChargedCandidate = get_1D(p, "title", "sim_pt_dxy_seg_recoChargedCandidate", ptBinning, "sim_pt", AND(dxy(20),n_dt_csc_seg(2),has_cand()))

    sim_eta_dxy = get_1D(p, "title", "sim_eta_dxy", "(100,-2.5.,2.5.)", "sim_eta", dxy(20))
    sim_eta_dxy_sh = get_1D(p, "title", "sim_eta_dxy_sh", "(100,-2.5.,2.5.)", "sim_eta", AND(dxy(20),n_dt_csc_st_sh()))
    sim_eta_dxy_seg = get_1D(p, "title", "sim_eta_dxy_seg", "(100,-2.5.,2.5.)", "sim_eta", AND(dxy(20),n_dt_csc_seg(2)))
    sim_eta_dxy_seg_recoTrackExtra = get_1D(p, "title", "sim_eta_dxy_seg_recoTrackExtra", "(100,-2.5.,2.5.)", "sim_eta", AND(dxy(20),n_dt_csc_seg(2),has_trackExtra()))
    sim_eta_dxy_seg_recoTrack = get_1D(p, "title", "sim_eta_dxy_seg_recoTrack", "(100,-2.5.,2.5.)", "sim_eta", AND(dxy(20),n_dt_csc_seg(2),has_track()))
    sim_eta_dxy_seg_recoChargedCandidate = get_1D(p, "title", "sim_eta_dxy_seg_recoChargedCandidate", "(100,-2.5.,2.5.)", "sim_eta", AND(dxy(20),n_dt_csc_seg(2),has_cand()))
    """

    ## simhit pT efficiencies
    def eff_sim_pt_sh(n):
        return clearEmptyBinsEff(TEfficiency(sim_pt_sh(n), sim_pt))
    def eff_sim_pt_sh_barrel(n):
        return clearEmptyBinsEff(TEfficiency(sim_pt_sh_barrel(n), sim_pt_barrel))
    def eff_sim_pt_sh_endcap(n):
        return clearEmptyBinsEff(TEfficiency(sim_pt_sh_endcap(n), sim_pt_endcap))
    def eff_sim_pt_sh_seg(n,m):
        return clearEmptyBinsEff(TEfficiency(sim_pt_sh_seg(n,m), sim_pt_sh(n)))
    def eff_sim_pt_sh_seg_barrel(n,m):
        return clearEmptyBinsEff(TEfficiency(sim_pt_sh_seg_barrel(n,m), sim_pt_sh_barrel(n)))
    def eff_sim_pt_sh_seg_endcap(n,m):
        return clearEmptyBinsEff(TEfficiency(sim_pt_sh_seg_endcap(n,m), sim_pt_sh_endcap(n)))
    def eff_sim_pt_seg(n):
        return clearEmptyBinsEff(TEfficiency(sim_pt_seg(n), sim_pt))
    def eff_sim_pt_seg_barrel(n):
        return clearEmptyBinsEff(TEfficiency(sim_pt_seg_barrel(n), sim_pt_barrel))
    def eff_sim_pt_seg_endcap(n):
        return clearEmptyBinsEff(TEfficiency(sim_pt_seg_endcap(n), sim_pt_endcap))
		
    ## simhit eta efficiencies
    def eff_sim_eta_sh(n, pt=10):
        return clearEmptyBinsEff(TEfficiency(sim_eta_sh_pt(n,pt), sim_eta_pt(pt)))
    def eff_sim_eta_sh_seg(n, m, pt=10):
        return clearEmptyBinsEff(TEfficiency(sim_eta_sh_seg_pt(n,m,pt), sim_eta_sh_pt(n,pt)))
    def eff_sim_eta_seg(n, pt):
        return clearEmptyBinsEff(TEfficiency(sim_eta_seg_pt(n,pt), sim_eta_pt(pt)))
        
    ## track pT efficiencies
    def eff_sim_pt_L1Extra():
        return clearEmptyBinsEff(TEfficiency(sim_pt_L1Extra, sim_pt))
    def eff_sim_pt_recoTrackExtra():
        return clearEmptyBinsEff(TEfficiency(sim_pt_recoTrackExtra, sim_pt))
    def eff_sim_pt_recoTrack():
        return clearEmptyBinsEff(TEfficiency(sim_pt_recoTrack, sim_pt))
    def eff_sim_pt_recoChargedCandidate():
        return clearEmptyBinsEff(TEfficiency(sim_pt_recoChargedCandidate, sim_pt))

    def eff_sim_pt_recoTrackExtra_barrel(): 
        return clearEmptyBinsEff(TEfficiency(sim_pt_recoTrackExtra_barrel, sim_pt_barrel))
    def eff_sim_pt_recoTrack_barrel(): 
        return clearEmptyBinsEff(TEfficiency(sim_pt_recoTrack_barrel, sim_pt_barrel))
    def eff_sim_pt_recoChargedCandidate_barrel(): 
        return clearEmptyBinsEff(TEfficiency(sim_pt_recoChargedCandidate_barrel, sim_pt_barrel))

    def eff_sim_pt_recoTrackExtra_endcap(): 
        return clearEmptyBinsEff(TEfficiency(sim_pt_recoTrackExtra_endcap, sim_pt_endcap))
    def eff_sim_pt_recoTrack_endcap(): 
        return clearEmptyBinsEff(TEfficiency(sim_pt_recoTrack_endcap, sim_pt_endcap))
    def eff_sim_pt_recoChargedCandidate_endcap(): 
        return clearEmptyBinsEff(TEfficiency(sim_pt_recoChargedCandidate_endcap, sim_pt_endcap))
    
    def eff_sim_pt_seg_recoTrackExtra(n, l2_pt):
        return clearEmptyBinsEff(TEfficiency(sim_pt_seg_recoTrackExtra(n, l2_pt), sim_pt_seg(n)))
    def eff_sim_pt_seg_recoTrack(n, l2_pt):
        return clearEmptyBinsEff(TEfficiency(sim_pt_seg_recoTrack(n, l2_pt), sim_pt_seg(n)))
    def eff_sim_pt_seg_recoChargedCandidate(n, l2_pt):
        return clearEmptyBinsEff(TEfficiency(sim_pt_seg_recoChargedCandidate(n, l2_pt), sim_pt_seg(n)))

    def eff_sim_pt_seg_recoTrackExtra_barrel(n, l2_pt):
        return clearEmptyBinsEff(TEfficiency(sim_pt_seg_recoTrackExtra_barrel(n, l2_pt), sim_pt_seg_barrel(n)))
    def eff_sim_pt_seg_recoTrack_barrel(n, l2_pt):
        return clearEmptyBinsEff(TEfficiency(sim_pt_seg_recoTrack_barrel(n, l2_pt), sim_pt_seg_barrel(n)))
    def eff_sim_pt_seg_recoChargedCandidate_barrel(n, l2_pt):
        return clearEmptyBinsEff(TEfficiency(sim_pt_seg_recoChargedCandidate_barrel(n, l2_pt), sim_pt_seg_barrel(n)))

    def eff_sim_pt_seg_recoTrackExtra_endcap(n, l2_pt):
        return clearEmptyBinsEff(TEfficiency(sim_pt_seg_recoTrackExtra_endcap(n, l2_pt), sim_pt_seg_endcap(n)))
    def eff_sim_pt_seg_recoTrack_endcap(n, l2_pt):
        return clearEmptyBinsEff(TEfficiency(sim_pt_seg_recoTrack_endcap(n, l2_pt), sim_pt_seg_endcap(n)))
    def eff_sim_pt_seg_recoChargedCandidate_endcap(n, l2_pt):
        return clearEmptyBinsEff(TEfficiency(sim_pt_seg_recoChargedCandidate_endcap(n, l2_pt), sim_pt_seg_endcap(n)))

    ## track eta efficiencies
    def eff_sim_eta_L1Extra():
        print "denom", sim_eta().GetEntries()
        print "num", sim_eta_L1Extra().GetEntries()
        return clearEmptyBinsEff(TEfficiency(sim_eta_L1Extra(), sim_eta()))
    def eff_sim_eta_recoTrackExtra():
        return clearEmptyBinsEff(TEfficiency(sim_eta_recoTrackExtra(), sim_eta()))
    def eff_sim_eta_recoTrack():
        return clearEmptyBinsEff(TEfficiency(sim_eta_recoTrack(), sim_eta()))
    def eff_sim_eta_recoChargedCandidate():
        return clearEmptyBinsEff(TEfficiency(sim_eta_recoChargedCandidate(), sim_eta()))

    def eff_sim_eta_seg_recoTrackExtra(n, l2_pt):
        return clearEmptyBinsEff(TEfficiency(sim_eta_seg_recoTrackExtra(n, l2_pt), sim_eta_seg(n)))
    def eff_sim_eta_seg_recoTrack(n, l2_pt):
        return clearEmptyBinsEff(TEfficiency(sim_eta_seg_recoTrack(n, l2_pt), sim_eta_seg(n)))
    def eff_sim_eta_seg_recoChargedCandidate(n, l2_pt):
        return clearEmptyBinsEff(TEfficiency(sim_eta_seg_recoChargedCandidate(n, l2_pt), sim_eta_seg(n)))

    def eff_sim_eta_seg_pt_L1Extra_recoTrackExtra(n, pt):
        return clearEmptyBinsEff(TEfficiency(sim_eta_seg_pt_L1Extra_recoTrackExtra(n,pt), sim_eta_seg_pt_L1Extra(n, pt)))
    def eff_sim_eta_seg_pt_L1Extra_recoTrack(n, pt):
        return clearEmptyBinsEff(TEfficiency(sim_eta_seg_pt_L1Extra_recoTrack(n,pt), sim_eta_seg_pt_L1Extra(n, pt)))
    def eff_sim_eta_seg_pt_L1Extra_recoChargedCandidate(n, pt):
        return clearEmptyBinsEff(TEfficiency(sim_eta_seg_pt_L1Extra_recoChargedCandidate(n,pt), sim_eta_seg_pt_L1Extra(n, pt)))

    def eff_sim_eta_seg_pt_dxy_recoTrackExtra(n, pt):
        return clearEmptyBinsEff(TEfficiency(sim_eta_seg_pt_dxy_recoTrackExtra(n,pt), sim_eta_seg_pt_dxy(n, pt)))
    def eff_sim_eta_seg_pt_dxy_recoTrack(n, pt):
        return clearEmptyBinsEff(TEfficiency(sim_eta_seg_pt_dxy_recoTrack(n,pt), sim_eta_seg_pt_dxy(n, pt)))
    def eff_sim_eta_seg_pt_dxy_recoChargedCandidate(n, pt):
        return clearEmptyBinsEff(TEfficiency(sim_eta_seg_pt_dxy_recoChargedCandidate(n,pt), sim_eta_seg_pt_dxy(n, pt)))

    def eff_sim_eta_seg_pt_dxy_L1Extra_recoTrackExtra(n, pt):
        return clearEmptyBinsEff(TEfficiency(sim_eta_seg_pt_dxy_L1Extra_recoTrackExtra(n,pt), sim_eta_seg_pt_dxy_L1Extra(n, pt)))
    def eff_sim_eta_seg_pt_dxy_L1Extra_recoTrack(n, pt):
        return clearEmptyBinsEff(TEfficiency(sim_eta_seg_pt_dxy_L1Extra_recoTrack(n,pt), sim_eta_seg_pt_dxy_L1Extra(n, pt)))
    def eff_sim_eta_seg_pt_dxy_L1Extra_recoChargedCandidate(n, pt):
        return clearEmptyBinsEff(TEfficiency(sim_eta_seg_pt_dxy_L1Extra_recoChargedCandidate(n,pt), sim_eta_seg_pt_dxy_L1Extra(n, pt)))

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
        base = TH1D("base","base", 50, -2.5, 2.5)
        base.SetStats(0)
        base.SetTitle("                                                                      14 TeV,  PU = %d; SimTrack #eta; Reconstruction efficiency"%(p.pu))
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
    makeSimHitsPlots = False
    if makeSimHitsPlots:
        makePtEffPlot(eff_sim_pt_sh(1), "eff_sim_pt_1sh", "1 DT/CSC Station with SimHits")
        makePtEffPlot(eff_sim_pt_sh(2), "eff_sim_pt_2sh", "2 DT/CSC Station with SimHits")
        makePtEffPlot(eff_sim_pt_sh(3), "eff_sim_pt_3sh", "3 DT/CSC Station with SimHits")
        makePtEffPlot(eff_sim_pt_sh(4), "eff_sim_pt_4sh", "4 DT/CSC Station with SimHits")
    
        makePtEffPlot(eff_sim_pt_sh_barrel(1), "eff_sim_pt_1sh_barrel", "1 DT Station with SimHits")
        makePtEffPlot(eff_sim_pt_sh_barrel(2), "eff_sim_pt_2sh_barrel", "2 DT Station with SimHits")
        makePtEffPlot(eff_sim_pt_sh_barrel(3), "eff_sim_pt_3sh_barrel", "3 DT Station with SimHits")
        makePtEffPlot(eff_sim_pt_sh_barrel(4), "eff_sim_pt_4sh_barrel", "4 DT Station with SimHits")

        makePtEffPlot(eff_sim_pt_sh_endcap(1), "eff_sim_pt_1sh_endcap", "1 CSC Station with SimHits")
        makePtEffPlot(eff_sim_pt_sh_endcap(2), "eff_sim_pt_2sh_endcap", "2 CSC Station with SimHits")
        makePtEffPlot(eff_sim_pt_sh_endcap(3), "eff_sim_pt_3sh_endcap", "3 CSC Station with SimHits")
        makePtEffPlot(eff_sim_pt_sh_endcap(4), "eff_sim_pt_4sh_endcap", "4 CSC Station with SimHits")

        makeEtaEffPlot(eff_sim_eta_sh(1), "eff_sim_eta_1sh", "1 DT/CSC Station with SimHits")
        makeEtaEffPlot(eff_sim_eta_sh(2), "eff_sim_eta_2sh", "2 DT/CSC Station with SimHits")
        makeEtaEffPlot(eff_sim_eta_sh(3), "eff_sim_eta_3sh", "3 DT/CSC Station with SimHits")
        makeEtaEffPlot(eff_sim_eta_sh(4), "eff_sim_eta_4sh", "4 DT/CSC Station with SimHits")

        sim_pts = [10, 15, 20]
        for pt in sim_pts:
            makeEtaEffPlot(eff_sim_eta_sh(1,pt), "eff_sim_eta_1sh_pt%d"%(pt), "1 DT/CSC Station with SimHits (pT>%d GeV)"%(pt))
            makeEtaEffPlot(eff_sim_eta_sh(2,pt), "eff_sim_eta_2sh_pt%d"%(pt), "2 DT/CSC Station with SimHits (pT>%d GeV)"%(pt))
            makeEtaEffPlot(eff_sim_eta_sh(3,pt), "eff_sim_eta_3sh_pt%d"%(pt), "3 DT/CSC Station with SimHits (pT>%d GeV)"%(pt))
            makeEtaEffPlot(eff_sim_eta_sh(4,pt), "eff_sim_eta_4sh_pt%d"%(pt), "4 DT/CSC Station with SimHits (pT>%d GeV)"%(pt))

    makeSegmentPlotsWithHits = False
    if makeSegmentPlotsWithHits:
        makePtEffPlot(eff_sim_pt_sh_seg(1,1), "eff_sim_pt_1sh_1seg", "1 DT/CSC Station with Segments")
        makePtEffPlot(eff_sim_pt_sh_seg(2,2), "eff_sim_pt_2sh_2seg", "2 DT/CSC Station with Segments")
        makePtEffPlot(eff_sim_pt_sh_seg(3,3), "eff_sim_pt_3sh_3seg", "3 DT/CSC Station with Segments")
        makePtEffPlot(eff_sim_pt_sh_seg(4,4), "eff_sim_pt_4sh_4seg", "4 DT/CSC Station with Segments")
                      
        makePtEffPlot(eff_sim_pt_sh_seg_barrel(1,1), "eff_sim_pt_1sh_1seg_barrel", "1 DT Station with Segments")
        makePtEffPlot(eff_sim_pt_sh_seg_barrel(2,2), "eff_sim_pt_2sh_2seg_barrel", "2 DT Station with Segments")
        makePtEffPlot(eff_sim_pt_sh_seg_barrel(3,3), "eff_sim_pt_3sh_3seg_barrel", "3 DT Station with Segments")
        makePtEffPlot(eff_sim_pt_sh_seg_barrel(4,4), "eff_sim_pt_4sh_4seg_barrel", "4 DT Station with Segments")

        makePtEffPlot(eff_sim_pt_sh_seg_endcap(1,1), "eff_sim_pt_1sh_1seg_endcap", "1 CSC Station with Segments")
        makePtEffPlot(eff_sim_pt_sh_seg_endcap(2,2), "eff_sim_pt_2sh_2seg_endcap", "2 CSC Station with Segments")
        makePtEffPlot(eff_sim_pt_sh_seg_endcap(3,3), "eff_sim_pt_3sh_3seg_endcap", "3 CSC Station with Segments")
        makePtEffPlot(eff_sim_pt_sh_seg_endcap(4,4), "eff_sim_pt_4sh_4seg_endcap", "4 CSC Station with Segments")

        makeEtaEffPlot(eff_sim_eta_sh_seg(1,1), "eff_sim_eta_1sh_1seg", "1 DT/CSC Station with Segments")
        makeEtaEffPlot(eff_sim_eta_sh_seg(2,2), "eff_sim_eta_2sh_2seg", "2 DT/CSC Station with Segments")
        makeEtaEffPlot(eff_sim_eta_sh_seg(3,3), "eff_sim_eta_3sh_3seg", "3 DT/CSC Station with Segments")
        makeEtaEffPlot(eff_sim_eta_sh_seg(4,4), "eff_sim_eta_4sh_4seg", "4 DT/CSC Station with Segments")

        sim_pts = [10, 15, 20]
        for pt in sim_pts:
            makeEtaEffPlot(eff_sim_eta_sh_seg(1,1,pt), "eff_sim_eta_1sh_1seg_pt%d"%(pt), "1 DT/CSC Station with Segments (pT>%d GeV)"%(pt))
            makeEtaEffPlot(eff_sim_eta_sh_seg(2,2,pt), "eff_sim_eta_2sh_2seg_pt%d"%(pt), "2 DT/CSC Station with Segments (pT>%d GeV)"%(pt))
            makeEtaEffPlot(eff_sim_eta_sh_seg(3,3,pt), "eff_sim_eta_3sh_3seg_pt%d"%(pt), "3 DT/CSC Station with Segments (pT>%d GeV)"%(pt))
            makeEtaEffPlot(eff_sim_eta_sh_seg(4,4,pt), "eff_sim_eta_4sh_4seg_pt%d"%(pt), "4 DT/CSC Station with Segments (pT>%d GeV)"%(pt))

    makeSegmentPlotsWithoutHits = False
    if makeSegmentPlotsWithoutHits:
        makePtEffPlot(eff_sim_pt_seg(1), "eff_sim_pt_1seg_endcap", "1 CSC/DT Station with Segments")
        makePtEffPlot(eff_sim_pt_seg(2), "eff_sim_pt_2seg_endcap", "2 CSC/DT Station with Segments")
        makePtEffPlot(eff_sim_pt_seg(3), "eff_sim_pt_3seg_endcap", "3 CSC/DT Station with Segments")
        makePtEffPlot(eff_sim_pt_seg(4), "eff_sim_pt_4seg_endcap", "4 CSC/DT Station with Segments")
        
        makePtEffPlot(eff_sim_pt_seg_endcap(1), "eff_sim_pt_1seg_endcap", "1 CSC Station with Segments")
        makePtEffPlot(eff_sim_pt_seg_endcap(2), "eff_sim_pt_2seg_endcap", "2 CSC Station with Segments")
        makePtEffPlot(eff_sim_pt_seg_endcap(3), "eff_sim_pt_3seg_endcap", "3 CSC Station with Segments")
        makePtEffPlot(eff_sim_pt_seg_endcap(4), "eff_sim_pt_4seg_endcap", "4 CSC Station with Segments")
        
        makePtEffPlot(eff_sim_pt_seg_barrel(1), "eff_sim_pt_1seg_barrel", "1 DT Station with Segments")
        makePtEffPlot(eff_sim_pt_seg_barrel(2), "eff_sim_pt_2seg_barrel", "2 DT Station with Segments")
        makePtEffPlot(eff_sim_pt_seg_barrel(3), "eff_sim_pt_3seg_barrel", "3 DT Station with Segments")
        makePtEffPlot(eff_sim_pt_seg_barrel(4), "eff_sim_pt_4seg_barrel", "4 DT Station with Segments")

        makeEtaEffPlot(eff_sim_eta_seg(1), "eff_sim_eta_1seg", "1 DT/CSC Station with Segments")
        makeEtaEffPlot(eff_sim_eta_seg(2), "eff_sim_eta_2seg", "2 DT/CSC Station with Segments")
        makeEtaEffPlot(eff_sim_eta_seg(3), "eff_sim_eta_3seg", "3 DT/CSC Station with Segments")
        makeEtaEffPlot(eff_sim_eta_seg(4), "eff_sim_eta_4seg", "4 DT/CSC Station with Segments")

    ## tracks 
    pt=0
    makeEtaEffPlot(eff_sim_eta_L1Extra(), "eff_sim_eta_L1Extra", "L1 Extra")
    makeEtaEffPlot(eff_sim_eta_recoTrackExtra(), "eff_sim_eta_recoTrackExtra", "L2 TrackExtra")
    makeEtaEffPlot(eff_sim_eta_recoTrack(), "eff_sim_eta_recoTrack", "L2 Track")
    makeEtaEffPlot(eff_sim_eta_recoChargedCandidate(), "eff_sim_eta_recoChargedCandidate", "L2 Candidate")

    makePtEffPlot(eff_sim_pt_L1Extra(), "eff_sim_pt_L1Extra", "L1 Extra")
    makePtEffPlot(eff_sim_pt_recoTrackExtra(), "eff_sim_pt_recoTrackExtra", "L2 TrackExtra")
    makePtEffPlot(eff_sim_pt_recoTrack(), "eff_sim_pt_recoTrack", "L2 Track")
    makePtEffPlot(eff_sim_pt_recoChargedCandidate(), "eff_sim_pt_recoChargedCandidate", "L2 Candidate")

    '''
    makePtEffPlot(eff_sim_pt_recoTrackExtra(), "eff_sim_pt_recoTrackExtra_pt%d"%(pt), "L2 TrackExtra, pT > %d GeV"%(pt))
    makePtEffPlot(eff_sim_pt_recoTrack(), "eff_sim_pt_recoTrack_pt%d"%(pt), "L2 Track, pT > %d GeV"%(pt))
    makePtEffPlot(eff_sim_pt_recoChargedCandidate(), "eff_sim_pt_recoChargedCandidate_pt%d"%(pt), "L2 Candidate, pT > %d GeV"%(pt))
    '''

    sim_pts = [10, 15, 20]
    for pt in sim_pts:

        for n in range(2,5):
            makePtEffPlot(eff_sim_pt_seg_recoTrackExtra(n, pt), "eff_sim_pt_%dseg_recoTrackExtra_pt%d"%(n, pt), "L2 TrackExtra with %d segments, pT > %d GeV"%(n,pt))
            makePtEffPlot(eff_sim_pt_seg_recoTrack(n, pt), "eff_sim_pt_%dseg_recoTrack_pt%d"%(n, pt), "L2 Track with %d segments, pT > %d GeV"%(n,pt))
            makePtEffPlot(eff_sim_pt_seg_recoChargedCandidate(n, pt), "eff_sim_pt_%dseg_recoChargedCandidate_pt%d"%(n, pt), "L2 Candidate with %d segments, pT > %d GeV"%(n,pt))
            
            makeEtaEffPlot(eff_sim_eta_seg_recoTrackExtra(n, pt), "eff_sim_eta_%dseg_recoTrackExtra_pt%d"%(n, pt), "L2 TrackExtra with %d segments, pT > %d GeV"%(n,pt))
            makeEtaEffPlot(eff_sim_eta_seg_recoTrack(n, pt), "eff_sim_eta_%dseg_recoTrack_pt%d"%(n, pt), "L2 Track with %d segments, pT > %d GeV"%(n,pt))
            makeEtaEffPlot(eff_sim_eta_seg_recoChargedCandidate(n, pt), "eff_sim_eta_%dseg_recoChargedCandidate_pt%d"%(n, pt), "L2 Candidate with %d segments, pT > %d GeV"%(n,pt))
            
            makePtEffPlot(eff_sim_pt_seg_recoTrackExtra_barrel(n, pt), "eff_sim_pt_%dseg_recoTrackExtra_barrel_pt%d"%(n, pt), "L2 TrackExtra with %d segments, pT > %d GeV (barrel)"%(n,pt))
            makePtEffPlot(eff_sim_pt_seg_recoTrack_barrel(n, pt), "eff_sim_pt_%dseg_recoTrack_barrel_pt%d"%(n, pt), "L2 Track with %d segments, pT > %d GeV (barrel)"%(n,pt))
            makePtEffPlot(eff_sim_pt_seg_recoChargedCandidate_barrel(n, pt), "eff_sim_pt_%dseg_recoChargedCandidate_barrel_pt%d"%(n, pt), "L2 Candidate with %d segments, pT > %d GeV (barrel)"%(n,pt))
            
            makePtEffPlot(eff_sim_pt_seg_recoTrackExtra_endcap(n, pt), "eff_sim_pt_%dseg_recoTrackExtra_endcap_pt%d"%(n, pt), "L2 TrackExtra with %d segments, pT > %d GeV (endcap)"%(n,pt))
            makePtEffPlot(eff_sim_pt_seg_recoTrack_endcap(n, pt), "eff_sim_pt_%dseg_recoTrack_endcap_pt%d"%(n, pt), "L2 Track with %d segments, pT > %d GeV (endcap)"%(n,pt))
            makePtEffPlot(eff_sim_pt_seg_recoChargedCandidate_endcap(n, pt), "eff_sim_pt_%dseg_recoChargedCandidate_endcap_pt%d"%(n, pt), "L2 Candidate with %d segments, pT > %d GeV (endcap)"%(n,pt))

            makeEtaEffPlot(eff_sim_eta_seg_pt_dxy_recoTrackExtra(n, pt), "eff_sim_eta_%dseg_pt%d_dxy_recoTrackExtra"%(n, pt), "L2 TrackExtra with %d segments"%(n))
            makeEtaEffPlot(eff_sim_eta_seg_pt_dxy_recoTrack(n, pt), "eff_sim_eta_%dseg_pt%d_dxy_recoTrack"%(n, pt), "L2 Track with %d segments"%(n))
            makeEtaEffPlot(eff_sim_eta_seg_pt_dxy_recoChargedCandidate(n, pt), "eff_sim_eta_%dseg_pt%d_dxy_recoChargedCandidate"%(n, pt), "L2 Candidate with %d segments"%(n))
            
            ##L1Extra 
            makeEtaEffPlot(eff_sim_eta_seg_pt_L1Extra_recoTrackExtra(n, pt), "eff_sim_eta_%dseg_pt%d_L1Extra_recoTrackExtra"%(n, pt), "L2 TrackExtra with %d segments and L1Extra"%(n))
            makeEtaEffPlot(eff_sim_eta_seg_pt_L1Extra_recoTrack(n, pt), "eff_sim_eta_%dseg_pt%d_L1Extra_recoTrack"%(n, pt), "L2 Track with %d segments and L1Extra"%(n))
            makeEtaEffPlot(eff_sim_eta_seg_pt_L1Extra_recoChargedCandidate(n, pt), "eff_sim_eta_%dseg_pt%d_L1Extra_recoChargedCandidate"%(n, pt), "L2 Candidate with %d segments and L1Extra"%(n))

            makeEtaEffPlot(eff_sim_eta_seg_pt_dxy_L1Extra_recoTrackExtra(n, pt), "eff_sim_eta_%dseg_pt%d_dxy_L1Extra_recoTrackExtra"%(n, pt), "L2 TrackExtra with %d segments and L1Extra"%(n))
            makeEtaEffPlot(eff_sim_eta_seg_pt_dxy_L1Extra_recoTrack(n, pt), "eff_sim_eta_%dseg_pt%d_dxy_L1Extra_recoTrack"%(n, pt), "L2 Track with %d segments and L1Extra"%(n))
            makeEtaEffPlot(eff_sim_eta_seg_pt_dxy_L1Extra_recoChargedCandidate(n, pt), "eff_sim_eta_%dseg_pt%d_dxy_L1Extra_recoChargedCandidate"%(n, pt), "L2 Candidate with %d segments and L1Extra"%(n))

    makeTrackPlotsWithoutSegments = False
    if makeTrackPlotsWithoutSegments:
    ## tracks
        makePtEffPlot(eff_sim_pt_recoTrackExtra(), "eff_sim_pt_recoTrackExtra", "L2 TrackExtra")
        makePtEffPlot(eff_sim_pt_recoTrack(), "eff_sim_pt_recoTrack", "L2 Track")
        makePtEffPlot(eff_sim_pt_recoChargedCandidate(), "eff_sim_pt_recoChargedCandidate", "L2 Candidate")
        
        makePtEffPlot(eff_sim_pt_recoTrackExtra_barrel(), "eff_sim_pt_recoTrackExtra_barrel", "L2 TrackExtra")
        makePtEffPlot(eff_sim_pt_recoTrack(), "eff_sim_pt_recoTrack_barrel", "L2 Track")
        makePtEffPlot(eff_sim_pt_recoChargedCandidate(), "eff_sim_pt_recoChargedCandidate_barrel", "L2 Candidate")

        makePtEffPlot(eff_sim_pt_recoTrackExtra_endcap(), "eff_sim_pt_recoTrackExtra_endcap", "L2 TrackExtra")
        makePtEffPlot(eff_sim_pt_recoTrack(), "eff_sim_pt_recoTrack_endcap", "L2 Track")
        makePtEffPlot(eff_sim_pt_recoChargedCandidate(), "eff_sim_pt_recoChargedCandidate_endcap", "L2 Candidate")
        
