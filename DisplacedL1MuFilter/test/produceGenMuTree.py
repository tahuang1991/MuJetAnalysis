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

#______________________________________________________________________________ 
if __name__ == "__main__":  

  ## extension for figures - add more?
  ext = ".png"

  ## Style
  gStyle.SetStatStyle(0)

  print "Making the plots"

  set_style()

  doTest = False
  verbose = False
  if doTest:
    file = TFile("/uscms/home/dildick/nobackup/work/MuonPhaseIITDRStudies/CMSSW_6_2_0_SLHC28_patch1/src/out_ana_ctau_1000_PU140_GEM.root")
    treeHits = file.Get("DisplacedL1MuFilter_PhaseIIGE21/L1MuTree")
  
  ch = TChain("DisplacedL1MuFilter_PhaseIIGE21/L1MuTree")
  dirname='/eos/uscms/store/user/lpcgem/DarkSUSY_MH-125_MGammaD-20000_ctau1000_14TeV_madgraph-pythia6-tauola/DarkSUSY_mH_125_mGammaD_20000_cT_1000_14TeV_PU140_L1MuANA_v36/160907_181932/0000/'
  dirname2='/eos/uscms/store/user/lpcgem/DarkSUSY_MH-125_MGammaD-20000_ctau100_14TeV_madgraph-pythia6-tauola/DarkSUSY_mH_125_mGammaD_20000_cT_100_14TeV_PU140_L1MuANA_v2/160913_042859/0000/'
  dirname3='/eos/uscms/store/user/lpcgem/DarkSUSY_MH-125_MGammaD-20000_ctau10_14TeV_madgraph-pythia6-tauola/DarkSUSY_mH_125_mGammaD_20000_cT_10_14TeV_PU140_L1MuANA_v2/160913_042635/0000/'

  ch = addfiles(ch, dirname=dirname)
  ch = addfiles(ch, dirname=dirname2)
  ch = addfiles(ch, dirname=dirname3)
  treeHits = ch

  f = ROOT.TFile("out_ana.root", "recreate")
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

  has_L1Mus = numpy.zeros(1, dtype=int)
  L1Mu_pts = numpy.zeros(1, dtype=float)
  L1Mu_etas = numpy.zeros(1, dtype=float)
  L1Mu_phis = numpy.zeros(1, dtype=float)
  L1Mu_qualitys = numpy.zeros(1, dtype=int)
  L1Mu_bxs = numpy.zeros(1, dtype=int)

  has_CSCTFs = numpy.zeros(1, dtype=int)
  CSCTF_pts = numpy.zeros(1, dtype=float)
  CSCTF_etas = numpy.zeros(1, dtype=float)
  CSCTF_phis = numpy.zeros(1, dtype=float)
  CSCTF_qualitys = numpy.zeros(1, dtype=int)
  CSCTF_bxs = numpy.zeros(1, dtype=int)

  ok_CSCTF_st1s = numpy.zeros(1, dtype=int)
  ok_CSCTF_st2s = numpy.zeros(1, dtype=int)
  ok_CSCTF_st3s = numpy.zeros(1, dtype=int)
  ok_CSCTF_st4s = numpy.zeros(1, dtype=int)

  DDY123_pts = numpy.zeros(1, dtype=float)

  has_DTTFs = numpy.zeros(1, dtype=int)
  DTTF_pts = numpy.zeros(1, dtype=float)
  DTTF_etas = numpy.zeros(1, dtype=float)
  DTTF_phis = numpy.zeros(1, dtype=float)
  DTTF_qualitys = numpy.zeros(1, dtype=int)
  DTTF_bxs = numpy.zeros(1, dtype=int)

  ## branches
  t.Branch('gen_pt', gen_pts, 'gen_pt/D')
  t.Branch('gen_eta', gen_etas, 'gen_eta/D')
  t.Branch('gen_phi', gen_phis, 'gen_phi/D')
  t.Branch('gen_dxy', gen_dxys, 'gen_dxy/D')

  t.Branch('has_L1Mu', has_L1Mus, 'has_L1Mu/I')
  t.Branch('L1Mu_pt', L1Mu_pts, 'L1Mu_pt/D')
  t.Branch('L1Mu_eta', L1Mu_etas, 'L1Mu_eta/D')
  t.Branch('L1Mu_phi', L1Mu_phis, 'L1Mu_phi/D')
  t.Branch('L1Mu_quality', L1Mu_qualitys, 'L1Mu_quality/I')
  t.Branch('L1Mu_bx', L1Mu_bxs, 'L1Mu_bx/I')

  t.Branch('has_CSCTF', has_CSCTFs, 'has_CSCTF/I')
  t.Branch('CSCTF_pt', CSCTF_pts, 'CSCTF_pt/D')
  t.Branch('CSCTF_eta', CSCTF_etas, 'CSCTF_eta/D')
  t.Branch('CSCTF_phi', CSCTF_phis, 'CSCTF_phi/D')
  t.Branch('CSCTF_quality', CSCTF_qualitys, 'CSCTF_quality/I')
  t.Branch('CSCTF_bx', CSCTF_bxs, 'CSCTF_bx/I')

  t.Branch('ok_CSCTF_st1', ok_CSCTF_st1s, 'ok_CSCTF_st1/I')
  t.Branch('ok_CSCTF_st2', ok_CSCTF_st2s, 'ok_CSCTF_st2/I')
  t.Branch('ok_CSCTF_st3', ok_CSCTF_st3s, 'ok_CSCTF_st3/I')
  t.Branch('ok_CSCTF_st4', ok_CSCTF_st4s, 'ok_CSCTF_st4/I')
  
  t.Branch('DDY123_pt', DDY123_pts, 'DDY123_pt/d')

  t.Branch('has_DTTF', has_DTTFs, 'has_DTTF/I')
  t.Branch('DTTF_pt', DTTF_pts, 'DTTF_pt/D')
  t.Branch('DTTF_eta', DTTF_etas, 'DTTF_eta/D')
  t.Branch('DTTF_phi', DTTF_phis, 'DTTF_phi/D')
  t.Branch('DTTF_quality', DTTF_qualitys, 'DTTF_quality/I')
  t.Branch('DTTF_bx', DTTF_bxs, 'DTTF_bx/I')

  print "Start run on events..."
  for k in range(0,treeHits.GetEntries()):
      treeHits.GetEntry(k)
      if k%1000==0: print "Event", k+1, "nL1Mu", treeHits.nL1Mu
      #if k>25000: break

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
          if abs(eta_prop)>2.4:
            continue
          if pt<0:
            continue
          
          gen_pts[0] = treeHits.genGdMu_pt[ij]
          gen_etas[0] = treeHits.genGdMu_eta_prop[ij]
          gen_phis[0] = treeHits.genGdMu_phi_prop[ij]
          gen_dxys[0] = treeHits.genGdMu_dxy[ij]

          #print "ok",  gen_pts[0], gen_etas[0], gen_phis[0], gen_phis[0]

          L1Mu_index = treeHits.genGdMu_L1Mu_index_prop[ij]
          L1Mu_dR_prop = treeHits.genGdMu_L1Mu_dR_prop[ij]

          has_L1Mus[0] = L1Mu_index != 99 and L1Mu_dR_prop < 0.2
          
          L1Mu_pts[0] = -99
          L1Mu_etas[0] = -99
          L1Mu_phis[0] = -99
          L1Mu_qualitys[0] = -99 
          L1Mu_bxs[0] = -99

          has_CSCTFs[0] = 0

          CSCTF_pts[0] = -99
          CSCTF_etas[0] = -99
          CSCTF_phis[0] = -99
          CSCTF_qualitys[0] = -99 
          CSCTF_bxs[0] = -99
          
          ok_CSCTF_st1s[0] = False
          ok_CSCTF_st2s[0] = False
          ok_CSCTF_st3s[0] = False
          ok_CSCTF_st4s[0] = False
          
          DDY123_pts[0] = 0

          has_DTTFs[0] = 0

          DTTF_pts[0] = -99
          DTTF_etas[0] = -99
          DTTF_phis[0] = -99
          DTTF_qualitys[0] = -99 
          DTTF_bxs[0] = -99

          #print has_L1Mus[0]
          if has_L1Mus[0]:
            
            #print "ok L1",  L1Mu_pts[0], L1Mu_etas[0], L1Mu_phis[0]

            L1Mu_pts[0] = treeHits.L1Mu_pt[L1Mu_index]
            L1Mu_etas[0] = treeHits.L1Mu_eta[L1Mu_index]
            L1Mu_phis[0] = treeHits.L1Mu_phi[L1Mu_index]
            L1Mu_bxs[0] = treeHits.L1Mu_bx[L1Mu_index]
            L1Mu_qualitys[0] = treeHits.L1Mu_quality[L1Mu_index]
          
            L1Mu_DTTF_index  = treeHits.L1Mu_DTTF_index[L1Mu_index]
            L1Mu_CSCTF_index = treeHits.L1Mu_CSCTF_index[L1Mu_index]
          
            has_CSCTFs[0] = L1Mu_CSCTF_index != 99 and L1Mu_CSCTF_index != -1
            has_DTTFs[0]  = L1Mu_DTTF_index  != 99 and L1Mu_DTTF_index  != -1
            
            if has_CSCTFs[0]:
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

              ok_CSCTF_st1 = CSCTF_phi1 != 99
              ok_CSCTF_st2 = CSCTF_phi2 != 99
              ok_CSCTF_st3 = CSCTF_phi3 != 99
              ok_CSCTF_st4 = CSCTF_phi4 != 99              
              
              ok_CSCTF_st1s[0] = ok_CSCTF_st1
              ok_CSCTF_st2s[0] = ok_CSCTF_st2
              ok_CSCTF_st3s[0] = ok_CSCTF_st3
              ok_CSCTF_st4s[0] = ok_CSCTF_st4  

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

              if verbose:
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

              if verbose:
                print "\t\tCSCTF_z1", CSCTF_z1 
                print "\t\tCSCTF_z2", CSCTF_z2 
                print "\t\tCSCTF_z3", CSCTF_z3 
                print "\t\tCSCTF_z4", CSCTF_z4 

              CSCTF_x1 = treeHits.CSCTF_x1[L1Mu_CSCTF_index]
              CSCTF_x2 = treeHits.CSCTF_x2[L1Mu_CSCTF_index]
              CSCTF_x3 = treeHits.CSCTF_x3[L1Mu_CSCTF_index]
              CSCTF_x4 = treeHits.CSCTF_x4[L1Mu_CSCTF_index]

              if verbose:
                print "\t\tCSCTF_x1", CSCTF_x1 
                print "\t\tCSCTF_x2", CSCTF_x2 
                print "\t\tCSCTF_x3", CSCTF_x3 
                print "\t\tCSCTF_x4", CSCTF_x4 

              CSCTF_y1 = treeHits.CSCTF_y1[L1Mu_CSCTF_index]
              CSCTF_y2 = treeHits.CSCTF_y2[L1Mu_CSCTF_index]
              CSCTF_y3 = treeHits.CSCTF_y3[L1Mu_CSCTF_index]
              CSCTF_y4 = treeHits.CSCTF_y4[L1Mu_CSCTF_index]

              if verbose:
                print "\t\tCSCTF_y1", CSCTF_y1 
                print "\t\tCSCTF_y2", CSCTF_y2 
                print "\t\tCSCTF_y3", CSCTF_y3 
                print "\t\tCSCTF_y4", CSCTF_y4 

              CSCTF_R1 = treeHits.CSCTF_R1[L1Mu_CSCTF_index]
              CSCTF_R2 = treeHits.CSCTF_R2[L1Mu_CSCTF_index]
              CSCTF_R3 = treeHits.CSCTF_R3[L1Mu_CSCTF_index]
              CSCTF_R4 = treeHits.CSCTF_R4[L1Mu_CSCTF_index]

              if verbose:
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

              parity = get_parity(CSCTF_isEven1, CSCTF_isEven2, CSCTF_isEven3, CSCTF_isEven4)
              etaPartition = get_eta_partition(L1Mu_etas[0])

              ok_position_based_endcap =  ok_CSCTF_st1 and ok_CSCTF_st2 and ok_CSCTF_st3 
              if ok_position_based_endcap and 0 <= parity and parity <= 3 and abs(L1Mu_etas[0])>=1.2 and abs(L1Mu_etas[0])<=2.4:

                deltay12_withLCTFit, deltay23_withLCTFit = deltay12_deltay23(CSCTF_fit_x1, CSCTF_fit_y1, CSCTF_fit_phi1,
                                                                             CSCTF_fit_x2, CSCTF_fit_y2, CSCTF_fit_phi2,
                                                                             CSCTF_fit_x3, CSCTF_fit_y3, CSCTF_fit_phi3)
                
                proportionalityFactor_withLCTFit = get_proptionality_factor_Tao(etaRanges[etaPartition], 
                                                                                ME1ME2ME3ParityCases[parity], True)
                
                DDY123_withLCTFit    = abs(deltay23_withLCTFit - proportionalityFactor_withLCTFit * deltay12_withLCTFit)
                positionPt_withLCTFit = pt_from_DDY123_Tao(DDY123_withLCTFit, etaRanges[etaPartition], ME1ME2ME3ParityCases[parity], True)
                DDY123_pts[0] = positionPt_withLCTFit

          ## fill the tree for each gen muon
          t.Fill()
          
          
f.Write()
f.Close()






