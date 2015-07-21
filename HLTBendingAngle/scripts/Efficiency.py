import ROOT
from array import array
from Helpers import *
c1 = ROOT.TCanvas("a","b",1000,700)
c1.SetGridx()
c1.SetGridy()
c1.SetTickx()
c1.SetTicky()

BINM=15
binLow = [5.5,7.5,9.5,11.5,13.5,15.4,17.6,19.5,20.5,22.5,26.5,30.5,35,41,50,60]


low = "1.6"
hig = "1.8"
ptmin = "20"

sta="ME11"
var="12"
tree = "HLTBendingAngle/trk_eff_csc_"+sta


den = "nlayerscsc>4 && abs(dxy_csc)<5 && has_csc_"+var+">0 && abs(csc_gp_eta)>"+low+" && abs(csc_gp_eta)<"+hig+" && Lxy_csc >0"# && pzvz_csc>0 && calculated_p_csc_10_15==0"
den2 = "nlayerscsc>4 && abs(dxy_csc)>10 && abs(dxy_csc)<30 && has_csc_"+var+">0 && abs(csc_gp_eta)>"+low+" && abs(csc_gp_eta)<"+hig+" && Lxy_csc <0 && pzvz_csc<0 && calculated_p_csc_10_15==0"
den4 = "nlayerscsc>4 && abs(dxy_csc)>30 && abs(dxy_csc)<500 && has_csc_"+var+">0 && abs(csc_gp_eta)>"+low+" && abs(csc_gp_eta)<"+hig+" && Lxy_csc <0 && pzvz_csc<0 && calculated_p_csc_10_15==0"

def new_den(dxy_min = 0, dxy_max = 5, eta_min = 1.6, eta_max = 1.7):
    return AND(has_csc(), dxy(dxy_min, dxy_max), eta_sh_st1(eta_min, eta_max), same_direction_cut(), has_reco_pt())
def new_num(dxy_min = 0, dxy_max = 5, eta_min = 1.6, eta_max = 1.7, sim_pt=10):
    return AND(new_den(dxy_min, dxy_max, eta_min, eta_max), p_from_povercosh(eta_min, sim_pt))

fabs = ""

if(sta=="ME11"):
    if(low=="1.5"):
        fabs = " && (1/abs(csc_bending_angle_"+var+") + 3.69 ) / 1.01 > 20"
        name = "15"


    if(low=="1.6"):
        name = "16"
        fabs = " && ((1/abs(csc_bending_angle_"+var+") + 4.283) /3.127) >"+ptmin #(1.3/abs(csc_bending_angle)-1.933)>20"

        
        
    if(low=="1.7"):
        fabs = " && (1/abs(csc_bending_angle_"+var+") + 7.131 ) /1.34 > 20"
        name = "17"


        
    if(low=="1.8"):
        name = "18"
        fabs = " && (1/abs(csc_bending_angle_"+var+") + 6.566) / 5.056>"+ptmin


        
    if(low=="1.9"):
        fabs = " && (1/abs(csc_bending_angle_"+var+") + 7.424) / 1.439 > 20"
        name = "19"

        
    if(low=="2.0"):
        #fabs = " && (1/abs(csc_bending_angle_"+var+") + 3.141 ) / 1.165 > 20"
        name = "20"
        fabs  = " && (1/abs(csc_bending_angle_"+var+") +3.792) / 5.368> "+ptmin


        
    if(low=="2.1"):
        fabs = " && (1/abs(csc_bending_angle_"+var+")+5.511 ) / 1.156 > 20"
        name = "21"


        
    if(low=="2.2"):
        name = "22"
        fabs = " && (1/abs(csc_bending_angle_"+var+") -0.3263 ) /4.61> "+ptmin


        
    if(low=="2.3"):
        fabs = " && (1/abs(csc_bending_angle_"+var+") - 1.342 ) / 0.6751 > 20"
        name = "23"
        
    if(low=="2.4"):
        fabs = " && (1/abs(csc_bending_angle_"+var+") +1.013 ) / 0.687 > 20"
        name = "24"



#fabs = " && calculated_pT_csc > 20"
num = den+fabs
num2 = den2+fabs
num4 = den4+fabs




f1 = ROOT.TFile("../../ct0.root")
t1 = f1.Get(tree)
e1 = ROOT.TH1F("e1","e1",BINM,array('d', binLow))

t1.Draw("p_SimTrack_csc/cosh(csc_gp_eta)>>e1",num)

ea = ROOT.TH1F("ea","ea",BINM,array('d', binLow))
eb = ROOT.TH1F("eb","eb",BINM,array('d', binLow))
ec = ROOT.TH1F("ec","ec",BINM,array('d', binLow))

t1.Draw("p_SimTrack_csc/cosh(csc_gp_eta)>> ea",den)
t1.Draw("p_SimTrack_csc/cosh(csc_gp_eta)>> eb",den2)
t1.Draw("p_SimTrack_csc/cosh(csc_gp_eta)>> ec",den4)

e2 = ROOT.TH1F("e2","e2",BINM,array('d', binLow))
t1.Draw("p_SimTrack_csc/cosh(csc_gp_eta)>>e2",num2)
e4 = ROOT.TH1F("e4","e4",BINM,array('d', binLow))
t1.Draw("p_SimTrack_csc/cosh(csc_gp_eta)>>e4",num4)


ea.Sumw2()
eb.Sumw2()
ec.Sumw2()
e1.Sumw2()
e2.Sumw2()
e4.Sumw2()

e1.Divide(ea)
e2.Divide(eb)
e4.Divide(ec)



e1.SetLineColor(ROOT.kBlue)
e1.SetLineWidth(2)
e1.SetLineStyle(1)
e1.SetMarkerStyle(22)
e1.SetMarkerColor(ROOT.kBlue)
e1.SetMarkerSize(2)

e2.SetLineColor(ROOT.kRed)
e2.SetLineWidth(2)
e2.SetLineStyle(1)
e2.SetMarkerStyle(22)
e2.SetMarkerColor(ROOT.kRed)
e2.SetMarkerSize(2)


e4.SetLineColor(ROOT.kGreen+2)
e4.SetLineWidth(2)
e4.SetLineStyle(1)
e4.SetMarkerStyle(20)
e4.SetMarkerColor(ROOT.kGreen+2)
e4.SetMarkerSize(2)
e4.SetStats(0)
e1.SetStats(0)
e2.SetStats(0)

b1 = ROOT.TH1F("b1","b1",35,0,60)
b1.GetYaxis().SetRangeUser(0.0,1.06)
b1.GetYaxis().SetTitleOffset(1.2)
b1.GetYaxis().SetNdivisions(520)
b1.GetYaxis().SetTitle("Efficiency")
b1.GetXaxis().SetTitle("p_{T} of Simulated Muon Track [GeV]")
b1.SetTitle("p_{T} Reconstruction Efficiency. 80k Ev, ME11- ME2, ct0 mm")
b1.SetStats(0)

b1.Draw()
e4.Draw("same P")
e1.Draw("same P")
e2.Draw("same P")

text1 = ROOT.TLatex(28,.418,"ME11 - ME2 in "+low+"< \eta <"+hig)
text1.Draw("same")
    

#aj.Draw("same")
#e3.Draw("same P")
legend = ROOT.TLegend(0.46,0.16,0.86,0.38)
legend.SetFillColor(ROOT.kWhite)
legend.SetMargin(0.15)
#legend.SetBorderSize(0)
#legend.SetFillStyle(0)
legend.SetHeader("Reconstructed p_{T} >20 GeV and")
legend.AddEntry(e1,"|d_{xy}| < 5 cm", "p")
legend.AddEntry(e2,"10 cm  < |d_{xy}| < 30 cm","p")
legend.AddEntry(e4,"50 cm < |d_{xy}| < 500 cm","p")
#legend.AddEntry(e2,"Sim pT > 20","l")
legend.Draw("same")

#c1.SaveAs("Whole3LCT.png")
c1.SaveAs("Eff_"+name+".pdf")
c1.SaveAs("poster8.png")

