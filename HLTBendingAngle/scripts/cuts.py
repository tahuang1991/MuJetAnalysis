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
def sim_dxy(min_dxy, max_dxy=999):
    return TCut("%f < abs(sim_dxy) && abs(sim_dxy) < %f"%(min_dxy, max_dxy))

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

    return AND(total_cut1, total_cut2, extra_cut1, extra_cut2, extra_cut3)

#_______________________________________________________________________________
def sim_pt(pt):
    return TCut("sim_pt>%f"%(pt))

#_______________________________________________________________________________
def sim_q(q):
    return TCut("sim_charge==%d"%(q))

#_______________________________________________________________________________
def sim_vz(vz_max = 30):
    return TCut("sim_vz < %f"%(vz_max))

#_______________________________________________________________________________
def cms_eta():
    return TCut("abs(sim_eta)<2.4")

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
def cand_seg_st(n):
    return OR(cand_dt_st(n), cand_csc_st(n))

#_______________________________________________________________________________
def cand_rpcgem_st(n):
    return OR(cand_rpcf_st(n), cand_rpcb_st(n), cand_gem_st(n))

#_______________________________________________________________________________
def cand_rpcgem_e_st(n):
    return OR(cand_rpcf_st(n), cand_gem_st(n))

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
def cand_3_st():
    ## 3 segments 
    TFormula.SetMaxima(100000,1000,1000000)
    cut = OR(AND(cand_dt_st(1), cand_dt_st(2), cand_dt_st(3)),
             AND(cand_dt_st(1), cand_dt_st(2), cand_dt_st(4)),
             AND(cand_dt_st(1), cand_dt_st(3), cand_dt_st(4)),
             AND(cand_dt_st(2), cand_dt_st(3), cand_dt_st(4)),
             
             AND(cand_csc_st(1), cand_csc_st(2), cand_csc_st(3)),
             AND(cand_csc_st(1), cand_csc_st(2), cand_csc_st(4)),
             AND(cand_csc_st(1), cand_csc_st(3), cand_csc_st(4)),
             AND(cand_csc_st(2), cand_csc_st(3), cand_csc_st(4)),

             
             AND(cand_dt_st(1), cand_dt_st(2), cand_csc_st(1)),
             AND(cand_dt_st(1), cand_dt_st(2), cand_csc_st(2)),
             AND(cand_dt_st(1), cand_dt_st(2), cand_csc_st(3)),
             AND(cand_dt_st(1), cand_dt_st(2), cand_csc_st(4)),

             AND(cand_dt_st(1), cand_dt_st(3), cand_csc_st(1)),
             AND(cand_dt_st(2), cand_dt_st(3), cand_csc_st(1)),

             AND(cand_dt_st(1), cand_csc_st(1), cand_csc_st(2)),
             AND(cand_dt_st(1), cand_csc_st(1), cand_csc_st(3)),
             AND(cand_dt_st(1), cand_csc_st(1), cand_csc_st(4)),

             AND(cand_dt_st(1), cand_csc_st(2), cand_csc_st(3)),
             AND(cand_dt_st(1), cand_csc_st(2), cand_csc_st(4)),

             AND(cand_dt_st(1), cand_csc_st(3), cand_csc_st(4)),

             AND(cand_dt_st(2), cand_csc_st(1), cand_csc_st(2)),
             AND(cand_dt_st(2), cand_csc_st(1), cand_csc_st(3)),

             # 2 segments and 1 other hit (barrel)
             AND(cand_dt_st(1), cand_dt_st(2), cand_rpcb_st(3)), 
             AND(cand_dt_st(1), cand_dt_st(2), cand_rpcb_st(4)),

             AND(cand_dt_st(1), cand_dt_st(3), cand_rpcb_st(2)),
             AND(cand_dt_st(1), cand_dt_st(3), cand_rpcb_st(4)),
 
             AND(cand_dt_st(1), cand_dt_st(4), cand_rpcb_st(2)),
             AND(cand_dt_st(1), cand_dt_st(4), cand_rpcb_st(3)),

             AND(cand_dt_st(2), cand_dt_st(3), cand_rpcb_st(1)),
             AND(cand_dt_st(2), cand_dt_st(3), cand_rpcb_st(4)),

             AND(cand_dt_st(2), cand_dt_st(4), cand_rpcb_st(1)),
             AND(cand_dt_st(2), cand_dt_st(4), cand_rpcb_st(3)),
             
             AND(cand_dt_st(3), cand_dt_st(4), cand_rpcb_st(1)),
             AND(cand_dt_st(3), cand_dt_st(4), cand_rpcb_st(2)),
             
             # 2 segments and 1 other hit (overlap)
             AND(cand_dt_st(1), cand_dt_st(2), cand_rpcf_st(1)), 
             AND(cand_dt_st(1), cand_dt_st(2), cand_rpcf_st(2)), 
             
             AND(cand_dt_st(1), cand_csc_st(1), cand_rpcf_st(2)), 
             AND(cand_dt_st(1), cand_csc_st(1), cand_rpcf_st(3)), 
             AND(cand_dt_st(1), cand_csc_st(1), cand_rpcf_st(4)), 

             AND(cand_dt_st(1), cand_csc_st(2), cand_rpcf_st(1)), 
             AND(cand_dt_st(1), cand_csc_st(2), cand_rpcf_st(3)), 
             AND(cand_dt_st(1), cand_csc_st(2), cand_rpcf_st(4)), 
             
             AND(cand_dt_st(1), cand_csc_st(3), cand_rpcf_st(1)), 
             AND(cand_dt_st(1), cand_csc_st(3), cand_rpcf_st(2)), 
             AND(cand_dt_st(1), cand_csc_st(3), cand_rpcf_st(4)), 
             
             AND(cand_dt_st(1), cand_csc_st(4), cand_rpcf_st(1)), 
             AND(cand_dt_st(1), cand_csc_st(4), cand_rpcf_st(2)), 
             AND(cand_dt_st(1), cand_csc_st(4), cand_rpcf_st(3)), 
             
             AND(cand_rpcb_st(1), cand_dt_st(2), cand_csc_st(1)), 
             AND(cand_rpcb_st(1), cand_dt_st(2), cand_csc_st(2)), 
             AND(cand_rpcb_st(1), cand_dt_st(2), cand_csc_st(3)), 
             AND(cand_rpcb_st(1), cand_dt_st(2), cand_csc_st(4)), 

             AND(cand_rpcb_st(2), cand_dt_st(1), cand_csc_st(1)), 
             AND(cand_rpcb_st(2), cand_dt_st(1), cand_csc_st(2)), 
             AND(cand_rpcb_st(2), cand_dt_st(1), cand_csc_st(3)), 
             AND(cand_rpcb_st(2), cand_dt_st(1), cand_csc_st(4)), 

             AND(cand_rpcb_st(1), cand_csc_st(1), cand_csc_st(2)), 
             AND(cand_rpcb_st(1), cand_csc_st(1), cand_csc_st(3)), 
             AND(cand_rpcb_st(1), cand_csc_st(1), cand_csc_st(4)), 
             AND(cand_rpcb_st(1), cand_csc_st(2), cand_csc_st(3)), 
             AND(cand_rpcb_st(1), cand_csc_st(2), cand_csc_st(4)), 
             AND(cand_rpcb_st(1), cand_csc_st(3), cand_csc_st(4)), 

             # 2 segments and 1 other hit (endcap)
             AND(cand_csc_st(1), cand_csc_st(2), cand_rpcgem_e_st(3)),
             AND(cand_csc_st(1), cand_csc_st(2), cand_rpcgem_e_st(4)),
             AND(cand_csc_st(1), cand_csc_st(3), cand_rpcgem_e_st(2)),
             AND(cand_csc_st(1), cand_csc_st(3), cand_rpcgem_e_st(4)),
             AND(cand_csc_st(1), cand_csc_st(4), cand_rpcgem_e_st(2)),
             AND(cand_csc_st(1), cand_csc_st(4), cand_rpcgem_e_st(3)),

             AND(cand_csc_st(2), cand_csc_st(3), cand_rpcgem_e_st(4)),
             AND(cand_csc_st(2), cand_csc_st(4), cand_rpcgem_e_st(3)),

             AND(cand_csc_st(3), cand_csc_st(4), cand_rpcgem_e_st(1)),
             )
    return cut

#_______________________________________________________________________________
def cand_3_st_tree(mytree):
    ## 3 segments 
    return ( (mytree.cand_dt_st_1>0 and mytree.cand_dt_st_2>0 and mytree.cand_dt_st_3>0) or
             (mytree.cand_dt_st_1>0 and mytree.cand_dt_st_2>0 and mytree.cand_dt_st_4>0) or
             (mytree.cand_dt_st_1>0 and mytree.cand_dt_st_3>0 and mytree.cand_dt_st_4>0) or
             (mytree.cand_dt_st_2>0 and mytree.cand_dt_st_3>0 and mytree.cand_dt_st_4>0) or
             
             (mytree.cand_csc_st_1>0 and mytree.cand_csc_st_2>0 and mytree.cand_csc_st_3>0) or
             (mytree.cand_csc_st_1>0 and mytree.cand_csc_st_2>0 and mytree.cand_csc_st_4>0) or
             (mytree.cand_csc_st_1>0 and mytree.cand_csc_st_3>0 and mytree.cand_csc_st_4>0) or
             (mytree.cand_csc_st_2>0 and mytree.cand_csc_st_3>0 and mytree.cand_csc_st_4>0) or

             
             (mytree.cand_dt_st_1>0 and mytree.cand_dt_st_2>0 and mytree.cand_csc_st_1>0) or
             (mytree.cand_dt_st_1>0 and mytree.cand_dt_st_2>0 and mytree.cand_csc_st_2>0) or
             (mytree.cand_dt_st_1>0 and mytree.cand_dt_st_2>0 and mytree.cand_csc_st_3>0) or
             (mytree.cand_dt_st_1>0 and mytree.cand_dt_st_2>0 and mytree.cand_csc_st_4>0) or

             (mytree.cand_dt_st_1>0 and mytree.cand_dt_st_3>0 and mytree.cand_csc_st_1>0) or
             (mytree.cand_dt_st_2>0 and mytree.cand_dt_st_3>0 and mytree.cand_csc_st_1>0) or

             (mytree.cand_dt_st_1>0 and mytree.cand_csc_st_1>0 and mytree.cand_csc_st_2>0) or
             (mytree.cand_dt_st_1>0 and mytree.cand_csc_st_1>0 and mytree.cand_csc_st_3>0) or
             (mytree.cand_dt_st_1>0 and mytree.cand_csc_st_1>0 and mytree.cand_csc_st_4>0) or

             (mytree.cand_dt_st_1>0 and mytree.cand_csc_st_2>0 and mytree.cand_csc_st_3>0) or
             (mytree.cand_dt_st_1>0 and mytree.cand_csc_st_2>0 and mytree.cand_csc_st_4>0) or

             (mytree.cand_dt_st_1>0 and mytree.cand_csc_st_3>0 and mytree.cand_csc_st_4>0) or

             (mytree.cand_dt_st_2>0 and mytree.cand_csc_st_1>0 and mytree.cand_csc_st_2>0) or
             (mytree.cand_dt_st_2>0 and mytree.cand_csc_st_1>0 and mytree.cand_csc_st_3>0) or

             # 2 segments and 1 other hit (barrel)
             (mytree.cand_dt_st_1>0 and mytree.cand_dt_st_2>0 and mytree.cand_rpcb_st_3>0) or 
             (mytree.cand_dt_st_1>0 and mytree.cand_dt_st_2>0 and mytree.cand_rpcb_st_4>0) or

             (mytree.cand_dt_st_1>0 and mytree.cand_dt_st_3>0 and mytree.cand_rpcb_st_2>0) or
             (mytree.cand_dt_st_1>0 and mytree.cand_dt_st_3>0 and mytree.cand_rpcb_st_4>0) or
 
             (mytree.cand_dt_st_1>0 and mytree.cand_dt_st_4>0 and mytree.cand_rpcb_st_2>0) or
             (mytree.cand_dt_st_1>0 and mytree.cand_dt_st_4>0 and mytree.cand_rpcb_st_3>0) or

             (mytree.cand_dt_st_2>0 and mytree.cand_dt_st_3>0 and mytree.cand_rpcb_st_1>0) or
             (mytree.cand_dt_st_2>0 and mytree.cand_dt_st_3>0 and mytree.cand_rpcb_st_4>0) or

             (mytree.cand_dt_st_2>0 and mytree.cand_dt_st_4>0 and mytree.cand_rpcb_st_1>0) or
             (mytree.cand_dt_st_2>0 and mytree.cand_dt_st_4>0 and mytree.cand_rpcb_st_3>0) or
             
             (mytree.cand_dt_st_3>0 and mytree.cand_dt_st_4>0 and mytree.cand_rpcb_st_1>0) or
             (mytree.cand_dt_st_3>0 and mytree.cand_dt_st_4>0 and mytree.cand_rpcb_st_2>0) or
             
             # 2 segments and 1 other hit (overlap)
             (mytree.cand_dt_st_1>0 and mytree.cand_dt_st_2>0 and mytree.cand_rpcf_st_1>0) or 
             (mytree.cand_dt_st_1>0 and mytree.cand_dt_st_2>0 and mytree.cand_rpcf_st_2>0) or 
             
             (mytree.cand_dt_st_1>0 and mytree.cand_csc_st_1>0 and mytree.cand_rpcf_st_2>0) or 
             (mytree.cand_dt_st_1>0 and mytree.cand_csc_st_1>0 and mytree.cand_rpcf_st_3>0) or 
             (mytree.cand_dt_st_1>0 and mytree.cand_csc_st_1>0 and mytree.cand_rpcf_st_4>0) or 

             (mytree.cand_dt_st_1>0 and mytree.cand_csc_st_2>0 and mytree.cand_rpcf_st_1>0) or 
             (mytree.cand_dt_st_1>0 and mytree.cand_csc_st_2>0 and mytree.cand_rpcf_st_3>0) or 
             (mytree.cand_dt_st_1>0 and mytree.cand_csc_st_2>0 and mytree.cand_rpcf_st_4>0) or 
             
             (mytree.cand_dt_st_1>0 and mytree.cand_csc_st_3>0 and mytree.cand_rpcf_st_1>0) or 
             (mytree.cand_dt_st_1>0 and mytree.cand_csc_st_3>0 and mytree.cand_rpcf_st_2>0) or 
             (mytree.cand_dt_st_1>0 and mytree.cand_csc_st_3>0 and mytree.cand_rpcf_st_4>0) or 
             
             (mytree.cand_dt_st_1>0 and mytree.cand_csc_st_4>0 and mytree.cand_rpcf_st_1>0) or 
             (mytree.cand_dt_st_1>0 and mytree.cand_csc_st_4>0 and mytree.cand_rpcf_st_2>0) or 
             (mytree.cand_dt_st_1>0 and mytree.cand_csc_st_4>0 and mytree.cand_rpcf_st_3>0) or 
             
             (mytree.cand_rpcb_st_1>0 and mytree.cand_dt_st_2>0 and mytree.cand_csc_st_1>0) or 
             (mytree.cand_rpcb_st_1>0 and mytree.cand_dt_st_2>0 and mytree.cand_csc_st_2>0) or 
             (mytree.cand_rpcb_st_1>0 and mytree.cand_dt_st_2>0 and mytree.cand_csc_st_3>0) or 
             (mytree.cand_rpcb_st_1>0 and mytree.cand_dt_st_2>0 and mytree.cand_csc_st_4>0) or 

             (mytree.cand_rpcb_st_2>0 and mytree.cand_dt_st_1>0 and mytree.cand_csc_st_1>0) or 
             (mytree.cand_rpcb_st_2>0 and mytree.cand_dt_st_1>0 and mytree.cand_csc_st_2>0) or 
             (mytree.cand_rpcb_st_2>0 and mytree.cand_dt_st_1>0 and mytree.cand_csc_st_3>0) or 
             (mytree.cand_rpcb_st_2>0 and mytree.cand_dt_st_1>0 and mytree.cand_csc_st_4>0) or 

             (mytree.cand_rpcb_st_1>0 and mytree.cand_csc_st_1>0 and mytree.cand_csc_st_2>0) or 
             (mytree.cand_rpcb_st_1>0 and mytree.cand_csc_st_1>0 and mytree.cand_csc_st_3>0) or 
             (mytree.cand_rpcb_st_1>0 and mytree.cand_csc_st_1>0 and mytree.cand_csc_st_4>0) or 
             (mytree.cand_rpcb_st_1>0 and mytree.cand_csc_st_2>0 and mytree.cand_csc_st_3>0) or 
             (mytree.cand_rpcb_st_1>0 and mytree.cand_csc_st_2>0 and mytree.cand_csc_st_4>0) or 
             (mytree.cand_rpcb_st_1>0 and mytree.cand_csc_st_3>0 and mytree.cand_csc_st_4>0) or 

             # 2 segments and 1 other hit (endcap)
             (mytree.cand_csc_st_1>0 and mytree.cand_csc_st_2>0 and mytree.cand_rpcf_st_3>0) or
             (mytree.cand_csc_st_1>0 and mytree.cand_csc_st_2>0 and mytree.cand_rpcf_st_4>0) or
             (mytree.cand_csc_st_1>0 and mytree.cand_csc_st_3>0 and mytree.cand_gem_st_2>0) or
             (mytree.cand_csc_st_1>0 and mytree.cand_csc_st_3>0 and mytree.cand_rpcf_st_4>0) or
             (mytree.cand_csc_st_1>0 and mytree.cand_csc_st_4>0 and mytree.cand_gem_st_2>0) or
             (mytree.cand_csc_st_1>0 and mytree.cand_csc_st_4>0 and mytree.cand_rpcf_st_3>0) or

             (mytree.cand_csc_st_2>0 and mytree.cand_csc_st_3>0 and mytree.cand_rpcf_st_4>0) or
             (mytree.cand_csc_st_2>0 and mytree.cand_csc_st_4>0 and mytree.cand_rpcf_st_3>0) or
             
             (mytree.cand_csc_st_3>0 and mytree.cand_csc_st_4>0 and mytree.cand_gem_st_1>0)
             )

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
