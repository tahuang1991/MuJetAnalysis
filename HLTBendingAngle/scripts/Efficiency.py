from ROOT import *
from array import array
from Helpers import *

#54import sys
#sys.argv.append( '-b' )



ctau = 0
sta="ME11"
var="12"
tree = "HLTBendingAngle/trk_eff_csc_"+sta
f1 = TFile("../../ct%d.root"%ctau)
t1 = f1.Get(tree)
mincut = 20

def denominator(dxy_min = 0, dxy_max = 5, eta_min = 1.6, eta_max = 1.7):
    return AND(has_csc(), has_csc_second(), dxy(dxy_min, dxy_max), eta_sh_st1(eta_min, eta_max), has_csc12(), same_direction_cut())

def numerator_pt_pos(dxy_min = 0, dxy_max = 5, eta_min = 1.6, eta_max = 1.7, sim_pt=10):
    return AND(denominator(dxy_min, dxy_max, eta_min, eta_max), pt_from_povercosh(eta_min, sim_pt))

def numerator_SimTrack_pt(dxy_min = 0, dxy_max = 5, eta_min = 1.6, eta_max = 1.7, sim_pt=10):
    return AND(denominator(dxy_min, dxy_max, eta_min, eta_max), pt_cut(eta_min, sim_pt))


def Plotter(etamin, etamax):
    c1 = TCanvas("a","b",1000,700)
    c1.SetGridx()
    c1.SetGridy()
    c1.SetTickx()
    c1.SetTicky()
    #gROOT.SetBatch(1)


    # In red related to pT
    # In blue related to pt position
    

    # Denominator SimTrack pt 0< dxy < 5
    SimTrack_pt_denominator_0dxy5 = TH1F("SimTrack_pt_denominator_0dxy5","SimTrack_pt_denominator_0dxy5", 60, 0, 60) #BINM,array.array('d', binLow))
    t1.Draw("pt_SimTrack_csc >> SimTrack_pt_denominator_0dxy5",denominator(0,5,etamin,etamax))

    
    SimTrack_pt_denominator_0dxy5.SetLineColor(kRed)
    SimTrack_pt_denominator_0dxy5.SetMarkerStyle(24)
    SimTrack_pt_denominator_0dxy5.SetMarkerColor(kRed)

    # Define pt_position as SimTrack total momentum over ( Global Position eta() measured at station ME11) 
    # Denominator for 0< dx < 5 on pt pos    
    pt_position_denominator_0dxy5 = TH1F("pt_position_denominator_0dxy5","pt_position_denominator_0dxy5", 60, 0, 60) #BINM,array.array('d', binLow))
    t1.Draw("csc_p_over_cosh_eta >> pt_position_denominator_0dxy5",denominator(0,5,etamin,etamax))


    pt_position_denominator_0dxy5.SetLineColor(kBlue)
    pt_position_denominator_0dxy5.SetLineWidth(2)
    pt_position_denominator_0dxy5.SetMarkerStyle(20)
    pt_position_denominator_0dxy5.SetMarkerColor(kBlue)
    pt_position_denominator_0dxy5.SetMarkerSize(1)
    
    # Numerator SimTrack pt
    SimTrack_pt_numerator_0dxy5 = TH1F("SimTrack_pt_numerator_0dxy5","SimTrack_pt_numerator_0dxy5", 60, 0, 60)#BINM,array.array('d', binLow))
    t1.Draw("pt_SimTrack_csc>> SimTrack_pt_numerator_0dxy5",numerator_SimTrack_pt(0, 5, etamin, etamax, mincut))


    SimTrack_pt_numerator_0dxy5.SetLineColor(kRed)
    SimTrack_pt_numerator_0dxy5.SetMarkerStyle(24)
    SimTrack_pt_numerator_0dxy5.SetMarkerColor(kRed)



    # Numerator for dx < 5 on pt pos
    pt_position_numerator_0dxy5 = TH1F("pt_position_numerator_0dxy5","pt_position_numerator_0dxy5", 60, 0, 60)#BINM,array.array('d', binLow))
    t1.Draw("csc_p_over_cosh_eta>> pt_position_numerator_0dxy5",numerator_pt_pos(0,5,etamin,etamax,mincut))


    pt_position_numerator_0dxy5.SetLineColor(kBlue)
    pt_position_numerator_0dxy5.SetLineWidth(2)
    pt_position_numerator_0dxy5.SetMarkerStyle(20)
    pt_position_numerator_0dxy5.SetMarkerColor(kBlue)
    pt_position_numerator_0dxy5.SetMarkerSize(1)


    # Define the efficiency objets 
    eff_pt_position = TEfficiency(pt_position_numerator_0dxy5, pt_position_denominator_0dxy5)
    eff_pt_position.SetLineColor(kBlue)
    eff_pt_position.SetLineWidth(2)
    eff_pt_position.SetMarkerStyle(20)
    eff_pt_position.SetMarkerColor(kBlue)
    eff_pt_position.SetMarkerSize(1)

    eff_SimTrack_pt = TEfficiency(SimTrack_pt_numerator_0dxy5, SimTrack_pt_denominator_0dxy5)
    eff_SimTrack_pt.SetLineColor(kRed)
    eff_SimTrack_pt.SetMarkerStyle(24)
    eff_SimTrack_pt.SetMarkerColor(kRed)



    
    # Initial background
    b1 = TH1F("b1","b1",35,0,60)
    b1.GetYaxis().SetRangeUser(0.0,1.06)
    b1.GetYaxis().SetTitleOffset(1.2)
    b1.GetYaxis().SetNdivisions(520)
    b1.GetYaxis().SetTitle("Efficiency")
    b1.GetXaxis().SetTitle(" p_{T} and p_{T}^{Pos} respectively [GeV]")
    b1.SetTitle(" p_{T} and p_{T}^{Pos} Reco. Efficiency, ME11- ME2, ct %d mm"%ctau)
    b1.SetStats(0)


    b1.Draw()
    eff_pt_position.Draw("same P")
    eff_SimTrack_pt.Draw("same P")

    #text1 = TLatex(28,.308,"ME11 - ME2 in %s < |\eta | < %s"%(etamin, etamax))
    #text1.Draw("same")
    
    legend = TLegend(0.5,0.141,0.865,0.35)
    legend.SetFillColor(ROOT.kWhite)
    legend.SetMargin(0.15)
    #legend.SetBorderSize(0)
    #legend.SetFillStyle(0)
    legend.SetHeader(" %s < |\eta^{GP} at ME11 | < %s"%(etamin, etamax))
    legend.AddEntry(eff_pt_position,"Reco p_{T}^{Pos} > 20 GeV", "p")
    legend.AddEntry(eff_SimTrack_pt,"Reco p_{T} > 20 GeV","p")
    legend.Draw("same") 

    kk = k*10
    c1.SaveAs("Efficiency_pt_ptposition_etamin_%.2s.pdf"%kk)
    c1.SaveAs("Efficiency_pt_ptposition_etamin_%.2s.png"%kk)



    

    ####################### Numerator #################################

    b1.GetYaxis().SetTitle("Numerator")
    b1.GetXaxis().SetTitle("p_{T} and p_{T}^{Pos} respectively [GeV] ")
    b1.SetTitle("p_{T} and p_{T}^{Pos} Numerator, ME11- ME2, ct %d mm"%ctau)
    b1.SetStats(0)
    b1.GetYaxis().SetRangeUser(0.0,400.06)
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
    b1.GetYaxis().SetRangeUser(0.0,400.06)
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
    
    Plotter(k,k+0.2)
