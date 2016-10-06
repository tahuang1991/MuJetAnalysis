from ROOT import *

file = TFile("out_ana.root")
treeHits = file.Get("L1MuTree")

c = TCanvas("c","",800,600)
c.cd()
treeHits.Draw("gen_pt")
c.SaveAs("test.png")
