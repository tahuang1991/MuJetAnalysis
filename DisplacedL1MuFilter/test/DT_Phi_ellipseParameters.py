import array
from ROOT import *
from cuts import *
import math
import array
from math import log10, floor
from logic import *
import numpy as np
import os
import random

    
## PT : [a_axis_, b_axis, alpha[deg] ]
dphi_dict = {}

## the dictionary is ordened by station combination and by priority basedon best background rejection

## 3 station combinations 1-2-3
dphi_dict['DPhib_MB1_MB3__DPhib_MB2_MB3'] = {                                                      
  3 : [ 0.12 , 0.48 , 53.0 ], #Acceptance 0.900242530849  #Rejection 0.684418145957
  5 : [ 0.08 , 0.22 , 59.0 ], #Acceptance 0.900314517925  #Rejection 0.765285996055
  7 : [ 0.16 , 0.08 , 45.0 ], #Acceptance 0.900654529625  #Rejection 0.841927303466
  10 : [ 0.06 , 0.22 , 53.0 ], #Acceptance 0.903643186616  #Rejection 0.898844744999
  15 : [ 0.18 , 0.06 , 58.0 ], #Acceptance 0.900689995071  #Rejection 0.937447168216
  20 : [ 0.14 , 0.06 , 55.0 ], #Acceptance 0.904300798352  #Rejection 0.94674556213
  30 : [ 0.1 , 0.06 , 52.0 ], #Acceptance 0.900384480951  #Rejection 0.954916877994
  40 : [ 0.04 , 0.2 , 50.0 ], #Acceptance 0.900641025641  #Rejection 0.96449704142
  }

dphi_dict['DPhib_MB1_MB2__DPhib_MB2_MB3'] = {                                                      
  3 : [ 0.26 , 0.1 , 27.0 ], #Acceptance 0.90009594627  #Rejection 0.680473372781
  5 : [ 0.1 , 0.16 , 32.0 ], #Acceptance 0.900453685148  #Rejection 0.76190476190
  7 : [ 0.08 , 0.12 , 29.0 ], #Acceptance 0.901789462229  #Rejection 0.83798253029
  10 : [ 0.18 , 0.06 , 37.0 ], #Acceptance 0.901688687358  #Rejection 0.897717666948
  15 : [ 0.08 , 0.06 , 34.0 ], #Acceptance 0.900320354855  #Rejection 0.9056072133
  20 : [ 0.04 , 0.18 , 29.0 ], #Acceptance 0.902137522534  #Rejection 0.949281487743
  30 : [ 0.04 , 0.12 , 29.0 ], #Acceptance 0.905277874869  #Rejection 0.950972104818
  40 : [ 0.12 , 0.04 , 37.0 ], #Acceptance 0.902243589744  #Rejection 0.952662721893
  }

dphi_dict['DPhib_MB1_MB2__DPhib_MB1_MB3'] = {
  3 : [ 0.18 , 0.28 , 20.0 ], #Acceptance 0.900109272141  #Rejection 0.682727528881
  5 : [ 0.1 , 0.16 , 34.0 ], #Acceptance 0.900133600534  #Rejection 0.761904761905
  7 : [ 0.1 , 0.16 , 27.0 ], #Acceptance 0.90124531646  #Rejection 0.839954916878
  10 : [ 0.08 , 0.32 , 33.0 ], #Acceptance 0.90010554296  #Rejection 0.898562975486
  15 : [ 0.06 , 0.18 , 30.0 ], #Acceptance 0.901028831937  #Rejection 0.934911242604
  20 : [ 0.22 , 0.06 , 28.0 ], #Acceptance 0.900283286119  #Rejection 0.950690335306
  30 : [ 0.06 , 0.1 , 20.0 ], #Acceptance 0.903180706047  #Rejection 0.952662721893
  40 : [ 0.04 , 0.16 , 24.0 ], #Acceptance 0.900641025641  #Rejection 0.955198647506
  }


## 3 station combinations 1-2-4
dphi_dict['DPhib_MB1_MB4__DPhib_MB2_MB4'] = {                                                      
  3 : [ 0.3 , 0.2 , 39.0 ], #Acceptance 0.900537475636  #Rejection 0.623664122137
  5 : [ 0.16 , 0.46 , 50.0 ], #Acceptance 0.900345210698  #Rejection 0.63893129771
  7 : [ 0.14 , 0.34 , 47.0 ], #Acceptance 0.901468960878  #Rejection 0.775572519084
  10 : [ 0.08 , 0.38 , 50.0 ], #Acceptance 0.900614030321  #Rejection 0.893129770992
  15 : [ 0.06 , 0.2 , 50.0 ], #Acceptance 0.901374673462  #Rejection 0.954198473282
  20 : [ 0.06 , 0.24 , 44.0 ], #Acceptance 0.900548159749  #Rejection 0.967938931298
  30 : [ 0.06 , 0.16 , 41.0 ], #Acceptance 0.901699029126  #Rejection 0.973282442748
  40 : [ 0.06 , 0.16 , 38.0 ], #Acceptance 0.900332225914  #Rejection 0.975572519084
  }

dphi_dict['DPhib_MB1_MB2__DPhib_MB1_MB4'] = {                                                      
  3 : [ 0.2 , 0.44 , 14.0 ], #Acceptance 0.900005906326  #Rejection 0.625190839695
  5 : [ 0.18 , 0.0 , 8.0 ], #Acceptance 0.900484088564  #Rejection 0.645038167939
  7 : [ 0.3 , 0.14 , 19.0 ], #Acceptance 0.9002104715  #Rejection 0.775572519084
  10 : [ 0.32 , 0.1 , 12.0 ], #Acceptance 0.900233657556  #Rejection 0.893129770992
  15 : [ 0.08 , 0.08 , 5.0 ], #Acceptance 0.901802920646  #Rejection 0.945801526718
  20 : [ 0.06 , 0.0 , 11.0 ], #Acceptance 0.910870648537  #Rejection 0.967175572519
  30 : [ 0.06 , 0.08 , 17.0 ], #Acceptance 0.903155339806  #Rejection 0.970229007634
  40 : [ 0.06 , 0.08 , 17.0 ], #Acceptance 0.915836101883  #Rejection 0.970229007634
  }    

dphi_dict['DPhib_MB1_MB2__DPhib_MB2_MB4'] = {                                                      
  3 : [ 0.34 , 0.14 , 18.0 ], #Acceptance 0.900872167425  #Rejection 0.620610687023
  5 : [ 0.0 , 0.14 , 15.0 ], #Acceptance 0.90318228712  #Rejection 0.641984732824
  7 : [ 0.4 , 0.1 , 18.0 ], #Acceptance 0.900275565778  #Rejection 0.771755725191
  10 : [ 0.06 , 0.2 , 13.0 ], #Acceptance 0.902678911047  #Rejection 0.887022900763
  15 : [ 0.06 , 0.14 , 23.0 ], #Acceptance 0.905014774528  #Rejection 0.940458015267
  20 : [ 0.0 , 0.04 , 18.0 ], #Acceptance 0.901758382573  #Rejection 0.967175572519
  30 : [ 0.16 , 0.04 , 15.0 ], #Acceptance 0.900970873786  #Rejection 0.971755725191
  40 : [ 0.04 , 0.2 , 23.0 ], #Acceptance 0.900332225914  #Rejection 0.974809160305
  }



## 3 station combinations 1-3-4
dphi_dict['DPhib_MB1_MB3__DPhib_MB1_MB4'] = {                                                      
  3 : [ 0.22 , 0.24 , 27.0 ], #Acceptance 0.900484453734  #Rejection 0.62540929928
  5 : [ 0.0 , 0.22 , 34.0 ], #Acceptance 0.900556543879  #Rejection 0.642436149312
  7 : [ 0.16 , 0.2 , 30.0 ], #Acceptance 0.900058673968  #Rejection 0.768827766863
  10 : [ 0.12 , 0.14 , 39.0 ], #Acceptance 0.900017869907  #Rejection 0.891290111329
  15 : [ 0.08 , 0.1 , 27.0 ], #Acceptance 0.900425682866  #Rejection 0.951538965291
  20 : [ 0.06 , 0.1 , 27.0 ], #Acceptance 0.90090143518  #Rejection 0.966601178782
  30 : [ 0.24 , 0.06 , 31.0 ], #Acceptance 0.900542495479  #Rejection 0.973804846103
  40 : [ 0.06 , 0.12 , 26.0 ], #Acceptance 0.902506963788  #Rejection 0.976424361493
  }

dphi_dict['DPhib_MB1_MB4__DPhib_MB3_MB4'] = {                                                      
  3 : [ 0.16 , 0.44 , 75.0 ], #Acceptance 0.90106774251  #Rejection 0.62278978389
  5 : [ 0.34 , 0.12 , 70.0 ], #Acceptance 0.900181162377  #Rejection 0.64047151277
  7 : [ 0.12 , 0.34 , 75.0 ], #Acceptance 0.900236473872  #Rejection 0.768827766863
  10 : [ 0.08 , 0.18 , 78.0 ], #Acceptance 0.904820407434  #Rejection 0.889980353635
  15 : [ 0.06 , 0.2 , 75.0 ], #Acceptance 0.902305782192  #Rejection 0.949574328749
  20 : [ 0.06 , 0.1 , 72.0 ], #Acceptance 0.901020045072  #Rejection 0.967256057629
  30 : [ 0.12 , 0.06 , 74.0 ], #Acceptance 0.900542495479  #Rejection 0.972495088409
  40 : [ 0.04 , 0.18 , 75.0 ], #Acceptance 0.901578458682  #Rejection 0.977079240341
  }

dphi_dict['DPhib_MB1_MB3__DPhib_MB3_MB4'] = {                                                      
  3 : [ 0.14 , 0.0 , 54.0 ], #Acceptance 0.901019135112  #Rejection 0.627373935822
  5 : [ 0.26 , 0.14 , 46.0 ], #Acceptance 0.900279087986  #Rejection 0.64047151277
  7 : [ 0.1 , 0.28 , 45.0 ], #Acceptance 0.900787653575  #Rejection 0.751146037983
  10 : [ 0.08 , 0.12 , 51.0 ], #Acceptance 0.905535203717  #Rejection 0.88605108055
  15 : [ 0.06 , 0.1 , 51.0 ], #Acceptance 0.900957786449  #Rejection 0.941060903733
  20 : [ 0.06 , 0.08 , 57.0 ], #Acceptance 0.901079350018  #Rejection 0.948919449902
  30 : [ 0.04 , 0.12 , 51.0 ], #Acceptance 0.900542495479  #Rejection 0.973804846103
  40 : [ 0.04 , 0.12 , 48.0 ], #Acceptance 0.907149489322  #Rejection 0.974459724951
  }


## 3 station combinations 2-3-4
dphi_dict['DPhib_MB2_MB4__DPhib_MB3_MB4'] = {                                                      
  3 : [ 0.4 , 0.12 , 64.0 ], #Acceptance 0.900904984973  #Rejection 0.581612258494
  5 : [ 0.34 , 0.12 , 64.0 ], #Acceptance 0.901566411801  #Rejection 0.596935376416
  7 : [ 0.08 , 0.24 , 56.0 ], #Acceptance 0.900158654024  #Rejection 0.727514990007
  10 : [ 0.08 , 0.3 , 69.0 ], #Acceptance 0.900016111584  #Rejection 0.834776815456
  15 : [ 0.06 , 0.22 , 69.0 ], #Acceptance 0.900998003992  #Rejection 0.90073284477
  20 : [ 0.06 , 0.16 , 66.0 ], #Acceptance 0.900607902736  #Rejection 0.9127248501
  30 : [ 0.06 , 0.18 , 63.0 ], #Acceptance 0.900082747207  #Rejection 0.91672218521
  40 : [ 0.06 , 0.22 , 63.0 ], #Acceptance 0.900186567164  #Rejection 0.916055962692
}

dphi_dict['DPhib_MB2_MB3__DPhib_MB2_MB4'] = {                                                      
  3 : [ 0.18 , 0.14 , 45.0 ], #Acceptance 0.900015111066  #Rejection 0.580946035976
  5 : [ 0.18 , 0.14 , 36.0 ], #Acceptance 0.900652953515  #Rejection 0.596269153897
  7 : [ 0.12 , 0.14 , 43.0 ], #Acceptance 0.901818986828  #Rejection 0.728181212525
  10 : [ 0.08 , 0.22 , 30.0 ], #Acceptance 0.900407392916  #Rejection 0.832778147901
  15 : [ 0.06 , 0.18 , 30.0 ], #Acceptance 0.901433496643  #Rejection 0.898067954697
  20 : [ 0.06 , 0.28 , 36.0 ], #Acceptance 0.900729483283  #Rejection 0.918054630247
  30 : [ 0.06 , 0.18 , 39.0 ], #Acceptance 0.900082747207  #Rejection 0.926715522985
  40 : [ 0.06 , 0.0 , 39.0 ], #Acceptance 0.902052238806  #Rejection 0.92071952032
  }

dphi_dict['DPhib_MB2_MB3__DPhib_MB3_MB4'] = {                                                      
  3 : [ 0.44 , 0.1 , 49.0 ], #Acceptance 0.900250172098  #Rejection 0.576282478348
  5 : [ 0.26 , 0.1 , 49.0 ], #Acceptance 0.900500710468  #Rejection 0.590273151233
  7 : [ 0.26 , 0.08 , 46.0 ], #Acceptance 0.90021399845  #Rejection 0.725516322452
  10 : [ 0.32 , 0.06 , 40.0 ], #Acceptance 0.900246277073  #Rejection 0.832111925383
  15 : [ 0.06 , 0.08 , 48.0 ], #Acceptance 0.901288332426  #Rejection 0.855429713524
  20 : [ 0.36 , 0.04 , 40.0 ], #Acceptance 0.900425531915  #Rejection 0.920053297801
  30 : [ 0.16 , 0.04 , 40.0 ], #Acceptance 0.900082747207  #Rejection 0.924050632911
  40 : [ 0.22 , 0.04 , 40.0 ], #Acceptance 0.900186567164  #Rejection 0.921385742838
  }


## 4 station combinations
dphi_dict['DPhib_MB1_MB4__DPhib_MB2_MB3'] = {                                                      
  3 : [ 0.2 , 0.38 , 73.0 ], #Acceptance 0.900453629032  #Rejection 0.615724381625
  5 : [ 0.0 , 0.2 , 71.0 ], #Acceptance 0.900332456019  #Rejection 0.632508833922
  7 : [ 0.42 , 0.14 , 80.0 ], #Acceptance 0.900380822678  #Rejection 0.764134275618
  10 : [ 0.0 , 0.1 , 77.0 ], #Acceptance 0.902040042948  #Rejection 0.888692579505
  15 : [ 0.08 , 0.16 , 79.0 ], #Acceptance 0.901094527363  #Rejection 0.950530035336
  20 : [ 0.0 , 0.06 , 77.0 ], #Acceptance 0.908326463314  #Rejection 0.966431095406
  30 : [ 0.14 , 0.06 , 71.0 ], #Acceptance 0.902158676759  #Rejection 0.971731448763
  40 : [ 0.08 , 0.06 , 71.0 ], #Acceptance 0.901028277635  #Rejection 0.973498233216
  }

dphi_dict['DPhib_MB1_MB3__DPhib_MB2_MB4'] = {                                                      
  3 : [ 0.14 , 0.34 , 44.0 ], #Acceptance 0.900843108504  #Rejection 0.60777385159
  5 : [ 0.44 , 0.18 , 43.0 ], #Acceptance 0.900170845454  #Rejection 0.628975265018
  7 : [ 0.12 , 0.0 , 38.0 ], #Acceptance 0.902221885955  #Rejection 0.764134275618
  10 : [ 0.18 , 0.1 , 43.0 ], #Acceptance 0.900682119624  #Rejection 0.876325088339
  15 : [ 0.08 , 0.12 , 45.0 ], #Acceptance 0.904228855721  #Rejection 0.931978798587
  20 : [ 0.28 , 0.06 , 46.0 ], #Acceptance 0.900577081616  #Rejection 0.95406360424
  30 : [ 0.12 , 0.06 , 43.0 ], #Acceptance 0.902719372021  #Rejection 0.962897526502
  40 : [ 0.06 , 0.08 , 48.0 ], #Acceptance 0.901028277635  #Rejection 0.970848056537
  }

dphi_dict['DPhib_MB1_MB2__DPhib_MB3_MB4'] = {                                                      
  3 : [ 0.16 , 0.1 , 40.0 ], #Acceptance 0.900843108504  #Rejection 0.541519434629
  5 : [ 0.1 , 0.12 , 32.0 ], #Acceptance 0.901325206631  #Rejection 0.554770318021
  7 : [ 0.08 , 0.1 , 32.0 ], #Acceptance 0.903205467706  #Rejection 0.663427561837
  10 : [ 0.06 , 0.1 , 32.0 ], #Acceptance 0.9057980168  #Rejection 0.775618374558
  15 : [ 0.06 , 0.08 , 29.0 ], #Acceptance 0.911791044776  #Rejection 0.787102473498
  20 : [ 0.06 , 0.08 , 29.0 ], #Acceptance 0.911953833471  #Rejection 0.787102473498
  30 : [ 0.06 , 0.08 , 29.0 ], #Acceptance 0.912251191477  #Rejection 0.787102473498
  40 : [ 0.06 , 0.08 , 29.0 ], #Acceptance 0.915167095116  #Rejection 0.787102473498
  }






#______________________________________________________________________________
def getEllipseParameters(dphi11, dphi12, dphi21, dphi22, pt):
  dphiString = 'DPhib_MB%d_MB%d__DPhib_MB%d_MB%d'%(dphi11, dphi12, dphi21, dphi22)
  return dphi_dict[dphiString][pt]


#______________________________________________________________________________
def getEllipseParametersString(dphiString, pt):
  return dphi_dict[dphiString][pt]


#______________________________________________________________________________
def getEllipse(x,y,a,b, alpha=0, x0=0, y0=0):
  rad_alpha = alpha/180*2*pi
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
      'DPhib_MB1_MB3__DPhib_MB2_MB3'
      'DPhib_MB1_MB2__DPhib_MB2_MB3',                                                      
      'DPhib_MB1_MB2__DPhib_MB1_MB3']
    return combinations[0]
    

  if 1 in stations and 2 in stations and 4 in stations:
    combinations = [
      'DPhib_MB1_MB4__DPhib_MB2_MB4',                                                      
      'DPhib_MB1_MB2__DPhib_MB1_MB4',                                                      
      'DPhib_MB1_MB2__DPhib_MB2_MB4']                                                      
    return combinations[0]


  if 1 in stations and 3 in stations and 4 in stations:
    combinations = [
      'DPhib_MB1_MB3__DPhib_MB1_MB4',                                                      
      'DPhib_MB1_MB4__DPhib_MB3_MB4',                                                      
      'DPhib_MB1_MB3__DPhib_MB3_MB4']                                                      
    return combinations[0]


  if 2 in stations and 3 in stations and 4 in stations:
    combinations = [
      'DPhib_MB2_MB4__DPhib_MB3_MB4',                                                      
      'DPhib_MB2_MB3__DPhib_MB2_MB4',                                                      
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
  
  dphiString = get_best_combination_station([dphi11, dphi12, dphi21, dphi22])

  for ptCut in [40, 30, 20, 15, 10, 7, 5, 3]:
    ## get the parameters for this ellips
    params = getEllipseParametersString(dphiString, ptCut)
    a_axis = params[0]
    b_axis = params[1]
    alpha  = params[2]

    if passEllipse(x, y, a_axis, b_axis, alpha):
      return ptCut

  return default_pt


