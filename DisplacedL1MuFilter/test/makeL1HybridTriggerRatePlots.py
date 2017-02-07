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

  ## extension for figures - add more?
  ext = ".png"

  ## Style
  gStyle.SetStatStyle(0)

  print "Making the plots"

  set_style()

  doTest = True

  ch = TChain("DisplacedL1MuFilter_PhaseIIGE21/L1MuTree")

  location0 = '/eos/uscms/store/user/lpcgem/Neutrino_Pt2to20_gun/NeutrinoGun_14TeV_PU140_L1MuANA_v25_StubReco/170127_001407/0000/'
  location1 = '/eos/uscms/store/user/lpcgem/Neutrino_Pt2to20_gun/NeutrinoGun_14TeV_PU140_L1MuANA_v25_StubReco/170127_001407/0001/'
  location2 = '/eos/uscms/store/user/lpcgem/Neutrino_Pt2to20_gun/NeutrinoGun_14TeV_PU140_L1MuANA_v25_StubReco/170127_001407/0002/'

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
                       "h_single_prompt_L1Mu_rate_eta00to09",
                       "h_single_prompt_L1Mu_rate_eta00to24",
                       "h_single_prompt_L1Mu_rate_eta12to24",
                       "h_single_prompt_L1Mu_rate_eta16to22",
                       "h_single_prompt_L1Mu_rate_eta16to20",
                       "h_single_prompt_L1Mu_rate_eta12to16",
                       "h_single_prompt_L1Mu_rate_eta12to22",

                       "h_single_prompt_L1Mu_rate_2_stubs_eta00to24",
                       "h_single_prompt_L1Mu_rate_3_stubs_eta00to24",

                       "h_single_prompt_L1Mu_rate_2_stubs_eta12to24",
                       "h_single_prompt_L1Mu_rate_3_stubs_eta12to24",

                       "h_single_prompt_L1Mu_rate_2_stubs_eta16to22",
                       "h_single_prompt_L1Mu_rate_3_stubs_eta16to22",

                       "h_single_prompt_L1Mu_rate_2_stubs_eta12to16",
                       "h_single_prompt_L1Mu_rate_3_stubs_eta12to16",

                       ## explicit stub requirement
                       "h_single_prompt_L1Mu_rate_MB1_MB4_eta00to09",

                       "h_single_prompt_L1Mu_rate_ME1_ME2_ME3_eta12to24",
                       "h_single_prompt_L1Mu_rate_ME1_ME2_ME3_eta16to22",
                       "h_single_prompt_L1Mu_rate_ME1_ME2_ME3_eta12to22",

                       "h_single_prompt_L1Mu_rate_2_stubs_ME11_eta16to22",
                       "h_single_prompt_L1Mu_rate_3_stubs_ME11_eta16to22",

                       "h_single_prompt_L1Mu_rate_2_stubs_ME21_eta16to22",
                       "h_single_prompt_L1Mu_rate_3_stubs_ME21_eta16to22",

                       "h_single_prompt_L1Mu_rate_2_stubs_ME11orME21_eta16to22",
                       "h_single_prompt_L1Mu_rate_3_stubs_ME11orME21_eta16to22",

                       ## with GEMs
                       "h_single_prompt_L1Mu_rate_2_stubs_GE11_ME11_eta16to22",
                       "h_single_prompt_L1Mu_rate_3_stubs_GE11_ME11_eta16to22",

                       "h_single_prompt_L1Mu_rate_2_stubs_GE21_ME21_eta16to22",
                       "h_single_prompt_L1Mu_rate_3_stubs_GE21_ME21_eta16to22",

                       "h_single_prompt_L1Mu_rate_GE11_ME11_GE21_ME21_eta16to22",
                       "h_single_prompt_L1Mu_rate_GE11_ME1_ME2_ME3_eta16to22",

                       "h_single_prompt_L1Mu_rate_2_stubs_GE11_ME11_OR_GE21_ME21_eta16to22",
                       "h_single_prompt_L1Mu_rate_3_stubs_GE11_ME11_OR_GE21_ME21_eta16to22",

                       "h_single_prompt_L1Mu_rate_GE11_ME11_GE21_ME21_eta16to20",
                       "h_single_prompt_L1Mu_rate_GE11_ME11_GE21_ME21_ME3_eta16to22",
                       "h_single_prompt_L1Mu_rate_GE11_ME11_ME21_ME3_eta16to22",

                       ## failing stations
                       "h_single_prompt_L1Mu_rate_2_stubs_ME11_Fail10p_eta16to22",
                       "h_single_prompt_L1Mu_rate_3_stubs_ME11_Fail10p_eta16to22",

                       "h_single_prompt_L1Mu_rate_2_stubs_ME11_Fail10p_GE11_eta16to22",
                       "h_single_prompt_L1Mu_rate_3_stubs_ME11_Fail10p_GE11_eta16to22",

                       "h_single_prompt_L1Mu_rate_2_stubs_ME21_Fail10p_eta16to22",
                       "h_single_prompt_L1Mu_rate_3_stubs_ME21_Fail10p_eta16to22",

                       "h_single_prompt_L1Mu_rate_2_stubs_ME21_Fail10p_GE21_eta16to22",
                       "h_single_prompt_L1Mu_rate_3_stubs_ME21_Fail10p_GE21_eta16to22",

                       ## displaced muons
                       "h_single_displaced_L1Mu_rate_position_ME1_ME2_ME3_eta12to16",
                       "h_single_displaced_L1Mu_rate_position_ME1_ME2_ME3_eta16to22",
                       "h_single_displaced_L1Mu_rate_position_ME1_ME2_ME3_eta12to24",

                       "h_single_displaced_L1Mu_rate_direction_MB1_MB4_eta00to09",

                       "h_single_displaced_L1Mu_rate_direction_ME1_ME2_eta12to16",
                       "h_single_displaced_L1Mu_rate_direction_ME1_ME2_eta12to22",

                       "h_single_displaced_L1Mu_rate_hybrid_ME1_ME2_ME3_eta12to16",
                       "h_single_displaced_L1Mu_rate_hybrid_ME1_ME2_ME3_eta12to22",
                       "h_single_displaced_L1Mu_rate_hybrid_ME1_ME2_ME3_eta16to22",

                       "h_single_displaced_L1Mu_rate_direction_GE11_ME11_GE21_ME21_eta16to22",

                       "h_single_displaced_L1Mu_rate_hybrid_GE11_ME11_ME21_ME3_eta16to22",
                       "h_single_displaced_L1Mu_rate_hybrid_GE11_ME11_GE21_ME21_ME3_eta16to22",

                       ## displaced muons + loose TT isolation
                       "h_single_displaced_L1Mu_rate_position_ME1_ME2_ME3_eta12to16_looseVeto",
                       "h_single_displaced_L1Mu_rate_position_ME1_ME2_ME3_eta16to22_looseVeto",
                       "h_single_displaced_L1Mu_rate_position_ME1_ME2_ME3_eta12to24_looseVeto",

                       "h_single_displaced_L1Mu_rate_direction_MB1_MB4_eta00to09_looseVeto",

                       "h_single_displaced_L1Mu_rate_direction_ME1_ME2_eta12to16_looseVeto",
                       "h_single_displaced_L1Mu_rate_direction_ME1_ME2_eta12to22_looseVeto",

                       "h_single_displaced_L1Mu_rate_hybrid_ME1_ME2_ME3_eta12to16_looseVeto",
                       "h_single_displaced_L1Mu_rate_hybrid_ME1_ME2_ME3_eta12to22_looseVeto",
                       "h_single_displaced_L1Mu_rate_hybrid_ME1_ME2_ME3_eta16to22_looseVeto",

                       "h_single_displaced_L1Mu_rate_direction_GE11_ME11_GE21_ME21_eta16to22_looseVeto",

                       "h_single_displaced_L1Mu_rate_hybrid_GE11_ME11_ME21_ME3_eta16to22_looseVeto",
                       "h_single_displaced_L1Mu_rate_hybrid_GE11_ME11_GE21_ME21_ME3_eta16to22_looseVeto",

                       ## displaced muons + medium TT isolation
                       "h_single_displaced_L1Mu_rate_position_ME1_ME2_ME3_eta12to16_mediumVeto",
                       "h_single_displaced_L1Mu_rate_position_ME1_ME2_ME3_eta16to22_mediumVeto",
                       "h_single_displaced_L1Mu_rate_position_ME1_ME2_ME3_eta12to24_mediumVeto",

                       "h_single_displaced_L1Mu_rate_direction_MB1_MB4_eta00to09_mediumVeto",

                       "h_single_displaced_L1Mu_rate_direction_ME1_ME2_eta12to16_mediumVeto",
                       "h_single_displaced_L1Mu_rate_direction_ME1_ME2_eta12to22_mediumVeto",

                       "h_single_displaced_L1Mu_rate_hybrid_ME1_ME2_ME3_eta12to16_mediumVeto",
                       "h_single_displaced_L1Mu_rate_hybrid_ME1_ME2_ME3_eta12to22_mediumVeto",
                       "h_single_displaced_L1Mu_rate_hybrid_ME1_ME2_ME3_eta16to22_mediumVeto",

                       "h_single_displaced_L1Mu_rate_direction_GE11_ME11_GE21_ME21_eta16to22_mediumVeto",

                       "h_single_displaced_L1Mu_rate_hybrid_GE11_ME11_ME21_ME3_eta16to22_mediumVeto",
                       "h_single_displaced_L1Mu_rate_hybrid_GE11_ME11_GE21_ME21_ME3_eta16to22_mediumVeto",

                       ## displaced muons + tight TT isolation
                       "h_single_displaced_L1Mu_rate_position_ME1_ME2_ME3_eta12to16_tightVeto",
                       "h_single_displaced_L1Mu_rate_position_ME1_ME2_ME3_eta16to22_tightVeto",
                       "h_single_displaced_L1Mu_rate_position_ME1_ME2_ME3_eta12to24_tightVeto",

                       "h_single_displaced_L1Mu_rate_direction_MB1_MB4_eta00to09_tightVeto",

                       "h_single_displaced_L1Mu_rate_direction_ME1_ME2_eta12to16_tightVeto",
                       "h_single_displaced_L1Mu_rate_direction_ME1_ME2_eta12to22_tightVeto",

                       "h_single_displaced_L1Mu_rate_hybrid_ME1_ME2_ME3_eta12to16_tightVeto",
                       "h_single_displaced_L1Mu_rate_hybrid_ME1_ME2_ME3_eta12to22_tightVeto",
                       "h_single_displaced_L1Mu_rate_hybrid_ME1_ME2_ME3_eta16to22_tightVeto",

                       "h_single_displaced_L1Mu_rate_direction_GE11_ME11_GE21_ME21_eta16to22_tightVeto",

                       "h_single_displaced_L1Mu_rate_hybrid_GE11_ME11_GE21_ME21_ME3_eta16to22_tightVeto",
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

      fillDPhiHistogram( h_dphi_ME11_ME21, treeHits )
      fillDPhiHistogram( h_dphi_ME11_ME21_charge_Pt0to5, treeHits, 0, 5 )
      fillDPhiHistogram( h_dphi_ME11_ME21_charge_Pt7to140, treeHits, 7, 999 )
      fillDPhiHistogram( h_dphi_ME11_ME21_charge_Pt10to140, treeHits, 10, 999 )
      fillDPhiHistogram( h_dphi_ME11_ME21_charge_Pt15to140, treeHits, 15, 999 )
      fillDPhiHistogram( h_dphi_ME11_ME21_charge_Pt20to140, treeHits, 20, 999 )
      fillDPhiHistogram( h_dphi_ME11_ME21_charge_Pt30to140, treeHits, 30, 999 )

      ## overall rates
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_eta12to22"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_eta12to22"],
                          treeHits, True, 1.2, 2.15, 0, minQuality)

      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_eta00to24"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_eta00to24"],
                          treeHits, True, 0.0, 2.4, 0, minQuality)
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_2_stubs_eta00to24"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_2_stubs_eta00to24"],
                          treeHits,True, 0.0, 2.4, 2, minQuality)
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_3_stubs_eta00to24"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_3_stubs_eta00to24"],
                          treeHits,True, 0.0, 2.4, 3, minQuality)

      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_eta12to24"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_eta12to24"],
                          treeHits, True, 1.2, 2.4, 0, minQuality)
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_2_stubs_eta12to24"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_2_stubs_eta12to24"],
                          treeHits, True, 1.2, 2.4, 2, minQuality)
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_3_stubs_eta12to24"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_3_stubs_eta12to24"],
                          treeHits, True, 1.2, 2.4, 3, minQuality)

      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_eta16to22"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_eta16to22"],
                          treeHits, True, 1.6, 2.2, 0, minQuality)
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_eta16to20"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_eta16to20"],
                          treeHits, True, 1.6, 2.2, 0, minQuality)
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_2_stubs_eta16to22"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_2_stubs_eta16to22"],
                          treeHits, True, 1.6, 2.2, 2, minQuality)
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_3_stubs_eta16to22"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_3_stubs_eta16to22"],
                          treeHits, True, 1.6, 2.2, 3, minQuality)

      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_eta12to16"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_eta12to16"],
                          treeHits, True, 1.2, 1.6, 0, minQuality)
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_2_stubs_eta12to16"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_2_stubs_eta12to16"],
                          treeHits, True, 1.2, 1.6, 2, minQuality)
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_3_stubs_eta12to16"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_3_stubs_eta12to16"],
                          treeHits, True, 1.2, 1.6, 3, minQuality)

      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_ME1_ME2_ME3_eta12to24"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_ME1_ME2_ME3_eta12to24"],
                          treeHits, True, 1.2, 2.4, 0, minQuality,
                          hasME1Cut=True, hasME2Cut=True, hasME3Cut=True)
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_ME1_ME2_ME3_eta16to22"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_ME1_ME2_ME3_eta16to22"],
                          treeHits, True, 1.6, 2.15, 0, minQuality,
                          hasME1Cut=True, hasME2Cut=True, hasME3Cut=True)
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_GE11_ME11_ME21_ME3_eta16to22"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_GE11_ME11_ME21_ME3_eta16to22"],
                          treeHits, True, 1.6, 2.15, 0, minQuality,
                          hasGE11Cut=True, hasME11Cut=True, hasME21Cut=True, hasME3Cut=True)
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_ME1_ME2_ME3_eta12to22"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_ME1_ME2_ME3_eta12to22"],
                          treeHits, True, 1.2, 2.15, 0, minQuality,
                          hasME1Cut=True, hasME2Cut=True, hasME3Cut=True)

      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_2_stubs_ME11_eta16to22"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_2_stubs_ME11_eta16to22"],
                          treeHits,True, 1.6, 2.15, 2, minQuality, hasME11Cut=True)
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_3_stubs_ME11_eta16to22"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_3_stubs_ME11_eta16to22"],
                          treeHits,True, 1.6, 2.15, 3, minQuality, hasME11Cut=True)

      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_2_stubs_ME21_eta16to22"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_2_stubs_ME21_eta16to22"],
                          treeHits,True, 1.6, 2.2, 2, minQuality, hasME21Cut=True)
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_3_stubs_ME21_eta16to22"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_3_stubs_ME21_eta16to22"],
                          treeHits,True, 1.6, 2.2, 3, minQuality, hasME21Cut=True)


      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_2_stubs_ME11orME21_eta16to22"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_2_stubs_ME11orME21_eta16to22"],
                          treeHits,True, 1.6, 2.2, 2, minQuality, hasME11ME21Cut=True)
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_3_stubs_ME11orME21_eta16to22"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_3_stubs_ME11orME21_eta16to22"],
                          treeHits,True, 1.6, 2.2, 3, minQuality, hasME11ME21Cut=True)

      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_2_stubs_ME11_Fail10p_eta16to22"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_2_stubs_ME11_Fail10p_eta16to22"],
                          treeHits,True, 1.6, 2.2, 2, minQuality, hasME11Cut=True, ME11FailRate=0.1)
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_3_stubs_ME11_Fail10p_eta16to22"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_3_stubs_ME11_Fail10p_eta16to22"],
                          treeHits,True, 1.6, 2.2, 3, minQuality, hasME11Cut=True, ME11FailRate=0.1)
      """
      ## barrel rates
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_eta00to09"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_eta00to09"],
                          treeHits, True, 0.0, 0.9, 0, minQuality)
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_MB1_MB4_eta00to09"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_MB1_MB4_eta00to09"],
                          treeHits, True, 0.0, 0.9, 0, minQuality,
                          hasMB1Cut=True, hasMB4Cut=True)

      """
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_2_stubs_GE11_GE21_eta16to22"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_2_stubs_GE11_GE21_eta16to22"],
                          treeHits,True, 1.6, 2.15, 2, minQuality, hasME11Cut=True, hasGE11Cut=True)
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_3_stubs_GE11_GE21_eta16to22"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_3_stubs_GE11_GE21_eta16to22"],
                          treeHits,True, 1.6, 2.15, 3, minQuality, hasME11Cut=True, hasGE11Cut=True)


      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_2_stubs_GE11_ME11_eta16to22"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_2_stubs_GE11_ME11_eta16to22"],
                          treeHits,True, 1.6, 2.15, 2, minQuality, hasME11Cut=True, hasGE11Cut=True)
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_3_stubs_GE11_ME11_eta16to22"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_3_stubs_GE11_ME11_eta16to22"],
                          treeHits,True, 1.6, 2.15, 3, minQuality, hasME11Cut=True, hasGE11Cut=True)

      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_2_stubs_GE21_ME21_eta16to22"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_2_stubs_GE21_ME21_eta16to22"],
                          treeHits,True, 1.6, 2.15, 2, minQuality, hasME21Cut=True, hasGE21Cut=True)
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_3_stubs_GE21_ME21_eta16to22"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_3_stubs_GE21_ME21_eta16to22"],
                          treeHits,True, 1.6, 2.15, 3, minQuality, hasME21Cut=True, hasGE21Cut=True)

      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_2_stubs_GE11_ME11_OR_GE21_ME21_eta16to22"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_2_stubs_GE11_ME11_OR_GE21_ME21_eta16to22"],
                          treeHits,True, 1.6, 2.15, 2, minQuality, hasME11ME21Cut=True, hasGE11GE21Cut=True)
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_3_stubs_GE11_ME11_OR_GE21_ME21_eta16to22"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_3_stubs_GE11_ME11_OR_GE21_ME21_eta16to22"],
                          treeHits,True, 1.6, 2.15, 3, minQuality, hasME11ME21Cut=True, hasGE11GE21Cut=True)


      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_GE11_ME11_GE21_ME21_eta16to22"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to22"],
                          treeHits,True, 1.6, 2.15, 0, minQuality, hasME11Cut=True, hasME21Cut=True, hasGE11Cut=True, hasGE21Cut=True)

      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_GE11_ME11_GE21_ME21_ME3_eta16to22"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_ME3_eta16to22"],
                          treeHits,True, 1.6, 2.15, 0, minQuality, hasME11Cut=True, hasME21Cut=True, hasGE11Cut=True, hasGE21Cut=True, hasME3Cut=True)

      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_GE11_ME11_GE21_ME21_eta16to20"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20"],
                          treeHits,True, 1.6, 2.0, 0, minQuality, hasME11Cut=True, hasME21Cut=True, hasGE11Cut=True, hasGE21Cut=True)

      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_GE11_ME11_GE21_ME21_ME3_eta16to20"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_ME3_eta16to20"],
                          treeHits,True, 1.6, 2.0, 0, minQuality, hasME11Cut=True, hasME21Cut=True, hasGE11Cut=True, hasGE21Cut=True, hasME3Cut=True)

      ## displaced L1Mu trigger rate curves
      #fillDisplacedPtHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_MB1_MB4_eta00to09"], treeHits, True, 0.0, 0.9, 0, minQuality, hasMB1Cut=True, hasMB4Cut=True)
      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_position_ME1_ME2_ME3_eta16to22"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_position_ME1_ME2_ME3_eta16to22"],
                                   treeHits, True, 1.6, 2.15, 0, minQuality, doPositionBased=True)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_position_ME1_ME2_ME3_eta12to24"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_position_ME1_ME2_ME3_eta12to24"],
                                   treeHits, True, 1.2, 2.4, 0, minQuality, doPositionBased=True)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_position_ME1_ME2_ME3_eta12to16"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_position_ME1_ME2_ME3_eta12to16"],
                                   treeHits, True, 1.2, 1.6, 0, minQuality, doPositionBased=True)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_direction_ME1_ME2_eta12to16"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_direction_ME1_ME2_eta12to16"],
                                   treeHits, True, 1.2, 1.6, 0, minQuality, doDirectionBasedNoGE21=True)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_direction_ME1_ME2_eta12to22"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_direction_ME1_ME2_eta12to22"],
                                   treeHits, True, 1.2, 2.15, 0, minQuality, doDirectionBasedNoGE21=True)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_direction_GE11_ME11_GE21_ME21_eta16to22"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_direction_GE11_ME11_GE21_ME21_eta16to22"],
                                   treeHits, True, 1.6, 2.15, 0, minQuality, doDirectionBasedGE21=True)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_hybrid_GE11_ME11_ME21_ME3_eta12to22"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_hybrid_GE11_ME11_ME21_ME3_eta12to22"],
                                   treeHits, True, 1.2, 2.15, 0, minQuality, doHybridBasedNoGE21=True)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_hybrid_GE11_ME11_GE21_ME21_ME3_eta16to22"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_hybrid_GE11_ME11_GE21_ME21_ME3_eta16to22"],
                                   treeHits, True, 1.6, 2.15, 0, minQuality, doHybridBasedGE21=True)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_hybrid_GE11_ME11_ME21_ME3_eta16to22"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_hybrid_GE11_ME11_ME21_ME3_eta16to22"],
                                   treeHits, True, 1.6, 2.15, 0, minQuality, doHybridBasedNoGE21=True)

      ## loose isolation
      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_position_ME1_ME2_ME3_eta16to22_looseVeto"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_position_ME1_ME2_ME3_eta16to22_looseVeto"],
                                   treeHits, True, 1.6, 2.15, 0, minQuality, doPositionBased=True, doVeto=True, vetoType=1)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_position_ME1_ME2_ME3_eta12to24_looseVeto"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_position_ME1_ME2_ME3_eta12to24_looseVeto"],
                                   treeHits, True, 1.2, 2.4, 0, minQuality, doPositionBased=True, doVeto=True, vetoType=1)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_position_ME1_ME2_ME3_eta12to16_looseVeto"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_position_ME1_ME2_ME3_eta12to16_looseVeto"],
                                   treeHits, True, 1.2, 1.6, 0, minQuality, doPositionBased=True, doVeto=True, vetoType=1)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_direction_ME1_ME2_eta12to16_looseVeto"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_direction_ME1_ME2_eta12to16_looseVeto"],
                                   treeHits, True, 1.2, 1.6, 0, minQuality, doDirectionBasedNoGE21=True, doVeto=True, vetoType=1)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_direction_ME1_ME2_eta12to22_looseVeto"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_direction_ME1_ME2_eta12to22_looseVeto"],
                                   treeHits, True, 1.2, 2.15, 0, minQuality, doDirectionBasedNoGE21=True, doVeto=True, vetoType=1)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_direction_GE11_ME11_GE21_ME21_eta16to22_looseVeto"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_direction_GE11_ME11_GE21_ME21_eta16to22_looseVeto"],
                                   treeHits, True, 1.6, 2.15, 0, minQuality, doDirectionBasedGE21=True, doVeto=True, vetoType=1)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_hybrid_GE11_ME11_GE21_ME21_ME3_eta16to22_looseVeto"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_hybrid_GE11_ME11_GE21_ME21_ME3_eta16to22_looseVeto"],
                                   treeHits, True, 1.6, 2.15, 0, minQuality, doHybridBasedGE21=True, doVeto=True, vetoType=1)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_hybrid_ME1_ME2_ME3_eta12to22_looseVeto"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_hybrid_ME1_ME2_ME3_eta12to22_looseVeto"],
                                   treeHits, True, 1.2, 2.15, 0, minQuality, doHybridBasedNoGE21=True, doVeto=True, vetoType=1)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_hybrid_GE11_ME11_ME21_ME3_eta16to22_looseVeto"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_hybrid_GE11_ME11_ME21_ME3_eta16to22_looseVeto"],
                                   treeHits, True, 1.6, 2.15, 0, minQuality, doHybridBasedNoGE21=True, doVeto=True, vetoType=1)

      ## medium isolation
      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_position_ME1_ME2_ME3_eta16to22_mediumVeto"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_position_ME1_ME2_ME3_eta16to22_mediumVeto"],
                                   treeHits, True, 1.6, 2.15, 0, minQuality, doPositionBased=True, doVeto=True, vetoType=2)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_position_ME1_ME2_ME3_eta12to24_mediumVeto"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_position_ME1_ME2_ME3_eta12to24_mediumVeto"],
                                   treeHits, True, 1.2, 2.4, 0, minQuality, doPositionBased=True, doVeto=True, vetoType=2)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_position_ME1_ME2_ME3_eta12to16_mediumVeto"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_position_ME1_ME2_ME3_eta12to16_mediumVeto"],
                                   treeHits, True, 1.2, 1.6, 0, minQuality, doPositionBased=True, doVeto=True, vetoType=2)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_direction_ME1_ME2_eta12to16_mediumVeto"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_direction_ME1_ME2_eta12to16_mediumVeto"],
                                   treeHits, True, 1.2, 1.6, 0, minQuality, doDirectionBasedNoGE21=True, doVeto=True, vetoType=2)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_direction_ME1_ME2_eta12to22_mediumVeto"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_direction_ME1_ME2_eta12to22_mediumVeto"],
                                   treeHits, True, 1.2, 2.15, 0, minQuality, doDirectionBasedNoGE21=True, doVeto=True, vetoType=2)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_direction_GE11_ME11_GE21_ME21_eta16to22_mediumVeto"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_direction_GE11_ME11_GE21_ME21_eta16to22_mediumVeto"],
                                   treeHits, True, 1.6, 2.15, 0, minQuality, doDirectionBasedGE21=True, doVeto=True, vetoType=2)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_hybrid_ME1_ME2_ME3_eta12to22_mediumVeto"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_hybrid_ME1_ME2_ME3_eta12to22_mediumVeto"],
                                   treeHits, True, 1.2, 2.15, 0, minQuality, doHybridBasedNoGE21=True, doVeto=True, vetoType=2)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_hybrid_GE11_ME11_GE21_ME21_ME3_eta16to22_mediumVeto"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_hybrid_GE11_ME11_GE21_ME21_ME3_eta16to22_mediumVeto"],
                                   treeHits, True, 1.6, 2.15, 0, minQuality, doHybridBasedGE21=True, doVeto=True, vetoType=2)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_hybrid_GE11_ME11_ME21_ME3_eta16to22_mediumVeto"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_hybrid_GE11_ME11_ME21_ME3_eta16to22_mediumVeto"],
                                   treeHits, True, 1.6, 2.15, 0, minQuality, doHybridBasedNoGE21=True, doVeto=True, vetoType=2)

      ## tight isolation
      """
      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_position_ME1_ME2_ME3_eta16to22_tightVeto"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_position_ME1_ME2_ME3_eta16to22_tightVeto"],
                                   treeHits, True, 1.6, 2.15, 0, minQuality, doPositionBased=True, doVeto=True, vetoType=3)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_position_ME1_ME2_ME3_eta12to24_tightVeto"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_position_ME1_ME2_ME3_eta12to24_tightVeto"],
                                   treeHits, True, 1.2, 2.4, 0, minQuality, doPositionBased=True, doVeto=True, vetoType=3)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_position_ME1_ME2_ME3_eta12to16_tightVeto"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_position_ME1_ME2_ME3_eta12to16_tightVeto"],
                                   treeHits, True, 1.2, 1.6, 0, minQuality, doPositionBased=True, doVeto=True, vetoType=3)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_direction_ME1_ME2_eta12to16_tightVeto"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_direction_ME1_ME2_eta12to16_tightVeto"],
                                   treeHits, True, 1.2, 1.6, 0, minQuality, doDirectionBasedNoGE21=True, doVeto=True, vetoType=3)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_direction_ME1_ME2_eta12to22_tightVeto"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_direction_ME1_ME2_eta12to22_tightVeto"],
                                   treeHits, True, 1.2, 2.15, 0, minQuality, doDirectionBasedNoGE21=True, doVeto=True, vetoType=3)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_direction_GE11_ME11_GE21_ME21_eta16to22_tightVeto"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_direction_GE11_ME11_GE21_ME21_eta16to22_tightVeto"],
                                   treeHits, True, 1.6, 2.15, 0, minQuality, doDirectionBasedGE21=True, doVeto=True, vetoType=3)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_hybrid_GE11_ME11_GE21_ME21_ME3_eta16to22_tightVeto"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_hybrid_GE11_ME11_GE21_ME21_ME3_eta16to22_tightVeto"],
                                   treeHits, True, 1.6, 2.15, 0, minQuality, doHybridBasedGE21=True, doVeto=True, vetoType=3)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_hybrid_ME1_ME2_ME3_eta12to22_tightVeto"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_hybrid_ME1_ME2_ME3_eta12to22_tightVeto"],
                                   treeHits, True, 1.2, 2.15, 0, minQuality, doHybridBasedNoGE21=True, doVeto=True, vetoType=3)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_hybrid_GE11_ME1_ME2_ME3_eta16to22_tightVeto"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_hybrid_GE11_ME1_ME2_ME3_eta16to22_tightVeto"],
                                   treeHits, True, 1.6, 2.15, 0, minQuality, doHybridBasedNoGE21=True, doVeto=True, vetoType=3)

      """

    ## make plots
    def makeDPhiPlot(h, title):
      c = TCanvas("c","c",800,600)
      c.Clear()
      gStyle.SetTitleBorderSize(0);
      #gStyle.SetPadLeftMargin(0.126);
      #gStyle.SetPadRightMargin(0.00);
      gStyle.SetPadTopMargin(0.06);
      gStyle.SetPadBottomMargin(0.13);
      gPad.SetTickx(1)
      gPad.SetTicky(1)
      gPad.SetLogx(0);
      gPad.SetLogy(0)
      gPad.SetGridx(1);
      gPad.SetGridy(1);

      gStyle.SetTitleStyle(0)
      gStyle.SetTitleAlign(13) ##// coord in top left
      gStyle.SetTitleX(0.)
      gStyle.SetTitleY(1.)
      gStyle.SetTitleW(1)
      gStyle.SetTitleH(0.058)
      gStyle.SetTitleBorderSize(0)

      gStyle.SetPadLeftMargin(0.126)
      gStyle.SetPadRightMargin(0.04)
      gStyle.SetPadTopMargin(0.06)
      gStyle.SetPadBottomMargin(0.13)
      gStyle.SetOptStat(0)
      gStyle.SetMarkerStyle(1)

      h.GetXaxis().SetTitleSize(0.05)
      h.GetYaxis().SetTitleSize(0.05)
      h.GetXaxis().SetLabelSize(0.05)
      h.GetYaxis().SetLabelSize(0.05)

      gStyle.SetTitleFontSize(0.065)

      h.SetTitle("           #scale[1.4]{#font[61]{CMS}} #font[52]{Simulation preliminary}                                                           14 TeV, 140 PU")
      h.SetStats(0)
      h.GetYaxis().SetTitle("charge*#Delta#Phi(GE1/1-ME1/1)")
      h.GetXaxis().SetTitle("charge*#Delta#Phi(GE2/1-ME2/1)")
      h.Draw("COLZ")

      c.SaveAs(targetDir + title + ".png")
      c.SaveAs(targetDir + title + ".pdf")
      c.SaveAs(targetDir + title + ".C")

    makeDPhiPlot(h_dphi_ME11_ME21, "dphi_ME11_ME21")
    makeDPhiPlot(h_dphi_ME11_ME21_charge_Pt0to5, "dphi_ME11_ME21_charge_Pt0to5")
    makeDPhiPlot(h_dphi_ME11_ME21_charge_Pt7to140, "dphi_ME11_ME21_charge_Pt7to140")
    makeDPhiPlot(h_dphi_ME11_ME21_charge_Pt10to140, "dphi_ME11_ME21_charge_Pt10to140")
    makeDPhiPlot(h_dphi_ME11_ME21_charge_Pt15to140, "dphi_ME11_ME21_charge_Pt15to140")
    makeDPhiPlot(h_dphi_ME11_ME21_charge_Pt20to140, "dphi_ME11_ME21_charge_Pt20to140")
    makeDPhiPlot(h_dphi_ME11_ME21_charge_Pt30to140, "dphi_ME11_ME21_charge_Pt30to140")

    def makeEtaPlots(legendTitle,
                     h1, h1Legend,
                     h2, h2Legend,
                     h3, h3Legend,
                     title, doEta=True):
      makePlots(legendTitle,
                h1, h1Legend,
                h2, h2Legend,
                h3, h3Legend,
                title, doEta)

    def makePlots(legendTitle,
                  h1, h1Legend,
                  h2, h2Legend,
                  h3, h3Legend,
                  title, doEta=False):
      c = TCanvas("c","c",800,600)
      c.Clear()
      gStyle.SetTitleBorderSize(0);
      gStyle.SetPadLeftMargin(0.126);
      gStyle.SetPadRightMargin(0.04);
      gStyle.SetPadTopMargin(0.06);
      gStyle.SetPadBottomMargin(0.13);
      gPad.SetTickx(1)
      gPad.SetTicky(1)
      gPad.SetLogy(1)
      gPad.SetLogx(1);
      if doEta:
        gPad.SetLogx(0);
        gPad.SetLogy(0)
      gPad.SetGridx(1);
      gPad.SetGridy(1);
      gStyle.SetErrorX(0)

      gStyle.SetTitleStyle(0)
      gStyle.SetTitleAlign(13) ##// coord in top left
      gStyle.SetTitleX(0.)
      gStyle.SetTitleY(1.)
      gStyle.SetTitleW(1)
      gStyle.SetTitleH(0.058)
      gStyle.SetTitleBorderSize(0)

      gStyle.SetPadLeftMargin(0.126)
      gStyle.SetPadRightMargin(0.04)
      gStyle.SetPadTopMargin(0.06)
      gStyle.SetPadBottomMargin(0.13)
      gStyle.SetOptStat(0)
      gStyle.SetMarkerStyle(1)

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
      nmyetabin = len(myetabin) - 1

      b1 = TH1F("b1","b1",nmyptbin,myptbin)
      if doEta:
        b1 = TH1F("b1","b1",nmyetabin,myetabin)
      b1.GetYaxis().SetRangeUser(0.2,10000)
      b1.GetXaxis().SetRangeUser(2,140)
      if doEta:
        b1.GetYaxis().SetRangeUser(0,50)
        b1.GetXaxis().SetRangeUser(0,2.5)
      b1.GetYaxis().SetTitleOffset(1.2)
      if not doEta:
        b1.GetYaxis().SetNdivisions(520)
      b1.GetYaxis().SetTitle("Trigger rate [kHz]")
      b1.GetXaxis().SetTitle("Muon trigger p_{T} threshold [GeV]")
      if doEta:
        b1.GetXaxis().SetTitle("Muon trigger #eta")
      b1.GetXaxis().SetTitleSize(0.05)
      b1.GetYaxis().SetTitleSize(0.05)
      b1.GetXaxis().SetLabelSize(0.05)
      b1.GetYaxis().SetLabelSize(0.05)
      gStyle.SetTitleFontSize(0.065)
      b1.SetTitle("           #scale[1.4]{#font[61]{CMS}} #font[52]{Simulation preliminary}                                                           14 TeV, 140 PU")
      b1.SetStats(0)
      b1.Draw()

      h11 = h1.Clone(h1.GetTitle() + "_clone")
      h21 = h2.Clone(h2.GetTitle() + "_clone")
      h31 = h3.Clone(h3.GetTitle() + "_clone")

      print "nEvents", nEvents, "entries", h1.GetEntries(), h2.GetEntries(), h3.GetEntries()
      if doEta:
        h11 = getRateEtaHistogram(nEvents, h11)
        h21 = getRateEtaHistogram(nEvents, h21)
        h31 = getRateEtaHistogram(nEvents, h31)
      else:
        h11 = getRatePtHistogram(nEvents, h11)
        h21 = getRatePtHistogram(nEvents, h21)
        h31 = getRatePtHistogram(nEvents, h31)

      ## set empty bins for displaced trigger histograms!
      def setEmptyBins(h):
        #hnew = h.Clone(h.GetName() + "_clone2");
        h.SetBinContent(1,0)
        h.SetBinContent(2,0)
        h.SetBinContent(3,0)
        h.SetBinContent(4,0)
        h.SetBinContent(5,0)
        h.SetBinContent(6,0)
        h.SetBinContent(8,0)
        h.SetBinContent(10,0)
        h.SetBinContent(12,0)
        h.SetBinContent(14,0)
        h.SetBinContent(15,0)
        #SetOwnership( h, False )
        return h

      if doEta:
        h11.SetLineColor(kRed)
        #h11.SetFillColor(kRed)
        h11.SetMarkerStyle(20)
        h11.SetMarkerColor(kRed)
        h11.Draw("E1X0 same")

        h21.SetLineColor(kViolet)
        #h21.SetFillColor(kViolet)
        h21.SetMarkerColor(kViolet)
        h21.SetMarkerStyle(21)
        h21.Draw("E1X0 same")

        h31.SetLineColor(kBlue)
        #h31.SetFillColor(kBlue)
        h31.SetMarkerColor(kBlue)
        h31.SetMarkerStyle(22)
        h31.Draw("E1X0 same")
      else:
        if (('Displaced' in h1Legend) and ('hybrid' in h1Legend)) or '(hybrid)' in h1Legend and False:
          setEmptyBins(h11)
        #h11.SetFillColor(kRed)
        h11.SetLineColor(kRed)
        h11.SetMarkerColor(kRed)
        h11.SetMarkerStyle(20)
        h11.Draw("E1X0 same")

        if (('Displaced' in h2Legend) and ('hybrid' in h2Legend)) or '(hybrid)' in h2Legend and False:
          setEmptyBins(h21)
        #h21.SetFillColor(kViolet)
        h21.SetLineColor(kViolet)
        h21.SetMarkerColor(kViolet)
        h21.SetMarkerStyle(21)
        h21.Draw("E1X0 same")

        if (('Displaced' in h3Legend) and ('hybrid' in h3Legend)) or '(hybrid)' in h3Legend and False:
          tex = drawLabel("Note: p_{T,min}^{hybrid} = 5 GeV", 0.6,0.8)
          setEmptyBins(h31)
        #h31.SetFillColor(kBlue)
        h31.SetLineColor(kBlue)
        h31.SetMarkerColor(kBlue)
        h31.SetMarkerStyle(22)
        h31.Draw("E1X0 same")

      #latex = applyTdrStyle()

      leg = TLegend(0.15,0.2,0.5,0.35,legendTitle,"brNDC")
      leg.SetFillColor(kWhite)
      leg.SetBorderSize(0)
      leg.SetFillStyle(0)
      leg.SetTextSize(0.03)
      leg.AddEntry(h11, h1Legend, "p")
      leg.AddEntry(h21, h2Legend, "p")
      leg.AddEntry(h31, h3Legend, "p")
      leg.Draw("same")

      if doEta:
        title.replace("_rate_pt_", "_rate_eta_")

      c.SaveAs(targetDir + title + ext)
      c.SaveAs(targetDir + title + ".pdf")
      c.SaveAs(targetDir + title + ".C")

      return

      ## ratios
      c = TCanvas("c","c",800,600)
      c.Clear()
      gStyle.SetTitleBorderSize(0);
      gStyle.SetPadLeftMargin(0.126);
      gStyle.SetPadRightMargin(0.04);
      gStyle.SetPadTopMargin(0.06);
      gStyle.SetPadBottomMargin(0.13);
#      gPad.SetLogy(1)

      b1 = TH1F("b1","b1",29,myptbin)
      b1.GetYaxis().SetRangeUser(0.01,1)
      b1.GetYaxis().SetTitleOffset(1.2)
      b1.GetYaxis().SetNdivisions(520)
      b1.GetYaxis().SetTitle("Ratio (normalized to prompt L1Mu)")
      b1.GetXaxis().SetTitle("L1Mu p_{T} cut [GeV]")
      b1.GetXaxis().SetTitleFont(62)
      b1.GetXaxis().SetTitleOffset(1.2)
      b1.GetXaxis().SetTitleSize(0.05)
      b1.GetYaxis().SetTitleSize(0.05)
      b1.SetTitle("                                                                  14TeV, " + pu)
      b1.SetStats(0)
      b1.Draw()

      #if isolation_cone != 0.12:
      h2.SetLineColor(kMagenta)
      h2.SetFillColor(kWhite)
      h2.Divide(h1)
      h2.Draw("same")

      h3.SetLineColor(kBlue)
      h3.SetFillColor(kWhite)
      h3.Divide(h1)
      h3.Draw("same")

      h4.SetLineColor(kGreen+1)
      h4.SetFillColor(kWhite)
      h4.Divide(h1)
      h4.Draw("same")

      h5.SetLineColor(kOrange+1)
      h5.SetFillColor(kWhite)
      h5.Divide(h1)
      h5.Draw("same")

      latex = applyTdrStyle()

      leg = TLegend(0.2,0.2,0.9,0.4,"","brNDC")
      leg.SetFillColor(kWhite)
      leg.SetBorderSize(0)
      leg.SetFillStyle(0)
      leg.SetTextSize(0.03)
      leg.AddEntry(h1,"Prompt L1Mu", "l")
      leg.AddEntry(None,"Displaced L1Mu", "")
      leg.AddEntry(None,"Veto Matching L1Tk #DeltaR#leq0.12 with p_{T}#geq%.0f"%(MatchingL1TkMinPt), "")
      leg.AddEntry(None,"Veto Non-matching L1Tk #DeltaR#leq%.1f:"%(isolation_cone), "")
      leg.AddEntry(h5,"p_{T} #geq 4 GeV", "l")
      leg.AddEntry(h4,"p_{T} #geq 3 GeV", "l")
      leg.AddEntry(h3,"p_{T} #geq 2.5 GeV", "l")
      leg.AddEntry(h2,"p_{T} #geq 2 GeV", "l")
      leg.Draw("same")


      c.SaveAs(targetDir + title + "_ratio" + ext)
      c.SaveAs(targetDir + title + "_ratio.C")
      c.SaveAs(targetDir + title + "_ratio.pdf")


    ## trigger rate plots
    makePlots("0.0<|#eta|<2.4",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_eta00to24"], "Prompt L1Mu",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_2_stubs_eta00to24"], "Prompt L1Mu, 2 stubs",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_3_stubs_eta00to24"], "Prompt L1Mu, 3 stubs",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu2st__L1Mu3st_eta00to24")

    makePlots("1.6<|#eta|<2.2",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_eta16to22"], "Prompt L1Mu",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_2_stubs_eta16to22"], "Prompt L1Mu, 2 CSC stubs",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_3_stubs_eta16to22"], "Prompt L1Mu, 3 CSC stubs",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu2st__L1Mu3st_eta16to22")

    makePlots("1.2<|#eta|<2.4",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_eta12to24"], "Prompt L1Mu",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_2_stubs_eta12to24"], "Prompt L1Mu, 2 CSC stubs",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_3_stubs_eta12to24"], "Prompt L1Mu, 3 CSC stubs",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu2st__L1Mu3st_eta12to24")

    makePlots("1.6<|#eta|<2.2",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_eta16to22"], "Prompt L1Mu",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_2_stubs_eta16to22"], "Prompt L1Mu, 2 CSC stubs",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_2_stubs_ME11_eta16to22"], "Prompt L1Mu, 2 CSC stubs, ME11",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu2st__L1Mu2stME11_eta16to22")

    makePlots("1.6<|#eta|<2.2",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_eta16to22"], "Prompt L1Mu",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_3_stubs_eta16to22"], "Prompt L1Mu, 3 CSC stubs",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_3_stubs_ME11_eta16to22"], "Prompt L1Mu, 3 CSC stubs, ME11",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu3st__L1Mu3stME11_eta16to22")

    makePlots("1.6<|#eta|<2.2",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_eta16to22"], "Prompt L1Mu",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_2_stubs_ME11_eta16to22"], "Prompt L1Mu, 2 CSC stubs, ME11",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_2_stubs_GE11_ME11_eta16to22"], "Prompt L1Mu, 2 CSC stubs, ME11, GE11",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu2stME11__L1Mu2stME11GE11_eta16to22")

    makePlots("1.6<|#eta|<2.2",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_eta16to22"], "Prompt L1Mu",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_3_stubs_ME11_eta16to22"], "Prompt L1Mu, 3 CSC stubs, ME11",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_3_stubs_GE11_ME11_eta16to22"], "Prompt L1Mu, 3 CSC stubs, ME11, GE11",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu3stME11__L1Mu3stME11GE11_eta16to22")

    makePlots("1.6<|#eta|<2.2",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_eta16to22"], "Prompt L1Mu",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_2_stubs_ME21_eta16to22"], "Prompt L1Mu, 2 CSC stubs, ME21",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_2_stubs_GE21_ME21_eta16to22"], "Prompt L1Mu, 2 CSC stubs, ME21, GE21",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu2stME21__L1Mu2stME21GE21_eta16to22")

    makePlots("1.6<|#eta|<2.2",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_eta16to22"], "Prompt L1Mu",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_3_stubs_ME21_eta16to22"], "Prompt L1Mu, 3 CSC stubs, ME21",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_3_stubs_GE21_ME21_eta16to22"], "Prompt L1Mu, 3 CSC stubs, ME21, GE21",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu3stME21__L1Mu3stME21GE21_eta16to22")

    makePlots("1.6<|#eta|<2.2",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_2_stubs_ME11_eta16to22"], "Prompt L1Mu, 2 CSC stubs, ME11",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_2_stubs_GE11_ME11_eta16to22"], "Prompt L1Mu, 2 CSC stubs, ME11, GE11",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_GE11_ME11_GE21_ME21_eta16to22"], "Prompt L1Mu, 2 CSC stubs, ME11, GE11, ME21, GE21",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu2stME11__L1Mu2stME11GE11__L1Mu2stME11GE11GE21_eta16to22")

    makePlots("1.6<|#eta|<2.2",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_3_stubs_ME11_eta16to22"], "Prompt L1Mu, 3 CSC stubs, ME11",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_3_stubs_GE11_ME11_eta16to22"], "Prompt L1Mu, 3 CSC stubs, ME11, GE11",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_GE11_ME11_GE21_ME21_eta16to22"], "Prompt L1Mu, 3 CSC stubs, ME11, ME21, GE11, GE21",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu3stME11__L1Mu3stME11GE11__L1Mu3stME11GE11GE21_eta16to22")

    makePlots("1.6<|#eta|<2.2",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_2_stubs_ME11_eta16to22"], "Prompt L1Mu, 2 CSC stubs, ME11",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_2_stubs_GE11_ME11_eta16to22"], "Prompt L1Mu, 2 CSC stubs, ME11, GE11",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_2_stubs_GE11_ME11_OR_GE21_ME21_eta16to22"], "Prompt L1Mu, 2 CSC stubs, GE11 or GE21",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu2stME11__L1Mu2stME11GE11__L1Mu2stGE11GE21_eta16to22")

    makePlots("1.6<|#eta|<2.2",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_3_stubs_ME11_eta16to22"], "Prompt L1Mu, 3 CSC stubs, ME11",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_3_stubs_GE11_ME11_eta16to22"], "Prompt L1Mu, 3 CSC stubs, ME11, GE11",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_3_stubs_GE11_ME11_OR_GE21_ME21_eta16to22"], "Prompt L1Mu, 3 CSC stubs, GE11 or GE21",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu3stME11__L1Mu3stME11GE11__L1Mu3stGE11GE21_eta16to22")


    ## eta
    makeEtaPlots("0.0<|#eta|<2.4",
              mapTH1F["h_single_prompt_L1Mu_rate_eta_eta00to24"], "Prompt L1Mu",
              mapTH1F["h_single_prompt_L1Mu_rate_eta_2_stubs_eta00to24"], "Prompt L1Mu, 2 stubs",
              mapTH1F["h_single_prompt_L1Mu_rate_eta_3_stubs_eta00to24"], "Prompt L1Mu, 3 stubs",
              "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu2st__L1Mu3st_eta00to24")

    makeEtaPlots("1.6<|#eta|<2.2",
              mapTH1F["h_single_prompt_L1Mu_rate_eta_eta16to22"], "Prompt L1Mu",
              mapTH1F["h_single_prompt_L1Mu_rate_eta_2_stubs_eta16to22"], "Prompt L1Mu, 2 CSC stubs",
              mapTH1F["h_single_prompt_L1Mu_rate_eta_3_stubs_eta16to22"], "Prompt L1Mu, 3 CSC stubs",
              "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu2st__L1Mu3st_eta16to22")

    makeEtaPlots("1.2<|#eta|<2.4",
              mapTH1F["h_single_prompt_L1Mu_rate_eta_eta12to24"], "Prompt L1Mu",
              mapTH1F["h_single_prompt_L1Mu_rate_eta_2_stubs_eta12to24"], "Prompt L1Mu, 2 CSC stubs",
              mapTH1F["h_single_prompt_L1Mu_rate_eta_3_stubs_eta12to24"], "Prompt L1Mu, 3 CSC stubs",
              "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu2st__L1Mu3st_eta12to24")

    makeEtaPlots("1.6<|#eta|<2.2",
              mapTH1F["h_single_prompt_L1Mu_rate_eta_eta16to22"], "Prompt L1Mu",
              mapTH1F["h_single_prompt_L1Mu_rate_eta_2_stubs_eta16to22"], "Prompt L1Mu, 2 CSC stubs",
              mapTH1F["h_single_prompt_L1Mu_rate_eta_2_stubs_ME11_eta16to22"], "Prompt L1Mu, 2 CSC stubs, ME11",
              "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu2st__L1Mu2stME11_eta16to22")

    makeEtaPlots("1.6<|#eta|<2.2",
              mapTH1F["h_single_prompt_L1Mu_rate_eta_eta16to22"], "Prompt L1Mu",
              mapTH1F["h_single_prompt_L1Mu_rate_eta_3_stubs_eta16to22"], "Prompt L1Mu, 3 CSC stubs",
              mapTH1F["h_single_prompt_L1Mu_rate_eta_3_stubs_ME11_eta16to22"], "Prompt L1Mu, 3 CSC stubs, ME11",
              "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu3st__L1Mu3stME11_eta16to22")

    makeEtaPlots("1.6<|#eta|<2.2",
              mapTH1F["h_single_prompt_L1Mu_rate_eta_eta16to22"], "Prompt L1Mu",
              mapTH1F["h_single_prompt_L1Mu_rate_eta_2_stubs_ME11_eta16to22"], "Prompt L1Mu, 2 CSC stubs, ME11",
              mapTH1F["h_single_prompt_L1Mu_rate_eta_2_stubs_GE11_ME11_eta16to22"], "Prompt L1Mu, 2 CSC stubs, ME11, GE11",
              "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu2stME11__L1Mu2stME11GE11_eta16to22")

    makeEtaPlots("1.6<|#eta|<2.2",
              mapTH1F["h_single_prompt_L1Mu_rate_eta_eta16to22"], "Prompt L1Mu",
              mapTH1F["h_single_prompt_L1Mu_rate_eta_3_stubs_ME11_eta16to22"], "Prompt L1Mu, 3 CSC stubs, ME11",
              mapTH1F["h_single_prompt_L1Mu_rate_eta_3_stubs_GE11_ME11_eta16to22"], "Prompt L1Mu, 3 CSC stubs, ME11, GE11",
              "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu3stME11__L1Mu3stME11GE11_eta16to22")

    makeEtaPlots("1.6<|#eta|<2.2",
              mapTH1F["h_single_prompt_L1Mu_rate_eta_eta16to22"], "Prompt L1Mu",
              mapTH1F["h_single_prompt_L1Mu_rate_eta_2_stubs_ME21_eta16to22"], "Prompt L1Mu, 2 CSC stubs, ME21",
              mapTH1F["h_single_prompt_L1Mu_rate_eta_2_stubs_GE21_ME21_eta16to22"], "Prompt L1Mu, 2 CSC stubs, ME21, GE21",
              "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu2stME21__L1Mu2stME21GE21_eta16to22")

    makeEtaPlots("1.6<|#eta|<2.2",
              mapTH1F["h_single_prompt_L1Mu_rate_eta_eta16to22"], "Prompt L1Mu",
              mapTH1F["h_single_prompt_L1Mu_rate_eta_3_stubs_ME21_eta16to22"], "Prompt L1Mu, 3 CSC stubs, ME21",
              mapTH1F["h_single_prompt_L1Mu_rate_eta_3_stubs_GE21_ME21_eta16to22"], "Prompt L1Mu, 3 CSC stubs, ME21, GE21",
              "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu3stME21__L1Mu3stME21GE21_eta16to22")

    makeEtaPlots("1.6<|#eta|<2.2",
              mapTH1F["h_single_prompt_L1Mu_rate_eta_2_stubs_ME11_eta16to22"], "Prompt L1Mu, 2 CSC stubs, ME11",
              mapTH1F["h_single_prompt_L1Mu_rate_eta_2_stubs_GE11_ME11_eta16to22"], "Prompt L1Mu, 2 CSC stubs, ME11, GE11",
              mapTH1F["h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to22"], "Prompt L1Mu, 2 CSC stubs, ME11, GE11, ME21, GE21",
              "Prompt_L1Mu_trigger_rate_eta__L1Mu2stME11__L1Mu2stME11GE11__L1Mu2stME11GE11GE21_eta16to22")

    makeEtaPlots("1.6<|#eta|<2.2",
              mapTH1F["h_single_prompt_L1Mu_rate_eta_3_stubs_ME11_eta16to22"], "Prompt L1Mu, 3 CSC stubs, ME11",
              mapTH1F["h_single_prompt_L1Mu_rate_eta_3_stubs_GE11_ME11_eta16to22"], "Prompt L1Mu, 3 CSC stubs, ME11, GE11",
              mapTH1F["h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to22"], "Prompt L1Mu, 3 CSC stubs, ME11, ME21, GE11, GE21",
              "Prompt_L1Mu_trigger_rate_eta__L1Mu3stME11__L1Mu3stME11GE11__L1Mu3stME11GE11GE21_eta16to22")

    makeEtaPlots("1.6<|#eta|<2.2",
              mapTH1F["h_single_prompt_L1Mu_rate_eta_2_stubs_ME11_eta16to22"], "Prompt L1Mu, 2 CSC stubs, ME11",
              mapTH1F["h_single_prompt_L1Mu_rate_eta_2_stubs_GE11_ME11_eta16to22"], "Prompt L1Mu, 2 CSC stubs, ME11, GE11",
              mapTH1F["h_single_prompt_L1Mu_rate_eta_2_stubs_GE11_ME11_OR_GE21_ME21_eta16to22"], "Prompt L1Mu, 2 CSC stubs, GE11 or GE21",
              "Prompt_L1Mu_trigger_rate_eta__L1Mu2stME11__L1Mu2stME11GE11__L1Mu2stGE11GE21_eta16to22")

    makeEtaPlots("1.6<|#eta|<2.2",
              mapTH1F["h_single_prompt_L1Mu_rate_eta_3_stubs_ME11_eta16to22"], "Prompt L1Mu, 3 CSC stubs, ME11",
              mapTH1F["h_single_prompt_L1Mu_rate_eta_3_stubs_GE11_ME11_eta16to22"], "Prompt L1Mu, 3 CSC stubs, ME11, GE11",
              mapTH1F["h_single_prompt_L1Mu_rate_eta_3_stubs_GE11_ME11_OR_GE21_ME21_eta16to22"], "Prompt L1Mu, 3 CSC stubs, GE11 or GE21",
              "Prompt_L1Mu_trigger_rate_eta__L1Mu3stME11__L1Mu3stME11GE11__L1Mu3stGE11GE21_eta16to22")

    ## displaced L1Mu trigger plots
    ## trigger rate plots vs pt
    makePlots("1.6<|#eta|<2.2",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_eta16to22"], "Prompt L1Mu",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_ME1_ME2_ME3_eta16to22"], "Prompt L1Mu, hit in ME1, ME2, ME3",
              mapTH1F["h_single_displaced_L1Mu_rate_pt_position_ME1_ME2_ME3_eta16to22"], "Displaced L1Mu, hit in ME1, ME2, ME3, position based",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu3st__DisplacedL1MuPositionBased_ME1_ME2_ME3_eta16to22")

    makePlots("1.2<|#eta|<2.4",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_eta12to24"], "Prompt L1Mu",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_ME1_ME2_ME3_eta12to24"], "Prompt L1Mu, hit in ME1, ME2, ME3",
              mapTH1F["h_single_displaced_L1Mu_rate_pt_position_ME1_ME2_ME3_eta12to24"], "Displaced L1Mu, hit in ME1, ME2, ME3, position based",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu3st__DisplacedL1MuPositionBased_ME1_ME2_ME3_eta12to24")

    makePlots("1.6<|#eta|<2.2",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_eta16to22"], "Prompt L1Mu",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_GE11_ME11_GE21_ME21_eta16to22"], "Prompt L1Mu, hit in GE11, ME11, GE21, ME21",
              mapTH1F["h_single_displaced_L1Mu_rate_pt_direction_GE11_ME11_GE21_ME21_eta16to22"], "Displaced L1Mu, hit in GE11, ME11, GE21, ME21 direction based",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu3st__DisplacedL1MuDirectionBased_GE11_ME11_GE21_ME21_eta16to22")

    makePlots("1.6<|#eta|<2.2",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_eta16to22"], "Prompt L1Mu",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_GE11_ME11_GE21_ME21_ME3_eta16to22"], "Prompt L1Mu, hit in GE11, ME11, GE21, ME21, ME3",
              mapTH1F["h_single_displaced_L1Mu_rate_pt_hybrid_GE11_ME11_GE21_ME21_ME3_eta16to22"], "Displaced L1Mu, hit in GE11, ME11, GE21, ME21, ME3 hybrid based",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu3st__DisplacedL1MuHybridBased_GE11_ME11_GE21_ME21_ME3_eta16to22")

    makePlots("1.6<|#eta|<2.2",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_eta16to22"], "Prompt L1Mu",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_GE11_ME11_ME21_ME3_eta16to22"], "Prompt L1Mu, hit in GE11, ME11, ME21, ME3",
              mapTH1F["h_single_displaced_L1Mu_rate_pt_hybrid_GE11_ME11_ME21_ME3_eta16to22"], "Displaced L1Mu, hit in GE11, ME11, ME21, ME3 hybrid based",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu3st__DisplacedL1MuHybridBased_GE11_ME11_ME21_ME3_eta16to22")

    makePlots("1.2<|#eta|<2.2",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_eta12to22"], "Prompt L1Mu",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_ME1_ME2_ME3_eta12to22"], "Prompt L1Mu, hit in ME1, ME2, ME3",
              mapTH1F["h_single_displaced_L1Mu_rate_pt_hybrid_ME1_ME2_ME3_eta12to22"], "Displaced L1Mu, hit in ME1, ME2, ME3 hybrid based",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu3st__DisplacedL1MuHybridBased_ME1_ME2_ME3_eta12to22")

    makePlots("0.0<|#eta|<0.9",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_eta00to09"], "Prompt L1Mu",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_MB1_MB4_eta00to09"], "Prompt L1Mu, hit in MB1, MB4",
              mapTH1F["h_single_displaced_L1Mu_rate_pt_direction_MB1_MB4_eta00to09"], "Displaced L1Mu, hit in MB1, MB4, direction based",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu2st__DisplacedL1Mu2st_MB1_MB4_eta00to09")

    ## rates vs eta
    makeEtaPlots("1.6<|#eta|<2.2",
                 mapTH1F["h_single_prompt_L1Mu_rate_eta_eta16to22"], "Prompt L1Mu",
                 mapTH1F["h_single_prompt_L1Mu_rate_eta_ME1_ME2_ME3_eta16to22"], "Prompt L1Mu, hit in ME1, ME2, ME3",
                 mapTH1F["h_single_displaced_L1Mu_rate_eta_position_ME1_ME2_ME3_eta16to22"], "Displaced L1Mu, hit in ME1, ME2, ME3 position based",
                 "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu3st__DisplacedL1MuPositionBased_ME1_ME2_ME3_eta16to22", doEta=True)

    makeEtaPlots("1.2<|#eta|<2.4",
                 mapTH1F["h_single_prompt_L1Mu_rate_eta_eta12to24"], "Prompt L1Mu",
                 mapTH1F["h_single_prompt_L1Mu_rate_eta_ME1_ME2_ME3_eta12to24"], "Prompt L1Mu, hit in ME1, ME2, ME3",
                 mapTH1F["h_single_displaced_L1Mu_rate_eta_position_ME1_ME2_ME3_eta12to24"], "Displaced L1Mu, hit in ME1, ME2, ME3 position based",
                 "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu3st__DisplacedL1MuPositionBased_ME1_ME2_ME3_eta12to24", doEta=True)

    makeEtaPlots("1.6<|#eta|<2.2",
                 mapTH1F["h_single_prompt_L1Mu_rate_eta_eta16to22"], "Prompt L1Mu",
                 mapTH1F["h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to22"], "Prompt L1Mu, hit in GE11, ME11, GE21, ME21",
                 mapTH1F["h_single_displaced_L1Mu_rate_eta_direction_GE11_ME11_GE21_ME21_eta16to22"], "Displaced L1Mu, hit in GE11, ME11, GE21, ME21 direction based",
                 "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu3st__DisplacedL1MuDirectionBased_GE11_ME11_GE21_ME21_eta16to22", doEta=True)

    makeEtaPlots("1.6<|#eta|<2.2",
                 mapTH1F["h_single_prompt_L1Mu_rate_eta_eta16to22"], "Prompt L1Mu",
                 mapTH1F["h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_ME3_eta16to22"], "Prompt L1Mu, hit in GE11, ME11, GE21, ME21, ME3",
                 mapTH1F["h_single_displaced_L1Mu_rate_eta_hybrid_GE11_ME11_GE21_ME21_ME3_eta16to22"], "Displaced L1Mu, hit in GE11, ME11, GE21, ME21, ME3 hybrid based",
                 "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu3st__DisplacedL1MuHybridBased_GE11_ME11_GE21_ME21_ME3_eta16to22", doEta=True)

    makeEtaPlots("1.6<|#eta|<2.2",
                 mapTH1F["h_single_prompt_L1Mu_rate_eta_eta16to22"], "Prompt L1Mu",
                 mapTH1F["h_single_prompt_L1Mu_rate_eta_ME1_ME2_ME3_eta16to22"], "Prompt L1Mu, hit in ME1, ME2, ME3",
                 mapTH1F["h_single_displaced_L1Mu_rate_eta_hybrid_GE11_ME1_ME2_ME3_eta16to22"], "Displaced L1Mu, hit in ME1, ME2, ME3 hybrid based",
                 "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu3st__DisplacedL1MuHybridBased_ME1_ME2_ME3_eta16to22")

    makeEtaPlots("1.2<|#eta|<2.2",
                 mapTH1F["h_single_prompt_L1Mu_rate_eta_eta12to22"], "Prompt L1Mu",
                 mapTH1F["h_single_prompt_L1Mu_rate_eta_ME1_ME2_ME3_eta12to22"], "Prompt L1Mu, hit in ME1, ME2, ME3",
                 mapTH1F["h_single_displaced_L1Mu_rate_eta_hybrid_ME1_ME2_ME3_eta12to22"], "Displaced L1Mu, hit in ME1, ME2, ME3 hybrid based",
                 "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu3st__DisplacedL1MuHybridBased_ME1_ME2_ME3_eta12to22")

    makeEtaPlots("0.0<|#eta|<0.9",
                 mapTH1F["h_single_prompt_L1Mu_rate_eta_eta00to09"], "Prompt L1Mu",
                 mapTH1F["h_single_prompt_L1Mu_rate_eta_MB1_MB4_eta00to09"], "Prompt L1Mu, hit in MB1, MB4",
                 mapTH1F["h_single_displaced_L1Mu_rate_eta_direction_MB1_MB4_eta00to09"], "Displaced L1Mu, hit in MB1, MB4, direction based",
                 "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu2st__DisplacedL1Mu2st_MB1_MB4_eta00to09")


    ## rates with isolation
    ## trigger rate plots vs pt
    makePlots("1.6<|#eta|<2.2",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_ME1_ME2_ME3_eta16to22"], "Prompt L1Mu, hit in ME1, ME2, ME3",
              mapTH1F["h_single_displaced_L1Mu_rate_pt_position_ME1_ME2_ME3_eta16to22"], "Displaced L1Mu, hit in ME1, ME2, ME3, position based",
              mapTH1F["h_single_displaced_L1Mu_rate_pt_position_ME1_ME2_ME3_eta16to22_looseVeto"], "Displaced L1Mu, hit in ME1, ME2, ME3, position based, loose veto",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu3st__DisplacedL1MuPositionBased_ME1_ME2_ME3_eta16to22_looseVeto")

    makePlots("1.2<|#eta|<2.4",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_ME1_ME2_ME3_eta12to24"], "Prompt L1Mu, hit in ME1, ME2, ME3",
              mapTH1F["h_single_displaced_L1Mu_rate_pt_position_ME1_ME2_ME3_eta12to24"], "Displaced L1Mu, hit in ME1, ME2, ME3, position based",
              mapTH1F["h_single_displaced_L1Mu_rate_pt_position_ME1_ME2_ME3_eta12to24_looseVeto"], "Displaced L1Mu, hit in ME1, ME2, ME3, position based, loose veto",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu3st__DisplacedL1MuPositionBased_ME1_ME2_ME3_eta12to24_looseVeto")

    makePlots("1.6<|#eta|<2.2",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_GE11_ME11_GE21_ME21_eta16to22"], "Prompt L1Mu, hit in GE11, ME11, GE21, ME21",
              mapTH1F["h_single_displaced_L1Mu_rate_pt_direction_GE11_ME11_GE21_ME21_eta16to22"], "Displaced L1Mu, hit in GE11, ME11, GE21, ME21 direction based",
              mapTH1F["h_single_displaced_L1Mu_rate_pt_direction_GE11_ME11_GE21_ME21_eta16to22_looseVeto"], "Displaced L1Mu, hit in GE11, ME11, GE21, ME21 direction based, loose veto",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu3st__DisplacedL1MuDirectionBased_GE11_ME11_GE21_ME21_eta16to22_looseVeto")

    makePlots("1.6<|#eta|<2.2",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_GE11_ME11_GE21_ME21_ME3_eta16to22"], "Prompt L1Mu, hit in GE11, ME11, GE21, ME21, ME3",
              mapTH1F["h_single_displaced_L1Mu_rate_pt_hybrid_GE11_ME11_GE21_ME21_ME3_eta16to22"], "Displaced L1Mu, hit in GE11, ME11, GE21, ME21, ME3 hybrid based",
              mapTH1F["h_single_displaced_L1Mu_rate_pt_hybrid_GE11_ME11_GE21_ME21_ME3_eta16to22_looseVeto"], "Displaced L1Mu, hit in GE11, ME11, GE21, ME21, ME3 hybrid based, loose veto",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu3st__DisplacedL1MuHybridBased_GE11_ME11_GE21_ME21_ME3_eta16to22_looseVeto")

    makePlots("1.6<|#eta|<2.2",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_ME1_ME2_ME3_eta16to22"], "Prompt L1Mu, hit in ME1, ME2, ME3",
              mapTH1F["h_single_displaced_L1Mu_rate_pt_hybrid_GE11_ME1_ME2_ME3_eta16to22"], "Displaced L1Mu, hit in GE11, ME1, ME2, ME3 hybrid based",
              mapTH1F["h_single_displaced_L1Mu_rate_pt_hybrid_GE11_ME1_ME2_ME3_eta16to22_looseVeto"], "Displaced L1Mu, hit in GE11, ME1, ME2, ME3 hybrid based, loose veto",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu3st__DisplacedL1MuHybridBased_ME1_ME2_ME3_eta16to22_looseVeto")

    makePlots("1.2<|#eta|<2.2",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_ME1_ME2_ME3_eta12to22"], "Prompt L1Mu, hit in ME1, ME2, ME3",
              mapTH1F["h_single_displaced_L1Mu_rate_pt_hybrid_ME1_ME2_ME3_eta12to22"], "Displaced L1Mu, hit in ME1, ME2, ME3 hybrid based",
              mapTH1F["h_single_displaced_L1Mu_rate_pt_hybrid_ME1_ME2_ME3_eta12to22_looseVeto"], "Displaced L1Mu, hit in ME1, ME2, ME3 hybrid based, loose veto",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu3st__DisplacedL1MuHybridBased_ME1_ME2_ME3_eta12to22_looseVeto")

    makePlots("0.0<|#eta|<0.9",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_MB1_MB4_eta00to09"], "Prompt L1Mu, hit in MB1, MB4",
              mapTH1F["h_single_displaced_L1Mu_rate_pt_direction_MB1_MB4_eta00to09"], "Displaced L1Mu, hit in MB1, MB4, direction based",
              mapTH1F["h_single_displaced_L1Mu_rate_pt_direction_MB1_MB4_eta00to09_looseVeto"], "Displaced L1Mu, hit in MB1, MB4, direction based, loose veto",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu2st__DisplacedL1Mu2st_MB1_MB4_eta00to09_looseVeto")

    ## rates vs eta
    makeEtaPlots("1.6<|#eta|<2.2",
                 mapTH1F["h_single_prompt_L1Mu_rate_eta_ME1_ME2_ME3_eta16to22"], "Prompt L1Mu, hit in ME1, ME2, ME3",
                 mapTH1F["h_single_displaced_L1Mu_rate_eta_position_ME1_ME2_ME3_eta16to22"], "Displaced L1Mu, hit in ME1, ME2, ME3 position based",
                 mapTH1F["h_single_displaced_L1Mu_rate_eta_position_ME1_ME2_ME3_eta16to22_looseVeto"], "Displaced L1Mu, hit in ME1, ME2, ME3 position based, loose veto",
                 "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu3st__DisplacedL1MuPositionBased_ME1_ME2_ME3_eta16to22_looseVeto", doEta=True)

    makeEtaPlots("1.2<|#eta|<2.4",
                 mapTH1F["h_single_prompt_L1Mu_rate_eta_ME1_ME2_ME3_eta12to24"], "Prompt L1Mu, hit in ME1, ME2, ME3",
                 mapTH1F["h_single_displaced_L1Mu_rate_eta_position_ME1_ME2_ME3_eta12to24"], "Displaced L1Mu, hit in ME1, ME2, ME3 position based",
                 mapTH1F["h_single_displaced_L1Mu_rate_eta_position_ME1_ME2_ME3_eta12to24_looseVeto"], "Displaced L1Mu, hit in ME1, ME2, ME3 position based, loose veto",
                 "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu3st__DisplacedL1MuPositionBased_ME1_ME2_ME3_eta12to24_looseVeto", doEta=True)

    makeEtaPlots("1.6<|#eta|<2.2",
                 mapTH1F["h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to22"], "Prompt L1Mu, hit in GE11, ME11, GE21, ME21",
                 mapTH1F["h_single_displaced_L1Mu_rate_eta_direction_GE11_ME11_GE21_ME21_eta16to22"], "Displaced L1Mu, hit in GE11, ME11, GE21, ME21 direction based",
                 mapTH1F["h_single_displaced_L1Mu_rate_eta_direction_GE11_ME11_GE21_ME21_eta16to22_looseVeto"], "Displaced L1Mu, hit in GE11, ME11, GE21, ME21 direction based, loose veto",
                 "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu3st__DisplacedL1MuDirectionBased_GE11_ME11_GE21_ME21_eta16to22_looseVeto", doEta=True)

    makeEtaPlots("1.6<|#eta|<2.2",
                 mapTH1F["h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_ME3_eta16to22"], "Prompt L1Mu, hit in GE11, ME11, GE21, ME21, ME3",
                 mapTH1F["h_single_displaced_L1Mu_rate_eta_hybrid_GE11_ME11_GE21_ME21_ME3_eta16to22"], "Displaced L1Mu, hit in GE11, ME11, GE21, ME21, ME3 hybrid based",
                 mapTH1F["h_single_displaced_L1Mu_rate_eta_hybrid_GE11_ME11_GE21_ME21_ME3_eta16to22_looseVeto"], "Displaced L1Mu, hit in GE11, ME11, GE21, ME21, ME3 hybrid based, loose veto",
                 "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu3st__DisplacedL1MuHybridBased_GE11_ME11_GE21_ME21_ME3_eta16to22_looseVeto", doEta=True)

    makeEtaPlots("1.6<|#eta|<2.2",
                 mapTH1F["h_single_prompt_L1Mu_rate_eta_ME1_ME2_ME3_eta16to22"], "Prompt L1Mu, hit in ME1, ME2, ME3",
                 mapTH1F["h_single_displaced_L1Mu_rate_eta_hybrid_GE11_ME1_ME2_ME3_eta16to22"], "Displaced L1Mu, hit in GE11, ME1, ME2, ME3 hybrid based",
                 mapTH1F["h_single_displaced_L1Mu_rate_eta_hybrid_GE11_ME1_ME2_ME3_eta16to22_looseVeto"], "Displaced L1Mu, hit in GE11, ME1, ME2, ME3 hybrid based, loose veto",
                 "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu3st__DisplacedL1MuHybridBased_ME1_ME2_ME3_eta16to22_looseVeto")

    makeEtaPlots("1.2<|#eta|<2.2",
                 mapTH1F["h_single_prompt_L1Mu_rate_eta_ME1_ME2_ME3_eta12to22"], "Prompt L1Mu, hit in ME1, ME2, ME3",
                 mapTH1F["h_single_displaced_L1Mu_rate_eta_hybrid_ME1_ME2_ME3_eta12to22"], "Displaced L1Mu, hit in ME1, ME2, ME3 hybrid based",
                 mapTH1F["h_single_displaced_L1Mu_rate_eta_hybrid_ME1_ME2_ME3_eta12to22_looseVeto"], "Displaced L1Mu, hit in ME1, ME2, ME3 hybrid based, loose veto",
                 "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu3st__DisplacedL1MuHybridBased_ME1_ME2_ME3_eta12to22_looseVeto")

    makeEtaPlots("0.0<|#eta|<0.9",
                 mapTH1F["h_single_prompt_L1Mu_rate_eta_MB1_MB4_eta00to09"], "Prompt L1Mu, hit in MB1, MB4",
                 mapTH1F["h_single_displaced_L1Mu_rate_eta_direction_MB1_MB4_eta00to09"], "Displaced L1Mu, hit in MB1, MB4, direction based",
                 mapTH1F["h_single_displaced_L1Mu_rate_eta_direction_MB1_MB4_eta00to09_looseVeto"], "Displaced L1Mu, hit in MB1, MB4, direction based, loose veto",
                 "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu2st__DisplacedL1Mu2st_MB1_MB4_eta00to09_looseVeto")


    ## trigger rate plots vs pt
    makePlots("1.6<|#eta|<2.2",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_ME1_ME2_ME3_eta16to22"], "Prompt L1Mu, hit in ME1, ME2, ME3",
              mapTH1F["h_single_displaced_L1Mu_rate_pt_position_ME1_ME2_ME3_eta16to22"], "Displaced L1Mu, hit in ME1, ME2, ME3, position based",
              mapTH1F["h_single_displaced_L1Mu_rate_pt_position_ME1_ME2_ME3_eta16to22_mediumVeto"], "Displaced L1Mu, hit in ME1, ME2, ME3, position based, medium veto",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu3st__DisplacedL1MuPositionBased_ME1_ME2_ME3_eta16to22_mediumVeto")

    makePlots("1.2<|#eta|<2.4",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_ME1_ME2_ME3_eta12to24"], "Prompt L1Mu, hit in ME1, ME2, ME3",
              mapTH1F["h_single_displaced_L1Mu_rate_pt_position_ME1_ME2_ME3_eta12to24"], "Displaced L1Mu, hit in ME1, ME2, ME3, position based",
              mapTH1F["h_single_displaced_L1Mu_rate_pt_position_ME1_ME2_ME3_eta12to24_mediumVeto"], "Displaced L1Mu, hit in ME1, ME2, ME3, position based, medium veto",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu3st__DisplacedL1MuPositionBased_ME1_ME2_ME3_eta12to24_mediumVeto")

    makePlots("1.6<|#eta|<2.2",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_GE11_ME11_GE21_ME21_eta16to22"], "Prompt L1Mu, hit in GE11, ME11, GE21, ME21",
              mapTH1F["h_single_displaced_L1Mu_rate_pt_direction_GE11_ME11_GE21_ME21_eta16to22"], "Displaced L1Mu, hit in GE11, ME11, GE21, ME21 direction based",
              mapTH1F["h_single_displaced_L1Mu_rate_pt_direction_GE11_ME11_GE21_ME21_eta16to22_mediumVeto"], "Displaced L1Mu, hit in GE11, ME11, GE21, ME21 direction based, medium veto",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu3st__DisplacedL1MuDirectionBased_GE11_ME11_GE21_ME21_eta16to22_mediumVeto")

    makePlots("1.6<|#eta|<2.2",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_GE11_ME11_GE21_ME21_ME3_eta16to22"], "Prompt L1Mu, hit in GE11, ME11, GE21, ME21, ME3",
              mapTH1F["h_single_displaced_L1Mu_rate_pt_hybrid_GE11_ME11_GE21_ME21_ME3_eta16to22"], "Displaced L1Mu, hit in GE11, ME11, GE21, ME21, ME3 hybrid based",
              mapTH1F["h_single_displaced_L1Mu_rate_pt_hybrid_GE11_ME11_GE21_ME21_ME3_eta16to22_mediumVeto"], "Displaced L1Mu, hit in GE11, ME11, GE21, ME21, ME3 hybrid based, medium veto",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu3st__DisplacedL1MuHybridBased_GE11_ME11_GE21_ME21_ME3_eta16to22_mediumVeto")

    makePlots("1.6<|#eta|<2.2",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_ME1_ME2_ME3_eta16to22"], "Prompt L1Mu, hit in ME1, ME2, ME3",
              mapTH1F["h_single_displaced_L1Mu_rate_pt_hybrid_GE11_ME1_ME2_ME3_eta16to22"], "Displaced L1Mu, hit in ME1, ME2, ME3 hybrid based",
              mapTH1F["h_single_displaced_L1Mu_rate_pt_hybrid_GE11_ME1_ME2_ME3_eta16to22_mediumVeto"], "Displaced L1Mu, hit in ME1, ME2, ME3 hybrid based, medium veto",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu3st__DisplacedL1MuHybridBased_ME1_ME2_ME3_eta16to22_mediumVeto")

    makePlots("1.2<|#eta|<2.2",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_ME1_ME2_ME3_eta12to22"], "Prompt L1Mu, hit in ME1, ME2, ME3",
              mapTH1F["h_single_displaced_L1Mu_rate_pt_hybrid_ME1_ME2_ME3_eta12to22"], "Displaced L1Mu, hit in ME1, ME2, ME3 hybrid based",
              mapTH1F["h_single_displaced_L1Mu_rate_pt_hybrid_ME1_ME2_ME3_eta12to22_mediumVeto"], "Displaced L1Mu, hit in ME1, ME2, ME3 hybrid based, medium veto",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu3st__DisplacedL1MuHybridBased_ME1_ME2_ME3_eta12to22_mediumVeto")

    makePlots("0.0<|#eta|<0.9",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_MB1_MB4_eta00to09"], "Prompt L1Mu, hit in MB1, MB4",
              mapTH1F["h_single_displaced_L1Mu_rate_pt_direction_MB1_MB4_eta00to09"], "Displaced L1Mu, hit in MB1, MB4, direction based",
              mapTH1F["h_single_displaced_L1Mu_rate_pt_direction_MB1_MB4_eta00to09_mediumVeto"], "Displaced L1Mu, hit in MB1, MB4, direction based, medium veto",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu2st__DisplacedL1Mu2st_MB1_MB4_eta00to09_mediumVeto")

    ## rates vs eta
    makeEtaPlots("1.6<|#eta|<2.2",
                 mapTH1F["h_single_prompt_L1Mu_rate_eta_ME1_ME2_ME3_eta16to22"], "Prompt L1Mu, hit in ME1, ME2, ME3",
                 mapTH1F["h_single_displaced_L1Mu_rate_eta_position_ME1_ME2_ME3_eta16to22"], "Displaced L1Mu, hit in ME1, ME2, ME3 position based",
                 mapTH1F["h_single_displaced_L1Mu_rate_eta_position_ME1_ME2_ME3_eta16to22_mediumVeto"], "Displaced L1Mu, hit in ME1, ME2, ME3 position based, medium veto",
                 "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu3st__DisplacedL1MuPositionBased_ME1_ME2_ME3_eta16to22_mediumVeto", doEta=True)

    makeEtaPlots("1.2<|#eta|<2.4",
                 mapTH1F["h_single_prompt_L1Mu_rate_eta_ME1_ME2_ME3_eta12to24"], "Prompt L1Mu, hit in ME1, ME2, ME3",
                 mapTH1F["h_single_displaced_L1Mu_rate_eta_position_ME1_ME2_ME3_eta12to24"], "Displaced L1Mu, hit in ME1, ME2, ME3 position based",
                 mapTH1F["h_single_displaced_L1Mu_rate_eta_position_ME1_ME2_ME3_eta12to24_mediumVeto"], "Displaced L1Mu, hit in ME1, ME2, ME3 position based, medium veto",
                 "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu3st__DisplacedL1MuPositionBased_ME1_ME2_ME3_eta12to24_mediumVeto", doEta=True)

    makeEtaPlots("1.6<|#eta|<2.2",
                 mapTH1F["h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to22"], "Prompt L1Mu, hit in GE11, ME11, GE21, ME21",
                 mapTH1F["h_single_displaced_L1Mu_rate_eta_direction_GE11_ME11_GE21_ME21_eta16to22"], "Displaced L1Mu, hit in GE11, ME11, GE21, ME21 direction based",
                 mapTH1F["h_single_displaced_L1Mu_rate_eta_direction_GE11_ME11_GE21_ME21_eta16to22_mediumVeto"], "Displaced L1Mu, hit in GE11, ME11, GE21, ME21 direction based, medium veto",
                 "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu3st__DisplacedL1MuDirectionBased_GE11_ME11_GE21_ME21_eta16to22_mediumVeto", doEta=True)

    makeEtaPlots("1.6<|#eta|<2.2",
                 mapTH1F["h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_ME3_eta16to22"], "Prompt L1Mu, hit in GE11, ME11, GE21, ME21, ME3",
                 mapTH1F["h_single_displaced_L1Mu_rate_eta_hybrid_GE11_ME11_GE21_ME21_ME3_eta16to22"], "Displaced L1Mu, hit in GE11, ME11, GE21, ME21, ME3 hybrid based",
                 mapTH1F["h_single_displaced_L1Mu_rate_eta_hybrid_GE11_ME11_GE21_ME21_ME3_eta16to22_mediumVeto"], "Displaced L1Mu, hit in GE11, ME11, GE21, ME21, ME3 hybrid based, medium veto",
                 "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu3st__DisplacedL1MuHybridBased_GE11_ME11_GE21_ME21_ME3_eta16to22_mediumVeto", doEta=True)

    makeEtaPlots("1.6<|#eta|<2.2",
                 mapTH1F["h_single_prompt_L1Mu_rate_eta_ME1_ME2_ME3_eta16to22"], "Prompt L1Mu, hit in ME1, ME2, ME3",
                 mapTH1F["h_single_displaced_L1Mu_rate_eta_hybrid_GE11_ME1_ME2_ME3_eta16to22"], "Displaced L1Mu, hit in ME1, ME2, ME3 hybrid based",
                 mapTH1F["h_single_displaced_L1Mu_rate_eta_hybrid_GE11_ME1_ME2_ME3_eta16to22_mediumVeto"], "Displaced L1Mu, hit in ME1, ME2, ME3 hybrid based, medium veto",
                 "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu3st__DisplacedL1MuHybridBased_ME1_ME2_ME3_eta16to22_mediumVeto")

    makeEtaPlots("1.2<|#eta|<2.2",
                 mapTH1F["h_single_prompt_L1Mu_rate_eta_ME1_ME2_ME3_eta12to22"], "Prompt L1Mu, hit in ME1, ME2, ME3",
                 mapTH1F["h_single_displaced_L1Mu_rate_eta_hybrid_ME1_ME2_ME3_eta12to22"], "Displaced L1Mu, hit in ME1, ME2, ME3 hybrid based",
                 mapTH1F["h_single_displaced_L1Mu_rate_eta_hybrid_ME1_ME2_ME3_eta12to22_mediumVeto"], "Displaced L1Mu, hit in ME1, ME2, ME3 hybrid based, medium veto",
                 "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu3st__DisplacedL1MuHybridBased_ME1_ME2_ME3_eta12to22_mediumVeto")

    makeEtaPlots("0.0<|#eta|<0.9",
                 mapTH1F["h_single_prompt_L1Mu_rate_eta_MB1_MB4_eta00to09"], "Prompt L1Mu, hit in MB1, MB4",
                 mapTH1F["h_single_displaced_L1Mu_rate_eta_direction_MB1_MB4_eta00to09"], "Displaced L1Mu, hit in MB1, MB4, direction based",
                 mapTH1F["h_single_displaced_L1Mu_rate_eta_direction_MB1_MB4_eta00to09_mediumVeto"], "Displaced L1Mu, hit in MB1, MB4, direction based, medium veto",
                 "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu2st__DisplacedL1Mu2st_MB1_MB4_eta00to09_mediumVeto")


    ### FINAL PLOTS FOR MUON TDR ###
    makePlots("1.6<|#eta|<2.2",
                 mapTH1F["h_single_prompt_L1Mu_rate_pt_ME1_ME2_ME3_eta16to22"], "L1Mu (constrained)",
                 mapTH1F["h_single_displaced_L1Mu_rate_pt_position_ME1_ME2_ME3_eta16to22"], "L1Mu (unconstrained)",
                 mapTH1F["h_single_displaced_L1Mu_rate_pt_hybrid_GE11_ME11_GE21_ME21_ME3_eta16to22"], "L1Mu (hybrid)",
                 "MuonTDR2017_Prompt_L1Mu_trigger_rate_pt__L1Mu__PositionBased_HybridBased_GE11_ME11_GE21_ME21_ME3_eta16to22")

    makeEtaPlots("1.6<|#eta|<2.2",
                 mapTH1F["h_single_prompt_L1Mu_rate_eta_ME1_ME2_ME3_eta16to22"], "L1Mu (constrained)",
                 mapTH1F["h_single_displaced_L1Mu_rate_eta_position_ME1_ME2_ME3_eta16to22"], "L1Mu (unconstrained)",
                 mapTH1F["h_single_displaced_L1Mu_rate_eta_hybrid_GE11_ME11_GE21_ME21_ME3_eta16to22"], "L1Mu (hybrid)",
                 "MuonTDR2017_Prompt_L1Mu_trigger_rate_eta__L1Mu__PositionBased_HybridBased_GE11_ME11_GE21_ME21_ME3_eta16to22")


    makePlots("1.6<|#eta|<2.2",
                 mapTH1F["h_single_displaced_L1Mu_rate_pt_position_ME1_ME2_ME3_eta16to22_mediumVeto"], "L1Mu (unconstrained)",
                 mapTH1F["h_single_displaced_L1Mu_rate_pt_hybrid_GE11_ME11_GE21_ME21_ME3_eta16to22_mediumVeto"], "L1Mu (hybrid)",
                 mapTH1F["h_single_prompt_L1Mu_rate_pt_ME1_ME2_ME3_eta16to22"], "L1Mu (hybrid)",
                 "MuonTDR2017_Prompt_L1Mu_trigger_rate_pt__L1Mu__PositionBased_HybridBased_GE11_ME11_GE21_ME21_ME3_eta16to22_mediumVeto")

    makeEtaPlots("1.6<|#eta|<2.2",
                 mapTH1F["h_single_displaced_L1Mu_rate_eta_position_ME1_ME2_ME3_eta16to22_mediumVeto"], "L1Mu (unconstrained)",
                 mapTH1F["h_single_displaced_L1Mu_rate_eta_hybrid_GE11_ME11_GE21_ME21_ME3_eta16to22_mediumVeto"], "L1Mu (hybrid)",
                 mapTH1F["h_single_prompt_L1Mu_rate_pt_ME1_ME2_ME3_eta16to22"], "L1Mu (hybrid)",
                 "MuonTDR2017_Prompt_L1Mu_trigger_rate_eta__L1Mu__PositionBased_HybridBased_GE11_ME11_GE21_ME21_ME3_eta16to22_mediumVeto")


    makePlots("1.6<|#eta|<2.2",
                 mapTH1F["h_single_displaced_L1Mu_rate_pt_position_ME1_ME2_ME3_eta16to22_looseVeto"], "L1Mu (unconstrained)",
                 mapTH1F["h_single_displaced_L1Mu_rate_pt_hybrid_GE11_ME11_GE21_ME21_ME3_eta16to22_looseVeto"], "L1Mu (hybrid)",
                 mapTH1F["h_single_prompt_L1Mu_rate_pt_ME1_ME2_ME3_eta16to22"], "L1Mu (hybrid)",
                 "MuonTDR2017_Prompt_L1Mu_trigger_rate_pt__L1Mu__PositionBased_HybridBased_GE11_ME11_GE21_ME21_ME3_eta16to22_looseVeto")

    makeEtaPlots("1.6<|#eta|<2.2",
                 mapTH1F["h_single_displaced_L1Mu_rate_eta_position_ME1_ME2_ME3_eta16to22_looseVeto"], "L1Mu (unconstrained)",
                 mapTH1F["h_single_displaced_L1Mu_rate_eta_hybrid_GE11_ME11_GE21_ME21_ME3_eta16to22_looseVeto"], "L1Mu (hybrid)",
                 mapTH1F["h_single_prompt_L1Mu_rate_pt_ME1_ME2_ME3_eta16to22"], "L1Mu (hybrid)",
                 "MuonTDR2017_Prompt_L1Mu_trigger_rate_eta__L1Mu__PositionBased_HybridBased_GE11_ME11_GE21_ME21_ME3_eta16to22_looseVeto")

  displacedL1MuHybridTriggerRate()

