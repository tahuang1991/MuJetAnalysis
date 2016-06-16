from ROOT import *

from Helpers import *
from ROOT import SetOwnership

def l1ExtraTrackEfficiency(p):

    etaBinning = "(50,-2.5,2.5)"

    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(5), Gd_fid()), has_L1Extra()), "eff_sim_eta_pt5_fid_L1Extra_pt0", "L1Extra")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(20), Gd_fid()), has_L1Extra(17)), "eff_sim_eta_pt20_fid_L1Extra_pt17", "L1Extra")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(20), sim_dxy(0, 5), Gd_fid()), has_L1Extra(17)), "eff_sim_eta_pt20_fid_dxy0dto5_L1Extra_pt17", "L1Extra")
    

def recoTrackEfficiency(p):

    ptBinning = "(50,0,100)"
    pts = [0,0,10,15,20,25]
    for pt in pts:
        makePtEffPlot(p, getEffObject(p, "sim_pt", ptBinning, AND(cms_eta(), n_dt_csc_seg(1), Gd_fid()), has_cand(pt)), "eff_sim_pt_%dseg_pt_fid_recoCand_pt%d"%(1, pt), "L2Mu")

    etaBinning = "(50,0,2.5)"
    
    def plot(n, min_dxy, max_dxy, min_sim_pt, min_l1_pt, min_reco_pt):
        makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(n_dt_csc_seg(n), sim_pt(min_sim_pt), sim_dxy(min_dxy, max_dxy), has_L1Extra(min_l1_pt), Gd_fid()), has_cand(min_reco_pt)),
                       "eff_sim_eta_%dseg_pt%d_dxy%dto%d_L1Extra_pt%d_fid_recoCand_pt%d"%(n, min_sim_pt, min_dxy, max_dxy, min_l1_pt, min_reco_pt), "L2Mu")
        
    ## make plots
    plot(1, 0, 0.1, 10, 0, 0)

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

        
def L1TrackEfficiency(p, min_dxy, max_dxy, min_sim_pt, min_l1_pt=0):
    ## vs eta
    efficiency = getEffObject(p, "abs(sim_eta)", "(25,0,2.5)", AND(sim_pt(min_sim_pt), sim_dxy(min_dxy, max_dxy), Gd_fid()), has_L1Extra(min_l1_pt))
    makeEtaEffPlot(p, efficiency, "eff_sim_eta_pt%d_dxy%dto%d_fid_L1_pt%d"%(min_sim_pt, min_dxy, max_dxy, min_l1_pt), "p_{T}^{SIM} > %.1f, p_{T}^{L1}>%.1f, |d_{xy}|<%.1f"%(min_sim_pt, min_l1_pt, max_dxy))
    
    ## vs dxy
    efficiency = getEffObject(p, "abs(sim_dxy)", "(50,0.1,30)", AND(sim_pt(min_sim_pt), cms_eta(), Gd_fid()), has_L1Extra(min_l1_pt))
    makeEffPlot(p, efficiency, 50, 0.1, 30, "eff_sim_dxy_pt%d_fid_L1_pt%d"%(min_sim_pt, min_l1_pt), "; SIM d_{xy}; reconstruction Efficiency", "p_{T}^{SIM} > %.1f, p_{T}^{L1}>%.1f, |#eta|<2.4"%(min_sim_pt, min_l1_pt))
    
def recoTrackEfficiency_2(p, min_dxy, max_dxy, min_sim_pt, min_l1_pt, min_reco_pt, extra_num_cut=cand_3_st()):
    return getEffObject(p, "abs(sim_eta)", "(25,0,2.5)", AND(n_dt_csc_seg(1), sim_pt(min_sim_pt), sim_dxy(min_dxy, max_dxy), has_L1Extra(min_l1_pt), Gd_fid()), AND(has_cand(min_reco_pt), extra_num_cut))

def recoTrackEfficiency_3(p, min_dxy, max_dxy, min_sim_pt, min_l1_pt, min_reco_pt, pattern_cut=cand_3_st()):
    return getEffObject(p, "abs(sim_eta)", "(25,0,2.5)", AND(TCut("abs(sim_eta)>1.6"), n_dt_csc_seg(1), sim_pt(min_sim_pt), sim_dxy(min_dxy, max_dxy), has_L1Extra(min_l1_pt), Gd_fid(), has_cand2(), pattern_cut), cand_pt(min_reco_pt))

def special_recoTrackEfficiency(p, min_dxy, max_dxy, sim_pt_cut, min_l1_pt, reco_pt_cut):
    tree = p.tree
    denom = 0.
    num = 0.
    loss_pt = 0.
    loss_missing = 0.
    loss_3seg = 0.

    loss_pt_01 = 0.
    loss_pt_02 = 0.
    loss_pt_03 = 0.
    loss_pt_04 = 0.
    loss_pt_05 = 0.
    loss_pt_06 = 0.
    loss_pt_07 = 0.
    loss_pt_08 = 0.
    loss_pt_09 = 0.
    loss_pt_10 = 0.

    num_eta = TH1F( 'num_eta', '', 25, 0, 2.4 )
    denom_eta = TH1F( 'denom_eta', '', 25, 0, 2.4 )
    offset = TH2F( 'offset', '', 25, 0, 2.4, 100, -5, 3)

    for k in range(0, tree.GetEntries()):
        tree.GetEntry(k)
        if k>10000000:
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

            ## efficiency loss cases
            case_bad_muon_missing_cand = False
            case_bad_muon_no_3_stubs = False
            case_bad_muon_cand_pt_low = False

            if tree.has_recoChargedCandidate is 0:
                case_bad_muon_missing_cand = True
            if not cand_3_st_tree_int(tree):
                case_bad_muon_no_3_stubs = True
            if tree.recoChargedCandidate_pt < reco_pt_cut:
                case_bad_muon_cand_pt_low = True

            ## good muons
            case_good_muon = ( (not case_bad_muon_missing_cand) and 
                               (not case_bad_muon_no_3_stubs) and 
                               (not case_bad_muon_cand_pt_low) )

            if case_good_muon:
                num = num + 1.
                num_eta.Fill(tree.sim_eta)

            ## print-outs and counters
            else:
                if case_bad_muon_missing_cand:
                    loss_missing = loss_missing + 1.
                elif case_bad_muon_no_3_stubs:
                    loss_3seg = loss_3seg + 1.
                    """
                    print "Denom!", k
                    print "No Num!"
                    print "sim_pt", tree.sim_pt
                    print "sim_eta", tree.sim_eta
                    if tree.cand_dt_st_1>0:
                        print "dt st1", tree.cand_dt_st_1>0
                    if tree.cand_dt_st_2>0:
                        print "dt st2", tree.cand_dt_st_2>0
                    if tree.cand_dt_st_3>0:
                        print "dt st3", tree.cand_dt_st_3>0
                    if tree.cand_dt_st_4>0:
                        print "dt st4", tree.cand_dt_st_4>0
                    if tree.cand_csc_st_1>0:
                        print "csc st1", tree.cand_csc_st_1>0
                    if tree.cand_csc_st_2>0:
                        print "csc st2", tree.cand_csc_st_2>0
                    if tree.cand_csc_st_3>0:
                        print "csc st3", tree.cand_csc_st_3>0
                    if tree.cand_csc_st_4>0:
                        print "csc st4", tree.cand_csc_st_4>0
                    if tree.cand_rpcf_st_1>0:
                        print "rpcf st1", tree.cand_rpcf_st_1>0
                    if tree.cand_rpcf_st_2>0:
                        print "rpcf st2", tree.cand_rpcf_st_2>0
                    if tree.cand_rpcf_st_3>0:
                        print "rpcf st3", tree.cand_rpcf_st_3>0
                    if tree.cand_rpcf_st_4>0:
                        print "rpcf st4", tree.cand_rpcf_st_4>0
                    if  tree.cand_rpcb_st_1>0:
                        print "rpcb st1", tree.cand_rpcb_st_1>0
                    if tree.cand_rpcb_st_2>0:
                        print "rpcb st2", tree.cand_rpcb_st_2>0
                    if tree.cand_rpcb_st_3>0:                        
                        print "rpcb st3", tree.cand_rpcb_st_3>0
                    if tree.cand_rpcb_st_4>0:
                        print "rpcb st4", tree.cand_rpcb_st_4>0
                    if tree.cand_gem_st_1>0:
                        print "gem st1", tree.cand_gem_st_1>0
                    if tree.cand_gem_st_2>0:
                        print "gem st2", tree.cand_gem_st_2>0
                    """
                elif case_bad_muon_cand_pt_low:
                    loss_pt = loss_pt + 1.
                if not case_bad_muon_no_3_stubs and case_bad_muon_cand_pt_low:
                    pt_offset = (tree.sim_pt-tree.recoChargedCandidate_pt)/tree.sim_pt
                    offset.Fill(abs(tree.sim_eta), pt_offset)
                    
                    if offset  < 0.1:
                        loss_pt_01 = loss_pt_01 + 1
                    if 0.1 < offset and offset < 0.2:
                        loss_pt_02 = loss_pt_02 + 1

                    
                    print "reco_pt", tree.recoChargedCandidate_pt
                    print "reco_eta", tree.recoChargedCandidate_eta
                    print "sim_eta", tree.sim_eta
                    print "sim_pt", tree.sim_pt
                    print "(sim_pt-reco_pt)/sim_pt", (tree.sim_pt-tree.recoChargedCandidate_pt)/tree.sim_pt
                    print

    print "------------------------------"
    print "Denominator:", denom
    print "Numerator:", num
    print "Total efficiency:", num/denom
    print "------------------------------"
    print "Total losses", denom - num
    print "\tmissing cand:", loss_missing, "% loss", loss_missing/denom*100
    print "\tpt too low:", loss_pt, "% loss", loss_pt/denom*100
    print "\ttoo few segments/rechits", loss_3seg, "% loss", loss_3seg/denom*100
    print "------------------------------"

    c = TCanvas("c","c",800,600)
    c.cd()
    offset.Draw("COLZ")
    offset.GetYaxis().SetTitle("(p_{T}^{SIM}-p_{T}^{RECO})/p_{T}^{SIM}")
    offset.GetXaxis().SetTitle("|#eta|")
    l = TLine(0, 1./6, 2.5, 1./6)
    l.SetLineColor(kRed)
    l.Draw("same")
    c.SaveAs("test.png")

    c = TCanvas("c","c",800,600)
    c.cd()
    offset_ProfX = offset.ProfileX()
    offset_ProfX.GetYaxis().SetTitle("(p_{T}^{SIM}-p_{T}^{RECO})/p_{T}^{SIM}")
    offset_ProfX.GetXaxis().SetTitle("|#eta|")
    offset_ProfX.Draw("s")
    l = TLine(0, 1./6, 2.5, 1./6)
    l.SetLineColor(kRed)
    l.Draw("same")
    c.SaveAs("test2.png")

    #makeEtaEffPlot(p, , "dummy", "")
    h = TEfficiency(num_eta, denom_eta)
    h = clearEmptyBinsEff(h)
    SetOwnership(h, False)
    return h



