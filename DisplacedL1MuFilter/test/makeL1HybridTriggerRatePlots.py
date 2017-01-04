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

  label = "Neutrino_Pt2to20_gun_TTI2023Upg14D_PU140bx25_ILT_SLHC14_20170104"; pu = 'PU140'; eff = False

  ## extension for figures - add more?
  ext = ".png"

  ## Style
  gStyle.SetStatStyle(0)

  print "Making the plots"

  set_style()

  doTest = True

  ch = TChain("DisplacedL1MuFilter_PhaseIIGE21/L1MuTree")

  location =  '/eos/uscms/store/user/lpcgem/Neutrino_Pt2to20_gun/NeutrinoGun_14TeV_PU140_L1MuANA_v15_StubReco/0000/'
  location1 = '/eos/uscms/store/user/lpcgem/Neutrino_Pt2to20_gun/NeutrinoGun_14TeV_PU140_L1MuANA_v15_StubReco/0001/'
  location2 = '/eos/uscms/store/user/lpcgem/Neutrino_Pt2to20_gun/NeutrinoGun_14TeV_PU140_L1MuANA_v15_StubReco/0002/'

  treeHits = addfiles(ch, dirname=location, ext=".root")
  #treeHits = addfiles(ch, dirname=location1, ext=".root")
  #treeHits = addfiles(ch, dirname=location2, ext=".root")

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

    ## add plots
    addManyPlotsToTH1F(myptbin, myetabin,
                       "h_single_prompt_L1Mu_rate_eta00to09",
                       "h_single_prompt_L1Mu_rate_eta00to24",
                       "h_single_prompt_L1Mu_rate_eta12to24",
                       "h_single_prompt_L1Mu_rate_eta16to22",
                       "h_single_prompt_L1Mu_rate_eta16to20",
                       "h_single_prompt_L1Mu_rate_eta12to16",

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

                       "h_single_prompt_L1Mu_rate_3_stubs_ME1_ME2_ME3_eta12to24",
                       "h_single_prompt_L1Mu_rate_3_stubs_ME1_ME2_ME3_eta16to22",

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
                       "h_single_prompt_L1Mu_rate_GE11_ME11_GE21_ME21_ME3_eta16to22",

                       "h_single_prompt_L1Mu_rate_2_stubs_GE11_ME11_OR_GE21_ME21_eta16to22",
                       "h_single_prompt_L1Mu_rate_3_stubs_GE11_ME11_OR_GE21_ME21_eta16to22",

                       "h_single_prompt_L1Mu_rate_GE11_ME11_GE21_ME21_eta16to20",
                       "h_single_prompt_L1Mu_rate_GE11_ME11_GE21_ME21_ME3_eta16to20",

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
                       "h_single_displaced_L1Mu_rate_MB1_MB4_eta00to09",

                       "h_single_displaced_L1Mu_rate_3_stubs_ME1_ME2_ME3_eta12to16",
                       "h_single_displaced_L1Mu_rate_3_stubs_ME1_ME2_ME3_eta16to22",
                       "h_single_displaced_L1Mu_rate_3_stubs_ME1_ME2_ME3_eta12to24",

                       "h_single_displaced_L1Mu_rate_GE11_ME11_GE21_ME21_eta16to22",
                       "h_single_displaced_L1Mu_rate_GE11_ME11_GE21_ME21_ME3_eta16to22",

                       "h_single_displaced_L1Mu_rate_GE11_ME11_GE21_ME21_eta16to20",
                       "h_single_displaced_L1Mu_rate_GE11_ME11_GE21_ME21_ME3_eta16to20",

                       ## displaced muons + loose TT isolation
                       "h_single_displaced_L1Mu_rate_MB1_MB4_eta00to09_looseIso",

                       "h_single_displaced_L1Mu_rate_3_stubs_ME1_ME2_ME3_eta12to16_looseIso",
                       "h_single_displaced_L1Mu_rate_3_stubs_ME1_ME2_ME3_eta16to22_looseIso",
                       "h_single_displaced_L1Mu_rate_3_stubs_ME1_ME2_ME3_eta12to24_looseIso",

                       "h_single_displaced_L1Mu_rate_GE11_ME11_GE21_ME21_eta16to22_looseIso",
                       "h_single_displaced_L1Mu_rate_GE11_ME11_GE21_ME21_ME3_eta16to22_looseIso",

                       "h_single_displaced_L1Mu_rate_GE11_ME11_GE21_ME21_eta16to20_looseIso",
                       "h_single_displaced_L1Mu_rate_GE11_ME11_GE21_ME21_ME3_eta16to20_looseIso",

                       ## displaced muons + medium TT isolation
                       "h_single_displaced_L1Mu_rate_MB1_MB4_eta00to09_mediumIso",

                       "h_single_displaced_L1Mu_rate_3_stubs_ME1_ME2_ME3_eta12to16_mediumIso",
                       "h_single_displaced_L1Mu_rate_3_stubs_ME1_ME2_ME3_eta16to22_mediumIso",
                       "h_single_displaced_L1Mu_rate_3_stubs_ME1_ME2_ME3_eta12to24_mediumIso",

                       "h_single_displaced_L1Mu_rate_GE11_ME11_GE21_ME21_eta16to22_mediumIso",
                       "h_single_displaced_L1Mu_rate_GE11_ME11_GE21_ME21_ME3_eta16to22_mediumIso",

                       "h_single_displaced_L1Mu_rate_GE11_ME11_GE21_ME21_eta16to20_mediumIso",
                       "h_single_displaced_L1Mu_rate_GE11_ME11_GE21_ME21_ME3_eta16to20_mediumIso",

                       ## displaced muons + tight TT isolation
                       "h_single_displaced_L1Mu_rate_MB1_MB4_eta00to09_tightIso",

                       "h_single_displaced_L1Mu_rate_3_stubs_ME1_ME2_ME3_eta12to16_tightIso",
                       "h_single_displaced_L1Mu_rate_3_stubs_ME1_ME2_ME3_eta16to22_tightIso",
                       "h_single_displaced_L1Mu_rate_3_stubs_ME1_ME2_ME3_eta12to24_tightIso",

                       "h_single_displaced_L1Mu_rate_GE11_ME11_GE21_ME21_eta16to22_tightIso",
                       "h_single_displaced_L1Mu_rate_GE11_ME11_GE21_ME21_ME3_eta16to22_tightIso",

                       "h_single_displaced_L1Mu_rate_GE11_ME11_GE21_ME21_eta16to20_tightIso",
                       "h_single_displaced_L1Mu_rate_GE11_ME11_GE21_ME21_ME3_eta16to20_tightIso",
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

      ## overall rates
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
                          treeHits, True, 1.6, 2.2, 0, minQuality)
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_2_stubs_eta12to16"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_2_stubs_eta12to16"],
                          treeHits, True, 1.6, 2.2, 2, minQuality)
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_3_stubs_eta12to16"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_3_stubs_eta12to16"],
                          treeHits, True, 1.6, 2.2, 3, minQuality)

      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_3_stubs_ME1_ME2_ME3_eta12to24"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_3_stubs_ME1_ME2_ME3_eta12to24"],
                          treeHits, True, 1.2, 2.4, 0, minQuality,
                          hasME1Cut=True, hasME2Cut=True, hasME3Cut=True)
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_3_stubs_ME1_ME2_ME3_eta16to22"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_3_stubs_ME1_ME2_ME3_eta16to22"],
                          treeHits, True, 1.6, 2.2, 0, minQuality,
                          hasME1Cut=True, hasME2Cut=True, hasME3Cut=True)

      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_2_stubs_ME11_eta16to22"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_2_stubs_ME11_eta16to22"],
                          treeHits,True, 1.6, 2.2, 2, minQuality, hasME11Cut=True)
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_3_stubs_ME11_eta16to22"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_3_stubs_ME11_eta16to22"],
                          treeHits,True, 1.6, 2.2, 3, minQuality, hasME11Cut=True)

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
                          treeHits,True, 1.6, 2.2, 2, minQuality, hasME11Cut=True, hasGE11Cut=True)
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_3_stubs_GE11_GE21_eta16to22"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_3_stubs_GE11_GE21_eta16to22"],
                          treeHits,True, 1.6, 2.2, 3, minQuality, hasME11Cut=True, hasGE11Cut=True)


      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_2_stubs_GE11_ME11_eta16to22"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_2_stubs_GE11_ME11_eta16to22"],
                          treeHits,True, 1.6, 2.2, 2, minQuality, hasME11Cut=True, hasGE11Cut=True)
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_3_stubs_GE11_ME11_eta16to22"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_3_stubs_GE11_ME11_eta16to22"],
                          treeHits,True, 1.6, 2.2, 3, minQuality, hasME11Cut=True, hasGE11Cut=True)

      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_2_stubs_GE21_ME21_eta16to22"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_2_stubs_GE21_ME21_eta16to22"],
                          treeHits,True, 1.6, 2.2, 2, minQuality, hasME21Cut=True, hasGE21Cut=True)
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_3_stubs_GE21_ME21_eta16to22"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_3_stubs_GE21_ME21_eta16to22"],
                          treeHits,True, 1.6, 2.2, 3, minQuality, hasME21Cut=True, hasGE21Cut=True)

      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_2_stubs_GE11_ME11_OR_GE21_ME21_eta16to22"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_2_stubs_GE11_ME11_OR_GE21_ME21_eta16to22"],
                          treeHits,True, 1.6, 2.2, 2, minQuality, hasME11ME21Cut=True, hasGE11GE21Cut=True)
      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_3_stubs_GE11_ME11_OR_GE21_ME21_eta16to22"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_3_stubs_GE11_ME11_OR_GE21_ME21_eta16to22"],
                          treeHits,True, 1.6, 2.2, 3, minQuality, hasME11ME21Cut=True, hasGE11GE21Cut=True)


      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_GE11_ME11_GE21_ME21_eta16to22"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to22"],
                          treeHits,True, 1.6, 2.2, 0, minQuality, hasME11Cut=True, hasME21Cut=True, hasGE11Cut=True, hasGE21Cut=True)

      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_GE11_ME11_GE21_ME21_ME3_eta16to22"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_ME3_eta16to22"],
                          treeHits,True, 1.6, 2.2, 0, minQuality, hasME11Cut=True, hasME21Cut=True, hasGE11Cut=True, hasGE21Cut=True, hasME3Cut=True)

      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_GE11_ME11_GE21_ME21_eta16to20"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20"],
                          treeHits,True, 1.6, 2.0, 0, minQuality, hasME11Cut=True, hasME21Cut=True, hasGE11Cut=True, hasGE21Cut=True)

      fillPtEtaHistogram( mapTH1F["h_single_prompt_L1Mu_rate_pt_GE11_ME11_GE21_ME21_ME3_eta16to20"],
                          mapTH1F["h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_ME3_eta16to20"],
                          treeHits,True, 1.6, 2.0, 0, minQuality, hasME11Cut=True, hasME21Cut=True, hasGE11Cut=True, hasGE21Cut=True, hasME3Cut=True)

      ## displaced L1Mu trigger rate curves
      #fillDisplacedPtHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_MB1_MB4_eta00to09"], treeHits, True, 0.0, 0.9, 0, minQuality, hasMB1Cut=True, hasMB4Cut=True)




      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_3_stubs_ME1_ME2_ME3_eta16to22"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_3_stubs_ME1_ME2_ME3_eta16to22"],
                                   treeHits, True, 1.6, 2.2, 0, minQuality, doPositionBased=True)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_3_stubs_ME1_ME2_ME3_eta12to24"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_3_stubs_ME1_ME2_ME3_eta12to24"],
                                   treeHits, True, 1.2, 2.4, 0, minQuality, doPositionBased=True)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_GE11_ME11_GE21_ME21_eta16to22"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to22"],
                                   treeHits, True, 1.6, 2.2, 0, minQuality, doDirectionBased=True)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_GE11_ME11_GE21_ME21_ME3_eta16to22"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_ME3_eta16to22"],
                                   treeHits, True, 1.6, 2.2, 0, minQuality, doHybridBased=True)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_GE11_ME11_GE21_ME21_eta16to20"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20"],
                                   treeHits, True, 1.6, 2.0, 0, minQuality, doDirectionBased=True)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_GE11_ME11_GE21_ME21_ME3_eta16to20"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_ME3_eta16to20"],
                                   treeHits, True, 1.6, 2.0, 0, minQuality, doHybridBased=True)

      ## loose isolation
      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_3_stubs_ME1_ME2_ME3_eta16to22_looseIso"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_3_stubs_ME1_ME2_ME3_eta16to22_looseIso"],
                                   treeHits, True, 1.6, 2.2, 0, minQuality, doPositionBased=True,
                                   doIsolation=True, isolationType=1)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_3_stubs_ME1_ME2_ME3_eta12to24_looseIso"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_3_stubs_ME1_ME2_ME3_eta12to24_looseIso"],
                                   treeHits, True, 1.2, 2.4, 0, minQuality, doPositionBased=True,
                                   doIsolation=True, isolationType=1)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_GE11_ME11_GE21_ME21_eta16to22_looseIso"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to22_looseIso"],
                                   treeHits, True, 1.6, 2.2, 0, minQuality, doDirectionBased=True,
                                   doIsolation=True, isolationType=1)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_GE11_ME11_GE21_ME21_ME3_eta16to22_looseIso"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_ME3_eta16to22_looseIso"],
                                   treeHits, True, 1.6, 2.2, 0, minQuality, doHybridBased=True,
                                   doIsolation=True, isolationType=1)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_GE11_ME11_GE21_ME21_eta16to20_looseIso"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20_looseIso"],
                                   treeHits, True, 1.6, 2.0, 0, minQuality, doDirectionBased=True,
                                   doIsolation=True, isolationType=1)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_GE11_ME11_GE21_ME21_ME3_eta16to20_looseIso"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_ME3_eta16to20_looseIso"],
                                   treeHits, True, 1.6, 2.0, 0, minQuality, doHybridBased=True,
                                   doIsolation=True, isolationType=1)

      ## medium isolation
      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_3_stubs_ME1_ME2_ME3_eta16to22_mediumIso"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_3_stubs_ME1_ME2_ME3_eta16to22_mediumIso"],
                                   treeHits, True, 1.6, 2.2, 0, minQuality, doPositionBased=True,
                                   doIsolation=True, isolationType=2)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_3_stubs_ME1_ME2_ME3_eta12to24_mediumIso"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_3_stubs_ME1_ME2_ME3_eta12to24_mediumIso"],
                                   treeHits, True, 1.2, 2.4, 0, minQuality, doPositionBased=True,
                                   doIsolation=True, isolationType=2)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_GE11_ME11_GE21_ME21_eta16to22_mediumIso"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to22_mediumIso"],
                                   treeHits, True, 1.6, 2.2, 0, minQuality, doDirectionBased=True,
                                   doIsolation=True, isolationType=2)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_GE11_ME11_GE21_ME21_ME3_eta16to22_mediumIso"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_ME3_eta16to22_mediumIso"],
                                   treeHits, True, 1.6, 2.2, 0, minQuality, doHybridBased=True,
                                   doIsolation=True, isolationType=2)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_GE11_ME11_GE21_ME21_eta16to20_mediumIso"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20_mediumIso"],
                                   treeHits, True, 1.6, 2.0, 0, minQuality, doDirectionBased=True,
                                   doIsolation=True, isolationType=2)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_GE11_ME11_GE21_ME21_ME3_eta16to20_mediumIso"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_ME3_eta16to20_mediumIso"],
                                   treeHits, True, 1.6, 2.0, 0, minQuality, doHybridBased=True,
                                   doIsolation=True, isolationType=2)


      ## tight isolation
      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_3_stubs_ME1_ME2_ME3_eta16to22_tightIso"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_3_stubs_ME1_ME2_ME3_eta16to22_tightIso"],
                                   treeHits, True, 1.6, 2.2, 0, minQuality, doPositionBased=True,
                                   doIsolation=True, isolationType=3)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_3_stubs_ME1_ME2_ME3_eta12to24_tightIso"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_3_stubs_ME1_ME2_ME3_eta12to24_tightIso"],
                                   treeHits, True, 1.2, 2.4, 0, minQuality, doPositionBased=True,
                                   doIsolation=True, isolationType=3)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_GE11_ME11_GE21_ME21_eta16to22_tightIso"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to22_tightIso"],
                                   treeHits, True, 1.6, 2.2, 0, minQuality, doDirectionBased=True,
                                   doIsolation=True, isolationType=3)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_GE11_ME11_GE21_ME21_ME3_eta16to22_tightIso"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_ME3_eta16to22_tightIso"],
                                   treeHits, True, 1.6, 2.2, 0, minQuality, doHybridBased=True,
                                   doIsolation=True, isolationType=3)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_GE11_ME11_GE21_ME21_eta16to20_tightIso"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20_tightIso"],
                                   treeHits, True, 1.6, 2.0, 0, minQuality, doDirectionBased=True,
                                   doIsolation=True, isolationType=3)

      fillDisplacedPtEtaHistogram( mapTH1F["h_single_displaced_L1Mu_rate_pt_GE11_ME11_GE21_ME21_ME3_eta16to20_tightIso"],
                                   mapTH1F["h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_ME3_eta16to20_tightIso"],
                                   treeHits, True, 1.6, 2.0, 0, minQuality, doHybridBased=True,
                                   doIsolation=True, isolationType=3)


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

      print "nEvents", nEvents, "entries", h1.GetEntries(), h2.GetEntries(), h3.GetEntries()
      if doEta:
        h1 = getRateEtaHistogram(nEvents, h1)
        h2 = getRateEtaHistogram(nEvents, h2)
        h3 = getRateEtaHistogram(nEvents, h3)
      else:
        h1 = getRatePtHistogram(nEvents, h1)
        h2 = getRatePtHistogram(nEvents, h2)
        h3 = getRatePtHistogram(nEvents, h3)

      if doEta:
        h1.SetLineColor(kRed)
        h1.SetFillColor(kRed)
        h1.Draw("P same")

        h2.SetLineColor(kViolet)
        h2.SetFillColor(kViolet)
        h2.Draw("P same")

        h3.SetLineColor(kBlue)
        h3.SetFillColor(kBlue)
        h3.Draw("P same")
      else:
        h1.SetFillColor(kRed)
        h1.SetLineColor(kRed)
        h1.SetMarkerColor(kRed)
        h1.Draw("P same")

        h2.SetFillColor(kViolet)
        h2.SetLineColor(kViolet)
        h2.SetMarkerColor(kViolet)
        h2.Draw("P same")

        h3.SetFillColor(kBlue)
        h3.SetLineColor(kBlue)
        h3.SetMarkerColor(kBlue)
        h3.Draw("P same")

      #latex = applyTdrStyle()

      leg = TLegend(0.15,0.2,0.5,0.35,legendTitle,"brNDC")
      leg.SetFillColor(kWhite)
      leg.SetBorderSize(0)
      leg.SetFillStyle(0)
      leg.SetTextSize(0.04)
      leg.AddEntry(h1, h1Legend, "f")
      leg.AddEntry(h2, h2Legend, "f")
      leg.AddEntry(h3, h3Legend, "f")
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

    ## trigger rate plots vs pt
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



    ## prompt trigger with failing chambers
    makePlots("1.6<|#eta|<2.2",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_2_stubs_ME11_eta16to22"], "Prompt L1Mu, 2 CSC stubs, ME11",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_2_stubs_ME11_Fail10p_eta16to22"], "Prompt L1Mu, 2 CSC stubs, failing ME11",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_2_stubs_ME11_Fail10p_GE11_eta16to22"], "Prompt L1Mu, 2 CSC stubs, failing ME11, GE11",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu2stME11__L1Mu2stME11Fail_eta16to22")

    """
    makePlots("1.6<|#eta|<2.2",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_2_stubs_ME11_eta16to22"], "Prompt L1Mu, 2 CSC stubs, ME11",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_2_stubs_ME11_Fail10p_GE11_eta16to22"], "Prompt L1Mu, 2 CSC stubs, ME11, GE11",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_2_stubs_ME11_Fail10p_GE11_GE21_eta16to22"], "Prompt L1Mu, 2 CSC stubs, ME11, GE11, GE21",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu2stME11__L1Mu2stME11FailGE11__L1Mu2stME11FailGE11GE21_eta16to22")

    makePlots("1.6<|#eta|<2.2",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_3_stubs_ME11_eta16to22"], "Prompt L1Mu, 3 CSC stubs, ME11",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_3_stubs_ME11_Fail10p_GE11_eta16to22"], "Prompt L1Mu, 3 CSC stubs, ME11, GE11",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_3_stubs_ME11_Fail10p_GE11_GE21_eta16to22"], "Prompt L1Mu, 3 CSC stubs, ME11, GE11, GE21",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu3stME11__L1Mu3stME11FailGE11__L1Mu3stME11FailGE11GE21_eta16to22")
    """

    ## displaced L1Mu trigger plots
    ## trigger rate plots vs pt
    makePlots("1.6<|#eta|<2.2",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_eta16to22"], "Prompt L1Mu",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_3_stubs_ME1_ME2_ME3_eta16to22"], "Prompt L1Mu, hit in ME1, ME2, ME3",
              mapTH1F["h_single_displaced_L1Mu_rate_pt_3_stubs_ME1_ME2_ME3_eta16to22"], "Displaced L1Mu, hit in ME1, ME2, ME3, position based",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu3st__DisplacedL1MuPositionBased_eta16to22")

    makePlots("1.2<|#eta|<2.4",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_eta12to24"], "Prompt L1Mu",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_3_stubs_ME1_ME2_ME3_eta12to24"], "Prompt L1Mu, hit in ME1, ME2, ME3",
              mapTH1F["h_single_displaced_L1Mu_rate_pt_3_stubs_ME1_ME2_ME3_eta12to24"], "Displaced L1Mu, hit in ME1, ME2, ME3, position based",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu3st__DisplacedL1MuPositionBased_eta12to24")

    makePlots("1.6<|#eta|<2.2",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_eta16to22"], "Prompt L1Mu",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_GE11_ME11_GE21_ME21_eta16to22"], "Prompt L1Mu, hit in GE11, ME11, GE21, ME21",
              mapTH1F["h_single_displaced_L1Mu_rate_pt_GE11_ME11_GE21_ME21_eta16to22"], "Displaced L1Mu, hit in GE11, ME11, GE21, ME21 direction based",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu3st__DisplacedL1MuDirectionBased_eta16to22")

    makePlots("1.6<|#eta|<2.2",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_eta16to22"], "Prompt L1Mu",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_GE11_ME11_GE21_ME21_ME3_eta16to22"], "Prompt L1Mu, hit in GE11, ME11, GE21, ME21, ME3",
              mapTH1F["h_single_displaced_L1Mu_rate_pt_GE11_ME11_GE21_ME21_ME3_eta16to22"], "Displaced L1Mu, hit in GE11, ME11, GE21, ME21, ME3 hybrid based",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu3st__DisplacedL1MuHybridBased_eta16to22")

    makePlots("1.6<|#eta|<2.0",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_eta16to20"], "Prompt L1Mu",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_GE11_ME11_GE21_ME21_eta16to20"], "Prompt L1Mu, hit in GE11, ME11, GE21, ME21",
              mapTH1F["h_single_displaced_L1Mu_rate_pt_GE11_ME11_GE21_ME21_eta16to20"], "Displaced L1Mu, hit in GE11, ME11, GE21, ME21 direction based",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu3st__DisplacedL1MuDirectionBased_eta16to20")

    makePlots("1.6<|#eta|<2.0",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_eta16to20"], "Prompt L1Mu",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_GE11_ME11_GE21_ME21_ME3_eta16to20"], "Prompt L1Mu, hit in GE11, ME11, GE21, ME21, ME3",
              mapTH1F["h_single_displaced_L1Mu_rate_pt_GE11_ME11_GE21_ME21_ME3_eta16to20"], "Displaced L1Mu, hit in GE11, ME11, GE21, ME21, ME3 hybrid based",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu3st__DisplacedL1MuHybridBased_eta16to20")

    makePlots("0.0<|#eta|<0.9",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_eta00to09"], "Prompt L1Mu",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_MB1_MB4_eta00to09"], "Prompt L1Mu, hit in MB1, MB4",
              mapTH1F["h_single_displaced_L1Mu_rate_pt_MB1_MB4_eta00to09"], "Displaced L1Mu, hit in MB1, MB4, direction based",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu2st__DisplacedL1Mu2st_eta00to09")


    ## rates vs eta
    makeEtaPlots("1.2<|#eta|<2.4",
                 mapTH1F["h_single_prompt_L1Mu_rate_eta_eta12to24"], "Prompt L1Mu",
                 mapTH1F["h_single_prompt_L1Mu_rate_eta_3_stubs_ME1_ME2_ME3_eta12to24"], "Prompt L1Mu, hit in ME1, ME2, ME3",
                 mapTH1F["h_single_displaced_L1Mu_rate_eta_3_stubs_ME1_ME2_ME3_eta12to24"], "Displaced L1Mu, hit in ME1, ME2, ME3 position based",
                 "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu3st__DisplacedL1MuPositionBased_eta12to24", doEta=True)

    makeEtaPlots("1.6<|#eta|<2.0",
                 mapTH1F["h_single_prompt_L1Mu_rate_eta_eta16to20"], "Prompt L1Mu",
                 mapTH1F["h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20"], "Prompt L1Mu, hit in GE11, ME11, GE21, ME21",
                 mapTH1F["h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20"], "Displaced L1Mu, hit in GE11, ME11, GE21, ME21 direction based",
                 "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu3st__DisplacedL1MuDirectionBased_eta16to20", doEta=True)

    makeEtaPlots("1.6<|#eta|<2.2",
                 mapTH1F["h_single_prompt_L1Mu_rate_eta_eta16to22"], "Prompt L1Mu",
                 mapTH1F["h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to22"], "Prompt L1Mu, hit in GE11, ME11, GE21, ME21",
                 mapTH1F["h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to22"], "Displaced L1Mu, hit in GE11, ME11, GE21, ME21 direction based",
                 "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu3st__DisplacedL1MuDirectionBased_eta16to22", doEta=True)

    makeEtaPlots("1.6<|#eta|<2.2",
                 mapTH1F["h_single_prompt_L1Mu_rate_eta_eta16to22"], "Prompt L1Mu",
                 mapTH1F["h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_ME3_eta16to22"], "Prompt L1Mu, hit in GE11, ME11, GE21, ME21, ME3",
                 mapTH1F["h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_ME3_eta16to22"], "Displaced L1Mu, hit in GE11, ME11, GE21, ME21, ME3 hybrid based",
                 "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu3st__DisplacedL1MuhybridBased_eta16to22", doEta=True)

    makeEtaPlots("1.6<|#eta|<2.0",
                 mapTH1F["h_single_prompt_L1Mu_rate_eta_eta16to20"], "Prompt L1Mu",
                 mapTH1F["h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_ME3_eta16to20"], "Prompt L1Mu, hit in GE11, ME11, GE21, ME21, ME3",
                 mapTH1F["h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_ME3_eta16to20"], "Displaced L1Mu, hit in GE11, ME11, GE21, ME21, ME3 hybrid based",
                 "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu3st__DisplacedL1MuhybridBased_eta16to20", doEta=True)

    makeEtaPlots("0.0<|#eta|<2.4",
                 mapTH1F["h_single_prompt_L1Mu_rate_eta_eta00to24"], "Prompt L1Mu",
                 mapTH1F["h_single_prompt_L1Mu_rate_eta_2_stubs_eta00to24"], "Prompt L1Mu, 2 stubs",
                 mapTH1F["h_single_prompt_L1Mu_rate_eta_3_stubs_eta00to24"], "Prompt L1Mu, 3 stubs",
                 "Prompt_L1Mu_trigger_rate_eta__L1Mu__L1Mu2st__L1Mu3st_eta00to24", doEta=True)



    ## rates with isolation

    makePlots("1.2<|#eta|<2.4",
              mapTH1F["h_single_prompt_L1Mu_rate_pt_3_stubs_ME1_ME2_ME3_eta12to24"], "Prompt L1Mu, hit in ME1, ME2, ME3",
              mapTH1F["h_single_displaced_L1Mu_rate_pt_3_stubs_ME1_ME2_ME3_eta12to24"], "Displaced L1Mu, hit in ME1, ME2, ME3, position based",
              mapTH1F["h_single_displaced_L1Mu_rate_pt_3_stubs_ME1_ME2_ME3_eta12to24_looseIso"], "Displaced L1Mu, hit in ME1, ME2, ME3, position based, loose Iso",
              "Prompt_L1Mu_trigger_rate_pt__L1Mu__L1Mu3st__DisplacedL1MuPositionBased_eta12to24_looseIso")


  displacedL1MuHybridTriggerRate()

