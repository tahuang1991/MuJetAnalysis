
from ROOT import *
import math
import array
#from math import log10, floor

pt_slope_inter = {
    1.6 : [3.759, 6.235], 
    1.8 : [6.785, 11.14],
    2.0 : [9.113, 10.36], 
    2.2 : [10.12, 8.317], 
}

pt_pos_slope_inter = {
    1.6 : [3.786, 6.165], 
    1.8 : [6.754, 10.67],
    2.0 : [9.026, 9.432], 
    2.2 : [10.09, 7.715], 
}

pt_pos_slope_inter_14 = {
    1.6 : [1.532, 2.187], 
    1.8 : [2.193, 3.799],
    2.0 : [2.974, 4.301], 
    2.2 : [3.916, 2.989], 
}


pt_slope_inter_14 = {
    1.6 : [1.523, 2.127], 
    1.8 : [2.182, 3.754],
    2.0 : [2.558, 2.52], 
    2.2 : [3.893, 2.933], 
}


def csc_second_gp_eta(eta_min, eta_max, var = 12):

    if (var == 12):
        return TCut("%f < abs(csc_gp_second_st2) && abs(csc_gp_second_st2)< %f"%(eta_min, eta_max))
    if (var == 13):
        return TCut("%f < abs(csc_gp_second_st3) && abs(csc_gp_second_st3)< %f"%(eta_min, eta_max))
    if (var == 14):
        return TCut("%f < abs(csc_gp_second_st4) && abs(csc_gp_second_st4)< %f"%(eta_min, eta_max))

def has_csc():
    return TCut("nlayerscsc>=4")

def has_csc_second(var=12):

    if (var==12):
        return TCut("nlayers_st2>=4")
    if (var==13):
        return TCut("nlayers_st3>=4")
    if (var==14):
        return TCut("nlayers_st4>=4")

def has_csc_hits(var):
    return TCut("has_csc_%d>0"%var)


def dxy(dxy_min, dxy_max):
    return TCut("%f <= abs(dxy_csc) && abs(dxy_csc)<%f"%(dxy_min, dxy_max))


def eta_sh_st1(eta_min, eta_max):
    return TCut("%f < abs(csc_gp_eta) && abs(csc_gp_eta)< %f"%(eta_min, eta_max))
    
def same_direction_cut():
    return TCut("Lxy_csc >0 && pzvz_csc>0")
    

def pt_cut(eta_min, sim_pt, var):

    slope = 0.0
    inter = 0.0
    
    if var ==12:
        slope = pt_slope_inter[eta_min][0]
        inter = pt_slope_inter[eta_min][1]
    if var ==14:
        slope = pt_slope_inter_14[eta_min][0]
        inter = pt_slope_inter_14[eta_min][1]
    
    return TCut("( (1/abs(csc_bending_angle_%d) + %f) / %f ) > %f"%(var, inter, slope, sim_pt))


def pt_from_povercosh(eta_min, sim_pt, var):
    slope = 0.0
    inter = 0.0
    
    if var ==12:
        slope = pt_pos_slope_inter[eta_min][0]
        inter = pt_pos_slope_inter[eta_min][1]
    if var ==14:
        slope = pt_pos_slope_inter_14[eta_min][0]
        inter = pt_pos_slope_inter_14[eta_min][1]

    return TCut("((1/abs(csc_bending_angle_%d) + %f) / %f ) > %f"%(var, inter, slope, sim_pt))



#_____________________________________________________________

def FitHistoFunction68(b1, xBins, xminBin, xmaxBin, yminBin, ymaxBin, printa): 
    
    r1 = TH1F("r1","1/abs(\Delta\phi) vs p^{Sim}",xBins,xminBin,xmaxBin)
    for x in range(xminBin,xmaxBin):

        if (printa > 0):
            print "*********** For bin x: %d **********************"%x
            

        # Find the total number of frequencies
        totalfreq = b1.Integral(x,x,0,ymaxBin+1)

        # Calculate half of the frequencies
        med = 0
        
        if (totalfreq%2 ==1) :
            med = (totalfreq-1)/2 + 1            # Set the value of the median

        if (totalfreq%2 ==0):
            med = (totalfreq/2) + 0.5               # This might need to be added 0.5

        temporal = 0
        midbin = 0
        
        for m in range (0,ymaxBin+1):
                temporal = b1.Integral(x,x,0,m)

                if (temporal >= med):
                    midbin = m              # Break once I get to the median
                    break

       
        if (printa > 0):

                print "suma: ",totalfreq
                print "Midbin: ",midbin
                print "mediana count: ",temporal


        
        # midbin is the actual value to be stored in (x, midbin) histogram.    
        # Find the error above the median
        
        sumerrup = 0                        # Sum of events up
        binerrup = 0                        # Bin which has the 34% of events
        
        for k in range (midbin, ymaxBin+1): # Looping over the midbin up to 10000 
            sumerrup = b1.Integral(x,x,midbin,k)
  
            if (sumerrup >= 0.33*totalfreq):     # If the summ is bigger or equal to 34% of the total number of entries, break
                binerrup = k
                break
        
        sumerrlow = 0
        binerrlow = 0

        
        for r in range (0, midbin):
            sumerrlow = b1.Integral(x,x,midbin,midbin-r)

            if (sumerrlow >= 0.33*totalfreq):
                binerrlow = midbin-r        # Store the bin which has the 34% value 
                break
        
        # error is the difference averaged on the bin low and bin up
 
        errorbin = abs(binerrup - binerrlow)/2
        if (totalfreq > 0):
            errorbin = errorbin / sqrt (totalfreq)
        
        if (printa > 0):
            print " X position: ",x
            print " Bin y: ",midbin
            print " Error: ",errorbin
            print " Error low: ",binerrlow
            print " Sum err low: ",sumerrlow
            print " Error high: ",binerrup
            print " Sum err high: ",sumerrup

        # Store in a histogram the values of (x, midbin) with an error given by errorbin

        r1.SetBinContent(x, midbin)
        r1.SetBinError(x, errorbin)

    return r1                               #Return the histogram 1D 
                             #Return the histogram 1D 


#_______________________________________________________________________________
def get_1D(p, title, h_name, h_bins, to_draw, cut, opt = "", color = kBlue):
    gStyle.SetStatStyle(0)
    gStyle.SetOptStat(11111111)
    #nbins = len(xbins)
    #h = TH1F("h_name", "h_name", nbins, xbins);
    p.tree.Draw(to_draw + ">>" + h_name + h_bins, cut)
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
def AND(*arg):
    """AND of any number of TCuts in PyROOT"""
    length = len(arg)
    if length == 0:
        print "ERROR: invalid number of arguments"
        return
    if length == 1:
        return arg[0] 
    if length==2:
        return ANDtwo(arg[0],arg[1])
    if length>2:
        result = arg[0]
        for i in range(1,len(arg)):
            result = ANDtwo(result,arg[i])
        return result

#_______________________________________________________________________________
def OR(*arg):
    """OR of any number of TCuts in PyROOT"""
    length = len(arg)
    if length == 0:
        print "ERROR: invalid number of arguments"
        return
    if length == 1:
        return arg[0] 
    if length==2:
        return ORtwo(arg[0],arg[1])
    if length>2:
        result = arg[0]
        for i in range(1,len(arg)):
            result = ORtwo(result,arg[i])
        return result

#_______________________________________________________________________________
def ANDtwo(cut1,cut2):
    """AND of two TCuts in PyROOT"""
    if cut1.GetTitle() == "":
        return cut2
    if cut2.GetTitle() == "":
        return cut1
    return TCut("(%s) && (%s)"%(cut1.GetTitle(),cut2.GetTitle()))


#_______________________________________________________________________________
def ORtwo(cut1,cut2):
    """OR of two TCuts in PyROOT"""
    if cut1.GetTitle() == "":
        return cut2
    if cut2.GetTitle() == "":
        return cut1
    return TCut("(%s) || (%s)"%(cut1.GetTitle(),cut2.GetTitle()))
