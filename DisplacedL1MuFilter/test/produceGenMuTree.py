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
  
  gen_pts = numpy.zeros(1, dtype=float)
  gen_etas = numpy.zeros(1, dtype=float)
  gen_phis = numpy.zeros(1, dtype=float)
  gen_dxys = numpy.zeros(1, dtype=float)

  L1Mu_pts = numpy.zeros(1, dtype=float)
  has_L1Mus = numpy.zeros(1, dtype=int)

  t.Branch('gen_pt', gen_pts, 'gen_pt/D')
  t.Branch('gen_eta', gen_etas, 'gen_eta/D')
  t.Branch('gen_phi', gen_phis, 'gen_phi/D')
  t.Branch('gen_dxy', gen_dxys, 'gen_dxy/D')

  t.Branch('L1Mu_pt', L1Mu_pts, 'L1Mu_pt/D')
  t.Branch('has_L1Mu', has_L1Mus, 'has_L1Mu/I')


  print "Start run on events..."
  for k in range(0,treeHits.GetEntries()):
      treeHits.GetEntry(k)
      if k%1000==0: print "Event", k+1, "nL1Mu", treeHits.nL1Mu
      if k>10000: break

      #print "event_number", event_number
      #print "lumi_number", lumi_number
      #print "run_number", run_number

      for i in range(0,2):

        for j in range(0,2):
          ij = i*2+j
          
          pt = abs(treeHits.genGdMu_pt[ij])
          eta = treeHits.genGdMu_eta[ij]
          phi = abs(treeHits.genGdMu_phi[ij])
          charge = treeHits.genGdMu_q[ij]
          eta_prop = treeHits.genGdMu_eta_prop[ij]
          phi_prop = treeHits.genGdMu_phi_prop[ij]
          dxy = abs(treeHits.genGdMu_dxy[ij])
          vz = abs(treeHits.genGd_vz[i])
          lxy =  abs(treeHits.genGd_lxy[i])
          SIM_index = treeHits.genGdMu_SIM_index[ij]
          SIM_dR = treeHits.genGdMu_SIM_dR[ij]

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
          
          gen_pts[0] = treeHits.genGdMu_pt[ij]
          gen_etas[0] = treeHits.genGdMu_eta_prop[ij]
          gen_phis[0] = treeHits.genGdMu_phi_prop[ij]
          gen_dxys[0] = treeHits.genGdMu_phi_prop[ij]

          L1Mu_index = treeHits.genGdMu_L1Mu_index_prop[ij]
          L1Mu_dR_prop = treeHits.genGdMu_L1Mu_dR_prop[ij]

          has_L1Mus[0] = L1Mu_index != 99 and L1Mu_dR_prop < 0.2
          
          #L1Mu_pts[0]
          
          t.Fill()
          
          
f.Write()
f.Close()






