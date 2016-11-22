## this file contains functions that check if a L1Mu is isolated
from Helpers import *
from hybridAlgorithmPtAssignment import *
import random

def is_L1Mu_isolated(treeHits, L1Mu_index,
                     dR_largeCone, ptCut_largeCone,
                     dR_smallCone, ptCut_smallCone):
    """checks if muon is isolated from track trigger track"""

    L1Mu_L1Tk_dR_min = treeHits.L1Mu_L1Tk_dR_prop[L1Mu_index]
    L1Mu_L1Tk_pt = treeHits.L1Mu_L1Tk_pt_prop[L1Mu_index]

    isMatched = False
    isUnmatched = False

    ## check if matched or unmatched
    ## L1Tk should have a momentum above a certain threshold to be matched or unmatched
    if L1Mu_L1Tk_dR_min <= dR_largeCone and L1Mu_L1Tk_pt >= ptCut_largeCone: isUnmatched = True
    if L1Mu_L1Tk_dR_min <= dR_smallCone and L1Mu_L1Tk_pt >= ptCut_smallCone: isMatched = True

    ## isolated means neither matched nor unmatched!
    return (not isMatched) and (not isUnmatched)

def isME11StubDisabled(failRate):
    random_number = random.random()
    return random_number < failRate


def isME21StubDisabled(failRate):
    random_number = random.random()
    return random_number < failRate

def fillPtEtaHistogram(ptHistogram,
                       etaHistogram,
                       treeHits,
                       doBXCut,
                       etaCutMin,
                       etaCutMax,
                       stubCut=2,
                       qualityCut=4,
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
        ptHistogram.Fill(prompt_L1Mu_pt)
    ## apply a 10 GeV pT cut for the eta histograms!!!
    #if (prompt_L1Mu_pt>20):
    #print "Max prompt pt, eta event", prompt_L1Mu_pt, prompt_L1Mu_eta
    if (prompt_L1Mu_pt>=20):
        etaHistogram.Fill(abs(prompt_L1Mu_eta))



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

        ## eta cut
        if not (etaCutMin <= abs(L1Mu_eta) and abs(L1Mu_eta) <= etaCutMax): continue

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
        if L1Mu_CSCTF_index != -1 and L1Mu_CSCTF_index < len(treeHits.CSCTF_bx1):
            has_CSC_ME1 = treeHits.CSCTF_bx1[L1Mu_CSCTF_index] != 99
            has_CSC_ME2 = treeHits.CSCTF_bx2[L1Mu_CSCTF_index] != 99
            has_CSC_ME3 = treeHits.CSCTF_bx3[L1Mu_CSCTF_index] != 99
            has_CSC_ME4 = treeHits.CSCTF_bx4[L1Mu_CSCTF_index] != 99

            L1Mu_eta_ME2 = treeHits.CSCTF_eta2[L1Mu_CSCTF_index]

            if hasME1Cut and not has_CSC_ME1: continue
            if hasME2Cut and not has_CSC_ME2: continue
            if hasME3Cut and not has_CSC_ME3: continue
            if hasME4Cut and not has_CSC_ME4: continue

            has_CSC_ME11 = treeHits.CSCTF_ri1[L1Mu_CSCTF_index] == 1 or treeHits.CSCTF_ri1[L1Mu_CSCTF_index] == 4
            has_CSC_ME21 = treeHits.CSCTF_ri2[L1Mu_CSCTF_index] == 1

            if hasME11Cut and not has_CSC_ME11: continue
            if hasME21Cut and not has_CSC_ME21: continue

            GE11_dPhi = treeHits.CSCTF_gemdphi1[L1Mu_CSCTF_index]
            GE21_dPhi = treeHits.CSCTF_gemdphi2[L1Mu_CSCTF_index]

            is_CSC_ME11_disabled = isME11StubDisabled(ME11FailRate)
            is_CSC_ME21_disabled = isME21StubDisabled(ME21FailRate)

            CSC_ME1_ch  = treeHits.CSCTF_ch1[L1Mu_CSCTF_index]
            CSC_ME2_ch  = treeHits.CSCTF_ch2[L1Mu_CSCTF_index]


            if hasGE11Cut and not passDPhicutTFTrack(1, CSC_ME1_ch, GE11_dPhi, L1Mu_pt):
                #print "muon failed the GE11 cut", CSC_ME1_ch, GE11_dPhi, L1Mu_pt
                continue
            if hasGE21Cut and not passDPhicutTFTrack(2, CSC_ME2_ch, GE21_dPhi, L1Mu_pt):
                #print "muon failed the GE21 cut", CSC_ME1_ch, GE11_dPhi, L1Mu_pt
                continue

            if (hasME11ME21Cut and not has_CSC_ME11 and not has_CSC_ME21): continue
            if (hasGE11GE21Cut and (not passDPhicutTFTrack(1, CSC_ME1_ch, GE11_dPhi, L1Mu_pt)) and
                                   (not passDPhicutTFTrack(2, CSC_ME2_ch, GE21_dPhi, L1Mu_pt))): continue

            ## check if stubs in station 1 and 2 can really be counted! -- they may be disabled
            if not has_CSC_ME11: has_actual_CSC_ME1 = has_CSC_ME1
            else:                has_actual_CSC_ME1 = (not is_CSC_ME11_disabled)

            if not has_CSC_ME21: has_actual_CSC_ME2 = has_CSC_ME2
            else:                has_actual_CSC_ME2 = (not is_CSC_ME21_disabled)

            ## no bending angles
            if is_CSC_ME11_disabled: GE11_dPhi = 99
            if is_CSC_ME21_disabled: GE21_dPhi = 99

            nCSCStubs = has_actual_CSC_ME1 + has_actual_CSC_ME2 + has_CSC_ME3 + has_CSC_ME4
            if nCSCStubs < stubCut: continue
            #print "is csc muon"
            #print "\t", nCSCStubs

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
            max_prompt_L1Mu_eta = L1Mu_eta_ME2#L1Mu_eta

    return max_prompt_L1Mu_pt, max_prompt_L1Mu_eta



"""
## calculate the displaced L1Mu pT
doComparatorFit = True
Displaced_L1Mu_pt = pt_endcap_position_based_algorithm(treeHits, i, L1Mu_CSCTF_index, doComparatorFit)
isIsolated = is_L1Mu_isolated(treeHits, i, 0.4, 4, 0.12, 0)
"""

def fillDisplacedPtEtaHistogram(ptHistogram,
                                etaHistogram,
                                treeHits,
                                doBXCut,
                                etaCutMin,
                                etaCutMax,
                                stubCut,
                                qualityCut,
                                hasMB1Cut=False,
                                hasMB2Cut=False,
                                hasMB3Cut=False,
                                hasMB4Cut=False,
                                doPositionBased=False,
                                doDirectionBased=False,
                                doHybridBased=False):
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
                                                                      doPositionBased,
                                                                      doDirectionBased,
                                                                      doHybridBased)
    #print "check pT ok", displaced_L1Mu_pt
    if (displaced_L1Mu_pt>0):
        ptHistogram.Fill(displaced_L1Mu_pt)
        #print "Max displaced pT event", displaced_L1Mu_pt
    if (displaced_L1Mu_pt>=20):
        etaHistogram.Fill(abs(displaced_L1Mu_eta))
        print "Max displaced pT eta event", displaced_L1Mu_pt, abs(displaced_L1Mu_eta)



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
                              doPositionBased=False,
                              doDirectionBased=False,
                              doHybridBased=False):

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
        L1Mu_CSCTF_index = treeHits.L1Mu_CSCTF_index[i]
        L1Mu_DTTF_index = treeHits.L1Mu_DTTF_index[i]

        L1Mu_eta_ME2 = -99

        ## define the L1Mu objects!!
        is_CSC_Muon =   (1.2 <= abs(L1Mu_eta) and abs(L1Mu_eta) <= 2.4) and L1Mu_CSCTF_index != -1
        is_DT_Muon =    (0.0 <= abs(L1Mu_eta) and abs(L1Mu_eta) <= 0.9) and L1Mu_DTTF_index != -1
        is_DTCSC_Muon = (0.9 <= abs(L1Mu_eta) and abs(L1Mu_eta) <= 1.2) and (L1Mu_DTTF_index != -1 or L1Mu_CSCTF_index != -1)

        ## eta cut
        if not (etaCutMin <= abs(L1Mu_eta) and abs(L1Mu_eta) <= etaCutMax): continue

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

        ## DT quantities
        has_DT_MB1 = False
        has_DT_MB2 = False
        has_DT_MB3 = False
        has_DT_MB4 = False
        nDTStubs = 0

        #print L1Mu_CSCTF_index
        if L1Mu_CSCTF_index != -1 and L1Mu_CSCTF_index < len(treeHits.CSCTF_bx1):
            has_CSC_ME1 = treeHits.CSCTF_bx1[L1Mu_CSCTF_index] != 99
            has_CSC_ME2 = treeHits.CSCTF_bx2[L1Mu_CSCTF_index] != 99
            has_CSC_ME3 = treeHits.CSCTF_bx3[L1Mu_CSCTF_index] != 99
            has_CSC_ME4 = treeHits.CSCTF_bx4[L1Mu_CSCTF_index] != 99

            L1Mu_eta_ME2 = treeHits.CSCTF_eta2[L1Mu_CSCTF_index]

            has_CSC_ME11 = treeHits.CSCTF_ri1[L1Mu_CSCTF_index] == 1 or treeHits.CSCTF_ri1[L1Mu_CSCTF_index] == 4
            has_CSC_ME21 = treeHits.CSCTF_ri2[L1Mu_CSCTF_index] == 1

            CSC_ME1_ch  = treeHits.CSCTF_ch1[L1Mu_CSCTF_index]
            CSC_ME2_ch  = treeHits.CSCTF_ch2[L1Mu_CSCTF_index]

            ## check if stubs in station 1 and 2 can really be counted! -- they may be disabled
            if not has_CSC_ME11: has_actual_CSC_ME1 = has_CSC_ME1
            else:                has_actual_CSC_ME1 = (not is_CSC_ME11_disabled)

            if not has_CSC_ME21: has_actual_CSC_ME2 = has_CSC_ME2
            else:                has_actual_CSC_ME2 = (not is_CSC_ME21_disabled)

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

        ## quality cut
        if L1Mu_quality < qualityCut: continue

        ## BX cut
        if abs(L1Mu_bx)>0 and doBXCut: continue

        #print L1Mu_CSCTF_index
        if is_CSC_Muon:
            if doPositionBased:  DisplacedL1Mu_pt, DisplacedL1Mu_eta = pt_endcap_position_based_algorithm(treeHits, i, True)
            if doDirectionBased: DisplacedL1Mu_pt, DisplacedL1Mu_eta = pt_endcap_direction_based_algorithm(treeHits, i)
            if doHybridBased:    DisplacedL1Mu_pt, DisplacedL1Mu_eta = pt_endcap_hybrid_algorithm(treeHits, i)

        #elif is_DT_Muon:
        #    DisplacedL1Mu_pt = pt_barrel_direction_based_algorithm(treeHits, i,
        #                                                           hasMB1Cut,
        #                                                           hasMB2Cut,
        #                                                           hasMB3Cut,
        #                                                           hasMB4Cut)
        else:
            DisplacedL1Mu_pt = -1

        ## calculate the max pT for the muons that pass the criteria
        if DisplacedL1Mu_pt > max_displaced_L1Mu_pt:
            max_displaced_L1Mu_pt = DisplacedL1Mu_pt
            max_displaced_L1Mu_eta = L1Mu_eta_ME2#DisplacedL1Mu_eta

    return max_displaced_L1Mu_pt, max_displaced_L1Mu_eta
