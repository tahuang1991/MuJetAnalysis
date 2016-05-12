from ROOT import *
from Helpers import *
from math import *
import array


BINM=22
binLow = [0,1,2,3,4,5,6,7,8,9,10,12,14,16,18,20,24,28,32,36,42,50,60]
test_fit = 30

#_____________________________________________________________________________________________________________________________________________________________________________________________________________________________
def denominator(dxy_min = 0, dxy_max = 5, eta_min = 1.6, eta_max = 1.7, minpt=0, maxpt = 500, stx=1, parity_case = 0):

        return AND(has_csc(1), has_csc(2), dxy_cut(dxy_min, dxy_max), eta_sh_cut(eta_min, eta_max, 2), has_csc_sh_pairs(12), SimTrack_pt_cut(minpt, maxpt), ME1X_only(stx), parity_csc(parity_case))


#_____________________________________________________________________________________________________________________________________________________________________________________________________________________________
def numerator_Position(dxy_min = 0, dxy_max = 5, eta_min = 1.6, eta_max = 1.7, minpt=0, maxpt = 500, stationx=0, parity_case=0, minptcut=0):

    return AND(denominator(dxy_min, dxy_max, eta_min, eta_max, minpt, maxpt, stationx, parity_case), pT_from_Positions(eta_min, stationx, parity_case, minptcut))


#_____________________________________________________________________________________________________________________________________________________________________________________________________________________________
def DeltaX23v12_Scatter(file, dir, xaxis, yaxis, x_bins, y_bins, etamin, etamax, minpt, maxpt, ctau, stationx, parity_case):
    
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
    
    xBins = int(x_bins[1:-1].split(',')[0])
    xminBin = float(x_bins[1:-1].split(',')[1])
    xmaxBin = float(x_bins[1:-1].split(',')[2])
    yBins = int(y_bins[1:-1].split(',')[0])
    yminBin = float(y_bins[1:-1].split(',')[1])
    ymaxBin = float(y_bins[1:-1].split(',')[2])

    todrawb1 = "%s"%yaxis+":"+"%s>>b1"%xaxis
    b1 = TH2F("b1","b1",xBins,xminBin,xmaxBin,yBins,yminBin,ymaxBin)
    b1.GetXaxis().SetTitle("|\Delta X_{12}|")
    b1.GetYaxis().SetTitle("|\Delta X_{23}|")
    b1.SetTitle("|\Delta X_{23}| vs |\Delta X_{12}|, ct %d mm"%ctau+" on %.1f < | \eta | < %.1f"%(etamin,etamax))
    b1.SetStats(1)    
    tt10.Draw(todrawb1,denominator(0,500,etamin, etamax, minpt, maxpt, stationx, parity_case ),"colz")



    even_odd = ""
    if parity_case == 0:
        even_odd = "Odd_Even_Even"
    if parity_case == 1:
        even_odd = "Odd_Odd_Odd"
    if parity_case == 2:
        even_odd = "Even_Even_Even"
    if parity_case == 3:
        even_odd = "Even_Odd_Odd"


    stationxx = ""
    if stationx == 1:
        stationxx = "ME11"
    if stationx == 2:
        stationxx = "ME12"
    if stationx == 3:
        stationxx = "ME13"

        
    legend = TLegend(0.11,0.805,0.38,0.89)
    legend.SetFillColor(ROOT.kWhite)
    legend.SetMargin(0.01)

    legend.AddEntry(0, stationxx+"_"+even_odd, "")
       
    r1 = FitHistoFunction68(b1, xBins,xminBin,xmaxBin, yBins,yminBin,ymaxBin, 0)    
    r1.Fit("pol1", "EFM ", "same", 0, xmaxBin)
    #r1.Fit("fxx")
    r1.GetXaxis().SetTitle("|\Delta Y_{12}|")
    r1.GetYaxis().SetTitle("|\Delta Y_{23}|")
    r1.SetTitle("|\Delta Y_{23}| vs |\Delta Y_{12}|, ct %d mm"%ctau+" on %.1f < | \eta | < %.1f"%(etamin,etamax))

    name = etamin*10
    b1.Draw("colz")
    r1.Draw("same")
    legend.Draw("same")
    c1.SaveAs("%s_Preliminary_Scatter_eta%d_%s.pdf"%(stationxx, name, even_odd))
       
    r1.Draw()
    legend.Draw("same")
    c1.SaveAs("%s_Preliminary_Profile_eta%d_%s.pdf"%(stationxx, name, even_odd))


#_____________________________________________________________________________________________________________________________________________________________________________________________________________________________
def DeltaY_Scatter(file, dir, xaxis, yaxis, x_bins, y_bins, etamin, etamax, minpt, maxpt, ctau, stationx, parity_case):
                  
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
    
    xBins = int(x_bins[1:-1].split(',')[0])
    xminBin = float(x_bins[1:-1].split(',')[1])
    xmaxBin = float(x_bins[1:-1].split(',')[2])
    yBins = int(y_bins[1:-1].split(',')[0])
    yminBin = float(y_bins[1:-1].split(',')[1])
    ymaxBin = float(y_bins[1:-1].split(',')[2])

    todrawb1 = "%s"%yaxis+":"+"%s>>b1"%xaxis
    b1 = TH2F("b1","b1",xBins,xminBin,xmaxBin,yBins,yminBin,ymaxBin)
    b1.GetXaxis().SetTitle(" p_{T} of Simulated Muon Track [GeV]")
    b1.GetYaxis().SetTitle("| \Delta \Delta Y|^{-1}")
    b1.SetTitle("| \Delta \Delta Y|^{-1} vs p_{T}^{SimT}, ct %d mm"%ctau+" on %.1f < | \eta | < %.1f"%(etamin,etamax))
    b1.SetStats(1)    
    tt10.Draw(todrawb1,denominator(0,500,etamin, etamax, minpt, maxpt, stationx, parity_case ),"colz")

  
    even_odd = ""
    if parity_case == 0:
        even_odd = "Odd_Even_Even"
    if parity_case == 1:
        even_odd = "Odd_Odd_Odd"
    if parity_case == 2:
        even_odd = "Even_Even_Even"
    if parity_case == 3:
        even_odd = "Even_Odd_Odd"


    stationxx = ""
    if stationx == 1:
        stationxx = "ME11"
    if stationx == 2:
        stationxx = "ME12"
    if stationx == 3:
        stationxx = "ME13"

        
    legend = TLegend(0.11,0.805,0.38,0.89)
    legend.SetFillColor(ROOT.kWhite)
    legend.SetMargin(0.01)
    legend.AddEntry(0, stationxx+"_"+even_odd, "")
       
    r1 = FitHistoFunction68(b1, xBins,xminBin,xmaxBin, yBins,yminBin,ymaxBin, 0)    
    r1.Fit("pol1", "F LL", "same", 3, 30)
    r1.GetXaxis().SetTitle(" p_{T} of Simulated Muon Track [GeV]")
    r1.GetYaxis().SetTitle("| \Delta \Delta Y|^{-1}")
    r1.SetTitle("| \Delta \Delta Y|^{-1} vs p_{T}^{SimT}, ct %d mm"%ctau+" on %.1f < | \eta | < %.1f"%(etamin,etamax))

    name = etamin*10
    b1.Draw("colz")
    r1.Draw("same")
    legend.Draw("same")
    c1.SaveAs("%s_Scatter_eta%d_%s.pdf"%(stationxx, name, even_odd))
       
    r1.Draw()
    legend.Draw("same")
    c1.SaveAs("%s_Profile_eta%d_%s.pdf"%(stationxx, name, even_odd))







#_____________________________________________________________________________________________________________________________________________________________________________________________________________________________
def DeltaY_Efficiency(file, dir, etamin, etamax, ctau, stationx, parity_case,  minptcut):



    c1 = TCanvas("a","b",1000,700)
    c1.SetGridx()
    c1.SetGridy()
    c1.SetTickx()
    c1.SetTicky()

    f = TFile(file)
    t1 = f.Get(dir)


    
    SimTrack_pt_denominator_0dxy5 = TH1F("SimTrack_pt_denominator_0dxy5","SimTrack_pt_denominator_0dxy5", BINM,array.array('d', binLow))
    t1.Draw("pt_SimTrack >> SimTrack_pt_denominator_0dxy5",denominator(0,5,etamin, etamax, 0, 500, stationx, parity_case ))
    SimTrack_pt_denominator_0dxy5.SetLineColor(kRed)
    SimTrack_pt_denominator_0dxy5.SetMarkerStyle(24)
    SimTrack_pt_denominator_0dxy5.SetMarkerColor(kRed)


    # Denominator SimTrack pt 10< dxy < 30
    SimTrack_pt_denominator_5dxy30 = TH1F("SimTrack_pt_denominator_5dxy30","SimTrack_pt_denominator_5dxy30", BINM,array.array('d', binLow))
    t1.Draw("pt_SimTrack >> SimTrack_pt_denominator_10dxy30",denominator(5,30,etamin, etamax, 0, 500, stationx, parity_case ))
    SimTrack_pt_denominator_5dxy30.SetLineColor(kPink+2)
    SimTrack_pt_denominator_5dxy30.SetLineWidth(2)
    SimTrack_pt_denominator_5dxy30.SetMarkerStyle(20)
    SimTrack_pt_denominator_5dxy30.SetMarkerColor(kPink+2)
    SimTrack_pt_denominator_5dxy30.SetMarkerSize(1)
    

    # Denominator SimTrack pt 50< dxy < 500
    SimTrack_pt_denominator_30dxy500 = TH1F("SimTrack_pt_denominator_30dxy500","SimTrack_pt_denominator_30dxy500", BINM,array.array('d', binLow))
    t1.Draw("pt_SimTrack >> SimTrack_pt_denominator_50dxy500",denominator(30,500,etamin, etamax, 0, 500, stationx, parity_case ))
    SimTrack_pt_denominator_30dxy500.SetLineColor(kGreen+2)
    SimTrack_pt_denominator_30dxy500.SetLineWidth(2)
    SimTrack_pt_denominator_30dxy500.SetMarkerStyle(20)
    SimTrack_pt_denominator_30dxy500.SetMarkerColor(kGreen+2)
    SimTrack_pt_denominator_30dxy500.SetMarkerSize(1)



               
    # Numerator SimTrack pt
    SimTrack_pt_numerator_0dxy5 = TH1F("SimTrack_pt_numerator_0dxy5","SimTrack_pt_numerator_0dxy5", BINM,array.array('d', binLow))
    t1.Draw("pt_SimTrack>> SimTrack_pt_numerator_0dxy5",numerator_Position(0, 5, etamin, etamax, 0, 500, stationx, parity_case, minptcut))
    SimTrack_pt_numerator_0dxy5.SetLineColor(kRed)
    SimTrack_pt_numerator_0dxy5.SetMarkerStyle(24)
    SimTrack_pt_numerator_0dxy5.SetMarkerColor(kRed)


    #print numerator_SimTrack_pt(0, 5, etamin, etamax, mincut, varsh)
    # Numerator SimTrack pt # 10 dx 30
    SimTrack_pt_numerator_5dxy30 = TH1F("SimTrack_pt_numerator_5dxy30","SimTrack_pt_numerator_5dxy30", BINM,array.array('d', binLow))
    t1.Draw("pt_SimTrack>> SimTrack_pt_numerator_10dxy30",numerator_Position(5, 30, etamin, etamax, 0, 500, stationx, parity_case, minptcut))
    SimTrack_pt_numerator_5dxy30.SetLineColor(kPink+2)
    SimTrack_pt_numerator_5dxy30.SetLineWidth(2)
    SimTrack_pt_numerator_5dxy30.SetMarkerStyle(20)
    SimTrack_pt_numerator_5dxy30.SetMarkerColor(kPink+2)
    SimTrack_pt_numerator_5dxy30.SetMarkerSize(1)

    
    # Numerator SimTrack pt #50 dx 500
    SimTrack_pt_numerator_30dxy500 = TH1F("SimTrack_pt_numerator_30dxy500","SimTrack_pt_numerator_30dxy500", BINM,array.array('d', binLow))
    t1.Draw("pt_SimTrack>> SimTrack_pt_numerator_50dxy500",numerator_Position(30, 500, etamin, etamax, 0, 500, stationx, parity_case, minptcut))
    SimTrack_pt_numerator_30dxy500.SetLineColor(kGreen+2)
    SimTrack_pt_numerator_30dxy500.SetLineWidth(2)
    SimTrack_pt_numerator_30dxy500.SetMarkerStyle(20)
    SimTrack_pt_numerator_30dxy500.SetMarkerColor(kGreen+2)
    SimTrack_pt_numerator_30dxy500.SetMarkerSize(1)
    


    # Red 
    eff_SimTrack_pt = TEfficiency(SimTrack_pt_numerator_0dxy5, SimTrack_pt_denominator_0dxy5)
    eff_SimTrack_pt.SetLineColor(kRed)
    eff_SimTrack_pt.SetMarkerStyle(22)
    eff_SimTrack_pt.SetMarkerColor(kRed)
    eff_SimTrack_pt.SetLineWidth(2)

    # Magenta 
    eff_SimTrack_pt_5dxy30 = TEfficiency(SimTrack_pt_numerator_5dxy30, SimTrack_pt_denominator_5dxy30)
    eff_SimTrack_pt_5dxy30.SetLineColor(kPink+2)
    eff_SimTrack_pt_5dxy30.SetMarkerStyle(21)
    eff_SimTrack_pt_5dxy30.SetMarkerColor(kPink+2)
    eff_SimTrack_pt_5dxy30.SetLineWidth(2)

    # Green 
    eff_SimTrack_pt_30dxy500 = TEfficiency(SimTrack_pt_numerator_30dxy500, SimTrack_pt_denominator_30dxy500)
    eff_SimTrack_pt_30dxy500.SetLineColor(kGreen+2)
    eff_SimTrack_pt_30dxy500.SetMarkerStyle(23)
    eff_SimTrack_pt_30dxy500.SetMarkerColor(kGreen+2)
    eff_SimTrack_pt_30dxy500.SetLineWidth(2)


    b1 = TH1F("b1","b1",35,0,60)
    b1.GetYaxis().SetRangeUser(0.0,1.06)
    b1.GetYaxis().SetTitleOffset(1.2)
    b1.GetYaxis().SetNdivisions(520)
    b1.GetYaxis().SetTitle("Efficiency")
    b1.GetXaxis().SetTitle(" p_{T} of Simulated Muon Track [GeV]")
    b1.SetTitle(" p_{T} Reco. Efficiency, ct %d mm"%(ctau)+", %.1f < | \eta_{gp} | < %.1f, using \Delta \Delta Y "%(etamin,etamax))
    b1.SetStats(0)


    b1.Draw()
    eff_SimTrack_pt.Draw("same P")
    eff_SimTrack_pt_5dxy30.Draw("same P")
    eff_SimTrack_pt_30dxy500.Draw("same P")


    legend = TLegend(0.5,0.10, 0.9, 0.35)
    legend.SetFillColor(ROOT.kWhite)
    legend.SetMargin(0.19)
    legend.SetHeader(" Reco. p_{T} > %d"%minptcut+" GeV, and: ")
    legend.AddEntry(eff_SimTrack_pt,"0 < | d_{xy} |  < 5" , "p")
    legend.AddEntry(eff_SimTrack_pt_5dxy30,"5 < | d_{xy} |  < 30","p")
    legend.AddEntry(eff_SimTrack_pt_30dxy500,"30 < | d_{xy} |  < 500","p")
    legend.Draw("same")
    



  
    even_odd = ""
    if parity_case == 0:
        even_odd = "Odd_Even_Even"
    if parity_case == 1:
        even_odd = "Odd_Odd_Odd"
    if parity_case == 2:
        even_odd = "Even_Even_Even"
    if parity_case == 3:
        even_odd = "Even_Odd_Odd"


    stationxx = ""
    if stationx == 1:
        stationxx = "ME11"
    if stationx == 2:
        stationxx = "ME12"
    if stationx == 3:
        stationxx = "ME13"

        
    legend2 = TLegend(0.5,0.35, 0.9, 0.405)
    legend2.SetFillColor(ROOT.kWhite)
    legend2.SetMargin(0.019)
    legend2.AddEntry(0, stationxx+"_"+even_odd, "")

    legend2.Draw("same")
    kk = etamin*10
    c1.SaveAs("%s_Reco_Eff_eta%d_pt%d_ct%d_%s.pdf"%(stationxx, kk, minptcut, ctau, even_odd)) 




ctau = 0
sta="ME11"
tree = "HLTBendingAngle/trk_eff_csc_"+sta

minptcut = 10


x_bins = "(480,0,120)"
y_bins = "(480,0,120)"
yaxis = "abs(delta_x_gp_23)"
xaxis = "abs(delta_x_gp_12)"
# Needed to get the ratio DeltaY23 to DeltaY12 but here using Delta X as it doesn't shift with pT


#DeltaX23v12_Scatter("../ct%d.root"%ctau,tree,xaxis,yaxis,x_bins,y_bins, 0.8, 1.6, 10, 500 , ctau, 2, 0)
#DeltaX23v12_Scatter("../ct%d.root"%ctau,tree,xaxis,yaxis,x_bins,y_bins, 0.8, 1.6, 10, 500 , ctau, 2, 1)
#DeltaX23v12_Scatter("../ct%d.root"%ctau,tree,xaxis,yaxis,x_bins,y_bins, 0.8, 1.6, 10, 500 , ctau, 2, 2)
#DeltaX23v12_Scatter("../ct%d.root"%ctau,tree,xaxis,yaxis,x_bins,y_bins, 0.8, 1.6, 10, 500 , ctau, 2, 3)





st =1

for x in range (0, 4):
        slopp = 0.0

        if st ==1:
                if x == 0:
                        slopp = 0.649
                if x == 1:
                        slopp = 0.3533
                if x == 2:
                        slopp = 0.5724
                if x == 3:
                        slopp = 0.3175
        if st ==2:
                if x == 0:
                        slopp = 1.279
                if x == 1:
                        slopp = 0.6357
                if x == 2:
                        slopp = 1.001
                if x == 3:
                        slopp = 0.5252

        x_bins = "(400,0,80)"
  

        xaxis = "pt_SimTrack"
        yaxis = "1/abs(abs(delta_y_gp_23) - %f*abs(delta_y_gp_12) )"%slopp

        y_bins = "(1200,0,10)"
        #DeltaY_Scatter("../ct%d.root"%ctau,tree,xaxis,yaxis,x_bins,y_bins, 1.6, 1.8, 0, 500 , ctau, st, x)
        y_bins = "(1200,0,20)"
        #DeltaY_Scatter("../ct%d.root"%ctau,tree,xaxis,yaxis,x_bins,y_bins, 1.8, 2.0, 0, 500 , ctau, st, x)
        y_bins = "(1200,0,40)"
        #DeltaY_Scatter("../ct%d.root"%ctau,tree,xaxis,yaxis,x_bins,y_bins, 2.0, 2.2, 0, 500 , ctau, st, x)
        y_bins = "(1200,0,60)"
        #DeltaY_Scatter("../ct%d.root"%ctau,tree,xaxis,yaxis,x_bins,y_bins, 2.2, 2.4, 0, 500 , ctau, st, x)





        DeltaY_Efficiency("../ct%d.root"%ctau,tree, 1.6, 1.8, ctau, st, x, 10)
        DeltaY_Efficiency("../ct%d.root"%ctau,tree, 1.8, 2.0, ctau, st, x, 10)
        DeltaY_Efficiency("../ct%d.root"%ctau,tree, 2.0, 2.2, ctau, st, x, 10)
        DeltaY_Efficiency("../ct%d.root"%ctau,tree, 2.2, 2.4, ctau, st, x, 10)

     


'''

# This is for 1.0 - 1.6
DeltaY_Scatter("../ct%d.root"%ctau,tree,xaxis,yaxis_even,x_bins,y_bins, 1.0, 1.2, 0, 500 , 0, ctau, 1)
DeltaY_Scatter("../ct%d.root"%ctau,tree,xaxis,yaxis_even,x_bins,y_bins, 1.0, 1.2, 0, 500 , 0, ctau, 0)
DeltaY_Scatter("../ct%d.root"%ctau,tree,xaxis,yaxis_even,x_bins,y_bins, 1.2, 1.4, 0, 500 , 0, ctau, 1)
DeltaY_Scatter("../ct%d.root"%ctau,tree,xaxis,yaxis_even,x_bins,y_bins, 1.2, 1.4, 0, 500 , 0, ctau, 0)
DeltaY_Scatter("../ct%d.root"%ctau,tree,xaxis,yaxis_even,x_bins,y_bins, 1.4, 1.6, 0, 500 , 0, ctau, 1)
DeltaY_Scatter("../ct%d.root"%ctau,tree,xaxis,yaxis_even,x_bins,y_bins, 1.4, 1.6, 0, 500 , 0, ctau, 0)

DeltaY_Efficiency("../ct%d.root"%ctau,tree, 1.2, 1.4, 0, minptcut, ctau, 0)
DeltaY_Efficiency("../ct%d.root"%ctau,tree, 1.2, 1.4, 0, minptcut, ctau, 1)
DeltaY_Efficiency("../ct%d.root"%ctau,tree, 1.4, 1.6, 0, minptcut, ctau, 0)
DeltaY_Efficiency("../ct%d.root"%ctau,tree, 1.4, 1.6, 0, minptcut, ctau, 1)

'''
