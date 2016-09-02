## this file contains functions that check if a L1Mu is isolated 
from Helpers import *
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
    if L1Mu_L1Tk_dR_min <= dR_largeCone and L1Mu_L1Tk_pt >= ptCut_largeCone: isUnmatched = True
    if L1Mu_L1Tk_dR_min <= dR_smallCone and L1Mu_L1Tk_pt >= ptCut_smallCone: isMatched = True

    ## isolated means neither matched nor unmatched!
    return (not isMatched) and (not isUnmatched)

def isME11StubDisabled(ME11FailRate):
    random_number = random.random()
    returnValue = False
    if random_number < ME11FailRate: 
        returnValue = True
    return returnValue


def isME21StubDisabled(ME21FailRate):
    random_number = random.random()
    returnValue = False
    if random_number < ME21FailRate: 
        returnValue = True
    return returnValue


def fillPtHistogram(histogram,
                    treeHits, 
                    doBXCut, 
                    etaCutMin, 
                    etaCutMax, 
                    stubCut, 
                    qualityCut, 
                    hasME11Cut=False, 
                    hasME21Cut=False, 
                    hasGE11Cut=False, 
                    hasGE21Cut=False,
                    ME11FailRate=0):
    prompt_L1Mu_pt = getMaxPromptPtEvent(treeHits,doBXCut, etaCutMin, 
                                         etaCutMax, stubCut, qualityCut,
                                         hasME11Cut, hasME21Cut, hasGE11Cut, 
                                         hasGE21Cut, ME11FailRate)
    if (prompt_L1Mu_pt>0): histogram.Fill(prompt_L1Mu_pt)


def getMaxPromptPtEvent(treeHits, 
                        doBXCut, 
                        etaCutMin, 
                        etaCutMax, 
                        stubCut, 
                        qualityCut, 
                        hasME11Cut=False, 
                        hasME21Cut=False, 
                        hasGE11Cut=False, 
                        hasGE21Cut=False,
                        ME11FailRate=0,
                        ME21FailRate=0):
    
    max_prompt_L1Mu_pt = -1

    ## check if this event has L1Mus
    if len(list(treeHits.L1Mu_pt))==0:
        return max_prompt_L1Mu_pt

    pts = list(treeHits.L1Mu_pt)
    for i in range(0,len(pts)):
        L1Mu_pt = treeHits.L1Mu_pt[i]
        L1Mu_eta = treeHits.L1Mu_eta[i]
        L1Mu_phi = treeHits.L1Mu_phi[i]
        L1Mu_bx = treeHits.L1Mu_bx[i]
        L1Mu_quality = treeHits.L1Mu_quality[i]
        L1Mu_CSCTF_index = treeHits.L1Mu_CSCTF_index[i]
        
        ## eta cut
        if not (etaCutMin <= abs(L1Mu_eta) and abs(L1Mu_eta) <= etaCutMax): continue

        ## quality cut
        if L1Mu_quality < qualityCut: continue

        ## BX cut
        if abs(L1Mu_bx)>0 and doBXCut: continue
        
        ## CSC quantities
        has_CSC_ME1 = False
        has_CSC_ME2 = False
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
        
        #print L1Mu_CSCTF_index
        if L1Mu_CSCTF_index != -1:
            has_CSC_ME1 = treeHits.CSCTF_bx1[L1Mu_CSCTF_index] != 99
            has_CSC_ME2 = treeHits.CSCTF_bx2[L1Mu_CSCTF_index] != 99
            has_CSC_ME3 = treeHits.CSCTF_bx3[L1Mu_CSCTF_index] != 99
            has_CSC_ME4 = treeHits.CSCTF_bx4[L1Mu_CSCTF_index] != 99
            has_CSC_ME11 = treeHits.CSCTF_ri1[L1Mu_CSCTF_index] == 1 or treeHits.CSCTF_ri1[L1Mu_CSCTF_index] == 4 
            has_CSC_ME21 = treeHits.CSCTF_ri2[L1Mu_CSCTF_index] == 1
            GE11_dPhi = treeHits.CSCTF_gemdphi1[L1Mu_CSCTF_index]
            GE21_dPhi = treeHits.CSCTF_gemdphi2[L1Mu_CSCTF_index]  
            is_CSC_ME11_disabled = isME11StubDisabled(ME11FailRate)
            is_CSC_ME21_disabled = isME21StubDisabled(ME21FailRate)
            CSC_ME1_ch  = treeHits.CSCTF_ch1[L1Mu_CSCTF_index]
            CSC_ME2_ch  = treeHits.CSCTF_ch2[L1Mu_CSCTF_index]
            
            ## check if stubs are disabled
            has_CSC_ME11 = has_CSC_ME11  and (not is_CSC_ME11_disabled)
            has_CSC_ME21 = has_CSC_ME21  and (not is_CSC_ME21_disabled)
            
            if is_CSC_ME11_disabled: GE11_dPhi = 2
            if is_CSC_ME21_disabled: GE21_dPhi = 2


        nCSCStubs = has_CSC_ME1 + has_CSC_ME2 + has_CSC_ME3 + has_CSC_ME4

        if nCSCStubs < stubCut: continue
        if hasME11Cut and not has_CSC_ME11: continue
        if hasME21Cut and not has_CSC_ME21: continue
        if hasGE11Cut and not passDPhicutTFTrack(1, CSC_ME1_ch, GE11_dPhi, L1Mu_pt): continue
        if hasGE21Cut and not passDPhicutTFTrack(2, CSC_ME2_ch, GE21_dPhi, L1Mu_pt): continue
        
        if False:
            print "\t\tMatched: L1Mu", "pt", L1Mu_pt, "eta", L1Mu_eta, 
            print "phi", L1Mu_phi, "Quality", L1Mu_quality, "L1mu_bx", L1Mu_bx,
            print "L1Mu_CSCTF_index", L1Mu_CSCTF_index, "nCSCStubs", nCSCStubs,
            #print "Displaced_L1Mu_pt", Displaced_L1Mu_pt
            print 
            
        #if L1Mu_bx==0:
        #  print k,i, "pt", L1Mu_pt, "eta", L1Mu_eta, "phi", L1Mu_phi, "bx", L1Mu_bx, "quality", L1Mu_quality
        
        ## calculate the max pT for the muons that pass the criteria
        if L1Mu_pt > max_prompt_L1Mu_pt:   max_prompt_L1Mu_pt = L1Mu_pt

    return max_prompt_L1Mu_pt
        


"""
## calculate the displaced L1Mu pT
doComparatorFit = True
Displaced_L1Mu_pt = pt_endcap_position_based_algorithm(treeHits, i, L1Mu_CSCTF_index, doComparatorFit)
isIsolated = is_L1Mu_isolated(treeHits, i, 0.4, 4, 0.12, 0)
"""
