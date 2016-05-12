from ROOT import *
from Helpers import *

varsh = 12
stx = "ME11 - ME2"
test = 15


def Factorial( n = 1 ):
    if (n <=0): return 1
    x= 1.0
    for b in range (1, int(n+1)):
        x = x*b
    return x

#_____________________________________________________________________________________________________________________________________________________________________________________________________________________________
def denominator(dxy_min = 0, dxy_max = 5, eta_min = 1.6, eta_max = 1.7, minpt=0, maxpt = 500, endcapx = 0, even_chambers_only = 0):
    if even_chambers_only == 0:
        return AND(has_csc(1), has_csc(2), dxy_cut(dxy_min, dxy_max), eta_sh_cut(eta_min, eta_max, 2), has_csc_sh_pairs(12), SimTrack_pt_cut(minpt, maxpt), endcap_csc(endcapx), ME11_only(), odd_chambers() )

    if even_chambers_only == 1:
        return AND(has_csc(1), has_csc(2), dxy_cut(dxy_min, dxy_max), eta_sh_cut(eta_min, eta_max, 2), has_csc_sh_pairs(12), SimTrack_pt_cut(minpt, maxpt), endcap_csc(endcapx), ME11_only(), even_chambers() )

#_____________________________________________________________________________________________________________________________________________________________________________________________________________________________
def Sigma_Direction(file, dir, xaxis, yaxis, x_bins, y_bins, etamin, etamax, minpt, maxpt, endcapx, ctau, even_chambers_only):
       
    c1 = TCanvas()
    c1.SetGridx()
    c1.SetGridy()
    c1.SetTickx()
    c1.SetTicky()
    gStyle.SetOptFit(0111)
    gStyle.SetOptStat(1)
    #c1.SetLogz()

    gStyle.SetStatY(0.9)
    gStyle.SetStatX(0.90)
    gStyle.SetStatW(0.1729)
    gStyle.SetStatH(0.12)

    f = TFile(file)
    tt10 = f.Get(dir) 
    xBins = int(x_bins[1:-1].split(',')[0])
    xminBin = float(x_bins[1:-1].split(',')[1])
    xmaxBin = float(x_bins[1:-1].split(',')[2])
    yBins = int(y_bins[1:-1].split(',')[0])
    yminBin = float(y_bins[1:-1].split(',')[1])
    ymaxBin = float(y_bins[1:-1].split(',')[2])


    legend = TLegend(0.11,0.805,0.38,0.89)
    legend.SetFillColor(ROOT.kWhite)
    legend.SetMargin(0.01)
 
    even_odd = ""
    if even_chambers_only == 0:
        even_odd = "Odd_Chambers"
    if even_chambers_only == 1:
        even_odd = "Even_Chambers"
    legend.AddEntry(0, even_odd+" only", "")
    legend.AddEntry(0, "%d < p_{T}^{Sim} < %d"%(minpt, maxpt), "")
    
    
 
    Direction_Based = TH1D("Direction_Based","Direction_Based",xBins, xminBin ,xmaxBin)
    Direction_Based.SetTitle("(p_{T} Reco - p_{T} Sim) on %.1f < | \eta | < %.1f , using Directions"%(etamin,etamax))
    Direction_Based.SetLineColor(kRed)
    Direction_Based.SetLineWidth(2)
    Direction_Based.GetYaxis().SetTitle("Count")
    Direction_Based.GetXaxis().SetTitle("p_{T} Reco - p_{T} Sim [GeV]")
    Direction_Based.SetStats(1)



    tt10.Draw(yaxis+">>Direction_Based",denominator(0,  500, etamin, etamax, minpt, maxpt, endcapx , even_chambers_only))
    
    legend.Draw("same")
    etacut = etamin*10

    Direction_Based.Draw()
    legend.Draw("same")
    Direction_Based.Fit("landau", "L", "same", xminBin, xmaxBin)
    
 
    
    c1.SaveAs("Sigma_%s_eta%d.pdf"%(even_odd, etacut))


    # Fit B0 to a function like B*exp(-(x-10)) + S*exp(-(x-10)^2)

  


sta="ME11"
tree = "HLTBendingAngle/trk_eff_csc_"+sta
ctau = 0





 

etamin = 2.2
etamax = etamin + 0.2

slope = 0.0
intercept = 0.0
slope_e = 0.0
intercept_e = 0.0


if etamin == 1.6:
    slope = 4.826
    intercept = 12.52
if etamin == 1.8:
    slope= 6.689
    intercept = 14.36
if etamin == 2.0:
    slope = 9.25
    intercept = 11.66
if etamin == 2.2:
    slope = 10.65
    intercept = 13.88

if etamin == 1.6:
    slope_e = 3.888
    intercept_e = 6.554
if etamin == 1.8:
    slope_e= 7.699
    intercept_e = 10.03
if etamin == 2.0:
    slope_e = 9.587
    intercept_e = 9.888
if etamin == 2.2:
    slope_e = 11.26
    intercept_e = 13.9





xaxis= ""  
yaxis_even = "((1/abs(csc_bending_angle_12)  +%f)/%f) - pt_SimTrack"%(intercept_e, slope_e)
yaxis_odd = "((1/abs(csc_bending_angle_12)  +%f)/%f) - pt_SimTrack"%(intercept, slope)

x_bins = "(200,-100,100)"
y_bins= "(210,-10, 200)"


minpt = 10
maxpt = 20


Sigma_Direction("../ct%d.root"%ctau,tree,xaxis,yaxis_even,x_bins,y_bins , etamin, etamax, minpt, maxpt, 0, ctau, 1)
Sigma_Direction("../ct%d.root"%ctau,tree,xaxis,yaxis_odd ,x_bins,y_bins , etamin, etamax, minpt, maxpt, 0, ctau, 0)


