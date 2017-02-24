## this file contains the pT assignment functions
from Helpers import *
from ROOT import *

## important ranges
DTCombinations = ['DT1_DT2','DT1_DT3','DT1_DT4',
                  'DT2_DT3','DT2_DT4','DT3_DT4']
ME1ME2ParityCases = ['oe','oo','ee','eo']
ME1ME2ParityCasesString = ['odd-even','odd-odd','even-even','even-odd']
ME1ME2ME3ParityCases = ['oee','ooo','eee','eoo']
dxyRanges = ['','_dxy0to5','_dxy5to50','_dxy50to100']
dxyRangesString = ['','|dxy| #leq 5 cm','5 < |dxy| #leq 50 cm','50 < |dxy| #leq 100 cm']
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

## calculate the bending in each station
def get_phi_dir_st1(delta_z_GE11_ME11, me11_phi, ge11_phi, Xvalue):
    numerator = TMath.Sin( deltaPhi2(me11_phi, ge11_phi) )
    denominator1 = 1. - TMath.Cos( deltaPhi2(me11_phi, ge11_phi) )
    denominator2 = delta_z_GE11_ME11 * Xvalue
    denominator = denominator1 - denominator2
    return ge11_phi - TMath.ATan( numerator / denominator)

def get_phi_dir_st2_variable_GE21_pad_size(delta_z_GE21_ME21, delta_z_ME11_ME21, me11_phi, me21_phi, ge21_phi, Xvalue):
    numerator = TMath.Sin( deltaPhi2(me21_phi, ge21_phi) )
    denominator1 = 1 - TMath.Cos( deltaPhi2(me21_phi, ge21_phi) )
    denominator2 = (delta_z_GE21_ME21 * Xvalue / (delta_z_ME11_ME21 * Xvalue + 1 ) )
    denominator = denominator1 - denominator2
    return ge21_phi - TMath.ATan( numerator / denominator )


def pt_barrel_direction_based_algorithm(treeHits,
                                        L1Mu_index, algorithm):
    returnValue = 0


    ## L1Mu variables
    L1Mu_pt = treeHits.L1Mu_pt[L1Mu_index]
    L1Mu_eta = treeHits.L1Mu_eta[L1Mu_index]
    L1Mu_bx = treeHits.L1Mu_bx[L1Mu_index]
    L1Mu_quality = treeHits.L1Mu_quality[L1Mu_index]
    L1Mu_DTTF_index = treeHits.L1Mu_DTTF_index[L1Mu_index]

    ## DT variables
    DTTF_eta = treeHits.DTTF_eta[L1Mu_DTTF_index]
    DTTF_nStubs = treeHits.DTTF_nStubs[L1Mu_DTTF_index]

    DTTF_phi1 = treeHits.DTTF_phi1[L1Mu_DTTF_index]
    DTTF_phi2 = treeHits.DTTF_phi2[L1Mu_DTTF_index]
    DTTF_phi3 = treeHits.DTTF_phi3[L1Mu_DTTF_index]
    DTTF_phi4 = treeHits.DTTF_phi4[L1Mu_DTTF_index]

    DTTF_phib1 = treeHits.DTTF_phib1[L1Mu_DTTF_index]
    DTTF_phib2 = treeHits.DTTF_phib2[L1Mu_DTTF_index]
    DTTF_phib3 = treeHits.DTTF_phib3[L1Mu_DTTF_index]
    DTTF_phib4 = treeHits.DTTF_phib4[L1Mu_DTTF_index]

    ok_DTTF_st1 = DTTF_phib1 != 99 and DTTF_phi1 != 99
    ok_DTTF_st2 = DTTF_phib2 != 99 and DTTF_phi2 != 99
    ok_DTTF_st3 = DTTF_phib3 != 99 and DTTF_phi3 != 99
    ok_DTTF_st4 = DTTF_phib4 != 99 and DTTF_phi4 != 99

    ## calculate the real bending
    DTTF_phib1 = normalizedPhi(DTTF_phib1 + DTTF_phi1)
    DTTF_phib2 = normalizedPhi(DTTF_phib2 + DTTF_phi2)
    DTTF_phib3 = normalizedPhi(DTTF_phib3 + DTTF_phi3)
    DTTF_phib4 = normalizedPhi(DTTF_phib4 + DTTF_phi4)

    ## inputs to the pt algorithms
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

    L1Mu_DT_status = L1Mu_status(DTTF_phib1, DTTF_phib2, DTTF_phib3, DTTF_phib4)
    
    ## get the pT for this muon
    if ok_DTTF_st1 and ok_DTTF_st2 and not ok_DTTF_st3 and not ok_DTTF_st4 and algorithm is 1: returnValue = pt_from_DPhi_DT(abs_DTTF_phib1_phib2, 'DT1_DT2')
    if ok_DTTF_st1 and ok_DTTF_st3 and not ok_DTTF_st2 and not ok_DTTF_st4 and algorithm is 2: returnValue = pt_from_DPhi_DT(abs_DTTF_phib1_phib3, 'DT1_DT3')
    if ok_DTTF_st1 and ok_DTTF_st4 and not ok_DTTF_st2 and not ok_DTTF_st3 and algorithm is 3: returnValue = pt_from_DPhi_DT(abs_DTTF_phib1_phib4, 'DT1_DT4')
    if ok_DTTF_st2 and ok_DTTF_st3 and not ok_DTTF_st1 and not ok_DTTF_st4 and algorithm is 4: returnValue = pt_from_DPhi_DT(abs_DTTF_phib2_phib3, 'DT2_DT3')
    if ok_DTTF_st2 and ok_DTTF_st4 and not ok_DTTF_st1 and not ok_DTTF_st3 and algorithm is 5: returnValue = pt_from_DPhi_DT(abs_DTTF_phib2_phib4, 'DT2_DT4')
    if ok_DTTF_st3 and ok_DTTF_st4 and not ok_DTTF_st1 and not ok_DTTF_st2 and algorithm is 6: returnValue = pt_from_DPhi_DT(abs_DTTF_phib3_phib4, 'DT3_DT4')
    if algorithm is 7: 
        if ok_DTTF_st1 and ok_DTTF_st4: returnValue = pt_from_DPhi_DT(abs_DTTF_phib1_phib4, 'DT1_DT4')
        else:
            if (ok_DTTF_st1 and ok_DTTF_st3) or (ok_DTTF_st2 and ok_DTTF_st4):
                if ok_DTTF_st1 and ok_DTTF_st3: returnValue = pt_from_DPhi_DT(abs_DTTF_phib1_phib3, 'DT1_DT3')
                if ok_DTTF_st2 and ok_DTTF_st4: returnValue = pt_from_DPhi_DT(abs_DTTF_phib2_phib4, 'DT2_DT4')
            else:
                if ok_DTTF_st1 and ok_DTTF_st2: returnValue = pt_from_DPhi_DT(abs_DTTF_phib1_phib2, 'DT1_DT2')
                if ok_DTTF_st2 and ok_DTTF_st3: returnValue = pt_from_DPhi_DT(abs_DTTF_phib2_phib3, 'DT2_DT3')
                if ok_DTTF_st3 and ok_DTTF_st4: returnValue = pt_from_DPhi_DT(abs_DTTF_phib3_phib4, 'DT3_DT4')
    
    if algorithm is 8:
        if ok_DTTF_st1 and ok_DTTF_st2 and not ok_DTTF_st3 and not ok_DTTF_st4: returnValue = pt_from_DPhi_DT(abs_DTTF_phib1_phib2, 'DT1_DT2')
        if ok_DTTF_st1 and ok_DTTF_st3 and not ok_DTTF_st2 and not ok_DTTF_st4: returnValue = pt_from_DPhi_DT(abs_DTTF_phib1_phib3, 'DT1_DT3')
        if ok_DTTF_st1 and ok_DTTF_st4 and not ok_DTTF_st2 and not ok_DTTF_st3: returnValue = pt_from_DPhi_DT(abs_DTTF_phib1_phib4, 'DT1_DT4')
        if ok_DTTF_st2 and ok_DTTF_st3 and not ok_DTTF_st1 and not ok_DTTF_st4: returnValue = pt_from_DPhi_DT(abs_DTTF_phib2_phib3, 'DT2_DT3')
        if ok_DTTF_st2 and ok_DTTF_st4 and not ok_DTTF_st1 and not ok_DTTF_st3: returnValue = pt_from_DPhi_DT(abs_DTTF_phib2_phib4, 'DT2_DT4')
        if ok_DTTF_st3 and ok_DTTF_st4 and not ok_DTTF_st1 and not ok_DTTF_st2: returnValue = pt_from_DPhi_DT(abs_DTTF_phib3_phib4, 'DT3_DT4')

    return returnValue, L1Mu_eta

def pt_endcap_position_based_algorithm(treeHits, L1Mu_index, doComparatorFit):
    '''First argument is the analysis tree. Second argument is the L1Mu to CSCTF index'''
    returnValue = 0

    ## L1Mu variables
    L1Mu_eta = treeHits.L1Mu_eta[L1Mu_index]
    L1Mu_bx = treeHits.L1Mu_bx[L1Mu_index]
    L1Mu_quality = treeHits.L1Mu_quality[L1Mu_index]
    L1Mu_CSCTF_index = treeHits.L1Mu_CSCTF_index[L1Mu_index]

    ## CSC variables
    CSCTF_eta = treeHits.CSCTF_eta[L1Mu_CSCTF_index]
    CSCTF_nStubs = treeHits.CSCTF_nStubs[L1Mu_CSCTF_index]

    CSCTF_phi1 = treeHits.CSCTF_phi1[L1Mu_CSCTF_index]
    CSCTF_phi2 = treeHits.CSCTF_phi2[L1Mu_CSCTF_index]
    CSCTF_phi3 = treeHits.CSCTF_phi3[L1Mu_CSCTF_index]
    CSCTF_phi4 = treeHits.CSCTF_phi4[L1Mu_CSCTF_index]

    CSCTF_eta1 = treeHits.CSCTF_eta1[L1Mu_CSCTF_index]
    CSCTF_eta2 = treeHits.CSCTF_eta2[L1Mu_CSCTF_index]
    CSCTF_eta3 = treeHits.CSCTF_eta3[L1Mu_CSCTF_index]
    CSCTF_eta4 = treeHits.CSCTF_eta4[L1Mu_CSCTF_index]

    ## check if ME1, ME2 and ME3 are available
    ok_CSCTF_st1 = CSCTF_phi1 != 99
    ok_CSCTF_st2 = CSCTF_phi2 != 99
    ok_CSCTF_st3 = CSCTF_phi3 != 99
    ok_CSCTF_st4 = CSCTF_phi4 != 99

    CSCTF_ch1 = treeHits.CSCTF_ch1[L1Mu_CSCTF_index]
    CSCTF_ch2 = treeHits.CSCTF_ch2[L1Mu_CSCTF_index]
    CSCTF_ch3 = treeHits.CSCTF_ch3[L1Mu_CSCTF_index]
    CSCTF_ch4 = treeHits.CSCTF_ch4[L1Mu_CSCTF_index]

    CSCTF_isEven1 = CSCTF_ch1%2==0
    CSCTF_isEven2 = CSCTF_ch2%2==0
    CSCTF_isEven3 = CSCTF_ch3%2==0
    CSCTF_isEven4 = CSCTF_ch4%2==0

    CSCTF_L1_DDY123 = treeHits.CSCTF_L1_DDY123[L1Mu_CSCTF_index] 
    #if CSCTF_L1_DDY123!=99:
        #if (not (ok_CSCTF_st1 and ok_CSCTF_st2 and ok_CSCTF_st3)):
            #print "AllTracks, DDY123_L1 ",CSCTF_L1_DDY123, " CSCTF_phi1 ",CSCTF_phi1," CSCTF_phi2 ",CSCTF_phi2," CSCTF_phi3 ",CSCTF_phi3
            
    ## actual calctulation of the pT
    if ok_CSCTF_st1 and ok_CSCTF_st2 and ok_CSCTF_st3:
        #returnValue = treeHits.CSCTF_L1_position_pt[L1Mu_CSCTF_index]
        DDY123_L1 = abs(treeHits.CSCTF_L1_DDY123[L1Mu_CSCTF_index])
        parity3 = get_parity(CSCTF_isEven1, CSCTF_isEven2, CSCTF_isEven3, CSCTF_isEven4)
        etaPartition = get_eta_partition(CSCTF_eta2)
        returnValue = pt_from_DDY123_Tao(DDY123_L1, etaRanges[etaPartition], ME1ME2ME3ParityCases[parity3], doComparatorFit)

    return returnValue, CSCTF_eta2

def pt_endcap_direction_based_algorithm(treeHits, L1Mu_index, useGE21):

    returnValue = 0

    ## L1Mu variables
    L1Mu_CSCTF_index = treeHits.L1Mu_CSCTF_index[L1Mu_index]

    ## CSC variables
    CSCTF_phi1 = treeHits.CSCTF_phi1[L1Mu_CSCTF_index]
    CSCTF_phi2 = treeHits.CSCTF_phi2[L1Mu_CSCTF_index]

    CSCTF_eta1 = treeHits.CSCTF_eta1[L1Mu_CSCTF_index]
    CSCTF_eta2 = treeHits.CSCTF_eta2[L1Mu_CSCTF_index]

    ## check if ME1, ME2 and ME3 are available
    ok_CSCTF_st1 = CSCTF_phi1 != 99
    ok_CSCTF_st2 = CSCTF_phi2 != 99

    CSCTF_ch1 = treeHits.CSCTF_ch1[L1Mu_CSCTF_index]
    CSCTF_ch2 = treeHits.CSCTF_ch2[L1Mu_CSCTF_index]
    CSCTF_ch3 = treeHits.CSCTF_ch3[L1Mu_CSCTF_index]
    CSCTF_ch4 = treeHits.CSCTF_ch4[L1Mu_CSCTF_index]

    CSCTF_isEven1 = CSCTF_ch1%2==0
    CSCTF_isEven2 = CSCTF_ch2%2==0
    CSCTF_isEven3 = CSCTF_ch3%2==0
    CSCTF_isEven4 = CSCTF_ch4%2==0

    GE11_phi_L1 = treeHits.GE11_phi_L1[L1Mu_CSCTF_index]
    GE11_phi_L2 = treeHits.GE11_phi_L2[L1Mu_CSCTF_index]
    GE21_phi_L1 = treeHits.GE21_phi_L1[L1Mu_CSCTF_index]
    GE21_phi_L2 = treeHits.GE21_phi_L2[L1Mu_CSCTF_index]

    ok_GE11 = GE11_phi_L1 != 99 or GE11_phi_L2 != 99
    ok_GE21 = GE21_phi_L1 != 99 or GE21_phi_L2 != 99

    #ok_GE11 = treeHits.CSCTF_gemdphi1[L1Mu_CSCTF_index] != 99
    #ok_GE21 = treeHits.CSCTF_gemdphi2[L1Mu_CSCTF_index] != 99

    ## actual calctulation of the pT
    if useGE21:
        if ok_CSCTF_st1 and ok_CSCTF_st2 and ok_GE11 and ok_GE21:
            returnValue = treeHits.CSCTF_L1_direction_pt_noGE21[L1Mu_CSCTF_index]
    else:
        if ok_CSCTF_st1 and ok_CSCTF_st2 and ok_GE11:
            returnValue = treeHits.CSCTF_L1_direction_pt_GE21[L1Mu_CSCTF_index]
        #DPhi = abs(treeHits.CSCTF_L1_DPhi12_GE21[L1Mu_CSCTF_index])
        #parity3 = get_parity(CSCTF_isEven1, CSCTF_isEven2, CSCTF_isEven3, CSCTF_isEven4)
        #etaPartition = get_eta_partition(CSCTF_eta2)

        ## get the reconstruction pT value
        #returnValue = pt_from_dPhi_GE21(DPhi, etaRanges[etaPartition], ME1ME2ME3ParityCases[parity3])
    
    return returnValue, CSCTF_eta2

def pt_endcap_hybrid_algorithm(treeHits, L1Mu_index, useGE21):

    returnValue = 0

    ## L1Mu variables
    L1Mu_CSCTF_index = treeHits.L1Mu_CSCTF_index[L1Mu_index]

    ## CSC variables
    CSCTF_phi1 = treeHits.CSCTF_phi1[L1Mu_CSCTF_index]
    CSCTF_phi2 = treeHits.CSCTF_phi2[L1Mu_CSCTF_index]
    CSCTF_phi3 = treeHits.CSCTF_phi3[L1Mu_CSCTF_index]

    CSCTF_eta1 = treeHits.CSCTF_eta1[L1Mu_CSCTF_index]
    CSCTF_eta2 = treeHits.CSCTF_eta2[L1Mu_CSCTF_index]
    CSCTF_eta3 = treeHits.CSCTF_eta3[L1Mu_CSCTF_index]
    CSCTF_eta4 = treeHits.CSCTF_eta4[L1Mu_CSCTF_index]

    ## check if ME1, ME2 and ME3 are available
    ok_CSCTF_st1 = CSCTF_phi1 != 99
    ok_CSCTF_st2 = CSCTF_phi2 != 99
    ok_CSCTF_st3 = CSCTF_phi3 != 99

    GE11_phi_L1 = treeHits.GE11_phi_L1[L1Mu_CSCTF_index]
    GE11_phi_L2 = treeHits.GE11_phi_L2[L1Mu_CSCTF_index]
    GE21_phi_L1 = treeHits.GE21_phi_L1[L1Mu_CSCTF_index]
    GE21_phi_L2 = treeHits.GE21_phi_L2[L1Mu_CSCTF_index]

    ok_GE11 = GE11_phi_L1 != 99 or GE11_phi_L2 != 99
    ok_GE21 = GE21_phi_L1 != 99 or GE21_phi_L2 != 99

    if useGE21:
        if ok_CSCTF_st1 and ok_CSCTF_st2 and ok_CSCTF_st3:
            returnValue = treeHits.CSCTF_L1_hybrid_pt_GE21[L1Mu_CSCTF_index]
            #if returnValue == 0.0:  returnValue = 2
            if returnValue == 30.0: returnValue = 120 ## very large value
    else:
        if ok_CSCTF_st1 and ok_CSCTF_st2 and ok_CSCTF_st3:
            returnValue = treeHits.CSCTF_L1_hybrid_pt_noGE21[L1Mu_CSCTF_index]
            #if returnValue == 0.0:  returnValue = 2
            if returnValue == 30.0: returnValue = 120 ## very large value
            
    return returnValue, CSCTF_eta2
    """
        if ok_CSCTF_st1 and ok_CSCTF_st2 and ok_CSCTF_st3 and ok_GE11 and ok_GE21:
            returnValue = treeHits.CSCTF_L1_hybrid_pt_GE21[L1Mu_CSCTF_index]
            if returnValue == 0.0:  returnValue = 2
            if returnValue == 30.0: returnValue = 120 ## very large value

    else:
    """
