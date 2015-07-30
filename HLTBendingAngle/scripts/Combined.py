from ROOT import *
from Helpers import *


stx = "ME11 - ME2"

def denominator(dxy_min = 0, dxy_max = 5, eta_min = 1.6, eta_max = 1.7):
    return AND(has_csc(), has_csc_second(), dxy(dxy_min, dxy_max), eta_sh_st1(eta_min, eta_max), has_csc12(), same_direction_cut())


def DrawProfileAndScatter_pT(file,dir,xaxis,yaxis,x_bins,y_bins,stat, etamin, etamax):
    
    c1 = TCanvas()
    c1.SetGridx()
    c1.SetGridy()
    c1.SetTickx()
    c1.SetTicky()
    gStyle.SetOptFit(0111)
    gStyle.SetOptStat(0)

        
    gStyle.SetStatY(0.25)
    gStyle.SetStatX(0.90)
    gStyle.SetStatW(0.1729)
    gStyle.SetStatH(0.12)

    f = TFile(file)

    tt10 = f.Get(dir)
    tt11 = f.Get(dir)
    tt12 = f.Get(dir)
    tt13 = f.Get(dir)           
    xBins = int(x_bins[1:-1].split(',')[0])
    xminBin = float(x_bins[1:-1].split(',')[1])
    xmaxBin = float(x_bins[1:-1].split(',')[2])
    yBins = int(y_bins[1:-1].split(',')[0])
    yminBin = float(y_bins[1:-1].split(',')[1])
    ymaxBin = float(y_bins[1:-1].split(',')[2])

    todrawb1 = "%s"%yaxis+":"+"%s>>b1"%xaxis
    todrawb2 = "%s"%yaxis+":"+"%s>>b2"%xaxis
    
    b1 = TH2F("b1","b1",xBins,xminBin,xmaxBin,yBins,yminBin,ymaxBin)
    b1.GetXaxis().SetTitle("p_{T} of Simulated Muon Track [GeV]")
    b1.GetYaxis().SetTitle("|\Delta \phi _{ "+stx+"}| ^{-1}")
    b1.SetTitle("|\Delta \phi _{"+stx+"}| ^{-1} vs p^{SimT}_{T}, ct %d mm"%ctau+" on %.1f < | \eta | < %.1f"%(etamin,etamax))
    b1.SetMaximum(30)
    b1.SetStats(1)

    binxmax = xBins
    tt10.Draw(todrawb1,denominator(0,5,etamin, etamax),"colz")

    printa = 0
    r1 = FitHistoFunction68(b1, 20, 0, 20, 0, 350, printa)
    r1.Fit("pol1", "EMF", "same", 0, binxmax)

    r1.GetXaxis().SetTitle("p_{T} of Simulated Muon Track [GeV]")
    r1.GetYaxis().SetTitle("|\Delta \phi _{"+stx+"}| ^{-1}")
    r1.SetTitle("|\Delta \phi _{"+stx+"}| ^{-1} vs p^{SimT}_{T}, ct %d mm"%ctau+" on %.1f < | \eta | < %.1f"%(etamin,etamax))
    #r1.SetTitle(" 1/ | \Delta \phi_{ 1 - 2} |  vs p^{simT} / cosh(GP.eta), ct 0 mm")
    name = etamin*10         
    r1.Draw("same")
    #r1.Draw()
 
    #text5.Draw("same")

    c1.SaveAs("Scatter_pT_%d"%name+".pdf")
    c1.SaveAs("Scatter_pT_%d"%name+".png")
    r1.Draw()


    c1.SaveAs("Profile_pT_%d"%name+".pdf")
    c1.SaveAs("Profile_pT_%d"%name+".png")




def DrawProfileAndScatter_pT_pos(file,dir,xaxis,yaxis,x_bins,y_bins,stat, etamin, etamax):
    
    c1 = TCanvas()
    c1.SetGridx()
    c1.SetGridy()
    c1.SetTickx()
    c1.SetTicky()
    gStyle.SetOptFit(0111)
    gStyle.SetOptStat(0)

        
    gStyle.SetStatY(0.25)
    gStyle.SetStatX(0.90)
    gStyle.SetStatW(0.1729)
    gStyle.SetStatH(0.12)

    f = TFile(file)

    tt10 = f.Get(dir)
    tt11 = f.Get(dir)
    tt12 = f.Get(dir)
    tt13 = f.Get(dir)           
    xBins = int(x_bins[1:-1].split(',')[0])
    xminBin = float(x_bins[1:-1].split(',')[1])
    xmaxBin = float(x_bins[1:-1].split(',')[2])
    yBins = int(y_bins[1:-1].split(',')[0])
    yminBin = float(y_bins[1:-1].split(',')[1])
    ymaxBin = float(y_bins[1:-1].split(',')[2])

    todrawb1 = "%s"%yaxis+":"+"%s>>b1"%xaxis
    todrawb2 = "%s"%yaxis+":"+"%s>>b2"%xaxis
    
    b1 = TH2F("b1","b1",xBins,xminBin,xmaxBin,yBins,yminBin,ymaxBin)
    b1.GetXaxis().SetTitle("p_{T}^{Pos} of Simulated Muon Track [GeV]")
    b1.GetYaxis().SetTitle("|\Delta \phi _{"+stx+"}| ^{-1}")
    b1.SetTitle("|\Delta \phi _{"+stx+"}| ^{-1} vs p^{Pos}_{T}, ct %d mm"%ctau+" on %.1f < | \eta | < %.1f"%(etamin,etamax))
    b1.SetMaximum(30)
    b1.SetStats(1)

    binxmax = xBins
    tt10.Draw(todrawb1,denominator(0,5,etamin, etamax),"colz")

    printa = 0
    r1 = FitHistoFunction68(b1, 20, 0, 20, 0, 350, printa)
    r1.Fit("pol1", "EMF", "same", 0, binxmax)

    r1.GetXaxis().SetTitle("p_{T}^{Pos} of Simulated Muon Track [GeV]")
    r1.GetYaxis().SetTitle("|\Delta \phi _{"+stx+"}| ^{-1}")
    r1.SetTitle("|\Delta \phi _{"+stx+"}| ^{-1} vs p^{Pos}_{T}, ct %d mm"%ctau+" on %.1f < | \eta | < %.1f"%(etamin,etamax))
    #r1.SetTitle(" 1/ | \Delta \phi_{ 1 - 2} |  vs p^{simT} / cosh(GP.eta), ct 0 mm")
    name = etamin*10         
    r1.Draw("same")
    #r1.Draw()
 
    #text5.Draw("same")

    c1.SaveAs("Scatter_pT_pos_%d"%name+".pdf")
    c1.SaveAs("Scatter_pT_pos_%d"%name+".png")
    r1.Draw()


    c1.SaveAs("Profile_pT_pos_%d"%name+".pdf")
    c1.SaveAs("Profile_pT_pos_%d"%name+".png")



ctau = 0
sta="ME11"
var="Denominator"
tree = "HLTBendingAngle/trk_eff_csc_"+sta


xaxis="pt_SimTrack_csc"
xaxis_pos = "csc_p_over_cosh_eta"

yaxis="1/abs(csc_bending_angle_12)"


x_bins = "(80,0,80)"
y_bins = "(350,0,350)"


DrawProfileAndScatter_pT("../../ct%d.root"%ctau,tree,xaxis,yaxis,x_bins,y_bins,sta, 1.6, 1.8)
#for k in pt_slope_inter:
#    DrawProfileAndScatter_pT("../../ct%d.root"%ctau,tree,xaxis,yaxis,x_bins,y_bins,sta, k, k+0.2)

#for k in pt_pos_slope_inter:
#    DrawProfileAndScatter_pT_pos("../../ct%d.root"%ctau,tree,xaxis_pos,yaxis,x_bins,y_bins,sta, k, k+0.2)

