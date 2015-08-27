from ROOT import *

from Helpers import *
from ROOT import SetOwnership

def recoHits(p):
    def draw_occ(target_dir, c_title, ext, t, title, h_name, h_bins, to_draw, cut="", opt = ""):
        gStyle.SetStatStyle(0)
        gStyle.SetOptStat(1110)
        c = TCanvas("c","c",600,600)
        c.Clear()
        t.Draw(to_draw + ">>" + h_name + h_bins, cut)
        h = TH2F(gDirectory.Get(h_name))
        if not h:
            sys.exit('h does not exist')
        h = TH2F(h.Clone(h_name))
        h.SetTitle(title)
        h.SetLineWidth(2)
        h.SetLineColor(kBlue)
        h.Draw(opt)
        c.SaveAs(target_dir + c_title + ext)

        #draw_occ("./", "hits_eta", ".png", p.hlt, "Reco hit;eta;hit", "h_", "(50,-2.5,2.5,10,0,10)", "eta:nHits")#, nocut(), "COLZ")


def genKinematics(p):
    print p
    draw_1D(p,"genGdMu_eta_max", "genGdMu_eta_max",  "GEN muon eta^{max}; GEN muon eta^{max}; Entries", "(100,-5,5)")
    draw_1D(p,"genGdMu_eta_max", "genGdMu_eta_max_pt",  "GEN muon eta^{max}; GEN muon eta^{max}; Entries", "(100,-5,5)","genGdMu_pt[0]>5 && genGdMu_pt[1]>5")

    draw_1D(p,"genGdMu_p[0]", "genGdMu_p0",  "GEN Muon p; GEN Muon p [GeV/c]; Entries", "(50,0,100)")
    draw_1D(p,"genGdMu_px[0]", "genGdMu_px0",  "GEN Muon px; GEN Muon px [GeV/c]; Entries", "(50,0,100)")
    draw_1D(p,"genGdMu_py[0]", "genGdMu_py0",  "GEN Muon py; GEN Muon py [GeV/c]; Entries", "(50,0,100)")
    draw_1D(p,"genGdMu_pz[0]", "genGdMu_pz0",  "GEN Muon pz; GEN Muon pz [GeV/c]; Entries", "(50,0,100)")
    draw_1D(p,"genGdMu_pt[0]", "genGdMu_pt0",  "GEN Muon pt; GEN Muon pt [GeV/c]; Entries", "(50,0,100)")
    draw_1D(p,"genGdMu_eta[0]", "genGdMu_eta0", "GEN Muon #eta; GEN Muon #eta; Entries", "(50,-2.5,2.5)")
    draw_1D(p,"genGdMu_phi_corr[0]", "genGdMu_phi_corr0", "GEN Muon #phi^{corr}; GEN Muon #phi^{corr}; Entries", "(60,-3.1416,3.1416)")
    draw_1D(p,"genGdMu_vx[0]", "genGdMu_vx0",  "GEN Muon vx; GEN Muon vx [cm]; Entries", "(200,-100,100)")
    draw_1D(p,"genGdMu_vy[0]", "genGdMu_vy0",  "GEN Muon vy; GEN Muon vy [cm]; Entries", "(200,-100,100)")
    draw_1D(p,"genGdMu_vz[0]", "genGdMu_vz0",  "GEN Muon vz; GEN Muon vz [cm]; Entries", "(200,-100,100)")
    draw_1D(p,"genGdMu_dxy[0]", "genGdMu_dxy0",  "GEN Muon dxy; GEN Muon dxy [cm]; Entries", "(200,-100,100)")

    draw_1D(p,"genGdMu_p[1]", "genGdMu_p1",  "GEN Muon p; GEN Muon p [GeV/c]; Entries", "(50,0,100)")
    draw_1D(p,"genGdMu_px[1]", "genGdMu_px1",  "GEN Muon px; GEN Muon px [GeV/c]; Entries", "(50,0,100)")
    draw_1D(p,"genGdMu_py[1]", "genGdMu_py1",  "GEN Muon py; GEN Muon py [GeV/c]; Entries", "(50,0,100)")
    draw_1D(p,"genGdMu_pz[1]", "genGdMu_pz1",  "GEN Muon pz; GEN Muon pz [GeV/c]; Entries", "(50,0,100)")
    draw_1D(p,"genGdMu_pt[1]", "genGdMu_pt1",  "GEN Muon pt; GEN Muon pt [GeV/c]; Entries", "(50,0,100)")
    draw_1D(p,"genGdMu_eta[1]", "genGdMu_eta1", "GEN Muon #eta; GEN Muon #eta; Entries", "(50,-2.5,2.5)")
    draw_1D(p,"genGdMu_phi_corr[1]", "genGdMu_phi_corr1", "GEN Muon #phi^{corr}; GEN Muon #phi^{corr}; Entries", "(60,-3.1416,3.1416)")
    draw_1D(p,"genGdMu_vx[1]", "genGdMu_vx1",  "GEN Muon vx; GEN Muon vx [cm]; Entries", "(200,-100,100)")
    draw_1D(p,"genGdMu_vy[1]", "genGdMu_vy1",  "GEN Muon vy; GEN Muon vy [cm]; Entries", "(200,-100,100)")
    draw_1D(p,"genGdMu_vz[1]", "genGdMu_vz1",  "GEN Muon vz; GEN Muon vz [cm]; Entries", "(200,-100,100)")
    draw_1D(p,"genGdMu_dxy[1]", "genGdMu_dxy1",  "GEN Muon dxy; GEN Muon dxy [cm]; Entries", "(200,-100,100)")

def simKinematics(p):
    draw_1D(p,"sim_pt", "sim_pt",  "SimTrack p_{T}; SimTrack p_{T} [GeV/c]; Entries", "(50,0,100)")
    draw_1D(p,"sim_eta", "sim_eta", "SimTrack #eta; SimTrack #eta; Entries", "(50,-2.5,2.5)")
    draw_1D(p,"sim_phi", "sim_phi", "SimTrack #phi; SimTrack #phi; Entries", "(60,-3.1416,3.1416)")
    draw_1D(p,"abs(sim_dxy)", "sim_abs_dxy", "SimTrack d_{xy}; SimTrack d_{xy} [cm]; Entries", "(100,0,20")

    ## 
def trackKinematics(p):
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
    etaBinning = "(50,-2.5,2.5)"

    
    sim_pt = get_1D(p, "title", "sim_pt", ptBinning, "sim_pt", nocut())

    sim_pt_eta = get_1D(p, "title", "sim_pt_eta", ptBinning, "sim_pt", cms_eta())
    sim_pt_barrel = get_1D(p, "title", "sim_pt_barrel", ptBinning, "sim_pt", barrel_eta_cut())
    sim_pt_endcap = get_1D(p, "title", "sim_pt_endcap", ptBinning, "sim_pt", endcap_eta_cut())
    sim_pt_seg = get_1D(p, "title", "sim_pt_dtseg", ptBinning, "sim_pt", n_dt_csc_seg(2))

    sim_pt_L1Extra = get_1D(p, "title", "sim_pt_L1Extra", ptBinning, "sim_pt", has_trackExtra())
    sim_pt_recoTrackExtra = get_1D(p, "title", "sim_pt_recoTrackExtra", ptBinning, "sim_pt", has_trackExtra())
    sim_pt_recoTrack = get_1D(p, "title", "sim_pt_recoTrack", ptBinning, "sim_pt", has_track())
    sim_pt_recoCand = get_1D(p, "title", "sim_pt_recoCand", ptBinning, "sim_pt", has_cand())

    sim_pt_eta_L1Extra = get_1D(p, "title", "sim_pt_eta_L1Extra", ptBinning, "sim_pt", AND(has_trackExtra(), cms_eta()))
    sim_pt_eta_recoTrackExtra = get_1D(p, "title", "sim_pt_eta_recoTrackExtra", ptBinning, "sim_pt", AND(has_trackExtra(), cms_eta()))
    sim_pt_eta_recoTrack = get_1D(p, "title", "sim_pt_eta_recoTrack", ptBinning, "sim_pt", AND(has_track(), cms_eta()))
    sim_pt_eta_recoCand = get_1D(p, "title", "sim_pt_eta_recoCand", ptBinning, "sim_pt", AND(has_cand(), cms_eta()))

    sim_pt_recoTrackExtra_barrel = get_1D(p, "title", "sim_pt_recoTrackExtra_barrel", ptBinning, "sim_pt", AND(has_trackExtra(), barrel_eta_cut()))
    sim_pt_recoTrack_barrel = get_1D(p, "title", "sim_pt_recoTrack_barrel", ptBinning, "sim_pt", AND(has_track(), barrel_eta_cut()))
    sim_pt_recoCand_barrel = get_1D(p, "title", "sim_pt_recoCand_barrel", ptBinning, "sim_pt", AND(has_cand(), barrel_eta_cut()))

    sim_pt_recoTrackExtra_endcap = get_1D(p, "title", "sim_pt_recoTrackExtra_endcap", ptBinning, "sim_pt", AND(has_trackExtra(), endcap_eta_cut()))
    sim_pt_recoTrack_endcap = get_1D(p, "title", "sim_pt_recoTrack_endcap", ptBinning, "sim_pt", AND(has_track(), endcap_eta_cut()))
    sim_pt_recoCand_endcap = get_1D(p, "title", "sim_pt_recoCand_endcap", ptBinning, "sim_pt", AND(has_cand(), endcap_eta_cut()))

    ## no eta cut
    def sim_pt_sh(n=2):
        return get_1D(p, "title", "sim_pt_%dsh"%(n), ptBinning, "sim_pt", n_dt_csc_st_sh(n))
    def sim_pt_seg(n=2):
        return get_1D(p, "title", "sim_pt_%dseg"%(n), ptBinning, "sim_pt", n_dt_csc_seg(n))
    def sim_pt_eta_seg(n=2):
        return get_1D(p, "title", "sim_pt_eta_%dseg"%(n), ptBinning, "sim_pt", AND(n_dt_csc_seg(n), cms_eta()))
    def sim_pt_eta_seg_L1Extra_fid(n=2):
        return get_1D(p, "title", "sim_pt_eta_%dseg_L1Extra_fid"%(n), ptBinning, "sim_pt", AND(n_dt_csc_seg(n), cms_eta(), has_L1Extra(), Gd_fid()))
    def sim_pt_eta_seg_L1Extra_fid_recoCand(n, l2_pt):
        return get_1D(p, "title", "sim_pt_eta_%dseg_L1Extra_fid_recoCand"%(n), ptBinning, "sim_pt", AND(n_dt_csc_seg(n), cms_eta(), has_L1Extra(), Gd_fid(), has_cand(l2_pt)))
    def sim_pt_eta_seg_dxy_L1Extra_fid(n, l2_pt):
        return get_1D(p, "title", "sim_pt_eta_%dseg_dxy_L1Extra_fid"%(n), ptBinning, "sim_pt", AND(n_dt_csc_seg(n), cms_eta(), has_L1Extra(), Gd_fid(), has_cand(l2_pt), sim_dxy(20)))
    def sim_pt_eta_seg_dxy_L1Extra_fid_recoCand(n, l2_pt):
        return get_1D(p, "title", "sim_pt_eta_%dseg_dxy_L1Extra_fid_recoCand"%(n), ptBinning, "sim_pt", AND(n_dt_csc_seg(n), cms_eta(), has_L1Extra(), Gd_fid(), has_cand(l2_pt), sim_dxy(20)))
    def sim_pt_eta_seg_dxy0to10_L1Extra_fid(n):
        return get_1D(p, "title", "sim_pt_eta_%dseg_dxy0to10_L1Extra_fid"%(n), ptBinning, "sim_pt", AND(n_dt_csc_seg(n), cms_eta(), has_L1Extra(), Gd_fid(), sim_dxy(0,10)))
    def sim_pt_eta_seg_dxy10to30_L1Extra_fid(n):
        return get_1D(p, "title", "sim_pt_eta_%dseg_dxy10to30_L1Extra_fid"%(n), ptBinning, "sim_pt", AND(n_dt_csc_seg(n), cms_eta(), has_L1Extra(), Gd_fid(), sim_dxy(10,30)))
    def sim_pt_eta_seg_dxy30to500_L1Extra_fid(n):
        return get_1D(p, "title", "sim_pt_eta_%dseg_dxy30to500_L1Extra_fid"%(n), ptBinning, "sim_pt", AND(n_dt_csc_seg(n), cms_eta(), has_L1Extra(), Gd_fid(), sim_dxy(30,500)))
    def sim_pt_eta_seg_dxy0to10_L1Extra_fid_recoCand(n, l2_pt):
        return get_1D(p, "title", "sim_pt_eta_%dseg_dxy0to10_L1Extra_fid_recoCand"%(n), ptBinning, "sim_pt", AND(n_dt_csc_seg(n), cms_eta(), has_L1Extra(), Gd_fid(), has_cand(l2_pt), sim_dxy(0,10)))
    def sim_pt_eta_seg_dxy10to30_L1Extra_fid_recoCand(n, l2_pt):
        return get_1D(p, "title", "sim_pt_eta_%dseg_dxy10to30_L1Extra_fid_recoCand"%(n), ptBinning, "sim_pt", AND(n_dt_csc_seg(n), cms_eta(), has_L1Extra(), Gd_fid(), has_cand(l2_pt), sim_dxy(10,30)))
    def sim_pt_eta_seg_dxy30to500_L1Extra_fid_recoCand(n, l2_pt):
        return get_1D(p, "title", "sim_pt_eta_%dseg_dxy30to500_L1Extra_fid_recoCand"%(n), ptBinning, "sim_pt", AND(n_dt_csc_seg(n), cms_eta(), has_L1Extra(), Gd_fid(), has_cand(l2_pt), sim_dxy(30,500)))

    def sim_pt_sh_gem(n=2,m=2):
        return get_1D(p, "title", "sim_pt_%dsh_%dgem"%(n,m), ptBinning, "sim_pt", AND(n_gem_st_sh(n), n_gem_seg(m)))
    def sim_pt_sh_seg(n=2,m=2):
        return get_1D(p, "title", "sim_pt_%dsh_%dseg"%(n,m), ptBinning, "sim_pt", AND(n_dt_csc_st_sh(n), n_dt_csc_seg(m)))
    def sim_pt_seg_recoTrackExtra(n=2, l2_pt=0):
        return get_1D(p, "title", "sim_pt_%dseg_recoTrackExtra"%(n), ptBinning, "sim_pt", AND(n_dt_csc_seg(n), has_trackExtra(l2_pt)))
    def sim_pt_seg_recoTrack(n=2, l2_pt=0):
        return get_1D(p, "title", "sim_pt_%dseg_recoTrack"%(n), ptBinning, "sim_pt", AND(n_dt_csc_seg(n), has_track(l2_pt)))
    def sim_pt_seg_recoCand(n=2, l2_pt=0):
        return get_1D(p, "title", "sim_pt_%dseg_recoCand"%(n), ptBinning, "sim_pt", AND(n_dt_csc_seg(n), has_cand(l2_pt)))
    def sim_pt_eta_seg_recoCand(n=2, l2_pt=0):
        return get_1D(p, "title", "sim_pt_eta_%dseg_recoCand"%(n), ptBinning, "sim_pt", AND(n_dt_csc_seg(n), has_cand(l2_pt), cms_eta()))

    


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
    def sim_pt_seg_recoCand_barrel(n=2, l2_pt=0):
        return get_1D(p, "title", "sim_pt_%dseg_recoCand_barrel"%(n), ptBinning, "sim_pt", AND(n_dt_seg(n), has_cand(l2_pt), barrel_eta_cut()))

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
    def sim_pt_seg_recoCand_endcap(n=2, l2_pt=0):
        return get_1D(p, "title", "sim_pt_%dseg_recoCand_endcap"%(n), ptBinning, "sim_pt", AND(n_csc_seg(n), has_cand(l2_pt), endcap_eta_cut()))

    ## gem
    def sim_pt_ge11():
        return get_1D(p, "title", "sim_pt_ge11", ptBinning, "sim_pt", AND(ge11_eta_cut(), sim_dxy(0,5)))
    def sim_pt_ge21():
        return get_1D(p, "title", "sim_pt_ge21", ptBinning, "sim_pt", AND(ge21_eta_cut(), sim_dxy(0,5)))
    def sim_pt_sh_ge11():
        return get_1D(p, "title", "sim_pt_sh_ge11", ptBinning, "sim_pt", AND(has_ge11_sh(), ge11_eta_cut(), sim_dxy(0,5)))
    def sim_pt_sh_ge21():
        return get_1D(p, "title", "sim_pt_sh_ge21", ptBinning, "sim_pt", AND(has_ge21_sh(), ge21_eta_cut(), sim_dxy(0,5)))
    def sim_pt_rh_ge11():
        return get_1D(p, "title", "sim_pt_rh_ge11", ptBinning, "sim_pt", AND(has_ge11_rh(), ge11_eta_cut(), sim_dxy(0,5)))
    def sim_pt_rh_ge21():
        return get_1D(p, "title", "sim_pt_rh_ge21", ptBinning, "sim_pt", AND(has_ge21_rh(), ge21_eta_cut(), sim_dxy(0,5)))


    """
    sim_pt_dxy = get_1D(p, "title", "sim_pt_dxy", ptBinning, "sim_pt", sim_dxy(20))
    sim_pt_dxy_sh = get_1D(p, "title", "sim_pt_dxy_sh", ptBinning, "sim_pt", AND(sim_dxy(20),n_dt_csc_st_sh(2)))
    sim_pt_dxy_seg = get_1D(p, "title", "sim_pt_dxy_seg", ptBinning, "sim_pt", AND(sim_dxy(20),n_dt_csc_seg(2)))
    sim_pt_dxy_recoTrackExtra = get_1D(p, "title", "sim_pt_dxy_recoTrackExtra", ptBinning, "sim_pt", AND(sim_dxy(20),has_trackExtra()))
    sim_pt_dxy_recoTrack = get_1D(p, "title", "sim_pt_dxy_recoTrack", ptBinning, "sim_pt", AND(sim_dxy(20),has_track()))
    sim_pt_dxy_recoCand = get_1D(p, "title", "sim_pt_dxy_recoCand", ptBinning, "sim_pt", AND(sim_dxy(20),has_cand()))
    sim_pt_dxy_seg_recoTrackExtra = get_1D(p, "title", "sim_pt_dxy_seg_recoTrackExtra", ptBinning, "sim_pt", AND(sim_dxy(20),n_dt_csc_seg(2),has_trackExtra()))
    sim_pt_dxy_seg_recoTrack = get_1D(p, "title", "sim_pt_dxy_seg_recoTrack", ptBinning, "sim_pt", AND(sim_dxy(20),n_dt_csc_seg(2),has_track()))
    sim_pt_dxy_seg_recoCand = get_1D(p, "title", "sim_pt_dxy_seg_recoCand", ptBinning, "sim_pt", AND(sim_dxy(20),n_dt_csc_seg(2),has_cand()))

    sim_eta_dxy = get_1D(p, "title", "sim_eta_dxy", etaBinning, "sim_eta", sim_dxy(20))
    sim_eta_dxy_sh = get_1D(p, "title", "sim_eta_dxy_sh", etaBinning, "sim_eta", AND(sim_dxy(20),n_dt_csc_st_sh()))
    sim_eta_dxy_seg = get_1D(p, "title", "sim_eta_dxy_seg", etaBinning, "sim_eta", AND(sim_dxy(20),n_dt_csc_seg(2)))
    sim_eta_dxy_seg_recoTrackExtra = get_1D(p, "title", "sim_eta_dxy_seg_recoTrackExtra", etaBinning, "sim_eta", AND(sim_dxy(20),n_dt_csc_seg(2),has_trackExtra()))
    sim_eta_dxy_seg_recoTrack = get_1D(p, "title", "sim_eta_dxy_seg_recoTrack", etaBinning, "sim_eta", AND(sim_dxy(20),n_dt_csc_seg(2),has_track()))
    sim_eta_dxy_seg_recoCand = get_1D(p, "title", "sim_eta_dxy_seg_recoCand", etaBinning, "sim_eta", AND(sim_dxy(20),n_dt_csc_seg(2),has_cand()))
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

    def eff_sim_pt_sh_ge11():
        return clearEmptyBinsEff(TEfficiency(sim_pt_sh_ge11(), sim_pt_ge11()))
    def eff_sim_pt_sh_ge21():
        return clearEmptyBinsEff(TEfficiency(sim_pt_sh_ge21(), sim_pt_ge21()))


    ## track pT efficiencies
    def eff_sim_pt_L1Extra():
        return clearEmptyBinsEff(TEfficiency(sim_pt_L1Extra, sim_pt))
    def eff_sim_pt_recoTrackExtra():
        return clearEmptyBinsEff(TEfficiency(sim_pt_recoTrackExtra, sim_pt))
    def eff_sim_pt_recoTrack():
        return clearEmptyBinsEff(TEfficiency(sim_pt_recoTrack, sim_pt))
    def eff_sim_pt_recoCand():
        return clearEmptyBinsEff(TEfficiency(sim_pt_recoCand, sim_pt))

    def eff_sim_pt_eta_L1Extra():
        return clearEmptyBinsEff(TEfficiency(sim_pt_eta_L1Extra, sim_pt_eta))
    def eff_sim_pt_eta_recoTrackExtra():
        return clearEmptyBinsEff(TEfficiency(sim_pt_eta_recoTrackExtra, sim_pt_eta))
    def eff_sim_pt_eta_recoTrack():
        return clearEmptyBinsEff(TEfficiency(sim_pt_eta_recoTrack, sim_pt_eta))
    def eff_sim_pt_eta_recoCand():
        return clearEmptyBinsEff(TEfficiency(sim_pt_eta_recoCand, sim_pt_eta))

    def eff_sim_pt_recoTrackExtra_barrel(): 
        return clearEmptyBinsEff(TEfficiency(sim_pt_recoTrackExtra_barrel, sim_pt_barrel))
    def eff_sim_pt_recoTrack_barrel(): 
        return clearEmptyBinsEff(TEfficiency(sim_pt_recoTrack_barrel, sim_pt_barrel))
    def eff_sim_pt_recoCand_barrel(): 
        return clearEmptyBinsEff(TEfficiency(sim_pt_recoCand_barrel, sim_pt_barrel))

    def eff_sim_pt_recoTrackExtra_endcap(): 
        return clearEmptyBinsEff(TEfficiency(sim_pt_recoTrackExtra_endcap, sim_pt_endcap))
    def eff_sim_pt_recoTrack_endcap(): 
        return clearEmptyBinsEff(TEfficiency(sim_pt_recoTrack_endcap, sim_pt_endcap))
    def eff_sim_pt_recoCand_endcap(): 
        return clearEmptyBinsEff(TEfficiency(sim_pt_recoCand_endcap, sim_pt_endcap))
    
    def eff_sim_pt_seg_recoTrackExtra(n, l2_pt):
        return clearEmptyBinsEff(TEfficiency(sim_pt_seg_recoTrackExtra(n, l2_pt), sim_pt_seg(n)))
    def eff_sim_pt_seg_recoTrack(n, l2_pt):
        return clearEmptyBinsEff(TEfficiency(sim_pt_seg_recoTrack(n, l2_pt), sim_pt_seg(n)))
    def eff_sim_pt_seg_recoCand(n, l2_pt):
        return clearEmptyBinsEff(TEfficiency(sim_pt_seg_recoCand(n, l2_pt), sim_pt_seg(n)))
    def eff_sim_pt_eta_seg_L1Extra_fid_recoCand(n, l2_pt):
        return clearEmptyBinsEff(TEfficiency(sim_pt_eta_seg_L1Extra_fid_recoCand(n, l2_pt), sim_pt_eta_seg_L1Extra_fid(n)))
    def eff_sim_pt_eta_seg_dxy_L1Extra_fid_recoCand(n, l2_pt):
        return clearEmptyBinsEff(TEfficiency(sim_pt_eta_seg_L1Extra_fid_recoCand(n, l2_pt), sim_pt_eta_seg_L1Extra_fid(n)))
    def eff_sim_pt_eta_seg_dxy0to10_L1Extra_fid_recoCand(n, l2_pt):
        return clearEmptyBinsEff(TEfficiency(sim_pt_eta_seg_dxy0to10_L1Extra_fid_recoCand(n, l2_pt), sim_pt_eta_seg_dxy0to10_L1Extra_fid(n)))
    def eff_sim_pt_eta_seg_dxy10to30_L1Extra_fid_recoCand(n, l2_pt):
        return clearEmptyBinsEff(TEfficiency(sim_pt_eta_seg_dxy10to30_L1Extra_fid_recoCand(n, l2_pt), sim_pt_eta_seg_dxy10to30_L1Extra_fid(n)))
    def eff_sim_pt_eta_seg_dxy30to500_L1Extra_fid_recoCand(n, l2_pt):
        return clearEmptyBinsEff(TEfficiency(sim_pt_eta_seg_dxy30to500_L1Extra_fid_recoCand(n, l2_pt), sim_pt_eta_seg_dxy30to500_L1Extra_fid(n)))


    def eff_sim_pt_seg_recoTrackExtra_barrel(n, l2_pt):
        return clearEmptyBinsEff(TEfficiency(sim_pt_seg_recoTrackExtra_barrel(n, l2_pt), sim_pt_seg_barrel(n)))
    def eff_sim_pt_seg_recoTrack_barrel(n, l2_pt):
        return clearEmptyBinsEff(TEfficiency(sim_pt_seg_recoTrack_barrel(n, l2_pt), sim_pt_seg_barrel(n)))
    def eff_sim_pt_seg_recoCand_barrel(n, l2_pt):
        return clearEmptyBinsEff(TEfficiency(sim_pt_seg_recoCand_barrel(n, l2_pt), sim_pt_seg_barrel(n)))

    def eff_sim_pt_seg_recoTrackExtra_endcap(n, l2_pt):
        return clearEmptyBinsEff(TEfficiency(sim_pt_seg_recoTrackExtra_endcap(n, l2_pt), sim_pt_seg_endcap(n)))
    def eff_sim_pt_seg_recoTrack_endcap(n, l2_pt):
        return clearEmptyBinsEff(TEfficiency(sim_pt_seg_recoTrack_endcap(n, l2_pt), sim_pt_seg_endcap(n)))
    def eff_sim_pt_seg_recoCand_endcap(n, l2_pt):
        return clearEmptyBinsEff(TEfficiency(sim_pt_seg_recoCand_endcap(n, l2_pt), sim_pt_seg_endcap(n)))

    def eff_sim_pt_seg_recoTrackExtra_ge11(n, l2_pt):
        return clearEmptyBinsEff(TEfficiency(sim_pt_seg_recoTrackExtra_ge11(n, l2_pt), sim_pt_seg_ge11(n)))
    def eff_sim_pt_seg_recoTrack_ge11(n, l2_pt):
        return clearEmptyBinsEff(TEfficiency(sim_pt_seg_recoTrack_ge11(n, l2_pt), sim_pt_seg_ge11(n)))
    def eff_sim_pt_seg_recoCand_ge11(n, l2_pt):
        return clearEmptyBinsEff(TEfficiency(sim_pt_seg_recoCand_ge11(n, l2_pt), sim_pt_seg_ge11(n)))


    """
    eff_sim_pt_dxy_recoTrackExtra = clearEmptyBinsEff(TEfficiency(sim_pt_dxy_recoTrackExtra, sim_pt_dxy))
    eff_sim_pt_dxy_recoTrack = clearEmptyBinsEff(TEfficiency(sim_pt_dxy_recoTrack, sim_pt_dxy))
    eff_sim_pt_dxy_recoCand = clearEmptyBinsEff(TEfficiency(sim_pt_dxy_recoCand, sim_pt_dxy))

    eff_sim_pt_dxy_seg_recoTrackExtra = clearEmptyBinsEff(TEfficiency(sim_pt_dxy_seg_recoTrackExtra, sim_pt_dxy_seg))
    eff_sim_pt_dxy_seg_recoTrack = clearEmptyBinsEff(TEfficiency(sim_pt_dxy_seg_recoTrack, sim_pt_dxy_seg))
    eff_sim_pt_dxy_seg_recoCand = clearEmptyBinsEff(TEfficiency(sim_pt_dxy_seg_recoCand, sim_pt_dxy_seg))
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
        base = TH1D("base","base", 25, 0, 2.5)
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
        tex2 = applyStupidTdrStyle()

        c.SaveAs(p.outputDir + plotTitle + p.ext)

    reco_pts = [0]
    for reco_pt in reco_pts:

        for n in range(1,2):
            makePtEffPlot(getEffObject(p, "sim_pt", ptBinning, AND(n_dt_csc_seg(1), Gd_fid()), has_cand(20)), "eff_sim_pt_%dseg_pt_fid_recoCand_pt%d"%(n, reco_pt), "L2Mu")
            #makePtEffPlot(eff_sim_pt_seg_recoTrack(n, pt), "eff_sim_pt_%dseg_recoTrack_pt%d"%(n, pt), "L2 Track with %d segments, pT > %d GeV"%(n,pt))
            #makePtEffPlot(eff_sim_pt_seg_recoCand(n, pt), "eff_sim_pt_%dseg_recoCand_pt%d"%(n, pt), "L2Mu with %d segments, pT > %d GeV"%(n,pt))
            #makePtEffPlot(eff_sim_pt_eta_seg_L1Extra_fid_recoCand(n, pt), "eff_sim_pt_eta_%dseg_L1Extra_fid_recoCand_pt%d"%(n, pt), "L2Mu with %d segments, pT > %d GeV, (|#eta^{SIM}| < 2.4)"%(n,pt))

            #makePtEffPlot(eff_sim_pt_eta_seg_dxy0to10_L1Extra_fid_recoCand(n, pt), "eff_sim_pt_eta_%dseg_dxy0to10_L1Extra_fid_recoCand_pt%d"%(n, pt), "L2Mu with %d segments, pT > %d GeV, (|#eta^{SIM}| < 2.4)"%(n,pt))
            #makePtEffPlot(eff_sim_pt_eta_seg_dxy10to30_L1Extra_fid_recoCand(n, pt), "eff_sim_pt_eta_%dseg_dxy10to30_L1Extra_fid_recoCand_pt%d"%(n, pt), "L2Mu with %d segments, pT > %d GeV, (|#eta^{SIM}| < 2.4)"%(n,pt))
            #makePtEffPlot(eff_sim_pt_eta_seg_dxy30to500_L1Extra_fid_recoCand(n, pt), "eff_sim_pt_eta_%dseg_dxy30to500_L1Extra_fid_recoCand_pt%d"%(n, pt), "L2Mu with %d segments, pT > %d GeV, (|#eta^{SIM}| < 2.4)"%(n,pt))
            
            #makePtEffPlot(eff_sim_pt_seg_recoTrackExtra_barrel(n, pt), "eff_sim_pt_%dseg_recoTrackExtra_barrel_pt%d"%(n, pt), "L2 TrackExtra with %d segments, pT > %d GeV (barrel)"%(n,pt))
            #makePtEffPlot(eff_sim_pt_seg_recoTrack_barrel(n, pt), "eff_sim_pt_%dseg_recoTrack_barrel_pt%d"%(n, pt), "L2 Track with %d segments, pT > %d GeV (barrel)"%(n,pt))
            #makePtEffPlot(eff_sim_pt_seg_recoCand_barrel(n, pt), "eff_sim_pt_%dseg_recoCand_barrel_pt%d"%(n, pt), "L2Mu with %d segments, pT > %d GeV (barrel)"%(n,pt))
            
            #makePtEffPlot(eff_sim_pt_seg_recoTrackExtra_endcap(n, pt), "eff_sim_pt_%dseg_recoTrackExtra_endcap_pt%d"%(n, pt), "L2 TrackExtra with %d segments, pT > %d GeV (endcap)"%(n,pt))
            #makePtEffPlot(eff_sim_pt_seg_recoTrack_endcap(n, pt), "eff_sim_pt_%dseg_recoTrack_endcap_pt%d"%(n, pt), "L2 Track with %d segments, pT > %d GeV (endcap)"%(n,pt))
            #makePtEffPlot(eff_sim_pt_seg_recoCand_endcap(n, pt), "eff_sim_pt_%dseg_recoCand_endcap_pt%d"%(n, pt), "L2Mu with %d segments, pT > %d GeV (endcap)"%(n,pt))
            
            def denom_cut(n, simpt, dxy_min, dxy_max):
                return AND(n_dt_csc_seg(n), sim_pt(simpt), sim_dxy(dxy_min, dxy_max), has_L1Extra(), Gd_fid())

            def denom_cut2(n, simpt, dxy_min, dxy_max):
                return AND(sim_pt(simpt), sim_dxy(dxy_min, dxy_max), Gd_fid())

            simpt = reco_pt*1.1
            etaBinning = "(25,0,2.5)"
            """
            makeEtaEffPlot(getEffObject(p, "abs(sim_eta)", etaBinning, denom_cut(n, simpt, 0, 10), has_cand(reco_pt)), "eff_sim_eta_%dseg_pt_dxy0to10_L1Extra_fid_recoCand_pt%d"%(n, reco_pt), "L2Mu")
            makeEtaEffPlot(getEffObject(p, "abs(sim_eta)", etaBinning, denom_cut2(n, 5, 0, 10), has_ge11_rh(2)), "eff_sim_eta_gemseg_st1", "GE11 segment")
            makeEtaEffPlot(getEffObject(p, "abs(sim_eta)", etaBinning, denom_cut2(n, 5, 0, 10), has_ge21_rh(2)), "eff_sim_eta_gemseg_st2", "GE11 segment")
            makeEtaEffPlot(getEffObject(p, "abs(sim_eta)", etaBinning, denom_cut2(n, 5, 0, 10), OR(has_ge11_rh(2), has_ge21_rh(2))), "eff_sim_eta_gemseg_st12", "GEM segment")

            makeEtaEffPlot(getEffObject(p, "abs(sim_eta)", etaBinning, AND(denom_cut2(n, 5, 0, 10), n_rpc_st_sh(1)), n_rpc_st_rh(1)), "eff_sim_eta_rpcseg1", "1 RPC segment")
            makeEtaEffPlot(getEffObject(p, "abs(sim_eta)", etaBinning, AND(denom_cut2(n, 5, 0, 10), n_rpc_st_sh(2)), n_rpc_st_rh(2)), "eff_sim_eta_rpcseg2", "2 RPC segments")
            makeEtaEffPlot(getEffObject(p, "abs(sim_eta)", etaBinning, AND(denom_cut2(n, 5, 0, 10), n_rpc_st_sh(3)), n_rpc_st_rh(3)), "eff_sim_eta_rpcseg3", "3 RPC segments") 
            makeEtaEffPlot(getEffObject(p, "abs(sim_eta)", etaBinning, AND(denom_cut2(n, 5, 0, 10), n_rpc_st_sh(4)), n_rpc_st_rh(4)), "eff_sim_eta_rpcseg4", "4 RPC segments") 

            makeEtaEffPlot(getEffObject(p, "abs(sim_eta)", etaBinning, AND(denom_cut2(n, 5, 0, 10), n_dt_csc_st_sh(1)), n_dt_csc_seg(1)), "eff_sim_eta_dtcscseg1", "1 DT/CSC segment")
            makeEtaEffPlot(getEffObject(p, "abs(sim_eta)", etaBinning, AND(denom_cut2(n, 5, 0, 10), n_dt_csc_st_sh(2)), n_dt_csc_seg(2)), "eff_sim_eta_dtcscseg2", "2 DT/CSC segments")
            makeEtaEffPlot(getEffObject(p, "abs(sim_eta)", etaBinning, AND(denom_cut2(n, 5, 0, 10), n_dt_csc_st_sh(3)), n_dt_csc_seg(3)), "eff_sim_eta_dtcscseg3", "3 DT/CSC segments") 
            makeEtaEffPlot(getEffObject(p, "abs(sim_eta)", etaBinning, AND(denom_cut2(n, 5, 0, 10), n_dt_csc_st_sh(4)), n_dt_csc_seg(4)), "eff_sim_eta_dtcscseg4", "4 DT/CSC segments") 

            makeEtaEffPlot(getEffObject(p, "abs(sim_eta)", etaBinning, AND(denom_cut2(n, 5, 0, 10), n_dt_csc_st_sh(1)), n_dt_csc_gem_seg(1)), "eff_sim_eta_dtcscgemseg1", "1 DT/CSC/GEM segment")
            makeEtaEffPlot(getEffObject(p, "abs(sim_eta)", etaBinning, AND(denom_cut2(n, 5, 0, 10), n_dt_csc_st_sh(2)), n_dt_csc_gem_seg(2)), "eff_sim_eta_dtcscgemseg2", "2 DT/CSC/GEM segments")
            makeEtaEffPlot(getEffObject(p, "abs(sim_eta)", etaBinning, AND(denom_cut2(n, 5, 0, 10), n_dt_csc_st_sh(3)), n_dt_csc_gem_seg(3)), "eff_sim_eta_dtcscgemseg3", "3 DT/CSC/GEM segments") 
            makeEtaEffPlot(getEffObject(p, "abs(sim_eta)", etaBinning, AND(denom_cut2(n, 5, 0, 10), n_dt_csc_st_sh(4)), n_dt_csc_gem_seg(4)), "eff_sim_eta_dtcscgemseg4", "4 DT/CSC/GEM segments") 
            """
           #            makeEtaEffPlot(getEffObject(p, "abs(sim_eta)", etaBinning, denom_cut(n, simpt, 10, 30), has_cand(reco_pt)), "eff_sim_eta_%dseg_pt_dxy10to30_L1Extra_fid_recoCand_pt%d"%(n, reco_pt), "L2Mu")
            #            makeEtaEffPlot(getEffObject(p, "abs(sim_eta)", etaBinning, denom_cut(n, simpt, 30, 500), has_cand(reco_pt)), "eff_sim_eta_%dseg_pt_dxy30to500_L1Extra_fid_recoCand_pt%d"%(n, reco_pt), "L2Mu")
            
            #        makeEtaEffPlot(getEffObject(p, "abs(sim_eta)", etaBinning, denom_cut(1, simpt, 0, 10), AND(n_dt_csc_gem_rpc_seg(3), has_cand(reco_pt))), "eff_sim_eta_%dseg_pt_dxy0to10_L1Extra_fid_recoCand_pt%d_3st"%(1, reco_pt), "L2Mu")
            #        makeEtaEffPlot(getEffObject(p, "abs(sim_eta)", etaBinning, denom_cut(1, simpt, 0, 10), AND(has_cand(reco_pt))), "eff_sim_eta_%dseg_pt_dxy0to10_L1Extra_fid_recoCand_pt%d"%(1, reco_pt), "L2Mu")
            #        makeEtaEffPlot(getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_dxy(0, 10), Gd_fid()), n_dt_csc_gem_rpc_seg(3)), "eff_sim_eta_3seg", "")
            
            #        makeEtaEffPlot(getEffObject(p, "abs(sim_eta)", etaBinning, denom_cut(1, simpt, 10, 30), has_cand(reco_pt)), "eff_sim_eta_%dseg_pt_dxy10to30_L1Extra_fid_recoCand_pt%d_3st"%(1, reco_pt), "L2Mu")
            #        makeEtaEffPlot(getEffObject(p, "abs(sim_eta)", etaBinning, denom_cut(1, simpt, 30, 500), has_cand(reco_pt)), "eff_sim_eta_%dseg_pt_dxy30to500_L1Extra_fid_recoCand_pt%d_3st"%(, reco_pt), "L2Mu")
            
        """
        h1 = getEffObject(p, "sim_eta", etaBinning, denom_cut(n, simpt, 0, 10), has_cand(reco_pt))
        h2 = getEffObject(p, "sim_eta", etaBinning, denom_cut(n, simpt, 10, 30), has_cand(reco_pt))
        h3 = getEffObject(p, "sim_eta", etaBinning, denom_cut(n, simpt, 30, 500), has_cand(reco_pt))#, "eff_sim_eta_%dseg_pt_dxy30to500_L1Extra_fid_recoCand_pt%d"%(n, reco_pt), "L2Mu")
        """
    
def recoTrackEfficiency_2(p, dxy_min, dxy_max, min_sim_pt, min_l1_pt, min_reco_pt):
    return getEffObject(p, "abs(sim_eta)", "(25,0,2.5)", AND(n_dt_csc_seg(1), sim_pt(min_sim_pt), sim_dxy(dxy_min, dxy_max), has_L1Extra(min_l1_pt), Gd_fid()), AND(has_cand(min_reco_pt), cand_3_st()))
    

def pTCorrelationPlots(p):
    
    fid = 0.
    num = 0.
    tree = p.tree
    sim_pT = TH1F( 'corr', '', 50, 0, 50 )
    reco_pT = TH1F( 'corr', '', 50, 0, 50 )
    rel_pT = TH1F( 'corr', '', 50, 0, 50 )
    corr  = TH2F( 'corr', 'pT cand vs pT simtrack', 100, -0.5, 0.5, 50, 0, 0.5 )
    corr  = TH2F( 'corr', '', 100, 0, 2.4, 40, -0.2, 0.2 )
    diff  = TH1F( 'diff', 'pT cand - pT simtrack/pT simtrack', 50, -5, 5 )
    #print "entries", tree.GetEntries()
    for k in range(0, tree.GetEntries()):
        tree.GetEntry(k)
        if (tree.sim_pt > 5 and
            tree.genGdMu_pt[0] > 5 and
            tree.genGdMu_pt[1] > 5 and
            abs(tree.genGdMu_eta[0]) > 0 and 
            abs(tree.genGdMu_eta[1]) > 0 and 
            abs(tree.genGdMu_eta[0]) < 2.4 and 
            abs(tree.genGdMu_eta[1]) < 2.4 and 
            tree.genGd_lxy > 0 and
            tree.genGd_lxy < 300 and
            abs(tree.genGd_vz) < 500 and
            tree.genGd0Gd1_dR > 2 and 
            5 < abs(tree.sim_dxy) and abs(tree.sim_dxy) < 10 and 
            ## 3 station requirement
            cand_3_st_tree(tree) and
            (tree.has_l1Extra>=1 and tree.l1Extra_dR<0.1 and tree.l1Extra_pt>0) and
            (tree.has_recoChargedCandidate>=1 and tree.recoChargedCandidate_pt>0)):
            sim_pT.Fill(tree.sim_pt)
            reco_pT.Fill(tree.recoChargedCandidate_pt)
            
            corr.Fill(abs(tree.sim_eta), 1/tree.sim_pt - 1/tree.recoChargedCandidate_pt)
            diff.Fill((tree.sim_pt - tree.recoChargedCandidate_pt)/tree.sim_pt)

    ##
    nBins = sim_pT.GetNbinsX()
    for bin in range(0,nBins):
        if sim_pT.GetBinContent(bin) >0:            
            #print bin
            #print sim_pT.GetBinContent(bin)
            #print reco_pT.GetBinContent(bin)
            #print (sim_pT.GetBinContent(bin)-reco_pT.GetBinContent(bin))/sim_pT.GetBinContent(bin)
            rel_pT.SetBinContent(bin, (sim_pT.GetBinContent(bin)-reco_pT.GetBinContent(bin))/sim_pT.GetBinContent(bin))
    
    c = TCanvas("c","c",800,600)
    c.Clear()
    c.SetHighLightColor(2);
    c.Range(0,0,1,1);
    c.SetFillColor(0);
    c.SetBorderMode(0);
    c.SetBorderSize(2);
    c.SetTickx(1);
    c.SetTicky(1);
    c.SetLeftMargin(0.126);
    c.SetRightMargin(0.04);
    c.SetTopMargin(0.06);
    c.SetBottomMargin(0.13);
    c.SetFrameBorderMode(0);


    gStyle.SetTitleStyle(0)
    gStyle.SetTitleAlign(13) ##coord in top left
    gStyle.SetTitleX(0.)
    gStyle.SetTitleY(1.)
    gStyle.SetTitleW(1)
    gStyle.SetTitleH(0.058)
    #        gStyle.SetTitleXOffset(0.05)
    gStyle.SetTitleBorderSize(0)
    #        gStyle.SetPadLeftMargin(0.3)
    gStyle.SetPadLeftMargin(0.126)
    gStyle.SetPadRightMargin(0.04)
    gStyle.SetPadTopMargin(0.06)
    gStyle.SetPadBottomMargin(0.13)
    gStyle.SetOptStat(0)
    gStyle.SetMarkerStyle(1)
    gPad.SetTickx(1)
    gPad.SetTicky(1)

    corr.SetTitle("                                                                      14 TeV,  PU = %d; #eta; 1/p_{T}^{SIM} - 1/p_{T}^{RECO}"%(p.pu))
    #corr.SetTitle("p_{T} correlation                                                                                     14 TeV; p_{T}^{SIM} [GeV]; p_{T}^{RECO} [GeV]")
    corr.GetXaxis().SetLabelSize(0.05)
    corr.GetYaxis().SetLabelSize(0.05)
    corr.GetXaxis().SetTitleSize(0.06)
    corr.GetYaxis().SetTitleSize(0.06)        
    corr.SetLineWidth(2)
#    corr.SetMarkerStyle(22)
    corr.SetMarkerSize(1)
#    corr.SetMarkerColor(kBlue)        
    corr.Draw()
#    corr.Draw("COLZ")
#    tex = drawLabel(p.ctau + ", " + p.mass,0.25,0.75,0.05)
#    tex3 = drawLabel("H #rightarrow 2n_{1} #rightarrow 2n_{D}2Z_{D} #rightarrow 2n_{D}4#mu",0.25,0.65,0.05)
#    tex2 = applyStupidTdrStyle()

    c.SaveAs(p.outputDir + "simPtVsCandPt" + p.ext)


    c = TCanvas("c","c",800,600)
    c.Clear()
    c.SetHighLightColor(2);
    c.Range(0,0,1,1);
    c.SetFillColor(0);
    c.SetBorderMode(0);
    c.SetBorderSize(2);
    c.SetTickx(1);
    c.SetTicky(1);
    c.SetLeftMargin(0.126);
    c.SetRightMargin(0.04);
    c.SetTopMargin(0.06);
    c.SetBottomMargin(0.13);
    c.SetFrameBorderMode(0);


    gStyle.SetTitleStyle(0)
    gStyle.SetTitleAlign(13) ##coord in top left
    gStyle.SetTitleX(0.)
    gStyle.SetTitleY(1.)
    gStyle.SetTitleW(1)
    gStyle.SetTitleH(0.058)
    #        gStyle.SetTitleXOffset(0.05)
    gStyle.SetTitleBorderSize(0)
    #        gStyle.SetPadLeftMargin(0.3)
    gStyle.SetPadLeftMargin(0.126)
    gStyle.SetPadRightMargin(0.04)
    gStyle.SetPadTopMargin(0.06)
    gStyle.SetPadBottomMargin(0.13)
    gStyle.SetOptStat(1111111)
    gStyle.SetMarkerStyle(1)
    gPad.SetTickx(1)
    gPad.SetTicky(1)

    diff.SetTitle("                                                                      14 TeV,  PU = %d; p_{T}^{SIM} [GeV]; p_{T}^{RECO} [GeV]"%(p.pu))
    #diff.SetTitle("p_{T} diffelation                                                                                     14 TeV; p_{T}^{SIM} [GeV]; p_{T}^{RECO} [GeV]")
    diff.GetXaxis().SetLabelSize(0.05)
    diff.GetYaxis().SetLabelSize(0.05)
    diff.GetXaxis().SetTitleSize(0.06)
    diff.GetYaxis().SetTitleSize(0.06)        
    diff.SetLineWidth(2)
    diff.SetMarkerStyle(1)
    diff.SetMarkerSize(15)
#    diff.SetMarkerColor(kBlue)        
    diff.Draw()
#    diff.Draw("COLZ")
    tex = drawLabel(p.ctau + ", " + p.mass,0.25,0.75,0.05)
    tex3 = drawLabel("H #rightarrow 2n_{1} #rightarrow 2n_{D}2Z_{D} #rightarrow 2n_{D}4#mu",0.25,0.65,0.05)
    tex2 = applyStupidTdrStyle()

    c.SaveAs(p.outputDir + "DiffsimPtVsCandPt" + p.ext)

            

