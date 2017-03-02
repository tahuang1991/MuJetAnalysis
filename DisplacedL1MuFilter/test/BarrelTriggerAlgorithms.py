## this file contains the pT assignment functions
from Helpers import *
from ROOT import *
from math import *

## PT : [a_axis_, b_axis, alpha[deg] ]
dphi_dict = {}

## the dictionary is ordened by station combination and by priority basedon best background rejection


## 3 station combinations 1-2-3
dphi_dict['DPhib_MB1_MB3__DPhib_MB2_MB3'] = {                                                      
  3 : [ 0.39 , 0.19 , 55.0 ], #Acceptance 0.900254703804  #Rejection 0.648069878839
  5 : [ 0.31 , 0.09 , 45.0 ], #Acceptance 0.901193978197  #Rejection 0.744998591152
  7 : [ 0.09 , 0.37 , 50.0 ], #Acceptance 0.90129051325  #Rejection 0.830092983939
  10 : [ 0.07 , 0.29 , 50.0 ], #Acceptance 0.900205233453  #Rejection 0.892082276698
  15 : [ 0.05 , 0.31 , 53.0 ], #Acceptance 0.900966183575  #Rejection 0.921949845027
  20 : [ 0.05 , 0.17 , 53.0 ], #Acceptance 0.90065681445  #Rejection 0.931811777966
  30 : [ 0.07 , 0.37 , 60.0 ], #Acceptance 0.900722021661  #Rejection 0.934065934066
  40 : [ 0.05 , 0.33 , 47.0 ], #Acceptance 0.901098901099  #Rejection 0.951253874331
  }

dphi_dict['DPhib_MB1_MB2__DPhib_MB2_MB3'] = {                                                      
  3 : [ 0.13 , 0.47 , 26.0 ], #Acceptance 0.900090378769  #Rejection 0.647224570301
  5 : [ 0.09 , 0.43 , 35.0 ], #Acceptance 0.900155736287  #Rejection 0.74471682164
  7 : [ 0.07 , 0.21 , 35.0 ], #Acceptance 0.900896463403  #Rejection 0.832065370527
  10 : [ 0.05 , 0.23 , 38.0 ], #Acceptance 0.901487942535  #Rejection 0.883629191321
  15 : [ 0.05 , 0.17 , 32.0 ], #Acceptance 0.90294246816  #Rejection 0.917441532826
  20 : [ 0.05 , 0.17 , 26.0 ], #Acceptance 0.900246305419  #Rejection 0.925894618202
  30 : [ 0.05 , 0.11 , 26.0 ], #Acceptance 0.904332129964  #Rejection 0.929839391378
  40 : [ 0.05 , 0.09 , 26.0 ], #Acceptance 0.934065934066  #Rejection 0.930966469428
  }

dphi_dict['DPhib_MB1_MB2__DPhib_MB1_MB3'] = {
  3 : [ 0.19 , 0.41 , 23.0 ], #Acceptance 0.900090378769  #Rejection 0.650042265427
  5 : [ 0.15 , 0.17 , 35.0 ], #Acceptance 0.900415296764  #Rejection 0.74584389969
  7 : [ 0.11 , 0.47 , 26.0 ], #Acceptance 0.900009851246  #Rejection 0.834037757115
  10 : [ 0.09 , 0.27 , 20.0 ], #Acceptance 0.900205233453  #Rejection 0.894054663285
  15 : [ 0.41 , 0.07 , 22.0 ], #Acceptance 0.90008783487  #Rejection 0.919413919414
  20 : [ 0.23 , 0.07 , 28.0 ], #Acceptance 0.901067323481  #Rejection 0.935474781629
  30 : [ 0.17 , 0.07 , 28.0 ], #Acceptance 0.900722021661  #Rejection 0.936038320654
  40 : [ 0.05 , 0.19 , 26.0 ], #Acceptance 0.901098901099  #Rejection 0.962806424345
  }


## 3 station combinations 1-2-4
dphi_dict['DPhib_MB1_MB4__DPhib_MB2_MB4'] = {                                                      
  3 : [ 0.47 , 0.15 , 42.0 ], #Acceptance 0.901776519053  #Rejection 0.58320610687
  5 : [ 0.17 , 0.49 , 50.0 ], #Acceptance 0.900311931375  #Rejection 0.60534351145
  7 : [ 0.29 , 0.15 , 36.0 ], #Acceptance 0.900507614213  #Rejection 0.754961832061
  10 : [ 0.31 , 0.07 , 42.0 ], #Acceptance 0.901667298219  #Rejection 0.884732824427
  15 : [ 0.07 , 0.19 , 47.0 ], #Acceptance 0.904511030622  #Rejection 0.949618320611
  20 : [ 0.05 , 0.17 , 50.0 ], #Acceptance 0.904282115869  #Rejection 0.967175572519
  30 : [ 0.05 , 0.09 , 50.0 ], #Acceptance 0.908333333333  #Rejection 0.974809160305
  40 : [ 0.05 , 0.35 , 44.0 ], #Acceptance 0.916666666667  #Rejection 0.974809160305
  }

dphi_dict['DPhib_MB1_MB2__DPhib_MB1_MB4'] = {                                                      
  3 : [ 0.21 , 0.41 , 11.0 ], #Acceptance 0.900102986612  #Rejection 0.593893129771
  5 : [ 0.21 , 0.23 , 20.0 ], #Acceptance 0.900311931375  #Rejection 0.603053435115
  7 : [ 0.33 , 0.15 , 12.0 ], #Acceptance 0.900507614213  #Rejection 0.758778625954
  10 : [ 0.11 , 0.13 , 14.0 ], #Acceptance 0.902425161046  #Rejection 0.880152671756
  15 : [ 0.19 , 0.07 , 19.0 ], #Acceptance 0.900230490616  #Rejection 0.949618320611
  20 : [ 0.07 , 0.07 , 5.0 ], #Acceptance 0.900503778338  #Rejection 0.964885496183
  30 : [ 0.05 , 0.27 , 11.0 ], #Acceptance 0.902777777778  #Rejection 0.975572519084
  40 : [ 0.15 , 0.05 , 6.0 ], #Acceptance 0.916666666667  #Rejection 0.976335877863
  }    

dphi_dict['DPhib_MB1_MB2__DPhib_MB2_MB4'] = {                                                      
  3 : [ 0.13 , 0.29 , 13.0 ], #Acceptance 0.900360453141  #Rejection 0.580916030534
  5 : [ 0.41 , 0.13 , 21.0 ], #Acceptance 0.900051988563  #Rejection 0.604580152672
  7 : [ 0.47 , 0.11 , 15.0 ], #Acceptance 0.900507614213  #Rejection 0.751145038168
  10 : [ 0.43 , 0.07 , 18.0 ], #Acceptance 0.900530503979  #Rejection 0.890839694656
  15 : [ 0.25 , 0.05 , 18.0 ], #Acceptance 0.900559762924  #Rejection 0.954198473282
  20 : [ 0.11 , 0.05 , 15.0 ], #Acceptance 0.907430730479  #Rejection 0.961832061069
  30 : [ 0.09 , 0.05 , 15.0 ], #Acceptance 0.916666666667  #Rejection 0.964122137405
  40 : [ 0.17 , 0.03 , 21.0 ], #Acceptance 0.916666666667  #Rejection 0.976335877863
  }



## 3 station combinations 1-3-4
dphi_dict['DPhib_MB1_MB3__DPhib_MB1_MB4'] = {                                                      
  3 : [ 0.23 , 0.39 , 36.0 ], #Acceptance 0.900840336134  #Rejection 0.584151931893
  5 : [ 0.23 , 0.33 , 29.0 ], #Acceptance 0.900052994171  #Rejection 0.60248853962
  7 : [ 0.19 , 0.17 , 30.0 ], #Acceptance 0.900667681855  #Rejection 0.751146037983
  10 : [ 0.13 , 0.11 , 32.0 ], #Acceptance 0.904398289554  #Rejection 0.886705959398
  15 : [ 0.11 , 0.07 , 35.0 ], #Acceptance 0.902361369063  #Rejection 0.948919449902
  20 : [ 0.05 , 0.15 , 27.0 ], #Acceptance 0.900150526844  #Rejection 0.968565815324
  30 : [ 0.05 , 0.15 , 36.0 ], #Acceptance 0.901746724891  #Rejection 0.977734119188
  40 : [ 0.13 , 0.05 , 31.0 ], #Acceptance 0.909090909091  #Rejection 0.97969875573
  }

dphi_dict['DPhib_MB1_MB4__DPhib_MB3_MB4'] = {                                                      
  3 : [ 0.19 , 0.43 , 72.0 ], #Acceptance 0.900735294118  #Rejection 0.581532416503
  5 : [ 0.27 , 0.13 , 73.0 ], #Acceptance 0.901430842607  #Rejection 0.598559266536
  7 : [ 0.33 , 0.11 , 67.0 ], #Acceptance 0.901136230526  #Rejection 0.749836280288
  10 : [ 0.13 , 0.09 , 70.0 ], #Acceptance 0.901496640195  #Rejection 0.885396201703
  15 : [ 0.29 , 0.07 , 80.0 ], #Acceptance 0.90023879013  #Rejection 0.950884086444
  20 : [ 0.05 , 0.13 , 75.0 ], #Acceptance 0.901655795283  #Rejection 0.967256057629
  30 : [ 0.05 , 0.09 , 69.0 ], #Acceptance 0.903930131004  #Rejection 0.977079240341
  40 : [ 0.09 , 0.05 , 74.0 ], #Acceptance 0.909090909091  #Rejection 0.978388998035
  }

dphi_dict['DPhib_MB1_MB3__DPhib_MB3_MB4'] = {                                                      
  3 : [ 0.15 , 0.41 , 51.0 ], #Acceptance 0.900105042017  #Rejection 0.582842174198
  5 : [ 0.15 , 0.23 , 51.0 ], #Acceptance 0.900158982512  #Rejection 0.601178781925
  7 : [ 0.19 , 0.11 , 52.0 ], #Acceptance 0.901136230526  #Rejection 0.744597249509
  10 : [ 0.07 , 0.35 , 45.0 ], #Acceptance 0.900580329872  #Rejection 0.867059593975
  15 : [ 0.19 , 0.05 , 53.0 ], #Acceptance 0.90023879013  #Rejection 0.924688932547
  20 : [ 0.05 , 0.09 , 51.0 ], #Acceptance 0.905669844456  #Rejection 0.966601178782
  30 : [ 0.05 , 0.07 , 48.0 ], #Acceptance 0.901746724891  #Rejection 0.966601178782
  40 : [ 0.03 , 0.25 , 48.0 ], #Acceptance 0.909090909091  #Rejection 0.977734119188
  }


## 3 station combinations 2-3-4
dphi_dict['DPhib_MB2_MB4__DPhib_MB3_MB4'] = {                                                      
  3 : [ 0.37 , 0.13 , 64.0 ], #Acceptance 0.900010659844  #Rejection 0.550299800133
  5 : [ 0.11 , 0.31 , 56.0 ], #Acceptance 0.90076418039  #Rejection 0.57161892072
  7 : [ 0.41 , 0.09 , 64.0 ], #Acceptance 0.901395016096  #Rejection 0.716189207195
  10 : [ 0.19 , 0.09 , 55.0 ], #Acceptance 0.900107742035  #Rejection 0.8254497002
  15 : [ 0.17 , 0.05 , 64.0 ], #Acceptance 0.904545454545  #Rejection 0.893404397069
  20 : [ 0.05 , 0.19 , 69.0 ], #Acceptance 0.900404448938  #Rejection 0.929380413058
  30 : [ 0.05 , 0.15 , 69.0 ], #Acceptance 0.907079646018  #Rejection 0.931379080613
  40 : [ 0.15 , 0.05 , 64.0 ], #Acceptance 0.90625  #Rejection 0.896069287142
  }

dphi_dict['DPhib_MB2_MB3__DPhib_MB2_MB4'] = {                                                      
  3 : [ 0.17 , 0.21 , 38.0 ], #Acceptance 0.900223856732  #Rejection 0.550299800133
  5 : [ 0.17 , 0.23 , 33.0 ], #Acceptance 0.900010763104  #Rejection 0.574283810793
  7 : [ 0.13 , 0.21 , 36.0 ], #Acceptance 0.901395016096  #Rejection 0.718854097268
  10 : [ 0.07 , 0.11 , 37.0 ], #Acceptance 0.904109589041  #Rejection 0.826782145237
  15 : [ 0.07 , 0.21 , 42.0 ], #Acceptance 0.900534759358  #Rejection 0.898734177215
  20 : [ 0.05 , 0.25 , 30.0 ], #Acceptance 0.900910010111  #Rejection 0.922051965356
  30 : [ 0.33 , 0.05 , 44.0 ], #Acceptance 0.900442477876  #Rejection 0.932045303131
  40 : [ 0.13 , 0.05 , 38.0 ], #Acceptance 0.90625  #Rejection 0.912058627582
  }

dphi_dict['DPhib_MB2_MB3__DPhib_MB3_MB4'] = {                                                      
  3 : [ 0.11 , 0.25 , 38.0 ], #Acceptance 0.900010659844  #Rejection 0.548301132578
  5 : [ 0.25 , 0.11 , 46.0 ], #Acceptance 0.900226025186  #Rejection 0.569620253165
  7 : [ 0.13 , 0.09 , 40.0 ], #Acceptance 0.900918087516  #Rejection 0.706862091939
  10 : [ 0.07 , 0.09 , 35.0 ], #Acceptance 0.902416499923  #Rejection 0.811459027315
  15 : [ 0.11 , 0.05 , 37.0 ], #Acceptance 0.902139037433  #Rejection 0.882744836775
  20 : [ 0.05 , 0.09 , 48.0 ], #Acceptance 0.903437815976  #Rejection 0.887408394404
  30 : [ 0.05 , 0.09 , 48.0 ], #Acceptance 0.904867256637  #Rejection 0.887408394404
  40 : [ 0.11 , 0.05 , 37.0 ], #Acceptance 0.90625  #Rejection 0.882744836775
  }


## 4 station combinations
dphi_dict['DPhib_MB1_MB4__DPhib_MB2_MB3'] = {                                                      
  3 : [ 0.35 , 0.21 , 80.0 ], #Acceptance 0.900401367623  #Rejection 0.57332155477
  5 : [ 0.21 , 0.35 , 66.0 ], #Acceptance 0.900330231162  #Rejection 0.597173144876
  7 : [ 0.27 , 0.15 , 80.0 ], #Acceptance 0.900970224155  #Rejection 0.745583038869
  10 : [ 0.11 , 0.15 , 66.0 ], #Acceptance 0.900283039408  #Rejection 0.885159010601
  15 : [ 0.07 , 0.29 , 69.0 ], #Acceptance 0.901819560273  #Rejection 0.947879858657
  20 : [ 0.09 , 0.07 , 80.0 ], #Acceptance 0.902737752161  #Rejection 0.962014134276
  30 : [ 0.33 , 0.05 , 74.0 ], #Acceptance 0.905844155844  #Rejection 0.975265017668
  40 : [ 0.33 , 0.05 , 74.0 ], #Acceptance 0.911111111111  #Rejection 0.975265017668
  }

dphi_dict['DPhib_MB1_MB3__DPhib_MB2_MB4'] = {                                                      
  3 : [ 0.15 , 0.27 , 47.0 ], #Acceptance 0.900995986324  #Rejection 0.578621908127
  5 : [ 0.15 , 0.25 , 47.0 ], #Acceptance 0.90108075653  #Rejection 0.592756183746
  7 : [ 0.13 , 0.29 , 38.0 ], #Acceptance 0.900301104048  #Rejection 0.75
  10 : [ 0.11 , 0.11 , 35.0 ], #Acceptance 0.900283039408  #Rejection 0.86925795053
  15 : [ 0.07 , 0.29 , 35.0 ], #Acceptance 0.900303260045  #Rejection 0.936395759717
  20 : [ 0.07 , 0.09 , 45.0 ], #Acceptance 0.906340057637  #Rejection 0.955830388693
  30 : [ 0.07 , 0.09 , 45.0 ], #Acceptance 0.915584415584  #Rejection 0.955830388693
  40 : [ 0.07 , 0.13 , 42.0 ], #Acceptance 0.911111111111  #Rejection 0.946996466431
  }

dphi_dict['DPhib_MB1_MB2__DPhib_MB3_MB4'] = {                                                      
  3 : [ 0.09 , 0.31 , 35.0 ], #Acceptance 0.900252712948  #Rejection 0.495583038869
  5 : [ 0.09 , 0.23 , 35.0 ], #Acceptance 0.902581807265  #Rejection 0.517667844523
  7 : [ 0.07 , 0.13 , 38.0 ], #Acceptance 0.902141184343  #Rejection 0.650176678445
  10 : [ 0.05 , 0.17 , 38.0 ], #Acceptance 0.902242543  #Rejection 0.776501766784
  15 : [ 0.05 , 0.15 , 29.0 ], #Acceptance 0.901061410159  #Rejection 0.828621908127
  20 : [ 0.05 , 0.11 , 29.0 ], #Acceptance 0.907780979827  #Rejection 0.839222614841
  30 : [ 0.05 , 0.11 , 29.0 ], #Acceptance 0.905844155844  #Rejection 0.839222614841
  40 : [ 0.05 , 0.09 , 29.0 ], #Acceptance 0.911111111111  #Rejection 0.840989399293
  }


#______________________________________________________________________________
def getEllipseParameters(dphi11, dphi12, dphi21, dphi22):
  return 'DPhib_MB%d_MB%d__DPhib_MB%d_MB%d'%(dphi11, dphi12, dphi21, dphi22)


#______________________________________________________________________________
def getEllipseParametersString(dphiString, pt):
  return dphi_dict[dphiString][pt]


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

    if passEllipse(x, y, a_axis, b_axis, alpha):
      return ptCut

  #print "returning default pt", default_pt
  return default_pt



def pt_from_DPhi_DT_ellipse_test():
  default_pt = 2
  dphi11, dphi12, dphi21, dphi22, x, y = 1, 2, 3, 4, 0.01, 0.01
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
        if     ok_DTTF_st1 and     ok_DTTF_st2 and     ok_DTTF_st3 and not ok_DTTF_st4: returnValue = pt_from_DPhi_DT_ellipse(1, 2, 1, 3, DTTF_phib1_phib2, DTTF_phib1_phib3)
        if     ok_DTTF_st1 and     ok_DTTF_st2 and not ok_DTTF_st3 and     ok_DTTF_st4: returnValue = pt_from_DPhi_DT_ellipse(1, 2, 1, 4, DTTF_phib1_phib2, DTTF_phib1_phib4)
        if     ok_DTTF_st1 and not ok_DTTF_st2 and     ok_DTTF_st3 and not ok_DTTF_st4: returnValue = pt_from_DPhi_DT_ellipse(1, 3, 1, 4, DTTF_phib1_phib3, DTTF_phib1_phib4)
        if not ok_DTTF_st1 and     ok_DTTF_st2 and     ok_DTTF_st3 and     ok_DTTF_st4: returnValue = pt_from_DPhi_DT_ellipse(2, 3, 2, 4, DTTF_phib2_phib3, DTTF_phib2_phib4)

        ## case 3: 4 stations
        if    ok_DTTF_st1 and      ok_DTTF_st2 and     ok_DTTF_st3 and     ok_DTTF_st4: returnValue = pt_from_DPhi_DT_ellipse(1, 4, 2, 3, DTTF_phib1_phib4, DTTF_phib2_phib3)

    return returnValue, L1Mu_eta


#  LocalWords:  dphi
