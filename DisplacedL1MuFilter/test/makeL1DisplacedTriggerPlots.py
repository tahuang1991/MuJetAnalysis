# run quiet mode
import sys
sys.argv.append( '-b' )
import ROOT 
ROOT.gROOT.SetBatch(1)
from Helpers import *
ROOT.gErrorIgnoreLevel=1001
from ROOT import * 
import random
#______________________________________________________________________________ 
if __name__ == "__main__":  

  ## extension for figures - add more?
  ext = ".png"

  ## Style
  gStyle.SetStatStyle(0)

  print "Making the plots"

  set_style()

  doTest = False
  if doTest:
    file = TFile("/uscms/home/dildick/nobackup/work/MuonPhaseIITDRStudies/CMSSW_6_2_0_SLHC28_patch1/src/out_ana_ctau_1000_PU140_GEM.root")
    treeHits = file.Get("DisplacedL1MuFilter_PhaseIIGE21/L1MuTree")
  
  ch = TChain("DisplacedL1MuFilter_PhaseIIGE21/L1MuTree")
  #dirname='/eos/uscms/store/user/lpcgem/DarkSUSY_MH-125_MGammaD-20000_ctau1000_14TeV_madgraph-pythia6-tauola/DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_L1MuANA/160627_185322/0000/', ext=".root")
  #dirname='/eos/uscms/store/user/lpcgem/DarkSUSY_MH-125_MGammaD-20000_ctau1000_14TeV_madgraph-pythia6-tauola/DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_L1MuANA_v2/160712_224712/0000/', ext=".root")
  #dirname='/eos/uscms/store/user/lpcgem/DarkSUSY_MH-125_MGammaD-20000_ctau1000_14TeV_madgraph-pythia6-tauola/DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_L1MuANA_v3/160713_025853/0000/', ext=".root")

  #dirname='/eos/uscms/store/user/lpcgem/DarkSUSY_MH-125_MGammaD-20000_ctau1000_14TeV_madgraph-pythia6-tauola/DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_L1MuANA_v5/160714_040828/0000/')
  #dirname='/eos/uscms/store/user/lpcgem/DarkSUSY_MH-125_MGammaD-20000_ctau1000_14TeV_madgraph-pythia6-tauola/DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_L1MuANA_v6/160719_220646/0000/')
  #dirname='/eos/uscms/store/user/lpcgem/DarkSUSY_MH-125_MGammaD-20000_ctau1000_14TeV_madgraph-pythia6-tauola/DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_L1MuANA_v7/160720_011325/0000/')
  #dirname='/eos/uscms/store/user/lpcgem/DarkSUSY_MH-125_MGammaD-20000_ctau1000_14TeV_madgraph-pythia6-tauola/DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_L1MuANA_v8/160725_235053/0000/')
  #dirname='/eos/uscms/store/user/lpcgem/DarkSUSY_MH-125_MGammaD-20000_ctau1000_14TeV_madgraph-pythia6-tauola/DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_L1MuANA_v13/160805_221951/0000/')
  #dirname='/eos/uscms/store/user/lpcgem/DarkSUSY_MH-125_MGammaD-20000_ctau1000_14TeV_madgraph-pythia6-tauola/DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_L1MuANA_v16/160806_183444/0000/')
  
  #dirname='/eos/uscms/store/user/lpcgem/DarkSUSY_MH-125_MGammaD-20000_ctau1000_14TeV_madgraph-pythia6-tauola/DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_L1MuANA_v17/160806_230658/0000/')
  #dirname='/eos/uscms/store/user/lpcgem/DarkSUSY_MH-125_MGammaD-20000_ctau1000_14TeV_madgraph-pythia6-tauola/DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_L1MuANA_v18/160806_234830/0000/')
  #dirname='/eos/uscms/store/user/lpcgem/DarkSUSY_MH-125_MGammaD-20000_ctau1000_14TeV_madgraph-pythia6-tauola/DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_L1MuANA_v23/160812_090122/0000/')
  #dirname='/eos/uscms/store/user/lpcgem/DarkSUSY_MH-125_MGammaD-20000_ctau1000_14TeV_madgraph-pythia6-tauola/DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_L1MuANA_v26/160816_221742/0000/')
  dirname = '/eos/uscms/store/user/lpcgem/DarkSUSY_MH-125_MGammaD-20000_ctau1000_14TeV_madgraph-pythia6-tauola/DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_L1MuANA_v28/160818_200220/0000/'
  
  ch = addfiles(ch, dirname=dirname)
  treeHits = ch

  label = "DisplacedL1MuTrigger_20160819_v2"
  targetDir = label + "/"
  
  verbose = False
  runTest = False
  printExtraInfo = False
  processRPC = False
  
  ## copy index file
  import shutil
  shutil.copy2('index.php', targetDir + 'index.php')

  def displacedTriggerEfficiency():
    print treeHits.GetEntries()
    
    ## some counters
    nL1MuTotal = 0

    nL1MuNotMatched = 0
    
    nL1MuMatched_GE11_GE21 = 0
    nL1MuMatched_GE11_ME11_GE21_ME21 = 0
    nL1MuMatched_ME1_ME2_ME3 = 0
    nL1MuMatched_GE0_GE21 = 0
    nL1MuMatched_GE11_GE0_GE21 = 0

    nL1MuMatched_CSCTF = 0
    nL1MuMatched_DTTF  = 0
    nL1MuMatched_RPCb  = 0
    nL1MuMatched_RPCf  = 0
    
    nL1MuMatched_DTTF_CSCTF = 0
    nL1MuMatched_RPCb_RPCf  = 0
    nL1MuMatched_DTTF_RPCb  = 0
    nL1MuMatched_DTTF_RPCf  = 0
    nL1MuMatched_CSCTF_RPCb = 0
    nL1MuMatched_CSCTF_RPCf = 0
    
    nL1MuMatched_CSCTF_DTTF_RPCb = 0
    nL1MuMatched_CSCTF_DTTF_RPCf = 0
    nL1MuMatched_DTTF_RPCb_RPCf  = 0
    nL1MuMatched_CSCTF_RPCb_RPCf = 0
    
    nL1MuMatched_DTTF_CSCTF_RPCb_RPCf = 0

    mapTH1F = ROOT.std.map("string,TH1F")()
    mapTH2F = ROOT.std.map("string,TH2F")()

    def addPlotToMapTH1F(name,nBin,minBin,maxBin):
      mapTH1F[name] = TH1F(name,"",nBin,minBin,maxBin)

    def addPlotToMapTH2F(name,nBin1,minBin1,maxBin1,nBin2,minBin2,maxBin2):
      mapTH2F[name] = TH2F(name,"",nBin1,minBin1,maxBin1,nBin2,minBin2,maxBin2)

    ## ranges
    ME1ME2ParityCases = ['ee','eo','oe','oo']
    ME1ME2ParityCasesString = ['even-even','even-odd','odd-even','odd-odd']
    ME1ME2ME3ParityCases = ['oee','ooo','eee','eoo']
    dxyRanges = ['','_dxy0to5','_dxy5to50','_dxy50to100']
    dxyRangesString = ['','|dxy| #leq 5 cm','5 < |dxy| #leq 50 cm','50 < |dxy| #leq 100 cm']
    L1MuPtCuts = ['10','15','20']
    padSizes = ['pad1','pad2','pad4','pad8']
    etaRanges = ['12to14','14to16','16to18','18to20','20to22','22to24']
    etaRangesString = ['1.2 #leq |#eta| #leq 1.4',
                       '1.4 #leq |#eta| #leq 1.6',
                       '1.6 #leq |#eta| #leq 1.8',
                       '1.8 #leq |#eta| #leq 2.0',
                       '2.0 #leq |#eta| #leq 2.2',
                       '2.2 #leq |#eta| #leq 2.4']
    etaRangesGE11 = ['16to18','18to20','20to22']
    etaRangesGE11String = ['1.6 #leq |#eta| #leq 1.8',
                           '1.8 #leq |#eta| #leq 2.0',
                           '2.0 #leq |#eta| #leq 2.2']

    ## declare plots
    nDT_stubs = TH1F("nDT_stubs","", 16,0.,16)
    nDT_stubs_vs_dxy = TH2F("nDT_stubs_vs_dxy","", 16,0.,16,100,0,100)
    nCSC_stubs = TH1F("nCSC_stubs","", 16,0.,16)
    
    ## Gen muon eta 
    GenMuEta0_MS2 = TH1F("GenMuEta0_MS2","", 100,-5,5)
    GenMuEta1_MS2 = TH1F("GenMuEta1_MS2","", 100,-5,5)
    GenMuEta2_MS2 = TH1F("GenMuEta2_MS2","", 100,-5,5)
    GenMuEta3_MS2 = TH1F("GenMuEta3_MS2","", 100,-5,5)
    GenMuEta_MS2 = TH1F("GenMuEta_MS2","", 100,-5,5)
    GenMuEta_leading_MS2_random_pt10 = TH1F("GenMuEta_leading_MS2_random_pt10","", 100,-5,5)
    GenMuEta_leading_random_pt10 = TH1F("GenMuEta_leading_random_pt10","", 100,-5,5)

    ## GEM plots
    phiGEMst1_even = TH1F("phiGEMst1_even","", 100,-1,1)
    phiGEMst2_even = TH1F("phiGEMst2_even","", 100,-1,1)
    phiGEMst1_odd = TH1F("phiGEMst1_odd","", 100,-1,1)
    phiGEMst2_odd = TH1F("phiGEMst2_odd","", 100,-1,1)

    phiGEMst1_phiGEMst2 = TH1F("phiGEMst1_phiGEMst2 ","", 100,-1,1)
    phiGEMst1_phiGEMst2_pt5to10 = TH1F("phiGEMst1_phiGEMst2_pt5to10","", 100,-1,1)
    phiGEMst1_phiGEMst2_pt10to20 = TH1F("phiGEMst1_phiGEMst2_pt10to20","", 100,-1,1)
    phiGEMst1_phiGEMst2_pt20 = TH1F("phiGEMst1_phiGEMst2_pt20","", 100,-1,1)

    abs_phiGEMst1_phiGEMst2 = TH1F("abs_phiGEMst1_phiGEMst2","", 100,-1,1)
    phiGEMst1_vs_phiGEMst2 = TH2F("phiGEMst1_vs_phiGEMst2","", 100,-3.2,3.2,100,-3.2,3.2)
    phiGEMst1_vs_phiGEMst2_dxy0to5 = TH2F("phiGEMst1_vs_phiGEMst2_dxy0to5","", 300,-3.2,3.2,300,-3.2,3.2)
    phiGEMst1_vs_phiGEMst2_dxy5to50 = TH2F("phiGEMst1_vs_phiGEMst2_dxy5to50","", 300,-3.2,3.2,300,-3.2,3.2)
    phiGEMst1_vs_phiGEMst2_dxy50to100 = TH2F("phiGEMst1_vs_phiGEMst2_dxy50to100","", 300,-3.2,3.2,300,-3.2,3.2)
    GenMuPt_vs_phiGEMst1_phiGEMst2 = TH2F("GenMuPt_vs_phiGEMst1_phiGEMst2","", 60,0.,60,100,-1,1)
    GenMuPt_vs_abs_phiGEMst1_phiGEMst2 = TH2F("GenMuPt_vs_abs_phiGEMst1_phiGEMst2","", 60,0.,60,100,0.,1.)
    GenMuPt_vs_abs_phiGEMst1_phiGEMst2_inv = TH2F("GenMuPt_vs_abs_phiGEMst1_phiGEMst2_inv","", 60,0.,60.,75,0.,150)
    GenMuPt_vs_abs_phiGEMst1_phiGEMst2_inv_dxy0to5 = TH2F("GenMuPt_vs_abs_phiGEMst1_phiGEMst2_inv_dxy0to5","", 60,0.,60.,75,0.,150)
    GenMuPt_vs_abs_phiGEMst1_phiGEMst2_inv_dxy5to50 = TH2F("GenMuPt_vs_abs_phiGEMst1_phiGEMst2_inv_dxy5to50","", 60,0.,60.,75,0.,150)
    GenMuPt_vs_abs_phiGEMst1_phiGEMst2_inv_dxy50to100 = TH2F("GenMuPt_vs_abs_phiGEMst1_phiGEMst2_inv_dxy50to100","", 60,0.,60.,75,0.,150)

    ## direction based pT trigger efficiency plots
    for pp in dxyRanges:
      addPlotToMapTH1F("GenMuPt_GE11_ME11_GE21_ME21" + pp, 60,0.,60.)
      for qq in L1MuPtCuts:
        addPlotToMapTH1F("Displaced_L1MuPt" + qq + "_GenMuPt_GE11_ME11_GE21_ME21" + pp + "_withoutLCTFit", 60,0.,60.)
        addPlotToMapTH1F("Displaced_L1MuPt" + qq + "_GenMuPt_GE11_ME11_GE21_ME21" + pp + "_withLCTFit", 60,0.,60.)

    for pp in ME1ME2ParityCases:
      for qq in etaRangesGE11:
        for rr in padSizes:
          addPlotToMapTH2F("GenMuPt_vs_abs_phiGEMst1_phiGEMst2_eta" + qq + "_" + pp + "_" + rr + "_withoutLCTFit", 60,0.,60.,100,0.,1)
          addPlotToMapTH2F("GenMuPt_vs_abs_phiGEMst1_phiGEMst2_eta" + qq + "_" + pp + "_" + rr + "_withLCTFit", 60,0.,60.,100,0.,1)

    ## CSC position resolution plots
    for qq in etaRangesGE11:
      addPlotToMapTH1F("csc_pos_sh_lct_ME1b_" + qq, 100,-0.002,0.002)
      addPlotToMapTH1F("csc_pos_sh_lct_ME21_" + qq, 100,-0.003,0.003)
      addPlotToMapTH1F("csc_pos_sh_fit_ME1b_" + qq, 200,-0.002,0.002)
      addPlotToMapTH1F("csc_pos_sh_fit_ME21_" + qq, 200,-0.003,0.003)

  
    csc_pos_sh_lct_ME1b_16to18_even = TH1F("csc_pos_sh_lct_ME1b_16to18_even","", 400,-0.01,0.01)
    csc_pos_sh_lct_ME1b_18to20_even = TH1F("csc_pos_sh_lct_ME1b_18to20_even","", 400,-0.01,0.01)
    csc_pos_sh_lct_ME1b_20to22_even = TH1F("csc_pos_sh_lct_ME1b_20to22_even","", 400,-0.01,0.01)
    csc_pos_sh_lct_ME1b_16to18_odd = TH1F("csc_pos_sh_lct_ME1b_16to18_odd","", 400,-0.01,0.01)
    csc_pos_sh_lct_ME1b_18to20_odd = TH1F("csc_pos_sh_lct_ME1b_18to20_odd","", 400,-0.01,0.01)
    csc_pos_sh_lct_ME1b_20to22_odd = TH1F("csc_pos_sh_lct_ME1b_20to22_odd","", 400,-0.01,0.01)
    
    csc_pos_sh_fit_ME1b_16to18_even = TH1F("csc_pos_sh_fit_ME1b_16to18_even","", 400,-0.01,0.01)
    csc_pos_sh_fit_ME1b_18to20_even = TH1F("csc_pos_sh_fit_ME1b_18to20_even","", 400,-0.01,0.01)
    csc_pos_sh_fit_ME1b_20to22_even = TH1F("csc_pos_sh_fit_ME1b_20to22_even","", 400,-0.01,0.01)
    csc_pos_sh_fit_ME1b_16to18_odd = TH1F("csc_pos_sh_fit_ME1b_16to18_odd","", 400,-0.01,0.01)
    csc_pos_sh_fit_ME1b_18to20_odd = TH1F("csc_pos_sh_fit_ME1b_18to20_odd","", 400,-0.01,0.01)
    csc_pos_sh_fit_ME1b_20to22_odd = TH1F("csc_pos_sh_fit_ME1b_20to22_odd","", 400,-0.01,0.01)

    
    csc_pos_sh_vs_lct_ME1b_16to18_even = TH2F("csc_pos_sh_vs_lct_ME1b_16to18_even","", 300,-3.2,3.2,300,-3.2,3.2)
    csc_pos_sh_vs_lct_ME1b_18to20_even = TH2F("csc_pos_sh_vs_lct_ME1b_18to20_even","", 300,-3.2,3.2,300,-3.2,3.2)
    csc_pos_sh_vs_lct_ME1b_20to22_even = TH2F("csc_pos_sh_vs_lct_ME1b_20to22_even","", 300,-3.2,3.2,300,-3.2,3.2)
    csc_pos_sh_vs_lct_ME1b_16to18_odd = TH2F("csc_pos_sh_vs_lct_ME1b_16to18_odd","", 300,-3.2,3.2,300,-3.2,3.2)
    csc_pos_sh_vs_lct_ME1b_18to20_odd = TH2F("csc_pos_sh_vs_lct_ME1b_18to20_odd","", 300,-3.2,3.2,300,-3.2,3.2)
    csc_pos_sh_vs_lct_ME1b_20to22_odd = TH2F("csc_pos_sh_vs_lct_ME1b_20to22_odd","", 300,-3.2,3.2,300,-3.2,3.2)
    
    csc_pos_sh_vs_fit_ME1b_16to18_even = TH2F("csc_pos_sh_vs_fit_ME1b_16to18_even","", 300,-3.2,3.2,300,-3.2,3.2)
    csc_pos_sh_vs_fit_ME1b_18to20_even = TH2F("csc_pos_sh_vs_fit_ME1b_18to20_even","", 300,-3.2,3.2,300,-3.2,3.2)
    csc_pos_sh_vs_fit_ME1b_20to22_even = TH2F("csc_pos_sh_vs_fit_ME1b_20to22_even","", 300,-3.2,3.2,300,-3.2,3.2)
    csc_pos_sh_vs_fit_ME1b_16to18_odd = TH2F("csc_pos_sh_vs_fit_ME1b_16to18_odd","", 300,-3.2,3.2,300,-3.2,3.2)
    csc_pos_sh_vs_fit_ME1b_18to20_odd = TH2F("csc_pos_sh_vs_fit_ME1b_18to20_odd","", 300,-3.2,3.2,300,-3.2,3.2)
    csc_pos_sh_vs_fit_ME1b_20to22_odd = TH2F("csc_pos_sh_vs_fit_ME1b_20to22_odd","", 300,-3.2,3.2,300,-3.2,3.2)


    csc_pos_sh_lct_ME21_16to18_even = TH1F("csc_pos_sh_lct_ME21_16to18_even","", 400,-0.01,0.01)
    csc_pos_sh_lct_ME21_18to20_even = TH1F("csc_pos_sh_lct_ME21_18to20_even","", 400,-0.01,0.01)
    csc_pos_sh_lct_ME21_20to22_even = TH1F("csc_pos_sh_lct_ME21_20to22_even","", 400,-0.01,0.01)
    csc_pos_sh_lct_ME21_16to18_odd = TH1F("csc_pos_sh_lct_ME21_16to18_odd","", 400,-0.01,0.01)
    csc_pos_sh_lct_ME21_18to20_odd = TH1F("csc_pos_sh_lct_ME21_18to20_odd","", 400,-0.01,0.01)
    csc_pos_sh_lct_ME21_20to22_odd = TH1F("csc_pos_sh_lct_ME21_20to22_odd","", 400,-0.01,0.01)
    
    csc_pos_sh_fit_ME21_16to18_even = TH1F("csc_pos_sh_fit_ME21_16to18_even","", 400,-0.01,0.01)
    csc_pos_sh_fit_ME21_18to20_even = TH1F("csc_pos_sh_fit_ME21_18to20_even","", 400,-0.01,0.01)
    csc_pos_sh_fit_ME21_20to22_even = TH1F("csc_pos_sh_fit_ME21_20to22_even","", 400,-0.01,0.01)
    csc_pos_sh_fit_ME21_16to18_odd = TH1F("csc_pos_sh_fit_ME21_16to18_odd","", 400,-0.01,0.01)
    csc_pos_sh_fit_ME21_18to20_odd = TH1F("csc_pos_sh_fit_ME21_18to20_odd","", 400,-0.01,0.01)
    csc_pos_sh_fit_ME21_20to22_odd = TH1F("csc_pos_sh_fit_ME21_20to22_odd","", 400,-0.01,0.01)



    csc_pos_sh_vs_lct_ME21_16to18_even = TH2F("csc_pos_sh_vs_lct_ME21_16to18_even","", 300,-3.2,3.2,300,-3.2,3.2)
    csc_pos_sh_vs_lct_ME21_18to20_even = TH2F("csc_pos_sh_vs_lct_ME21_18to20_even","", 300,-3.2,3.2,300,-3.2,3.2)
    csc_pos_sh_vs_lct_ME21_20to22_even = TH2F("csc_pos_sh_vs_lct_ME21_20to22_even","", 300,-3.2,3.2,300,-3.2,3.2)
    csc_pos_sh_vs_lct_ME21_16to18_odd = TH2F("csc_pos_sh_vs_lct_ME21_16to18_odd","", 300,-3.2,3.2,300,-3.2,3.2)
    csc_pos_sh_vs_lct_ME21_18to20_odd = TH2F("csc_pos_sh_vs_lct_ME21_18to20_odd","", 300,-3.2,3.2,300,-3.2,3.2)
    csc_pos_sh_vs_lct_ME21_20to22_odd = TH2F("csc_pos_sh_vs_lct_ME21_20to22_odd","", 300,-3.2,3.2,300,-3.2,3.2)
    
    csc_pos_sh_vs_fit_ME21_16to18_even = TH2F("csc_pos_sh_vs_fit_ME21_16to18_even","", 300,-3.2,3.2,300,-3.2,3.2)
    csc_pos_sh_vs_fit_ME21_18to20_even = TH2F("csc_pos_sh_vs_fit_ME21_18to20_even","", 300,-3.2,3.2,300,-3.2,3.2)
    csc_pos_sh_vs_fit_ME21_20to22_even = TH2F("csc_pos_sh_vs_fit_ME21_20to22_even","", 300,-3.2,3.2,300,-3.2,3.2)
    csc_pos_sh_vs_fit_ME21_16to18_odd = TH2F("csc_pos_sh_vs_fit_ME21_16to18_odd","", 300,-3.2,3.2,300,-3.2,3.2)
    csc_pos_sh_vs_fit_ME21_18to20_odd = TH2F("csc_pos_sh_vs_fit_ME21_18to20_odd","", 300,-3.2,3.2,300,-3.2,3.2)
    csc_pos_sh_vs_fit_ME21_20to22_odd = TH2F("csc_pos_sh_vs_fit_ME21_20to22_odd","", 300,-3.2,3.2,300,-3.2,3.2)


    ## plots for position based pT measurement
    for pp in ME1ME2ME3ParityCases:
      for qq in etaRanges:
        ## plots without position LCT fit
        addPlotToMapTH2F("deltay12_vs_deltay23_eta" + qq + "_" + pp + "_withoutLCTFit", 30,-30.,30.,30,-30.,30)
        addPlotToMapTH2F("GenMuPt_vs_inv_deltaDeltaY123_eta" + qq + "_" + pp + "_withoutLCTFit", 30,0.,60.,100,0.,10)
        addPlotToMapTH2F("GenMuPt_vs_deltaDeltaY123_eta" + qq + "_" + pp + "_withoutLCTFit", 30,0.,60.,100,0.,20)
        ## same plots with position LCT fit
        addPlotToMapTH2F("deltay12_vs_deltay23_eta" + qq + "_" + pp + "_withLCTFit", 30,-30.,30.,30,-30.,30)
        addPlotToMapTH2F("GenMuPt_vs_inv_deltaDeltaY123_eta" + qq + "_" + pp + "_withLCTFit", 30,0.,60.,100,0.,10)
        addPlotToMapTH2F("GenMuPt_vs_deltaDeltaY123_eta" + qq + "_" + pp + "_withLCTFit", 30,0.,60.,100,0.,20)


    for pp in dxyRanges:
      addPlotToMapTH1F("GenMuPt_ME1_ME2_ME3" + pp, 60,0.,60.)
      for qq in L1MuPtCuts:
        addPlotToMapTH1F("Displaced_L1MuPt" + qq + "_GenMuPt_ME1_ME2_ME3" + pp + "_withoutLCTFit", 60,0.,60.)
        addPlotToMapTH1F("Displaced_L1MuPt" + qq + "_GenMuPt_ME1_ME2_ME3" + pp + "_withLCTFit", 60,0.,60.)
    
    ## DT plots
    phiDTst1_phiDTst2 = TH1F("phiDTst1_phiDTst2","", 100,-1.,1.)
    phiDTst1_phiDTst3 = TH1F("phiDTst1_phiDTst3","", 100,-1.,1.)
    phiDTst1_phiDTst4 = TH1F("phiDTst1_phiDTst4","", 100,-1.,1.)
    phiDTst1_phiDTst4_pt5to10 = TH1F("phiDTst1_phiDTst4_pt5to10","", 100,-1.,1.)
    phiDTst1_phiDTst4_pt10to20 = TH1F("phiDTst1_phiDTst4_pt10to20","", 100,-1.,1.)
    phiDTst1_phiDTst4_pt20 = TH1F("phiDTst1_phiDTst4_pt20","", 100,-1.,1.)
    phiDTst2_phiDTst3 = TH1F("phiDTst2_phiDTst3","", 100,-1.,1.)
    phiDTst2_phiDTst4 = TH1F("phiDTst2_phiDTst4","", 100,-1.,1.)
    phiDTst3_phiDTst4 = TH1F("phiDTst3_phiDTst4","", 100,-1.,1.)

    phiDTst1_vs_phiDTst4_dxy0to5 = TH2F("phiDTst1_phiDTst4_dxy0to5","", 300,0,6.3,300,0.,6.3)
    phiDTst1_vs_phiDTst4_dxy5to50 = TH2F("phiDTst1_phiDTst4_dxy5to50","", 300,0,6.3,300,0.,6.3)
    phiDTst1_vs_phiDTst4_dxy50to100 = TH2F("phiDTst1_phiDTst4_dxy50to100","", 300,0,6.3,300,0.,6.3)


    abs_phiDTst1_phiDTst2 = TH1F("abs_phiDTst1_phiDTst2","", 100,-1.,1.)
    abs_phiDTst1_phiDTst3 = TH1F("abs_phiDTst1_phiDTst3","", 100,-1.,1.)
    abs_phiDTst1_phiDTst4 = TH1F("abs_phiDTst1_phiDTst4","", 100,-1.,1.)
    abs_phiDTst2_phiDTst3 = TH1F("abs_phiDTst2_phiDTst3","", 100,-1.,1.)
    abs_phiDTst2_phiDTst4 = TH1F("abs_phiDTst2_phiDTst4","", 100,-1.,1.)
    abs_phiDTst3_phiDTst4 = TH1F("abs_phiDTst3_phiDTst4","", 100,-1.,1.)

    GenMuPt_vs_phiDTst1_phiDTst2 = TH2F("GenMuPt_vs_phiDTst1_phiDTst2","", 60,0.,60,100,-1.,1.)
    GenMuPt_vs_phiDTst1_phiDTst3 = TH2F("GenMuPt_vs_phiDTst1_phiDTst3","", 60,0.,60,100,-1.,1.)
    GenMuPt_vs_phiDTst1_phiDTst4 = TH2F("GenMuPt_vs_phiDTst1_phiDTst4","", 60,0.,60,100,-1.,1.)
    GenMuPt_vs_phiDTst2_phiDTst3 = TH2F("GenMuPt_vs_phiDTst2_phiDTst3","", 60,0.,60,100,-1.,1.)
    GenMuPt_vs_phiDTst2_phiDTst4 = TH2F("GenMuPt_vs_phiDTst2_phiDTst4","", 60,0.,60,100,-1.,1.)
    GenMuPt_vs_phiDTst3_phiDTst4 = TH2F("GenMuPt_vs_phiDTst3_phiDTst4","", 60,0.,60,100,-1.,1.)

    GenMuPt_vs_abs_phiDTst1_phiDTst2 = TH2F("GenMuPt_vs_abs_phiDTst1_phiDTst2","", 60,0.,60,100,0.,1.)
    GenMuPt_vs_abs_phiDTst1_phiDTst3 = TH2F("GenMuPt_vs_abs_phiDTst1_phiDTst3","", 60,0.,60,100,0.,1.)
    GenMuPt_vs_abs_phiDTst1_phiDTst4 = TH2F("GenMuPt_vs_abs_phiDTst1_phiDTst4","", 60,0.,60,100,0.,1.)
    GenMuPt_vs_abs_phiDTst2_phiDTst3 = TH2F("GenMuPt_vs_abs_phiDTst2_phiDTst3","", 60,0.,60,100,0.,1.)
    GenMuPt_vs_abs_phiDTst2_phiDTst4 = TH2F("GenMuPt_vs_abs_phiDTst2_phiDTst4","", 60,0.,60,100,0.,1.)
    GenMuPt_vs_abs_phiDTst3_phiDTst4 = TH2F("GenMuPt_vs_abs_phiDTst3_phiDTst4","", 60,0.,60,100,0.,1.)

    GenMuPt_vs_abs_phiDTst1_phiDTst2_inv = TH2F("GenMuPt_vs_abs_phiDTst1_phiDTst2_inv","", 60,0.,60.,75,0.,150)
    GenMuPt_vs_abs_phiDTst1_phiDTst3_inv = TH2F("GenMuPt_vs_abs_phiDTst1_phiDTst3_inv","", 60,0.,60.,75,0.,150)
    GenMuPt_vs_abs_phiDTst1_phiDTst4_inv = TH2F("GenMuPt_vs_abs_phiDTst1_phiDTst4_inv","", 60,0.,60.,75,0.,150)
    GenMuPt_vs_abs_phiDTst2_phiDTst3_inv = TH2F("GenMuPt_vs_abs_phiDTst2_phiDTst3_inv","", 60,0.,60.,75,0.,150)
    GenMuPt_vs_abs_phiDTst2_phiDTst4_inv = TH2F("GenMuPt_vs_abs_phiDTst2_phiDTst4_inv","", 60,0.,60.,75,0.,150)
    GenMuPt_vs_abs_phiDTst3_phiDTst4_inv = TH2F("GenMuPt_vs_abs_phiDTst3_phiDTst4_inv","", 60,0.,60.,75,0.,150)

    GenMuPt_vs_abs_phiDTst1_phiDTst4_inv_dxy0to5 = TH2F("GenMuPt_vs_abs_phiDTst1_phiDTst4_inv_dxy0to5","", 60,0.,60.,75,0.,150)
    GenMuPt_vs_abs_phiDTst1_phiDTst4_inv_dxy5to50 = TH2F("GenMuPt_vs_abs_phiDTst1_phiDTst4_inv_dxy5to50","", 60,0.,60.,75,0.,150)
    GenMuPt_vs_abs_phiDTst1_phiDTst4_inv_dxy50to100 = TH2F("GenMuPt_vs_abs_phiDTst1_phiDTst4_inv_dxy50to100","", 60,0.,60.,75,0.,150)

    GenMuPt = TH1F("GenMuPt","", 60,0.,60)
    GenMuPt_DT1_DT2 = TH1F("GenMuPt_DT1_DT2","", 60,0.,60)
    GenMuPt_DT1_DT3 = TH1F("GenMuPt_DT1_DT3","", 60,0.,60)
    GenMuPt_DT1_DT4 = TH1F("GenMuPt_DT1_DT4","", 60,0.,60)
    GenMuPt_DT2_DT3 = TH1F("GenMuPt_DT2_DT3","", 60,0.,60)
    GenMuPt_DT2_DT4 = TH1F("GenMuPt_DT2_DT4","", 60,0.,60)
    GenMuPt_DT3_DT4 = TH1F("GenMuPt_DT3_DT4","", 60,0.,60)

    GenMuPt_dxy0to5 = TH1F("GenMuPt_dxy0to5","", 60,0.,60)
    GenMuPt_DT1_DT2_dxy0to5 = TH1F("GenMuPt_DT1_DT2_dxy0to5","", 60,0.,60)
    GenMuPt_DT1_DT3_dxy0to5 = TH1F("GenMuPt_DT1_DT3_dxy0to5","", 60,0.,60)
    GenMuPt_DT1_DT4_dxy0to5 = TH1F("GenMuPt_DT1_DT4_dxy0to5","", 60,0.,60)
    GenMuPt_DT2_DT3_dxy0to5 = TH1F("GenMuPt_DT2_DT3_dxy0to5","", 60,0.,60)
    GenMuPt_DT2_DT4_dxy0to5 = TH1F("GenMuPt_DT2_DT4_dxy0to5","", 60,0.,60)
    GenMuPt_DT3_DT4_dxy0to5 = TH1F("GenMuPt_DT3_DT4_dxy0to5","", 60,0.,60)

    GenMuPt_dxy5to50 = TH1F("GenMuPt_dxy5to50","", 60,0.,60)
    GenMuPt_DT1_DT2_dxy5to50 = TH1F("GenMuPt_DT1_DT2_dxy5to50","", 60,0.,60)
    GenMuPt_DT1_DT3_dxy5to50 = TH1F("GenMuPt_DT1_DT3_dxy5to50","", 60,0.,60)
    GenMuPt_DT1_DT4_dxy5to50 = TH1F("GenMuPt_DT1_DT4_dxy5to50","", 60,0.,60)
    GenMuPt_DT2_DT3_dxy5to50 = TH1F("GenMuPt_DT2_DT3_dxy5to50","", 60,0.,60)
    GenMuPt_DT2_DT4_dxy5to50 = TH1F("GenMuPt_DT2_DT4_dxy5to50","", 60,0.,60)
    GenMuPt_DT3_DT4_dxy5to50 = TH1F("GenMuPt_DT3_DT4_dxy5to50","", 60,0.,60)

    GenMuPt_dxy50to100 = TH1F("GenMuPt_dxy50to100","", 60,0.,60)
    GenMuPt_DT1_DT2_dxy50to100 = TH1F("GenMuPt_DT1_DT2_dxy50to100","", 60,0.,60)
    GenMuPt_DT1_DT3_dxy50to100 = TH1F("GenMuPt_DT1_DT3_dxy50to100","", 60,0.,60)
    GenMuPt_DT1_DT4_dxy50to100 = TH1F("GenMuPt_DT1_DT4_dxy50to100","", 60,0.,60)
    GenMuPt_DT2_DT3_dxy50to100 = TH1F("GenMuPt_DT2_DT3_dxy50to100","", 60,0.,60)
    GenMuPt_DT2_DT4_dxy50to100 = TH1F("GenMuPt_DT2_DT4_dxy50to100","", 60,0.,60)
    GenMuPt_DT3_DT4_dxy50to100 = TH1F("GenMuPt_DT3_DT4_dxy50to100","", 60,0.,60)
    

    GenMuPt_eta16to22 = TH1F("GenMuPt_eta16to22","", 60,0.,60)
    GenMuPt_dxy0to5_eta16to22 = TH1F("GenMuPt_dxy0to5_eta16to22","", 60,0.,60)
    GenMuPt_dxy5to50_eta16to22 = TH1F("GenMuPt_dxy5to50_eta16to22","", 60,0.,60)
    GenMuPt_dxy50to100_eta16to22 = TH1F("GenMuPt_dxy50to100_eta16to22","", 60,0.,60)


    GenMuPt_barrel = TH1F("GenMuPt_barrel","", 60,0.,60)
    GenMuPt_DT1_DT2_barrel = TH1F("GenMuPt_DT1_DT2_barrel","", 60,0.,60)
    GenMuPt_DT1_DT3_barrel = TH1F("GenMuPt_DT1_DT3_barrel","", 60,0.,60)
    GenMuPt_DT1_DT4_barrel = TH1F("GenMuPt_DT1_DT4_barrel","", 60,0.,60)
    GenMuPt_DT2_DT3_barrel = TH1F("GenMuPt_DT2_DT3_barrel","", 60,0.,60)
    GenMuPt_DT2_DT4_barrel = TH1F("GenMuPt_DT2_DT4_barrel","", 60,0.,60)
    GenMuPt_DT3_DT4_barrel = TH1F("GenMuPt_DT3_DT4_barrel","", 60,0.,60)

    GenMuPt_dxy0to5_barrel = TH1F("GenMuPt_dxy0to5_barrel","", 60,0.,60)
    GenMuPt_DT1_DT2_dxy0to5_barrel = TH1F("GenMuPt_DT1_DT2_dxy0to5_barrel","", 60,0.,60)
    GenMuPt_DT1_DT3_dxy0to5_barrel = TH1F("GenMuPt_DT1_DT3_dxy0to5_barrel","", 60,0.,60)
    GenMuPt_DT1_DT4_dxy0to5_barrel = TH1F("GenMuPt_DT1_DT4_dxy0to5_barrel","", 60,0.,60)
    GenMuPt_DT2_DT3_dxy0to5_barrel = TH1F("GenMuPt_DT2_DT3_dxy0to5_barrel","", 60,0.,60)
    GenMuPt_DT2_DT4_dxy0to5_barrel = TH1F("GenMuPt_DT2_DT4_dxy0to5_barrel","", 60,0.,60)
    GenMuPt_DT3_DT4_dxy0to5_barrel = TH1F("GenMuPt_DT3_DT4_dxy0to5_barrel","", 60,0.,60)

    GenMuPt_dxy5to50_barrel = TH1F("GenMuPt_dxy5to50_barrel","", 60,0.,60)
    GenMuPt_DT1_DT2_dxy5to50_barrel = TH1F("GenMuPt_DT1_DT2_dxy5to50_barrel","", 60,0.,60)
    GenMuPt_DT1_DT3_dxy5to50_barrel = TH1F("GenMuPt_DT1_DT3_dxy5to50_barrel","", 60,0.,60)
    GenMuPt_DT1_DT4_dxy5to50_barrel = TH1F("GenMuPt_DT1_DT4_dxy5to50_barrel","", 60,0.,60)
    GenMuPt_DT2_DT3_dxy5to50_barrel = TH1F("GenMuPt_DT2_DT3_dxy5to50_barrel","", 60,0.,60)
    GenMuPt_DT2_DT4_dxy5to50_barrel = TH1F("GenMuPt_DT2_DT4_dxy5to50_barrel","", 60,0.,60)
    GenMuPt_DT3_DT4_dxy5to50_barrel = TH1F("GenMuPt_DT3_DT4_dxy5to50_barrel","", 60,0.,60)

    GenMuPt_dxy50to100_barrel = TH1F("GenMuPt_dxy50to100_barrel","", 60,0.,60)
    GenMuPt_DT1_DT2_dxy50to100_barrel = TH1F("GenMuPt_DT1_DT2_dxy50to100_barrel","", 60,0.,60)
    GenMuPt_DT1_DT3_dxy50to100_barrel = TH1F("GenMuPt_DT1_DT3_dxy50to100_barrel","", 60,0.,60)
    GenMuPt_DT1_DT4_dxy50to100_barrel = TH1F("GenMuPt_DT1_DT4_dxy50to100_barrel","", 60,0.,60)
    GenMuPt_DT2_DT3_dxy50to100_barrel = TH1F("GenMuPt_DT2_DT3_dxy50to100_barrel","", 60,0.,60)
    GenMuPt_DT2_DT4_dxy50to100_barrel = TH1F("GenMuPt_DT2_DT4_dxy50to100_barrel","", 60,0.,60)
    GenMuPt_DT3_DT4_dxy50to100_barrel = TH1F("GenMuPt_DT3_DT4_dxy50to100_barrel","", 60,0.,60)


    GenMuPt_overlap = TH1F("GenMuPt_overlap","", 60,0.,60)
    GenMuPt_DT1_DT2_overlap = TH1F("GenMuPt_DT1_DT2_overlap","", 60,0.,60)
    GenMuPt_DT1_DT3_overlap = TH1F("GenMuPt_DT1_DT3_overlap","", 60,0.,60)
    GenMuPt_DT1_DT4_overlap = TH1F("GenMuPt_DT1_DT4_overlap","", 60,0.,60)
    GenMuPt_DT2_DT3_overlap = TH1F("GenMuPt_DT2_DT3_overlap","", 60,0.,60)
    GenMuPt_DT2_DT4_overlap = TH1F("GenMuPt_DT2_DT4_overlap","", 60,0.,60)
    GenMuPt_DT3_DT4_overlap = TH1F("GenMuPt_DT3_DT4_overlap","", 60,0.,60)

    GenMuPt_dxy0to5_overlap = TH1F("GenMuPt_dxy0to5_overlap","", 60,0.,60)
    GenMuPt_DT1_DT2_dxy0to5_overlap = TH1F("GenMuPt_DT1_DT2_dxy0to5_overlap","", 60,0.,60)
    GenMuPt_DT1_DT3_dxy0to5_overlap = TH1F("GenMuPt_DT1_DT3_dxy0to5_overlap","", 60,0.,60)
    GenMuPt_DT1_DT4_dxy0to5_overlap = TH1F("GenMuPt_DT1_DT4_dxy0to5_overlap","", 60,0.,60)
    GenMuPt_DT2_DT3_dxy0to5_overlap = TH1F("GenMuPt_DT2_DT3_dxy0to5_overlap","", 60,0.,60)
    GenMuPt_DT2_DT4_dxy0to5_overlap = TH1F("GenMuPt_DT2_DT4_dxy0to5_overlap","", 60,0.,60)
    GenMuPt_DT3_DT4_dxy0to5_overlap = TH1F("GenMuPt_DT3_DT4_dxy0to5_overlap","", 60,0.,60)

    GenMuPt_dxy5to50_overlap = TH1F("GenMuPt_dxy5to50_overlap","", 60,0.,60)
    GenMuPt_DT1_DT2_dxy5to50_overlap = TH1F("GenMuPt_DT1_DT2_dxy5to50_overlap","", 60,0.,60)
    GenMuPt_DT1_DT3_dxy5to50_overlap = TH1F("GenMuPt_DT1_DT3_dxy5to50_overlap","", 60,0.,60)
    GenMuPt_DT1_DT4_dxy5to50_overlap = TH1F("GenMuPt_DT1_DT4_dxy5to50_overlap","", 60,0.,60)
    GenMuPt_DT2_DT3_dxy5to50_overlap = TH1F("GenMuPt_DT2_DT3_dxy5to50_overlap","", 60,0.,60)
    GenMuPt_DT2_DT4_dxy5to50_overlap = TH1F("GenMuPt_DT2_DT4_dxy5to50_overlap","", 60,0.,60)
    GenMuPt_DT3_DT4_dxy5to50_overlap = TH1F("GenMuPt_DT3_DT4_dxy5to50_overlap","", 60,0.,60)

    GenMuPt_dxy50to100_overlap = TH1F("GenMuPt_dxy50to100_overlap","", 60,0.,60)
    GenMuPt_DT1_DT2_dxy50to100_overlap = TH1F("GenMuPt_DT1_DT2_dxy50to100_overlap","", 60,0.,60)
    GenMuPt_DT1_DT3_dxy50to100_overlap = TH1F("GenMuPt_DT1_DT3_dxy50to100_overlap","", 60,0.,60)
    GenMuPt_DT1_DT4_dxy50to100_overlap = TH1F("GenMuPt_DT1_DT4_dxy50to100_overlap","", 60,0.,60)
    GenMuPt_DT2_DT3_dxy50to100_overlap = TH1F("GenMuPt_DT2_DT3_dxy50to100_overlap","", 60,0.,60)
    GenMuPt_DT2_DT4_dxy50to100_overlap = TH1F("GenMuPt_DT2_DT4_dxy50to100_overlap","", 60,0.,60)
    GenMuPt_DT3_DT4_dxy50to100_overlap = TH1F("GenMuPt_DT3_DT4_dxy50to100_overlap","", 60,0.,60)



    GenMuPt_endcap = TH1F("GenMuPt_endcap","", 60,0.,60)
    GenMuPt_DT1_DT2_endcap = TH1F("GenMuPt_DT1_DT2_endcap","", 60,0.,60)
    GenMuPt_DT1_DT3_endcap = TH1F("GenMuPt_DT1_DT3_endcap","", 60,0.,60)
    GenMuPt_DT1_DT4_endcap = TH1F("GenMuPt_DT1_DT4_endcap","", 60,0.,60)
    GenMuPt_DT2_DT3_endcap = TH1F("GenMuPt_DT2_DT3_endcap","", 60,0.,60)
    GenMuPt_DT2_DT4_endcap = TH1F("GenMuPt_DT2_DT4_endcap","", 60,0.,60)
    GenMuPt_DT3_DT4_endcap = TH1F("GenMuPt_DT3_DT4_endcap","", 60,0.,60)

    GenMuPt_dxy0to5_endcap = TH1F("GenMuPt_dxy0to5_endcap","", 60,0.,60)
    GenMuPt_DT1_DT2_dxy0to5_endcap = TH1F("GenMuPt_DT1_DT2_dxy0to5_endcap","", 60,0.,60)
    GenMuPt_DT1_DT3_dxy0to5_endcap = TH1F("GenMuPt_DT1_DT3_dxy0to5_endcap","", 60,0.,60)
    GenMuPt_DT1_DT4_dxy0to5_endcap = TH1F("GenMuPt_DT1_DT4_dxy0to5_endcap","", 60,0.,60)
    GenMuPt_DT2_DT3_dxy0to5_endcap = TH1F("GenMuPt_DT2_DT3_dxy0to5_endcap","", 60,0.,60)
    GenMuPt_DT2_DT4_dxy0to5_endcap = TH1F("GenMuPt_DT2_DT4_dxy0to5_endcap","", 60,0.,60)
    GenMuPt_DT3_DT4_dxy0to5_endcap = TH1F("GenMuPt_DT3_DT4_dxy0to5_endcap","", 60,0.,60)

    GenMuPt_dxy5to50_endcap = TH1F("GenMuPt_dxy5to50_endcap","", 60,0.,60)
    GenMuPt_DT1_DT2_dxy5to50_endcap = TH1F("GenMuPt_DT1_DT2_dxy5to50_endcap","", 60,0.,60)
    GenMuPt_DT1_DT3_dxy5to50_endcap = TH1F("GenMuPt_DT1_DT3_dxy5to50_endcap","", 60,0.,60)
    GenMuPt_DT1_DT4_dxy5to50_endcap = TH1F("GenMuPt_DT1_DT4_dxy5to50_endcap","", 60,0.,60)
    GenMuPt_DT2_DT3_dxy5to50_endcap = TH1F("GenMuPt_DT2_DT3_dxy5to50_endcap","", 60,0.,60)
    GenMuPt_DT2_DT4_dxy5to50_endcap = TH1F("GenMuPt_DT2_DT4_dxy5to50_endcap","", 60,0.,60)
    GenMuPt_DT3_DT4_dxy5to50_endcap = TH1F("GenMuPt_DT3_DT4_dxy5to50_endcap","", 60,0.,60)

    GenMuPt_dxy50to100_endcap = TH1F("GenMuPt_dxy50to100_endcap","", 60,0.,60)
    GenMuPt_DT1_DT2_dxy50to100_endcap = TH1F("GenMuPt_DT1_DT2_dxy50to100_endcap","", 60,0.,60)
    GenMuPt_DT1_DT3_dxy50to100_endcap = TH1F("GenMuPt_DT1_DT3_dxy50to100_endcap","", 60,0.,60)
    GenMuPt_DT1_DT4_dxy50to100_endcap = TH1F("GenMuPt_DT1_DT4_dxy50to100_endcap","", 60,0.,60)
    GenMuPt_DT2_DT3_dxy50to100_endcap = TH1F("GenMuPt_DT2_DT3_dxy50to100_endcap","", 60,0.,60)
    GenMuPt_DT2_DT4_dxy50to100_endcap = TH1F("GenMuPt_DT2_DT4_dxy50to100_endcap","", 60,0.,60)
    GenMuPt_DT3_DT4_dxy50to100_endcap = TH1F("GenMuPt_DT3_DT4_dxy50to100_endcap","", 60,0.,60)


    Prompt_L1MuPt10_GenMuPt = TH1F("Prompt_L1MuPt10_GenMuPt","", 60,0.,60)
    Prompt_L1MuPt15_GenMuPt = TH1F("Prompt_L1MuPt15_GenMuPt","", 60,0.,60)
    Prompt_L1MuPt20_GenMuPt = TH1F("Prompt_L1MuPt20_GenMuPt","", 60,0.,60)

    Prompt_L1MuPt10_GenMuPt_eta16to22 = TH1F("Prompt_L1MuPt10_GenMuPt_eta16to22","", 60,0.,60)
    Prompt_L1MuPt15_GenMuPt_eta16to22 = TH1F("Prompt_L1MuPt15_GenMuPt_eta16to22","", 60,0.,60)
    Prompt_L1MuPt20_GenMuPt_eta16to22 = TH1F("Prompt_L1MuPt20_GenMuPt_eta16to22","", 60,0.,60)


    Prompt_L1MuPt10_GenMuPt_dxy0to5 = TH1F("Prompt_L1MuPt10_GenMuPt_dxy0to5","", 60,0.,60)
    Prompt_L1MuPt15_GenMuPt_dxy0to5 = TH1F("Prompt_L1MuPt15_GenMuPt_dxy0to5","", 60,0.,60)
    Prompt_L1MuPt20_GenMuPt_dxy0to5 = TH1F("Prompt_L1MuPt20_GenMuPt_dxy0to5","", 60,0.,60)

    Prompt_L1MuPt10_GenMuPt_dxy5to50 = TH1F("Prompt_L1MuPt10_GenMuPt_dxy5to50","", 60,0.,60)
    Prompt_L1MuPt15_GenMuPt_dxy5to50 = TH1F("Prompt_L1MuPt15_GenMuPt_dxy5to50","", 60,0.,60)
    Prompt_L1MuPt20_GenMuPt_dxy5to50 = TH1F("Prompt_L1MuPt20_GenMuPt_dxy5to50","", 60,0.,60)

    Prompt_L1MuPt10_GenMuPt_dxy50to100 = TH1F("Prompt_L1MuPt10_GenMuPt_dxy50to100","", 60,0.,60)
    Prompt_L1MuPt15_GenMuPt_dxy50to100 = TH1F("Prompt_L1MuPt15_GenMuPt_dxy50to100","", 60,0.,60)
    Prompt_L1MuPt20_GenMuPt_dxy50to100 = TH1F("Prompt_L1MuPt20_GenMuPt_dxy50to100","", 60,0.,60)


    Prompt_L1MuPt10_GenMuPt_dxy0to5_eta16to22 = TH1F("Prompt_L1MuPt10_GenMuPt_dxy0to5_eta16to22","", 60,0.,60)
    Prompt_L1MuPt15_GenMuPt_dxy0to5_eta16to22 = TH1F("Prompt_L1MuPt15_GenMuPt_dxy0to5_eta16to22","", 60,0.,60)
    Prompt_L1MuPt20_GenMuPt_dxy0to5_eta16to22 = TH1F("Prompt_L1MuPt20_GenMuPt_dxy0to5_eta16to22","", 60,0.,60)

    Prompt_L1MuPt10_GenMuPt_dxy5to50_eta16to22 = TH1F("Prompt_L1MuPt10_GenMuPt_dxy5to50_eta16to22","", 60,0.,60)
    Prompt_L1MuPt15_GenMuPt_dxy5to50_eta16to22 = TH1F("Prompt_L1MuPt15_GenMuPt_dxy5to50_eta16to22","", 60,0.,60)
    Prompt_L1MuPt20_GenMuPt_dxy5to50_eta16to22 = TH1F("Prompt_L1MuPt20_GenMuPt_dxy5to50_eta16to22","", 60,0.,60)

    Prompt_L1MuPt10_GenMuPt_dxy50to100_eta16to22 = TH1F("Prompt_L1MuPt10_GenMuPt_dxy50to100_eta16to22","", 60,0.,60)
    Prompt_L1MuPt15_GenMuPt_dxy50to100_eta16to22 = TH1F("Prompt_L1MuPt15_GenMuPt_dxy50to100_eta16to22","", 60,0.,60)
    Prompt_L1MuPt20_GenMuPt_dxy50to100_eta16to22 = TH1F("Prompt_L1MuPt20_GenMuPt_dxy50to100_eta16to22","", 60,0.,60)


    Displaced_L1MuPt10_GenMuPt = TH1F("Displaced_L1MuPt10_GenMuPt","", 60,0.,60)
    Displaced_L1MuPt15_GenMuPt = TH1F("Displaced_L1MuPt15_GenMuPt","", 60,0.,60)
    Displaced_L1MuPt20_GenMuPt = TH1F("Displaced_L1MuPt20_GenMuPt","", 60,0.,60)

    Displaced_L1MuPt10_GenMuPt_dxy0to5 = TH1F("Displaced_L1MuPt10_GenMuPt_dxy0to5","", 60,0.,60)
    Displaced_L1MuPt15_GenMuPt_dxy0to5 = TH1F("Displaced_L1MuPt15_GenMuPt_dxy0to5","", 60,0.,60)
    Displaced_L1MuPt20_GenMuPt_dxy0to5 = TH1F("Displaced_L1MuPt20_GenMuPt_dxy0to5","", 60,0.,60)

    Displaced_L1MuPt10_GenMuPt_dxy5to50 = TH1F("Displaced_L1MuPt10_GenMuPt_dxy5to50","", 60,0.,60)
    Displaced_L1MuPt15_GenMuPt_dxy5to50 = TH1F("Displaced_L1MuPt15_GenMuPt_dxy5to50","", 60,0.,60)
    Displaced_L1MuPt20_GenMuPt_dxy5to50 = TH1F("Displaced_L1MuPt20_GenMuPt_dxy5to50","", 60,0.,60)

    Displaced_L1MuPt10_GenMuPt_dxy50to100 = TH1F("Displaced_L1MuPt10_GenMuPt_dxy50to100","", 60,0.,60)
    Displaced_L1MuPt15_GenMuPt_dxy50to100 = TH1F("Displaced_L1MuPt15_GenMuPt_dxy50to100","", 60,0.,60)
    Displaced_L1MuPt20_GenMuPt_dxy50to100 = TH1F("Displaced_L1MuPt20_GenMuPt_dxy50to100","", 60,0.,60)

    Displaced_L1MuPt10_GenMuPt_barrel = TH1F("Displaced_L1MuPt10_GenMuPt_barrel","", 60,0.,60)
    Displaced_L1MuPt15_GenMuPt_barrel = TH1F("Displaced_L1MuPt15_GenMuPt_barrel","", 60,0.,60)
    Displaced_L1MuPt20_GenMuPt_barrel = TH1F("Displaced_L1MuPt20_GenMuPt_barrel","", 60,0.,60)

    Displaced_L1MuPt10_GenMuPt_dxy0to5_barrel = TH1F("Displaced_L1MuPt10_GenMuPt_dxy0to5_barrel","", 60,0.,60)
    Displaced_L1MuPt15_GenMuPt_dxy0to5_barrel = TH1F("Displaced_L1MuPt15_GenMuPt_dxy0to5_barrel","", 60,0.,60)
    Displaced_L1MuPt20_GenMuPt_dxy0to5_barrel = TH1F("Displaced_L1MuPt20_GenMuPt_dxy0to5_barrel","", 60,0.,60)

    Displaced_L1MuPt10_GenMuPt_dxy5to50_barrel = TH1F("Displaced_L1MuPt10_GenMuPt_dxy5to50_barrel","", 60,0.,60)
    Displaced_L1MuPt15_GenMuPt_dxy5to50_barrel = TH1F("Displaced_L1MuPt15_GenMuPt_dxy5to50_barrel","", 60,0.,60)
    Displaced_L1MuPt20_GenMuPt_dxy5to50_barrel = TH1F("Displaced_L1MuPt20_GenMuPt_dxy5to50_barrel","", 60,0.,60)

    Displaced_L1MuPt10_GenMuPt_dxy50to100_barrel = TH1F("Displaced_L1MuPt10_GenMuPt_dxy50to100_barrel","", 60,0.,60)
    Displaced_L1MuPt15_GenMuPt_dxy50to100_barrel = TH1F("Displaced_L1MuPt15_GenMuPt_dxy50to100_barrel","", 60,0.,60)
    Displaced_L1MuPt20_GenMuPt_dxy50to100_barrel = TH1F("Displaced_L1MuPt20_GenMuPt_dxy50to100_barrel","", 60,0.,60)

    Displaced_L1MuPt10_GenMuPt_overlap = TH1F("Displaced_L1MuPt10_GenMuPt_overlap","", 60,0.,60)
    Displaced_L1MuPt15_GenMuPt_overlap = TH1F("Displaced_L1MuPt15_GenMuPt_overlap","", 60,0.,60)
    Displaced_L1MuPt20_GenMuPt_overlap = TH1F("Displaced_L1MuPt20_GenMuPt_overlap","", 60,0.,60)

    Displaced_L1MuPt10_GenMuPt_dxy0to5_overlap = TH1F("Displaced_L1MuPt10_GenMuPt_dxy0to5_overlap","", 60,0.,60)
    Displaced_L1MuPt15_GenMuPt_dxy0to5_overlap = TH1F("Displaced_L1MuPt15_GenMuPt_dxy0to5_overlap","", 60,0.,60)
    Displaced_L1MuPt20_GenMuPt_dxy0to5_overlap = TH1F("Displaced_L1MuPt20_GenMuPt_dxy0to5_overlap","", 60,0.,60)

    Displaced_L1MuPt10_GenMuPt_dxy5to50_overlap = TH1F("Displaced_L1MuPt10_GenMuPt_dxy5to50_overlap","", 60,0.,60)
    Displaced_L1MuPt15_GenMuPt_dxy5to50_overlap = TH1F("Displaced_L1MuPt15_GenMuPt_dxy5to50_overlap","", 60,0.,60)
    Displaced_L1MuPt20_GenMuPt_dxy5to50_overlap = TH1F("Displaced_L1MuPt20_GenMuPt_dxy5to50_overlap","", 60,0.,60)

    Displaced_L1MuPt10_GenMuPt_dxy50to100_overlap = TH1F("Displaced_L1MuPt10_GenMuPt_dxy50to100_overlap","", 60,0.,60)
    Displaced_L1MuPt15_GenMuPt_dxy50to100_overlap = TH1F("Displaced_L1MuPt15_GenMuPt_dxy50to100_overlap","", 60,0.,60)
    Displaced_L1MuPt20_GenMuPt_dxy50to100_overlap = TH1F("Displaced_L1MuPt20_GenMuPt_dxy50to100_overlap","", 60,0.,60)

    Displaced_L1MuPt10_GenMuPt_endcap = TH1F("Displaced_L1MuPt10_GenMuPt_endcap","", 60,0.,60)
    Displaced_L1MuPt15_GenMuPt_endcap = TH1F("Displaced_L1MuPt15_GenMuPt_endcap","", 60,0.,60)
    Displaced_L1MuPt20_GenMuPt_endcap = TH1F("Displaced_L1MuPt20_GenMuPt_endcap","", 60,0.,60)

    Displaced_L1MuPt10_GenMuPt_dxy0to5_endcap = TH1F("Displaced_L1MuPt10_GenMuPt_dxy0to5_endcap","", 60,0.,60)
    Displaced_L1MuPt15_GenMuPt_dxy0to5_endcap = TH1F("Displaced_L1MuPt15_GenMuPt_dxy0to5_endcap","", 60,0.,60)
    Displaced_L1MuPt20_GenMuPt_dxy0to5_endcap = TH1F("Displaced_L1MuPt20_GenMuPt_dxy0to5_endcap","", 60,0.,60)

    Displaced_L1MuPt10_GenMuPt_dxy5to50_endcap = TH1F("Displaced_L1MuPt10_GenMuPt_dxy5to50_endcap","", 60,0.,60)
    Displaced_L1MuPt15_GenMuPt_dxy5to50_endcap = TH1F("Displaced_L1MuPt15_GenMuPt_dxy5to50_endcap","", 60,0.,60)
    Displaced_L1MuPt20_GenMuPt_dxy5to50_endcap = TH1F("Displaced_L1MuPt20_GenMuPt_dxy5to50_endcap","", 60,0.,60)

    Displaced_L1MuPt10_GenMuPt_dxy50to100_endcap = TH1F("Displaced_L1MuPt10_GenMuPt_dxy50to100_endcap","", 60,0.,60)
    Displaced_L1MuPt15_GenMuPt_dxy50to100_endcap = TH1F("Displaced_L1MuPt15_GenMuPt_dxy50to100_endcap","", 60,0.,60)
    Displaced_L1MuPt20_GenMuPt_dxy50to100_endcap = TH1F("Displaced_L1MuPt20_GenMuPt_dxy50to100_endcap","", 60,0.,60)


    Prompt_L1MuPt10_GenMuPt_barrel = TH1F("Prompt_L1MuPt10_GenMuPt_barrel","", 60,0.,60)
    Prompt_L1MuPt15_GenMuPt_barrel = TH1F("Prompt_L1MuPt15_GenMuPt_barrel","", 60,0.,60)
    Prompt_L1MuPt20_GenMuPt_barrel = TH1F("Prompt_L1MuPt20_GenMuPt_barrel","", 60,0.,60)

    Prompt_L1MuPt10_GenMuPt_dxy0to5_barrel = TH1F("Prompt_L1MuPt10_GenMuPt_dxy0to5_barrel","", 60,0.,60)
    Prompt_L1MuPt15_GenMuPt_dxy0to5_barrel = TH1F("Prompt_L1MuPt15_GenMuPt_dxy0to5_barrel","", 60,0.,60)
    Prompt_L1MuPt20_GenMuPt_dxy0to5_barrel = TH1F("Prompt_L1MuPt20_GenMuPt_dxy0to5_barrel","", 60,0.,60)

    Prompt_L1MuPt10_GenMuPt_dxy5to50_barrel = TH1F("Prompt_L1MuPt10_GenMuPt_dxy5to50_barrel","", 60,0.,60)
    Prompt_L1MuPt15_GenMuPt_dxy5to50_barrel = TH1F("Prompt_L1MuPt15_GenMuPt_dxy5to50_barrel","", 60,0.,60)
    Prompt_L1MuPt20_GenMuPt_dxy5to50_barrel = TH1F("Prompt_L1MuPt20_GenMuPt_dxy5to50_barrel","", 60,0.,60)

    Prompt_L1MuPt10_GenMuPt_dxy50to100_barrel = TH1F("Prompt_L1MuPt10_GenMuPt_dxy50to100_barrel","", 60,0.,60)
    Prompt_L1MuPt15_GenMuPt_dxy50to100_barrel = TH1F("Prompt_L1MuPt15_GenMuPt_dxy50to100_barrel","", 60,0.,60)
    Prompt_L1MuPt20_GenMuPt_dxy50to100_barrel = TH1F("Prompt_L1MuPt20_GenMuPt_dxy50to100_barrel","", 60,0.,60)

    Prompt_L1MuPt10_GenMuPt_overlap = TH1F("Prompt_L1MuPt10_GenMuPt_overlap","", 60,0.,60)
    Prompt_L1MuPt15_GenMuPt_overlap = TH1F("Prompt_L1MuPt15_GenMuPt_overlap","", 60,0.,60)
    Prompt_L1MuPt20_GenMuPt_overlap = TH1F("Prompt_L1MuPt20_GenMuPt_overlap","", 60,0.,60)

    Prompt_L1MuPt10_GenMuPt_dxy0to5_overlap = TH1F("Prompt_L1MuPt10_GenMuPt_dxy0to5_overlap","", 60,0.,60)
    Prompt_L1MuPt15_GenMuPt_dxy0to5_overlap = TH1F("Prompt_L1MuPt15_GenMuPt_dxy0to5_overlap","", 60,0.,60)
    Prompt_L1MuPt20_GenMuPt_dxy0to5_overlap = TH1F("Prompt_L1MuPt20_GenMuPt_dxy0to5_overlap","", 60,0.,60)

    Prompt_L1MuPt10_GenMuPt_dxy5to50_overlap = TH1F("Prompt_L1MuPt10_GenMuPt_dxy5to50_overlap","", 60,0.,60)
    Prompt_L1MuPt15_GenMuPt_dxy5to50_overlap = TH1F("Prompt_L1MuPt15_GenMuPt_dxy5to50_overlap","", 60,0.,60)
    Prompt_L1MuPt20_GenMuPt_dxy5to50_overlap = TH1F("Prompt_L1MuPt20_GenMuPt_dxy5to50_overlap","", 60,0.,60)

    Prompt_L1MuPt10_GenMuPt_dxy50to100_overlap = TH1F("Prompt_L1MuPt10_GenMuPt_dxy50to100_overlap","", 60,0.,60)
    Prompt_L1MuPt15_GenMuPt_dxy50to100_overlap = TH1F("Prompt_L1MuPt15_GenMuPt_dxy50to100_overlap","", 60,0.,60)
    Prompt_L1MuPt20_GenMuPt_dxy50to100_overlap = TH1F("Prompt_L1MuPt20_GenMuPt_dxy50to100_overlap","", 60,0.,60)


    Prompt_L1MuPt10_GenMuPt_endcap = TH1F("Prompt_L1MuPt10_GenMuPt_endcap","", 60,0.,60)
    Prompt_L1MuPt15_GenMuPt_endcap = TH1F("Prompt_L1MuPt15_GenMuPt_endcap","", 60,0.,60)
    Prompt_L1MuPt20_GenMuPt_endcap = TH1F("Prompt_L1MuPt20_GenMuPt_endcap","", 60,0.,60)

    Prompt_L1MuPt10_GenMuPt_dxy0to5_endcap = TH1F("Prompt_L1MuPt10_GenMuPt_dxy0to5_endcap","", 60,0.,60)
    Prompt_L1MuPt15_GenMuPt_dxy0to5_endcap = TH1F("Prompt_L1MuPt15_GenMuPt_dxy0to5_endcap","", 60,0.,60)
    Prompt_L1MuPt20_GenMuPt_dxy0to5_endcap = TH1F("Prompt_L1MuPt20_GenMuPt_dxy0to5_endcap","", 60,0.,60)

    Prompt_L1MuPt10_GenMuPt_dxy5to50_endcap = TH1F("Prompt_L1MuPt10_GenMuPt_dxy5to50_endcap","", 60,0.,60)
    Prompt_L1MuPt15_GenMuPt_dxy5to50_endcap = TH1F("Prompt_L1MuPt15_GenMuPt_dxy5to50_endcap","", 60,0.,60)
    Prompt_L1MuPt20_GenMuPt_dxy5to50_endcap = TH1F("Prompt_L1MuPt20_GenMuPt_dxy5to50_endcap","", 60,0.,60)

    Prompt_L1MuPt10_GenMuPt_dxy50to100_endcap = TH1F("Prompt_L1MuPt10_GenMuPt_dxy50to100_endcap","", 60,0.,60)
    Prompt_L1MuPt15_GenMuPt_dxy50to100_endcap = TH1F("Prompt_L1MuPt15_GenMuPt_dxy50to100_endcap","", 60,0.,60)
    Prompt_L1MuPt20_GenMuPt_dxy50to100_endcap = TH1F("Prompt_L1MuPt20_GenMuPt_dxy50to100_endcap","", 60,0.,60)

    for k in range(0,treeHits.GetEntries()):
      treeHits.GetEntry(k)
      if k%1000==0: print "Event", k+1, "nL1Mu", treeHits.nL1Mu
      if k>10000 and runTest: break

      ## plots for Alexei July 27 2016
      random_number = random.random()
      if random_number<0.5:
        choose_dark_boson = 0
      else:
        choose_dark_boson = 1

      pt_muon1_choose_dark_boson = abs(treeHits.genGdMu_pt[choose_dark_boson*2+0])
      pt_muon2_choose_dark_boson = abs(treeHits.genGdMu_pt[choose_dark_boson*2+1])

      if pt_muon1_choose_dark_boson > 10 and pt_muon2_choose_dark_boson > 10:
        
        eta_muon1_choose_dark_boson = treeHits.genGdMu_eta[choose_dark_boson*2+0]
        eta_muon2_choose_dark_boson = treeHits.genGdMu_eta[choose_dark_boson*2+1]
        
        eta_prop_muon1_choose_dark_boson = treeHits.genGdMu_eta_prop[choose_dark_boson*2+0]
        eta_prop_muon2_choose_dark_boson = treeHits.genGdMu_eta_prop[choose_dark_boson*2+1]

        if abs(eta_muon1_choose_dark_boson) > abs(eta_muon2_choose_dark_boson):
          GenMuEta_leading_random_pt10.Fill(eta_muon1_choose_dark_boson)
        else:
          GenMuEta_leading_random_pt10.Fill(eta_muon2_choose_dark_boson)

        if abs(eta_prop_muon1_choose_dark_boson) > abs(eta_prop_muon2_choose_dark_boson):
          GenMuEta_leading_MS2_random_pt10.Fill(eta_prop_muon1_choose_dark_boson)
        else:
          GenMuEta_leading_MS2_random_pt10.Fill(eta_prop_muon2_choose_dark_boson)
        

      for i in range(0,2):

        for j in range(0,2):
          ij = i*2+j
          
          pt = abs(treeHits.genGdMu_pt[ij])
          eta = treeHits.genGdMu_eta[ij]
          phi = abs(treeHits.genGdMu_phi[ij])
          #charge = abs(treeHits.genGdMu_q[ij])
          eta_prop = treeHits.genGdMu_eta_prop[ij]
          phi_prop = treeHits.genGdMu_phi_prop[ij]
          dxy = abs(treeHits.genGdMu_dxy[ij])
          vz = abs(treeHits.genGd_vz[i])
          lxy =  abs(treeHits.genGd_lxy[i])
          SIM_index = treeHits.genGdMu_SIM_index[ij]
          SIM_dR = treeHits.genGdMu_SIM_dR[ij]

          if ij==0: GenMuEta0_MS2.Fill(eta_prop)
          if ij==1: GenMuEta1_MS2.Fill(eta_prop)
          if ij==2: GenMuEta2_MS2.Fill(eta_prop)
          if ij==3: GenMuEta3_MS2.Fill(eta_prop)
          GenMuEta_MS2.Fill(eta_prop)

          ## exclude all the bad muons
          #if (abs(treeHits.genGdMu_eta_prop[i*2+0])>2.4): 
          #  continue
          #if (abs(treeHits.genGdMu_eta_prop[i*2+1])>2.4): 
          #  continue
          #if (abs(treeHits.genGdMu_pt[i*2+0])<5): 
          #  continue
          #if (abs(treeHits.genGdMu_pt[i*2+1])<5): 
          #  continue
          if (abs(treeHits.genGd0Gd1_dR) < 2):
            continue
          if (abs(treeHits.genGd_genMuMu_dR[i]) < 1):
            continue
          if treeHits.genGdMu_eta_prop[ij] == -99 or treeHits.genGdMu_phi_prop[ij] == -99:
            continue
          if lxy > 300:
            continue
          if vz > 500:
            continue
          if abs(eta_prop)>2.5:
            continue
          if pt<0:
            continue

          muon_barrel = abs(eta_prop)<=0.9
          muon_overlap = abs(eta_prop)>0.9 and abs(eta_prop)<=1.2
          muon_endcap = abs(eta_prop)>1.2 and abs(eta_prop)<=2.4

          GenMuPt.Fill(pt)
          if dxy <= 5:                GenMuPt_dxy0to5.Fill(pt)
          if 5 < dxy  and dxy <= 50:  GenMuPt_dxy5to50.Fill(pt)
          if 50 < dxy and dxy <= 100: GenMuPt_dxy50to100.Fill(pt)

          if (1.6 < abs(eta_prop) and abs(eta_prop) < 2.2):
            GenMuPt_eta16to22.Fill(pt)
            if dxy <= 5:                GenMuPt_dxy0to5_eta16to22.Fill(pt)
            if 5 < dxy  and dxy <= 50:  GenMuPt_dxy5to50_eta16to22.Fill(pt)
            if 50 < dxy and dxy <= 100: GenMuPt_dxy50to100_eta16to22.Fill(pt)
            

          if muon_barrel:
            GenMuPt_barrel.Fill(pt)
            if dxy <= 5:                GenMuPt_dxy0to5_barrel.Fill(pt)
            if 5 < dxy  and dxy <= 50:  GenMuPt_dxy5to50_barrel.Fill(pt)
            if 50 < dxy and dxy <= 100: GenMuPt_dxy50to100_barrel.Fill(pt)

          if muon_overlap:
            GenMuPt_overlap.Fill(pt)
            if dxy <= 5:                GenMuPt_dxy0to5_overlap.Fill(pt)
            if 5 < dxy  and dxy <= 50:  GenMuPt_dxy5to50_overlap.Fill(pt)
            if 50 < dxy and dxy <= 100: GenMuPt_dxy50to100_overlap.Fill(pt)

          if muon_endcap:
            GenMuPt_endcap.Fill(pt)
            if dxy <= 5:                GenMuPt_dxy0to5_endcap.Fill(pt)
            if 5 < dxy  and dxy <= 50:  GenMuPt_dxy5to50_endcap.Fill(pt)
            if 50 < dxy and dxy <= 100: GenMuPt_dxy50to100_endcap.Fill(pt)

          ## this is to make sure there are no freak L1Mu-GenMu matches!!
          L1Mu_index = treeHits.genGdMu_L1Mu_index_prop[ij]
          L1Mu_dR_prop = treeHits.genGdMu_L1Mu_dR_prop[ij]

          if verbose:
            print "\tGenMu", i, j,
            print "pt", pt,
#            print "eta", eta,
#            print "phi", phi,
            print "eta_prop", eta_prop,
            print "phi_prop", phi_prop,
#            print "dR_corr", treeHits.genGdMu_L1Mu_dR_corr[ij],
            print "index", treeHits.genGdMu_L1Mu_index_prop[ij],
            print "dR_prop", treeHits.genGdMu_L1Mu_dR_prop[ij],
            print "abs(dxy)", abs(treeHits.genGdMu_dxy[ij]),
            print "lxy", lxy,
            print "vz", vz
            #print "SIM_index", SIM_index
            #print "SIM_dR", SIM_dR

          if L1Mu_index != 99 and L1Mu_dR_prop < 0.2:
            L1Mu_quality = treeHits.L1Mu_quality[L1Mu_index]
            if L1Mu_quality <=0 :
              print "\t\tL1Mu was matched to GenMu, but has quality too low: ", L1Mu_quality 
              continue

            nL1MuTotal += 1
            L1Mu_pt = treeHits.L1Mu_pt[L1Mu_index]
            L1Mu_eta = treeHits.L1Mu_eta[L1Mu_index]
            L1Mu_phi = treeHits.L1Mu_phi[L1Mu_index]
            L1Mu_bx = treeHits.L1Mu_bx[L1Mu_index]
            L1Mu_quality = treeHits.L1Mu_quality[L1Mu_index]
            L1Mu_L1Tk_dR_prop = treeHits.L1Mu_L1Tk_dR_prop[L1Mu_index]
            L1Mu_L1Tk_pt_prop = treeHits.L1Mu_L1Tk_pt_prop[L1Mu_index]
            L1Mu_L1Tk_dR_prop_true = treeHits.L1Mu_L1Tk_dR_prop_true[L1Mu_index]
     
            ## L1Mu pT trigger turn-on curves
            if L1Mu_pt>=10:
              Prompt_L1MuPt10_GenMuPt.Fill(pt)
              if dxy <= 5:                Prompt_L1MuPt10_GenMuPt_dxy0to5.Fill(pt)
              if 5 < dxy  and dxy <= 50:  Prompt_L1MuPt10_GenMuPt_dxy5to50.Fill(pt)
              if 50 < dxy and dxy <= 100: Prompt_L1MuPt10_GenMuPt_dxy50to100.Fill(pt)
            if L1Mu_pt>=15:
              Prompt_L1MuPt15_GenMuPt.Fill(pt)
              if dxy <= 5:                Prompt_L1MuPt15_GenMuPt_dxy0to5.Fill(pt)
              if 5 < dxy  and dxy <= 50:  Prompt_L1MuPt15_GenMuPt_dxy5to50.Fill(pt)
              if 50 < dxy and dxy <= 100: Prompt_L1MuPt15_GenMuPt_dxy50to100.Fill(pt)
            if L1Mu_pt>=20:
              Prompt_L1MuPt20_GenMuPt.Fill(pt)
              if dxy <= 5:                Prompt_L1MuPt20_GenMuPt_dxy0to5.Fill(pt)
              if 5 < dxy  and dxy <= 50:  Prompt_L1MuPt20_GenMuPt_dxy5to50.Fill(pt)
              if 50 < dxy and dxy <= 100: Prompt_L1MuPt20_GenMuPt_dxy50to100.Fill(pt)

            if (1.6 < abs(eta_prop) and abs(eta_prop) < 2.2):
              if L1Mu_pt>=10:
                Prompt_L1MuPt10_GenMuPt_eta16to22.Fill(pt)
                if dxy <= 5:                Prompt_L1MuPt10_GenMuPt_dxy0to5_eta16to22.Fill(pt)
                if 5 < dxy  and dxy <= 50:  Prompt_L1MuPt10_GenMuPt_dxy5to50_eta16to22.Fill(pt)
                if 50 < dxy and dxy <= 100: Prompt_L1MuPt10_GenMuPt_dxy50to100_eta16to22.Fill(pt)
              if L1Mu_pt>=15:
                Prompt_L1MuPt15_GenMuPt_eta16to22.Fill(pt)
                if dxy <= 5:                Prompt_L1MuPt15_GenMuPt_dxy0to5_eta16to22.Fill(pt)
                if 5 < dxy  and dxy <= 50:  Prompt_L1MuPt15_GenMuPt_dxy5to50_eta16to22.Fill(pt)
                if 50 < dxy and dxy <= 100: Prompt_L1MuPt15_GenMuPt_dxy50to100_eta16to22.Fill(pt)
              if L1Mu_pt>=20:
                Prompt_L1MuPt20_GenMuPt_eta16to22.Fill(pt)
                if dxy <= 5:                Prompt_L1MuPt20_GenMuPt_dxy0to5_eta16to22.Fill(pt)
                if 5 < dxy  and dxy <= 50:  Prompt_L1MuPt20_GenMuPt_dxy5to50_eta16to22.Fill(pt)
                if 50 < dxy and dxy <= 100: Prompt_L1MuPt20_GenMuPt_dxy50to100_eta16to22.Fill(pt)


            if muon_barrel:
              if L1Mu_pt>=10:
                Prompt_L1MuPt10_GenMuPt_barrel.Fill(pt)
                if dxy <= 5:                Prompt_L1MuPt10_GenMuPt_dxy0to5_barrel.Fill(pt)
                if 5 < dxy  and dxy <= 50:  Prompt_L1MuPt10_GenMuPt_dxy5to50_barrel.Fill(pt)
                if 50 < dxy and dxy <= 100: Prompt_L1MuPt10_GenMuPt_dxy50to100_barrel.Fill(pt)
              if L1Mu_pt>=15:
                Prompt_L1MuPt15_GenMuPt_barrel.Fill(pt)
                if dxy <= 5:                Prompt_L1MuPt15_GenMuPt_dxy0to5_barrel.Fill(pt)
                if 5 < dxy  and dxy <= 50:  Prompt_L1MuPt15_GenMuPt_dxy5to50_barrel.Fill(pt)
                if 50 < dxy and dxy <= 100: Prompt_L1MuPt15_GenMuPt_dxy50to100_barrel.Fill(pt)
              if L1Mu_pt>=20:
                Prompt_L1MuPt20_GenMuPt_barrel.Fill(pt)
                if dxy <= 5:                Prompt_L1MuPt20_GenMuPt_dxy0to5_barrel.Fill(pt)
                if 5 < dxy  and dxy <= 50:  Prompt_L1MuPt20_GenMuPt_dxy5to50_barrel.Fill(pt)
                if 50 < dxy and dxy <= 100: Prompt_L1MuPt20_GenMuPt_dxy50to100_barrel.Fill(pt)


            if muon_overlap:
              if L1Mu_pt>=10:
                Prompt_L1MuPt10_GenMuPt_overlap.Fill(pt)
                if dxy <= 5:                Prompt_L1MuPt10_GenMuPt_dxy0to5_overlap.Fill(pt)
                if 5 < dxy  and dxy <= 50:  Prompt_L1MuPt10_GenMuPt_dxy5to50_overlap.Fill(pt)
                if 50 < dxy and dxy <= 100: Prompt_L1MuPt10_GenMuPt_dxy50to100_overlap.Fill(pt)
              if L1Mu_pt>=15:
                Prompt_L1MuPt15_GenMuPt_overlap.Fill(pt)
                if dxy <= 5:                Prompt_L1MuPt15_GenMuPt_dxy0to5_overlap.Fill(pt)
                if 5 < dxy  and dxy <= 50:  Prompt_L1MuPt15_GenMuPt_dxy5to50_overlap.Fill(pt)
                if 50 < dxy and dxy <= 100: Prompt_L1MuPt15_GenMuPt_dxy50to100_overlap.Fill(pt)
              if L1Mu_pt>=20:
                Prompt_L1MuPt20_GenMuPt_overlap.Fill(pt)
                if dxy <= 5:                Prompt_L1MuPt20_GenMuPt_dxy0to5_overlap.Fill(pt)
                if 5 < dxy  and dxy <= 50:  Prompt_L1MuPt20_GenMuPt_dxy5to50_overlap.Fill(pt)
                if 50 < dxy and dxy <= 100: Prompt_L1MuPt20_GenMuPt_dxy50to100_overlap.Fill(pt)


            if muon_endcap:
              if L1Mu_pt>=10:
                Prompt_L1MuPt10_GenMuPt_endcap.Fill(pt)
                if dxy <= 5:                Prompt_L1MuPt10_GenMuPt_dxy0to5_endcap.Fill(pt)
                if 5 < dxy  and dxy <= 50:  Prompt_L1MuPt10_GenMuPt_dxy5to50_endcap.Fill(pt)
                if 50 < dxy and dxy <= 100: Prompt_L1MuPt10_GenMuPt_dxy50to100_endcap.Fill(pt)
              if L1Mu_pt>=15:
                Prompt_L1MuPt15_GenMuPt_endcap.Fill(pt)
                if dxy <= 5:                Prompt_L1MuPt15_GenMuPt_dxy0to5_endcap.Fill(pt)
                if 5 < dxy  and dxy <= 50:  Prompt_L1MuPt15_GenMuPt_dxy5to50_endcap.Fill(pt)
                if 50 < dxy and dxy <= 100: Prompt_L1MuPt15_GenMuPt_dxy50to100_endcap.Fill(pt)
              if L1Mu_pt>=20:
                Prompt_L1MuPt20_GenMuPt_endcap.Fill(pt)
                if dxy <= 5:                Prompt_L1MuPt20_GenMuPt_dxy0to5_endcap.Fill(pt)
                if 5 < dxy  and dxy <= 50:  Prompt_L1MuPt20_GenMuPt_dxy5to50_endcap.Fill(pt)
                if 50 < dxy and dxy <= 100: Prompt_L1MuPt20_GenMuPt_dxy50to100_endcap.Fill(pt)


            if verbose:
              print "\t\tMatched: L1Mu", "pt", L1Mu_pt, "eta", L1Mu_eta, 
              print "phi", L1Mu_phi, "Quality", L1Mu_quality, "L1mu_bx", L1Mu_bx,
              print "L1Mu_L1Tk_dR_min", L1Mu_L1Tk_dR_prop, "L1Mu_L1Tk_pt", L1Mu_L1Tk_pt_prop
              print 

            ## Check for matches -- summary
            L1Mu_DTTF_index  = treeHits.L1Mu_DTTF_index[L1Mu_index]
            L1Mu_CSCTF_index = treeHits.L1Mu_CSCTF_index[L1Mu_index]
            if processRPC:
              L1Mu_RPCb_index  = treeHits.L1Mu_RPCb_index[L1Mu_index]
              L1Mu_RPCf_index  = treeHits.L1Mu_RPCf_index[L1Mu_index]

            m_CSCTF = L1Mu_CSCTF_index != 99 and L1Mu_CSCTF_index != -1
            m_DTTF  = L1Mu_DTTF_index  != 99 and L1Mu_DTTF_index  != -1
            m_RPCb = False
            m_RPCf = False
            if processRPC:
              m_RPCb  = L1Mu_RPCb_index  != 99 and L1Mu_RPCb_index  != -1
              m_RPCf  = L1Mu_RPCf_index  != 99 and L1Mu_RPCf_index  != -1

            n_CSCTF = not m_CSCTF
            n_DTTF  = not m_DTTF
            n_RPCb  = not m_RPCb
            n_RPCf  = not m_RPCf

            if n_CSCTF and n_DTTF and n_RPCb and n_RPCf: nL1MuNotMatched +=1
            
            if m_CSCTF and n_DTTF and n_RPCb and n_RPCf: nL1MuMatched_CSCTF += 1
            if n_CSCTF and m_DTTF and n_RPCb and n_RPCf: nL1MuMatched_DTTF  += 1
            if n_CSCTF and n_DTTF and m_RPCb and n_RPCf: nL1MuMatched_RPCb  += 1
            if n_CSCTF and n_DTTF and n_RPCb and m_RPCf: nL1MuMatched_RPCf  += 1
              
            if m_CSCTF and m_DTTF and n_RPCb and n_RPCf: nL1MuMatched_DTTF_CSCTF += 1
            if n_CSCTF and n_DTTF and m_RPCb and m_RPCf: nL1MuMatched_RPCb_RPCf  += 1
            if n_CSCTF and m_DTTF and m_RPCb and n_RPCf: nL1MuMatched_DTTF_RPCb  += 1
            if n_CSCTF and m_DTTF and n_RPCb and m_RPCf: nL1MuMatched_DTTF_RPCf  += 1
            if m_CSCTF and n_DTTF and m_RPCb and n_RPCf: nL1MuMatched_CSCTF_RPCb += 1
            if m_CSCTF and n_DTTF and n_RPCb and m_RPCf: nL1MuMatched_CSCTF_RPCf += 1
              
            if m_CSCTF and m_DTTF and m_RPCb and n_RPCf: nL1MuMatched_CSCTF_DTTF_RPCb += 1
            if m_CSCTF and m_DTTF and n_RPCb and m_RPCf: nL1MuMatched_CSCTF_DTTF_RPCf += 1
            if n_CSCTF and m_DTTF and m_RPCb and m_RPCf: nL1MuMatched_DTTF_RPCb_RPCf  += 1
            if m_CSCTF and n_DTTF and m_RPCb and m_RPCf: nL1MuMatched_CSCTF_RPCb_RPCf += 1
            
            if m_CSCTF and m_DTTF and m_RPCb and m_RPCf: nL1MuMatched_DTTF_CSCTF_RPCb_RPCf +=1


            ## Matched to DT
            if verbose:
              print "\t\t>>>>INFO: Number of DTTFs", treeHits.nDTTF
              print
            
            if m_DTTF:
              if verbose:
                print "\t\t>>>>INFO: Matching DTTF with index", L1Mu_DTTF_index
              DTTF_pt = treeHits.DTTF_pt[L1Mu_DTTF_index]
              DTTF_eta = treeHits.DTTF_eta[L1Mu_DTTF_index]
              DTTF_phi = treeHits.DTTF_phi[L1Mu_DTTF_index]
              DTTF_bx = treeHits.DTTF_bx[L1Mu_DTTF_index]
              DTTF_nStubs = treeHits.DTTF_nStubs[L1Mu_DTTF_index]

              DTTF_phib1 = treeHits.DTTF_phib1[L1Mu_DTTF_index]
              DTTF_phib2 = treeHits.DTTF_phib2[L1Mu_DTTF_index]
              DTTF_phib3 = treeHits.DTTF_phib3[L1Mu_DTTF_index]
              DTTF_phib4 = treeHits.DTTF_phib4[L1Mu_DTTF_index]

              DTTF_phi1 = treeHits.DTTF_phi1[L1Mu_DTTF_index]
              DTTF_phi2 = treeHits.DTTF_phi2[L1Mu_DTTF_index]
              DTTF_phi3 = treeHits.DTTF_phi3[L1Mu_DTTF_index]
              DTTF_phi4 = treeHits.DTTF_phi4[L1Mu_DTTF_index]
              
              ok_DTTF_st1 = DTTF_phib1 != 99 and DTTF_phi1 != 99 
              ok_DTTF_st2 = DTTF_phib2 != 99 and DTTF_phi2 != 99 
              ok_DTTF_st3 = DTTF_phib3 != 99 and DTTF_phi3 != 99
              ok_DTTF_st4 = DTTF_phib4 != 99 and DTTF_phi4 != 99

              DTTF_phib1 = normalizedPhi(DTTF_phib1 + DTTF_phi1)
              DTTF_phib2 = normalizedPhi(DTTF_phib2 + DTTF_phi2)
              DTTF_phib3 = normalizedPhi(DTTF_phib3 + DTTF_phi3)
              DTTF_phib4 = normalizedPhi(DTTF_phib4 + DTTF_phi4)

              """
              DTTF_pt_1_2 = getPtFromDphi(1,2,DTTF_phib1,DTTF_phib2, 'pol3')
              DTTF_pt_1_3 = getPtFromDphi(1,3,DTTF_phib1,DTTF_phib3, 'pol2')
              DTTF_pt_1_4 = getPtFromDphi(1,4,DTTF_phib1,DTTF_phib4, 'pol3')
              DTTF_pt_2_3 = getPtFromDphi(2,3,DTTF_phib2,DTTF_phib3, 'pol3')
              DTTF_pt_2_4 = getPtFromDphi(2,4,DTTF_phib2,DTTF_phib4, 'pol2')
              DTTF_pt_3_4 = getPtFromDphi(3,4,DTTF_phib3,DTTF_phib4, 'pol3')
              """
              
              if verbose:
                print "\t\tDTTF", L1Mu_DTTF_index
                print "\t\tDTTF_pt", DTTF_pt
                print "\t\tDTTF_eta", DTTF_eta
                print "\t\tDTTF_phi", DTTF_phi
                print "\t\tDTTF_bx", DTTF_bx
                print "\t\tDTTF_nStubs", DTTF_nStubs
                print "\t\tDTTF_phib1", DTTF_phib1 
                print "\t\tDTTF_phib2", DTTF_phib2
                print "\t\tDTTF_phib3", DTTF_phib3
                print "\t\tDTTF_phib4", DTTF_phib4
                print "\t\tDTTF_phi1", DTTF_phi1 
                print "\t\tDTTF_phi2", DTTF_phi2
                print "\t\tDTTF_phi3", DTTF_phi3
                print "\t\tDTTF_phi4", DTTF_phi4
                #print "\t\tDTTF_phib1p", DTTF_phib1p 
                #print "\t\tDTTF_phib2p", DTTF_phib2p
                #print "\t\tDTTF_phib3p", DTTF_phib3p
                #print "\t\tDTTF_phib4p", DTTF_phib4p
                print
                """
                print "Pt from 1, 2", DTTF_pt_1_2 
                print "Pt from 1, 3", DTTF_pt_1_3
                print "Pt from 1, 4", DTTF_pt_1_4
                print "Pt from 2, 3", DTTF_pt_2_3
                print "Pt from 2, 4", DTTF_pt_2_4
                print "Pt from 3, 4", DTTF_pt_3_4
                """

              ## fill histograms
              DTTF_phib1_phib2 = deltaPhi(DTTF_phib1, DTTF_phib2) 
              DTTF_phib1_phib3 = deltaPhi(DTTF_phib1, DTTF_phib3)
              DTTF_phib1_phib4 = deltaPhi(DTTF_phib1, DTTF_phib4)
              DTTF_phib2_phib3 = deltaPhi(DTTF_phib2, DTTF_phib3)
              DTTF_phib2_phib4 = deltaPhi(DTTF_phib2, DTTF_phib4)
              DTTF_phib3_phib4 = deltaPhi(DTTF_phib3, DTTF_phib4)

              abs_DTTF_phib1_phib2 = abs(DTTF_phib1_phib2)
              abs_DTTF_phib1_phib3 = abs(DTTF_phib1_phib3)
              abs_DTTF_phib1_phib4 = abs(DTTF_phib1_phib4)
              abs_DTTF_phib2_phib3 = abs(DTTF_phib2_phib3)
              abs_DTTF_phib2_phib4 = abs(DTTF_phib2_phib4)
              abs_DTTF_phib3_phib4 = abs(DTTF_phib3_phib4)

              if ok_DTTF_st1 and ok_DTTF_st2: phiDTst1_phiDTst2.Fill(DTTF_phib1_phib2)
              if ok_DTTF_st1 and ok_DTTF_st3: phiDTst1_phiDTst3.Fill(DTTF_phib1_phib3)
              if ok_DTTF_st1 and ok_DTTF_st4: phiDTst1_phiDTst4.Fill(DTTF_phib1_phib4)
              if ok_DTTF_st2 and ok_DTTF_st3: phiDTst2_phiDTst3.Fill(DTTF_phib2_phib3)
              if ok_DTTF_st2 and ok_DTTF_st4: phiDTst2_phiDTst4.Fill(DTTF_phib2_phib4)
              if ok_DTTF_st3 and ok_DTTF_st4: phiDTst3_phiDTst4.Fill(DTTF_phib3_phib4)

              if ok_DTTF_st1 and ok_DTTF_st2: abs_phiDTst1_phiDTst2.Fill(abs_DTTF_phib1_phib2)
              if ok_DTTF_st1 and ok_DTTF_st3: abs_phiDTst1_phiDTst3.Fill(abs_DTTF_phib1_phib3)
              if ok_DTTF_st1 and ok_DTTF_st4: abs_phiDTst1_phiDTst4.Fill(abs_DTTF_phib1_phib4)
              if ok_DTTF_st2 and ok_DTTF_st3: abs_phiDTst2_phiDTst3.Fill(abs_DTTF_phib2_phib3)
              if ok_DTTF_st2 and ok_DTTF_st4: abs_phiDTst2_phiDTst4.Fill(abs_DTTF_phib2_phib4)
              if ok_DTTF_st3 and ok_DTTF_st4: abs_phiDTst3_phiDTst4.Fill(abs_DTTF_phib3_phib4)

              if ok_DTTF_st1 and ok_DTTF_st2: GenMuPt_vs_phiDTst1_phiDTst2.Fill(pt, DTTF_phib1_phib2)
              if ok_DTTF_st1 and ok_DTTF_st3: GenMuPt_vs_phiDTst1_phiDTst3.Fill(pt, DTTF_phib1_phib3)
              if ok_DTTF_st1 and ok_DTTF_st4: GenMuPt_vs_phiDTst1_phiDTst4.Fill(pt, DTTF_phib1_phib4)
              if ok_DTTF_st2 and ok_DTTF_st3: GenMuPt_vs_phiDTst2_phiDTst3.Fill(pt, DTTF_phib2_phib3)
              if ok_DTTF_st2 and ok_DTTF_st4: GenMuPt_vs_phiDTst2_phiDTst4.Fill(pt, DTTF_phib2_phib4)
              if ok_DTTF_st3 and ok_DTTF_st4: GenMuPt_vs_phiDTst3_phiDTst4.Fill(pt, DTTF_phib3_phib4)

              if ok_DTTF_st1 and ok_DTTF_st2: GenMuPt_vs_abs_phiDTst1_phiDTst2.Fill(pt, abs_DTTF_phib1_phib2)
              if ok_DTTF_st1 and ok_DTTF_st3: GenMuPt_vs_abs_phiDTst1_phiDTst3.Fill(pt, abs_DTTF_phib1_phib3)
              if ok_DTTF_st1 and ok_DTTF_st4: GenMuPt_vs_abs_phiDTst1_phiDTst4.Fill(pt, abs_DTTF_phib1_phib4)
              if ok_DTTF_st2 and ok_DTTF_st3: GenMuPt_vs_abs_phiDTst2_phiDTst3.Fill(pt, abs_DTTF_phib2_phib3)
              if ok_DTTF_st2 and ok_DTTF_st4: GenMuPt_vs_abs_phiDTst2_phiDTst4.Fill(pt, abs_DTTF_phib2_phib4)
              if ok_DTTF_st3 and ok_DTTF_st4: GenMuPt_vs_abs_phiDTst3_phiDTst4.Fill(pt, abs_DTTF_phib3_phib4)

              ## base histograms for pT from dphi assignment
              if ok_DTTF_st1 and ok_DTTF_st2: GenMuPt_DT1_DT2.Fill(pt)
              if ok_DTTF_st1 and ok_DTTF_st3: GenMuPt_DT1_DT3.Fill(pt)
              if ok_DTTF_st1 and ok_DTTF_st4: GenMuPt_DT1_DT4.Fill(pt)
              if ok_DTTF_st2 and ok_DTTF_st3: GenMuPt_DT2_DT3.Fill(pt)
              if ok_DTTF_st3 and ok_DTTF_st4: GenMuPt_DT2_DT4.Fill(pt)
              if ok_DTTF_st4 and ok_DTTF_st4: GenMuPt_DT3_DT4.Fill(pt)

              if dxy <= 5:
                if ok_DTTF_st1 and ok_DTTF_st2: GenMuPt_DT1_DT2_dxy0to5.Fill(pt)
                if ok_DTTF_st1 and ok_DTTF_st3: GenMuPt_DT1_DT3_dxy0to5.Fill(pt)
                if ok_DTTF_st1 and ok_DTTF_st4: 
                  GenMuPt_DT1_DT4_dxy0to5.Fill(pt)
                  phiDTst1_vs_phiDTst4_dxy0to5.Fill(DTTF_phi1, DTTF_phi4)
                if ok_DTTF_st2 and ok_DTTF_st3: GenMuPt_DT2_DT3_dxy0to5.Fill(pt)
                if ok_DTTF_st2 and ok_DTTF_st4: GenMuPt_DT2_DT4_dxy0to5.Fill(pt)
                if ok_DTTF_st3 and ok_DTTF_st4: GenMuPt_DT3_DT4_dxy0to5.Fill(pt)
              if 5 < dxy  and dxy <= 50:
                if ok_DTTF_st1 and ok_DTTF_st2: GenMuPt_DT1_DT2_dxy5to50.Fill(pt)
                if ok_DTTF_st1 and ok_DTTF_st3: GenMuPt_DT1_DT3_dxy5to50.Fill(pt)
                if ok_DTTF_st1 and ok_DTTF_st4: 
                  GenMuPt_DT1_DT4_dxy5to50.Fill(pt)
                  phiDTst1_vs_phiDTst4_dxy5to50.Fill(DTTF_phi1, DTTF_phi4)
                if ok_DTTF_st2 and ok_DTTF_st3: GenMuPt_DT2_DT3_dxy5to50.Fill(pt)
                if ok_DTTF_st2 and ok_DTTF_st4: GenMuPt_DT2_DT4_dxy5to50.Fill(pt)
                if ok_DTTF_st3 and ok_DTTF_st4: GenMuPt_DT3_DT4_dxy5to50.Fill(pt)
              if 50 < dxy and dxy <= 100:
                if ok_DTTF_st1 and ok_DTTF_st2: GenMuPt_DT1_DT2_dxy50to100.Fill(pt)
                if ok_DTTF_st1 and ok_DTTF_st3: GenMuPt_DT1_DT3_dxy50to100.Fill(pt)
                if ok_DTTF_st1 and ok_DTTF_st4: 
                  GenMuPt_DT1_DT4_dxy50to100.Fill(pt)
                  phiDTst1_vs_phiDTst4_dxy50to100.Fill(DTTF_phi1, DTTF_phi4)
                if ok_DTTF_st2 and ok_DTTF_st3: GenMuPt_DT2_DT3_dxy50to100.Fill(pt)
                if ok_DTTF_st2 and ok_DTTF_st4: GenMuPt_DT2_DT4_dxy50to100.Fill(pt)
                if ok_DTTF_st3 and ok_DTTF_st4: GenMuPt_DT3_DT4_dxy50to100.Fill(pt)

              if muon_barrel:
                if dxy <= 5:
                  if ok_DTTF_st1 and ok_DTTF_st2: GenMuPt_DT1_DT2_dxy0to5_barrel.Fill(pt)
                  if ok_DTTF_st1 and ok_DTTF_st3: GenMuPt_DT1_DT3_dxy0to5_barrel.Fill(pt)
                  if ok_DTTF_st1 and ok_DTTF_st4: GenMuPt_DT1_DT4_dxy0to5_barrel.Fill(pt)
                  if ok_DTTF_st2 and ok_DTTF_st3: GenMuPt_DT2_DT3_dxy0to5_barrel.Fill(pt)
                  if ok_DTTF_st2 and ok_DTTF_st4: GenMuPt_DT2_DT4_dxy0to5_barrel.Fill(pt)
                  if ok_DTTF_st3 and ok_DTTF_st4: GenMuPt_DT3_DT4_dxy0to5_barrel.Fill(pt)
                if 5 < dxy  and dxy <= 50:
                  if ok_DTTF_st1 and ok_DTTF_st2: GenMuPt_DT1_DT2_dxy5to50_barrel.Fill(pt)
                  if ok_DTTF_st1 and ok_DTTF_st3: GenMuPt_DT1_DT3_dxy5to50_barrel.Fill(pt)
                  if ok_DTTF_st1 and ok_DTTF_st4: GenMuPt_DT1_DT4_dxy5to50_barrel.Fill(pt)
                  if ok_DTTF_st2 and ok_DTTF_st3: GenMuPt_DT2_DT3_dxy5to50_barrel.Fill(pt)
                  if ok_DTTF_st2 and ok_DTTF_st4: GenMuPt_DT2_DT4_dxy5to50_barrel.Fill(pt)
                  if ok_DTTF_st3 and ok_DTTF_st4: GenMuPt_DT3_DT4_dxy5to50_barrel.Fill(pt)
                if 50 < dxy and dxy <= 100:
                  if ok_DTTF_st1 and ok_DTTF_st2: GenMuPt_DT1_DT2_dxy50to100_barrel.Fill(pt)
                  if ok_DTTF_st1 and ok_DTTF_st3: GenMuPt_DT1_DT3_dxy50to100_barrel.Fill(pt)
                  if ok_DTTF_st1 and ok_DTTF_st4: GenMuPt_DT1_DT4_dxy50to100_barrel.Fill(pt)
                  if ok_DTTF_st2 and ok_DTTF_st3: GenMuPt_DT2_DT3_dxy50to100_barrel.Fill(pt)
                  if ok_DTTF_st2 and ok_DTTF_st4: GenMuPt_DT2_DT4_dxy50to100_barrel.Fill(pt)
                  if ok_DTTF_st3 and ok_DTTF_st4: GenMuPt_DT3_DT4_dxy50to100_barrel.Fill(pt)
              if muon_overlap:
                if dxy <= 5:
                  if ok_DTTF_st1 and ok_DTTF_st2: GenMuPt_DT1_DT2_dxy0to5_overlap.Fill(pt)
                  if ok_DTTF_st1 and ok_DTTF_st3: GenMuPt_DT1_DT3_dxy0to5_overlap.Fill(pt)
                  if ok_DTTF_st1 and ok_DTTF_st4: GenMuPt_DT1_DT4_dxy0to5_overlap.Fill(pt)
                  if ok_DTTF_st2 and ok_DTTF_st3: GenMuPt_DT2_DT3_dxy0to5_overlap.Fill(pt)
                  if ok_DTTF_st2 and ok_DTTF_st4: GenMuPt_DT2_DT4_dxy0to5_overlap.Fill(pt)
                  if ok_DTTF_st3 and ok_DTTF_st4: GenMuPt_DT3_DT4_dxy0to5_overlap.Fill(pt)
                if 5 < dxy  and dxy <= 50:
                  if ok_DTTF_st1 and ok_DTTF_st2: GenMuPt_DT1_DT2_dxy5to50_overlap.Fill(pt)
                  if ok_DTTF_st1 and ok_DTTF_st3: GenMuPt_DT1_DT3_dxy5to50_overlap.Fill(pt)
                  if ok_DTTF_st1 and ok_DTTF_st4: GenMuPt_DT1_DT4_dxy5to50_overlap.Fill(pt)
                  if ok_DTTF_st2 and ok_DTTF_st3: GenMuPt_DT2_DT3_dxy5to50_overlap.Fill(pt)
                  if ok_DTTF_st2 and ok_DTTF_st4: GenMuPt_DT2_DT4_dxy5to50_overlap.Fill(pt)
                  if ok_DTTF_st3 and ok_DTTF_st4: GenMuPt_DT3_DT4_dxy5to50_overlap.Fill(pt)
                if 50 < dxy and dxy <= 100:
                  if ok_DTTF_st1 and ok_DTTF_st2: GenMuPt_DT1_DT2_dxy50to100_overlap.Fill(pt)
                  if ok_DTTF_st1 and ok_DTTF_st3: GenMuPt_DT1_DT3_dxy50to100_overlap.Fill(pt)
                  if ok_DTTF_st1 and ok_DTTF_st4: GenMuPt_DT1_DT4_dxy50to100_overlap.Fill(pt)
                  if ok_DTTF_st2 and ok_DTTF_st3: GenMuPt_DT2_DT3_dxy50to100_overlap.Fill(pt)
                  if ok_DTTF_st2 and ok_DTTF_st4: GenMuPt_DT2_DT4_dxy50to100_overlap.Fill(pt)
                  if ok_DTTF_st3 and ok_DTTF_st4: GenMuPt_DT3_DT4_dxy50to100_overlap.Fill(pt)
              if muon_endcap:
                if dxy <= 5:
                  if ok_DTTF_st1 and ok_DTTF_st2: GenMuPt_DT1_DT2_dxy0to5_endcap.Fill(pt)
                  if ok_DTTF_st1 and ok_DTTF_st3: GenMuPt_DT1_DT3_dxy0to5_endcap.Fill(pt)
                  if ok_DTTF_st1 and ok_DTTF_st4: GenMuPt_DT1_DT4_dxy0to5_endcap.Fill(pt)
                  if ok_DTTF_st2 and ok_DTTF_st3: GenMuPt_DT2_DT3_dxy0to5_endcap.Fill(pt)
                  if ok_DTTF_st2 and ok_DTTF_st4: GenMuPt_DT2_DT4_dxy0to5_endcap.Fill(pt)
                  if ok_DTTF_st3 and ok_DTTF_st4: GenMuPt_DT3_DT4_dxy0to5_endcap.Fill(pt)
                if 5 < dxy  and dxy <= 50:
                  if ok_DTTF_st1 and ok_DTTF_st2: GenMuPt_DT1_DT2_dxy5to50_endcap.Fill(pt)
                  if ok_DTTF_st1 and ok_DTTF_st3: GenMuPt_DT1_DT3_dxy5to50_endcap.Fill(pt)
                  if ok_DTTF_st1 and ok_DTTF_st4: GenMuPt_DT1_DT4_dxy5to50_endcap.Fill(pt)
                  if ok_DTTF_st2 and ok_DTTF_st3: GenMuPt_DT2_DT3_dxy5to50_endcap.Fill(pt)
                  if ok_DTTF_st2 and ok_DTTF_st4: GenMuPt_DT2_DT4_dxy5to50_endcap.Fill(pt)
                  if ok_DTTF_st3 and ok_DTTF_st4: GenMuPt_DT3_DT4_dxy5to50_endcap.Fill(pt)
                if 50 < dxy and dxy <= 100:
                  if ok_DTTF_st1 and ok_DTTF_st2: GenMuPt_DT1_DT2_dxy50to100_endcap.Fill(pt)
                  if ok_DTTF_st1 and ok_DTTF_st3: GenMuPt_DT1_DT3_dxy50to100_endcap.Fill(pt)
                  if ok_DTTF_st1 and ok_DTTF_st4: GenMuPt_DT1_DT4_dxy50to100_endcap.Fill(pt)
                  if ok_DTTF_st2 and ok_DTTF_st3: GenMuPt_DT2_DT3_dxy50to100_endcap.Fill(pt)
                  if ok_DTTF_st2 and ok_DTTF_st4: GenMuPt_DT2_DT4_dxy50to100_endcap.Fill(pt)
                  if ok_DTTF_st3 and ok_DTTF_st4: GenMuPt_DT3_DT4_dxy50to100_endcap.Fill(pt)



              L1Mu_DT_status = L1Mu_status(DTTF_phib1, DTTF_phib2, DTTF_phib3, DTTF_phib4)
              nDT_stubs.Fill(L1Mu_DT_status ) 
              nDT_stubs_vs_dxy.Fill(L1Mu_DT_status, dxy) 


              if ok_DTTF_st1 and ok_DTTF_st2 and DTTF_phib1!=DTTF_phib2: GenMuPt_vs_abs_phiDTst1_phiDTst2_inv.Fill(pt, 1./abs_DTTF_phib1_phib2) 
              if ok_DTTF_st1 and ok_DTTF_st3 and DTTF_phib1!=DTTF_phib3: GenMuPt_vs_abs_phiDTst1_phiDTst3_inv.Fill(pt, 1./abs_DTTF_phib1_phib3)
              if ok_DTTF_st1 and ok_DTTF_st4 and DTTF_phib1!=DTTF_phib4: GenMuPt_vs_abs_phiDTst1_phiDTst4_inv.Fill(pt, 1./abs_DTTF_phib1_phib4)
              if ok_DTTF_st2 and ok_DTTF_st3 and DTTF_phib2!=DTTF_phib3: GenMuPt_vs_abs_phiDTst2_phiDTst3_inv.Fill(pt, 1./abs_DTTF_phib2_phib3)
              if ok_DTTF_st2 and ok_DTTF_st4 and DTTF_phib2!=DTTF_phib4: GenMuPt_vs_abs_phiDTst2_phiDTst4_inv.Fill(pt, 1./abs_DTTF_phib2_phib4)
              if ok_DTTF_st3 and ok_DTTF_st4 and DTTF_phib3!=DTTF_phib4: GenMuPt_vs_abs_phiDTst3_phiDTst4_inv.Fill(pt, 1./abs_DTTF_phib3_phib4)


              if ok_DTTF_st1 and ok_DTTF_st4 and DTTF_phib1!=DTTF_phib4:
                if dxy <= 5:                GenMuPt_vs_abs_phiDTst1_phiDTst4_inv_dxy0to5.Fill(pt, 1./abs_DTTF_phib1_phib4)
                if 5 < dxy  and dxy <= 50:  GenMuPt_vs_abs_phiDTst1_phiDTst4_inv_dxy5to50.Fill(pt, 1./abs_DTTF_phib1_phib4)
                if 50 < dxy and dxy <= 100: GenMuPt_vs_abs_phiDTst1_phiDTst4_inv_dxy50to100.Fill(pt, 1./abs_DTTF_phib1_phib4)

              if ok_DTTF_st1 and ok_DTTF_st4:
                pt_special = 0
                if DTTF_phib1 != DTTF_phib4:
                  pt_special = ( ( 1./abs_DTTF_phib1_phib4) + 3.86872357483  ) /  1.48212936934
                else:
                  pt_special = 140 ## max pT  

                if pt_special>=10: 
                  Displaced_L1MuPt10_GenMuPt.Fill(pt)
                  if dxy <= 5:                Displaced_L1MuPt10_GenMuPt_dxy0to5.Fill(pt)
                  if 5 < dxy  and dxy <= 50:  Displaced_L1MuPt10_GenMuPt_dxy5to50.Fill(pt)
                  if 50 < dxy and dxy <= 100: Displaced_L1MuPt10_GenMuPt_dxy50to100.Fill(pt)
                if pt_special>=15:
                  Displaced_L1MuPt15_GenMuPt.Fill(pt)
                  if dxy <= 5:                Displaced_L1MuPt15_GenMuPt_dxy0to5.Fill(pt)
                  if 5 < dxy  and dxy <= 50:  Displaced_L1MuPt15_GenMuPt_dxy5to50.Fill(pt)
                  if 50 < dxy and dxy <= 100: Displaced_L1MuPt15_GenMuPt_dxy50to100.Fill(pt)
 
                if pt_special>=20: 
                  Displaced_L1MuPt20_GenMuPt.Fill(pt)
                  if dxy <= 5:                Displaced_L1MuPt20_GenMuPt_dxy0to5.Fill(pt)
                  if 5 < dxy  and dxy <= 50:  Displaced_L1MuPt20_GenMuPt_dxy5to50.Fill(pt)
                  if 50 < dxy and dxy <= 100: Displaced_L1MuPt20_GenMuPt_dxy50to100.Fill(pt)

                
            else:
              if printExtraInfo:
                print "\t\t>>>>INFO: No Matching DTTF!!! Print all available DTTF..."
                print
                for jj in range(0,treeHits.nDTTF):
                  DTTF_pt = treeHits.DTTF_pt[jj]
                  DTTF_eta = treeHits.DTTF_eta[jj]
                  DTTF_phi = treeHits.DTTF_phi[jj]
                  DTTF_bx = treeHits.DTTF_bx[jj]
                  DTTF_nStubs = treeHits.DTTF_nStubs[jj]
                  DTTF_phib1 = treeHits.DTTF_phib1[jj]
                  DTTF_phib2 = treeHits.DTTF_phib2[jj]
                  DTTF_phib3 = treeHits.DTTF_phib3[jj]
                  DTTF_phib4 = treeHits.DTTF_phib4[jj]
                  print "\t\tDTTF", jj
                  print "\t\tDTTF_pt", DTTF_pt
                  print "\t\tDTTF_eta", DTTF_eta
                  print "\t\tDTTF_phi", DTTF_phi
                  print "\t\tDTTF_bx", DTTF_bx
                  print "\t\tDTTF_nStubs", DTTF_nStubs
                  print "\t\tDTTF_phib1", DTTF_phib1 
                  print "\t\tDTTF_phib2", DTTF_phib2
                  print "\t\tDTTF_phib3", DTTF_phib3
                  print "\t\tDTTF_phib4", DTTF_phib4
                  print
 
            ## Matched to CSC
            if verbose:
              print "\t\t>>>>INFO: Number of CSCTFs", treeHits.nCSCTF
              print

            if m_CSCTF:
              if verbose:
                print "\t\t>>>>INFO: Matching CSCTF with index", L1Mu_CSCTF_index 
              CSCTF_pt = treeHits.CSCTF_pt[L1Mu_CSCTF_index]
              CSCTF_eta = treeHits.CSCTF_eta[L1Mu_CSCTF_index]
              CSCTF_phi = treeHits.CSCTF_phi[L1Mu_CSCTF_index]
              CSCTF_bx = treeHits.CSCTF_bx[L1Mu_CSCTF_index]
              CSCTF_nStubs = treeHits.CSCTF_nStubs[L1Mu_CSCTF_index]

              CSCTF_phi1 = treeHits.CSCTF_phi1[L1Mu_CSCTF_index]
              CSCTF_phi2 = treeHits.CSCTF_phi2[L1Mu_CSCTF_index]
              CSCTF_phi3 = treeHits.CSCTF_phi3[L1Mu_CSCTF_index]
              CSCTF_phi4 = treeHits.CSCTF_phi4[L1Mu_CSCTF_index]

              ok_CSCTF_st1 = CSCTF_phi1 != 99
              ok_CSCTF_st2 = CSCTF_phi2 != 99
              ok_CSCTF_st3 = CSCTF_phi3 != 99
              ok_CSCTF_st4 = CSCTF_phi4 != 99

              ok_CSCTF_rec_st1 = False
              ok_CSCTF_rec_st2 = False
              ok_CSCTF_rec_st3 = False
              ok_CSCTF_rec_st4 = False

              if ok_CSCTF_st1: CSCTF_phi1 = normalizedPhi2(treeHits.CSCTF_phi1[L1Mu_CSCTF_index])
              if ok_CSCTF_st2: CSCTF_phi2 = normalizedPhi2(treeHits.CSCTF_phi2[L1Mu_CSCTF_index])
              if ok_CSCTF_st3: CSCTF_phi3 = normalizedPhi2(treeHits.CSCTF_phi3[L1Mu_CSCTF_index])
              if ok_CSCTF_st4: CSCTF_phi4 = normalizedPhi2(treeHits.CSCTF_phi4[L1Mu_CSCTF_index])
              
              CSCTF_ch1 = treeHits.CSCTF_ch1[L1Mu_CSCTF_index]
              CSCTF_ch2 = treeHits.CSCTF_ch2[L1Mu_CSCTF_index]
              CSCTF_ch3 = treeHits.CSCTF_ch3[L1Mu_CSCTF_index]
              CSCTF_ch4 = treeHits.CSCTF_ch4[L1Mu_CSCTF_index]

              CSCTF_isOdd1 = CSCTF_ch1%2==1
              CSCTF_isOdd2 = CSCTF_ch2%2==1
              CSCTF_isOdd3 = CSCTF_ch3%2==1
              CSCTF_isOdd4 = CSCTF_ch4%2==1

              CSCTF_isEven1 = not CSCTF_isOdd1
              CSCTF_isEven2 = not CSCTF_isOdd2
              CSCTF_isEven3 = not CSCTF_isOdd3
              CSCTF_isEven4 = not CSCTF_isOdd4

              CSCTF_gemdphi1 = treeHits.CSCTF_gemdphi1[L1Mu_CSCTF_index]
              CSCTF_gemdphi2 = treeHits.CSCTF_gemdphi2[L1Mu_CSCTF_index]

              CSCTF_z1 = treeHits.CSCTF_z1[L1Mu_CSCTF_index]
              CSCTF_z2 = treeHits.CSCTF_z2[L1Mu_CSCTF_index]
              CSCTF_z3 = treeHits.CSCTF_z3[L1Mu_CSCTF_index]
              CSCTF_z4 = treeHits.CSCTF_z4[L1Mu_CSCTF_index]

              CSCTF_x1 = treeHits.CSCTF_x1[L1Mu_CSCTF_index]
              CSCTF_x2 = treeHits.CSCTF_x2[L1Mu_CSCTF_index]
              CSCTF_x3 = treeHits.CSCTF_x3[L1Mu_CSCTF_index]
              CSCTF_x4 = treeHits.CSCTF_x4[L1Mu_CSCTF_index]

              CSCTF_y1 = treeHits.CSCTF_y1[L1Mu_CSCTF_index]
              CSCTF_y2 = treeHits.CSCTF_y2[L1Mu_CSCTF_index]
              CSCTF_y3 = treeHits.CSCTF_y3[L1Mu_CSCTF_index]
              CSCTF_y4 = treeHits.CSCTF_y4[L1Mu_CSCTF_index]

              CSCTF_R1 = treeHits.CSCTF_R1[L1Mu_CSCTF_index]
              CSCTF_R2 = treeHits.CSCTF_R2[L1Mu_CSCTF_index]
              CSCTF_R3 = treeHits.CSCTF_R3[L1Mu_CSCTF_index]
              CSCTF_R4 = treeHits.CSCTF_R4[L1Mu_CSCTF_index]

              ## get SIM index
              GEN_SIM_index = int(treeHits.genGdMu_SIM_index[ij])

              if GEN_SIM_index != -99:
                CSCTF_rec_ch1 = treeHits.CSCTF_rec_ch1[GEN_SIM_index]
                CSCTF_rec_ch2 = treeHits.CSCTF_rec_ch1[GEN_SIM_index]
                CSCTF_rec_ch3 = treeHits.CSCTF_rec_ch3[GEN_SIM_index]
                CSCTF_rec_ch4 = treeHits.CSCTF_rec_ch4[GEN_SIM_index]

                CSCTF_rec_phi1 = treeHits.CSCTF_rec_phi1[GEN_SIM_index]
                CSCTF_rec_phi2 = treeHits.CSCTF_rec_phi2[GEN_SIM_index]
                CSCTF_rec_phi3 = treeHits.CSCTF_rec_phi3[GEN_SIM_index]
                CSCTF_rec_phi4 = treeHits.CSCTF_rec_phi4[GEN_SIM_index]

                CSCTF_rec_phib1 = treeHits.CSCTF_rec_phib1[GEN_SIM_index]
                CSCTF_rec_phib2 = treeHits.CSCTF_rec_phib2[GEN_SIM_index]
                CSCTF_rec_phib3 = treeHits.CSCTF_rec_phib3[GEN_SIM_index]
                CSCTF_rec_phib4 = treeHits.CSCTF_rec_phib4[GEN_SIM_index]

                CSCTF_rec_z1 = treeHits.CSCTF_rec_z1[GEN_SIM_index]
                CSCTF_rec_z2 = treeHits.CSCTF_rec_z2[GEN_SIM_index]
                CSCTF_rec_z3 = treeHits.CSCTF_rec_z3[GEN_SIM_index]
                CSCTF_rec_z4 = treeHits.CSCTF_rec_z4[GEN_SIM_index]

                CSCTF_rec_x1 = treeHits.CSCTF_rec_x1[GEN_SIM_index]
                CSCTF_rec_x2 = treeHits.CSCTF_rec_x2[GEN_SIM_index]
                CSCTF_rec_x3 = treeHits.CSCTF_rec_x3[GEN_SIM_index]
                CSCTF_rec_x4 = treeHits.CSCTF_rec_x4[GEN_SIM_index]

                CSCTF_rec_y1 = treeHits.CSCTF_rec_y1[GEN_SIM_index]
                CSCTF_rec_y2 = treeHits.CSCTF_rec_y2[GEN_SIM_index]
                CSCTF_rec_y3 = treeHits.CSCTF_rec_y3[GEN_SIM_index]
                CSCTF_rec_y4 = treeHits.CSCTF_rec_y4[GEN_SIM_index]

                CSCTF_rec_R1 = treeHits.CSCTF_rec_R1[GEN_SIM_index]
                CSCTF_rec_R2 = treeHits.CSCTF_rec_R2[GEN_SIM_index]
                CSCTF_rec_R3 = treeHits.CSCTF_rec_R3[GEN_SIM_index]
                CSCTF_rec_R4 = treeHits.CSCTF_rec_R4[GEN_SIM_index]

                ## simulated and fitted positions in a chamber
                CSCTF_sim_phi1 = treeHits.CSCTF_sim_phi1[GEN_SIM_index]
                CSCTF_sim_phi2 = treeHits.CSCTF_sim_phi2[GEN_SIM_index]
                CSCTF_sim_phi3 = treeHits.CSCTF_sim_phi3[GEN_SIM_index]
                CSCTF_sim_phi4 = treeHits.CSCTF_sim_phi4[GEN_SIM_index]

                CSCTF_fit_phi1 = treeHits.CSCTF_fit_phi1[GEN_SIM_index]
                CSCTF_fit_phi2 = treeHits.CSCTF_fit_phi2[GEN_SIM_index]
                CSCTF_fit_phi3 = treeHits.CSCTF_fit_phi3[GEN_SIM_index]
                CSCTF_fit_phi4 = treeHits.CSCTF_fit_phi4[GEN_SIM_index]

                CSCTF_fit_x1 = treeHits.CSCTF_fit_x1[GEN_SIM_index]
                CSCTF_fit_x2 = treeHits.CSCTF_fit_x2[GEN_SIM_index]
                CSCTF_fit_x3 = treeHits.CSCTF_fit_x3[GEN_SIM_index]
                CSCTF_fit_x4 = treeHits.CSCTF_fit_x4[GEN_SIM_index]

                CSCTF_fit_y1 = treeHits.CSCTF_fit_y1[GEN_SIM_index]
                CSCTF_fit_y2 = treeHits.CSCTF_fit_y2[GEN_SIM_index]
                CSCTF_fit_y3 = treeHits.CSCTF_fit_y3[GEN_SIM_index]
                CSCTF_fit_y4 = treeHits.CSCTF_fit_y4[GEN_SIM_index]

                CSCTF_fit_z1 = treeHits.CSCTF_fit_z1[GEN_SIM_index]
                CSCTF_fit_z2 = treeHits.CSCTF_fit_z2[GEN_SIM_index]
                CSCTF_fit_z3 = treeHits.CSCTF_fit_z3[GEN_SIM_index]
                CSCTF_fit_z4 = treeHits.CSCTF_fit_z4[GEN_SIM_index]

                CSCTF_fit_R1 = treeHits.CSCTF_fit_R1[GEN_SIM_index]
                CSCTF_fit_R2 = treeHits.CSCTF_fit_R2[GEN_SIM_index]
                CSCTF_fit_R3 = treeHits.CSCTF_fit_R3[GEN_SIM_index]
                CSCTF_fit_R4 = treeHits.CSCTF_fit_R4[GEN_SIM_index]

                ## check if the recovered stations are there
                ok_CSCTF_rec_st1 = CSCTF_rec_phi1 != 99
                ok_CSCTF_rec_st2 = CSCTF_rec_phi2 != 99
                ok_CSCTF_rec_st3 = CSCTF_rec_phi3 != 99
                ok_CSCTF_rec_st4 = CSCTF_rec_phi4 != 99

                ## recovered stub positions and directions
                if ok_CSCTF_rec_st1: CSCTF_rec_phi1 = normalizedPhi2(CSCTF_rec_phi1)
                if ok_CSCTF_rec_st2: CSCTF_rec_phi2 = normalizedPhi2(CSCTF_rec_phi2)
                if ok_CSCTF_rec_st3: CSCTF_rec_phi3 = normalizedPhi2(CSCTF_rec_phi3)
                if ok_CSCTF_rec_st4: CSCTF_rec_phi4 = normalizedPhi2(CSCTF_rec_phi4)

                if ok_CSCTF_rec_st1: CSCTF_rec_phib1 = normalizedPhi2(CSCTF_rec_phib1)
                if ok_CSCTF_rec_st2: CSCTF_rec_phib2 = normalizedPhi2(CSCTF_rec_phib2)
                if ok_CSCTF_rec_st3: CSCTF_rec_phib3 = normalizedPhi2(CSCTF_rec_phib3)
                if ok_CSCTF_rec_st4: CSCTF_rec_phib4 = normalizedPhi2(CSCTF_rec_phib4)

                ## in case the CSC stub was not found in the CSCTF track, check if it can be recovered
                ## this is done by matching the SIM muon to the CSC stubs
                if not ok_CSCTF_st1 and ok_CSCTF_rec_st1: 
                  CSCTF_phi1 = CSCTF_rec_phi1
                  CSCTF_z1 = CSCTF_rec_z1 
                  CSCTF_x1 = CSCTF_rec_x1 
                  CSCTF_y1 = CSCTF_rec_y1 
                  CSCTF_R1 = CSCTF_rec_R1 
                  CSCTF_ch1 = CSCTF_rec_ch1
                  CSCTF_isOdd1 = CSCTF_ch1%2==1
                  CSCTF_isEven1 = not CSCTF_isOdd1
                if not ok_CSCTF_st2 and ok_CSCTF_rec_st2: 
                  CSCTF_phi2 = CSCTF_rec_phi2
                  CSCTF_z2 = CSCTF_rec_z2 
                  CSCTF_x2 = CSCTF_rec_x2 
                  CSCTF_y2 = CSCTF_rec_y2 
                  CSCTF_R2 = CSCTF_rec_R2 
                  CSCTF_ch2 = CSCTF_rec_ch2
                  CSCTF_isOdd2 = CSCTF_ch2%2==1
                  CSCTF_isEven2 = not CSCTF_isOdd2
                if not ok_CSCTF_st3 and ok_CSCTF_rec_st3: 
                  CSCTF_phi3 = CSCTF_rec_phi3
                  CSCTF_z3 = CSCTF_rec_z3 
                  CSCTF_x3 = CSCTF_rec_x3 
                  CSCTF_y3 = CSCTF_rec_y3 
                  CSCTF_R3 = CSCTF_rec_R3 
                  CSCTF_ch3 = CSCTF_rec_ch3
                  CSCTF_isOdd3 = CSCTF_ch3%2==1
                  CSCTF_isEven3 = not CSCTF_isOdd3
                if not ok_CSCTF_st4 and ok_CSCTF_rec_st4: 
                  CSCTF_phi4 = CSCTF_rec_phi4
                  CSCTF_z4 = CSCTF_rec_z4 
                  CSCTF_x4 = CSCTF_rec_x4 
                  CSCTF_y4 = CSCTF_rec_y4 
                  CSCTF_R4 = CSCTF_rec_R4 
                  CSCTF_ch4 = CSCTF_rec_ch4
                  CSCTF_isOdd4 = CSCTF_ch4%2==1
                  CSCTF_isEven4 = not CSCTF_isOdd4
                  
                ## plot with position resolution of the CSC stubs
                if (1.6 < abs(eta_prop) and abs(eta_prop) <= 1.8):
                  if (CSCTF_phi1!=99 and CSCTF_sim_phi1 != 99):     mapTH1F["csc_pos_sh_lct_ME1b_16to18"].Fill(CSCTF_phi1 - CSCTF_sim_phi1)
                  if (CSCTF_phi2!=99 and CSCTF_sim_phi2 != 99):     mapTH1F["csc_pos_sh_lct_ME21_16to18"].Fill(CSCTF_phi2 - CSCTF_sim_phi2)
                  if (CSCTF_fit_phi1!=99 and CSCTF_sim_phi1 != 99): mapTH1F["csc_pos_sh_fit_ME1b_16to18"].Fill(CSCTF_fit_phi1 - CSCTF_sim_phi1)
                  if (CSCTF_fit_phi2!=99 and CSCTF_sim_phi2 != 99): mapTH1F["csc_pos_sh_fit_ME21_16to18"].Fill(CSCTF_fit_phi2 - CSCTF_sim_phi2)
                if (1.8 < abs(eta_prop) and abs(eta_prop) <= 2.0):
                  if (CSCTF_phi1!=99 and CSCTF_sim_phi1 != 99):     mapTH1F["csc_pos_sh_lct_ME1b_18to20"].Fill(CSCTF_phi1 - CSCTF_sim_phi1)
                  if (CSCTF_phi2!=99 and CSCTF_sim_phi2 != 99):     mapTH1F["csc_pos_sh_lct_ME21_18to20"].Fill(CSCTF_phi2 - CSCTF_sim_phi2)
                  if (CSCTF_fit_phi1!=99 and CSCTF_sim_phi1 != 99): mapTH1F["csc_pos_sh_fit_ME1b_18to20"].Fill(CSCTF_fit_phi1 - CSCTF_sim_phi1)
                  if (CSCTF_fit_phi2!=99 and CSCTF_sim_phi2 != 99): mapTH1F["csc_pos_sh_fit_ME21_18to20"].Fill(CSCTF_fit_phi2 - CSCTF_sim_phi2)
                if (2.0 < abs(eta_prop) and abs(eta_prop) <= 2.2):
                  if (CSCTF_phi1!=99 and CSCTF_sim_phi1 != 99):     mapTH1F["csc_pos_sh_lct_ME1b_20to22"].Fill(CSCTF_phi1 - CSCTF_sim_phi1)
                  if (CSCTF_phi2!=99 and CSCTF_sim_phi2 != 99):     mapTH1F["csc_pos_sh_lct_ME21_20to22"].Fill(CSCTF_phi2 - CSCTF_sim_phi2)
                  if (CSCTF_fit_phi1!=99 and CSCTF_sim_phi1 != 99): mapTH1F["csc_pos_sh_fit_ME1b_20to22"].Fill(CSCTF_fit_phi1 - CSCTF_sim_phi1)
                  if (CSCTF_fit_phi2!=99 and CSCTF_sim_phi2 != 99): mapTH1F["csc_pos_sh_fit_ME21_20to22"].Fill(CSCTF_fit_phi2 - CSCTF_sim_phi2)
                  
                ## split up resolution in even/odd
                if not CSCTF_isOdd1:
                  if (CSCTF_phi1!=99 and CSCTF_sim_phi1 != 99):
                    if (1.6 < abs(eta_prop) and abs(eta_prop) <= 1.8):
                      csc_pos_sh_lct_ME1b_16to18_even.Fill(CSCTF_phi1 - CSCTF_sim_phi1)
                      csc_pos_sh_vs_lct_ME1b_16to18_even.Fill(CSCTF_phi1,CSCTF_sim_phi1)
                    if (1.8 < abs(eta_prop) and abs(eta_prop) <= 2.0): 
                      csc_pos_sh_lct_ME1b_18to20_even.Fill(CSCTF_phi1 - CSCTF_sim_phi1)
                      csc_pos_sh_vs_lct_ME1b_18to20_even.Fill(CSCTF_phi1,CSCTF_sim_phi1)
                    if (2.0 < abs(eta_prop) and abs(eta_prop) <= 2.2): 
                      csc_pos_sh_lct_ME1b_20to22_even.Fill(CSCTF_phi1 - CSCTF_sim_phi1)
                      csc_pos_sh_vs_lct_ME1b_20to22_even.Fill(CSCTF_phi1,CSCTF_sim_phi1)
                  if (CSCTF_fit_phi1!=99 and CSCTF_sim_phi1 != 99):
                    if (1.6 < abs(eta_prop) and abs(eta_prop) <= 1.8): 
                      csc_pos_sh_fit_ME1b_16to18_even.Fill(CSCTF_fit_phi1 - CSCTF_sim_phi1)
                      csc_pos_sh_vs_fit_ME1b_16to18_even.Fill(CSCTF_fit_phi1,CSCTF_sim_phi1)
                    if (1.8 < abs(eta_prop) and abs(eta_prop) <= 2.0): 
                      csc_pos_sh_fit_ME1b_18to20_even.Fill(CSCTF_fit_phi1 - CSCTF_sim_phi1)
                      csc_pos_sh_vs_fit_ME1b_18to20_even.Fill(CSCTF_fit_phi1,CSCTF_sim_phi1)
                    if (2.0 < abs(eta_prop) and abs(eta_prop) <= 2.2): 
                      csc_pos_sh_fit_ME1b_20to22_even.Fill(CSCTF_fit_phi1 - CSCTF_sim_phi1)
                      csc_pos_sh_vs_fit_ME1b_20to22_even.Fill(CSCTF_fit_phi1,CSCTF_sim_phi1)

                else:
                  if (CSCTF_phi1!=99 and CSCTF_sim_phi1 != 99):
                    if (1.6 < abs(eta_prop) and abs(eta_prop) <= 1.8):
                      csc_pos_sh_lct_ME1b_16to18_odd.Fill(CSCTF_phi1 - CSCTF_sim_phi1)
                      csc_pos_sh_vs_lct_ME1b_16to18_odd.Fill(CSCTF_phi1,CSCTF_sim_phi1)
                    if (1.8 < abs(eta_prop) and abs(eta_prop) <= 2.0):
                      csc_pos_sh_lct_ME1b_18to20_odd.Fill(CSCTF_phi1 - CSCTF_sim_phi1)
                      csc_pos_sh_vs_lct_ME1b_18to20_odd.Fill(CSCTF_phi1,CSCTF_sim_phi1)
                    if (2.0 < abs(eta_prop) and abs(eta_prop) <= 2.2):
                      csc_pos_sh_lct_ME1b_20to22_odd.Fill(CSCTF_phi1 - CSCTF_sim_phi1)
                      csc_pos_sh_vs_lct_ME1b_20to22_odd.Fill(CSCTF_phi1,CSCTF_sim_phi1)
                  if (CSCTF_fit_phi1!=99 and CSCTF_sim_phi1 != 99):
                    if (1.6 < abs(eta_prop) and abs(eta_prop) <= 1.8): 
                      csc_pos_sh_fit_ME1b_16to18_odd.Fill(CSCTF_fit_phi1 - CSCTF_sim_phi1)
                      csc_pos_sh_vs_fit_ME1b_16to18_odd.Fill(CSCTF_fit_phi1,CSCTF_sim_phi1)
                    if (1.8 < abs(eta_prop) and abs(eta_prop) <= 2.0): 
                      csc_pos_sh_fit_ME1b_18to20_odd.Fill(CSCTF_fit_phi1 - CSCTF_sim_phi1)
                      csc_pos_sh_vs_fit_ME1b_18to20_odd.Fill(CSCTF_fit_phi1,CSCTF_sim_phi1)
                    if (2.0 < abs(eta_prop) and abs(eta_prop) <= 2.2): 
                      csc_pos_sh_fit_ME1b_20to22_odd.Fill(CSCTF_fit_phi1 - CSCTF_sim_phi1)
                      csc_pos_sh_vs_fit_ME1b_20to22_odd.Fill(CSCTF_fit_phi1,CSCTF_sim_phi1)

                if not CSCTF_isOdd2:
                  if (CSCTF_phi2!=99 and CSCTF_sim_phi2 != 99):
                    if (1.6 < abs(eta_prop) and abs(eta_prop) <= 1.8):
                      csc_pos_sh_lct_ME21_16to18_even.Fill(CSCTF_phi2 - CSCTF_sim_phi2)
                      csc_pos_sh_vs_lct_ME21_16to18_even.Fill(CSCTF_phi2,CSCTF_sim_phi2)
                    if (1.8 < abs(eta_prop) and abs(eta_prop) <= 2.0): 
                      csc_pos_sh_lct_ME21_18to20_even.Fill(CSCTF_phi2 - CSCTF_sim_phi2)
                      csc_pos_sh_vs_lct_ME21_18to20_even.Fill(CSCTF_phi2,CSCTF_sim_phi2)
                    if (2.0 < abs(eta_prop) and abs(eta_prop) <= 2.2): 
                      csc_pos_sh_lct_ME21_20to22_even.Fill(CSCTF_phi2 - CSCTF_sim_phi2)
                      csc_pos_sh_vs_lct_ME21_20to22_even.Fill(CSCTF_phi2,CSCTF_sim_phi2)
                  if (CSCTF_fit_phi2!=99 and CSCTF_sim_phi2 != 99):
                    if (1.6 < abs(eta_prop) and abs(eta_prop) <= 1.8): 
                      csc_pos_sh_fit_ME21_16to18_even.Fill(CSCTF_fit_phi2 - CSCTF_sim_phi2)
                      csc_pos_sh_vs_fit_ME21_16to18_even.Fill(CSCTF_fit_phi2,CSCTF_sim_phi2)
                    if (1.8 < abs(eta_prop) and abs(eta_prop) <= 2.0): 
                      csc_pos_sh_fit_ME21_18to20_even.Fill(CSCTF_fit_phi2 - CSCTF_sim_phi2)
                      csc_pos_sh_vs_fit_ME21_18to20_even.Fill(CSCTF_fit_phi2,CSCTF_sim_phi2)
                    if (2.0 < abs(eta_prop) and abs(eta_prop) <= 2.2): 
                      csc_pos_sh_fit_ME21_20to22_even.Fill(CSCTF_fit_phi2 - CSCTF_sim_phi2)
                      csc_pos_sh_vs_fit_ME21_20to22_even.Fill(CSCTF_fit_phi2,CSCTF_sim_phi2)

                else:
                  if (CSCTF_phi2!=99 and CSCTF_sim_phi2 != 99):
                    if (1.6 < abs(eta_prop) and abs(eta_prop) <= 1.8):
                      csc_pos_sh_lct_ME21_16to18_odd.Fill(CSCTF_phi2 - CSCTF_sim_phi2)
                      csc_pos_sh_vs_lct_ME21_16to18_odd.Fill(CSCTF_phi2,CSCTF_sim_phi2)
                    if (1.8 < abs(eta_prop) and abs(eta_prop) <= 2.0):
                      csc_pos_sh_lct_ME21_18to20_odd.Fill(CSCTF_phi2 - CSCTF_sim_phi2)
                      csc_pos_sh_vs_lct_ME21_18to20_odd.Fill(CSCTF_phi2,CSCTF_sim_phi2)
                    if (2.0 < abs(eta_prop) and abs(eta_prop) <= 2.2):
                      csc_pos_sh_lct_ME21_20to22_odd.Fill(CSCTF_phi2 - CSCTF_sim_phi2)
                      csc_pos_sh_vs_lct_ME21_20to22_odd.Fill(CSCTF_phi2,CSCTF_sim_phi2)
                  if (CSCTF_fit_phi2!=99 and CSCTF_sim_phi2 != 99):
                    if (1.6 < abs(eta_prop) and abs(eta_prop) <= 1.8): 
                      csc_pos_sh_fit_ME21_16to18_odd.Fill(CSCTF_fit_phi2 - CSCTF_sim_phi2)
                      csc_pos_sh_vs_fit_ME21_16to18_odd.Fill(CSCTF_fit_phi2,CSCTF_sim_phi2)
                    if (1.8 < abs(eta_prop) and abs(eta_prop) <= 2.0): 
                      csc_pos_sh_fit_ME21_18to20_odd.Fill(CSCTF_fit_phi2 - CSCTF_sim_phi2)
                      csc_pos_sh_vs_fit_ME21_18to20_odd.Fill(CSCTF_fit_phi2,CSCTF_sim_phi2)
                    if (2.0 < abs(eta_prop) and abs(eta_prop) <= 2.2): 
                      csc_pos_sh_fit_ME21_20to22_odd.Fill(CSCTF_fit_phi2 - CSCTF_sim_phi2)
                      csc_pos_sh_vs_fit_ME21_20to22_odd.Fill(CSCTF_fit_phi2,CSCTF_sim_phi2)
                      

                ## GEM variables
                GE11_bx_L1 = treeHits.GE11_bx_L1[GEN_SIM_index]
                GE11_bx_L2 = treeHits.GE11_bx_L2[GEN_SIM_index]
                GE21_bx_L1 = treeHits.GE21_bx_L1[GEN_SIM_index]
                GE21_bx_L2 = treeHits.GE21_bx_L2[GEN_SIM_index]
                GE11_phi_L1 = treeHits.GE11_phi_L1[GEN_SIM_index]
                GE11_phi_L2 = treeHits.GE11_phi_L2[GEN_SIM_index]
                GE21_phi_L1 = treeHits.GE21_phi_L1[GEN_SIM_index]
                GE21_phi_L2 = treeHits.GE21_phi_L2[GEN_SIM_index]
                GE11_z_L1 = treeHits.GE11_z_L1[GEN_SIM_index]
                GE11_z_L2 = treeHits.GE11_z_L2[GEN_SIM_index]
                GE21_z_L1 = treeHits.GE21_z_L1[GEN_SIM_index]
                GE21_z_L2 = treeHits.GE21_z_L2[GEN_SIM_index]
                GE11_ch1 = treeHits.GE11_ch_L1[GEN_SIM_index]
                GE21_ch2 = treeHits.GE21_ch_L1[GEN_SIM_index]
                GE11_isOdd = GE11_ch1%2==1
                GE21_isOdd = GE21_ch2%2==1
                GE0_phi = treeHits.GE0_phi[GEN_SIM_index]
                GE0_phib = treeHits.GE0_phib[GEN_SIM_index]

                GE11_sim_bx_L1 = treeHits.GE11_sim_bx_L1[GEN_SIM_index]
                GE11_sim_bx_L2 = treeHits.GE11_sim_bx_L2[GEN_SIM_index]
                GE21_sim_bx_L1 = treeHits.GE21_sim_bx_L1[GEN_SIM_index]
                GE21_sim_bx_L2 = treeHits.GE21_sim_bx_L2[GEN_SIM_index]
                GE11_sim_phi_L1 = treeHits.GE11_sim_phi_L1[GEN_SIM_index]
                GE11_sim_phi_L2 = treeHits.GE11_sim_phi_L2[GEN_SIM_index]
                GE21_sim_phi_L1 = treeHits.GE21_sim_phi_L1[GEN_SIM_index]
                GE21_sim_phi_L2 = treeHits.GE21_sim_phi_L2[GEN_SIM_index]
                GE11_sim_z_L1 = treeHits.GE11_sim_z_L1[GEN_SIM_index]
                GE11_sim_z_L2 = treeHits.GE11_sim_z_L2[GEN_SIM_index]
                GE21_sim_z_L1 = treeHits.GE21_sim_z_L1[GEN_SIM_index]
                GE21_sim_z_L2 = treeHits.GE21_sim_z_L2[GEN_SIM_index]
                GE11_sim_ch1 = treeHits.GE11_sim_ch_L1[GEN_SIM_index]
                GE21_sim_ch2 = treeHits.GE21_sim_ch_L1[GEN_SIM_index]
                GE11_sim_isOdd = GE11_sim_ch1%2==1
                GE21_sim_isOdd = GE21_sim_ch2%2==1
                GE0_sim_phi = treeHits.GE0_sim_phi[GEN_SIM_index]
                GE0_sim_phib = treeHits.GE0_sim_phib[GEN_SIM_index]


                ## GEM pad positions
                GE21_pad1_phi_L1 = treeHits.GE21_pad1_phi_L1[GEN_SIM_index] 
                GE21_pad1_phi_L2 = treeHits.GE21_pad1_phi_L2[GEN_SIM_index]
                GE21_pad2_phi_L1 = treeHits.GE21_pad2_phi_L1[GEN_SIM_index] 
                GE21_pad2_phi_L2 = treeHits.GE21_pad2_phi_L2[GEN_SIM_index]
                GE21_pad4_phi_L1 = treeHits.GE21_pad4_phi_L1[GEN_SIM_index] 
                GE21_pad4_phi_L2 = treeHits.GE21_pad4_phi_L2[GEN_SIM_index]
                GE21_pad8_phi_L1 = treeHits.GE21_pad8_phi_L1[GEN_SIM_index] 
                GE21_pad8_phi_L2 = treeHits.GE21_pad8_phi_L2[GEN_SIM_index]


                ## normalize the GEM position angles
                if GE11_phi_L1 != 99: GE11_phi_L1 = normalizedPhi2(GE11_phi_L1)
                if GE11_phi_L2 != 99: GE11_phi_L2 = normalizedPhi2(GE11_phi_L2)
                if GE21_phi_L1 != 99: GE21_phi_L1 = normalizedPhi2(GE21_phi_L1)
                if GE21_phi_L2 != 99: GE21_phi_L2 = normalizedPhi2(GE21_phi_L2)
                if GE0_phi != 99: GE0_phi = normalizedPhi(GE21_phi_L2)


              ## check if GEM hits are present
              ok_GE11_L1 = GE11_bx_L1 != 99 
              ok_GE11_L2 = GE11_bx_L2 != 99 
              ok_GE21_L1 = GE21_bx_L1 != 99 
              ok_GE21_L2 = GE21_bx_L2 != 99

              ok_GE0 = GE0_phi != 99
              ok_GE11 = ok_GE11_L1 or ok_GE11_L2
              ok_GE21 = ok_GE21_L1 or ok_GE21_L2

              ## L1MU counters
              if ok_GE11 and ok_GE21:             nL1MuMatched_GE11_GE21 += 1
              if ok_GE0 and ok_GE21:              nL1MuMatched_GE0_GE21 += 1
              if (ok_GE0 or ok_GE11) and ok_GE21: nL1MuMatched_GE11_GE0_GE21 += 1

              ## check if CSC hits are present
              ok_CSCTF_st1 = ok_CSCTF_st1 or ok_CSCTF_rec_st1
              ok_CSCTF_st2 = ok_CSCTF_st2 or ok_CSCTF_rec_st2
              ok_CSCTF_st3 = ok_CSCTF_st3 or ok_CSCTF_rec_st3
              ok_CSCTF_st4 = ok_CSCTF_st4 or ok_CSCTF_rec_st4

              if verbose:
                print "\t\tCSCTF", L1Mu_CSCTF_index
                print "\t\tCSCTF_pt", CSCTF_pt
                print "\t\tCSCTF_eta", CSCTF_eta
                print "\t\tCSCTF_phi", CSCTF_phi
                print "\t\tCSCTF_bx", CSCTF_bx
                print "\t\tCSCTF_nStubs", CSCTF_nStubs
                print "\t\tCSCTF_phi1", CSCTF_phi1 
                print "\t\tCSCTF_phi2", CSCTF_phi2
                print "\t\tCSCTF_phi3", CSCTF_phi3
                print "\t\tCSCTF_phi4", CSCTF_phi4
                print "\t\tCSCTF_ch1", CSCTF_ch1 
                print "\t\tCSCTF_ch2", CSCTF_ch2
                print "\t\tCSCTF_ch3", CSCTF_ch3 
                print "\t\tCSCTF_ch4", CSCTF_ch4
                print "\t\tCSCTF_z1", CSCTF_z1 
                print "\t\tCSCTF_z2", CSCTF_z2

                print "\t\tCSCTF_gemdphi1", CSCTF_gemdphi1
                print "\t\tCSCTF_gemdphi2", CSCTF_gemdphi2
                print "\t\tGEN_SIM_index", GEN_SIM_index
                print "\t\tCSCTF_rec_ch1", CSCTF_rec_ch1
                print "\t\tCSCTF_rec_ch2", CSCTF_rec_ch2
                print "\t\tCSCTF_rec_phi1", CSCTF_rec_phi1 
                print "\t\tCSCTF_rec_phi2", CSCTF_rec_phi2
                print "\t\tCSCTF_rec_phib1", CSCTF_rec_phib1 
                print "\t\tCSCTF_rec_phib2", CSCTF_rec_phib2
                print "\t\tGE11_ch1", GE11_ch1 
                print "\t\tGE21_ch2", GE21_ch2
                print "\t\tok_GE11_L1", ok_GE11_L1, "GE11_phi_L1", GE11_phi_L1, "GE11_bx_L1", GE11_bx_L1, "GE11_z_L1", GE11_z_L1
                print "\t\tok_GE11_L2", ok_GE11_L2, "GE11_phi_L2", GE11_phi_L2, "GE11_bx_L2", GE11_bx_L2, "GE11_z_L2", GE11_z_L2
                print "\t\tok_GE21_L1", ok_GE21_L1, "GE21_phi_L1", GE21_phi_L1, "GE21_bx_L1", GE21_bx_L1, "GE21_z_L1", GE21_z_L1
                print "\t\tok_GE21_L2", ok_GE21_L2, "GE21_phi_L2", GE21_phi_L2, "GE21_bx_L2", GE21_bx_L2, "GE21_z_L2", GE21_z_L2
                print "\t\tok_GE0", ok_GE0, "GE0_phi", GE0_phi, "GE0_phib", GE0_phib
                print               

              ## stub directions
              ok_direction_based_endcap = ok_GE11 and ok_GE21 and ok_CSCTF_st1 and ok_CSCTF_st2

              ## all necessary elements for the bending angle algorithm are present!
              if ok_direction_based_endcap and abs(eta_prop)>=1.6 and abs(eta_prop)<=2.2:
                nL1MuMatched_GE11_ME11_GE21_ME21 += 1

                ## denominators for efficiency plots
                if dxy <= 100:              mapTH1F["GenMuPt_GE11_ME11_GE21_ME21"].Fill(pt)               
                if dxy <= 5:                mapTH1F["GenMuPt_GE11_ME11_GE21_ME21_dxy0to5"].Fill(pt)               
                if 5 < dxy  and dxy <= 50:  mapTH1F["GenMuPt_GE11_ME11_GE21_ME21_dxy5to50"].Fill(pt)  
                if 50 < dxy and dxy <= 100: mapTH1F["GenMuPt_GE11_ME11_GE21_ME21_dxy50to100"].Fill(pt)

                def getBestValue(value1, value2):
                  if value1 != 99: return value1
                  else:            return value2

                ## get GEM phi positions...
                GE11_phi = getBestValue(GE11_phi_L1, GE11_phi_L2)
                GE21_phi = getBestValue(GE21_phi_L1, GE21_phi_L2)
                GE21_pad1_phi = getBestValue(GE21_pad1_phi_L1, GE21_pad1_phi_L2)
                GE21_pad2_phi = getBestValue(GE21_pad2_phi_L1, GE21_pad2_phi_L2)
                GE21_pad4_phi = getBestValue(GE21_pad4_phi_L1, GE21_pad4_phi_L2)
                GE21_pad8_phi = getBestValue(GE21_pad8_phi_L1, GE21_pad8_phi_L2)

                ## get GEM z positions...
                GE11_z = getBestValue(GE11_z_L1, GE11_z_L2)
                GE21_z = getBestValue(GE21_z_L1, GE21_z_L2)

                if verbose:
                  print "\t\tCSCTF_z1", CSCTF_z1
                  print "\t\tCSCTF_z2", CSCTF_z2
                  print "\t\tCSCTF_R1", CSCTF_R1
                  print "\t\tCSCTF_R2", CSCTF_R2
                  print "\t\tCSCTF_fit_R1", CSCTF_fit_R1
                  print "\t\tCSCTF_fit_R2", CSCTF_fit_R2
                  print "\t\tGEM_z1", GE11_z
                  print "\t\tGEM_z2", GE21_z
                
                ## these variable do not depend on the thickness of a pad or the LCT position fit
                delta_z_GE11_ME11 = abs(CSCTF_z1 - GE11_z)
                delta_z_GE21_ME21 = abs(CSCTF_z2 - GE21_z)
                delta_z_ME11_ME21 = abs(CSCTF_z1 - CSCTF_z2)

                ## calculate X values - depend on the LCT position fit
                X_withoutLCTFit = (CSCTF_R2/CSCTF_R1 - 1)/delta_z_ME11_ME21
                X_withLCTFit = (CSCTF_R2/CSCTF_R1 - 1)/delta_z_ME11_ME21

                ## calculate the bending in each station
                def phi_dir_st1_variable_GE21_pad_size(me11_phi, ge11_phi, Xvalue):
                  numerator = TMath.Sin( deltaPhi2(me11_phi, ge11_phi) )
                  denominator = 1. - TMath.Cos( deltaPhi2(me11_phi, ge11_phi) ) - delta_z_GE11_ME11 * Xvalue
                  return ge11_phi - TMath.ATan( numerator / denominator)

                def phi_dir_st2_variable_GE21_pad_size(me11_phi, me21_phi, ge21_phi, Xvalue):
                  numerator = TMath.Sin( deltaPhi2(me21_phi, ge21_phi) )
                  denominator = 1 - TMath.Cos( deltaPhi2(me21_phi, ge21_phi) ) - (delta_z_GE21_ME21 * Xvalue / (delta_z_ME11_ME21 * Xvalue + 1 ) )
                  return ge21_phi - TMath.ATan( numerator / denominator )


                ## bending in station 1,2 for different pad sizes and different LCT position resolutions
                phi_dir_st1_withoutLCTFit = phi_dir_st1_variable_GE21_pad_size(CSCTF_phi1, GE11_phi, X_withoutLCTFit)
                phi_dir_st1_withLCTFit = phi_dir_st1_variable_GE21_pad_size(CSCTF_fit_phi1, GE11_phi, X_withLCTFit)

                phi_dir_st2_GE21_pad1_withoutLCTFit = phi_dir_st2_variable_GE21_pad_size(CSCTF_phi1, CSCTF_phi2, GE21_pad1_phi, X_withoutLCTFit)
                phi_dir_st2_GE21_pad2_withoutLCTFit = phi_dir_st2_variable_GE21_pad_size(CSCTF_phi1, CSCTF_phi2, GE21_pad2_phi, X_withoutLCTFit)
                phi_dir_st2_GE21_pad4_withoutLCTFit = phi_dir_st2_variable_GE21_pad_size(CSCTF_phi1, CSCTF_phi2, GE21_pad4_phi, X_withoutLCTFit)
                phi_dir_st2_GE21_pad8_withoutLCTFit = phi_dir_st2_variable_GE21_pad_size(CSCTF_phi1, CSCTF_phi2, GE21_pad8_phi, X_withoutLCTFit)

                phi_dir_st2_GE21_pad1_withLCTFit = phi_dir_st2_variable_GE21_pad_size(CSCTF_fit_phi1, CSCTF_fit_phi2, GE21_pad1_phi, X_withLCTFit)
                phi_dir_st2_GE21_pad2_withLCTFit = phi_dir_st2_variable_GE21_pad_size(CSCTF_fit_phi1, CSCTF_fit_phi2, GE21_pad2_phi, X_withLCTFit)
                phi_dir_st2_GE21_pad4_withLCTFit = phi_dir_st2_variable_GE21_pad_size(CSCTF_fit_phi1, CSCTF_fit_phi2, GE21_pad4_phi, X_withLCTFit)
                phi_dir_st2_GE21_pad8_withLCTFit = phi_dir_st2_variable_GE21_pad_size(CSCTF_fit_phi1, CSCTF_fit_phi2, GE21_pad8_phi, X_withLCTFit)


                ## difference in bending for different pad sizes and different LCT position resolutions
                delta_phi_dir_GE21_pad1_withoutLCTFit = abs( deltaPhi2( phi_dir_st1_withoutLCTFit, phi_dir_st2_GE21_pad1_withoutLCTFit) )
                delta_phi_dir_GE21_pad2_withoutLCTFit = abs( deltaPhi2( phi_dir_st1_withoutLCTFit, phi_dir_st2_GE21_pad2_withoutLCTFit) )
                delta_phi_dir_GE21_pad4_withoutLCTFit = abs( deltaPhi2( phi_dir_st1_withoutLCTFit, phi_dir_st2_GE21_pad4_withoutLCTFit) )
                delta_phi_dir_GE21_pad8_withoutLCTFit = abs( deltaPhi2( phi_dir_st1_withoutLCTFit, phi_dir_st2_GE21_pad8_withoutLCTFit) )

                delta_phi_dir_GE21_pad1_withLCTFit = abs( deltaPhi2( phi_dir_st1_withoutLCTFit, phi_dir_st2_GE21_pad1_withLCTFit) )
                delta_phi_dir_GE21_pad2_withLCTFit = abs( deltaPhi2( phi_dir_st1_withoutLCTFit, phi_dir_st2_GE21_pad2_withLCTFit) )
                delta_phi_dir_GE21_pad4_withLCTFit = abs( deltaPhi2( phi_dir_st1_withoutLCTFit, phi_dir_st2_GE21_pad4_withLCTFit) )
                delta_phi_dir_GE21_pad8_withLCTFit = abs( deltaPhi2( phi_dir_st1_withoutLCTFit, phi_dir_st2_GE21_pad8_withLCTFit) )

                ## only fill the plots that apply!!
                parity = get_parity_ME11_ME21(CSCTF_isEven1, CSCTF_isEven2)
                etaPart = get_eta_partition_GE11(eta_prop)

                mapTH2F["GenMuPt_vs_abs_phiGEMst1_phiGEMst2_eta" + etaRangesGE11[etaPart] + "_" +  ME1ME2ParityCases[parity] + "_pad1_withoutLCTFit"].Fill(pt, delta_phi_dir_GE21_pad1_withoutLCTFit)
                mapTH2F["GenMuPt_vs_abs_phiGEMst1_phiGEMst2_eta" + etaRangesGE11[etaPart] + "_" +  ME1ME2ParityCases[parity] + "_pad2_withoutLCTFit"].Fill(pt, delta_phi_dir_GE21_pad2_withoutLCTFit)
                mapTH2F["GenMuPt_vs_abs_phiGEMst1_phiGEMst2_eta" + etaRangesGE11[etaPart] + "_" +  ME1ME2ParityCases[parity] + "_pad4_withoutLCTFit"].Fill(pt, delta_phi_dir_GE21_pad4_withoutLCTFit)
                mapTH2F["GenMuPt_vs_abs_phiGEMst1_phiGEMst2_eta" + etaRangesGE11[etaPart] + "_" +  ME1ME2ParityCases[parity] + "_pad8_withoutLCTFit"].Fill(pt, delta_phi_dir_GE21_pad8_withoutLCTFit)

                mapTH2F["GenMuPt_vs_abs_phiGEMst1_phiGEMst2_eta" + etaRangesGE11[etaPart] + "_" +  ME1ME2ParityCases[parity] + "_pad1_withLCTFit"].Fill(pt, delta_phi_dir_GE21_pad1_withLCTFit)
                mapTH2F["GenMuPt_vs_abs_phiGEMst1_phiGEMst2_eta" + etaRangesGE11[etaPart] + "_" +  ME1ME2ParityCases[parity] + "_pad2_withLCTFit"].Fill(pt, delta_phi_dir_GE21_pad2_withLCTFit)
                mapTH2F["GenMuPt_vs_abs_phiGEMst1_phiGEMst2_eta" + etaRangesGE11[etaPart] + "_" +  ME1ME2ParityCases[parity] + "_pad4_withLCTFit"].Fill(pt, delta_phi_dir_GE21_pad4_withLCTFit)
                mapTH2F["GenMuPt_vs_abs_phiGEMst1_phiGEMst2_eta" + etaRangesGE11[etaPart] + "_" +  ME1ME2ParityCases[parity] + "_pad8_withLCTFit"].Fill(pt, delta_phi_dir_GE21_pad8_withLCTFit)

                
                ## need a function that gets the pT from the inverse directions
                directionBasedPt_withoutLCTFit = 0
                directionBasedPt_withLCTFit = 0


                
                ## displaced pT assignment plots
                if dxy <= 100:
                  if directionBasedPt_withoutLCTFit >= 10: mapTH1F["Displaced_L1MuPt10_GenMuPt_GE11_ME11_GE21_ME21_withoutLCTFit"].Fill(pt)
                  if directionBasedPt_withoutLCTFit >= 15: mapTH1F["Displaced_L1MuPt15_GenMuPt_GE11_ME11_GE21_ME21_withoutLCTFit"].Fill(pt)
                  if directionBasedPt_withoutLCTFit >= 20: mapTH1F["Displaced_L1MuPt20_GenMuPt_GE11_ME11_GE21_ME21_withoutLCTFit"].Fill(pt)
                  if directionBasedPt_withLCTFit >= 10: mapTH1F["Displaced_L1MuPt10_GenMuPt_GE11_ME11_GE21_ME21_withLCTFit"].Fill(pt)
                  if directionBasedPt_withLCTFit >= 15: mapTH1F["Displaced_L1MuPt15_GenMuPt_GE11_ME11_GE21_ME21_withLCTFit"].Fill(pt)
                  if directionBasedPt_withLCTFit >= 20: mapTH1F["Displaced_L1MuPt20_GenMuPt_GE11_ME11_GE21_ME21_withLCTFit"].Fill(pt)
                if dxy <= 5:
                  if directionBasedPt_withoutLCTFit >= 10: mapTH1F["Displaced_L1MuPt10_GenMuPt_GE11_ME11_GE21_ME21_dxy0to5_withoutLCTFit"].Fill(pt)
                  if directionBasedPt_withoutLCTFit >= 15: mapTH1F["Displaced_L1MuPt15_GenMuPt_GE11_ME11_GE21_ME21_dxy0to5_withoutLCTFit"].Fill(pt)
                  if directionBasedPt_withoutLCTFit >= 20: mapTH1F["Displaced_L1MuPt20_GenMuPt_GE11_ME11_GE21_ME21_dxy0to5_withoutLCTFit"].Fill(pt)
                  if directionBasedPt_withLCTFit >= 10: mapTH1F["Displaced_L1MuPt10_GenMuPt_GE11_ME11_GE21_ME21_dxy0to5_withLCTFit"].Fill(pt)
                  if directionBasedPt_withLCTFit >= 15: mapTH1F["Displaced_L1MuPt15_GenMuPt_GE11_ME11_GE21_ME21_dxy0to5_withLCTFit"].Fill(pt)
                  if directionBasedPt_withLCTFit >= 20: mapTH1F["Displaced_L1MuPt20_GenMuPt_GE11_ME11_GE21_ME21_dxy0to5_withLCTFit"].Fill(pt)
                if 5 < dxy  and dxy <= 50:
                  if directionBasedPt_withoutLCTFit >= 10: mapTH1F["Displaced_L1MuPt10_GenMuPt_GE11_ME11_GE21_ME21_dxy5to50_withoutLCTFit"].Fill(pt)
                  if directionBasedPt_withoutLCTFit >= 15: mapTH1F["Displaced_L1MuPt15_GenMuPt_GE11_ME11_GE21_ME21_dxy5to50_withoutLCTFit"].Fill(pt)
                  if directionBasedPt_withoutLCTFit >= 20: mapTH1F["Displaced_L1MuPt20_GenMuPt_GE11_ME11_GE21_ME21_dxy5to50_withoutLCTFit"].Fill(pt)
                  if directionBasedPt_withLCTFit >= 10: mapTH1F["Displaced_L1MuPt10_GenMuPt_GE11_ME11_GE21_ME21_dxy5to50_withLCTFit"].Fill(pt)
                  if directionBasedPt_withLCTFit >= 15: mapTH1F["Displaced_L1MuPt15_GenMuPt_GE11_ME11_GE21_ME21_dxy5to50_withLCTFit"].Fill(pt)
                  if directionBasedPt_withLCTFit >= 20: mapTH1F["Displaced_L1MuPt20_GenMuPt_GE11_ME11_GE21_ME21_dxy5to50_withLCTFit"].Fill(pt)
                if 50 < dxy and dxy <= 100:
                  if directionBasedPt_withoutLCTFit >= 10: mapTH1F["Displaced_L1MuPt10_GenMuPt_GE11_ME11_GE21_ME21_dxy50to100_withoutLCTFit"].Fill(pt)
                  if directionBasedPt_withoutLCTFit >= 15: mapTH1F["Displaced_L1MuPt15_GenMuPt_GE11_ME11_GE21_ME21_dxy50to100_withoutLCTFit"].Fill(pt)
                  if directionBasedPt_withoutLCTFit >= 20: mapTH1F["Displaced_L1MuPt20_GenMuPt_GE11_ME11_GE21_ME21_dxy50to100_withoutLCTFit"].Fill(pt)
                  if directionBasedPt_withLCTFit >= 10: mapTH1F["Displaced_L1MuPt10_GenMuPt_GE11_ME11_GE21_ME21_dxy50to100_withLCTFit"].Fill(pt)
                  if directionBasedPt_withLCTFit >= 15: mapTH1F["Displaced_L1MuPt15_GenMuPt_GE11_ME11_GE21_ME21_dxy50to100_withLCTFit"].Fill(pt)
                  if directionBasedPt_withLCTFit >= 20: mapTH1F["Displaced_L1MuPt20_GenMuPt_GE11_ME11_GE21_ME21_dxy50to100_withLCTFit"].Fill(pt)



              ## End of direction based pT assignment method  


              ## get the parity
              parity = get_parity(CSCTF_isEven1, CSCTF_isEven2, CSCTF_isEven3, CSCTF_isEven4)

              ## stub positions
              ok_position_based_endcap =  ok_CSCTF_st1 and ok_CSCTF_st2 and ok_CSCTF_st3
              if ok_position_based_endcap and 0 <= parity and parity <= 3 and abs(eta_prop)>=1.2 and abs(eta_prop)<=1.6:
                nL1MuMatched_ME1_ME2_ME3 += 1

                etaPartition = get_eta_partition(eta_prop)
                
                ## get the deltaYs
                deltay12_withoutLCTFit, deltay23_withoutLCTFit = deltay12_deltay23(CSCTF_x1, CSCTF_y1, CSCTF_phi1,
                                                                                   CSCTF_x2, CSCTF_y2, CSCTF_phi2,
                                                                                   CSCTF_x3, CSCTF_y3, CSCTF_phi3)

                deltay12_withLCTFit, deltay23_withLCTFit = deltay12_deltay23(CSCTF_fit_x1, CSCTF_fit_y1, CSCTF_fit_phi1,
                                                                             CSCTF_fit_x2, CSCTF_fit_y2, CSCTF_fit_phi2,
                                                                             CSCTF_fit_x3, CSCTF_fit_y3, CSCTF_fit_phi3)
                ## only use pT>10GeV muons for this study
                if pt > 10:
                  mapTH2F["deltay12_vs_deltay23_eta" + etaRanges[etaPartition] + "_" + ME1ME2ME3ParityCases[parity] + "_withoutLCTFit"].Fill(deltay12_withoutLCTFit, deltay23_withoutLCTFit)
                  mapTH2F["deltay12_vs_deltay23_eta" + etaRanges[etaPartition] + "_" + ME1ME2ME3ParityCases[parity] + "_withLCTFit"].Fill(deltay12_withLCTFit, deltay23_withLCTFit)
                
                proportionalityFactor_withoutLCTFit = get_proptionality_factor(etaRanges[etaPartition], ME1ME2ME3ParityCases[parity], False)
                proportionalityFactor_withLCTFit =    get_proptionality_factor(etaRanges[etaPartition], ME1ME2ME3ParityCases[parity], True)

                deltaDeltaY123_withoutLCTFit = abs(deltay23_withoutLCTFit - proportionalityFactor_withoutLCTFit * deltay12_withoutLCTFit)
                deltaDeltaY123_withLCTFit    = abs(deltay23_withLCTFit    - proportionalityFactor_withLCTFit    * deltay12_withLCTFit)

                mapTH2F["GenMuPt_vs_inv_deltaDeltaY123_eta" + etaRanges[etaPartition] + "_" + ME1ME2ME3ParityCases[parity] + "_withoutLCTFit"].Fill(pt, 1./deltaDeltaY123_withoutLCTFit)
                mapTH2F["GenMuPt_vs_deltaDeltaY123_eta" + etaRanges[etaPartition] + "_" + ME1ME2ME3ParityCases[parity] + "_withoutLCTFit"].Fill(pt, deltaDeltaY123_withoutLCTFit)

                mapTH2F["GenMuPt_vs_inv_deltaDeltaY123_eta" + etaRanges[etaPartition] + "_" + ME1ME2ME3ParityCases[parity] + "_withLCTFit"].Fill(pt, 1./deltaDeltaY123_withLCTFit)
                mapTH2F["GenMuPt_vs_deltaDeltaY123_eta" + etaRanges[etaPartition] + "_" + ME1ME2ME3ParityCases[parity] + "_withLCTFit"].Fill(pt, deltaDeltaY123_withLCTFit)
                
                ## get the reconstruction pT value
                #print "True pt", pt, "deltaDeltaY123_withoutLCTFit", deltaDeltaY123_withoutLCTFit, "deltaDeltaY123_withLCTFit", deltaDeltaY123_withLCTFit
                positionPt_withoutLCTFit = pt_from_deltaDeltaY123(deltaDeltaY123_withoutLCTFit, etaRanges[etaPartition], ME1ME2ME3ParityCases[parity], False)
                positionPt_withLCTFit = pt_from_deltaDeltaY123(deltaDeltaY123_withLCTFit,       etaRanges[etaPartition], ME1ME2ME3ParityCases[parity], True)

                
                ## fill plots!!!
                if dxy <= 100:
                  mapTH1F["GenMuPt_ME1_ME2_ME3"].Fill(pt)                 
                  if positionPt_withoutLCTFit>=10: 
                    mapTH1F["Displaced_L1MuPt10_GenMuPt_ME1_ME2_ME3_withoutLCTFit"].Fill(pt)
                  if positionPt_withoutLCTFit>=15: 
                    mapTH1F["Displaced_L1MuPt15_GenMuPt_ME1_ME2_ME3_withoutLCTFit"].Fill(pt)
                  if positionPt_withoutLCTFit>=20: 
                    mapTH1F["Displaced_L1MuPt20_GenMuPt_ME1_ME2_ME3_withoutLCTFit"].Fill(pt)
                  if positionPt_withLCTFit>=10: 
                    mapTH1F["Displaced_L1MuPt10_GenMuPt_ME1_ME2_ME3_withLCTFit"].Fill(pt)
                  if positionPt_withLCTFit>=15: 
                    mapTH1F["Displaced_L1MuPt15_GenMuPt_ME1_ME2_ME3_withLCTFit"].Fill(pt)
                  if positionPt_withLCTFit>=20: 
                    mapTH1F["Displaced_L1MuPt20_GenMuPt_ME1_ME2_ME3_withLCTFit"].Fill(pt)

                if dxy <= 5:                
                  mapTH1F["GenMuPt_ME1_ME2_ME3_dxy0to5"].Fill(pt)               
                  if positionPt_withoutLCTFit>=10: 
                    mapTH1F["Displaced_L1MuPt10_GenMuPt_ME1_ME2_ME3_dxy0to5_withoutLCTFit"].Fill(pt)
                  if positionPt_withoutLCTFit>=15: 
                    mapTH1F["Displaced_L1MuPt15_GenMuPt_ME1_ME2_ME3_dxy0to5_withoutLCTFit"].Fill(pt)
                  if positionPt_withoutLCTFit>=20: 
                    mapTH1F["Displaced_L1MuPt20_GenMuPt_ME1_ME2_ME3_dxy0to5_withoutLCTFit"].Fill(pt)
                  if positionPt_withLCTFit>=10: 
                    mapTH1F["Displaced_L1MuPt10_GenMuPt_ME1_ME2_ME3_dxy0to5_withLCTFit"].Fill(pt)
                  if positionPt_withLCTFit>=15: 
                    mapTH1F["Displaced_L1MuPt15_GenMuPt_ME1_ME2_ME3_dxy0to5_withLCTFit"].Fill(pt)
                  if positionPt_withLCTFit>=20: 
                    mapTH1F["Displaced_L1MuPt20_GenMuPt_ME1_ME2_ME3_dxy0to5_withLCTFit"].Fill(pt)


                if 5 < dxy and dxy <= 50:  
                  mapTH1F["GenMuPt_ME1_ME2_ME3_dxy5to50"].Fill(pt)  
                  if positionPt_withoutLCTFit>=10: 
                    mapTH1F["Displaced_L1MuPt10_GenMuPt_ME1_ME2_ME3_dxy5to50_withoutLCTFit"].Fill(pt)
                  if positionPt_withoutLCTFit>=15: 
                    mapTH1F["Displaced_L1MuPt15_GenMuPt_ME1_ME2_ME3_dxy5to50_withoutLCTFit"].Fill(pt)
                  if positionPt_withoutLCTFit>=20: 
                    mapTH1F["Displaced_L1MuPt20_GenMuPt_ME1_ME2_ME3_dxy5to50_withoutLCTFit"].Fill(pt)
                  if positionPt_withLCTFit>=10: 
                    mapTH1F["Displaced_L1MuPt10_GenMuPt_ME1_ME2_ME3_dxy5to50_withLCTFit"].Fill(pt)
                  if positionPt_withLCTFit>=15: 
                    mapTH1F["Displaced_L1MuPt15_GenMuPt_ME1_ME2_ME3_dxy5to50_withLCTFit"].Fill(pt)
                  if positionPt_withLCTFit>=20: 
                    mapTH1F["Displaced_L1MuPt20_GenMuPt_ME1_ME2_ME3_dxy5to50_withLCTFit"].Fill(pt)

                if 50 < dxy and dxy <= 100: 
                  mapTH1F["GenMuPt_ME1_ME2_ME3_dxy50to100"].Fill(pt)
                  if positionPt_withoutLCTFit>=10: 
                    mapTH1F["Displaced_L1MuPt10_GenMuPt_ME1_ME2_ME3_dxy50to100_withoutLCTFit"].Fill(pt)
                  if positionPt_withoutLCTFit>=15: 
                    mapTH1F["Displaced_L1MuPt15_GenMuPt_ME1_ME2_ME3_dxy50to100_withoutLCTFit"].Fill(pt)
                  if positionPt_withoutLCTFit>=20: 
                    mapTH1F["Displaced_L1MuPt20_GenMuPt_ME1_ME2_ME3_dxy50to100_withoutLCTFit"].Fill(pt)
                  if positionPt_withLCTFit>=10: 
                    mapTH1F["Displaced_L1MuPt10_GenMuPt_ME1_ME2_ME3_dxy50to100_withLCTFit"].Fill(pt)
                  if positionPt_withLCTFit>=15: 
                    mapTH1F["Displaced_L1MuPt15_GenMuPt_ME1_ME2_ME3_dxy50to100_withLCTFit"].Fill(pt)
                  if positionPt_withLCTFit>=20: 
                    mapTH1F["Displaced_L1MuPt20_GenMuPt_ME1_ME2_ME3_dxy50to100_withLCTFit"].Fill(pt)
                
                
              ## End of directional/position pT assignment
            else:
              if printExtraInfo:
                print "\t\t>>>>INFO: No Matching CSCTF!!! Print all available CSCTF..."
                print 
                for jj in range(0,treeHits.nCSCTF):
                  CSCTF_pt = treeHits.CSCTF_pt[jj]
                  CSCTF_eta = treeHits.CSCTF_eta[jj]
                  CSCTF_phi = treeHits.CSCTF_phi[jj]
                  CSCTF_bx = treeHits.CSCTF_bx[jj]
                  CSCTF_nStubs = treeHits.CSCTF_nStubs[jj]
                  print "\t\tCSCTF", jj
                  print "\t\tCSCTF_pt", CSCTF_pt
                  print "\t\tCSCTF_eta", CSCTF_eta
                  print "\t\tCSCTF_phi", CSCTF_phi
                  print "\t\tCSCTF_bx", CSCTF_bx
                  print "\t\tCSCTF_nStubs", CSCTF_nStubs
                  print

            ## Matched to RPCb
            if verbose and processRPC:
              print "\t\t>>>>INFO: Number of RPCbs", treeHits.nRPCb
              print

            if m_RPCb and processRPC:
              if verbose:
                print "\t\t>>>>INFO: Matching RPCb with index", L1Mu_RPCb_index 
              RPCb_pt = treeHits.RPCb_pt[L1Mu_RPCb_index]
              RPCb_eta = treeHits.RPCb_eta[L1Mu_RPCb_index]
              RPCb_phi = treeHits.RPCb_phi[L1Mu_RPCb_index]
              RPCb_bx = treeHits.RPCb_bx[L1Mu_RPCb_index]
              RPCb_nStubs = treeHits.RPCb_nStubs[L1Mu_RPCb_index]
              RPCb_phi1 = treeHits.RPCb_phi1[L1Mu_RPCb_index]
              RPCb_phi2 = treeHits.RPCb_phi2[L1Mu_RPCb_index]
              RPCb_phi3 = treeHits.RPCb_phi3[L1Mu_RPCb_index]
              RPCb_phi4 = treeHits.RPCb_phi4[L1Mu_RPCb_index]
              if verbose:
                print "\t\tRPCb", L1Mu_RPCb_index
                print "\t\tRPCb_pt", RPCb_pt
                print "\t\tRPCb_eta", RPCb_eta
                print "\t\tRPCb_phi", RPCb_phi
                print "\t\tRPCb_bx", RPCb_bx
                print "\t\tRPCb_nStubs", RPCb_nStubs
                print               
            else:
              if printExtraInfo:
                print "\t\t>>>>INFO: No Matching RPCb!!! Print all available RPCb..."
                print 
                for jj in range(0,treeHits.nRPCb):
                  RPCb_pt = treeHits.RPCb_pt[jj]
                  RPCb_eta = treeHits.RPCb_eta[jj]
                  RPCb_phi = treeHits.RPCb_phi[jj]
                  RPCb_bx = treeHits.RPCb_bx[jj]
                  RPCb_nStubs = treeHits.RPCb_nStubs[jj]
                  print "\t\tRPCb", jj
                  print "\t\tRPCb_pt", RPCb_pt
                  print "\t\tRPCb_eta", RPCb_eta
                  print "\t\tRPCb_phi", RPCb_phi
                  print "\t\tRPCb_bx", RPCb_bx
                  print "\t\tRPCb_nStubs", RPCb_nStubs
                  print


            ## Matched to RPCf
            if verbose and processRPC:
              print "\t\t>>>>INFO: Number of RPCfs", treeHits.nRPCf
              print

            if m_RPCf and processRPC:
              if verbose:
                print "\t\t>>>>INFO: Matching RPCf with index", L1Mu_RPCf_index 
              RPCf_pt = treeHits.RPCf_pt[L1Mu_RPCf_index]
              RPCf_eta = treeHits.RPCf_eta[L1Mu_RPCf_index]
              RPCf_phi = treeHits.RPCf_phi[L1Mu_RPCf_index]
              RPCf_bx = treeHits.RPCf_bx[L1Mu_RPCf_index]
              RPCf_nStubs = treeHits.RPCf_nStubs[L1Mu_RPCf_index]
              if verbose:
                print "\t\tRPCf", L1Mu_RPCf_index
                print "\t\tRPCf_pt", RPCf_pt
                print "\t\tRPCf_eta", RPCf_eta
                print "\t\tRPCf_phi", RPCf_phi
                print "\t\tRPCf_bx", RPCf_bx
                print "\t\tRPCf_nStubs", RPCf_nStubs
                print               
            else:
              if printExtraInfo:
                print "\t\t>>>>INFO: No Matching RPCf!!! Print all available RPCf..."
                print 
                for jj in range(0,treeHits.nRPCf):
                  RPCf_pt = treeHits.RPCf_pt[jj]
                  RPCf_eta = treeHits.RPCf_eta[jj]
                  RPCf_phi = treeHits.RPCf_phi[jj]
                  RPCf_bx = treeHits.RPCf_bx[jj]
                  RPCf_nStubs = treeHits.RPCf_nStubs[jj]
                  print "\t\tRPCf", jj
                  print "\t\tRPCf_pt", RPCf_pt
                  print "\t\tRPCf_eta", RPCf_eta
                  print "\t\tRPCf_phi", RPCf_phi
                  print "\t\tRPCf_bx", RPCf_bx
                  print "\t\tRPCf_nStubs", RPCf_nStubs
                  print


    ## print out
    if verbose or True:
      print "-----------------------------------"
      print "Summary of the L1Mu matches: "
      print 
      print "Total                       ", nL1MuTotal
      print "Not Matched                 ", nL1MuNotMatched
      print "Matched GE11_GE21           ", nL1MuMatched_GE11_GE21
      print "Matched GE11_ME11_GE21_ME21 ", nL1MuMatched_GE11_ME11_GE21_ME21
      print "Matched ME1_ME2_ME3         ", nL1MuMatched_ME1_ME2_ME3
      print "Matched ME0_GE21            ", nL1MuMatched_GE0_GE21
      print "Matched GE11_ME0_GE21       ", nL1MuMatched_GE11_GE0_GE21
      print "Matched CSCTF               ", nL1MuMatched_CSCTF
      print "Matched DTTF                ", nL1MuMatched_DTTF
      print "Matched RPCb                ", nL1MuMatched_RPCb
      print "Matched RPCf                ", nL1MuMatched_RPCf
      print "Matched DTTF_CSCTF          ", nL1MuMatched_DTTF_CSCTF
      print "Matched RPCb_RPCf           ", nL1MuMatched_RPCb_RPCf
      print "Matched DTTF_RPCb           ", nL1MuMatched_DTTF_RPCb
      print "Matched DTTF_RPCf           ", nL1MuMatched_DTTF_RPCf
      print "Matched CSCTF_RPCb          ", nL1MuMatched_CSCTF_RPCb
      print "Matched CSCTF_RPCf          ", nL1MuMatched_CSCTF_RPCf
      print "Matched CSCTF_DTTF_RPCb     ", nL1MuMatched_CSCTF_DTTF_RPCb
      print "Matched CSCTF_DTTF_RPCf     ", nL1MuMatched_CSCTF_DTTF_RPCf
      print "Matched DTTF_RPCb_RPCf      ", nL1MuMatched_DTTF_RPCb_RPCf
      print "Matched CSCTF_RPCb_RPCf     ", nL1MuMatched_CSCTF_RPCb_RPCf
      print "Matched DTTF_CSCTF_RPCb_RPCf", nL1MuMatched_DTTF_CSCTF_RPCb_RPCf
      print "-----------------------------------"


    def makeSimplePlot(hist, cTitle, title, option = ''):
      c = TCanvas("c","c",800,600)
      c.Clear()
      gStyle.SetTitleBorderSize(0);
      gStyle.SetPadLeftMargin(0.126);
      gStyle.SetPadRightMargin(0.04);
      gStyle.SetPadTopMargin(0.06);
      gStyle.SetPadBottomMargin(0.13);
      gPad.SetTickx(1)
      gPad.SetTicky(1)
      hist.Draw(option)
      hist.SetTitle(title)
      c.SaveAs(cTitle)


    def makeSimplePlotMap(thisMap, key, title, option = ''):
      c = TCanvas("c","c",800,600)
      c.Clear()
      gStyle.SetTitleBorderSize(0);
      gStyle.SetPadLeftMargin(0.126);
      gStyle.SetPadRightMargin(0.04);
      gStyle.SetPadTopMargin(0.06);
      gStyle.SetPadBottomMargin(0.13);
      gPad.SetTickx(1)
      gPad.SetTicky(1)
      hist = thisMap[key]
      hist.Draw(option)
      hist.SetTitle(title)
      c.SaveAs(targetDir + key + ".png")


    def makeSimplePlotGaussianFit(hist, cTitle, title, option = ''):
      gStyle.SetOptStat(1111111)
      gStyle.SetOptFit(1111111);
      c = TCanvas("c","c",800,600)
      c.Clear()
      gStyle.SetTitleBorderSize(0);
      gStyle.SetPadLeftMargin(0.126);
      gStyle.SetPadRightMargin(0.04);
      gStyle.SetPadTopMargin(0.06);
      gStyle.SetPadBottomMargin(0.13);
      gPad.SetTickx(1)
      gPad.SetTicky(1)
      hist.SetTitle(title)
      hist.Draw(option)
      #print hist.GetRMS(), hist.GetStdDev()
      g1 = TF1("g1","gaus",-hist.GetStdDev(), hist.GetStdDev())
      hist.Fit(g1,"LRQ")
      c.SaveAs(cTitle)


    def makeSimplePlotGaussianFitMap(key, title, option = ''):
      gStyle.SetOptStat(1111111)
      gStyle.SetOptFit(1111111);
      c = TCanvas("c","c",800,600)
      c.Clear()
      gStyle.SetTitleBorderSize(0);
      gStyle.SetPadLeftMargin(0.126);
      gStyle.SetPadRightMargin(0.04);
      gStyle.SetPadTopMargin(0.06);
      gStyle.SetPadBottomMargin(0.13);
      gPad.SetTickx(1)
      gPad.SetTicky(1)
      hist = mapTH1F[key]
      hist.SetTitle(title)
      hist.Draw(option)
      #print hist.GetRMS(), hist.GetStdDev()
      if "fit" in key:
        g1 = TF1("g1","gaus",-hist.GetStdDev(), hist.GetStdDev())
      else:
        g1 = TF1("g1","gaus",-2*hist.GetStdDev(), 2*hist.GetStdDev())
      hist.Fit(g1,"LRQ")
      c.SaveAs(targetDir + key + ".png")


    def make2DMedianPlot(hist, ctitle, title, plotColz = True, doFit = False, fitfunction = "pol1", option = 'colz'):
      c = TCanvas("c","c",800,600)
      c.Clear()    
      gStyle.SetOptStat(1111111)
      gStyle.SetOptFit(1111);
      gStyle.SetTitleBorderSize(0);
      gStyle.SetPadLeftMargin(0.126);
      gStyle.SetPadRightMargin(0.04);
      gStyle.SetPadTopMargin(0.06);
      gStyle.SetPadBottomMargin(0.13);
      gPad.SetTickx(1)
      gPad.SetTicky(1)
      hist2 = hist.Clone()
      hist2.SetTitle(title)
      hist2.Draw(option)
      g = get1DHistogramMedianY(hist2)
      #g.SetMarkerColor(kRed)
      g.SetTitle(title)
      if doFit:
        print g.GetXaxis().GetXmin(), g.GetXaxis().GetXmax()
        p1fit = TF1("p1fit", fitfunction, g.GetXaxis().GetXmin(), g.GetXaxis().GetXmax())
        g.Fit(p1fit,"RQ")
        npar = g.GetFunction("p1fit").GetNpar()
        
        p0 = g.GetFunction("p1fit").GetParameter("p0")
        p1 = g.GetFunction("p1fit").GetParameter("p1")
        p0_err = g.GetFunction("p1fit").GetParError(0)
        p1_err = g.GetFunction("p1fit").GetParError(1)
        if npar>2:
          p2 = g.GetFunction("p1fit").GetParameter(2)
          p2_err = g.GetFunction("p1fit").GetParError(2)
        else:
          p2 = 0; p2_err = 0; p3 = 0; p3_err = 0

        if npar>3:
          p3 = g.GetFunction("p1fit").GetParameter(3)
          p3_err = g.GetFunction("p1fit").GetParError(3)
        else:
          p3 = 0; p3_err = 0

        #print "[", p0, ", ", p1, ", ", p2, ", ", p3, "]"
        #print "[", p0_err, ", ", p1_err, ", ", p2_err, ", ", p3_err, "]"
       
        """
        x = []
        double err[1];  // error on the function at point x0
        
        r->GetConfidenceIntervals(1, 1, 1, x, err, 0.683, false);
        cout << " function value at " << x[0] << " = " << myFunction->Eval(x[0]) << " +/- " << err[0] << endl;
        """
      gPad.Update()
      if plotColz:
        hist2.Draw(option + "same")
      g.Draw("p same")
      gPad.Update()
      #st = g.FindObject("stats")
      #if st:
      #  st.SetY1NDC(0.2)#; //new y start position
      #  st.SetY2NDC(0.4)#; //new y end position
      #  gPad.Modified()
      #g2.Draw("same")
      c.SaveAs(ctitle)
      SetOwnership( g, True )
      SetOwnership( hist2, True )


    def make2DMedianPlotMap(thisMap, key, title, plotColz = True, doFit = False):
      c = TCanvas("c","c",800,600)
      c.Clear()    
      gStyle.SetOptStat(1111111)
      gStyle.SetOptFit(1111);
      gStyle.SetTitleBorderSize(0);
      gStyle.SetPadLeftMargin(0.126);
      gStyle.SetPadRightMargin(0.04);
      gStyle.SetPadTopMargin(0.06);
      gStyle.SetPadBottomMargin(0.13);
      gPad.SetTickx(1)
      gPad.SetTicky(1)
      hist2 = thisMap[key]
      hist2.SetTitle(title)
      hist2.Draw()
      g = get1DHistogramMedianY(hist2)
      #g.SetMarkerColor(kRed)
      g.SetTitle(title)
      if doFit:
        #print g.GetXaxis().GetXmin(), g.GetXaxis().GetXmax()
        p1fit = TF1("p1fit", "[0]*x", g.GetXaxis().GetXmin(), g.GetXaxis().GetXmax())
        #p1fit.SetParameter(0,0)
        g.Fit(p1fit,"RQ")
        #npar = g.GetFunction("p1fit").GetNpar()
        
        #p0 = g.GetFunction("p1fit").GetParameter("p0")
        #p1 = g.GetFunction("p1fit").GetParameter("p1")
        #p0_err = g.GetFunction("p1fit").GetParError(0)
        #p1_err = g.GetFunction("p1fit").GetParError(1)

        #print "deltay12_deltay23_dict['" + key[21:] + "'] = ", p0
        #"[", p0, ", ", p1, ", ", p2, ", ", p3, "]"
        #print "[", p0_err, ", ", p1_err, ", ", p2_err, ", ", p3_err, "]"
       
      gPad.Update()
      if plotColz:
        hist2.Draw("same")
      g.Draw("p same")
      gPad.Update()
      c.SaveAs(targetDir + key + "_fit.png")
      #SetOwnership( g, True )
      #SetOwnership( hist2, True )

    ### close make2DMedianPlot

      
    makeSimplePlot(GenMuEta_leading_MS2_random_pt10, targetDir + "GenMuEta_leading_MS2_random_pt10.png", ";Muon #eta at 2nd muon station; Entries", "")
    makeSimplePlot(GenMuEta_leading_random_pt10, targetDir + "GenMuEta_leading_random_pt10.png", ";Muon #eta; Entries", "")
    makeSimplePlot(GenMuEta_leading_MS2_random_pt10, targetDir + "GenMuEta_leading_MS2_random_pt10.C", ";Muon #eta at 2nd muon station; Entries", "")
    makeSimplePlot(GenMuEta_leading_random_pt10, targetDir + "GenMuEta_leading_random_pt10.C", ";Muon #eta; Entries", "")

    makeSimplePlot(GenMuEta0_MS2, targetDir + "GenMuEta0_MS2.png", ";Muon #eta at 2nd muon station; Entries", "")
    makeSimplePlot(GenMuEta1_MS2, targetDir + "GenMuEta1_MS2.png", ";Muon #eta at 2nd muon station; Entries", "")
    makeSimplePlot(GenMuEta2_MS2, targetDir + "GenMuEta2_MS2.png", ";Muon #eta at 2nd muon station; Entries", "")
    makeSimplePlot(GenMuEta3_MS2, targetDir + "GenMuEta3_MS2.png", ";Muon #eta at 2nd muon station; Entries", "")
    makeSimplePlot(GenMuEta_MS2, targetDir + "GenMuEta_MS2.png", ";Muon #eta at 2nd muon station; Entries", "")

    ## CSC position resolutions
    makeSimplePlotGaussianFitMap("csc_pos_sh_lct_ME1b_16to18", 
                                 "#Phi resolution in ME1b chamber, 1.6<|#eta|<1.8;#Phi(LCT)-#Phi(SimHit); Entries","")
    makeSimplePlotGaussianFitMap("csc_pos_sh_lct_ME1b_18to20", 
                              "#Phi resolution in ME1b chamber, 1.8<|#eta|<2.0;#Phi(LCT)-#Phi(SimHit); Entries","")
    makeSimplePlotGaussianFitMap("csc_pos_sh_lct_ME1b_20to22", 
                              "#Phi resolution in ME1b chamber, 2.0<|#eta|<2.2;#Phi(LCT)-#Phi(SimHit); Entries","")
    makeSimplePlotGaussianFitMap("csc_pos_sh_lct_ME21_16to18", 
                              "#Phi resolution in ME21 chamber, 1.6<|#eta|<1.8;#Phi(LCT)-#Phi(SimHit); Entries","")
    makeSimplePlotGaussianFitMap("csc_pos_sh_lct_ME21_18to20", 
                              "#Phi resolution in ME21 chamber, 1.8<|#eta|<2.0;#Phi(LCT)-#Phi(SimHit); Entries","")
    makeSimplePlotGaussianFitMap("csc_pos_sh_lct_ME21_20to22", 
                              "#Phi resolution in ME21 chamber, 2.0<|#eta|<2.2;#Phi(LCT)-#Phi(SimHit); Entries","")

    makeSimplePlotGaussianFitMap("csc_pos_sh_fit_ME1b_16to18", 
                              "#Phi resolution in ME1b chamber, 1.6<|#eta|<1.8;#Phi(Fit to digis)-#Phi(SimHit); Entries","")
    makeSimplePlotGaussianFitMap("csc_pos_sh_fit_ME1b_18to20", 
                              "#Phi resolution in ME1b chamber, 1.8<|#eta|<2.0;#Phi(Fit to digis)-#Phi(SimHit); Entries","")
    makeSimplePlotGaussianFitMap("csc_pos_sh_fit_ME1b_20to22", 
                              "#Phi resolution in ME1b chamber, 2.0<|#eta|<2.2;#Phi(Fit to digis)-#Phi(SimHit); Entries","")
    makeSimplePlotGaussianFitMap("csc_pos_sh_fit_ME21_16to18", 
                              "#Phi resolution in ME21 chamber, 1.6<|#eta|<1.8;#Phi(Fit to digis)-#Phi(SimHit); Entries","")
    makeSimplePlotGaussianFitMap("csc_pos_sh_fit_ME21_18to20", 
                              "#Phi resolution in ME21 chamber, 1.8<|#eta|<2.0;#Phi(Fit to digis)-#Phi(SimHit); Entries","")
    makeSimplePlotGaussianFitMap("csc_pos_sh_fit_ME21_20to22", 
                              "#Phi resolution in ME21 chamber, 2.0<|#eta|<2.2;#Phi(Fit to digis)-#Phi(SimHit); Entries","")



    makeSimplePlotGaussianFit(csc_pos_sh_lct_ME1b_16to18_even, targetDir + "csc_pos_sh_lct_ME1b_16to18_even.png", 
                   "#Phi resolution in ME1b even chamber, 1.6<|#eta|<1.8;#Phi(LCT)-#Phi(SimHit); Entries","")
    makeSimplePlotGaussianFit(csc_pos_sh_lct_ME1b_18to20_even, targetDir + "csc_pos_sh_lct_ME1b_18to20_even.png", 
                   "#Phi resolution in ME1b even chamber, 1.8<|#eta|<2.0;#Phi(LCT)-#Phi(SimHit); Entries","")
    makeSimplePlotGaussianFit(csc_pos_sh_lct_ME1b_20to22_even, targetDir + "csc_pos_sh_lct_ME1b_20to22_even.png", 
                   "#Phi resolution in ME1b even chamber, 2.0<|#eta|<2.2;#Phi(LCT)-#Phi(SimHit); Entries","")
    makeSimplePlotGaussianFit(csc_pos_sh_lct_ME1b_16to18_odd, targetDir + "csc_pos_sh_lct_ME1b_16to18_odd.png", 
                   "#Phi resolution in ME1b odd chamber, 1.6<|#eta|<1.8;#Phi(LCT)-#Phi(SimHit); Entries","")
    makeSimplePlotGaussianFit(csc_pos_sh_lct_ME1b_18to20_odd, targetDir + "csc_pos_sh_lct_ME1b_18to20_odd.png", 
                   "#Phi resolution in ME1b odd chamber, 1.8<|#eta|<2.0;#Phi(LCT)-#Phi(SimHit); Entries","")
    makeSimplePlotGaussianFit(csc_pos_sh_lct_ME1b_20to22_odd, targetDir + "csc_pos_sh_lct_ME1b_20to22_odd.png", 
                   "#Phi resolution in ME1b odd chamber, 2.0<|#eta|<2.2;#Phi(LCT)-#Phi(SimHit); Entries","")

    makeSimplePlotGaussianFit(csc_pos_sh_fit_ME1b_16to18_even, targetDir + "csc_pos_sh_fit_ME1b_16to18_even.png", 
                   "#Phi resolution in ME1b even chamber, 1.6<|#eta|<1.8;#Phi(Fit to digis)-#Phi(SimHit); Entries","")
    makeSimplePlotGaussianFit(csc_pos_sh_fit_ME1b_18to20_even, targetDir + "csc_pos_sh_fit_ME1b_18to20_even.png", 
                   "#Phi resolution in ME1b even chamber, 1.8<|#eta|<2.0;#Phi(Fit to digis)-#Phi(SimHit); Entries","")
    makeSimplePlotGaussianFit(csc_pos_sh_fit_ME1b_20to22_even, targetDir + "csc_pos_sh_fit_ME1b_20to22_even.png", 
                   "#Phi resolution in ME1b even chamber, 2.0<|#eta|<2.2;#Phi(Fit to digis)-#Phi(SimHit); Entries","")
    makeSimplePlotGaussianFit(csc_pos_sh_fit_ME1b_16to18_odd, targetDir + "csc_pos_sh_fit_ME1b_16to18_odd.png", 
                   "#Phi resolution in ME1b odd chamber, 1.6<|#eta|<1.8;#Phi(Fit to digis)-#Phi(SimHit); Entries","")
    makeSimplePlotGaussianFit(csc_pos_sh_fit_ME1b_18to20_odd, targetDir + "csc_pos_sh_fit_ME1b_18to20_odd.png", 
                   "#Phi resolution in ME1b odd chamber, 1.8<|#eta|<2.0;#Phi(Fit to digis)-#Phi(SimHit); Entries","")
    makeSimplePlotGaussianFit(csc_pos_sh_fit_ME1b_20to22_odd, targetDir + "csc_pos_sh_fit_ME1b_20to22_odd.png", 
                   "#Phi resolution in ME1b odd chamber, 2.0<|#eta|<2.2;#Phi(Fit to digis)-#Phi(SimHit); Entries","")



    makeSimplePlot(csc_pos_sh_vs_lct_ME1b_16to18_even, targetDir + "csc_pos_sh_vs_lct_ME1b_16to18_even.png", 
                   "#Phi resolution in ME1b even chamber, 1.6<|#eta|<1.8;#Phi(LCT);#Phi(SimHit)","")
    makeSimplePlot(csc_pos_sh_vs_lct_ME1b_18to20_even, targetDir + "csc_pos_sh_vs_lct_ME1b_18to20_even.png", 
                   "#Phi resolution in ME1b even chamber, 1.8<|#eta|<2.0;#Phi(LCT);#Phi(SimHit)","")
    makeSimplePlot(csc_pos_sh_vs_lct_ME1b_20to22_even, targetDir + "csc_pos_sh_vs_lct_ME1b_20to22_even.png", 
                   "#Phi resolution in ME1b even chamber, 2.0<|#eta|<2.2;#Phi(LCT);#Phi(SimHit)","")
    makeSimplePlot(csc_pos_sh_vs_lct_ME1b_16to18_odd, targetDir + "csc_pos_sh_vs_lct_ME1b_16to18_odd.png", 
                   "#Phi resolution in ME1b odd chamber, 1.6<|#eta|<1.8;#Phi(LCT);#Phi(SimHit)","")
    makeSimplePlot(csc_pos_sh_vs_lct_ME1b_18to20_odd, targetDir + "csc_pos_sh_vs_lct_ME1b_18to20_odd.png", 
                   "#Phi resolution in ME1b odd chamber, 1.8<|#eta|<2.0;#Phi(LCT);#Phi(SimHit)","")
    makeSimplePlot(csc_pos_sh_vs_lct_ME1b_20to22_odd, targetDir + "csc_pos_sh_vs_lct_ME1b_20to22_odd.png", 
                   "#Phi resolution in ME1b odd chamber, 2.0<|#eta|<2.2;#Phi(LCT);#Phi(SimHit)","")

    makeSimplePlot(csc_pos_sh_vs_fit_ME1b_16to18_even, targetDir + "csc_pos_sh_vs_fit_ME1b_16to18_even.png", 
                   "#Phi resolution in ME1b even chamber, 1.6<|#eta|<1.8;#Phi(Fit to digis);#Phi(SimHit)","")
    makeSimplePlot(csc_pos_sh_vs_fit_ME1b_18to20_even, targetDir + "csc_pos_sh_vs_fit_ME1b_18to20_even.png", 
                   "#Phi resolution in ME1b even chamber, 1.8<|#eta|<2.0;#Phi(Fit to digis);#Phi(SimHit)","")
    makeSimplePlot(csc_pos_sh_vs_fit_ME1b_20to22_even, targetDir + "csc_pos_sh_vs_fit_ME1b_20to22_even.png", 
                   "#Phi resolution in ME1b even chamber, 2.0<|#eta|<2.2;#Phi(Fit to digis);#Phi(SimHit)","")
    makeSimplePlot(csc_pos_sh_vs_fit_ME1b_16to18_odd, targetDir + "csc_pos_sh_vs_fit_ME1b_16to18_odd.png", 
                   "#Phi resolution in ME1b odd chamber, 1.6<|#eta|<1.8;#Phi(Fit to digis);#Phi(SimHit)","")
    makeSimplePlot(csc_pos_sh_vs_fit_ME1b_18to20_odd, targetDir + "csc_pos_sh_vs_fit_ME1b_18to20_odd.png", 
                   "#Phi resolution in ME1b odd chamber, 1.8<|#eta|<2.0;#Phi(Fit to digis);#Phi(SimHit)","")
    makeSimplePlot(csc_pos_sh_vs_fit_ME1b_20to22_odd, targetDir + "csc_pos_sh_vs_fit_ME1b_20to22_odd.png", 
                   "#Phi resolution in ME1b odd chamber, 2.0<|#eta|<2.2;#Phi(Fit to digis);#Phi(SimHit)","")



    makeSimplePlotGaussianFit(csc_pos_sh_lct_ME21_16to18_even, targetDir + "csc_pos_sh_lct_ME21_16to18_even.png", 
                   "#Phi resolution in ME21 even chamber, 1.6<|#eta|<1.8;#Phi(Fit to digis);#Phi(SimHit)","")
    makeSimplePlotGaussianFit(csc_pos_sh_lct_ME21_18to20_even, targetDir + "csc_pos_sh_lct_ME21_18to20_even.png", 
                   "#Phi resolution in ME21 even chamber, 1.8<|#eta|<2.0;#Phi(LCT)-#Phi(SimHit); Entries","")
    makeSimplePlotGaussianFit(csc_pos_sh_lct_ME21_20to22_even, targetDir + "csc_pos_sh_lct_ME21_20to22_even.png", 
                   "#Phi resolution in ME21 even chamber, 2.0<|#eta|<2.2;#Phi(LCT)-#Phi(SimHit); Entries","")
    makeSimplePlotGaussianFit(csc_pos_sh_lct_ME21_16to18_odd, targetDir + "csc_pos_sh_lct_ME21_16to18_odd.png", 
                   "#Phi resolution in ME21 odd chamber, 1.6<|#eta|<1.8;#Phi(LCT)-#Phi(SimHit); Entries","")
    makeSimplePlotGaussianFit(csc_pos_sh_lct_ME21_18to20_odd, targetDir + "csc_pos_sh_lct_ME21_18to20_odd.png", 
                   "#Phi resolution in ME21 odd chamber, 1.8<|#eta|<2.0;#Phi(LCT)-#Phi(SimHit); Entries","")
    makeSimplePlotGaussianFit(csc_pos_sh_lct_ME21_20to22_odd, targetDir + "csc_pos_sh_lct_ME21_20to22_odd.png", 
                   "#Phi resolution in ME21 odd chamber, 2.0<|#eta|<2.2;#Phi(LCT)-#Phi(SimHit); Entries","")

    makeSimplePlotGaussianFit(csc_pos_sh_fit_ME21_16to18_even, targetDir + "csc_pos_sh_fit_ME21_16to18_even.png", 
                   "#Phi resolution in ME21 even chamber, 1.6<|#eta|<1.8;#Phi(Fit to digis)-#Phi(SimHit); Entries","")
    makeSimplePlotGaussianFit(csc_pos_sh_fit_ME21_18to20_even, targetDir + "csc_pos_sh_fit_ME21_18to20_even.png", 
                   "#Phi resolution in ME21 even chamber, 1.8<|#eta|<2.0;#Phi(Fit to digis)-#Phi(SimHit); Entries","")
    makeSimplePlotGaussianFit(csc_pos_sh_fit_ME21_20to22_even, targetDir + "csc_pos_sh_fit_ME21_20to22_even.png", 
                   "#Phi resolution in ME21 even chamber, 2.0<|#eta|<2.2;#Phi(Fit to digis)-#Phi(SimHit); Entries","")
    makeSimplePlotGaussianFit(csc_pos_sh_fit_ME21_16to18_odd, targetDir + "csc_pos_sh_fit_ME21_16to18_odd.png", 
                   "#Phi resolution in ME21 odd chamber, 1.6<|#eta|<1.8;#Phi(Fit to digis)-#Phi(SimHit); Entries","")
    makeSimplePlotGaussianFit(csc_pos_sh_fit_ME21_18to20_odd, targetDir + "csc_pos_sh_fit_ME21_18to20_odd.png", 
                   "#Phi resolution in ME21 odd chamber, 1.8<|#eta|<2.0;#Phi(Fit to digis)-#Phi(SimHit); Entries","")
    makeSimplePlotGaussianFit(csc_pos_sh_fit_ME21_20to22_odd, targetDir + "csc_pos_sh_fit_ME21_20to22_odd.png", 
                   "#Phi resolution in ME21 odd chamber, 2.0<|#eta|<2.2;#Phi(Fit to digis)-#Phi(SimHit); Entries","")



    makeSimplePlot(csc_pos_sh_vs_lct_ME21_16to18_even, targetDir + "csc_pos_sh_vs_lct_ME21_16to18_even.png", 
                   "#Phi resolution in ME21 even chamber, 1.6<|#eta|<1.8;#Phi(LCT);#Phi(SimHit)","")
    makeSimplePlot(csc_pos_sh_vs_lct_ME21_18to20_even, targetDir + "csc_pos_sh_vs_lct_ME21_18to20_even.png", 
                   "#Phi resolution in ME21 even chamber, 1.8<|#eta|<2.0;#Phi(LCT);#Phi(SimHit)","")
    makeSimplePlot(csc_pos_sh_vs_lct_ME21_20to22_even, targetDir + "csc_pos_sh_vs_lct_ME21_20to22_even.png", 
                   "#Phi resolution in ME21 even chamber, 2.0<|#eta|<2.2;#Phi(LCT);#Phi(SimHit)","")
    makeSimplePlot(csc_pos_sh_vs_lct_ME21_16to18_odd, targetDir + "csc_pos_sh_vs_lct_ME21_16to18_odd.png", 
                   "#Phi resolution in ME21 odd chamber, 1.6<|#eta|<1.8;#Phi(LCT);#Phi(SimHit)","")
    makeSimplePlot(csc_pos_sh_vs_lct_ME21_18to20_odd, targetDir + "csc_pos_sh_vs_lct_ME21_18to20_odd.png", 
                   "#Phi resolution in ME21 odd chamber, 1.8<|#eta|<2.0;#Phi(LCT);#Phi(SimHit)","")
    makeSimplePlot(csc_pos_sh_vs_lct_ME21_20to22_odd, targetDir + "csc_pos_sh_vs_lct_ME21_20to22_odd.png", 
                   "#Phi resolution in ME21 odd chamber, 2.0<|#eta|<2.2;#Phi(LCT);#Phi(SimHit)","")

    makeSimplePlot(csc_pos_sh_vs_fit_ME21_16to18_even, targetDir + "csc_pos_sh_vs_fit_ME21_16to18_even.png", 
                   "#Phi resolution in ME21 even chamber, 1.6<|#eta|<1.8;#Phi(Fit to digis);#Phi(SimHit)","")
    makeSimplePlot(csc_pos_sh_vs_fit_ME21_18to20_even, targetDir + "csc_pos_sh_vs_fit_ME21_18to20_even.png", 
                   "#Phi resolution in ME21 even chamber, 1.8<|#eta|<2.0;#Phi(Fit to digis);#Phi(SimHit)","")
    makeSimplePlot(csc_pos_sh_vs_fit_ME21_20to22_even, targetDir + "csc_pos_sh_vs_fit_ME21_20to22_even.png", 
                   "#Phi resolution in ME21 even chamber, 2.0<|#eta|<2.2;#Phi(Fit to digis);#Phi(SimHit)","")
    makeSimplePlot(csc_pos_sh_vs_fit_ME21_16to18_odd, targetDir + "csc_pos_sh_vs_fit_ME21_16to18_odd.png", 
                   "#Phi resolution in ME21 odd chamber, 1.6<|#eta|<1.8;#Phi(Fit to digis);#Phi(SimHit)","")
    makeSimplePlot(csc_pos_sh_vs_fit_ME21_18to20_odd, targetDir + "csc_pos_sh_vs_fit_ME21_18to20_odd.png", 
                   "#Phi resolution in ME21 odd chamber, 1.8<|#eta|<2.0;#Phi(Fit to digis);#Phi(SimHit)","")
    makeSimplePlot(csc_pos_sh_vs_fit_ME21_20to22_odd, targetDir + "csc_pos_sh_vs_fit_ME21_20to22_odd.png", 
                   "#Phi resolution in ME21 odd chamber, 2.0<|#eta|<2.2;#Phi(Fit to digis);#Phi(SimHit)","")


    ## Plots for position based pT measurement (CSC only!!!)
    for pp in ME1ME2ME3ParityCases:
      for qq,rr in zip(etaRanges, etaRangesString):
        makeSimplePlotMap(mapTH2F, "deltay12_vs_deltay23_eta" + qq + "_" + pp + "_withoutLCTFit", pp + " " + rr +  ";#Delta Y_{12} [cm]; #Delta Y_{23} [cm]",'colz')
        make2DMedianPlotMap(mapTH2F, "deltay12_vs_deltay23_eta" + qq + "_" + pp + "_withoutLCTFit", pp + " " + rr +  ";#Delta Y_{12} [cm]; #Delta Y_{23} [cm]", True, True)
        makeSimplePlotMap(mapTH2F, "GenMuPt_vs_inv_deltaDeltaY123_eta" + qq + "_" + pp + "_withoutLCTFit", pp + " " + rr +  "; p_{T} [GeV]; 1/#Delta#Delta Y_{123} [GeV]",'colz')
        makeSimplePlotMap(mapTH2F, "GenMuPt_vs_deltaDeltaY123_eta" + qq + "_" + pp + "_withoutLCTFit", pp + " " + rr +  "; p_{T} [GeV]; #Delta#Delta Y_{123} [1/GeV]",'colz')

        makeSimplePlotMap(mapTH2F, "deltay12_vs_deltay23_eta" + qq + "_" + pp + "_withLCTFit", pp + " " + rr +  ";#Delta Y_{12} [cm]; #Delta Y_{23} [cm]",'colz')
        make2DMedianPlotMap(mapTH2F, "deltay12_vs_deltay23_eta" + qq + "_" + pp + "_withLCTFit", pp + " " + rr +  ";#Delta Y_{12} [cm]; #Delta Y_{23} [cm]", True, True)
        makeSimplePlotMap(mapTH2F, "GenMuPt_vs_inv_deltaDeltaY123_eta" + qq + "_" + pp + "_withLCTFit", pp + " " + rr +  "; p_{T} [GeV]; 1/#Delta#Delta Y_{123} [GeV]",'colz')
        makeSimplePlotMap(mapTH2F, "GenMuPt_vs_deltaDeltaY123_eta" + qq + "_" + pp + "_withLCTFit", pp + " " + rr +  "; p_{T} [GeV]; #Delta#Delta Y_{123} [1/GeV]",'colz')

        generateLUT = False
        if generateLUT:
          ## get the arrays with 90% cutoff numbers
          #print "Numbers for GenMuPt_vs_deltaDeltaY123_eta" + qq + "_" + pp + "_withoutLCTFit"
          lut1 = get1DHistogramFractionY(mapTH2F["GenMuPt_vs_deltaDeltaY123_eta" + qq + "_" + pp + "_withoutLCTFit"], .90)
          print "    deltaDeltaY123_dict['eta" + qq + "_" + pp + "_withoutLCTFit_x'] = ", lut1[0]
          print "    deltaDeltaY123_dict['eta" + qq + "_" + pp + "_withoutLCTFit_y'] = ", lut1[1]

          #print "Numbers for GenMuPt_vs_deltaDeltaY123_eta" + qq + "_" + pp + "_withLCTFit"
          lut2 = get1DHistogramFractionY(mapTH2F["GenMuPt_vs_deltaDeltaY123_eta" + qq + "_" + pp + "_withLCTFit"], 0.90)
          print "    deltaDeltaY123_dict['eta" + qq + "_" + pp + "_withLCTFit_x'] = ", lut1[0]
          print "    deltaDeltaY123_dict['eta" + qq + "_" + pp + "_withLCTFit_y'] = ", lut1[1]

    ## plots with DTs
    makeSimplePlot(GenMuPt_vs_phiDTst1_phiDTst2, targetDir + "GenMuPt_vs_phiDTst1_phiDTst2.png", ";p_{T} [GeV]; #Delta#Phi_{12}", "COLZ")
    makeSimplePlot(GenMuPt_vs_phiDTst1_phiDTst3, targetDir + "GenMuPt_vs_phiDTst1_phiDTst3.png", ";p_{T} [GeV]; #Delta#Phi_{13}", "COLZ")
    makeSimplePlot(GenMuPt_vs_phiDTst1_phiDTst4, targetDir + "GenMuPt_vs_phiDTst1_phiDTst4.png", ";p_{T} [GeV]; #Delta#Phi_{14}", "COLZ")
    makeSimplePlot(GenMuPt_vs_phiDTst2_phiDTst3, targetDir + "GenMuPt_vs_phiDTst2_phiDTst3.png", ";p_{T} [GeV]; #Delta#Phi_{23}", "COLZ")
    makeSimplePlot(GenMuPt_vs_phiDTst2_phiDTst4, targetDir + "GenMuPt_vs_phiDTst2_phiDTst4.png", ";p_{T} [GeV]; #Delta#Phi_{24}", "COLZ")
    makeSimplePlot(GenMuPt_vs_phiDTst3_phiDTst4, targetDir + "GenMuPt_vs_phiDTst3_phiDTst4.png", ";p_{T} [GeV]; #Delta#Phi_{34}", "COLZ")

    makeSimplePlot(nDT_stubs, targetDir + "nDT_stubs.png", "; status; Number of entries")
    makeSimplePlot(nDT_stubs_vs_dxy, targetDir + "nDT_stubs_vs_dxy.png", "; status; d_{xy} [cm]", "COLZ")

    makeSimplePlot(phiDTst1_vs_phiDTst4_dxy0to5, targetDir + "phiDTst1_vs_phiDTst4_dxy0to5.png", "; #Delta#Phi_1; #Delta#Phi_4", "COLZ")
    makeSimplePlot(phiDTst1_vs_phiDTst4_dxy5to50, targetDir + "phiDTst1_vs_phiDTst4_dxy5to50.png", "; #Delta#Phi_1; #Delta#Phi_4", "COLZ")
    makeSimplePlot(phiDTst1_vs_phiDTst4_dxy50to100, targetDir + "phiDTst1_vs_phiDTst4_dxy50to100.png", "; #Delta#Phi_1; #Delta#Phi_4", "COLZ")

    makeSimplePlot(phiDTst1_phiDTst2, targetDir + "phiDTst1_phiDTst2.png", ";#Delta#Phi_{12}; Entries")
    makeSimplePlot(phiDTst1_phiDTst3, targetDir + "phiDTst1_phiDTst3.png", ";#Delta#Phi_{13}; Entries")
    makeSimplePlot(phiDTst1_phiDTst4, targetDir + "phiDTst1_phiDTst4.png", ";#Delta#Phi_{14}; Entries")
    makeSimplePlot(phiDTst2_phiDTst3, targetDir + "phiDTst2_phiDTst3.png", ";#Delta#Phi_{23}; Entries")
    makeSimplePlot(phiDTst2_phiDTst4, targetDir + "phiDTst2_phiDTst4.png", ";#Delta#Phi_{24}; Entries")
    makeSimplePlot(phiDTst3_phiDTst4, targetDir + "phiDTst3_phiDTst4.png", ";#Delta#Phi_{34}; Entries")

    makeSimplePlot(abs_phiDTst1_phiDTst2, targetDir + "abs_phiDTst1_phiDTst2.png", ";|#Delta#Phi_{12}|; Entries")
    makeSimplePlot(abs_phiDTst1_phiDTst3, targetDir + "abs_phiDTst1_phiDTst3.png", ";|#Delta#Phi_{13}|; Entries")
    makeSimplePlot(abs_phiDTst1_phiDTst4, targetDir + "abs_phiDTst1_phiDTst4.png", ";|#Delta#Phi_{14}|; Entries")
    makeSimplePlot(abs_phiDTst2_phiDTst3, targetDir + "abs_phiDTst2_phiDTst3.png", ";|#Delta#Phi_{23}|; Entries")
    makeSimplePlot(abs_phiDTst2_phiDTst4, targetDir + "abs_phiDTst2_phiDTst4.png", ";|#Delta#Phi_{24}|; Entries")
    makeSimplePlot(abs_phiDTst3_phiDTst4, targetDir + "abs_phiDTst3_phiDTst4.png", ";|#Delta#Phi_{34}|; Entries")

    make2DMedianPlot(GenMuPt_vs_phiDTst1_phiDTst2, targetDir + "GenMuPt_vs_phiDTst1_phiDTst2_pol1.png", 
                        "GenMuPt_vs_phiDTst1_phiDTst2_pol1; GEN Mu p_{T} [GeV]; #Delta#Phi_{dir}(1,2)", False, True)
    make2DMedianPlot(GenMuPt_vs_phiDTst1_phiDTst3, targetDir + "GenMuPt_vs_phiDTst1_phiDTst3_pol1.png", 
                        "GenMuPt_vs_phiDTst1_phiDTst3_pol1; GEN Mu p_{T} [GeV]; #Delta#Phi_{dir}(1,3)", False, True)
    make2DMedianPlot(GenMuPt_vs_phiDTst1_phiDTst4, targetDir + "GenMuPt_vs_phiDTst1_phiDTst4_pol1.png", 
                        "GenMuPt_vs_phiDTst1_phiDTst4_pol1; GEN Mu p_{T} [GeV]; #Delta#Phi_{dir}(1,4)", False, True)
    make2DMedianPlot(GenMuPt_vs_phiDTst2_phiDTst3, targetDir + "GenMuPt_vs_phiDTst2_phiDTst3_pol1.png", 
                        "GenMuPt_vs_phiDTst2_phiDTst3_pol1; GEN Mu p_{T} [GeV]; #Delta#Phi_{dir}(2,3)", False, True)
    make2DMedianPlot(GenMuPt_vs_phiDTst2_phiDTst4, targetDir + "GenMuPt_vs_phiDTst2_phiDTst4_pol1.png", 
                        "GenMuPt_vs_phiDTst2_phiDTst4_pol1; GEN Mu p_{T} [GeV]; #Delta#Phi_{dir}(2,4)", False, True)
    make2DMedianPlot(GenMuPt_vs_phiDTst3_phiDTst4, targetDir + "GenMuPt_vs_phiDTst3_phiDTst4_pol1.png", 
                        "GenMuPt_vs_phiDTst3_phiDTst4_pol1; GEN Mu p_{T} [GeV]; #Delta#Phi_{dir}(3,4)", False, True)

    make2DMedianPlot(GenMuPt_vs_abs_phiDTst1_phiDTst2, targetDir + "GenMuPt_vs_abs_phiDTst1_phiDTst2_pol1.png", 
                        "GenMuPt_vs_phiDTst1_phiDTst2_pol1; GEN Mu p_{T} [GeV]; |#Delta#Phi_{dir}(1,2)|")
    make2DMedianPlot(GenMuPt_vs_abs_phiDTst1_phiDTst3, targetDir + "GenMuPt_vs_abs_phiDTst1_phiDTst3_pol1.png", 
                        "GenMuPt_vs_phiDTst1_phiDTst2_pol1; GEN Mu p_{T} [GeV]; |#Delta#Phi_{dir}(1,3)|")
    make2DMedianPlot(GenMuPt_vs_abs_phiDTst1_phiDTst4, targetDir + "GenMuPt_vs_abs_phiDTst1_phiDTst4_pol1.png", 
                        "GenMuPt_vs_phiDTst1_phiDTst2_pol1; GEN Mu p_{T} [GeV]; |#Delta#Phi_{dir}(1,4)|")
    make2DMedianPlot(GenMuPt_vs_abs_phiDTst2_phiDTst3, targetDir + "GenMuPt_vs_abs_phiDTst2_phiDTst3_pol1.png", 
                        "GenMuPt_vs_phiDTst1_phiDTst2_pol1; GEN Mu p_{T} [GeV]; |#Delta#Phi_{dir}(2,3)|")
    make2DMedianPlot(GenMuPt_vs_abs_phiDTst2_phiDTst4, targetDir + "GenMuPt_vs_abs_phiDTst2_phiDTst4_pol1.png", 
                        "GenMuPt_vs_phiDTst1_phiDTst2_pol1; GEN Mu p_{T} [GeV]; |#Delta#Phi_{dir}(2,4)|")
    make2DMedianPlot(GenMuPt_vs_abs_phiDTst3_phiDTst4, targetDir + "GenMuPt_vs_abs_phiDTst3_phiDTst4_pol1.png", 
                        "GenMuPt_vs_phiDTst1_phiDTst2_pol1; GEN Mu p_{T} [GeV]; |#Delta#Phi_{dir}(3,4)|")

    make2DMedianPlot(GenMuPt_vs_abs_phiDTst1_phiDTst2_inv, targetDir + "GenMuPt_vs_abs_phiDTst1_phiDTst2_inv_pol1.png", 
                        "GenMuPt_vs_abs_phiDTst1_phiDTst2_inv_pol1; GEN Mu p_{T} [GeV]; 1/|#Delta#Phi_{dir}(1,2)|", False, True, "pol1")
    make2DMedianPlot(GenMuPt_vs_abs_phiDTst1_phiDTst3_inv, targetDir + "GenMuPt_vs_abs_phiDTst1_phiDTst3_inv_pol1.png", 
                        "GenMuPt_vs_abs_phiDTst1_phiDTst3_inv_pol1; GEN Mu p_{T} [GeV]; 1/|#Delta#Phi_{dir}(1,3)|", False, True, "pol1")
    make2DMedianPlot(GenMuPt_vs_abs_phiDTst1_phiDTst4_inv, targetDir + "GenMuPt_vs_abs_phiDTst1_phiDTst4_inv_pol1.png", 
                        "GenMuPt_vs_abs_phiDTst1_phiDTst4_inv_pol1; GEN Mu p_{T} [GeV]; 1/|#Delta#Phi_{dir}(1,4)|", False, True, "pol1")
    make2DMedianPlot(GenMuPt_vs_abs_phiDTst2_phiDTst3_inv, targetDir + "GenMuPt_vs_abs_phiDTst2_phiDTst3_inv_pol1.png", 
                        "GenMuPt_vs_abs_phiDTst2_phiDTst3_inv_pol1; GEN Mu p_{T} [GeV]; 1/|#Delta#Phi_{dir}(2,4)|", False, True, "pol1")
    make2DMedianPlot(GenMuPt_vs_abs_phiDTst2_phiDTst4_inv, targetDir + "GenMuPt_vs_abs_phiDTst2_phiDTst4_inv_pol1.png", 
                        "GenMuPt_vs_abs_phiDTst2_phiDTst4_inv_pol1; GEN Mu p_{T} [GeV]; 1/|#Delta#Phi_{dir}(2,4)|", False, True, "pol1")
    make2DMedianPlot(GenMuPt_vs_abs_phiDTst3_phiDTst4_inv, targetDir + "GenMuPt_vs_abs_phiDTst3_phiDTst4_inv_pol1.png", 
                        "GenMuPt_vs_abs_phiDTst3_phiDTst4_inv_pol1; GEN Mu p_{T} [GeV]; 1/|#Delta#Phi_{dir}(3,4)|", False, True, "pol1")

    make2DMedianPlot(GenMuPt_vs_abs_phiDTst1_phiDTst2_inv, targetDir + "GenMuPt_vs_abs_phiDTst1_phiDTst2_inv_pol1_v2.png", 
                        "GenMuPt_vs_abs_phiDTst1_phiDTst2_inv_pol1_v2; GEN Mu p_{T} [GeV]; 1/|#Delta#Phi_{dir}(1,2)|", True, True, "pol1")
    make2DMedianPlot(GenMuPt_vs_abs_phiDTst1_phiDTst3_inv, targetDir + "GenMuPt_vs_abs_phiDTst1_phiDTst3_inv_pol1_v2.png", 
                        "GenMuPt_vs_abs_phiDTst1_phiDTst3_inv_pol1_v2; GEN Mu p_{T} [GeV]; 1/|#Delta#Phi_{dir}(1,3)|", True, True, "pol1")
    make2DMedianPlot(GenMuPt_vs_abs_phiDTst1_phiDTst4_inv, targetDir + "GenMuPt_vs_abs_phiDTst1_phiDTst4_inv_pol1_v2.png", 
                        "GenMuPt_vs_abs_phiDTst1_phiDTst4_inv_pol1_v2; GEN Mu p_{T} [GeV]; 1/|#Delta#Phi_{dir}(1,4)|", True, True, "pol1")
    make2DMedianPlot(GenMuPt_vs_abs_phiDTst2_phiDTst3_inv, targetDir + "GenMuPt_vs_abs_phiDTst2_phiDTst3_inv_pol1_v2.png", 
                        "GenMuPt_vs_abs_phiDTst2_phiDTst3_inv_pol1_v2; GEN Mu p_{T} [GeV]; 1/|#Delta#Phi_{dir}(2,3)|", True, True, "pol1")
    make2DMedianPlot(GenMuPt_vs_abs_phiDTst2_phiDTst4_inv, targetDir + "GenMuPt_vs_abs_phiDTst2_phiDTst4_inv_pol1_v2.png", 
                        "GenMuPt_vs_abs_phiDTst2_phiDTst4_inv_pol1_v2; GEN Mu p_{T} [GeV]; 1/|#Delta#Phi_{dir}(2,4)|", True, True, "pol1")
    make2DMedianPlot(GenMuPt_vs_abs_phiDTst3_phiDTst4_inv, targetDir + "GenMuPt_vs_abs_phiDTst3_phiDTst4_inv_pol1_v2.png", 
                        "GenMuPt_vs_abs_phiDTst3_phiDTst4_inv_pol1_v2; GEN Mu p_{T} [GeV]; 1/|#Delta#Phi_{dir}(3,4)|", True, True, "pol1")

    make2DMedianPlot(GenMuPt_vs_abs_phiDTst1_phiDTst4_inv_dxy0to5, targetDir + "GenMuPt_vs_abs_phiDTst1_phiDTst4_inv_dxy0to5_pol1.png", 
                        "GenMuPt_vs_abs_phiDTst1_phiDTst4_inv_dxy0to5_pol1; GEN Mu p_{T} [GeV]; 1/|#Delta#Phi_{dir}(1,4)|", False, True, "pol1")
    make2DMedianPlot(GenMuPt_vs_abs_phiDTst1_phiDTst4_inv_dxy5to50, targetDir + "GenMuPt_vs_abs_phiDTst1_phiDTst4_inv_dxy5to50_pol1.png", 
                        "GenMuPt_vs_abs_phiDTst1_phiDTst4_inv_dxy5to50_pol1; GEN Mu p_{T} [GeV]; 1/|#Delta#Phi_{dir}(1,4)|", False, True, "pol1")
    make2DMedianPlot(GenMuPt_vs_abs_phiDTst1_phiDTst4_inv_dxy50to100, targetDir + "GenMuPt_vs_abs_phiDTst1_phiDTst4_inv_dxy50to100_pol1.png",
                        "GenMuPt_vs_abs_phiDTst1_phiDTst4_inv_dxy50to100_pol1; GEN Mu p_{T} [GeV]; 1/|#Delta#Phi_{dir}(1,4)|",  False, True, "pol1")

    make2DMedianPlot(GenMuPt_vs_abs_phiDTst1_phiDTst4_inv_dxy0to5, targetDir + "GenMuPt_vs_abs_phiDTst1_phiDTst4_inv_dxy0to5_pol1.png", 
                        "GenMuPt_vs_abs_phiDTst1_phiDTst4_inv_dxy0to5_pol1; GEN Mu p_{T} [GeV]; 1/|#Delta#Phi_{dir}(1,4)|", True, True, "pol1")
    make2DMedianPlot(GenMuPt_vs_abs_phiDTst1_phiDTst4_inv_dxy5to50, targetDir + "GenMuPt_vs_abs_phiDTst1_phiDTst4_inv_dxy5to50_pol1.png", 
                        "GenMuPt_vs_abs_phiDTst1_phiDTst4_inv_dxy5to50_pol1; GEN Mu p_{T} [GeV]; 1/|#Delta#Phi_{dir}(1,4)|", True, True, "pol1")
    make2DMedianPlot(GenMuPt_vs_abs_phiDTst1_phiDTst4_inv_dxy50to100, targetDir + "GenMuPt_vs_abs_phiDTst1_phiDTst4_inv_dxy50to100_pol1.png", 
                        "GenMuPt_vs_abs_phiDTst1_phiDTst4_inv_dxy50to100_pol1; GEN Mu p_{T} [GeV]; 1/|#Delta#Phi_{dir}(1,4)|", True, True, "pol1")


    ## plots with GEMs :-)
    makeSimplePlot(phiGEMst1_vs_phiGEMst2_dxy0to5, targetDir + "phiGEMst1_vs_phiGEMst2_dxy0to5.png", "; #Phi_{direction}(GE11); #Phi_{direction}(GE21)", "COLZ") 
    makeSimplePlot(phiGEMst1_vs_phiGEMst2_dxy5to50, targetDir + "phiGEMst1_vs_phiGEMst2_dxy5to50.png", "; #Phi_{direction}(GE11); #Phi_{direction}(GE21)", "COLZ")
    makeSimplePlot(phiGEMst1_vs_phiGEMst2_dxy50to100, targetDir + "phiGEMst1_vs_phiGEMst2_dxy50to100.png", "; #Phi_{direction}(GE11); #Phi_{direction}(GE21)", "COLZ")


    evenOddCases = ['ee','eo','oe','oo']
    etaRanges = ['16to18','18to20','20to22']
    padSizes = ['pad1','pad2','pad4','pad8']
    
    for pp in evenOddCases:
      for qq in etaRanges:
        for rr in padSizes:
          plotTitle = "GenMuPt_vs_abs_phiGEMst1_phiGEMst2_eta" + qq + "_" + pp + "_" + rr + "_withoutLCTFit"
          make2DMedianPlot(mapTH2F[plotTitle], targetDir + plotTitle + ".png", rr + " " + pp + " " + qq + ";GEN Mu p_{T} [GeV]; |#Delta#Phi_{dir}(GE11,GE21)|")
          plotTitle = "GenMuPt_vs_abs_phiGEMst1_phiGEMst2_eta" + qq + "_" + pp + "_" + rr + "_withLCTFit"
          make2DMedianPlot(mapTH2F[plotTitle], targetDir + plotTitle + ".png", rr + " " + pp + " " + qq + ";GEN Mu p_{T} [GeV]; |#Delta#Phi_{dir}(GE11,GE21)|")

          
    """
    makeSimplePlot(phiGEMst1_phiGEMst2, targetDir + "phiGEMst1_phiGEMst2.png", "; #Phi_{dir}(GE11)-#Phi_{dir}(GE21); Entries")
    makeSimplePlot(phiGEMst1_phiGEMst2_pt5to10, targetDir + "phiGEMst1_phiGEMst2_pt5to10.png", "; #Phi_{dir}(GE11)-#Phi_{dir}(GE21); Entries")
    makeSimplePlot(phiGEMst1_phiGEMst2_pt10to20, targetDir + "phiGEMst1_phiGEMst2_pt10to20.png", "; #Phi_{dir}(GE11)-#Phi_{dir}(GE21); Entries")
    makeSimplePlot(phiGEMst1_phiGEMst2_pt20, targetDir + "phiGEMst1_phiGEMst2_pt20.png", "; #Phi_{dir}(GE11)-#Phi_{dir}(GE21); Entries")
    """

    """
    make2DMedianPlot(GenMuPt_vs_abs_phiDTst1_phiDTst2_inv, targetDir + "GenMuPt_vs_abs_phiDTst1_phiDTst2_inv_pol3.png", False, True, "pol3")
    make2DMedianPlot(GenMuPt_vs_abs_phiDTst1_phiDTst3_inv, targetDir + "GenMuPt_vs_abs_phiDTst1_phiDTst3_inv_pol3.png", False, True, "pol3")
    make2DMedianPlot(GenMuPt_vs_abs_phiDTst1_phiDTst4_inv, targetDir + "GenMuPt_vs_abs_phiDTst1_phiDTst4_inv_pol3.png", False, True, "pol3")
    make2DMedianPlot(GenMuPt_vs_abs_phiDTst2_phiDTst3_inv, targetDir + "GenMuPt_vs_abs_phiDTst2_phiDTst3_inv_pol3.png", False, True, "pol3")
    make2DMedianPlot(GenMuPt_vs_abs_phiDTst2_phiDTst4_inv, targetDir + "GenMuPt_vs_abs_phiDTst2_phiDTst4_inv_pol3.png", False, True, "pol3")
    make2DMedianPlot(GenMuPt_vs_abs_phiDTst3_phiDTst4_inv, targetDir + "GenMuPt_vs_abs_phiDTst3_phiDTst4_inv_pol3.png", False, True, "pol3")
    
    make2DMedianPlot(GenMuPt_vs_abs_phiDTst1_phiDTst2_inv, targetDir + "GenMuPt_vs_abs_phiDTst1_phiDTst2_inv_pol3_v2.png", True, True, "pol3")
    make2DMedianPlot(GenMuPt_vs_abs_phiDTst1_phiDTst3_inv, targetDir + "GenMuPt_vs_abs_phiDTst1_phiDTst3_inv_pol3_v2.png", True, True, "pol3")
    make2DMedianPlot(GenMuPt_vs_abs_phiDTst1_phiDTst4_inv, targetDir + "GenMuPt_vs_abs_phiDTst1_phiDTst4_inv_pol3_v2.png", True, True, "pol3")
    make2DMedianPlot(GenMuPt_vs_abs_phiDTst2_phiDTst3_inv, targetDir + "GenMuPt_vs_abs_phiDTst2_phiDTst3_inv_pol3_v2.png", True, True, "pol3")
    make2DMedianPlot(GenMuPt_vs_abs_phiDTst2_phiDTst4_inv, targetDir + "GenMuPt_vs_abs_phiDTst2_phiDTst4_inv_pol3_v2.png", True, True, "pol3")
    make2DMedianPlot(GenMuPt_vs_abs_phiDTst3_phiDTst4_inv, targetDir + "GenMuPt_vs_abs_phiDTst3_phiDTst4_inv_pol3_v2.png", True, True, "pol3")
    """

    ## L1Mu pT trigger turn-on curves
    def makeEffPlot(eff1, eff2, eff3, title, doPt = True):
      
      c = TCanvas("c","c",800,600)
      c.Clear()    
      gStyle.SetTitleBorderSize(0);
      gStyle.SetPadLeftMargin(0.126);
      gStyle.SetPadRightMargin(0.04);
      gStyle.SetPadTopMargin(0.06);
      gStyle.SetPadBottomMargin(0.13);
      gPad.SetTickx(1)
      gPad.SetTicky(1)
      #gPad.SetLogx(1)
      
      if doPt: mmax = 60;  xaxisTitle = "True Muon p_{T} [GeV]"
      else:    mmax = 2.5; xaxisTitle = "True Muon #eta"

      b1 = TH1F("b1","b1", 25, 0, mmax)
      #b1.GetYaxis().SetRangeUser(.01,100)
      b1.GetYaxis().SetTitleOffset(1.2)
      b1.GetYaxis().SetNdivisions(520)
      b1.GetYaxis().SetTitle("Trigger efficiency")
      b1.GetXaxis().SetTitle(xaxisTitle)
      b1.GetXaxis().SetTitleOffset(1.2)
      b1.SetTitle("                                                                  14TeV, PU140")
      b1.SetStats(0)
      b1.Draw()

      eff1.SetLineColor(kBlue)
      eff1.Draw("same")
      eff2.SetLineColor(kRed)
      eff2.Draw("same")
      if eff3 is not None:
        eff3.SetLineColor(kGreen+1)
        eff3.Draw("same")

      latex = applyTdrStyle()

      ## get the pT cut from the title
      len_string = len('Prompt_L1MuPt')
      
      index = title.find('Prompt_L1MuPt')
      if index == -1:
        len_string = len('Displaced_L1MuPt')
        index = title.find('Displaced_L1MuPt')
      ptCut = title[index+len_string:index+len_string+2]
      #print len_string, ptCut

      leg = TLegend(0.6,0.2,0.9,0.45,"","brNDC")
      leg.SetFillColor(kWhite)
      leg.SetBorderSize(1)
      leg.SetFillStyle(1001)
      leg.SetTextSize(0.04)
      leg.SetHeader("L1Mu trigger p_{T} #geq " + ptCut +  "GeV")
      leg.AddEntry(eff1,"|dxy| #leq 5 cm", "l")
      leg.AddEntry(eff2,"5 < |dxy| #leq 50 cm", "l")
      if eff3 is not None:
        leg.AddEntry(eff3,"50 < |dxy| #leq 100 cm", "l")
      leg.Draw("same")
      c.SaveAs(title)
    
    def myTEfficiency(name_num,  name_denom):
      return TEfficiency(mapTH1F[name_num], mapTH1F[name_denom])

    ## pt effciency plots for prompt muons
    makeEffPlot(TEfficiency(Prompt_L1MuPt10_GenMuPt_dxy0to5, GenMuPt_dxy0to5),
                TEfficiency(Prompt_L1MuPt10_GenMuPt_dxy5to50, GenMuPt_dxy5to50),
                TEfficiency(Prompt_L1MuPt10_GenMuPt_dxy50to100, GenMuPt_dxy50to100),
                targetDir + "Prompt_L1MuPt10_GenMuPt_dxy0to100.png", True)

    makeEffPlot(TEfficiency(Prompt_L1MuPt15_GenMuPt_dxy0to5, GenMuPt_dxy0to5),
                TEfficiency(Prompt_L1MuPt15_GenMuPt_dxy5to50, GenMuPt_dxy5to50),
                TEfficiency(Prompt_L1MuPt15_GenMuPt_dxy50to100, GenMuPt_dxy50to100),
                targetDir + "Prompt_L1MuPt15_GenMuPt_dxy0to100.png", True)

    makeEffPlot(TEfficiency(Prompt_L1MuPt20_GenMuPt_dxy0to5, GenMuPt_dxy0to5),
                TEfficiency(Prompt_L1MuPt20_GenMuPt_dxy5to50, GenMuPt_dxy5to50),
                TEfficiency(Prompt_L1MuPt20_GenMuPt_dxy50to100, GenMuPt_dxy50to100),
                targetDir + "Prompt_L1MuPt20_GenMuPt_dxy0to100.png", True)


    makeEffPlot(TEfficiency(Prompt_L1MuPt10_GenMuPt_dxy0to5_eta16to22, GenMuPt_dxy0to5_eta16to22),
                TEfficiency(Prompt_L1MuPt10_GenMuPt_dxy5to50_eta16to22, GenMuPt_dxy5to50_eta16to22),
                TEfficiency(Prompt_L1MuPt10_GenMuPt_dxy50to100_eta16to22, GenMuPt_dxy50to100_eta16to22),
                targetDir + "Prompt_L1MuPt10_GenMuPt_dxy0to100_eta16to22.png", True)

    makeEffPlot(TEfficiency(Prompt_L1MuPt15_GenMuPt_dxy0to5_eta16to22, GenMuPt_dxy0to5_eta16to22),
                TEfficiency(Prompt_L1MuPt15_GenMuPt_dxy5to50_eta16to22, GenMuPt_dxy5to50_eta16to22),
                TEfficiency(Prompt_L1MuPt15_GenMuPt_dxy50to100_eta16to22, GenMuPt_dxy50to100_eta16to22),
                targetDir + "Prompt_L1MuPt15_GenMuPt_dxy0to100_eta16to22.png", True)

    makeEffPlot(TEfficiency(Prompt_L1MuPt20_GenMuPt_dxy0to5_eta16to22, GenMuPt_dxy0to5_eta16to22),
                TEfficiency(Prompt_L1MuPt20_GenMuPt_dxy5to50_eta16to22, GenMuPt_dxy5to50_eta16to22),
                TEfficiency(Prompt_L1MuPt20_GenMuPt_dxy50to100_eta16to22, GenMuPt_dxy50to100_eta16to22),
                targetDir + "Prompt_L1MuPt20_GenMuPt_dxy0to100_eta16to22.png", True)


    makeEffPlot(TEfficiency(Prompt_L1MuPt10_GenMuPt_dxy0to5_eta16to22, GenMuPt_dxy0to5_eta16to22),
                TEfficiency(Prompt_L1MuPt10_GenMuPt_dxy5to50_eta16to22, GenMuPt_dxy5to50_eta16to22),
                None,
                targetDir + "Prompt_L1MuPt10_GenMuPt_dxy0to50_eta16to22.png", True)

    makeEffPlot(TEfficiency(Prompt_L1MuPt15_GenMuPt_dxy0to5_eta16to22, GenMuPt_dxy0to5_eta16to22),
                TEfficiency(Prompt_L1MuPt15_GenMuPt_dxy5to50_eta16to22, GenMuPt_dxy5to50_eta16to22),
                None,
                targetDir + "Prompt_L1MuPt15_GenMuPt_dxy0to50_eta16to22.png", True)

    makeEffPlot(TEfficiency(Prompt_L1MuPt20_GenMuPt_dxy0to5_eta16to22, GenMuPt_dxy0to5_eta16to22),
                TEfficiency(Prompt_L1MuPt20_GenMuPt_dxy5to50_eta16to22, GenMuPt_dxy5to50_eta16to22),
                None,
                targetDir + "Prompt_L1MuPt20_GenMuPt_dxy0to50_eta16to22.png", True)

    
    ## properly normalized bending angle plots DT
    makeEffPlot(TEfficiency(Displaced_L1MuPt10_GenMuPt_dxy0to5,    GenMuPt_DT1_DT4_dxy0to5),
                TEfficiency(Displaced_L1MuPt10_GenMuPt_dxy5to50,   GenMuPt_DT1_DT4_dxy5to50),
                TEfficiency(Displaced_L1MuPt10_GenMuPt_dxy50to100, GenMuPt_DT1_DT4_dxy50to100),
                targetDir + "Displaced_L1MuPt10_GenMuPt_DT1_DT4_dxy0to100.png", True)

    makeEffPlot(TEfficiency(Displaced_L1MuPt15_GenMuPt_dxy0to5,    GenMuPt_DT1_DT4_dxy0to5),
                TEfficiency(Displaced_L1MuPt15_GenMuPt_dxy5to50,   GenMuPt_DT1_DT4_dxy5to50),
                TEfficiency(Displaced_L1MuPt15_GenMuPt_dxy50to100, GenMuPt_DT1_DT4_dxy50to100),
                targetDir + "Displaced_L1MuPt15_GenMuPt_DT1_DT4_dxy0to100.png", True)

    makeEffPlot(TEfficiency(Displaced_L1MuPt20_GenMuPt_dxy0to5,    GenMuPt_DT1_DT4_dxy0to5),
                TEfficiency(Displaced_L1MuPt20_GenMuPt_dxy5to50,   GenMuPt_DT1_DT4_dxy5to50),
                TEfficiency(Displaced_L1MuPt20_GenMuPt_dxy50to100, GenMuPt_DT1_DT4_dxy50to100),
                targetDir + "Displaced_L1MuPt20_GenMuPt_DT1_DT4_dxy0to100.png", True)


    ## Direction based pT efficiency plots (with GEMs)
    makeEffPlot(myTEfficiency("Displaced_L1MuPt10_GenMuPt_GE11_ME11_GE21_ME21_dxy0to5_withoutLCTFit",    "GenMuPt_GE11_ME11_GE21_ME21_dxy0to5"),
                myTEfficiency("Displaced_L1MuPt10_GenMuPt_GE11_ME11_GE21_ME21_dxy5to50_withoutLCTFit",   "GenMuPt_GE11_ME11_GE21_ME21_dxy5to50"),
                myTEfficiency("Displaced_L1MuPt10_GenMuPt_GE11_ME11_GE21_ME21_dxy50to100_withoutLCTFit", "GenMuPt_GE11_ME11_GE21_ME21_dxy50to100"),
                targetDir + "Displaced_L1MuPt10_GenMuPt_GE11_ME11_GE21_ME21_dxy0to100_withoutLCTFit.png", True)

    makeEffPlot(myTEfficiency("Displaced_L1MuPt15_GenMuPt_GE11_ME11_GE21_ME21_dxy0to5_withoutLCTFit",    "GenMuPt_GE11_ME11_GE21_ME21_dxy0to5"),
                myTEfficiency("Displaced_L1MuPt15_GenMuPt_GE11_ME11_GE21_ME21_dxy5to50_withoutLCTFit",   "GenMuPt_GE11_ME11_GE21_ME21_dxy5to50"),
                myTEfficiency("Displaced_L1MuPt15_GenMuPt_GE11_ME11_GE21_ME21_dxy50to100_withoutLCTFit", "GenMuPt_GE11_ME11_GE21_ME21_dxy50to100"),
                targetDir + "Displaced_L1MuPt15_GenMuPt_GE11_ME11_GE21_ME21_dxy0to100_withoutLCTFit.png", True)

    makeEffPlot(myTEfficiency("Displaced_L1MuPt20_GenMuPt_GE11_ME11_GE21_ME21_dxy0to5_withoutLCTFit",    "GenMuPt_GE11_ME11_GE21_ME21_dxy0to5"),
                myTEfficiency("Displaced_L1MuPt20_GenMuPt_GE11_ME11_GE21_ME21_dxy5to50_withoutLCTFit",   "GenMuPt_GE11_ME11_GE21_ME21_dxy5to50"),
                myTEfficiency("Displaced_L1MuPt20_GenMuPt_GE11_ME11_GE21_ME21_dxy50to100_withoutLCTFit", "GenMuPt_GE11_ME11_GE21_ME21_dxy50to100"),
                targetDir + "Displaced_L1MuPt20_GenMuPt_GE11_ME11_GE21_ME21_dxy0to100_withoutLCTFit.png", True)


    makeEffPlot(myTEfficiency("Displaced_L1MuPt10_GenMuPt_GE11_ME11_GE21_ME21_dxy0to5_withoutLCTFit",    "GenMuPt_GE11_ME11_GE21_ME21_dxy0to5"),
                myTEfficiency("Displaced_L1MuPt10_GenMuPt_GE11_ME11_GE21_ME21_dxy5to50_withoutLCTFit",   "GenMuPt_GE11_ME11_GE21_ME21_dxy5to50"),
                None,
                targetDir + "Displaced_L1MuPt10_GenMuPt_GE11_ME11_GE21_ME21_dxy0to50_withoutLCTFit.png", True)

    makeEffPlot(myTEfficiency("Displaced_L1MuPt15_GenMuPt_GE11_ME11_GE21_ME21_dxy0to5_withoutLCTFit",    "GenMuPt_GE11_ME11_GE21_ME21_dxy0to5"),
                myTEfficiency("Displaced_L1MuPt15_GenMuPt_GE11_ME11_GE21_ME21_dxy5to50_withoutLCTFit",   "GenMuPt_GE11_ME11_GE21_ME21_dxy5to50"),
                None,
                targetDir + "Displaced_L1MuPt15_GenMuPt_GE11_ME11_GE21_ME21_dxy0to50_withoutLCTFit.png", True)

    makeEffPlot(myTEfficiency("Displaced_L1MuPt20_GenMuPt_GE11_ME11_GE21_ME21_dxy0to5_withoutLCTFit",    "GenMuPt_GE11_ME11_GE21_ME21_dxy0to5"),
                myTEfficiency("Displaced_L1MuPt20_GenMuPt_GE11_ME11_GE21_ME21_dxy5to50_withoutLCTFit",   "GenMuPt_GE11_ME11_GE21_ME21_dxy5to50"),
                None,
                targetDir + "Displaced_L1MuPt20_GenMuPt_GE11_ME11_GE21_ME21_dxy0to50_withoutLCTFit.png", True)

    

    makeEffPlot(myTEfficiency("Displaced_L1MuPt10_GenMuPt_GE11_ME11_GE21_ME21_dxy0to5_withLCTFit",    "GenMuPt_GE11_ME11_GE21_ME21_dxy0to5"),
                myTEfficiency("Displaced_L1MuPt10_GenMuPt_GE11_ME11_GE21_ME21_dxy5to50_withLCTFit",   "GenMuPt_GE11_ME11_GE21_ME21_dxy5to50"),
                myTEfficiency("Displaced_L1MuPt10_GenMuPt_GE11_ME11_GE21_ME21_dxy50to100_withLCTFit", "GenMuPt_GE11_ME11_GE21_ME21_dxy50to100"),
                targetDir + "Displaced_L1MuPt10_GenMuPt_GE11_ME11_GE21_ME21_dxy0to100_withLCTFit.png", True)

    makeEffPlot(myTEfficiency("Displaced_L1MuPt15_GenMuPt_GE11_ME11_GE21_ME21_dxy0to5_withLCTFit",    "GenMuPt_GE11_ME11_GE21_ME21_dxy0to5"),
                myTEfficiency("Displaced_L1MuPt15_GenMuPt_GE11_ME11_GE21_ME21_dxy5to50_withLCTFit",   "GenMuPt_GE11_ME11_GE21_ME21_dxy5to50"),
                myTEfficiency("Displaced_L1MuPt15_GenMuPt_GE11_ME11_GE21_ME21_dxy50to100_withLCTFit", "GenMuPt_GE11_ME11_GE21_ME21_dxy50to100"),
                targetDir + "Displaced_L1MuPt15_GenMuPt_GE11_ME11_GE21_ME21_dxy0to100_withLCTFit.png", True)

    makeEffPlot(myTEfficiency("Displaced_L1MuPt20_GenMuPt_GE11_ME11_GE21_ME21_dxy0to5_withLCTFit",    "GenMuPt_GE11_ME11_GE21_ME21_dxy0to5"),
                myTEfficiency("Displaced_L1MuPt20_GenMuPt_GE11_ME11_GE21_ME21_dxy5to50_withLCTFit",   "GenMuPt_GE11_ME11_GE21_ME21_dxy5to50"),
                myTEfficiency("Displaced_L1MuPt20_GenMuPt_GE11_ME11_GE21_ME21_dxy50to100_withLCTFit", "GenMuPt_GE11_ME11_GE21_ME21_dxy50to100"),
                targetDir + "Displaced_L1MuPt20_GenMuPt_GE11_ME11_GE21_ME21_dxy0to100_withLCTFit.png", True)


    makeEffPlot(myTEfficiency("Displaced_L1MuPt10_GenMuPt_GE11_ME11_GE21_ME21_dxy0to5_withLCTFit",    "GenMuPt_GE11_ME11_GE21_ME21_dxy0to5"),
                myTEfficiency("Displaced_L1MuPt10_GenMuPt_GE11_ME11_GE21_ME21_dxy5to50_withLCTFit",   "GenMuPt_GE11_ME11_GE21_ME21_dxy5to50"),
                None,
                targetDir + "Displaced_L1MuPt10_GenMuPt_GE11_ME11_GE21_ME21_dxy0to50_withLCTFit.png", True)

    makeEffPlot(myTEfficiency("Displaced_L1MuPt15_GenMuPt_GE11_ME11_GE21_ME21_dxy0to5_withLCTFit",    "GenMuPt_GE11_ME11_GE21_ME21_dxy0to5"),
                myTEfficiency("Displaced_L1MuPt15_GenMuPt_GE11_ME11_GE21_ME21_dxy5to50_withLCTFit",   "GenMuPt_GE11_ME11_GE21_ME21_dxy5to50"),
                None,
                targetDir + "Displaced_L1MuPt15_GenMuPt_GE11_ME11_GE21_ME21_dxy0to50_withLCTFit.png", True)

    makeEffPlot(myTEfficiency("Displaced_L1MuPt20_GenMuPt_GE11_ME11_GE21_ME21_dxy0to5_withLCTFit",    "GenMuPt_GE11_ME11_GE21_ME21_dxy0to5"),
                myTEfficiency("Displaced_L1MuPt20_GenMuPt_GE11_ME11_GE21_ME21_dxy5to50_withLCTFit",   "GenMuPt_GE11_ME11_GE21_ME21_dxy5to50"),
                None,
                targetDir + "Displaced_L1MuPt20_GenMuPt_GE11_ME11_GE21_ME21_dxy0to50_withLCTFit.png", True)



    ## position based pT efficiency plots (ME1 ME2 ME3)
    makeEffPlot(myTEfficiency("Displaced_L1MuPt10_GenMuPt_ME1_ME2_ME3_dxy0to5_withoutLCTFit",    "GenMuPt_ME1_ME2_ME3_dxy0to5"),
                myTEfficiency("Displaced_L1MuPt10_GenMuPt_ME1_ME2_ME3_dxy5to50_withoutLCTFit",   "GenMuPt_ME1_ME2_ME3_dxy5to50"),
                myTEfficiency("Displaced_L1MuPt10_GenMuPt_ME1_ME2_ME3_dxy50to100_withoutLCTFit", "GenMuPt_ME1_ME2_ME3_dxy50to100"),
                targetDir + "Displaced_L1MuPt10_GenMuPt_ME1_ME2_ME3_dxy0to100_withoutLCTFit.png", True)

    makeEffPlot(myTEfficiency("Displaced_L1MuPt15_GenMuPt_ME1_ME2_ME3_dxy0to5_withoutLCTFit",    "GenMuPt_ME1_ME2_ME3_dxy0to5"),
                myTEfficiency("Displaced_L1MuPt15_GenMuPt_ME1_ME2_ME3_dxy5to50_withoutLCTFit",   "GenMuPt_ME1_ME2_ME3_dxy5to50"),
                myTEfficiency("Displaced_L1MuPt15_GenMuPt_ME1_ME2_ME3_dxy50to100_withoutLCTFit", "GenMuPt_ME1_ME2_ME3_dxy50to100"),
                targetDir + "Displaced_L1MuPt15_GenMuPt_ME1_ME2_ME3_dxy0to100_withoutLCTFit.png", True)

    makeEffPlot(myTEfficiency("Displaced_L1MuPt20_GenMuPt_ME1_ME2_ME3_dxy0to5_withoutLCTFit",    "GenMuPt_ME1_ME2_ME3_dxy0to5"),
                myTEfficiency("Displaced_L1MuPt20_GenMuPt_ME1_ME2_ME3_dxy5to50_withoutLCTFit",   "GenMuPt_ME1_ME2_ME3_dxy5to50"),
                myTEfficiency("Displaced_L1MuPt20_GenMuPt_ME1_ME2_ME3_dxy50to100_withoutLCTFit", "GenMuPt_ME1_ME2_ME3_dxy50to100"),
                targetDir + "Displaced_L1MuPt20_GenMuPt_ME1_ME2_ME3_dxy0to100_withoutLCTFit.png", True)

    
    makeEffPlot(myTEfficiency("Displaced_L1MuPt10_GenMuPt_ME1_ME2_ME3_dxy0to5_withoutLCTFit",    "GenMuPt_ME1_ME2_ME3_dxy0to5"),
                myTEfficiency("Displaced_L1MuPt10_GenMuPt_ME1_ME2_ME3_dxy5to50_withoutLCTFit",   "GenMuPt_ME1_ME2_ME3_dxy5to50"),
                None,
                targetDir + "Displaced_L1MuPt10_GenMuPt_ME1_ME2_ME3_dxy0to50_withoutLCTFit.png", True)

    makeEffPlot(myTEfficiency("Displaced_L1MuPt15_GenMuPt_ME1_ME2_ME3_dxy0to5_withoutLCTFit",    "GenMuPt_ME1_ME2_ME3_dxy0to5"),
                myTEfficiency("Displaced_L1MuPt15_GenMuPt_ME1_ME2_ME3_dxy5to50_withoutLCTFit",   "GenMuPt_ME1_ME2_ME3_dxy5to50"),
                None,
                targetDir + "Displaced_L1MuPt15_GenMuPt_ME1_ME2_ME3_dxy0to50_withoutLCTFit.png", True)

    makeEffPlot(myTEfficiency("Displaced_L1MuPt20_GenMuPt_ME1_ME2_ME3_dxy0to5_withoutLCTFit",    "GenMuPt_ME1_ME2_ME3_dxy0to5"),
                myTEfficiency("Displaced_L1MuPt20_GenMuPt_ME1_ME2_ME3_dxy5to50_withoutLCTFit",   "GenMuPt_ME1_ME2_ME3_dxy5to50"),
                None,
                targetDir + "Displaced_L1MuPt20_GenMuPt_ME1_ME2_ME3_dxy0to50_withoutLCTFit.png", True)




    makeEffPlot(myTEfficiency("Displaced_L1MuPt10_GenMuPt_ME1_ME2_ME3_dxy0to5_withLCTFit",    "GenMuPt_ME1_ME2_ME3_dxy0to5"),
                myTEfficiency("Displaced_L1MuPt10_GenMuPt_ME1_ME2_ME3_dxy5to50_withLCTFit",   "GenMuPt_ME1_ME2_ME3_dxy5to50"),
                myTEfficiency("Displaced_L1MuPt10_GenMuPt_ME1_ME2_ME3_dxy50to100_withLCTFit", "GenMuPt_ME1_ME2_ME3_dxy50to100"),
                targetDir + "Displaced_L1MuPt10_GenMuPt_ME1_ME2_ME3_dxy0to100_withLCTFit.png", True)

    makeEffPlot(myTEfficiency("Displaced_L1MuPt15_GenMuPt_ME1_ME2_ME3_dxy0to5_withLCTFit",    "GenMuPt_ME1_ME2_ME3_dxy0to5"),
                myTEfficiency("Displaced_L1MuPt15_GenMuPt_ME1_ME2_ME3_dxy5to50_withLCTFit",   "GenMuPt_ME1_ME2_ME3_dxy5to50"),
                myTEfficiency("Displaced_L1MuPt15_GenMuPt_ME1_ME2_ME3_dxy50to100_withLCTFit", "GenMuPt_ME1_ME2_ME3_dxy50to100"),
                targetDir + "Displaced_L1MuPt15_GenMuPt_ME1_ME2_ME3_dxy0to100_withLCTFit.png", True)

    makeEffPlot(myTEfficiency("Displaced_L1MuPt20_GenMuPt_ME1_ME2_ME3_dxy0to5_withLCTFit",    "GenMuPt_ME1_ME2_ME3_dxy0to5"),
                myTEfficiency("Displaced_L1MuPt20_GenMuPt_ME1_ME2_ME3_dxy5to50_withLCTFit",   "GenMuPt_ME1_ME2_ME3_dxy5to50"),
                myTEfficiency("Displaced_L1MuPt20_GenMuPt_ME1_ME2_ME3_dxy50to100_withLCTFit", "GenMuPt_ME1_ME2_ME3_dxy50to100"),
                targetDir + "Displaced_L1MuPt20_GenMuPt_ME1_ME2_ME3_dxy0to100_withLCTFit.png", True)

    
    makeEffPlot(myTEfficiency("Displaced_L1MuPt10_GenMuPt_ME1_ME2_ME3_dxy0to5_withLCTFit",    "GenMuPt_ME1_ME2_ME3_dxy0to5"),
                myTEfficiency("Displaced_L1MuPt10_GenMuPt_ME1_ME2_ME3_dxy5to50_withLCTFit",   "GenMuPt_ME1_ME2_ME3_dxy5to50"),
                None,
                targetDir + "Displaced_L1MuPt10_GenMuPt_ME1_ME2_ME3_dxy0to50_withLCTFit.png", True)

    makeEffPlot(myTEfficiency("Displaced_L1MuPt15_GenMuPt_ME1_ME2_ME3_dxy0to5_withLCTFit",    "GenMuPt_ME1_ME2_ME3_dxy0to5"),
                myTEfficiency("Displaced_L1MuPt15_GenMuPt_ME1_ME2_ME3_dxy5to50_withLCTFit",   "GenMuPt_ME1_ME2_ME3_dxy5to50"),
                None,
                targetDir + "Displaced_L1MuPt15_GenMuPt_ME1_ME2_ME3_dxy0to50_withLCTFit.png", True)

    makeEffPlot(myTEfficiency("Displaced_L1MuPt20_GenMuPt_ME1_ME2_ME3_dxy0to5_withLCTFit",    "GenMuPt_ME1_ME2_ME3_dxy0to5"),
                myTEfficiency("Displaced_L1MuPt20_GenMuPt_ME1_ME2_ME3_dxy5to50_withLCTFit",   "GenMuPt_ME1_ME2_ME3_dxy5to50"),
                None,
                targetDir + "Displaced_L1MuPt20_GenMuPt_ME1_ME2_ME3_dxy0to50_withLCTFit.png", True)


  displacedTriggerEfficiency()
  exit()

  def makedEtadPhidRPlots():
    ## deta, dphi, dR plot for L1Tk
    draw_1D(ch, "L1Tk_eta_prop", targetDir + "L1Tk_eta_prop", "#eta_{prop}; #eta_{prop}; Entries", "(100,-2.5,2.5)", cut="", opt = "")
    draw_1D(ch, "L1Tk_phi_prop", targetDir + "L1Tk_phi_prop", "#phi_{prop}; #phi_{prop}; Entries", "(100,-2.5,2.5)", cut="", opt = "")

    draw_1D(ch, "L1Tk_deta_prop", targetDir + "L1Tk_deta_prop", "d#eta; d#eta; Entries", "(100,0.,1.)", cut="", opt = "")
    draw_1D(ch, "L1Tk_dphi_prop", targetDir + "L1Tk_dphi_prop", "d#phi; d#phi; Entries", "(100,0.,1.)", cut="", opt = "")
    draw_1D(ch, "L1Tk_dR_prop", targetDir + "L1Tk_dR_prop", "dR; dR; Entries", "(100,0.,1.)", cut="", opt = "")

    draw_1D(ch, "L1Tk_deta_prop", targetDir + "L1Tk_deta_prop_pt5", "d#eta; d#eta; Entries", "(100,0.,1.)", cut="L1Tk_pt>5", opt = "")
    draw_1D(ch, "L1Tk_dphi_prop", targetDir + "L1Tk_dphi_prop_pt5", "d#phi; d#phi; Entries", "(100,0.,1.)", cut="L1Tk_pt>5", opt = "")
    draw_1D(ch, "L1Tk_dR_prop", targetDir + "L1Tk_dR_prop_pt5", "dR; dR; Entries", "(100,0.,1.)", cut="L1Tk_pt>5", opt = "")

    draw_1D(ch, "L1Tk_deta_prop", targetDir + "L1Tk_deta_prop_pt20", "d#eta; d#eta; Entries", "(100,0.,1.)", cut="L1Tk_pt>20", opt = "")
    draw_1D(ch, "L1Tk_dphi_prop", targetDir + "L1Tk_dphi_prop_pt20", "d#phi; d#phi; Entries", "(100,0.,1.)", cut="L1Tk_pt>20", opt = "")
    draw_1D(ch, "L1Tk_dR_prop", targetDir + "L1Tk_dR_prop_pt20", "dR; dR; Entries", "(100,0.,1.)", cut="L1Tk_pt>20", opt = "")

    draw_1D(ch, "L1Tk_deta_prop", targetDir + "L1Tk_deta_prop_pt30", "d#eta; d#eta; Entries", "(100,0.,1.)", cut="L1Tk_pt>30", opt = "")
    draw_1D(ch, "L1Tk_dphi_prop", targetDir + "L1Tk_dphi_prop_pt30", "d#phi; d#phi; Entries", "(100,0.,1.)", cut="L1Tk_pt>30", opt = "")
    draw_1D(ch, "L1Tk_dR_prop", targetDir + "L1Tk_dR_prop_pt30", "dR; dR; Entries", "(100,0.,1.)", cut="L1Tk_pt>30", opt = "")

  if not eff and False:
    makedEtadPhidRPlots()

  def makeRateVsPtHistogram():

    h_single_L1Mu_rate = TH1F("h_single_L1Mu_rate"," ",len(myptbin)-1, myptbin)
    h_single_displaced_rate = TH1F("h_single_displaced_rate"," ",len(myptbin)-1, myptbin)
    h_single_displaced_rate_dR0p4_L1TkPt2 = TH1F("h_single_displaced_rate_dR0p4_L1TkPt2"," ",len(myptbin)-1, myptbin)
    h_single_displaced_rate_dR0p4_L1TkPt2p5 = TH1F("h_single_displaced_rate_dR0p4_L1TkPt2p5"," ",len(myptbin)-1, myptbin)
    h_single_displaced_rate_dR0p4_L1TkPt3 = TH1F("h_single_displaced_rate_dR0p4_L1TkPt3"," ",len(myptbin)-1, myptbin)
    h_single_displaced_rate_dR0p4_L1TkPt4 = TH1F("h_single_displaced_rate_dR0p4_L1TkPt4"," ",len(myptbin)-1, myptbin)

    h_single_displaced_rate_dR0p3_L1TkPt2 = TH1F("h_single_displaced_rate_dR0p3_L1TkPt2"," ",len(myptbin)-1, myptbin)
    h_single_displaced_rate_dR0p3_L1TkPt2p5 = TH1F("h_single_displaced_rate_dR0p3_L1TkPt2p5"," ",len(myptbin)-1, myptbin)
    h_single_displaced_rate_dR0p3_L1TkPt3 = TH1F("h_single_displaced_rate_dR0p3_L1TkPt3"," ",len(myptbin)-1, myptbin)
    h_single_displaced_rate_dR0p3_L1TkPt4 = TH1F("h_single_displaced_rate_dR0p3_L1TkPt4"," ",len(myptbin)-1, myptbin)

    h_single_displaced_rate_dR0p2_L1TkPt2 = TH1F("h_single_displaced_rate_dR0p2_L1TkPt2"," ",len(myptbin)-1, myptbin)
    h_single_displaced_rate_dR0p2_L1TkPt2p5 = TH1F("h_single_displaced_rate_dR0p2_L1TkPt2p5"," ",len(myptbin)-1, myptbin)
    h_single_displaced_rate_dR0p2_L1TkPt3 = TH1F("h_single_displaced_rate_dR0p2_L1TkPt3"," ",len(myptbin)-1, myptbin)
    h_single_displaced_rate_dR0p2_L1TkPt4 = TH1F("h_single_displaced_rate_dR0p2_L1TkPt4"," ",len(myptbin)-1, myptbin)

    h_single_displaced_rate_dR0p12_L1TkPt2 = TH1F("h_single_displaced_rate_dR0p12_L1TkPt2"," ",len(myptbin)-1, myptbin)
    h_single_displaced_rate_dR0p12_L1TkPt2p5 = TH1F("h_single_displaced_rate_dR0p12_L1TkPt2p5"," ",len(myptbin)-1, myptbin)
    h_single_displaced_rate_dR0p12_L1TkPt3 = TH1F("h_single_displaced_rate_dR0p12_L1TkPt3"," ",len(myptbin)-1, myptbin)
    h_single_displaced_rate_dR0p12_L1TkPt4 = TH1F("h_single_displaced_rate_dR0p12_L1TkPt4"," ",len(myptbin)-1, myptbin)
    
    for k in range(0,ch.GetEntries()):
      if k%1000==0: print "Processing event", k
#    for k in range(0,100):
      ch.GetEntry(k)
      
      treeHits = ch
      ## get the max value of the momentum
      pts = list(treeHits.L1Mu_pt)

      if len(pts)>=1:
              
        def getMaxPts():
          maxPt1, maxPt2, maxPt3, maxPt4, maxPt5 = 0., 0., 0., 0., 0., 

          maxPt_trig_dR0p4_L1TkPt4 = 0.
          maxPt_trig_dR0p4_L1TkPt3 = 0.
          maxPt_trig_dR0p4_L1TkPt2p5 = 0.
          maxPt_trig_dR0p4_L1TkPt2 = 0.
          
          maxPt_trig_dR0p3_L1TkPt4 = 0.
          maxPt_trig_dR0p3_L1TkPt3 = 0.
          maxPt_trig_dR0p3_L1TkPt2p5 = 0.
          maxPt_trig_dR0p3_L1TkPt2 = 0.

          maxPt_trig_dR0p2_L1TkPt4 = 0.
          maxPt_trig_dR0p2_L1TkPt3 = 0.
          maxPt_trig_dR0p2_L1TkPt2p5 = 0.
          maxPt_trig_dR0p2_L1TkPt2 = 0.
          
          maxPt_trig_dR0p12_L1TkPt4 = 0.
          maxPt_trig_dR0p12_L1TkPt3 = 0.
          maxPt_trig_dR0p12_L1TkPt2p5 = 0.
          maxPt_trig_dR0p12_L1TkPt2 = 0.

          for i in range(0,len(pts)):
            L1Mu_pt = treeHits.L1Mu_pt[i]
            L1Mu_eta = treeHits.L1Mu_eta[i]
            L1Mu_phi = treeHits.L1Mu_phi[i]
            L1Mu_bx = treeHits.L1Mu_bx[i]
            L1Mu_quality = treeHits.L1Mu_quality[i]

            L1Mu_L1Tk_dR_min = treeHits.L1Mu_L1Tk_dR_prop[i]
            L1Mu_L1Tk_pt = treeHits.L1Mu_L1Tk_pt_prop[i]

            if L1Mu_bx==0:
              print k,i, "pt", L1Mu_pt, "eta", L1Mu_eta, "phi", L1Mu_phi, "bx", L1Mu_bx, "quality", L1Mu_quality


            unMatched_dR0p4_L1TkPt4 = False
            unMatched_dR0p4_L1TkPt3 = False
            unMatched_dR0p4_L1TkPt2p5 = False
            unMatched_dR0p4_L1TkPt2 = False

            unMatched_dR0p3_L1TkPt4 = False
            unMatched_dR0p3_L1TkPt3 = False
            unMatched_dR0p3_L1TkPt2p5 = False
            unMatched_dR0p3_L1TkPt2 = False

            unMatched_dR0p2_L1TkPt4 = False
            unMatched_dR0p2_L1TkPt3 = False
            unMatched_dR0p2_L1TkPt2p5 = False
            unMatched_dR0p2_L1TkPt2 = False

            unMatched_dR0p12_L1TkPt4 = False
            unMatched_dR0p12_L1TkPt3 = False
            unMatched_dR0p12_L1TkPt2p5 = False
            unMatched_dR0p12_L1TkPt2 = False

            ## matched 
            matched = L1Mu_L1Tk_dR_min <= 0.12 and L1Mu_quality >= 4
            matched = matched and L1Mu_L1Tk_pt>=MatchingL1TkMinPt
            
            ## unmatched 
            if L1Mu_L1Tk_dR_min <= 0.4 and L1Mu_L1Tk_pt>=4:   unMatched_dR0p4_L1TkPt4 = True
            if L1Mu_L1Tk_dR_min <= 0.4 and L1Mu_L1Tk_pt>=3:   unMatched_dR0p4_L1TkPt3 = True
            if L1Mu_L1Tk_dR_min <= 0.4 and L1Mu_L1Tk_pt>=2.5: unMatched_dR0p4_L1TkPt2p5 = True
            if L1Mu_L1Tk_dR_min <= 0.4 and L1Mu_L1Tk_pt>=2:   unMatched_dR0p4_L1TkPt2 = True

            if L1Mu_L1Tk_dR_min <= 0.3 and L1Mu_L1Tk_pt>=4:   unMatched_dR0p3_L1TkPt4 = True
            if L1Mu_L1Tk_dR_min <= 0.3 and L1Mu_L1Tk_pt>=3:   unMatched_dR0p3_L1TkPt3 = True
            if L1Mu_L1Tk_dR_min <= 0.3 and L1Mu_L1Tk_pt>=2.5: unMatched_dR0p3_L1TkPt2p5 = True
            if L1Mu_L1Tk_dR_min <= 0.3 and L1Mu_L1Tk_pt>=2:   unMatched_dR0p3_L1TkPt2 = True

            if L1Mu_L1Tk_dR_min <= 0.2 and L1Mu_L1Tk_pt>=4:   unMatched_dR0p2_L1TkPt4 = True
            if L1Mu_L1Tk_dR_min <= 0.2 and L1Mu_L1Tk_pt>=3:   unMatched_dR0p2_L1TkPt3 = True
            if L1Mu_L1Tk_dR_min <= 0.2 and L1Mu_L1Tk_pt>=2.5: unMatched_dR0p2_L1TkPt2p5 = True
            if L1Mu_L1Tk_dR_min <= 0.2 and L1Mu_L1Tk_pt>=2:   unMatched_dR0p2_L1TkPt2 = True

            if L1Mu_L1Tk_dR_min <= 0.12 and L1Mu_L1Tk_pt>=4:   unMatched_dR0p12_L1TkPt4 = True
            if L1Mu_L1Tk_dR_min <= 0.12 and L1Mu_L1Tk_pt>=3:   unMatched_dR0p12_L1TkPt3 = True
            if L1Mu_L1Tk_dR_min <= 0.12 and L1Mu_L1Tk_pt>=2.5: unMatched_dR0p12_L1TkPt2p5 = True
            if L1Mu_L1Tk_dR_min <= 0.12 and L1Mu_L1Tk_pt>=2:   unMatched_dR0p12_L1TkPt2 = True

            common = (abs(L1Mu_bx) == 0) and (L1Mu_quality >= 4) and L1Mu_pt>=0
            trigL1Mu = common
            trig_dR0p4_L1TkPt4 =   (not matched) and (not unMatched_dR0p4_L1TkPt4) and common
            trig_dR0p4_L1TkPt3 =   (not matched) and (not unMatched_dR0p4_L1TkPt3) and common
            trig_dR0p4_L1TkPt2p5 = (not matched) and (not unMatched_dR0p4_L1TkPt2p5) and common
            trig_dR0p4_L1TkPt2 =   (not matched) and (not unMatched_dR0p4_L1TkPt2) and common

            trig_dR0p3_L1TkPt4 =   (not matched) and (not unMatched_dR0p3_L1TkPt4) and common
            trig_dR0p3_L1TkPt3 =   (not matched) and (not unMatched_dR0p3_L1TkPt3) and common
            trig_dR0p3_L1TkPt2p5 = (not matched) and (not unMatched_dR0p3_L1TkPt2p5) and common
            trig_dR0p3_L1TkPt2 =   (not matched) and (not unMatched_dR0p3_L1TkPt2) and common

            trig_dR0p2_L1TkPt4 =   (not matched) and (not unMatched_dR0p2_L1TkPt4) and common
            trig_dR0p2_L1TkPt3 =   (not matched) and (not unMatched_dR0p2_L1TkPt3) and common
            trig_dR0p2_L1TkPt2p5 = (not matched) and (not unMatched_dR0p2_L1TkPt2p5) and common
            trig_dR0p2_L1TkPt2 =   (not matched) and (not unMatched_dR0p2_L1TkPt2) and common

            trig_dR0p12_L1TkPt4 =   (not matched) and (not unMatched_dR0p12_L1TkPt4) and common
            trig_dR0p12_L1TkPt3 =   (not matched) and (not unMatched_dR0p12_L1TkPt3) and common
            trig_dR0p12_L1TkPt2p5 = (not matched) and (not unMatched_dR0p12_L1TkPt2p5) and common
            trig_dR0p12_L1TkPt2 =   (not matched) and (not unMatched_dR0p12_L1TkPt2) and common


            if trigL1Mu                         and L1Mu_pt > maxPt1:                                     maxPt1 = L1Mu_pt

            if trig_dR0p4_L1TkPt4               and L1Mu_pt > maxPt_trig_dR0p4_L1TkPt4: maxPt_trig_dR0p4_L1TkPt4 = L1Mu_pt
            if trig_dR0p3_L1TkPt4               and L1Mu_pt > maxPt_trig_dR0p3_L1TkPt4: maxPt_trig_dR0p3_L1TkPt4 = L1Mu_pt
            if trig_dR0p2_L1TkPt4               and L1Mu_pt > maxPt_trig_dR0p2_L1TkPt4: maxPt_trig_dR0p2_L1TkPt4 = L1Mu_pt
            if trig_dR0p12_L1TkPt4              and L1Mu_pt > maxPt_trig_dR0p12_L1TkPt4: maxPt_trig_dR0p12_L1TkPt4 = L1Mu_pt

            if trig_dR0p4_L1TkPt3               and L1Mu_pt > maxPt_trig_dR0p4_L1TkPt3: maxPt_trig_dR0p4_L1TkPt3 = L1Mu_pt
            if trig_dR0p3_L1TkPt3               and L1Mu_pt > maxPt_trig_dR0p3_L1TkPt3: maxPt_trig_dR0p3_L1TkPt3 = L1Mu_pt
            if trig_dR0p2_L1TkPt3               and L1Mu_pt > maxPt_trig_dR0p2_L1TkPt3: maxPt_trig_dR0p2_L1TkPt3 = L1Mu_pt
            if trig_dR0p12_L1TkPt3              and L1Mu_pt > maxPt_trig_dR0p12_L1TkPt3: maxPt_trig_dR0p12_L1TkPt3 = L1Mu_pt

            if trig_dR0p4_L1TkPt2p5               and L1Mu_pt > maxPt_trig_dR0p4_L1TkPt2p5: maxPt_trig_dR0p4_L1TkPt2p5 = L1Mu_pt
            if trig_dR0p3_L1TkPt2p5               and L1Mu_pt > maxPt_trig_dR0p3_L1TkPt2p5: maxPt_trig_dR0p3_L1TkPt2p5 = L1Mu_pt
            if trig_dR0p2_L1TkPt2p5               and L1Mu_pt > maxPt_trig_dR0p2_L1TkPt2p5: maxPt_trig_dR0p2_L1TkPt2p5 = L1Mu_pt
            if trig_dR0p12_L1TkPt2p5              and L1Mu_pt > maxPt_trig_dR0p12_L1TkPt2p5: maxPt_trig_dR0p12_L1TkPt2p5 = L1Mu_pt

            if trig_dR0p4_L1TkPt2               and L1Mu_pt > maxPt_trig_dR0p4_L1TkPt2: maxPt_trig_dR0p4_L1TkPt2 = L1Mu_pt
            if trig_dR0p3_L1TkPt2               and L1Mu_pt > maxPt_trig_dR0p3_L1TkPt2: maxPt_trig_dR0p3_L1TkPt2 = L1Mu_pt
            if trig_dR0p2_L1TkPt2               and L1Mu_pt > maxPt_trig_dR0p2_L1TkPt2: maxPt_trig_dR0p2_L1TkPt2 = L1Mu_pt
            if trig_dR0p12_L1TkPt2              and L1Mu_pt > maxPt_trig_dR0p12_L1TkPt2: maxPt_trig_dR0p12_L1TkPt2 = L1Mu_pt

          return maxPt1, maxPt_trig_dR0p4_L1TkPt4, maxPt_trig_dR0p4_L1TkPt3, maxPt_trig_dR0p4_L1TkPt2p5, maxPt_trig_dR0p4_L1TkPt2, maxPt_trig_dR0p3_L1TkPt4, maxPt_trig_dR0p3_L1TkPt3, maxPt_trig_dR0p3_L1TkPt2p5, maxPt_trig_dR0p3_L1TkPt2, maxPt_trig_dR0p2_L1TkPt4, maxPt_trig_dR0p2_L1TkPt3, maxPt_trig_dR0p2_L1TkPt2p5, maxPt_trig_dR0p2_L1TkPt2, maxPt_trig_dR0p12_L1TkPt4, maxPt_trig_dR0p12_L1TkPt3, maxPt_trig_dR0p12_L1TkPt2p5, maxPt_trig_dR0p12_L1TkPt2

        
        maxPt1, maxPt_trig_dR0p4_L1TkPt4, maxPt_trig_dR0p4_L1TkPt3, maxPt_trig_dR0p4_L1TkPt2p5, maxPt_trig_dR0p4_L1TkPt2, maxPt_trig_dR0p3_L1TkPt4, maxPt_trig_dR0p3_L1TkPt3, maxPt_trig_dR0p3_L1TkPt2p5, maxPt_trig_dR0p3_L1TkPt2, maxPt_trig_dR0p2_L1TkPt4, maxPt_trig_dR0p2_L1TkPt3, maxPt_trig_dR0p2_L1TkPt2p5, maxPt_trig_dR0p2_L1TkPt2, maxPt_trig_dR0p12_L1TkPt4, maxPt_trig_dR0p12_L1TkPt3, maxPt_trig_dR0p12_L1TkPt2p5, maxPt_trig_dR0p12_L1TkPt2 = getMaxPts()
        
        if (maxPt1>0): h_single_L1Mu_rate.Fill(maxPt1)
        if (maxPt_trig_dR0p4_L1TkPt4>0): h_single_displaced_rate_dR0p4_L1TkPt4.Fill(maxPt_trig_dR0p4_L1TkPt4)
        if (maxPt_trig_dR0p4_L1TkPt3>0): h_single_displaced_rate_dR0p4_L1TkPt3.Fill(maxPt_trig_dR0p4_L1TkPt3)
        if (maxPt_trig_dR0p4_L1TkPt2p5>0): h_single_displaced_rate_dR0p4_L1TkPt2p5.Fill(maxPt_trig_dR0p4_L1TkPt2p5)
        if (maxPt_trig_dR0p4_L1TkPt2>0): h_single_displaced_rate_dR0p4_L1TkPt2.Fill(maxPt_trig_dR0p4_L1TkPt2)

        if (maxPt_trig_dR0p3_L1TkPt4>0): h_single_displaced_rate_dR0p3_L1TkPt4.Fill(maxPt_trig_dR0p3_L1TkPt4)
        if (maxPt_trig_dR0p3_L1TkPt3>0): h_single_displaced_rate_dR0p3_L1TkPt3.Fill(maxPt_trig_dR0p3_L1TkPt3)
        if (maxPt_trig_dR0p3_L1TkPt2p5>0): h_single_displaced_rate_dR0p3_L1TkPt2p5.Fill(maxPt_trig_dR0p3_L1TkPt2p5)
        if (maxPt_trig_dR0p3_L1TkPt2>0): h_single_displaced_rate_dR0p3_L1TkPt2.Fill(maxPt_trig_dR0p3_L1TkPt2)

        if (maxPt_trig_dR0p2_L1TkPt4>0): h_single_displaced_rate_dR0p2_L1TkPt4.Fill(maxPt_trig_dR0p2_L1TkPt4)
        if (maxPt_trig_dR0p2_L1TkPt3>0): h_single_displaced_rate_dR0p2_L1TkPt3.Fill(maxPt_trig_dR0p2_L1TkPt3)
        if (maxPt_trig_dR0p2_L1TkPt2p5>0): h_single_displaced_rate_dR0p2_L1TkPt2p5.Fill(maxPt_trig_dR0p2_L1TkPt2p5)
        if (maxPt_trig_dR0p2_L1TkPt2>0): h_single_displaced_rate_dR0p2_L1TkPt2.Fill(maxPt_trig_dR0p2_L1TkPt2)

        if (maxPt_trig_dR0p12_L1TkPt4>0): h_single_displaced_rate_dR0p12_L1TkPt4.Fill(maxPt_trig_dR0p12_L1TkPt4)
        if (maxPt_trig_dR0p12_L1TkPt3>0): h_single_displaced_rate_dR0p12_L1TkPt3.Fill(maxPt_trig_dR0p12_L1TkPt3)
        if (maxPt_trig_dR0p12_L1TkPt2p5>0): h_single_displaced_rate_dR0p12_L1TkPt2p5.Fill(maxPt_trig_dR0p12_L1TkPt2p5)
        if (maxPt_trig_dR0p12_L1TkPt2>0): h_single_displaced_rate_dR0p12_L1TkPt2.Fill(maxPt_trig_dR0p12_L1TkPt2)

    def makePlots(h1, h2, h3, h4, h5, isolation_cone, title):
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

      b1 = TH1F("b1","b1",29,myptbin)
      b1.GetYaxis().SetRangeUser(.1,10000)
      b1.GetYaxis().SetTitleOffset(1.2)
      b1.GetYaxis().SetNdivisions(520)
      b1.GetYaxis().SetTitle("L1Mu Trigger Rate [kHz]")
      b1.GetXaxis().SetTitle("L1Mu p_{T} cut [GeV]")
      b1.GetXaxis().SetTitleFont(62)
      b1.GetXaxis().SetTitleOffset(1.2)
      b1.GetXaxis().SetTitleSize(0.05)
      b1.GetYaxis().SetTitleSize(0.05)
      b1.SetTitle("                                                                  14TeV, " + pu)
      b1.SetStats(0)
      b1.Draw()

      h1 = getRatePtHistogram(treeHits, h1)
      h1.SetFillColor(kRed)
      h1.Draw("e3same")
      
      #if isolation_cone != 0.12:    
      h2 = getRatePtHistogram(treeHits, h2)
      h2.SetFillColor(kMagenta)
      h2.Draw("e3same")
      
      h3 = getRatePtHistogram(treeHits, h3)
      h3.SetFillColor(kBlue)
      h3.Draw("e3same")
      
      h4 = getRatePtHistogram(treeHits, h4)
      h4.SetFillColor(kGreen+1)
      h4.Draw("e3same")
      
      h5 = getRatePtHistogram(treeHits, h5)
      h5.SetFillColor(kOrange+1)
      h5.Draw("e3same")

      latex = applyTdrStyle()      

      if isolation_cone == 0.12:
        leg = TLegend(0.2,0.75,0.5,0.85,"","brNDC")
        leg.SetFillColor(kWhite)
        leg.SetBorderSize(0)
        leg.SetFillStyle(0)
        leg.SetTextSize(0.03)
        leg.AddEntry(h1,"Prompt L1Mu", "f")
        leg.AddEntry(None,"Displaced L1Mu", "")
        leg.AddEntry(h5,"Veto Matching L1Tk #DeltaR#leq0.12 with p_{T}#geq%.0f"%(MatchingL1TkMinPt), "f")
        leg.Draw("same")
      else:
        leg = TLegend(0.2,0.6,0.9,0.85,"","brNDC")
        leg.SetFillColor(kWhite)
        leg.SetBorderSize(0)
        leg.SetFillStyle(0)
        leg.SetTextSize(0.03)
        leg.AddEntry(h1,"Prompt L1Mu", "f")
        leg.AddEntry(None,"Displaced L1Mu", "")
        leg.AddEntry(None,"Veto Matching L1Tk #DeltaR#leq0.12 with p_{T}#geq%.0f"%(MatchingL1TkMinPt), "")
        leg.AddEntry(None,"Veto Non-matching L1Tk #DeltaR#leq%.1f:"%(isolation_cone), "")
        leg.AddEntry(h5,"p_{T} #geq 4 GeV", "f")        
        leg.AddEntry(h4,"p_{T} #geq 3 GeV", "f")
        leg.AddEntry(h3,"p_{T} #geq 2.5 GeV", "f")
        leg.AddEntry(h2,"p_{T} #geq 2 GeV", "f")
        leg.Draw("same")

      c.SaveAs(targetDir + title + ext)

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

      print title, "%.2f"%(1./h2.GetBinContent(11))
      print title, "%.2f"%(1./h3.GetBinContent(11))
      print title, "%.2f"%(1./h4.GetBinContent(11))
      print title, "%.2f"%(1./h5.GetBinContent(11))
      print 
      print title, "%.2f"%(2./(h2.GetBinContent(13) + h2.GetBinContent(14)))
      print title, "%.2f"%(2./(h3.GetBinContent(13) + h3.GetBinContent(14)))
      print title, "%.2f"%(2./(h4.GetBinContent(13) + h4.GetBinContent(14)))
      print title, "%.2f"%(2./(h5.GetBinContent(13) + h5.GetBinContent(14)))
      """
      print 
      print title, "%.2f"%(1./h2.GetBinContent(16))
      print title, "%.2f"%(1./h3.GetBinContent(16))
      print title, "%.2f"%(1./h4.GetBinContent(16))
      print title, "%.2f"%(1./h5.GetBinContent(16))
      """

      latex = applyTdrStyle()      

      if isolation_cone == 0.12:
        leg = TLegend(0.2,0.2,0.9,0.4,"","brNDC")
        leg.SetFillColor(kWhite)
        leg.SetBorderSize(0)
        leg.SetFillStyle(0)
        leg.SetTextSize(0.03)
        leg.AddEntry(h1,"Prompt L1Mu", "l")
        leg.AddEntry(None,"Displaced L1Mu", "")
        leg.AddEntry(h5,"Veto Matching L1Tk #DeltaR#leq0.12 with p_{T}#geq%.0f"%(MatchingL1TkMinPt), "l")
        leg.Draw("same")
      else:
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

    ## trigger rate plots vs pt
    makePlots(h_single_L1Mu_rate, 
              h_single_displaced_rate_dR0p4_L1TkPt2, 
              h_single_displaced_rate_dR0p4_L1TkPt2p5, 
              h_single_displaced_rate_dR0p4_L1TkPt3, 
              h_single_displaced_rate_dR0p4_L1TkPt4, 0.4, "L1Mu_trigger_rate_pt_dR0p4")
    makePlots(h_single_L1Mu_rate, 
              h_single_displaced_rate_dR0p3_L1TkPt2, 
              h_single_displaced_rate_dR0p3_L1TkPt2p5, 
              h_single_displaced_rate_dR0p3_L1TkPt3, 
              h_single_displaced_rate_dR0p3_L1TkPt4, 0.3, "L1Mu_trigger_rate_pt_dR0p3")
    makePlots(h_single_L1Mu_rate, 
              h_single_displaced_rate_dR0p2_L1TkPt2, 
              h_single_displaced_rate_dR0p2_L1TkPt2p5, 
              h_single_displaced_rate_dR0p2_L1TkPt3, 
              h_single_displaced_rate_dR0p2_L1TkPt4, 0.2, "L1Mu_trigger_rate_pt_dR0p2")
    makePlots(h_single_L1Mu_rate, 
              h_single_displaced_rate_dR0p12_L1TkPt2, 
              h_single_displaced_rate_dR0p12_L1TkPt2p5, 
              h_single_displaced_rate_dR0p12_L1TkPt3, 
              h_single_displaced_rate_dR0p12_L1TkPt4, 0.12, "L1Mu_trigger_rate_pt_dR0p12")

  if not eff:
    makeRateVsPtHistogram()    
    pass

  def makeRateVsEtaHistogram(ptCut):

    h_single_L1Mu_rate = TH1F("h_single_L1Mu_rate"," ",len(myetabin)-1, myetabin)

    h_single_displaced_rate_dR0p4_L1TkPt2 = TH1F("h_single_displaced_rate_dR0p4_L1TkPt2"," ",len(myetabin)-1, myetabin)
    h_single_displaced_rate_dR0p4_L1TkPt2p5 = TH1F("h_single_displaced_rate_dR0p4_L1TkPt2p5"," ",len(myetabin)-1, myetabin)
    h_single_displaced_rate_dR0p4_L1TkPt3 = TH1F("h_single_displaced_rate_dR0p4_L1TkPt3"," ",len(myetabin)-1, myetabin)
    h_single_displaced_rate_dR0p4_L1TkPt4 = TH1F("h_single_displaced_rate_dR0p4_L1TkPt4"," ",len(myetabin)-1, myetabin)

    h_single_displaced_rate_dR0p3_L1TkPt2 = TH1F("h_single_displaced_rate_dR0p3_L1TkPt2"," ",len(myetabin)-1, myetabin)
    h_single_displaced_rate_dR0p3_L1TkPt2p5 = TH1F("h_single_displaced_rate_dR0p3_L1TkPt2p5"," ",len(myetabin)-1, myetabin)
    h_single_displaced_rate_dR0p3_L1TkPt3 = TH1F("h_single_displaced_rate_dR0p3_L1TkPt3"," ",len(myetabin)-1, myetabin)
    h_single_displaced_rate_dR0p3_L1TkPt4 = TH1F("h_single_displaced_rate_dR0p3_L1TkPt4"," ",len(myetabin)-1, myetabin)

    h_single_displaced_rate_dR0p2_L1TkPt2 = TH1F("h_single_displaced_rate_dR0p2_L1TkPt2"," ",len(myetabin)-1, myetabin)
    h_single_displaced_rate_dR0p2_L1TkPt2p5 = TH1F("h_single_displaced_rate_dR0p2_L1TkPt2p5"," ",len(myetabin)-1, myetabin)
    h_single_displaced_rate_dR0p2_L1TkPt3 = TH1F("h_single_displaced_rate_dR0p2_L1TkPt3"," ",len(myetabin)-1, myetabin)
    h_single_displaced_rate_dR0p2_L1TkPt4 = TH1F("h_single_displaced_rate_dR0p2_L1TkPt4"," ",len(myetabin)-1, myetabin)

    h_single_displaced_rate_dR0p12_L1TkPt2 = TH1F("h_single_displaced_rate_dR0p12_L1TkPt2"," ",len(myetabin)-1, myetabin)
    h_single_displaced_rate_dR0p12_L1TkPt2p5 = TH1F("h_single_displaced_rate_dR0p12_L1TkPt2p5"," ",len(myetabin)-1, myetabin)
    h_single_displaced_rate_dR0p12_L1TkPt3 = TH1F("h_single_displaced_rate_dR0p12_L1TkPt3"," ",len(myetabin)-1, myetabin)
    h_single_displaced_rate_dR0p12_L1TkPt4 = TH1F("h_single_displaced_rate_dR0p12_L1TkPt4"," ",len(myetabin)-1, myetabin)

    for k in range(0,1000):#,treeHits.GetEntries()): #
      treeHits.GetEntry(k)

      ## get the max value of the momentum
      pts = list(treeHits.L1Mu_pt)
      if len(pts)>=1:
      
        def getMaxPts():
          maxPt1 = 0.
          maxPtIndex1 = -1

          maxPt_trig_dR0p4_L1TkPt4 = 0.
          maxPt_trig_dR0p4_L1TkPt3 = 0.
          maxPt_trig_dR0p4_L1TkPt2p5 = 0.
          maxPt_trig_dR0p4_L1TkPt2 = 0.
          
          maxPt_trig_dR0p3_L1TkPt4 = 0.
          maxPt_trig_dR0p3_L1TkPt3 = 0.
          maxPt_trig_dR0p3_L1TkPt2p5 = 0.
          maxPt_trig_dR0p3_L1TkPt2 = 0.

          maxPt_trig_dR0p2_L1TkPt4 = 0.
          maxPt_trig_dR0p2_L1TkPt3 = 0.
          maxPt_trig_dR0p2_L1TkPt2p5 = 0.
          maxPt_trig_dR0p2_L1TkPt2 = 0.
          
          maxPt_trig_dR0p12_L1TkPt4 = 0.
          maxPt_trig_dR0p12_L1TkPt3 = 0.
          maxPt_trig_dR0p12_L1TkPt2p5 = 0.
          maxPt_trig_dR0p12_L1TkPt2 = 0.

          
          maxPtIndex_trig_dR0p4_L1TkPt4 = -1
          maxPtIndex_trig_dR0p4_L1TkPt3 = -1
          maxPtIndex_trig_dR0p4_L1TkPt2p5 = -1
          maxPtIndex_trig_dR0p4_L1TkPt2 = -1
          
          maxPtIndex_trig_dR0p3_L1TkPt4 = -1
          maxPtIndex_trig_dR0p3_L1TkPt3 = -1
          maxPtIndex_trig_dR0p3_L1TkPt2p5 = -1
          maxPtIndex_trig_dR0p3_L1TkPt2 = -1

          maxPtIndex_trig_dR0p2_L1TkPt4 = -1
          maxPtIndex_trig_dR0p2_L1TkPt3 = -1
          maxPtIndex_trig_dR0p2_L1TkPt2p5 = -1
          maxPtIndex_trig_dR0p2_L1TkPt2 = -1
          
          maxPtIndex_trig_dR0p12_L1TkPt4 = -1
          maxPtIndex_trig_dR0p12_L1TkPt3 = -1
          maxPtIndex_trig_dR0p12_L1TkPt2p5 = -1
          maxPtIndex_trig_dR0p12_L1TkPt2 = -1

          for i in range(0,len(pts)):

            L1Mu_pt = treeHits.L1Mu_pt[i]
            L1Mu_bx = treeHits.L1Mu_bx[i]
            L1Mu_quality = treeHits.L1Mu_quality[i]
            L1Mu_L1Tk_dR_min = treeHits.L1Mu_L1Tk_dR_prop[i]
            L1Mu_L1Tk_pt = treeHits.L1Mu_L1Tk_pt_prop[i]
            
            matched = False
            unMatched_dR0p4_L1TkPt4 = False
            unMatched_dR0p4_L1TkPt3 = False
            unMatched_dR0p4_L1TkPt2p5 = False
            unMatched_dR0p4_L1TkPt2 = False

            unMatched_dR0p3_L1TkPt4 = False
            unMatched_dR0p3_L1TkPt3 = False
            unMatched_dR0p3_L1TkPt2p5 = False
            unMatched_dR0p3_L1TkPt2 = False

            unMatched_dR0p2_L1TkPt4 = False
            unMatched_dR0p2_L1TkPt3 = False
            unMatched_dR0p2_L1TkPt2p5 = False
            unMatched_dR0p2_L1TkPt2 = False

            unMatched_dR0p12_L1TkPt4 = False
            unMatched_dR0p12_L1TkPt3 = False
            unMatched_dR0p12_L1TkPt2p5 = False
            unMatched_dR0p12_L1TkPt2 = False

            ## matched 
            matched = L1Mu_L1Tk_dR_min <= 0.12 and L1Mu_quality >= 4
            matched = matched and L1Mu_L1Tk_pt>=MatchingL1TkMinPt

            ## unmatched 
            if L1Mu_L1Tk_dR_min <= 0.4 and L1Mu_L1Tk_pt>=4:   unMatched_dR0p4_L1TkPt4 = True
            if L1Mu_L1Tk_dR_min <= 0.4 and L1Mu_L1Tk_pt>=3:   unMatched_dR0p4_L1TkPt3 = True
            if L1Mu_L1Tk_dR_min <= 0.4 and L1Mu_L1Tk_pt>=2.5: unMatched_dR0p4_L1TkPt2p5 = True
            if L1Mu_L1Tk_dR_min <= 0.4 and L1Mu_L1Tk_pt>=2:   unMatched_dR0p4_L1TkPt2 = True

            if L1Mu_L1Tk_dR_min <= 0.3 and L1Mu_L1Tk_pt>=4:   unMatched_dR0p3_L1TkPt4 = True
            if L1Mu_L1Tk_dR_min <= 0.3 and L1Mu_L1Tk_pt>=3:   unMatched_dR0p3_L1TkPt3 = True
            if L1Mu_L1Tk_dR_min <= 0.3 and L1Mu_L1Tk_pt>=2.5: unMatched_dR0p3_L1TkPt2p5 = True
            if L1Mu_L1Tk_dR_min <= 0.3 and L1Mu_L1Tk_pt>=2:   unMatched_dR0p3_L1TkPt2 = True

            if L1Mu_L1Tk_dR_min <= 0.2 and L1Mu_L1Tk_pt>=4:   unMatched_dR0p2_L1TkPt4 = True
            if L1Mu_L1Tk_dR_min <= 0.2 and L1Mu_L1Tk_pt>=3:   unMatched_dR0p2_L1TkPt3 = True
            if L1Mu_L1Tk_dR_min <= 0.2 and L1Mu_L1Tk_pt>=2.5: unMatched_dR0p2_L1TkPt2p5 = True
            if L1Mu_L1Tk_dR_min <= 0.2 and L1Mu_L1Tk_pt>=2:   unMatched_dR0p2_L1TkPt2 = True

            if L1Mu_L1Tk_dR_min <= 0.12 and L1Mu_L1Tk_pt>=4:   unMatched_dR0p12_L1TkPt4 = True
            if L1Mu_L1Tk_dR_min <= 0.12 and L1Mu_L1Tk_pt>=3:   unMatched_dR0p12_L1TkPt3 = True
            if L1Mu_L1Tk_dR_min <= 0.12 and L1Mu_L1Tk_pt>=2.5: unMatched_dR0p12_L1TkPt2p5 = True
            if L1Mu_L1Tk_dR_min <= 0.12 and L1Mu_L1Tk_pt>=2:   unMatched_dR0p12_L1TkPt2 = True

            common = (L1Mu_pt >= ptCut) and (abs(L1Mu_bx) == 0) and (L1Mu_quality >= 4)
            trig_dR0p4_L1TkPt4 =   (not matched) and (not unMatched_dR0p4_L1TkPt4)   and common
            trig_dR0p4_L1TkPt3 =   (not matched) and (not unMatched_dR0p4_L1TkPt3)   and common
            trig_dR0p4_L1TkPt2p5 = (not matched) and (not unMatched_dR0p4_L1TkPt2p5) and common
            trig_dR0p4_L1TkPt2 =   (not matched) and (not unMatched_dR0p4_L1TkPt2)   and common

            trig_dR0p3_L1TkPt4 =   (not matched) and (not unMatched_dR0p3_L1TkPt4)   and common
            trig_dR0p3_L1TkPt3 =   (not matched) and (not unMatched_dR0p3_L1TkPt3)   and common
            trig_dR0p3_L1TkPt2p5 = (not matched) and (not unMatched_dR0p3_L1TkPt2p5) and common
            trig_dR0p3_L1TkPt2 =   (not matched) and (not unMatched_dR0p3_L1TkPt2)   and common

            trig_dR0p2_L1TkPt4 =   (not matched) and (not unMatched_dR0p2_L1TkPt4)   and common
            trig_dR0p2_L1TkPt3 =   (not matched) and (not unMatched_dR0p2_L1TkPt3)   and common
            trig_dR0p2_L1TkPt2p5 = (not matched) and (not unMatched_dR0p2_L1TkPt2p5) and common
            trig_dR0p2_L1TkPt2 =   (not matched) and (not unMatched_dR0p2_L1TkPt2)   and common

            trig_dR0p12_L1TkPt4 =   (not matched) and common
            trig_dR0p12_L1TkPt3 =   (not matched) and common
            trig_dR0p12_L1TkPt2p5 = (not matched) and common
            trig_dR0p12_L1TkPt2 =   (not matched) and common



            if common             and L1Mu_pt > maxPt1: maxPt1 = L1Mu_pt; maxPtIndex1 = i

            if trig_dR0p4_L1TkPt4 and L1Mu_pt > maxPt_trig_dR0p4_L1TkPt4:     maxPt_trig_dR0p4_L1TkPt4 = L1Mu_pt;   maxPtIndex_trig_dR0p4_L1TkPt4 = i
            if trig_dR0p4_L1TkPt3 and L1Mu_pt > maxPt_trig_dR0p4_L1TkPt3:     maxPt_trig_dR0p4_L1TkPt3 = L1Mu_pt;   maxPtIndex_trig_dR0p4_L1TkPt3 = i
            if trig_dR0p4_L1TkPt2p5 and L1Mu_pt > maxPt_trig_dR0p4_L1TkPt2p5: maxPt_trig_dR0p4_L1TkPt2p5 = L1Mu_pt; maxPtIndex_trig_dR0p4_L1TkPt2p5 = i
            if trig_dR0p4_L1TkPt2 and L1Mu_pt > maxPt_trig_dR0p4_L1TkPt2:     maxPt_trig_dR0p4_L1TkPt2 = L1Mu_pt;   maxPtIndex_trig_dR0p4_L1TkPt2 = i

            if trig_dR0p3_L1TkPt4 and L1Mu_pt > maxPt_trig_dR0p3_L1TkPt4:     maxPt_trig_dR0p3_L1TkPt4 = L1Mu_pt;   maxPtIndex_trig_dR0p3_L1TkPt4 = i
            if trig_dR0p3_L1TkPt3 and L1Mu_pt > maxPt_trig_dR0p3_L1TkPt3:     maxPt_trig_dR0p3_L1TkPt3 = L1Mu_pt;   maxPtIndex_trig_dR0p3_L1TkPt3 = i
            if trig_dR0p3_L1TkPt2p5 and L1Mu_pt > maxPt_trig_dR0p3_L1TkPt2p5: maxPt_trig_dR0p3_L1TkPt2p5 = L1Mu_pt; maxPtIndex_trig_dR0p3_L1TkPt2p5 = i
            if trig_dR0p3_L1TkPt2 and L1Mu_pt > maxPt_trig_dR0p3_L1TkPt2:     maxPt_trig_dR0p3_L1TkPt2 = L1Mu_pt;   maxPtIndex_trig_dR0p3_L1TkPt2 = i

            if trig_dR0p2_L1TkPt4 and L1Mu_pt > maxPt_trig_dR0p2_L1TkPt4:     maxPt_trig_dR0p2_L1TkPt4 = L1Mu_pt;   maxPtIndex_trig_dR0p2_L1TkPt4 = i
            if trig_dR0p2_L1TkPt3 and L1Mu_pt > maxPt_trig_dR0p2_L1TkPt3:     maxPt_trig_dR0p2_L1TkPt3 = L1Mu_pt;   maxPtIndex_trig_dR0p2_L1TkPt3 = i
            if trig_dR0p2_L1TkPt2p5 and L1Mu_pt > maxPt_trig_dR0p2_L1TkPt2p5: maxPt_trig_dR0p2_L1TkPt2p5 = L1Mu_pt; maxPtIndex_trig_dR0p2_L1TkPt2p5 = i
            if trig_dR0p2_L1TkPt2 and L1Mu_pt > maxPt_trig_dR0p2_L1TkPt2:     maxPt_trig_dR0p2_L1TkPt2 = L1Mu_pt;   maxPtIndex_trig_dR0p2_L1TkPt2 = i

            if trig_dR0p12_L1TkPt4 and L1Mu_pt > maxPt_trig_dR0p12_L1TkPt4:     maxPt_trig_dR0p12_L1TkPt4 = L1Mu_pt;   maxPtIndex_trig_dR0p12_L1TkPt4 = i
            if trig_dR0p12_L1TkPt3 and L1Mu_pt > maxPt_trig_dR0p12_L1TkPt3:     maxPt_trig_dR0p12_L1TkPt3 = L1Mu_pt;   maxPtIndex_trig_dR0p12_L1TkPt3 = i
            if trig_dR0p12_L1TkPt2p5 and L1Mu_pt > maxPt_trig_dR0p12_L1TkPt2p5: maxPt_trig_dR0p12_L1TkPt2p5 = L1Mu_pt; maxPtIndex_trig_dR0p12_L1TkPt2p5 = i
            if trig_dR0p12_L1TkPt2 and L1Mu_pt > maxPt_trig_dR0p12_L1TkPt2:     maxPt_trig_dR0p12_L1TkPt2 = L1Mu_pt;   maxPtIndex_trig_dR0p12_L1TkPt2 = i

          return maxPt1, maxPtIndex1, maxPt_trig_dR0p4_L1TkPt4, maxPt_trig_dR0p4_L1TkPt3, maxPt_trig_dR0p4_L1TkPt2p5, maxPt_trig_dR0p4_L1TkPt2, maxPt_trig_dR0p3_L1TkPt4, maxPt_trig_dR0p3_L1TkPt3, maxPt_trig_dR0p3_L1TkPt2p5, maxPt_trig_dR0p3_L1TkPt2, maxPt_trig_dR0p2_L1TkPt4, maxPt_trig_dR0p2_L1TkPt3, maxPt_trig_dR0p2_L1TkPt2p5, maxPt_trig_dR0p2_L1TkPt2, maxPt_trig_dR0p12_L1TkPt4, maxPt_trig_dR0p12_L1TkPt3, maxPt_trig_dR0p12_L1TkPt2p5, maxPt_trig_dR0p12_L1TkPt2, maxPtIndex_trig_dR0p4_L1TkPt4, maxPtIndex_trig_dR0p4_L1TkPt3, maxPtIndex_trig_dR0p4_L1TkPt2p5, maxPtIndex_trig_dR0p4_L1TkPt2, maxPtIndex_trig_dR0p3_L1TkPt4, maxPtIndex_trig_dR0p3_L1TkPt3, maxPtIndex_trig_dR0p3_L1TkPt2p5, maxPtIndex_trig_dR0p3_L1TkPt2, maxPtIndex_trig_dR0p2_L1TkPt4, maxPtIndex_trig_dR0p2_L1TkPt3, maxPtIndex_trig_dR0p2_L1TkPt2p5, maxPtIndex_trig_dR0p2_L1TkPt2, maxPtIndex_trig_dR0p12_L1TkPt4, maxPtIndex_trig_dR0p12_L1TkPt3, maxPtIndex_trig_dR0p12_L1TkPt2p5, maxPtIndex_trig_dR0p12_L1TkPt2
        
        maxPt1, maxPtIndex1, maxPt_trig_dR0p4_L1TkPt4, maxPt_trig_dR0p4_L1TkPt3, maxPt_trig_dR0p4_L1TkPt2p5, maxPt_trig_dR0p4_L1TkPt2, maxPt_trig_dR0p3_L1TkPt4, maxPt_trig_dR0p3_L1TkPt3, maxPt_trig_dR0p3_L1TkPt2p5, maxPt_trig_dR0p3_L1TkPt2, maxPt_trig_dR0p2_L1TkPt4, maxPt_trig_dR0p2_L1TkPt3, maxPt_trig_dR0p2_L1TkPt2p5, maxPt_trig_dR0p2_L1TkPt2, maxPt_trig_dR0p12_L1TkPt4, maxPt_trig_dR0p12_L1TkPt3, maxPt_trig_dR0p12_L1TkPt2p5, maxPt_trig_dR0p12_L1TkPt2, maxPtIndex_trig_dR0p4_L1TkPt4, maxPtIndex_trig_dR0p4_L1TkPt3, maxPtIndex_trig_dR0p4_L1TkPt2p5, maxPtIndex_trig_dR0p4_L1TkPt2, maxPtIndex_trig_dR0p3_L1TkPt4, maxPtIndex_trig_dR0p3_L1TkPt3, maxPtIndex_trig_dR0p3_L1TkPt2p5, maxPtIndex_trig_dR0p3_L1TkPt2, maxPtIndex_trig_dR0p2_L1TkPt4, maxPtIndex_trig_dR0p2_L1TkPt3, maxPtIndex_trig_dR0p2_L1TkPt2p5, maxPtIndex_trig_dR0p2_L1TkPt2, maxPtIndex_trig_dR0p12_L1TkPt4, maxPtIndex_trig_dR0p12_L1TkPt3, maxPtIndex_trig_dR0p12_L1TkPt2p5, maxPtIndex_trig_dR0p12_L1TkPt2 = getMaxPts()

        if (maxPt1>0): h_single_L1Mu_rate.Fill(treeHits.L1Mu_eta[maxPtIndex1])

        if (maxPt_trig_dR0p4_L1TkPt4>0): h_single_displaced_rate_dR0p4_L1TkPt4.Fill(treeHits.L1Mu_eta[maxPtIndex_trig_dR0p4_L1TkPt4])
        if (maxPt_trig_dR0p4_L1TkPt3>0): h_single_displaced_rate_dR0p4_L1TkPt3.Fill(treeHits.L1Mu_eta[maxPtIndex_trig_dR0p4_L1TkPt3])
        if (maxPt_trig_dR0p4_L1TkPt2p5>0): h_single_displaced_rate_dR0p4_L1TkPt2p5.Fill(treeHits.L1Mu_eta[maxPtIndex_trig_dR0p4_L1TkPt2p5])
        if (maxPt_trig_dR0p4_L1TkPt2>0): h_single_displaced_rate_dR0p4_L1TkPt2.Fill(treeHits.L1Mu_eta[maxPtIndex_trig_dR0p4_L1TkPt2])

        if (maxPt_trig_dR0p3_L1TkPt4>0): h_single_displaced_rate_dR0p3_L1TkPt4.Fill(treeHits.L1Mu_eta[maxPtIndex_trig_dR0p3_L1TkPt4])
        if (maxPt_trig_dR0p3_L1TkPt3>0): h_single_displaced_rate_dR0p3_L1TkPt3.Fill(treeHits.L1Mu_eta[maxPtIndex_trig_dR0p3_L1TkPt3])
        if (maxPt_trig_dR0p3_L1TkPt2p5>0): h_single_displaced_rate_dR0p3_L1TkPt2p5.Fill(treeHits.L1Mu_eta[maxPtIndex_trig_dR0p3_L1TkPt2p5])
        if (maxPt_trig_dR0p3_L1TkPt2>0): h_single_displaced_rate_dR0p3_L1TkPt2.Fill(treeHits.L1Mu_eta[maxPtIndex_trig_dR0p3_L1TkPt2])

        if (maxPt_trig_dR0p2_L1TkPt4>0): h_single_displaced_rate_dR0p2_L1TkPt4.Fill(treeHits.L1Mu_eta[maxPtIndex_trig_dR0p2_L1TkPt4])
        if (maxPt_trig_dR0p2_L1TkPt3>0): h_single_displaced_rate_dR0p2_L1TkPt3.Fill(treeHits.L1Mu_eta[maxPtIndex_trig_dR0p2_L1TkPt3])
        if (maxPt_trig_dR0p2_L1TkPt2p5>0): h_single_displaced_rate_dR0p2_L1TkPt2p5.Fill(treeHits.L1Mu_eta[maxPtIndex_trig_dR0p2_L1TkPt2p5])
        if (maxPt_trig_dR0p2_L1TkPt2>0): h_single_displaced_rate_dR0p2_L1TkPt2.Fill(treeHits.L1Mu_eta[maxPtIndex_trig_dR0p2_L1TkPt2])

        if (maxPt_trig_dR0p12_L1TkPt4>0): h_single_displaced_rate_dR0p12_L1TkPt4.Fill(treeHits.L1Mu_eta[maxPtIndex_trig_dR0p12_L1TkPt4])
        if (maxPt_trig_dR0p12_L1TkPt3>0): h_single_displaced_rate_dR0p12_L1TkPt3.Fill(treeHits.L1Mu_eta[maxPtIndex_trig_dR0p12_L1TkPt3])
        if (maxPt_trig_dR0p12_L1TkPt2p5>0): h_single_displaced_rate_dR0p12_L1TkPt2p5.Fill(treeHits.L1Mu_eta[maxPtIndex_trig_dR0p12_L1TkPt2p5])
        if (maxPt_trig_dR0p12_L1TkPt2>0): h_single_displaced_rate_dR0p12_L1TkPt2.Fill(treeHits.L1Mu_eta[maxPtIndex_trig_dR0p12_L1TkPt2])

                                                                                    
    def makePlots(h1, h2, h3, h4, h5, isolation_cone, title):
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

      b1 = TH1F("b1","b1",len(myetabin)-1, myetabin)
      b1.GetYaxis().SetRangeUser(.001,100)
      b1.GetYaxis().SetTitleOffset(1.2)
      b1.GetYaxis().SetNdivisions(520)
      b1.GetYaxis().SetTitle("L1 Trigger Rate [kHz]")
      b1.GetXaxis().SetTitle("L1 muon #eta")
      b1.GetXaxis().SetTitleFont(62)
      b1.GetXaxis().SetTitleOffset(1.2)
      b1.GetXaxis().SetTitleSize(0.05)
      b1.GetYaxis().SetTitleSize(0.05)
      b1.SetTitle("                                                                  14TeV, " + pu)
      b1.SetStats(0)
      b1.Draw()

      h1 = getRateEtaHistogram(treeHits, h1)
      h1.SetLineColor(kRed)
      h1.Draw("same")
      
      if isolation_cone != 0.12:    
        h2 = getRateEtaHistogram(treeHits, h2)
        h2.SetLineColor(kMagenta)
        h2.Draw("same")

        h3 = getRateEtaHistogram(treeHits, h3)
        h3.SetLineColor(kBlue)
        h3.Draw("same")
        
        h4 = getRateEtaHistogram(treeHits, h4)
        h4.SetLineColor(kGreen+1)
        h4.Draw("same")

      h5 = getRateEtaHistogram(treeHits, h5)
      h5.SetLineColor(kOrange+1)
      h5.Draw("same")
      
      latex = applyTdrStyle()      
 
      if isolation_cone == 0.12:
        leg = TLegend(0.2,0.7,0.9,0.9,"","brNDC")
        leg.SetFillColor(kWhite)
        leg.SetBorderSize(0)
        leg.SetFillStyle(0)
        leg.SetTextSize(0.03)
        leg.AddEntry(h1,"Prompt L1Mu", "l")
        leg.AddEntry(None,"Displaced L1Mu", "")
        leg.AddEntry(h5,"Matching L1Tk #DeltaR#leq0.12 with p_{T}#geq%.0f"%(MatchingL1TkMinPt), "l")
        leg.Draw("same")
      else:
        leg = TLegend(0.2,0.7,0.9,0.9,"","brNDC")
        leg.SetFillColor(kWhite)
        leg.SetBorderSize(0)
        leg.SetFillStyle(0)
        leg.SetTextSize(0.03)
        leg.AddEntry(h1,"Prompt L1Mu", "l")
        leg.AddEntry(None,"Displaced L1Mu", "")
        leg.AddEntry(None,"Matching L1Tk #DeltaR#leq0.12 with p_{T}#geq%.0f"%(MatchingL1TkMinPt), "")
        leg.AddEntry(None,"Non-matching L1Tk #DeltaR#leq%.1f:"%(isolation_cone), "")
        leg.AddEntry(h5,"p_{T} #geq 4 GeV", "l")        
        leg.AddEntry(h4,"p_{T} #geq 3 GeV", "l")
        leg.AddEntry(h3,"p_{T} #geq 2.5 GeV", "l")
        leg.AddEntry(h2,"p_{T} #geq 2 GeV", "l")
        leg.Draw("same")

      c.SaveAs(targetDir + title + "ptCut%d.png"%(ptCut))

      ## ratios 
      c = TCanvas("c","c",800,600)
      c.Clear()    
      gStyle.SetTitleBorderSize(0);
      gStyle.SetPadLeftMargin(0.126);
      gStyle.SetPadRightMargin(0.04);
      gStyle.SetPadTopMargin(0.06);
      gStyle.SetPadBottomMargin(0.13);
#      gPad.SetLogy(1)

      b1 = TH1F("b1","b1",len(myetabin)-1, myetabin)
      b1.GetYaxis().SetRangeUser(0.0001,1)
      b1.GetYaxis().SetTitleOffset(1.2)
      b1.GetYaxis().SetNdivisions(520)
      b1.GetYaxis().SetTitle("Ratio (normalized to prompt L1Mu)")
      b1.GetXaxis().SetTitle("L1 muon #eta")
      b1.GetXaxis().SetTitleFont(62)
      b1.GetXaxis().SetTitleOffset(1.2)
      b1.GetXaxis().SetTitleSize(0.05)
      b1.GetYaxis().SetTitleSize(0.05)
      b1.SetTitle("14TeV," + pu)
      b1.SetStats(0)
      b1.Draw()

      if isolation_cone != 0.12:    
        h2.SetLineColor(kMagenta)
        h2.Divide(h1)
        h2.SetFillColor(kWhite)
        h2.Draw("same")
        
        h3.SetLineColor(kBlue)
        h3.Divide(h1)
        h2.SetFillColor(kWhite)
        h3.Draw("same")
        
        h4.SetLineColor(kGreen+1)
        h4.Divide(h1)
        h4.SetFillColor(kWhite)
        h4.Draw("same")
        
      h5.SetLineColor(kOrange+1)
      h5.Divide(h1)
      h5.SetFillColor(kWhite)
      h5.Draw("same")
      """
      print title, "%.2f"%(h2.GetBinContent(11)) #pt10
      print title, "%.2f"%(h3.GetBinContent(11))
      print title, "%.2f"%(h4.GetBinContent(11))
      print title, "%.2f"%(h5.GetBinContent(11))
      print 
      print title, "%.2f"%((h2.GetBinContent(13) + h2.GetBinContent(14))/2.) #average of pt14 and pt16
      print title, "%.2f"%((h3.GetBinContent(13) + h3.GetBinContent(14))/2.)
      print title, "%.2f"%((h4.GetBinContent(13) + h4.GetBinContent(14))/2.)
      print title, "%.2f"%((h5.GetBinContent(13) + h5.GetBinContent(14))/2.)
     """

      latex = applyTdrStyle()      

      if isolation_cone == 0.12:
        leg = TLegend(0.2,0.2,0.9,0.4,"","brNDC")
        leg.SetFillColor(kWhite)
        leg.SetBorderSize(0)
        leg.SetFillStyle(0)
        leg.SetTextSize(0.03)
        leg.AddEntry(None,"Displaced L1Mu", "")
        leg.AddEntry(h5,"Matching L1Tk #DeltaR#leq0.12 with p_{T}#geq%.0f"%(MatchingL1TkMinPt), "l")
        leg.Draw("same")
      else:
        leg = TLegend(0.2,0.2,0.9,0.4,"","brNDC")
        leg.SetFillColor(kWhite)
        leg.SetBorderSize(0)
        leg.SetFillStyle(0)
        leg.SetTextSize(0.03)
        leg.AddEntry(None,"Displaced L1Mu", "")
        leg.AddEntry(None,"Matching L1Tk #DeltaR#leq0.12 with p_{T}#geq%.0f"%(MatchingL1TkMinPt), "")
        leg.AddEntry(None,"Non-matching L1Tk #DeltaR#leq%.1f:"%(isolation_cone), "")
        leg.AddEntry(h5,"p_{T} #geq 4 GeV", "l")        
        leg.AddEntry(h4,"p_{T} #geq 3 GeV", "l")
        leg.AddEntry(h3,"p_{T} #geq 2.5 GeV", "l")
        leg.AddEntry(h2,"p_{T} #geq 2 GeV", "l")
        leg.Draw("same")

      c.SaveAs(targetDir + title + "ptCut%d_ratio"%(ptCut) + ext)

    ## trigger rate plots vs pt
    makePlots(h_single_L1Mu_rate, 
              h_single_displaced_rate_dR0p4_L1TkPt2,
              h_single_displaced_rate_dR0p4_L1TkPt2p5, 
              h_single_displaced_rate_dR0p4_L1TkPt3, 
              h_single_displaced_rate_dR0p4_L1TkPt4, 0.4,
              "L1Mu_trigger_rate_pt_dR0p4")

    makePlots(h_single_L1Mu_rate, 
              h_single_displaced_rate_dR0p3_L1TkPt2,
              h_single_displaced_rate_dR0p3_L1TkPt2p5, 
              h_single_displaced_rate_dR0p3_L1TkPt3, 
              h_single_displaced_rate_dR0p3_L1TkPt4, 0.3,
              "L1Mu_trigger_rate_pt_dR0p3")

    makePlots(h_single_L1Mu_rate, 
              h_single_displaced_rate_dR0p2_L1TkPt2,
              h_single_displaced_rate_dR0p2_L1TkPt2p5, 
              h_single_displaced_rate_dR0p2_L1TkPt3, 
              h_single_displaced_rate_dR0p2_L1TkPt4, 0.2,
              "L1Mu_trigger_rate_pt_dR0p2")

    makePlots(h_single_L1Mu_rate, 
              h_single_displaced_rate_dR0p12_L1TkPt2,
              h_single_displaced_rate_dR0p12_L1TkPt2p5, 
              h_single_displaced_rate_dR0p12_L1TkPt3, 
              h_single_displaced_rate_dR0p12_L1TkPt4, 0.12,
              "L1Mu_trigger_rate_pt_dR0p12")

  if not eff and False:
    makeRateVsEtaHistogram(10)
    makeRateVsEtaHistogram(15)
    makeRateVsEtaHistogram(20)
    pass


#  exit()
  
  def makedRL1MuL1TkHistogram():

    thisTargetDir = "dRL1MuL1TkHistogram/"

    if False:
      draw_1D(ch, "genGdMu_deta_prop", thisTargetDir + "genGdMu_deta_prop", "d#eta; d#eta; Entries", "(100,0.,1.)", cut="", opt = "")
      draw_1D(ch, "genGdMu_dphi_prop", thisTargetDir + "genGdMu_dphi_prop", "d#phi; d#phi; Entries", "(100,0.,1.)", cut="", opt = "")
      draw_1D(ch, "genGdMu_dR_prop", thisTargetDir + "genGdMu_dR_prop", "dR; dR; Entries", "(100,0.,1.)", cut="", opt = "")

      draw_1D(ch, "genGdMu_deta_prop", thisTargetDir + "genGdMu_deta_prop_pt5", "d#eta; d#eta; Entries", "(100,0.,1.)", cut="genGdMu_pt>5", opt = "")
      draw_1D(ch, "genGdMu_dphi_prop", thisTargetDir + "genGdMu_dphi_prop_pt5", "d#phi; d#phi; Entries", "(100,0.,1.)", cut="genGdMu_pt>5", opt = "")
      draw_1D(ch, "genGdMu_dR_prop", thisTargetDir + "genGdMu_dR_prop_pt5", "dR; dR; Entries", "(100,0.,1.)", cut="genGdMu_pt>5", opt = "")

      draw_1D(ch, "genGdMu_deta_prop", thisTargetDir + "genGdMu_deta_prop_pt20", "d#eta; d#eta; Entries", "(100,0.,1.)", cut="genGdMu_pt>20", opt = "")
      draw_1D(ch, "genGdMu_dphi_prop", thisTargetDir + "genGdMu_dphi_prop_pt20", "d#phi; d#phi; Entries", "(100,0.,1.)", cut="genGdMu_pt>20", opt = "")
      draw_1D(ch, "genGdMu_dR_prop", thisTargetDir + "genGdMu_dR_prop_pt20", "dR; dR; Entries", "(100,0.,1.)", cut="genGdMu_pt>20", opt = "")

      draw_1D(ch, "genGdMu_deta_prop", thisTargetDir + "genGdMu_deta_prop_pt30", "d#eta; d#eta; Entries", "(100,0.,1.)", cut="genGdMu_pt>30", opt = "")
      draw_1D(ch, "genGdMu_dphi_prop", thisTargetDir + "genGdMu_dphi_prop_pt30", "d#phi; d#phi; Entries", "(100,0.,1.)", cut="genGdMu_pt>30", opt = "")
      draw_1D(ch, "genGdMu_dR_prop", thisTargetDir + "genGdMu_dR_prop_pt30", "dR; dR; Entries", "(100,0.,1.)", cut="genGdMu_pt>30", opt = "")


      draw_1D(ch, "genGdMu_deta_prop", thisTargetDir + "genGdMu_deta_prop_dxy0to0p1_pt5", "d#eta; d#eta; Entries", "(100,0.,1.)", cut="abs(genGdMu_dxy)<0.1 && genGdMu_pt>5", opt = "")
      draw_1D(ch, "genGdMu_dphi_prop", thisTargetDir + "genGdMu_dphi_prop_dxy0to0p1_pt5", "d#phi; d#phi; Entries", "(100,0.,1.)", cut="abs(genGdMu_dxy)<0.1 && genGdMu_pt>5", opt = "")
      draw_1D(ch, "genGdMu_dR_prop", thisTargetDir + "genGdMu_dR_prop_dxy0to0p1_pt5", "dR; dR; Entries", "(100,0.,1.)", cut="abs(genGdMu_dxy)<0.1 && genGdMu_pt>5", opt = "")

      draw_1D(ch, "genGdMu_deta_prop", thisTargetDir + "genGdMu_deta_prop_dxy1to5_pt5", "d#eta; d#eta; Entries", "(100,0.,1.)", cut="1<abs(genGdMu_dxy) && abs(genGdMu_dxy)<5 && genGdMu_pt>5", opt = "")
      draw_1D(ch, "genGdMu_dphi_prop", thisTargetDir + "genGdMu_dphi_prop_dxy1to5_pt5", "d#phi; d#phi; Entries", "(100,0.,1.)", cut="1<abs(genGdMu_dxy) && abs(genGdMu_dxy)<5 && genGdMu_pt>5", opt = "")
      draw_1D(ch, "genGdMu_dR_prop", thisTargetDir + "genGdMu_dR_prop_dxy1to5_pt5", "dR; dR; Entries", "(100,0.,1.)", cut="1<abs(genGdMu_dxy) && abs(genGdMu_dxy)<5 && genGdMu_pt>5", opt = "")

      draw_1D(ch, "genGdMu_deta_prop", thisTargetDir + "genGdMu_deta_prop_dxy5to10_pt5", "d#eta; d#eta; Entries", "(100,0.,1.)", cut="5<abs(genGdMu_dxy) && abs(genGdMu_dxy)<10 && genGdMu_pt>5", opt = "")
      draw_1D(ch, "genGdMu_dphi_prop", thisTargetDir + "genGdMu_dphi_prop_dxy5to10_pt5", "d#phi; d#phi; Entries", "(100,0.,1.)", cut="5<abs(genGdMu_dxy) && abs(genGdMu_dxy)<10 && genGdMu_pt>5", opt = "")
      draw_1D(ch, "genGdMu_dR_prop", thisTargetDir + "genGdMu_dR_prop_dxy5to10_pt5", "dR; dR; Entries", "(100,0.,1.)", cut="5<abs(genGdMu_dxy) && abs(genGdMu_dxy)<10 && genGdMu_pt>5", opt = "")

      draw_1D(ch, "genGdMu_deta_prop", thisTargetDir + "genGdMu_deta_prop_dxy10to50_pt5", "d#eta; d#eta; Entries", "(100,0.,1.)", cut="10<abs(genGdMu_dxy) && abs(genGdMu_dxy)<30 && genGdMu_pt>5", opt = "")
      draw_1D(ch, "genGdMu_dphi_prop", thisTargetDir + "genGdMu_dphi_prop_dxy10to50_pt5", "d#phi; d#phi; Entries", "(100,0.,1.)", cut="10<abs(genGdMu_dxy) && abs(genGdMu_dxy)<30 && genGdMu_pt>5", opt = "")
      draw_1D(ch, "genGdMu_dR_prop", thisTargetDir + "genGdMu_dR_prop_dxy10to50_pt5", "dR; dR; Entries", "(100,0.,1.)", cut="10<abs(genGdMu_dxy) && abs(genGdMu_dxy)<30 && genGdMu_pt>5", opt = "")


      draw_1D(ch, "genGdMu_deta_prop", thisTargetDir + "genGdMu_deta_prop_dxy0to0p1_pt20", "d#eta; d#eta; Entries", "(100,0.,1.)", cut="abs(genGdMu_dxy)<0.1 && genGdMu_pt>20", opt = "")
      draw_1D(ch, "genGdMu_dphi_prop", thisTargetDir + "genGdMu_dphi_prop_dxy0to0p1_pt20", "d#phi; d#phi; Entries", "(100,0.,1.)", cut="abs(genGdMu_dxy)<0.1 && genGdMu_pt>20", opt = "")
      draw_1D(ch, "genGdMu_dR_prop", thisTargetDir + "genGdMu_dR_prop_dxy0to0p1_pt20", "dR; dR; Entries", "(100,0.,1.)", cut="abs(genGdMu_dxy)<0.1 && genGdMu_pt>20", opt = "")

      draw_1D(ch, "genGdMu_deta_prop", thisTargetDir + "genGdMu_deta_prop_dxy1to5_pt20", "d#eta; d#eta; Entries", "(100,0.,1.)", cut="1<abs(genGdMu_dxy) && abs(genGdMu_dxy)<5 && genGdMu_pt>20", opt = "")
      draw_1D(ch, "genGdMu_dphi_prop", thisTargetDir + "genGdMu_dphi_prop_dxy1to5_pt20", "d#phi; d#phi; Entries", "(100,0.,1.)", cut="1<abs(genGdMu_dxy) && abs(genGdMu_dxy)<5 && genGdMu_pt>20", opt = "")
      draw_1D(ch, "genGdMu_dR_prop", thisTargetDir + "genGdMu_dR_prop_dxy1to5_pt20", "dR; dR; Entries", "(100,0.,1.)", cut="1<abs(genGdMu_dxy) && abs(genGdMu_dxy)<5 && genGdMu_pt>20", opt = "")

      draw_1D(ch, "genGdMu_deta_prop", thisTargetDir + "genGdMu_deta_prop_dxy5to10_pt20", "d#eta; d#eta; Entries", "(100,0.,1.)", cut="5<abs(genGdMu_dxy) && abs(genGdMu_dxy)<10 && genGdMu_pt>20", opt = "")
      draw_1D(ch, "genGdMu_dphi_prop", thisTargetDir + "genGdMu_dphi_prop_dxy5to10_pt20", "d#phi; d#phi; Entries", "(100,0.,1.)", cut="5<abs(genGdMu_dxy) && abs(genGdMu_dxy)<10 && genGdMu_pt>20", opt = "")
      draw_1D(ch, "genGdMu_dR_prop", thisTargetDir + "genGdMu_dR_prop_dxy5to10_pt20", "dR; dR; Entries", "(100,0.,1.)", cut="5<abs(genGdMu_dxy) && abs(genGdMu_dxy)<10 && genGdMu_pt>20", opt = "")

      draw_1D(ch, "genGdMu_deta_prop", thisTargetDir + "genGdMu_deta_prop_dxy10to50_pt20", "d#eta; d#eta; Entries", "(100,0.,1.)", cut="10<abs(genGdMu_dxy) && abs(genGdMu_dxy)<30 && genGdMu_pt>20", opt = "")
      draw_1D(ch, "genGdMu_dphi_prop", thisTargetDir + "genGdMu_dphi_prop_dxy10to50_pt20", "d#phi; d#phi; Entries", "(100,0.,1.)", cut="10<abs(genGdMu_dxy) && abs(genGdMu_dxy)<30 && genGdMu_pt>20", opt = "")
      draw_1D(ch, "genGdMu_dR_prop", thisTargetDir + "genGdMu_dR_prop_dxy10to50_pt20", "dR; dR; Entries", "(100,0.,1.)", cut="10<abs(genGdMu_dxy) && abs(genGdMu_dxy)<30 && genGdMu_pt>20", opt = "")


      draw_1D(ch, "genGdMu_deta_corr", thisTargetDir + "genGdMu_deta_corr", "d#eta; d#eta; Entries", "(100,0.,1.)", cut="", opt = "")
      draw_1D(ch, "genGdMu_dphi_corr", thisTargetDir + "genGdMu_dphi_corr", "d#phi; d#phi; Entries", "(100,0.,1.)", cut="", opt = "")
      draw_1D(ch, "genGdMu_dR_corr", thisTargetDir + "genGdMu_dR_corr", "dR; dR; Entries", "(100,0.,1.)", cut="", opt = "")

      draw_1D(ch, "genGdMu_deta_corr", thisTargetDir + "genGdMu_deta_corr_pt5", "d#eta; d#eta; Entries", "(100,0.,1.)", cut="genGdMu_pt>5", opt = "")
      draw_1D(ch, "genGdMu_dphi_corr", thisTargetDir + "genGdMu_dphi_corr_pt5", "d#phi; d#phi; Entries", "(100,0.,1.)", cut="genGdMu_pt>5", opt = "")
      draw_1D(ch, "genGdMu_dR_corr", thisTargetDir + "genGdMu_dR_corr_pt5", "dR; dR; Entries", "(100,0.,1.)", cut="genGdMu_pt>5", opt = "")

      draw_1D(ch, "genGdMu_deta_corr", thisTargetDir + "genGdMu_deta_corr_pt20", "d#eta; d#eta; Entries", "(100,0.,1.)", cut="genGdMu_pt>20", opt = "")
      draw_1D(ch, "genGdMu_dphi_corr", thisTargetDir + "genGdMu_dphi_corr_pt20", "d#phi; d#phi; Entries", "(100,0.,1.)", cut="genGdMu_pt>20", opt = "")
      draw_1D(ch, "genGdMu_dR_corr", thisTargetDir + "genGdMu_dR_corr_pt20", "dR; dR; Entries", "(100,0.,1.)", cut="genGdMu_pt>20", opt = "")

      draw_1D(ch, "genGdMu_deta_corr", thisTargetDir + "genGdMu_deta_corr_pt30", "d#eta; d#eta; Entries", "(100,0.,1.)", cut="genGdMu_pt>30", opt = "")
      draw_1D(ch, "genGdMu_dphi_corr", thisTargetDir + "genGdMu_dphi_corr_pt30", "d#phi; d#phi; Entries", "(100,0.,1.)", cut="genGdMu_pt>30", opt = "")
      draw_1D(ch, "genGdMu_dR_corr", thisTargetDir + "genGdMu_dR_corr_pt30", "dR; dR; Entries", "(100,0.,1.)", cut="genGdMu_pt>30", opt = "")


    genGdMu_L1Mu_dR_fid = TH1F("genGdMu_L1Mu_dR_fid","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy0to0p1 = TH1F("genGdMu_L1Mu_dR_fid_dxy0to0p1","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy1to5 = TH1F("genGdMu_L1Mu_dR_fid_dxy1to5","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy5to10 = TH1F("genGdMu_L1Mu_dR_fid_dxy5to10","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy10to50 = TH1F("genGdMu_L1Mu_dR_fid_dxy10to50","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)

    genGdMu_L1Mu_dR_fid_barrel = TH1F("genGdMu_L1Mu_dR_fid_barrel","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy0to0p1_barrel = TH1F("genGdMu_L1Mu_dR_fid_dxy0to0p1_barrel","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy1to5_barrel = TH1F("genGdMu_L1Mu_dR_fid_dxy1to5_barrel","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy5to10_barrel = TH1F("genGdMu_L1Mu_dR_fid_dxy5to10_barrel","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy10to50_barrel = TH1F("genGdMu_L1Mu_dR_fid_dxy10to50_barrel","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)

    genGdMu_L1Mu_dR_fid_overlap = TH1F("genGdMu_L1Mu_dR_fid_overlap","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy0to0p1_overlap = TH1F("genGdMu_L1Mu_dR_fid_dxy0to0p1_overlap","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy1to5_overlap = TH1F("genGdMu_L1Mu_dR_fid_dxy1to5_overlap","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy5to10_overlap = TH1F("genGdMu_L1Mu_dR_fid_dxy5to10_overlap","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy10to50_overlap = TH1F("genGdMu_L1Mu_dR_fid_dxy10to50_overlap","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)

    genGdMu_L1Mu_dR_fid_endcap = TH1F("genGdMu_L1Mu_dR_fid_endcap","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap = TH1F("genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy1to5_endcap = TH1F("genGdMu_L1Mu_dR_fid_dxy1to5_endcap","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy5to10_endcap = TH1F("genGdMu_L1Mu_dR_fid_dxy5to10_endcap","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy10to50_endcap = TH1F("genGdMu_L1Mu_dR_fid_dxy10to50_endcap","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)

    genGdMu_L1Mu_dR_fid_endcap_12_14 = TH1F("genGdMu_L1Mu_dR_fid_endcap_12_14","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_12_14 = TH1F("genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_12_14","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy1to5_endcap_12_14 = TH1F("genGdMu_L1Mu_dR_fid_dxy1to5_endcap_12_14","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy5to10_endcap_12_14 = TH1F("genGdMu_L1Mu_dR_fid_dxy5to10_endcap_12_14","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy10to50_endcap_12_14 = TH1F("genGdMu_L1Mu_dR_fid_dxy10to50_endcap_12_14","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)

    genGdMu_L1Mu_dR_fid_endcap_14_16 = TH1F("genGdMu_L1Mu_dR_fid_endcap_14_16","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_14_16 = TH1F("genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_14_16","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy1to5_endcap_14_16 = TH1F("genGdMu_L1Mu_dR_fid_dxy1to5_endcap_14_16","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy5to10_endcap_14_16 = TH1F("genGdMu_L1Mu_dR_fid_dxy5to10_endcap_14_16","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy10to50_endcap_14_16 = TH1F("genGdMu_L1Mu_dR_fid_dxy10to50_endcap_14_16","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)

    genGdMu_L1Mu_dR_fid_endcap_16_18 = TH1F("genGdMu_L1Mu_dR_fid_endcap_16_18","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_16_18 = TH1F("genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_16_18","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy1to5_endcap_16_18 = TH1F("genGdMu_L1Mu_dR_fid_dxy1to5_endcap_16_18","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy5to10_endcap_16_18 = TH1F("genGdMu_L1Mu_dR_fid_dxy5to10_endcap_16_18","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy10to50_endcap_16_18 = TH1F("genGdMu_L1Mu_dR_fid_dxy10to50_endcap_16_18","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)

    genGdMu_L1Mu_dR_fid_endcap_18_20 = TH1F("genGdMu_L1Mu_dR_fid_endcap_18_20","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_18_20 = TH1F("genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_18_20","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy1to5_endcap_18_20 = TH1F("genGdMu_L1Mu_dR_fid_dxy1to5_endcap_18_20","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy5to10_endcap_18_20 = TH1F("genGdMu_L1Mu_dR_fid_dxy5to10_endcap_18_20","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy10to50_endcap_18_20 = TH1F("genGdMu_L1Mu_dR_fid_dxy10to50_endcap_18_20","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)

    genGdMu_L1Mu_dR_fid_endcap_20_22 = TH1F("genGdMu_L1Mu_dR_fid_endcap_20_22","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_20_22 = TH1F("genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_20_22","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy1to5_endcap_20_22 = TH1F("genGdMu_L1Mu_dR_fid_dxy1to5_endcap_20_22","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy5to10_endcap_20_22 = TH1F("genGdMu_L1Mu_dR_fid_dxy5to10_endcap_20_22","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy10to50_endcap_20_22 = TH1F("genGdMu_L1Mu_dR_fid_dxy10to50_endcap_20_22","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)

    genGdMu_L1Mu_dR_fid_endcap_22_24 = TH1F("genGdMu_L1Mu_dR_fid_endcap_22_24","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_22_24 = TH1F("genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_22_24","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy1to5_endcap_22_24 = TH1F("genGdMu_L1Mu_dR_fid_dxy1to5_endcap_22_24","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy5to10_endcap_22_24 = TH1F("genGdMu_L1Mu_dR_fid_dxy5to10_endcap_22_24","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    genGdMu_L1Mu_dR_fid_dxy10to50_endcap_22_24 = TH1F("genGdMu_L1Mu_dR_fid_dxy10to50_endcap_22_24","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)

    L1Mu_L1Tk_dR_fid = TH1F("L1Mu_L1Tk_dR_fid","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy0to0p1 = TH1F("L1Mu_L1Tk_dR_fid_dxy0to0p1","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy0to1 = TH1F("L1Mu_L1Tk_dR_fid_dxy0to1","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy1to5 = TH1F("L1Mu_L1Tk_dR_fid_dxy1to5","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy5to10 = TH1F("L1Mu_L1Tk_dR_fid_dxy5to10","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy10to50 = TH1F("L1Mu_L1Tk_dR_fid_dxy10to50","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)

    L1Mu_L1Tk_dR_fid_barrel = TH1F("L1Mu_L1Tk_dR_fid_barrel","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy0to0p1_barrel = TH1F("L1Mu_L1Tk_dR_fid_dxy0to0p1_barrel","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy0to1_barrel = TH1F("L1Mu_L1Tk_dR_fid_dxy0to1_barrel","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy1to5_barrel = TH1F("L1Mu_L1Tk_dR_fid_dxy1to5_barrel","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy5to10_barrel = TH1F("L1Mu_L1Tk_dR_fid_dxy5to10_barrel","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy10to50_barrel = TH1F("L1Mu_L1Tk_dR_fid_dxy10to50_barrel","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)

    L1Mu_L1Tk_dR_fid_overlap = TH1F("L1Mu_L1Tk_dR_fid_overlap","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy0to0p1_overlap = TH1F("L1Mu_L1Tk_dR_fid_dxy0to0p1_overlap","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy0to1_overlap = TH1F("L1Mu_L1Tk_dR_fid_dxy0to1_overlap","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy1to5_overlap = TH1F("L1Mu_L1Tk_dR_fid_dxy1to5_overlap","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy5to10_overlap = TH1F("L1Mu_L1Tk_dR_fid_dxy5to10_overlap","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy10to50_overlap = TH1F("L1Mu_L1Tk_dR_fid_dxy10to50_overlap","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)

    L1Mu_L1Tk_dR_fid_endcap = TH1F("L1Mu_L1Tk_dR_fid_endcap","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap = TH1F("L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy0to1_endcap = TH1F("L1Mu_L1Tk_dR_fid_dxy0to1_endcap","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy1to5_endcap = TH1F("L1Mu_L1Tk_dR_fid_dxy1to5_endcap","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy5to10_endcap = TH1F("L1Mu_L1Tk_dR_fid_dxy5to10_endcap","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy10to50_endcap = TH1F("L1Mu_L1Tk_dR_fid_dxy10to50_endcap","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)

    L1Mu_L1Tk_dR_fid_endcap_12_14 = TH1F("L1Mu_L1Tk_dR_fid_endcap_12_14","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_12_14 = TH1F("L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_12_14","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy0to1_endcap_12_14 = TH1F("L1Mu_L1Tk_dR_fid_dxy0to1_endcap_12_14","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy1to5_endcap_12_14 = TH1F("L1Mu_L1Tk_dR_fid_dxy1to5_endcap_12_14","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy5to10_endcap_12_14 = TH1F("L1Mu_L1Tk_dR_fid_dxy5to10_endcap_12_14","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy10to50_endcap_12_14 = TH1F("L1Mu_L1Tk_dR_fid_dxy10to50_endcap_12_14","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)

    L1Mu_L1Tk_dR_fid_endcap_14_16 = TH1F("L1Mu_L1Tk_dR_fid_endcap_14_16","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_14_16 = TH1F("L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_14_16","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy0to1_endcap_14_16 = TH1F("L1Mu_L1Tk_dR_fid_dxy0to1_endcap_14_16","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy1to5_endcap_14_16 = TH1F("L1Mu_L1Tk_dR_fid_dxy1to5_endcap_14_16","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy5to10_endcap_14_16 = TH1F("L1Mu_L1Tk_dR_fid_dxy5to10_endcap_14_16","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy10to50_endcap_14_16 = TH1F("L1Mu_L1Tk_dR_fid_dxy10to50_endcap_14_16","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)

    L1Mu_L1Tk_dR_fid_endcap_16_18 = TH1F("L1Mu_L1Tk_dR_fid_endcap_16_18","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_16_18 = TH1F("L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_16_18","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy0to1_endcap_16_18 = TH1F("L1Mu_L1Tk_dR_fid_dxy0to1_endcap_16_18","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy1to5_endcap_16_18 = TH1F("L1Mu_L1Tk_dR_fid_dxy1to5_endcap_16_18","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy5to10_endcap_16_18 = TH1F("L1Mu_L1Tk_dR_fid_dxy5to10_endcap_16_18","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy10to50_endcap_16_18 = TH1F("L1Mu_L1Tk_dR_fid_dxy10to50_endcap_16_18","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)

    L1Mu_L1Tk_dR_fid_endcap_18_20 = TH1F("L1Mu_L1Tk_dR_fid_endcap_18_20","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_18_20 = TH1F("L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_18_20","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy0to1_endcap_18_20 = TH1F("L1Mu_L1Tk_dR_fid_dxy0to1_endcap_18_20","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy1to5_endcap_18_20 = TH1F("L1Mu_L1Tk_dR_fid_dxy1to5_endcap_18_20","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy5to10_endcap_18_20 = TH1F("L1Mu_L1Tk_dR_fid_dxy5to10_endcap_18_20","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy10to50_endcap_18_20 = TH1F("L1Mu_L1Tk_dR_fid_dxy10to50_endcap_18_20","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)

    L1Mu_L1Tk_dR_fid_endcap_20_22 = TH1F("L1Mu_L1Tk_dR_fid_endcap_20_22","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_20_22 = TH1F("L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_20_22","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy0to1_endcap_20_22 = TH1F("L1Mu_L1Tk_dR_fid_dxy0to1_endcap_20_22","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy1to5_endcap_20_22 = TH1F("L1Mu_L1Tk_dR_fid_dxy1to5_endcap_20_22","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy5to10_endcap_20_22 = TH1F("L1Mu_L1Tk_dR_fid_dxy5to10_endcap_20_22","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy10to50_endcap_20_22 = TH1F("L1Mu_L1Tk_dR_fid_dxy10to50_endcap_20_22","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)

    L1Mu_L1Tk_dR_fid_endcap_22_24 = TH1F("L1Mu_L1Tk_dR_fid_endcap_22_24","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_22_24 = TH1F("L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_22_24","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy0to1_endcap_22_24 = TH1F("L1Mu_L1Tk_dR_fid_dxy0to1_endcap_22_24","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy1to5_endcap_22_24 = TH1F("L1Mu_L1Tk_dR_fid_dxy1to5_endcap_22_24","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy5to10_endcap_22_24 = TH1F("L1Mu_L1Tk_dR_fid_dxy5to10_endcap_22_24","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy10to50_endcap_22_24 = TH1F("L1Mu_L1Tk_dR_fid_dxy10to50_endcap_22_24","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)

    L1Mu_L1Tk_dR_fid_dxy1to50 = TH1F("L1Mu_L1Tk_dR_fid_dxy1to50","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy1to50_barrel = TH1F("L1Mu_L1Tk_dR_fid_dxy1to50_barrel","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy1to50_overlap = TH1F("L1Mu_L1Tk_dR_fid_dxy1to50_overlap","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy1to50_endcap = TH1F("L1Mu_L1Tk_dR_fid_dxy1to50_endcap","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy1to50_endcap_12_14 = TH1F("L1Mu_L1Tk_dR_fid_dxy1to50_endcap_12_14","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy1to50_endcap_14_16 = TH1F("L1Mu_L1Tk_dR_fid_dxy1to50_endcap_14_16","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy1to50_endcap_16_18 = TH1F("L1Mu_L1Tk_dR_fid_dxy1to50_endcap_16_18","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy1to50_endcap_18_20 = TH1F("L1Mu_L1Tk_dR_fid_dxy1to50_endcap_18_20","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy1to50_endcap_20_22 = TH1F("L1Mu_L1Tk_dR_fid_dxy1to50_endcap_20_22","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy1to50_endcap_22_24 = TH1F("L1Mu_L1Tk_dR_fid_dxy1to50_endcap_22_24","dR(Gen Mu,closest L1Mu);dR; Entries", 100,0.,1.)

    L1Mu_L1Tk_dR_fid_barrel_pt2 = TH1F("L1Mu_L1Tk_dR_fid_barrel_pt2","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy0to0p1_barrel_pt2 = TH1F("L1Mu_L1Tk_dR_fid_dxy0to0p1_barrel_pt2","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy1to5_barrel_pt2 = TH1F("L1Mu_L1Tk_dR_fid_dxy1to5_barrel_pt2","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy5to10_barrel_pt2 = TH1F("L1Mu_L1Tk_dR_fid_dxy5to10_barrel_pt2","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy10to50_barrel_pt2 = TH1F("L1Mu_L1Tk_dR_fid_dxy10to50_barrel_pt2","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)

    L1Mu_L1Tk_dR_fid_overlap_pt2 = TH1F("L1Mu_L1Tk_dR_fid_overlap_pt2","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy0to0p1_overlap_pt2 = TH1F("L1Mu_L1Tk_dR_fid_dxy0to0p1_overlap_pt2","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy1to5_overlap_pt2 = TH1F("L1Mu_L1Tk_dR_fid_dxy1to5_overlap_pt2","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy5to10_overlap_pt2 = TH1F("L1Mu_L1Tk_dR_fid_dxy5to10_overlap_pt2","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy10to50_overlap_pt2 = TH1F("L1Mu_L1Tk_dR_fid_dxy10to50_overlap_pt2","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)

    L1Mu_L1Tk_dR_fid_endcap_pt2 = TH1F("L1Mu_L1Tk_dR_fid_endcap_pt2","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_pt2 = TH1F("L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_pt2","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy1to5_endcap_pt2 = TH1F("L1Mu_L1Tk_dR_fid_dxy1to5_endcap_pt2","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy5to10_endcap_pt2 = TH1F("L1Mu_L1Tk_dR_fid_dxy5to10_endcap_pt2","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_fid_dxy10to50_endcap_pt2 = TH1F("L1Mu_L1Tk_dR_fid_dxy10to50_endcap_pt2","dR(real L1Mu,closest L1Tk);dR; Entries", 100,0.,1.)


    L1Mu_L1Tk_dR_true_fid = TH1F("L1Mu_L1Tk_dR_true_fid","dR(real L1Mu,true L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_true_fid_dxy0to0p1 = TH1F("L1Mu_L1Tk_dR_true_fid_dxy0to0p1","dR(real L1Mu,true L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_true_fid_dxy1to5 = TH1F("L1Mu_L1Tk_dR_true_fid_dxy1to5","dR(real L1Mu,true L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_true_fid_dxy5to10 = TH1F("L1Mu_L1Tk_dR_true_fid_dxy5to10","dR(real L1Mu,true L1Tk);dR; Entries", 100,0.,1.)
    L1Mu_L1Tk_dR_true_fid_dxy10to50 = TH1F("L1Mu_L1Tk_dR_true_fid_dxy10to50","dR(real L1Mu,true L1Tk);dR; Entries", 100,0.,1.)

    ## pt plots
    L1Mu_L1Tk_pt_fid = TH1F("L1Mu_L1Tk_pt_fid","L1Tk p_{T};GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy0to0p1 = TH1F("L1Mu_L1Tk_pt_fid_dxy0to0p1","L1Tk p_{T};GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy0to1 = TH1F("L1Mu_L1Tk_pt_fid_dxy0to1","L1Tk p_{T};GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy1to5 = TH1F("L1Mu_L1Tk_pt_fid_dxy1to5","L1Tk p_{T};GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy5to10 = TH1F("L1Mu_L1Tk_pt_fid_dxy5to10","L1Tk p_{T};GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy10to50 = TH1F("L1Mu_L1Tk_pt_fid_dxy10to50","L1Tk p_{T};GeV; Entries", 50,0.,50.)

    L1Mu_L1Tk_pt_fid_barrel = TH1F("L1Mu_L1Tk_pt_fid_barrel","L1Tk p_{T} barrel;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy0to0p1_barrel = TH1F("L1Mu_L1Tk_pt_fid_dxy0to0p1_barrel","L1Tk p_{T} barrel;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy0to1_barrel = TH1F("L1Mu_L1Tk_pt_fid_dxy0to1_barrel","L1Tk p_{T} barrel;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy1to5_barrel = TH1F("L1Mu_L1Tk_pt_fid_dxy1to5_barrel","L1Tk p_{T} barrel;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy5to10_barrel = TH1F("L1Mu_L1Tk_pt_fid_dxy5to10_barrel","L1Tk p_{T} barrel;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy10to50_barrel = TH1F("L1Mu_L1Tk_pt_fid_dxy10to50_barrel","L1Tk p_{T} barrel;GeV; Entries", 50,0.,50.)

    L1Mu_L1Tk_pt_fid_overlap = TH1F("L1Mu_L1Tk_pt_fid_overlap","L1Tk p_{T} overlap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy0to0p1_overlap = TH1F("L1Mu_L1Tk_pt_fid_dxy0to0p1_overlap","L1Tk p_{T} overlap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy0to1_overlap = TH1F("L1Mu_L1Tk_pt_fid_dxy0to1_overlap","L1Tk p_{T} overlap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy1to5_overlap = TH1F("L1Mu_L1Tk_pt_fid_dxy1to5_overlap","L1Tk p_{T} overlap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy5to10_overlap = TH1F("L1Mu_L1Tk_pt_fid_dxy5to10_overlap","L1Tk p_{T} overlap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy10to50_overlap = TH1F("L1Mu_L1Tk_pt_fid_dxy10to50_overlap","L1Tk p_{T} overlap;GeV; Entries", 50,0.,50.)

    L1Mu_L1Tk_pt_fid_endcap = TH1F("L1Mu_L1Tk_pt_fid_endcap","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap = TH1F("L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy0to1_endcap = TH1F("L1Mu_L1Tk_pt_fid_dxy0to1_endcap","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy1to5_endcap = TH1F("L1Mu_L1Tk_pt_fid_dxy1to5_endcap","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy5to10_endcap = TH1F("L1Mu_L1Tk_pt_fid_dxy5to10_endcap","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy10to50_endcap = TH1F("L1Mu_L1Tk_pt_fid_dxy10to50_endcap","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)

    L1Mu_L1Tk_pt_fid_endcap_12_14 = TH1F("L1Mu_L1Tk_pt_fid_endcap_12_14","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_12_14 = TH1F("L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_12_14","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy0to1_endcap_12_14 = TH1F("L1Mu_L1Tk_pt_fid_dxy0to1_endcap_12_14","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy1to5_endcap_12_14 = TH1F("L1Mu_L1Tk_pt_fid_dxy1to5_endcap_12_14","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy5to10_endcap_12_14 = TH1F("L1Mu_L1Tk_pt_fid_dxy5to10_endcap_12_14","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy10to50_endcap_12_14 = TH1F("L1Mu_L1Tk_pt_fid_dxy10to50_endcap_12_14","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)

    L1Mu_L1Tk_pt_fid_endcap_14_16 = TH1F("L1Mu_L1Tk_pt_fid_endcap_14_16","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_14_16 = TH1F("L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_14_16","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy0to1_endcap_14_16 = TH1F("L1Mu_L1Tk_pt_fid_dxy0to1_endcap_14_16","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy1to5_endcap_14_16 = TH1F("L1Mu_L1Tk_pt_fid_dxy1to5_endcap_14_16","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy5to10_endcap_14_16 = TH1F("L1Mu_L1Tk_pt_fid_dxy5to10_endcap_14_16","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy10to50_endcap_14_16 = TH1F("L1Mu_L1Tk_pt_fid_dxy10to50_endcap_14_16","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)

    L1Mu_L1Tk_pt_fid_endcap_16_18 = TH1F("L1Mu_L1Tk_pt_fid_endcap_16_18","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_16_18 = TH1F("L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_16_18","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy0to1_endcap_16_18 = TH1F("L1Mu_L1Tk_pt_fid_dxy0to1_endcap_16_18","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy1to5_endcap_16_18 = TH1F("L1Mu_L1Tk_pt_fid_dxy1to5_endcap_16_18","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy5to10_endcap_16_18 = TH1F("L1Mu_L1Tk_pt_fid_dxy5to10_endcap_16_18","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy10to50_endcap_16_18 = TH1F("L1Mu_L1Tk_pt_fid_dxy10to50_endcap_16_18","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)

    L1Mu_L1Tk_pt_fid_endcap_18_20 = TH1F("L1Mu_L1Tk_pt_fid_endcap_18_20","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_18_20 = TH1F("L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_18_20","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy0to1_endcap_18_20 = TH1F("L1Mu_L1Tk_pt_fid_dxy0to1_endcap_18_20","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy1to5_endcap_18_20 = TH1F("L1Mu_L1Tk_pt_fid_dxy1to5_endcap_18_20","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy5to10_endcap_18_20 = TH1F("L1Mu_L1Tk_pt_fid_dxy5to10_endcap_18_20","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy10to50_endcap_18_20 = TH1F("L1Mu_L1Tk_pt_fid_dxy10to50_endcap_18_20","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)

    L1Mu_L1Tk_pt_fid_endcap_20_22 = TH1F("L1Mu_L1Tk_pt_fid_endcap_20_22","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_20_22 = TH1F("L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_20_22","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy0to1_endcap_20_22 = TH1F("L1Mu_L1Tk_pt_fid_dxy0to1_endcap_20_22","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy1to5_endcap_20_22 = TH1F("L1Mu_L1Tk_pt_fid_dxy1to5_endcap_20_22","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy5to10_endcap_20_22 = TH1F("L1Mu_L1Tk_pt_fid_dxy5to10_endcap_20_22","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy10to50_endcap_20_22 = TH1F("L1Mu_L1Tk_pt_fid_dxy10to50_endcap_20_22","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)

    L1Mu_L1Tk_pt_fid_endcap_22_24 = TH1F("L1Mu_L1Tk_pt_fid_endcap_22_24","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_22_24 = TH1F("L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_22_24","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy0to1_endcap_22_24 = TH1F("L1Mu_L1Tk_pt_fid_dxy0to1_endcap_22_24","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy1to5_endcap_22_24 = TH1F("L1Mu_L1Tk_pt_fid_dxy1to5_endcap_22_24","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy5to10_endcap_22_24 = TH1F("L1Mu_L1Tk_pt_fid_dxy5to10_endcap_22_24","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)
    L1Mu_L1Tk_pt_fid_dxy10to50_endcap_22_24 = TH1F("L1Mu_L1Tk_pt_fid_dxy10to50_endcap_22_24","L1Tk p_{T} endcap;GeV; Entries", 50,0.,50.)

    L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_barrel = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_barrel","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_overlap = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_overlap","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_12_14 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_12_14","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_14_16 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_14_16","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_16_18 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_16_18","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_18_20 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_18_20","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_20_22 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_20_22","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_22_24 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_22_24","", 100,0.,1.,50,0.,50.)

    L1Mu_L1Tk_dRvspt_fid_dxy1to5_barrel = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy1to5_barrel","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy1to5_overlap = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy1to5_overlap","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_12_14 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_12_14","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_14_16 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_14_16","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_16_18 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_16_18","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_18_20 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_18_20","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_20_22 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_20_22","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_22_24 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_22_24","", 100,0.,1.,50,0.,50.)

    L1Mu_L1Tk_dRvspt_fid_dxy5to10_barrel = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy5to10_barrel","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy5to10_overlap = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy5to10_overlap","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_12_14 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_12_14","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_14_16 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_14_16","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_16_18 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_16_18","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_18_20 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_18_20","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_20_22 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_20_22","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_22_24 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_22_24","", 100,0.,1.,50,0.,50.)

    L1Mu_L1Tk_dRvspt_fid_dxy10to50_barrel = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy10to50_barrel","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy10to50_overlap = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy10to50_overlap","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_12_14 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_12_14","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_14_16 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_14_16","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_16_18 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_16_18","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_18_20 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_18_20","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_20_22 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_20_22","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_22_24 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_22_24","", 100,0.,1.,50,0.,50.)

    L1Mu_L1Tk_dRvspt_fid_dxy0to1_barrel = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy0to1_barrel","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy0to1_overlap = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy0to1_overlap","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_12_14 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_12_14","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_14_16 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_14_16","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_16_18 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_16_18","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_18_20 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_18_20","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_20_22 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_20_22","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_22_24 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_22_24","", 100,0.,1.,50,0.,50.)

    L1Mu_L1Tk_dRvspt_fid_dxy1to50_barrel = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy1to50_barrel","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy1to50_overlap = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy1to50_overlap","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_12_14 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_12_14","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_14_16 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_14_16","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_16_18 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_16_18","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_18_20 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_18_20","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_20_22 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_20_22","", 100,0.,1.,50,0.,50.)
    L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_22_24 = TH2F("L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_22_24","", 100,0.,1.,50,0.,50.)

    L1Mu_dxyvslxy_fid = TH2F("L1Mu_dxyvslxy_fid","; dxy [cm]; Lxy [cm]",100,0.01,100.,300,0.,300.)
    L1Mu_dxyvslxy_fid_endcap_22_24 = TH2F("L1Mu_dxyvslxy_fid_endcap_22_24","", 100,0.,1.,300,0.,300.)
    L1Mu_dxyvslxy_fid_endcap_22_24 = TH2F("L1Mu_dxyvslxy_fid_endcap_22_24","", 100,0.,1.,300,0.,300.)
    L1Mu_dxyvslxy_fid_endcap_22_24 = TH2F("L1Mu_dxyvslxy_fid_endcap_22_24","", 100,0.,1.,300,0.,300.)
    L1Mu_dxyvslxy_fid_endcap_22_24 = TH2F("L1Mu_dxyvslxy_fid_endcap_22_24","", 100,0.,1.,300,0.,300.)

    treeHits = ch

    for k in range(0,treeHits.GetEntries()):
      treeHits.GetEntry(k)
      if k%1000==0: print "Event", k, "nL1Mu", treeHits.nL1Mu

      for i in range(0,2):
        for j in range(0,2):
          ij = i*2+j
          
          pt = abs(treeHits.genGdMu_pt[ij])
          eta = treeHits.genGdMu_eta[ij]
          phi = abs(treeHits.genGdMu_phi[ij])
          eta_prop = treeHits.genGdMu_eta_prop[ij]
          phi_prop = treeHits.genGdMu_phi_prop[ij]
          dxy = abs(treeHits.genGdMu_dxy[ij])
          vz = abs(treeHits.genGd_vz[i])
          lxy =  abs(treeHits.genGd_lxy[i])

          ## exclude all the bad muons
          if (abs(treeHits.genGdMu_eta_prop[i*2+0])>2.4): 
            continue
          if (abs(treeHits.genGdMu_eta_prop[i*2+1])>2.4): 
            continue
          if (abs(treeHits.genGdMu_pt[i*2+0])<5): 
            continue
          if (abs(treeHits.genGdMu_pt[i*2+1])<5): 
            continue
          if (abs(treeHits.genGd0Gd1_dR) < 2):
            continue
          if (abs(treeHits.genGd_genMuMu_dR[i]) < 1):
            continue
          if treeHits.genGdMu_eta_prop[ij] == -99 or treeHits.genGdMu_phi_prop[ij] == -99:
            continue
          if lxy > 300:
            continue
          if vz > 500:
            continue

          L1Mu_index = treeHits.genGdMu_L1Mu_index_prop[ij]
          L1Mu_dR_prop = treeHits.genGdMu_L1Mu_dR_prop[ij]

          if L1Mu_index != 99:
            L1Mu_pt = treeHits.L1Mu_pt[L1Mu_index]
            L1Mu_eta = treeHits.L1Mu_eta[L1Mu_index]
            L1Mu_phi = treeHits.L1Mu_phi[L1Mu_index]
            L1Mu_bx = treeHits.L1Mu_bx[L1Mu_index]
            L1Mu_quality = treeHits.L1Mu_quality[L1Mu_index]
            L1Mu_L1Tk_dR_prop = treeHits.L1Mu_L1Tk_dR_prop[L1Mu_index]
            L1Mu_L1Tk_pt_prop = treeHits.L1Mu_L1Tk_pt_prop[L1Mu_index]
            L1Mu_L1Tk_dR_prop_true = treeHits.L1Mu_L1Tk_dR_prop_true[L1Mu_index]
            
            dxy_region1 = dxy<=0.1
            dxy_region5 = dxy<=1
            dxy_region2 = 1<dxy and dxy<=5
            dxy_region3 = 5<dxy and dxy<=10
            dxy_region4 = 10<dxy and dxy<=50
            dxy_region6 = 1<dxy and dxy<=50

            eta_all = abs(eta_prop)<=2.4 
            eta_barrel = abs(eta_prop)<0.9
            eta_overlap = abs(eta_prop)<=1.2 and abs(eta_prop)>0.9
            eta_endcap = abs(eta_prop)<=2.4 and abs(eta_prop)>1.2

            eta_region1 = abs(eta_prop)<=1.4 and abs(eta_prop)>1.2 
            eta_region2 = abs(eta_prop)<=1.6 and abs(eta_prop)>1.4
            eta_region3 = abs(eta_prop)<=1.8 and abs(eta_prop)>1.6
            eta_region4 = abs(eta_prop)<=2.0 and abs(eta_prop)>1.8
            eta_region5 = abs(eta_prop)<=2.2 and abs(eta_prop)>2.0
            eta_region6 = abs(eta_prop)<=2.4 and abs(eta_prop)>2.2

            L1Mu_dxyvslxy_fid.Fill(dxy, lxy)

            if eta_all: genGdMu_L1Mu_dR_fid.Fill(L1Mu_dR_prop)
            if dxy_region1 and eta_all: genGdMu_L1Mu_dR_fid_dxy0to0p1.Fill(L1Mu_dR_prop)
            if dxy_region2 and eta_all: genGdMu_L1Mu_dR_fid_dxy1to5.Fill(L1Mu_dR_prop)
            if dxy_region3 and eta_all: genGdMu_L1Mu_dR_fid_dxy5to10.Fill(L1Mu_dR_prop)
            if dxy_region4 and eta_all: genGdMu_L1Mu_dR_fid_dxy10to50.Fill(L1Mu_dR_prop)
            
            if eta_barrel: genGdMu_L1Mu_dR_fid_barrel.Fill(L1Mu_dR_prop)
            if dxy_region1 and eta_barrel: genGdMu_L1Mu_dR_fid_dxy0to0p1_barrel.Fill(L1Mu_dR_prop)
            if dxy_region2 and eta_barrel: genGdMu_L1Mu_dR_fid_dxy1to5_barrel.Fill(L1Mu_dR_prop)
            if dxy_region3 and eta_barrel: genGdMu_L1Mu_dR_fid_dxy5to10_barrel.Fill(L1Mu_dR_prop)
            if dxy_region4 and eta_barrel: genGdMu_L1Mu_dR_fid_dxy10to50_barrel.Fill(L1Mu_dR_prop)

            if eta_overlap: genGdMu_L1Mu_dR_fid_overlap.Fill(L1Mu_dR_prop)
            if dxy_region1 and eta_overlap: genGdMu_L1Mu_dR_fid_dxy0to0p1_overlap.Fill(L1Mu_dR_prop)
            if dxy_region2 and eta_overlap: genGdMu_L1Mu_dR_fid_dxy1to5_overlap.Fill(L1Mu_dR_prop)
            if dxy_region3 and eta_overlap: genGdMu_L1Mu_dR_fid_dxy5to10_overlap.Fill(L1Mu_dR_prop)
            if dxy_region4 and eta_overlap: genGdMu_L1Mu_dR_fid_dxy10to50_overlap.Fill(L1Mu_dR_prop)

            if eta_endcap: genGdMu_L1Mu_dR_fid_endcap.Fill(L1Mu_dR_prop)
            if dxy_region1 and eta_endcap: genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap.Fill(L1Mu_dR_prop)
            if dxy_region2 and eta_endcap: genGdMu_L1Mu_dR_fid_dxy1to5_endcap.Fill(L1Mu_dR_prop)
            if dxy_region3 and eta_endcap: genGdMu_L1Mu_dR_fid_dxy5to10_endcap.Fill(L1Mu_dR_prop)
            if dxy_region4 and eta_endcap: genGdMu_L1Mu_dR_fid_dxy10to50_endcap.Fill(L1Mu_dR_prop)

            if eta_region1: genGdMu_L1Mu_dR_fid_endcap_12_14.Fill(L1Mu_dR_prop)
            if dxy_region1 and eta_region1: genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_12_14.Fill(L1Mu_dR_prop)
            if dxy_region2 and eta_region1: genGdMu_L1Mu_dR_fid_dxy1to5_endcap_12_14.Fill(L1Mu_dR_prop)
            if dxy_region3 and eta_region1: genGdMu_L1Mu_dR_fid_dxy5to10_endcap_12_14.Fill(L1Mu_dR_prop)
            if dxy_region4 and eta_region1: genGdMu_L1Mu_dR_fid_dxy10to50_endcap_12_14.Fill(L1Mu_dR_prop)

            if eta_region2: genGdMu_L1Mu_dR_fid_endcap_14_16.Fill(L1Mu_dR_prop)
            if dxy_region1 and eta_region2: genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_14_16.Fill(L1Mu_dR_prop)
            if dxy_region2 and eta_region2: genGdMu_L1Mu_dR_fid_dxy1to5_endcap_14_16.Fill(L1Mu_dR_prop)
            if dxy_region3 and eta_region2: genGdMu_L1Mu_dR_fid_dxy5to10_endcap_14_16.Fill(L1Mu_dR_prop)
            if dxy_region4 and eta_region2: genGdMu_L1Mu_dR_fid_dxy10to50_endcap_14_16.Fill(L1Mu_dR_prop)

            if eta_region3: genGdMu_L1Mu_dR_fid_endcap_16_18.Fill(L1Mu_dR_prop)
            if dxy_region1 and eta_region3: genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_16_18.Fill(L1Mu_dR_prop)
            if dxy_region2 and eta_region3: genGdMu_L1Mu_dR_fid_dxy1to5_endcap_16_18.Fill(L1Mu_dR_prop)
            if dxy_region3 and eta_region3: genGdMu_L1Mu_dR_fid_dxy5to10_endcap_16_18.Fill(L1Mu_dR_prop)
            if dxy_region4 and eta_region3: genGdMu_L1Mu_dR_fid_dxy10to50_endcap_16_18.Fill(L1Mu_dR_prop)

            if eta_region4: genGdMu_L1Mu_dR_fid_endcap_18_20.Fill(L1Mu_dR_prop)
            if dxy_region1 and eta_region4: genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_18_20.Fill(L1Mu_dR_prop)
            if dxy_region2 and eta_region4: genGdMu_L1Mu_dR_fid_dxy1to5_endcap_18_20.Fill(L1Mu_dR_prop)
            if dxy_region3 and eta_region4: genGdMu_L1Mu_dR_fid_dxy5to10_endcap_18_20.Fill(L1Mu_dR_prop)
            if dxy_region4 and eta_region4: genGdMu_L1Mu_dR_fid_dxy10to50_endcap_18_20.Fill(L1Mu_dR_prop)

            if eta_region5: genGdMu_L1Mu_dR_fid_endcap_20_22.Fill(L1Mu_dR_prop)
            if dxy_region1 and eta_region5: genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_20_22.Fill(L1Mu_dR_prop)
            if dxy_region2 and eta_region5: genGdMu_L1Mu_dR_fid_dxy1to5_endcap_20_22.Fill(L1Mu_dR_prop)
            if dxy_region3 and eta_region5: genGdMu_L1Mu_dR_fid_dxy5to10_endcap_20_22.Fill(L1Mu_dR_prop)
            if dxy_region4 and eta_region5: genGdMu_L1Mu_dR_fid_dxy10to50_endcap_20_22.Fill(L1Mu_dR_prop)

            if eta_region6: genGdMu_L1Mu_dR_fid_endcap_22_24.Fill(L1Mu_dR_prop)
            if dxy_region1 and eta_region6: genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_22_24.Fill(L1Mu_dR_prop)
            if dxy_region2 and eta_region6: genGdMu_L1Mu_dR_fid_dxy1to5_endcap_22_24.Fill(L1Mu_dR_prop)
            if dxy_region3 and eta_region6: genGdMu_L1Mu_dR_fid_dxy5to10_endcap_22_24.Fill(L1Mu_dR_prop)
            if dxy_region4 and eta_region6: genGdMu_L1Mu_dR_fid_dxy10to50_endcap_22_24.Fill(L1Mu_dR_prop)

            good_L1Mu = L1Mu_quality>=4 and abs(L1Mu_bx)==0 and L1Mu_dR_prop<=0.2

            if good_L1Mu: 
              L1Mu_L1Tk_dR_fid.Fill(L1Mu_L1Tk_dR_prop)
              if eta_barrel: L1Mu_L1Tk_dR_fid_barrel.Fill(L1Mu_L1Tk_dR_prop)
              if eta_overlap: L1Mu_L1Tk_dR_fid_overlap.Fill(L1Mu_L1Tk_dR_prop)
              if eta_endcap: L1Mu_L1Tk_dR_fid_endcap.Fill(L1Mu_L1Tk_dR_prop)
              if eta_region1: L1Mu_L1Tk_dR_fid_endcap_12_14.Fill(L1Mu_L1Tk_dR_prop)
              if eta_region2: L1Mu_L1Tk_dR_fid_endcap_14_16.Fill(L1Mu_L1Tk_dR_prop)
              if eta_region3: L1Mu_L1Tk_dR_fid_endcap_16_18.Fill(L1Mu_L1Tk_dR_prop)
              if eta_region4: L1Mu_L1Tk_dR_fid_endcap_18_20.Fill(L1Mu_L1Tk_dR_prop)
              if eta_region5: L1Mu_L1Tk_dR_fid_endcap_20_22.Fill(L1Mu_L1Tk_dR_prop)
              if eta_region6: L1Mu_L1Tk_dR_fid_endcap_22_24.Fill(L1Mu_L1Tk_dR_prop)              



              if dxy_region1: 
                L1Mu_L1Tk_dR_fid_dxy0to0p1.Fill(L1Mu_L1Tk_dR_prop)
                if eta_barrel: L1Mu_L1Tk_dR_fid_dxy0to0p1_barrel.Fill(L1Mu_L1Tk_dR_prop)
                if eta_overlap: L1Mu_L1Tk_dR_fid_dxy0to0p1_overlap.Fill(L1Mu_L1Tk_dR_prop)
                if eta_endcap: L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region1: L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_12_14.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region2: L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_14_16.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region3: L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_16_18.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region4: L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_18_20.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region5: L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_20_22.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region6: L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_22_24.Fill(L1Mu_L1Tk_dR_prop)              

              if dxy_region5: 
                L1Mu_L1Tk_dR_fid_dxy0to1.Fill(L1Mu_L1Tk_dR_prop)
                if eta_barrel: L1Mu_L1Tk_dR_fid_dxy0to1_barrel.Fill(L1Mu_L1Tk_dR_prop)
                if eta_overlap: L1Mu_L1Tk_dR_fid_dxy0to1_overlap.Fill(L1Mu_L1Tk_dR_prop)
                if eta_endcap: L1Mu_L1Tk_dR_fid_dxy0to1_endcap.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region1: L1Mu_L1Tk_dR_fid_dxy0to1_endcap_12_14.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region2: L1Mu_L1Tk_dR_fid_dxy0to1_endcap_14_16.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region3: L1Mu_L1Tk_dR_fid_dxy0to1_endcap_16_18.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region4: L1Mu_L1Tk_dR_fid_dxy0to1_endcap_18_20.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region5: L1Mu_L1Tk_dR_fid_dxy0to1_endcap_20_22.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region6: L1Mu_L1Tk_dR_fid_dxy0to1_endcap_22_24.Fill(L1Mu_L1Tk_dR_prop)              
                
              if dxy_region2: 
                L1Mu_L1Tk_dR_fid_dxy1to5.Fill(L1Mu_L1Tk_dR_prop)
                if eta_barrel: L1Mu_L1Tk_dR_fid_dxy1to5_barrel.Fill(L1Mu_L1Tk_dR_prop)
                if eta_overlap: L1Mu_L1Tk_dR_fid_dxy1to5_overlap.Fill(L1Mu_L1Tk_dR_prop)
                if eta_endcap: L1Mu_L1Tk_dR_fid_dxy1to5_endcap.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region1: L1Mu_L1Tk_dR_fid_dxy1to5_endcap_12_14.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region2: L1Mu_L1Tk_dR_fid_dxy1to5_endcap_14_16.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region3: L1Mu_L1Tk_dR_fid_dxy1to5_endcap_16_18.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region4: L1Mu_L1Tk_dR_fid_dxy1to5_endcap_18_20.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region5: L1Mu_L1Tk_dR_fid_dxy1to5_endcap_20_22.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region6: L1Mu_L1Tk_dR_fid_dxy1to5_endcap_22_24.Fill(L1Mu_L1Tk_dR_prop)              

              if dxy_region3: 
                L1Mu_L1Tk_dR_fid_dxy5to10.Fill(L1Mu_L1Tk_dR_prop)
                if eta_barrel: L1Mu_L1Tk_dR_fid_dxy5to10_barrel.Fill(L1Mu_L1Tk_dR_prop)
                if eta_overlap: L1Mu_L1Tk_dR_fid_dxy5to10_overlap.Fill(L1Mu_L1Tk_dR_prop)
                if eta_endcap: L1Mu_L1Tk_dR_fid_dxy5to10_endcap.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region1: L1Mu_L1Tk_dR_fid_dxy5to10_endcap_12_14.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region2: L1Mu_L1Tk_dR_fid_dxy5to10_endcap_14_16.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region3: L1Mu_L1Tk_dR_fid_dxy5to10_endcap_16_18.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region4: L1Mu_L1Tk_dR_fid_dxy5to10_endcap_18_20.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region5: L1Mu_L1Tk_dR_fid_dxy5to10_endcap_20_22.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region6: L1Mu_L1Tk_dR_fid_dxy5to10_endcap_22_24.Fill(L1Mu_L1Tk_dR_prop)
              
              if dxy_region4: 
                L1Mu_L1Tk_dR_fid_dxy10to50.Fill(L1Mu_L1Tk_dR_prop)
                if eta_barrel: L1Mu_L1Tk_dR_fid_dxy10to50_barrel.Fill(L1Mu_L1Tk_dR_prop)
                if eta_overlap: L1Mu_L1Tk_dR_fid_dxy10to50_overlap.Fill(L1Mu_L1Tk_dR_prop)
                if eta_endcap: L1Mu_L1Tk_dR_fid_dxy10to50_endcap.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region1: L1Mu_L1Tk_dR_fid_dxy10to50_endcap_12_14.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region2: L1Mu_L1Tk_dR_fid_dxy10to50_endcap_14_16.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region3: L1Mu_L1Tk_dR_fid_dxy10to50_endcap_16_18.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region4: L1Mu_L1Tk_dR_fid_dxy10to50_endcap_18_20.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region5: L1Mu_L1Tk_dR_fid_dxy10to50_endcap_20_22.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region6: L1Mu_L1Tk_dR_fid_dxy10to50_endcap_22_24.Fill(L1Mu_L1Tk_dR_prop)              

              if dxy_region6: 
                L1Mu_L1Tk_dR_fid_dxy1to50.Fill(L1Mu_L1Tk_dR_prop)
                if eta_barrel: L1Mu_L1Tk_dR_fid_dxy1to50_barrel.Fill(L1Mu_L1Tk_dR_prop)
                if eta_overlap: L1Mu_L1Tk_dR_fid_dxy1to50_overlap.Fill(L1Mu_L1Tk_dR_prop)
                if eta_endcap:  L1Mu_L1Tk_dR_fid_dxy1to50_endcap.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region1: L1Mu_L1Tk_dR_fid_dxy1to50_endcap_12_14.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region2: L1Mu_L1Tk_dR_fid_dxy1to50_endcap_14_16.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region3: L1Mu_L1Tk_dR_fid_dxy1to50_endcap_16_18.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region4: L1Mu_L1Tk_dR_fid_dxy1to50_endcap_18_20.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region5: L1Mu_L1Tk_dR_fid_dxy1to50_endcap_20_22.Fill(L1Mu_L1Tk_dR_prop)
                if eta_region6: L1Mu_L1Tk_dR_fid_dxy1to50_endcap_22_24.Fill(L1Mu_L1Tk_dR_prop)              

              L1Mu_L1Tk_pt_fid.Fill(L1Mu_L1Tk_pt_prop)
              if eta_barrel: L1Mu_L1Tk_pt_fid_barrel.Fill(L1Mu_L1Tk_pt_prop)
              if eta_overlap: L1Mu_L1Tk_pt_fid_overlap.Fill(L1Mu_L1Tk_pt_prop)
              if eta_endcap: L1Mu_L1Tk_pt_fid_endcap.Fill(L1Mu_L1Tk_pt_prop)
              if eta_region1: L1Mu_L1Tk_pt_fid_endcap_12_14.Fill(L1Mu_L1Tk_pt_prop)
              if eta_region2: L1Mu_L1Tk_pt_fid_endcap_14_16.Fill(L1Mu_L1Tk_pt_prop)
              if eta_region3: L1Mu_L1Tk_pt_fid_endcap_16_18.Fill(L1Mu_L1Tk_pt_prop)
              if eta_region4: L1Mu_L1Tk_pt_fid_endcap_18_20.Fill(L1Mu_L1Tk_pt_prop)
              if eta_region5: L1Mu_L1Tk_pt_fid_endcap_20_22.Fill(L1Mu_L1Tk_pt_prop)
              if eta_region6: L1Mu_L1Tk_pt_fid_endcap_22_24.Fill(L1Mu_L1Tk_pt_prop)              

              if dxy_region1: 
                L1Mu_L1Tk_pt_fid_dxy0to0p1.Fill(L1Mu_L1Tk_pt_prop)
                if eta_barrel: L1Mu_L1Tk_pt_fid_dxy0to0p1_barrel.Fill(L1Mu_L1Tk_pt_prop)
                if eta_overlap: L1Mu_L1Tk_pt_fid_dxy0to0p1_overlap.Fill(L1Mu_L1Tk_pt_prop)
                if eta_endcap: L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region1: L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_12_14.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region2: L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_14_16.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region3: L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_16_18.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region4: L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_18_20.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region5: L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_20_22.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region6: L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_22_24.Fill(L1Mu_L1Tk_pt_prop)              

              if dxy_region5: 
                L1Mu_L1Tk_pt_fid_dxy0to1.Fill(L1Mu_L1Tk_pt_prop)
                if eta_barrel: L1Mu_L1Tk_pt_fid_dxy0to1_barrel.Fill(L1Mu_L1Tk_pt_prop)
                if eta_overlap: L1Mu_L1Tk_pt_fid_dxy0to1_overlap.Fill(L1Mu_L1Tk_pt_prop)
                if eta_endcap: L1Mu_L1Tk_pt_fid_dxy0to1_endcap.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region1: L1Mu_L1Tk_pt_fid_dxy0to1_endcap_12_14.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region2: L1Mu_L1Tk_pt_fid_dxy0to1_endcap_14_16.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region3: L1Mu_L1Tk_pt_fid_dxy0to1_endcap_16_18.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region4: L1Mu_L1Tk_pt_fid_dxy0to1_endcap_18_20.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region5: L1Mu_L1Tk_pt_fid_dxy0to1_endcap_20_22.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region6: L1Mu_L1Tk_pt_fid_dxy0to1_endcap_22_24.Fill(L1Mu_L1Tk_pt_prop)              

              if dxy_region2: 
                L1Mu_L1Tk_pt_fid_dxy1to5.Fill(L1Mu_L1Tk_pt_prop)
                if eta_barrel: L1Mu_L1Tk_pt_fid_dxy1to5_barrel.Fill(L1Mu_L1Tk_pt_prop)
                if eta_overlap: L1Mu_L1Tk_pt_fid_dxy1to5_overlap.Fill(L1Mu_L1Tk_pt_prop)
                if eta_endcap: L1Mu_L1Tk_pt_fid_dxy1to5_endcap.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region1: L1Mu_L1Tk_pt_fid_dxy1to5_endcap_12_14.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region2: L1Mu_L1Tk_pt_fid_dxy1to5_endcap_14_16.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region3: L1Mu_L1Tk_pt_fid_dxy1to5_endcap_16_18.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region4: L1Mu_L1Tk_pt_fid_dxy1to5_endcap_18_20.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region5: L1Mu_L1Tk_pt_fid_dxy1to5_endcap_20_22.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region6: L1Mu_L1Tk_pt_fid_dxy1to5_endcap_22_24.Fill(L1Mu_L1Tk_pt_prop)              

              if dxy_region3: 
                L1Mu_L1Tk_pt_fid_dxy5to10.Fill(L1Mu_L1Tk_pt_prop)
                if eta_barrel: L1Mu_L1Tk_pt_fid_dxy5to10_barrel.Fill(L1Mu_L1Tk_pt_prop)
                if eta_overlap: L1Mu_L1Tk_pt_fid_dxy5to10_overlap.Fill(L1Mu_L1Tk_pt_prop)
                if eta_endcap: L1Mu_L1Tk_pt_fid_dxy5to10_endcap.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region1: L1Mu_L1Tk_pt_fid_dxy5to10_endcap_12_14.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region2: L1Mu_L1Tk_pt_fid_dxy5to10_endcap_14_16.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region3: L1Mu_L1Tk_pt_fid_dxy5to10_endcap_16_18.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region4: L1Mu_L1Tk_pt_fid_dxy5to10_endcap_18_20.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region5: L1Mu_L1Tk_pt_fid_dxy5to10_endcap_20_22.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region6: L1Mu_L1Tk_pt_fid_dxy5to10_endcap_22_24.Fill(L1Mu_L1Tk_pt_prop)              

              if dxy_region4: 
                L1Mu_L1Tk_pt_fid_dxy10to50.Fill(L1Mu_L1Tk_pt_prop)
                if eta_barrel: L1Mu_L1Tk_pt_fid_dxy10to50_barrel.Fill(L1Mu_L1Tk_pt_prop)
                if eta_overlap: L1Mu_L1Tk_pt_fid_dxy10to50_overlap.Fill(L1Mu_L1Tk_pt_prop)
                if eta_endcap: L1Mu_L1Tk_pt_fid_dxy10to50_endcap.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region1: L1Mu_L1Tk_pt_fid_dxy10to50_endcap_12_14.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region2: L1Mu_L1Tk_pt_fid_dxy10to50_endcap_14_16.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region3: L1Mu_L1Tk_pt_fid_dxy10to50_endcap_16_18.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region4: L1Mu_L1Tk_pt_fid_dxy10to50_endcap_18_20.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region5: L1Mu_L1Tk_pt_fid_dxy10to50_endcap_20_22.Fill(L1Mu_L1Tk_pt_prop)
                if eta_region6: L1Mu_L1Tk_pt_fid_dxy10to50_endcap_22_24.Fill(L1Mu_L1Tk_pt_prop)              
                
              ### 2D plots
              if dxy_region1: 
                if eta_barrel: L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_barrel.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_overlap: L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_overlap.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region1: L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_12_14.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region2: L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_14_16.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region3: L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_16_18.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region4: L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_18_20.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region5: L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_20_22.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region6: L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_22_24.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
              if dxy_region2: 
                if eta_barrel: L1Mu_L1Tk_dRvspt_fid_dxy1to5_barrel.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_overlap: L1Mu_L1Tk_dRvspt_fid_dxy1to5_overlap.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region1: L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_12_14.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region2: L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_14_16.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region3: L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_16_18.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region4: L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_18_20.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region5: L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_20_22.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region6: L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_22_24.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
              if dxy_region3: 
                if eta_barrel: L1Mu_L1Tk_dRvspt_fid_dxy5to10_barrel.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_overlap: L1Mu_L1Tk_dRvspt_fid_dxy5to10_overlap.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region1: L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_12_14.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region2: L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_14_16.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region3: L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_16_18.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region4: L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_18_20.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region5: L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_20_22.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region6: L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_22_24.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
              if dxy_region4: 
                if eta_barrel: L1Mu_L1Tk_dRvspt_fid_dxy10to50_barrel.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_overlap: L1Mu_L1Tk_dRvspt_fid_dxy10to50_overlap.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region1: L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_12_14.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region2: L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_14_16.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region3: L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_16_18.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region4: L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_18_20.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region5: L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_20_22.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region6: L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_22_24.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)

              if dxy<=1:
                if eta_barrel: L1Mu_L1Tk_dRvspt_fid_dxy0to1_barrel.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_overlap: L1Mu_L1Tk_dRvspt_fid_dxy0to1_overlap.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region1: L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_12_14.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region2: L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_14_16.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region3: L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_16_18.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region4: L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_18_20.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region5: L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_20_22.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region6: L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_22_24.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)              
              if 1<dxy and dxy<=50:
                if eta_barrel: L1Mu_L1Tk_dRvspt_fid_dxy1to50_barrel.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_overlap: L1Mu_L1Tk_dRvspt_fid_dxy1to50_overlap.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region1: L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_12_14.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region2: L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_14_16.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region3: L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_16_18.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region4: L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_18_20.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region5: L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_20_22.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)
                if eta_region6: L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_22_24.Fill(L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt_prop)              

            extra_cuts = L1Mu_quality>=4 and abs(L1Mu_bx)==0
            if extra_cuts: L1Mu_L1Tk_dR_true_fid.Fill(L1Mu_L1Tk_dR_prop_true)
            if dxy_region1 and extra_cuts: L1Mu_L1Tk_dR_true_fid_dxy0to0p1.Fill(L1Mu_L1Tk_dR_prop_true)
            if dxy_region2 and extra_cuts: L1Mu_L1Tk_dR_true_fid_dxy1to5.Fill(L1Mu_L1Tk_dR_prop_true)
            if dxy_region3 and extra_cuts: L1Mu_L1Tk_dR_true_fid_dxy5to10.Fill(L1Mu_L1Tk_dR_prop_true)
            if dxy_region4 and extra_cuts: L1Mu_L1Tk_dR_true_fid_dxy10to50.Fill(L1Mu_L1Tk_dR_prop_true)

            
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid, "genGdMu_L1Mu_dR_fid")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy0to0p1, "genGdMu_L1Mu_dR_fid_dxy0to0p1")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy1to5, "genGdMu_L1Mu_dR_fid_dxy1to5")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy5to10, "genGdMu_L1Mu_dR_fid_dxy5to10")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy10to50, "genGdMu_L1Mu_dR_fid_dxy10to50")

    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_barrel, "genGdMu_L1Mu_dR_fid_barrel")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy0to0p1_barrel, "genGdMu_L1Mu_dR_fid_dxy0to0p1_barrel")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy1to5_barrel, "genGdMu_L1Mu_dR_fid_dxy1to5_barrel")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy5to10_barrel, "genGdMu_L1Mu_dR_fid_dxy5to10_barrel")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy10to50_barrel, "genGdMu_L1Mu_dR_fid_dxy10to50_barrel")

    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_overlap, "genGdMu_L1Mu_dR_fid_overlap")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy0to0p1_overlap, "genGdMu_L1Mu_dR_fid_dxy0to0p1_overlap")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy1to5_overlap, "genGdMu_L1Mu_dR_fid_dxy1to5_overlap")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy5to10_overlap, "genGdMu_L1Mu_dR_fid_dxy5to10_overlap")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy10to50_overlap, "genGdMu_L1Mu_dR_fid_dxy10to50_overlap")

    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_endcap, "genGdMu_L1Mu_dR_fid_endcap")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap, "genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy1to5_endcap, "genGdMu_L1Mu_dR_fid_dxy1to5_endcap")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy5to10_endcap, "genGdMu_L1Mu_dR_fid_dxy5to10_endcap")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy10to50_endcap, "genGdMu_L1Mu_dR_fid_dxy10to50_endcap")

    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_endcap_12_14, "genGdMu_L1Mu_dR_fid_endcap_12_14")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_12_14, "genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_12_14")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy1to5_endcap_12_14, "genGdMu_L1Mu_dR_fid_dxy1to5_endcap_12_14")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy5to10_endcap_12_14, "genGdMu_L1Mu_dR_fid_dxy5to10_endcap_12_14")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy10to50_endcap_12_14, "genGdMu_L1Mu_dR_fid_dxy10to50_endcap_12_14")

    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_endcap_14_16, "genGdMu_L1Mu_dR_fid_endcap_14_16")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_14_16, "genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_14_16")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy1to5_endcap_14_16, "genGdMu_L1Mu_dR_fid_dxy1to5_endcap_14_16")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy5to10_endcap_14_16, "genGdMu_L1Mu_dR_fid_dxy5to10_endcap_14_16")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy10to50_endcap_14_16, "genGdMu_L1Mu_dR_fid_dxy10to50_endcap_14_16")

    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_endcap_16_18, "genGdMu_L1Mu_dR_fid_endcap_16_18")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_16_18, "genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_16_18")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy1to5_endcap_16_18, "genGdMu_L1Mu_dR_fid_dxy1to5_endcap_16_18")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy5to10_endcap_16_18, "genGdMu_L1Mu_dR_fid_dxy5to10_endcap_16_18")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy10to50_endcap_16_18, "genGdMu_L1Mu_dR_fid_dxy10to50_endcap_16_18")

    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_endcap_18_20, "genGdMu_L1Mu_dR_fid_endcap_18_20")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_18_20, "genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_18_20")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy1to5_endcap_18_20, "genGdMu_L1Mu_dR_fid_dxy1to5_endcap_18_20")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy5to10_endcap_18_20, "genGdMu_L1Mu_dR_fid_dxy5to10_endcap_18_20")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy10to50_endcap_18_20, "genGdMu_L1Mu_dR_fid_dxy10to50_endcap_18_20")

    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_endcap_20_22, "genGdMu_L1Mu_dR_fid_endcap_20_22")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_20_22, "genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_20_22")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy1to5_endcap_20_22, "genGdMu_L1Mu_dR_fid_dxy1to5_endcap_20_22")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy5to10_endcap_20_22, "genGdMu_L1Mu_dR_fid_dxy5to10_endcap_20_22")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy10to50_endcap_20_22, "genGdMu_L1Mu_dR_fid_dxy10to50_endcap_20_22")

    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_endcap_22_24, "genGdMu_L1Mu_dR_fid_endcap_22_24")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_22_24, "genGdMu_L1Mu_dR_fid_dxy0to0p1_endcap_22_24")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy1to5_endcap_22_24, "genGdMu_L1Mu_dR_fid_dxy1to5_endcap_22_24")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy5to10_endcap_22_24, "genGdMu_L1Mu_dR_fid_dxy5to10_endcap_22_24")
    makeSimplePlot(thisTargetDir, genGdMu_L1Mu_dR_fid_dxy10to50_endcap_22_24, "genGdMu_L1Mu_dR_fid_dxy10to50_endcap_22_24")

    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid, "L1Mu_L1Tk_dR_fid")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy0to0p1, "L1Mu_L1Tk_dR_fid_dxy0to0p1")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy0to1, "L1Mu_L1Tk_dR_fid_dxy0to1")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy1to5, "L1Mu_L1Tk_dR_fid_dxy1to5")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy5to10, "L1Mu_L1Tk_dR_fid_dxy5to10")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy10to50, "L1Mu_L1Tk_dR_fid_dxy10to50")

    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_barrel, "L1Mu_L1Tk_dR_fid_barrel")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy0to0p1_barrel, "L1Mu_L1Tk_dR_fid_dxy0to0p1_barrel")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy0to1_barrel, "L1Mu_L1Tk_dR_fid_dxy0to1_barrel")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy1to5_barrel, "L1Mu_L1Tk_dR_fid_dxy1to5_barrel")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy5to10_barrel, "L1Mu_L1Tk_dR_fid_dxy5to10_barrel")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy10to50_barrel, "L1Mu_L1Tk_dR_fid_dxy10to50_barrel")

    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_overlap, "L1Mu_L1Tk_dR_fid_overlap")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy0to0p1_overlap, "L1Mu_L1Tk_dR_fid_dxy0to0p1_overlap")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy0to1_overlap, "L1Mu_L1Tk_dR_fid_dxy0to1_overlap")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy1to5_overlap, "L1Mu_L1Tk_dR_fid_dxy1to5_overlap")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy5to10_overlap, "L1Mu_L1Tk_dR_fid_dxy5to10_overlap")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy10to50_overlap, "L1Mu_L1Tk_dR_fid_dxy10to50_overlap")

    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_endcap, "L1Mu_L1Tk_dR_fid_endcap")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap, "L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy0to1_endcap, "L1Mu_L1Tk_dR_fid_dxy0to1_endcap")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy1to5_endcap, "L1Mu_L1Tk_dR_fid_dxy1to5_endcap")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy5to10_endcap, "L1Mu_L1Tk_dR_fid_dxy5to10_endcap")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy10to50_endcap, "L1Mu_L1Tk_dR_fid_dxy10to50_endcap")

    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_endcap_12_14, "L1Mu_L1Tk_dR_fid_endcap_12_14")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_12_14, "L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_12_14")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy0to1_endcap_12_14, "L1Mu_L1Tk_dR_fid_dxy0to1_endcap_12_14")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy1to5_endcap_12_14, "L1Mu_L1Tk_dR_fid_dxy1to5_endcap_12_14")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy5to10_endcap_12_14, "L1Mu_L1Tk_dR_fid_dxy5to10_endcap_12_14")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy10to50_endcap_12_14, "L1Mu_L1Tk_dR_fid_dxy10to50_endcap_12_14")

    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_endcap_14_16, "L1Mu_L1Tk_dR_fid_endcap_14_16")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_14_16, "L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_14_16")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy0to1_endcap_14_16, "L1Mu_L1Tk_dR_fid_dxy0to1_endcap_14_16")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy1to5_endcap_14_16, "L1Mu_L1Tk_dR_fid_dxy1to5_endcap_14_16")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy5to10_endcap_14_16, "L1Mu_L1Tk_dR_fid_dxy5to10_endcap_14_16")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy10to50_endcap_14_16, "L1Mu_L1Tk_dR_fid_dxy10to50_endcap_14_16")

    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_endcap_16_18, "L1Mu_L1Tk_dR_fid_endcap_16_18")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_16_18, "L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_16_18")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy0to1_endcap_16_18, "L1Mu_L1Tk_dR_fid_dxy0to1_endcap_16_18")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy1to5_endcap_16_18, "L1Mu_L1Tk_dR_fid_dxy1to5_endcap_16_18")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy5to10_endcap_16_18, "L1Mu_L1Tk_dR_fid_dxy5to10_endcap_16_18")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy10to50_endcap_16_18, "L1Mu_L1Tk_dR_fid_dxy10to50_endcap_16_18")

    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_endcap_18_20, "L1Mu_L1Tk_dR_fid_endcap_18_20")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_18_20, "L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_18_20")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy0to1_endcap_18_20, "L1Mu_L1Tk_dR_fid_dxy0to1_endcap_18_20")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy1to5_endcap_18_20, "L1Mu_L1Tk_dR_fid_dxy1to5_endcap_18_20")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy5to10_endcap_18_20, "L1Mu_L1Tk_dR_fid_dxy5to10_endcap_18_20")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy10to50_endcap_18_20, "L1Mu_L1Tk_dR_fid_dxy10to50_endcap_18_20")

    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_endcap_20_22, "L1Mu_L1Tk_dR_fid_endcap_20_22")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_20_22, "L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_20_22")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy0to1_endcap_20_22, "L1Mu_L1Tk_dR_fid_dxy0to1_endcap_20_22")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy1to5_endcap_20_22, "L1Mu_L1Tk_dR_fid_dxy1to5_endcap_20_22")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy5to10_endcap_20_22, "L1Mu_L1Tk_dR_fid_dxy5to10_endcap_20_22")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy10to50_endcap_20_22, "L1Mu_L1Tk_dR_fid_dxy10to50_endcap_20_22")

    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_endcap_22_24, "L1Mu_L1Tk_dR_fid_endcap_22_24")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_22_24, "L1Mu_L1Tk_dR_fid_dxy0to0p1_endcap_22_24")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy0to1_endcap_22_24, "L1Mu_L1Tk_dR_fid_dxy0to1_endcap_22_24")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy1to5_endcap_22_24, "L1Mu_L1Tk_dR_fid_dxy1to5_endcap_22_24")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy5to10_endcap_22_24, "L1Mu_L1Tk_dR_fid_dxy5to10_endcap_22_24")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy10to50_endcap_22_24, "L1Mu_L1Tk_dR_fid_dxy10to50_endcap_22_24")

    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy1to50,"L1Mu_L1Tk_dR_fid_dxy1to50")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy1to50_barrel,"L1Mu_L1Tk_dR_fid_dxy1to50_barrel")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy1to50_overlap,"L1Mu_L1Tk_dR_fid_dxy1to50_overlap")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy1to50_endcap,"L1Mu_L1Tk_dR_fid_dxy1to50_endcap")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy1to50_endcap_12_14,"L1Mu_L1Tk_dR_fid_dxy1to50_endcap_12_14")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy1to50_endcap_14_16,"L1Mu_L1Tk_dR_fid_dxy1to50_endcap_14_16")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy1to50_endcap_16_18,"L1Mu_L1Tk_dR_fid_dxy1to50_endcap_16_18")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy1to50_endcap_18_20,"L1Mu_L1Tk_dR_fid_dxy1to50_endcap_18_20")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy1to50_endcap_20_22,"L1Mu_L1Tk_dR_fid_dxy1to50_endcap_20_22")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_fid_dxy1to50_endcap_22_24,"L1Mu_L1Tk_dR_fid_dxy1to50_endcap_22_24")

    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_true_fid, "L1Mu_L1Tk_dR_true_fid")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_true_fid_dxy0to0p1, "L1Mu_L1Tk_dR_true_fid_dxy0to0p1")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_true_fid_dxy1to5, "L1Mu_L1Tk_dR_true_fid_dxy1to5")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_true_fid_dxy5to10, "L1Mu_L1Tk_dR_true_fid_dxy5to10")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dR_true_fid_dxy10to50, "L1Mu_L1Tk_dR_true_fid_dxy10to50")

    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid, "L1Mu_L1Tk_pt_fid")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy0to0p1, "L1Mu_L1Tk_pt_fid_dxy0to0p1")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy1to5, "L1Mu_L1Tk_pt_fid_dxy1to5")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy5to10, "L1Mu_L1Tk_pt_fid_dxy5to10")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy10to50, "L1Mu_L1Tk_pt_fid_dxy10to50")

    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_barrel, "L1Mu_L1Tk_pt_fid_barrel")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy0to0p1_barrel, "L1Mu_L1Tk_pt_fid_dxy0to0p1_barrel")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy1to5_barrel, "L1Mu_L1Tk_pt_fid_dxy1to5_barrel")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy5to10_barrel, "L1Mu_L1Tk_pt_fid_dxy5to10_barrel")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy10to50_barrel, "L1Mu_L1Tk_pt_fid_dxy10to50_barrel")

    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_overlap, "L1Mu_L1Tk_pt_fid_overlap")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy0to0p1_overlap, "L1Mu_L1Tk_pt_fid_dxy0to0p1_overlap")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy1to5_overlap, "L1Mu_L1Tk_pt_fid_dxy1to5_overlap")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy5to10_overlap, "L1Mu_L1Tk_pt_fid_dxy5to10_overlap")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy10to50_overlap, "L1Mu_L1Tk_pt_fid_dxy10to50_overlap")

    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_endcap, "L1Mu_L1Tk_pt_fid_endcap")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap, "L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy1to5_endcap, "L1Mu_L1Tk_pt_fid_dxy1to5_endcap")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy5to10_endcap, "L1Mu_L1Tk_pt_fid_dxy5to10_endcap")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy10to50_endcap, "L1Mu_L1Tk_pt_fid_dxy10to50_endcap")

    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_endcap_12_14, "L1Mu_L1Tk_pt_fid_endcap_12_14")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_12_14, "L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_12_14")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy0to1_endcap_12_14, "L1Mu_L1Tk_pt_fid_dxy0to1_endcap_12_14")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy1to5_endcap_12_14, "L1Mu_L1Tk_pt_fid_dxy1to5_endcap_12_14")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy5to10_endcap_12_14, "L1Mu_L1Tk_pt_fid_dxy5to10_endcap_12_14")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy10to50_endcap_12_14, "L1Mu_L1Tk_pt_fid_dxy10to50_endcap_12_14")

    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_endcap_14_16, "L1Mu_L1Tk_pt_fid_endcap_14_16")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_14_16, "L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_14_16")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy0to1_endcap_14_16, "L1Mu_L1Tk_pt_fid_dxy0to1_endcap_14_16")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy1to5_endcap_14_16, "L1Mu_L1Tk_pt_fid_dxy1to5_endcap_14_16")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy5to10_endcap_14_16, "L1Mu_L1Tk_pt_fid_dxy5to10_endcap_14_16")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy10to50_endcap_14_16, "L1Mu_L1Tk_pt_fid_dxy10to50_endcap_14_16")

    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_endcap_16_18, "L1Mu_L1Tk_pt_fid_endcap_16_18")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_16_18, "L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_16_18")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy0to1_endcap_16_18, "L1Mu_L1Tk_pt_fid_dxy0to1_endcap_16_18")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy1to5_endcap_16_18, "L1Mu_L1Tk_pt_fid_dxy1to5_endcap_16_18")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy5to10_endcap_16_18, "L1Mu_L1Tk_pt_fid_dxy5to10_endcap_16_18")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy10to50_endcap_16_18, "L1Mu_L1Tk_pt_fid_dxy10to50_endcap_16_18")

    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_endcap_18_20, "L1Mu_L1Tk_pt_fid_endcap_18_20")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_18_20, "L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_18_20")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy0to1_endcap_18_20, "L1Mu_L1Tk_pt_fid_dxy0to1_endcap_18_20")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy1to5_endcap_18_20, "L1Mu_L1Tk_pt_fid_dxy1to5_endcap_18_20")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy5to10_endcap_18_20, "L1Mu_L1Tk_pt_fid_dxy5to10_endcap_18_20")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy10to50_endcap_18_20, "L1Mu_L1Tk_pt_fid_dxy10to50_endcap_18_20")

    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_endcap_20_22, "L1Mu_L1Tk_pt_fid_endcap_20_22")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_20_22, "L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_20_22")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy0to1_endcap_20_22, "L1Mu_L1Tk_pt_fid_dxy0to1_endcap_20_22")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy1to5_endcap_20_22, "L1Mu_L1Tk_pt_fid_dxy1to5_endcap_20_22")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy5to10_endcap_20_22, "L1Mu_L1Tk_pt_fid_dxy5to10_endcap_20_22")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy10to50_endcap_20_22, "L1Mu_L1Tk_pt_fid_dxy10to50_endcap_20_22")

    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_endcap_22_24, "L1Mu_L1Tk_pt_fid_endcap_22_24")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_22_24, "L1Mu_L1Tk_pt_fid_dxy0to0p1_endcap_22_24")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy0to1_endcap_22_24, "L1Mu_L1Tk_pt_fid_dxy0to1_endcap_22_24")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy1to5_endcap_22_24, "L1Mu_L1Tk_pt_fid_dxy1to5_endcap_22_24")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy5to10_endcap_22_24, "L1Mu_L1Tk_pt_fid_dxy5to10_endcap_22_24")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_pt_fid_dxy10to50_endcap_22_24, "L1Mu_L1Tk_pt_fid_dxy10to50_endcap_22_24")

    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_barrel, "L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_barrel")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_overlap, "L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_overlap")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_12_14, "L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_12_14")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_14_16, "L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_14_16")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_16_18, "L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_16_18")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_18_20, "L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_18_20")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_20_22, "L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_20_22")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_22_24, "L1Mu_L1Tk_dRvspt_fid_dxy0to0p1_endcap_22_24")
                 
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy1to5_barrel, "L1Mu_L1Tk_dRvspt_fid_dxy1to5_barrel")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy1to5_overlap, "L1Mu_L1Tk_dRvspt_fid_dxy1to5_overlap")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_12_14, "L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_12_14")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_14_16, "L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_14_16")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_16_18, "L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_16_18")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_18_20, "L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_18_20")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_20_22, "L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_20_22")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_22_24, "L1Mu_L1Tk_dRvspt_fid_dxy1to5_endcap_22_24")

    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy5to10_barrel, "L1Mu_L1Tk_dRvspt_fid_dxy5to10_barrel")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy5to10_overlap, "L1Mu_L1Tk_dRvspt_fid_dxy5to10_overlap")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_12_14, "L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_12_14")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_14_16, "L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_14_16")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_16_18, "L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_16_18")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_18_20, "L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_18_20")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_20_22, "L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_20_22")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_22_24, "L1Mu_L1Tk_dRvspt_fid_dxy5to10_endcap_22_24")

    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy10to50_barrel, "L1Mu_L1Tk_dRvspt_fid_dxy10to50_barrel")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy10to50_overlap, "L1Mu_L1Tk_dRvspt_fid_dxy10to50_overlap")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_12_14, "L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_12_14")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_14_16, "L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_14_16")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_16_18, "L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_16_18")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_18_20, "L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_18_20")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_20_22, "L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_20_22")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_22_24, "L1Mu_L1Tk_dRvspt_fid_dxy10to50_endcap_22_24")

    makeSimplePlot(thisTargetDir, L1Mu_dxyvslxy_fid, "L1Mu_dxyvslxy_fid", True)    

    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy1to50_barrel, "L1Mu_L1Tk_dRvspt_fid_dxy1to50_barrel")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy1to50_overlap, "L1Mu_L1Tk_dRvspt_fid_dxy1to50_overlap")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_12_14, "L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_12_14")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_14_16, "L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_14_16")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_16_18, "L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_16_18")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_18_20, "L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_18_20")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_20_22, "L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_20_22")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_22_24, "L1Mu_L1Tk_dRvspt_fid_dxy1to50_endcap_22_24")

    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy0to1_barrel, "L1Mu_L1Tk_dRvspt_fid_dxy0to1_barrel")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy0to1_overlap, "L1Mu_L1Tk_dRvspt_fid_dxy0to1_overlap")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_12_14, "L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_12_14")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_14_16, "L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_14_16")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_16_18, "L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_16_18")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_18_20, "L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_18_20")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_20_22, "L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_20_22")
    makeSimplePlot(thisTargetDir, L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_22_24, "L1Mu_L1Tk_dRvspt_fid_dxy0to1_endcap_22_24")



  if eff and False:
    makedRL1MuL1TkHistogram()

  #exit()

  def makeEfficiencyHistogram():

    h_single_L1Mu_efficiency_L1Tk_pt0 = TH1F("h_single_L1Mu_efficiency_L1Tk_pt0"," ", 1000, 0, 20)
    h_single_L1Mu_efficiency_L1Tk_pt2 = TH1F("h_single_L1Mu_efficiency_L1Tk_pt2"," ", 1000, 0, 20)
    h_single_L1Mu_efficiency_L1Tk_pt3 = TH1F("h_single_L1Mu_efficiency_L1Tk_pt3"," ", 1000, 0, 20)
    h_single_L1Mu_efficiency_L1Tk_pt4 = TH1F("h_single_L1Mu_efficiency_L1Tk_pt4"," ", 1000, 0, 20)

    binning2 = [0.05, 0.07, 0.1, 0.2, 0.3, 0.5, 1, 2, 4, 6, 10, 15, 20, 30, 50, 100, 200, 250, 275, 300, 400, 500, 1000]
    nBins = len(binning2) - 1
    genMu_dxy_fid = TH1F("genMu_dxy_fid"," ", nBins, np.asarray(binning2))
    genMu_dxy_lxy_fid = TH2F("genMu_dxy_lxy_fid"," ", 100, 0, 100, 300, 0, 300)
    genMu_dxy_fidT = TH1F("genMu_dxy_fidT"," ", nBins, np.asarray(binning2))
    L1Mu_genMu_dxy_fid = TH1F("L1Mu_genMu_dxy_fid"," ", nBins, np.asarray(binning2))
    L1Mu_genMu_dxy_fidT = TH1F("L1Mu_genMu_dxy_fidT"," ", nBins, np.asarray(binning2))
    L1Mu_genMu_dxy_fid_Q = TH1F("L1Mu_genMu_dxy_fid_Q"," ", nBins, np.asarray(binning2))
    L1Mu_genMu_dxy_fid_BX_Q = TH1F("L1Mu_genMu_dxy_fid_BX_Q"," ", nBins, np.asarray(binning2))
    L1Mu_genMu_dxy_fid_BX_Q_V = TH1F("L1Mu_genMu_dxy_fid_BX_Q_V"," ", nBins, np.asarray(binning2))
    L1Mu_genMu_dxy_fid_BX_Q_V_I = TH1F("L1Mu_genMu_dxy_fid_BX_Q_V_I"," ", nBins, np.asarray(binning2))

    genMu_lxy_fid = TH1F("genMu_lxy_fid"," ", nBins, np.asarray(binning2))
    L1Mu_genMu_lxy_fid = TH1F("L1Mu_genMu_lxy_fid"," ", nBins, np.asarray(binning2))
    L1Mu_genMu_lxy_fid_Q = TH1F("L1Mu_genMu_lxy_fid_Q"," ", nBins, np.asarray(binning2))
    L1Mu_genMu_lxy_fid_BX_Q = TH1F("L1Mu_genMu_lxy_fid_BX_Q"," ", nBins, np.asarray(binning2))
    L1Mu_genMu_lxy_fid_BX_Q_V = TH1F("L1Mu_genMu_lxy_fid_BX_Q_V"," ", nBins, np.asarray(binning2))
    L1Mu_genMu_lxy_fid_BX_Q_V_I = TH1F("L1Mu_genMu_lxy_fid_BX_Q_V_I"," ", nBins, np.asarray(binning2))

    genMu_dxy_fid_barrel = TH1F("genMu_dxy_fid_barrel"," ", nBins, np.asarray(binning2))
    L1Mu_genMu_dxy_fid_barrel = TH1F("L1Mu_genMu_dxy_fid_barrel"," ", nBins, np.asarray(binning2))
    L1Mu_genMu_dxy_fid_Q_barrel = TH1F("L1Mu_genMu_dxy_fid_Q_barrel"," ", nBins, np.asarray(binning2))
    L1Mu_genMu_dxy_fid_BX_Q_barrel = TH1F("L1Mu_genMu_dxy_fid_BX_Q_barrel"," ", nBins, np.asarray(binning2))
    L1Mu_genMu_dxy_fid_BX_Q_V_barrel = TH1F("L1Mu_genMu_dxy_fid_BX_Q_V_barrel"," ", nBins, np.asarray(binning2))
    L1Mu_genMu_dxy_fid_BX_Q_V_I_barrel = TH1F("L1Mu_genMu_dxy_fid_BX_Q_V_I_barrel"," ", nBins, np.asarray(binning2))

    genMu_dxy_fid_overlap = TH1F("genMu_dxy_fid_overlap"," ", nBins, np.asarray(binning2))
    L1Mu_genMu_dxy_fid_overlap = TH1F("L1Mu_genMu_dxy_fid_overlap"," ", nBins, np.asarray(binning2))
    L1Mu_genMu_dxy_fid_Q_overlap = TH1F("L1Mu_genMu_dxy_fid_Q_overlap"," ", nBins, np.asarray(binning2))
    L1Mu_genMu_dxy_fid_BX_Q_overlap = TH1F("L1Mu_genMu_dxy_fid_BX_Q_overlap"," ", nBins, np.asarray(binning2))
    L1Mu_genMu_dxy_fid_BX_Q_V_overlap = TH1F("L1Mu_genMu_dxy_fid_BX_Q_V_overlap"," ", nBins, np.asarray(binning2))
    L1Mu_genMu_dxy_fid_BX_Q_V_I_overlap = TH1F("L1Mu_genMu_dxy_fid_BX_Q_V_I_overlap"," ", nBins, np.asarray(binning2))

    genMu_dxy_fid_endcap = TH1F("genMu_dxy_fid_endcap"," ", nBins, np.asarray(binning2))
    L1Mu_genMu_dxy_fid_endcap = TH1F("L1Mu_genMu_dxy_fid_endcap"," ", nBins, np.asarray(binning2))
    L1Mu_genMu_dxy_fid_Q_endcap = TH1F("L1Mu_genMu_dxy_fid_Q_endcap"," ", nBins, np.asarray(binning2))
    L1Mu_genMu_dxy_fid_BX_Q_endcap = TH1F("L1Mu_genMu_dxy_fid_BX_Q_endcap"," ", nBins, np.asarray(binning2))
    L1Mu_genMu_dxy_fid_BX_Q_V_endcap = TH1F("L1Mu_genMu_dxy_fid_BX_Q_V_endcap"," ", nBins, np.asarray(binning2))
    L1Mu_genMu_dxy_fid_BX_Q_V_I_endcap = TH1F("L1Mu_genMu_dxy_fid_BX_Q_V_I_endcap"," ", nBins, np.asarray(binning2))

    genMu_eta_dxy0to0p1_fid = TH1F("genMu_eta_dxy0to0p1_fid"," ", 25, 0, 2.5)
    genMu_eta_dxy1to5_fid = TH1F("genMu_eta_dxy1to5_fid"," ", 25, 0, 2.5)
    genMu_eta_dxy5to10_fid = TH1F("genMu_eta_dxy5to10_fid"," ", 25, 0, 2.5)
    genMu_eta_dxy10_fid = TH1F("genMu_eta_dxy10_fid"," ", 25, 0, 2.5)

    L1Mu_genMu_eta_dxy0to0p1_fid_L1TkPt0 = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_L1TkPt0"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_L1TkPt0 = TH1F("L1Mu_genMu_eta_dxy1to5_fid_L1TkPt0"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_L1TkPt0 = TH1F("L1Mu_genMu_eta_dxy5to10_fid_L1TkPt0"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_L1TkPt0 = TH1F("L1Mu_genMu_eta_dxy10_fid_L1TkPt0"," ", 25, 0, 2.5)
    

    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt2 = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt2"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt2 = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt2"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt2 = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt2"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt2 = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt2"," ", 25, 0, 2.5)

    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt2 = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt2"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt2 = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt2"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt2 = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt2"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt2 = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt2"," ", 25, 0, 2.5)

    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt2 = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt2"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt2 = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt2"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt2 = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt2"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt2 = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt2"," ", 25, 0, 2.5)

    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt2 = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt2"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt2 = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt2"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt2 = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt2"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt2 = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt2"," ", 25, 0, 2.5)


    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt2p5 = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt2p5"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt2p5 = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt2p5"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt2p5 = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt2p5"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt2p5 = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt2p5"," ", 25, 0, 2.5)

    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt2p5 = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt2p5"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt2p5 = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt2p5"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt2p5 = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt2p5"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt2p5 = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt2p5"," ", 25, 0, 2.5)

    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt2p5 = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt2p5"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt2p5 = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt2p5"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt2p5 = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt2p5"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt2p5 = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt2p5"," ", 25, 0, 2.5)

    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt2p5 = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt2p5"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt2p5 = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt2p5"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt2p5 = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt2p5"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt2p5 = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt2p5"," ", 25, 0, 2.5)


    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt3 = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt3"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt3 = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt3"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt3 = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt3"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt3 = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt3"," ", 25, 0, 2.5)

    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt3 = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt3"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt3 = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt3"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt3 = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt3"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt3 = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt3"," ", 25, 0, 2.5)

    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt3 = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt3"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt3 = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt3"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt3 = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt3"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt3 = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt3"," ", 25, 0, 2.5)

    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt3 = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt3"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt3 = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt3"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt3 = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt3"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt3 = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt3"," ", 25, 0, 2.5)


    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt4 = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt4"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt4 = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt4"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt4 = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt4"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt4 = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt4"," ", 25, 0, 2.5)

    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt4 = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt4"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt4 = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt4"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt4 = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt4"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt4 = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt4"," ", 25, 0, 2.5)

    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt4 = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt4"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt4 = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt4"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt4 = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt4"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt4 = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt4"," ", 25, 0, 2.5)

    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt4 = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt4"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt4 = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt4"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt4 = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt4"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt4 = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt4"," ", 25, 0, 2.5)


    ## plots per eta section
    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt4_total = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt4_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt4_total = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt4_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt4_total = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt4_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt4_total = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt4_total"," ", 25, 0, 2.5)

    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt3_total = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt3_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt3_total = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt3_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt3_total = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt3_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt3_total = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt3_total"," ", 25, 0, 2.5)

    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt2p5_total = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt2p5_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt2p5_total = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt2p5_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt2p5_total = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt2p5_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt2p5_total = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt2p5_total"," ", 25, 0, 2.5)

    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt2_total = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt2_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt2_total = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt2_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt2_total = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt2_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt2_total = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt2_total"," ", 25, 0, 2.5)


    L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt4_total = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt4_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt4_total = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt4_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt4_total = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt4_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt4_total = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt4_total"," ", 25, 0, 2.5)

    L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt3_total = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt3_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt3_total = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt3_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt3_total = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt3_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt3_total = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt3_total"," ", 25, 0, 2.5)

    L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt2p5_total = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt2p5_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt2p5_total = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt2p5_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt2p5_total = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt2p5_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt2p5_total = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt2p5_total"," ", 25, 0, 2.5)

    L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt2_total = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt2_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt2_total = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt2_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt2_total = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt2_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt2_total = TH1F("L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt2_total"," ", 25, 0, 2.5)

 
    L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt4_total = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt4_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt4_total = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt4_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt4_total = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt4_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt4_total = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt4_total"," ", 25, 0, 2.5)

    L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt3_total = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt3_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt3_total = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt3_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt3_total = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt3_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt3_total = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt3_total"," ", 25, 0, 2.5)

    L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt2p5_total = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt2p5_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt2p5_total = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt2p5_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt2p5_total = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt2p5_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt2p5_total = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt2p5_total"," ", 25, 0, 2.5)

    L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt2_total = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt2_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt2_total = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt2_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt2_total = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt2_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt2_total = TH1F("L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt2_total"," ", 25, 0, 2.5)


    L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt4_total = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt4_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt4_total = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt4_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt4_total = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt4_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt4_total = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt4_total"," ", 25, 0, 2.5)

    L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt3_total = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt3_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt3_total = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt3_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt3_total = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt3_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt3_total = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt3_total"," ", 25, 0, 2.5)

    L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt2p5_total = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt2p5_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt2p5_total = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt2p5_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt2p5_total = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt2p5_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt2p5_total = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt2p5_total"," ", 25, 0, 2.5)

    L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt2_total = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt2_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt2_total = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt2_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt2_total = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt2_total"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt2_total = TH1F("L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt2_total"," ", 25, 0, 2.5)


    ## pt plots
    genMu_pt_dxy0to0p1_fid = TH1F("genMu_pt_dxy0to0p1_fid"," ", 25,0,50)
    genMu_pt_dxy1to5_fid = TH1F("genMu_pt_dxy1to5_fid"," ", 25,0,50)
    genMu_pt_dxy5to10_fid = TH1F("genMu_pt_dxy5to10_fid"," ", 25,0,50)
    genMu_pt_dxy10_fid = TH1F("genMu_pt_dxy10_fid"," ", 25,0,50)

    L1Mu_genMu_pt_dxy0to0p1_fid_L1TkPt0 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_L1TkPt0"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_L1TkPt0 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_L1TkPt0"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_L1TkPt0 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_L1TkPt0"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_L1TkPt0 = TH1F("L1Mu_genMu_pt_dxy10_fid_L1TkPt0"," ", 25,0,50)

    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt2 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_dR0p4_L1TkPt2"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt2 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt2"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt2 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt2"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt2 = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt2"," ", 25,0,50)

    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt2 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_dR0p3_L1TkPt2"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt2 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt2"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt2 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt2"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt2 = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt2"," ", 25,0,50)

    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt2 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_dR0p2_L1TkPt2"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt2 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt2"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt2 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt2"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt2 = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt2"," ", 25,0,50)

    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt2 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_dR0p12_L1TkPt2"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt2 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt2"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt2 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt2"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt2 = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt2"," ", 25,0,50)


    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt2p5 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_dR0p4_L1TkPt2p5"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt2p5 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt2p5"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt2p5 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt2p5"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt2p5 = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt2p5"," ", 25,0,50)

    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt2p5 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_dR0p3_L1TkPt2p5"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt2p5 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt2p5"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt2p5 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt2p5"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt2p5 = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt2p5"," ", 25,0,50)

    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt2p5 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_dR0p2_L1TkPt2p5"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt2p5 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt2p5"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt2p5 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt2p5"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt2p5 = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt2p5"," ", 25,0,50)

    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt2p5 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_dR0p12_L1TkPt2p5"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt2p5 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt2p5"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt2p5 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt2p5"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt2p5 = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt2p5"," ", 25,0,50)


    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt3 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_dR0p4_L1TkPt3"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt3 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt3"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt3 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt3"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt3 = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt3"," ", 25,0,50)

    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt3 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_dR0p3_L1TkPt3"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt3 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt3"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt3 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt3"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt3 = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt3"," ", 25,0,50)

    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt3 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_dR0p2_L1TkPt3"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt3 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt3"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt3 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt3"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt3 = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt3"," ", 25,0,50)

    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt3 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_dR0p12_L1TkPt3"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt3 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt3"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt3 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt3"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt3 = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt3"," ", 25,0,50)


    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt4 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_dR0p4_L1TkPt4"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt4 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt4"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt4 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt4"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt4 = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt4"," ", 25,0,50)

    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt4 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_dR0p3_L1TkPt4"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt4 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt4"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt4 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt4"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt4 = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt4"," ", 25,0,50)

    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt4 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_dR0p2_L1TkPt4"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt4 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt4"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt4 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt4"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt4 = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt4"," ", 25,0,50)

    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt4 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_dR0p12_L1TkPt4"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt4 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt4"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt4 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt4"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt4 = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt4"," ", 25,0,50)

    ## plots per eta section
    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt4_total = TH1F("L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt4_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt4_total = TH1F("L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt4_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt4_total = TH1F("L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt4_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt4_total = TH1F("L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt4_total"," ", 25,0,50)

    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt3_total = TH1F("L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt3_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt3_total = TH1F("L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt3_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt3_total = TH1F("L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt3_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt3_total = TH1F("L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt3_total"," ", 25,0,50)

    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt2p5_total = TH1F("L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt2p5_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt2p5_total = TH1F("L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt2p5_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt2p5_total = TH1F("L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt2p5_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt2p5_total = TH1F("L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt2p5_total"," ", 25,0,50)

    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt2_total = TH1F("L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt2_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt2_total = TH1F("L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt2_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt2_total = TH1F("L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt2_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt2_total = TH1F("L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt2_total"," ", 25,0,50)


    L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt4_total = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt4_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt4_total = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt4_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt4_total = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt4_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt4_total = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt4_total"," ", 25,0,50)

    L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt3_total = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt3_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt3_total = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt3_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt3_total = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt3_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt3_total = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt3_total"," ", 25,0,50)

    L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt2p5_total = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt2p5_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt2p5_total = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt2p5_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt2p5_total = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt2p5_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt2p5_total = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt2p5_total"," ", 25,0,50)

    L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt2_total = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt2_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt2_total = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt2_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt2_total = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt2_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt2_total = TH1F("L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt2_total"," ", 25,0,50)

 
    L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt4_total = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt4_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt4_total = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt4_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt4_total = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt4_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt4_total = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt4_total"," ", 25,0,50)

    L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt3_total = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt3_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt3_total = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt3_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt3_total = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt3_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt3_total = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt3_total"," ", 25,0,50)

    L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt2p5_total = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt2p5_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt2p5_total = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt2p5_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt2p5_total = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt2p5_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt2p5_total = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt2p5_total"," ", 25,0,50)

    L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt2_total = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt2_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt2_total = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt2_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt2_total = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt2_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt2_total = TH1F("L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt2_total"," ", 25,0,50)


    L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt4_total = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt4_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt4_total = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt4_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt4_total = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt4_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt4_total = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt4_total"," ", 25,0,50)

    L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt3_total = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt3_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt3_total = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt3_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt3_total = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt3_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt3_total = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt3_total"," ", 25,0,50)

    L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt2p5_total = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt2p5_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt2p5_total = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt2p5_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt2p5_total = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt2p5_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt2p5_total = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt2p5_total"," ", 25,0,50)

    L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt2_total = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt2_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt2_total = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt2_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt2_total = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt2_total"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt2_total = TH1F("L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt2_total"," ", 25,0,50)


    ## temporary check for Slava
    L1Mu_genMu_pt_dxy0to0p1_fid = TH1F("L1Mu_genMu_pt_dxy0top01_fid"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid = TH1F("L1Mu_genMu_pt_dxy1to5_fid"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid = TH1F("L1Mu_genMu_pt_dxy5to10_fid"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid = TH1F("L1Mu_genMu_pt_dxy10_fid"," ", 25,0,50)

    L1Mu_genMu_pt_dxy0to0p1_fid_L1MuPt10 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_L1MuPt10"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_L1MuPt10 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_L1MuPt10"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_L1MuPt10 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_L1MuPt10"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_L1MuPt10 = TH1F("L1Mu_genMu_pt_dxy10_fid_L1MuPt10"," ", 25,0,50)

    L1Mu_genMu_pt_dxy0to0p1_fid_L1MuPt15 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_L1MuPt15"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_L1MuPt15 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_L1MuPt15"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_L1MuPt15 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_L1MuPt15"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_L1MuPt15 = TH1F("L1Mu_genMu_pt_dxy10_fid_L1MuPt15"," ", 25,0,50)

    L1Mu_genMu_pt_dxy0to0p1_fid_L1MuPt20 = TH1F("L1Mu_genMu_pt_dxy0top01_fid_L1MuPt20"," ", 25,0,50)
    L1Mu_genMu_pt_dxy1to5_fid_L1MuPt20 = TH1F("L1Mu_genMu_pt_dxy1to5_fid_L1MuPt20"," ", 25,0,50)
    L1Mu_genMu_pt_dxy5to10_fid_L1MuPt20 = TH1F("L1Mu_genMu_pt_dxy5to10_fid_L1MuPt20"," ", 25,0,50)
    L1Mu_genMu_pt_dxy10_fid_L1MuPt20 = TH1F("L1Mu_genMu_pt_dxy10_fid_L1MuPt20"," ", 25,0,50)


    L1Mu_genMu_eta_dxy0to0p1_fid = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid = TH1F("L1Mu_genMu_eta_dxy1to5_fid"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid = TH1F("L1Mu_genMu_eta_dxy5to10_fid"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid = TH1F("L1Mu_genMu_eta_dxy10_fid"," ", 25, 0, 2.5)

    L1Mu_genMu_eta_dxy0to0p1_fid_L1MuPt10 = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_L1MuPt10"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_L1MuPt10 = TH1F("L1Mu_genMu_eta_dxy1to5_fid_L1MuPt10"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_L1MuPt10 = TH1F("L1Mu_genMu_eta_dxy5to10_fid_L1MuPt10"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_L1MuPt10 = TH1F("L1Mu_genMu_eta_dxy10_fid_L1MuPt10"," ", 25, 0, 2.5)

    L1Mu_genMu_eta_dxy0to0p1_fid_L1MuPt15 = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_L1MuPt15"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_L1MuPt15 = TH1F("L1Mu_genMu_eta_dxy1to5_fid_L1MuPt15"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_L1MuPt15 = TH1F("L1Mu_genMu_eta_dxy5to10_fid_L1MuPt15"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_L1MuPt15 = TH1F("L1Mu_genMu_eta_dxy10_fid_L1MuPt15"," ", 25, 0, 2.5)

    L1Mu_genMu_eta_dxy0to0p1_fid_L1MuPt20 = TH1F("L1Mu_genMu_eta_dxy0to0p1_fid_L1MuPt20"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy1to5_fid_L1MuPt20 = TH1F("L1Mu_genMu_eta_dxy1to5_fid_L1MuPt20"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy5to10_fid_L1MuPt20 = TH1F("L1Mu_genMu_eta_dxy5to10_fid_L1MuPt20"," ", 25, 0, 2.5)
    L1Mu_genMu_eta_dxy10_fid_L1MuPt20 = TH1F("L1Mu_genMu_eta_dxy10_fid_L1MuPt20"," ", 25, 0, 2.5)

    verbose = False

    nTotalMuon = 0
    nGoodMuon = 0
  
    nGoodGenMu = 0
    nGoodGenMuMissingL1Mu = 0
    nGoodGenMuMatchedL1MuMatchedToL1Tk = 0
    nGoodGenMuMatchedL1MuMatchedToL1TkPt3 = 0
    nGoodGenMuMatchedL1MuMatchedToL1TkPt4 = 0
    nGoodGenMuMatchedL1MuMatchedToL1TkPt5 = 0
    nGoodGenMuMatchedL1MuMatchedToL1TkPt6 = 0
    nGoodGenMuMatchedL1MuMatchedToL1TkPt10 = 0
    nGoodGenMuMatchedL1MuNotMatchedToL1Tk = 0
    nGoodGenMuMatchedL1MuNotMatchedToL1TkL1MuQLessThan4 = 0
    nGoodGenMuMatchedL1MuNotMatchedToL1TkL1MuBXNot0 = 0
    nGoodGenMuMatchedL1MuTriggered = 0

    treeHits = ch

    for k in range(0,treeHits.GetEntries()):
      treeHits.GetEntry(k)
      print "Event", k, "nL1Mu", treeHits.nL1Mu
      #if verbose:
      for i in range(0,2):
        for j in range(0,2):
          ij = i*2+j
          
          ## exclude all the bad muons
          if (abs(treeHits.genGdMu_eta_prop[i*2+0])>2.4): 
            continue
          if (abs(treeHits.genGdMu_eta_prop[i*2+1])>2.4): 
            continue
          if (abs(treeHits.genGdMu_pt[i*2+0])<5): 
            continue
          if (abs(treeHits.genGdMu_pt[i*2+1])<5): 
            continue
          if (abs(treeHits.genGd0Gd1_dR) < 2):
            continue
          if (abs(treeHits.genGd_genMuMu_dR[i]) < 1):
            continue
          if treeHits.genGdMu_eta_prop[ij] == -99 or treeHits.genGdMu_phi_prop[ij] == -99:
            continue

          pt = abs(treeHits.genGdMu_pt[ij])
          eta = treeHits.genGdMu_eta[ij]
          phi = abs(treeHits.genGdMu_phi[ij])
          phi_corr = abs(treeHits.genGdMu_phi_corr[ij])
          eta_prop = treeHits.genGdMu_eta_prop[ij]
          phi_prop = treeHits.genGdMu_phi_prop[ij]
          dxy = treeHits.genGdMu_dxy[ij]
          vz = abs(treeHits.genGd_vz[i])
          lxy =  abs(treeHits.genGd_lxy[i])

          genMu_dxy_lxy_fid.Fill(dxy,lxy)

          if verbose or True:
            print "\tGenMu", i, j,
            print "pt", pt,
            print "eta", eta,
            print "phi", phi,
            print "eta_prop", eta_prop,
            print "phi_prop", phi_prop,
            print "phi_corr", phi_corr,
#            print "index_corr", treeHits.genGdMu_L1Mu_index_corr[ij],
            print "dR_corr", treeHits.genGdMu_L1Mu_dR_corr[ij],
#            print "index_prop", treeHits.genGdMu_L1Mu_index_prop[ij],
            print "dR_prop", treeHits.genGdMu_L1Mu_dR_prop[ij],
            print "abs(dxy)", abs(treeHits.genGdMu_dxy[ij])
          L1Mu_index = treeHits.genGdMu_L1Mu_index_prop[ij]
          L1Mu_dR_prop = treeHits.genGdMu_L1Mu_dR_prop[ij]

          trigL1Mu = False
          trig_dR0p4_L1TkPt4 = False 
          trig_dR0p4_L1TkPt3 = False 
          trig_dR0p4_L1TkPt2p5 = False
          trig_dR0p4_L1TkPt2 = False
          
          trig_dR0p3_L1TkPt4 = False 
          trig_dR0p3_L1TkPt3 = False
          trig_dR0p3_L1TkPt2p5 = False
          trig_dR0p3_L1TkPt2 = False
          
          trig_dR0p2_L1TkPt4 = False
          trig_dR0p2_L1TkPt3 = False
          trig_dR0p2_L1TkPt2p5 = False
          trig_dR0p2_L1TkPt2 = False

          trig_dR0p12_L1TkPt4 = False
          trig_dR0p12_L1TkPt3 = False
          trig_dR0p12_L1TkPt2p5 = False
          trig_dR0p12_L1TkPt2 = False

          if L1Mu_index == 99 and verbose:
            for ii in range(0,treeHits.nL1Mu):     
              if treeHits.L1Mu_bx[ii] != 0: continue
              print "\t\tNot Matched: L1Mu", ii,
              print "L1Mu_pt", treeHits.L1Mu_pt[ii],
              print "L1Mu_eta", treeHits.L1Mu_eta[ii],
              print "L1Mu_phi", treeHits.L1Mu_phi[ii],
              print "L1Mu_bx", treeHits.L1Mu_bx[ii],
              print "L1Mu_quality", treeHits.L1Mu_quality[ii],
              print "L1Mu_dR_prop", deltaR(eta_prop, phi_prop, treeHits.L1Mu_eta[ii], treeHits.L1Mu_phi[ii]),
              print "L1Mu_dR_corr", deltaR(eta, phi_corr, treeHits.L1Mu_eta[ii], treeHits.L1Mu_phi[ii]),
              print "index_prop", treeHits.genGdMu_L1Mu_index_prop[ij],
              print "dR_prop", treeHits.genGdMu_L1Mu_dR_prop[ij]

          if L1Mu_index != 99:
            nTotalMuon +=1 
            L1Mu_pt = treeHits.L1Mu_pt[L1Mu_index]
            L1Mu_eta = treeHits.L1Mu_eta[L1Mu_index]
            L1Mu_phi = treeHits.L1Mu_phi[L1Mu_index]
            L1Mu_bx = treeHits.L1Mu_bx[L1Mu_index]
            L1Mu_quality = treeHits.L1Mu_quality[L1Mu_index]
            L1Mu_L1Tk_dR_prop = treeHits.L1Mu_L1Tk_dR_prop[L1Mu_index]
            L1Mu_L1Tk_pt = treeHits.L1Mu_L1Tk_pt_prop[L1Mu_index]
            if verbose or True:
              print "\t\tMatched: L1Mu", "pt", L1Mu_pt, "eta", L1Mu_eta, "phi", L1Mu_phi, "Quality", L1Mu_quality,
              print "L1Mu_L1Tk_dR_min", L1Mu_L1Tk_dR_prop, "L1Mu_L1Tk_pt", L1Mu_L1Tk_pt
                
            matched = L1Mu_L1Tk_dR_prop <= 0.12 and L1Mu_quality >= 4
            matched = matched and L1Mu_L1Tk_pt>=MatchingL1TkMinPtEff ## optional pT cut to increase the efficiency of matched L1Mu

            common = (abs(L1Mu_bx) <= 0) and (L1Mu_quality >= 4)
            
            if (common): trigL1Mu = True
            if ((not matched) and not (L1Mu_L1Tk_dR_prop <= 0.4 and L1Mu_L1Tk_pt>=4) and common): trig_dR0p4_L1TkPt4 = True
            if ((not matched) and not (L1Mu_L1Tk_dR_prop <= 0.4 and L1Mu_L1Tk_pt>=3) and common): trig_dR0p4_L1TkPt3 = True
            if ((not matched) and not (L1Mu_L1Tk_dR_prop <= 0.4 and L1Mu_L1Tk_pt>=2.5) and common): trig_dR0p4_L1TkPt2p5 = True
            if ((not matched) and not (L1Mu_L1Tk_dR_prop <= 0.4 and L1Mu_L1Tk_pt>=2) and common): trig_dR0p4_L1TkPt2 = True

            if ((not matched) and not (L1Mu_L1Tk_dR_prop <= 0.3 and L1Mu_L1Tk_pt>=4) and common): trig_dR0p3_L1TkPt4 = True
            if ((not matched) and not (L1Mu_L1Tk_dR_prop <= 0.3 and L1Mu_L1Tk_pt>=3) and common): trig_dR0p3_L1TkPt3 = True
            if ((not matched) and not (L1Mu_L1Tk_dR_prop <= 0.3 and L1Mu_L1Tk_pt>=2.5) and common): trig_dR0p3_L1TkPt2p5 = True
            if ((not matched) and not (L1Mu_L1Tk_dR_prop <= 0.3 and L1Mu_L1Tk_pt>=2) and common): trig_dR0p3_L1TkPt2 = True
            
            if ((not matched) and not (L1Mu_L1Tk_dR_prop <= 0.2 and L1Mu_L1Tk_pt>=4) and common): trig_dR0p2_L1TkPt4 = True
            if ((not matched) and not (L1Mu_L1Tk_dR_prop <= 0.2 and L1Mu_L1Tk_pt>=3) and common): trig_dR0p2_L1TkPt3 = True
            if ((not matched) and not (L1Mu_L1Tk_dR_prop <= 0.2 and L1Mu_L1Tk_pt>=2.5) and common): trig_dR0p2_L1TkPt2p5 = True
            if ((not matched) and not (L1Mu_L1Tk_dR_prop <= 0.2 and L1Mu_L1Tk_pt>=2) and common): trig_dR0p2_L1TkPt2 = True

            if ((not matched) and not (L1Mu_L1Tk_dR_prop <= 0.12 and L1Mu_L1Tk_pt>=4) and common): trig_dR0p12_L1TkPt4 = True
            if ((not matched) and not (L1Mu_L1Tk_dR_prop <= 0.12 and L1Mu_L1Tk_pt>=3) and common): trig_dR0p12_L1TkPt3 = True
            if ((not matched) and not (L1Mu_L1Tk_dR_prop <= 0.12 and L1Mu_L1Tk_pt>=2.5) and common): trig_dR0p12_L1TkPt2p5 = True
            if ((not matched) and not (L1Mu_L1Tk_dR_prop <= 0.12 and L1Mu_L1Tk_pt>=2) and common): trig_dR0p12_L1TkPt2 = True


            L1Mu_barrel = abs(L1Mu_eta)<=0.9
            L1Mu_overlap = abs(L1Mu_eta)>0.9 and abs(L1Mu_eta)<=1.2
            L1Mu_endcap = abs(L1Mu_eta)>1.2 and abs(L1Mu_eta)<=2.4

            matched_barrel = L1Mu_L1Tk_dR_prop <= 0.12 and L1Mu_quality >= 4
            matched_barrel = matched_barrel and L1Mu_L1Tk_pt>=0 ## optional pT cut to increase the efficiency of matched L1Mu

            matched_overlap = L1Mu_L1Tk_dR_prop <= 0.10 and L1Mu_quality >= 4
            matched_overlap = matched_overlap and L1Mu_L1Tk_pt>=0 ## optional pT cut to increase the efficiency of matched L1Mu

            matched_endcap = L1Mu_L1Tk_dR_prop <= 0.09 and L1Mu_quality >= 4
            matched_endcap = matched_endcap and L1Mu_L1Tk_pt>=0 ## optional pT cut to increase the efficiency of matched L1Mu

            trig_dR0p4_L1TkPt4_barrel = L1Mu_barrel and (not matched_barrel) and not (L1Mu_L1Tk_dR_prop <= 0.4 and L1Mu_L1Tk_pt>=4) and common
            trig_dR0p4_L1TkPt3_barrel = L1Mu_barrel and (not matched_barrel) and not (L1Mu_L1Tk_dR_prop <= 0.4 and L1Mu_L1Tk_pt>=3) and common
            trig_dR0p4_L1TkPt2p5_barrel = L1Mu_barrel and (not matched_barrel) and not (L1Mu_L1Tk_dR_prop <= 0.4 and L1Mu_L1Tk_pt>=2.5) and common
            trig_dR0p4_L1TkPt2_barrel = L1Mu_barrel and (not matched_barrel) and not (L1Mu_L1Tk_dR_prop <= 0.4 and L1Mu_L1Tk_pt>=2) and common

            trig_dR0p3_L1TkPt4_barrel = L1Mu_barrel and (not matched_barrel) and not (L1Mu_L1Tk_dR_prop <= 0.3 and L1Mu_L1Tk_pt>=4) and common
            trig_dR0p3_L1TkPt3_barrel = L1Mu_barrel and (not matched_barrel) and not (L1Mu_L1Tk_dR_prop <= 0.3 and L1Mu_L1Tk_pt>=3) and common
            trig_dR0p3_L1TkPt2p5_barrel = L1Mu_barrel and (not matched_barrel) and not (L1Mu_L1Tk_dR_prop <= 0.3 and L1Mu_L1Tk_pt>=2.5) and common
            trig_dR0p3_L1TkPt2_barrel = L1Mu_barrel and (not matched_barrel) and not (L1Mu_L1Tk_dR_prop <= 0.3 and L1Mu_L1Tk_pt>=2) and common

            trig_dR0p2_L1TkPt4_barrel = L1Mu_barrel and (not matched_barrel) and not (L1Mu_L1Tk_dR_prop <= 0.2 and L1Mu_L1Tk_pt>=4) and common
            trig_dR0p2_L1TkPt3_barrel = L1Mu_barrel and (not matched_barrel) and not (L1Mu_L1Tk_dR_prop <= 0.2 and L1Mu_L1Tk_pt>=3) and common
            trig_dR0p2_L1TkPt2p5_barrel = L1Mu_barrel and (not matched_barrel) and not (L1Mu_L1Tk_dR_prop <= 0.2 and L1Mu_L1Tk_pt>=2.5) and common
            trig_dR0p2_L1TkPt2_barrel = L1Mu_barrel and (not matched_barrel) and not (L1Mu_L1Tk_dR_prop <= 0.2 and L1Mu_L1Tk_pt>=2) and common

            trig_dR0p12_L1TkPt4_barrel = L1Mu_barrel and (not matched_barrel) and not (L1Mu_L1Tk_dR_prop <= 0.12 and L1Mu_L1Tk_pt>=4) and common
            trig_dR0p12_L1TkPt3_barrel = L1Mu_barrel and (not matched_barrel) and not (L1Mu_L1Tk_dR_prop <= 0.12 and L1Mu_L1Tk_pt>=3) and common
            trig_dR0p12_L1TkPt2p5_barrel = L1Mu_barrel and (not matched_barrel) and not (L1Mu_L1Tk_dR_prop <= 0.12 and L1Mu_L1Tk_pt>=2.5) and common
            trig_dR0p12_L1TkPt2_barrel = L1Mu_barrel and (not matched_barrel) and not (L1Mu_L1Tk_dR_prop <= 0.12 and L1Mu_L1Tk_pt>=2) and common


            trig_dR0p4_L1TkPt4_overlap = L1Mu_overlap and (not matched_overlap) and not (L1Mu_L1Tk_dR_prop <= 0.4 and L1Mu_L1Tk_pt>=4) and common
            trig_dR0p4_L1TkPt3_overlap = L1Mu_overlap and (not matched_overlap) and not (L1Mu_L1Tk_dR_prop <= 0.4 and L1Mu_L1Tk_pt>=3) and common
            trig_dR0p4_L1TkPt2p5_overlap = L1Mu_overlap and (not matched_overlap) and not (L1Mu_L1Tk_dR_prop <= 0.4 and L1Mu_L1Tk_pt>=2.5) and common
            trig_dR0p4_L1TkPt2_overlap = L1Mu_overlap and (not matched_overlap) and not (L1Mu_L1Tk_dR_prop <= 0.4 and L1Mu_L1Tk_pt>=2) and common

            trig_dR0p3_L1TkPt4_overlap = L1Mu_overlap and (not matched_overlap) and not (L1Mu_L1Tk_dR_prop <= 0.3 and L1Mu_L1Tk_pt>=4) and common
            trig_dR0p3_L1TkPt3_overlap = L1Mu_overlap and (not matched_overlap) and not (L1Mu_L1Tk_dR_prop <= 0.3 and L1Mu_L1Tk_pt>=3) and common
            trig_dR0p3_L1TkPt2p5_overlap = L1Mu_overlap and (not matched_overlap) and not (L1Mu_L1Tk_dR_prop <= 0.3 and L1Mu_L1Tk_pt>=2.5) and common
            trig_dR0p3_L1TkPt2_overlap = L1Mu_overlap and (not matched_overlap) and not (L1Mu_L1Tk_dR_prop <= 0.3 and L1Mu_L1Tk_pt>=2) and common

            trig_dR0p2_L1TkPt4_overlap = L1Mu_overlap and (not matched_overlap) and not (L1Mu_L1Tk_dR_prop <= 0.2 and L1Mu_L1Tk_pt>=4) and common
            trig_dR0p2_L1TkPt3_overlap = L1Mu_overlap and (not matched_overlap) and not (L1Mu_L1Tk_dR_prop <= 0.2 and L1Mu_L1Tk_pt>=3) and common
            trig_dR0p2_L1TkPt2p5_overlap = L1Mu_overlap and (not matched_overlap) and not (L1Mu_L1Tk_dR_prop <= 0.2 and L1Mu_L1Tk_pt>=2.5) and common
            trig_dR0p2_L1TkPt2_overlap = L1Mu_overlap and (not matched_overlap) and not (L1Mu_L1Tk_dR_prop <= 0.2 and L1Mu_L1Tk_pt>=2) and common

            trig_dR0p12_L1TkPt4_overlap = L1Mu_overlap and (not matched_overlap) and not (L1Mu_L1Tk_dR_prop <= 0.12 and L1Mu_L1Tk_pt>=4) and common
            trig_dR0p12_L1TkPt3_overlap = L1Mu_overlap and (not matched_overlap) and not (L1Mu_L1Tk_dR_prop <= 0.12 and L1Mu_L1Tk_pt>=3) and common
            trig_dR0p12_L1TkPt2p5_overlap = L1Mu_overlap and (not matched_overlap) and not (L1Mu_L1Tk_dR_prop <= 0.12 and L1Mu_L1Tk_pt>=2.5) and common
            trig_dR0p12_L1TkPt2_overlap = L1Mu_overlap and (not matched_overlap) and not (L1Mu_L1Tk_dR_prop <= 0.12 and L1Mu_L1Tk_pt>=2) and common
            

            trig_dR0p4_L1TkPt4_endcap = L1Mu_endcap and (not matched_endcap) and not (L1Mu_L1Tk_dR_prop <= 0.4 and L1Mu_L1Tk_pt>=4) and common
            trig_dR0p4_L1TkPt3_endcap = L1Mu_endcap and (not matched_endcap) and not (L1Mu_L1Tk_dR_prop <= 0.4 and L1Mu_L1Tk_pt>=3) and common
            trig_dR0p4_L1TkPt2p5_endcap = L1Mu_endcap and (not matched_endcap) and not (L1Mu_L1Tk_dR_prop <= 0.4 and L1Mu_L1Tk_pt>=2.5) and common
            trig_dR0p4_L1TkPt2_endcap = L1Mu_endcap and (not matched_endcap) and not (L1Mu_L1Tk_dR_prop <= 0.4 and L1Mu_L1Tk_pt>=2) and common

            trig_dR0p3_L1TkPt4_endcap = L1Mu_endcap and (not matched_endcap) and not (L1Mu_L1Tk_dR_prop <= 0.3 and L1Mu_L1Tk_pt>=4) and common
            trig_dR0p3_L1TkPt3_endcap = L1Mu_endcap and (not matched_endcap) and not (L1Mu_L1Tk_dR_prop <= 0.3 and L1Mu_L1Tk_pt>=3) and common
            trig_dR0p3_L1TkPt2p5_endcap = L1Mu_endcap and (not matched_endcap) and not (L1Mu_L1Tk_dR_prop <= 0.3 and L1Mu_L1Tk_pt>=2.5) and common
            trig_dR0p3_L1TkPt2_endcap = L1Mu_endcap and (not matched_endcap) and not (L1Mu_L1Tk_dR_prop <= 0.3 and L1Mu_L1Tk_pt>=2) and common

            trig_dR0p2_L1TkPt4_endcap = L1Mu_endcap and (not matched_endcap) and not (L1Mu_L1Tk_dR_prop <= 0.2 and L1Mu_L1Tk_pt>=4) and common
            trig_dR0p2_L1TkPt3_endcap = L1Mu_endcap and (not matched_endcap) and not (L1Mu_L1Tk_dR_prop <= 0.2 and L1Mu_L1Tk_pt>=3) and common
            trig_dR0p2_L1TkPt2p5_endcap = L1Mu_endcap and (not matched_endcap) and not (L1Mu_L1Tk_dR_prop <= 0.2 and L1Mu_L1Tk_pt>=2.5) and common
            trig_dR0p2_L1TkPt2_endcap = L1Mu_endcap and (not matched_endcap) and not (L1Mu_L1Tk_dR_prop <= 0.2 and L1Mu_L1Tk_pt>=2) and common

            trig_dR0p12_L1TkPt4_endcap = L1Mu_endcap and (not matched_endcap) and not (L1Mu_L1Tk_dR_prop <= 0.12 and L1Mu_L1Tk_pt>=4) and common
            trig_dR0p12_L1TkPt3_endcap = L1Mu_endcap and (not matched_endcap) and not (L1Mu_L1Tk_dR_prop <= 0.12 and L1Mu_L1Tk_pt>=3) and common
            trig_dR0p12_L1TkPt2p5_endcap = L1Mu_endcap and (not matched_endcap) and not (L1Mu_L1Tk_dR_prop <= 0.12 and L1Mu_L1Tk_pt>=2.5) and common
            trig_dR0p12_L1TkPt2_endcap = L1Mu_endcap and (not matched_endcap) and not (L1Mu_L1Tk_dR_prop <= 0.12 and L1Mu_L1Tk_pt>=2) and common

            
            trig_dR0p4_L1TkPt4_total = trig_dR0p4_L1TkPt4_barrel or trig_dR0p4_L1TkPt4_overlap or trig_dR0p4_L1TkPt4_endcap
            trig_dR0p3_L1TkPt4_total = trig_dR0p3_L1TkPt4_barrel or trig_dR0p3_L1TkPt4_overlap or trig_dR0p3_L1TkPt4_endcap
            trig_dR0p2_L1TkPt4_total = trig_dR0p2_L1TkPt4_barrel or trig_dR0p2_L1TkPt4_overlap or trig_dR0p2_L1TkPt4_endcap
            trig_dR0p12_L1TkPt4_total = trig_dR0p12_L1TkPt4_barrel or trig_dR0p12_L1TkPt4_overlap or trig_dR0p12_L1TkPt4_endcap

            trig_dR0p4_L1TkPt3_total = trig_dR0p4_L1TkPt3_barrel or trig_dR0p4_L1TkPt3_overlap or trig_dR0p4_L1TkPt3_endcap
            trig_dR0p3_L1TkPt3_total = trig_dR0p3_L1TkPt3_barrel or trig_dR0p3_L1TkPt3_overlap or trig_dR0p3_L1TkPt3_endcap
            trig_dR0p2_L1TkPt3_total = trig_dR0p2_L1TkPt3_barrel or trig_dR0p2_L1TkPt3_overlap or trig_dR0p2_L1TkPt3_endcap
            trig_dR0p12_L1TkPt3_total = trig_dR0p12_L1TkPt3_barrel or trig_dR0p12_L1TkPt3_overlap or trig_dR0p12_L1TkPt3_endcap
            
            trig_dR0p4_L1TkPt2p5_total = trig_dR0p4_L1TkPt2p5_barrel or trig_dR0p4_L1TkPt2p5_overlap or trig_dR0p4_L1TkPt2p5_endcap
            trig_dR0p3_L1TkPt2p5_total = trig_dR0p3_L1TkPt2p5_barrel or trig_dR0p3_L1TkPt2p5_overlap or trig_dR0p3_L1TkPt2p5_endcap
            trig_dR0p2_L1TkPt2p5_total = trig_dR0p2_L1TkPt2p5_barrel or trig_dR0p2_L1TkPt2p5_overlap or trig_dR0p2_L1TkPt2p5_endcap
            trig_dR0p12_L1TkPt2p5_total = trig_dR0p12_L1TkPt2p5_barrel or trig_dR0p12_L1TkPt2p5_overlap or trig_dR0p12_L1TkPt2p5_endcap

            trig_dR0p4_L1TkPt2_total = trig_dR0p4_L1TkPt2_barrel or trig_dR0p4_L1TkPt2_overlap or trig_dR0p4_L1TkPt2_endcap
            trig_dR0p3_L1TkPt2_total = trig_dR0p3_L1TkPt2_barrel or trig_dR0p3_L1TkPt2_overlap or trig_dR0p3_L1TkPt2_endcap
            trig_dR0p2_L1TkPt2_total = trig_dR0p2_L1TkPt2_barrel or trig_dR0p2_L1TkPt2_overlap or trig_dR0p2_L1TkPt2_endcap
            trig_dR0p12_L1TkPt2_total = trig_dR0p12_L1TkPt2_barrel or trig_dR0p12_L1TkPt2_overlap or trig_dR0p12_L1TkPt2_endcap


          dxy_range1 = (abs(dxy) <= 0.1)
          dxy_range2 = (abs(dxy) > 1 and abs(dxy) <= 5)
          dxy_range3 = (abs(dxy) > 5 and abs(dxy) <= 10)
          dxy_range4 = (abs(dxy) > 10 and abs(dxy) <= 50)

          eta_fid = abs(eta_prop)<=2.4 and vz < 500 and lxy < 300
          eta_fid_barrel = abs(eta_prop)<=0.9 and vz < 500 and lxy < 300
          eta_fid_overlap = 0.9< abs(eta_prop) and abs(eta_prop)<=1.2 and vz < 500 and lxy < 300
          eta_fid_endcap = abs(eta_prop)>1.2 and vz < 500 and lxy < 300
          eta_fid_tight = abs(eta_prop)<2.4 and vz < 300 and lxy < 300
          pt_fid = pt>=5 and vz < 500 and lxy < 300
          
          if eta_fid:
            genMu_dxy_fid.Fill(abs(dxy))
            if L1Mu_index != 99 and L1Mu_dR_prop < 0.2: 
              L1Mu_genMu_dxy_fid.Fill(abs(dxy))
              if (L1Mu_quality >= 4):
                L1Mu_genMu_dxy_fid_Q.Fill(abs(dxy))
                if (abs(L1Mu_bx) <= 0):
                  L1Mu_genMu_dxy_fid_BX_Q.Fill(abs(dxy))
                  if not matched:
                    L1Mu_genMu_dxy_fid_BX_Q_V.Fill(abs(dxy))
                    if trig_dR0p4_L1TkPt4:
                      L1Mu_genMu_dxy_fid_BX_Q_V_I.Fill(abs(dxy))
                      if abs(dxy)<1:
                        print "ALARM"

          if eta_fid:
            genMu_lxy_fid.Fill(abs(lxy))
            if L1Mu_index != 99 and L1Mu_dR_prop < 0.2: 
              L1Mu_genMu_lxy_fid.Fill(abs(lxy))
              if (L1Mu_quality >= 4):
                L1Mu_genMu_lxy_fid_Q.Fill(abs(lxy))
                if (abs(L1Mu_bx) <= 0):
                  L1Mu_genMu_lxy_fid_BX_Q.Fill(abs(lxy))
                  if not matched:
                    L1Mu_genMu_lxy_fid_BX_Q_V.Fill(abs(lxy))
                    if trig_dR0p4_L1TkPt4:
                      L1Mu_genMu_lxy_fid_BX_Q_V_I.Fill(abs(lxy))
                      if abs(lxy)<1:
                        print "ALARM"

          if eta_fid_barrel:
            genMu_dxy_fid_barrel.Fill(abs(dxy))
            if L1Mu_index != 99 and L1Mu_dR_prop < 0.2: 
              L1Mu_genMu_dxy_fid_barrel.Fill(abs(dxy))
              if (L1Mu_quality >= 4):
                L1Mu_genMu_dxy_fid_Q_barrel.Fill(abs(dxy))
                if (abs(L1Mu_bx) <= 0):
                  L1Mu_genMu_dxy_fid_BX_Q_barrel.Fill(abs(dxy))
                  if not matched:
                    L1Mu_genMu_dxy_fid_BX_Q_V_barrel.Fill(abs(dxy))
                    if trig_dR0p4_L1TkPt4:
                      L1Mu_genMu_dxy_fid_BX_Q_V_I_barrel.Fill(abs(dxy))
                      if abs(dxy)<1:
                        print "ALARM"

          if eta_fid_overlap:
            genMu_dxy_fid_overlap.Fill(abs(dxy))
            if L1Mu_index != 99 and L1Mu_dR_prop < 0.2: 
              L1Mu_genMu_dxy_fid_overlap.Fill(abs(dxy))
              if (L1Mu_quality >= 4):
                L1Mu_genMu_dxy_fid_Q_overlap.Fill(abs(dxy))
                if (abs(L1Mu_bx) <= 0):
                  L1Mu_genMu_dxy_fid_BX_Q_overlap.Fill(abs(dxy))
                  if not matched:
                    L1Mu_genMu_dxy_fid_BX_Q_V_overlap.Fill(abs(dxy))
                    if trig_dR0p4_L1TkPt4:
                      L1Mu_genMu_dxy_fid_BX_Q_V_I_overlap.Fill(abs(dxy))
                      if abs(dxy)<1:
                        print "ALARM"

          if eta_fid_endcap:
            genMu_dxy_fid_endcap.Fill(abs(dxy))
            if L1Mu_index != 99 and L1Mu_dR_prop < 0.2: 
              L1Mu_genMu_dxy_fid_endcap.Fill(abs(dxy))
              if (L1Mu_quality >= 4):
                L1Mu_genMu_dxy_fid_Q_endcap.Fill(abs(dxy))
                if (abs(L1Mu_bx) <= 0):
                  L1Mu_genMu_dxy_fid_BX_Q_endcap.Fill(abs(dxy))
                  if not matched:
                    L1Mu_genMu_dxy_fid_BX_Q_V_endcap.Fill(abs(dxy))
                    if trig_dR0p4_L1TkPt4:
                      L1Mu_genMu_dxy_fid_BX_Q_V_I_endcap.Fill(abs(dxy))
                      if abs(dxy)<1:
                        print "ALARM"

          if eta_fid_tight:
            genMu_dxy_fidT.Fill(abs(dxy))
            if treeHits.genGdMu_L1Mu_index_corr[ij] != 99 and L1Mu_dR_prop < 0.2: 
              L1Mu_genMu_dxy_fidT.Fill(abs(dxy))

          eta = abs(eta_prop)
          ## pt efficiencies
          if dxy_range1 and eta_fid:
            genMu_pt_dxy0to0p1_fid.Fill(pt)
            if trigL1Mu:      L1Mu_genMu_pt_dxy0to0p1_fid.Fill(pt)

            ### plots with different veto cones per eta section
            if trig_dR0p4_L1TkPt4_total:   L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt4_total.Fill(pt)
            if trig_dR0p4_L1TkPt3_total:   L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt3_total.Fill(pt)
            if trig_dR0p4_L1TkPt2p5_total: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p4_L1TkPt2_total:   L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt2_total.Fill(pt)

            if trig_dR0p3_L1TkPt4_total: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt4_total.Fill(pt)
            if trig_dR0p3_L1TkPt3_total: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt3_total.Fill(pt)
            if trig_dR0p3_L1TkPt2p5_total: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p3_L1TkPt2_total: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt2_total.Fill(pt)

            if trig_dR0p2_L1TkPt4_total: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt4_total.Fill(pt)
            if trig_dR0p2_L1TkPt3_total: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt3_total.Fill(pt)
            if trig_dR0p2_L1TkPt2p5_total: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p2_L1TkPt2_total: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt2_total.Fill(pt)

            if trig_dR0p12_L1TkPt4_total: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt4_total.Fill(pt)
            if trig_dR0p12_L1TkPt3_total: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt3_total.Fill(pt)
            if trig_dR0p12_L1TkPt2p5_total: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p12_L1TkPt2_total: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt2_total.Fill(pt)


            if trig_dR0p4_L1TkPt4: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt4.Fill(pt)
            if trig_dR0p4_L1TkPt3: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt3.Fill(pt)
            if trig_dR0p4_L1TkPt2p5: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt2p5.Fill(pt)
            if trig_dR0p4_L1TkPt2: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt2.Fill(pt)

            if trig_dR0p3_L1TkPt4: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt4.Fill(pt)
            if trig_dR0p3_L1TkPt3: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt3.Fill(pt)
            if trig_dR0p3_L1TkPt2p5: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt2p5.Fill(pt)
            if trig_dR0p3_L1TkPt2: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt2.Fill(pt)

            if trig_dR0p2_L1TkPt4: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt4.Fill(pt)
            if trig_dR0p2_L1TkPt3: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt3.Fill(pt)
            if trig_dR0p2_L1TkPt2p5: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt2p5.Fill(pt)
            if trig_dR0p2_L1TkPt2: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt2.Fill(pt)

            if trig_dR0p12_L1TkPt4: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt4.Fill(pt)
            if trig_dR0p12_L1TkPt3: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt3.Fill(pt)
            if trig_dR0p12_L1TkPt2p5: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt2p5.Fill(pt)
            if trig_dR0p12_L1TkPt2: L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt2.Fill(pt)

          if dxy_range2 and eta_fid:
            genMu_pt_dxy1to5_fid.Fill(pt)
            nGoodGenMu += 1
            if trigL1Mu:             L1Mu_genMu_pt_dxy1to5_fid.Fill(pt)

            ### plots with different veto cones per eta section
            if trig_dR0p4_L1TkPt4_total:   L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt4_total.Fill(pt)
            if trig_dR0p4_L1TkPt3_total:   L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt3_total.Fill(pt)
            if trig_dR0p4_L1TkPt2p5_total: L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p4_L1TkPt2_total:   L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt2_total.Fill(pt)

            if trig_dR0p3_L1TkPt4_total: L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt4_total.Fill(pt)
            if trig_dR0p3_L1TkPt3_total: L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt3_total.Fill(pt)
            if trig_dR0p3_L1TkPt2p5_total: L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p3_L1TkPt2_total: L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt2_total.Fill(pt)

            if trig_dR0p2_L1TkPt4_total: L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt4_total.Fill(pt)
            if trig_dR0p2_L1TkPt3_total: L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt3_total.Fill(pt)
            if trig_dR0p2_L1TkPt2p5_total: L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p2_L1TkPt2_total: L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt2_total.Fill(pt)

            if trig_dR0p12_L1TkPt4_total: L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt4_total.Fill(pt)
            if trig_dR0p12_L1TkPt3_total: L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt3_total.Fill(pt)
            if trig_dR0p12_L1TkPt2p5_total: L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p12_L1TkPt2_total: L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt2_total.Fill(pt)


            if trig_dR0p4_L1TkPt4:   L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt4.Fill(pt)
            if trig_dR0p4_L1TkPt3:   L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt3.Fill(pt)
            if trig_dR0p4_L1TkPt2p5: L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt2p5.Fill(pt)
            if trig_dR0p4_L1TkPt2:   L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt2.Fill(pt)

            if trig_dR0p3_L1TkPt4: L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt4.Fill(pt)
            if trig_dR0p3_L1TkPt3: L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt3.Fill(pt)
            if trig_dR0p3_L1TkPt2p5: L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt2p5.Fill(pt)
            if trig_dR0p3_L1TkPt2: L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt2.Fill(pt)

            if trig_dR0p2_L1TkPt4: L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt4.Fill(pt)
            if trig_dR0p2_L1TkPt3: L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt3.Fill(pt)
            if trig_dR0p2_L1TkPt2p5: L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt2p5.Fill(pt)
            if trig_dR0p2_L1TkPt2: L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt2.Fill(pt)

            if trig_dR0p12_L1TkPt4: L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt4.Fill(pt)
            if trig_dR0p12_L1TkPt3: L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt3.Fill(pt)
            if trig_dR0p12_L1TkPt2p5: L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt2p5.Fill(pt)
            if trig_dR0p12_L1TkPt2: 
              L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt2.Fill(pt)
              nGoodGenMuMatchedL1MuTriggered += 1
            else:
              print "\t\tGood GenMu with small dxy was not triggered", L1Mu_index              
              if L1Mu_index == 99:
                print "\t\t\tMissing L1Mu!"
                nGoodGenMuMissingL1Mu += 1
                print "\t\tlxy", lxy
              if L1Mu_index != 99:
                print "\t\t\tL1Mu was there!"
                L1Mu_pt = treeHits.L1Mu_pt[L1Mu_index]
                L1Mu_eta = treeHits.L1Mu_eta[L1Mu_index]
                L1Mu_phi = treeHits.L1Mu_phi[L1Mu_index]
                L1Mu_bx = treeHits.L1Mu_bx[L1Mu_index]
                L1Mu_quality = treeHits.L1Mu_quality[L1Mu_index]
                L1Mu_L1Tk_dR_prop = treeHits.L1Mu_L1Tk_dR_prop[L1Mu_index]
                L1Mu_L1Tk_pt = treeHits.L1Mu_L1Tk_pt_prop[L1Mu_index]
                matched = L1Mu_L1Tk_dR_prop <= 0.12 and L1Mu_quality >= 4
                common = (abs(L1Mu_bx) <= 0) and (L1Mu_quality >= 4)
#                print "\t\tProperties:", "pt", L1Mu_pt, "eta", L1Mu_eta, "phi", L1Mu_phi, "Quality", L1Mu_quality,
#                print "L1Tk_dR", L1Mu_L1Tk_dR_prop, "L1Tk_pt", L1Mu_L1Tk_pt, "bx", L1Mu_bx
                if (matched):
                  print "\t\t\tL1Mu was matched to a L1Tk!", L1Mu_L1Tk_dR_prop, L1Mu_L1Tk_pt
                  nGoodGenMuMatchedL1MuMatchedToL1Tk += 1
                  if L1Mu_L1Tk_pt >= 3: nGoodGenMuMatchedL1MuMatchedToL1TkPt3 += 1 
                  if L1Mu_L1Tk_pt >= 4: nGoodGenMuMatchedL1MuMatchedToL1TkPt4 += 1
                  if L1Mu_L1Tk_pt >= 5: nGoodGenMuMatchedL1MuMatchedToL1TkPt5 += 1
                  if L1Mu_L1Tk_pt >= 6: nGoodGenMuMatchedL1MuMatchedToL1TkPt6 += 1
                  if L1Mu_L1Tk_pt >= 10: nGoodGenMuMatchedL1MuMatchedToL1TkPt10 += 1

                else:
                  nGoodGenMuMatchedL1MuNotMatchedToL1Tk += 1              
                  if (not abs(L1Mu_bx) <= 0):
                    print "\t\t\tL1Mu does not have bx=0!"
                    nGoodGenMuMatchedL1MuNotMatchedToL1TkL1MuBXNot0 += 1
                  else:
                    if (L1Mu_quality<4):
                      print "\t\t\tL1Mu does not have Q>=0!"
                      nGoodGenMuMatchedL1MuNotMatchedToL1TkL1MuQLessThan4 += 1

          if dxy_range3 and eta_fid:
            genMu_pt_dxy5to10_fid.Fill(pt)
            if trigL1Mu:             L1Mu_genMu_pt_dxy5to10_fid.Fill(pt)

            ### plots with different veto cones per eta section
            if trig_dR0p4_L1TkPt4_total:   L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt4_total.Fill(pt)
            if trig_dR0p4_L1TkPt3_total:   L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt3_total.Fill(pt)
            if trig_dR0p4_L1TkPt2p5_total: L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p4_L1TkPt2_total:   L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt2_total.Fill(pt)

            if trig_dR0p3_L1TkPt4_total: L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt4_total.Fill(pt)
            if trig_dR0p3_L1TkPt3_total: L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt3_total.Fill(pt)
            if trig_dR0p3_L1TkPt2p5_total: L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p3_L1TkPt2_total: L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt2_total.Fill(pt)

            if trig_dR0p2_L1TkPt4_total: L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt4_total.Fill(pt)
            if trig_dR0p2_L1TkPt3_total: L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt3_total.Fill(pt)
            if trig_dR0p2_L1TkPt2p5_total: L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p2_L1TkPt2_total: L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt2_total.Fill(pt)

            if trig_dR0p12_L1TkPt4_total: L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt4_total.Fill(pt)
            if trig_dR0p12_L1TkPt3_total: L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt3_total.Fill(pt)
            if trig_dR0p12_L1TkPt2p5_total: L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p12_L1TkPt2_total: L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt2_total.Fill(pt)


            if trig_dR0p4_L1TkPt4:   L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt4.Fill(pt)
            if trig_dR0p4_L1TkPt3:   L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt3.Fill(pt)
            if trig_dR0p4_L1TkPt2p5: L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt2p5.Fill(pt)
            if trig_dR0p4_L1TkPt2:   L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt2.Fill(pt)

            if trig_dR0p3_L1TkPt4: L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt4.Fill(pt)
            if trig_dR0p3_L1TkPt3: L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt3.Fill(pt)
            if trig_dR0p3_L1TkPt2p5: L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt2p5.Fill(pt)
            if trig_dR0p3_L1TkPt2: L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt2.Fill(pt)

            if trig_dR0p2_L1TkPt4: L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt4.Fill(pt)
            if trig_dR0p2_L1TkPt3: L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt3.Fill(pt)
            if trig_dR0p2_L1TkPt2p5: L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt2p5.Fill(pt)
            if trig_dR0p2_L1TkPt2: L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt2.Fill(pt)

            if trig_dR0p12_L1TkPt4: L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt4.Fill(pt)
            if trig_dR0p12_L1TkPt3: L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt3.Fill(pt)
            if trig_dR0p12_L1TkPt2p5: L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt2p5.Fill(pt)
            if trig_dR0p12_L1TkPt2: L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt2.Fill(pt)

          if dxy_range4 and eta_fid:
            genMu_pt_dxy10_fid.Fill(pt)
            if trigL1Mu:             L1Mu_genMu_pt_dxy10_fid.Fill(pt)

            ### plots with different veto cones per eta section
            if trig_dR0p4_L1TkPt4_total:   L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt4_total.Fill(pt)
            if trig_dR0p4_L1TkPt3_total:   L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt3_total.Fill(pt)
            if trig_dR0p4_L1TkPt2p5_total: L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p4_L1TkPt2_total:   L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt2_total.Fill(pt)

            if trig_dR0p3_L1TkPt4_total: L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt4_total.Fill(pt)
            if trig_dR0p3_L1TkPt3_total: L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt3_total.Fill(pt)
            if trig_dR0p3_L1TkPt2p5_total: L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p3_L1TkPt2_total: L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt2_total.Fill(pt)

            if trig_dR0p2_L1TkPt4_total: L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt4_total.Fill(pt)
            if trig_dR0p2_L1TkPt3_total: L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt3_total.Fill(pt)
            if trig_dR0p2_L1TkPt2p5_total: L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p2_L1TkPt2_total: L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt2_total.Fill(pt)

            if trig_dR0p12_L1TkPt4_total: L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt4_total.Fill(pt)
            if trig_dR0p12_L1TkPt3_total: L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt3_total.Fill(pt)
            if trig_dR0p12_L1TkPt2p5_total: L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p12_L1TkPt2_total: L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt2_total.Fill(pt)


            if trig_dR0p4_L1TkPt4:   L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt4.Fill(pt)
            if trig_dR0p4_L1TkPt3:   L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt3.Fill(pt)
            if trig_dR0p4_L1TkPt2p5: L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt2p5.Fill(pt)
            if trig_dR0p4_L1TkPt2:   L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt2.Fill(pt)
             
            if trig_dR0p3_L1TkPt4: L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt4.Fill(pt)
            if trig_dR0p3_L1TkPt3: L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt3.Fill(pt)
            if trig_dR0p3_L1TkPt2p5: L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt2p5.Fill(pt)
            if trig_dR0p3_L1TkPt2: L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt2.Fill(pt)

            if trig_dR0p2_L1TkPt4: L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt4.Fill(pt)
            if trig_dR0p2_L1TkPt3: L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt3.Fill(pt)
            if trig_dR0p2_L1TkPt2p5: L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt2p5.Fill(pt)
            if trig_dR0p2_L1TkPt2: L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt2.Fill(pt)

            if trig_dR0p12_L1TkPt4: L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt4.Fill(pt)
            if trig_dR0p12_L1TkPt3: L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt3.Fill(pt)
            if trig_dR0p12_L1TkPt2p5: L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt2p5.Fill(pt)
            if trig_dR0p12_L1TkPt2: L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt2.Fill(pt)
            
          ## eta efficiencies
          if dxy_range1 and pt_fid:
            genMu_eta_dxy0to0p1_fid.Fill(eta)
            if trigL1Mu:             L1Mu_genMu_eta_dxy0to0p1_fid.Fill(eta)

            ### plots with different veto cones per eta section
            if trig_dR0p4_L1TkPt4_total:   
              L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt4_total.Fill(pt)
              print ">>>>OK!!!<<<<"
            if trig_dR0p4_L1TkPt3_total:   L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt3_total.Fill(pt)
            if trig_dR0p4_L1TkPt2p5_total: L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p4_L1TkPt2_total:   L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt2_total.Fill(pt)

            if trig_dR0p3_L1TkPt4_total: L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt4_total.Fill(pt)
            if trig_dR0p3_L1TkPt3_total: L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt3_total.Fill(pt)
            if trig_dR0p3_L1TkPt2p5_total: L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p3_L1TkPt2_total: L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt2_total.Fill(pt)

            if trig_dR0p2_L1TkPt4_total: L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt4_total.Fill(pt)
            if trig_dR0p2_L1TkPt3_total: L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt3_total.Fill(pt)
            if trig_dR0p2_L1TkPt2p5_total: L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p2_L1TkPt2_total: L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt2_total.Fill(pt)

            if trig_dR0p12_L1TkPt4_total: L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt4_total.Fill(pt)
            if trig_dR0p12_L1TkPt3_total: L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt3_total.Fill(pt)
            if trig_dR0p12_L1TkPt2p5_total: L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p12_L1TkPt2_total: L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt2_total.Fill(pt)


            if trig_dR0p4_L1TkPt4:   L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt4.Fill(eta)
            if trig_dR0p4_L1TkPt3:   L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt3.Fill(eta)
            if trig_dR0p4_L1TkPt2p5: L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt2p5.Fill(eta)
            if trig_dR0p4_L1TkPt2:   L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt2.Fill(eta)

            if trig_dR0p3_L1TkPt4: L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt4.Fill(eta)
            if trig_dR0p3_L1TkPt3: L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt3.Fill(eta)
            if trig_dR0p3_L1TkPt2p5: L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt2p5.Fill(eta)
            if trig_dR0p3_L1TkPt2: L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt2.Fill(eta)

            if trig_dR0p2_L1TkPt4: L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt4.Fill(eta)
            if trig_dR0p2_L1TkPt3: L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt3.Fill(eta)
            if trig_dR0p2_L1TkPt2p5: L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt2p5.Fill(eta)
            if trig_dR0p2_L1TkPt2: L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt2.Fill(eta)

            if trig_dR0p12_L1TkPt4: L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt4.Fill(eta)
            if trig_dR0p12_L1TkPt3: L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt3.Fill(eta)
            if trig_dR0p12_L1TkPt2p5: L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt2p5.Fill(eta)
            if trig_dR0p12_L1TkPt2: L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt2.Fill(eta)

          if dxy_range2 and pt_fid:
            genMu_eta_dxy1to5_fid.Fill(eta)
            if trigL1Mu:             L1Mu_genMu_eta_dxy1to5_fid.Fill(eta)

            ### plots with different veto cones per eta section
            if trig_dR0p4_L1TkPt4_total:   L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt4_total.Fill(pt)
            if trig_dR0p4_L1TkPt3_total:   L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt3_total.Fill(pt)
            if trig_dR0p4_L1TkPt2p5_total: L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p4_L1TkPt2_total:   L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt2_total.Fill(pt)

            if trig_dR0p3_L1TkPt4_total: L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt4_total.Fill(pt)
            if trig_dR0p3_L1TkPt3_total: L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt3_total.Fill(pt)
            if trig_dR0p3_L1TkPt2p5_total: L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p3_L1TkPt2_total: L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt2_total.Fill(pt)

            if trig_dR0p2_L1TkPt4_total: L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt4_total.Fill(pt)
            if trig_dR0p2_L1TkPt3_total: L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt3_total.Fill(pt)
            if trig_dR0p2_L1TkPt2p5_total: L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p2_L1TkPt2_total: L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt2_total.Fill(pt)

            if trig_dR0p12_L1TkPt4_total: L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt4_total.Fill(pt)
            if trig_dR0p12_L1TkPt3_total: L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt3_total.Fill(pt)
            if trig_dR0p12_L1TkPt2p5_total: L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p12_L1TkPt2_total: L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt2_total.Fill(pt)


            if trig_dR0p4_L1TkPt4:   L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt4.Fill(eta)
            if trig_dR0p4_L1TkPt3:   L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt3.Fill(eta)
            if trig_dR0p4_L1TkPt2p5: L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt2p5.Fill(eta)
            if trig_dR0p4_L1TkPt2:   L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt2.Fill(eta)

            if trig_dR0p3_L1TkPt4: L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt4.Fill(eta)
            if trig_dR0p3_L1TkPt3: L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt3.Fill(eta)
            if trig_dR0p3_L1TkPt2p5: L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt2p5.Fill(eta)
            if trig_dR0p3_L1TkPt2: L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt2.Fill(eta)

            if trig_dR0p2_L1TkPt4: L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt4.Fill(eta)
            if trig_dR0p2_L1TkPt3: L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt3.Fill(eta)
            if trig_dR0p2_L1TkPt2p5: L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt2p5.Fill(eta)
            if trig_dR0p2_L1TkPt2: L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt2.Fill(eta)

            if trig_dR0p12_L1TkPt4: L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt4.Fill(eta)
            if trig_dR0p12_L1TkPt3: L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt3.Fill(eta)
            if trig_dR0p12_L1TkPt2p5: L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt2p5.Fill(eta)
            if trig_dR0p12_L1TkPt2: L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt2.Fill(eta)

          if dxy_range3 and pt_fid:
            genMu_eta_dxy5to10_fid.Fill(eta)
            if trigL1Mu:             L1Mu_genMu_eta_dxy5to10_fid.Fill(eta)

            ### plots with different veto cones per eta section
            if trig_dR0p4_L1TkPt4_total:   L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt4_total.Fill(pt)
            if trig_dR0p4_L1TkPt3_total:   L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt3_total.Fill(pt)
            if trig_dR0p4_L1TkPt2p5_total: L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p4_L1TkPt2_total:   L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt2_total.Fill(pt)

            if trig_dR0p3_L1TkPt4_total: L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt4_total.Fill(pt)
            if trig_dR0p3_L1TkPt3_total: L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt3_total.Fill(pt)
            if trig_dR0p3_L1TkPt2p5_total: L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p3_L1TkPt2_total: L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt2_total.Fill(pt)

            if trig_dR0p2_L1TkPt4_total: L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt4_total.Fill(pt)
            if trig_dR0p2_L1TkPt3_total: L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt3_total.Fill(pt)
            if trig_dR0p2_L1TkPt2p5_total: L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p2_L1TkPt2_total: L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt2_total.Fill(pt)

            if trig_dR0p12_L1TkPt4_total: L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt4_total.Fill(pt)
            if trig_dR0p12_L1TkPt3_total: L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt3_total.Fill(pt)
            if trig_dR0p12_L1TkPt2p5_total: L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p12_L1TkPt2_total: L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt2_total.Fill(pt)


            if trig_dR0p4_L1TkPt4:   L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt4.Fill(eta)
            if trig_dR0p4_L1TkPt3:   L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt3.Fill(eta)
            if trig_dR0p4_L1TkPt2p5: L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt2p5.Fill(eta)
            if trig_dR0p4_L1TkPt2:   L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt2.Fill(eta)

            if trig_dR0p3_L1TkPt4: L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt4.Fill(eta)
            if trig_dR0p3_L1TkPt3: L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt3.Fill(eta)
            if trig_dR0p3_L1TkPt2p5: L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt2p5.Fill(eta)
            if trig_dR0p3_L1TkPt2: L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt2.Fill(eta)

            if trig_dR0p2_L1TkPt4: L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt4.Fill(eta)
            if trig_dR0p2_L1TkPt3: L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt3.Fill(eta)
            if trig_dR0p2_L1TkPt2p5: L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt2p5.Fill(eta)
            if trig_dR0p2_L1TkPt2: L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt2.Fill(eta)

            if trig_dR0p12_L1TkPt4: L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt4.Fill(eta)
            if trig_dR0p12_L1TkPt3: L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt3.Fill(eta)
            if trig_dR0p12_L1TkPt2p5: L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt2p5.Fill(eta)
            if trig_dR0p12_L1TkPt2: L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt2.Fill(eta)

          if dxy_range4 and pt_fid:
            genMu_eta_dxy10_fid.Fill(eta)
            if trigL1Mu:             L1Mu_genMu_eta_dxy10_fid.Fill(eta)


            ### plots with different veto cones per eta section
            if trig_dR0p4_L1TkPt4_total:   L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt4_total.Fill(pt)
            if trig_dR0p4_L1TkPt3_total:   L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt3_total.Fill(pt)
            if trig_dR0p4_L1TkPt2p5_total: L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p4_L1TkPt2_total:   L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt2_total.Fill(pt)

            if trig_dR0p3_L1TkPt4_total: L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt4_total.Fill(pt)
            if trig_dR0p3_L1TkPt3_total: L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt3_total.Fill(pt)
            if trig_dR0p3_L1TkPt2p5_total: L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p3_L1TkPt2_total: L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt2_total.Fill(pt)

            if trig_dR0p2_L1TkPt4_total: L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt4_total.Fill(pt)
            if trig_dR0p2_L1TkPt3_total: L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt3_total.Fill(pt)
            if trig_dR0p2_L1TkPt2p5_total: L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p2_L1TkPt2_total: L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt2_total.Fill(pt)

            if trig_dR0p12_L1TkPt4_total: L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt4_total.Fill(pt)
            if trig_dR0p12_L1TkPt3_total: L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt3_total.Fill(pt)
            if trig_dR0p12_L1TkPt2p5_total: L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt2p5_total.Fill(pt)
            if trig_dR0p12_L1TkPt2_total: L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt2_total.Fill(pt)


            if trig_dR0p4_L1TkPt4:   L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt4.Fill(eta)
            if trig_dR0p4_L1TkPt3:   L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt3.Fill(eta)
            if trig_dR0p4_L1TkPt2p5: L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt2p5.Fill(eta)
            if trig_dR0p4_L1TkPt2:   L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt2.Fill(eta)

            if trig_dR0p3_L1TkPt4: L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt4.Fill(eta)
            if trig_dR0p3_L1TkPt3: L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt3.Fill(eta)
            if trig_dR0p3_L1TkPt2p5: L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt2p5.Fill(eta)
            if trig_dR0p3_L1TkPt2: L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt2.Fill(eta)

            if trig_dR0p2_L1TkPt4: L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt4.Fill(eta)
            if trig_dR0p2_L1TkPt3: L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt3.Fill(eta)
            if trig_dR0p2_L1TkPt2p5: L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt2p5.Fill(eta)
            if trig_dR0p2_L1TkPt2: L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt2.Fill(eta)

            if trig_dR0p12_L1TkPt4: L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt4.Fill(eta)
            if trig_dR0p12_L1TkPt3: L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt3.Fill(eta)
            if trig_dR0p12_L1TkPt2p5: L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt2p5.Fill(eta)
            if trig_dR0p12_L1TkPt2: L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt2.Fill(eta)
    
    print "---------------------------------------------"
    print "Trigger Report"
    print "---------------------------------------------"
    print "nGoodGenMu", nGoodGenMu
    print "nGoodGenMuMatchedL1MuTriggered", nGoodGenMuMatchedL1MuTriggered
    print "nGoodGenMuMissingL1Mu", nGoodGenMuMissingL1Mu
    print "nGoodGenMuMatchedL1MuMatchedToL1Tk", nGoodGenMuMatchedL1MuMatchedToL1Tk
    print "\tnGoodGenMuMatchedL1MuMatchedToL1TkPt3", nGoodGenMuMatchedL1MuMatchedToL1TkPt3
    print "\tnGoodGenMuMatchedL1MuMatchedToL1TkPt4", nGoodGenMuMatchedL1MuMatchedToL1TkPt4
    print "\tnGoodGenMuMatchedL1MuMatchedToL1TkPt5", nGoodGenMuMatchedL1MuMatchedToL1TkPt5
    print "\tnGoodGenMuMatchedL1MuMatchedToL1TkPt6", nGoodGenMuMatchedL1MuMatchedToL1TkPt6
    print "\tnGoodGenMuMatchedL1MuMatchedToL1TkPt10", nGoodGenMuMatchedL1MuMatchedToL1TkPt10
    print "nGoodGenMuMatchedL1MuNotMatchedToL1Tk", nGoodGenMuMatchedL1MuNotMatchedToL1Tk
    print "nGoodGenMuMatchedL1MuNotMatchedToL1TkL1MuQLessThan4", nGoodGenMuMatchedL1MuNotMatchedToL1TkL1MuQLessThan4
    print "nGoodGenMuMatchedL1MuNotMatchedToL1TkL1MuBXNot0", nGoodGenMuMatchedL1MuNotMatchedToL1TkL1MuBXNot0
    print "---------------------------------------------"

    c = TCanvas("c","c",800,600)
    c.Clear()    
    gStyle.SetTitleBorderSize(0);
    gStyle.SetPadLeftMargin(0.126);
    gStyle.SetPadRightMargin(0.04);
    gStyle.SetPadTopMargin(0.06);
    gStyle.SetPadBottomMargin(0.13);
    gPad.SetTickx(1)
    gPad.SetTicky(1)
#    gStyle.SetPalette(kBlackBody)
    genMu_dxy_lxy_fid.Draw("colz")
    c.SaveAs("genMu_dxy_lxy_fid_plot.png")

    def makeEffPlot(eff1, eff2, eff3, eff4, title, doPt = True):
      
      c = TCanvas("c","c",800,600)
      c.Clear()    
      gStyle.SetTitleBorderSize(0);
      gStyle.SetPadLeftMargin(0.126);
      gStyle.SetPadRightMargin(0.04);
      gStyle.SetPadTopMargin(0.06);
      gStyle.SetPadBottomMargin(0.13);
      gPad.SetTickx(1)
      gPad.SetTicky(1)
      #gPad.SetLogx(1)
      
      if doPt: mmax = 50;  xaxisTitle = "True Muon p_{T} [GeV]"
      else:    mmax = 2.5; xaxisTitle = "True Muon #eta"

      b1 = TH1F("b1","b1", 25, 0, mmax)
      #b1.GetYaxis().SetRangeUser(.01,100)
      b1.GetYaxis().SetTitleOffset(1.2)
      b1.GetYaxis().SetNdivisions(520)
      b1.GetYaxis().SetTitle("Trigger efficiency")
      b1.GetXaxis().SetTitle(xaxisTitle)
      b1.GetXaxis().SetTitleFont(62)
      b1.GetXaxis().SetTitleOffset(1.2)
      b1.GetXaxis().SetTitleSize(0.045)
      b1.SetTitle("                                                                  14TeV, " + pu)
      b1.SetStats(0)
      b1.Draw()

      eff1.SetLineColor(kRed)
      eff1.Draw("same")
      eff2.SetLineColor(kMagenta+1)
      eff2.Draw("same")
      eff3.SetLineColor(kGreen+1)
      eff3.Draw("same")
      eff4.SetLineColor(kBlue)
      eff4.Draw("same")
      
      if doPt:
        errorAverage = sqrt(eff3.GetEfficiencyErrorUp(8)*eff3.GetEfficiencyErrorUp(8) + eff3.GetEfficiencyErrorUp(9)*eff3.GetEfficiencyErrorUp(9))/2.
        print title, "pt15", "%.2f"%((eff3.GetEfficiency(8) + eff3.GetEfficiency(9))/2.), "+/-%f"%(errorAverage)
        print title, "pt20", "%.2f"%(eff3.GetEfficiency(11)), "+/-%f"%(eff3.GetEfficiencyErrorUp(11))
        print

      latex = applyTdrStyle()      

      leg = TLegend(0.7,0.4,0.9,0.6,"","brNDC")
      leg.SetFillColor(kWhite)
      leg.SetBorderSize(0)
      leg.SetFillStyle(0)
      leg.SetTextSize(0.03)
      leg.AddEntry(eff1,"|dxy| #leq 0.1", "l")
      leg.AddEntry(eff2,"1 < |dxy| #leq 5", "l")
      leg.AddEntry(eff3,"5 < |dxy| #leq 10", "l")
      leg.AddEntry(eff4,"10 < |dxy| #leq 50", "l")
      leg.Draw("same")
      c.SaveAs(title)
    
    ## pt effciency plots
    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt2, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt2,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt2,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt2,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p4_L1TkPt2" + ext, True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt2p5, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt2p5,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt2p5,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt2p5,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p4_L1TkPt2p5" + ext, True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt3, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt3,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt3,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt3,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p4_L1TkPt3" + ext, True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt4, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt4,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt4,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt4,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p4_L1TkPt4" + ext, True)


    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt2, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt2,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt2,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt2,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p3_L1TkPt2" + ext, True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt2p5, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt2p5,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt2p5,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt2p5,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p3_L1TkPt2p5" + ext, True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt3, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt3,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt3,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt3,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p3_L1TkPt3" + ext, True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt4, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt4,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt4,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt4,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p3_L1TkPt4" + ext, True)


    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt2, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt2,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt2,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt2,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p2_L1TkPt2" + ext, True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt2p5, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt2p5,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt2p5,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt2p5,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p2_L1TkPt2p5" + ext, True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt3, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt3,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt3,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt3,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p2_L1TkPt3" + ext, True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt4, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt4,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt4,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt4,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p2_L1TkPt4" + ext, True)


    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt2, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt2,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt2,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt2,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p12_L1TkPt2" + ext, True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt2p5, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt2p5,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt2p5,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt2p5,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p12_L1TkPt2p5" + ext, True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt3, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt3,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt3,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt3,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p12_L1TkPt3" + ext, True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt4, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt4,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt4,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt4,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p12_L1TkPt4" + ext, True)

    
    ## eta effciency plots
    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt2, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt2,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt2,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt2,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p4_L1TkPt2" + ext, False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt2p5, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt2p5,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt2p5,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt2p5,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p4_L1TkPt2p5" + ext, False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt3, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt3,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt3,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt3,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p4_L1TkPt3" + ext, False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt4, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt4,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt4,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt4,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p4_L1TkPt4" + ext, False)


    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt2, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt2,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt2,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt2,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p3_L1TkPt2" + ext, False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt2p5, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt2p5,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt2p5,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt2p5,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p3_L1TkPt2p5" + ext, False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt3, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt3,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt3,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt3,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p3_L1TkPt3" + ext, False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt4, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt4,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt4,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt4,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p3_L1TkPt4" + ext, False)


    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt2, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt2,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt2,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt2,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p2_L1TkPt2" + ext, False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt2p5, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt2p5,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt2p5,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt2p5,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p2_L1TkPt2p5" + ext, False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt3, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt3,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt3,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt3,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p2_L1TkPt3" + ext, False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt4, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt4,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt4,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt4,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p2_L1TkPt4" + ext, False)


    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt2, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt2,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt2,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt2,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p12_L1TkPt2" + ext, False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt2p5, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt2p5,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt2p5,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt2p5,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p12_L1TkPt2p5" + ext, False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt3, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt3,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt3,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt3,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p12_L1TkPt3" + ext, False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt4, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt4,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt4,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt4,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p12_L1TkPt4" + ext, False)


    ## PLOTS WITH DIFFERENT CONE SIZES IN BARREL/overlap/endcap
    ## pt effciency plots
    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt2_total, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt2_total,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt2_total,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt2_total,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p4_L1TkPt2_total" + ext, True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt2p5_total, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt2p5_total,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt2p5_total,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt2p5_total,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p4_L1TkPt2p5_total" + ext, True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt3_total, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt3_total,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt3_total,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt3_total,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p4_L1TkPt3_total" + ext, True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p4_L1TkPt4_total, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p4_L1TkPt4_total,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p4_L1TkPt4_total,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p4_L1TkPt4_total,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p4_L1TkPt4_total" + ext, True)


    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt2_total, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt2_total,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt2_total,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt2_total,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p3_L1TkPt2_total" + ext, True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt2p5_total, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt2p5_total,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt2p5_total,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt2p5_total,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p3_L1TkPt2p5_total" + ext, True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt3_total, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt3_total,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt3_total,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt3_total,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p3_L1TkPt3_total" + ext, True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p3_L1TkPt4_total, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p3_L1TkPt4_total,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p3_L1TkPt4_total,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p3_L1TkPt4_total,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p3_L1TkPt4_total" + ext, True)


    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt2_total, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt2_total,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt2_total,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt2_total,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p2_L1TkPt2_total" + ext, True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt2p5_total, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt2p5_total,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt2p5_total,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt2p5_total,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p2_L1TkPt2p5_total" + ext, True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt3_total, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt3_total,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt3_total,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt3_total,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p2_L1TkPt3_total" + ext, True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p2_L1TkPt4_total, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p2_L1TkPt4_total,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p2_L1TkPt4_total,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p2_L1TkPt4_total,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p2_L1TkPt4_total" + ext, True)


    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt2_total, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt2_total,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt2_total,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt2_total,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p12_L1TkPt2_total" + ext, True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt2p5_total, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt2p5_total,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt2p5_total,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt2p5_total,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p12_L1TkPt2p5_total" + ext, True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt3_total, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt3_total,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt3_total,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt3_total,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p12_L1TkPt3_total" + ext, True)

    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid_dR0p12_L1TkPt4_total, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid_dR0p12_L1TkPt4_total,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid_dR0p12_L1TkPt4_total,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid_dR0p12_L1TkPt4_total,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid_dR0p12_L1TkPt4_total" + ext, True)

    
    ## eta effciency plots
    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt2_total, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt2_total,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt2_total,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt2_total,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p4_L1TkPt2_total" + ext, False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt2p5_total, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt2p5_total,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt2p5_total,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt2p5_total,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p4_L1TkPt2p5_total" + ext, False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt3_total, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt3_total,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt3_total,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt3_total,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p4_L1TkPt3_total" + ext, False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p4_L1TkPt4_total, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p4_L1TkPt4_total,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p4_L1TkPt4_total,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p4_L1TkPt4_total,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p4_L1TkPt4_total" + ext, False)


    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt2_total, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt2_total,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt2_total,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt2_total,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p3_L1TkPt2_total" + ext, False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt2p5_total, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt2p5_total,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt2p5_total,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt2p5_total,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p3_L1TkPt2p5_total" + ext, False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt3_total, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt3_total,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt3_total,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt3_total,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p3_L1TkPt3_total" + ext, False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p3_L1TkPt4_total, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p3_L1TkPt4_total,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p3_L1TkPt4_total,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p3_L1TkPt4_total,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p3_L1TkPt4_total" + ext, False)


    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt2_total, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt2_total,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt2_total,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt2_total,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p2_L1TkPt2_total" + ext, False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt2p5_total, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt2p5_total,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt2p5_total,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt2p5_total,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p2_L1TkPt2p5_total" + ext, False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt3_total, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt3_total,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt3_total,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt3_total,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p2_L1TkPt3_total" + ext, False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p2_L1TkPt4_total, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p2_L1TkPt4_total,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p2_L1TkPt4_total,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p2_L1TkPt4_total,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p2_L1TkPt4_total" + ext, False)


    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt2_total, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt2_total,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt2_total,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt2_total,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p12_L1TkPt2_total" + ext, False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt2p5_total, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt2p5_total,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt2p5_total,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt2p5_total,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p12_L1TkPt2p5_total" + ext, False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt3_total, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt3_total,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt3_total,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt3_total,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p12_L1TkPt3_total" + ext, False)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid_dR0p12_L1TkPt4_total, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid_dR0p12_L1TkPt4_total,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid_dR0p12_L1TkPt4_total,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid_dR0p12_L1TkPt4_total,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid_dR0p12_L1TkPt4_total" + ext, False)



    ## debug for slava
    makeEffPlot(TEfficiency(L1Mu_genMu_pt_dxy0to0p1_fid, genMu_pt_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_pt_dxy1to5_fid,   genMu_pt_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_pt_dxy5to10_fid,  genMu_pt_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_pt_dxy10_fid,     genMu_pt_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_pt_fid" + ext, True)

    makeEffPlot(TEfficiency(L1Mu_genMu_eta_dxy0to0p1_fid, genMu_eta_dxy0to0p1_fid),
                TEfficiency(L1Mu_genMu_eta_dxy1to5_fid,   genMu_eta_dxy1to5_fid),
                TEfficiency(L1Mu_genMu_eta_dxy5to10_fid,  genMu_eta_dxy5to10_fid),
                TEfficiency(L1Mu_genMu_eta_dxy10_fid,     genMu_eta_dxy10_fid),
                targetDir + "L1Mu_trigger_efficiency_eta_fid" + ext, False)

    def makeDxyEffPlot(eff1, eff2, eff3, eff4, eff5, title):
      
      c = TCanvas("c","c",800,600)
      c.Clear()    
      gStyle.SetTitleBorderSize(0);
      gStyle.SetPadLeftMargin(0.126);
      gStyle.SetPadRightMargin(0.04);
      gStyle.SetPadTopMargin(0.06);
      gStyle.SetPadBottomMargin(0.13);
      gPad.SetTickx(1)
      gPad.SetTicky(1)
      gPad.SetLogx(1)
      
      binning2 = [0.05, 0.07, 0.1, 0.2, 0.3, 0.5, 1, 2, 4, 6, 10, 15, 20, 30, 50, 100, 200, 250, 275, 300, 400, 500, 1000] #
      nBins = len(binning2) - 1

      #b1 = TH1F("b1","b1", 30, 0, 30)
      b1 = TH1F("b1","b1", nBins, np.asarray(binning2))
      #b1.GetYaxis().SetRangeUser(.01,100)
      b1.GetYaxis().SetTitleOffset(1.2)
      b1.GetYaxis().SetNdivisions(520)
      b1.GetYaxis().SetTitle("Trigger Reconstruction efficiency")
      b1.GetXaxis().SetTitle("True Muon d_{xy} [cm]")
      b1.GetXaxis().SetTitleFont(62)
      b1.GetXaxis().SetTitleOffset(1.2)
      b1.GetXaxis().SetTitleSize(0.045)
      b1.SetTitle("                                                                  14TeV, " + pu)
      b1.SetStats(0)
      b1.Draw()

      eff1.SetLineColor(kBlue)
      eff1.SetLineWidth(2)
      eff1.Draw("same")
      if eff2:
        eff2.SetLineColor(kOrange+1)
        eff2.SetLineWidth(2)
        eff2.Draw("same")
      if eff3:
        eff3.SetLineColor(kRed)
        eff3.SetLineWidth(2)
        eff3.Draw("same")
      if eff4:
        eff4.SetLineColor(kGreen+1)
        eff4.SetLineWidth(2)
        eff4.Draw("same")
      if eff5:
        eff5.SetLineColor(kMagenta+1)
        eff5.SetLineWidth(2)
        eff5.Draw("same")
        
      latex = applyTdrStyle()      

      leg = TLegend(0.25,0.2,0.75,0.45,"","brNDC")
      leg.SetFillColor(kWhite)
      leg.SetBorderSize(0)
      leg.SetFillStyle(0)
      leg.SetTextSize(0.03)
      leg.AddEntry(eff1,"L1Mu", "l")
      leg.AddEntry(eff2,"L1Mu (Q#geq4)", "l")
      leg.AddEntry(eff3,"L1Mu (Q#geq4, BX=0)", "l")
      leg.AddEntry(eff4,"L1Mu (Q#geq4, BX=0) + veto (dR#leq0.12)", "l")
      leg.AddEntry(eff5,"L1Mu (Q#geq4, BX=0) + veto (dR#leq0.12) + isol (dR<0.2, p_{T}^{L1Tk}#geq4)", "l")
      leg.Draw("same")
      c.SaveAs(targetDir + title)
      
    #makeDxyEffPlot(TEfficiency(firstSecondBin(L1Mu_genMu_dxy_fidT), firstSecondBin(genMu_dxy_fidT)), 
    #               "L1Mu_trigger_efficiency_dxy_fidT" + ext)
    makeDxyEffPlot(TEfficiency(firstSecondBin(L1Mu_genMu_lxy_fid), firstSecondBin(genMu_lxy_fid)),
                   TEfficiency(firstSecondBin(L1Mu_genMu_lxy_fid_Q), firstSecondBin(genMu_lxy_fid)), 
                   TEfficiency(firstSecondBin(L1Mu_genMu_lxy_fid_BX_Q), firstSecondBin(genMu_lxy_fid)),
                   TEfficiency(firstSecondBin(L1Mu_genMu_lxy_fid_BX_Q_V), firstSecondBin(genMu_lxy_fid)),
                   TEfficiency(firstSecondBin(L1Mu_genMu_lxy_fid_BX_Q_V_I), firstSecondBin(genMu_lxy_fid)),
                   "L1Mu_trigger_efficiency_lxy_fid" + ext)

    makeDxyEffPlot(TEfficiency(firstSecondBin(L1Mu_genMu_dxy_fid), firstSecondBin(genMu_dxy_fid)),
                   TEfficiency(firstSecondBin(L1Mu_genMu_dxy_fid_Q), firstSecondBin(genMu_dxy_fid)), 
                   TEfficiency(firstSecondBin(L1Mu_genMu_dxy_fid_BX_Q), firstSecondBin(genMu_dxy_fid)),
                   TEfficiency(firstSecondBin(L1Mu_genMu_dxy_fid_BX_Q_V), firstSecondBin(genMu_dxy_fid)),
                   TEfficiency(firstSecondBin(L1Mu_genMu_dxy_fid_BX_Q_V_I), firstSecondBin(genMu_dxy_fid)),
                   "L1Mu_trigger_efficiency_dxy_fid" + ext)

    makeDxyEffPlot(TEfficiency(firstSecondBin(L1Mu_genMu_dxy_fid_barrel), firstSecondBin(genMu_dxy_fid_barrel)),
                   TEfficiency(firstSecondBin(L1Mu_genMu_dxy_fid_Q_barrel), firstSecondBin(genMu_dxy_fid_barrel)), 
                   TEfficiency(firstSecondBin(L1Mu_genMu_dxy_fid_BX_Q_barrel), firstSecondBin(genMu_dxy_fid_barrel)),
                   TEfficiency(firstSecondBin(L1Mu_genMu_dxy_fid_BX_Q_V_barrel), firstSecondBin(genMu_dxy_fid_barrel)),
                   TEfficiency(firstSecondBin(L1Mu_genMu_dxy_fid_BX_Q_V_I_barrel), firstSecondBin(genMu_dxy_fid_barrel)),
                   "L1Mu_trigger_efficiency_dxy_fid_barrel" + ext)

    makeDxyEffPlot(TEfficiency(firstSecondBin(L1Mu_genMu_dxy_fid_overlap), firstSecondBin(genMu_dxy_fid_overlap)),
                   TEfficiency(firstSecondBin(L1Mu_genMu_dxy_fid_Q_overlap), firstSecondBin(genMu_dxy_fid_overlap)), 
                   TEfficiency(firstSecondBin(L1Mu_genMu_dxy_fid_BX_Q_overlap), firstSecondBin(genMu_dxy_fid_overlap)),
                   TEfficiency(firstSecondBin(L1Mu_genMu_dxy_fid_BX_Q_V_overlap), firstSecondBin(genMu_dxy_fid_overlap)),
                   TEfficiency(firstSecondBin(L1Mu_genMu_dxy_fid_BX_Q_V_I_overlap), firstSecondBin(genMu_dxy_fid_overlap)),
                   "L1Mu_trigger_efficiency_dxy_fid_overlap" + ext)
 
    makeDxyEffPlot(TEfficiency(firstSecondBin(L1Mu_genMu_dxy_fid_endcap), firstSecondBin(genMu_dxy_fid_endcap)),
                   TEfficiency(firstSecondBin(L1Mu_genMu_dxy_fid_Q_endcap), firstSecondBin(genMu_dxy_fid_endcap)), 
                   TEfficiency(firstSecondBin(L1Mu_genMu_dxy_fid_BX_Q_endcap), firstSecondBin(genMu_dxy_fid_endcap)),
                   TEfficiency(firstSecondBin(L1Mu_genMu_dxy_fid_BX_Q_V_endcap), firstSecondBin(genMu_dxy_fid_endcap)),
                   TEfficiency(firstSecondBin(L1Mu_genMu_dxy_fid_BX_Q_V_I_endcap), firstSecondBin(genMu_dxy_fid_endcap)),
                   "L1Mu_trigger_efficiency_dxy_fid_endcap" + ext)

    """
    makeDxyEffPlot(TEfficiency(firstSecondBin(L1Mu_genMu_dxy_fid_BX_Q), firstSecondBin(genMu_dxy_fid)), 
                   "L1Mu_trigger_efficiency_dxy_fid_BX_Q" + ext)
    makeDxyEffPlot(TEfficiency(firstSecondBin(L1Mu_genMu_dxy_fid_BX_Q_V), firstSecondBin(genMu_dxy_fid)), 
                   "L1Mu_trigger_efficiency_dxy_fid_BX_Q_V" + ext)
    """               
  if eff:
    makeEfficiencyHistogram()

  exit()


  def fitSigma():
    ### fits to get the sigma
    c = TCanvas("c","c",800,600)
    c.Clear()
    gStyle.SetTitleBorderSize(0);
    gStyle.SetPadLeftMargin(0.126);
    gStyle.SetPadRightMargin(0.04);
    gStyle.SetPadTopMargin(0.06);
    gStyle.SetPadBottomMargin(0.13);
    treeHits.Draw("abs(dEta_sim_corr)>>h_name(100,0,0.1)")
    h = TH1F(gDirectory.Get("h_name").Clone("h_name"))
    if not h:
      sys.exit('h does not exist')
    h.SetTitle("PU = 140, 14 TeV; |d#eta_{corr}(L1Mu,SIM)|; Entries")
    h.SetLineWidth(2)
    h.SetLineColor(kBlue)
    h.GetXaxis().SetLabelSize(0.05)
    h.GetYaxis().SetLabelSize(0.05)
    h.GetXaxis().SetTitleSize(0.06)
    h.GetYaxis().SetTitleSize(0.06)
    h.Draw()
    h.SaveAs("dEta_sim_corr_fit.root")
  
    c = TCanvas("c","c",800,600)
    c.Clear()
    gStyle.SetTitleBorderSize(0);
    gStyle.SetPadLeftMargin(0.126);
    gStyle.SetPadRightMargin(0.04);
    gStyle.SetPadTopMargin(0.06);
    gStyle.SetPadBottomMargin(0.13);
    treeHits.Draw("abs(dPhi_sim_corr)>>h_name(100,0,0.1")
    h = TH1F(gDirectory.Get("h_name").Clone("h_name"))
    if not h:
      sys.exit('h does not exist')
    h.SetTitle("PU = 140, 14 TeV; |d#phi_{corr}(L1Mu,SIM)|; Entries")
    h.SetLineWidth(2)
    h.SetLineColor(kBlue)
    h.GetXaxis().SetLabelSize(0.05)
    h.GetYaxis().SetLabelSize(0.05)
    h.GetXaxis().SetTitleSize(0.06)
    h.GetYaxis().SetTitleSize(0.06)
    h.Fit("gaus","L")
    h.Draw()
    h.SaveAs("dPhi_sim_corr_fit.root")

    c = TCanvas("c","c",800,600)
    c.Clear()
    gStyle.SetTitleBorderSize(0);
    gStyle.SetPadLeftMargin(0.126);
    gStyle.SetPadRightMargin(0.04);
    gStyle.SetPadTopMargin(0.06);
    gStyle.SetPadBottomMargin(0.13);
    treeHits.Draw("abs(dEta_L1Tk_corr)>>h_name(100,0,0.1)")
    h = TH1F(gDirectory.Get("h_name").Clone("h_name"))
    if not h:
      sys.exit('h does not exist')
    h.SetTitle("PU = 140, 14 TeV; |d#eta_{corr}(L1Mu,L1TK)|; Entries")
    h.SetLineWidth(2)
    h.SetLineColor(kBlue)
    h.GetXaxis().SetLabelSize(0.05)
    h.GetYaxis().SetLabelSize(0.05)
    h.GetXaxis().SetTitleSize(0.06)
    h.GetYaxis().SetTitleSize(0.06)
    h.Draw()
    h.SaveAs("dEta_L1Tk_corr_fit.root")
  
    c = TCanvas("c","c",800,600)
    c.Clear()
    gStyle.SetTitleBorderSize(0);
    gStyle.SetPadLeftMargin(0.126);
    gStyle.SetPadRightMargin(0.04);
    gStyle.SetPadTopMargin(0.06);
    gStyle.SetPadBottomMargin(0.13);
    treeHits.Draw("abs(dPhi_L1Tk_corr)>>h_name(100,0,0.1")
    h = TH1F(gDirectory.Get("h_name").Clone("h_name"))
    if not h:
      sys.exit('h does not exist')
    h.SetTitle("PU = 140, 14 TeV; |d#phi_{corr}(L1Mu,L1TK)|; Entries")
    h.SetLineWidth(2)
    h.SetLineColor(kBlue)
    h.GetXaxis().SetLabelSize(0.05)
    h.GetYaxis().SetLabelSize(0.05)
    h.GetXaxis().SetTitleSize(0.06)
    h.GetYaxis().SetTitleSize(0.06)
    h.Fit("gaus","L")
    h.Draw()
    h.SaveAs("dPhi_L1Tk_corr_fit.root")


  ### regular plots
  draw_1D(treeHits,"abs(dEta_sim_corr)",  "dEta_sim_corr",  "PU = 140, 14 TeV; |d#eta_{corr}(L1Mu,SIM)|; Entries", "(100,0,1)")
  draw_1D(treeHits,"abs(dPhi_sim_corr)",  "dPhi_sim_corr",  "PU = 140, 14 TeV; |d#phi_{corr}(L1Mu,SIM)|; Entries", "(100,0,1)")

  draw_1D(treeHits,"dR_sim_corr",  "dR_sim_corr",  "PU = 140, 14 TeV; |dR_{corr}(L1Mu,SIM)|; Entries", "(100,0,0.2)")
  draw_1D(treeHits,"dR_sim_corr",  "dR_sim_corr_fid",  "PU = 140, 14 TeV; |dR_{corr}(L1Mu,SIM)|; Entries", "(100,0,0.2)",TCut("abs(eta)<=2.5"))
  draw_1D(treeHits,"dR_sim_corr",  "dR_sim_corr_pt10_fid",  "PU = 140, 14 TeV; |dR_{corr}(L1Mu,SIM)|; Entries", "(100,0,0.2)",TCut("pt>=10 && abs(eta)<=2.5"))
  draw_1D(treeHits,"dR_sim_corr",  "dR_sim_corr_pt15_fid",  "PU = 140, 14 TeV; |dR_{corr}(L1Mu,SIM)|; Entries", "(100,0,0.2)",TCut("pt>=15 && abs(eta)<=2.5"))
  draw_1D(treeHits,"dR_sim_corr",  "dR_sim_corr_pt20_fid",  "PU = 140, 14 TeV; |dR_{corr}(L1Mu,SIM)|; Entries", "(100,0,0.2)",TCut("pt>=20 && abs(eta)<=2.5"))

  draw_1D(treeHits,"abs(dEta_sim_prop)",  "dEta_sim_prop",  "PU = 140, 14 TeV; |d#eta_{corr}(L1Mu,SIM)|; Entries", "(100,0,1)")
  draw_1D(treeHits,"abs(dPhi_sim_prop)",  "dPhi_sim_prop",  "PU = 140, 14 TeV; |d#phi_{corr}(L1Mu,SIM)|; Entries", "(100,0,1)")

  draw_1D(treeHits,"dR_sim_prop",  "dR_sim_prop",  "PU = 140, 14 TeV; |dR_{prop}(L1Mu,SIM)|; Entries", "(100,0,0.2)")
  draw_1D(treeHits,"dR_sim_prop",  "dR_sim_prop_fid",  "PU = 140, 14 TeV; |dR_{prop}(L1Mu,SIM)|; Entries", "(100,0,0.2)",TCut("abs(eta)<=2.5"))
  draw_1D(treeHits,"dR_sim_prop",  "dR_sim_prop_pt10_fid",  "PU = 140, 14 TeV; |dR_{prop}(L1Mu,SIM)|; Entries", "(100,0,0.2)",TCut("pt>=10 && abs(eta)<=2.5"))
  draw_1D(treeHits,"dR_sim_prop",  "dR_sim_prop_pt15_fid",  "PU = 140, 14 TeV; |dR_{prop}(L1Mu,SIM)|; Entries", "(100,0,0.2)",TCut("pt>=15 && abs(eta)<=2.5"))
  draw_1D(treeHits,"dR_sim_prop",  "dR_sim_prop_pt20_fid",  "PU = 140, 14 TeV; |dR_{prop}(L1Mu,SIM)|; Entries", "(100,0,0.2)",TCut("pt>=20 && abs(eta)<=2.5"))

  draw_1D(treeHits,"pt",  "pt_L1",  "p_{T,L1} [GeV]", "(100,0,200)")
  draw_1D(treeHits,"eta",  "eta_L1",  "#eta_{L1}", "(60,-3,3)")
  draw_1D(treeHits,"phi",  "phi_L1",  "#phi_{L1}", "(70,-3.5,3.5)")
  draw_1D(treeHits,"quality",  "quality",  "quality", "(10,0,10)")
  draw_1D(treeHits,"charge",  "charge",  "charge", "(5,-2,2)")

  draw_2D(treeHits,"dPhi_sim_corr:dEta_sim_prop",  "dEta_dPhi_sim_prop",  "PU = 140, 14 TeV; |d#eta_{corr}(L1Mu,SIM)|; |d#phi_{corr}(L1Mu,SIM)|", "(100,0,0.2,100,0,0.2)")
  draw_2D(treeHits,"dPhi_sim_prop:dEta_sim_prop",  "dEta_dPhi_sim_prop",  "PU = 140, 14 TeV; |d#eta_{prop}(L1Mu,SIM)|; |d#phi_{prop}(L1Mu,SIM)|", "(100,0,0.2,100,0,0.2)")


  draw_1D(treeHits,"dEta_L1Tk_corr",  "dEta_L1Tk_corr",  "PU = 140, 14 TeV; |d#eta_{corr}(L1Mu,L1Tk)|; Entries", "(100,0,1)")
  draw_1D(treeHits,"dPhi_L1Tk_corr",  "dPhi_L1Tk_corr",  "PU = 140, 14 TeV; |d#phi_{corr}(L1Mu,L1Tk)|; Entries", "(100,0,1)")

  draw_1D(treeHits,"dR_L1Tk_corr",  "dR_L1Tk_corr",  "PU = 140, 14 TeV; |dR_{prop}(L1Mu,L1Tk)|; Entries", "(100,0,1)")
  draw_1D(treeHits,"dR_L1Tk_corr",  "dR_L1Tk_corr_pt10_fid",  "PU = 140, 14 TeV; |dR_{prop}(L1Mu,L1Tk)|; Entries", "(100,0,1)",TCut("pt>=10 && abs(eta)<=2.5"))
  draw_1D(treeHits,"dR_L1Tk_corr",  "dR_L1Tk_corr_pt20_fid",  "PU = 140, 14 TeV; |dR_{prop}(L1Mu,L1Tk)|; Entries", "(100,0,1)",TCut("pt>=20 && abs(eta)<=2.5"))

  draw_1D(treeHits,"dEta_L1Tk_prop",  "dEta_L1Tk_prop",  "PU = 140, 14 TeV; |d#eta_{prop}(L1Mu,L1Tk)|; Entries", "(100,0,1)")
  draw_1D(treeHits,"dPhi_L1Tk_prop",  "dPhi_L1Tk_prop",  "PU = 140, 14 TeV; |d#phi_{prop}(L1Mu,L1Tk)|; Entries", "(100,0,1)")

  draw_1D(treeHits,"dR_L1Tk_prop",  "dR_L1Tk_prop",  "PU = 140, 14 TeV; |dR_{prop}(L1Mu,L1Tk)|; Entries", "(100,0,1)")
  draw_1D(treeHits,"dR_L1Tk_prop",  "dR_L1Tk_prop_pt10_fid",  "PU = 140, 14 TeV; |dR_{prop}(L1Mu,L1Tk)|; Entries", "(100,0,1)",TCut("pt>=10 && abs(eta)<=2.5"))
  draw_1D(treeHits,"dR_L1Tk_prop",  "dR_L1Tk_prop_pt20_fid",  "PU = 140, 14 TeV; |dR_{prop}(L1Mu,L1Tk)|; Entries", "(100,0,1)",TCut("pt>=20 && abs(eta)<=2.5"))

  draw_2D(treeHits,"dPhi_L1Tk_corr:dEta_L1Tk_prop",  "dEta_dPhi_L1Tk_prop",  "PU = 140, 14 TeV; |d#eta_{corr}(L1Mu,L1TK)|; |d#phi_{corr}(L1Mu,L1TK)|", "(100,0,1,100,0,1)")
  draw_2D(treeHits,"dPhi_L1Tk_prop:dEta_L1Tk_prop",  "dEta_dPhi_L1Tk_prop",  "PU = 140, 14 TeV; |d#eta_{prop}(L1Mu,L1TK)|; |d#phi_{prop}(L1Mu,L1TK)|", "(100,0,1,100,0,1)")


  draw_1D(treeHits,"dEta_sim_L1Tk",  "dEta_sim_L1Tk",  "PU = 140, 14 TeV; |d#eta(SIM,L1Tk)|; Entries", "(100,0,0.05)")
  draw_1D(treeHits,"dPhi_sim_L1Tk",  "dPhi_sim_L1Tk",  "PU = 140, 14 TeV; |d#phi(SIM,L1Tk)|; Entries", "(100,0,0.05)")


  etaBinning = "(25,0,2.5)"

  makeEtaEffPlot(getEffObject(treeHits, "abs(eta_sim)", etaBinning, TCut(""), TCut("pt_sim>=0")), "eff_sim_eta_pt0_sim", "")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta_sim)", etaBinning, TCut(""), TCut("pt_sim>=10")), "eff_sim_eta_pt10_sim", "")

  makeEtaEffPlot(getEffObject(treeHits, "abs(eta_sim)", etaBinning, AND(TCut("pt_sim>=10"), TCut("abs(dR_sim_prop)<=0.2")), TCut("abs(dR_L1Tk_prop)<=0.12") ), "eff_sim_eta_pt10_L1MuDR02_dR012_L1Tk_prop", 
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 10 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta_sim)", etaBinning, AND(TCut("pt_sim>=10"), TCut("abs(dR_sim_corr)<=0.2")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_sim_eta_pt10_L1MuDR02_dR012_L1Tk_prop", 
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 10 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta_sim)", etaBinning, AND(TCut("pt_sim>=15"), TCut("abs(dR_sim_prop)<=0.2")), TCut("abs(dR_L1Tk_prop)<=0.12") ), "eff_sim_eta_pt15_L1MuDR02_dR012_L1Tk_prop", 
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 15 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta_sim)", etaBinning, AND(TCut("pt_sim>=15"), TCut("abs(dR_sim_corr)<=0.2")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_sim_eta_pt15_L1MuDR02_dR012_L1Tk_prop", 
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 15 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta_sim)", etaBinning, AND(TCut("pt_sim>=20"), TCut("abs(dR_sim_prop)<=0.2")), TCut("abs(dR_L1Tk_prop)<=0.12") ), "eff_sim_eta_pt20_L1MuDR02_dR012_L1Tk_prop", 
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 20 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta_sim)", etaBinning, AND(TCut("pt_sim>=20"), TCut("abs(dR_sim_corr)<=0.2")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_sim_eta_pt20_L1MuDR02_dR012_L1Tk_prop", 
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 20 GeV, dR(L1Tk,L1Mu)<=0.12")

  makeEtaEffPlot(getEffObject(treeHits, "abs(eta_sim)", etaBinning, AND(TCut("pt_sim>=10"), TCut("abs(dR_sim_corr)<=0.2")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_sim_eta_pt10_L1MuDR02_dR012_L1Tk_corr", 
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 10 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta_sim)", etaBinning, AND(TCut("pt_sim>=10"), TCut("abs(dR_sim_corr)<=0.2")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_sim_eta_pt10_L1MuDR02_dR012_L1Tk_corr", 
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 10 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta_sim)", etaBinning, AND(TCut("pt_sim>=15"), TCut("abs(dR_sim_corr)<=0.2")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_sim_eta_pt15_L1MuDR02_dR012_L1Tk_corr",
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 15 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta_sim)", etaBinning, AND(TCut("pt_sim>=15"), TCut("abs(dR_sim_corr)<=0.2")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_sim_eta_pt15_L1MuDR02_dR012_L1Tk_corr", 
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 15 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta_sim)", etaBinning, AND(TCut("pt_sim>=20"), TCut("abs(dR_sim_corr)<=0.2")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_sim_eta_pt20_L1MuDR02_dR012_L1Tk_corr", 
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 20 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta_sim)", etaBinning, AND(TCut("pt_sim>=20"), TCut("abs(dR_sim_corr)<=0.2")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_sim_eta_pt20_L1MuDR02_dR012_L1Tk_corr", 
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 20 GeV, dR(L1Tk,L1Mu)<=0.12")



  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt_sim>=10"), TCut("abs(dR_sim_prop)<=0.2")), TCut("abs(dR_L1Tk_prop)<=0.12") ), "eff_L1_eta_pt10_L1MuDR02_dR012_L1Tk_prop", 
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 10 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt_sim>=10"), TCut("abs(dR_sim_corr)<=0.2")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_L1_eta_pt10_L1MuDR02_dR012_L1Tk_prop", 
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 10 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt_sim>=15"), TCut("abs(dR_sim_prop)<=0.2")), TCut("abs(dR_L1Tk_prop)<=0.12") ), "eff_L1_eta_pt15_L1MuDR02_dR012_L1Tk_prop", 
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 15 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt_sim>=15"), TCut("abs(dR_sim_corr)<=0.2")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_L1_eta_pt15_L1MuDR02_dR012_L1Tk_prop", 
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 15 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt_sim>=20"), TCut("abs(dR_sim_prop)<=0.2")), TCut("abs(dR_L1Tk_prop)<=0.12") ), "eff_L1_eta_pt20_L1MuDR02_dR012_L1Tk_prop", 
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 20 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt_sim>=20"), TCut("abs(dR_sim_corr)<=0.2")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_L1_eta_pt20_L1MuDR02_dR012_L1Tk_prop", 
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 20 GeV, dR(L1Tk,L1Mu)<=0.12")

  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt_sim>=10"), TCut("abs(dR_sim_corr)<=0.2")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_L1_eta_pt10_L1MuDR02_dR012_L1Tk_corr", 
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 10 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt_sim>=10"), TCut("abs(dR_sim_corr)<=0.2")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_L1_eta_pt10_L1MuDR02_dR012_L1Tk_corr", 
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 10 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt_sim>=15"), TCut("abs(dR_sim_corr)<=0.2")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_L1_eta_pt15_L1MuDR02_dR012_L1Tk_corr",
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 15 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt_sim>=15"), TCut("abs(dR_sim_corr)<=0.2")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_L1_eta_pt15_L1MuDR02_dR012_L1Tk_corr", 
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 15 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt_sim>=20"), TCut("abs(dR_sim_corr)<=0.2")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_L1_eta_pt20_L1MuDR02_dR012_L1Tk_corr", 
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 20 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt_sim>=20"), TCut("abs(dR_sim_corr)<=0.2")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_L1_eta_pt20_L1MuDR02_dR012_L1Tk_corr", 
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 20 GeV, dR(L1Tk,L1Mu)<=0.12")

  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt_sim>=10"), TCut("abs(dR_sim_corr)<=0.2"), TCut("quality>=4")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_L1_eta_pt10_Q4_L1MuDR02_dR012_L1Tk_corr", 
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 10 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt_sim>=10"), TCut("abs(dR_sim_corr)<=0.2"), TCut("quality>=4")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_L1_eta_pt10_Q4_L1MuDR02_dR012_L1Tk_corr", 
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 10 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt_sim>=15"), TCut("abs(dR_sim_corr)<=0.2"), TCut("quality>=4")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_L1_eta_pt15_Q4_L1MuDR02_dR012_L1Tk_corr",
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 15 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt_sim>=15"), TCut("abs(dR_sim_corr)<=0.2"), TCut("quality>=4")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_L1_eta_pt15_Q4_L1MuDR02_dR012_L1Tk_corr", 
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 15 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt_sim>=20"), TCut("abs(dR_sim_corr)<=0.2"), TCut("quality>=4")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_L1_eta_pt20_Q4_L1MuDR02_dR012_L1Tk_corr", 
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 20 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt_sim>=20"), TCut("abs(dR_sim_corr)<=0.2"), TCut("quality>=4")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_L1_eta_pt20_Q4_L1MuDR02_dR012_L1Tk_corr", 
                 "dR(SIM,L1Mu)<=0.2, p_{T}^{SIM} >= 20 GeV, dR(L1Tk,L1Mu)<=0.12")

  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt>=10"), TCut("quality>=4")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_L1_eta_pt10_Q4_dR012_L1Tk_corr", 
                 "p_{T} >= 10 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt>=10"), TCut("quality>=4")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_L1_eta_pt10_Q4_dR012_L1Tk_corr", 
                 "p_{T} >= 10 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt>=15"), TCut("quality>=4")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_L1_eta_pt15_Q4_dR012_L1Tk_corr",
                 "p_{T} >= 15 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt>=15"), TCut("quality>=4")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_L1_eta_pt15_Q4_dR012_L1Tk_corr", 
                 "p_{T} >= 15 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt>=20"), TCut("quality>=4")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_L1_eta_pt20_Q4_dR012_L1Tk_corr", 
                 "p_{T} >= 20 GeV, dR(L1Tk,L1Mu)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt>=20"), TCut("quality>=4")), TCut("abs(dR_L1Tk_corr)<=0.12") ), "eff_L1_eta_pt20_Q4_dR012_L1Tk_corr", 
                 "p_{T} >= 20 GeV, dR(L1Tk,L1Mu)<=0.12")



  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, TCut("pt>=10"), TCut("abs(dR_sim_corr)<=0.2")), "eff_L1_eta_pt10_sim_corr", "dR(SIM,L1Mu)<=0.2, p_{T} >= 10 GeV")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, TCut("pt>=15"), TCut("abs(dR_sim_corr)<=0.2")), "eff_L1_eta_pt15_sim_corr", "dR(SIM,L1Mu)<=0.2, p_{T} >= 15 GeV")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, TCut("pt>=20"), TCut("abs(dR_sim_corr)<=0.2")), "eff_L1_eta_pt20_sim_corr", "dR(SIM,L1Mu)<=0.2, p_{T} >= 20 GeV")
  
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, TCut("pt>=10"), TCut("abs(dR_sim_prop)<=0.2")), "eff_L1_eta_pt10_sim_prop", "dR(SIM,L1Mu)<=0.2, p_{T} >= 10 GeV")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, TCut("pt>=15"), TCut("abs(dR_sim_prop)<=0.2")), "eff_L1_eta_pt15_sim_prop", "dR(SIM,L1Mu)<=0.2, p_{T} >= 15 GeV")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, TCut("pt>=20"), TCut("abs(dR_sim_prop)<=0.2")), "eff_L1_eta_pt20_sim_prop", "dR(SIM,L1Mu)<=0.2, p_{T} >= 20 GeV")

  makeEtaEffPlot(getEffObject(treeHits, "abs(eta_sim)", etaBinning, TCut("pt>=10"), TCut("abs(dR_sim_corr)<=0.2")), "eff_sim_eta_pt10_sim_corr", "dR(SIM,L1Mu)<=0.2, p_{T} >= 10 GeV")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta_sim)", etaBinning, TCut("pt>=15"), TCut("abs(dR_sim_corr)<=0.2")), "eff_sim_eta_pt15_sim_corr", "dR(SIM,L1Mu)<=0.2, p_{T} >= 15 GeV")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta_sim)", etaBinning, TCut("pt>=20"), TCut("abs(dR_sim_corr)<=0.2")), "eff_sim_eta_pt20_sim_corr", "dR(SIM,L1Mu)<=0.2, p_{T} >= 20 GeV")
  
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta_sim)", etaBinning, TCut("pt>=10"), TCut("abs(dR_sim_prop)<=0.2")), "eff_sim_eta_pt10_sim_prop", "dR(SIM,L1Mu)<=0.2, p_{T} >= 10 GeV")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta_sim)", etaBinning, TCut("pt>=15"), TCut("abs(dR_sim_prop)<=0.2")), "eff_sim_eta_pt15_sim_prop", "dR(SIM,L1Mu)<=0.2, p_{T} >= 15 GeV")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta_sim)", etaBinning, TCut("pt>=20"), TCut("abs(dR_sim_prop)<=0.2")), "eff_sim_eta_pt20_sim_prop", "dR(SIM,L1Mu)<=0.2, p_{T} >= 20 GeV")

  """
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt>=10"),TCut("abs(dR_sim_prop)<=0.2")), TCut("abs(dR_L1Tk_prop)<=0.12")), "eff_L1_eta_pt10_sim_prop_L1Tk_prop", "dR(SIM,L1Mu)<=0.2, p_{T} >= 10 GeV, dR(L1Mu,L1Tk)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt>=20"),TCut("abs(dR_sim_prop)<=0.2")), TCut("abs(dR_L1Tk_prop)<=0.12")), "eff_L1_eta_pt20_sim_prop_L1Tk_prop", "dR(SIM,L1Mu)<=0.2, p_{T} >= 20 GeV, dR(L1Mu,L1Tk)<=0.12")

  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt>=10"),TCut("abs(dR_sim_corr)<=0.2")), TCut("abs(dR_L1Tk_corr)<=0.12")), "eff_L1_eta_pt10_sim_corr_L1Tk_corr", "dR(SIM,L1Mu)<=0.2, p_{T} >= 10 GeV, dR(L1Mu,L1Tk)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt>=20"),TCut("abs(dR_sim_corr)<=0.2")), TCut("abs(dR_L1Tk_corr)<=0.12")), "eff_L1_eta_pt20_sim_corr_L1Tk_corr", "dR(SIM,L1Mu)<=0.2, p_{T} >= 20 GeV, dR(L1Mu,L1Tk)<=0.12")


  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt>=10"),TCut("abs(dR_sim_prop)<=0.2"), TCut("quality>=4")), TCut("abs(dR_L1Tk_prop)<=0.12")), "eff_L1_eta_pt10_sim_prop_L1Tk_prop_q", "dR(SIM,L1Mu)<=0.2, p_{T} >= 10 GeV, dR(L1Mu,L1Tk)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt>=20"),TCut("abs(dR_sim_prop)<=0.2"), TCut("quality>=4")), TCut("abs(dR_L1Tk_prop)<=0.12")), "eff_L1_eta_pt20_sim_prop_L1Tk_prop_q", "dR(SIM,L1Mu)<=0.2, p_{T} >= 20 GeV, dR(L1Mu,L1Tk)<=0.12")

  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt>=10"),TCut("abs(dR_sim_corr)<=0.2"), TCut("quality>=4")), TCut("abs(dR_L1Tk_corr)<=0.12")), "eff_L1_eta_pt10_sim_corr_L1Tk_corr_q", "dR(SIM,L1Mu)<=0.2, p_{T} >= 10 GeV, dR(L1Mu,L1Tk)<=0.12")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt>=20"),TCut("abs(dR_sim_corr)<=0.2"), TCut("quality>=4")), TCut("abs(dR_L1Tk_corr)<=0.12")), "eff_L1_eta_pt20_sim_corr_L1Tk_corr_q", "dR(SIM,L1Mu)<=0.2, p_{T} >= 20 GeV, dR(L1Mu,L1Tk)<=0.12")

  #  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, TCut("pt>=15"), TCut("abs(dR_sim_prop)<=0.2")), "eff_L1_eta_pt15_sim_prop", "dR(SIM,L1Mu)<=0.2, p_{T} >= 15 GeV")
  #  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, TCut("pt>=20"), TCut("abs(dR_sim_prop)<=0.2")), "eff_L1_eta_pt20_sim_prop", "dR(SIM,L1Mu)<=0.2, p_{T} >= 20 GeV")
   """

  denom = 0.
  n_L1_sim_corr = 0.
  n_L1_sim_corr_fid = 0.
  
  num = 0.
  num2 = 0.

  h_L1_eta_pt10 = TH1F("h_L1_eta_pt10", "title", 25,0,2.5)
  h_L1_eta_pt15 = TH1F("h_L1_eta_pt15", "title", 25,0,2.5)
  h_L1_eta_pt20 = TH1F("h_L1_eta_pt20", "title", 25,0,2.5)

  h_L1_eta_pt10_sim_corr = TH1F("h_L1_eta_pt10_sim_corr", "title", 25,0,2.5)
  h_L1_eta_pt10_sim_prop = TH1F("h_L1_eta_pt10_sim_prop", "title", 25,0,2.5)
  h_L1_eta_pt15_sim_corr = TH1F("h_L1_eta_pt15_sim_corr", "title", 25,0,2.5)
  h_L1_eta_pt15_sim_prop = TH1F("h_L1_eta_pt15_sim_prop", "title", 25,0,2.5)
  h_L1_eta_pt20_sim_corr = TH1F("h_L1_eta_pt20_sim_corr", "title", 25,0,2.5)
  h_L1_eta_pt20_sim_prop = TH1F("h_L1_eta_pt20_sim_prop", "title", 25,0,2.5)


  denom = 0.
  num = 0.
  num2 = 0.

  for k in range(0,treeHits.GetEntries()):
    treeHits.GetEntry(k)
    #print "event", k

    if (abs(treeHits.dR_sim_corr)<=0.2):
      n_L1_sim_corr = n_L1_sim_corr + 1

    if (abs(treeHits.dR_sim_corr)<=0.2 and abs(treeHits.eta)<=2.5 and treeHits.pt>=10):
      n_L1_sim_corr_fid = n_L1_sim_corr_fid + 1

    if (abs(treeHits.eta)<=2.5):

      if (treeHits.pt>=10):
        h_L1_eta_pt10.Fill(abs(treeHits.eta))
        if (abs(treeHits.dR_sim_corr)<=0.2):
          h_L1_eta_pt10_sim_corr.Fill(abs(treeHits.eta))
        if (abs(treeHits.dR_sim_prop)<=0.2):
          h_L1_eta_pt10_sim_prop.Fill(abs(treeHits.eta))

      if (treeHits.pt>=15):
        h_L1_eta_pt15.Fill(abs(treeHits.eta))
        if (abs(treeHits.dR_sim_corr)<=0.2):
          h_L1_eta_pt15_sim_corr.Fill(abs(treeHits.eta))
        if (abs(treeHits.dR_sim_prop)<=0.2):
          h_L1_eta_pt15_sim_prop.Fill(abs(treeHits.eta))

      if (treeHits.pt>=20):
        h_L1_eta_pt20.Fill(abs(treeHits.eta))
        if (abs(treeHits.dR_sim_prop)<=0.2):
          h_L1_eta_pt20_sim_prop.Fill(abs(treeHits.eta))
        if (abs(treeHits.dR_sim_corr)<=0.2): 
          h_L1_eta_pt20_sim_corr.Fill(abs(treeHits.eta))
          if treeHits.L1Mu_quality>=4:
            denom += 1
            if (abs(treeHits.dR_L1Tk_prop)<=0.12):
              num += 1
            if (abs(treeHits.dR_L1Tk_corr)<=0.12):
              num2 += 1


        """
        else:
        print "Did not make the cut"
        print "event", k
        print treeHits.dR_sim_corr
        print treeHits.pt, treeHits.eta, treeHits.phi
        print treeHits.pt_sim, treeHits.eta_sim, treeHits.phi_sim
        print 
        """
          
#  print "num", num, "denom", denom, "eff", num/denom
#  print "num2", num2, "denom", denom, "eff2", num2/denom

  makeEtaEffPlot(TEfficiency(h_L1_eta_pt10_sim_corr, h_L1_eta_pt10), "eff_L1_eta_pt10_sim_corr_loop", "dR(SIM,L1Mu)<=0.2, p_{T} >= 10 GeV")
  makeEtaEffPlot(TEfficiency(h_L1_eta_pt10_sim_prop, h_L1_eta_pt10), "eff_L1_eta_pt10_sim_prop_loop", "dR(SIM,L1Mu)<=0.2, p_{T} >= 10 GeV")

  makeEtaEffPlot(TEfficiency(h_L1_eta_pt15_sim_corr, h_L1_eta_pt15), "eff_L1_eta_pt15_sim_corr_loop", "dR(SIM,L1Mu)<=0.2, p_{T} >= 15 GeV")
  makeEtaEffPlot(TEfficiency(h_L1_eta_pt15_sim_prop, h_L1_eta_pt15), "eff_L1_eta_pt15_sim_prop_loop", "dR(SIM,L1Mu)<=0.2, p_{T} >= 15 GeV")

  makeEtaEffPlot(TEfficiency(h_L1_eta_pt20_sim_corr, h_L1_eta_pt20), "eff_L1_eta_pt20_sim_corr_loop", "dR(SIM,L1Mu)<=0.2, p_{T} >= 20 GeV")
  makeEtaEffPlot(TEfficiency(h_L1_eta_pt20_sim_prop, h_L1_eta_pt20), "eff_L1_eta_pt20_sim_prop_loop", "dR(SIM,L1Mu)<=0.2, p_{T} >= 20 GeV")

  
  """
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt>10"), TCut("dR_sim_corr<0.2")), TCut("dR_L1Tk<0.12")), "eff_L1_eta_pt10_sim_L1_dRL1Tk_012", "dR(SIM,L1Mu)<0.2, p_{T} > 10 GeV, L1Mu is matched")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt>10"), TCut("dR_sim_corr<0.2")), TCut("dR_L1Tk_corr<0.12")), "eff_L1_eta_pt10_sim_L1_dRL1TkCorr_012", "dR(SIM,L1Mu)<0.2, p_{T} > 10 GeV, L1Mu is matched")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt>15"), TCut("dR_sim_corr<0.2")), TCut("dR_L1Tk<0.12")), "eff_L1_eta_pt15_sim_L1_dRL1Tk_012", "dR(SIM,L1Mu)<0.2, p_{T} > 15 GeV, L1Mu is matched")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt>15"), TCut("dR_sim_corr<0.2")), TCut("dR_L1Tk_corr<0.12")), "eff_L1_eta_pt15_sim_L1_dRL1TkCorr_012", "dR(SIM,L1Mu)<0.2, p_{T} > 15 GeV, L1Mu is matched")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt>20"), TCut("dR_sim_corr<0.2")), TCut("dR_L1Tk<0.12")), "eff_L1_eta_pt20_sim_L1_dRL1Tk_012", "dR(SIM,L1Mu)<0.2, p_{T} > 20 GeV, L1Mu is matched")
  makeEtaEffPlot(getEffObject(treeHits, "abs(eta)", etaBinning, AND(TCut("pt>20"), TCut("dR_sim_corr<0.2")), TCut("dR_L1Tk_corr<0.12")), "eff_L1_eta_pt20_sim_L1_dRL1TkCorr_012", "dR(SIM,L1Mu)<0.2, p_{T} > 20 GeV, L1Mu is matched")
  """
