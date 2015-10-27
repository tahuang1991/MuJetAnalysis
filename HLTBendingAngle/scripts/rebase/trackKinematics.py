from ROOT import *

from Helpers import *

def trackKinematics(p):
    draw_1D(p,"l1Extra_pt",  "l1Extra_pt",  "L1Extra p_{T}; L1Extra p_{T} [GeV/c]; Entries", "(50,0,100)")
    draw_1D(p,"l1Extra_eta", "l1Extra_eta", "L1Extra #eta; L1Extra #eta; Entries", "(50,-2.5,2.5)")
    draw_1D(p,"l1Extra_phi", "l1Extra_phi", "L1Extra #phi; L1Extra #phi; Entries", "(60,-3.1416,3.1416)")
    draw_1D(p,"l1Extra_dR", "l1Extra_dR", "dR(SimTrack,L1Extra); dR(SimTrack, L1Extra); Entries", "(100,0,1.0")
    draw_1D(p,"l1Extra_dR", "l1Extra_dR_dxy10_eta24", "dR(SimTrack,L1Extra); dR(SimTrack, L1Extra); Entries", "(100,0,1.0", AND(cms_eta(),sim_dxy(10)))

    draw_1D(p,"recoTrackExtra_pt_outer",  "recoTrackExtra_pt_outer",  "TrackExtra outer p_{T}; TrackExtra p_{T}^{outer} [GeV/c]; Entries", "(50,0,100)")
    draw_1D(p,"recoTrackExtra_eta_outer", "recoTrackExtra_eta_outer", "TrackExtra outer #eta; TrackExtra #eta^{outer}; Entries", "(50,-2.5,2.5)")
    draw_1D(p,"recoTrackExtra_phi_outer", "recoTrackExtra_phi_outer", "TrackExtra outer #phi; TrackExtra #phi^{outer}; Entries", "(60,-3.1416,3.1416)")

    draw_1D(p,"recoTrackExtra_pt_inner",  "recoTrackExtra_pt_inner",  "TrackExtra inner p_{T}; TrackExtra p_{T}^{inner} [GeV/c]; Entries", "(50,0,100)")
    draw_1D(p,"recoTrackExtra_eta_inner", "recoTrackExtra_eta_inner", "TrackExtra inner #eta; TrackExtra #eta^{inner}; Entries", "(50,-2.5,2.5)")
    draw_1D(p,"recoTrackExtra_phi_inner", "recoTrackExtra_phi_inner", "TrackExtra inner #phi; TrackExtra #phi^{inner}; Entries", "(60,-3.1416,3.1416)")

    draw_1D(p,"recoTrack_pt_outer",  "recoTrack_pt_outer",  "Track outer p_{T}; Track p_{T}^{outer} [GeV/c]; Entries", "(50,0,100)")
    draw_1D(p,"recoTrack_eta_outer", "recoTrack_eta_outer", "Track outer #eta; Track #eta^{outer}; Entries", "(50,-2.5,2.5)")
    draw_1D(p,"recoTrack_phi_outer", "recoTrack_phi_outer", "Track outer #phi; Track #phi^{outer}; Entries", "(60,-3.1416,3.1416)")

    draw_1D(p,"recoChargedCandidate_pt",  "recoChargedCandidate_pt",  "Charged Candidate p_{T}; Charged Candidate p_{T} [GeV/c]; Entries", "(50,0,100)")
    draw_1D(p,"recoChargedCandidate_eta", "recoChargedCandidate_eta", "Charged Candidate #eta; Charged Candidate #eta; Entries", "(50,-2.5,2.5)")
    draw_1D(p,"recoChargedCandidate_phi", "recoChargedCandidate_phi", "Charged Candidate #phi; Charged Candidate #phi; Entries", "(60,-3.1416,3.1416)")

    draw_1D(p,"recoChargedCandidate_nHits", "recoChargedCandidate_nHits", "Charged Candidate hits; Charged Candidate hits; Entries", "(20,0,20)")
    draw_1D(p,"recoChargedCandidate_nHitsGEM", "recoChargedCandidate_nHitsGEM", "Charged Candidate GEM hits; Charged Candidate GEM hits; Entries", "(20,0,20)")
    draw_1D(p,"recoChargedCandidate_nHitsCSC", "recoChargedCandidate_nHitsCSC", "Charged Candidate RPC hits; Charged Candidate RPC hits; Entries", "(20,0,20)")
    draw_1D(p,"recoChargedCandidate_nHitsDT", "recoChargedCandidate_nHitsDT", "Charged Candidate DT hits; Charged Candidate DT hits; Entries", "(20,0,20)")
    draw_1D(p,"recoChargedCandidate_nHitsCSC", "recoChargedCandidate_nHitsRPC", "Charged Candidate CSC hits; Charged Candidate CSC hits; Entries", "(20,0,20)")
