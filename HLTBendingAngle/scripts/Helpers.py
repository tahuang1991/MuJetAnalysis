from ROOT import *
import math
import array
#from math import log10, floor

pt_slope_inter = {
    1.6 : [3.575, 5.873], 
    1.8 : [4.804, 5.337],
    2.0 : [5.035, 2.587], 
    2.2 : [4.322, -5.725], 
}

pt_pos_slope_inter = {
    1.6 : [3.623, 5.965], 
    1.8 : [4.948, 5.476],
    2.0 : [5.079, 2.854], 
    2.2 : [4.332, -5.632], 
}



def has_csc():
    return TCut("nlayerscsc>=4")

def has_csc_second():
    return TCut("csc_second_nlayers>=4")


def has_csc12():
    return TCut("has_csc_12>0")

def has_csc13():
    return TCut("has_csc_13>0")

def has_csc14():
    return TCut("has_csc_14>0")

def dxy(dxy_min, dxy_max):
    return TCut("%f <= abs(dxy_csc) && abs(dxy_csc)<%f"%(dxy_min, dxy_max))


def eta_sh_st1(eta_min, eta_max):
    return TCut("%f < abs(csc_gp_eta) && abs(csc_gp_eta)< %f"%(eta_min, eta_max))
    
def same_direction_cut():
    return TCut("Lxy_csc >0 && pzvz_csc>0")
    

def pt_cut(eta_min, sim_pt, var=12):
    slope = pt_slope_inter[eta_min][0]
    inter = pt_slope_inter[eta_min][1]
    return TCut("( (1/abs(csc_bending_angle_%d) + %f) / %f ) > %f"%(var, inter, slope, sim_pt))


def pt_from_povercosh(eta_min, sim_pt, var=12):
    slope = pt_pos_slope_inter[eta_min][0]
    inter = pt_pos_slope_inter[eta_min][1]
    return TCut("((1/abs(csc_bending_angle_%d) + %f) / %f ) > %f"%(var, inter, slope, sim_pt))



#_____________________________________________________________

def FitHistoFunction68(b1, xBins, xminBin, xmaxBin, yminBin, ymaxBin, printa): 

    
    r1 = TH1F("r1","1/abs(\Delta\phi) vs p^{Sim}",xBins,xminBin,xmaxBin)
    
    for x in range(xminBin,xmaxBin):
        printa = 0;
        if (printa > 0):
            print "*********** For bin x: ",x
            
        firstbin = 0                        # First Bin with hits
        flag = 0                            # A simple way to tell if it has already been used
        suma = 0                            # Total number of entries (sum of frequencies) on the vertical axis

        # Find the total number of frequencies
        for y in range (yminBin,ymaxBin):
            pp = b1.GetBin(x,y)
            h = b1.GetBinContent(pp)

            if flag ==0 and h>0:
                flag =1 
                firstbin = y                # First bin with hits

            
            if h>0:
                suma = suma + h             # Adding the sume




        # Find the median value
        
        midbin = 0                          # Bin number of the median entry
        med = 0                             # Median 
        temps = 0

        if (suma%2 ==1) :
            med = (suma-1)/2 + 1            # Set the value of the median

        if (suma%2 ==0):
            med = (suma/2)                  # This might need to be added 0.5
         

        for m in range (0,ymaxBin):
                pp = b1.GetBin(x,m)
                h = b1.GetBinContent(pp)

                if h > 0:
                    temps = temps + h       # Summing the values until I get to the median
                if temps >= med:
                    midbin = m              # Break once I get to the median
                    break

       
        if (printa > 0):

                print "suma: ",suma
                print "Midbin: ",midbin
                print "mediana count: ",temps


        
        # midbin is the actual value to be stored in (x, midbin) histogram.    
        # Find the error above the median
        
        sumerrup = 0                        # Sum of events up
        binerrup = 0                        # Bin which has the 34% of events
        
        for k in range (midbin, 10000):     # Looping over the midbin up to 10000 
            pp = b1.GetBin(x,k)
            h = b1.GetBinContent(pp)
            if h>0:
                sumerrup = h + sumerrup     # Summing the events
            if (sumerrup >= 0.33*suma):     # If the summ is bigger or equal to 34% of the total number of entries, break
                binerrup = k
                break
        
        sumerrlow = 0
        binerrlow = 0

        
        for r in range (0, midbin):
            pp = b1.GetBin(x,midbin-r)      # Get the bin starting from midbin, midbin -1 and so on up to 0
            h = b1.GetBinContent(pp)
      
            if h>0:
                sumerrlow = sumerrlow + h   # Store the value for a valid h

            if (sumerrlow >= 0.33*suma):
                binerrlow = midbin-r        # Store the bin which has the 34% value 
                break
        
        # error is the difference averaged on the bin low and bin up
 
        errorbin = abs(binerrup - binerrlow)/2

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
