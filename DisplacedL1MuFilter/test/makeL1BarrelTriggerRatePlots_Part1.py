# Run quiet mode
import sys
sys.argv.append( '-b' )
import ROOT
ROOT.gROOT.SetBatch(1)
from Helpers import *
from TriggerAlgorithms import *

ROOT.gErrorIgnoreLevel=1001
from ROOT import *
import random
#______________________________________________________________________________
if __name__ == "__main__":

  label = "Neutrino_Pt2to20_gun_TTI2023Upg14D_PU140bx25_ILT_SLHC14_Barrel20170301"; pu = 'PU140'; eff = False

  ## extension for figures - add more?
  ext = ".png"

  ## Style
  gStyle.SetStatStyle(0)

  print "Making the plots"

  set_style()

  doTest = False

  ch = TChain("DisplacedL1MuFilter_PhaseIIGE21/L1MuTree")

  location0 = '/Users/Sven/Documents/work/DisplacedMuL1Studies/NeutrinoGun_14TeV_PU140_L1MuANA_v30_StubReco/0000/'
  location1 = '/Users/Sven/Documents/work/DisplacedMuL1Studies/NeutrinoGun_14TeV_PU140_L1MuANA_v30_StubReco/0001/'
  location2 = '/Users/Sven/Documents/work/DisplacedMuL1Studies/NeutrinoGun_14TeV_PU140_L1MuANA_v30_StubReco/0002/'

  tree = addfiles(ch, dirname=location0, ext=".root")
  tree = addfiles(ch, dirname=location1, ext=".root")
  tree = addfiles(ch, dirname=location2, ext=".root")

  targetDir = label + "/"

  f = TFile.Open(label + ".root","RECREATE")
  

  verbose = True

  ## copy index file
  import shutil
  #shutil.copy2('index.php', targetDir + 'index.php')

  def displacedL1MuHybridTriggerRate():

    ## helper functions to make many plots!!
    mapTH1F = ROOT.std.map("string,TH1F")()
    mapTH2F = ROOT.std.map("string,TH2F")()

    def addPlotToMapTH1F(name,nBin,minBin,maxBin):
      mapTH1F[name] = TH1F(name,"",nBin,minBin,maxBin)

    def addPlotToMapTH1F_v2(name,bins):
      mapTH1F[name] = TH1F(name,"",len(bins)-1, bins)

    def addManyPlotsToTH1F(ptbins, etabins, *arg):
      for i in range(0,len(arg)):
        #addPlotToMapTH1F_v2(arg[i].replace("rate_", "rate_pt_"), ptbins)
        addPlotToMapTH1F(arg[i].replace("rate_", "rate_pt_"), 100, 0, 100)
        addPlotToMapTH1F_v2(arg[i].replace("rate_", "rate_eta_L1Pt7_"), etabins)
        addPlotToMapTH1F_v2(arg[i].replace("rate_", "rate_eta_L1Pt10_"), etabins)

    ## binning
        
    ptbin = [
      2.0,   2.5,   3.0,   3.5,   4.0,   4.5,   5.0,   6.0,   7.0,   8.0,
      10.0,  12.0,  14.0,  16.0,  18.0,  20.0,  25.0,  30.0,  35.0,  40.0,
      45.0,  50.0,  60.0,  70.0,  80.0,  90.0, 100.0, 120.0, 140.0]
    myptbin = np.asarray(ptbin)
    nmyptbin = len(myptbin) - 1

    etabin = [
      0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95,
      1.0, 1.05, 1.1, 1.15, 1.2, 1.25, 1.3, 1.35, 1.4, 1.45, 1.5, 1.55, 1.6, 1.65, 1.7, 1.75, 1.8, 1.85, 1.9, 1.95,
      2.0, 2.05, 2.1, 2.15, 2.2, 2.25, 2.3, 2.35, 2.4, 2.45, 2.5]
    myetabin = np.asarray(etabin)

    h_dphi_ME11_ME21 = TH2F("h_dphi_ME11_ME21","",100,-0.05,0.05,100,-0.05,0.05)
    h_dphi_ME11_ME21_charge = TH2F("h_dphi_ME11_ME21_charge","",100,-0.05,0.05,100,-0.05,0.05)
    h_dphi_ME11_ME21_charge_Pt0to5 = TH2F("h_dphi_ME11_ME21_charge_Pt0to5","",100,-0.05,0.05,100,-0.05,0.05)
    h_dphi_ME11_ME21_charge_Pt7to140 = TH2F("h_dphi_ME11_ME21_charge_Pt7to140","",100,-0.05,0.05,100,-0.05,0.05)
    h_dphi_ME11_ME21_charge_Pt10to140 = TH2F("h_dphi_ME11_ME21_charge_Pt10to140","",100,-0.05,0.05,100,-0.05,0.05)
    h_dphi_ME11_ME21_charge_Pt15to140 = TH2F("h_dphi_ME11_ME21_charge_Pt15to140","",100,-0.05,0.05,100,-0.05,0.05)
    h_dphi_ME11_ME21_charge_Pt20to140 = TH2F("h_dphi_ME11_ME21_charge_Pt20to140","",100,-0.05,0.05,100,-0.05,0.05)
    h_dphi_ME11_ME21_charge_Pt30to140 = TH2F("h_dphi_ME11_ME21_charge_Pt30to140","",100,-0.05,0.05,100,-0.05,0.05)

    ## add plots
    addManyPlotsToTH1F(myptbin, myetabin,
                       "h_single_prompt_L1Mu_rate_eta0to0p9",
                       "h_single_prompt_L1Mu_rate_eta0to1p1",
                       "h_single_prompt_L1Mu_rate_eta0to2p4",

                       "h_single_prompt_L1Mu_rate_2_stubs_eta0to2p4",
                       "h_single_prompt_L1Mu_rate_3_stubs_eta0to2p4",

                       ## explicit stub requirement
                       "h_single_prompt_L1Mu_rate_MB1_MB2_eta0to0p9",
                       "h_single_prompt_L1Mu_rate_MB1_MB3_eta0to0p9",
                       "h_single_prompt_L1Mu_rate_MB1_MB4_eta0to0p9",
                       "h_single_prompt_L1Mu_rate_MB2_MB3_eta0to0p9",
                       "h_single_prompt_L1Mu_rate_MB2_MB4_eta0to0p9",
                       "h_single_prompt_L1Mu_rate_MB3_MB4_eta0to0p9",

                       ## displaced muons
                       "h_single_displaced_L1Mu_rate_direction_MB1_MB2_eta0to0p9",
                       "h_single_displaced_L1Mu_rate_direction_MB1_MB3_eta0to0p9",
                       "h_single_displaced_L1Mu_rate_direction_MB1_MB4_eta0to0p9",
                       "h_single_displaced_L1Mu_rate_direction_MB2_MB3_eta0to0p9",
                       "h_single_displaced_L1Mu_rate_direction_MB2_MB4_eta0to0p9",
                       "h_single_displaced_L1Mu_rate_direction_MB3_MB4_eta0to0p9",
                       "h_single_displaced_L1Mu_rate_direction_MB1_MB2_MB3_MB4_eta0to0p9",
                       "h_single_displaced_L1Mu_rate_direction_MB1_MB2_MB3_MB4_algo16_eta0to0p9",

                       ## displaced muons + loose TT isolation
                       "h_single_displaced_L1Mu_rate_direction_MB1_MB2_eta0to0p9_looseVeto",
                       "h_single_displaced_L1Mu_rate_direction_MB1_MB3_eta0to0p9_looseVeto",
                       "h_single_displaced_L1Mu_rate_direction_MB1_MB4_eta0to0p9_looseVeto",
                       "h_single_displaced_L1Mu_rate_direction_MB2_MB3_eta0to0p9_looseVeto",
                       "h_single_displaced_L1Mu_rate_direction_MB2_MB4_eta0to0p9_looseVeto",
                       "h_single_displaced_L1Mu_rate_direction_MB3_MB4_eta0to0p9_looseVeto",
                       "h_single_displaced_L1Mu_rate_direction_MB1_MB2_MB3_MB4_algo16_eta0to0p9",
                       "h_single_displaced_L1Mu_rate_direction_MB1_MB2_MB3_MB4_algo16_eta0to0p9_looseVeto",

                       ## displaced muons + medium TT isolation
                       "h_single_displaced_L1Mu_rate_direction_MB1_MB2_eta0to0p9_mediumVeto",
                       "h_single_displaced_L1Mu_rate_direction_MB1_MB3_eta0to0p9_mediumVeto",
                       "h_single_displaced_L1Mu_rate_direction_MB1_MB4_eta0to0p9_mediumVeto",
                       "h_single_displaced_L1Mu_rate_direction_MB2_MB3_eta0to0p9_mediumVeto",
                       "h_single_displaced_L1Mu_rate_direction_MB2_MB4_eta0to0p9_mediumVeto",
                       "h_single_displaced_L1Mu_rate_direction_MB3_MB4_eta0to0p9_mediumVeto",
                       "h_single_displaced_L1Mu_rate_direction_MB1_MB2_MB3_MB4_eta0to0p9_mediumVeto",
                       "h_single_displaced_L1Mu_rate_direction_MB1_MB2_MB3_MB4_algo16_eta0to0p9_mediumVeto",

                       ## displaced muons + tight TT isolation
                       "h_single_displaced_L1Mu_rate_direction_MB1_MB2_eta0to0p9_tightVeto",
                       "h_single_displaced_L1Mu_rate_direction_MB1_MB3_eta0to0p9_tightVeto",
                       "h_single_displaced_L1Mu_rate_direction_MB1_MB4_eta0to0p9_tightVeto",
                       "h_single_displaced_L1Mu_rate_direction_MB2_MB3_eta0to0p9_tightVeto",
                       "h_single_displaced_L1Mu_rate_direction_MB2_MB4_eta0to0p9_tightVeto",
                       "h_single_displaced_L1Mu_rate_direction_MB3_MB4_eta0to0p9_tightVeto",
                       "h_single_displaced_L1Mu_rate_direction_MB1_MB2_MB3_MB4_eta0to0p9_tightVeto",
                       "h_single_displaced_L1Mu_rate_direction_MB1_MB2_MB3_MB4_algo16_eta0to0p9_tightVeto",
                       )


    maxEntries = tree.GetEntries()
    if doTest:
      maxEntries = 10000

    print "nEvents", maxEntries
    for k in range(0,maxEntries):
      if k%1000==0: print "Processing event", k

      ## get event
      tree.GetEntry(k)

      ## get the max value of the momentum
      pts = list(tree.L1Mu_pt)

      ## ignore events without L1Mu
      if len(pts)==0: continue
      
      ## calibrate trigger rate
      fillPromptHistogram(mapTH1F, "h_single_prompt_L1Mu_rate_eta0to2p4", tree, 0.0, 2.4, 0)
      fillPromptHistogram(mapTH1F, "h_single_prompt_L1Mu_rate_eta0to1p1", tree, 0.0, 1.1, 0)
      fillPromptHistogram(mapTH1F, "h_single_prompt_L1Mu_rate_eta0to0p9", tree, 0.0, 0.9, 2)

      ## barrel rates
      fillPromptHistogram(mapTH1F, "h_single_prompt_L1Mu_rate_MB1_MB2_eta0to0p9", tree, 0.0, 0.9, 0, hasMB1Cut=True, hasMB2Cut=True)
      fillPromptHistogram(mapTH1F, "h_single_prompt_L1Mu_rate_MB1_MB3_eta0to0p9", tree, 0.0, 0.9, 0, hasMB1Cut=True, hasMB3Cut=True)
      fillPromptHistogram(mapTH1F, "h_single_prompt_L1Mu_rate_MB1_MB4_eta0to0p9", tree, 0.0, 0.9, 0, hasMB1Cut=True, hasMB4Cut=True)
      fillPromptHistogram(mapTH1F, "h_single_prompt_L1Mu_rate_MB2_MB3_eta0to0p9", tree, 0.0, 0.9, 0, hasMB2Cut=True, hasMB3Cut=True)
      fillPromptHistogram(mapTH1F, "h_single_prompt_L1Mu_rate_MB2_MB4_eta0to0p9", tree, 0.0, 0.9, 0, hasMB2Cut=True, hasMB4Cut=True)
      fillPromptHistogram(mapTH1F, "h_single_prompt_L1Mu_rate_MB3_MB4_eta0to0p9", tree, 0.0, 0.9, 0, hasMB3Cut=True, hasMB4Cut=True)

      ## overall rates
      fillPromptHistogram(mapTH1F, "h_single_prompt_L1Mu_rate_2_stubs_eta0to2p4", tree, 0.0, 2.4, 2)
      fillPromptHistogram(mapTH1F, "h_single_prompt_L1Mu_rate_3_stubs_eta0to2p4", tree, 0.0, 2.4, 3)

      ## displaced algorithms
      ##
      ## 1: direction based
      fillDisplacedBarrelHistogram(mapTH1F, "h_single_displaced_L1Mu_rate_direction_MB1_MB2_eta0to0p9", tree, 0, 0.9, 0, algorithm=1)
      fillDisplacedBarrelHistogram(mapTH1F, "h_single_displaced_L1Mu_rate_direction_MB1_MB3_eta0to0p9", tree, 0, 0.9, 0, algorithm=2)
      fillDisplacedBarrelHistogram(mapTH1F, "h_single_displaced_L1Mu_rate_direction_MB1_MB4_eta0to0p9", tree, 0, 0.9, 0, algorithm=3)
      fillDisplacedBarrelHistogram(mapTH1F, "h_single_displaced_L1Mu_rate_direction_MB2_MB3_eta0to0p9", tree, 0, 0.9, 0, algorithm=4)
      fillDisplacedBarrelHistogram(mapTH1F, "h_single_displaced_L1Mu_rate_direction_MB2_MB4_eta0to0p9", tree, 0, 0.9, 0, algorithm=5)
      fillDisplacedBarrelHistogram(mapTH1F, "h_single_displaced_L1Mu_rate_direction_MB3_MB4_eta0to0p9", tree, 0, 0.9, 0, algorithm=6)
      fillDisplacedBarrelHistogram(mapTH1F, "h_single_displaced_L1Mu_rate_direction_MB1_MB2_MB3_MB4_eta0to0p9", tree, 0, 0.9, 0, algorithm=7)
      fillDisplacedBarrelHistogram(mapTH1F, "h_single_displaced_L1Mu_rate_direction_MB1_MB2_MB3_MB4_algo16_eta0to0p9", tree, 0, 0.9, 0, algorithm=16)

      ## loose isolation
      fillDisplacedBarrelHistogram(mapTH1F, "h_single_displaced_L1Mu_rate_direction_MB1_MB2_eta0to0p9_looseVeto", tree, 0, 0.9, 0, algorithm=1, vetoType=1)
      fillDisplacedBarrelHistogram(mapTH1F, "h_single_displaced_L1Mu_rate_direction_MB1_MB3_eta0to0p9_looseVeto", tree, 0, 0.9, 0, algorithm=2, vetoType=1)
      fillDisplacedBarrelHistogram(mapTH1F, "h_single_displaced_L1Mu_rate_direction_MB1_MB4_eta0to0p9_looseVeto", tree, 0, 0.9, 0, algorithm=3, vetoType=1)
      fillDisplacedBarrelHistogram(mapTH1F, "h_single_displaced_L1Mu_rate_direction_MB2_MB3_eta0to0p9_looseVeto", tree, 0, 0.9, 0, algorithm=4, vetoType=1)
      fillDisplacedBarrelHistogram(mapTH1F, "h_single_displaced_L1Mu_rate_direction_MB2_MB4_eta0to0p9_looseVeto", tree, 0, 0.9, 0, algorithm=5, vetoType=1)
      fillDisplacedBarrelHistogram(mapTH1F, "h_single_displaced_L1Mu_rate_direction_MB3_MB4_eta0to0p9_looseVeto", tree, 0, 0.9, 0, algorithm=6, vetoType=1)
      fillDisplacedBarrelHistogram(mapTH1F, "h_single_displaced_L1Mu_rate_direction_MB1_MB2_MB3_MB4_eta0to0p9_looseVeto", tree, 0, 0.9, 0, algorithm=7, vetoType=1)
      fillDisplacedBarrelHistogram(mapTH1F, "h_single_displaced_L1Mu_rate_direction_MB1_MB2_MB3_MB4_algo16_eta0to0p9_looseVeto", tree, 0, 0.9, 0, algorithm=16, vetoType=1)

      ## medium isolation
      fillDisplacedBarrelHistogram(mapTH1F, "h_single_displaced_L1Mu_rate_direction_MB1_MB2_eta0to0p9_mediumVeto", tree, 0, 0.9, 0, algorithm=1, vetoType=2)
      fillDisplacedBarrelHistogram(mapTH1F, "h_single_displaced_L1Mu_rate_direction_MB1_MB3_eta0to0p9_mediumVeto", tree, 0, 0.9, 0, algorithm=2, vetoType=2)
      fillDisplacedBarrelHistogram(mapTH1F, "h_single_displaced_L1Mu_rate_direction_MB1_MB4_eta0to0p9_mediumVeto", tree, 0, 0.9, 0, algorithm=3, vetoType=2)
      fillDisplacedBarrelHistogram(mapTH1F, "h_single_displaced_L1Mu_rate_direction_MB2_MB3_eta0to0p9_mediumVeto", tree, 0, 0.9, 0, algorithm=4, vetoType=2)
      fillDisplacedBarrelHistogram(mapTH1F, "h_single_displaced_L1Mu_rate_direction_MB2_MB4_eta0to0p9_mediumVeto", tree, 0, 0.9, 0, algorithm=5, vetoType=2)
      fillDisplacedBarrelHistogram(mapTH1F, "h_single_displaced_L1Mu_rate_direction_MB3_MB4_eta0to0p9_mediumVeto", tree, 0, 0.9, 0, algorithm=6, vetoType=2)
      fillDisplacedBarrelHistogram(mapTH1F, "h_single_displaced_L1Mu_rate_direction_MB1_MB2_MB3_MB4_eta0to0p9_mediumVeto", tree, 0, 0.9, 0, algorithm=7, vetoType=2)
      fillDisplacedBarrelHistogram(mapTH1F, "h_single_displaced_L1Mu_rate_direction_MB1_MB2_MB3_MB4_algo16_eta0to0p9_mediumVeto", tree, 0, 0.9, 0, algorithm=16, vetoType=2)

      ## tight isolation
      fillDisplacedBarrelHistogram(mapTH1F, "h_single_displaced_L1Mu_rate_direction_MB1_MB2_eta0to0p9_tightVeto", tree, 0, 0.9, 0, algorithm=1, vetoType=3)
      fillDisplacedBarrelHistogram(mapTH1F, "h_single_displaced_L1Mu_rate_direction_MB1_MB3_eta0to0p9_tightVeto", tree, 0, 0.9, 0, algorithm=2, vetoType=3)
      fillDisplacedBarrelHistogram(mapTH1F, "h_single_displaced_L1Mu_rate_direction_MB1_MB4_eta0to0p9_tightVeto", tree, 0, 0.9, 0, algorithm=3, vetoType=3)
      fillDisplacedBarrelHistogram(mapTH1F, "h_single_displaced_L1Mu_rate_direction_MB2_MB3_eta0to0p9_tightVeto", tree, 0, 0.9, 0, algorithm=4, vetoType=3)
      fillDisplacedBarrelHistogram(mapTH1F, "h_single_displaced_L1Mu_rate_direction_MB2_MB4_eta0to0p9_tightVeto", tree, 0, 0.9, 0, algorithm=5, vetoType=3)
      fillDisplacedBarrelHistogram(mapTH1F, "h_single_displaced_L1Mu_rate_direction_MB3_MB4_eta0to0p9_tightVeto", tree, 0, 0.9, 0, algorithm=6, vetoType=3)
      fillDisplacedBarrelHistogram(mapTH1F, "h_single_displaced_L1Mu_rate_direction_MB1_MB2_MB3_MB4_eta0to0p9_tightVeto", tree, 0, 0.9, 0, algorithm=7, vetoType=3)
      fillDisplacedBarrelHistogram(mapTH1F, "h_single_displaced_L1Mu_rate_direction_MB1_MB2_MB3_MB4_algo16_eta0to0p9_tightVeto", tree, 0, 0.9, 0, algorithm=16, vetoType=3)

    ## output ROOT file
    
    f.Write();
    f.Close();

    exit()

  displacedL1MuHybridTriggerRate()

