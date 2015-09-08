from ROOT import *

from Helpers import *
from ROOT import SetOwnership

def l1ExtraTrackEfficiency(p):

    etaBinning = "(50,-2.5,2.5)"

    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(5), Gd_fid()), has_L1Extra()), "eff_sim_eta_pt5_fid_L1Extra_pt0", "L1Extra")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(20), Gd_fid()), has_L1Extra(17)), "eff_sim_eta_pt20_fid_L1Extra_pt17", "L1Extra")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(20), sim_dxy(0, 5), Gd_fid()), has_L1Extra(17)), "eff_sim_eta_pt20_fid_dxy0dto5_L1Extra_pt17", "L1Extra")
    

def recoTrackEfficiency(p):

    def ptEfficiencies():

        ptBinning = "(50,0,100)"

        pts = [0,0,10,15,20,25]

        for pt in pts:
            makePtEffPlot(p, getEffObject(p, "sim_pt", ptBinning, AND(cms_eta(), n_dt_csc_seg(1), Gd_fid()), has_cand(pt)), "eff_sim_pt_%dseg_pt_fid_recoCand_pt%d"%(1, pt), "L2Mu")

    def etaEfficiencies():

        etaBinning = "(50,-2.5,2.5)"

        def plot(n, min_dxy, max_dxy, min_sim_pt, min_l1_pt, min_reco_pt):
            makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(n_dt_csc_seg(n), sim_pt(min_sim_pt), sim_dxy(min_dxy, max_dxy), has_L1Extra(min_l1_pt), Gd_fid()), has_cand(min_reco_pt)), 
                           "eff_sim_eta_%dseg_pt%d_dxy%dto%d_L1Extra_pt%d_fid_recoCand_pt%d"%(n, min_sim_pt, min_dxy, max_dxy, min_l1_pt, min_reco_pt), "L2Mu")
        
        ## make plots
        plot(1, 0, 10, 22, 0, 17)

        """
        makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(min_sim_pt), sim_dxy(min_dxy, max_dxy), Gd_fid()), has_ge11_rh(2)), 
                       "eff_sim_eta_pt%d_dxy%dto%d_fid_gemseg_st1"%(min_sim_pt, min_dxy, max_dxy), "GE11 segment")
        makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(min_sim_pt), sim_dxy(min_dxy, max_dxy), Gd_fid()), has_ge21_rh(2)), 
                       "eff_sim_eta_pt%d_dxy%dto%d_fid_gemseg_st2"%(min_sim_pt, min_dxy, max_dxy), "GE21 segment")
        makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(min_sim_pt), sim_dxy(min_dxy, max_dxy), Gd_fid()), OR(has_ge11_rh(2), has_ge21_rh(2))), 
                       "eff_sim_eta_pt%d_dxy%dto%d_fid_gemseg_st12"%(min_sim_pt, min_dxy, max_dxy), "GEM segment")

        makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(min_sim_pt), sim_dxy(min_dxy, max_dxy), Gd_fid()), n_rpc_st_sh(1)), 
                       "eff_sim_eta_pt%d_dxy%dto%d_fid_rpcsh_st1"%(min_sim_pt, min_dxy, max_dxy), "1 RPC")
        makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(min_sim_pt), sim_dxy(min_dxy, max_dxy), Gd_fid()), n_rpc_st_sh(2)), 
                       "eff_sim_eta_pt%d_dxy%dto%d_fid_rpcsh_st2"%(min_sim_pt, min_dxy, max_dxy), "2 RPC")
        makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(min_sim_pt), sim_dxy(min_dxy, max_dxy), Gd_fid()), n_rpc_st_sh(3)), 
                       "eff_sim_eta_pt%d_dxy%dto%d_fid_rpcsh_st3"%(min_sim_pt, min_dxy, max_dxy), "3 RPC")
        makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(min_sim_pt), sim_dxy(min_dxy, max_dxy), Gd_fid()), n_rpc_st_sh(4)), 
                       "eff_sim_eta_pt%d_dxy%dto%d_fid_rpcsh_st4"%(min_sim_pt, min_dxy, max_dxy), "4 RPC")
        """

    ## call to functions
    etaEfficiencies()




#    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, denom_cut(1, min_sim_pt, 10, 30), has_cand(reco_pt)), "eff_sim_eta_%dseg_pt_dxy10to30_L1Extra_fid_recoCand_pt%d_3st"%(1, reco_pt), "L2Mu")
    """
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(denom_cut2(n, 5, 0, 10), n_rpc_st_sh(1)), n_rpc_st_rh(1)), "eff_sim_eta_rpcseg1", "1 RPC segment")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(denom_cut2(n, 5, 0, 10), n_rpc_st_sh(2)), n_rpc_st_rh(2)), "eff_sim_eta_rpcseg2", "2 RPC segments")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(denom_cut2(n, 5, 0, 10), n_rpc_st_sh(3)), n_rpc_st_rh(3)), "eff_sim_eta_rpcseg3", "3 RPC segments") 
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(denom_cut2(n, 5, 0, 10), n_rpc_st_sh(4)), n_rpc_st_rh(4)), "eff_sim_eta_rpcseg4", "4 RPC segments") 
    
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(denom_cut2(n, 5, 0, 10), n_dt_csc_st_sh(1)), n_dt_csc_seg(1)), "eff_sim_eta_dtcscseg1", "1 DT/CSC segment")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(denom_cut2(n, 5, 0, 10), n_dt_csc_st_sh(2)), n_dt_csc_seg(2)), "eff_sim_eta_dtcscseg2", "2 DT/CSC segments")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(denom_cut2(n, 5, 0, 10), n_dt_csc_st_sh(3)), n_dt_csc_seg(3)), "eff_sim_eta_dtcscseg3", "3 DT/CSC segments") 
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(denom_cut2(n, 5, 0, 10), n_dt_csc_st_sh(4)), n_dt_csc_seg(4)), "eff_sim_eta_dtcscseg4", "4 DT/CSC segments") 
    
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(denom_cut2(n, 5, 0, 10), n_dt_csc_st_sh(1)), n_dt_csc_gem_seg(1)), "eff_sim_eta_dtcscgemseg1", "1 DT/CSC/GEM segment")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(denom_cut2(n, 5, 0, 10), n_dt_csc_st_sh(2)), n_dt_csc_gem_seg(2)), "eff_sim_eta_dtcscgemseg2", "2 DT/CSC/GEM segments")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(denom_cut2(n, 5, 0, 10), n_dt_csc_st_sh(3)), n_dt_csc_gem_seg(3)), "eff_sim_eta_dtcscgemseg3", "3 DT/CSC/GEM segments") 
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(denom_cut2(n, 5, 0, 10), n_dt_csc_st_sh(4)), n_dt_csc_gem_seg(4)), "eff_sim_eta_dtcscgemseg4", "4 DT/CSC/GEM segments") 
    """
    #            makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, denom_cut(n, min_sim_pt, 10, 30), has_cand(reco_pt)), "eff_sim_eta_%dseg_pt_dxy10to30_L1Extra_fid_recoCand_pt%d"%(n, reco_pt), "L2Mu")
    #            makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, denom_cut(n, min_sim_pt, 30, 500), has_cand(reco_pt)), "eff_sim_eta_%dseg_pt_dxy30to500_L1Extra_fid_recoCand_pt%d"%(n, reco_pt), "L2Mu")
    
    #        makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, denom_cut(1, min_sim_pt, 0, 10), AND(n_dt_csc_gem_rpc_seg(3), has_cand(reco_pt))), "eff_sim_eta_%dseg_pt_dxy0to10_L1Extra_fid_recoCand_pt%d_3st"%(1, reco_pt), "L2Mu")
    #        makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, denom_cut(1, min_sim_pt, 0, 10), AND(has_cand(reco_pt))), "eff_sim_eta_%dseg_pt_dxy0to10_L1Extra_fid_recoCand_pt%d"%(1, reco_pt), "L2Mu")
    #        makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_dxy(0, 10), Gd_fid()), n_dt_csc_gem_rpc_seg(3)), "eff_sim_eta_3seg", "")
    
    
    #        makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, denom_cut(1, min_sim_pt, 30, 500), has_cand(reco_pt)), "eff_sim_eta_%dseg_pt_dxy30to500_L1Extra_fid_recoCand_pt%d_3st"%(, reco_pt), "L2Mu")
    
    """
    h1 = getEffObject(p, "sim_eta", etaBinning, denom_cut(n, min_sim_pt, 0, 10), has_cand(reco_pt))
    h2 = getEffObject(p, "sim_eta", etaBinning, denom_cut(n, min_sim_pt, 10, 30), has_cand(reco_pt))
    h3 = getEffObject(p, "sim_eta", etaBinning, denom_cut(n, min_sim_pt, 30, 500), has_cand(reco_pt))#, "eff_sim_eta_%dseg_pt_dxy30to500_L1Extra_fid_recoCand_pt%d"%(n, reco_pt), "L2Mu")
    """
    


    
def recoTrackEfficiency_2(p, min_dxy, max_dxy, min_sim_pt, min_l1_pt, min_reco_pt):
    return getEffObject(p, "abs(sim_eta)", "(25,0,2.5)", AND(n_dt_csc_seg(1), sim_pt(min_sim_pt), sim_dxy(min_dxy, max_dxy), has_L1Extra(min_l1_pt), Gd_fid()), AND(has_cand(min_reco_pt), cand_3_st()))
    


def special_recoTrackEfficiency(p, min_dxy, max_dxy, sim_pt_cut, min_l1_pt, reco_pt_cut):
    tree = p.tree
    denom = 0
    num = 0
    loss_pt = 0
    loss_missing = 0
    loss_3seg = 0
    num_eta = TH1F( 'num_eta', '', 25, 0, 2.4 )
    denom_eta = TH1F( 'denom_eta', '', 25, 0, 2.4 )

    for k in range(0, tree.GetEntries()):
        tree.GetEntry(k)
        if k>10000:
            break
        if (tree.sim_pt > sim_pt_cut and
            tree.genGdMu_pt[0] > 5 and
            tree.genGdMu_pt[1] > 5 and
            abs(tree.sim_eta) < 2.4 and 
            abs(tree.genGdMu_eta[0]) > 0 and 
            abs(tree.genGdMu_eta[1]) > 0 and 
            abs(tree.genGdMu_eta[0]) < 2.4 and 
            abs(tree.genGdMu_eta[1]) < 2.4 and 
            tree.genGd_lxy > 0 and
            tree.genGd_lxy < 300 and
            abs(tree.genGd_vz) < 500 and
            tree.genGd0Gd1_dR > 2 and 
            (tree.n_dt_seg + tree.n_csc_seg >= 1) and 
            (min_dxy < abs(tree.sim_dxy) and abs(tree.sim_dxy) < max_dxy) and 
            (tree.has_l1Extra>=1 and tree.l1Extra_dR<0.1 and tree.l1Extra_pt>min_l1_pt)):

            denom = denom + 1.
            denom_eta.Fill(tree.sim_eta)
            if (cand_3_st_tree_int(tree) and tree.has_recoChargedCandidate>=1 and tree.recoChargedCandidate_pt>reco_pt_cut):
                num = num + 1.
                num_eta.Fill(tree.sim_eta)
            else:
                print "Denom!", k
                print "No Num!"
                print "sim_pt", tree.sim_pt
                print "sim_eta", tree.sim_eta
                print "has_cand", tree.has_recoChargedCandidate>=1
                print "cand_pt", tree.recoChargedCandidate_pt
                print "cand_eta", tree.recoChargedCandidate_eta
                print "has 3 stubs", cand_3_st_tree_int(tree)
                print
                if tree.has_recoChargedCandidate is 0:
                    loss_missing = loss_missing + 1
                elif not cand_3_st_tree(tree):
                    loss_3seg = loss_3seg + 1
                elif tree.recoChargedCandidate_pt < reco_pt_cut:
                    loss_pt = loss_pt + 1
                    
    print "eff", num, denom, num/denom
    print "losses total", denom - num
    print "losses missing", loss_missing
    print "losses pt", loss_pt
    print "losses seg", loss_3seg

    #makeEtaEffPlot(p, , "dummy", "")
    h = TEfficiency(num_eta, denom_eta)
    h = clearEmptyBinsEff(h)
    SetOwnership(h, False)
    return h
            

