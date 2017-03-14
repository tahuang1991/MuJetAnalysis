## this file contains the pT assignment functions
from Helpers import *
from ROOT import *
from math import *
import pprint

dphi_dict = {}

##_________________________________________________
def is_L1Mu_isolated(treeHits, L1Mu_index, vetoType):
    """checks if muon is isolated from track trigger track"""

    isL1LooseVeto = treeHits.isL1LooseVeto[L1Mu_index]==1
    isL1MediumVeto = treeHits.isL1MediumVeto[L1Mu_index]==1
    isL1TightVeto = treeHits.isL1TightVeto[L1Mu_index]==1
    
    # The loose veto rejects prompt muons by matching a L1Tk within
    # a radius R<0.12 with an L1Tk pT > 4 GeV. The medium and tight
    # veto apply L1Tk pT cuts of 3 and 2 GeV respectively on L1Tk
    # in R<0.12.

    isMatched = False
    if vetoType == 1 and isL1LooseVeto:  isMatched = True
    if vetoType == 2 and isL1MediumVeto: isMatched = True
    if vetoType == 3 and isL1TightVeto:  isMatched = True
    return (not isMatched)


## intialize an empty dictionary
def initalizeEmptyDictionary(dphi_dict):
  DT_dPhi_combinations = [
    ((1, 2),(1, 3)),
    ((1, 2),(1, 4)),
    ((1, 2),(2, 3)),
    ((1, 2),(2, 4)),
    ((1, 2),(3, 4)),
    ((1, 3),(1, 4)),
    ((1, 3),(2, 3)),
    ((1, 3),(2, 4)),
    ((1, 3),(3, 4)),
    ((1, 4),(2, 3)),
    ((1, 4),(2, 4)),
    ((1, 4),(3, 4)),
    ((2, 3),(2, 4)),
    ((2, 3),(3, 4)),
    ((2, 4),(3, 4)),
    ]
  
  for combination in DT_dPhi_combinations:
    first = combination[0]
    second = combination[1]
    pString = "DPhib_MB%d_MB%d__DPhib_MB%d_MB%d"%(first[0], first[1], second[0], second[1])
    dphi_dict[pString] = {}
    for ptCut in [3,5,7,10,15,20,30,40]:
      ## PT : [a_axis_, b_axis, alpha[deg] ]
      dphi_dict[pString]['Pt%d'%(ptCut)] = []
    
  return dphi_dict

dphi_dict = initalizeEmptyDictionary(dphi_dict)

dphi_dict['DPhib_MB1_MB2__DPhib_MB1_MB3']['Pt3'] = [ 0 , 0 , 0 ]
dphi_dict['DPhib_MB1_MB2__DPhib_MB1_MB3']['Pt5'] = [ 0.29 , 0.19 , 33.0 ]
dphi_dict['DPhib_MB1_MB2__DPhib_MB1_MB3']['Pt7'] = [ 0.13 , 0.17 , 28.0 ]
dphi_dict['DPhib_MB1_MB2__DPhib_MB1_MB3']['Pt10'] = [ 0.11 , 0.35 , 26.0 ]
dphi_dict['DPhib_MB1_MB2__DPhib_MB1_MB3']['Pt15'] = [ 0.19 , 0.07 , 21.0 ]
dphi_dict['DPhib_MB1_MB2__DPhib_MB1_MB3']['Pt20'] = [ 0.23 , 0.07 , 28.0 ]
dphi_dict['DPhib_MB1_MB2__DPhib_MB1_MB3']['Pt30'] = [ 0.19 , 0.07 , 28.0 ]
dphi_dict['DPhib_MB1_MB2__DPhib_MB1_MB3']['Pt40'] = [ 0.05 , 0.19 , 26.0 ]
dphi_dict['DPhib_MB1_MB2__DPhib_MB1_MB4']['Pt3'] = [ 0 , 0 , 0 ]
dphi_dict['DPhib_MB1_MB2__DPhib_MB1_MB4']['Pt5'] = [ 0.49 , 0.13 , 11.0 ]
dphi_dict['DPhib_MB1_MB2__DPhib_MB1_MB4']['Pt7'] = [ 0.21 , 0.25 , 7.0 ]
dphi_dict['DPhib_MB1_MB2__DPhib_MB1_MB4']['Pt10'] = [ 0.33 , 0.13 , 12.0 ]
dphi_dict['DPhib_MB1_MB2__DPhib_MB1_MB4']['Pt15'] = [ 0.19 , 0.07 , 13.0 ]
dphi_dict['DPhib_MB1_MB2__DPhib_MB1_MB4']['Pt20'] = [ 0.07 , 0.09 , 14.0 ]
dphi_dict['DPhib_MB1_MB2__DPhib_MB1_MB4']['Pt30'] = [ 0.05 , 0.29 , 11.0 ]
dphi_dict['DPhib_MB1_MB2__DPhib_MB1_MB4']['Pt40'] = [ 0.15 , 0.05 , 6.0 ]
dphi_dict['DPhib_MB1_MB2__DPhib_MB2_MB3']['Pt3'] = [ 0.37 , 0.49 , 40.0 ]
dphi_dict['DPhib_MB1_MB2__DPhib_MB2_MB3']['Pt5'] = [ 0.25 , 0.13 , 33.0 ]
dphi_dict['DPhib_MB1_MB2__DPhib_MB2_MB3']['Pt7'] = [ 0.09 , 0.27 , 38.0 ]
dphi_dict['DPhib_MB1_MB2__DPhib_MB2_MB3']['Pt10'] = [ 0.07 , 0.19 , 35.0 ]
dphi_dict['DPhib_MB1_MB2__DPhib_MB2_MB3']['Pt15'] = [ 0.05 , 0.31 , 32.0 ]
dphi_dict['DPhib_MB1_MB2__DPhib_MB2_MB3']['Pt20'] = [ 0.15 , 0.05 , 40.0 ]
dphi_dict['DPhib_MB1_MB2__DPhib_MB2_MB3']['Pt30'] = [ 0.05 , 0.13 , 26.0 ]
dphi_dict['DPhib_MB1_MB2__DPhib_MB2_MB3']['Pt40'] = [ 0.05 , 0.09 , 26.0 ]
dphi_dict['DPhib_MB1_MB2__DPhib_MB2_MB4']['Pt3'] = [ 0 , 0 , 0 ]
dphi_dict['DPhib_MB1_MB2__DPhib_MB2_MB4']['Pt5'] = [ 0.13 , 0.41 , 22.0 ]
dphi_dict['DPhib_MB1_MB2__DPhib_MB2_MB4']['Pt7'] = [ 0.45 , 0.15 , 18.0 ]
dphi_dict['DPhib_MB1_MB2__DPhib_MB2_MB4']['Pt10'] = [ 0.37 , 0.09 , 18.0 ]
dphi_dict['DPhib_MB1_MB2__DPhib_MB2_MB4']['Pt15'] = [ 0.05 , 0.17 , 13.0 ]
dphi_dict['DPhib_MB1_MB2__DPhib_MB2_MB4']['Pt20'] = [ 0.11 , 0.05 , 15.0 ]
dphi_dict['DPhib_MB1_MB2__DPhib_MB2_MB4']['Pt30'] = [ 0.09 , 0.05 , 15.0 ]
dphi_dict['DPhib_MB1_MB2__DPhib_MB2_MB4']['Pt40'] = [ 0.17 , 0.03 , 21.0 ]
dphi_dict['DPhib_MB1_MB2__DPhib_MB3_MB4']['Pt3'] = [ 0.49 , 0.19 , 36.0 ]
dphi_dict['DPhib_MB1_MB2__DPhib_MB3_MB4']['Pt5'] = [ 0.29 , 0.09 , 36.0 ]
dphi_dict['DPhib_MB1_MB2__DPhib_MB3_MB4']['Pt7'] = [ 0.15 , 0.07 , 36.0 ]
dphi_dict['DPhib_MB1_MB2__DPhib_MB3_MB4']['Pt10'] = [ 0.07 , 0.13 , 32.0 ]
dphi_dict['DPhib_MB1_MB2__DPhib_MB3_MB4']['Pt15'] = [ 0.05 , 0.19 , 32.0 ]
dphi_dict['DPhib_MB1_MB2__DPhib_MB3_MB4']['Pt20'] = [ 0.05 , 0.11 , 29.0 ]
dphi_dict['DPhib_MB1_MB2__DPhib_MB3_MB4']['Pt30'] = [ 0.05 , 0.11 , 29.0 ]
dphi_dict['DPhib_MB1_MB2__DPhib_MB3_MB4']['Pt40'] = [ 0.05 , 0.09 , 29.0 ]
dphi_dict['DPhib_MB1_MB3__DPhib_MB1_MB4']['Pt3'] = [ 0 , 0 , 0 ]
dphi_dict['DPhib_MB1_MB3__DPhib_MB1_MB4']['Pt5'] = [ 0.17 , 0.47 , 31.0 ]
dphi_dict['DPhib_MB1_MB3__DPhib_MB1_MB4']['Pt7'] = [ 0.21 , 0.49 , 30.0 ]
dphi_dict['DPhib_MB1_MB3__DPhib_MB1_MB4']['Pt10'] = [ 0.15 , 0.23 , 36.0 ]
dphi_dict['DPhib_MB1_MB3__DPhib_MB1_MB4']['Pt15'] = [ 0.09 , 0.23 , 36.0 ]
dphi_dict['DPhib_MB1_MB3__DPhib_MB1_MB4']['Pt20'] = [ 0.07 , 0.09 , 30.0 ]
dphi_dict['DPhib_MB1_MB3__DPhib_MB1_MB4']['Pt30'] = [ 0.05 , 0.15 , 36.0 ]
dphi_dict['DPhib_MB1_MB3__DPhib_MB1_MB4']['Pt40'] = [ 0.13 , 0.05 , 31.0 ]
dphi_dict['DPhib_MB1_MB3__DPhib_MB2_MB3']['Pt3'] = [ 0 , 0 , 0 ]
dphi_dict['DPhib_MB1_MB3__DPhib_MB2_MB3']['Pt5'] = [ 0.37 , 0.09 , 51.0 ]
dphi_dict['DPhib_MB1_MB3__DPhib_MB2_MB3']['Pt7'] = [ 0.09 , 0.41 , 56.0 ]
dphi_dict['DPhib_MB1_MB3__DPhib_MB2_MB3']['Pt10'] = [ 0.07 , 0.23 , 56.0 ]
dphi_dict['DPhib_MB1_MB3__DPhib_MB2_MB3']['Pt15'] = [ 0.05 , 0.17 , 56.0 ]
dphi_dict['DPhib_MB1_MB3__DPhib_MB2_MB3']['Pt20'] = [ 0.05 , 0.17 , 53.0 ]
dphi_dict['DPhib_MB1_MB3__DPhib_MB2_MB3']['Pt30'] = [ 0.07 , 0.39 , 60.0 ]
dphi_dict['DPhib_MB1_MB3__DPhib_MB2_MB3']['Pt40'] = [ 0.05 , 0.33 , 47.0 ]
dphi_dict['DPhib_MB1_MB3__DPhib_MB2_MB4']['Pt3'] = [ 0 , 0 , 0 ]
dphi_dict['DPhib_MB1_MB3__DPhib_MB2_MB4']['Pt5'] = [ 0.47 , 0.11 , 45.0 ]
dphi_dict['DPhib_MB1_MB3__DPhib_MB2_MB4']['Pt7'] = [ 0.23 , 0.13 , 45.0 ]
dphi_dict['DPhib_MB1_MB3__DPhib_MB2_MB4']['Pt10'] = [ 0.11 , 0.23 , 41.0 ]
dphi_dict['DPhib_MB1_MB3__DPhib_MB2_MB4']['Pt15'] = [ 0.07 , 0.15 , 41.0 ]
dphi_dict['DPhib_MB1_MB3__DPhib_MB2_MB4']['Pt20'] = [ 0.07 , 0.09 , 45.0 ]
dphi_dict['DPhib_MB1_MB3__DPhib_MB2_MB4']['Pt30'] = [ 0.13 , 0.05 , 47.0 ]
dphi_dict['DPhib_MB1_MB3__DPhib_MB2_MB4']['Pt40'] = [ 0.07 , 0.13 , 42.0 ]
dphi_dict['DPhib_MB1_MB3__DPhib_MB3_MB4']['Pt3'] = [ 0 , 0 , 0 ]
dphi_dict['DPhib_MB1_MB3__DPhib_MB3_MB4']['Pt5'] = [ 0.17 , 0.33 , 59.0 ]
dphi_dict['DPhib_MB1_MB3__DPhib_MB3_MB4']['Pt7'] = [ 0.17 , 0.17 , 45.0 ]
dphi_dict['DPhib_MB1_MB3__DPhib_MB3_MB4']['Pt10'] = [ 0.11 , 0.11 , 45.0 ]
dphi_dict['DPhib_MB1_MB3__DPhib_MB3_MB4']['Pt15'] = [ 0.07 , 0.11 , 57.0 ]
dphi_dict['DPhib_MB1_MB3__DPhib_MB3_MB4']['Pt20'] = [ 0.05 , 0.11 , 51.0 ]
dphi_dict['DPhib_MB1_MB3__DPhib_MB3_MB4']['Pt30'] = [ 0.05 , 0.07 , 48.0 ]
dphi_dict['DPhib_MB1_MB3__DPhib_MB3_MB4']['Pt40'] = [ 0.03 , 0.25 , 48.0 ]
dphi_dict['DPhib_MB1_MB4__DPhib_MB2_MB3']['Pt3'] = [ 0 , 0 , 0 ]
dphi_dict['DPhib_MB1_MB4__DPhib_MB2_MB3']['Pt5'] = [ 0.11 , 0.47 , 71.0 ]
dphi_dict['DPhib_MB1_MB4__DPhib_MB2_MB3']['Pt7'] = [ 0.43 , 0.21 , 80.0 ]
dphi_dict['DPhib_MB1_MB4__DPhib_MB2_MB3']['Pt10'] = [ 0.25 , 0.13 , 80.0 ]
dphi_dict['DPhib_MB1_MB4__DPhib_MB2_MB3']['Pt15'] = [ 0.13 , 0.09 , 71.0 ]
dphi_dict['DPhib_MB1_MB4__DPhib_MB2_MB3']['Pt20'] = [ 0.13 , 0.07 , 74.0 ]
dphi_dict['DPhib_MB1_MB4__DPhib_MB2_MB3']['Pt30'] = [ 0.05 , 0.17 , 66.0 ]
dphi_dict['DPhib_MB1_MB4__DPhib_MB2_MB3']['Pt40'] = [ 0.33 , 0.05 , 74.0 ]
dphi_dict['DPhib_MB1_MB4__DPhib_MB2_MB4']['Pt3'] = [ 0 , 0 , 0 ]
dphi_dict['DPhib_MB1_MB4__DPhib_MB2_MB4']['Pt5'] = [ 0 , 0 , 0 ]
dphi_dict['DPhib_MB1_MB4__DPhib_MB2_MB4']['Pt7'] = [ 0.49 , 0.15 , 42.0 ]
dphi_dict['DPhib_MB1_MB4__DPhib_MB2_MB4']['Pt10'] = [ 0.33 , 0.09 , 42.0 ]
dphi_dict['DPhib_MB1_MB4__DPhib_MB2_MB4']['Pt15'] = [ 0.09 , 0.35 , 41.0 ]
dphi_dict['DPhib_MB1_MB4__DPhib_MB2_MB4']['Pt20'] = [ 0.17 , 0.05 , 39.0 ]
dphi_dict['DPhib_MB1_MB4__DPhib_MB2_MB4']['Pt30'] = [ 0.05 , 0.09 , 50.0 ]
dphi_dict['DPhib_MB1_MB4__DPhib_MB2_MB4']['Pt40'] = [ 0.05 , 0.35 , 44.0 ]
dphi_dict['DPhib_MB1_MB4__DPhib_MB3_MB4']['Pt3'] = [ 0 , 0 , 0 ]
dphi_dict['DPhib_MB1_MB4__DPhib_MB3_MB4']['Pt5'] = [ 0.47 , 0.17 , 76.0 ]
dphi_dict['DPhib_MB1_MB4__DPhib_MB3_MB4']['Pt7'] = [ 0.27 , 0.19 , 70.0 ]
dphi_dict['DPhib_MB1_MB4__DPhib_MB3_MB4']['Pt10'] = [ 0.13 , 0.35 , 69.0 ]
dphi_dict['DPhib_MB1_MB4__DPhib_MB3_MB4']['Pt15'] = [ 0.07 , 0.13 , 78.0 ]
dphi_dict['DPhib_MB1_MB4__DPhib_MB3_MB4']['Pt20'] = [ 0.05 , 0.13 , 78.0 ]
dphi_dict['DPhib_MB1_MB4__DPhib_MB3_MB4']['Pt30'] = [ 0.05 , 0.07 , 75.0 ]
dphi_dict['DPhib_MB1_MB4__DPhib_MB3_MB4']['Pt40'] = [ 0.09 , 0.05 , 74.0 ]
dphi_dict['DPhib_MB2_MB3__DPhib_MB2_MB4']['Pt3'] = [ 0 , 0 , 0 ]
dphi_dict['DPhib_MB2_MB3__DPhib_MB2_MB4']['Pt5'] = [ 0.11 , 0.43 , 34.0 ]
dphi_dict['DPhib_MB2_MB3__DPhib_MB2_MB4']['Pt7'] = [ 0.19 , 0.21 , 41.0 ]
dphi_dict['DPhib_MB2_MB3__DPhib_MB2_MB4']['Pt10'] = [ 0.13 , 0.09 , 39.0 ]
dphi_dict['DPhib_MB2_MB3__DPhib_MB2_MB4']['Pt15'] = [ 0.11 , 0.07 , 41.0 ]
dphi_dict['DPhib_MB2_MB3__DPhib_MB2_MB4']['Pt20'] = [ 0.05 , 0.39 , 30.0 ]
dphi_dict['DPhib_MB2_MB3__DPhib_MB2_MB4']['Pt30'] = [ 0.15 , 0.05 , 44.0 ]
dphi_dict['DPhib_MB2_MB3__DPhib_MB2_MB4']['Pt40'] = [ 0.13 , 0.05 , 38.0 ]
dphi_dict['DPhib_MB2_MB3__DPhib_MB3_MB4']['Pt3'] = [ 0 , 0 , 0 ]
dphi_dict['DPhib_MB2_MB3__DPhib_MB3_MB4']['Pt5'] = [ 0.11 , 0.35 , 37.0 ]
dphi_dict['DPhib_MB2_MB3__DPhib_MB3_MB4']['Pt7'] = [ 0.11 , 0.17 , 47.0 ]
dphi_dict['DPhib_MB2_MB3__DPhib_MB3_MB4']['Pt10'] = [ 0.07 , 0.13 , 44.0 ]
dphi_dict['DPhib_MB2_MB3__DPhib_MB3_MB4']['Pt15'] = [ 0.13 , 0.05 , 43.0 ]
dphi_dict['DPhib_MB2_MB3__DPhib_MB3_MB4']['Pt20'] = [ 0.05 , 0.09 , 48.0 ]
dphi_dict['DPhib_MB2_MB3__DPhib_MB3_MB4']['Pt30'] = [ 0.05 , 0.09 , 48.0 ]
dphi_dict['DPhib_MB2_MB3__DPhib_MB3_MB4']['Pt40'] = [ 0.11 , 0.05 , 37.0 ]
dphi_dict['DPhib_MB2_MB4__DPhib_MB3_MB4']['Pt3'] = [ 0 , 0 , 0 ]
dphi_dict['DPhib_MB2_MB4__DPhib_MB3_MB4']['Pt5'] = [ 0.11 , 0.41 , 68.0 ]
dphi_dict['DPhib_MB2_MB4__DPhib_MB3_MB4']['Pt7'] = [ 0.13 , 0.31 , 56.0 ]
dphi_dict['DPhib_MB2_MB4__DPhib_MB3_MB4']['Pt10'] = [ 0.29 , 0.07 , 67.0 ]
dphi_dict['DPhib_MB2_MB4__DPhib_MB3_MB4']['Pt15'] = [ 0.41 , 0.05 , 64.0 ]
dphi_dict['DPhib_MB2_MB4__DPhib_MB3_MB4']['Pt20'] = [ 0.05 , 0.23 , 69.0 ]
dphi_dict['DPhib_MB2_MB4__DPhib_MB3_MB4']['Pt30'] = [ 0.11 , 0.05 , 58.0 ]
dphi_dict['DPhib_MB2_MB4__DPhib_MB3_MB4']['Pt40'] = [ 0.15 , 0.05 , 64.0 ]

pprint.pprint(dphi_dict)
"""
dphi_dict = {
  'DPhib_MB1_MB2__DPhib_MB1_MB3': {'Pt10': [0.09, 0.19, 32.0],
                                  'Pt15': [0.07, 0.15, 35.0],
                                  'Pt20': [0.07, 0.15, 32.0],
                                  'Pt3': [0.27, 0.41, 23.0],
                                  'Pt30': [0.07, 0.25, 26.0],
                                  'Pt40': [0.05, 0.09, 26.0],
                                  'Pt5': [0.17, 0.39, 29.0],
                                  'Pt7': [0.11, 0.37, 32.0]},
 'DPhib_MB1_MB2__DPhib_MB1_MB4': {'Pt10': [0.07, 0.13, 6.0],
                                  'Pt15': [0.07, 0.17, 11.0],
                                  'Pt20': [0.07, 0.09, 8.0],
                                  'Pt3': [0.21, 0.37, 5.0],
                                  'Pt30': [0.05, 0.07, 5.0],
                                  'Pt40': [0.03, 0.07, 11.0],
                                  'Pt5': [0.21, 0.49, 11.0],
                                  'Pt7': [0.15, 0.17, 19.0]},
 'DPhib_MB1_MB2__DPhib_MB2_MB3': {'Pt10': [0.07, 0.19, 32.0],
                                  'Pt15': [0.05, 0.25, 35.0],
                                  'Pt20': [0.05, 0.27, 32.0],
                                  'Pt3': [0.15, 0.43, 38.0],
                                  'Pt30': [0.05, 0.17, 32.0],
                                  'Pt40': [0.03, 0.23, 35.0],
                                  'Pt5': [0.11, 0.21, 38.0],
                                  'Pt7': [0.17, 0.07, 30.0]},
 'DPhib_MB1_MB2__DPhib_MB2_MB4': {'Pt10': [0.07, 0.11, 22.0],
                                  'Pt15': [0.15, 0.05, 18.0],
                                  'Pt20': [0.11, 0.05, 21.0],
                                  'Pt3': [0.13, 0.39, 13.0],
                                  'Pt30': [0.03, 0.13, 10.0],
                                  'Pt40': [0.03, 0.11, 10.0],
                                  'Pt5': [0.29, 0.15, 21.0],
                                  'Pt7': [0.23, 0.11, 18.0]},
 'DPhib_MB1_MB2__DPhib_MB3_MB4': {'Pt10': [0.05, 0.17, 38.0],
                                  'Pt15': [0.05, 0.15, 29.0],
                                  'Pt20': [0.05, 0.11, 29.0],
                                  'Pt3': [0.09, 0.31, 35.0],
                                  'Pt30': [0.05, 0.11, 29.0],
                                  'Pt40': [0.05, 0.09, 29.0],
                                  'Pt5': [0.09, 0.23, 35.0],
                                  'Pt7': [0.07, 0.13, 38.0]},
 'DPhib_MB1_MB3__DPhib_MB1_MB4': {'Pt10': [0.11, 0.13, 37.0],
                                  'Pt15': [0.09, 0.11, 30.0],
                                  'Pt20': [0.07, 0.11, 39.0],
                                  'Pt3': [0.23, 0.39, 36.0],
                                  'Pt30': [0.05, 0.09, 33.0],
                                  'Pt40': [0.05, 0.07, 27.0],
                                  'Pt5': [0.19, 0.47, 30.0],
                                  'Pt7': [0.17, 0.31, 35.0]},
 'DPhib_MB1_MB3__DPhib_MB2_MB3': {'Pt10': [0.07, 0.29, 53.0],
                                  'Pt15': [0.13, 0.05, 51.0],
                                  'Pt20': [0.05, 0.13, 59.0],
                                  'Pt3': [0.45, 0.17, 45.0],
                                  'Pt30': [0.05, 0.23, 53.0],
                                  'Pt40': [0.03, 0.13, 56.0],
                                  'Pt5': [0.09, 0.31, 59.0],
                                  'Pt7': [0.07, 0.37, 56.0]},
 'DPhib_MB1_MB3__DPhib_MB2_MB4': {'Pt10': [0.11, 0.11, 35.0],
                                  'Pt15': [0.07, 0.29, 35.0],
                                  'Pt20': [0.07, 0.09, 45.0],
                                  'Pt3': [0.15, 0.27, 47.0],
                                  'Pt30': [0.07, 0.09, 45.0],
                                  'Pt40': [0.07, 0.13, 42.0],
                                  'Pt5': [0.15, 0.25, 47.0],
                                  'Pt7': [0.13, 0.29, 38.0]},
 'DPhib_MB1_MB3__DPhib_MB3_MB4': {'Pt10': [0.09, 0.11, 54.0],
                                  'Pt15': [0.07, 0.09, 54.0],
                                  'Pt20': [0.05, 0.11, 51.0],
                                  'Pt3': [0.15, 0.39, 51.0],
                                  'Pt30': [0.03, 0.27, 51.0],
                                  'Pt40': [0.03, 0.07, 48.0],
                                  'Pt5': [0.15, 0.31, 51.0],
                                  'Pt7': [0.11, 0.15, 53.0]},
 'DPhib_MB1_MB4__DPhib_MB2_MB3': {'Pt10': [0.11, 0.15, 66.0],
                                  'Pt15': [0.07, 0.29, 69.0],
                                  'Pt20': [0.09, 0.07, 80.0],
                                  'Pt3': [0.35, 0.21, 80.0],
                                  'Pt30': [0.33, 0.05, 74.0],
                                  'Pt40': [0.33, 0.05, 74.0],
                                  'Pt5': [0.21, 0.35, 66.0],
                                  'Pt7': [0.27, 0.15, 80.0]},
 'DPhib_MB1_MB4__DPhib_MB2_MB4': {'Pt10': [0.05, 0.21, 37.0],
                                  'Pt15': [0.07, 0.49, 44.0],
                                  'Pt20': [0.05, 0.19, 50.0],
                                  'Pt3': [0.41, 0.17, 42.0],
                                  'Pt30': [0.05, 0.09, 50.0],
                                  'Pt40': [0.03, 0.07, 47.0],
                                  'Pt5': [0.13, 0.31, 37.0],
                                  'Pt7': [0.13, 0.39, 50.0]},
 'DPhib_MB1_MB4__DPhib_MB3_MB4': {'Pt10': [0.09, 0.21, 75.0],
                                  'Pt15': [0.07, 0.11, 78.0],
                                  'Pt20': [0.05, 0.15, 75.0],
                                  'Pt3': [0.19, 0.41, 72.0],
                                  'Pt30': [0.05, 0.07, 69.0],
                                  'Pt40': [0.11, 0.03, 70.0],
                                  'Pt5': [0.19, 0.35, 72.0],
                                  'Pt7': [0.17, 0.25, 66.0]},
 'DPhib_MB2_MB3__DPhib_MB2_MB4': {'Pt10': [0.11, 0.09, 38.0],
                                  'Pt15': [0.07, 0.35, 39.0],
                                  'Pt20': [0.05, 0.25, 30.0],
                                  'Pt3': [0.17, 0.19, 32.0],
                                  'Pt30': [0.05, 0.13, 32.0],
                                  'Pt40': [0.05, 0.11, 45.0],
                                  'Pt5': [0.17, 0.17, 30.0],
                                  'Pt7': [0.15, 0.13, 37.0]},
 'DPhib_MB2_MB3__DPhib_MB3_MB4': {'Pt10': [0.11, 0.07, 40.0],
                                  'Pt15': [0.05, 0.15, 48.0],
                                  'Pt20': [0.05, 0.13, 48.0],
                                  'Pt3': [0.27, 0.11, 43.0],
                                  'Pt30': [0.05, 0.15, 48.0],
                                  'Pt40': [0.03, 0.11, 35.0],
                                  'Pt5': [0.11, 0.15, 35.0],
                                  'Pt7': [0.09, 0.11, 35.0]},
 'DPhib_MB2_MB4__DPhib_MB3_MB4': {'Pt10': [0.17, 0.07, 64.0],
                                  'Pt15': [0.07, 0.15, 66.0],
                                  'Pt20': [0.05, 0.19, 69.0],
                                  'Pt3': [0.29, 0.09, 70.0],
                                  'Pt30': [0.21, 0.05, 61.0],
                                  'Pt40': [0.03, 0.11, 56.0],
                                  'Pt5': [0.49, 0.11, 64.0],
                                  'Pt7': [0.49, 0.07, 67.0]}}
"""

#______________________________________________________________________________
def getEllipseParameters(dphi11, dphi12, dphi21, dphi22):
  return 'DPhib_MB%d_MB%d__DPhib_MB%d_MB%d'%(dphi11, dphi12, dphi21, dphi22)


#______________________________________________________________________________
def getEllipseParametersString(dphiString, pt):
  return dphi_dict[dphiString]["Pt%d"%pt]


#______________________________________________________________________________
def getEllipse(x,y,a,b, alpha=0, x0=0, y0=0):
  rad_alpha = alpha/180*math.pi
  x1 = x*cos(rad_alpha)+y*sin(rad_alpha)-x0
  y1 = x*sin(rad_alpha)-y*cos(rad_alpha)-y0
  #print "x ",x," y ",y," a ",a," b ",b," alpha ",alpha*180/pi," x1 ",x1," y1 ",y1
  return x1*x1/(a*a) + y1*y1/(b*b)


#______________________________________________________________________________
def passEllipse(x,y,a,b,alpha, x0=0, y0=0):
  return getEllipse(x,y,a,b,alpha, x0, y0) <= 1.0


#______________________________________________________________________________
def failEllipse(x,y,a,b,alpha, x0=0, y0=0):
  return getEllipse(x,y,a,b,alpha,x0, y0) > 1.0


#______________________________________________________________________________
def get_best_combination_station(stations):
  if 1 in stations and 2 in stations and 3 in stations:
    combinations = [
      'DPhib_MB1_MB2__DPhib_MB1_MB3',
      'DPhib_MB1_MB3__DPhib_MB2_MB3',
      'DPhib_MB1_MB2__DPhib_MB2_MB3']
    return combinations[0]


  if 1 in stations and 2 in stations and 4 in stations:
    combinations = [
      'DPhib_MB1_MB2__DPhib_MB1_MB4',
      'DPhib_MB1_MB4__DPhib_MB2_MB4',
      'DPhib_MB1_MB2__DPhib_MB2_MB4']
    return combinations[0]


  if 1 in stations and 3 in stations and 4 in stations:
    combinations = [
      'DPhib_MB1_MB4__DPhib_MB3_MB4',
      'DPhib_MB1_MB3__DPhib_MB1_MB4',
      'DPhib_MB1_MB3__DPhib_MB3_MB4']
    return combinations[0]


  if 2 in stations and 3 in stations and 4 in stations:
    combinations = [
      'DPhib_MB2_MB3__DPhib_MB2_MB4',
      'DPhib_MB2_MB4__DPhib_MB3_MB4',
      'DPhib_MB2_MB3__DPhib_MB3_MB4']
    return combinations[0]


  if (1 in stations and 2 in stations and
      3 in stations and 4 in stations):
    combinations = [
      'DPhib_MB1_MB4__DPhib_MB2_MB3',
      'DPhib_MB1_MB3__DPhib_MB2_MB4',
      'DPhib_MB1_MB2__DPhib_MB3_MB4']
    return combinations[0]


#______________________________________________________________________________
def pt_from_DPhi_DT_ellipse(dphi11, dphi12, dphi21, dphi22, x, y):
  default_pt = 2

  dphiString = getEllipseParameters(dphi11, dphi12, dphi21, dphi22)
  #print dphiString
  for ptCut in [40, 30, 20, 15, 10, 7, 5, 3]:
    #print ptCut
    ## get the parameters for this ellips
    params = getEllipseParametersString(dphiString, ptCut)
    a_axis = params[0]
    b_axis = params[1]
    alpha  = params[2]

    ## do not consider dangerous cases!
    if a_axis==0. or b_axis==0.: continue

    if passEllipse(x, y, a_axis, b_axis, alpha):
      return ptCut

  #print "returning default pt", default_pt
  return default_pt



def pt_from_DPhi_DT_ellipse_test():
  default_pt = 2
  dphi11, dphi12, dphi21, dphi22, x, y = 1, 2, 3, 4, 0.2, 0.2
  dphiString = getEllipseParameters(dphi11, dphi12, dphi21, dphi22)
  print dphiString
  for ptCut in [40, 30, 20, 15, 10, 7, 5, 3]:
    print ptCut
    ## get the parameters for this ellips
    params = getEllipseParametersString(dphiString, ptCut)
    a_axis = params[0]
    b_axis = params[1]
    alpha  = params[2]
    
    if passEllipse(x, y, a_axis, b_axis, alpha):
      print "\tPass!"
      return ptCut
    else:
      print "\tFail ellipse"
  print "returning default pt", default_pt
  return default_pt
  
#pt_from_DPhi_DT_ellipse_test()

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
def fillDisplacedBarrelHistogram(mapTH1F,
                                 key,
                                 treeHits,
                                 etaCutMin,
                                 etaCutMax,
                                 stubCut,
                                 algorithm=0,
                                 vetoType=0):
    doBXCut = True
    qualityCut=4
    displaced_L1Mu_pt, displaced_L1Mu_eta, iLMu = getMaxDisplacedBarrelPtEtaEvent(treeHits,
                                                                                  doBXCut,
                                                                                  etaCutMin,
                                                                                  etaCutMax,
                                                                                  stubCut,
                                                                                  qualityCut,
                                                                                  algorithm,
                                                                                  vetoType)
    if (displaced_L1Mu_pt>0):
        mapTH1F[key.replace("rate_", "rate_pt_")].Fill(displaced_L1Mu_pt)
    ## apply a 7/10 GeV pT cut for the eta histograms!!!
    if (displaced_L1Mu_pt>=7):
        mapTH1F[key.replace("rate_", "rate_eta_L1Pt7_")].Fill(abs(displaced_L1Mu_eta))
    if (displaced_L1Mu_pt>=10):
        mapTH1F[key.replace("rate_", "rate_eta_L1Pt10_")].Fill(abs(displaced_L1Mu_eta))


#______________________________________________________________________________
def getMaxDisplacedBarrelPtEtaEvent(treeHits,
                              doBXCut,
                              etaCutMin,
                              etaCutMax,
                              stubCut,
                              qualityCut,
                              algorithm=0,
                              vetoType=0):

    max_displaced_L1Mu_pt = -1
    max_displaced_L1Mu_eta = -99

    ## check if this event has L1Mus
    if len(list(treeHits.L1Mu_pt))==0:
        return max_displaced_L1Mu_pt, max_displaced_L1Mu_eta

    pts = list(treeHits.L1Mu_pt)
    nGoodMuons = 0
    iL1Mu = -1
    for i in range(0,len(pts)):

        L1Mu_eta = treeHits.L1Mu_eta[i]
        L1Mu_bx = treeHits.L1Mu_bx[i]
        L1Mu_quality = treeHits.L1Mu_quality[i]

        ## BX cut
        if abs(L1Mu_bx)>0 and doBXCut: continue

        ## quality cut
        if L1Mu_quality < qualityCut: continue

        ## check if muon is isolated
        if (vetoType!=0) and (not is_L1Mu_isolated(treeHits, i, vetoType)): continue

        ## eta cut
        if not (etaCutMin <=abs(L1Mu_eta) and abs(L1Mu_eta) < etaCutMax): continue

        L1Mu_DTTF_index = treeHits.L1Mu_DTTF_index[i]

        DisplacedL1Mu_pt, DisplacedL1Mu_eta = -1, -1

        #print L1Mu_DTTF_index
        if L1Mu_DTTF_index != -1 and L1Mu_DTTF_index < len(treeHits.DTTF_phi1):
            DisplacedL1Mu_pt, DisplacedL1Mu_eta = pt_barrel_direction_based_algorithm(treeHits, i, algorithm)

            ## calculate the max pT for the muons that pass the criteria
            if DisplacedL1Mu_pt > max_displaced_L1Mu_pt:
                iL1Mu = i
                max_displaced_L1Mu_pt = DisplacedL1Mu_pt
                max_displaced_L1Mu_eta = DisplacedL1Mu_eta

    return max_displaced_L1Mu_pt, max_displaced_L1Mu_eta, iL1Mu


#______________________________________________________________________________
def pt_barrel_direction_based_algorithm(treeHits,  L1Mu_index, algorithm):
    returnValue = 2


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
    
    ## algorithm 1-6: 2 stations exclusive
    if algorithm==1 and ok_DTTF_st1 and ok_DTTF_st2 and not ok_DTTF_st3 and not ok_DTTF_st4: returnValue = pt_from_DPhi_DT(abs_DTTF_phib1_phib2, 'DT1_DT2')
    if algorithm==2 and ok_DTTF_st1 and ok_DTTF_st3 and not ok_DTTF_st2 and not ok_DTTF_st4: returnValue = pt_from_DPhi_DT(abs_DTTF_phib1_phib3, 'DT1_DT3')
    if algorithm==3 and ok_DTTF_st1 and ok_DTTF_st4 and not ok_DTTF_st2 and not ok_DTTF_st3: returnValue = pt_from_DPhi_DT(abs_DTTF_phib1_phib4, 'DT1_DT4')
    if algorithm==4 and ok_DTTF_st2 and ok_DTTF_st3 and not ok_DTTF_st1 and not ok_DTTF_st4: returnValue = pt_from_DPhi_DT(abs_DTTF_phib2_phib3, 'DT2_DT3')
    if algorithm==5 and ok_DTTF_st2 and ok_DTTF_st4 and not ok_DTTF_st1 and not ok_DTTF_st3: returnValue = pt_from_DPhi_DT(abs_DTTF_phib2_phib4, 'DT2_DT4')
    if algorithm==6 and ok_DTTF_st3 and ok_DTTF_st4 and not ok_DTTF_st1 and not ok_DTTF_st2: returnValue = pt_from_DPhi_DT(abs_DTTF_phib3_phib4, 'DT3_DT4')

    ## algorithm 7-10: 3 stations exclusive
    if algorithm==7 and      ok_DTTF_st1 and     ok_DTTF_st2 and     ok_DTTF_st3 and not ok_DTTF_st4: returnValue = pt_from_DPhi_DT_ellipse(1, 2, 1, 3, DTTF_phib1_phib2, DTTF_phib1_phib3)
    if algorithm==8 and      ok_DTTF_st1 and     ok_DTTF_st2 and not ok_DTTF_st3 and     ok_DTTF_st4: returnValue = pt_from_DPhi_DT_ellipse(1, 2, 1, 4, DTTF_phib1_phib2, DTTF_phib1_phib4)
    if algorithm==9 and      ok_DTTF_st1 and not ok_DTTF_st2 and     ok_DTTF_st3 and not ok_DTTF_st4: returnValue = pt_from_DPhi_DT_ellipse(1, 3, 1, 4, DTTF_phib1_phib3, DTTF_phib1_phib4)
    if algorithm==10 and not ok_DTTF_st1 and     ok_DTTF_st2 and     ok_DTTF_st3 and     ok_DTTF_st4: returnValue = pt_from_DPhi_DT_ellipse(2, 3, 2, 4, DTTF_phib2_phib3, DTTF_phib2_phib4)
      
    ## algorithm 11:1 4 stations exclusive
    if algorithm==11 and ok_DTTF_st1 and ok_DTTF_st2 and ok_DTTF_st3 and ok_DTTF_st4: returnValue = pt_from_DPhi_DT_ellipse(1, 4, 2, 3, DTTF_phib1_phib4, DTTF_phib2_phib3)

    ## algorithm 12: simple combined trigger
    if algorithm==12:
      if ok_DTTF_st1 and ok_DTTF_st4: returnValue = pt_from_DPhi_DT(abs_DTTF_phib1_phib4, 'DT1_DT4')
      else:
        if (ok_DTTF_st1 and ok_DTTF_st3) or (ok_DTTF_st2 and ok_DTTF_st4):
          if ok_DTTF_st1 and ok_DTTF_st3: returnValue = pt_from_DPhi_DT(abs_DTTF_phib1_phib3, 'DT1_DT3')
          if ok_DTTF_st2 and ok_DTTF_st4: returnValue = pt_from_DPhi_DT(abs_DTTF_phib2_phib4, 'DT2_DT4')
        else:
          if ok_DTTF_st1 and ok_DTTF_st2: returnValue = pt_from_DPhi_DT(abs_DTTF_phib1_phib2, 'DT1_DT2')
          if ok_DTTF_st2 and ok_DTTF_st3: returnValue = pt_from_DPhi_DT(abs_DTTF_phib2_phib3, 'DT2_DT3')
          if ok_DTTF_st3 and ok_DTTF_st4: returnValue = pt_from_DPhi_DT(abs_DTTF_phib3_phib4, 'DT3_DT4')

    ## algorithm 13: elaborate combined trigger
    if algorithm==13:
      if ok_DTTF_st1 and ok_DTTF_st2 and not ok_DTTF_st3 and not ok_DTTF_st4: returnValue = pt_from_DPhi_DT(abs_DTTF_phib1_phib2, 'DT1_DT2')
      if ok_DTTF_st1 and ok_DTTF_st3 and not ok_DTTF_st2 and not ok_DTTF_st4: returnValue = pt_from_DPhi_DT(abs_DTTF_phib1_phib3, 'DT1_DT3')
      if ok_DTTF_st1 and ok_DTTF_st4 and not ok_DTTF_st2 and not ok_DTTF_st3: returnValue = pt_from_DPhi_DT(abs_DTTF_phib1_phib4, 'DT1_DT4')
      if ok_DTTF_st2 and ok_DTTF_st3 and not ok_DTTF_st1 and not ok_DTTF_st4: returnValue = pt_from_DPhi_DT(abs_DTTF_phib2_phib3, 'DT2_DT3')
      if ok_DTTF_st2 and ok_DTTF_st4 and not ok_DTTF_st1 and not ok_DTTF_st3: returnValue = pt_from_DPhi_DT(abs_DTTF_phib2_phib4, 'DT2_DT4')
      if ok_DTTF_st3 and ok_DTTF_st4 and not ok_DTTF_st1 and not ok_DTTF_st2: returnValue = pt_from_DPhi_DT(abs_DTTF_phib3_phib4, 'DT3_DT4')
      
      if     ok_DTTF_st1 and     ok_DTTF_st2 and     ok_DTTF_st3 and not ok_DTTF_st4: returnValue = pt_from_DPhi_DT_ellipse(1, 2, 1, 3, DTTF_phib1_phib2, DTTF_phib1_phib3)
      if     ok_DTTF_st1 and     ok_DTTF_st2 and not ok_DTTF_st3 and     ok_DTTF_st4: returnValue = pt_from_DPhi_DT_ellipse(1, 2, 1, 4, DTTF_phib1_phib2, DTTF_phib1_phib4)
      if     ok_DTTF_st1 and not ok_DTTF_st2 and     ok_DTTF_st3 and not ok_DTTF_st4: returnValue = pt_from_DPhi_DT_ellipse(1, 3, 1, 4, DTTF_phib1_phib3, DTTF_phib1_phib4)
      if not ok_DTTF_st1 and     ok_DTTF_st2 and     ok_DTTF_st3 and     ok_DTTF_st4: returnValue = pt_from_DPhi_DT_ellipse(2, 3, 2, 4, DTTF_phib2_phib3, DTTF_phib2_phib4)
      
      if ok_DTTF_st1 and ok_DTTF_st2 and ok_DTTF_st3 and ok_DTTF_st4: returnValue = pt_from_DPhi_DT_ellipse(1, 4, 2, 3, DTTF_phib1_phib4, DTTF_phib2_phib3)

    return returnValue, L1Mu_eta
