import ROOT

def FitHistoFunction68(b1, xBins, xminBin, xmaxBin, yminBin, ymaxBin, printa): 

    r1 = ROOT.TH1F("r1","1/abs(\Delta\phi) vs p^{Sim}",xBins,xminBin,xmaxBin)
    
    for x in range(xminBin,xmaxBin):

        if (printa > 0):
            print "*********** For bin x: ",x
            
        binsnonz = 0                        # Numbers of non zero bins
        binsy = 0                           # Number of bins (generally ybins)
        flag = 0                            # A simple way to tell if it has already been used
        firstbin = 0                        # Bin number of the first bin with hits
        suma = 0                            # Total number of entries (sum of frequencies) on the vertical axis

        # Find the total number of frequencies
        for y in range (yminBin,ymaxBin):
            pp = b1.GetBin(x,y)
            h = b1.GetBinContent(pp)
            binsy = binsy + 1

            if flag ==0 and h>0:
                flag =1 
                firstbin = y                # First bin with hits

            
            if h>0:
                binsnonz = binsnonz + 1     #Adding to the counter of non zer o bins
                suma = suma + h             # Adding the sume


        # Find the median value
        
        midbin = 0                          # Bin number of the median entry
        med = 0                             # Median 


        if (suma%2 ==1) :
            med = (suma-1)/2 + 1            # Set the value of the median
            temps = 0                       # Defining the counter
            
            for m in range (yminBin,ymaxBin):
                pp = b1.GetBin(x,m)
                h = b1.GetBinContent(pp)

                if h > 0:
                    temps = temps + h       # Summing the values until I get to the median
                if temps >= med:
                    midbin = m              # Break once I get to the median
                    break


            #print "Suma: ", suma
            #print "med: ",med
            #print "Temps: ",temps
            #print "bin m: ",m

            #for yy in range (m+1, ymaxBin):
            
            #    print "bin yy after m: ",yy
            #    print "bin m+1 content: ",b1.GetBinContent(b1.GetBin(x,yy)) 
 
        if (suma%2 == 0):
            med = suma/2                    # Definig for the odd cases (FIXME)
            temps = 0;                      # Counter
            
            for m in range (yminBin,ymaxBin):
                pp = b1.GetBin(x,m)
                h = b1.GetBinContent(pp)
                if h > 0:
                    temps = temps + h
                if temps > med:
                    midbin = m              # Same as before, this should be the "First bin bigger than the median"
                    break

            #print "Temps: ",temps
            #print "Bin m: ",m

            
            auxbin = 0;                     # Bin lower than the median
            seconds = 0                     # Second counter
            if (temps > med):               # If the first sum is above the median do this (don't do this if it's exactly equal).

                for q in range (yminBin,ymaxBin):
                    pp = b1.GetBin(x,q)
                    h = b1.GetBinContent(pp)
                    if h > 0:
                        seconds = seconds + h    

                    if seconds<med and seconds + b1.GetBinContent(b1.GetBin(x,q+1)) > med:
                        auxbin = q
                        break

            if (auxbin > 0):                # If auxbin was filled, do this:
                midbin = (midbin + auxbin) /2

            if (printa > 0):

                print "suma: ",suma
                print "Midbin: ",midbin
                print "auxbin: ",auxbin
                print "mediana c: ",temps


        # midbin is the actual value to be stored in (x, midbin) histogram.    
        # Find the error above the median
        
        sumerrup = 0                        # Sum of events up
        binerrup = 0                        # Bin which has the 34% of events
        
        for k in range (midbin, 10000):     # Looping over the midbin up to 10000 
            pp = b1.GetBin(x,k)
            h = b1.GetBinContent(pp)
            if h>0:
                sumerrup = h + sumerrup     # Summing the events
            if (sumerrup >= 0.34*suma):     # If the summ is bigger or equal to 34% of the total number of entries, break
                binerrup = k
                break
        
        sumerrlow = 0
        binerrlow = 0

        
        for r in range (0, midbin):
            pp = b1.GetBin(x,midbin-r)      # Get the bin starting from midbin, midbin -1 and so on up to 0
            h = b1.GetBinContent(pp)
      
            if h>0:
                sumerrlow = sumerrlow + h   # Store the value for a valid h

            if (sumerrlow >= 0.34*suma):
                binerrlow = midbin-r        # Store the bin which has the 34% value 
                break
        
        # error is the difference averaged on the bin low and bin up
 
        if binerrup == binerrlow and binerrup > 0 : 
            
            errorbin = binerrup
            
        else:
            errorbin = abs(binerrup - binerrlow)/2

        if (printa > 0):
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



def draw2D(file,dir,den,xaxis,yaxis,x_bins,y_bins,stat, low, hig):
    
    c1 = ROOT.TCanvas()
    c1.SetGridx()
    c1.SetGridy()
    c1.SetTickx()
    c1.SetTicky()
    ROOT.gStyle.SetOptFit(0111)
    ROOT.gStyle.SetOptStat(0)

    name = "0"
    if(low == "1.5"):
        name = "15"
    if(low=="1.6"):
        name = "16"
    if(low=="1.7"):
        name = "17"
    if(low=="1.8"):
        name = "18"
    if(low == "1.9"):
        name = "19"
    if(low == "2.0"):
        name = "20"
    if(low == "2.1"):
        name = "21"
    if(low == "2.2"):
        name = "22"
    if(low == "2.3"):
        name = "23"
    if(low == "2.4"):
        name = "24"
        
    ROOT.gStyle.SetStatY(0.25)
    ROOT.gStyle.SetStatX(0.90)
    ROOT.gStyle.SetStatW(0.1729)
    ROOT.gStyle.SetStatH(0.12)

    f = ROOT.TFile(file)

    tt10 = f.Get(dir)
    tt11 = f.Get(dir)
    tt12 = f.Get(dir)
    tt13 = f.Get(dir)           
    xBins = int(x_bins[1:-1].split(',')[0])
    xminBin = float(x_bins[1:-1].split(',')[1])
    xmaxBin = float(x_bins[1:-1].split(',')[2])
    yBins = int(y_bins[1:-1].split(',')[0])
    yminBin = float(y_bins[1:-1].split(',')[1])
    ymaxBin = float(y_bins[1:-1].split(',')[2])

    todrawb1 = "%s"%yaxis+":"+"%s>>b1"%xaxis
    todrawb2 = "%s"%yaxis+":"+"%s>>b2"%xaxis
    
    b1 = ROOT.TH2F("b1","b1",xBins,xminBin,xmaxBin,yBins,yminBin,ymaxBin)
    b1.GetXaxis().SetTitle("p of Simulated Muon Track / cosh (Global Position eta) [GeV/?]")
    b1.GetYaxis().SetTitle("1/ abs(\Delta \phi _{1,2})")
    b1.SetTitle("1/abs(\Delta \phi_{SH in CSC ST 1-2 }) vs p^{SimT}, ct0, 80k Ev, ME11 - ME2, Lxy>0, pzvz>0")
    b1.SetTitle(" 1/ | \Delta \phi_{ 1 - 2} |  vs p^{simT} / cosh(GP.eta), ct 0 mm")
    b1.SetMaximum(5)
    b1.SetStats(1)

    binxmax = xBins
    tt10.Draw(todrawb1,den,"colz")

    text4 = ROOT.TLatex(06.2,59.9,low+"< \eta_{gp} <"+hig)
    text5 = ROOT.TLatex(03.2,51.9,"No Lxy cut")


    printa = 0
    r1 = FitHistoFunction68(b1, 20, 0, 20, 0, 300, printa)
    r1.Fit("pol1", "EMF", "same", 0, binxmax)

    r1.GetXaxis().SetTitle("p of Simulated Muon Track/ cosh( Global Position eta) [GeV/ ?]")
    r1.GetYaxis().SetTitle("1/ abs(\Delta \phi _{1,2})")
    r1.SetTitle("1/ abs(\Delta \phi_{SH in CSC ST 1-2 } ) vs p^{SimT}, ct0, 80k Ev, ME11 - ME2, Lxy>0, pzvz>0")
    r1.SetTitle(" 1/ | \Delta \phi_{ 1 - 2} |  vs p^{simT} / cosh(GP.eta), ct 0 mm")
                
    r1.Draw("same")
    r1.Draw()
    text4.Draw("same")
    #text5.Draw("same")


    c1.SaveAs("Profile_"+name+".pdf")
    c1.SaveAs("Poster3.png")


low = "2.2"
hig = "2.4"
sta="ME11"
var="Denominator"
tree = "HLTBendingAngle/trk_eff_csc_"+sta
den = "nlayerscsc>4 && pt_SimTrack_csc>0 && has_csc_12>0 && abs(csc_gp_eta)>"+low+" && abs(csc_gp_eta)<"+hig+" && Lxy_csc <0 && pzvz_csc<0"





xaxis="p_SimTrack_csc/cosh(csc_gp_eta)"
yaxis="1/abs(csc_bending_angle_12)"
#yaxis="1/abs(csc_gv_phi - csc_second_gv_phi)"

x_bins = "(120,0,120)"
y_bins = "(300,0,300)"
draw2D("../../ct0.root",tree,den,xaxis,yaxis,x_bins,y_bins,sta, low, hig)

