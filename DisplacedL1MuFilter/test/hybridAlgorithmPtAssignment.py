## this file contains the pT assignment functions
from Helpers import *

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



def pt_barrel_direction_based_algorithm(tree, L1Mu_index, L1Mu_DTTF_index, doComparatorFit):
    pass

def pt_endcap_direction_based_algorithm(tree, L1Mu_index, L1Mu_CSCTF_index, doComparatorFit):
    pass

def pt_endcap_position_based_algorithm(treeHits, L1Mu_index, L1Mu_CSCTF_index, doComparatorFit):
    '''First argument is the analysis tree. Second argument is the L1Mu to CSCTF index''' 
    returnValue = 0
    
    ## L1Mu variables
    L1Mu_pt = treeHits.L1Mu_pt[L1Mu_index]
    L1Mu_eta = treeHits.L1Mu_eta[L1Mu_index]
    L1Mu_phi = treeHits.L1Mu_phi[L1Mu_index]
    L1Mu_bx = treeHits.L1Mu_bx[L1Mu_index]
    L1Mu_quality = treeHits.L1Mu_quality[L1Mu_index]
    
    ## CSC variables
    CSCTF_pt = treeHits.CSCTF_pt[L1Mu_CSCTF_index]
    CSCTF_eta = treeHits.CSCTF_eta[L1Mu_CSCTF_index]
    CSCTF_phi = treeHits.CSCTF_phi[L1Mu_CSCTF_index]
    CSCTF_bx = treeHits.CSCTF_bx[L1Mu_CSCTF_index]
    CSCTF_nStubs = treeHits.CSCTF_nStubs[L1Mu_CSCTF_index]

    CSCTF_phi1 = treeHits.CSCTF_phi1[L1Mu_CSCTF_index]
    CSCTF_phi2 = treeHits.CSCTF_phi2[L1Mu_CSCTF_index]
    CSCTF_phi3 = treeHits.CSCTF_phi3[L1Mu_CSCTF_index]
    CSCTF_phi4 = treeHits.CSCTF_phi4[L1Mu_CSCTF_index]

    ## check if ME1, ME2 and ME3 are available
    ok_CSCTF_st1 = CSCTF_phi1 != 99
    ok_CSCTF_st2 = CSCTF_phi2 != 99
    ok_CSCTF_st3 = CSCTF_phi3 != 99
    ok_CSCTF_st4 = CSCTF_phi4 != 99

    CSCTF_ch1 = treeHits.CSCTF_ch1[L1Mu_CSCTF_index]
    CSCTF_ch2 = treeHits.CSCTF_ch2[L1Mu_CSCTF_index]
    CSCTF_ch3 = treeHits.CSCTF_ch3[L1Mu_CSCTF_index]
    CSCTF_ch4 = treeHits.CSCTF_ch4[L1Mu_CSCTF_index]
    
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
    
    CSCTF_x1 = treeHits.CSCTF_x1[L1Mu_CSCTF_index]
    CSCTF_x2 = treeHits.CSCTF_x2[L1Mu_CSCTF_index]
    CSCTF_x3 = treeHits.CSCTF_x3[L1Mu_CSCTF_index]
    CSCTF_x4 = treeHits.CSCTF_x4[L1Mu_CSCTF_index]

    CSCTF_y1 = treeHits.CSCTF_y1[L1Mu_CSCTF_index]
    CSCTF_y2 = treeHits.CSCTF_y2[L1Mu_CSCTF_index]
    CSCTF_y3 = treeHits.CSCTF_y3[L1Mu_CSCTF_index]
    CSCTF_y4 = treeHits.CSCTF_y4[L1Mu_CSCTF_index]
    
    CSCTF_z1 = treeHits.CSCTF_z1[L1Mu_CSCTF_index]
    CSCTF_z2 = treeHits.CSCTF_z2[L1Mu_CSCTF_index]
    CSCTF_z3 = treeHits.CSCTF_z3[L1Mu_CSCTF_index]
    CSCTF_z4 = treeHits.CSCTF_z4[L1Mu_CSCTF_index]
    
    CSCTF_R1 = treeHits.CSCTF_R1[L1Mu_CSCTF_index]
    CSCTF_R2 = treeHits.CSCTF_R2[L1Mu_CSCTF_index]
    CSCTF_R3 = treeHits.CSCTF_R3[L1Mu_CSCTF_index]
    CSCTF_R4 = treeHits.CSCTF_R4[L1Mu_CSCTF_index]
    
    ## fitted variables after fitting to the comparator digis
    CSCTF_fit_phi1 = treeHits.CSCTF_fit_phi1[L1Mu_CSCTF_index]
    CSCTF_fit_phi2 = treeHits.CSCTF_fit_phi2[L1Mu_CSCTF_index]
    CSCTF_fit_phi3 = treeHits.CSCTF_fit_phi3[L1Mu_CSCTF_index]
    CSCTF_fit_phi4 = treeHits.CSCTF_fit_phi4[L1Mu_CSCTF_index]
    
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

    ## do a fit to eta
    Rs_out, st_out, chi2ndf_R = getFittedPositions(
        [CSCTF_fit_R1, CSCTF_fit_R2, CSCTF_fit_R3, CSCTF_fit_R4], 
        [CSCTF_fit_z1, CSCTF_fit_z2, CSCTF_fit_z3, CSCTF_fit_z4])
    
    if 1 in st_out: index_st1 = st_out.index(1)
    if 2 in st_out: index_st2 = st_out.index(2)
    if 3 in st_out: index_st3 = st_out.index(3)
    if 4 in st_out: index_st4 = st_out.index(4)
    
    CSCTF_etafit_R1 = 99
    CSCTF_etafit_R2 = 99
    CSCTF_etafit_R3 = 99
    CSCTF_etafit_R4 = 99

    CSCTF_etafit_eta1 = 99
    CSCTF_etafit_eta2 = 99
    CSCTF_etafit_eta3 = 99
    CSCTF_etafit_eta4 = 99

    if ok_CSCTF_st1: 
        CSCTF_etafit_R1 = Rs_out[index_st1]
        CSCTF_etafit_eta1 = get_eta_from_Z_R(CSCTF_etafit_R1, CSCTF_fit_z1)
    
    if ok_CSCTF_st2: 
        CSCTF_etafit_R2 = Rs_out[index_st2]
        CSCTF_etafit_eta2 = get_eta_from_Z_R(CSCTF_etafit_R2, CSCTF_fit_z2)

    if ok_CSCTF_st3: 
        CSCTF_etafit_R3 = Rs_out[index_st3]
        CSCTF_etafit_eta3 = get_eta_from_Z_R(CSCTF_etafit_R3, CSCTF_fit_z3)

    if ok_CSCTF_st4: 
        CSCTF_etafit_R4 = Rs_out[index_st4]
        CSCTF_etafit_eta4 = get_eta_from_Z_R(CSCTF_etafit_R4, CSCTF_fit_z4)


    ## check if you want to use the LCT positions or the fitted positions...
    ## the tag "algo" are the actual variables used in the calculation
    
    CSCTF_algo_phi1 = CSCTF_phi1
    CSCTF_algo_phi2 = CSCTF_phi2
    CSCTF_algo_phi3 = CSCTF_phi3
    CSCTF_algo_phi4 = CSCTF_phi4
    
    CSCTF_algo_x1 = CSCTF_x1
    CSCTF_algo_x2 = CSCTF_x2
    CSCTF_algo_x3 = CSCTF_x3
    CSCTF_algo_x4 = CSCTF_x4
    
    CSCTF_algo_y1 = CSCTF_y1
    CSCTF_algo_y2 = CSCTF_y2
    CSCTF_algo_y3 = CSCTF_y3
    CSCTF_algo_y4 = CSCTF_y4
    
    CSCTF_algo_z1 = CSCTF_z1
    CSCTF_algo_z2 = CSCTF_z2
    CSCTF_algo_z3 = CSCTF_z3
    CSCTF_algo_z4 = CSCTF_z4
    
    CSCTF_algo_R1 = CSCTF_R1
    CSCTF_algo_R2 = CSCTF_R2
    CSCTF_algo_R3 = CSCTF_R3
    CSCTF_algo_R4 = CSCTF_R4
    
    if doComparatorFit:
        CSCTF_algo_phi1 = CSCTF_fit_phi1
        CSCTF_algo_phi2 = CSCTF_fit_phi2
        CSCTF_algo_phi3 = CSCTF_fit_phi3
        CSCTF_algo_phi4 = CSCTF_fit_phi4
        
        CSCTF_algo_x1 = CSCTF_fit_x1
        CSCTF_algo_x2 = CSCTF_fit_x2
        CSCTF_algo_x3 = CSCTF_fit_x3
        CSCTF_algo_x4 = CSCTF_fit_x4
        
        CSCTF_algo_y1 = CSCTF_fit_y1
        CSCTF_algo_y2 = CSCTF_fit_y2
        CSCTF_algo_y3 = CSCTF_fit_y3
        CSCTF_algo_y4 = CSCTF_fit_y4
        
        CSCTF_algo_z1 = CSCTF_fit_z1
        CSCTF_algo_z2 = CSCTF_fit_z2
        CSCTF_algo_z3 = CSCTF_fit_z3
        CSCTF_algo_z4 = CSCTF_fit_z4
        
        CSCTF_algo_R1 = CSCTF_fit_R1
        CSCTF_algo_R2 = CSCTF_fit_R2
        CSCTF_algo_R3 = CSCTF_fit_R3
        CSCTF_algo_R4 = CSCTF_fit_R4

    doLinearFitToStubs = True
    if doLinearFitToStubs:
        CSCTF_algo_R1 = CSCTF_etafit_R1
        CSCTF_algo_R2 = CSCTF_etafit_R2
        CSCTF_algo_R3 = CSCTF_etafit_R3
        CSCTF_algo_R4 = CSCTF_etafit_R4
        
    ## actual calctulation of the pT
    if ok_CSCTF_st1 and ok_CSCTF_st2 and ok_CSCTF_st3:
        parity3 = get_parity(CSCTF_isEven1, CSCTF_isEven2, CSCTF_isEven3, CSCTF_isEven4)
        etaPartition = get_eta_partition(L1Mu_eta)
    
        deltay12, deltay23 = deltay12_deltay23_R(CSCTF_algo_R1, CSCTF_algo_phi1,
                                                 CSCTF_algo_R2, CSCTF_algo_phi2,
                                                 CSCTF_algo_R3, CSCTF_algo_phi3)
    
        proportionalityFactor = get_proptionality_factor(etaRanges[etaPartition], ME1ME2ME3ParityCases[parity], doComparatorFit)
        
        DDY123 = abs(deltay23 - proportionalityFactor * deltay12)
    
        ## get the reconstruction pT value
        print "True pt", pt, "DDY123_withoutLCTFit", DDY123_withoutLCTFit, "DDY123_withLCTFit", DDY123_withLCTFit
        
        positionPt = pt_from_DDY123_v2(DDY123, etaRanges[etaPartition], ME1ME2ME3ParityCases[parity], doComparatorFit)
        #positionPt_withLCTFit =    pt_from_DDY123_v2(DDY123_withLCTFit,    etaRanges[etaPartition], ME1ME2ME3ParityCases[parity], True)
        returnValue = positionPt

    return returnValue

def pt_endcap_hybrid_algorithm(tree, L1Mu_index, L1Mu_CSCTF_index, doComparatorFit):
    pass
