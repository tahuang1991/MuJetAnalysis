from ROOT import *
from logic import *

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
    extra_cut2 = Gd_vz(500)
    extra_cut3 = Gd_lxy(300, 0.)
    extra_cut4 = cms_eta()

    return AND(total_cut1, total_cut2, extra_cut1, extra_cut2, extra_cut3, extra_cut4)

#_______________________________________________________________________________
def sim_pt(min_pt, max_pt=99999):
    return TCut("%f < sim_pt && sim_pt < %f"%(min_pt, max_pt))

#_______________________________________________________________________________
def sim_eta(min_eta=0, max_eta=2.4):
    return TCut("%f < abs(sim_eta) && abs(sim_eta) < %f"%(min_eta, max_eta))

#_______________________________________________________________________________
def cms_eta():
    return TCut("abs(sim_eta)<2.4")

#_______________________________________________________________________________
def sim_dxy(min_dxy, max_dxy=999):
    return TCut("%f < abs(sim_dxy) && abs(sim_dxy) < %f"%(min_dxy, max_dxy))

#_______________________________________________________________________________
def sim_q(q):
    return TCut("sim_charge==%d"%(q))

#_______________________________________________________________________________
def sim_vz(vz_max = 30):
    return TCut("sim_vz < %f"%(vz_max))

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
def has_cand(pt_min=0, pt_max=9999):
    return AND(TCut("has_recoChargedCandidate>=1"), 
               TCut("recoChargedCandidate_pt>%f"%(pt_min)), 
               TCut("recoChargedCandidate_pt<%f"%(pt_max)))

#_______________________________________________________________________________
def has_cand2():
    return TCut("has_recoChargedCandidate>=1")

#_______________________________________________________________________________
def cand_pt(pt_min=0):
    return TCut("recoChargedCandidate_pt>%f"%(pt_min))
                
#_______________________________________________________________________________
def has_cand_too_low():
    return AND(TCut("has_recoChargedCandidate>=1"), 
               TCut("recoChargedCandidate_pt<0.8*sim_pt"))
