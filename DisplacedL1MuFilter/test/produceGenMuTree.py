# Run quiet mode
import sys
sys.argv.append( '-b' )
import ROOT
ROOT.gROOT.SetBatch(1)
from Helpers import *
ROOT.gErrorIgnoreLevel=1001
from ROOT import *
import random
import numpy
from BarrelTriggerAlgorithms import *
from EndcapTriggerAlgorithms import *

def deltaPhi(phi1, phi2):
  result = phi1 - phi2;
  while (result > M_PI):
    result -= 2*M_PI;
  while (result <= -M_PI):
    result += 2*M_PI;
  return result;

#______________________________________________________________________________
if __name__ == "__main__":

  ## extension for figures - add more?
  ext = ".png"

  ## Style
  gStyle.SetStatStyle(0)

  print "Making the plots"

  set_style()

  verbose = False

  ch = TChain("DisplacedL1MuFilter_PhaseIIGE21/L1MuTree")

  dirname1='/Users/Sven/Documents/work/DisplacedMuL1Studies/DarkSUSY_MH-125_MGammaD-20000_ctauX_14TeV_madgraph-pythia6-tauola/DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_L1MuANA_v54/'
  dirname2='/Users/Sven/Documents/work/DisplacedMuL1Studies/DarkSUSY_MH-125_MGammaD-20000_ctauX_14TeV_madgraph-pythia6-tauola/DarkSUSY_mH_125_mGammaD_20000_cT_100_14TeV_PU140_L1MuANA_v54/'
  dirname3='/Users/Sven/Documents/work/DisplacedMuL1Studies/DarkSUSY_MH-125_MGammaD-20000_ctauX_14TeV_madgraph-pythia6-tauola/DarkSUSY_mH_125_mGammaD_20000_cT_10_14TeV_PU140_L1MuANA_v54/'

  #dirname1='/eos/uscms/store/user/lpcgem/DarkSUSY_MH-125_MGammaD-20000_ctau1000_14TeV_madgraph-pythia6-tauola/DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_L1MuANA_v54/170214_025720/0000/'
  #dirname2='/eos/uscms/store/user/lpcgem/DarkSUSY_MH-125_MGammaD-20000_ctau100_14TeV_madgraph-pythia6-tauola/DarkSUSY_mH_125_mGammaD_20000_cT_100_14TeV_PU140_L1MuANA_v54/170214_025529/0000/'
  #dirname3='/eos/uscms/store/user/lpcgem/DarkSUSY_MH-125_MGammaD-20000_ctau10_14TeV_madgraph-pythia6-tauola/DarkSUSY_mH_125_mGammaD_20000_cT_10_14TeV_PU140_L1MuANA_v54/170214_022535/0000/'

  print "Start run on", ch.GetEntries(), "events."
  ch = addfiles(ch, dirname=dirname1)
  print "Start run on", ch.GetEntries(), "events."
  ch = addfiles(ch, dirname=dirname2)
  print "Start run on", ch.GetEntries(), "events."
  ch = addfiles(ch, dirname=dirname3)
  print "Start run on", ch.GetEntries(), "events."
  treeHits = ch

  f = ROOT.TFile("out_ana_pu140_displaced_L1Mu_DDY123_StubRec_Barrel20170302.root", "recreate")
  t = ROOT.TTree("L1MuTree", "L1MuTree")

  ## ranges
  DTCombinations = ['DT1_DT2','DT1_DT3','DT1_DT4',
                    'DT2_DT3','DT2_DT4','DT3_DT4']
  ME1ME2ParityCases = ['oe','oo','ee','eo']
  ME1ME2ParityCasesString = ['odd-even','odd-odd','even-even','even-odd']
  ME1ME2ME3ParityCases = ['oee','ooo','eee','eoo']
  dxyRanges = ['','_dxy0to5','_dxy5to50','_dxy50to100']
  dxyRangesString = ['','|d_{xy}|<5 cm','5 <|d_{xy}|<50 cm','50 <|d_{xy}|<100 cm']
  L1MuPtCuts = ['10','15','20']
  fitTypes = ['withLCTFit', 'withoutLCTFit']
  L1MuPtSlices = ['2to5','5to10','10to20','20to30','30to100']
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
  binLow = [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,12.0,14.0,16.0,18.0,20.0,24.0,28.0,32.0,36.0,42.0,50.0]
  ptbins = np.asarray(binLow)

  ## arrays
  gen_pts = numpy.zeros(1, dtype=float)
  gen_etas = numpy.zeros(1, dtype=float)
  gen_phis = numpy.zeros(1, dtype=float)
  gen_dxys = numpy.zeros(1, dtype=float)

  sim_pts = numpy.zeros(1, dtype=float)
  sim_etas = numpy.zeros(1, dtype=float)
  sim_phis = numpy.zeros(1, dtype=float)

  SIM_L1Mu_indexs = numpy.zeros(1, dtype=int)
  SIM_L1Mu_dRs = numpy.zeros(1, dtype=float)

  has_L1Mus = numpy.zeros(1, dtype=int)
  L1Mu_pts = numpy.zeros(1, dtype=float)
  L1Mu_etas = numpy.zeros(1, dtype=float)
  L1Mu_phis = numpy.zeros(1, dtype=float)
  L1Mu_qualitys = numpy.zeros(1, dtype=int)
  L1Mu_bxs = numpy.zeros(1, dtype=int)
  L1Mu_trues = numpy.zeros(1, dtype=int)

  has_CSCTFs = numpy.zeros(1, dtype=int)
  CSCTF_pts = numpy.zeros(1, dtype=float)
  CSCTF_etas = numpy.zeros(1, dtype=float)
  CSCTF_phis = numpy.zeros(1, dtype=float)
  CSCTF_qualitys = numpy.zeros(1, dtype=int)
  CSCTF_bxs = numpy.zeros(1, dtype=int)

  CSCTF_eta2s = numpy.zeros(1, dtype=float)
  CSCTF_sim_eta2s = numpy.zeros(1, dtype=float)

  ## check if station is there
  ok_CSCTF_st1s = numpy.zeros(1, dtype=int)
  ok_CSCTF_st2s = numpy.zeros(1, dtype=int)
  ok_CSCTF_st3s = numpy.zeros(1, dtype=int)
  ok_CSCTF_st4s = numpy.zeros(1, dtype=int)

  ok_CSCTF_sim_st1s = numpy.zeros(1, dtype=int)
  ok_CSCTF_sim_st2s = numpy.zeros(1, dtype=int)
  ok_CSCTF_sim_st3s = numpy.zeros(1, dtype=int)
  ok_CSCTF_sim_st4s = numpy.zeros(1, dtype=int)

  ## phi-eta
  CSCTF_phi1s = numpy.zeros(1, dtype=float)
  CSCTF_phi2s = numpy.zeros(1, dtype=float)
  CSCTF_phi3s = numpy.zeros(1, dtype=float)
  CSCTF_phi4s = numpy.zeros(1, dtype=float)

  CSCTF_sim_phi1s = numpy.zeros(1, dtype=float)
  CSCTF_sim_phi2s = numpy.zeros(1, dtype=float)
  CSCTF_sim_phi3s = numpy.zeros(1, dtype=float)
  CSCTF_sim_phi4s = numpy.zeros(1, dtype=float)

  CSCTF_eta1s = numpy.zeros(1, dtype=float)
  CSCTF_eta2s = numpy.zeros(1, dtype=float)
  CSCTF_eta3s = numpy.zeros(1, dtype=float)
  CSCTF_eta4s = numpy.zeros(1, dtype=float)

  CSCTF_sim_eta1s = numpy.zeros(1, dtype=float)
  CSCTF_sim_eta2s = numpy.zeros(1, dtype=float)
  CSCTF_sim_eta3s = numpy.zeros(1, dtype=float)
  CSCTF_sim_eta4s = numpy.zeros(1, dtype=float)

  ## ch number
  CSCTF_ch1s = numpy.zeros(1, dtype=float)
  CSCTF_ch2s = numpy.zeros(1, dtype=float)
  CSCTF_ch3s = numpy.zeros(1, dtype=float)
  CSCTF_ch4s = numpy.zeros(1, dtype=float)

  CSCTF_sim_ch1s = numpy.zeros(1, dtype=float)
  CSCTF_sim_ch2s = numpy.zeros(1, dtype=float)
  CSCTF_sim_ch3s = numpy.zeros(1, dtype=float)
  CSCTF_sim_ch4s = numpy.zeros(1, dtype=float)

  ## global z
  CSCTF_z1s = numpy.zeros(1, dtype=float)
  CSCTF_z2s = numpy.zeros(1, dtype=float)
  CSCTF_z3s = numpy.zeros(1, dtype=float)
  CSCTF_z4s = numpy.zeros(1, dtype=float)

  CSCTF_sim_z1s = numpy.zeros(1, dtype=float)
  CSCTF_sim_z2s = numpy.zeros(1, dtype=float)
  CSCTF_sim_z3s = numpy.zeros(1, dtype=float)
  CSCTF_sim_z4s = numpy.zeros(1, dtype=float)

  ## chamber number
  CSCTF_ch1s = numpy.zeros(1, dtype=int)
  CSCTF_ch2s = numpy.zeros(1, dtype=int)
  CSCTF_ch3s = numpy.zeros(1, dtype=int)
  CSCTF_ch4s = numpy.zeros(1, dtype=int)

  CSCTF_sim_ch1s = numpy.zeros(1, dtype=int)
  CSCTF_sim_ch2s = numpy.zeros(1, dtype=int)
  CSCTF_sim_ch3s = numpy.zeros(1, dtype=int)
  CSCTF_sim_ch4s = numpy.zeros(1, dtype=int)

  CSCTF_isEven1s = numpy.zeros(1, dtype=int)
  CSCTF_isEven2s = numpy.zeros(1, dtype=int)
  CSCTF_isEven3s = numpy.zeros(1, dtype=int)
  CSCTF_isEven4s = numpy.zeros(1, dtype=int)

  CSCTF_sim_isEven1s = numpy.zeros(1, dtype=int)
  CSCTF_sim_isEven2s = numpy.zeros(1, dtype=int)
  CSCTF_sim_isEven3s = numpy.zeros(1, dtype=int)
  CSCTF_sim_isEven4s = numpy.zeros(1, dtype=int)


  ## displaced trigger
  paritys_sim = numpy.zeros(1, dtype=int)
  partitions_sim = numpy.zeros(1, dtype=int)
  paritys_L1 = numpy.zeros(1, dtype=int)
  partitions_L1 = numpy.zeros(1, dtype=int)

  DDY123_pts = numpy.zeros(1, dtype=float)
  DDY123_withLCTFits = numpy.zeros(1, dtype=float)
  DDY123_withoutLCTFits = numpy.zeros(1, dtype=float)

  CSCTF_sim_DDY123s = numpy.zeros(1, dtype=float)
  CSCTF_L1_DDY123s = numpy.zeros(1, dtype=float)

  CSCTF_sim_DPhi12_noGE21s = numpy.zeros(1, dtype=float)
  CSCTF_L1_DPhi12_noGE21s = numpy.zeros(1, dtype=float)
  CSCTF_sim_DPhi12_GE21s = numpy.zeros(1, dtype=float)
  CSCTF_L1_DPhi12_GE21s = numpy.zeros(1, dtype=float)

  CSCTF_sim_position_pts = numpy.zeros(1, dtype=float)
  CSCTF_L1_position_pts = numpy.zeros(1, dtype=float)
  CSCTF_sim_direction_pt_noGE21s = numpy.zeros(1, dtype=float)
  CSCTF_L1_direction_pt_noGE21s = numpy.zeros(1, dtype=float)
  CSCTF_sim_direction_pt_GE21s = numpy.zeros(1, dtype=float)
  CSCTF_L1_direction_pt_GE21s = numpy.zeros(1, dtype=float)

  CSCTF_sim_hybrid_pt_noGE21s = numpy.zeros(1, dtype=float)
  CSCTF_L1_hybrid_pt_noGE21s = numpy.zeros(1, dtype=float)
  CSCTF_sim_hybrid_pt_GE21s = numpy.zeros(1, dtype=float)
  CSCTF_L1_hybrid_pt_GE21s = numpy.zeros(1, dtype=float)

  CSCTF_sim_eta_st2s = numpy.zeros(1, dtype=float)
  CSCTF_L1_eta_st2s = numpy.zeros(1, dtype=float)

  ## isolation
  L1Mu_isLooseVetos = numpy.zeros(1, dtype=int)
  L1Mu_isMediumVetos = numpy.zeros(1, dtype=int)
  L1Mu_isTightVetos = numpy.zeros(1, dtype=int)

  ## gem hits are there!!
  ok_GE11_L1s = numpy.zeros(1, dtype=int)
  ok_GE11_L2s = numpy.zeros(1, dtype=int)
  ok_GE21_L1s = numpy.zeros(1, dtype=int)
  ok_GE21_L2s = numpy.zeros(1, dtype=int)

  ok_GE11_sim_L1s = numpy.zeros(1, dtype=int)
  ok_GE11_sim_L2s = numpy.zeros(1, dtype=int)
  ok_GE21_sim_L1s = numpy.zeros(1, dtype=int)
  ok_GE21_sim_L2s = numpy.zeros(1, dtype=int)

  ## phi
  GE11_L1_phis = numpy.zeros(1, dtype=float)
  GE11_L2_phis = numpy.zeros(1, dtype=float)
  GE21_L1_phis = numpy.zeros(1, dtype=float)
  GE21_L2_phis = numpy.zeros(1, dtype=float)

  GE11_sim_L1_phis = numpy.zeros(1, dtype=float)
  GE11_sim_L2_phis = numpy.zeros(1, dtype=float)
  GE21_sim_L1_phis = numpy.zeros(1, dtype=float)
  GE21_sim_L2_phis = numpy.zeros(1, dtype=float)

  ## BX
  GE11_L1_bxs = numpy.zeros(1, dtype=int)
  GE11_L2_bxs = numpy.zeros(1, dtype=int)
  GE21_L1_bxs = numpy.zeros(1, dtype=int)
  GE21_L2_bxs = numpy.zeros(1, dtype=int)

  GE11_sim_L1_bxs = numpy.zeros(1, dtype=int)
  GE11_sim_L2_bxs = numpy.zeros(1, dtype=int)
  GE21_sim_L1_bxs = numpy.zeros(1, dtype=int)
  GE21_sim_L2_bxs = numpy.zeros(1, dtype=int)

  ## global z
  GE11_L1_zs = numpy.zeros(1, dtype=float)
  GE11_L2_zs = numpy.zeros(1, dtype=float)
  GE21_L1_zs = numpy.zeros(1, dtype=float)
  GE21_L2_zs = numpy.zeros(1, dtype=float)

  GE11_sim_L1_zs = numpy.zeros(1, dtype=float)
  GE11_sim_L2_zs = numpy.zeros(1, dtype=float)
  GE21_sim_L1_zs = numpy.zeros(1, dtype=float)
  GE21_sim_L2_zs = numpy.zeros(1, dtype=float)






  has_DTTFs = numpy.zeros(1, dtype=int)
  DTTF_pts = numpy.zeros(1, dtype=float)
  DTTF_etas = numpy.zeros(1, dtype=float)
  DTTF_phis = numpy.zeros(1, dtype=float)
  DTTF_qualitys = numpy.zeros(1, dtype=int)
  DTTF_bxs = numpy.zeros(1, dtype=int)

  ok_DTTF_st1s = numpy.zeros(1, dtype=int)
  ok_DTTF_st2s = numpy.zeros(1, dtype=int)
  ok_DTTF_st3s = numpy.zeros(1, dtype=int)
  ok_DTTF_st4s = numpy.zeros(1, dtype=int)

  DTTF_phi1s = numpy.zeros(1, dtype=float)
  DTTF_phi2s = numpy.zeros(1, dtype=float)
  DTTF_phi3s = numpy.zeros(1, dtype=float)
  DTTF_phi4s = numpy.zeros(1, dtype=float)

  DTTF_phib1s = numpy.zeros(1, dtype=float)
  DTTF_phib2s = numpy.zeros(1, dtype=float)
  DTTF_phib3s = numpy.zeros(1, dtype=float)
  DTTF_phib4s = numpy.zeros(1, dtype=float)

  DTTF_phib1_phib2s = numpy.zeros(1, dtype=float)
  DTTF_phib1_phib3s = numpy.zeros(1, dtype=float)
  DTTF_phib1_phib4s = numpy.zeros(1, dtype=float)
  DTTF_phib2_phib3s = numpy.zeros(1, dtype=float)
  DTTF_phib2_phib4s = numpy.zeros(1, dtype=float)
  DTTF_phib3_phib4s = numpy.zeros(1, dtype=float)

  abs_DTTF_phib1_phib2s = numpy.zeros(1, dtype=float)
  abs_DTTF_phib1_phib3s = numpy.zeros(1, dtype=float)
  abs_DTTF_phib1_phib4s = numpy.zeros(1, dtype=float)
  abs_DTTF_phib2_phib3s = numpy.zeros(1, dtype=float)
  abs_DTTF_phib2_phib4s = numpy.zeros(1, dtype=float)
  abs_DTTF_phib3_phib4s = numpy.zeros(1, dtype=float)

  DTTF_DT1_DT2_pts = numpy.zeros(1, dtype=float)
  DTTF_DT1_DT3_pts = numpy.zeros(1, dtype=float)
  DTTF_DT1_DT4_pts = numpy.zeros(1, dtype=float)
  DTTF_DT2_DT3_pts = numpy.zeros(1, dtype=float)
  DTTF_DT2_DT4_pts = numpy.zeros(1, dtype=float)
  DTTF_DT3_DT4_pts = numpy.zeros(1, dtype=float)

  DTTF_DT1_DT2_DT3_pts = numpy.zeros(1, dtype=float)
  DTTF_DT1_DT2_DT4_pts = numpy.zeros(1, dtype=float)
  DTTF_DT1_DT3_DT4_pts = numpy.zeros(1, dtype=float)
  DTTF_DT2_DT3_DT4_pts = numpy.zeros(1, dtype=float)

  DTTF_DT1_DT2_DT3_DT4_pts = numpy.zeros(1, dtype=float)

  ## branches
  t.Branch('gen_pt', gen_pts, 'gen_pt/D')
  t.Branch('gen_eta', gen_etas, 'gen_eta/D')
  t.Branch('gen_phi', gen_phis, 'gen_phi/D')
  t.Branch('gen_dxy', gen_dxys, 'gen_dxy/D')

  t.Branch('sim_pt', sim_pts, 'sim_pt/D')
  t.Branch('sim_eta', sim_etas, 'sim_eta/D')
  t.Branch('sim_phi', sim_phis, 'sim_phi/D')

  t.Branch('SIM_L1Mu_index', SIM_L1Mu_indexs, 'SIM_L1Mu_index/I')
  t.Branch('SIM_L1Mu_dR', SIM_L1Mu_dRs, 'SIM_L1Mu_dR/D')

  t.Branch('has_L1Mu', has_L1Mus, 'has_L1Mu/I')
  t.Branch('L1Mu_pt', L1Mu_pts, 'L1Mu_pt/D')
  t.Branch('L1Mu_eta', L1Mu_etas, 'L1Mu_eta/D')
  t.Branch('L1Mu_phi', L1Mu_phis, 'L1Mu_phi/D')
  t.Branch('L1Mu_quality', L1Mu_qualitys, 'L1Mu_quality/I')
  t.Branch('L1Mu_bx', L1Mu_bxs, 'L1Mu_bx/I')
  t.Branch('L1Mu_true', L1Mu_trues, 'L1Mu_true/I')

  t.Branch('has_CSCTF', has_CSCTFs, 'has_CSCTF/I')
  t.Branch('CSCTF_pt', CSCTF_pts, 'CSCTF_pt/D')
  t.Branch('CSCTF_eta', CSCTF_etas, 'CSCTF_eta/D')
  t.Branch('CSCTF_phi', CSCTF_phis, 'CSCTF_phi/D')
  t.Branch('CSCTF_quality', CSCTF_qualitys, 'CSCTF_quality/I')
  t.Branch('CSCTF_bx', CSCTF_bxs, 'CSCTF_bx/I')

  t.Branch('CSCTF_eta2', CSCTF_eta2s, 'CSCTF_eta2/D')
  t.Branch('CSCTF_sim_eta2', CSCTF_sim_eta2s, 'CSCTF_sim_eta2/D')

  t.Branch('ok_CSCTF_st1', ok_CSCTF_st1s, 'ok_CSCTF_st1/I')
  t.Branch('ok_CSCTF_st2', ok_CSCTF_st2s, 'ok_CSCTF_st2/I')
  t.Branch('ok_CSCTF_st3', ok_CSCTF_st3s, 'ok_CSCTF_st3/I')
  t.Branch('ok_CSCTF_st4', ok_CSCTF_st4s, 'ok_CSCTF_st4/I')

  t.Branch('ok_CSCTF_sim_st1', ok_CSCTF_sim_st1s, 'ok_CSCTF_sim_st1/I')
  t.Branch('ok_CSCTF_sim_st2', ok_CSCTF_sim_st2s, 'ok_CSCTF_sim_st2/I')
  t.Branch('ok_CSCTF_sim_st3', ok_CSCTF_sim_st3s, 'ok_CSCTF_sim_st3/I')
  t.Branch('ok_CSCTF_sim_st4', ok_CSCTF_sim_st4s, 'ok_CSCTF_sim_st4/I')


  t.Branch('CSCTF_phi1', CSCTF_phi1s, 'CSCTF_phi1/D')
  t.Branch('CSCTF_phi2', CSCTF_phi2s, 'CSCTF_phi2/D')
  t.Branch('CSCTF_phi3', CSCTF_phi3s, 'CSCTF_phi3/D')
  t.Branch('CSCTF_phi4', CSCTF_phi4s, 'CSCTF_phi4/D')

  t.Branch('CSCTF_sim_phi1', CSCTF_sim_phi1s, 'CSCTF_sim_phi1/D')
  t.Branch('CSCTF_sim_phi2', CSCTF_sim_phi2s, 'CSCTF_sim_phi2/D')
  t.Branch('CSCTF_sim_phi3', CSCTF_sim_phi3s, 'CSCTF_sim_phi3/D')
  t.Branch('CSCTF_sim_phi4', CSCTF_sim_phi4s, 'CSCTF_sim_phi4/D')

  t.Branch('CSCTF_eta1', CSCTF_eta1s, 'CSCTF_eta1/D')
  t.Branch('CSCTF_eta2', CSCTF_eta2s, 'CSCTF_eta2/D')
  t.Branch('CSCTF_eta3', CSCTF_eta3s, 'CSCTF_eta3/D')
  t.Branch('CSCTF_eta4', CSCTF_eta4s, 'CSCTF_eta4/D')

  t.Branch('CSCTF_sim_eta1', CSCTF_sim_eta1s, 'CSCTF_sim_eta1/D')
  t.Branch('CSCTF_sim_eta2', CSCTF_sim_eta2s, 'CSCTF_sim_eta2/D')
  t.Branch('CSCTF_sim_eta3', CSCTF_sim_eta3s, 'CSCTF_sim_eta3/D')
  t.Branch('CSCTF_sim_eta4', CSCTF_sim_eta4s, 'CSCTF_sim_eta4/D')

  t.Branch('CSCTF_z1', CSCTF_z1s, 'CSCTF_z1/D')
  t.Branch('CSCTF_z2', CSCTF_z2s, 'CSCTF_z2/D')
  t.Branch('CSCTF_z3', CSCTF_z3s, 'CSCTF_z3/D')
  t.Branch('CSCTF_z4', CSCTF_z4s, 'CSCTF_z4/D')

  t.Branch('CSCTF_sim_z1', CSCTF_sim_z1s, 'CSCTF_sim_z1/D')
  t.Branch('CSCTF_sim_z2', CSCTF_sim_z2s, 'CSCTF_sim_z2/D')
  t.Branch('CSCTF_sim_z3', CSCTF_sim_z3s, 'CSCTF_sim_z3/D')
  t.Branch('CSCTF_sim_z4', CSCTF_sim_z4s, 'CSCTF_sim_z4/D')

  t.Branch('CSCTF_ch1', CSCTF_ch1s, 'CSCTF_ch1/I')
  t.Branch('CSCTF_ch2', CSCTF_ch2s, 'CSCTF_ch2/I')
  t.Branch('CSCTF_ch3', CSCTF_ch3s, 'CSCTF_ch3/I')
  t.Branch('CSCTF_ch4', CSCTF_ch4s, 'CSCTF_ch4/I')

  t.Branch('CSCTF_sim_ch1', CSCTF_sim_ch1s, 'CSCTF_sim_ch1/I')
  t.Branch('CSCTF_sim_ch2', CSCTF_sim_ch2s, 'CSCTF_sim_ch2/I')
  t.Branch('CSCTF_sim_ch3', CSCTF_sim_ch3s, 'CSCTF_sim_ch3/I')
  t.Branch('CSCTF_sim_ch4', CSCTF_sim_ch4s, 'CSCTF_sim_ch4/I')

  t.Branch('CSCTF_isEven1', CSCTF_isEven1s, 'CSCTF_isEven1/I')
  t.Branch('CSCTF_isEven2', CSCTF_isEven2s, 'CSCTF_isEven2/I')
  t.Branch('CSCTF_isEven3', CSCTF_isEven3s, 'CSCTF_isEven3/I')
  t.Branch('CSCTF_isEven4', CSCTF_isEven4s, 'CSCTF_isEven4/I')

  t.Branch('CSCTF_sim_isEven1', CSCTF_sim_isEven1s, 'CSCTF_sim_isEven1/I')
  t.Branch('CSCTF_sim_isEven2', CSCTF_sim_isEven2s, 'CSCTF_sim_isEven2/I')
  t.Branch('CSCTF_sim_isEven3', CSCTF_sim_isEven3s, 'CSCTF_sim_isEven3/I')
  t.Branch('CSCTF_sim_isEven4', CSCTF_sim_isEven4s, 'CSCTF_sim_isEven4/I')

  t.Branch('parity_L1', paritys_L1, 'parity_L1/I')
  t.Branch('parity_sim', paritys_sim, 'parity_sim/I')
  t.Branch('partition_L1', partitions_L1, 'partition_L1/I')
  t.Branch('partition_sim', partitions_sim, 'partition_sim/I')

  t.Branch('DDY123_pt', DDY123_pts, 'DDY123_pt/D')
  t.Branch('DDY123_withLCTFit', DDY123_withLCTFits, 'DDY123_withLCTFit/D')
  t.Branch('DDY123_withoutLCTFit', DDY123_withoutLCTFits, 'DDY123_withoutLCTFit/D')

  t.Branch('CSCTF_sim_DDY123', CSCTF_sim_DDY123s, 'CSCTF_sim_DDY123/D')
  t.Branch('CSCTF_L1_DDY123', CSCTF_L1_DDY123s, 'CSCTF_L1_DDY123/D')

  t.Branch('CSCTF_sim_DPhi12_noGE21', CSCTF_sim_DPhi12_noGE21s, 'CSCTF_sim_DPhi12_noGE21/D')
  t.Branch('CSCTF_L1_DPhi12_noGE21', CSCTF_L1_DPhi12_noGE21s, 'CSCTF_L1_DPhi12_noGE21/D')
  t.Branch('CSCTF_sim_DPhi12_GE21', CSCTF_sim_DPhi12_GE21s, 'CSCTF_sim_DPhi12_GE21/D')
  t.Branch('CSCTF_L1_DPhi12_GE21', CSCTF_L1_DPhi12_GE21s, 'CSCTF_L1_DPhi12_GE21/D')

  t.Branch('CSCTF_sim_position_pt', CSCTF_sim_position_pts, 'CSCTF_sim_position_pt/D')
  t.Branch('CSCTF_L1_position_pt', CSCTF_L1_position_pts, 'CSCTF_L1_position_pt/D')

  t.Branch('CSCTF_sim_direction_pt_noGE21', CSCTF_sim_direction_pt_noGE21s, 'CSCTF_sim_direction_pt_noGE21/D')
  t.Branch('CSCTF_L1_direction_pt_noGE21', CSCTF_L1_direction_pt_noGE21s, 'CSCTF_L1_direction_pt_noGE21/D')
  t.Branch('CSCTF_sim_direction_pt_GE21', CSCTF_sim_direction_pt_GE21s, 'CSCTF_sim_direction_pt_GE21/D')
  t.Branch('CSCTF_L1_direction_pt_GE21', CSCTF_L1_direction_pt_GE21s, 'CSCTF_L1_direction_pt_GE21/D')

  t.Branch('CSCTF_sim_hybrid_pt_noGE21', CSCTF_sim_hybrid_pt_noGE21s, 'CSCTF_sim_hybrid_pt_noGE21/D')
  t.Branch('CSCTF_L1_hybrid_pt_noGE21', CSCTF_L1_hybrid_pt_noGE21s, 'CSCTF_L1_hybrid_pt_noGE21/D')
  t.Branch('CSCTF_sim_hybrid_pt_GE21', CSCTF_sim_hybrid_pt_GE21s, 'CSCTF_sim_hybrid_pt_GE21/D')
  t.Branch('CSCTF_L1_hybrid_pt_GE21', CSCTF_L1_hybrid_pt_GE21s, 'CSCTF_L1_hybrid_pt_GE21/D')

  t.Branch('CSCTF_sim_eta_st2', CSCTF_sim_eta_st2s, 'CSCTF_sim_eta_st2/D')
  t.Branch('CSCTF_L1_eta_st2', CSCTF_L1_eta_st2s, 'CSCTF_L1_eta_st2/D')

  ## isolation
  t.Branch('L1Mu_isLooseVeto', L1Mu_isLooseVetos, 'L1Mu_isLooseVeto/I')
  t.Branch('L1Mu_isMediumVeto', L1Mu_isMediumVetos, 'L1Mu_isMediumVeto/I')
  t.Branch('L1Mu_isTightVeto', L1Mu_isTightVetos, 'L1Mu_isTightVeto/I')

  ## GEM information
  t.Branch('ok_GE11_L1', ok_GE11_L1s, 'ok_GE11_L1/I')
  t.Branch('ok_GE11_L2', ok_GE11_L2s, 'ok_GE11_L2/I')
  t.Branch('ok_GE21_L1', ok_GE21_L1s, 'ok_GE21_L1/I')
  t.Branch('ok_GE21_L2', ok_GE21_L2s, 'ok_GE21_L2/I')

  t.Branch('ok_GE11_sim_L1', ok_GE11_sim_L1s, 'ok_GE11_sim_L1/I')
  t.Branch('ok_GE11_sim_L2', ok_GE11_sim_L2s, 'ok_GE11_sim_L2/I')
  t.Branch('ok_GE21_sim_L1', ok_GE21_sim_L1s, 'ok_GE21_sim_L1/I')
  t.Branch('ok_GE21_sim_L2', ok_GE21_sim_L2s, 'ok_GE21_sim_L2/I')

  t.Branch('GE11_L1_phi', GE11_L1_phis, 'GE11_L1_phi/D')
  t.Branch('GE11_L2_phi', GE11_L2_phis, 'GE11_L2_phi/D')
  t.Branch('GE21_L1_phi', GE21_L1_phis, 'GE21_L1_phi/D')
  t.Branch('GE21_L2_phi', GE21_L2_phis, 'GE21_L2_phi/D')

  t.Branch('GE11_sim_L1_phi', GE11_sim_L1_phis, 'GE11_sim_L1_phi/D')
  t.Branch('GE11_sim_L2_phi', GE11_sim_L2_phis, 'GE11_sim_L2_phi/D')
  t.Branch('GE21_sim_L1_phi', GE21_sim_L1_phis, 'GE21_sim_L1_phi/D')
  t.Branch('GE21_sim_L2_phi', GE21_sim_L2_phis, 'GE21_sim_L2_phi/D')

  t.Branch('GE11_L1_bx', GE11_L1_bxs, 'GE11_L1_bx/I')
  t.Branch('GE11_L2_bx', GE11_L2_bxs, 'GE11_L2_bx/I')
  t.Branch('GE21_L1_bx', GE21_L1_bxs, 'GE21_L1_bx/I')
  t.Branch('GE21_L2_bx', GE21_L2_bxs, 'GE21_L2_bx/I')

  t.Branch('GE11_sim_L1_bx', GE11_sim_L1_bxs, 'GE11_sim_L1_bx/I')
  t.Branch('GE11_sim_L2_bx', GE11_sim_L2_bxs, 'GE11_sim_L2_bx/I')
  t.Branch('GE21_sim_L1_bx', GE21_sim_L1_bxs, 'GE21_sim_L1_bx/I')
  t.Branch('GE21_sim_L2_bx', GE21_sim_L2_bxs, 'GE21_sim_L2_bx/I')

  t.Branch('GE11_L1_z', GE11_L1_zs, 'GE11_L1_z/D')
  t.Branch('GE11_L2_z', GE11_L2_zs, 'GE11_L2_z/D')
  t.Branch('GE21_L1_z', GE21_L1_zs, 'GE21_L1_z/D')
  t.Branch('GE21_L2_z', GE21_L2_zs, 'GE21_L2_z/D')

  t.Branch('GE11_sim_L1_z', GE11_sim_L1_zs, 'GE11_sim_L1_z/D')
  t.Branch('GE11_sim_L2_z', GE11_sim_L2_zs, 'GE11_sim_L2_z/D')
  t.Branch('GE21_sim_L1_z', GE21_sim_L1_zs, 'GE21_sim_L1_z/D')
  t.Branch('GE21_sim_L2_z', GE21_sim_L2_zs, 'GE21_sim_L2_z/D')


  t.Branch('has_DTTF', has_DTTFs, 'has_DTTF/I')
  t.Branch('DTTF_pt', DTTF_pts, 'DTTF_pt/D')
  t.Branch('DTTF_eta', DTTF_etas, 'DTTF_eta/D')
  t.Branch('DTTF_phi', DTTF_phis, 'DTTF_phi/D')
  t.Branch('DTTF_quality', DTTF_qualitys, 'DTTF_quality/I')
  t.Branch('DTTF_bx', DTTF_bxs, 'DTTF_bx/I')

  t.Branch('ok_DTTF_st1', ok_DTTF_st1s, 'ok_DTTF_st1/I')
  t.Branch('ok_DTTF_st2', ok_DTTF_st2s, 'ok_DTTF_st2/I')
  t.Branch('ok_DTTF_st3', ok_DTTF_st3s, 'ok_DTTF_st3/I')
  t.Branch('ok_DTTF_st4', ok_DTTF_st4s, 'ok_DTTF_st4/I')

  t.Branch('DTTF_phi1', DTTF_phi1s, 'DTTF_phi1/D')
  t.Branch('DTTF_phi2', DTTF_phi2s, 'DTTF_phi2/D')
  t.Branch('DTTF_phi3', DTTF_phi3s, 'DTTF_phi3/D')
  t.Branch('DTTF_phi4', DTTF_phi4s, 'DTTF_phi4/D')

  t.Branch('DTTF_phib1', DTTF_phib1s, 'DTTF_phib1/D')
  t.Branch('DTTF_phib2', DTTF_phib2s, 'DTTF_phib2/D')
  t.Branch('DTTF_phib3', DTTF_phib3s, 'DTTF_phib3/D')
  t.Branch('DTTF_phib4', DTTF_phib4s, 'DTTF_phib4/D')

  t.Branch('DTTF_phib1_phib2', DTTF_phib1_phib2s, 'DTTF_phib1_phib2/D')
  t.Branch('DTTF_phib1_phib3', DTTF_phib1_phib3s, 'DTTF_phib1_phib3/D')
  t.Branch('DTTF_phib1_phib4', DTTF_phib1_phib4s, 'DTTF_phib1_phib4/D')
  t.Branch('DTTF_phib2_phib3', DTTF_phib2_phib3s, 'DTTF_phib2_phib3/D')
  t.Branch('DTTF_phib2_phib4', DTTF_phib2_phib4s, 'DTTF_phib2_phib4/D')
  t.Branch('DTTF_phib3_phib4', DTTF_phib3_phib4s, 'DTTF_phib3_phib4/D')

  t.Branch('abs_DTTF_phib1_phib2', abs_DTTF_phib1_phib2s, 'abs_DTTF_phib1_phib2/D')
  t.Branch('abs_DTTF_phib1_phib3', abs_DTTF_phib1_phib3s, 'abs_DTTF_phib1_phib3/D')
  t.Branch('abs_DTTF_phib1_phib4', abs_DTTF_phib1_phib4s, 'abs_DTTF_phib1_phib4/D')
  t.Branch('abs_DTTF_phib2_phib3', abs_DTTF_phib2_phib3s, 'abs_DTTF_phib2_phib3/D')
  t.Branch('abs_DTTF_phib2_phib4', abs_DTTF_phib2_phib4s, 'abs_DTTF_phib2_phib4/D')
  t.Branch('abs_DTTF_phib3_phib4', abs_DTTF_phib3_phib4s, 'abs_DTTF_phib3_phib4/D')

  t.Branch('DTTF_DT1_DT2_pt', DTTF_DT1_DT2_pts, 'DTTF_DT1_DT2_pt/D')
  t.Branch('DTTF_DT1_DT3_pt', DTTF_DT1_DT3_pts, 'DTTF_DT1_DT3_pt/D')
  t.Branch('DTTF_DT1_DT4_pt', DTTF_DT1_DT4_pts, 'DTTF_DT1_DT4_pt/D')
  t.Branch('DTTF_DT2_DT3_pt', DTTF_DT2_DT3_pts, 'DTTF_DT2_DT3_pt/D')
  t.Branch('DTTF_DT2_DT4_pt', DTTF_DT2_DT4_pts, 'DTTF_DT2_DT4_pt/D')
  t.Branch('DTTF_DT3_DT4_pt', DTTF_DT3_DT4_pts, 'DTTF_DT3_DT4_pt/D')

  t.Branch('DTTF_DT1_DT2_DT3_pt', DTTF_DT1_DT2_DT3_pts, 'DTTF_DT1_DT2_DT3_pt/D')
  t.Branch('DTTF_DT1_DT2_DT4_pt', DTTF_DT1_DT2_DT4_pts, 'DTTF_DT1_DT2_DT4_pt/D')
  t.Branch('DTTF_DT1_DT3_DT4_pt', DTTF_DT1_DT3_DT4_pts, 'DTTF_DT1_DT3_DT4_pt/D')
  t.Branch('DTTF_DT2_DT3_DT4_pt', DTTF_DT2_DT3_DT4_pts, 'DTTF_DT2_DT3_DT4_pt/D')

  t.Branch('DTTF_DT1_DT2_DT3_DT4_pt', DTTF_DT1_DT2_DT3_DT4_pts, 'DTTF_DT1_DT2_DT3_DT4_pt/D')


  print "Start run on", treeHits.GetEntries(), "events."
  for k in range(0,treeHits.GetEntries()):
      treeHits.GetEntry(k)
      if k%1000==0: print "Event", k+1, "nL1Mu", treeHits.nL1Mu
      #if k>100000: break

      #print "event_number", event_number
      #print "lumi_number", lumi_number
      #print "run_number", run_number

      for i in range(0,2):

        for j in range(0,2):
          ij = i*2+j

          pt = abs(treeHits.genGdMu_pt[ij])
          #eta = treeHits.genGdMu_eta[ij]
          #phi = abs(treeHits.genGdMu_phi[ij])
          charge = treeHits.genGdMu_q[ij]
          eta_prop = treeHits.genGdMu_eta_prop[ij]
          phi_prop = treeHits.genGdMu_phi_prop[ij]
          dxy = abs(treeHits.genGdMu_dxy[ij])
          vz = abs(treeHits.genGd_vz[i])
          lxy =  abs(treeHits.genGd_lxy[i])
          #SIM_index = treeHits.genGdMu_SIM_index[ij]
          #SIM_dR = treeHits.genGdMu_SIM_dR[ij]

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
          if abs(eta_prop)<0:
            continue
          if pt<0:
            continue

          gen_pts[0] = treeHits.genGdMu_pt[ij]
          gen_etas[0] = treeHits.genGdMu_eta_prop[ij]
          gen_phis[0] = treeHits.genGdMu_phi_prop[ij]
          gen_dxys[0] = treeHits.genGdMu_dxy[ij]

          if verbose: print "Muon", gen_pts[0], gen_etas[0], gen_phis[0], gen_phis[0], gen_dxys[0]

          sim_index = treeHits.genGdMu_SIM_index[ij]
          if verbose: print "sim_index", sim_index

          L1Mu_index = treeHits.genGdMu_L1Mu_index_prop[ij]
          L1Mu_dR_prop = treeHits.genGdMu_L1Mu_dR_prop[ij]

          has_sim = sim_index != -99
          has_L1Mus[0] = L1Mu_index != -99 and L1Mu_dR_prop < 0.2

          if not has_sim:
            if verbose: print "ERROR, no SIM"
            continue
          if not has_L1Mus[0]:
            if verbose: print "ERROR, no L1Mu"
            continue
          if sim_index>3:
            continue

          #print "sim_index", sim_index
          sim_pts[0] = treeHits.pt_sim[sim_index]
          sim_etas[0] = treeHits.eta_sim[sim_index]
          if verbose: print "sim_pt", sim_pts[0]

          #if abs(float(gen_pts[0]) - float(sim_pts[0])) > 0.01:
          #  print "Error, different gen-sim pt", gen_pts[0], sim_pts[0]

          L1Mu_pts[0] = -99
          L1Mu_etas[0] = -99
          L1Mu_phis[0] = -99
          L1Mu_qualitys[0] = -99
          L1Mu_bxs[0] = -99
          L1Mu_trues[0] = 0

          has_CSCTFs[0] = 0

          CSCTF_pts[0] = -99
          CSCTF_etas[0] = -99
          CSCTF_phis[0] = -99
          CSCTF_qualitys[0] = -99
          CSCTF_bxs[0] = -99

          ok_CSCTF_st1s[0] = 0
          ok_CSCTF_st2s[0] = 0
          ok_CSCTF_st3s[0] = 0
          ok_CSCTF_st4s[0] = 0

          ok_CSCTF_sim_st1s[0] = 0
          ok_CSCTF_sim_st2s[0] = 0
          ok_CSCTF_sim_st3s[0] = 0
          ok_CSCTF_sim_st4s[0] = 0

          CSCTF_phi1s[0] = -99
          CSCTF_phi2s[0] = -99
          CSCTF_phi3s[0] = -99
          CSCTF_phi4s[0] = -99

          CSCTF_sim_phi1s[0] = -99
          CSCTF_sim_phi2s[0] = -99
          CSCTF_sim_phi3s[0] = -99
          CSCTF_sim_phi4s[0] = -99

          CSCTF_eta1s[0] = -99
          CSCTF_eta2s[0] = -99
          CSCTF_eta3s[0] = -99
          CSCTF_eta4s[0] = -99

          CSCTF_sim_eta1s[0] = -99
          CSCTF_sim_eta2s[0] = -99
          CSCTF_sim_eta3s[0] = -99
          CSCTF_sim_eta4s[0] = -99

          CSCTF_z1s[0] = -99
          CSCTF_z2s[0] = -99
          CSCTF_z3s[0] = -99
          CSCTF_z4s[0] = -99

          CSCTF_sim_z1s[0] = -99
          CSCTF_sim_z2s[0] = -99
          CSCTF_sim_z3s[0] = -99
          CSCTF_sim_z4s[0] = -99

          CSCTF_ch1s[0] = -99
          CSCTF_ch2s[0] = -99
          CSCTF_ch3s[0] = -99
          CSCTF_ch4s[0] = -99

          CSCTF_sim_ch1s[0] = -99
          CSCTF_sim_ch2s[0] = -99
          CSCTF_sim_ch3s[0] = -99
          CSCTF_sim_ch4s[0] = -99

          CSCTF_isEven1s[0] = -99
          CSCTF_isEven2s[0] = -99
          CSCTF_isEven3s[0] = -99
          CSCTF_isEven4s[0] = -99

          CSCTF_sim_isEven1s[0] = -99
          CSCTF_sim_isEven2s[0] = -99
          CSCTF_sim_isEven3s[0] = -99
          CSCTF_sim_isEven4s[0] = -99

          DDY123_pts[0] = 0
          DDY123_withoutLCTFits[0] = -1
          DDY123_withLCTFits[0] = -1

          CSCTF_sim_DDY123s[0] = 99
          CSCTF_L1_DDY123s[0] = 99

          CSCTF_sim_DPhi12_noGE21s[0] = 99
          CSCTF_L1_DPhi12_noGE21s[0] = 99
          CSCTF_sim_DPhi12_GE21s[0] = 99
          CSCTF_L1_DPhi12_GE21s[0] = 99

          CSCTF_sim_position_pts[0] = 0
          CSCTF_L1_position_pts[0] = 0

          CSCTF_sim_direction_pt_noGE21s[0] = 0
          CSCTF_L1_direction_pt_noGE21s[0] = 0
          CSCTF_sim_direction_pt_GE21s[0] = 0
          CSCTF_L1_direction_pt_GE21s[0] = 0

          CSCTF_sim_hybrid_pt_noGE21s[0] = 0
          CSCTF_L1_hybrid_pt_noGE21s[0] = 0
          CSCTF_sim_hybrid_pt_GE21s[0] = 0
          CSCTF_L1_hybrid_pt_GE21s[0] = 0

          CSCTF_sim_eta_st2s[0] = 99
          CSCTF_L1_eta_st2s[0] = 99

          L1Mu_isLooseVetos[0] = 0
          L1Mu_isMediumVetos[0] = 0
          L1Mu_isTightVetos[0] = 0

          ok_GE11_L1s[0] = 0
          ok_GE11_L2s[0] = 0
          ok_GE21_L1s[0] = 0
          ok_GE21_L2s[0] = 0

          ok_GE11_sim_L1s[0] = 0
          ok_GE11_sim_L2s[0] = 0
          ok_GE21_sim_L1s[0] = 0
          ok_GE21_sim_L2s[0] = 0


          GE11_L1_phis[0] = -99
          GE11_L2_phis[0] = -99
          GE21_L1_phis[0] = -99
          GE21_L2_phis[0] = -99

          GE11_sim_L1_phis[0] = -99
          GE11_sim_L2_phis[0] = -99
          GE21_sim_L1_phis[0] = -99
          GE21_sim_L2_phis[0] = -99

          GE11_L1_bxs[0] = 99
          GE11_L2_bxs[0] = 99
          GE21_L1_bxs[0] = 99
          GE21_L2_bxs[0] = 99

          GE11_sim_L1_bxs[0] = 99
          GE11_sim_L2_bxs[0] = 99
          GE21_sim_L1_bxs[0] = 99
          GE21_sim_L2_bxs[0] = 99

          GE11_L1_zs[0] = -9999
          GE11_L2_zs[0] = -9999
          GE21_L1_zs[0] = -9999
          GE21_L2_zs[0] = -9999

          GE11_sim_L1_zs[0] = -9999
          GE11_sim_L2_zs[0] = -9999
          GE21_sim_L1_zs[0] = -9999
          GE21_sim_L2_zs[0] = -9999


          paritys_L1[0] = 99
          paritys_sim[0] = 99
          partitions_L1[0] = 99
          partitions_sim[0] = 99

          has_DTTFs[0] = 0

          DTTF_pts[0] = -99
          DTTF_etas[0] = -99
          DTTF_phis[0] = -99
          DTTF_qualitys[0] = -99
          DTTF_bxs[0] = -99

          CSCTF_sim_phi1s[0] = treeHits.CSCTF_rec_phi1[sim_index]
          CSCTF_sim_phi2s[0] = treeHits.CSCTF_rec_phi2[sim_index]
          CSCTF_sim_phi3s[0] = treeHits.CSCTF_rec_phi3[sim_index]
          CSCTF_sim_phi4s[0] = treeHits.CSCTF_rec_phi4[sim_index]

          ok_CSCTF_sim_st1s[0] = int(CSCTF_sim_phi1s[0] != -99)
          ok_CSCTF_sim_st2s[0] = int(CSCTF_sim_phi2s[0] != -99)
          ok_CSCTF_sim_st3s[0] = int(CSCTF_sim_phi3s[0] != -99)
          ok_CSCTF_sim_st4s[0] = int(CSCTF_sim_phi4s[0] != -99)

          CSCTF_sim_eta1s[0] = treeHits.CSCTF_rec_eta1[sim_index]
          CSCTF_sim_eta2s[0] = treeHits.CSCTF_rec_eta2[sim_index]
          CSCTF_sim_eta3s[0] = treeHits.CSCTF_rec_eta3[sim_index]
          CSCTF_sim_eta4s[0] = treeHits.CSCTF_rec_eta4[sim_index]

          CSCTF_sim_z1s[0] = treeHits.CSCTF_rec_z1[sim_index]
          CSCTF_sim_z2s[0] = treeHits.CSCTF_rec_z2[sim_index]
          CSCTF_sim_z3s[0] = treeHits.CSCTF_rec_z3[sim_index]
          CSCTF_sim_z4s[0] = treeHits.CSCTF_rec_z4[sim_index]

          CSCTF_sim_ch1s[0] = treeHits.CSCTF_rec_ch1[sim_index]
          CSCTF_sim_ch2s[0] = treeHits.CSCTF_rec_ch2[sim_index]
          CSCTF_sim_ch3s[0] = treeHits.CSCTF_rec_ch3[sim_index]
          CSCTF_sim_ch4s[0] = treeHits.CSCTF_rec_ch4[sim_index]

          CSCTF_sim_isEven1s[0] = CSCTF_sim_ch1s[0]%2==0
          CSCTF_sim_isEven2s[0] = CSCTF_sim_ch2s[0]%2==0
          CSCTF_sim_isEven3s[0] = CSCTF_sim_ch3s[0]%2==0
          CSCTF_sim_isEven4s[0] = CSCTF_sim_ch4s[0]%2==0


          ## GEM information
          GE11_sim_L1_phis[0] = treeHits.GE11_sim_pad_phi_L1[sim_index]
          GE11_sim_L2_phis[0] = treeHits.GE11_sim_pad_phi_L2[sim_index]
          GE21_sim_L1_phis[0] = treeHits.GE21_sim_pad_phi_L1[sim_index]
          GE21_sim_L2_phis[0] = treeHits.GE21_sim_pad_phi_L2[sim_index]

          GE11_sim_L1_bxs[0] = treeHits.GE11_sim_pad_bx_L1[sim_index]
          GE11_sim_L2_bxs[0] = treeHits.GE11_sim_pad_bx_L2[sim_index]
          GE21_sim_L1_bxs[0] = treeHits.GE21_sim_pad_bx_L1[sim_index]
          GE21_sim_L2_bxs[0] = treeHits.GE21_sim_pad_bx_L2[sim_index]

          GE11_sim_L1_zs[0] = treeHits.GE11_sim_z_L1[sim_index]
          GE11_sim_L2_zs[0] = treeHits.GE11_sim_z_L2[sim_index]
          GE21_sim_L1_zs[0] = treeHits.GE21_sim_z_L1[sim_index]
          GE21_sim_L2_zs[0] = treeHits.GE21_sim_z_L2[sim_index]

          ok_GE11_sim_L1s[0] = int(GE11_sim_L1_phis[0] != 99)
          ok_GE11_sim_L2s[0] = int(GE11_sim_L2_phis[0] != 99)
          ok_GE21_sim_L1s[0] = int(GE21_sim_L1_phis[0] != 99)
          ok_GE21_sim_L2s[0] = int(GE21_sim_L2_phis[0] != 99)

          ## DT information

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

          DTTF_DT1_DT2_DT3_pts[0] = -99
          DTTF_DT1_DT2_DT4_pts[0] = -99
          DTTF_DT1_DT3_DT4_pts[0] = -99
          DTTF_DT2_DT3_DT4_pts[0] = -99
          
          DTTF_DT1_DT2_DT3_DT4_pts[0] = -99

          ## check if it's a DT muon
          L1Mu_DTTF_index  = treeHits.L1Mu_DTTF_index[L1Mu_index]
          if L1Mu_DTTF_index  != 99 and L1Mu_DTTF_index  != -1:

            L1Mu_pts[0] = treeHits.L1Mu_pt[L1Mu_index]
            L1Mu_etas[0] = treeHits.L1Mu_eta[L1Mu_index]
            L1Mu_phis[0] = treeHits.L1Mu_phi[L1Mu_index]
            L1Mu_bxs[0] = treeHits.L1Mu_bx[L1Mu_index]
            L1Mu_qualitys[0] = treeHits.L1Mu_quality[L1Mu_index]

            L1Mu_L1Tk_dR_prop = treeHits.L1Mu_L1Tk_dR_prop[L1Mu_index]
            L1Mu_L1Tk_pt_prop = treeHits.L1Mu_L1Tk_pt_prop[L1Mu_index]
            L1Mu_L1Tk_dR_min = treeHits.L1Mu_L1Tk_dR_prop[L1Mu_index]
            L1Mu_L1Tk_pt = treeHits.L1Mu_L1Tk_pt_prop[L1Mu_index]

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

            DTTF_DT1_DT2_DT3_pts[0] = pt_from_DPhi_DT_ellipse(1,2, 1,3, DTTF_phib1_phib2s[0], DTTF_phib1_phib3s[0])
            DTTF_DT1_DT2_DT4_pts[0] = pt_from_DPhi_DT_ellipse(1,2, 1,4, DTTF_phib1_phib2s[0], DTTF_phib1_phib4s[0])
            DTTF_DT1_DT3_DT4_pts[0] = pt_from_DPhi_DT_ellipse(1,3, 1,4, DTTF_phib1_phib3s[0], DTTF_phib1_phib4s[0])
            DTTF_DT2_DT3_DT4_pts[0] = pt_from_DPhi_DT_ellipse(2,3, 2,4, DTTF_phib2_phib3s[0], DTTF_phib2_phib4s[0])
          
            DTTF_DT1_DT2_DT3_DT4_pts[0] = pt_from_DPhi_DT_ellipse(1,4, 2,3, DTTF_phib1_phib4s[0], DTTF_phib2_phib3s[0])


            #print DTTF_DT1_DT2_pts[0], DTTF_DT1_DT3_pts[0], DTTF_DT1_DT4_pts[0]
            #print

            if L1Mu_L1Tk_dR_min <= 0.12 and L1Mu_L1Tk_pt >= 4:
              L1Mu_isLooseVetos[0] = 1

            if L1Mu_L1Tk_dR_min <= 0.12 and L1Mu_L1Tk_pt >= 3:
              L1Mu_isMediumVetos[0] = 1

            if L1Mu_L1Tk_dR_min <= 0.12 and L1Mu_L1Tk_pt >= 2:
              L1Mu_isTightVetos[0] = 1

          t.Fill()
          continue


          if verbose and False:
            print "\t\tGE11_sim_L1_phis", GE11_sim_pad_L1_phis[0]
            print "\t\tGE11_sim_L2_phis", GE11_sim_pad_L2_phis[0]
            print "\t\tGE21_sim_L1_phis", GE21_sim_pad_L1_phis[0]
            print "\t\tGE21_sim_L2_phis", GE21_sim_pad_L2_phis[0]
            print

          #print ok_CSCTF_sim_st1s[0], ok_CSCTF_sim_st2s[0], ok_CSCTF_sim_st3s[0], ok_CSCTF_sim_st4s[0]

          ## find the L1Mu closest matching to the
          deltaRMin = 999
          SIM_L1Mu_index = 999
          for iii in range(0,len(treeHits.L1Mu_pt)):
            #print "Checking muon" , iii
            L1Mu_CSCTF_index = treeHits.L1Mu_CSCTF_index[iii]
            #print "CSCTF index", L1Mu_CSCTF_index, "max", len(treeHits.CSCTF_phi1)
            if L1Mu_CSCTF_index == -1:
              #print "\tNot an endcap muon. Skipping...\n"
              continue
            CSCTF_phi1 = treeHits.CSCTF_phi1[L1Mu_CSCTF_index]
            CSCTF_phi2 = treeHits.CSCTF_phi2[L1Mu_CSCTF_index]
            CSCTF_phi3 = treeHits.CSCTF_phi3[L1Mu_CSCTF_index]
            CSCTF_phi4 = treeHits.CSCTF_phi4[L1Mu_CSCTF_index]

            CSCTF_eta1 = treeHits.CSCTF_eta1[L1Mu_CSCTF_index]
            CSCTF_eta2 = treeHits.CSCTF_eta2[L1Mu_CSCTF_index]
            CSCTF_eta3 = treeHits.CSCTF_eta3[L1Mu_CSCTF_index]
            CSCTF_eta4 = treeHits.CSCTF_eta4[L1Mu_CSCTF_index]

            deltaEta1 = abs(CSCTF_sim_eta1s[0]-CSCTF_eta1)
            deltaEta2 = abs(CSCTF_sim_eta2s[0]-CSCTF_eta2)
            deltaEta3 = abs(CSCTF_sim_eta3s[0]-CSCTF_eta3)
            deltaEta4 = abs(CSCTF_sim_eta4s[0]-CSCTF_eta4)

            deltaPhi1 = abs(deltaPhi(CSCTF_sim_phi1s[0], CSCTF_phi1))
            deltaPhi2 = abs(deltaPhi(CSCTF_sim_phi2s[0], CSCTF_phi2))
            deltaPhi3 = abs(deltaPhi(CSCTF_sim_phi3s[0], CSCTF_phi3))
            deltaPhi4 = abs(deltaPhi(CSCTF_sim_phi4s[0], CSCTF_phi4))

            ## sanity check
            if CSCTF_sim_eta1s[0] == 99. or CSCTF_eta1 == 99.: deltaEta1 = 99.
            if CSCTF_sim_eta2s[0] == 99. or CSCTF_eta2 == 99.: deltaEta2 = 99.
            if CSCTF_sim_eta3s[0] == 99. or CSCTF_eta3 == 99.: deltaEta3 = 99.
            if CSCTF_sim_eta4s[0] == 99. or CSCTF_eta4 == 99.: deltaEta4 = 99.

            if CSCTF_sim_phi1s[0] == 99. or CSCTF_phi1 == 99.: deltaPhi1 = 99.
            if CSCTF_sim_phi2s[0] == 99. or CSCTF_phi2 == 99.: deltaPhi2 = 99.
            if CSCTF_sim_phi3s[0] == 99. or CSCTF_phi3 == 99.: deltaPhi3 = 99.
            if CSCTF_sim_phi4s[0] == 99. or CSCTF_phi4 == 99.: deltaPhi4 = 99.

            deltaR1 = deltaEta1*deltaEta1 + deltaPhi1*deltaPhi1
            deltaR2 = deltaEta2*deltaEta2 + deltaPhi2*deltaPhi2
            deltaR3 = deltaEta3*deltaEta3 + deltaPhi3*deltaPhi3
            deltaR4 = deltaEta4*deltaEta4 + deltaPhi4*deltaPhi4

            ## sanity check
            if deltaEta1 == 99. or deltaPhi1 == 99.: deltaR1 = 99.
            if deltaEta2 == 99. or deltaPhi2 == 99.: deltaR2 = 99.
            if deltaEta3 == 99. or deltaPhi3 == 99.: deltaR3 = 99.
            if deltaEta4 == 99. or deltaPhi4 == 99.: deltaR4 = 99.

            if verbose or False:
              print "\t\tCSCTF_sim_phi1", CSCTF_sim_phi1s[0], "\tCSCTF_phi1", CSCTF_phi1, "Delta", deltaPhi1
              print "\t\tCSCTF_sim_phi2", CSCTF_sim_phi2s[0], "\tCSCTF_phi2", CSCTF_phi2, "Delta", deltaPhi2
              print "\t\tCSCTF_sim_phi3", CSCTF_sim_phi3s[0], "\tCSCTF_phi3", CSCTF_phi3, "Delta", deltaPhi3
              print "\t\tCSCTF_sim_phi4", CSCTF_sim_phi4s[0], "\tCSCTF_phi4", CSCTF_phi4, "Delta", deltaPhi4
              print

              print "\t\tCSCTF_sim_eta1", CSCTF_sim_eta1s[0], "\tCSCTF_eta1", CSCTF_eta1, "Delta", deltaEta1
              print "\t\tCSCTF_sim_eta2", CSCTF_sim_eta2s[0], "\tCSCTF_eta2", CSCTF_eta2, "Delta", deltaEta2
              print "\t\tCSCTF_sim_eta3", CSCTF_sim_eta3s[0], "\tCSCTF_eta3", CSCTF_eta3, "Delta", deltaEta3
              print "\t\tCSCTF_sim_eta4", CSCTF_sim_eta4s[0], "\tCSCTF_eta4", CSCTF_eta4, "Delta", deltaEta4
              print

              print "deltaR1", deltaR1
              print "deltaR2", deltaR2
              print "deltaR3", deltaR3
              print "deltaR4", deltaR4

            deltaR = 0
            if deltaR1 != 99.: deltaR += deltaR1
            if deltaR2 != 99.: deltaR += deltaR2
            if deltaR3 != 99.: deltaR += deltaR3
            if deltaR4 != 99.: deltaR += deltaR4
            if deltaR1 == 99 and deltaR2 == 99 and deltaR3 == 99 and deltaR4 == 99: deltaR = 9999

            #print "phi values", treeHits.L1Mu_phi[iii], treeHits.CSCTF_rec_phi2[sim_index]
            #print "deltaEta", deltaEta, "deltaPhi", deltaPhi
            #print "sim", iii, deltaR
            if deltaR < deltaRMin:
              SIM_L1Mu_index = iii
              deltaRMin = deltaR
          #print "found index", SIM_L1Mu_index, "deltaRMin", deltaRMin, "L1Mu index", L1Mu_index
          #print
          SIM_L1Mu_indexs[0] = SIM_L1Mu_index
          SIM_L1Mu_dRs[0] = deltaRMin

          if SIM_L1Mu_index == L1Mu_index:
            L1Mu_trues[0] = 1
          else:
            pass
            """
            print
            print "ERROR: SIM_L1Mu_index", SIM_L1Mu_index, "deltaRMin", deltaRMin, "L1Mu_index", L1Mu_index
            print "L1Mu_index    : ", treeHits.L1Mu_pt[L1Mu_index], treeHits.L1Mu_eta[L1Mu_index], treeHits.L1Mu_phi[L1Mu_index], treeHits.L1Mu_bx[L1Mu_index]
            if SIM_L1Mu_index != 999:
              print "SIM_L1Mu_index: ", treeHits.L1Mu_pt[SIM_L1Mu_index], treeHits.L1Mu_eta[SIM_L1Mu_index], treeHits.L1Mu_phi[SIM_L1Mu_index], treeHits.L1Mu_bx[SIM_L1Mu_index]

              print "\t\tCSCTF_sim_phi1", CSCTF_sim_phi1s[0], "\tCSCTF_phi1", treeHits.CSCTF_phi1[SIM_L1Mu_index], treeHits.CSCTF_phi1[L1Mu_index]
              print "\t\tCSCTF_sim_phi2", CSCTF_sim_phi2s[0], "\tCSCTF_phi2", treeHits.CSCTF_phi2[SIM_L1Mu_index], treeHits.CSCTF_phi2[L1Mu_index]
              print "\t\tCSCTF_sim_phi3", CSCTF_sim_phi3s[0], "\tCSCTF_phi3", treeHits.CSCTF_phi3[SIM_L1Mu_index], treeHits.CSCTF_phi3[L1Mu_index]
              print "\t\tCSCTF_sim_phi4", CSCTF_sim_phi4s[0], "\tCSCTF_phi4", treeHits.CSCTF_phi4[SIM_L1Mu_index], treeHits.CSCTF_phi4[L1Mu_index]
              print

              print "\t\tCSCTF_sim_eta1", CSCTF_sim_eta1s[0], "\tCSCTF_eta1", treeHits.CSCTF_eta1[SIM_L1Mu_index], treeHits.CSCTF_eta1[L1Mu_index]
              print "\t\tCSCTF_sim_eta2", CSCTF_sim_eta2s[0], "\tCSCTF_eta2", treeHits.CSCTF_eta2[SIM_L1Mu_index], treeHits.CSCTF_eta2[L1Mu_index]
              print "\t\tCSCTF_sim_eta3", CSCTF_sim_eta3s[0], "\tCSCTF_eta3", treeHits.CSCTF_eta3[SIM_L1Mu_index], treeHits.CSCTF_eta3[L1Mu_index]
              print "\t\tCSCTF_sim_eta4", CSCTF_sim_eta4s[0], "\tCSCTF_eta4", treeHits.CSCTF_eta4[SIM_L1Mu_index], treeHits.CSCTF_eta4[L1Mu_index]
              print
            """

          ## matching L1Mu was not found
          if SIM_L1Mu_index == 999:
            continue

          L1Mu_pts[0] = treeHits.L1Mu_pt[SIM_L1Mu_index]
          L1Mu_etas[0] = treeHits.L1Mu_eta[SIM_L1Mu_index]
          L1Mu_phis[0] = treeHits.L1Mu_phi[SIM_L1Mu_index]
          L1Mu_bxs[0] = treeHits.L1Mu_bx[SIM_L1Mu_index]
          L1Mu_qualitys[0] = treeHits.L1Mu_quality[SIM_L1Mu_index]

          L1Mu_DTTF_index  = treeHits.L1Mu_DTTF_index[SIM_L1Mu_index]
          L1Mu_CSCTF_index = treeHits.L1Mu_CSCTF_index[SIM_L1Mu_index]

          has_CSCTFs[0] = L1Mu_CSCTF_index != 99 and L1Mu_CSCTF_index != -1
          has_DTTFs[0]  = L1Mu_DTTF_index  != 99 and L1Mu_DTTF_index  != -1


          CSCTF_sim_DDY123s[0] = treeHits.CSCTF_sim_DDY123[sim_index]
          CSCTF_L1_DDY123s[0] = treeHits.CSCTF_L1_DDY123[L1Mu_CSCTF_index]
          if verbose: print "CSCTF_sim_DDY123s[0]", CSCTF_sim_DDY123s[0]
          if verbose: print "CSCTF_L1_DDY123s[0]", CSCTF_L1_DDY123s[0]

          CSCTF_sim_DPhi12_noGE21s[0] = treeHits.CSCTF_sim_DPhi12_noGE21[sim_index]
          CSCTF_L1_DPhi12_noGE21s[0] = treeHits.CSCTF_L1_DPhi12_noGE21[L1Mu_CSCTF_index]
          if verbose: print "CSCTF_sim_DPhi12_noGE21s[0]", CSCTF_sim_DPhi12_noGE21s[0]
          if verbose: print "CSCTF_L1_DPhi12_noGE21s[0]", CSCTF_L1_DPhi12_noGE21s[0]

          CSCTF_sim_DPhi12_GE21s[0] = treeHits.CSCTF_sim_DPhi12_GE21[sim_index]
          CSCTF_L1_DPhi12_GE21s[0] = treeHits.CSCTF_L1_DPhi12_GE21[L1Mu_CSCTF_index]
          if verbose: print "CSCTF_sim_DPhi12_GE21s[0]", CSCTF_sim_DPhi12_GE21s[0]
          if verbose: print "CSCTF_L1_DPhi12_GE21s[0]", CSCTF_L1_DPhi12_GE21s[0]


          CSCTF_sim_position_pts[0] = treeHits.CSCTF_sim_position_pt[sim_index]
          CSCTF_L1_position_pts[0] = treeHits.CSCTF_L1_position_pt[L1Mu_CSCTF_index]
          if verbose: print "CSCTF_sim_position_pts[0]", CSCTF_sim_position_pts[0]
          if verbose: print "CSCTF_L1_position_pts[0]", CSCTF_L1_position_pts[0]


          CSCTF_sim_direction_pt_noGE21s[0] = treeHits.CSCTF_sim_direction_pt_noGE21[sim_index]
          CSCTF_L1_direction_pt_noGE21s[0] = treeHits.CSCTF_L1_direction_pt_noGE21[L1Mu_CSCTF_index]
          if verbose: print "CSCTF_sim_direction_pt_noGE21s[0]", CSCTF_sim_direction_pt_noGE21s[0]
          if verbose: print "CSCTF_L1_direction_pt_noGE21s[0]", CSCTF_L1_direction_pt_noGE21s[0]

          CSCTF_sim_direction_pt_GE21s[0] = treeHits.CSCTF_sim_direction_pt_GE21[sim_index]
          CSCTF_L1_direction_pt_GE21s[0] = treeHits.CSCTF_L1_direction_pt_GE21[L1Mu_CSCTF_index]
          if verbose: print "CSCTF_sim_direction_pt_GE21s[0]", CSCTF_sim_direction_pt_GE21s[0]
          if verbose: print "CSCTF_L1_direction_pt_GE21s[0]", CSCTF_L1_direction_pt_GE21s[0]


          CSCTF_sim_hybrid_pt_noGE21s[0] = treeHits.CSCTF_sim_hybrid_pt_noGE21[sim_index]
          CSCTF_L1_hybrid_pt_noGE21s[0] = treeHits.CSCTF_L1_hybrid_pt_noGE21[L1Mu_CSCTF_index]
          if verbose: print "CSCTF_sim_hybrid_pt_noGE21s[0]", CSCTF_sim_hybrid_pt_noGE21s[0]
          if verbose: print "CSCTF_L1_hybrid_pt_noGE21s[0]", CSCTF_L1_hybrid_pt_noGE21s[0]

          CSCTF_sim_hybrid_pt_GE21s[0] = treeHits.CSCTF_sim_hybrid_pt_GE21[sim_index]
          CSCTF_L1_hybrid_pt_GE21s[0] = treeHits.CSCTF_L1_hybrid_pt_GE21[L1Mu_CSCTF_index]
          if verbose: print "CSCTF_sim_hybrid_pt_GE21s[0]", CSCTF_sim_hybrid_pt_GE21s[0]
          if verbose: print "CSCTF_L1_hybrid_pt_GE21s[0]", CSCTF_L1_hybrid_pt_GE21s[0]

          CSCTF_sim_eta_st2s[0] = treeHits.CSCTF_sim_eta_st2[sim_index]
          CSCTF_L1_eta_st2s[0] = treeHits.CSCTF_L1_eta_st2[L1Mu_CSCTF_index]
          if verbose: print "CSCTF_sim_eta_st2s[0]", CSCTF_sim_eta_st2s[0]
          if verbose: print "CSCTF_L1_eta_st2s[0]", CSCTF_L1_eta_st2s[0]

          ## CSC information
          CSCTF_eta1s[0] = treeHits.CSCTF_eta1[L1Mu_CSCTF_index]
          CSCTF_eta2s[0] = treeHits.CSCTF_eta2[L1Mu_CSCTF_index]
          CSCTF_eta3s[0] = treeHits.CSCTF_eta3[L1Mu_CSCTF_index]
          CSCTF_eta4s[0] = treeHits.CSCTF_eta4[L1Mu_CSCTF_index]

          CSCTF_phi1s[0] = treeHits.CSCTF_phi1[L1Mu_CSCTF_index]
          CSCTF_phi2s[0] = treeHits.CSCTF_phi2[L1Mu_CSCTF_index]
          CSCTF_phi3s[0] = treeHits.CSCTF_phi3[L1Mu_CSCTF_index]
          CSCTF_phi4s[0] = treeHits.CSCTF_phi4[L1Mu_CSCTF_index]

          CSCTF_z1s[0] = treeHits.CSCTF_z1[L1Mu_CSCTF_index]
          CSCTF_z2s[0] = treeHits.CSCTF_z2[L1Mu_CSCTF_index]
          CSCTF_z3s[0] = treeHits.CSCTF_z3[L1Mu_CSCTF_index]
          CSCTF_z4s[0] = treeHits.CSCTF_z4[L1Mu_CSCTF_index]

          CSCTF_ch1s[0] = treeHits.CSCTF_ch1[L1Mu_CSCTF_index]
          CSCTF_ch2s[0] = treeHits.CSCTF_ch2[L1Mu_CSCTF_index]
          CSCTF_ch3s[0] = treeHits.CSCTF_ch3[L1Mu_CSCTF_index]
          CSCTF_ch4s[0] = treeHits.CSCTF_ch4[L1Mu_CSCTF_index]

          ok_CSCTF_st1s[0] = int(CSCTF_phi1s[0] != -99)
          ok_CSCTF_st2s[0] = int(CSCTF_phi2s[0] != -99)
          ok_CSCTF_st3s[0] = int(CSCTF_phi3s[0] != -99)
          ok_CSCTF_st4s[0] = int(CSCTF_phi4s[0] != -99)

          CSCTF_ch1s[0] = treeHits.CSCTF_ch1[L1Mu_CSCTF_index]
          CSCTF_ch2s[0] = treeHits.CSCTF_ch2[L1Mu_CSCTF_index]
          CSCTF_ch3s[0] = treeHits.CSCTF_ch3[L1Mu_CSCTF_index]
          CSCTF_ch4s[0] = treeHits.CSCTF_ch4[L1Mu_CSCTF_index]

          CSCTF_isEven1s[0] = CSCTF_ch1s[0]%2==0
          CSCTF_isEven2s[0] = CSCTF_ch2s[0]%2==0
          CSCTF_isEven3s[0] = CSCTF_ch3s[0]%2==0
          CSCTF_isEven4s[0] = CSCTF_ch4s[0]%2==0



          ## GEM information
          GE11_L1_phis[0] = treeHits.GE11_phi_L1[L1Mu_CSCTF_index]
          GE11_L2_phis[0] = treeHits.GE11_phi_L2[L1Mu_CSCTF_index]
          GE21_L1_phis[0] = treeHits.GE21_phi_L1[L1Mu_CSCTF_index]
          GE21_L2_phis[0]  =treeHits.GE21_phi_L2[L1Mu_CSCTF_index]

          GE11_L1_bxs[0] = treeHits.GE11_bx_L1[L1Mu_CSCTF_index]
          GE11_L2_bxs[0] = treeHits.GE11_bx_L2[L1Mu_CSCTF_index]
          GE21_L1_bxs[0] = treeHits.GE21_bx_L1[L1Mu_CSCTF_index]
          GE21_L2_bxs[0] = treeHits.GE21_bx_L2[L1Mu_CSCTF_index]

          if verbose:
            print "BX", GE11_sim_L1_bxs[0], GE11_L1_bxs[0]
            print "BX", GE11_sim_L2_bxs[0], GE11_L2_bxs[0]
            print "BX", GE21_sim_L1_bxs[0], GE21_L1_bxs[0]
            print "BX", GE21_sim_L2_bxs[0], GE21_L2_bxs[0]

          GE11_L1_zs[0] = treeHits.GE11_z_L1[L1Mu_CSCTF_index]
          GE11_L2_zs[0] = treeHits.GE11_z_L2[L1Mu_CSCTF_index]
          GE21_L1_zs[0] = treeHits.GE21_z_L1[L1Mu_CSCTF_index]
          GE21_L2_zs[0] = treeHits.GE21_z_L2[L1Mu_CSCTF_index]

          ok_GE11_L1s[0] = int(GE11_L1_phis[0] != 99)
          ok_GE11_L2s[0] = int(GE11_L2_phis[0] != 99)
          ok_GE21_L1s[0] = int(GE21_L1_phis[0] != 99)
          ok_GE21_L2s[0] = int(GE21_L2_phis[0] != 99)


          if verbose:
            print "\t\tCompare stubs SIM vs L1Mu"
            print "\t\tCSCTF_sim_phi1", CSCTF_sim_phi1s[0], "\tCSCTF_phi1", CSCTF_phi1s[0]
            print "\t\tCSCTF_sim_phi2", CSCTF_sim_phi2s[0], "\tCSCTF_phi2", CSCTF_phi2s[0]
            print "\t\tCSCTF_sim_phi3", CSCTF_sim_phi3s[0], "\tCSCTF_phi3", CSCTF_phi3s[0]
            print "\t\tCSCTF_sim_phi4", CSCTF_sim_phi4s[0], "\tCSCTF_phi4", CSCTF_phi4s[0]
            print

            print "\t\tCSCTF_sim_eta1", CSCTF_sim_eta1s[0], "\tCSCTF_eta1", CSCTF_eta1s[0]
            print "\t\tCSCTF_sim_eta2", CSCTF_sim_eta2s[0], "\tCSCTF_eta2", CSCTF_eta2s[0]
            print "\t\tCSCTF_sim_eta3", CSCTF_sim_eta3s[0], "\tCSCTF_eta3", CSCTF_eta3s[0]
            print "\t\tCSCTF_sim_eta4", CSCTF_sim_eta4s[0], "\tCSCTF_eta4", CSCTF_eta4s[0]
            print

            print "\t\tCSCTF_sim_z1", CSCTF_sim_z1s[0], "\tCSCTF_z1", CSCTF_z1s[0]
            print "\t\tCSCTF_sim_z2", CSCTF_sim_z2s[0], "\tCSCTF_z2", CSCTF_z2s[0]
            print "\t\tCSCTF_sim_z3", CSCTF_sim_z3s[0], "\tCSCTF_z3", CSCTF_z3s[0]
            print "\t\tCSCTF_sim_z4", CSCTF_sim_z4s[0], "\tCSCTF_z4", CSCTF_z4s[0]
            print

          parity_sim = get_parity(CSCTF_sim_isEven1s[0],
                                  CSCTF_sim_isEven2s[0],
                                  CSCTF_sim_isEven3s[0],
                                  CSCTF_sim_isEven4s[0])

          parity_L1 = get_parity(CSCTF_isEven1s[0],
                                 CSCTF_isEven2s[0],
                                 CSCTF_isEven3s[0],
                                 CSCTF_isEven4s[0])

          etaPartition_sim = get_eta_partition(CSCTF_sim_eta_st2s[0])
          etaPartition_L1 = get_eta_partition(CSCTF_L1_eta_st2s[0])

          paritys_sim[0] = parity_sim
          paritys_L1[0] = parity_L1

          partitions_sim[0] = etaPartition_sim
          partitions_L1[0] = etaPartition_L1

          ## Track-Trigger isolation
          L1Mu_L1Tk_dR_min = treeHits.L1Mu_L1Tk_dR_prop[SIM_L1Mu_index]
          L1Mu_L1Tk_pt = treeHits.L1Mu_L1Tk_pt_prop[SIM_L1Mu_index]

          #print "L1Mu_L1Tk_dR_min", L1Mu_L1Tk_dR_min
          #print "L1Mu_L1Tk_pt", L1Mu_L1Tk_pt

          if L1Mu_L1Tk_dR_min <= 0.12 and L1Mu_L1Tk_pt >= 4:
            L1Mu_isLooseVetos[0] = 1
            #print "L1Mu_isLooseVetos"

          if L1Mu_L1Tk_dR_min <= 0.12 and L1Mu_L1Tk_pt >= 3:
            L1Mu_isMediumVetos[0] = 1
            #print "L1Mu_isMediumVetos"

          if L1Mu_L1Tk_dR_min <= 0.12 and L1Mu_L1Tk_pt >= 2:
            L1Mu_isTightVetos[0] = 1
            #print "L1Mu_isTightVetos"



          #print "partition", partitions_sim[0]
          #print "partition L1", partitions_L1[0]

          t.Fill()
          continue
          """


              CSCTF_phi1 = treeHits.CSCTF_phi1[L1Mu_CSCTF_index]
              CSCTF_phi2 = treeHits.CSCTF_phi2[L1Mu_CSCTF_index]
              CSCTF_phi3 = treeHits.CSCTF_phi3[L1Mu_CSCTF_index]
              CSCTF_phi4 = treeHits.CSCTF_phi4[L1Mu_CSCTF_index]
              if verbose:
                print "\t\tCSCTF_phi1", CSCTF_phi1
                print "\t\tCSCTF_phi2", CSCTF_phi2
                print "\t\tCSCTF_phi3", CSCTF_phi3
                print "\t\tCSCTF_phi4", CSCTF_phi4

              CSCTF_eta1 = treeHits.CSCTF_eta1[L1Mu_CSCTF_index]
              CSCTF_eta2 = treeHits.CSCTF_eta2[L1Mu_CSCTF_index]
              CSCTF_eta3 = treeHits.CSCTF_eta3[L1Mu_CSCTF_index]
              CSCTF_eta4 = treeHits.CSCTF_eta4[L1Mu_CSCTF_index]
              if verbose:
                print "\t\tCSCTF_eta1", CSCTF_eta1
                print "\t\tCSCTF_eta2", CSCTF_eta2
                print "\t\tCSCTF_eta3", CSCTF_eta3
                print "\t\tCSCTF_eta4", CSCTF_eta4

              CSCTF_phi1s[0] = treeHits.CSCTF_phi1[L1Mu_CSCTF_index]
              CSCTF_phi2s[0] = treeHits.CSCTF_phi2[L1Mu_CSCTF_index]
              CSCTF_phi3s[0] = treeHits.CSCTF_phi3[L1Mu_CSCTF_index]
              CSCTF_phi4s[0] = treeHits.CSCTF_phi4[L1Mu_CSCTF_index]

              CSCTF_rec_phi1 = treeHits.CSCTF_rec_phi1[sim_index]
              CSCTF_rec_phi2 = treeHits.CSCTF_rec_phi2[sim_index]
              CSCTF_rec_phi3 = treeHits.CSCTF_rec_phi3[sim_index]
              CSCTF_rec_phi4 = treeHits.CSCTF_rec_phi4[sim_index]

              CSCTF_sim_phi1s[0] = treeHits.CSCTF_rec_phi1[sim_index]
              CSCTF_sim_phi2s[0] = treeHits.CSCTF_rec_phi2[sim_index]
              CSCTF_sim_phi3s[0] = treeHits.CSCTF_rec_phi3[sim_index]
              CSCTF_sim_phi4s[0] = treeHits.CSCTF_rec_phi4[sim_index]

              if verbose:
                print "\t\tCSCTF_rec_phi1", CSCTF_rec_phi1, "\tCSCTF_phi1", CSCTF_phi1s[0], "Delta", abs(CSCTF_rec_phi1-CSCTF_phi1s[0])
                print "\t\tCSCTF_rec_phi2", CSCTF_rec_phi2, "\tCSCTF_phi2", CSCTF_phi2s[0], "Delta", abs(CSCTF_rec_phi2-CSCTF_phi2s[0])
                print "\t\tCSCTF_rec_phi3", CSCTF_rec_phi3, "\tCSCTF_phi3", CSCTF_phi3s[0], "Delta", abs(CSCTF_rec_phi3-CSCTF_phi3s[0])
                print "\t\tCSCTF_rec_phi4", CSCTF_rec_phi4, "\tCSCTF_phi4", CSCTF_phi4s[0], "Delta", abs(CSCTF_rec_phi4-CSCTF_phi4s[0])

              CSCTF_rec_eta1 = treeHits.CSCTF_rec_eta1[sim_index]
              CSCTF_rec_eta2 = treeHits.CSCTF_rec_eta2[sim_index]
              CSCTF_rec_eta3 = treeHits.CSCTF_rec_eta3[sim_index]
              CSCTF_rec_eta4 = treeHits.CSCTF_rec_eta4[sim_index]

              CSCTF_eta1s[0] = treeHits.CSCTF_eta1[L1Mu_CSCTF_index]
              CSCTF_eta2s[0] = treeHits.CSCTF_eta2[L1Mu_CSCTF_index]
              CSCTF_eta3s[0] = treeHits.CSCTF_eta3[L1Mu_CSCTF_index]
              CSCTF_eta4s[0] = treeHits.CSCTF_eta4[L1Mu_CSCTF_index]

              CSCTF_sim_eta1s[0] = treeHits.CSCTF_rec_eta1[sim_index]
              CSCTF_sim_eta2s[0] = treeHits.CSCTF_rec_eta2[sim_index]
              CSCTF_sim_eta3s[0] = treeHits.CSCTF_rec_eta3[sim_index]
              CSCTF_sim_eta4s[0] = treeHits.CSCTF_rec_eta4[sim_index]

              if verbose:
                print "\t\tCSCTF_rec_eta1", CSCTF_rec_eta1, "\tCSCTF_eta1", CSCTF_eta1s[0], "Delta", abs(CSCTF_rec_eta1-CSCTF_eta1s[0])
                print "\t\tCSCTF_rec_eta2", CSCTF_rec_eta2, "\tCSCTF_eta2", CSCTF_eta2s[0], "Delta", abs(CSCTF_rec_eta2-CSCTF_eta2s[0])
                print "\t\tCSCTF_rec_eta3", CSCTF_rec_eta3, "\tCSCTF_eta3", CSCTF_eta3s[0], "Delta", abs(CSCTF_rec_eta3-CSCTF_eta3s[0])
                print "\t\tCSCTF_rec_eta4", CSCTF_rec_eta4, "\tCSCTF_eta4", CSCTF_eta4s[0], "Delta", abs(CSCTF_rec_eta4-CSCTF_eta4s[0])

              ## stub positions
              CSCTF_rec_z1 = treeHits.CSCTF_rec_z1[sim_index]
              CSCTF_rec_z2 = treeHits.CSCTF_rec_z2[sim_index]
              CSCTF_rec_z3 = treeHits.CSCTF_rec_z3[sim_index]
              CSCTF_rec_z4 = treeHits.CSCTF_rec_z4[sim_index]

              CSCTF_z1s[0] = treeHits.CSCTF_z1[L1Mu_CSCTF_index]
              CSCTF_z2s[0] = treeHits.CSCTF_z2[L1Mu_CSCTF_index]
              CSCTF_z3s[0] = treeHits.CSCTF_z3[L1Mu_CSCTF_index]
              CSCTF_z4s[0] = treeHits.CSCTF_z4[L1Mu_CSCTF_index]

              CSCTF_sim_z1s[0] = treeHits.CSCTF_rec_z1[sim_index]
              CSCTF_sim_z2s[0] = treeHits.CSCTF_rec_z2[sim_index]
              CSCTF_sim_z3s[0] = treeHits.CSCTF_rec_z3[sim_index]
              CSCTF_sim_z4s[0] = treeHits.CSCTF_rec_z4[sim_index]

              if verbose:
                print "\t\tCSCTF_rec_z1", CSCTF_sim_z1s[0], "\tCSCTF_z1", CSCTF_z1s[0], "Delta", abs(CSCTF_rec_z1-CSCTF_z1s[0])/CSCTF_rec_z1
                print "\t\tCSCTF_rec_z2", CSCTF_sim_z2s[0], "\tCSCTF_z2", CSCTF_z2s[0], "Delta", abs(CSCTF_rec_z2-CSCTF_z2s[0])/CSCTF_rec_z2
                print "\t\tCSCTF_rec_z3", CSCTF_sim_z3s[0], "\tCSCTF_z3", CSCTF_z3s[0], "Delta", abs(CSCTF_rec_z3-CSCTF_z3s[0])/CSCTF_rec_z3
                print "\t\tCSCTF_rec_z4", CSCTF_sim_z4s[0], "\tCSCTF_z4", CSCTF_z4s[0], "Delta", abs(CSCTF_rec_z4-CSCTF_z4s[0])/CSCTF_rec_z4
              ####


              ok_CSCTF_sim_st1 = CSCTF_rec_phi1 != 99
              ok_CSCTF_sim_st2 = CSCTF_rec_phi2 != 99
              ok_CSCTF_sim_st3 = CSCTF_rec_phi3 != 99
              ok_CSCTF_sim_st4 = CSCTF_rec_phi4 != 99

              ok_CSCTF_sim_st1s[0] = int(ok_CSCTF_sim_st1)
              ok_CSCTF_sim_st2s[0] = int(ok_CSCTF_sim_st2)
              ok_CSCTF_sim_st3s[0] = int(ok_CSCTF_sim_st3)
              ok_CSCTF_sim_st4s[0] = int(ok_CSCTF_sim_st4)


              CSCTF_rec_ch1 = treeHits.CSCTF_rec_ch1[sim_index]
              CSCTF_rec_ch2 = treeHits.CSCTF_rec_ch1[sim_index]
              CSCTF_rec_ch3 = treeHits.CSCTF_rec_ch3[sim_index]
              CSCTF_rec_ch4 = treeHits.CSCTF_rec_ch4[sim_index]

              CSCTF_rec_isOdd1 = CSCTF_rec_ch1%2==1
              CSCTF_rec_isOdd2 = CSCTF_rec_ch2%2==1
              CSCTF_rec_isOdd3 = CSCTF_rec_ch3%2==1
              CSCTF_rec_isOdd4 = CSCTF_rec_ch4%2==1

              CSCTF_rec_isEven1 = not CSCTF_rec_isOdd1
              CSCTF_rec_isEven2 = not CSCTF_rec_isOdd2
              CSCTF_rec_isEven3 = not CSCTF_rec_isOdd3
              CSCTF_rec_isEven4 = not CSCTF_rec_isOdd4


              CSCTF_sim_eta2 = treeHits.CSCTF_rec_eta2[sim_index]

              ok_CSCTF_st1 = CSCTF_phi1 != 99
              ok_CSCTF_st2 = CSCTF_phi2 != 99
              ok_CSCTF_st3 = CSCTF_phi3 != 99
              ok_CSCTF_st4 = CSCTF_phi4 != 99

              ok_CSCTF_st1s[0] = int(ok_CSCTF_st1)
              ok_CSCTF_st2s[0] = int(ok_CSCTF_st2)
              ok_CSCTF_st3s[0] = int(ok_CSCTF_st3)
              ok_CSCTF_st4s[0] = int(ok_CSCTF_st4)

              if verbose:
                print "\t\tok_CSCTF_st1", ok_CSCTF_st1
                print "\t\tok_CSCTF_st2", ok_CSCTF_st2
                print "\t\tok_CSCTF_st3", ok_CSCTF_st3
                print "\t\tok_CSCTF_st4", ok_CSCTF_st4

              ## ignore muons with only 1 stub
              #if ok_CSCTF_st1 + ok_CSCTF_st2 + ok_CSCTF_st3 + ok_CSCTF_st4 < 2: continue

              if ok_CSCTF_st1: CSCTF_phi1 = normalizedPhi2(treeHits.CSCTF_phi1[L1Mu_CSCTF_index])
              if ok_CSCTF_st2: CSCTF_phi2 = normalizedPhi2(treeHits.CSCTF_phi2[L1Mu_CSCTF_index])
              if ok_CSCTF_st3: CSCTF_phi3 = normalizedPhi2(treeHits.CSCTF_phi3[L1Mu_CSCTF_index])
              if ok_CSCTF_st4: CSCTF_phi4 = normalizedPhi2(treeHits.CSCTF_phi4[L1Mu_CSCTF_index])

              CSCTF_ch1 = treeHits.CSCTF_ch1[L1Mu_CSCTF_index]
              CSCTF_ch2 = treeHits.CSCTF_ch2[L1Mu_CSCTF_index]
              CSCTF_ch3 = treeHits.CSCTF_ch3[L1Mu_CSCTF_index]
              CSCTF_ch4 = treeHits.CSCTF_ch4[L1Mu_CSCTF_index]

              if verbose and False:
                print "\t\tCSCTF_ch1", CSCTF_ch1
                print "\t\tCSCTF_ch2", CSCTF_ch2
                print "\t\tCSCTF_ch3", CSCTF_ch3
                print "\t\tCSCTF_ch4", CSCTF_ch4

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

              if verbose and False:
                print "\t\tCSCTF_z1", CSCTF_z1
                print "\t\tCSCTF_z2", CSCTF_z2
                print "\t\tCSCTF_z3", CSCTF_z3
                print "\t\tCSCTF_z4", CSCTF_z4

              CSCTF_x1 = treeHits.CSCTF_x1[L1Mu_CSCTF_index]
              CSCTF_x2 = treeHits.CSCTF_x2[L1Mu_CSCTF_index]
              CSCTF_x3 = treeHits.CSCTF_x3[L1Mu_CSCTF_index]
              CSCTF_x4 = treeHits.CSCTF_x4[L1Mu_CSCTF_index]

              if verbose and False:
                print "\t\tCSCTF_x1", CSCTF_x1
                print "\t\tCSCTF_x2", CSCTF_x2
                print "\t\tCSCTF_x3", CSCTF_x3
                print "\t\tCSCTF_x4", CSCTF_x4

              CSCTF_y1 = treeHits.CSCTF_y1[L1Mu_CSCTF_index]
              CSCTF_y2 = treeHits.CSCTF_y2[L1Mu_CSCTF_index]
              CSCTF_y3 = treeHits.CSCTF_y3[L1Mu_CSCTF_index]
              CSCTF_y4 = treeHits.CSCTF_y4[L1Mu_CSCTF_index]

              if verbose and False:
                print "\t\tCSCTF_y1", CSCTF_y1
                print "\t\tCSCTF_y2", CSCTF_y2
                print "\t\tCSCTF_y3", CSCTF_y3
                print "\t\tCSCTF_y4", CSCTF_y4

              CSCTF_R1 = treeHits.CSCTF_R1[L1Mu_CSCTF_index]
              CSCTF_R2 = treeHits.CSCTF_R2[L1Mu_CSCTF_index]
              CSCTF_R3 = treeHits.CSCTF_R3[L1Mu_CSCTF_index]
              CSCTF_R4 = treeHits.CSCTF_R4[L1Mu_CSCTF_index]

              if verbose and False:
                print "\t\tCSCTF_R1", CSCTF_R1
                print "\t\tCSCTF_R2", CSCTF_R2
                print "\t\tCSCTF_R3", CSCTF_R3
                print "\t\tCSCTF_R4", CSCTF_R4

              ## fitted positions in a chamber
              CSCTF_fit_phi1 = treeHits.CSCTF_fit_phi1[L1Mu_CSCTF_index]
              CSCTF_fit_phi2 = treeHits.CSCTF_fit_phi2[L1Mu_CSCTF_index]
              CSCTF_fit_phi3 = treeHits.CSCTF_fit_phi3[L1Mu_CSCTF_index]
              CSCTF_fit_phi4 = treeHits.CSCTF_fit_phi4[L1Mu_CSCTF_index]

              CSCTF_fit_dphi1 = treeHits.CSCTF_fit_dphi1[L1Mu_CSCTF_index]
              CSCTF_fit_dphi2 = treeHits.CSCTF_fit_dphi2[L1Mu_CSCTF_index]
              CSCTF_fit_dphi3 = treeHits.CSCTF_fit_dphi3[L1Mu_CSCTF_index]
              CSCTF_fit_dphi4 = treeHits.CSCTF_fit_dphi4[L1Mu_CSCTF_index]

              CSCTF_fit_x1 = treeHits.CSCTF_fit_x1[L1Mu_CSCTF_index]
              CSCTF_fit_x2 = treeHits.CSCTF_fit_x2[L1Mu_CSCTF_index]
              CSCTF_fit_x3 = treeHits.CSCTF_fit_x3[L1Mu_CSCTF_index]
              CSCTF_fit_x4 = treeHits.CSCTF_fit_x4[L1Mu_CSCTF_index]

              CSCTF_fit_y1 = treeHits.CSCTF_fit_y1[L1Mu_CSCTF_index]
              CSCTF_fit_y2 = treeHits.CSCTF_fit_y2[L1Mu_CSCTF_index]
              CSCTF_fit_y3 = treeHits.CSCTF_fit_y3[L1Mu_CSCTF_index]
              CSCTF_fit_y4 = treeHits.CSCTF_fit_y4[L1Mu_CSCTF_index]

              CSCTF_fit_z1 = treeHits.CSCTF_fit_z1[L1Mu_CSCTF_index]
              CSCTF_fit_z2 = treeHits.CSCTF_fit_z2[L1Mu_CSCTF_index]
              CSCTF_fit_z3 = treeHits.CSCTF_fit_z3[L1Mu_CSCTF_index]
              CSCTF_fit_z4 = treeHits.CSCTF_fit_z4[L1Mu_CSCTF_index]

              CSCTF_fit_R1 = treeHits.CSCTF_fit_R1[L1Mu_CSCTF_index]
              CSCTF_fit_R2 = treeHits.CSCTF_fit_R2[L1Mu_CSCTF_index]
              CSCTF_fit_R3 = treeHits.CSCTF_fit_R3[L1Mu_CSCTF_index]
              CSCTF_fit_R4 = treeHits.CSCTF_fit_R4[L1Mu_CSCTF_index]

              GE11_phi_L1[L1Mu_CSCTF_index], GE11_phi_L2[L1Mu_CSCTF_index], GE21_phi_L1[L1Mu_CSCTF_index], GE21_phi_L2[L1Mu_CSCTF_index];
              GE21_pad2_phi_L1[L1Mu_CSCTF_index], GE21_pad2_phi_L2[L1Mu_CSCTF_index];
              GE11_bx_L1[L1Mu_CSCTF_index], GE11_bx_L2[L1Mu_CSCTF_index], GE21_bx_L1[L1Mu_CSCTF_index], GE21_bx_L2[L1Mu_CSCTF_index];
              GE11_ch_L1[L1Mu_CSCTF_index], GE11_ch_L2[L1Mu_CSCTF_index], GE21_ch_L1[L1Mu_CSCTF_index], GE21_ch_L2[L1Mu_CSCTF_index];
              GE11_z_L1[L1Mu_CSCTF_index], GE11_z_L2[L1Mu_CSCTF_index], GE21_z_L1[L1Mu_CSCTF_index], GE21_z_L2[L1Mu_CSCTF_index];



              parity_sim = get_parity(CSCTF_rec_isEven1, CSCTF_rec_isEven2, CSCTF_rec_isEven3, CSCTF_rec_isEven4)
              parity_L1 = get_parity(CSCTF_isEven1, CSCTF_isEven2, CSCTF_isEven3, CSCTF_isEven4)

              etaPartition_sim = get_eta_partition(CSCTF_rec_eta2)
              etaPartition_L1 = get_eta_partition(CSCTF_eta2)

              paritys_sim[0] = parity_sim
              partitions_sim[0] = etaPartition_sim

              paritys_L1[0] = parity_L1
              partitions_L1[0] = etaPartition_L1


              ok_position_based_endcap =  ok_CSCTF_st1 and ok_CSCTF_st2 and ok_CSCTF_st3
              if False and ok_position_based_endcap and 0 <= parity and parity <= 3 and abs(CSCTF_sim_eta2)>=1.2 and abs(CSCTF_sim_eta2)<=2.4:

                deltay12_withoutLCTFit, deltay23_withoutLCTFit = deltay12_deltay23(CSCTF_x1, CSCTF_y1, CSCTF_phi1,
                                                                                   CSCTF_x2, CSCTF_y2, CSCTF_phi2,
                                                                                   CSCTF_x3, CSCTF_y3, CSCTF_phi3)

                deltay12_withLCTFit, deltay23_withLCTFit = deltay12_deltay23(CSCTF_fit_x1, CSCTF_fit_y1, CSCTF_fit_phi1,
                                                                             CSCTF_fit_x2, CSCTF_fit_y2, CSCTF_fit_phi2,
                                                                             CSCTF_fit_x3, CSCTF_fit_y3, CSCTF_fit_phi3)

                proportionalityFactor = get_proptionality_factor_Tao(etaRanges[etaPartition],
                                                                     ME1ME2ME3ParityCases[parity], True)

                DDY123_withoutLCTFit = abs(deltay23_withoutLCTFit - proportionalityFactor * deltay12_withoutLCTFit)
                DDY123_withLCTFit    = abs(deltay23_withLCTFit - proportionalityFactor * deltay12_withLCTFit)

                positionPt_withLCTFit = pt_from_DDY123_Tao(DDY123_withLCTFit, etaRanges[etaPartition], ME1ME2ME3ParityCases[parity], True)

                DDY123_pts[0] = positionPt_withLCTFit

                DDY123_withLCTFits[0] = DDY123_withLCTFit
                DDY123_withoutLCTFits[0] = DDY123_withoutLCTFit

          """
          ## fill the tree for each gen muon
#          t.Fill()


f.Write()
f.Close()






