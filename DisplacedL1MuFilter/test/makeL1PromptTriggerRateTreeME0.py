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
import numpy as n
#______________________________________________________________________________
if __name__ == "__main__":

  label = "SingleNu_PU200_ME0Segment192"; pu = 'PU200'; eff = False

  ## extension for figures - add more?
  ext = ".png"

  ## Style
  #gStyle.SetStatStyle(0)

  print "Making the plots"

  set_style()

  doTest = False

  ch = TChain("DisplacedL1MuFilter_PhaseIIGE21_ME0Segment192/L1MuTree")

  location0 = '/eos/uscms/store/user/lpcgem/SingleNu_91X_FlatPt05_50_phase2_realistic_Extended2023D4_GEN_SIM_v2/SingleNu_EMTF_ME0_PU0_ANA_v1/170504_214525/0000/'
  location1 = '/eos/uscms/store/user/lpcgem/SingleNu_91X_FlatPt05_50_phase2_realistic_Extended2023D4_GEN_SIM_v2/SingleNu_EMTF_ME0_PU0_ANA_v1/170504_214525/0001/'

  tree = addfiles(ch, dirname=location0, ext=".root")
  tree = addfiles(ch, dirname=location1, ext=".root")

  file = TFile.Open("combined.root","RECREATE");
  ch.CloneTree();
  file.Write();
  #delete file.
  exit(1)

  targetDir = label + "/"

  if not os.path.exists(targetDir):
    os.makedirs(targetDir)
  verbose = False

  ## copy index file
  #import shutil
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

    L1MuRatetree = TTree("L1MuTriggerRate", "L1MuTriggerRate")

    ok_CSCTF_st1s = n.zeros(1, dtype=int)
    ok_CSCTF_st2s = n.zeros(1, dtype=int)
    ok_CSCTF_st3s = n.zeros(1, dtype=int)
    ok_CSCTF_st4s = n.zeros(1, dtype=int)

    CSCTF_phi1s = n.zeros(1, dtype=float)
    CSCTF_phi2s = n.zeros(1, dtype=float)
    CSCTF_phi3s = n.zeros(1, dtype=float)
    CSCTF_phi4s = n.zeros(1, dtype=float)


    #L1Mu track
    L1Mu_pt = n.zeros(1, dtype=float)
    L1Mu_charge = n.zeros(1, dtype=int)
    L1Mu_eta = n.zeros(1, dtype=float)
    L1Mu_eta_st2 = n.zeros(1, dtype=float)
    L1Mu_phi = n.zeros(1, dtype=float)
    L1Mu_bx = n.zeros(1, dtype=int)
    L1Mu_nstubs = n.zeros(1, dtype=int)
    L1Mu_quality = n.zeros(1, dtype=int)

    L1MuRatetree.Branch("L1Mu_pt",L1Mu_pt,"L1Mu_pt/D")
    L1MuRatetree.Branch("L1Mu_charge",L1Mu_charge,"L1Mu_charge/I")
    L1MuRatetree.Branch("L1Mu_eta",L1Mu_eta,"L1Mu_eta/D")
    L1MuRatetree.Branch("L1Mu_eta_st2",L1Mu_eta_st2,"L1Mu_eta_st2/D")
    L1MuRatetree.Branch("L1Mu_phi",L1Mu_phi,"L1Mu_phi/D")
    L1MuRatetree.Branch("L1Mu_bx",L1Mu_bx,"L1Mu_bx/I")
    L1MuRatetree.Branch("L1Mu_nstubs",L1Mu_nstubs,"L1Mu_nstubs/I")
    L1MuRatetree.Branch("L1Mu_quality",L1Mu_quality,"L1Mu_quality/I")

    L1MuRatetree.Branch('ok_CSCTF_st1', ok_CSCTF_st1s, 'ok_CSCTF_st1/I')
    L1MuRatetree.Branch('ok_CSCTF_st2', ok_CSCTF_st2s, 'ok_CSCTF_st2/I')
    L1MuRatetree.Branch('ok_CSCTF_st3', ok_CSCTF_st3s, 'ok_CSCTF_st3/I')
    L1MuRatetree.Branch('ok_CSCTF_st4', ok_CSCTF_st4s, 'ok_CSCTF_st4/I')

    L1MuRatetree.Branch('CSCTF_phi1', CSCTF_phi1s, 'CSCTF_phi1/D')
    L1MuRatetree.Branch('CSCTF_phi2', CSCTF_phi2s, 'CSCTF_phi2/D')
    L1MuRatetree.Branch('CSCTF_phi3', CSCTF_phi3s, 'CSCTF_phi3/D')
    L1MuRatetree.Branch('CSCTF_phi4', CSCTF_phi4s, 'CSCTF_phi4/D')

    #L1MuRatetree.Branch()

    h_eventcount = TH1F("h_eventcount","",10,0,10)

    maxEntries = ch.GetEntries()
    if doTest:
      maxEntries = 10000

    nEvents = maxEntries
    print "nEvents", nEvents
    for k in range(0,nEvents):
      if k%1==0: print "Processing event", k

      h_eventcount.Fill(1)
      ch.GetEntry(k)
      treeHits = ch

      def initbranches():
	  #init branches
	  L1Mu_pt[0] = -1
	  L1Mu_eta[0]= -9
	  L1Mu_eta_st2[0]= -9
	  L1Mu_phi[0] = -9
	  L1Mu_charge[0] = -9
	  L1Mu_bx[0] = 0
	  L1Mu_quality[0] = -1

          ok_CSCTF_st1s[0] = 0
          ok_CSCTF_st2s[0] = 0
          ok_CSCTF_st3s[0] = 0
          ok_CSCTF_st4s[0] = 0

          CSCTF_phi1s[0] = -99
          CSCTF_phi2s[0] = -99
          CSCTF_phi3s[0] = -99
          CSCTF_phi4s[0] = -99


      initbranches()

      doBXCut = True
      etaCutMin = 2.0
      etaCutMax = 2.5
      stubCut = 2
      qualityCut = 0
       # ptHistogram.Fill(prompt_L1Mu_pt)
      ## get the max value of the momentum
      pts = list(treeHits.L1Mu_pt)
      print "Muons in this event: ", len(pts)
      ## ignore events without L1Mu
      if len(pts)==0: continue

      ## function that returns the most likely high pT muon in the event
      max_pt, max_eta, found_index = getMaxPromptPtEtaEvent(treeHits,
                                                            doBXCut,
                                                            etaCutMin,
                                                            etaCutMax,
                                                            stubCut,
                                                            qualityCut)
      for i in range(0,len(pts)):
        initbranches()

        L1Mu_pt[0] = treeHits.L1Mu_pt[i]
        L1Mu_eta[0] = treeHits.L1Mu_eta[i]
        L1Mu_phi[0] = treeHits.L1Mu_phi[i]
        L1Mu_bx[0] = treeHits.L1Mu_bx[i]
        L1Mu_quality[0] = treeHits.L1Mu_quality[i]
        L1Mu_CSCTF_index = treeHits.L1Mu_CSCTF_index[i]
        L1Mu_charge[0] = treeHits.L1Mu_charge[i]

        ## eta cut
        if not (etaCutMin <= abs(L1Mu_eta[0]) and abs(L1Mu_eta[0]) <= etaCutMax): continue

        ## quality cut
        if L1Mu_quality[0] < qualityCut: continue

        ## BX cut
        if abs(L1Mu_bx[0]) != 0 and doBXCut: continue

        print "L1Mu pt", L1Mu_pt[0]
        print "L1Mu eta", L1Mu_eta[0]
        print "L1Mu phi", L1Mu_phi[0]
        print "L1Mu bx", L1Mu_bx[0]
        print "L1Mu quality", L1Mu_quality[0]

        print L1Mu_CSCTF_index

        ## not a CSC muon
        if L1Mu_CSCTF_index == -1: continue

        ## in case there is more than 1 muon, pick the one with likely the highest pT
        if found_index != i: continue

        CSCTF_phi1s[0] = treeHits.CSCTF_phi1[L1Mu_CSCTF_index]
        CSCTF_phi2s[0] = treeHits.CSCTF_phi2[L1Mu_CSCTF_index]
        CSCTF_phi3s[0] = treeHits.CSCTF_phi3[L1Mu_CSCTF_index]
        CSCTF_phi4s[0] = treeHits.CSCTF_phi4[L1Mu_CSCTF_index]

	L1MuRatetree.Fill()

    print "rate events", L1MuRatetree.GetEntries()

    c = TCanvas("c","c",800,600)
    c.Clear()
    h_eventcount.Draw()
    c.SaveAs("h_eventcount.png")
    #make plots before write into root
    targetroot = TFile(label + ".root","RECREATE")
    h_eventcount.Write()
    #h_dphi_ME11_ME21.Write()
    L1MuRatetree.Write()
    targetroot.Close()


    ## trigger rate plots
  displacedL1MuHybridTriggerRate()
