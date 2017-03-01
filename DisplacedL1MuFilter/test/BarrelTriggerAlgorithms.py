## this file contains the pT assignment functions
from Helpers import *
from ROOT import *
from math import *

## PT : [a_axis_, b_axis, alpha[deg] ]
dphi_dict = {}

## the dictionary is ordened by station combination and by priority basedon best background rejection

## 3 station combinations 1-2-3
dphi_dict['DPhib_MB1_MB3__DPhib_MB2_MB3'] = {                                                      
  3 : [ 0.31 , 0.11 , 45.0 ], #Acceptance 0.900029316916  #Rejection 0.680191603269
  5 : [ 0.45 , 0.13 , 58.0 ], #Acceptance 0.900439768426  #Rejection 0.763031839955
  7 : [ 0.15 , 0.07 , 48.0 ], #Acceptance 0.900172571944  #Rejection 0.841927303466
  10 : [ 0.07 , 0.21 , 50.0 ], #Acceptance 0.903017746853  #Rejection 0.898844744999
  15 : [ 0.05 , 0.15 , 53.0 ], #Acceptance 0.903739526861  #Rejection 0.933784164553
  20 : [ 0.37 , 0.05 , 58.0 ], #Acceptance 0.900077259851  #Rejection 0.951535643843
  30 : [ 0.35 , 0.05 , 55.0 ], #Acceptance 0.900034952814  #Rejection 0.958861651169
  40 : [ 0.21 , 0.05 , 55.0 ], #Acceptance 0.900641025641  #Rejection 0.960552268245
  }

dphi_dict['DPhib_MB1_MB2__DPhib_MB2_MB3'] = {                                                      
 3 : [ 0.11 , 0.25 , 35.0 ], #Acceptance 0.901108712454  #Rejection 0.676528599606
 5 : [ 0.09 , 0.23 , 35.0 ], #Acceptance 0.900634602538  #Rejection 0.764158918005
 7 : [ 0.07 , 0.31 , 32.0 ], #Acceptance 0.900157024922  #Rejection 0.841927303466
 10 : [ 0.05 , 0.17 , 38.0 ], #Acceptance 0.90071143773  #Rejection 0.89123696816
 15 : [ 0.05 , 0.13 , 26.0 ], #Acceptance 0.906542631838  #Rejection 0.92786700479
 20 : [ 0.05 , 0.09 , 29.0 ], #Acceptance 0.902189029101  #Rejection 0.929839391378
 30 : [ 0.05 , 0.09 , 26.0 ], #Acceptance 0.91104508913  #Rejection 0.930966469428
 40 : [ 0.05 , 0.09 , 26.0 ], #Acceptance 0.916666666667  #Rejection 0.930966469428
 }

dphi_dict['DPhib_MB1_MB2__DPhib_MB1_MB3'] = {
  3 : [ 0.15 , 0.49 , 32.0 ], #Acceptance 0.900069294528  #Rejection 0.681036911806
  5 : [ 0.13 , 0.45 , 30.0 ], #Acceptance 0.900258851035  #Rejection 0.76246830093
  7 : [ 0.11 , 0.15 , 33.0 ], #Acceptance 0.90093437602  #Rejection 0.842209072978
  10 : [ 0.09 , 0.11 , 20.0 ], #Acceptance 0.903721366586  #Rejection 0.898562975486
  15 : [ 0.11 , 0.07 , 28.0 ], #Acceptance 0.900597585017  #Rejection 0.937447168216
  20 : [ 0.05 , 0.17 , 27.0 ], #Acceptance 0.900077259851  #Rejection 0.942519019442
  30 : [ 0.25 , 0.05 , 22.0 ], #Acceptance 0.901083537225  #Rejection 0.957171034094
  40 : [ 0.23 , 0.05 , 25.0 ], #Acceptance 0.901442307692  #Rejection 0.964778810933
  }


## 3 station combinations 1-2-4
dphi_dict['DPhib_MB1_MB4__DPhib_MB2_MB4'] = {                                                      
  3 : [ 0.19 , 0.45 , 47.0 ], #Acceptance 0.900064969582  #Rejection 0.625190839695
  5 : [ 0.19 , 0.39 , 47.0 ], #Acceptance 0.900662645822  #Rejection 0.643511450382
  7 : [ 0.15 , 0.45 , 44.0 ], #Acceptance 0.901360470415  #Rejection 0.773282442748
  10 : [ 0.25 , 0.07 , 42.0 ], #Acceptance 0.900043471173  #Rejection 0.89465648855
  15 : [ 0.07 , 0.17 , 47.0 ], #Acceptance 0.902530940859  #Rejection 0.952671755725
  20 : [ 0.07 , 0.27 , 38.0 ], #Acceptance 0.900121022282  #Rejection 0.967175572519
  30 : [ 0.05 , 0.15 , 47.0 ], #Acceptance 0.902669902913  #Rejection 0.974045801527
  40 : [ 0.05 , 0.09 , 50.0 ], #Acceptance 0.901439645626  #Rejection 0.974809160305
  }

dphi_dict['DPhib_MB1_MB2__DPhib_MB1_MB4'] = {                                                      
  3 : [ 0.19 , 0.43 , 8.0 ], #Acceptance 0.900340598114  #Rejection 0.624427480916
  5 : [ 0.19 , 0.21 , 10.0 ], #Acceptance 0.900206332831  #Rejection 0.635114503817
  7 : [ 0.15 , 0.19 , 14.0 ], #Acceptance 0.900123679129  #Rejection 0.774809160305
  10 : [ 0.09 , 0.27 , 7.0 ], #Acceptance 0.900124979623  #Rejection 0.889312977099
  15 : [ 0.07 , 0.15 , 8.0 ], #Acceptance 0.900304055501  #Rejection 0.953435114504
  20 : [ 0.07 , 0.09 , 14.0 ], #Acceptance 0.908663771624  #Rejection 0.964122137405
  30 : [ 0.05 , 0.29 , 11.0 ], #Acceptance 0.901213592233  #Rejection 0.975572519084
  40 : [ 0.05 , 0.15 , 11.0 ], #Acceptance 0.900332225914  #Rejection 0.975572519084
  }    

dphi_dict['DPhib_MB1_MB2__DPhib_MB2_MB4'] = {                                                      
  3 : [ 0.31 , 0.13 , 21.0 ], #Acceptance 0.900124032839  #Rejection 0.617557251908
  5 : [ 0.11 , 0.35 , 13.0 ], #Acceptance 0.900563447345  #Rejection 0.631297709924
  7 : [ 0.07 , 0.43 , 16.0 ], #Acceptance 0.900557640983  #Rejection 0.769465648855
  10 : [ 0.25 , 0.07 , 18.0 ], #Acceptance 0.901537792751  #Rejection 0.891603053435
  15 : [ 0.21 , 0.05 , 18.0 ], #Acceptance 0.900817952122  #Rejection 0.954961832061
  20 : [ 0.05 , 0.15 , 23.0 ], #Acceptance 0.900263401438  #Rejection 0.96106870229
  30 : [ 0.09 , 0.05 , 15.0 ], #Acceptance 0.906553398058  #Rejection 0.964122137405
  40 : [ 0.09 , 0.05 , 15.0 ], #Acceptance 0.918050941307  #Rejection 0.964122137405
  }



## 3 station combinations 1-3-4
dphi_dict['DPhib_MB1_MB3__DPhib_MB1_MB4'] = {                                                      
  3 : [ 0.23 , 0.25 , 26.0 ], #Acceptance 0.900808503054  #Rejection 0.624099541585
  5 : [ 0.17 , 0.23 , 37.0 ], #Acceptance 0.900931925381  #Rejection 0.638506876228
  7 : [ 0.17 , 0.41 , 26.0 ], #Acceptance 0.900094233949  #Rejection 0.776031434185
  10 : [ 0.09 , 0.13 , 40.0 ], #Acceptance 0.902273945675  #Rejection 0.890635232482
  15 : [ 0.07 , 0.17 , 30.0 ], #Acceptance 0.902979780064  #Rejection 0.948919449902
  20 : [ 0.07 , 0.11 , 36.0 ], #Acceptance 0.901909619262  #Rejection 0.966601178782
  30 : [ 0.05 , 0.11 , 27.0 ], #Acceptance 0.902551737995  #Rejection 0.974459724951
  40 : [ 0.05 , 0.13 , 30.0 ], #Acceptance 0.902506963788  #Rejection 0.975114603798
  }

dphi_dict['DPhib_MB1_MB4__DPhib_MB3_MB4'] = {                                                      
  3 : [ 0.33 , 0.15 , 67.0 ], #Acceptance 0.900484453734  #Rejection 0.623444662737
  5 : [ 0.15 , 0.31 , 78.0 ], #Acceptance 0.901699009319  #Rejection 0.633922724296
  7 : [ 0.27 , 0.11 , 67.0 ], #Acceptance 0.900272033853  #Rejection 0.773411918795
  10 : [ 0.17 , 0.07 , 70.0 ], #Acceptance 0.901514474625  #Rejection 0.890635232482
  15 : [ 0.07 , 0.21 , 69.0 ], #Acceptance 0.900957786449  #Rejection 0.952848722986
  20 : [ 0.05 , 0.19 , 75.0 ], #Acceptance 0.90090143518  #Rejection 0.96463654224
  30 : [ 0.05 , 0.15 , 69.0 ], #Acceptance 0.900743419731  #Rejection 0.974459724951
  40 : [ 0.05 , 0.13 , 69.0 ], #Acceptance 0.901578458682  #Rejection 0.975114603798
  }

dphi_dict['DPhib_MB1_MB3__DPhib_MB3_MB4'] = {                                                      
  3 : [ 0.15 , 0.17 , 60.0 ], #Acceptance 0.900565466064  #Rejection 0.618205631958
  5 : [ 0.15 , 0.15 , 45.0 ], #Acceptance 0.901796934928  #Rejection 0.62540929928
  7 : [ 0.11 , 0.17 , 51.0 ], #Acceptance 0.901054353431  #Rejection 0.765553372626
  10 : [ 0.07 , 0.21 , 45.0 ], #Acceptance 0.900799678342  #Rejection 0.879502292076
  15 : [ 0.05 , 0.45 , 48.0 ], #Acceptance 0.900035473572  #Rejection 0.948919449902
  20 : [ 0.05 , 0.11 , 51.0 ], #Acceptance 0.904696951726  #Rejection 0.96463654224
  30 : [ 0.05 , 0.09 , 51.0 ], #Acceptance 0.911593329315  #Rejection 0.966601178782
  40 : [ 0.05 , 0.09 , 51.0 ], #Acceptance 0.922934076137  #Rejection 0.966601178782
  }


## 3 station combinations 2-3-4
dphi_dict['DPhib_MB2_MB4__DPhib_MB3_MB4'] = {                                                      
  3 : [ 0.11 , 0.29 , 56.0 ], #Acceptance 0.900703504088  #Rejection 0.583610926049
  5 : [ 0.27 , 0.11 , 67.0 ], #Acceptance 0.90148183233  #Rejection 0.596269153897
  7 : [ 0.31 , 0.09 , 64.0 ], #Acceptance 0.901616057263  #Rejection 0.73017988008
  10 : [ 0.09 , 0.17 , 66.0 ], #Acceptance 0.901788385849  #Rejection 0.830779480346
  15 : [ 0.07 , 0.15 , 63.0 ], #Acceptance 0.900671384504  #Rejection 0.890739506995
  20 : [ 0.21 , 0.05 , 61.0 ], #Acceptance 0.900729483283  #Rejection 0.915389740173
  30 : [ 0.05 , 0.29 , 69.0 ], #Acceptance 0.900289615225  #Rejection 0.926715522985
  40 : [ 0.05 , 0.45 , 69.0 ], #Acceptance 0.900186567164  #Rejection 0.923384410393
  }

dphi_dict['DPhib_MB2_MB3__DPhib_MB2_MB4'] = {                                                      
  3 : [ 0.17 , 0.21 , 33.0 ], #Acceptance 0.901106465857  #Rejection 0.585609593604
  5 : [ 0.17 , 0.21 , 39.0 ], #Acceptance 0.900839028351  #Rejection 0.598934043971
  7 : [ 0.13 , 0.19 , 39.0 ], #Acceptance 0.90061985758  #Rejection 0.730846102598
  10 : [ 0.11 , 0.09 , 38.0 ], #Acceptance 0.90031532672  #Rejection 0.831445702865
  15 : [ 0.07 , 0.21 , 39.0 ], #Acceptance 0.90012701869  #Rejection 0.894070619587
  20 : [ 0.07 , 0.09 , 39.0 ], #Acceptance 0.90103343465  #Rejection 0.902731512325
  30 : [ 0.05 , 0.35 , 30.0 ], #Acceptance 0.900289615225  #Rejection 0.91672218521
  40 : [ 0.11 , 0.05 , 35.0 ], #Acceptance 0.901119402985  #Rejection 0.904063957362
  }

dphi_dict['DPhib_MB2_MB3__DPhib_MB3_MB4'] = {                                                      
  3 : [ 0.29 , 0.11 , 43.0 ], #Acceptance 0.900266962172  #Rejection 0.583610926049
  5 : [ 0.19 , 0.11 , 43.0 ], #Acceptance 0.900128560796  #Rejection 0.597601598934
  7 : [ 0.09 , 0.11 , 38.0 ], #Acceptance 0.90102571671  #Rejection 0.706862091939
  10 : [ 0.09 , 0.07 , 43.0 ], #Acceptance 0.900131194329  #Rejection 0.81745502998
  15 : [ 0.05 , 0.13 , 48.0 ], #Acceptance 0.906877154781  #Rejection 0.880079946702
  20 : [ 0.11 , 0.05 , 37.0 ], #Acceptance 0.908389057751  #Rejection 0.882744836775
  30 : [ 0.09 , 0.05 , 40.0 ], #Acceptance 0.902565163426  #Rejection 0.887408394404
  40 : [ 0.05 , 0.09 , 48.0 ], #Acceptance 0.900186567164  #Rejection 0.887408394404
  }


## 4 station combinations
dphi_dict['DPhib_MB1_MB4__DPhib_MB2_MB3'] = {                                                      
  3 : [ 0.33 , 0.21 , 71.0 ], #Acceptance 0.900361986804  #Rejection 0.620141342756
  5 : [ 0.19 , 0.31 , 70.0 ], #Acceptance 0.900609502701  #Rejection 0.632508833922
  7 : [ 0.15 , 0.25 , 73.0 ], #Acceptance 0.900027742049  #Rejection 0.763250883392
  10 : [ 0.11 , 0.13 , 76.0 ], #Acceptance 0.900682119624  #Rejection 0.886925795053
  15 : [ 0.07 , 0.25 , 69.0 ], #Acceptance 0.900895522388  #Rejection 0.947879858657
  20 : [ 0.11 , 0.07 , 74.0 ], #Acceptance 0.900329760923  #Rejection 0.962014134276
  30 : [ 0.05 , 0.49 , 66.0 ], #Acceptance 0.900196243342  #Rejection 0.974381625442
  40 : [ 0.43 , 0.05 , 71.0 ], #Acceptance 0.901028277635  #Rejection 0.976148409894
  }

dphi_dict['DPhib_MB1_MB3__DPhib_MB2_MB4'] = {                                                      
  3 : [ 0.21 , 0.15 , 42.0 ], #Acceptance 0.900545271261  #Rejection 0.60777385159
  5 : [ 0.31 , 0.19 , 37.0 ], #Acceptance 0.90047097936  #Rejection 0.63074204947
  7 : [ 0.11 , 0.49 , 41.0 ], #Acceptance 0.900027742049  #Rejection 0.762367491166
  10 : [ 0.09 , 0.11 , 37.0 ], #Acceptance 0.900240005053  #Rejection 0.872791519435
  15 : [ 0.07 , 0.13 , 38.0 ], #Acceptance 0.900945273632  #Rejection 0.93816254417
  20 : [ 0.11 , 0.07 , 43.0 ], #Acceptance 0.902390766694  #Rejection 0.952296819788
  30 : [ 0.05 , 0.33 , 38.0 ], #Acceptance 0.900196243342  #Rejection 0.962014134276
  40 : [ 0.05 , 0.33 , 35.0 ], #Acceptance 0.901028277635  #Rejection 0.966431095406
  }

dphi_dict['DPhib_MB1_MB2__DPhib_MB3_MB4'] = {                                                      
  3 : [ 0.09 , 0.31 , 32.0 ], #Acceptance 0.900384897361  #Rejection 0.540636042403
  5 : [ 0.09 , 0.21 , 32.0 ], #Acceptance 0.90164842776  #Rejection 0.560954063604
  7 : [ 0.07 , 0.13 , 35.0 ], #Acceptance 0.900582583037  #Rejection 0.679328621908
  10 : [ 0.05 , 0.15 , 38.0 ], #Acceptance 0.903682182783  #Rejection 0.781802120141
  15 : [ 0.05 , 0.13 , 32.0 ], #Acceptance 0.902039800995  #Rejection 0.827738515901
  20 : [ 0.05 , 0.15 , 29.0 ], #Acceptance 0.902720527617  #Rejection 0.828621908127
  30 : [ 0.05 , 0.11 , 32.0 ], #Acceptance 0.90243902439  #Rejection 0.832155477032
  40 : [ 0.05 , 0.09 , 32.0 ], #Acceptance 0.901028277635  #Rejection 0.837455830389
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
      print "\tPass! Pt", ptCut 
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
