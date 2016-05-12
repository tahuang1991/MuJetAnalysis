import ROOT
import random
import os
import numpy as np

ROOT.gROOT.SetBatch(1)
ROOT.gStyle.SetStatW(0.07)
ROOT.gStyle.SetStatH(0.06)

ROOT.gStyle.SetOptStat(0)



ROOT.gStyle.SetTitleStyle(0)
ROOT.gStyle.SetTitleAlign(13) ## coord in top left
ROOT.gStyle.SetTitleX(0.)
ROOT.gStyle.SetTitleY(1.)
ROOT.gStyle.SetTitleW(1)
ROOT.gStyle.SetTitleH(0.058)
ROOT.gStyle.SetTitleBorderSize(0)

ROOT.gStyle.SetPadLeftMargin(0.126)
ROOT.gStyle.SetPadRightMargin(0.04)
ROOT.gStyle.SetPadTopMargin(0.06)
ROOT.gStyle.SetPadBottomMargin(0.13)

ROOT.gStyle.SetMarkerStyle(1)

c1 = ROOT.TCanvas()
c1.SetGridx()
c1.SetGridy()
c1.SetTickx()
c1.SetTicky()
ptbin = [2.0,   2.5,   3.0,   3.5,   4.0, 4.5,   5.0,   6.0,   7.0,   8.0,  10.0,  12.0,  14.0, 16.0,  18.0,  20.0,  25.0,  30.0,  35.0,  40.0,  45.0, 50.0,  60.0,  70.0,  80.0,  90.0, 100.0, 120.0, 140.0, 200.0]
myptbin = np.asarray(ptbin)
#___________________________________________________
def getRatecount(tree,todraw,cut):
    
    htemp = ROOT.TH1F("htemp"," ",50,-100,100)
    tree.Draw(todraw+">>htemp",cut)
    print "cuts ",cut, " entries ",htemp.GetEntries()
    return htemp.GetEntries()

#____________________________________________________
def getRate(filedir, treename, todraw, cut):
    #f = ROOT.TFile(file)
    #t = f.Get(dir)
    tree = ROOT.TChain(treename)
    if os.path.isdir(filedir):
    	  ls = os.listdir(filedir)
    	  for x in ls:
		x = filedir[:]+x
		tree.Add(x)
    elif os.path.isfile(filedir):
	  tree.Add(filedir)
    else:
	  print " it is not file nor dir ", filedir

    h = ROOT.TH1F("h"," ",29,myptbin)
    n=1
    for x in ptbin:
#	print "cut ",cut+" && pt>=%f"%x
	content = getRatecount(tree,"pt_SimTrack",cut+"&& %s>=%f"%(todraw,x))
    	#content = tree.GetEntries(cut+"&& pt>=%f"%x)
#	print "bin n ",n,"pt ",x ,"  content ",content
	h.SetBinContent(n, content)
	n= n+1
    h.Sumw2()
 #  print "before scale "
 #   h.Print("all")
    #ntotalEvents = getRatecount(tree,"pt_SimTrack",cut)
    ntotalEvents = getRatecount(tree,"pt_SimTrack","1")
    #h.Scale(40000./ntotalEvents/3./2.*0.795)
    h.Scale(30000.*140/ntotalEvents)
#    print "after scale "
 #   h.Print("all")
    return h


b1 = ROOT.TH1F("b1","b1",29,myptbin)
b1.GetYaxis().SetRangeUser(0.01,100000)
b1.GetYaxis().SetTitleOffset(1.2)
b1.GetYaxis().SetNdivisions(520)
b1.GetYaxis().SetTitle("L1 Trigger Rate [kHz]")
b1.GetXaxis().SetTitle("L1 muon p_{T} threshold [GeV]")
b1.GetXaxis().SetTitleFont(62)
b1.GetXaxis().SetTitleOffset(1.2)
b1.GetXaxis().SetTitleSize(0.045)
b1.GetYaxis().SetTitleSize(0.045)
b1.SetTitle("CMS Simulation Preliminary"+" "*26 +" PU140, 14TeV")
b1.SetStats(0)

treename = "DisplacedMuonTriggerRateGENSIM/trk_rate_csc_sim"
treename2 = "DisplacedMuonTriggerRateGENSIM/trk_rate_csc_position"
treename3 = "DisplacedMuonTriggerRateGENSIM/trk_rate_csc_direction"
filedir = "/fdata/hepx/store/user/tahuang/MinBias_TuneCUETP8M1_13TeV-pythia8/crab_MinbiasOnly_20160210_v2/160210_174957/0000/"
#filedir = "/fdata/hepx/store/user/taohuang/Ptassignment_30_Nov_ct0/out_ana_minbias_test_1M_20160210.root"
cut = "abs(csc_st2_gp_eta)<2.4 && abs(csc_st2_gp_eta)>1.6"
#tfile1 = ROOT.TFile("/uscms_data/d3/tahuang/CMSSW_6_2_0_SLHC25_patch1/src/GEMCode/GEMValidation/test/Rate_Neutrino_SLHC25_2019withoutGEM_PU140_0706.root")
#tfile2 = ROOT.TFile("/uscms_data/d3/tahuang/CMSSW_6_2_0_SLHC25_patch1/src/GEMCode/GEMValidation/test/Rate_Neutrino_SLHC25_2019withGEM_PU140_0706.root")
#tfile3 = ROOT.TFile("/uscms_data/d3/tahuang/CMSSW_6_2_0_SLHC25_patch1/src/GEMCode/GEMValidation/test/Rate_Neutrino_SLHC25_2023NoRPC_PU140_0706.root")
#tfile4 = ROOT.TFile("/uscms_data/d3/tahuang/CMSSW_6_2_0_SLHC25_patch1/src/GEMCode/GEMValidation/test/Rate_Neutrino_SLHC25_PU140_0706.root")
e1 = getRate(filedir, treename,"pt_SimTrack",cut)
e2 = getRate(filedir, treename2,"pt_position_sh",cut)
e3 = getRate(filedir, treename3,"abs(pt_direction_sh)",cut+"&& abs(pt_direction_sh)<99")
#e3 = getRate(tree2, cut3)
#e4 = getRate(tree4, cut2)
#e4 = getRate("/uscms_data/d3/tahuang/CMSSW_6_2_0_SLHC25_patch1/src/GEMCode/GEMValidation/test/Rate_Neutrino_SLHC25_PU140_0706.root",treename, cut)

#e0 = getAllEff("/eos/uscms/store/user/tahuang/SLHC25_patch1_2023Muon_1M_Ana_PU140_Pt2_50_ME11_step0/",treename, den, num)

e2.SetFillColor(ROOT.kBlue+1)
#e3.SetFillColor(ROOT.kRed-4)
e3.SetFillColor(ROOT.kMagenta+2)
e1.SetFillColor(ROOT.kGreen+2)

b1.Draw()
e1.Draw("e3same")
e2.Draw("e3same")
e3.Draw("e3same")
#e4.Draw("e3same")
ROOT.gPad.SetLogx()
ROOT.gPad.SetLogy()


legend = ROOT.TLegend(0.5,0.7,0.93,0.95)
legend.SetFillStyle(0)
#legend.SetFillColor(ROOT.kWhite)
legend.SetTextFont(62)
#legend.SetTextSize(0.040)
legend.SetBorderSize(0)
#legend.SetTextSize()
#legend.SetHeader("p_{T}^{sim}>10,2.14>|#eta|>1.64, has at least 3stubs and hasME1")
legend.AddEntry(e1,"true pt","f")
legend.AddEntry(e2,"position based reco pt","f")
legend.AddEntry(e3,"direction based reco pt","f")
#legend.AddEntry(e2,"#splitline{Phase I, 3+stubs}{and one stub in YE1/1}","f")
#legend.AddEntry(e3,"#splitline{Phase II with GE11 only}{3+stubs and YE1/1 bending angle}","f")
#legend.AddEntry(e4,"#splitline{Full PhaseII, 3+stubs }{and YE1/1 bending angle}","f")
legend.Draw("same")

tex = ROOT.TLatex(0.15,0.88,"1.6<|#eta|<2.4")
tex.SetTextSize(0.05)
tex.SetTextFont(62)
tex.SetNDC()
tex.Draw("same")


c1.SaveAs("Trigrate_pt_displacedMuon_Gensim_all_PU140_brazos.pdf")
c1.SaveAs("Trigrate_pt_displacedMuon_Gensim_all_PU140_brazos.png")
