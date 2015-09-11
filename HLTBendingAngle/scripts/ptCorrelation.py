from ROOT import *
from Helpers import *

def pTCorrelationPlots(p):
    
    def base_cut(min_sim_pt=5, max_sim_pt = 999, min_dxy=0, max_dxy=10, min_l1_pt=0):
        return AND(n_dt_csc_seg(1), sim_pt(min_sim_pt, max_sim_pt), sim_dxy(min_dxy, max_dxy), has_L1Extra(min_l1_pt), Gd_fid())

    draw_2D(p, "simPtVsRecoPt_3st", 'pT correlation; p_{T}^{SIM} [GeV]; p_{T}^{RECO} [GeV]', "(100, 0, 100, 100, 0, 100)", "recoChargedCandidate_pt:sim_pt", AND(base_cut(), has_cand(), cand_3_st()), "COLZ")

    title =  ";|#eta|; (p_{T}^{SIM}-p_{T}^{RECO})/p_{T}^{SIM}"
    binning = "(60, 0, 3.0, 150, -1.5, 1.5)"
    toplot = "(sim_pt-recoChargedCandidate_pt)/sim_pt:abs(sim_eta)"

    draw_2D(p, "absEtaVsRelPt_3st", title, binning, toplot, AND(base_cut(), has_cand(), cand_3_st()), "COLZ")
    draw_2D(p, "absEtaVsRelPt_3st_pt5to10", '5 < p_{T} < 10 GeV' + title, binning, toplot, AND(base_cut(5,10), has_cand(), cand_3_st()), "COLZ")
    draw_2D(p, "absEtaVsRelPt_3st_pt10to15", '10 < p_{T} < 15 GeV' + title, binning, toplot, AND(base_cut(10,15), has_cand(), cand_3_st()), "COLZ")
    draw_2D(p, "absEtaVsRelPt_3st_pt15to20", '15 < p_{T} < 20 GeV' + title, binning, toplot, AND(base_cut(15,20), has_cand(), cand_3_st()), "COLZ")
    draw_2D(p, "absEtaVsRelPt_3st_pt20to40", '20 < p_{T} < 40 GeV' + title, binning, toplot, AND(base_cut(20,40), has_cand(), cand_3_st()), "COLZ")

    draw_2D(p, "absEtaVsRelPt_3seg", title, binning, toplot, AND(base_cut(), has_cand(), cand_3_st_3_segments()), "COLZ")
    draw_2D(p, "absEtaVsRelPt_3seg_pt5to10", '5 < p_{T} < 10 GeV' + title, binning, toplot, AND(base_cut(5,10), has_cand(), cand_3_st_3_segments()), "COLZ")
    draw_2D(p, "absEtaVsRelPt_3seg_pt10to15", '10 < p_{T} < 15 GeV' + title, binning, toplot, AND(base_cut(10,15), has_cand(), cand_3_st_3_segments()), "COLZ")
    draw_2D(p, "absEtaVsRelPt_3seg_pt15to20", '15 < p_{T} < 20 GeV' + title, binning, toplot, AND(base_cut(15,20), has_cand(), cand_3_st_3_segments()), "COLZ")
    draw_2D(p, "absEtaVsRelPt_3seg_pt20to40", '20 < p_{T} < 40 GeV' + title, binning, toplot, AND(base_cut(20,40), has_cand(), cand_3_st_3_segments()), "COLZ")

    draw_2D(p, "absEtaVsRelPt_2seg1rh", title, binning, toplot, AND(base_cut(), has_cand(), cand_3_st_2_segments_1_rechit()), "COLZ")
    draw_2D(p, "absEtaVsRelPt_2seg1rh_pt5to10", '5 < p_{T} < 10 GeV' + title, binning, toplot, AND(base_cut(5,10), has_cand(), cand_3_st_2_segments_1_rechit()), "COLZ")
    draw_2D(p, "absEtaVsRelPt_2seg1rh_pt10to15", '10 < p_{T} < 15 GeV' + title, binning, toplot, AND(base_cut(10,15), has_cand(), cand_3_st_2_segments_1_rechit()), "COLZ")
    draw_2D(p, "absEtaVsRelPt_2seg1rh_pt15to20", '15 < p_{T} < 20 GeV' + title, binning, toplot, AND(base_cut(15,20), has_cand(), cand_3_st_2_segments_1_rechit()), "COLZ")
    draw_2D(p, "absEtaVsRelPt_2seg1rh_pt20to40", '20 < p_{T} < 40 GeV' + title, binning, toplot, AND(base_cut(20,40), has_cand(), cand_3_st_2_segments_1_rechit()), "COLZ")

    draw_2D(p, "absEtaVsRelPt_2seg1rh_gem", title, binning, toplot, AND(base_cut(), has_cand(), cand_3_st_2_segments_1_rechit_gem_endcap()), "COLZ")
    draw_2D(p, "absEtaVsRelPt_2seg1rh_gem_pt5to10", '5 < p_{T} < 10 GeV' + title, binning, toplot, AND(base_cut(5,10), has_cand(), cand_3_st_2_segments_1_rechit_gem_endcap()), "COLZ")
    draw_2D(p, "absEtaVsRelPt_2seg1rh_gem_pt10to15", '10 < p_{T} < 15 GeV' + title, binning, toplot, AND(base_cut(10,15), has_cand(), cand_3_st_2_segments_1_rechit_gem_endcap()), "COLZ")
    draw_2D(p, "absEtaVsRelPt_2seg1rh_gem_pt15to20", '15 < p_{T} < 20 GeV' + title, binning, toplot, AND(base_cut(15,20), has_cand(), cand_3_st_2_segments_1_rechit_gem_endcap()), "COLZ")
    draw_2D(p, "absEtaVsRelPt_2seg1rh_gem_pt20to40", '20 < p_{T} < 40 GeV' + title, binning, toplot, AND(base_cut(20,40), has_cand(), cand_3_st_2_segments_1_rechit_gem_endcap()), "COLZ")

    draw_2D(p, "absEtaVsRelPt_2seg1rh_GE21", title, binning, toplot, AND(base_cut(), has_cand(), cand_3_st_2_segments_1_rechit_GE21_endcap()), "COLZ")
    draw_2D(p, "absEtaVsRelPt_2seg1rh_GE21_pt5to10", '5 < p_{T} < 10 GeV' + title, binning, toplot, AND(base_cut(5,10), has_cand(), cand_3_st_2_segments_1_rechit_GE21_endcap()), "COLZ")
    draw_2D(p, "absEtaVsRelPt_2seg1rh_GE21_pt10to15", '10 < p_{T} < 15 GeV' + title, binning, toplot, AND(base_cut(10,15), has_cand(), cand_3_st_2_segments_1_rechit_GE21_endcap()), "COLZ")
    draw_2D(p, "absEtaVsRelPt_2seg1rh_GE21_pt15to20", '15 < p_{T} < 20 GeV' + title, binning, toplot, AND(base_cut(15,20), has_cand(), cand_3_st_2_segments_1_rechit_GE21_endcap()), "COLZ")
    draw_2D(p, "absEtaVsRelPt_2seg1rh_GE21_pt20to40", '20 < p_{T} < 40 GeV' + title, binning, toplot, AND(base_cut(20,40), has_cand(), cand_3_st_2_segments_1_rechit_GE21_endcap()), "COLZ")

    draw_2D(p, "absEtaVsRelPt_2seg1rh_GE21_noCSCst2", title, binning, toplot, AND(base_cut(), has_cand(), cand_3_st_2_segments_1_rechit_GE21_nocscst2_endcap()), "COLZ")
    draw_2D(p, "absEtaVsRelPt_2seg1rh_GE21_noCSCst2_pt5to10", '5 < p_{T} < 10 GeV' + title, binning, toplot, AND(base_cut(5,10), has_cand(), cand_3_st_2_segments_1_rechit_GE21_nocscst2_endcap()), "COLZ")
    draw_2D(p, "absEtaVsRelPt_2seg1rh_GE21_noCSCst2_pt10to15", '10 < p_{T} < 15 GeV' + title, binning, toplot, AND(base_cut(10,15), has_cand(), cand_3_st_2_segments_1_rechit_GE21_nocscst2_endcap()), "COLZ")
    draw_2D(p, "absEtaVsRelPt_2seg1rh_GE21_noCSCst2_pt15to20", '15 < p_{T} < 20 GeV' + title, binning, toplot, AND(base_cut(15,20), has_cand(), cand_3_st_2_segments_1_rechit_GE21_nocscst2_endcap()), "COLZ")
    draw_2D(p, "absEtaVsRelPt_2seg1rh_GE21_noCSCst2_pt20to40", '20 < p_{T} < 40 GeV' + title, binning, toplot, AND(base_cut(20,40), has_cand(), cand_3_st_2_segments_1_rechit_GE21_nocscst2_endcap()), "COLZ")

    title =  ";|#eta|; RMS (p_{T}^{SIM}-p_{T}^{RECO})/p_{T}^{SIM}"

    draw_2DProfX(p, "absEtaVsRelPt_3st_ProfX", title, binning, toplot, AND(base_cut(), has_cand(), cand_3_st()))
    draw_2DProfX(p, "absEtaVsRelPt_3st_pt5to10_ProfX", '5 < p_{T} < 10 GeV' + title, binning, toplot, AND(base_cut(5,10), has_cand(), cand_3_st()))
    draw_2DProfX(p, "absEtaVsRelPt_3st_pt10to15_ProfX", '10 < p_{T} < 15 GeV' + title, binning, toplot, AND(base_cut(10,15), has_cand(), cand_3_st()))
    draw_2DProfX(p, "absEtaVsRelPt_3st_pt15to20_ProfX", '15 < p_{T} < 20 GeV' + title, binning, toplot, AND(base_cut(15,20), has_cand(), cand_3_st()))
    draw_2DProfX(p, "absEtaVsRelPt_3st_pt20to40_ProfX", '20 < p_{T} < 40 GeV' + title, binning, toplot, AND(base_cut(20,40), has_cand(), cand_3_st()))

    draw_2DProfX(p, "absEtaVsRelPt_3seg_pt5to10_ProfX", '5 < p_{T} < 10 GeV' + title, binning, toplot, AND(base_cut(5,10), has_cand(), cand_3_st_3_segments()))
    draw_2DProfX(p, "absEtaVsRelPt_3seg_pt10to15_ProfX", '10 < p_{T} < 15 GeV' + title, binning, toplot, AND(base_cut(10,15), has_cand(), cand_3_st_3_segments()))
    draw_2DProfX(p, "absEtaVsRelPt_3seg_pt15to20_ProfX", '15 < p_{T} < 20 GeV' + title, binning, toplot, AND(base_cut(15,20), has_cand(), cand_3_st_3_segments()))
    draw_2DProfX(p, "absEtaVsRelPt_3seg_pt20to40_ProfX", '20 < p_{T} < 40 GeV' + title, binning, toplot, AND(base_cut(20,40), has_cand(), cand_3_st_3_segments()))

    draw_2DProfX(p, "absEtaVsRelPt_2seg1rh_pt5to10_ProfX", '5 < p_{T} < 10 GeV' + title, binning, toplot, AND(base_cut(5,10), has_cand(), cand_3_st_2_segments_1_rechit()))
    draw_2DProfX(p, "absEtaVsRelPt_2seg1rh_pt10to15_ProfX", '10 < p_{T} < 15 GeV' + title, binning, toplot, AND(base_cut(10,15), has_cand(), cand_3_st_2_segments_1_rechit()))
    draw_2DProfX(p, "absEtaVsRelPt_2seg1rh_pt15to20_ProfX", '15 < p_{T} < 20 GeV' + title, binning, toplot, AND(base_cut(15,20), has_cand(), cand_3_st_2_segments_1_rechit()))
    draw_2DProfX(p, "absEtaVsRelPt_2seg1rh_pt20to40_ProfX", '20 < p_{T} < 40 GeV' + title, binning, toplot, AND(base_cut(20,40), has_cand(), cand_3_st_2_segments_1_rechit()))

    draw_2DProfX(p, "absEtaVsRelPt_2seg1rh_gem_pt5to10_ProfX", '5 < p_{T} < 10 GeV' + title, binning, toplot, AND(base_cut(5,10), has_cand(), cand_3_st_2_segments_1_rechit_gem_endcap()))
    draw_2DProfX(p, "absEtaVsRelPt_2seg1rh_gem_pt10to15_ProfX", '10 < p_{T} < 15 GeV' + title, binning, toplot, AND(base_cut(10,15), has_cand(), cand_3_st_2_segments_1_rechit_gem_endcap()))
    draw_2DProfX(p, "absEtaVsRelPt_2seg1rh_gem_pt15to20_ProfX", '15 < p_{T} < 20 GeV' + title, binning, toplot, AND(base_cut(15,20), has_cand(), cand_3_st_2_segments_1_rechit_gem_endcap()))
    draw_2DProfX(p, "absEtaVsRelPt_2seg1rh_gem_pt20to40_ProfX", '20 < p_{T} < 40 GeV' + title, binning, toplot, AND(base_cut(20,40), has_cand(), cand_3_st_2_segments_1_rechit_gem_endcap()))

    draw_2DProfX(p, "absEtaVsRelPt_2seg1rh_GE21_pt5to10_ProfX", '5 < p_{T} < 10 GeV' + title, binning, toplot, AND(base_cut(5,10), has_cand(), cand_3_st_2_segments_1_rechit_GE21_endcap()))
    draw_2DProfX(p, "absEtaVsRelPt_2seg1rh_GE21_pt10to15_ProfX", '10 < p_{T} < 15 GeV' + title, binning, toplot, AND(base_cut(10,15), has_cand(), cand_3_st_2_segments_1_rechit_GE21_endcap()))
    draw_2DProfX(p, "absEtaVsRelPt_2seg1rh_GE21_pt15to20_ProfX", '15 < p_{T} < 20 GeV' + title, binning, toplot, AND(base_cut(15,20), has_cand(), cand_3_st_2_segments_1_rechit_GE21_endcap()))
    draw_2DProfX(p, "absEtaVsRelPt_2seg1rh_GE21_pt20to40_ProfX", '20 < p_{T} < 40 GeV' + title, binning, toplot, AND(base_cut(20,40), has_cand(), cand_3_st_2_segments_1_rechit_GE21_endcap()))

    draw_2DProfX(p, "absEtaVsRelPt_2seg1rh_GE21_noCSCst2_pt5to10_ProfX", '5 < p_{T} < 10 GeV' + title, binning, toplot, AND(base_cut(5,10), has_cand(), cand_3_st_2_segments_1_rechit_GE21_nocscst2_endcap()))
    draw_2DProfX(p, "absEtaVsRelPt_2seg1rh_GE21_noCSCst2_pt10to15_ProfX", '10 < p_{T} < 15 GeV' + title, binning, toplot, AND(base_cut(10,15), has_cand(), cand_3_st_2_segments_1_rechit_GE21_nocscst2_endcap()))
    draw_2DProfX(p, "absEtaVsRelPt_2seg1rh_GE21_noCSCst2_pt15to20_ProfX", '15 < p_{T} < 20 GeV' + title, binning, toplot, AND(base_cut(15,20), has_cand(), cand_3_st_2_segments_1_rechit_GE21_nocscst2_endcap()))
    draw_2DProfX(p, "absEtaVsRelPt_2seg1rh_GE21_noCSCst2_pt20to40_ProfX", '20 < p_{T} < 40 GeV' + title, binning, toplot, AND(base_cut(20,40), has_cand(), cand_3_st_2_segments_1_rechit_GE21_nocscst2_endcap()))


    def base_cut_eta(min_sim_eta=0, max_sim_eta = 2.4, min_dxy=0, max_dxy=10, min_l1_pt=0):
        return AND(n_dt_csc_seg(1), sim_eta(min_sim_eta, max_sim_eta), sim_dxy(min_dxy, max_dxy), has_L1Extra(min_l1_pt), Gd_fid())

    title =  ";p_{T}^{SIM}; (p_{T}^{SIM}-p_{T}^{RECO})/p_{T}^{SIM}"
    binning = "(100, 0, 100, 150, -1.5, 1.5)"
    toplot = "(sim_pt-recoChargedCandidate_pt)/sim_pt:sim_pt"

    draw_2D(p, "simPtVsRelPt_3st_eta00to24", '0.0 < #eta < 2.4' + title, binning, toplot, AND(base_cut_eta(), has_cand(), cand_3_st()), "COLZ")
    draw_2D(p, "simPtVsRelPt_3st_eta15to18", '1.5 < #eta < 1.8' + title, binning, toplot, AND(base_cut_eta(1.5,1.8), has_cand(), cand_3_st()), "COLZ")
    draw_2D(p, "simPtVsRelPt_3st_eta18to21", '1.8 < #eta < 2.1' + title, binning, toplot, AND(base_cut_eta(1.8,2.1), has_cand(), cand_3_st()), "COLZ")
    draw_2D(p, "simPtVsRelPt_3st_eta21to24", '2.1 < #eta < 2.4' + title, binning, toplot, AND(base_cut_eta(2.1,2.4), has_cand(), cand_3_st()), "COLZ")
    draw_2D(p, "simPtVsRelPt_3st_eta18to24", '1.8 < #eta < 2.4' + title, binning, toplot, AND(base_cut_eta(1.8,2.4), has_cand(), cand_3_st()), "COLZ")

    draw_2D(p, "simPtVsRelPt_3seg_eta00to24", '0.0 < #eta < 2.4' + title, binning, toplot, AND(base_cut_eta(), has_cand(), cand_3_st_3_segments()), "COLZ")
    draw_2D(p, "simPtVsRelPt_3seg_eta15to18", '1.5 < #eta < 1.8' + title, binning, toplot, AND(base_cut_eta(1.5,1.8), has_cand(), cand_3_st_3_segments()), "COLZ")
    draw_2D(p, "simPtVsRelPt_3seg_eta18to21", '1.8 < #eta < 2.1' + title, binning, toplot, AND(base_cut_eta(1.8,2.1), has_cand(), cand_3_st_3_segments()), "COLZ")
    draw_2D(p, "simPtVsRelPt_3seg_eta21to24", '2.1 < #eta < 2.4' + title, binning, toplot, AND(base_cut_eta(2.1,2.4), has_cand(), cand_3_st_3_segments()), "COLZ")
    draw_2D(p, "simPtVsRelPt_3seg_eta18to24", '1.8 < #eta < 2.4' + title, binning, toplot, AND(base_cut_eta(1.8,2.4), has_cand(), cand_3_st_3_segments()), "COLZ")

    draw_2D(p, "simPtVsRelPt_2seg1rh_eta00to24", '0.0 < #eta < 2.4' + title, binning, toplot, AND(base_cut_eta(), has_cand(), cand_3_st_2_segments_1_rechit()), "COLZ")
    draw_2D(p, "simPtVsRelPt_2seg1rh_eta15to18", '1.5 < #eta < 1.8' + title, binning, toplot, AND(base_cut_eta(1.5,1.8), has_cand(), cand_3_st_2_segments_1_rechit()), "COLZ")
    draw_2D(p, "simPtVsRelPt_2seg1rh_eta18to21", '1.8 < #eta < 2.1' + title, binning, toplot, AND(base_cut_eta(1.8,2.1), has_cand(), cand_3_st_2_segments_1_rechit()), "COLZ")
    draw_2D(p, "simPtVsRelPt_2seg1rh_eta21to24", '2.1 < #eta < 2.4' + title, binning, toplot, AND(base_cut_eta(2.1,2.4), has_cand(), cand_3_st_2_segments_1_rechit()), "COLZ")
    draw_2D(p, "simPtVsRelPt_2seg1rh_eta18to24", '1.8 < #eta < 2.4' + title, binning, toplot, AND(base_cut_eta(1.8,2.4), has_cand(), cand_3_st_2_segments_1_rechit()), "COLZ")

    draw_2D(p, "simPtVsRelPt_2seg1rh_gem_eta00to24", '0.0 < #eta < 2.4' + title, binning, toplot, AND(base_cut_eta(), has_cand(), cand_3_st_2_segments_1_rechit_gem_endcap()), "COLZ")
    draw_2D(p, "simPtVsRelPt_2seg1rh_gem_eta15to18", '1.5 < #eta < 1.8' + title, binning, toplot, AND(base_cut_eta(1.5,1.8), has_cand(), cand_3_st_2_segments_1_rechit_gem_endcap()), "COLZ")
    draw_2D(p, "simPtVsRelPt_2seg1rh_gem_eta18to21", '1.8 < #eta < 2.1' + title, binning, toplot, AND(base_cut_eta(1.8,2.1), has_cand(), cand_3_st_2_segments_1_rechit_gem_endcap()), "COLZ")
    draw_2D(p, "simPtVsRelPt_2seg1rh_gem_eta21to24", '2.1 < #eta < 2.4' + title, binning, toplot, AND(base_cut_eta(2.1,2.4), has_cand(), cand_3_st_2_segments_1_rechit_gem_endcap()), "COLZ")
    draw_2D(p, "simPtVsRelPt_2seg1rh_gem_eta18to24", '1.8 < #eta < 2.4' + title, binning, toplot, AND(base_cut_eta(1.8,2.4), has_cand(), cand_3_st_2_segments_1_rechit_gem_endcap()), "COLZ")

    draw_2D(p, "simPtVsRelPt_2seg1rh_GE21_eta00to24", '0.0 < #eta < 2.4' + title, binning, toplot, AND(base_cut_eta(), has_cand(), cand_3_st_2_segments_1_rechit_GE21_endcap()), "COLZ")
    draw_2D(p, "simPtVsRelPt_2seg1rh_GE21_eta15to18", '1.5 < #eta < 1.8' + title, binning, toplot, AND(base_cut_eta(1.5,1.8), has_cand(), cand_3_st_2_segments_1_rechit_GE21_endcap()), "COLZ")
    draw_2D(p, "simPtVsRelPt_2seg1rh_GE21_eta18to21", '1.8 < #eta < 2.1' + title, binning, toplot, AND(base_cut_eta(1.8,2.1), has_cand(), cand_3_st_2_segments_1_rechit_GE21_endcap()), "COLZ")
    draw_2D(p, "simPtVsRelPt_2seg1rh_GE21_eta21to24", '2.1 < #eta < 2.4' + title, binning, toplot, AND(base_cut_eta(2.1,2.4), has_cand(), cand_3_st_2_segments_1_rechit_GE21_endcap()), "COLZ")
    draw_2D(p, "simPtVsRelPt_2seg1rh_GE21_eta18to24", '1.8 < #eta < 2.4' + title, binning, toplot, AND(base_cut_eta(1.8,2.4), has_cand(), cand_3_st_2_segments_1_rechit_GE21_endcap()), "COLZ")

    draw_2D(p, "simPtVsRelPt_2seg1rh_GE21_noCSCst2_eta00to24", '0.0 < #eta < 2.4' + title, binning, toplot, AND(base_cut_eta(), has_cand(), cand_3_st_2_segments_1_rechit_GE21_nocscst2_endcap()), "COLZ")
    draw_2D(p, "simPtVsRelPt_2seg1rh_GE21_noCSCst2_eta15to18", '1.5 < #eta < 1.8' + title, binning, toplot, AND(base_cut_eta(1.5,1.8), has_cand(), cand_3_st_2_segments_1_rechit_GE21_nocscst2_endcap()), "COLZ")
    draw_2D(p, "simPtVsRelPt_2seg1rh_GE21_noCSCst2_eta18to21", '1.8 < #eta < 2.1' + title, binning, toplot, AND(base_cut_eta(1.8,2.1), has_cand(), cand_3_st_2_segments_1_rechit_GE21_nocscst2_endcap()), "COLZ")
    draw_2D(p, "simPtVsRelPt_2seg1rh_GE21_noCSCst2_eta21to24", '2.1 < #eta < 2.4' + title, binning, toplot, AND(base_cut_eta(2.1,2.4), has_cand(), cand_3_st_2_segments_1_rechit_GE21_nocscst2_endcap()), "COLZ")
    draw_2D(p, "simPtVsRelPt_2seg1rh_GE21_noCSCst2_eta18to24", '1.8 < #eta < 2.4' + title, binning, toplot, AND(base_cut_eta(1.8,2.4), has_cand(), cand_3_st_2_segments_1_rechit_GE21_nocscst2_endcap()), "COLZ")


    title =  ";p_{T}^{SIM}; RMS (p_{T}^{SIM}-p_{T}^{RECO})/p_{T}^{SIM}"

    draw_2DProfX(p, "simPtVsRelPt_3st_eta00to24_ProfX", '0.0 < #eta < 2.4' + title, binning, toplot, AND(base_cut_eta(), has_cand(), cand_3_st()))
    draw_2DProfX(p, "simPtVsRelPt_3st_eta15to18_ProfX", '1.5 < #eta < 1.8' + title, binning, toplot, AND(base_cut_eta(1.5,1.8), has_cand(), cand_3_st()))
    draw_2DProfX(p, "simPtVsRelPt_3st_eta18to21_ProfX", '1.8 < #eta < 2.1' + title, binning, toplot, AND(base_cut_eta(1.8,2.1), has_cand(), cand_3_st()))
    draw_2DProfX(p, "simPtVsRelPt_3st_eta21to24_ProfX", '2.1 < #eta < 2.4' + title, binning, toplot, AND(base_cut_eta(2.1,2.4), has_cand(), cand_3_st()))
    draw_2DProfX(p, "simPtVsRelPt_3st_eta18to24_ProfX", '1.8 < #eta < 2.4' + title, binning, toplot, AND(base_cut_eta(1.8,2.4), has_cand(), cand_3_st()))

    draw_2DProfX(p, "simPtVsRelPt_3seg_eta00to24_ProfX", '0.0 < #eta < 2.4' + title, binning, toplot, AND(base_cut_eta(), has_cand(), cand_3_st_3_segments()))
    draw_2DProfX(p, "simPtVsRelPt_3seg_eta15to18_ProfX", '1.5 < #eta < 1.8' + title, binning, toplot, AND(base_cut_eta(1.5,1.8), has_cand(), cand_3_st_3_segments()))
    draw_2DProfX(p, "simPtVsRelPt_3seg_eta18to21_ProfX", '1.8 < #eta < 2.1' + title, binning, toplot, AND(base_cut_eta(1.8,2.1), has_cand(), cand_3_st_3_segments()))
    draw_2DProfX(p, "simPtVsRelPt_3seg_eta21to24_ProfX", '2.1 < #eta < 2.4' + title, binning, toplot, AND(base_cut_eta(2.1,2.4), has_cand(), cand_3_st_3_segments()))
    draw_2DProfX(p, "simPtVsRelPt_3seg_eta18to24_ProfX", '1.8 < #eta < 2.4' + title, binning, toplot, AND(base_cut_eta(1.8,2.4), has_cand(), cand_3_st_3_segments()))

    draw_2DProfX(p, "simPtVsRelPt_2seg1rh_eta00to24_ProfX", '0.0 < #eta < 2.4' + title, binning, toplot, AND(base_cut_eta(), has_cand(), cand_3_st_2_segments_1_rechit()))
    draw_2DProfX(p, "simPtVsRelPt_2seg1rh_eta15to18_ProfX", '1.5 < #eta < 1.8' + title, binning, toplot, AND(base_cut_eta(1.5,1.8), has_cand(), cand_3_st_2_segments_1_rechit()))
    draw_2DProfX(p, "simPtVsRelPt_2seg1rh_eta18to21_ProfX", '1.8 < #eta < 2.1' + title, binning, toplot, AND(base_cut_eta(1.8,2.1), has_cand(), cand_3_st_2_segments_1_rechit()))
    draw_2DProfX(p, "simPtVsRelPt_2seg1rh_eta21to24_ProfX", '2.1 < #eta < 2.4' + title, binning, toplot, AND(base_cut_eta(2.1,2.4), has_cand(), cand_3_st_2_segments_1_rechit()))
    draw_2DProfX(p, "simPtVsRelPt_2seg1rh_eta18to24_ProfX", '1.8 < #eta < 2.4' + title, binning, toplot, AND(base_cut_eta(1.8,2.4), has_cand(), cand_3_st_2_segments_1_rechit()))

    draw_2DProfX(p, "simPtVsRelPt_2seg1rh_gem_eta00to24_ProfX", '0.0 < #eta < 2.4' + title, binning, toplot, AND(base_cut_eta(), has_cand(), cand_3_st_2_segments_1_rechit_gem_endcap()))
    draw_2DProfX(p, "simPtVsRelPt_2seg1rh_gem_eta15to18_ProfX", '1.5 < #eta < 1.8' + title, binning, toplot, AND(base_cut_eta(1.5,1.8), has_cand(), cand_3_st_2_segments_1_rechit_gem_endcap()))
    draw_2DProfX(p, "simPtVsRelPt_2seg1rh_gem_eta18to21_ProfX", '1.8 < #eta < 2.1' + title, binning, toplot, AND(base_cut_eta(1.8,2.1), has_cand(), cand_3_st_2_segments_1_rechit_gem_endcap()))
    draw_2DProfX(p, "simPtVsRelPt_2seg1rh_gem_eta21to24_ProfX", '2.1 < #eta < 2.4' + title, binning, toplot, AND(base_cut_eta(2.1,2.4), has_cand(), cand_3_st_2_segments_1_rechit_gem_endcap()))
    draw_2DProfX(p, "simPtVsRelPt_2seg1rh_gem_eta18to24_ProfX", '1.8 < #eta < 2.4' + title, binning, toplot, AND(base_cut_eta(1.8,2.4), has_cand(), cand_3_st_2_segments_1_rechit_gem_endcap()))

    draw_2DProfX(p, "simPtVsRelPt_2seg1rh_GE21_eta00to24_ProfX", '0.0 < #eta < 2.4' + title, binning, toplot, AND(base_cut_eta(), has_cand(), cand_3_st_2_segments_1_rechit_GE21_endcap()))
    draw_2DProfX(p, "simPtVsRelPt_2seg1rh_GE21_eta15to18_ProfX", '1.5 < #eta < 1.8' + title, binning, toplot, AND(base_cut_eta(1.5,1.8), has_cand(), cand_3_st_2_segments_1_rechit_GE21_endcap()))
    draw_2DProfX(p, "simPtVsRelPt_2seg1rh_GE21_eta18to21_ProfX", '1.8 < #eta < 2.1' + title, binning, toplot, AND(base_cut_eta(1.8,2.1), has_cand(), cand_3_st_2_segments_1_rechit_GE21_endcap()))
    draw_2DProfX(p, "simPtVsRelPt_2seg1rh_GE21_eta21to24_ProfX", '2.1 < #eta < 2.4' + title, binning, toplot, AND(base_cut_eta(2.1,2.4), has_cand(), cand_3_st_2_segments_1_rechit_GE21_endcap()))
    draw_2DProfX(p, "simPtVsRelPt_2seg1rh_GE21_eta18to24_ProfX", '1.8 < #eta < 2.4' + title, binning, toplot, AND(base_cut_eta(1.8,2.4), has_cand(), cand_3_st_2_segments_1_rechit_GE21_endcap()))

    draw_2DProfX(p, "simPtVsRelPt_2seg1rh_GE21_noCSCst2_eta00to24_ProfX", '0.0 < #eta < 2.4' + title, binning, toplot, AND(base_cut_eta(), has_cand(), cand_3_st_2_segments_1_rechit_GE21_nocscst2_endcap()))
    draw_2DProfX(p, "simPtVsRelPt_2seg1rh_GE21_noCSCst2_eta15to18_ProfX", '1.5 < #eta < 1.8' + title, binning, toplot, AND(base_cut_eta(1.5,1.8), has_cand(), cand_3_st_2_segments_1_rechit_GE21_nocscst2_endcap()))
    draw_2DProfX(p, "simPtVsRelPt_2seg1rh_GE21_noCSCst2_eta18to21_ProfX", '1.8 < #eta < 2.1' + title, binning, toplot, AND(base_cut_eta(1.8,2.1), has_cand(), cand_3_st_2_segments_1_rechit_GE21_nocscst2_endcap()))
    draw_2DProfX(p, "simPtVsRelPt_2seg1rh_GE21_noCSCst2_eta21to24_ProfX", '2.1 < #eta < 2.4' + title, binning, toplot, AND(base_cut_eta(2.1,2.4), has_cand(), cand_3_st_2_segments_1_rechit_GE21_nocscst2_endcap()))
    draw_2DProfX(p, "simPtVsRelPt_2seg1rh_GE21_noCSCst2_eta18to24_ProfX", '1.8 < #eta < 2.4' + title, binning, toplot, AND(base_cut_eta(1.8,2.4), has_cand(), cand_3_st_2_segments_1_rechit_GE21_nocscst2_endcap()))


