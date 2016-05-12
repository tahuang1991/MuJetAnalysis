from ROOT import *
from math import *
import array



def has_csc(stx = 1):
    if stx == 1:
        return TCut("nlayerscsc>=4")
    if stx == 2:
        return TCut("nlayers_st2>=4")
    if stx == 3:
        return TCut("nlayers_st3>=4")
    if stx == 4:
        return TCut("nlayers_st4>=4")


def dxy_cut(dxy_min, dxy_max):
    return TCut("%f <= abs(dxy) && abs(dxy)<%f"%(dxy_min, dxy_max))


def eta_sh_cut(eta_min, eta_max, stx = 2):
    if stx ==1:
        return TCut("%f <= abs(csc_gp_eta) && abs(csc_gp_eta)<= %f"%(eta_min, eta_max))
    if stx == 2:
        return TCut("%f <= abs(csc_gp_second_st2) && abs(csc_gp_second_st2)<= %f"%(eta_min, eta_max))
    if stx == 3:
            return TCut("%f <= abs(csc_gp_second_st3) && abs(csc_gp_second_st3)<= %f"%(eta_min, eta_max))
    if stx == 3:
            return TCut("%f <= abs(csc_gp_second_st4) && abs(csc_gp_second_st4)<= %f"%(eta_min, eta_max))
    

def has_csc_sh_pairs(var):
    return TCut("has_csc_%d>0"%var)


def SimTrack_pt_cut(minpt, maxpt):
    return TCut("pt_SimTrack > %d && pt_SimTrack < %d"%(minpt,maxpt))


def endcap_csc(value = 1):
    if value == 0:
        return TCut("endcap_st1 >0 && endcap_st2 >0 && endcap_st3 >0 && endcap_st4 >0")
    
    if value == 1:
        return TCut("endcap_st1 == 1 && endcap_st2 == 1 && endcap_st3 == 1 && endcap_st4 == 1")

    if value == 2:
        return TCut("endcap_st1 == 2 && endcap_st2 == 2 && endcap_st3 == 2 && endcap_st4 == 2")


def ME1X_only(X):
    if X == 1:
        return TCut("csc_ring == 1  || csc_ring == 4")

    if X ==2:

        return TCut("csc_ring == 2")

    if X ==3:
        
        return TCut("csc_ring == 3")

def parity_csc(case):
    if case ==0:
        return TCut("csc_chamber%2 == 1 && csc_chamber_st2%2 == 0 && csc_chamber_st3%2 == 0")
    if case ==1:
        return TCut("csc_chamber%2 == 1 && csc_chamber_st2%2 == 1 && csc_chamber_st3%2 == 1")
    if case == 2:
        return TCut("csc_chamber%2 == 0 && csc_chamber_st2%2 == 0 && csc_chamber_st3%2 == 0")
    if case ==3:
        return TCut("csc_chamber%2 == 0 && csc_chamber_st2%2 == 1 && csc_chamber_st3%2 == 1")


def pT_from_Direction(etamin = 1.6, stx = 1, parity_case=0, minptcut=10):

    slope = 1.0
    intercept = 1.0

    if stx ==1:
        if parity_case ==0 :
            if etamin == 1.6:
                slope = 5.257
                intercept = 14.5
            if etamin == 1.8:
                slope= 6.376
                intercept = 13.05
            if etamin == 2.0:
                slope = 9.337
                intercept = 15.06
            if etamin == 2.2:
                slope = 10.86
                intercept = 12.69

        if parity_case ==1 :
            if etamin == 1.6:
                slope = 4.837
                intercept = 11.98
            if etamin == 1.8:
                slope= 6.868
                intercept = 15.32
            if etamin == 2.0:
                slope = 10.14
                intercept =17.15
            if etamin == 2.2:
                slope = 10.75
                intercept = 10.67
                
        if parity_case ==2 :
            if etamin == 1.6:
                slope = 4.5
                intercept =8.347
            if etamin == 1.8:
                slope= 8.434
                intercept = 16.35
            if etamin == 2.0:
                slope = 10.16
                intercept =10.55
            if etamin == 2.2:
                slope = 11.28
                intercept = 10.86

        if parity_case ==3 :
            if etamin == 1.6:
                slope = 7.225
                intercept = 19.92
            if etamin == 1.8:
                slope= 9.508
                intercept = 21.44
            if etamin == 2.0:
                slope = 11.02
                intercept =16.94
            if etamin == 2.2:
                slope = 11.34
                intercept = 11.64

                
    return TCut(" (( 1/abs(csc_bending_angle_12) + %f )/%f ) > %f"%(intercept, slope, minptcut))





def pT_from_Positions(etamin = 1.6, stx = 1, parity_case=0, minptcut=10):

    slope = 1.0
    intercept = 1.0
    prop = 0.0

    if stx ==1:
        if parity_case ==0 :
            prop = 0.649
            if etamin == 1.6:
                slope = 0.05517
                intercept = 0.08284
            if etamin == 1.8:
                slope= 0.08192
                intercept = 0.1122
            if etamin == 2.0:
                slope = 0.1682
                intercept = 0.2233
            if etamin == 2.2:
                slope = 0.5304
                intercept = 1.061

        if parity_case ==1 :
            prop = 0.3533
            if etamin == 1.6:
                slope = 0.1121
                intercept = 0.2312
            if etamin == 1.8:
                slope= 0.1593
                intercept = 0.2771
            if etamin == 2.0:
                slope = 0.3293
                intercept = 0.5923
            if etamin == 2.2:
                slope = 0.8649
                intercept = 1.429

        if parity_case ==2 :
            prop = 0.5724
            if etamin == 1.6:
                slope = 0.04756
                intercept = 0.06255
            if etamin == 1.8:
                slope= 0.08478
                intercept = 0.1368
            if etamin == 2.0:
                slope = 0.1608
                intercept = 0.1612
            if etamin == 2.2:
                slope = 0.4944
                intercept = 1.043
                
        if parity_case ==3 :
            prop = 0.3175
            if etamin == 1.6:
                slope = 0.1026
                intercept = 0.1795
            if etamin == 1.8:
                slope= 0.1495
                intercept = 0.2236
            if etamin == 2.0:
                slope = 0.3166
                intercept = 0.5733
            if etamin == 2.2:
                slope = 0.8348
                intercept = 1.468



    return TCut(" (( 1/abs(abs(delta_y_gp_23) - %f*abs(delta_y_gp_12) )  + %f )/%f ) > %f"%(prop, intercept, slope, minptcut))





def Combined_pT(etamin = 1.6, endcapx = 0, minptcut = 10, even_chambers_only= 0):


    slope_phi = 0.0
    intercept_phi = 0.0
    sigma_phi = 0.0

    if even_chambers_only ==0 :
        if etamin == 1.6:
            slope_phi = 4.826
            intercept_phi = 12.52
            sigma_phi = 2.12
        if etamin == 1.8:
            slope_phi= 6.689
            intercept_phi = 14.36
            sigma_phi = 2.861
        if etamin == 2.0:
            slope_phi = 9.25
            intercept_phi = 11.66
            sigma_phi = 3.427
        if etamin == 2.2:
            slope_phi = 10.65
            intercept_phi = 13.88
            sigma_phi = 3.232

            
    if even_chambers_only ==1 :
        if etamin == 1.6:
            slope_phi = 3.888
            intercept_phi = 6.554
            sigma_phi = 2.44
        if etamin == 1.8:
            slope_phi= 7.699
            intercept_phi = 10.03
            sigma_phi = 3.252
        if etamin == 2.0:
            slope_phi = 9.587
            intercept_phi = 9.888
            sigma_phi = 3.278
        if etamin == 2.2:
            slope_phi = 11.26
            intercept_phi = 13.9
            sigma_phi = 3.166

    slope_y = 0.0
    intercept_y = 0.0
    mxx = 0.0
    sigma_y = 0.0

    if even_chambers_only ==0 :
        mxx = 0.3627
        if etamin == 1.6:
            slope_y = 0.08319
            intercept_y = 0.01966
            sigma_y =1.298
        if etamin == 1.8:
            slope_y= 0.1463
            intercept_y = 0.1762
            sigma_y = 2.006
        if etamin == 2.0:
            slope_y = 0.2977
            intercept_y = 0.5032
            sigma_y = 2.724
        if etamin == 2.2:
            slope_y = 0.7292
            intercept_y = 1.027
            sigma_y = 2.833

    if even_chambers_only ==1 :
        mxx = 0.574
        if etamin == 1.6:
            slope_y = 0.04374
            intercept_y = 0.01856
            sigma_y = 1.235
        if etamin == 1.8:
            slope_y= 0.08826
            intercept_y = 0.1192
            sigma_y = 1.942
        if etamin == 2.0:
            slope_y = 0.1534
            intercept_y = 0.1095
            sigma_y = 2.552
        if etamin == 2.2:
            slope_y = 0.4237
            intercept_y = 0.5927
            sigma_y = 3.109

    return TCut("(((((1/abs(csc_bending_angle_12) + %f )/%f )/(%f*%f)) +  ((( 1/abs(abs(delta_y_gp_23) - %f*abs(delta_y_gp_12) )  + %f )/%f )/(%f*%f)))/(1/(%f*%f) + 1/(%f*%f))) >%f "%(intercept_phi, slope_phi, sigma_phi, sigma_phi, mxx, intercept_y, slope_y, sigma_y, sigma_y, sigma_phi, sigma_phi, sigma_y, sigma_y, minptcut))
                
    #return TCut(" (((1/abs(csc_bending_angle_12) + %f )/%f )/(%f*%f)) > %f"%(intercept_phi, slope_phi, sigma_phi, sigma_phi, minptcut))
                
    #return TCut("( (     +  (( 1/abs(abs(delta_y_gp_23) - %f*abs(delta_y_gp_12) )  + %f )/%f )/(%f%f)    )/( 1/(%f*%f) + 1/(%f*%f)  )   ) > %f"%(intercept_phi, slope_phi, sigma_phi, sigma_phi, multiplier, intercept_y, slope_y, sigma_y, sigma_y, sigma_phi, sigma_phi, sigma_y, sigma_y, minptcut)     )

    

#_____________________________________________________________

def FitHistoFunction68(b1, xBins, xminBin, xmaxBin, yBins, yminBin, ymaxBin, printa): 
    
    r1 = TH1F("r1","1/abs(\Delta\phi) vs p^{Sim}",xBins,xminBin,xmaxBin)
    for x in range(0,xBins):

        if (printa > 0):
            print "*********** For bin x: %d **********************"%x
            

        # Find the total number of frequencies
        totalfreq = b1.Integral(x,x,0,yBins+1)

        # Calculate half of the frequencies
        med = 0
        
        if (totalfreq%2 ==1) :
            med = (totalfreq-1)/2 + 1            # Set the value of the median

        if (totalfreq%2 ==0):
            med = (totalfreq/2) + 0.5               # This might need to be added 0.5

        temporal = 0
        midbin = 0
        
        for m in range (0,yBins+1):
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
        
        sumerrup = 0                       # Sum of events up
        binerrup = 0                       # Bin which has the 34% of events
        
        for k in range (midbin, yBins+1): # Looping over the midbin up to 10000 
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

        
        if errorbin ==0:
            errorbin == 1

            
        scale = yBins / ymaxBin
        if ymaxBin < yBins:
            scale = ymaxBin / yBins


        r1.SetBinContent(x, midbin*scale)
        r1.SetBinError(x, errorbin*scale)

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
