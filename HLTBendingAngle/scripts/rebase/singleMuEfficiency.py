from ROOT import *

from Helpers import *
from ROOT import SetOwnership

def l1ExtraTrackEfficiency(p):

    etaBinning = "(50,-2.5,2.5)"
    ptBinning = "(50,0,50)"

    ## simhits
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(5)), n_dt_st_sh(1)), "eff_sim_eta_pt5_dt_st_1", ">=1 DT st with simhits")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(5)), n_dt_st_sh(2)), "eff_sim_eta_pt5_dt_st_2", ">=2 DT st with simhits")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(5)), n_dt_st_sh(3)), "eff_sim_eta_pt5_dt_st_3", ">=3 DT st with simhits")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(5)), n_dt_st_sh(4)), "eff_sim_eta_pt5_dt_st_4", ">=4 DT st with simhits")

    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(5)), n_csc_st_sh(1)), "eff_sim_eta_pt5_csc_st_1", ">=1 CSC st with simhits")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(5)), n_csc_st_sh(2)), "eff_sim_eta_pt5_csc_st_2", ">=2 CSC st with simhits")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(5)), n_csc_st_sh(3)), "eff_sim_eta_pt5_csc_st_3", ">=3 CSC st with simhits")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(5)), n_csc_st_sh(4)), "eff_sim_eta_pt5_csc_st_4", ">=4 CSC st with simhits")

    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(5)), n_dt_csc_st_sh(1)), "eff_sim_eta_pt5_dt_csc_st_1", ">=1 DT/CSC st with simhits")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(5)), n_dt_csc_st_sh(2)), "eff_sim_eta_pt5_dt_csc_st_2", ">=2 DT/CSC st with simhits")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(5)), n_dt_csc_st_sh(3)), "eff_sim_eta_pt5_dt_csc_st_3", ">=3 DT/CSC st with simhits")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(5)), n_dt_csc_st_sh(4)), "eff_sim_eta_pt5_dt_csc_st_4", ">=4 DT/CSC st with simhits")

    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(5)), n_rpc_st_sh(1)), "eff_sim_eta_pt5_rpc_st_1", ">=1 RPC st with simhits")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(5)), n_rpc_st_sh(2)), "eff_sim_eta_pt5_rpc_st_2", ">=2 RPC st with simhits")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(5)), n_rpc_st_sh(3)), "eff_sim_eta_pt5_rpc_st_3", ">=3 RPC st with simhits")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(5)), n_rpc_st_sh(4)), "eff_sim_eta_pt5_rpc_st_4", ">=4 RPC st with simhits")

    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(5)), n_gem_st_sh(1)), "eff_sim_eta_pt5_gem_st_1", ">=1 GEM st with simhits")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(5)), n_gem_st_sh(2)), "eff_sim_eta_pt5_gem_st_2", ">=2 GEM st with simhits")
    
    ## segments
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(5), n_dt_st_sh(1)), n_dt_st_seg(1)), "eff_sim_eta_pt5_dt_seg_1", ">=1 DT st with segments")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(5), n_dt_st_sh(2)), n_dt_st_seg(2)), "eff_sim_eta_pt5_dt_seg_2", ">=2 DT st with segments")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(5), n_dt_st_sh(3)), n_dt_st_seg(3)), "eff_sim_eta_pt5_dt_seg_3", ">=3 DT st with segments")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(5), n_dt_st_sh(4)), n_dt_st_seg(4)), "eff_sim_eta_pt5_dt_seg_4", ">=4 DT st with segments")

    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(5), n_csc_st_sh(1)), n_csc_st_seg(1)), "eff_sim_eta_pt5_csc_seg_1", ">=1 CSC st with segments")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(5), n_csc_st_sh(2)), n_csc_st_seg(2)), "eff_sim_eta_pt5_csc_seg_2", ">=2 CSC st with segments")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(5), n_csc_st_sh(3)), n_csc_st_seg(3)), "eff_sim_eta_pt5_csc_seg_3", ">=3 CSC st with segments")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(5), n_csc_st_sh(4)), n_csc_st_seg(4)), "eff_sim_eta_pt5_csc_seg_4", ">=4 CSC st with segments")

    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(5), n_dt_csc_st_sh(1)), n_dt_csc_st_seg(1)), "eff_sim_eta_pt5_dt_csc_seg_1", ">=1 DT/CSC st with segments")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(5), n_dt_csc_st_sh(2)), n_dt_csc_st_seg(2)), "eff_sim_eta_pt5_dt_csc_seg_2", ">=2 DT/CSC st with segments")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(5), n_dt_csc_st_sh(3)), n_dt_csc_st_seg(3)), "eff_sim_eta_pt5_dt_csc_seg_3", ">=3 DT/CSC st with segments")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(5), n_dt_csc_st_sh(4)), n_dt_csc_st_seg(4)), "eff_sim_eta_pt5_dt_csc_seg_4", ">=4 DT/CSC st with segments")

    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(5), n_rpc_st_sh(1)), n_rpc_st_rh(1)), "eff_sim_eta_pt5_rpc_seg_1", ">=1 RPC st with rechits")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(5), n_rpc_st_sh(2)), n_rpc_st_rh(2)), "eff_sim_eta_pt5_rpc_seg_2", ">=2 RPC st with rechits")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(5), n_rpc_st_sh(3)), n_rpc_st_rh(3)), "eff_sim_eta_pt5_rpc_seg_3", ">=3 RPC st with rechits")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(5), n_rpc_st_sh(4)), n_rpc_st_rh(4)), "eff_sim_eta_pt5_rpc_seg_4", ">=4 RPC st with rechits")

    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(5), n_gem_st_sh(1)), n_gem_st_rh(1)), "eff_sim_eta_pt5_gem_seg_1", ">=1 GEM st with rechits")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(5), n_gem_st_sh(2)), n_gem_st_rh(2)), "eff_sim_eta_pt5_gem_seg_2", ">=2 GEM st with rechits")

    ## L1
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(5)), has_L1Extra()), "eff_sim_eta_pt5_L1Extra_pt0", "L1Extra")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(6)), has_L1Extra(5)), "eff_sim_eta_pt6_L1Extra_pt5", "L1Extra, p_{T}>5 GeV")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(11)), has_L1Extra(10)), "eff_sim_eta_pt11_L1Extra_pt10", "L1Extra, p_{T}>10 GeV")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(16.5)), has_L1Extra(15)), "eff_sim_eta_pt16_L1Extra_pt15", "L1Extra, p_{T}>15 GeV")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(22)), has_L1Extra(20)), "eff_sim_eta_pt22_L1Extra_pt20", "L1Extra, p_{T}>20 GeV")

    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(20)), has_L1Extra(17)), "eff_sim_eta_pt20_L1Extra_pt17", "L1Extra")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(20), sim_dxy(0, 5)), has_L1Extra(17)), "eff_sim_eta_pt20_dxy0to5_L1Extra_pt17", "L1Extra")


    makePtEffPlot(p, getEffObject(p, "sim_pt", ptBinning, AND(sim_eta(0., 2.4)), has_L1Extra(10)), "eff_sim_pt_eta00-24_L1Extra_pt10", "p_{T}^{L1}>10 GeV")
    makePtEffPlot(p, getEffObject(p, "sim_pt", ptBinning, AND(sim_eta(0., 2.4)), has_L1Extra(15)), "eff_sim_pt_eta00-24_L1Extra_pt15", "p_{T}^{L1}>15 GeV")
    makePtEffPlot(p, getEffObject(p, "sim_pt", ptBinning, AND(sim_eta(0., 2.4)), has_L1Extra(20)), "eff_sim_pt_eta00-24_L1Extra_pt20", "p_{T}^{L1}>20 GeV")

    makePtEffPlot(p, getEffObject(p, "sim_pt", ptBinning, AND(sim_eta(0., 0.9)), has_L1Extra(10)), "eff_sim_pt_eta00-09_L1Extra_pt10", "p_{T}^{L1}>10 GeV; |#eta|<0.9")
    makePtEffPlot(p, getEffObject(p, "sim_pt", ptBinning, AND(sim_eta(0., 0.9)), has_L1Extra(15)), "eff_sim_pt_eta00-09_L1Extra_pt15", "p_{T}^{L1}>15 GeV; |#eta|<0.9")
    makePtEffPlot(p, getEffObject(p, "sim_pt", ptBinning, AND(sim_eta(0., 0.9)), has_L1Extra(20)), "eff_sim_pt_eta00-09_L1Extra_pt20", "p_{T}^{L1}>20 GeV; |#eta|<0.9")

    makePtEffPlot(p, getEffObject(p, "sim_pt", ptBinning, AND(sim_eta(0.9, 1.2)), has_L1Extra(10)), "eff_sim_pt_eta09-12_L1Extra_pt10", "p_{T}^{L1}>10 GeV; 0.9<|#eta|<1.2")
    makePtEffPlot(p, getEffObject(p, "sim_pt", ptBinning, AND(sim_eta(0.9, 1.2)), has_L1Extra(15)), "eff_sim_pt_eta09-12_L1Extra_pt15", "p_{T}^{L1}>15 GeV; 0.9<|#eta|<1.2")
    makePtEffPlot(p, getEffObject(p, "sim_pt", ptBinning, AND(sim_eta(0.9, 1.2)), has_L1Extra(20)), "eff_sim_pt_eta09-12_L1Extra_pt20", "p_{T}^{L1}>20 GeV; 0.9<|#eta|<1.2")

    makePtEffPlot(p, getEffObject(p, "sim_pt", ptBinning, AND(sim_eta(1.2, 1.5)), has_L1Extra(10)), "eff_sim_pt_eta12-15_L1Extra_pt10", "p_{T}^{L1}>10 GeV; 1.2<|#eta|<1.5")
    makePtEffPlot(p, getEffObject(p, "sim_pt", ptBinning, AND(sim_eta(1.2, 1.5)), has_L1Extra(15)), "eff_sim_pt_eta12-15_L1Extra_pt15", "p_{T}^{L1}>15 GeV; 1.2<|#eta|<1.5")
    makePtEffPlot(p, getEffObject(p, "sim_pt", ptBinning, AND(sim_eta(1.2, 1.5)), has_L1Extra(20)), "eff_sim_pt_eta12-15_L1Extra_pt20", "p_{T}^{L1}>20 GeV; 1.2<|#eta|<1.5")

    makePtEffPlot(p, getEffObject(p, "sim_pt", ptBinning, AND(sim_eta(1.5, 1.8)), has_L1Extra(10)), "eff_sim_pt_eta15-18_L1Extra_pt10", "p_{T}^{L1}>10 GeV; 1.5<|#eta|<1.8")
    makePtEffPlot(p, getEffObject(p, "sim_pt", ptBinning, AND(sim_eta(1.5, 1.8)), has_L1Extra(15)), "eff_sim_pt_eta15-18_L1Extra_pt15", "p_{T}^{L1}>15 GeV; 1.5<|#eta|<1.8")
    makePtEffPlot(p, getEffObject(p, "sim_pt", ptBinning, AND(sim_eta(1.5, 1.8)), has_L1Extra(20)), "eff_sim_pt_eta15-18_L1Extra_pt20", "p_{T}^{L1}>20 GeV; 1.5<|#eta|<1.8")

    makePtEffPlot(p, getEffObject(p, "sim_pt", ptBinning, AND(sim_eta(1.8, 2.1)), has_L1Extra(10)), "eff_sim_pt_eta18-21_L1Extra_pt10", "p_{T}^{L1}>10 GeV; 1.8<|#eta|<2.1")
    makePtEffPlot(p, getEffObject(p, "sim_pt", ptBinning, AND(sim_eta(1.8, 2.1)), has_L1Extra(15)), "eff_sim_pt_eta18-21_L1Extra_pt15", "p_{T}^{L1}>15 GeV; 1.8<|#eta|<2.1")
    makePtEffPlot(p, getEffObject(p, "sim_pt", ptBinning, AND(sim_eta(1.8, 2.1)), has_L1Extra(20)), "eff_sim_pt_eta18-21_L1Extra_pt20", "p_{T}^{L1}>20 GeV; 1.8<|#eta|<2.1")

    makePtEffPlot(p, getEffObject(p, "sim_pt", ptBinning, AND(sim_eta(2.1, 2.4)), has_L1Extra(10)), "eff_sim_pt_eta21-24_L1Extra_pt10", "p_{T}^{L1}>10 GeV; 2.1<|#eta|<2.4")
    makePtEffPlot(p, getEffObject(p, "sim_pt", ptBinning, AND(sim_eta(2.1, 2.4)), has_L1Extra(15)), "eff_sim_pt_eta21-24_L1Extra_pt15", "p_{T}^{L1}>15 GeV; 2.1<|#eta|<2.4")
    makePtEffPlot(p, getEffObject(p, "sim_pt", ptBinning, AND(sim_eta(2.1, 2.4)), has_L1Extra(20)), "eff_sim_pt_eta21-24_L1Extra_pt20", "p_{T}^{L1}>20 GeV; 2.1<|#eta|<2.4")

    makePtEffPlot(p, getEffObject(p, "sim_pt", ptBinning, AND(sim_eta(1.2, 2.4)), has_L1Extra(10)), "eff_sim_pt_eta12-24_L1Extra_pt10", "p_{T}^{L1}>10 GeV; 1.2<|#eta|<2.4")
    makePtEffPlot(p, getEffObject(p, "sim_pt", ptBinning, AND(sim_eta(1.2, 2.4)), has_L1Extra(15)), "eff_sim_pt_eta12-24_L1Extra_pt15", "p_{T}^{L1}>15 GeV; 1.2<|#eta|<2.4")
    makePtEffPlot(p, getEffObject(p, "sim_pt", ptBinning, AND(sim_eta(1.2, 2.4)), has_L1Extra(20)), "eff_sim_pt_eta12-24_L1Extra_pt20", "p_{T}^{L1}>20 GeV; 1.2<|#eta|<2.4")

    #makeEtaEffPlot(p, getEffObject(p, "sim_pt", ptBinning, AND(sim_pt(20), sim_dxy(0, 5)), has_L1Extra(17)), "eff_sim_eta_pt20_dxy0to5_L1Extra_pt17", "L1Extra")

    ## reco 
    makePtEffPlot(p, getEffObject(p, "sim_pt", ptBinning, AND(sim_eta(0., 2.4)), has_cand(0)), "eff_sim_pt_cand", "p_{T}^{L2}>10 GeV")

    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(5)), has_cand()), "eff_sim_eta_pt5_cand_pt0", "L2Mu")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(6)), has_cand(5)), "eff_sim_eta_pt6_cand_pt5", "L2Mu, p_{T}^{L2}>5 GeV")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(11)), has_cand(10)), "eff_sim_eta_pt11_cand_pt10", "L2Mu, p_{T}^{L2}>10 GeV")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(16.5)), has_cand(15)), "eff_sim_eta_pt16_cand_pt15", "L2Mu, p_{T}^{L2}>15 GeV")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(22)), has_cand(20)), "eff_sim_eta_pt22_cand_pt20", "L2Mu, p_{T}^{L2}>20 GeV")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(33)), has_cand(30)), "eff_sim_eta_pt33_cand_pt30", "L2Mu, p_{T}^{L2}>30 GeV")

    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(5), has_L1Extra()), has_cand()), "eff_sim_eta_l1Extra_pt5_cand_pt0", "L2Mu")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(6), has_L1Extra(6)), has_cand(5)), "eff_sim_eta_l1Extra_pt6_cand_pt5", "L2Mu, p_{T}^{L2}>5 GeV")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(11), has_L1Extra(11)), has_cand(10)), "eff_sim_eta_l1Extra_pt11_cand_pt10", "L2Mu, p_{T}^{L2}>10 GeV")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(16.5), has_L1Extra(16.5)), has_cand(15)), "eff_sim_eta_l1Extra_pt16_cand_pt15", "L2Mu, p_{T}^{L2}>15 GeV")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(22), has_L1Extra(22)), has_cand(20)), "eff_sim_eta_l1Extra_pt22_cand_pt20", "L2Mu, p_{T}^{L2}>20 GeV")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(33), has_L1Extra(33)), has_cand(30)), "eff_sim_eta_l1Extra_pt33_cand_pt30", "L2Mu, p_{T}^{L2}>30 GeV")
