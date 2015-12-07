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

  
  draw_1D(treeHits,"dEta_sim",  "dEta_sim",  "dEta_sim", "(50,0,5)")
  draw_1D(treeHits,"dPhi_sim",  "dPhi_sim",  "dPhi_sim", "(50,0,5)")
  draw_1D(treeHits,"dR_sim",  "dR_sim",  "dR_sim", "(50,0,5)")

  draw_1D(treeHits,"pt_L1",  "pt_L1",  "pt_L1", "(100,0,200)")
  draw_1D(treeHits,"eta_L1",  "eta_L1",  "eta_L1", "(60,-3,3)")
  draw_1D(treeHits,"phi_L1",  "phi_L1",  "phi_L1", "(70,-3.5,5.3)")
  draw_1D(treeHits,"quality",  "quality",  "quality", "(10,0,10)")
  draw_1D(treeHits,"charge",  "charge",  "charge", "(5,-2,2)")
