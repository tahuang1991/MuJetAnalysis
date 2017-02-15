## this file contains functions that check if a L1Mu is isolated
from Helpers import *
from hybridAlgorithmPtAssignment import *
import random

##_________________________________________________
def is_L1Mu_isolated(treeHits, L1Mu_index, vetoType):
    """checks if muon is isolated from track trigger track"""

    L1Mu_L1Tk_dR_min = treeHits.L1Mu_L1Tk_dR_prop[L1Mu_index]
    L1Mu_L1Tk_pt = treeHits.L1Mu_L1Tk_pt_prop[L1Mu_index]
    verbose = False
    if verbose:
        print "Checking veto"
        print "L1Mu_L1Tk_dR_min", L1Mu_L1Tk_dR_min
        print "L1Mu_L1Tk_pt", L1Mu_L1Tk_pt
    # The loose veto rejects prompt muons by matching a L1Tk within
    # a radius R<0.12 with an L1Tk pT > 4 GeV. The medium and tight
    # veto apply L1Tk pT cuts of 3 and 2 GeV respectively on L1Tk
    # in R<0.12.

    ## loose
    if vetoType == 1:
        dR_largeCone = 0.12
        ptCut_largeCone = 4
        dR_smallCone = 0.12
        ptCut_smallCone = 4

    ## medium
    if vetoType == 2:
        dR_largeCone = 0.12
        ptCut_largeCone = 4
        dR_smallCone = 0.12
        ptCut_smallCone = 3

    ## tight
    if vetoType == 3:
        dR_largeCone = 0.12
        ptCut_largeCone = 4
        dR_smallCone = 0.12
        ptCut_smallCone = 2

    isMatched = False
    isUnmatched = False

    ## check if matched or unmatched
    ## L1Tk should have a momentum above a certain threshold to be matched or unmatched
    #if L1Mu_L1Tk_dR_min <= dR_largeCone and L1Mu_L1Tk_pt >= ptCut_largeCone: isUnmatched = True
    if L1Mu_L1Tk_dR_min <= dR_smallCone and L1Mu_L1Tk_pt >= ptCut_smallCone: isMatched = True

    ## isolated means neither matched nor unmatched!
    return (not isMatched) and (not isUnmatched)

##_________________________________________________
def isME11StubDisabled(failRate):
    random_number = random.random()
    return random_number < failRate


##_________________________________________________
def isME21StubDisabled(failRate):
    random_number = random.random()
    return random_number < failRate

##_________________________________________________
def fillDPhiHistogram( h_dphi_ME11_ME21, treeHits, min_pt = 0, max_pt = 999 ):

    ## check if this event has L1Mus
    if len(list(treeHits.L1Mu_pt))==0:
        return max_prompt_L1Mu_pt, max_prompt_L1Mu_eta

    pts = list(treeHits.L1Mu_pt)
    #print "\tN L1Mus event", len(pts)
    for i in range(0,len(pts)):
        L1Mu_pt = treeHits.L1Mu_pt[i]
        L1Mu_eta = treeHits.L1Mu_eta[i]
        L1Mu_phi = treeHits.L1Mu_phi[i]
        L1Mu_bx = treeHits.L1Mu_bx[i]
        L1Mu_quality = treeHits.L1Mu_quality[i]
        L1Mu_CSCTF_index = treeHits.L1Mu_CSCTF_index[i]
        L1Mu_DTTF_index = treeHits.L1Mu_DTTF_index[i]
        L1Mu_charge = treeHits.L1Mu_charge[i]
        #print "L1Mu_charge", L1Mu_charge

        if L1Mu_pt < min_pt or L1Mu_pt > max_pt: continue

        ## eta cut
        #if not (etaCutMin <= abs(L1Mu_eta) and abs(L1Mu_eta) <= etaCutMax): continue

        ## quality cut
        if L1Mu_quality < 4: continue

        ## BX cut
        if abs(L1Mu_bx)>0 and True: continue

        ## not a CSC muon
        if L1Mu_CSCTF_index == -1: continue

        ## check even or odd
        GE11_even_L1 = treeHits.GE11_ch_L1[L1Mu_CSCTF_index] % 2 ==0
        GE11_even_L2 = treeHits.GE11_ch_L2[L1Mu_CSCTF_index] % 2 ==0
        
        GE21_even_L1 = treeHits.GE21_ch_L1[L1Mu_CSCTF_index] % 2 ==0
        GE21_even_L2 = treeHits.GE21_ch_L2[L1Mu_CSCTF_index] % 2 ==0

        GE11_phi_L1 = treeHits.GE11_phi_L1[L1Mu_CSCTF_index]
        GE11_phi_L2 = treeHits.GE11_phi_L2[L1Mu_CSCTF_index]

        GE21_phi_L1 = treeHits.GE21_pad2_phi_L1[L1Mu_CSCTF_index]
        GE21_phi_L2 = treeHits.GE21_pad2_phi_L2[L1Mu_CSCTF_index]

        GE11_z_L1 = treeHits.GE11_z_L1[L1Mu_CSCTF_index]
        GE11_z_L2 = treeHits.GE11_z_L2[L1Mu_CSCTF_index]

        GE21_z_L1 = treeHits.GE21_z_L1[L1Mu_CSCTF_index]
        GE21_z_L2 = treeHits.GE21_z_L2[L1Mu_CSCTF_index]

        """
        if GE11_even_L1:
            print "GE11 even L1", GE11_phi_L1, GE11_z_L1
        else:
            print "GE11 odd L1", GE11_phi_L1, GE11_z_L1
            
        if GE11_even_L2:
            print "GE11 even L2", GE11_phi_L2, GE11_z_L2
        else:
            print "GE11 odd L2", GE11_phi_L2, GE11_z_L2
        """

        if GE21_even_L1:
            print "GE21 even L1", GE21_phi_L1, GE21_z_L1
        else:
            print "GE21 odd L1", GE21_phi_L1, GE21_z_L1
            
        if GE21_even_L2:
            print "GE21 even L2", GE21_phi_L2, GE21_z_L2
        else:
            print "GE21 odd L2", GE21_phi_L2, GE21_z_L2


        CSCTF_fit_phi1 = treeHits.CSCTF_fit_phi1[L1Mu_CSCTF_index]
        CSCTF_fit_phi2 = treeHits.CSCTF_fit_phi2[L1Mu_CSCTF_index]

        GE11_phi = getBestValue(GE11_phi_L1, GE11_phi_L2)
        GE21_phi = getBestValue(GE21_phi_L1, GE21_phi_L2)

        #GE11_ME11_dphi = - GE11_phi + CSCTF_fit_phi1
        #GE21_ME21_dphi = - GE21_phi + CSCTF_fit_phi2

        if CSCTF_fit_phi1 == 99 or CSCTF_fit_phi2 == 99:
            continue

        if GE11_phi == 99.:
            GE11_ME11_dphi = 99#0.025
        else:
            GE11_ME11_dphi = L1Mu_charge*(- GE11_phi + CSCTF_fit_phi1)

        if GE21_phi == 99.:
            GE21_ME21_dphi = 99#0.025
        else:
            GE21_ME21_dphi = L1Mu_charge*(- GE21_phi + CSCTF_fit_phi2)

        """
        print "GE11_phi_L1", GE11_phi_L1
        print "GE11_phi_L2", GE11_phi_L2
        print "GE21_phi_L1", GE21_phi_L1
        print "GE21_phi_L2", GE21_phi_L2
        print "ME11_phi", CSCTF_fit_phi1
        print "ME21_phi", CSCTF_fit_phi2
        print "GE11_phi", GE11_phi
        print "GE21_phi", GE21_phi
        print "GE11_ME11_dphi", GE11_ME11_dphi
        print "GE21_ME21_dphi", GE21_ME21_dphi
        print
        """

        h_dphi_ME11_ME21.Fill(GE11_ME11_dphi, GE21_ME21_dphi)

##_________________________________________________
def fillPromptHistogram(mapTH1F,
                       key,
                       treeHits,
                       etaCutMin,
                       etaCutMax,
                       stubCut=2,
                       hasME1Cut=False,
                       hasME2Cut=False,
                       hasME3Cut=False,
                       hasME4Cut=False,
                       hasME11Cut=False,
                       hasME21Cut=False,
                       hasGE11Cut=False,
                       hasGE21Cut=False,
                       hasME11ME21Cut=False,
                       hasGE11GE21Cut=False,
                       ME11FailRate=0,
                       ME21FailRate=0,
                       hasMB1Cut=False,
                       hasMB2Cut=False,
                       hasMB3Cut=False,
                       hasMB4Cut=False):
    doBXCut = True
    qualityCut=4
    prompt_L1Mu_pt, prompt_L1Mu_eta = getMaxPromptPtEtaEvent(treeHits,
                                                             doBXCut,
                                                             etaCutMin,
                                                             etaCutMax,
                                                             stubCut,
                                                             qualityCut,
                                                             hasME1Cut,
                                                             hasME2Cut,
                                                             hasME3Cut,
                                                             hasME4Cut,
                                                             hasME11Cut,
                                                             hasME21Cut,
                                                             hasGE11Cut,
                                                             hasGE21Cut,
                                                             hasME11ME21Cut,
                                                             hasGE11GE21Cut,
                                                             ME11FailRate,
                                                             ME21FailRate,
                                                             hasMB1Cut,
                                                             hasMB2Cut,
                                                             hasMB3Cut,
                                                             hasMB4Cut)

    if (prompt_L1Mu_pt>0):
        mapTH1F[key.replace("rate_", "rate_pt_")].Fill(prompt_L1Mu_pt)
    ## apply a 7/10 GeV pT cut for the eta histograms!!!
    if (prompt_L1Mu_pt>=7):
        mapTH1F[key.replace("rate_", "rate_eta_L1Pt7_")].Fill(abs(prompt_L1Mu_eta))
    if (prompt_L1Mu_pt>=10):
        mapTH1F[key.replace("rate_", "rate_eta_L1Pt10_")].Fill(abs(prompt_L1Mu_eta))



def getMaxPromptPtEtaEvent(treeHits,
                           doBXCut,
                           etaCutMin,
                           etaCutMax,
                           stubCut,
                           qualityCut,
                           hasME1Cut=False,
                           hasME2Cut=False,
                           hasME3Cut=False,
                           hasME4Cut=False,
                           hasME11Cut=False,
                           hasME21Cut=False,
                           hasGE11Cut=False,
                           hasGE21Cut=False,
                           hasME11ME21Cut=False,
                           hasGE11GE21Cut=False,
                           ME11FailRate=0,
                           ME21FailRate=0,
                           hasMB1Cut=False,
                           hasMB2Cut=False,
                           hasMB3Cut=False,
                           hasMB4Cut=False):

    max_prompt_L1Mu_pt = -1
    max_prompt_L1Mu_eta = -99

    ## check if this event has L1Mus
    if len(list(treeHits.L1Mu_pt))==0:
        return max_prompt_L1Mu_pt, max_prompt_L1Mu_eta

    pts = list(treeHits.L1Mu_pt)
    #print "\tN L1Mus event", len(pts)
    for i in range(0,len(pts)):
        L1Mu_pt = treeHits.L1Mu_pt[i]
        L1Mu_eta = treeHits.L1Mu_eta[i]
        L1Mu_phi = treeHits.L1Mu_phi[i]
        L1Mu_bx = treeHits.L1Mu_bx[i]
        L1Mu_quality = treeHits.L1Mu_quality[i]
        L1Mu_CSCTF_index = treeHits.L1Mu_CSCTF_index[i]
        L1Mu_DTTF_index = treeHits.L1Mu_DTTF_index[i]

        L1Mu_eta_ME2 = -99

        """
        ## get the DTTF index
        getDTTFindex = True
        if getDTTFindex:
            iDTTF_index = -1
            iDTTF_dEta = 99
            for iDTTF in range(0,len(treeHits.DTTF_bx)):
                if treeHits.DTTF_bx[iDTTF] == L1Mu_bx and deltaPhi2(L1Mu_phi, treeHits.DTTF_phi[iDTTF])<0.001:
                    iDTTF_index = iDTTF
                    #print "found index",
            L1Mu_DTTF_index = iDTTF_index

        """

        ## eta cut
        if not (etaCutMin <= abs(L1Mu_eta) and abs(L1Mu_eta) < etaCutMax): continue

        ## quality cut
        if L1Mu_quality < qualityCut: continue

        ## BX cut
        if abs(L1Mu_bx)>0 and doBXCut: continue

        ## CSC quantities
        has_CSC_ME1 = False
        has_CSC_ME2 = False
        has_actual_CSC_ME1 = False
        has_actual_CSC_ME2 = False
        has_CSC_ME3 = False
        has_CSC_ME4 = False
        has_CSC_ME11 = False
        has_CSC_ME21 = False
        is_CSC_ME11_disabled = False
        is_CSC_ME21_disabled = False
        has_GE11 = False
        has_GE21 = False
        GE11_dPhi = 99
        CSC_ME1_ch = -1
        CSC_ME2_ch = -2
        nCSCStubs = 0

        ## DT quantities
        has_DT_MB1 = False
        has_DT_MB2 = False
        has_DT_MB3 = False
        has_DT_MB4 = False
        nDTStubs = 0

        #print L1Mu_CSCTF_index
        #print L1Mu_CSCTF_index, len(treeHits.CSCTF_bx1)
        if L1Mu_CSCTF_index != -1 and L1Mu_CSCTF_index < len(treeHits.CSCTF_phi1):
            has_CSC_ME1 = treeHits.CSCTF_phi1[L1Mu_CSCTF_index] != 99
            has_CSC_ME2 = treeHits.CSCTF_phi2[L1Mu_CSCTF_index] != 99
            has_CSC_ME3 = treeHits.CSCTF_phi3[L1Mu_CSCTF_index] != 99
            has_CSC_ME4 = treeHits.CSCTF_phi4[L1Mu_CSCTF_index] != 99

            L1Mu_eta_ME2 = treeHits.CSCTF_eta2[L1Mu_CSCTF_index]

            if hasME1Cut and not has_CSC_ME1: continue
            if hasME2Cut and not has_CSC_ME2: continue
            if hasME3Cut and not has_CSC_ME3: continue
            if hasME4Cut and not has_CSC_ME4: continue

            has_CSC_ME11 = treeHits.CSCTF_ri1[L1Mu_CSCTF_index] == 1 or treeHits.CSCTF_ri1[L1Mu_CSCTF_index] == 4
            has_CSC_ME21 = treeHits.CSCTF_ri2[L1Mu_CSCTF_index] == 1

            GE11_phi = getBestValue(treeHits.GE11_phi_L1[L1Mu_CSCTF_index], treeHits.GE11_phi_L2[L1Mu_CSCTF_index])
            GE21_phi = getBestValue(treeHits.GE21_pad2_phi_L1[L1Mu_CSCTF_index], treeHits.GE21_pad2_phi_L2[L1Mu_CSCTF_index])

            GE11_dPhi = treeHits.CSCTF_phi1[L1Mu_CSCTF_index] - GE11_phi
            GE21_dPhi = treeHits.CSCTF_phi2[L1Mu_CSCTF_index] - GE21_phi

            CSC_ME1_ch  = treeHits.CSCTF_ch1[L1Mu_CSCTF_index]
            CSC_ME2_ch  = treeHits.CSCTF_ch2[L1Mu_CSCTF_index]

            """
            re-enable this to disable a certain percentage of CSC
            is_CSC_ME11_disabled = isME11StubDisabled(ME11FailRate)
            is_CSC_ME21_disabled = isME21StubDisabled(ME21FailRate)

            if hasME11Cut and not has_CSC_ME11 and not is_CSC_ME11_disabled: continue
            if hasME21Cut and not has_CSC_ME21 and not is_CSC_ME21_disabled: continue

            ## check if stubs in station 1 and 2 can really be counted! -- they may be disabled
            if not has_CSC_ME11: has_actual_CSC_ME1 = has_CSC_ME1
            else:                has_actual_CSC_ME1 = (not is_CSC_ME11_disabled)

            if not has_CSC_ME21: has_actual_CSC_ME2 = has_CSC_ME2
            else:                has_actual_CSC_ME2 = (not is_CSC_ME21_disabled)
            """

            nCSCStubs = has_CSC_ME1 + has_CSC_ME2 + has_CSC_ME3 + has_CSC_ME4
            if nCSCStubs < stubCut: continue

            if hasME11Cut and not has_CSC_ME11: continue
            if hasME21Cut and not has_CSC_ME21: continue
            #print "is csc muon"
            #print "\t", nCSCStubs

            ## OR of ME11 and ME21
            if (hasME11ME21Cut and not (has_CSC_ME11 or has_CSC_ME21)): continue

            ## no bending angles
            if is_CSC_ME11_disabled: GE11_dPhi = 99
            if is_CSC_ME21_disabled: GE21_dPhi = 99

            if hasGE11Cut and not passDPhicutTFTrack(1, CSC_ME1_ch, GE11_dPhi, L1Mu_pt):
                #print "muon failed the GE11 cut", CSC_ME1_ch, GE11_dPhi, L1Mu_pt
                continue
            if hasGE21Cut and not passDPhicutTFTrack(2, CSC_ME2_ch, GE21_dPhi, L1Mu_pt):
                #print "muon failed the GE21 cut", CSC_ME1_ch, GE11_dPhi, L1Mu_pt
                continue
            if (hasGE11GE21Cut and not (passDPhicutTFTrack(1, CSC_ME1_ch, GE11_dPhi, L1Mu_pt) or
                                        passDPhicutTFTrack(2, CSC_ME2_ch, GE21_dPhi, L1Mu_pt))): continue


        if L1Mu_DTTF_index != -1 and L1Mu_DTTF_index < len(treeHits.DTTF_phi1):
            has_DT_MB1 = treeHits.DTTF_phi1[L1Mu_DTTF_index] != 99
            has_DT_MB2 = treeHits.DTTF_phi2[L1Mu_DTTF_index] != 99
            has_DT_MB3 = treeHits.DTTF_phi3[L1Mu_DTTF_index] != 99
            has_DT_MB4 = treeHits.DTTF_phi4[L1Mu_DTTF_index] != 99

            if hasMB1Cut and not has_DT_MB1: continue
            if hasMB2Cut and not has_DT_MB2: continue
            if hasMB3Cut and not has_DT_MB3: continue
            if hasMB4Cut and not has_DT_MB4: continue

            nDTStubs = has_DT_MB1 + has_DT_MB2 + has_DT_MB3 + has_DT_MB4
            if nDTStubs < stubCut: continue
            #print "is dt muon"
            #print "\t", nDTStubs

        ## define the L1Mu objects!!
        is_CSC_Muon =   (1.2 <= abs(L1Mu_eta) and abs(L1Mu_eta) <= 2.4) and L1Mu_CSCTF_index != -1
        is_DT_Muon =    (0.0 <= abs(L1Mu_eta) and abs(L1Mu_eta) <= 0.9) and L1Mu_DTTF_index != -1
        is_DTCSC_Muon = (0.9 <= abs(L1Mu_eta) and abs(L1Mu_eta) <= 1.2) and (L1Mu_DTTF_index != -1 or L1Mu_CSCTF_index != -1)

        ## muon must be DT or CSC (no RPC)
        #if not (is_DT_Muon or is_CSC_Muon):
        #    continue

        if False:
            print "\t\tMatched: L1Mu", "pt", L1Mu_pt, "eta", L1Mu_eta,
            print "phi", L1Mu_phi, "Quality", L1Mu_quality, "L1mu_bx", L1Mu_bx,
            print "L1Mu_CSCTF_index", L1Mu_CSCTF_index, "nCSCStubs", nCSCStubs,
            print "L1Mu_DTTF_index", L1Mu_DTTF_index, "nDTStubs", nDTStubs,
            #print "Displaced_L1Mu_pt", Displaced_L1Mu_pt
            print

        #if L1Mu_bx==0:
        #  print k,i, "pt", L1Mu_pt, "eta", L1Mu_eta, "phi", L1Mu_phi, "bx", L1Mu_bx, "quality", L1Mu_quality

        ## calculate the max pT for the muons that pass the criteria
        if L1Mu_pt > max_prompt_L1Mu_pt:
            max_prompt_L1Mu_pt = L1Mu_pt
            max_prompt_L1Mu_eta = L1Mu_eta#L1Mu_eta

    return max_prompt_L1Mu_pt, max_prompt_L1Mu_eta



"""
## calculate the displaced L1Mu pT
doComparatorFit = True
Displaced_L1Mu_pt = pt_endcap_position_based_algorithm(treeHits, i, L1Mu_CSCTF_index, doComparatorFit)
isIsolated = is_L1Mu_isolated(treeHits, i, 0.4, 4, 0.12, 0)
"""

def fillDisplacedHistogram(mapTH1F,
                           key,
                           treeHits,
                           etaCutMin,
                           etaCutMax,
                           stubCut,
                           hasMB1Cut=False,
                           hasMB2Cut=False,
                           hasMB3Cut=False,
                           hasMB4Cut=False,
                           algorithm=0,
                           vetoType=0):
    doBXCut = True
    qualityCut=4
    displaced_L1Mu_pt, displaced_L1Mu_eta = getMaxDisplacedPtEtaEvent(treeHits,
                                                                      doBXCut,
                                                                      etaCutMin,
                                                                      etaCutMax,
                                                                      stubCut,
                                                                      qualityCut,
                                                                      hasMB1Cut,
                                                                      hasMB2Cut,
                                                                      hasMB3Cut,
                                                                      hasMB4Cut,
                                                                      algorithm,
                                                                      vetoType)
    if (displaced_L1Mu_pt>0):
        mapTH1F[key.replace("rate_", "rate_pt_")].Fill(displaced_L1Mu_pt)
    ## apply a 7/10 GeV pT cut for the eta histograms!!!
    if (displaced_L1Mu_pt>=7):
        mapTH1F[key.replace("rate_", "rate_eta_L1Pt7_")].Fill(abs(displaced_L1Mu_eta))
    if (displaced_L1Mu_pt>=10):
        mapTH1F[key.replace("rate_", "rate_eta_L1Pt10_")].Fill(abs(displaced_L1Mu_eta))



## 1: postion based endcap
## 2: direction based endcap
## 3: hybrid endcap
## 4: direction based barrel
displaced_pt_methods = [1, 2, 3]

def getMaxDisplacedPtEtaEvent(treeHits,
                              doBXCut,
                              etaCutMin,
                              etaCutMax,
                              stubCut,
                              qualityCut,
                              hasMB1Cut=False,
                              hasMB2Cut=False,
                              hasMB3Cut=False,
                              hasMB4Cut=False,
                              algorithm=0,
                              vetoType=0):

    max_displaced_L1Mu_pt = -1
    max_displaced_L1Mu_eta = -99

    ## check if this event has L1Mus
    if len(list(treeHits.L1Mu_pt))==0:
        return max_displaced_L1Mu_pt, max_displaced_L1Mu_eta

    pts = list(treeHits.L1Mu_pt)
    for i in range(0,len(pts)):

        L1Mu_eta = treeHits.L1Mu_eta[i]
        L1Mu_bx = treeHits.L1Mu_bx[i]
        L1Mu_quality = treeHits.L1Mu_quality[i]

        ## quality cut
        if L1Mu_quality < qualityCut: continue

        ## BX cut
        if abs(L1Mu_bx)>0 and doBXCut: continue

        ## check if muon is isolated
        if (vetoType!=0) and (not is_L1Mu_isolated(treeHits, i, vetoType)): continue

        ## eta cut
        #if not (etaCutMin <= abs(L1Mu_eta) and abs(L1Mu_eta) <= etaCutMax): continue

        L1Mu_CSCTF_index = treeHits.L1Mu_CSCTF_index[i]
        L1Mu_DTTF_index = treeHits.L1Mu_DTTF_index[i]
        L1Mu_eta_ME2 = -99

        ## define the L1Mu objects!!
        is_CSC_Muon =   (1.2 <= abs(L1Mu_eta) and abs(L1Mu_eta) <= 2.4) and L1Mu_CSCTF_index != -1
        is_DT_Muon =    (0.0 <= abs(L1Mu_eta) and abs(L1Mu_eta) <= 0.9) and L1Mu_DTTF_index != -1
        is_DTCSC_Muon = (0.9 <= abs(L1Mu_eta) and abs(L1Mu_eta) <= 1.2) and (L1Mu_DTTF_index != -1 or L1Mu_CSCTF_index != -1)

        ## CSC quantities
        has_CSC_ME1 = False
        has_CSC_ME2 = False
        has_CSC_ME3 = False
        has_CSC_ME4 = False
        has_actual_CSC_ME1 = False
        has_actual_CSC_ME2 = False
        has_CSC_ME11 = False
        has_CSC_ME21 = False
        is_CSC_ME11_disabled = False
        is_CSC_ME21_disabled = False
        GE11_dPhi = 99
        CSC_ME1_ch = -1
        CSC_ME2_ch = -2
        nCSCStubs = 0
        CSCTF_eta2 = -99


        ## DT quantities
        has_DT_MB1 = False
        has_DT_MB2 = False
        has_DT_MB3 = False
        has_DT_MB4 = False
        nDTStubs = 0

        DisplacedL1Mu_pt, DisplacedL1Mu_eta = -1, -1

        #print L1Mu_CSCTF_index
        if L1Mu_CSCTF_index != -1 and L1Mu_CSCTF_index < len(treeHits.CSCTF_phi1):
            has_CSC_ME1 = treeHits.CSCTF_phi1[L1Mu_CSCTF_index] != 99
            has_CSC_ME2 = treeHits.CSCTF_phi2[L1Mu_CSCTF_index] != 99
            has_CSC_ME3 = treeHits.CSCTF_phi3[L1Mu_CSCTF_index] != 99
            has_CSC_ME4 = treeHits.CSCTF_phi4[L1Mu_CSCTF_index] != 99

            L1Mu_eta_ME2 = treeHits.CSCTF_eta2[L1Mu_CSCTF_index]

            has_CSC_ME11 = treeHits.CSCTF_ri1[L1Mu_CSCTF_index] == 1 or treeHits.CSCTF_ri1[L1Mu_CSCTF_index] == 4
            has_CSC_ME21 = treeHits.CSCTF_ri2[L1Mu_CSCTF_index] == 1

            CSC_ME1_ch  = treeHits.CSCTF_ch1[L1Mu_CSCTF_index]
            CSC_ME2_ch  = treeHits.CSCTF_ch2[L1Mu_CSCTF_index]
            CSCTF_eta2 = treeHits.CSCTF_eta2[L1Mu_CSCTF_index]

            ## check if stubs in station 1 and 2 can really be counted! -- they may be disabled
            if not has_CSC_ME11: has_actual_CSC_ME1 = has_CSC_ME1
            else:                has_actual_CSC_ME1 = (not is_CSC_ME11_disabled)

            if not has_CSC_ME21: has_actual_CSC_ME2 = has_CSC_ME2
            else:                has_actual_CSC_ME2 = (not is_CSC_ME21_disabled)

            L1Mu_eta = treeHits.CSCTF_L1_eta_st2[L1Mu_CSCTF_index]

            if not (etaCutMin <= abs(L1Mu_eta_ME2) and abs(L1Mu_eta_ME2) <= etaCutMax): continue

            ## position based
            if algorithm==1: DisplacedL1Mu_pt, DisplacedL1Mu_eta = pt_endcap_position_based_algorithm(treeHits, i, True)
            ## direction based - no GE21
            if algorithm==2: DisplacedL1Mu_pt, DisplacedL1Mu_eta = pt_endcap_direction_based_algorithm(treeHits, i, False)
            ## direction based - with GE21
            if algorithm==3: DisplacedL1Mu_pt, DisplacedL1Mu_eta = pt_endcap_direction_based_algorithm(treeHits, i, True)
            ## hybrid based - no GE21
            if algorithm==4: DisplacedL1Mu_pt, DisplacedL1Mu_eta = pt_endcap_hybrid_algorithm(treeHits, i, False)
            ## hybrid based - with GE21
            if algorithm==5: DisplacedL1Mu_pt, DisplacedL1Mu_eta = pt_endcap_hybrid_algorithm(treeHits, i, True)

        #print L1Mu_DTTF_index
        if is_DT_Muon:
            has_DT_MB1 = treeHits.DTTF_phi1[L1Mu_DTTF_index] != 99 and treeHits.DTTF_phib1[L1Mu_DTTF_index] != 99
            has_DT_MB2 = treeHits.DTTF_phi2[L1Mu_DTTF_index] != 99 and treeHits.DTTF_phib2[L1Mu_DTTF_index] != 99
            has_DT_MB3 = treeHits.DTTF_phi3[L1Mu_DTTF_index] != 99 and treeHits.DTTF_phib3[L1Mu_DTTF_index] != 99
            has_DT_MB4 = treeHits.DTTF_phi4[L1Mu_DTTF_index] != 99 and treeHits.DTTF_phib4[L1Mu_DTTF_index] != 99

            if hasMB1Cut and not has_DT_MB1: continue
            if hasMB2Cut and not has_DT_MB2: continue
            if hasMB3Cut and not has_DT_MB3: continue
            if hasMB4Cut and not has_DT_MB4: continue

            DisplacedL1Mu_pt, DisplacedL1Mu_eta = -1, -1

        ## calculate the max pT for the muons that pass the criteria
        if DisplacedL1Mu_pt > max_displaced_L1Mu_pt:
            max_displaced_L1Mu_pt = DisplacedL1Mu_pt
            max_displaced_L1Mu_eta = DisplacedL1Mu_eta

    return max_displaced_L1Mu_pt, max_displaced_L1Mu_eta
