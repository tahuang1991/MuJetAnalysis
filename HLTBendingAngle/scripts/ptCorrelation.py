from ROOT import *
from Helpers import *

def makePlot(p, corr, title, oneD=False):
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
    gStyle.SetFillStyle(0)
    gPad.SetTickx(1)
    gPad.SetTicky(1)

    corr.SetTitle("                                                                      14 TeV,  PU = %d"%(p.pu))
    corr.GetXaxis().SetLabelSize(0.05)
    corr.GetYaxis().SetLabelSize(0.05)
    corr.GetXaxis().SetTitleSize(0.06)
    corr.GetYaxis().SetTitleSize(0.06)        
    corr.SetLineWidth(2)
    #    corr.SetMarkerStyle(22)
    corr.SetMarkerSize(1)
    #    corr.SetMarkerColor(kBlue)        
    corr.Draw("s")
    if not oneD:
        corr.Draw("COLZ")
    #    tex = drawLabel(p.ctau + ", " + p.mass,0.25,0.75,0.05)
    #    tex3 = drawLabel("H #rightarrow 2n_{1} #rightarrow 2n_{D}2Z_{D} #rightarrow 2n_{D}4#mu",0.25,0.65,0.05)
    tex2 = applyTdrStyle()

    c.SaveAs(p.outputDir + title + p.ext)
    
    
def pTCorrelationPlots(p):
    
    def base_cut(min_sim_pt=5, max_sim_pt = 999, min_dxy=0, max_dxy=10, min_l1_pt=0):
        return AND(n_dt_csc_seg(1), sim_pt(min_sim_pt, max_sim_pt), sim_dxy(min_dxy, max_dxy), has_L1Extra(min_l1_pt), Gd_fid())

    draw_2D(p, "simPtVsRecoPt_3st", 'pT correlation; p_{T}^{SIM} [GeV]; p_{T}^{RECO} [GeV]', "(100, 0, 100, 100, 0, 100)", "recoChargedCandidate_pt:sim_pt", AND(base_cut(), has_cand(), cand_3_st()), "COLZ")

    absEtaVsRelPt_axisTitle =  ";|#eta|; |p_{T}^{SIM}-p_{T}^{RECO}|/p_{T}^{SIM}"
    binning = "(60, 0, 3.0, 100, -1.0, 1.0)"
    toplot = "(sim_pt-recoChargedCandidate_pt)/sim_pt:abs(sim_eta)"

    draw_2D(p, "absEtaVsRelPt_3st_pt5to10", '5 < p_{T} < 10 GeV' + absEtaVsRelPt_axisTitle, binning, toplot, AND(base_cut(5,10), has_cand(), cand_3_st()), "COLZ")
    draw_2D(p, "absEtaVsRelPt_3st_pt10to15", '10 < p_{T} < 15 GeV' + absEtaVsRelPt_axisTitle, binning, toplot, AND(base_cut(10,15), has_cand(), cand_3_st()), "COLZ")
    draw_2D(p, "absEtaVsRelPt_3st_pt15to20", '15 < p_{T} < 20 GeV' + absEtaVsRelPt_axisTitle, binning, toplot, AND(base_cut(15,20), has_cand(), cand_3_st()), "COLZ")
    draw_2D(p, "absEtaVsRelPt_3st_pt20to40", '20 < p_{T} < 40 GeV' + absEtaVsRelPt_axisTitle, binning, toplot, AND(base_cut(20,40), has_cand(), cand_3_st()), "COLZ")

    draw_2D(p, "absEtaVsRelPt_3seg_pt5to10", '5 < p_{T} < 10 GeV' + absEtaVsRelPt_axisTitle, binning, toplot, AND(base_cut(5,10), has_cand(), cand_3_st_3_segments()), "COLZ")
    draw_2D(p, "absEtaVsRelPt_3seg_pt10to15", '10 < p_{T} < 15 GeV' + absEtaVsRelPt_axisTitle, binning, toplot, AND(base_cut(10,15), has_cand(), cand_3_st_3_segments()), "COLZ")
    draw_2D(p, "absEtaVsRelPt_3seg_pt15to20", '15 < p_{T} < 20 GeV' + absEtaVsRelPt_axisTitle, binning, toplot, AND(base_cut(15,20), has_cand(), cand_3_st_3_segments()), "COLZ")
    draw_2D(p, "absEtaVsRelPt_3seg_pt20to40", '20 < p_{T} < 40 GeV' + absEtaVsRelPt_axisTitle, binning, toplot, AND(base_cut(20,40), has_cand(), cand_3_st_3_segments()), "COLZ")

    draw_2D(p, "absEtaVsRelPt_2seg1rh_pt5to10", '5 < p_{T} < 10 GeV' + absEtaVsRelPt_axisTitle, binning, toplot, AND(base_cut(5,10), has_cand(), cand_3_st_2_segments_1_rechit()), "COLZ")
    draw_2D(p, "absEtaVsRelPt_2seg1rh_pt10to15", '10 < p_{T} < 15 GeV' + absEtaVsRelPt_axisTitle, binning, toplot, AND(base_cut(10,15), has_cand(), cand_3_st_2_segments_1_rechit()), "COLZ")
    draw_2D(p, "absEtaVsRelPt_2seg1rh_pt15to20", '15 < p_{T} < 20 GeV' + absEtaVsRelPt_axisTitle, binning, toplot, AND(base_cut(15,20), has_cand(), cand_3_st_2_segments_1_rechit()), "COLZ")
    draw_2D(p, "absEtaVsRelPt_2seg1rh_pt20to40", '20 < p_{T} < 40 GeV' + absEtaVsRelPt_axisTitle, binning, toplot, AND(base_cut(20,40), has_cand(), cand_3_st_2_segments_1_rechit()), "COLZ")

    draw_2D(p, "absEtaVsRelPt_2seg1rh_gem_pt5to10", '5 < p_{T} < 10 GeV' + absEtaVsRelPt_axisTitle, binning, toplot, AND(base_cut(5,10), has_cand(), cand_3_st_2_segments_1_rechit_gem_endcap()), "COLZ")
    draw_2D(p, "absEtaVsRelPt_2seg1rh_gem_pt10to15", '10 < p_{T} < 15 GeV' + absEtaVsRelPt_axisTitle, binning, toplot, AND(base_cut(10,15), has_cand(), cand_3_st_2_segments_1_rechit_gem_endcap()), "COLZ")
    draw_2D(p, "absEtaVsRelPt_2seg1rh_gem_pt15to20", '15 < p_{T} < 20 GeV' + absEtaVsRelPt_axisTitle, binning, toplot, AND(base_cut(15,20), has_cand(), cand_3_st_2_segments_1_rechit_gem_endcap()), "COLZ")
    draw_2D(p, "absEtaVsRelPt_2seg1rh_gem_pt20to40", '20 < p_{T} < 40 GeV' + absEtaVsRelPt_axisTitle, binning, toplot, AND(base_cut(20,40), has_cand(), cand_3_st_2_segments_1_rechit_gem_endcap()), "COLZ")

    draw_2D(p, "absEtaVsRelPt_2seg1rh_GE21_pt5to10", '5 < p_{T} < 10 GeV' + absEtaVsRelPt_axisTitle, binning, toplot, AND(base_cut(5,10), has_cand(), cand_3_st_2_segments_1_rechit_GE21_endcap()), "COLZ")
    draw_2D(p, "absEtaVsRelPt_2seg1rh_GE21_pt10to15", '10 < p_{T} < 15 GeV' + absEtaVsRelPt_axisTitle, binning, toplot, AND(base_cut(10,15), has_cand(), cand_3_st_2_segments_1_rechit_GE21_endcap()), "COLZ")
    draw_2D(p, "absEtaVsRelPt_2seg1rh_GE21_pt15to20", '15 < p_{T} < 20 GeV' + absEtaVsRelPt_axisTitle, binning, toplot, AND(base_cut(15,20), has_cand(), cand_3_st_2_segments_1_rechit_GE21_endcap()), "COLZ")
    draw_2D(p, "absEtaVsRelPt_2seg1rh_GE21_pt20to40", '20 < p_{T} < 40 GeV' + absEtaVsRelPt_axisTitle, binning, toplot, AND(base_cut(20,40), has_cand(), cand_3_st_2_segments_1_rechit_GE21_endcap()), "COLZ")

    draw_2D(p, "absEtaVsRelPt_2seg1rh_GE21_noCSCst2_pt5to10", '5 < p_{T} < 10 GeV' + absEtaVsRelPt_axisTitle, binning, toplot, AND(base_cut(5,10), has_cand(), cand_3_st_2_segments_1_rechit_GE21_nocscst2_endcap()), "COLZ")
    draw_2D(p, "absEtaVsRelPt_2seg1rh_GE21_noCSCst2_pt10to15", '10 < p_{T} < 15 GeV' + absEtaVsRelPt_axisTitle, binning, toplot, AND(base_cut(10,15), has_cand(), cand_3_st_2_segments_1_rechit_GE21_nocscst2_endcap()), "COLZ")
    draw_2D(p, "absEtaVsRelPt_2seg1rh_GE21_noCSCst2_pt15to20", '15 < p_{T} < 20 GeV' + absEtaVsRelPt_axisTitle, binning, toplot, AND(base_cut(15,20), has_cand(), cand_3_st_2_segments_1_rechit_GE21_nocscst2_endcap()), "COLZ")
    draw_2D(p, "absEtaVsRelPt_2seg1rh_GE21_noCSCst2_pt20to40", '20 < p_{T} < 40 GeV' + absEtaVsRelPt_axisTitle, binning, toplot, AND(base_cut(20,40), has_cand(), cand_3_st_2_segments_1_rechit_GE21_nocscst2_endcap()), "COLZ")


    draw_2DProfX(p, "absEtaVsRelPt_3st_pt5to10_ProfX", '5 < p_{T} < 10 GeV' + absEtaVsRelPt_axisTitle, binning, toplot, AND(base_cut(5,10), has_cand(), cand_3_st()))
    draw_2DProfX(p, "absEtaVsRelPt_3st_pt10to15_ProfX", '10 < p_{T} < 15 GeV' + absEtaVsRelPt_axisTitle, binning, toplot, AND(base_cut(10,15), has_cand(), cand_3_st()))
    draw_2DProfX(p, "absEtaVsRelPt_3st_pt15to20_ProfX", '15 < p_{T} < 20 GeV' + absEtaVsRelPt_axisTitle, binning, toplot, AND(base_cut(15,20), has_cand(), cand_3_st()))
    draw_2DProfX(p, "absEtaVsRelPt_3st_pt20to40_ProfX", '20 < p_{T} < 40 GeV' + absEtaVsRelPt_axisTitle, binning, toplot, AND(base_cut(20,40), has_cand(), cand_3_st()))

    draw_2DProfX(p, "absEtaVsRelPt_3seg_pt5to10_ProfX", '5 < p_{T} < 10 GeV' + absEtaVsRelPt_axisTitle, binning, toplot, AND(base_cut(5,10), has_cand(), cand_3_st_3_segments()))
    draw_2DProfX(p, "absEtaVsRelPt_3seg_pt10to15_ProfX", '10 < p_{T} < 15 GeV' + absEtaVsRelPt_axisTitle, binning, toplot, AND(base_cut(10,15), has_cand(), cand_3_st_3_segments()))
    draw_2DProfX(p, "absEtaVsRelPt_3seg_pt15to20_ProfX", '15 < p_{T} < 20 GeV' + absEtaVsRelPt_axisTitle, binning, toplot, AND(base_cut(15,20), has_cand(), cand_3_st_3_segments()))
    draw_2DProfX(p, "absEtaVsRelPt_3seg_pt20to40_ProfX", '20 < p_{T} < 40 GeV' + absEtaVsRelPt_axisTitle, binning, toplot, AND(base_cut(20,40), has_cand(), cand_3_st_3_segments()))

    draw_2DProfX(p, "absEtaVsRelPt_2seg1rh_pt5to10_ProfX", '5 < p_{T} < 10 GeV' + absEtaVsRelPt_axisTitle, binning, toplot, AND(base_cut(5,10), has_cand(), cand_3_st_2_segments_1_rechit()))
    draw_2DProfX(p, "absEtaVsRelPt_2seg1rh_pt10to15_ProfX", '10 < p_{T} < 15 GeV' + absEtaVsRelPt_axisTitle, binning, toplot, AND(base_cut(10,15), has_cand(), cand_3_st_2_segments_1_rechit()))
    draw_2DProfX(p, "absEtaVsRelPt_2seg1rh_pt15to20_ProfX", '15 < p_{T} < 20 GeV' + absEtaVsRelPt_axisTitle, binning, toplot, AND(base_cut(15,20), has_cand(), cand_3_st_2_segments_1_rechit()))
    draw_2DProfX(p, "absEtaVsRelPt_2seg1rh_pt20to40_ProfX", '20 < p_{T} < 40 GeV' + absEtaVsRelPt_axisTitle, binning, toplot, AND(base_cut(20,40), has_cand(), cand_3_st_2_segments_1_rechit()))

    draw_2DProfX(p, "absEtaVsRelPt_2seg1rh_gem_pt5to10_ProfX", '5 < p_{T} < 10 GeV' + absEtaVsRelPt_axisTitle, binning, toplot, AND(base_cut(5,10), has_cand(), cand_3_st_2_segments_1_rechit_gem_endcap()))
    draw_2DProfX(p, "absEtaVsRelPt_2seg1rh_gem_pt10to15_ProfX", '10 < p_{T} < 15 GeV' + absEtaVsRelPt_axisTitle, binning, toplot, AND(base_cut(10,15), has_cand(), cand_3_st_2_segments_1_rechit_gem_endcap()))
    draw_2DProfX(p, "absEtaVsRelPt_2seg1rh_gem_pt15to20_ProfX", '15 < p_{T} < 20 GeV' + absEtaVsRelPt_axisTitle, binning, toplot, AND(base_cut(15,20), has_cand(), cand_3_st_2_segments_1_rechit_gem_endcap()))
    draw_2DProfX(p, "absEtaVsRelPt_2seg1rh_gem_pt20to40_ProfX", '20 < p_{T} < 40 GeV' + absEtaVsRelPt_axisTitle, binning, toplot, AND(base_cut(20,40), has_cand(), cand_3_st_2_segments_1_rechit_gem_endcap()))

    draw_2DProfX(p, "absEtaVsRelPt_2seg1rh_GE21_pt5to10_ProfX", '5 < p_{T} < 10 GeV' + absEtaVsRelPt_axisTitle, binning, toplot, AND(base_cut(5,10), has_cand(), cand_3_st_2_segments_1_rechit_GE21_endcap()))
    draw_2DProfX(p, "absEtaVsRelPt_2seg1rh_GE21_pt10to15_ProfX", '10 < p_{T} < 15 GeV' + absEtaVsRelPt_axisTitle, binning, toplot, AND(base_cut(10,15), has_cand(), cand_3_st_2_segments_1_rechit_GE21_endcap()))
    draw_2DProfX(p, "absEtaVsRelPt_2seg1rh_GE21_pt15to20_ProfX", '15 < p_{T} < 20 GeV' + absEtaVsRelPt_axisTitle, binning, toplot, AND(base_cut(15,20), has_cand(), cand_3_st_2_segments_1_rechit_GE21_endcap()))
    draw_2DProfX(p, "absEtaVsRelPt_2seg1rh_GE21_pt20to40_ProfX", '20 < p_{T} < 40 GeV' + absEtaVsRelPt_axisTitle, binning, toplot, AND(base_cut(20,40), has_cand(), cand_3_st_2_segments_1_rechit_GE21_endcap()))

    draw_2DProfX(p, "absEtaVsRelPt_2seg1rh_GE21_noCSCst2_pt5to10_ProfX", '5 < p_{T} < 10 GeV' + absEtaVsRelPt_axisTitle, binning, toplot, AND(base_cut(5,10), has_cand(), cand_3_st_2_segments_1_rechit_GE21_nocscst2_endcap()))
    draw_2DProfX(p, "absEtaVsRelPt_2seg1rh_GE21_noCSCst2_pt10to15_ProfX", '10 < p_{T} < 15 GeV' + absEtaVsRelPt_axisTitle, binning, toplot, AND(base_cut(10,15), has_cand(), cand_3_st_2_segments_1_rechit_GE21_nocscst2_endcap()))
    draw_2DProfX(p, "absEtaVsRelPt_2seg1rh_GE21_noCSCst2_pt15to20_ProfX", '15 < p_{T} < 20 GeV' + absEtaVsRelPt_axisTitle, binning, toplot, AND(base_cut(15,20), has_cand(), cand_3_st_2_segments_1_rechit_GE21_nocscst2_endcap()))
    draw_2DProfX(p, "absEtaVsRelPt_2seg1rh_GE21_noCSCst2_pt20to40_ProfX", '20 < p_{T} < 40 GeV' + absEtaVsRelPt_axisTitle, binning, toplot, AND(base_cut(20,40), has_cand(), cand_3_st_2_segments_1_rechit_GE21_nocscst2_endcap()))


    """
    sim_pT = TH1F( 'sim_pT', '', 50, 0, 50 )
    reco_pT = TH1F( 'reco_pT', '', 50, 0, 50 )
    rel_pT = TH1F( 'rel_pT', '', 50, 0, 50 )

    relPt = TH1F( 'relPt', ';(p_{T}^{SIM} - p_{T}^{RECO})/p_{T}^{SIM}; Entries', 50, -1, 1 )
    relPt_eta18to24 = TH1F( 'relPt_eta18to24', ';(p_{T}^{SIM} - p_{T}^{RECO})/p_{T}^{SIM}; Entries', 50, -1, 1 )
    relPt_eta18to24_3seg = TH1F( 'relPt_eta18to24_3seg', ';(p_{T}^{SIM} - p_{T}^{RECO})/p_{T}^{SIM}; Entries', 50, -1, 1 )
    relPt_eta18to24_2seg = TH1F( 'relPt_eta18to24_2seg', ';(p_{T}^{SIM} - p_{T}^{RECO})/p_{T}^{SIM}; Entries', 50, -1, 1 )
    relPt_eta18to24_2seg_1rh = TH1F( 'relPt_eta18to24_2seg_1rh', ';(p_{T}^{SIM} - p_{T}^{RECO})/p_{T}^{SIM}; Entries', 50, -1, 1 )
    relPt_eta18to24_2seg_GE21 = TH1F( 'relPt_eta18to24_2seg_GE21', ';(p_{T}^{SIM} - p_{T}^{RECO})/p_{T}^{SIM}; Entries', 50, -1, 1 )
    relPt_eta18to24_2seg_GE21_noCSCst2 = TH1F( 'relPt_eta18to24_2seg_GE21_noCSCst2', ';(p_{T}^{SIM} - p_{T}^{RECO})/p_{T}^{SIM}; Entries', 50, -1, 1 )

    delPt = TH1F( 'delPt', ';p_{T}^{SIM} - p_{T}^{RECO} [GeV]; Entries', 20, -10, 10 )
    delPt_eta18to24 = TH1F( 'delPt_eta18to24', ';p_{T}^{SIM} - p_{T}^{RECO} [GeV]; Entries', 20, -10, 10 )
    delPt_eta18to24_3seg = TH1F( 'delPt_eta18to24_3seg', ';p_{T}^{SIM} - p_{T}^{RECO} [GeV]; Entries', 20, -10, 10 )
    delPt_eta18to24_2seg = TH1F( 'delPt_eta18to24_2seg', ';p_{T}^{SIM} - p_{T}^{RECO} [GeV]; Entries', 20, -10, 10 )
    delPt_eta18to24_2seg_1rh = TH1F( 'delPt_eta18to24_2seg_1rh', ';p_{T}^{SIM} - p_{T}^{RECO} [GeV]; Entries', 20, -10, 10 )
    delPt_eta18to24_2seg_GE21 = TH1F( 'delPt_eta18to24_2seg_GE21', ';p_{T}^{SIM} - p_{T}^{RECO} [GeV]; Entries', 20, -10, 10 )
    delPt_eta18to24_2seg_GE21_noCSCst2 = TH1F( 'delPt_eta18to24_2seg_GE21_noCSCst2', ';p_{T}^{SIM} - p_{T}^{RECO} [GeV]; Entries', 20, -10, 10 )

    simPtVsRecoPt = TH2F( 'simPtVsRecoPt', '; p_{T}^{SIM} [GeV]; p_{T}^{RECO} [GeV]', 100, 0, 100, 100, 0, 100)
    invPtVsInvRecoPt = TH2F( 'invPtVsInvRecoPt', '; 1/p_{T}^{SIM} [1/GeV]; 1/p_{T}^{RECO} [1/GeV]', 20, 0, 0.2, 50, 0, 0.5)
    qInvPtVsInvRecoPt = TH2F( 'qInvPtVsInvRecoPt', '; q/p_{T}^{SIM} [1/GeV]; 1/p_{T}^{RECO} [1/GeV]', 40, -0.2, 0.2, 50, 0, 0.5)
    absEtaVsSimPtMinusRecoPt = TH2F( 'absEtaVsSimPtMinusRecoPt', '; |#eta|; p_{T}^{SIM} - p_{T}^{RECO} [GeV]', 60, 0, 3.0, 50, -25, 25)
    absEtaVsRelPt = TH2F( 'absEtaVsRelPt', '; |#eta|; (p_{T}^{SIM} - p_{T}^{RECO})/p_{T}^{SIM}', 60, 0, 3.0, 100, -1, 1)
    absEtaVsAbsRelPt = TH2F( 'absEtaVsAbsRelPt', '; |#eta|; |p_{T}^{SIM} - p_{T}^{RECO}|/p_{T}^{SIM}', 60, 0, 3.0, 100, 0, 1.0)

    simPtVsRelPt_eta09to12 = TH2F( 'simPtVsRelPt_eta09to12', '; p_{T}^{SIM}; (p_{T}^{SIM} - p_{T}^{RECO})/p_{T}^{SIM}', 100, 0, 100, 100, -1, 1)
    simPtVsRelPt_eta12to15 = TH2F( 'simPtVsRelPt_eta12to15', '; p_{T}^{SIM}; (p_{T}^{SIM} - p_{T}^{RECO})/p_{T}^{SIM}', 100, 0, 100, 100, -1, 1)
    simPtVsRelPt_eta15to18 = TH2F( 'simPtVsRelPt_eta15to18', '; p_{T}^{SIM}; (p_{T}^{SIM} - p_{T}^{RECO})/p_{T}^{SIM}', 100, 0, 100, 100, -1, 1)
    simPtVsRelPt_eta18to21 = TH2F( 'simPtVsRelPt_eta18to21', '; p_{T}^{SIM}; (p_{T}^{SIM} - p_{T}^{RECO})/p_{T}^{SIM}', 100, 0, 100, 100, -1, 1)
    simPtVsRelPt_eta21to24 = TH2F( 'simPtVsRelPt_eta21to24', '; p_{T}^{SIM}; (p_{T}^{SIM} - p_{T}^{RECO})/p_{T}^{SIM}', 100, 0, 100, 100, -1, 1)
    simPtVsRelPt_eta18to24 = TH2F( 'simPtVsRelPt_eta18to24', '; p_{T}^{SIM}; (p_{T}^{SIM} - p_{T}^{RECO})/p_{T}^{SIM}', 100, 0, 100, 100, -1, 1)

    simPtVsRelPt_eta09to12_3seg = TH2F( 'simPtVsRelPt_eta09to12_3seg', '; p_{T}^{SIM}; (p_{T}^{SIM} - p_{T}^{RECO})/p_{T}^{SIM}', 100, 0, 100, 100, -1, 1)
    simPtVsRelPt_eta12to15_3seg = TH2F( 'simPtVsRelPt_eta12to15_3seg', '; p_{T}^{SIM}; (p_{T}^{SIM} - p_{T}^{RECO})/p_{T}^{SIM}', 100, 0, 100, 100, -1, 1)
    simPtVsRelPt_eta15to18_3seg = TH2F( 'simPtVsRelPt_eta15to18_3seg', '; p_{T}^{SIM}; (p_{T}^{SIM} - p_{T}^{RECO})/p_{T}^{SIM}', 100, 0, 100, 100, -1, 1)
    simPtVsRelPt_eta18to21_3seg = TH2F( 'simPtVsRelPt_eta18to21_3seg', '; p_{T}^{SIM}; (p_{T}^{SIM} - p_{T}^{RECO})/p_{T}^{SIM}', 100, 0, 100, 100, -1, 1)
    simPtVsRelPt_eta21to24_3seg = TH2F( 'simPtVsRelPt_eta21to24_3seg', '; p_{T}^{SIM}; (p_{T}^{SIM} - p_{T}^{RECO})/p_{T}^{SIM}', 100, 0, 100, 100, -1, 1)

    simPtVsRelPt_eta09to12_2seg = TH2F( 'simPtVsRelPt_eta09to12_2seg', '; p_{T}^{SIM}; (p_{T}^{SIM} - p_{T}^{RECO})/p_{T}^{SIM}', 100, 0, 100, 100, -1, 1)
    simPtVsRelPt_eta12to15_2seg = TH2F( 'simPtVsRelPt_eta12to15_2seg', '; p_{T}^{SIM}; (p_{T}^{SIM} - p_{T}^{RECO})/p_{T}^{SIM}', 100, 0, 100, 100, -1, 1)
    simPtVsRelPt_eta15to18_2seg = TH2F( 'simPtVsRelPt_eta15to18_2seg', '; p_{T}^{SIM}; (p_{T}^{SIM} - p_{T}^{RECO})/p_{T}^{SIM}', 100, 0, 100, 100, -1, 1)
    simPtVsRelPt_eta18to21_2seg = TH2F( 'simPtVsRelPt_eta18to21_2seg', '; p_{T}^{SIM}; (p_{T}^{SIM} - p_{T}^{RECO})/p_{T}^{SIM}', 100, 0, 100, 100, -1, 1)
    simPtVsRelPt_eta21to24_2seg = TH2F( 'simPtVsRelPt_eta21to24_2seg', '; p_{T}^{SIM}; (p_{T}^{SIM} - p_{T}^{RECO})/p_{T}^{SIM}', 100, 0, 100, 100, -1, 1)

    simPtVsRelPt_eta09to12_2seg_1rh = TH2F( 'simPtVsRelPt_eta09to12_2seg_1rh', '; p_{T}^{SIM}; (p_{T}^{SIM} - p_{T}^{RECO})/p_{T}^{SIM}', 100, 0, 100, 100, -1, 1)
    simPtVsRelPt_eta12to15_2seg_1rh = TH2F( 'simPtVsRelPt_eta12to15_2seg_1rh', '; p_{T}^{SIM}; (p_{T}^{SIM} - p_{T}^{RECO})/p_{T}^{SIM}', 100, 0, 100, 100, -1, 1)
    simPtVsRelPt_eta15to18_2seg_1rh = TH2F( 'simPtVsRelPt_eta15to18_2seg_1rh', '; p_{T}^{SIM}; (p_{T}^{SIM} - p_{T}^{RECO})/p_{T}^{SIM}', 100, 0, 100, 100, -1, 1)
    simPtVsRelPt_eta18to21_2seg_1rh = TH2F( 'simPtVsRelPt_eta18to21_2seg_1rh', '; p_{T}^{SIM}; (p_{T}^{SIM} - p_{T}^{RECO})/p_{T}^{SIM}', 100, 0, 100, 100, -1, 1)
    simPtVsRelPt_eta21to24_2seg_1rh = TH2F( 'simPtVsRelPt_eta21to24_2seg_1rh', '; p_{T}^{SIM}; (p_{T}^{SIM} - p_{T}^{RECO})/p_{T}^{SIM}', 100, 0, 100, 100, -1, 1)

    simPtVsRelPt_eta09to12_2seg_gem = TH2F( 'simPtVsRelPt_eta09to12_2seg_gem', '; p_{T}^{SIM}; (p_{T}^{SIM} - p_{T}^{RECO})/p_{T}^{SIM}', 100, 0, 100, 100, -1, 1)
    simPtVsRelPt_eta12to15_2seg_gem = TH2F( 'simPtVsRelPt_eta12to15_2seg_gem', '; p_{T}^{SIM}; (p_{T}^{SIM} - p_{T}^{RECO})/p_{T}^{SIM}', 100, 0, 100, 100, -1, 1)
    simPtVsRelPt_eta15to18_2seg_gem = TH2F( 'simPtVsRelPt_eta15to18_2seg_gem', '; p_{T}^{SIM}; (p_{T}^{SIM} - p_{T}^{RECO})/p_{T}^{SIM}', 100, 0, 100, 100, -1, 1)
    simPtVsRelPt_eta18to21_2seg_gem = TH2F( 'simPtVsRelPt_eta18to21_2seg_gem', '; p_{T}^{SIM}; (p_{T}^{SIM} - p_{T}^{RECO})/p_{T}^{SIM}', 100, 0, 100, 100, -1, 1)
    simPtVsRelPt_eta21to24_2seg_gem = TH2F( 'simPtVsRelPt_eta21to24_2seg_gem', '; p_{T}^{SIM}; (p_{T}^{SIM} - p_{T}^{RECO})/p_{T}^{SIM}', 100, 0, 100, 100, -1, 1)

    simPtVsRelPt_eta09to12_2seg_GE21 = TH2F( 'simPtVsRelPt_eta09to12_2seg_GE21', '; p_{T}^{SIM}; (p_{T}^{SIM} - p_{T}^{RECO})/p_{T}^{SIM}', 100, 0, 100, 100, -1, 1)
    simPtVsRelPt_eta12to15_2seg_GE21 = TH2F( 'simPtVsRelPt_eta12to15_2seg_GE21', '; p_{T}^{SIM}; (p_{T}^{SIM} - p_{T}^{RECO})/p_{T}^{SIM}', 100, 0, 100, 100, -1, 1)
    simPtVsRelPt_eta15to18_2seg_GE21 = TH2F( 'simPtVsRelPt_eta15to18_2seg_GE21', '; p_{T}^{SIM}; (p_{T}^{SIM} - p_{T}^{RECO})/p_{T}^{SIM}', 100, 0, 100, 100, -1, 1)
    simPtVsRelPt_eta18to21_2seg_GE21 = TH2F( 'simPtVsRelPt_eta18to21_2seg_GE21', '; p_{T}^{SIM}; (p_{T}^{SIM} - p_{T}^{RECO})/p_{T}^{SIM}', 100, 0, 100, 100, -1, 1)
    simPtVsRelPt_eta21to24_2seg_GE21 = TH2F( 'simPtVsRelPt_eta21to24_2seg_GE21', '; p_{T}^{SIM}; (p_{T}^{SIM} - p_{T}^{RECO})/p_{T}^{SIM}', 100, 0, 100, 100, -1, 1)

    simPtVsRelPt_eta09to12_2seg_GE21_noCSCst2 = TH2F( 'simPtVsRelPt_eta09to12_2seg_GE21_noCSCst2', '; p_{T}^{SIM}; (p_{T}^{SIM} - p_{T}^{RECO})/p_{T}^{SIM}', 100, 0, 100, 100, -1, 1)
    simPtVsRelPt_eta12to15_2seg_GE21_noCSCst2 = TH2F( 'simPtVsRelPt_eta12to15_2seg_GE21_noCSCst2', '; p_{T}^{SIM}; (p_{T}^{SIM} - p_{T}^{RECO})/p_{T}^{SIM}', 100, 0, 100, 100, -1, 1)
    simPtVsRelPt_eta15to18_2seg_GE21_noCSCst2 = TH2F( 'simPtVsRelPt_eta15to18_2seg_GE21_noCSCst2', '; p_{T}^{SIM}; (p_{T}^{SIM} - p_{T}^{RECO})/p_{T}^{SIM}', 100, 0, 100, 100, -1, 1)
    simPtVsRelPt_eta18to21_2seg_GE21_noCSCst2 = TH2F( 'simPtVsRelPt_eta18to21_2seg_GE21_noCSCst2', '; p_{T}^{SIM}; (p_{T}^{SIM} - p_{T}^{RECO})/p_{T}^{SIM}', 100, 0, 100, 100, -1, 1)
    simPtVsRelPt_eta21to24_2seg_GE21_noCSCst2 = TH2F( 'simPtVsRelPt_eta21to24_2seg_GE21_noCSCst2', '; p_{T}^{SIM}; (p_{T}^{SIM} - p_{T}^{RECO})/p_{T}^{SIM}', 100, 0, 100, 100, -1, 1)

    simPtVsRelPt_eta18to24 = TH2F( 'simPtVsRelPt_eta18to24', '; p_{T}^{SIM}; (p_{T}^{SIM} - p_{T}^{RECO})/p_{T}^{SIM}', 50, 0, 100, 50, -1, 1)
    simPtVsRelPt_eta18to24_3seg = TH2F( 'simPtVsRelPt_eta18to24_3seg', '; p_{T}^{SIM}; (p_{T}^{SIM} - p_{T}^{RECO})/p_{T}^{SIM}', 50, 0, 100, 50, -1, 1)
    simPtVsRelPt_eta18to24_2seg = TH2F( 'simPtVsRelPt_eta18to24_2seg', '; p_{T}^{SIM}; (p_{T}^{SIM} - p_{T}^{RECO})/p_{T}^{SIM}', 50, 0, 100, 50, -1, 1)
    simPtVsRelPt_eta18to24_2seg_1rh = TH2F( 'simPtVsRelPt_eta18to24_2seg_1rh', '; p_{T}^{SIM}; (p_{T}^{SIM} - p_{T}^{RECO})/p_{T}^{SIM}', 50, 0, 100, 50, -1, 1)
    simPtVsRelPt_eta18to24_2seg_GE21 = TH2F( 'simPtVsRelPt_eta18to24_2seg_GE21', '; p_{T}^{SIM}; (p_{T}^{SIM} - p_{T}^{RECO})/p_{T}^{SIM}', 50, 0, 100, 50, -1, 1)
    simPtVsRelPt_eta18to24_2seg_GE21_noCSCst2 = TH2F( 'simPtVsRelPt_eta18to24_2seg_GE21_noCSCst2', '; p_{T}^{SIM}; (p_{T}^{SIM} - p_{T}^{RECO})/p_{T}^{SIM}', 50, 0, 100, 50, -1, 1)

    ## updates September 8
    diff  = TH1F( 'diff', 'pT cand - pT simtrack/pT simtrack', 50, -5, 5 )

    
    
    tree = p.tree
    #print "entries", tree.GetEntries()
    for k in range(0, tree.GetEntries()):
        tree.GetEntry(k)
        if (tree.sim_pt > 5 and
            abs(tree.sim_eta) < 2.4 and 
            tree.genGdMu_pt[0] > 5 and
            tree.genGdMu_pt[1] > 5 and
            abs(tree.genGdMu_eta[0]) > 0 and 
            abs(tree.genGdMu_eta[1]) > 0 and 
            abs(tree.genGdMu_eta[0]) < 2.4 and 
            abs(tree.genGdMu_eta[1]) < 2.4 and 
            tree.genGd_lxy > 0 and
            tree.genGd_lxy < 300 and
            abs(tree.genGd_vz) < 500 and
            (tree.genGd0Gd1_dR > 2) and 
            (tree.n_dt_seg + tree.n_csc_seg >= 1) and 
            0 < abs(tree.sim_dxy) and abs(tree.sim_dxy) < 10 and 
            (tree.has_l1Extra>0 and tree.l1Extra_dR<0.1 and tree.l1Extra_pt>0) ):
            
            sim_pT.Fill(tree.sim_pt)
            reco_pT.Fill(tree.recoChargedCandidate_pt)
            
            if (tree.has_recoChargedCandidate>=1 and tree.recoChargedCandidate_pt>0):
                
                ## 3 station requirement
                if (cand_3_st_tree_int(tree)):

                    simPtVsRecoPt.Fill(tree.sim_pt, tree.recoChargedCandidate_pt)
                    invPtVsInvRecoPt.Fill(1./tree.sim_pt, 1/tree.recoChargedCandidate_pt)
                    qInvPtVsInvRecoPt.Fill(tree.sim_charge/tree.sim_pt, 1/tree.recoChargedCandidate_pt)
                    absEtaVsSimPtMinusRecoPt.Fill(abs(tree.sim_eta), tree.sim_pt - tree.recoChargedCandidate_pt)
                    absEtaVsRelPt.Fill(abs(tree.sim_eta), (tree.sim_pt - tree.recoChargedCandidate_pt)/tree.sim_pt)
                    absEtaVsAbsRelPt.Fill(abs(tree.sim_eta), abs(tree.sim_pt - tree.recoChargedCandidate_pt)/tree.sim_pt)

                    relPt.Fill((tree.sim_pt - tree.recoChargedCandidate_pt)/tree.sim_pt)
                    delPt.Fill(tree.sim_pt - tree.recoChargedCandidate_pt)
                    
                    if 5 < tree.sim_pt and tree.sim_pt < 10:
                        absEtaVsRelPt_pt5to10.Fill(abs(tree.sim_eta), (tree.sim_pt - tree.recoChargedCandidate_pt)/tree.sim_pt)
                    if 10 < tree.sim_pt and tree.sim_pt < 15:
                        absEtaVsRelPt_pt10to15.Fill(abs(tree.sim_eta), (tree.sim_pt - tree.recoChargedCandidate_pt)/tree.sim_pt)
                    if 15 < tree.sim_pt and tree.sim_pt < 20:
                        absEtaVsRelPt_pt15to20.Fill(abs(tree.sim_eta), (tree.sim_pt - tree.recoChargedCandidate_pt)/tree.sim_pt)
                    if 20 < tree.sim_pt and tree.sim_pt < 40:                    
                        absEtaVsRelPt_pt20to40.Fill(abs(tree.sim_eta), (tree.sim_pt - tree.recoChargedCandidate_pt)/tree.sim_pt)

                    if (0.9 < abs(tree.sim_eta) and abs(tree.sim_eta) < 1.2):
                        simPtVsRelPt_eta09to12.Fill(tree.sim_pt, (tree.sim_pt - tree.recoChargedCandidate_pt)/tree.sim_pt)
                    elif (1.2 < abs(tree.sim_eta) and abs(tree.sim_eta) < 1.5):
                        simPtVsRelPt_eta12to15.Fill(tree.sim_pt, (tree.sim_pt - tree.recoChargedCandidate_pt)/tree.sim_pt)
                    elif (1.5 < abs(tree.sim_eta) and abs(tree.sim_eta) < 1.8):
                        simPtVsRelPt_eta15to18.Fill(tree.sim_pt, (tree.sim_pt - tree.recoChargedCandidate_pt)/tree.sim_pt)
                    elif (1.8 < abs(tree.sim_eta) and abs(tree.sim_eta) < 2.1):
                        simPtVsRelPt_eta18to21.Fill(tree.sim_pt, (tree.sim_pt - tree.recoChargedCandidate_pt)/tree.sim_pt)
                    elif (2.1 < abs(tree.sim_eta) and abs(tree.sim_eta) < 2.4):
                        simPtVsRelPt_eta21to24.Fill(tree.sim_pt, (tree.sim_pt - tree.recoChargedCandidate_pt)/tree.sim_pt)
                    if (1.8 < abs(tree.sim_eta) and abs(tree.sim_eta) < 2.4):
                        simPtVsRelPt_eta18to24.Fill(tree.sim_pt, (tree.sim_pt - tree.recoChargedCandidate_pt)/tree.sim_pt)
                        relPt_eta18to24.Fill((tree.sim_pt - tree.recoChargedCandidate_pt)/tree.sim_pt)
                        delPt_eta18to24.Fill(tree.sim_pt - tree.recoChargedCandidate_pt)

                if (cand_3_st_tree_3_segments_endcap_int(tree)):

                    if (1.2 < abs(tree.sim_eta) and abs(tree.sim_eta) < 1.5):
                        simPtVsRelPt_eta12to15_3seg.Fill(tree.sim_pt, (tree.sim_pt - tree.recoChargedCandidate_pt)/tree.sim_pt)
                    elif (1.5 < abs(tree.sim_eta) and abs(tree.sim_eta) < 1.8):
                        simPtVsRelPt_eta15to18_3seg.Fill(tree.sim_pt, (tree.sim_pt - tree.recoChargedCandidate_pt)/tree.sim_pt)
                    elif (1.8 < abs(tree.sim_eta) and abs(tree.sim_eta) < 2.1):
                        simPtVsRelPt_eta18to21_3seg.Fill(tree.sim_pt, (tree.sim_pt - tree.recoChargedCandidate_pt)/tree.sim_pt)
                    elif (2.1 < abs(tree.sim_eta) and abs(tree.sim_eta) < 2.4):
                        simPtVsRelPt_eta21to24_3seg.Fill(tree.sim_pt, (tree.sim_pt - tree.recoChargedCandidate_pt)/tree.sim_pt)
                    if (1.8 < abs(tree.sim_eta) and abs(tree.sim_eta) < 2.4):
                        simPtVsRelPt_eta18to24_3seg.Fill(tree.sim_pt, (tree.sim_pt - tree.recoChargedCandidate_pt)/tree.sim_pt)
                        relPt_eta18to24_3seg.Fill((tree.sim_pt - tree.recoChargedCandidate_pt)/tree.sim_pt)
                        delPt_eta18to24_3seg.Fill(tree.sim_pt - tree.recoChargedCandidate_pt)

                if cand_3_st_tree_2_segments_endcap_int(tree):

                    if (1.2 < abs(tree.sim_eta) and abs(tree.sim_eta) < 1.5):
                        simPtVsRelPt_eta12to15_2seg.Fill(tree.sim_pt, (tree.sim_pt - tree.recoChargedCandidate_pt)/tree.sim_pt)
                    elif (1.5 < abs(tree.sim_eta) and abs(tree.sim_eta) < 1.8):
                        simPtVsRelPt_eta15to18_2seg.Fill(tree.sim_pt, (tree.sim_pt - tree.recoChargedCandidate_pt)/tree.sim_pt)
                    elif (1.8 < abs(tree.sim_eta) and abs(tree.sim_eta) < 2.1):
                        simPtVsRelPt_eta18to21_2seg.Fill(tree.sim_pt, (tree.sim_pt - tree.recoChargedCandidate_pt)/tree.sim_pt)
                    elif (2.1 < abs(tree.sim_eta) and abs(tree.sim_eta) < 2.4):
                        simPtVsRelPt_eta21to24_2seg.Fill(tree.sim_pt, (tree.sim_pt - tree.recoChargedCandidate_pt)/tree.sim_pt)
                    if (1.8 < abs(tree.sim_eta) and abs(tree.sim_eta) < 2.4):
                        simPtVsRelPt_eta18to24_2seg.Fill(tree.sim_pt, (tree.sim_pt - tree.recoChargedCandidate_pt)/tree.sim_pt)
                        relPt_eta18to24_2seg.Fill((tree.sim_pt - tree.recoChargedCandidate_pt)/tree.sim_pt)

                if cand_3_st_tree_2_segments_1_rechit_endcap_int(tree):

                    if (1.2 < abs(tree.sim_eta) and abs(tree.sim_eta) < 1.5):
                        simPtVsRelPt_eta12to15_2seg_1rh.Fill(tree.sim_pt, (tree.sim_pt - tree.recoChargedCandidate_pt)/tree.sim_pt)
                    elif (1.5 < abs(tree.sim_eta) and abs(tree.sim_eta) < 1.8):
                        simPtVsRelPt_eta15to18_2seg_1rh.Fill(tree.sim_pt, (tree.sim_pt - tree.recoChargedCandidate_pt)/tree.sim_pt)
                    elif (1.8 < abs(tree.sim_eta) and abs(tree.sim_eta) < 2.1):
                        simPtVsRelPt_eta18to21_2seg_1rh.Fill(tree.sim_pt, (tree.sim_pt - tree.recoChargedCandidate_pt)/tree.sim_pt)
                    elif (2.1 < abs(tree.sim_eta) and abs(tree.sim_eta) < 2.4):
                        simPtVsRelPt_eta21to24_2seg_1rh.Fill(tree.sim_pt, (tree.sim_pt - tree.recoChargedCandidate_pt)/tree.sim_pt)
                    if (1.8 < abs(tree.sim_eta) and abs(tree.sim_eta) < 2.4):
                        simPtVsRelPt_eta18to24_2seg_1rh.Fill(tree.sim_pt, (tree.sim_pt - tree.recoChargedCandidate_pt)/tree.sim_pt)
                        relPt_eta18to24_2seg_1rh.Fill((tree.sim_pt - tree.recoChargedCandidate_pt)/tree.sim_pt)
                        delPt_eta18to24_2seg_1rh.Fill(tree.sim_pt - tree.recoChargedCandidate_pt)

                if cand_3_st_tree_2_segments_1_rechit_gem_endcap_int(tree):

                    if (1.2 < abs(tree.sim_eta) and abs(tree.sim_eta) < 1.5):
                        simPtVsRelPt_eta12to15_2seg_gem.Fill(tree.sim_pt, (tree.sim_pt - tree.recoChargedCandidate_pt)/tree.sim_pt)
                    elif (1.5 < abs(tree.sim_eta) and abs(tree.sim_eta) < 1.8):
                        simPtVsRelPt_eta15to18_2seg_gem.Fill(tree.sim_pt, (tree.sim_pt - tree.recoChargedCandidate_pt)/tree.sim_pt)
                    elif (1.8 < abs(tree.sim_eta) and abs(tree.sim_eta) < 2.1):
                        simPtVsRelPt_eta18to21_2seg_gem.Fill(tree.sim_pt, (tree.sim_pt - tree.recoChargedCandidate_pt)/tree.sim_pt)
                    elif (2.1 < abs(tree.sim_eta) and abs(tree.sim_eta) < 2.4):
                        simPtVsRelPt_eta21to24_2seg_gem.Fill(tree.sim_pt, (tree.sim_pt - tree.recoChargedCandidate_pt)/tree.sim_pt)

                if cand_3_st_tree_2_segments_1_rechit_GE21_endcap_int(tree):

                    if (1.2 < abs(tree.sim_eta) and abs(tree.sim_eta) < 1.5):
                        simPtVsRelPt_eta12to15_2seg_GE21.Fill(tree.sim_pt, (tree.sim_pt - tree.recoChargedCandidate_pt)/tree.sim_pt)
                    elif (1.5 < abs(tree.sim_eta) and abs(tree.sim_eta) < 1.8):
                        simPtVsRelPt_eta15to18_2seg_GE21.Fill(tree.sim_pt, (tree.sim_pt - tree.recoChargedCandidate_pt)/tree.sim_pt)
                    elif (1.8 < abs(tree.sim_eta) and abs(tree.sim_eta) < 2.1):
                        simPtVsRelPt_eta18to21_2seg_GE21.Fill(tree.sim_pt, (tree.sim_pt - tree.recoChargedCandidate_pt)/tree.sim_pt)
                    elif (2.1 < abs(tree.sim_eta) and abs(tree.sim_eta) < 2.4):
                        simPtVsRelPt_eta21to24_2seg_GE21.Fill(tree.sim_pt, (tree.sim_pt - tree.recoChargedCandidate_pt)/tree.sim_pt)
                    if (1.8 < abs(tree.sim_eta) and abs(tree.sim_eta) < 2.4):
                        simPtVsRelPt_eta18to24_2seg_GE21.Fill(tree.sim_pt, (tree.sim_pt - tree.recoChargedCandidate_pt)/tree.sim_pt)
                        relPt_eta18to24_2seg_GE21.Fill((tree.sim_pt - tree.recoChargedCandidate_pt)/tree.sim_pt)
                        delPt_eta18to24_2seg_GE21.Fill(tree.sim_pt - tree.recoChargedCandidate_pt)

                if cand_3_st_tree_2_segments_1_rechit_GE21_nocscst2_endcap_int(tree):


                    if (1.2 < abs(tree.sim_eta) and abs(tree.sim_eta) < 1.5):
                        simPtVsRelPt_eta12to15_2seg_GE21_noCSCst2.Fill(tree.sim_pt, (tree.sim_pt - tree.recoChargedCandidate_pt)/tree.sim_pt)
                    elif (1.5 < abs(tree.sim_eta) and abs(tree.sim_eta) < 1.8):
                        simPtVsRelPt_eta15to18_2seg_GE21_noCSCst2.Fill(tree.sim_pt, (tree.sim_pt - tree.recoChargedCandidate_pt)/tree.sim_pt)
                    elif (1.8 < abs(tree.sim_eta) and abs(tree.sim_eta) < 2.1):
                        simPtVsRelPt_eta18to21_2seg_GE21_noCSCst2.Fill(tree.sim_pt, (tree.sim_pt - tree.recoChargedCandidate_pt)/tree.sim_pt)
                    elif (2.1 < abs(tree.sim_eta) and abs(tree.sim_eta) < 2.4):
                        simPtVsRelPt_eta21to24_2seg_GE21_noCSCst2.Fill(tree.sim_pt, (tree.sim_pt - tree.recoChargedCandidate_pt)/tree.sim_pt)
                    if (2.1 < abs(tree.sim_eta) and abs(tree.sim_eta) < 2.4):
                        simPtVsRelPt_eta18to24_2seg_GE21_noCSCst2.Fill(tree.sim_pt, (tree.sim_pt - tree.recoChargedCandidate_pt)/tree.sim_pt)
                        relPt_eta18to24_2seg_GE21_noCSCst2.Fill((tree.sim_pt - tree.recoChargedCandidate_pt)/tree.sim_pt)
                        delPt_eta18to24_2seg_GE21_noCSCst2.Fill(tree.sim_pt - tree.recoChargedCandidate_pt)


    simPtVsRecoPt_ProfX = simPtVsRecoPt.ProfileX()
    invPtVsInvRecoPt_ProfX = invPtVsInvRecoPt.ProfileX()
    qInvPtVsInvRecoPt_ProfX = qInvPtVsInvRecoPt.ProfileX()
    absEtaVsSimPtMinusRecoPt_ProfX = absEtaVsSimPtMinusRecoPt.ProfileX()
    absEtaVsRelPt_ProfX = absEtaVsRelPt.ProfileX()
    absEtaVsAbsRelPt_ProfX = absEtaVsAbsRelPt.ProfileX()

    simPtVsRelPt_eta09to12_ProfX = simPtVsRelPt_eta09to12.ProfileX()
    simPtVsRelPt_eta12to15_ProfX = simPtVsRelPt_eta12to15.ProfileX()
    simPtVsRelPt_eta15to18_ProfX = simPtVsRelPt_eta15to18.ProfileX()
    simPtVsRelPt_eta18to21_ProfX = simPtVsRelPt_eta18to21.ProfileX()
    simPtVsRelPt_eta21to24_ProfX = simPtVsRelPt_eta21to24.ProfileX()
    simPtVsRelPt_eta18to24_ProfX = simPtVsRelPt_eta18to24.ProfileX()

    simPtVsRelPt_eta09to12_3seg_ProfX = simPtVsRelPt_eta09to12_3seg.ProfileX()
    simPtVsRelPt_eta12to15_3seg_ProfX = simPtVsRelPt_eta12to15_3seg.ProfileX()
    simPtVsRelPt_eta15to18_3seg_ProfX = simPtVsRelPt_eta15to18_3seg.ProfileX()
    simPtVsRelPt_eta18to21_3seg_ProfX = simPtVsRelPt_eta18to21_3seg.ProfileX()
    simPtVsRelPt_eta21to24_3seg_ProfX = simPtVsRelPt_eta21to24_3seg.ProfileX()

    simPtVsRelPt_eta09to12_2seg_ProfX = simPtVsRelPt_eta09to12_2seg.ProfileX()
    simPtVsRelPt_eta12to15_2seg_ProfX = simPtVsRelPt_eta12to15_2seg.ProfileX()
    simPtVsRelPt_eta15to18_2seg_ProfX = simPtVsRelPt_eta15to18_2seg.ProfileX()
    simPtVsRelPt_eta18to21_2seg_ProfX = simPtVsRelPt_eta18to21_2seg.ProfileX()
    simPtVsRelPt_eta21to24_2seg_ProfX = simPtVsRelPt_eta21to24_2seg.ProfileX()

    simPtVsRelPt_eta09to12_2seg_1rh_ProfX = simPtVsRelPt_eta09to12_2seg_1rh.ProfileX()
    simPtVsRelPt_eta12to15_2seg_1rh_ProfX = simPtVsRelPt_eta12to15_2seg_1rh.ProfileX()
    simPtVsRelPt_eta15to18_2seg_1rh_ProfX = simPtVsRelPt_eta15to18_2seg_1rh.ProfileX()
    simPtVsRelPt_eta18to21_2seg_1rh_ProfX = simPtVsRelPt_eta18to21_2seg_1rh.ProfileX()
    simPtVsRelPt_eta21to24_2seg_1rh_ProfX = simPtVsRelPt_eta21to24_2seg_1rh.ProfileX()

    simPtVsRelPt_eta09to12_2seg_gem_ProfX = simPtVsRelPt_eta09to12_2seg_gem.ProfileX()
    simPtVsRelPt_eta12to15_2seg_gem_ProfX = simPtVsRelPt_eta12to15_2seg_gem.ProfileX()
    simPtVsRelPt_eta15to18_2seg_gem_ProfX = simPtVsRelPt_eta15to18_2seg_gem.ProfileX()
    simPtVsRelPt_eta18to21_2seg_gem_ProfX = simPtVsRelPt_eta18to21_2seg_gem.ProfileX()
    simPtVsRelPt_eta21to24_2seg_gem_ProfX = simPtVsRelPt_eta21to24_2seg_gem.ProfileX()

    simPtVsRelPt_eta09to12_2seg_GE21_ProfX = simPtVsRelPt_eta09to12_2seg_GE21.ProfileX()
    simPtVsRelPt_eta12to15_2seg_GE21_ProfX = simPtVsRelPt_eta12to15_2seg_GE21.ProfileX()
    simPtVsRelPt_eta15to18_2seg_GE21_ProfX = simPtVsRelPt_eta15to18_2seg_GE21.ProfileX()
    simPtVsRelPt_eta18to21_2seg_GE21_ProfX = simPtVsRelPt_eta18to21_2seg_GE21.ProfileX()
    simPtVsRelPt_eta21to24_2seg_GE21_ProfX = simPtVsRelPt_eta21to24_2seg_GE21.ProfileX()

    simPtVsRelPt_eta09to12_2seg_GE21_noCSCst2_ProfX = simPtVsRelPt_eta09to12_2seg_GE21_noCSCst2.ProfileX()
    simPtVsRelPt_eta12to15_2seg_GE21_noCSCst2_ProfX = simPtVsRelPt_eta12to15_2seg_GE21_noCSCst2.ProfileX()
    simPtVsRelPt_eta15to18_2seg_GE21_noCSCst2_ProfX = simPtVsRelPt_eta15to18_2seg_GE21_noCSCst2.ProfileX()
    simPtVsRelPt_eta18to21_2seg_GE21_noCSCst2_ProfX = simPtVsRelPt_eta18to21_2seg_GE21_noCSCst2.ProfileX()
    simPtVsRelPt_eta21to24_2seg_GE21_noCSCst2_ProfX = simPtVsRelPt_eta21to24_2seg_GE21_noCSCst2.ProfileX()

    simPtVsRelPt_eta18to24_ProfX = simPtVsRelPt_eta18to24.ProfileX()
    simPtVsRelPt_eta18to24_3seg_ProfX = simPtVsRelPt_eta18to24_3seg.ProfileX()
    simPtVsRelPt_eta18to24_2seg_ProfX = simPtVsRelPt_eta18to24_2seg.ProfileX()
    simPtVsRelPt_eta18to24_2seg_1rh_ProfX = simPtVsRelPt_eta18to24_2seg_1rh.ProfileX()
    simPtVsRelPt_eta18to24_2seg_GE21_ProfX = simPtVsRelPt_eta18to24_2seg_GE21.ProfileX()
    simPtVsRelPt_eta18to24_2seg_GE21_noCSCst2_ProfX = simPtVsRelPt_eta18to24_2seg_GE21_noCSCst2.ProfileX()

    makePlot(p, absEtaVsRelPt_pt5to10, "absEtaVsRelPt_pt5to10")
    makePlot(p, absEtaVsRelPt_pt10to15, "absEtaVsRelPt_pt10to15")
    makePlot(p, absEtaVsRelPt_pt15to20, "absEtaVsRelPt_pt15to20")
    makePlot(p, absEtaVsRelPt_pt20to40, "absEtaVsRelPt_pt20to40")

    absEtaVsRelPt_pt5to10_ProfX = absEtaVsRelPt_pt5to10.ProfileX()
    absEtaVsRelPt_pt10to15_ProfX = absEtaVsRelPt_pt10to15.ProfileX()
    absEtaVsRelPt_pt15to20_ProfX = absEtaVsRelPt_pt15to20.ProfileX()
    absEtaVsRelPt_pt20to40_ProfX = absEtaVsRelPt_pt20to40.ProfileX()

    makePlot(p, absEtaVsRelPt_pt5to10_ProfX, "absEtaVsRelPt_pt5to10_ProfX", True)
    makePlot(p, absEtaVsRelPt_pt10to15_ProfX, "absEtaVsRelPt_pt10to15_ProfX", True)
    makePlot(p, absEtaVsRelPt_pt15to20_ProfX, "absEtaVsRelPt_pt15to20_ProfX", True)
    makePlot(p, absEtaVsRelPt_pt20to40_ProfX, "absEtaVsRelPt_pt20to40_ProfX", True)


    ## correlation
    makeCorrelationPlots = False
    if makeCorrelationPlots:
        makePlot(p, simPtVsRecoPt, "simPtVsRecoPt")
        makePlot(p, invPtVsInvRecoPt, "invPtVsInvRecoPt")
        makePlot(p, qInvPtVsInvRecoPt, "qInvPtVsInvRecoPt")
        makePlot(p, absEtaVsSimPtMinusRecoPt, "absEtaVsSimPtMinusRecoPt")
        makePlot(p, absEtaVsRelPt, "absEtaVsRelPt")
        makePlot(p, absEtaVsAbsRelPt, "absEtaVsAbsRelPt")

        makePlot(p, simPtVsRelPt_eta09to12, "simPtVsRelPt_eta09to12")
        makePlot(p, simPtVsRelPt_eta12to15, "simPtVsRelPt_eta12to15")
        makePlot(p, simPtVsRelPt_eta15to18, "simPtVsRelPt_eta15to18")
        makePlot(p, simPtVsRelPt_eta18to21, "simPtVsRelPt_eta18to21")
        makePlot(p, simPtVsRelPt_eta21to24, "simPtVsRelPt_eta21to24")
        
        makePlot(p, simPtVsRelPt_eta09to12_3seg, "simPtVsRelPt_eta09to12_3seg")
        makePlot(p, simPtVsRelPt_eta12to15_3seg, "simPtVsRelPt_eta12to15_3seg")
        makePlot(p, simPtVsRelPt_eta15to18_3seg, "simPtVsRelPt_eta15to18_3seg")
        makePlot(p, simPtVsRelPt_eta18to21_3seg, "simPtVsRelPt_eta18to21_3seg") 
        makePlot(p, simPtVsRelPt_eta21to24_3seg, "simPtVsRelPt_eta21to24_3seg")
        
        makePlot(p, simPtVsRelPt_eta09to12_2seg, "simPtVsRelPt_eta09to12_2seg")
        makePlot(p, simPtVsRelPt_eta12to15_2seg, "simPtVsRelPt_eta12to15_2seg")
        makePlot(p, simPtVsRelPt_eta15to18_2seg, "simPtVsRelPt_eta15to18_2seg")
        makePlot(p, simPtVsRelPt_eta18to21_2seg, "simPtVsRelPt_eta18to21_2seg")
        makePlot(p, simPtVsRelPt_eta21to24_2seg, "simPtVsRelPt_eta21to24_2seg")
        
        makePlot(p, simPtVsRelPt_eta12to15_2seg_1rh, "simPtVsRelPt_eta12to15_2seg_1rh") 
        makePlot(p, simPtVsRelPt_eta15to18_2seg_1rh, "simPtVsRelPt_eta15to18_2seg_1rh") 
        makePlot(p, simPtVsRelPt_eta18to21_2seg_1rh, "simPtVsRelPt_eta18to21_2seg_1rh")
        makePlot(p, simPtVsRelPt_eta21to24_2seg_1rh, "simPtVsRelPt_eta21to24_2seg_1rh")
        
        makePlot(p, simPtVsRelPt_eta12to15_2seg_gem, "simPtVsRelPt_eta12to15_2seg_gem")
        makePlot(p, simPtVsRelPt_eta15to18_2seg_gem, "simPtVsRelPt_eta15to18_2seg_gem")
        makePlot(p, simPtVsRelPt_eta18to21_2seg_gem, "simPtVsRelPt_eta18to21_2seg_gem")
        makePlot(p, simPtVsRelPt_eta21to24_2seg_gem, "simPtVsRelPt_eta21to24_2seg_gem")
        
        makePlot(p, simPtVsRelPt_eta12to15_2seg_GE21, "simPtVsRelPt_eta12to15_2seg_GE21")
        makePlot(p, simPtVsRelPt_eta15to18_2seg_GE21, "simPtVsRelPt_eta15to18_2seg_GE21")
        makePlot(p, simPtVsRelPt_eta18to21_2seg_GE21, "simPtVsRelPt_eta18to21_2seg_GE21")
        makePlot(p, simPtVsRelPt_eta21to24_2seg_GE21, "simPtVsRelPt_eta21to24_2seg_GE21")

        makePlot(p, simPtVsRelPt_eta12to15_2seg_GE21_noCSCst2, "simPtVsRelPt_eta12to15_2seg_GE21_noCSCst2")
        makePlot(p, simPtVsRelPt_eta15to18_2seg_GE21_noCSCst2, "simPtVsRelPt_eta15to18_2seg_GE21_noCSCst2")
        makePlot(p, simPtVsRelPt_eta18to21_2seg_GE21_noCSCst2, "simPtVsRelPt_eta18to21_2seg_GE21_noCSCst2")
        makePlot(p, simPtVsRelPt_eta21to24_2seg_GE21_noCSCst2, "simPtVsRelPt_eta21to24_2seg_GE21_noCSCst2")
        
        makePlot(p, simPtVsRelPt_eta18to24, "simPtVsRelPt_eta18to24")
        makePlot(p, simPtVsRelPt_eta18to24_3seg, "simPtVsRelPt_eta18to24_3seg")
        makePlot(p, simPtVsRelPt_eta18to24_2seg, "simPtVsRelPt_eta18to24_2seg")
        makePlot(p, simPtVsRelPt_eta18to24_2seg_1rh, "simPtVsRelPt_eta18to24_2seg_1rh")
        makePlot(p, simPtVsRelPt_eta18to24_2seg_GE21, "simPtVsRelPt_eta18to24_2seg_GE21")
        makePlot(p, simPtVsRelPt_eta18to24_2seg_GE21_noCSCst2, "simPtVsRelPt_eta18to24_2seg_GE21_noCSCst2")


    ## profile
    makeProfile = True
    if makeProfile:
        makePlot(p, simPtVsRecoPt_ProfX, "simPtVsRecoPt_ProfX", True)
        makePlot(p, invPtVsInvRecoPt_ProfX, "invPtVsInvRecoPt_ProfX", True)
        makePlot(p, qInvPtVsInvRecoPt_ProfX, "qInvPtVsInvRecoPt_ProfX", True)
        makePlot(p, absEtaVsSimPtMinusRecoPt_ProfX, "absEtaVsSimPtMinusRecoPt_ProfX", True)
        makePlot(p, absEtaVsRelPt_ProfX, "absEtaVsRelPt_ProfX", True)
        makePlot(p, absEtaVsAbsRelPt_ProfX, "absEtaVsAbsRelPt_ProfX", True)
        
        makePlot(p, simPtVsRelPt_eta09to12_ProfX, "simPtVsRelPt_eta09to12_ProfX", True)
        makePlot(p, simPtVsRelPt_eta12to15_ProfX, "simPtVsRelPt_eta12to15_ProfX", True)
        makePlot(p, simPtVsRelPt_eta15to18_ProfX, "simPtVsRelPt_eta15to18_ProfX", True)
        makePlot(p, simPtVsRelPt_eta18to21_ProfX, "simPtVsRelPt_eta18to21_ProfX", True)
        makePlot(p, simPtVsRelPt_eta21to24_ProfX, "simPtVsRelPt_eta21to24_ProfX", True)
        
        makePlot(p, simPtVsRelPt_eta09to12_3seg_ProfX, "simPtVsRelPt_eta09to12_3seg_ProfX", True)
        makePlot(p, simPtVsRelPt_eta12to15_3seg_ProfX, "simPtVsRelPt_eta12to15_3seg_ProfX", True)
        makePlot(p, simPtVsRelPt_eta15to18_3seg_ProfX, "simPtVsRelPt_eta15to18_3seg_ProfX", True)
        makePlot(p, simPtVsRelPt_eta18to21_3seg_ProfX, "simPtVsRelPt_eta18to21_3seg_ProfX", True) 
        makePlot(p, simPtVsRelPt_eta21to24_3seg_ProfX, "simPtVsRelPt_eta21to24_3seg_ProfX", True)
        
        makePlot(p, simPtVsRelPt_eta09to12_2seg_ProfX, "simPtVsRelPt_eta09to12_2seg_ProfX", True)
        makePlot(p, simPtVsRelPt_eta12to15_2seg_ProfX, "simPtVsRelPt_eta12to15_2seg_ProfX", True)
        makePlot(p, simPtVsRelPt_eta15to18_2seg_ProfX, "simPtVsRelPt_eta15to18_2seg_ProfX", True)
        makePlot(p, simPtVsRelPt_eta18to21_2seg_ProfX, "simPtVsRelPt_eta18to21_2seg_ProfX", True)
        makePlot(p, simPtVsRelPt_eta21to24_2seg_ProfX, "simPtVsRelPt_eta21to24_2seg_ProfX", True)
        
        makePlot(p, simPtVsRelPt_eta12to15_2seg_1rh_ProfX, "simPtVsRelPt_eta12to15_2seg_1rh_ProfX", True) 
        makePlot(p, simPtVsRelPt_eta15to18_2seg_1rh_ProfX, "simPtVsRelPt_eta15to18_2seg_1rh_ProfX", True) 
        makePlot(p, simPtVsRelPt_eta18to21_2seg_1rh_ProfX, "simPtVsRelPt_eta18to21_2seg_1rh_ProfX", True)
        makePlot(p, simPtVsRelPt_eta21to24_2seg_1rh_ProfX, "simPtVsRelPt_eta21to24_2seg_1rh_ProfX", True)
        
        makePlot(p, simPtVsRelPt_eta12to15_2seg_gem_ProfX, "simPtVsRelPt_eta12to15_2seg_gem_ProfX", True)
        makePlot(p, simPtVsRelPt_eta15to18_2seg_gem_ProfX, "simPtVsRelPt_eta15to18_2seg_gem_ProfX", True)
        makePlot(p, simPtVsRelPt_eta18to21_2seg_gem_ProfX, "simPtVsRelPt_eta18to21_2seg_gem_ProfX", True)
        makePlot(p, simPtVsRelPt_eta21to24_2seg_gem_ProfX, "simPtVsRelPt_eta21to24_2seg_gem_ProfX", True)
        
        makePlot(p, simPtVsRelPt_eta12to15_2seg_GE21_ProfX, "simPtVsRelPt_eta12to15_2seg_GE21_ProfX", True)
        makePlot(p, simPtVsRelPt_eta15to18_2seg_GE21_ProfX, "simPtVsRelPt_eta15to18_2seg_GE21_ProfX", True)
        makePlot(p, simPtVsRelPt_eta18to21_2seg_GE21_ProfX, "simPtVsRelPt_eta18to21_2seg_GE21_ProfX", True)
        makePlot(p, simPtVsRelPt_eta21to24_2seg_GE21_ProfX, "simPtVsRelPt_eta21to24_2seg_GE21_ProfX", True)
        
        makePlot(p, simPtVsRelPt_eta12to15_2seg_GE21_noCSCst2_ProfX, "simPtVsRelPt_eta12to15_2seg_GE21_noCSCst2_ProfX", True)
        makePlot(p, simPtVsRelPt_eta15to18_2seg_GE21_noCSCst2_ProfX, "simPtVsRelPt_eta15to18_2seg_GE21_noCSCst2_ProfX", True)
        makePlot(p, simPtVsRelPt_eta18to21_2seg_GE21_noCSCst2_ProfX, "simPtVsRelPt_eta18to21_2seg_GE21_noCSCst2_ProfX", True)
        makePlot(p, simPtVsRelPt_eta21to24_2seg_GE21_noCSCst2_ProfX, "simPtVsRelPt_eta21to24_2seg_GE21_noCSCst2_ProfX", True)

        makePlot(p, simPtVsRelPt_eta18to24_ProfX, "simPtVsRelPt_eta18to24_ProfX", True)
        makePlot(p, simPtVsRelPt_eta18to24_3seg_ProfX, "simPtVsRelPt_eta18to24_3seg_ProfX", True)
        makePlot(p, simPtVsRelPt_eta18to24_2seg_ProfX, "simPtVsRelPt_eta18to24_2seg_ProfX", True)
        makePlot(p, simPtVsRelPt_eta18to24_2seg_1rh_ProfX, "simPtVsRelPt_eta18to24_2seg_1rh_ProfX", True)
        makePlot(p, simPtVsRelPt_eta18to24_2seg_GE21_ProfX, "simPtVsRelPt_eta18to24_2seg_GE21_ProfX", True)
        makePlot(p, simPtVsRelPt_eta18to24_2seg_GE21_noCSCst2_ProfX, "simPtVsRelPt_eta18to24_2seg_GE21_noCSCst2_ProfX", True)


    ## relative pt
    makerelpt = False
    if makerelpt:
        makePlot(p, relPt, "relPt", True)
        makePlot(p, relPt_eta18to24, "relPt_eta18to24", True)
        makePlot(p, relPt_eta18to24_3seg, "relPt_eta18to24_3seg", True)
        makePlot(p, relPt_eta18to24_2seg, "relPt_eta18to24_2seg", True)
        makePlot(p, relPt_eta18to24_2seg_1rh, "relPt_eta18to24_2seg_1rh", True)
        makePlot(p, relPt_eta18to24_2seg_GE21, "relPt_eta18to24_2seg_GE21", True)
        makePlot(p, relPt_eta18to24_2seg_GE21_noCSCst2, "relPt_eta18to24_2seg_GE21_noCSCst2", True)

        makePlot(p, delPt, "delPt", True)
        makePlot(p, delPt_eta18to24, "delPt_eta18to24", True)
        makePlot(p, delPt_eta18to24_3seg, "delPt_eta18to24_3seg", True)
        makePlot(p, delPt_eta18to24_2seg, "delPt_eta18to24_2seg", True)
        makePlot(p, delPt_eta18to24_2seg_1rh, "delPt_eta18to24_2seg_1rh", True)
        makePlot(p, delPt_eta18to24_2seg_GE21, "delPt_eta18to24_2seg_GE21", True)
        makePlot(p, delPt_eta18to24_2seg_GE21_noCSCst2, "delPt_eta18to24_2seg_GE21_noCSCst2", True)
    """
