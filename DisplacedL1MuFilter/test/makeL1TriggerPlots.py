import sys

from ROOT import *

## run quiet mode
import sys
sys.argv.append( '-b' )

import ROOT 
ROOT.gROOT.SetBatch(1)
from Helpers import *

if __name__ == "__main__":  

  inputFile = 'out_filter_ana.root'
  targetDir = './'
  
  ## extension for figures - add more?
  ext = ".png"
  
  ## Trees
  analyzer = "DisplacedL1MuFilter_PhaseIIGE21"
  recHits = "L1MuTree"

  ## Style
  gStyle.SetStatStyle(0);

  ## input
  file = TFile.Open(inputFile)
  if not file:
    sys.exit('Input ROOT file %s is missing.' %(inputFile))

  dirAna = file.Get(analyzer)
  if not dirAna:
    sys.exit('Directory %s does not exist.' %(dirAna))
    
  treeHits = dirAna.Get(recHits)
  if not treeHits:
    sys.exit('Tree %s does not exist.' %(treeHits))
  
  print "Making the plots"

  draw_1D(treeHits,"dEta_sim_corr",  "dEta_sim_corr",  "dEta_sim_corr", "(100,0,1)")

  draw_1D(treeHits,"dEta_sim_corr",  "dEta_sim_corr",  "dEta_sim_corr", "(100,0,1)")
  draw_1D(treeHits,"dPhi_sim_corr",  "dPhi_sim_corr",  "dPhi_sim_corr", "(100,0,1)")
  draw_1D(treeHits,"dR_sim_corr",  "dR_sim_corr",  "dR_sim_corr", "(100,0,1)")

  draw_1D(treeHits,"dR_sim_corr",  "dR_sim_corr_pt10_fid",  "dR_sim_corr_pt10_fid", "(100,0,1)",TCut("pt>10 && abs(eta)<2.5"))
  draw_1D(treeHits,"dR_sim_corr",  "dR_sim_corr_pt15_fid",  "dR_sim_corr_pt15_fid", "(100,0,1)",TCut("pt>15 && abs(eta)<2.5"))
  draw_1D(treeHits,"dR_sim_corr",  "dR_sim_corr_pt20_fid",  "dR_sim_corr_pt20_fid", "(100,0,1)",TCut("pt>20 && abs(eta)<2.5"))

  draw_1D(treeHits,"dEta_sim_prop",  "dEta_sim_prop",  "dEta_sim_prop", "(100,0,1)")
  draw_1D(treeHits,"dPhi_sim_prop",  "dPhi_sim_prop",  "dPhi_sim_prop", "(100,0,1)")
  draw_1D(treeHits,"dR_sim_prop",  "dR_sim_prop",  "dR_sim_prop", "(100,0,1)")

  draw_1D(treeHits,"dR_sim_prop",  "dR_sim_prop_pt10_fid",  "dR_sim_prop_pt10_fid", "(100,0,1)",TCut("pt>10 && abs(eta)<2.5"))
  draw_1D(treeHits,"dR_sim_prop",  "dR_sim_prop_pt15_fid",  "dR_sim_prop_pt15_fid", "(100,0,1)",TCut("pt>15 && abs(eta)<2.5"))
  draw_1D(treeHits,"dR_sim_prop",  "dR_sim_prop_pt20_fid",  "dR_sim_prop_pt20_fid", "(100,0,1)",TCut("pt>20 && abs(eta)<2.5"))

  draw_1D(treeHits,"pt",  "pt_L1",  "pt_L1", "(100,0,200)")
  draw_1D(treeHits,"eta",  "eta_L1",  "eta_L1", "(60,-3,3)")
  draw_1D(treeHits,"phi",  "phi_L1",  "phi_L1", "(70,-3.5,3.5)")
  draw_1D(treeHits,"quality",  "quality",  "quality", "(10,0,10)")
  draw_1D(treeHits,"charge",  "charge",  "charge", "(5,-2,2)")

  draw_1D(treeHits,"dEta_L1Tk_corr",  "dEta_L1Tk_corr",  "dEta_L1Tk_corr", "(100,0,1)")
  draw_1D(treeHits,"dPhi_L1Tk_corr",  "dPhi_L1Tk_corr",  "dPhi_L1Tk_corr", "(100,0,1)")
  draw_1D(treeHits,"dR_L1Tk_corr",  "dR_L1Tk_corr",  "dR_L1Tk_corr", "(100,0,1)")

  draw_1D(treeHits,"dEta_L1Tk_prop",  "dEta_L1Tk_prop",  "dEta_L1Tk_prop", "(100,0,1)")
  draw_1D(treeHits,"dPhi_L1Tk_prop",  "dPhi_L1Tk_prop",  "dPhi_L1Tk_prop", "(100,0,1)")
  draw_1D(treeHits,"dR_L1Tk_prop",  "dR_L1Tk_prop",  "dR_L1Tk_prop", "(100,0,1)")

  etaBinning = "(50,-2.5,2.5)"
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, TCut("pt>10"), TCut("abs(dR_sim_corr)<0.2")), "eff_L1_eta_pt10_sim_corr", "dR(SIM,L1Mu)<0.2, p_{T} > 10 GeV")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, TCut("pt>15"), TCut("abs(dR_sim_corr)<0.2")), "eff_L1_eta_pt15_sim_corr", "dR(SIM,L1Mu)<0.2, p_{T} > 15 GeV")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, TCut("pt>20"), TCut("abs(dR_sim_corr)<0.2")), "eff_L1_eta_pt20_sim_corr", "dR(SIM,L1Mu)<0.2, p_{T} > 20 GeV")

  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, TCut("pt>10"), TCut("abs(dR_sim_prop)<0.2")), "eff_L1_eta_pt10_sim_prop", "dR(SIM,L1Mu)<0.2, p_{T} > 10 GeV")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, TCut("pt>15"), TCut("abs(dR_sim_prop)<0.2")), "eff_L1_eta_pt15_sim_prop", "dR(SIM,L1Mu)<0.2, p_{T} > 15 GeV")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, TCut("pt>20"), TCut("abs(dR_sim_prop)<0.2")), "eff_L1_eta_pt20_sim_prop", "dR(SIM,L1Mu)<0.2, p_{T} > 20 GeV")

  """
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt>10"), TCut("dR_sim_corr<0.2")), TCut("dR_L1Tk<0.12")), "eff_L1_eta_pt10_sim_L1_dRL1Tk_012", "dR(SIM,L1Mu)<0.2, p_{T} > 10 GeV, L1Mu is matched")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt>10"), TCut("dR_sim_corr<0.2")), TCut("dR_L1Tk_corr<0.12")), "eff_L1_eta_pt10_sim_L1_dRL1TkCorr_012", "dR(SIM,L1Mu)<0.2, p_{T} > 10 GeV, L1Mu is matched")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt>15"), TCut("dR_sim_corr<0.2")), TCut("dR_L1Tk<0.12")), "eff_L1_eta_pt15_sim_L1_dRL1Tk_012", "dR(SIM,L1Mu)<0.2, p_{T} > 15 GeV, L1Mu is matched")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt>15"), TCut("dR_sim_corr<0.2")), TCut("dR_L1Tk_corr<0.12")), "eff_L1_eta_pt15_sim_L1_dRL1TkCorr_012", "dR(SIM,L1Mu)<0.2, p_{T} > 15 GeV, L1Mu is matched")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt>20"), TCut("dR_sim_corr<0.2")), TCut("dR_L1Tk<0.12")), "eff_L1_eta_pt20_sim_L1_dRL1Tk_012", "dR(SIM,L1Mu)<0.2, p_{T} > 20 GeV, L1Mu is matched")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt>20"), TCut("dR_sim_corr<0.2")), TCut("dR_L1Tk_corr<0.12")), "eff_L1_eta_pt20_sim_L1_dRL1TkCorr_012", "dR(SIM,L1Mu)<0.2, p_{T} > 20 GeV, L1Mu is matched")
  """
