import array
from ROOT import *
from cuts import *
import math
import array
from math import log10, floor
from logic import *
import numpy as np
import os

ptbin = [
    2.0,   2.5,   3.0,   3.5,   4.0,   4.5,   5.0,   6.0,   7.0,   8.0,  
    10.0,  12.0,  14.0,  16.0,  18.0,  20.0,  25.0,  30.0,  35.0,  40.0,  
    45.0,  50.0,  60.0,  70.0,  80.0,  90.0, 100.0, 120.0, 140.0, 200.0]
myptbin = np.asarray(ptbin)
nmyptbin = len(myptbin) - 1



etabin = [
    0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 
    1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9,
    2.0, 2.1, 2.2, 2.3, 2.4, 2.5]
myetabin = np.asarray(etabin)

#______________________________________________________________________________                                                                                                  
M_PI = 4*math.atan(1)


def get_eta_partition(eta):

  etaPartition = -1
  if   (abs(eta)>=1.2 and abs(eta)<1.4): etaPartition = 0
  elif (abs(eta)>=1.4 and abs(eta)<1.6): etaPartition = 1
  elif (abs(eta)>=1.6 and abs(eta)<1.8): etaPartition = 2
  elif (abs(eta)>=1.8 and abs(eta)<2.0): etaPartition = 3
  elif (abs(eta)>=2.0 and abs(eta)<2.2): etaPartition = 4
  elif (abs(eta)>=2.2 and abs(eta)<2.4): etaPartition = 5
  return etaPartition
 

def get_eta_partition_GE11(eta):

  etaPartition = -1
  if   (abs(eta)>=1.6 and abs(eta)<1.8): etaPartition = 0
  elif (abs(eta)>=1.8 and abs(eta)<2.0): etaPartition = 1
  elif (abs(eta)>=2.0 and abs(eta)<2.2): etaPartition = 2
  return etaPartition

def deltay12_deltay23(x1, y1, phi1,
                      x2, y2, phi2,
                      x3, y3, phi3):
  ## reference angle
  referenceAngle = phi2

  ## calculate the difference between the y' after the transformation
  ## this function needs more information August 16th 2016
  y1_prime = - x1 * sin(referenceAngle) + y1 * cos(referenceAngle) 
  y2_prime = - x2 * sin(referenceAngle) + y2 * cos(referenceAngle) 
  y3_prime = - x3 * sin(referenceAngle) + y3 * cos(referenceAngle) 
  
  deltay12 = y2_prime - y1_prime
  deltay23 = y3_prime - y2_prime
  return deltay12, deltay23


def get_parity(isEven1, isEven2, isEven3, isEven4):
  ## parity cases
  ## 0. odd even even
  ## 1. odd odd odd
  ## 2. even even even
  ## 3. even odd odd
  
  totalParity = -1
  if not isEven1 and     isEven2 and     isEven3: totalParity = 0
  if not isEven1 and not isEven2 and not isEven3: totalParity = 1
  if     isEven1 and     isEven2 and     isEven3: totalParity = 2
  if     isEven1 and not isEven2 and not isEven3: totalParity = 3
  return totalParity


def get_parity_ME11_ME21(isEven1, isEven2):
  ## parity cases
  ## 0. even even
  ## 1. even odd
  ## 2. odd even
  ## 3. even odd
  
  totalParity = -1
  if     isEven1 and     isEven2: totalParity = 0
  if     isEven1 and not isEven2: totalParity = 1
  if not isEven1 and     isEven2: totalParity = 2
  if not isEven1 and not isEven2: totalParity = 3
  return totalParity

#______________________________________________________________________________                                               


## dictionary with:
## 1. proportionality factor
## 2. slope
## 3. intercept
## numbers derived by Jose Dimas Valle
dict_prop_slope_intercept = {
  0 : {
    0 : [1.279, 0.04784, 0.1122],
    1 : [1.279, 0.65424, 0.09761],
    2 : [0.648, 0.05527, 0.08944],
    3 : [0.648, 0.08295, 0.1279],
    4 : [0.648, 0.1660, 0.2158],
    5 : [0.648, 0.4952, 0.7103],
    },
  1 : {
    0 : [0.6357, 0.0827, 0.2021],
    1 : [0.6357, 0.0906, 0.1773],
    2 : [0.3542, 0.1067, 0.1957],
    3 : [0.3542, 0.1561, 0.2645],
    4 : [0.3542, 0.3156, 0.4514],
    5 : [0.3542, 0.8242, 1.0712],
    },
  2 : {
    0 : [1.001, 0.038, 0.008345],
    1 : [1.001, 0.04157, 0.0617],
    2 : [0.5636, 0.0562, 0.08417],
    3 : [0.5636, 0.0870, 0.1426],
    4 : [0.5636, 0.1676, 0.2198],
    5 : [0.5636, 0.4953, 0.7272],
    },
  3 : {
    0 : [0.5252, 0.0739, 0.1714],
    1 : [0.5252, 0.07838, 0.1307],
    2 : [0.3217, 0.1066, 0.2026],
    3 : [0.3217, 0.1435, 0.2118],
    4 : [0.3217, 0.2874, 0.4055],
    5 : [0.3217, 0.7625, 1.075],
    }
  }


## dictionary with:
## 0. odd even even
## 1. odd odd odd
## 2. even even even
## 3. even odd odd
## numbers derived by Sven Dildick August 2016
## 1. proportionality factor
## 2. slope
## 3. intercept
dict_prop_slope_intercept_DIGIL1 = {
  0 : {
    0 : [1.1, 0.04784, 0.1122],
    1 : [1.1, 0.65424, 0.09761],
    2 : [0.64, 0.05527, 0.08944],
    3 : [0.64, 0.08295, 0.1279],
    4 : [0.6, 0.1660, 0.2158],
    5 : [0.6, 0.4952, 0.7103],
    },
  1 : {
    0 : [0.58, 0.0827, 0.2021],
    1 : [0.58, 0.0906, 0.1773],
    2 : [0.3542, 0.1067, 0.1957],
    3 : [0.3542, 0.1561, 0.2645],
    4 : [0.3542, 0.3156, 0.4514],
    5 : [0.3542, 0.8242, 1.0712],
    },
  2 : {
    0 : [1.001, 0.038, 0.008345],
    1 : [1.001, 0.04157, 0.0617],
    2 : [0.5636, 0.0562, 0.08417],
    3 : [0.5636, 0.0870, 0.1426],
    4 : [0.5636, 0.1676, 0.2198],
    5 : [0.5636, 0.4953, 0.7272],
    },
  3 : {
    0 : [0.5252, 0.0739, 0.1714],
    1 : [0.5252, 0.07838, 0.1307],
    2 : [0.3217, 0.1066, 0.2026],
    3 : [0.3217, 0.1435, 0.2118],
    4 : [0.3217, 0.2874, 0.4055],
    5 : [0.3217, 0.7625, 1.075],
  }
}


#______________________________________________________________________________                       
def get_proptionality_factor(etaPartition, parity):
  return dict_prop_slope_intercept_DIGIL1[parity][etaPartition][0]


#______________________________________________________________________________               
def get_proptionality_factor_withoutLCTFit(etaPartition, parity):
  return 1

#______________________________________________________________________________               
def get_proptionality_factor_withLCTFit(etaPartition, parity):
  return 1

#______________________________________________________________________________               
def pt_from_position(x1, y1, z1, phi1, isEven1,
                     x2, y2, z2, phi2, isEven2,
                     x3, y3, z3, phi3, isEven3,
                     x4, y4, z4, phi4, isEven4,
                     eta):

  etaPartition = get_eta_partition(eta)
  totalParity = get_parity(isEven1, isEven2, isEven3, isEven4)
  deltay12, deltay23 = deltay12_deltay23(x1, y1, phi1,
                                         x2, y2, phi2,
                                         x3, y3, phi3)
  ## debug
  debug = False
  if debug:
    print "etaPartition", etaPartition
    print "totalParity", totalParity
    print "deltay12", deltay12, "deltay23", deltay23
  

  if totalParity < 0 or totalParity > 3 or etaPartition == -1: return -99
  
  preResult1 = 1./abs(deltay23 - dict_prop_slope_intercept[totalParity][etaPartition][0] * deltay12)
  preResult2 = dict_prop_slope_intercept[totalParity][etaPartition][1]
  preResult3 = dict_prop_slope_intercept[totalParity][etaPartition][2]
  
  result = (preResult1 + preResult2) / preResult3
  return result


#______________________________________________________________________________                                                                                                  
def poly_library(st1, st2, pol):
  if pol == 'pol1':
    if st1==1 and st2==2: return [5.746, 1.787, 0, 0]
    if st1==1 and st2==3: return [-2.232, 1.316, 0, 0]
    if st1==1 and st2==4: return [2.902, 1.06, 0, 0]
    if st1==2 and st2==3: return [5.673, 1.509, 0, 0]
    if st1==2 and st2==4: return [-1.954, 1.387, 0, 0]
    if st1==3 and st2==4: return [9.49, 1.701, 0, 0]

  if pol == 'pol2':
    if st1==1 and st2==2: return [-5.242, 3.51, -0.05, 0]
    if st1==1 and st2==3: return [-4.949, 1.803, -0.01521, 0]
    if st1==1 and st2==4: return [-3.815, 1.25, -0.0059, 0]
    if st1==2 and st2==3: return [-5.676, 3.146, -0.04168, 0]
    if st1==2 and st2==4: return [-6.098, 2.019, -0.01753, 0]
    if st1==3 and st2==4: return [-5.73,  4.098, -0.06534, 0]

  if pol == 'pol3':
    if st1==1 and st2==2: return [-9.07, 4.337, -0.09737, 0.0007264]
    if st1==1 and st2==3: return [-3.847, 1.544, 0.0003261, -0.0002424]
    if st1==1 and st2==4: return [2.217, 0.8523, 0.01741, -0.0003688]
    if st1==2 and st2==3: return [-8.221, 3.66, -0.06812, 0.0003513]
    if st1==2 and st2==4: return [-7.146, 2.234, -0.02903, 0.0001623]
    if st1==3 and st2==4: return [-12.02, 4.979, -0.1118, 0.0006741]


#______________________________________________________________________________                                                                                                  
def poly_resolution_library(st1, st2, pol):
  if pol == 'pol1':
    if st1==1 and st2==2: return [ 0.232997504786 ,  0.017828278707 ,  0 ,  0 ]
    if st1==1 and st2==3: return [ 0.104940544565 ,  0.0106112367459 ,  0 ,  0 ]
    if st1==1 and st2==4: return [ 0.0925582264163 ,  0.00956934260453 ,  0 ,  0 ]
    if st1==2 and st2==3: return [ 0.216945979301 ,  0.016118034413 ,  0 ,  0 ]
    if st1==2 and st2==4: return [ 0.163140326149 ,  0.0135758108182 ,  0 ,  0 ]
    if st1==3 and st2==4: return [ 0.330823642594 ,  0.0231212343975 ,  0 ,  0 ]

  if pol == 'pol2':
    if st1==1 and st2==2: return [ 0.425399442245 ,  0.0586066270926 ,  0.00163445427321 ,  0 ]
    if st1==1 and st2==3: return [ 0.192621978027 ,  0.0308062180816 ,  0.000904397271426 ,  0 ]
    if st1==1 and st2==4: return [ 0.178716461728 ,  0.0277746891351 ,  0.000852731696197 ,  0 ]
    if st1==2 and st2==3: return [ 0.366360930694 ,  0.0455322268289 ,  0.00108424619265 ,  0 ]
    if st1==2 and st2==4: return [ 0.296314120328 ,  0.0400845995546 ,  0.00104606620245 ,  0 ]
    if st1==3 and st2==4: return [ 0.610542572048 ,  0.0758914148344 ,  0.00197003210269 ,  0 ]

  if pol == 'pol3':
    if st1==1 and st2==2: return [ 0.761866989134 ,  0.148505001684 ,  0.00791521266201 ,  0.000119935087897 ]
    if st1==1 and st2==3: return [ 0.349128668505 ,  0.0750168990651 ,  0.00420312018117 ,  6.40341791597e-05 ]
    if st1==1 and st2==4: return [ 0.329886125573 ,  0.0688219584793 ,  0.00399634981601 ,  6.39899740996e-05 ]
    if st1==2 and st2==3: return [ 0.695634434177 ,  0.127903932904 ,  0.00623745201508 ,  8.16246655536e-05 ]
    if st1==2 and st2==4: return [ 0.553850340289 ,  0.103963455628 ,  0.00524106684519 ,  7.24391536905e-05 ]
    if st1==3 and st2==4: return [ 1.10865695068 ,  0.196820380084 ,  0.00978414190039 ,  0.000138975821929 ]
    

#______________________________________________________________________________                                                                                                  
def getPtFromDphi(st1, st2, dphi1, dphi2, pol):
  if dphi1 != 99 and dphi2 != 99 and dphi1 != dphi2:
    values = poly_library(st1, st2, pol)
    abs_deltaPhi_inv = 1./abs(deltaPhi(dphi1, dphi2))
    values_corr = [values[3], values[2], values[1], values[0] - abs_deltaPhi_inv]
    
    roots = np.roots(values_corr)
    #print roots
    #p0_term = values[0]
    #p1_term = abs_deltaPhi_inv*values[1]
    #p2_term = abs_deltaPhi_inv*abs_deltaPhi_inv*values[2]
    #p3_term = abs_deltaPhi_inv*abs_deltaPhi_inv*abs_deltaPhi_inv*values[3]
    return 0#p0_term + p1_term + p2_term + p3_term
  else: 
    return 0
 

#______________________________________________________________________________                                                                                                  
def getPtErrorFromDphi(st1, st2, dphi1, dphi2, pol):
  if dphi1 != 99 and dphi2 != 99 and dphi1 != dphi2:
    values = poly_library(st1, st2, pol)
    abs_deltaPhi_inv = 1./abs(deltaPhi(dphi1, dphi2))

    p0_term = values[0]
    p1_term = abs_deltaPhi_inv*values[1]
    p2_term = abs_deltaPhi_inv*abs_deltaPhi_inv*values[2]
    p3_term = abs_deltaPhi_inv*abs_deltaPhi_inv*abs_deltaPhi_inv*values[3]
    return p0_term + p1_term + p2_term + p3_term
  else: 
    return 0


#______________________________________________________________________________                                                                                                  
def L1Mu_status(st1, st2, st3, st4):
  def ok(st):
    return st != 99
  def nok(st):
    return st==99

  ## should not happen!
  if nok(st1) and nok(st2) and nok(st3) and nok(st4): status = 0

  if ok(st1) and nok(st2) and nok(st3) and nok(st4):  status = 1
  if nok(st1) and ok(st2) and nok(st3) and nok(st4):  status = 2
  if nok(st1) and nok(st2) and ok(st3) and nok(st4):  status = 3
  if nok(st1) and nok(st2) and nok(st3) and ok(st4):  status = 4

  ## low quality
  if ok(st1) and ok(st2) and nok(st3) and nok(st4):  status = 5
  if ok(st1) and nok(st2) and ok(st3) and nok(st4):  status = 6
  if ok(st1) and nok(st2) and nok(st3) and ok(st4):  status = 7
  if nok(st1) and ok(st2) and ok(st3) and nok(st4):  status = 8
  if nok(st1) and ok(st2) and nok(st3) and ok(st4):  status = 9
  if nok(st1) and nok(st2) and ok(st3) and ok(st4):  status = 10

  ## high quality
  if nok(st1) and ok(st2) and ok(st3) and ok(st4):  status = 11
  if ok(st1) and nok(st2) and ok(st3) and ok(st4):  status = 12
  if ok(st1) and ok(st2) and nok(st3) and ok(st4):  status = 13
  if ok(st1) and ok(st2) and ok(st3) and nok(st4):  status = 14

  ## highest quality
  if ok(st1) and ok(st2) and ok(st3) and ok(st4):  status = 15

  return status

#______________________________________________________________________________                                                                                                  
def addfiles(ch, dirname=".", ext=".root"):
  theInputFiles = []
  if not os.path.isdir(dirname):
    print "ERROR: This is not a valid directory: ", dirname
    exit()
  ls = os.listdir(dirname)
  theInputFiles.extend([dirname[:] + x for x in ls if x.endswith(ext)])
  for pfile in theInputFiles:
    print pfile
    ch.Add(pfile)

  return ch


#______________________________________________________________________________                                                                                                  
def deltaPhi(phi1, phi2):
  result = phi1 - phi2;
  while (result > 2*M_PI): 
    result -= 4*M_PI;
  while (result <= -2*M_PI):
    result += 4*M_PI;
  return result;


#______________________________________________________________________________                                                                                                  
def deltaPhi2(phi1, phi2):
  result = phi1 - phi2;
  while (result > M_PI): 
    result -= 2*M_PI;
  while (result <= -M_PI):
    result += 2*M_PI;
  return result;

#______________________________________________________________________________                       
def normalizedPhi(phi1):
  result = phi1;
  while (result > 2*M_PI): 
    result -= 4*M_PI;
  while (result <= -2*M_PI):
    result += 4*M_PI;
  return result;

#______________________________________________________________________________                       
def normalizedPhi2(phi1):
  result = phi1;
  while (result > M_PI): 
    result -= 2*M_PI;
  while (result <= -M_PI):
    result += 2*M_PI;
  return result;

#______________________________________________________________________________                                                                                                  
def getQuantilesX(hist2d):
  probs = array.array('d', [0.025, 0.16, 0.5, 1 - 0.16, 0.975] )
  q = array.array('d', [0.0]*len(probs))
  hist1d = hist2d.QuantilesX(len(probs), q, probs)
  SetOwnership( hist1d, True )
  return hist1d


#______________________________________________________________________________                                                                                                  
def getMedian(yintegral):
  if (yintegral%2 == 1):
    return (yintegral-1)/2 + 1
  else:
    return (yintegral/2) + 0.5
  

#______________________________________________________________________________                                                                                                  
def get1DHistogramMedianY(hist2d):
    '''this function returns a 1d histogram
    for a 2d histgram using the median and the x-sigma resolution on the median'''

    xBins = hist2d.GetXaxis().GetNbins()
    yBins = hist2d.GetYaxis().GetNbins()
    xmin = hist2d.GetXaxis().GetXmin()
    xmax = hist2d.GetXaxis().GetXmax()
    ymin = hist2d.GetYaxis().GetXmin()
    ymax = hist2d.GetYaxis().GetXmax()
 
    xs = []
    ys = []
    xs_e_up = []
    xs_e_dw = []
    ys_e_up = []
    ys_e_dw = []

    r1 = TH1F("r1","",xBins,xmin,xmax)
    for x in range(1,xBins+1):
      #print "bin:", x
      probSum = array.array('d', [.32, .5, .68])
      q = array.array('d', [0.0]*len(probSum))
      entries = hist2d.Integral(x,x,0,yBins+1)
      ## do not compute quantiles for empty histograms!!!
      if entries == 0:
        continue
      tempHist = hist2d.ProjectionY("bin1",x,x)
      tempHist.GetQuantiles(len(probSum), q, probSum)
      #print "q", q

      xval = hist2d.GetBinCenter(x)
      xval_e_up = hist2d.GetBinWidth(x)/2.
      xval_e_dw = hist2d.GetBinWidth(x)/2.
      yval = q[1]
      yval_e_up = q[2] - yval
      yval_e_dw = yval - q[0]

      r1.SetBinContent(x, yval)
      error = (q[2]- q[0])/(2*sqrt(entries))
      r1.SetBinError(x, error)

      """
      xs.append(xval) 
      xs_e_up.append(xval_e_up)
      xs_e_dw.append(xval_e_dw)
      ys.append(yval)
      ys_e_up.append(yval_e_up)
      ys_e_dw.append(yval_e_dw)
      """

    """
    print "xval", xs
    print
    print "yval", ys
    print
    print "yval_e_up", ys_e_up
    print
    print "yval_e_dw", ys_e_dw
    """
    SetOwnership( r1, False )
    return r1
    """
    tgraph = TGraphAsymmErrors(len(xs), 
                               array.array("f",xs), 
                               array.array("f",ys), 
                               array.array("f",xs_e_dw), 
                               array.array("f",xs_e_up), 
                               array.array("f",ys_e_dw), 
                               array.array("f",ys_e_up))
    SetOwnership( tgraph, False )
    return tgraph
    """

#_______________________________________________________________________________
def applyTdrStyle():
    cmsText     = "CMS Phase II Simulation"
    cmsTextFont   = 61  ## default is helvetic-bold

    lumiTextSize     = 0.6
    lumiTextOffset   = 0.2
    cmsTextSize      = 0.75
    cmsTextOffset    = 0.1  ## only used in outOfFrame version
    
    relPosX    = 0.045
    relPosY    = 0.035
    relExtraDY = 1.2
    
    ## ratio of "CMS" and extra text size
    extraOverCmsTextSize  = 0.76

    lumi_14TeV = "PU = 0"

    """
    H = pad.GetWh();
    W = pad.GetWw();
    l = pad.GetLeftMargin();
    b = pad.GetBottomMargin();
    e = 0.025;
    """
    t = gPad.GetTopMargin();
    r = gPad.GetRightMargin();


    latex = TLatex()
    latex.SetNDC();
    latex.SetTextAngle(0);
    latex.SetTextColor(kBlack);    
    
    extraTextSize = extraOverCmsTextSize*cmsTextSize;
    """
    latex.SetTextFont(cmsTextFont);
    latex.SetTextSize(cmsTextSize*t);
    latex.SetTextFont(42);
    latex.SetTextAlign(31); 
    latex.SetTextSize(lumiTextSize*t);    
    latex.DrawLatex(1-r,1-t+lumiTextOffset*t,lumiText);    
    """

    """
    alignY_=3;
    alignX_=2;    
    align_ = 10*alignX_ + alignY_;
    latex.SetTextAlign(align_);
    posX_ = 1-r - relPosX*(1-l-r)
    posY_ = 1-t - relPosY*(1-t-b)
    """
    latex.DrawLatex(0.52, 0.87, cmsText);
    return latex


#______________________________________________________________________________
def addfiles(ch, dirname=".", ext=".root"):
  theInputFiles = []
  if not os.path.isdir(dirname):
    print "ERROR: This is not a valid directory: ", dirname
    exit()
  ls = os.listdir(dirname)
  theInputFiles.extend([dirname[:] + x for x in ls if x.endswith(ext)])
  for pfile in theInputFiles:
    ch.Add(pfile)  

  return ch

#______________________________________________________________________________
def firstSecondBin(h):
    h.SetBinContent(1,h.GetBinContent(0) + h.GetBinContent(1))
    h.SetBinContent(0,0)
    return h
#______________________________________________________________________________
def getBackwardCumulative(h):
    htemp = TH1F("htemp"," ",len(myptbin)-1, myptbin)
    ## keep the underflow
    htemp.SetBinContent(0,h.GetBinContent(0))
    for i in range(1,len(myptbin)+1):        
        sum = 0
        for j in range(i,len(myptbin)+1):
            sum += h.GetBinContent(j)
        htemp.SetBinContent(i, sum)
    htemp.Sumw2()
    SetOwnership(htemp, False)
    return htemp

#______________________________________________________________________________
def getRatecount(tree, todraw, cut):
    htemp = TH1F("htemp"," ",len(myptbin)-1, myptbin)
    tree.Draw(todraw+">>htemp",cut)
    return htemp.GetEntries()

#___________________________________________________
def getTotalEventNumber(tree):
    eventList = []
    for k in range(0,tree.GetEntries()):
        tree.GetEntry(k)
        eventList.append(tree.event)
    return len(set(eventList))

#______________________________________________________________________________
def scaleToRate(tree, h):
    ntotalEvents = tree.GetEntries()
    averageRate = 30000. #[kHz]
    bunchCrossingWindow = 1.
    h.Scale(averageRate/bunchCrossingWindow/ntotalEvents)
    return h

#______________________________________________________________________________
def getRatePtHistogram(tree, h):
    h = getBackwardCumulative(h)
    h = scaleToRate(tree, h)
    return h
        
#______________________________________________________________________________
def getRateEtaHistogram(tree, h):
    h = scaleToRate(tree, h)
    return h

#______________________________________________________________________________
def getRate(treecut):
   
    #f = ROOT.TFile(file)
    #t = f.Get(dir)
    h = TH1F("h"," ",len(myptbin)-1, myptbin)
    n=1
    for x in ptbin:
       #print "cut ",cut+" && pt>=%f"%x
       content = getRatecount(tree,"pt",cut+"&& pt>=%f"%x)
       #content = tree.GetEntries(cut+"&& pt>=%f"%x)
       print "bin n ",n,"pt ",x ,"  content ",content
       h.SetBinContent(n, content)
       n= n+1
    h.Sumw2()
    #print "before scale "
    #h.Print("all")
    ntotalEvents = getTotalEventNumber(tree)
    averageRate = 30000. #[kHz]
    bunchCrossingWindow = 1.
#    h.Scale(40000./ntotalEvents/3.*0.795)
    h.Scale(averageRate/bunchCrossingWindow/ntotalEvents)
    SetOwnership(h, False)
    return h

#______________________________________________________________________________
def set_style():
   gStyle.SetStatStyle(0)
   gStyle.SetOptStat(11111111)
   gStyle.SetTitleBorderSize(0);
   gStyle.SetPadLeftMargin(0.126);
   gStyle.SetPadRightMargin(0.04);
   gStyle.SetPadTopMargin(0.06);
   gStyle.SetPadBottomMargin(0.13);
   
#______________________________________________________________________________
def draw_1D(p, to_draw, c_title, title, h_bins, cut="", opt = ""):
   gStyle.SetStatStyle(0)
   gStyle.SetOptStat(11111111)

   c = TCanvas("c","c",800,600)
   c.Clear()
   gStyle.SetTitleBorderSize(0);
   gStyle.SetPadLeftMargin(0.126);
   gStyle.SetPadRightMargin(0.04);
   gStyle.SetPadTopMargin(0.06);
   gStyle.SetPadBottomMargin(0.13);
   p.Draw(to_draw + ">>" + "h_name" + h_bins, cut)
   h = TH1F(gDirectory.Get("h_name").Clone("h_name"))
   if not h:
      sys.exit('h does not exist')
   h.SetTitle(title)
   h.SetLineWidth(2)
   h.SetLineColor(kBlue)
   h.GetXaxis().SetLabelSize(0.05)
   h.GetYaxis().SetLabelSize(0.05)
   h.GetXaxis().SetTitleSize(0.06)
   h.GetYaxis().SetTitleSize(0.06)
   header = "                                                         PU = 140, 14 TeV"
#   h.SetTitle(header)
   h.Draw()
   h.SetMinimum(0.)
   h.SetMaximum(h.GetMaximum()*1.2)
   c.SaveAs("" + c_title + ".png")
      

#______________________________________________________________________________
def draw_1D_root(p, to_draw, c_title, title, h_bins, cut="", opt = ""):
   p.Draw(to_draw + ">>" + "h_name" + h_bins, cut)
   h = TH1F(gDirectory.Get("h_name").Clone("h_name"))
   if not h:
      sys.exit('h does not exist')
   h.SetTitle(title)
   h.SetLineWidth(2)
   h.SetLineColor(kBlue)
   h.GetXaxis().SetLabelSize(0.05)
   h.GetYaxis().SetLabelSize(0.05)
   h.GetXaxis().SetTitleSize(0.06)
   h.GetYaxis().SetTitleSize(0.06)
   h.Draw()
   h.SetMinimum(0.)
   h.SetMaximum(h.GetMaximum()*1.2)
   h.SaveAs("" + c_title + ".root")


#_______________________________________________________________________________
def draw_2D(p, to_draw, c_title, title, h_bins, cut="", opt = ""):
  gStyle.SetStatStyle(0)
  gStyle.SetOptStat(1110)
  c = TCanvas("c","c",800,600)
  c.Clear()
  gStyle.SetPadLeftMargin(0.126);
  gStyle.SetPadRightMargin(0.04);
  gStyle.SetPadTopMargin(0.06);
  gStyle.SetPadBottomMargin(0.13);
  p.Draw(to_draw + ">>h_" + h_bins, cut)
  h = TH2F(gDirectory.Get("h_"))
  if not h:
    sys.exit('h does not exist')
  h = TH2F(h.Clone("h_"))
  h.SetTitle(title)
  h.SetLineWidth(2)
  h.SetLineColor(kBlue)
  h.Draw(opt) 
  c.SaveAs("" + c_title + ".png")


#_______________________________________________________________________________
def applyTdrStyle():
    cmsText     = "CMS PhaseII Simulation"
    cmsTextFont   = 61  ## default is helvetic-bold

    lumiTextSize     = 0.6
    lumiTextOffset   = 0.2
    cmsTextSize      = 0.75
    cmsTextOffset    = 0.1  ## only used in outOfFrame version
    
    relPosX    = 0.045
    relPosY    = 0.035
    relExtraDY = 1.2
    
    ## ratio of "CMS" and extra text size
    extraOverCmsTextSize  = 0.76

    lumi_14TeV = "PU = 140"

    """
    H = pad.GetWh();
    W = pad.GetWw();
    l = pad.GetLeftMargin();
    b = pad.GetBottomMargin();
    e = 0.025;
    """
    t = gPad.GetTopMargin();
    r = gPad.GetRightMargin();
    latex = TLatex()
    latex.SetNDC();
    latex.SetTextAngle(0);
    latex.SetTextColor(kBlack);    
    
    extraTextSize = extraOverCmsTextSize*cmsTextSize;
    """
    latex.SetTextFont(cmsTextFont);
    latex.SetTextSize(cmsTextSize*t);
    latex.SetTextFont(42);
    latex.SetTextAlign(31); 
    latex.SetTextSize(lumiTextSize*t);    
    latex.DrawLatex(1-r,1-t+lumiTextOffset*t,lumiText);    
    """

    """
    alignY_=3;
    alignX_=2;    
    align_ = 10*alignX_ + alignY_;
    latex.SetTextAlign(align_);
    posX_ = 1-r - relPosX*(1-l-r)
    posY_ = 1-t - relPosY*(1-t-b)
    """
    latex.DrawLatex(0.52, 0.87, cmsText);
    return latex


#_______________________________________________________________________________
def getEffObject(p, variable, binning, denom_cut, extra_num_cut):

    denom = get_1D(p, "denom", "denom", binning, variable, denom_cut)
    num = get_1D(p, "num", "num", binning, variable, AND(denom_cut, extra_num_cut))
    print "denom", denom.GetEntries()
    print "num", num.GetEntries()
    h = TEfficiency(num, denom)
#    h = clearEmptyBinsEff(h)
    SetOwnership(h, False)
    return h

#_______________________________________________________________________________
def makeEtaEffPlot(h, plotTitle, legTitle):
    c = TCanvas("c","c",800,600)
    c.Clear()
    gStyle.SetTitleStyle(0);
    gStyle.SetTitleAlign(13); ##coord in top left
    gStyle.SetTitleX(0.);
    gStyle.SetTitleY(1.);
    gStyle.SetTitleW(1);
    gStyle.SetTitleH(0.058);
    #gStyle.SetTitleXOffset(0.05)
    gStyle.SetTitleBorderSize(0);
    gStyle.SetPadLeftMargin(0.126);
    gStyle.SetPadRightMargin(0.04);
    gStyle.SetPadTopMargin(0.06);
    gStyle.SetPadBottomMargin(0.13);
    gStyle.SetOptStat(0);
    gStyle.SetMarkerStyle(1);
    gPad.SetTickx(1)
    gPad.SetTicky(1)
    #gStyle.SetStatStyle(0)
    base = TH1D("base","base", 25, 0, 2.5)
    base.SetStats(0)
    base.SetTitle("                                                                      14 TeV,  PU = 140; #eta; Efficiency")
    base.SetMinimum(0)
    base.SetMaximum(1.1)
    base.GetXaxis().SetLabelSize(0.05)
    base.GetYaxis().SetLabelSize(0.05)
    base.GetXaxis().SetTitleSize(0.06)
    base.GetYaxis().SetTitleSize(0.06)
    #base.GetXaxis().SetLimits(0,maxbin)
    base.Draw()
    h.SetMarkerColor(kBlue)
    h.SetLineColor(kBlue)
    h.SetLineWidth(2)
    h.SetMarkerStyle(1)
    h.SetMarkerSize(15)
    h.Draw("same")
    leg = TLegend(0.1,0.3,0.75,0.45,"","brNDC")
    leg.SetFillColor(kWhite)
    leg.SetBorderSize(0)
    leg.SetFillStyle(0)
    leg.SetTextSize(0.04)
    leg.AddEntry(h,legTitle,"l")
    leg.Draw("same")
    #tex = drawLabel(p.ctau + ", " + p.mass,0.45,0.55,0.05)
    #tex4 = drawLabel(p.mass,0.55,0.47,0.05)
    #tex3 = drawLabel("H #rightarrow 2n_{1} #rightarrow 2n_{D}2Z_{D} #rightarrow 2n_{D}4#mu",0.45,0.65,0.05)
    tex2 = applyTdrStyle()
    c.SaveAs(plotTitle + ".png")


#_______________________________________________________________________________
def makeSimplePlot(targetDir, h, plotTitle, setLogx=False):
    c = TCanvas("c","c",800,600)
    c.Clear()
    gStyle.SetTitleStyle(0);
    gStyle.SetTitleAlign(13); ##coord in top left
    gStyle.SetTitleX(0.);
    gStyle.SetTitleY(0.);
    gStyle.SetTitleW(1);
    gStyle.SetTitleH(0.058);
    #gStyle.SetTitleXOffset(0.05)
    gStyle.SetTitleBorderSize(0);
    gStyle.SetPadLeftMargin(0.126);
    gStyle.SetPadRightMargin(0.04);
    gStyle.SetPadTopMargin(0.06);
    gStyle.SetPadBottomMargin(0.13);
    gStyle.SetOptStat(0);
    gStyle.SetMarkerStyle(1);
    gPad.SetTickx(1)
    gPad.SetTicky(1)
    if setLogx:
        gPad.SetLogx()
    #gStyle.SetStatStyle(0)
    gStyle.SetOptStat(11111111)
    h.SetStats(1)
    h.GetXaxis().SetLabelSize(0.05)
    h.GetYaxis().SetLabelSize(0.05)
    h.GetXaxis().SetTitleSize(0.06)
    h.GetYaxis().SetTitleSize(0.06)
    #h.GetXaxis().SetLimits(0,maxbin)
    h.Draw()
    h.SetMarkerColor(kBlue)
    h.SetLineColor(kBlue)
    h.SetLineWidth(2)
    h.SetMarkerStyle(1)
    h.SetMarkerSize(15)
    #tex = drawLabel(p.ctau + ", " + p.mass,0.45,0.55,0.05)
    #tex4 = drawLabel(p.mass,0.55,0.47,0.05)
    #tex3 = drawLabel("H #rightarrow 2n_{1} #rightarrow 2n_{D}2Z_{D} #rightarrow 2n_{D}4#mu",0.45,0.65,0.05)
    tex2 = applyTdrStyle()
    c.SaveAs(targetDir + plotTitle + ".png")


#_______________________________________________________________________________
def get_1D(p, title, h_name, h_bins, to_draw, cut, opt = "", color = kBlue):
    gStyle.SetStatStyle(0)
    gStyle.SetOptStat(11111111)
    #nbins = len(xbins)
    #h = TH1F("h_name", "h_name", nbins, xbins);
    p.Draw(to_draw + ">>" + h_name + h_bins, cut)
    h = TH1F(gDirectory.Get(h_name).Clone(h_name))
    if not h:
        sys.exit('%s does not exist'%(to_draw))
    h.SetTitle(title)
    h.SetLineWidth(2)
    h.SetLineColor(color)    
    h.SetMinimum(0.)
    SetOwnership(h, False)
    return h

#_______________________________________________________________________________
def to_array(x, fmt="d"):
    return array.array(fmt, x)
