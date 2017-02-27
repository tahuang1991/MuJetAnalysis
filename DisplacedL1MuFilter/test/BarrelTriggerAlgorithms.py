## this file contains the pT assignment functions
from Helpers import *
from ROOT import *

#______________________________________________________________________________
def pt_from_DPhi_DT(DPhi, DT_type):

    Pt_dict = {}
    DPhi_dict = {}

    binLow = [3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,12.0,14.0,16.0,18.0,20.0,24.0,28.0,32.0,36.0,42.0,50.0]

    Pt_dict['DT1_DT2'] =  [3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0, 36.0, 42.0]
    DPhi_dict['DT1_DT2'] =  [0.4409166666666667, 0.1908051948051948, 0.11985024154589373, 0.09283333333333332, 0.07680000000000001, 0.0643731343283582, 0.05664723926380369, 0.0498625, 0.04719396551724138, 0.043472727272727274, 0.04341355932203391, 0.04370038910505837, 0.044390070921985825, 0.045082089552238816, 0.04535570469798658, 0.04629464285714286, 0.04681428571428572, 0.04832500000000001]

    Pt_dict['DT1_DT3'] =  [3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0, 36.0, 42.0]
    DPhi_dict['DT1_DT3'] =  [0.7153999999999999, 0.52405, 0.28248750000000006, 0.19926244343891406, 0.16401477832512315, 0.13742857142857143, 0.11878896103896104, 0.10268253968253971, 0.08850628366247756, 0.07799284009546541, 0.07045631067961167, 0.06336458333333332, 0.05774454148471616, 0.05411052631578949, 0.0491657458563536, 0.047915094339622655, 0.04808536585365854, 0.048833333333333354]

    Pt_dict['DT1_DT4'] =  [4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0, 36.0, 42.0]
    DPhi_dict['DT1_DT4'] =  [0.7152, 0.45605, 0.30988349514563107, 0.24174789915966385, 0.19359615384615386, 0.15707772020725388, 0.13356491228070178, 0.1064389534883721, 0.08990909090909091, 0.08115068493150687, 0.0722357142857143, 0.0646298076923077, 0.057612021857923516, 0.05361538461538461, 0.04822857142857144, 0.0498918918918919, 0.047575757575757584]

    Pt_dict['DT2_DT3'] =  [3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0, 36.0, 42.0]
    DPhi_dict['DT2_DT3'] =  [0.5790000000000001, 0.38479411764705884, 0.19879850746268657, 0.1410168539325843, 0.11312716763005781, 0.09687843137254902, 0.08549166666666667, 0.07561097256857856, 0.06696994535519125, 0.05906714628297363, 0.054882575757575776, 0.049907161803713525, 0.05138912133891214, 0.0538978494623656, 0.05092452830188681, 0.04774766355140187, 0.05181159420289857, 0.053333333333333344]

    Pt_dict['DT2_DT4'] =  [4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0, 36.0, 42.0]
    DPhi_dict['DT2_DT4'] =  [0.6513333333333334, 0.38794736842105265, 0.26101298701298703, 0.1996214285714286, 0.15861006289308177, 0.13258620689655173, 0.11008032128514056, 0.090284046692607, 0.0772006920415225, 0.06872500000000001, 0.06323648648648648, 0.05838075313807533, 0.05675675675675676, 0.05637974683544305, 0.05084782608695654, 0.0514047619047619, 0.052440000000000014]

    Pt_dict['DT3_DT4'] =  [4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0, 36.0, 42.0]
    DPhi_dict['DT3_DT4'] =  [0.46840000000000004, 0.25570270270270273, 0.16560550458715598, 0.12402958579881657, 0.09708730158730158, 0.08288000000000001, 0.06968926553672317, 0.058116853932584284, 0.052528957528957546, 0.04980503144654089, 0.04863445378151261, 0.04883177570093458, 0.049464135021097054, 0.04774496644295303, 0.04876000000000001, 0.04692857142857144, 0.04775757575757576]

    DPhi_range = DPhi_dict[DT_type]
    pt_range = Pt_dict[DT_type]

    found_pt = 0
    if DPhi > DPhi_range[0]:
      found_pt = 3.5
    elif DPhi < DPhi_range[-1]:
      found_pt = 55
    else:
      for ii in range(0,len(DPhi_range)):
        if DPhi > DPhi_range[ii]:
          found_pt = pt_range[ii-1]
          break

    return found_pt

#______________________________________________________________________________
def pt_barrel_direction_based_algorithm(treeHits,  L1Mu_index, algorithm):
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

    if ok_DTTF_st1 and ok_DTTF_st2 and algorithm is 10: returnValue = pt_from_DPhi_DT(abs_DTTF_phib1_phib2, 'DT1_DT2')
    if ok_DTTF_st1 and ok_DTTF_st3 and algorithm is 11: returnValue = pt_from_DPhi_DT(abs_DTTF_phib1_phib3, 'DT1_DT3')
    if ok_DTTF_st1 and ok_DTTF_st4 and algorithm is 12: returnValue = pt_from_DPhi_DT(abs_DTTF_phib1_phib4, 'DT1_DT4')
    if ok_DTTF_st2 and ok_DTTF_st3 and algorithm is 13: returnValue = pt_from_DPhi_DT(abs_DTTF_phib2_phib3, 'DT2_DT3')
    if ok_DTTF_st2 and ok_DTTF_st4 and algorithm is 14: returnValue = pt_from_DPhi_DT(abs_DTTF_phib2_phib4, 'DT2_DT4')
    if ok_DTTF_st3 and ok_DTTF_st4 and algorithm is 15: returnValue = pt_from_DPhi_DT(abs_DTTF_phib3_phib4, 'DT3_DT4')

    if algorithm is 16:
        ## case 1: 2 stations
        if ok_DTTF_st1 and ok_DTTF_st2 and not ok_DTTF_st3 and not ok_DTTF_st4: returnValue = pt_from_DPhi_DT(abs_DTTF_phib1_phib2, 'DT1_DT2')
        if ok_DTTF_st1 and ok_DTTF_st3 and not ok_DTTF_st2 and not ok_DTTF_st4: returnValue = pt_from_DPhi_DT(abs_DTTF_phib1_phib3, 'DT1_DT3')
        if ok_DTTF_st1 and ok_DTTF_st4 and not ok_DTTF_st2 and not ok_DTTF_st3: returnValue = pt_from_DPhi_DT(abs_DTTF_phib1_phib4, 'DT1_DT4')
        if ok_DTTF_st2 and ok_DTTF_st3 and not ok_DTTF_st1 and not ok_DTTF_st4: returnValue = pt_from_DPhi_DT(abs_DTTF_phib2_phib3, 'DT2_DT3')
        if ok_DTTF_st2 and ok_DTTF_st4 and not ok_DTTF_st1 and not ok_DTTF_st3: returnValue = pt_from_DPhi_DT(abs_DTTF_phib2_phib4, 'DT2_DT4')
        if ok_DTTF_st3 and ok_DTTF_st4 and not ok_DTTF_st1 and not ok_DTTF_st2: returnValue = pt_from_DPhi_DT(abs_DTTF_phib3_phib4, 'DT3_DT4')

        ## case 2: 3 stations
        if     ok_DTTF_st1 and     ok_DTTF_st2 and     ok_DTTF_st3 and not ok_DTTF_st4: returnValue = pt_from_DPhi_DT_ellipse(1, 3, 2, 3, DTTF_phib1_phib3, DTTF_phib2_phib3)
        if     ok_DTTF_st1 and     ok_DTTF_st2 and not ok_DTTF_st3 and     ok_DTTF_st4: returnValue = pt_from_DPhi_DT_ellipse(1, 4, 2, 4, DTTF_phib1_phib4, DTTF_phib2_phib4)
        if     ok_DTTF_st1 and not ok_DTTF_st2 and     ok_DTTF_st3 and not ok_DTTF_st4: returnValue = pt_from_DPhi_DT_ellipse(1, 3, 1, 4, DTTF_phib1_phib3, DTTF_phib1_phib4)
        if not ok_DTTF_st1 and     ok_DTTF_st2 and     ok_DTTF_st3 and     ok_DTTF_st4: returnValue = pt_from_DPhi_DT_ellipse(2, 3, 3, 4, DTTF_phib2_phib3, DTTF_phib3_phib4)

        ## case 3: 4 stations
        if ok_DTTF_st1 and ok_DTTF_st2 and ok_DTTF_st3 and ok_DTTF_st4: returnValue = pt_from_DPhi_DT_ellipse(dphi11, dphi12, dphi21, dphi22, DTTF_phib1_phib4, DTTF_phib1_phib4)

    return returnValue, L1Mu_eta
