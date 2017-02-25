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
import numpy as n
#______________________________________________________________________________
if __name__ == "__main__":

  label = "Neutrino_Pt2to20_gun_TTI2023Upg14D_PU140bx25_ILT_SLHC14_20170223_BarrelTree"; pu = 'PU140'; eff = False

  ## extension for figures - add more?
  ext = ".png"

  ## Style
  #gStyle.SetStatStyle(0)

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

    ok_DTTF_st1s = n.zeros(1, dtype=int)
    ok_DTTF_st2s = n.zeros(1, dtype=int)
    ok_DTTF_st3s = n.zeros(1, dtype=int)
    ok_DTTF_st4s = n.zeros(1, dtype=int)
    
    DTTF_phi1s = n.zeros(1, dtype=float)
    DTTF_phi2s = n.zeros(1, dtype=float)
    DTTF_phi3s = n.zeros(1, dtype=float)
    DTTF_phi4s = n.zeros(1, dtype=float)
    
    DTTF_phib1s = n.zeros(1, dtype=float)
    DTTF_phib2s = n.zeros(1, dtype=float)
    DTTF_phib3s = n.zeros(1, dtype=float)
    DTTF_phib4s = n.zeros(1, dtype=float)
    
    DTTF_phib1_phib2s = n.zeros(1, dtype=float)
    DTTF_phib1_phib3s = n.zeros(1, dtype=float)
    DTTF_phib1_phib4s = n.zeros(1, dtype=float)
    DTTF_phib2_phib3s = n.zeros(1, dtype=float)
    DTTF_phib2_phib4s = n.zeros(1, dtype=float)
    DTTF_phib3_phib4s = n.zeros(1, dtype=float)
    
    abs_DTTF_phib1_phib2s = n.zeros(1, dtype=float)
    abs_DTTF_phib1_phib3s = n.zeros(1, dtype=float)
    abs_DTTF_phib1_phib4s = n.zeros(1, dtype=float)
    abs_DTTF_phib2_phib3s = n.zeros(1, dtype=float)
    abs_DTTF_phib2_phib4s = n.zeros(1, dtype=float)
    abs_DTTF_phib3_phib4s = n.zeros(1, dtype=float)

    DTTF_DT1_DT2_pts = n.zeros(1, dtype=float)
    DTTF_DT1_DT3_pts = n.zeros(1, dtype=float)
    DTTF_DT1_DT4_pts = n.zeros(1, dtype=float)
    DTTF_DT2_DT3_pts = n.zeros(1, dtype=float)
    DTTF_DT2_DT4_pts = n.zeros(1, dtype=float)
    DTTF_DT3_DT4_pts = n.zeros(1, dtype=float)


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

    L1MuRatetree.Branch('ok_DTTF_st1', ok_DTTF_st1s, 'ok_DTTF_st1/I')
    L1MuRatetree.Branch('ok_DTTF_st2', ok_DTTF_st2s, 'ok_DTTF_st2/I')
    L1MuRatetree.Branch('ok_DTTF_st3', ok_DTTF_st3s, 'ok_DTTF_st3/I')
    L1MuRatetree.Branch('ok_DTTF_st4', ok_DTTF_st4s, 'ok_DTTF_st4/I')
    
    L1MuRatetree.Branch('DTTF_phi1', DTTF_phi1s, 'DTTF_phi1/D')
    L1MuRatetree.Branch('DTTF_phi2', DTTF_phi2s, 'DTTF_phi2/D')
    L1MuRatetree.Branch('DTTF_phi3', DTTF_phi3s, 'DTTF_phi3/D')
    L1MuRatetree.Branch('DTTF_phi4', DTTF_phi4s, 'DTTF_phi4/D')
    
    L1MuRatetree.Branch('DTTF_phib1', DTTF_phib1s, 'DTTF_phib1/D')
    L1MuRatetree.Branch('DTTF_phib2', DTTF_phib2s, 'DTTF_phib2/D')
    L1MuRatetree.Branch('DTTF_phib3', DTTF_phib3s, 'DTTF_phib3/D')
    L1MuRatetree.Branch('DTTF_phib4', DTTF_phib4s, 'DTTF_phib4/D')
    
    L1MuRatetree.Branch('DTTF_phib1_phib2', DTTF_phib1_phib2s, 'DTTF_phib1_phib2/D')
    L1MuRatetree.Branch('DTTF_phib1_phib3', DTTF_phib1_phib3s, 'DTTF_phib1_phib3/D')
    L1MuRatetree.Branch('DTTF_phib1_phib4', DTTF_phib1_phib4s, 'DTTF_phib1_phib4/D')
    L1MuRatetree.Branch('DTTF_phib2_phib3', DTTF_phib2_phib3s, 'DTTF_phib2_phib3/D')
    L1MuRatetree.Branch('DTTF_phib2_phib4', DTTF_phib2_phib4s, 'DTTF_phib2_phib4/D')
    L1MuRatetree.Branch('DTTF_phib3_phib4', DTTF_phib3_phib4s, 'DTTF_phib3_phib4/D')

    L1MuRatetree.Branch('abs_DTTF_phib1_phib2', abs_DTTF_phib1_phib2s, 'abs_DTTF_phib1_phib2/D')
    L1MuRatetree.Branch('abs_DTTF_phib1_phib3', abs_DTTF_phib1_phib3s, 'abs_DTTF_phib1_phib3/D')
    L1MuRatetree.Branch('abs_DTTF_phib1_phib4', abs_DTTF_phib1_phib4s, 'abs_DTTF_phib1_phib4/D')
    L1MuRatetree.Branch('abs_DTTF_phib2_phib3', abs_DTTF_phib2_phib3s, 'abs_DTTF_phib2_phib3/D')
    L1MuRatetree.Branch('abs_DTTF_phib2_phib4', abs_DTTF_phib2_phib4s, 'abs_DTTF_phib2_phib4/D')
    L1MuRatetree.Branch('abs_DTTF_phib3_phib4', abs_DTTF_phib3_phib4s, 'abs_DTTF_phib3_phib4/D')

    L1MuRatetree.Branch('DTTF_DT1_DT2_pt', DTTF_DT1_DT2_pts, 'DTTF_DT1_DT2_pt/D')
    L1MuRatetree.Branch('DTTF_DT1_DT3_pt', DTTF_DT1_DT3_pts, 'DTTF_DT1_DT3_pt/D')
    L1MuRatetree.Branch('DTTF_DT1_DT4_pt', DTTF_DT1_DT4_pts, 'DTTF_DT1_DT4_pt/D')
    L1MuRatetree.Branch('DTTF_DT2_DT3_pt', DTTF_DT2_DT3_pts, 'DTTF_DT2_DT3_pt/D')
    L1MuRatetree.Branch('DTTF_DT2_DT4_pt', DTTF_DT2_DT4_pts, 'DTTF_DT2_DT4_pt/D')
    L1MuRatetree.Branch('DTTF_DT3_DT4_pt', DTTF_DT3_DT4_pts, 'DTTF_DT3_DT4_pt/D')

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

          ok_DTTF_st1s[0] = 0
          ok_DTTF_st2s[0] = 0
          ok_DTTF_st3s[0] = 0
          ok_DTTF_st4s[0] = 0

          DTTF_phi1s[0] = -99
          DTTF_phi2s[0] = -99
          DTTF_phi3s[0] = -99
          DTTF_phi4s[0] = -99

          DTTF_phib1s[0] = -99
          DTTF_phib2s[0] = -99
          DTTF_phib3s[0] = -99
          DTTF_phib4s[0] = -99

          DTTF_phib1_phib2s[0] = -99
          DTTF_phib1_phib3s[0] = -99
          DTTF_phib1_phib4s[0] = -99
          DTTF_phib2_phib3s[0] = -99
          DTTF_phib2_phib4s[0] = -99
          DTTF_phib3_phib4s[0] = -99

          abs_DTTF_phib1_phib2s[0] = -99
          abs_DTTF_phib1_phib3s[0] = -99
          abs_DTTF_phib1_phib4s[0] = -99
          abs_DTTF_phib2_phib3s[0] = -99
          abs_DTTF_phib2_phib4s[0] = -99
          abs_DTTF_phib3_phib4s[0] = -99

          DTTF_DT1_DT2_pts[0] = -99
          DTTF_DT1_DT3_pts[0] = -99
          DTTF_DT1_DT4_pts[0] = -99
          DTTF_DT2_DT3_pts[0] = -99
          DTTF_DT2_DT4_pts[0] = -99
          DTTF_DT3_DT4_pts[0] = -99


      initbranches()

      doBXCut = True
      etaCutMin = 0.0
      etaCutMax = 0.9
      stubCut = 2
      qualityCut = 4
       # ptHistogram.Fill(prompt_L1Mu_pt)
      ## get the max value of the momentum
      pts = list(treeHits.L1Mu_pt)

      ## ignore events without L1Mu
      if len(pts)==0: continue

      minQuality = 4

      ## function that returns the most likely high pT muon in the event
      max_pt, max_eta, found_index = getMaxDisplacedBarrelPtEtaEvent(treeHits,
                                                                     doBXCut,
                                                                     etaCutMin,
                                                                     etaCutMax,
                                                                     stubCut,
                                                                     qualityCut, 
                                                                     algorithm=9)
      for i in range(0,len(pts)):
        initbranches()

        L1Mu_pt[0] = treeHits.L1Mu_pt[i]
        L1Mu_eta[0] = treeHits.L1Mu_eta[i]
        L1Mu_phi[0] = treeHits.L1Mu_phi[i]
        L1Mu_bx[0] = treeHits.L1Mu_bx[i]
        L1Mu_quality[0] = treeHits.L1Mu_quality[i]
        L1Mu_DTTF_index = treeHits.L1Mu_DTTF_index[i]
        L1Mu_charge[0] = treeHits.L1Mu_charge[i]
     
        ## eta cut
        if not (etaCutMin <= abs(L1Mu_eta[0]) and abs(L1Mu_eta[0]) <= etaCutMax): continue
     
        ## quality cut
        if L1Mu_quality[0] < qualityCut: continue
     
        ## BX cut
        if abs(L1Mu_bx[0]) != 0 and doBXCut: continue
      
        print L1Mu_DTTF_index
      
        ## not a CSC muon
        if L1Mu_DTTF_index == -1: continue

        ## in case there is more than 1 muon, pick the one with likely the highest pT
        if found_index != i: continue

        DTTF_phib1s[0] = treeHits.DTTF_phib1[L1Mu_DTTF_index]
        DTTF_phib2s[0] = treeHits.DTTF_phib2[L1Mu_DTTF_index]
        DTTF_phib3s[0] = treeHits.DTTF_phib3[L1Mu_DTTF_index]
        DTTF_phib4s[0] = treeHits.DTTF_phib4[L1Mu_DTTF_index]
        
        DTTF_phi1s[0] = treeHits.DTTF_phi1[L1Mu_DTTF_index]
        DTTF_phi2s[0] = treeHits.DTTF_phi2[L1Mu_DTTF_index]
        DTTF_phi3s[0] = treeHits.DTTF_phi3[L1Mu_DTTF_index]
        DTTF_phi4s[0] = treeHits.DTTF_phi4[L1Mu_DTTF_index]
        
        ok_DTTF_st1s[0] = DTTF_phib1s[0] != 99 and DTTF_phi1s[0] != 99 
        ok_DTTF_st2s[0] = DTTF_phib2s[0] != 99 and DTTF_phi2s[0] != 99 
        ok_DTTF_st3s[0] = DTTF_phib3s[0] != 99 and DTTF_phi3s[0] != 99
        ok_DTTF_st4s[0] = DTTF_phib4s[0] != 99 and DTTF_phi4s[0] != 99
        
        DTTF_phib1s[0] = normalizedPhi(DTTF_phib1s[0] + DTTF_phi1s[0])
        DTTF_phib2s[0] = normalizedPhi(DTTF_phib2s[0] + DTTF_phi2s[0])
        DTTF_phib3s[0] = normalizedPhi(DTTF_phib3s[0] + DTTF_phi3s[0])
        DTTF_phib4s[0] = normalizedPhi(DTTF_phib4s[0] + DTTF_phi4s[0])
        
        DTTF_phib1_phib2s[0] = deltaPhi(DTTF_phib1s[0], DTTF_phib2s[0])
        DTTF_phib1_phib3s[0] = deltaPhi(DTTF_phib1s[0], DTTF_phib3s[0])
        DTTF_phib1_phib4s[0] = deltaPhi(DTTF_phib1s[0], DTTF_phib4s[0])
        DTTF_phib2_phib3s[0] = deltaPhi(DTTF_phib2s[0], DTTF_phib3s[0])
        DTTF_phib2_phib4s[0] = deltaPhi(DTTF_phib2s[0], DTTF_phib4s[0])
        DTTF_phib3_phib4s[0] = deltaPhi(DTTF_phib3s[0], DTTF_phib4s[0])

        abs_DTTF_phib1_phib2s[0] = abs(deltaPhi(DTTF_phib1s[0], DTTF_phib2s[0]))
        abs_DTTF_phib1_phib3s[0] = abs(deltaPhi(DTTF_phib1s[0], DTTF_phib3s[0]))
        abs_DTTF_phib1_phib4s[0] = abs(deltaPhi(DTTF_phib1s[0], DTTF_phib4s[0]))
        abs_DTTF_phib2_phib3s[0] = abs(deltaPhi(DTTF_phib2s[0], DTTF_phib3s[0]))
        abs_DTTF_phib2_phib4s[0] = abs(deltaPhi(DTTF_phib2s[0], DTTF_phib4s[0]))
        abs_DTTF_phib3_phib4s[0] = abs(deltaPhi(DTTF_phib3s[0], DTTF_phib4s[0]))
        
        DTTF_DT1_DT2_pts[0] = pt_from_DPhi_DT(abs_DTTF_phib1_phib2s[0], 'DT1_DT2')
        DTTF_DT1_DT3_pts[0] = pt_from_DPhi_DT(abs_DTTF_phib1_phib3s[0], 'DT1_DT3')
        DTTF_DT1_DT4_pts[0] = pt_from_DPhi_DT(abs_DTTF_phib1_phib4s[0], 'DT1_DT4')
        DTTF_DT2_DT3_pts[0] = pt_from_DPhi_DT(abs_DTTF_phib2_phib3s[0], 'DT2_DT3')
        DTTF_DT2_DT4_pts[0] = pt_from_DPhi_DT(abs_DTTF_phib2_phib4s[0], 'DT2_DT4')
        DTTF_DT3_DT4_pts[0] = pt_from_DPhi_DT(abs_DTTF_phib3_phib4s[0], 'DT3_DT4')
        
	L1MuRatetree.Fill()

    print "rate events", L1MuRatetree.GetEntries()

    c = TCanvas("c","c",800,600)
    c.Clear()
    h_eventcount.Draw()
    c.SaveAs("h_eventcount.png")
    #make plots before write into root 
    targetroot = TFile("target.root","RECREATE")
    h_eventcount.Write()
    #h_dphi_ME11_ME21.Write()
    L1MuRatetree.Write()
    targetroot.Close()
 

    ## trigger rate plots
  displacedL1MuHybridTriggerRate()
