from ROOT import *
from Helpers import *


#_____________________________________________________________________________________________________________________________________________________________________________________________________________________________
def denominator(dxy_min = 0, dxy_max = 5, eta_min = 1.6, eta_max = 1.7, minpt=0, maxpt = 500, stx=1, parity_case = 0):

        return AND(has_csc(1), has_csc(2), dxy_cut(dxy_min, dxy_max), eta_sh_cut(eta_min, eta_max, 2), has_csc_sh_pairs(12), SimTrack_pt_cut(minpt, maxpt), ME1X_only(stx), parity_csc(parity_case))


#_____________________________________________________________________________________________________________________________________________________________________________________________________________________________
def Sigma_Position(file, dir, xaxis, x_bins, etamin, etamax, minpt, maxpt, ctau, stationx, parity_case):
       
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
 


    legend = TLegend(0.11,0.805,0.38,0.89)
    legend.SetFillColor(kWhite)
    legend.SetMargin(0.01)
 

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

    legend.AddEntry(0, stationxx+"_"+even_odd, "")
    legend.AddEntry(0, "%d < p_{T}^{Sim} < %d"%(minpt, maxpt), "")
    
    
        
 
    Position_Based = TH1D("Position_Based","Position_Based",xBins, xminBin ,xmaxBin)
    Position_Based.SetTitle("(p_{T}Reco - p_{T} Sim) on %.1f < | \eta | < %.1f , using \Delta \Delta Y"%(etamin,etamax))
    Position_Based.SetLineColor(kRed)
    Position_Based.SetLineWidth(2)
    Position_Based.GetYaxis().SetTitle("Count")
    Position_Based.GetXaxis().SetTitle("1/(p_{T} Reco) - 1/(p_{T} Sim) [GeV^{-1}]")
    Position_Based.SetStats(1)


    tt10.Draw(xaxis+">>Position_Based",denominator(0,  500, etamin, etamax, minpt, maxpt, stationx, parity_case))
    
    legend.Draw("same")
    etacut = etamin*10

    Position_Based.Draw()
    legend.Draw("same")
    Position_Based.Fit("gaus", "L", "same", -10, 10)
    

    c1.SaveAs("%s_Sigma_%s_eta%d.pdf"%(stationxx, even_odd, etacut))


    # Fit B0 to a function like B*exp(-(x-10)) + S*exp(-(x-10)^2)

  


sta="ME11"
tree = "HLTBendingAngle/trk_eff_csc_"+sta
ctau = 0


stx = 1
for parity_case in range (0, 4):

        for etamin in (1.6, 1.8, 2.0, 2.2):
                if parity_case ==0 :
                    prop = 0.649
                    if etamin == 1.6:
                        slope = 0.05517
                        intercept = 0.08284
                    if etamin == 1.8:
                        slope= 0.08192
                        intercept = 0.1122
                    if etamin == 2.0:
                        slope = 0.1682
                        intercept = 0.2233
                    if etamin == 2.2:
                        slope = 0.5304
                        intercept = 1.061

                if parity_case ==1 :
                    prop = 0.3533
                    if etamin == 1.6:
                        slope = 0.1121
                        intercept = 0.2312
                    if etamin == 1.8:
                        slope= 0.1593
                        intercept = 0.2771
                    if etamin == 2.0:
                        slope = 0.3293
                        intercept = 0.5923
                    if etamin == 2.2:
                        slope = 0.8649
                        intercept = 1.429

                if parity_case ==2 :
                    prop = 0.5724
                    if etamin == 1.6:
                        slope = 0.04756
                        intercept = 0.06255
                    if etamin == 1.8:
                        slope= 0.08478
                        intercept = 0.1368
                    if etamin == 2.0:
                        slope = 0.1608
                        intercept = 0.1612
                    if etamin == 2.2:
                        slope = 0.4944
                        intercept = 1.043
                        
                if parity_case ==3 :
                    prop = 0.3175
                    if etamin == 1.6:
                        slope = 0.1026
                        intercept = 0.1795
                    if etamin == 1.8:
                        slope= 0.1495
                        intercept = 0.2236
                    if etamin == 2.0:
                        slope = 0.3166
                        intercept = 0.5733
                    if etamin == 2.2:
                        slope = 0.8348
                        intercept = 1.468

                print "case: ",parity_case
                print "etamin: ",etamin
                xaxis = " (( 1/abs(abs(delta_y_gp_23) - %f*abs(delta_y_gp_12) )  + %f )/%f )  - (pt_SimTrack)"%(prop, intercept, slope)
                
                x_bins = "(200,-50,50)"



                minpt = 10
                maxpt = 20
                etamax = etamin + 0.2

                Sigma_Position("/home/taohuang/work/CMSSW_7_4_4/src/MuJetAnalysis/HLTBendingAngle/test/ct%d.root"%ctau,tree,xaxis,x_bins, etamin, etamax, minpt, maxpt, ctau, stx, parity_case)


                


