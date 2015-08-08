from ROOT import *
from array import array
from Helpers import *

#54import sys
#sys.argv.append( '-b' )


ctau = 1000
sta="ME11"
varsh=12
tree = "HLTBendingAngle/trk_eff_csc_"+sta
f1 = TFile("../ct%d.root"%ctau)
t1 = f1.Get(tree)
mincut = 20

BINM=22
binLow = [0,1,2,3,4,5,6,7,8,9,10,12,14,16,18,20,24,28,32,36,42,50,60]


def denominator(dxy_min = 0, dxy_max = 5, eta_min = 1.6, eta_max = 1.7, var=12):
    return AND(AND( same_direction_cut(), has_csc(), has_csc_second(var), dxy(dxy_min, dxy_max), eta_sh_st1(eta_min, eta_max), csc_second_gp_eta(eta_min, eta_max, var), has_csc_hits(var)), OR(has_csc_second(13), has_csc_second(14)))

def numerator_pt_pos(dxy_min = 0, dxy_max = 5, eta_min = 1.6, eta_max = 1.7, sim_pt=10, var=12):
    return AND(denominator(dxy_min, dxy_max, eta_min, eta_max, var), pt_from_povercosh(eta_min, sim_pt, var))

def numerator_SimTrack_pt(dxy_min = 0, dxy_max = 5, eta_min = 1.6, eta_max = 1.7, sim_pt=10, var=12):
    return AND(denominator(dxy_min, dxy_max, eta_min, eta_max, var), pt_cut(eta_min, sim_pt, var))


def Plotter(etamin, etamax, dxy1, dxy2):
    c1 = TCanvas("a","b",1000,700)
    c1.SetGridx()
    c1.SetGridy()
    c1.SetTickx()
    c1.SetTicky()
    #gROOT.SetBatch(1)


    # In red related to pT
    # In blue related to pt position
    

    # Denominator SimTrack pt 0< dxy < 5
    SimTrack_pt_denominator_0dxy5 = TH1F("SimTrack_pt_denominator_0dxy5","SimTrack_pt_denominator_0dxy5", BINM,array.array('d', binLow))
    t1.Draw("pt_SimTrack_csc >> SimTrack_pt_denominator_0dxy5",denominator(0,5,etamin,etamax, varsh))
    print "%f < eta < %f"%(etamin, etamax)
    print denominator(0,5,etamin,etamax, varsh)

    # Denominator SimTrack pt 10< dxy < 30
    SimTrack_pt_denominator_10dxy30 = TH1F("SimTrack_pt_denominator_10dxy30","SimTrack_pt_denominator_10dxy30", BINM,array.array('d', binLow))
    t1.Draw("pt_SimTrack_csc >> SimTrack_pt_denominator_10dxy30",denominator(10,30,etamin,etamax,varsh))



    # Denominator SimTrack pt 50< dxy < 500
    SimTrack_pt_denominator_50dxy500 = TH1F("SimTrack_pt_denominator_50dxy500","SimTrack_pt_denominator_50dxy500", BINM,array.array('d', binLow))
    t1.Draw("pt_SimTrack_csc >> SimTrack_pt_denominator_50dxy500",denominator(50,500,etamin,etamax,varsh))

    
    SimTrack_pt_denominator_0dxy5.SetLineColor(kRed)
    SimTrack_pt_denominator_0dxy5.SetMarkerStyle(24)
    SimTrack_pt_denominator_0dxy5.SetMarkerColor(kRed)

    # Define pt_position as SimTrack total momentum over ( Global Position eta() measured at station ME11) 
    # Denominator for 0< dx < 5 on pt pos    
    pt_position_denominator_0dxy5 = TH1F("pt_position_denominator_0dxy5","pt_position_denominator_0dxy5", BINM,array.array('d', binLow))
    t1.Draw("csc_p_over_cosh_eta >> pt_position_denominator_0dxy5",denominator(0,5,etamin,etamax,varsh))


    pt_position_denominator_10dxy30 = TH1F("pt_position_denominator_10dxy30","pt_position_denominator_10dxy30", BINM,array.array('d', binLow))
    t1.Draw("csc_p_over_cosh_eta >> pt_position_denominator_10dxy30",denominator(10,30,etamin,etamax,varsh))

    pt_position_denominator_50dxy500 = TH1F("pt_position_denominator_50dxy500","pt_position_denominator_50dxy500", BINM,array.array('d', binLow))
    t1.Draw("csc_p_over_cosh_eta >> pt_position_denominator_50dxy500",denominator(50,500,etamin,etamax,varsh))

    pt_position_denominator_0dxy5.SetLineColor(kBlue)
    pt_position_denominator_0dxy5.SetLineWidth(2)
    pt_position_denominator_0dxy5.SetMarkerStyle(20)
    pt_position_denominator_0dxy5.SetMarkerColor(kBlue)
    pt_position_denominator_0dxy5.SetMarkerSize(1)
    
    # Numerator SimTrack pt
    SimTrack_pt_numerator_0dxy5 = TH1F("SimTrack_pt_numerator_0dxy5","SimTrack_pt_numerator_0dxy5", BINM,array.array('d', binLow))
    t1.Draw("pt_SimTrack_csc>> SimTrack_pt_numerator_0dxy5",numerator_SimTrack_pt(0, 5, etamin, etamax, mincut, varsh))

    print numerator_SimTrack_pt(0, 5, etamin, etamax, mincut, varsh)
    # Numerator SimTrack pt # 10 dx 30
    SimTrack_pt_numerator_10dxy30 = TH1F("SimTrack_pt_numerator_10dxy30","SimTrack_pt_numerator_10dxy30", BINM,array.array('d', binLow))
    t1.Draw("pt_SimTrack_csc>> SimTrack_pt_numerator_10dxy30",numerator_SimTrack_pt(10, 30, etamin, etamax, mincut, varsh))

    # Numerator SimTrack pt # 10 dx 30
    SimTrack_pt_numerator_50dxy500 = TH1F("SimTrack_pt_numerator_50dxy500","SimTrack_pt_numerator_50dxy500", BINM,array.array('d', binLow))
    t1.Draw("pt_SimTrack_csc>> SimTrack_pt_numerator_50dxy500",numerator_SimTrack_pt(50, 500, etamin, etamax, mincut, varsh))
    
    SimTrack_pt_numerator_0dxy5.SetLineColor(kRed)
    SimTrack_pt_numerator_0dxy5.SetMarkerStyle(24)
    SimTrack_pt_numerator_0dxy5.SetMarkerColor(kRed)



    # Numerator for dx < 5 on pt pos
    pt_position_numerator_0dxy5 = TH1F("pt_position_numerator_0dxy5","pt_position_numerator_0dxy5", BINM,array.array('d', binLow))
    t1.Draw("csc_p_over_cosh_eta>> pt_position_numerator_0dxy5",numerator_pt_pos(0,5,etamin,etamax,mincut, varsh))


    pt_position_numerator_10dxy30 = TH1F("pt_position_numerator_10dxy30","pt_position_numerator_10dxy30", BINM,array.array('d', binLow))
    t1.Draw("csc_p_over_cosh_eta>> pt_position_numerator_10dxy30",numerator_pt_pos(10,30,etamin,etamax,mincut, varsh))

    pt_position_numerator_50dxy500 = TH1F("pt_position_numerator_50dxy500","pt_position_numerator_50dxy500", BINM,array.array('d', binLow))
    t1.Draw("csc_p_over_cosh_eta>> pt_position_numerator_50dxy500",numerator_pt_pos(50,500,etamin,etamax,mincut, varsh))

    pt_position_numerator_0dxy5.SetLineColor(kBlue)
    pt_position_numerator_0dxy5.SetLineWidth(2)
    pt_position_numerator_0dxy5.SetMarkerStyle(20)
    pt_position_numerator_0dxy5.SetMarkerColor(kBlue)
    pt_position_numerator_0dxy5.SetMarkerSize(1)


    # Define the efficiency objets 
    eff_pt_position = TEfficiency(pt_position_numerator_0dxy5, pt_position_denominator_0dxy5)
    eff_pt_position.SetLineColor(kBlue+2)
    eff_pt_position.SetLineWidth(2)
    eff_pt_position.SetMarkerStyle(20)
    eff_pt_position.SetMarkerColor(kBlue+2)
    eff_pt_position.SetMarkerSize(1)

    # Black
    eff_pt_position_10dxy30 = TEfficiency(pt_position_numerator_10dxy30, pt_position_denominator_10dxy30)
    eff_pt_position_10dxy30.SetLineColor(kBlack)
    eff_pt_position_10dxy30.SetMarkerStyle(20)
    eff_pt_position_10dxy30.SetMarkerColor(kBlack)
    eff_pt_position_10dxy30.SetLineWidth(2)


    # Brown
    eff_pt_position_50dxy500 = TEfficiency(pt_position_numerator_10dxy30, pt_position_denominator_10dxy30)
    eff_pt_position_50dxy500.SetLineColor(kOrange+3)
    eff_pt_position_50dxy500.SetMarkerStyle(20)
    eff_pt_position_50dxy500.SetMarkerColor(kOrange+3)
    eff_pt_position_50dxy500.SetLineWidth(2)

    # Red 
    eff_SimTrack_pt = TEfficiency(SimTrack_pt_numerator_0dxy5, SimTrack_pt_denominator_0dxy5)
    eff_SimTrack_pt.SetLineColor(kRed)
    eff_SimTrack_pt.SetMarkerStyle(22)
    eff_SimTrack_pt.SetMarkerColor(kRed)
    eff_SimTrack_pt.SetLineWidth(2)

    # Magenta 
    eff_SimTrack_pt_10dxy30 = TEfficiency(SimTrack_pt_numerator_10dxy30, SimTrack_pt_denominator_10dxy30)
    eff_SimTrack_pt_10dxy30.SetLineColor(kPink+2)
    eff_SimTrack_pt_10dxy30.SetMarkerStyle(21)
    eff_SimTrack_pt_10dxy30.SetMarkerColor(kPink+2)
    eff_SimTrack_pt_10dxy30.SetLineWidth(2)

    # Green 
    eff_SimTrack_pt_50dxy500 = TEfficiency(SimTrack_pt_numerator_50dxy500, SimTrack_pt_denominator_50dxy500)
    eff_SimTrack_pt_50dxy500.SetLineColor(kGreen+2)
    eff_SimTrack_pt_50dxy500.SetMarkerStyle(23)
    eff_SimTrack_pt_50dxy500.SetMarkerColor(kGreen+2)
    eff_SimTrack_pt_50dxy500.SetLineWidth(2)


    
    
    # Initial background
    b1 = TH1F("b1","b1",35,0,60)
    b1.GetYaxis().SetRangeUser(0.0,1.06)
    b1.GetYaxis().SetTitleOffset(1.2)
    b1.GetYaxis().SetNdivisions(520)
    b1.GetYaxis().SetTitle("Efficiency")
    b1.GetXaxis().SetTitle(" p_{T} and p_{T}^{Pos} respectively [GeV]")
    b1.SetTitle(" p_{T} and p_{T}^{Pos} Reco. Efficiency, csc_%d, ct %d mm"%(varsh,ctau)+", %d < | d_{xy} | < %d"%(dxy1, dxy2))
    b1.SetStats(0)


    b1.Draw()

    if (dxy1 == 0 and dxy2 == 5):
        eff_pt_position.Draw("same P")
        eff_SimTrack_pt.Draw("same P")

    if (dxy1 == 10 and dxy2 == 30):
        eff_SimTrack_pt_10dxy30.Draw("same P")
        eff_pt_position_10dxy30.Draw("same P")

    if (dxy1 == 50 and dxy2 == 500):
        eff_SimTrack_pt_50dxy500.Draw("same P")
        eff_pt_position_50dxy500.Draw("same P")

    #text1 = TLatex(28,.308,"ME11 - ME2 in %s < |\eta | < %s"%(etamin, etamax))
    #text1.Draw("same")
    
    legend = TLegend(0.5,0.141,0.865,0.35)
    legend.SetFillColor(ROOT.kWhite)
    legend.SetMargin(0.15)
    #legend.SetBorderSize(0)
    #legend.SetFillStyle(0)
    legend.SetHeader(" %s < |\eta^{GP} at ME11 | < %s"%(etamin, etamax))
    if (dxy1 == 0 and dxy2 == 5):
        legend.AddEntry(eff_pt_position,"Reco p_{T}^{Pos} > %d GeV"%mincut, "p")
        legend.AddEntry(eff_SimTrack_pt,"Reco p_{T} > %d GeV"%mincut,"p")
    if (dxy1 == 10 and dxy2 == 30):
        legend.AddEntry(eff_pt_position_10dxy30,"Reco p_{T}^{Pos} > %d GeV"%mincut, "p")
        legend.AddEntry(eff_SimTrack_pt_10dxy30,"Reco p_{T} > %d GeV"%mincut,"p")

    if (dxy1 == 50 and dxy2 == 500):
        legend.AddEntry(eff_pt_position_50dxy500,"Reco p_{T}^{Pos} > %d GeV"%mincut, "p")
        legend.AddEntry(eff_SimTrack_pt_50dxy500,"Reco p_{T} > %d GeV"%mincut,"p")
    legend.Draw("same") 

    kk = k*10
    c1.SaveAs("Efficiency_pt_ptposition_csc_%d"%varsh+"_etamin_%.2s_"%kk+"%dsdxy%d_ct%d_recopT%d.pdf"%(dxy1,dxy2,ctau, mincut))
    c1.SaveAs("Efficiency_pt_ptposition_csc_%d"%varsh+"_etamin_%.2s_"%kk+"%dsdxy%d_ct%d_recopT%d.png"%(dxy1,dxy2,ctau, mincut))


    # Numerator and Denominator for debug only

    

    ####################### Numerator #################################

    b1.GetYaxis().SetTitle("Numerator")
    b1.GetXaxis().SetTitle("p_{T} and p_{T}^{Pos} respectively [GeV] ")
    b1.SetTitle("p_{T} and p_{T}^{Pos} Numerator, ME11- ME2, ct %d mm"%ctau)
    b1.SetStats(0)
    b1.GetYaxis().SetRangeUser(0.0,1000.06)
    b1.Draw()
    pt_position_numerator_0dxy5.Draw("same P")
    SimTrack_pt_numerator_0dxy5.Draw("same P")


    #text1 = TLatex(28,.418,"ME11 - ME2 in %s < |\eta | < %s"%(etamin, etamax))
    #text1.Draw("same")

    legend = TLegend(0.58,.650,0.86,0.88)
    legend.SetFillColor(ROOT.kWhite)
    legend.SetMargin(0.15)
    #legend.SetBorderSize(0)
    #legend.SetFillStyle(0)
    legend.SetHeader(" %s < |\eta^{GP} at ME11 | < %s"%(etamin, etamax))
    legend.AddEntry(pt_position_numerator_0dxy5,"p_{T}^{Pos}", "p")
    legend.AddEntry(SimTrack_pt_numerator_0dxy5,"p_{T}","p")
    legend.Draw("same")

    

    c1.SaveAs("Numerator_pt_ptposition_etamin_%.2s.pdf"%kk)
    c1.SaveAs("Numerator_pt_ptposition_etamin_%.2s.png"%kk)


    ########################### Denominator ###########################

    b1.GetYaxis().SetTitle("Denominator")
    b1.GetXaxis().SetTitle("p_{T} and p_{T}^{Pos} respectively [GeV] ")
    b1.SetTitle("p_{T} and p_{T}^{Pos} Denominator, ME11- ME2, ct %d mm"%ctau)
    b1.SetStats(0)
    b1.GetYaxis().SetRangeUser(0.0,1000.06)
    b1.Draw()

  
    pt_position_denominator_0dxy5.Draw("same P")
    SimTrack_pt_denominator_0dxy5.Draw("same P")


    #text1 = TLatex(0.28,0.818,"%s < |\eta | < %s"%(etamin, etamax))
    #text1.Draw("same")
    
    legend = TLegend(0.58,.650,0.86,0.88)
    legend.SetFillColor(ROOT.kWhite)
    legend.SetMargin(0.15)
    #legend.SetBorderSize(0)
    #legend.SetFillStyle(0)
    legend.SetHeader(" %s < |\eta^{GP} at ME11 | < %s"%(etamin, etamax))
    legend.AddEntry(pt_position_denominator_0dxy5,"p_{T}^{Pos}", "p")
    legend.AddEntry(SimTrack_pt_denominator_0dxy5,"p_{T}","p")
    legend.Draw("same") 

    c1.SaveAs("Denominator_pt_ptposition_etamin_%.2s.pdf"%kk)
    c1.SaveAs("Denominator_pt_ptposition_etamin_%.2s.png"%kk)



for k in pt_slope_inter:
    
    Plotter(k,k+0.2, 0, 5)
    Plotter(k,k+0.2, 10, 30)
    Plotter(k,k+0.2, 50, 500)
