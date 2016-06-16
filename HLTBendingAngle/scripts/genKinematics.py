from ROOT import *

from Helpers import *

def genKinematics(p):
    draw_1D(p,"genGdMu_eta_max", "genGdMu_eta_max",  "GEN muon eta^{max}; GEN muon eta^{max}; Entries", "(100,-5,5)")
    draw_1D(p,"genGdMu_eta_max", "genGdMu_eta_max_pt",  "GEN muon eta^{max}; GEN muon eta^{max}; Entries", "(100,-5,5)","genGdMu_pt[0]>5 && genGdMu_pt[1]>5")

    draw_1D(p,"genGdMu_p[0]", "genGdMu_p0",  "GEN Muon p; GEN Muon p [GeV/c]; Entries", "(50,0,100)")
    draw_1D(p,"genGdMu_px[0]", "genGdMu_px0",  "GEN Muon px; GEN Muon px [GeV/c]; Entries", "(50,0,100)")
    draw_1D(p,"genGdMu_py[0]", "genGdMu_py0",  "GEN Muon py; GEN Muon py [GeV/c]; Entries", "(50,0,100)")
    draw_1D(p,"genGdMu_pz[0]", "genGdMu_pz0",  "GEN Muon pz; GEN Muon pz [GeV/c]; Entries", "(50,0,100)")
    draw_1D(p,"genGdMu_pt[0]", "genGdMu_pt0",  "GEN Muon pt; GEN Muon pt [GeV/c]; Entries", "(50,0,100)")
    draw_1D(p,"genGdMu_eta[0]", "genGdMu_eta0", "GEN Muon #eta; GEN Muon #eta; Entries", "(50,-2.5,2.5)")
    draw_1D(p,"genGdMu_phi_corr[0]", "genGdMu_phi_corr0", "GEN Muon #phi^{corr}; GEN Muon #phi^{corr}; Entries", "(60,-3.1416,3.1416)")
    draw_1D(p,"genGdMu_vx[0]", "genGdMu_vx0",  "GEN Muon vx; GEN Muon vx [cm]; Entries", "(200,-100,100)")
    draw_1D(p,"genGdMu_vy[0]", "genGdMu_vy0",  "GEN Muon vy; GEN Muon vy [cm]; Entries", "(200,-100,100)")
    draw_1D(p,"genGdMu_vz[0]", "genGdMu_vz0",  "GEN Muon vz; GEN Muon vz [cm]; Entries", "(200,-100,100)")
    draw_1D(p,"genGdMu_dxy[0]", "genGdMu_dxy0",  "GEN Muon dxy; GEN Muon dxy [cm]; Entries", "(200,-100,100)")

    draw_1D(p,"genGdMu_p[1]", "genGdMu_p1",  "GEN Muon p; GEN Muon p [GeV/c]; Entries", "(50,0,100)")
    draw_1D(p,"genGdMu_px[1]", "genGdMu_px1",  "GEN Muon px; GEN Muon px [GeV/c]; Entries", "(50,0,100)")
    draw_1D(p,"genGdMu_py[1]", "genGdMu_py1",  "GEN Muon py; GEN Muon py [GeV/c]; Entries", "(50,0,100)")
    draw_1D(p,"genGdMu_pz[1]", "genGdMu_pz1",  "GEN Muon pz; GEN Muon pz [GeV/c]; Entries", "(50,0,100)")
    draw_1D(p,"genGdMu_pt[1]", "genGdMu_pt1",  "GEN Muon pt; GEN Muon pt [GeV/c]; Entries", "(50,0,100)")
    draw_1D(p,"genGdMu_eta[1]", "genGdMu_eta1", "GEN Muon #eta; GEN Muon #eta; Entries", "(50,-2.5,2.5)")
    draw_1D(p,"genGdMu_phi_corr[1]", "genGdMu_phi_corr1", "GEN Muon #phi^{corr}; GEN Muon #phi^{corr}; Entries", "(60,-3.1416,3.1416)")
    draw_1D(p,"genGdMu_vx[1]", "genGdMu_vx1",  "GEN Muon vx; GEN Muon vx [cm]; Entries", "(200,-100,100)")
    draw_1D(p,"genGdMu_vy[1]", "genGdMu_vy1",  "GEN Muon vy; GEN Muon vy [cm]; Entries", "(200,-100,100)")
    draw_1D(p,"genGdMu_vz[1]", "genGdMu_vz1",  "GEN Muon vz; GEN Muon vz [cm]; Entries", "(200,-100,100)")
    draw_1D(p,"genGdMu_dxy[1]", "genGdMu_dxy1",  "GEN Muon dxy; GEN Muon dxy [cm]; Entries", "(200,-100,100)")

