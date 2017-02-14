# Run quiet mode
import sys
sys.argv.append( '-b' )
import ROOT
ROOT.gROOT.SetBatch(1)
from Helpers import *
from hybridAlgorithmPtAssignment import *
from TTTrackIsolation import *

ROOT.gErrorIgnoreLevel=1001
from ROOT import *
import random
#______________________________________________________________________________
if __name__ == "__main__":

  label = "Neutrino_Pt2to20_gun_TTI2023Upg14D_PU140bx25_ILT_SLHC14_20170105_v2"; pu = 'PU140'; eff = False
  label = "Neutrino_Pt2to20_gun_TTI2023Upg14D_PU140bx25_ILT_SLHC14_20170110"; pu = 'PU140'; eff = False
  label = "Neutrino_Pt2to20_gun_TTI2023Upg14D_PU140bx25_ILT_SLHC14_20170119"; pu = 'PU140'; eff = False
  label = "Neutrino_Pt2to20_gun_TTI2023Upg14D_PU140bx25_ILT_SLHC14_20170123"; pu = 'PU140'; eff = False
  label = "Neutrino_Pt2to20_gun_TTI2023Upg14D_PU140bx25_ILT_SLHC14_20170124"; pu = 'PU140'; eff = False
  label = "Neutrino_Pt2to20_gun_TTI2023Upg14D_PU140bx25_ILT_SLHC14_20170125"; pu = 'PU140'; eff = False
  label = "Neutrino_Pt2to20_gun_TTI2023Upg14D_PU140bx25_ILT_SLHC14_20170126"; pu = 'PU140'; eff = False
  label = "Neutrino_Pt2to20_gun_TTI2023Upg14D_PU140bx25_ILT_SLHC14_20170131"; pu = 'PU140'; eff = False
  label = "Neutrino_Pt2to20_gun_TTI2023Upg14D_PU140bx25_ILT_SLHC14_20170207"; pu = 'PU140'; eff = False
  label = "Neutrino_Pt2to20_gun_TTI2023Upg14D_PU140bx25_ILT_SLHC14_20170207_v2"; pu = 'PU140'; eff = False
  label = "Neutrino_Pt2to20_gun_TTI2023Upg14D_PU140bx25_ILT_SLHC14_20170214"; pu = 'PU140'; eff = False

  ## extension for figures - add more?
  ext = ".png"

  ## Style
  gStyle.SetStatStyle(0)

  print "Making the plots"

  set_style()

  doTest = True

  ch = TChain("DisplacedL1MuFilter_PhaseIIGE21/L1MuTree")

  location0 = '/Users/Sven/Documents/work/DisplacedMuL1Studies/NeutrinoGun_14TeV_PU140_L1MuANA_v29_StubReco/0000/'
  location1 = '/Users/Sven/Documents/work/DisplacedMuL1Studies/NeutrinoGun_14TeV_PU140_L1MuANA_v29_StubReco/0001/'
  location2 = '/Users/Sven/Documents/work/DisplacedMuL1Studies/NeutrinoGun_14TeV_PU140_L1MuANA_v29_StubReco/0002/'

  treeHits = addfiles(ch, dirname=location0, ext=".root")
  treeHits = addfiles(ch, dirname=location1, ext=".root")
  treeHits = addfiles(ch, dirname=location2, ext=".root")

  targetDir = label + "/"

  verbose = False

  ## copy index file
  import shutil
  shutil.copy2('index.php', targetDir + 'index.php')

  def displacedL1MuHybridTriggerRate():

    ## helper functions to make many plots!!
    mapTH1F = ROOT.std.map("string,TH1F")()
    mapTH2F = ROOT.std.map("string,TH2F")()

    def addPlotToMapTH1F(name,nBin,minBin,maxBin):
      mapTH1F[name] = TH1F(name,"",nBin,minBin,maxBin)

    def addPlotToMapTH1F_v2(name,bins):
      mapTH1F[name] = TH1F(name,"",len(bins)-1, bins)

    def addManyPlotsToTH1F(ptbins, etabins, *arg):
      for i in range(1,len(arg)):
        addPlotToMapTH1F_v2(arg[i].replace("rate_", "rate_pt_"), ptbins)
        addPlotToMapTH1F_v2(arg[i].replace("rate_", "rate_eta_"), etabins)

    ## binning
    ptbin = [
      1, 2.0,   2.5,   3.0,   3.5,   4.0,   4.5,   5.0,   6.0,   7.0,   8.0,
      10.0,  12.0,  14.0,  16.0,  18.0,  20.0,  25.0,  30.0,  35.0,  40.0,
      45.0,  50.0,  60.0,  70.0,  80.0,  90.0, 100.0, 120.0, 140.0]
    myptbin = np.asarray(ptbin)
    nmyptbin = len(myptbin) - 1

    etabin = [
      0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95,
      1.0, 1.05, 1.1, 1.15, 1.2, 1.25, 1.3, 1.35, 1.4, 1.45, 1.5, 1.55, 1.6, 1.65, 1.7, 1.75, 1.8, 1.85, 1.9, 1.95,
      2.0, 2.05, 2.1, 2.15, 2.2, 2.25, 2.3, 2.35, 2.4, 2.45, 2.5]
    myetabin = np.asarray(etabin)

    f = TFile.Open(label + ".root","RECREATE")

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
                       "h_single_prompt_L1Mu_rate_eta1p1to2p4",
                       "h_single_prompt_L1Mu_rate_eta1p2to2p4",
                       "h_single_prompt_L1Mu_rate_eta1p6to2p2",
                       "h_single_prompt_L1Mu_rate_eta1p6to2p15",
                       "h_single_prompt_L1Mu_rate_eta1p2to1p6",
                       "h_single_prompt_L1Mu_rate_eta1p2to2p2",

                       "h_single_prompt_L1Mu_rate_2_stubs_eta0to2p4",
                       "h_single_prompt_L1Mu_rate_3_stubs_eta0to2p4",

                       "h_single_prompt_L1Mu_rate_2_stubs_eta1p2to2p4",
                       "h_single_prompt_L1Mu_rate_3_stubs_eta1p2to2p4",

                       "h_single_prompt_L1Mu_rate_2_stubs_eta1p2to2p2",
                       "h_single_prompt_L1Mu_rate_3_stubs_eta1p2to2p2",

                       "h_single_prompt_L1Mu_rate_2_stubs_eta1p6to2p2",
                       "h_single_prompt_L1Mu_rate_3_stubs_eta1p6to2p2",

                       "h_single_prompt_L1Mu_rate_2_stubs_eta1p6to2p15",
                       "h_single_prompt_L1Mu_rate_3_stubs_eta1p6to2p15",

                       "h_single_prompt_L1Mu_rate_2_stubs_eta1p2to1p6",
                       "h_single_prompt_L1Mu_rate_3_stubs_eta1p2to1p6",

                       ## explicit stub requirement
                       "h_single_prompt_L1Mu_rate_MB1_MB4_eta0to0p9",

                       "h_single_prompt_L1Mu_rate_ME1_ME2_ME3_eta1p2to2p4",
                       "h_single_prompt_L1Mu_rate_ME1_ME2_ME3_eta1p6to2p15",
                       "h_single_prompt_L1Mu_rate_ME1_ME2_ME3_eta1p2to2p2",

                       "h_single_prompt_L1Mu_rate_2_stubs_ME11_eta1p6to2p2",
                       "h_single_prompt_L1Mu_rate_3_stubs_ME11_eta1p6to2p2",
                       "h_single_prompt_L1Mu_rate_2_stubs_ME11_eta1p6to2p15",
                       "h_single_prompt_L1Mu_rate_3_stubs_ME11_eta1p6to2p15",

                       "h_single_prompt_L1Mu_rate_2_stubs_ME21_eta1p6to2p2",
                       "h_single_prompt_L1Mu_rate_3_stubs_ME21_eta1p6to2p2",

                       "h_single_prompt_L1Mu_rate_2_stubs_ME11orME21_eta1p6to2p2",
                       "h_single_prompt_L1Mu_rate_3_stubs_ME11orME21_eta1p6to2p2",

                       "h_single_prompt_L1Mu_rate_GE11_ME11_ME21_ME3_eta1p6to2p15",

                       ## with GEMs
                       "h_single_prompt_L1Mu_rate_2_stubs_GE11_ME11_eta1p6to2p15",
                       "h_single_prompt_L1Mu_rate_3_stubs_GE11_ME11_eta1p6to2p15",

                       "h_single_prompt_L1Mu_rate_2_stubs_GE21_ME21_eta1p6to2p2",
                       "h_single_prompt_L1Mu_rate_3_stubs_GE21_ME21_eta1p6to2p2",

                       "h_single_prompt_L1Mu_rate_GE11_ME11_OR_GE21_ME21_eta1p6to2p15",
                       "h_single_prompt_L1Mu_rate_2_stubs_GE11_ME11_OR_GE21_ME21_eta1p6to2p15",
                       "h_single_prompt_L1Mu_rate_3_stubs_GE11_ME11_OR_GE21_ME21_eta1p6to2p15",

                       "h_single_prompt_L1Mu_rate_GE11_ME11_GE21_ME21_eta1p6to2p2",

                       "h_single_prompt_L1Mu_rate_GE11_ME11_GE21_ME21_ME3_eta1p6to2p15",
                       "h_single_prompt_L1Mu_rate_GE11_ME11_ME21_ME3_eta1p6to2p2",

                       ## failing stations
                       "h_single_prompt_L1Mu_rate_2_stubs_ME11_Fail10p_eta1p6to2p2",
                       "h_single_prompt_L1Mu_rate_3_stubs_ME11_Fail10p_eta1p6to2p2",

                       "h_single_prompt_L1Mu_rate_2_stubs_ME11_Fail10p_GE11_eta1p6to2p2",
                       "h_single_prompt_L1Mu_rate_3_stubs_ME11_Fail10p_GE11_eta1p6to2p2",

                       "h_single_prompt_L1Mu_rate_2_stubs_ME21_Fail10p_eta1p6to2p2",
                       "h_single_prompt_L1Mu_rate_3_stubs_ME21_Fail10p_eta1p6to2p2",

                       "h_single_prompt_L1Mu_rate_2_stubs_ME21_Fail10p_GE21_eta1p6to2p2",
                       "h_single_prompt_L1Mu_rate_3_stubs_ME21_Fail10p_GE21_eta1p6to2p2",

                       ## displaced muons
                       "h_single_displaced_L1Mu_rate_position_ME1_ME2_ME3_eta1p2to1p6",
                       "h_single_displaced_L1Mu_rate_position_ME1_ME2_ME3_eta1p6to2p15",
                       "h_single_displaced_L1Mu_rate_position_ME1_ME2_ME3_eta1p2to2p4",

                       "h_single_displaced_L1Mu_rate_direction_MB1_MB4_eta0to0p9",

                       "h_single_displaced_L1Mu_rate_direction_ME1_ME2_eta1p2to1p6",
                       "h_single_displaced_L1Mu_rate_direction_ME1_ME2_eta1p2to2p15",

                       "h_single_displaced_L1Mu_rate_hybrid_ME1_ME2_ME3_eta1p2to1p6",
                       "h_single_displaced_L1Mu_rate_hybrid_ME1_ME2_ME3_eta1p2to2p15",
                       "h_single_displaced_L1Mu_rate_hybrid_ME1_ME2_ME3_eta1p6to2p15",

                       "h_single_displaced_L1Mu_rate_direction_GE11_ME11_GE21_ME21_eta1p6to2p15",

                       "h_single_displaced_L1Mu_rate_hybrid_GE11_ME11_ME21_ME3_eta1p6to2p15",
                       "h_single_displaced_L1Mu_rate_hybrid_GE11_ME11_GE21_ME21_ME3_eta1p6to2p15",

                       ## displaced muons + loose TT isolation
                       "h_single_displaced_L1Mu_rate_position_ME1_ME2_ME3_eta1p2to1p6_looseVeto",
                       "h_single_displaced_L1Mu_rate_position_ME1_ME2_ME3_eta1p6to2p15_looseVeto",
                       "h_single_displaced_L1Mu_rate_position_ME1_ME2_ME3_eta1p2to2p4_looseVeto",

                       "h_single_displaced_L1Mu_rate_direction_MB1_MB4_eta0to0p9_looseVeto",

                       "h_single_displaced_L1Mu_rate_direction_ME1_ME2_eta1p2to1p6_looseVeto",
                       "h_single_displaced_L1Mu_rate_direction_ME1_ME2_eta1p2to2p15_looseVeto",

                       "h_single_displaced_L1Mu_rate_hybrid_ME1_ME2_ME3_eta1p2to1p6_looseVeto",
                       "h_single_displaced_L1Mu_rate_hybrid_ME1_ME2_ME3_eta1p2to2p15_looseVeto",
                       "h_single_displaced_L1Mu_rate_hybrid_ME1_ME2_ME3_eta1p6to2p15_looseVeto",

                       "h_single_displaced_L1Mu_rate_direction_GE11_ME11_GE21_ME21_eta1p6to2p15_looseVeto",

                       "h_single_displaced_L1Mu_rate_hybrid_GE11_ME11_ME21_ME3_eta1p6to2p15_looseVeto",
                       "h_single_displaced_L1Mu_rate_hybrid_GE11_ME11_GE21_ME21_ME3_eta1p6to2p15_looseVeto",

                       ## displaced muons + medium TT isolation
                       "h_single_displaced_L1Mu_rate_position_ME1_ME2_ME3_eta1p2to1p6_mediumVeto",
                       "h_single_displaced_L1Mu_rate_position_ME1_ME2_ME3_eta1p6to2p15_mediumVeto",
                       "h_single_displaced_L1Mu_rate_position_ME1_ME2_ME3_eta1p2to2p4_mediumVeto",

                       "h_single_displaced_L1Mu_rate_direction_MB1_MB4_eta0to0p9_mediumVeto",

                       "h_single_displaced_L1Mu_rate_direction_ME1_ME2_eta1p2to1p6_mediumVeto",
                       "h_single_displaced_L1Mu_rate_direction_ME1_ME2_eta1p2to2p15_mediumVeto",

                       "h_single_displaced_L1Mu_rate_hybrid_ME1_ME2_ME3_eta1p2to1p6_mediumVeto",
                       "h_single_displaced_L1Mu_rate_hybrid_ME1_ME2_ME3_eta1p2to2p15_mediumVeto",
                       "h_single_displaced_L1Mu_rate_hybrid_ME1_ME2_ME3_eta1p6to2p15_mediumVeto",

                       "h_single_displaced_L1Mu_rate_direction_GE11_ME11_GE21_ME21_eta1p6to2p15_mediumVeto",

                       "h_single_displaced_L1Mu_rate_hybrid_GE11_ME11_ME21_ME3_eta1p6to2p15_mediumVeto",
                       "h_single_displaced_L1Mu_rate_hybrid_GE11_ME11_GE21_ME21_ME3_eta1p6to2p15_mediumVeto",

                       ## displaced muons + tight TT isolation
                       "h_single_displaced_L1Mu_rate_position_ME1_ME2_ME3_eta1p2to1p6_tightVeto",
                       "h_single_displaced_L1Mu_rate_position_ME1_ME2_ME3_eta1p6to2p15_tightVeto",
                       "h_single_displaced_L1Mu_rate_position_ME1_ME2_ME3_eta1p2to2p4_tightVeto",

                       "h_single_displaced_L1Mu_rate_direction_MB1_MB4_eta0to0p9_tightVeto",

                       "h_single_displaced_L1Mu_rate_direction_ME1_ME2_eta1p2to1p6_tightVeto",
                       "h_single_displaced_L1Mu_rate_direction_ME1_ME2_eta1p2to2p15_tightVeto",

                       "h_single_displaced_L1Mu_rate_hybrid_ME1_ME2_ME3_eta1p2to1p6_tightVeto",
                       "h_single_displaced_L1Mu_rate_hybrid_ME1_ME2_ME3_eta1p2to2p15_tightVeto",
                       "h_single_displaced_L1Mu_rate_hybrid_ME1_ME2_ME3_eta1p6to2p15_tightVeto",

                       "h_single_displaced_L1Mu_rate_direction_GE11_ME11_GE21_ME21_eta1p6to2p15_tightVeto",

                       "h_single_displaced_L1Mu_rate_hybrid_GE11_ME11_GE21_ME21_ME3_eta1p6to2p15_tightVeto",
                       )


    maxEntries = ch.GetEntries()
    if doTest:
      maxEntries = 10000

    nEvents3stationPassPrompt = 0
    nEvents3stationPassDisplaced = 0

    nEvents = maxEntries
    print "nEvents", nEvents
    for k in range(0,nEvents):
      if k%1000==0: print "Processing event", k

      ch.GetEntry(k)
      treeHits = ch

      ## get the max value of the momentum
      pts = list(treeHits.L1Mu_pt)

      ## ignore events without L1Mu
      if len(pts)==0: continue

      minQuality = 4

      """
      fillDPhiHistogram( h_dphi_ME11_ME21, treeHits )
      fillDPhiHistogram( h_dphi_ME11_ME21_charge_Pt0to5, treeHits, 0, 5 )
      fillDPhiHistogram( h_dphi_ME11_ME21_charge_Pt7to140, treeHits, 7, 999 )
      fillDPhiHistogram( h_dphi_ME11_ME21_charge_Pt10to140, treeHits, 10, 999 )
      fillDPhiHistogram( h_dphi_ME11_ME21_charge_Pt15to140, treeHits, 15, 999 )
      fillDPhiHistogram( h_dphi_ME11_ME21_charge_Pt20to140, treeHits, 20, 999 )
      fillDPhiHistogram( h_dphi_ME11_ME21_charge_Pt30to140, treeHits, 30, 999 )
      """
      
      ## calibrate trigger rate
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_eta0to2p4"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_eta0to2p4"],
                          treeHits, True, 0.0, 2.4, 0, minQuality)

      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_eta1p1to2p4"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_eta1p1to2p4"],
                          treeHits, True, 1.1, 2.4, 0, minQuality)

      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_eta0to1p1"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_eta0to1p1"],
                          treeHits, True, 0.0, 1.1, 0, minQuality)
      ## overall rates
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_2_stubs_eta0to2p4"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_2_stubs_eta0to2p4"],
                          treeHits,True, 0.0, 2.4, 2, minQuality)
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_3_stubs_eta0to2p4"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_3_stubs_eta0to2p4"],
                          treeHits,True, 0.0, 2.4, 3, minQuality)

      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_eta1p2to2p4"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_eta1p2to2p4"],
                          treeHits, True, 1.2, 2.4, 0, minQuality)
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_2_stubs_eta1p2to2p4"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_2_stubs_eta1p2to2p4"],
                          treeHits, True, 1.2, 2.4, 2, minQuality)
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_3_stubs_eta1p2to2p4"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_3_stubs_eta1p2to2p4"],
                          treeHits, True, 1.2, 2.4, 3, minQuality)

      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_eta1p2to2p2"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_eta1p2to2p2"],
                          treeHits, True, 1.2, 2.2, 0, minQuality)
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_2_stubs_eta1p2to2p2"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_2_stubs_eta1p2to2p2"],
                          treeHits, True, 1.2, 2.2, 2, minQuality)
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_3_stubs_eta1p2to2p2"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_3_stubs_eta1p2to2p2"],
                          treeHits, True, 1.2, 2.2, 3, minQuality)

      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_eta1p6to2p2"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_eta1p6to2p2"],
                          treeHits, True, 1.6, 2.2, 0, minQuality)
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_2_stubs_eta1p6to2p2"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_2_stubs_eta1p6to2p2"],
                          treeHits, True, 1.6, 2.2, 2, minQuality)
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_3_stubs_eta1p6to2p2"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_3_stubs_eta1p6to2p2"],
                          treeHits, True, 1.6, 2.2, 3, minQuality)


      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_eta1p6to2p15"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_eta1p6to2p15"],
                          treeHits, True, 1.6, 2.15, 0, minQuality)
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_2_stubs_eta1p6to2p15"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_2_stubs_eta1p6to2p15"],
                          treeHits, True, 1.6, 2.15, 2, minQuality)
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_3_stubs_eta1p6to2p15"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_3_stubs_eta1p6to2p15"],
                          treeHits, True, 1.6, 2.15, 3, minQuality)


      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_eta1p2to1p6"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_eta1p2to1p6"],
                          treeHits, True, 1.2, 1.6, 0, minQuality)
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_2_stubs_eta1p2to1p6"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_2_stubs_eta1p2to1p6"],
                          treeHits, True, 1.2, 1.6, 2, minQuality)
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_3_stubs_eta1p2to1p6"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_3_stubs_eta1p2to1p6"],
                          treeHits, True, 1.2, 1.6, 3, minQuality)


      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_2_stubs_ME11_eta1p6to2p2"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_2_stubs_ME11_eta1p6to2p2"],
                          treeHits,True, 1.6, 2.2, 2, minQuality, hasME11Cut=True)
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_3_stubs_ME11_eta1p6to2p2"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_3_stubs_ME11_eta1p6to2p2"],
                          treeHits,True, 1.6, 2.2, 3, minQuality, hasME11Cut=True)


      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_2_stubs_ME11_eta1p6to2p15"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_2_stubs_ME11_eta1p6to2p15"],
                          treeHits,True, 1.6, 2.15, 2, minQuality, hasME11Cut=True)
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_3_stubs_ME11_eta1p6to2p15"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_3_stubs_ME11_eta1p6to2p15"],
                          treeHits,True, 1.6, 2.15, 3, minQuality, hasME11Cut=True)


      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_2_stubs_GE11_ME11_eta1p6to2p15"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_2_stubs_GE11_ME11_eta1p6to2p15"],
                          treeHits,True, 1.6, 2.15, 2, minQuality, hasME11Cut=True, hasGE11Cut=True)
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_3_stubs_GE11_ME11_eta1p6to2p15"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_3_stubs_GE11_ME11_eta1p6to2p15"],
                          treeHits,True, 1.6, 2.15, 3, minQuality, hasME11Cut=True, hasGE11Cut=True)

      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_2_stubs_GE11_ME11_GE21_ME21_eta1p6to2p15"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_2_stubs_GE11_ME11_GE21_ME21_eta1p6to2p15"],
                          treeHits,True, 1.6, 2.15, 2, minQuality, hasME11Cut=True, hasGE11Cut=True, hasME21Cut=True, hasGE21Cut=True)
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_3_stubs_GE11_ME11_GE21_ME21_eta1p6to2p15"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_3_stubs_GE11_ME11_GE21_ME21_eta1p6to2p15"],
                          treeHits,True, 1.6, 2.15, 3, minQuality, hasME11Cut=True, hasGE11Cut=True, hasME21Cut=True, hasGE21Cut=True)


      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_ME1_ME2_ME3_eta1p2to2p4"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_ME1_ME2_ME3_eta1p2to2p4"],
                          treeHits, True, 1.2, 2.4, 0, minQuality,
                          hasME1Cut=True, hasME2Cut=True, hasME3Cut=True)
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_ME1_ME2_ME3_eta1p2to2p2"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_ME1_ME2_ME3_eta1p2to2p2"],
                          treeHits, True, 1.2, 2.2, 0, minQuality,
                          hasME1Cut=True, hasME2Cut=True, hasME3Cut=True)
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_ME1_ME2_ME3_eta1p6to2p15"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_ME1_ME2_ME3_eta1p6to2p15"],
                          treeHits, True, 1.6, 2.15, 0, minQuality,
                          hasME1Cut=True, hasME2Cut=True, hasME3Cut=True)


      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_position_ME1_ME2_ME3_eta1p6to2p15"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_position_ME1_ME2_ME3_eta1p6to2p15"],
                                   treeHits, True, 1.6, 2.15, 0, minQuality, doPositionBased=True)
      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_position_ME1_ME2_ME3_eta1p2to2p4"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_position_ME1_ME2_ME3_eta1p2to2p4"],
                                   treeHits, True, 1.2, 2.4, 0, minQuality, doPositionBased=True)


      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_GE11_ME11_GE21_ME21_ME3_eta1p6to2p15"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_ME3_eta1p6to2p15"],
                          treeHits,True, 1.6, 2.15, 0, minQuality, hasME11Cut=True, hasME21Cut=True, hasGE11Cut=True, hasGE21Cut=True, hasME3Cut=True)
      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_hybrid_GE11_ME11_GE21_ME21_ME3_eta1p6to2p15"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_hybrid_GE11_ME11_GE21_ME21_ME3_eta1p6to2p15"],
                                   treeHits, True, 1.6, 2.15, 0, minQuality, doHybridBasedGE21=True)


      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_GE11_ME11_ME21_ME3_eta1p6to2p15"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_GE11_ME11_ME21_ME3_eta1p6to2p15"],
                          treeHits,True, 1.6, 2.15, 0, minQuality, hasME11Cut=True, hasME21Cut=True, hasGE11Cut=True, hasGE21Cut=False, hasME3Cut=True)
      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_hybrid_GE11_ME11_ME21_ME3_eta1p6to2p15"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_hybrid_GE11_ME11_ME21_ME3_eta1p6to2p15"],
                                   treeHits, True, 1.6, 2.15, 0, minQuality, doHybridBasedNoGE21=True)

      ## loose isolation
      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_position_ME1_ME2_ME3_eta1p6to2p15_looseVeto"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_position_ME1_ME2_ME3_eta1p6to2p15_looseVeto"],
                                   treeHits, True, 1.6, 2.15, 0, minQuality, doPositionBased=True, doVeto=True, vetoType=1)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_position_ME1_ME2_ME3_eta1p2to2p4_looseVeto"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_position_ME1_ME2_ME3_eta1p2to2p4_looseVeto"],
                                   treeHits, True, 1.2, 2.4, 0, minQuality, doPositionBased=True, doVeto=True, vetoType=1)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_position_ME1_ME2_ME3_eta1p2to1p6_looseVeto"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_position_ME1_ME2_ME3_eta1p2to1p6_looseVeto"],
                                   treeHits, True, 1.2, 1.6, 0, minQuality, doPositionBased=True, doVeto=True, vetoType=1)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_direction_ME1_ME2_eta1p2to1p6_looseVeto"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_direction_ME1_ME2_eta1p2to1p6_looseVeto"],
                                   treeHits, True, 1.2, 1.6, 0, minQuality, doDirectionBasedNoGE21=True, doVeto=True, vetoType=1)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_direction_ME1_ME2_eta1p2to2p15_looseVeto"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_direction_ME1_ME2_eta1p2to2p15_looseVeto"],
                                   treeHits, True, 1.2, 2.15, 0, minQuality, doDirectionBasedNoGE21=True,doVeto=True, vetoType=1)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_direction_GE11_ME11_GE21_ME21_eta1p6to2p15_looseVeto"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_direction_GE11_ME11_GE21_ME21_eta1p6to2p15_looseVeto"],
                                   treeHits, True, 1.6, 2.15, 0, minQuality, doDirectionBasedGE21=True, doVeto=True, vetoType=1)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_hybrid_GE11_ME11_GE21_ME21_ME3_eta1p6to2p15_looseVeto"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_hybrid_GE11_ME11_GE21_ME21_ME3_eta1p6to2p15_looseVeto"],
                                   treeHits, True, 1.6, 2.15, 0, minQuality, doHybridBasedGE21=True, doVeto=True, vetoType=1)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_hybrid_ME1_ME2_ME3_eta1p2to2p15_looseVeto"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_hybrid_ME1_ME2_ME3_eta1p2to2p15_looseVeto"],
                                   treeHits, True, 1.2, 2.15, 0, minQuality, doHybridBasedNoGE21=True, doVeto=True, vetoType=1)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_hybrid_GE11_ME11_ME21_ME3_eta1p6to2p15_looseVeto"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_hybrid_GE11_ME11_ME21_ME3_eta1p6to2p15_looseVeto"],
                                   treeHits, True, 1.6, 2.15, 0, minQuality, doHybridBasedNoGE21=True, doVeto=True, vetoType=1)

      ## medium isolation
      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_position_ME1_ME2_ME3_eta1p6to2p15_mediumVeto"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_position_ME1_ME2_ME3_eta1p6to2p15_mediumVeto"],
                                   treeHits, True, 1.6, 2.15, 0, minQuality, doPositionBased=True, doVeto=True, vetoType=2)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_position_ME1_ME2_ME3_eta1p2to2p4_mediumVeto"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_position_ME1_ME2_ME3_eta1p2to2p4_mediumVeto"],
                                   treeHits, True, 1.2, 2.4, 0, minQuality, doPositionBased=True, doVeto=True, vetoType=2)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_position_ME1_ME2_ME3_eta1p2to1p6_mediumVeto"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_position_ME1_ME2_ME3_eta1p2to1p6_mediumVeto"],
                                   treeHits, True, 1.2, 1.6, 0, minQuality, doPositionBased=True, doVeto=True, vetoType=2)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_direction_ME1_ME2_eta1p2to1p6_mediumVeto"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_direction_ME1_ME2_eta1p2to1p6_mediumVeto"],
                                   treeHits, True, 1.2, 1.6, 0, minQuality, doDirectionBasedNoGE21=True, doVeto=True, vetoType=2)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_direction_ME1_ME2_eta1p2to2p15_mediumVeto"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_direction_ME1_ME2_eta1p2to2p15_mediumVeto"],
                                   treeHits, True, 1.2, 2.15, 0, minQuality, doDirectionBasedNoGE21=True, doVeto=True, vetoType=2)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_direction_GE11_ME11_GE21_ME21_eta1p6to2p15_mediumVeto"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_direction_GE11_ME11_GE21_ME21_eta1p6to2p15_mediumVeto"],
                                   treeHits, True, 1.6, 2.15, 0, minQuality, doDirectionBasedGE21=True, doVeto=True, vetoType=2)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_hybrid_ME1_ME2_ME3_eta1p2to2p15_mediumVeto"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_hybrid_ME1_ME2_ME3_eta1p2to2p15_mediumVeto"],
                                   treeHits, True, 1.2, 2.15, 0, minQuality, doHybridBasedNoGE21=True, doVeto=True, vetoType=2)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_hybrid_GE11_ME11_GE21_ME21_ME3_eta1p6to2p15_mediumVeto"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_hybrid_GE11_ME11_GE21_ME21_ME3_eta1p6to2p15_mediumVeto"],
                                   treeHits, True, 1.6, 2.15, 0, minQuality, doHybridBasedGE21=True, doVeto=True, vetoType=2)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_hybrid_GE11_ME11_ME21_ME3_eta1p6to2p15_mediumVeto"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_hybrid_GE11_ME11_ME21_ME3_eta1p6to2p15_mediumVeto"],
                                   treeHits, True, 1.6, 2.15, 0, minQuality, doHybridBasedNoGE21=True, doVeto=True, vetoType=2)


                                   

      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_GE11_ME11_OR_GE21_ME21_eta1p6to2p15"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_GE11_ME11_OR_GE21_ME21_eta1p6to2p15"],
                          treeHits,True, 1.6, 2.15, 0, minQuality, hasME11ME21Cut=True, hasGE11GE21Cut=True)
      continue

      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_2_stubs_GE11_ME11_OR_GE21_ME21_eta1p6to2p15"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_2_stubs_GE11_ME11_OR_GE21_ME21_eta1p6to2p15"],
                          treeHits,True, 1.6, 2.15, 2, minQuality, hasME11ME21Cut=True, hasGE11GE21Cut=True)
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_3_stubs_GE11_ME11_OR_GE21_ME21_eta1p6to2p15"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_3_stubs_GE11_ME11_OR_GE21_ME21_eta1p6to2p15"],
                          treeHits,True, 1.6, 2.15, 3, minQuality, hasME11ME21Cut=True, hasGE11GE21Cut=True)


      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_2_stubs_ME21_eta1p6to2p2"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_2_stubs_ME21_eta1p6to2p2"],
                          treeHits,True, 1.6, 2.2, 2, minQuality, hasME21Cut=True)
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_3_stubs_ME21_eta1p6to2p2"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_3_stubs_ME21_eta1p6to2p2"],
                          treeHits,True, 1.6, 2.2, 3, minQuality, hasME21Cut=True)




      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_GE11_ME11_ME21_ME3_eta1p6to2p2"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_GE11_ME11_ME21_ME3_eta1p6to2p2"],
                          treeHits, True, 1.6, 2.2, 0, minQuality,
                          hasGE11Cut=True, hasME11Cut=True, hasME21Cut=True, hasME3Cut=True)



      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_2_stubs_ME11orME21_eta1p6to2p2"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_2_stubs_ME11orME21_eta1p6to2p2"],
                          treeHits,True, 1.6, 2.2, 2, minQuality, hasME11ME21Cut=True)
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_3_stubs_ME11orME21_eta1p6to2p2"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_3_stubs_ME11orME21_eta1p6to2p2"],
                          treeHits,True, 1.6, 2.2, 3, minQuality, hasME11ME21Cut=True)

      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_2_stubs_ME11_Fail10p_eta1p6to2p2"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_2_stubs_ME11_Fail10p_eta1p6to2p2"],
                          treeHits,True, 1.6, 2.2, 2, minQuality, hasME11Cut=True, ME11FailRate=0.1)
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_3_stubs_ME11_Fail10p_eta1p6to2p2"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_3_stubs_ME11_Fail10p_eta1p6to2p2"],
                          treeHits,True, 1.6, 2.2, 3, minQuality, hasME11Cut=True, ME11FailRate=0.1)
      """
      ## barrel rates
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_eta0to0p9"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_eta0to0p9"],
                          treeHits, True, 0.0, 0.9, 0, minQuality)
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_MB1_MB4_eta0to0p9"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_MB1_MB4_eta0to0p9"],
                          treeHits, True, 0.0, 0.9, 0, minQuality,
                          hasMB1Cut=True, hasMB4Cut=True)

      """
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_2_stubs_GE11_GE21_eta1p6to2p2"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_2_stubs_GE11_GE21_eta1p6to2p2"],
                          treeHits,True, 1.6, 2.15, 2, minQuality, hasME11Cut=True, hasGE11Cut=True)
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_3_stubs_GE11_GE21_eta1p6to2p2"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_3_stubs_GE11_GE21_eta1p6to2p2"],
                          treeHits,True, 1.6, 2.15, 3, minQuality, hasME11Cut=True, hasGE11Cut=True)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_direction_GE11_ME11_GE21_ME21_eta1p6to2p15"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_direction_GE11_ME11_GE21_ME21_eta1p6to2p15"],
                                   treeHits, True, 1.6, 2.15, 0, minQuality, doDirectionBasedGE21=True)


      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_2_stubs_GE21_ME21_eta1p6to2p2"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_2_stubs_GE21_ME21_eta1p6to2p2"],
                          treeHits,True, 1.6, 2.15, 2, minQuality, hasME21Cut=True, hasGE21Cut=True)
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_3_stubs_GE21_ME21_eta1p6to2p2"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_3_stubs_GE21_ME21_eta1p6to2p2"],
                          treeHits,True, 1.6, 2.15, 3, minQuality, hasME21Cut=True, hasGE21Cut=True)

      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_GE11_ME11_GE21_ME21_eta1p6to2p2"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta1p6to2p2"],
                          treeHits,True, 1.6, 2.15, 0, minQuality, hasME11Cut=True, hasME21Cut=True, hasGE11Cut=True, hasGE21Cut=True)


      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_GE11_ME11_GE21_ME21_eta16to20"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20"],
                          treeHits,True, 1.6, 2.0, 0, minQuality, hasME11Cut=True, hasME21Cut=True, hasGE11Cut=True, hasGE21Cut=True)

      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_GE11_ME11_GE21_ME21_ME3_eta16to20"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_ME3_eta16to20"],
                          treeHits,True, 1.6, 2.0, 0, minQuality, hasME11Cut=True, hasME21Cut=True, hasGE11Cut=True, hasGE21Cut=True, hasME3Cut=True)

      ## displaced L1Mu trigger rate curves
      #fillDisplacedPtHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_MB1_MB4_eta0to0p9"], treeHits, True, 0.0, 0.9, 0, minQuality, hasMB1Cut=True, hasMB4Cut=True)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_position_ME1_ME2_ME3_eta1p2to1p6"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_position_ME1_ME2_ME3_eta1p2to1p6"],
                                   treeHits, True, 1.2, 1.6, 0, minQuality, doPositionBased=True)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_direction_ME1_ME2_eta1p2to1p6"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_direction_ME1_ME2_eta1p2to1p6"],
                                   treeHits, True, 1.2, 1.6, 0, minQuality, doDirectionBasedNoGE21=True)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_direction_ME1_ME2_eta1p2to2p2"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_direction_ME1_ME2_eta1p2to2p2"],
                                   treeHits, True, 1.2, 2.15, 0, minQuality, doDirectionBasedNoGE21=True)


      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_hybrid_GE11_ME11_ME21_ME3_eta1p2to2p2"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_hybrid_GE11_ME11_ME21_ME3_eta1p2to2p2"],
                                   treeHits, True, 1.2, 2.15, 0, minQuality, doHybridBasedNoGE21=True)




      ## tight isolation
      """
      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_position_ME1_ME2_ME3_eta1p6to2p15_tightVeto"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_position_ME1_ME2_ME3_eta1p6to2p15_tightVeto"],
                                   treeHits, True, 1.6, 2.15, 0, minQuality, doPositionBased=True, doVeto=True, vetoType=3)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_position_ME1_ME2_ME3_eta1p2to2p4_tightVeto"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_position_ME1_ME2_ME3_eta1p2to2p4_tightVeto"],
                                   treeHits, True, 1.2, 2.4, 0, minQuality, doPositionBased=True, doVeto=True, vetoType=3)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_position_ME1_ME2_ME3_eta1p2to1p6_tightVeto"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_position_ME1_ME2_ME3_eta1p2to1p6_tightVeto"],
                                   treeHits, True, 1.2, 1.6, 0, minQuality, doPositionBased=True, doVeto=True, vetoType=3)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_direction_ME1_ME2_eta1p2to1p6_tightVeto"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_direction_ME1_ME2_eta1p2to1p6_tightVeto"],
                                   treeHits, True, 1.2, 1.6, 0, minQuality, doDirectionBasedNoGE21=True, doVeto=True, vetoType=3)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_direction_ME1_ME2_eta1p2to2p2_tightVeto"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_direction_ME1_ME2_eta1p2to2p2_tightVeto"],
                                   treeHits, True, 1.2, 2.15, 0, minQuality, doDirectionBasedNoGE21=True, doVeto=True, vetoType=3)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_direction_GE11_ME11_GE21_ME21_eta1p6to2p15_tightVeto"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_direction_GE11_ME11_GE21_ME21_eta1p6to2p15_tightVeto"],
                                   treeHits, True, 1.6, 2.15, 0, minQuality, doDirectionBasedGE21=True, doVeto=True, vetoType=3)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_hybrid_GE11_ME11_GE21_ME21_ME3_eta1p6to2p15_tightVeto"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_hybrid_GE11_ME11_GE21_ME21_ME3_eta1p6to2p15_tightVeto"],
                                   treeHits, True, 1.6, 2.15, 0, minQuality, doHybridBasedGE21=True, doVeto=True, vetoType=3)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_hybrid_ME1_ME2_ME3_eta1p2to2p2_tightVeto"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_hybrid_ME1_ME2_ME3_eta1p2to2p2_tightVeto"],
                                   treeHits, True, 1.2, 2.15, 0, minQuality, doHybridBasedNoGE21=True, doVeto=True, vetoType=3)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_hybrid_GE11_ME1_ME2_ME3_eta1p6to2p15_tightVeto"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_hybrid_GE11_ME1_ME2_ME3_eta1p6to2p15_tightVeto"],
                                   treeHits, True, 1.6, 2.15, 0, minQuality, doHybridBasedNoGE21=True, doVeto=True, vetoType=3)

      """

    ## output ROOT file
    
    f.Write();
    f.Close();

    exit()

  displacedL1MuHybridTriggerRate()

