# Run quiet mode
import sys
sys.argv.append( '-b' )
import ROOT 
ROOT.gROOT.SetBatch(1)
#from Helpers import *
ROOT.gErrorIgnoreLevel=1001
from ROOT import * 
import random
import os
import numpy as np
from math import *

ROOT.gROOT.SetBatch(1)
ROOT.gStyle.SetStatW(0.07)
ROOT.gStyle.SetStatH(0.06)

ROOT.gStyle.SetOptStat(111110)

#ROOT.gStyle.SetErrorX(0)
#ROOT.gStyle.SetErrorY(0)

ROOT.gStyle.SetTitleStyle(0)
ROOT.gStyle.SetTitleAlign(13) ## coord in top left
ROOT.gStyle.SetTitleX(0.)
ROOT.gStyle.SetTitleY(1.)
ROOT.gStyle.SetTitleW(1)
ROOT.gStyle.SetTitleH(0.058)
ROOT.gStyle.SetTitleBorderSize(0)

ROOT.gStyle.SetPadLeftMargin(0.126)
ROOT.gStyle.SetPadRightMargin(0.10)
ROOT.gStyle.SetPadTopMargin(0.06)
ROOT.gStyle.SetPadBottomMargin(0.13)

ROOT.gStyle.SetMarkerStyle(1)



def frange(end,start=0,inc=0,precision=1):
    """A range function that accepts float increments."""
    import math
    if not start:
        start = end + 0.0
        end = 0.0
    else: end += 0.0

    if not inc:
        inc = 1.0
    count = int(math.ceil((start - end) / inc))

    L = [None] * (count+1)

    L[0] = end
    for i in (xrange(1,count)):
        L[i] = L[i-1] + inc
    L[count] = start
    return L

def addFilesToChain(ch, filedir):
    if os.path.isdir(filedir):
    	  ls = os.listdir(filedir)
    	  for x in ls:
	      	if not(x.endswith(".root")):
			#print "x.endswith(.root) ", x.endswith(".root")
			continue
		x = filedir[:]+x
    		if os.path.isdir(x):
			continue
		ch.Add(x)
    elif os.path.isfile(filedir):
	  ch.Add(filedir)
    else:
	  print " it is not file or dir ", filedir

## draw an ellipse that includes 95% of the entries

signalAcceptance = 0.90

def getEllipse(x,y,a,b, alpha=0, x0=0, y0=0):
  x1 = x*cos(alpha)+y*sin(alpha)-x0
  y1 = x*sin(alpha)-y*cos(alpha)-y0
  #print "x ",x," y ",y," a ",a," b ",b," alpha ",alpha*180/pi," x1 ",x1," y1 ",y1
  return x1*x1/(a*a) + y1*y1/(b*b)

def passEllipse(x,y,a,b,alpha, x0=0, y0=0):
    return getEllipse(x,y,a,b,alpha, x0, y0) <= 1.0

def failEllipse(x,y,a,b,alpha, x0=0, y0=0):
    return getEllipse(x,y,a,b,alpha,x0, y0) > 1.0

def getBackgroundRejectionEllipse(a_axis, b_axis, alpha, x0, y0, signalHist, backgroundHist):
    if signalHist.GetEntries()==0 or backgroundHist.GetEntries()==0:
    	print "warning!!! entries (S and B) ",signalHist.GetEntries(),backgroundHist.GetEntries()
    	return (1.0,0)
    #print "signal and bg, integral/entris ", signalHist.Integral() / signalHist.GetEntries(), backgroundHist.Integral() / backgroundHist.GetEntries()
    signalEntriesTotal = signalHist.GetEntries()*1.0
    backgroundEntriesTotal = backgroundHist.GetEntries()*1.0
    #backgroundIntegral = backgroundHist.Integral()
    #backgroundoverunderflow = backgroundEntriesTotal - backgroundIntegral

    entriesInEllipseSignal  = 0.0
    entriesOutEllipseBackground  = 0.0
    entriesInEllipseBackground  = 0.0

    signalAcceptanceFactor = 0.0
    background = 0.0
    
    ## loop on entries in histogram
    for j in range(1,signalHist.GetNbinsX()+1):
        for k in range(1,signalHist.GetNbinsY()+1):
            
            ## get the bin centers
            signal_x = signalHist.GetXaxis().GetBinCenter(j)
            signal_y = signalHist.GetYaxis().GetBinCenter(k)

            background_x = backgroundHist.GetXaxis().GetBinCenter(j)
            background_y = backgroundHist.GetYaxis().GetBinCenter(k)

            ## signal passes
            if passEllipse(signal_x, signal_y, a_axis, b_axis, alpha, x0, y0):
                entriesInEllipseSignal += signalHist.GetBinContent(j,k)

            ## background passes
            if passEllipse(background_x, background_y, a_axis, b_axis, alpha, x0, y0):
                entriesInEllipseBackground += backgroundHist.GetBinContent(j,k)
		#print "background event in j ",j," k ",k," : ",backgroundHist.GetBinContent(j,k)," total outellipse ",entriesOutEllipseBackground," backgroundEntriesTotal  ",backgroundEntriesTotal

    ## current signal acceptance
    signalAcceptanceFactor = entriesInEllipseSignal / signalEntriesTotal

    ## current background rejection, overflow and underflow should be excluded
    #background = (entriesOutEllipseBackground + backgroundoverunderflow) / backgroundEntriesTotal
    background = 1 - entriesInEllipseBackground/backgroundEntriesTotal
    #print "Signal in Ellipse ",entriesInEllipseSignal," entries ",signalEntriesTotal," BG in Ellipse ",entriesOutEllipseBackground," entries ",backgroundEntriesTotal," backgroundoverunderflow ",backgroundoverunderflow
            #if background<0.50:
            #    break
            #print j,k,signalAcceptanceFactor,background

    return signalAcceptanceFactor, background
            



def get_proptionality_factor(eta, npar):
	slope=0.0
	#slopes_1 = [0,0.645, 0.852,0]
	slopes_1 = [1.279, 0.6357, 1.001, 0.5252]
	slopes_2 = [0.630, .364, .541, .325]
	#slopes_1 = [1.279, 0.6457, 1.001, 0.5252]
	#slopes_2 = [0.648, 0.3542, 0.5636, 0.3217]
	if (abs(eta)<1.6):
		slope = slopes_1[npar]
	if (abs(eta)>=1.6):
		slope = slopes_2[npar]
    
	return slope


def drawEllipse(hist, hist2, nEvent_list, ddYDPhiCuts, a, b, alpha, x0, y0, eff1, nrate, xtitle, ytitle,st_title, text, picname):
    gStyle.SetTitleBorderSize(0);
    gStyle.SetPadLeftMargin(0.126);
    gStyle.SetPadRightMargin(0.04);
    gStyle.SetPadTopMargin(0.06);
    gStyle.SetPadBottomMargin(0.13);
    gPad.SetTickx(1)
    gPad.SetTicky(1)
    xBins = hist.GetXaxis().GetNbins()
    yBins = hist.GetYaxis().GetNbins()
    xmin = hist.GetXaxis().GetXmin()
    xmax = hist.GetXaxis().GetXmax()
    ymin = hist.GetYaxis().GetXmin()
    ymax = hist.GetYaxis().GetXmax()
    btest = TH2F("btest","btest",xBins/2,xmin/2.0,xmax/2.0,yBins/2,ymin/2.0,ymax/2.0)
    btest.GetXaxis().SetTitle(hist.GetXaxis().GetTitle())
    btest.GetYaxis().SetTitle(hist.GetYaxis().GetTitle())
    hist.SetTitle(st_title[1])
    btest.SetTitle(hist.GetTitle())
    el2 = TEllipse(x0,y0,a,b,0,360, alpha*180.0/pi);
    el2.SetLineColor(kBlack);
    #el2.SetLineWidth(3);
    el2.SetFillStyle(4000)
    #meanx_s = hist.GetMean(1)
    #meany_s = hist.GetMean(2)
    #meanx_b = hist2.GetMean(1)
    #meany_b = hist2.GetMean(2)
    c = TCanvas("c_%d_%d"%(int(a*100),int(b*100)),"c_%d_%d"%(int(a*100),int(b*100)),900,400)
    #c.Clear()
    c.Divide(2,1)
    c.cd(1)
    btest.Draw()
    hist.Draw("samecolz")

    el2.Draw("same")
    
    xline1 = TLine(-ddYDPhiCuts[0], ymin/2, -ddYDPhiCuts[0], ymax/4) 
    xline2 = TLine(ddYDPhiCuts[0], ymin/2, ddYDPhiCuts[0], ymax/4) 
    xline1.SetLineColor(kBlack)
    xline2.SetLineColor(kBlack)
    xline1.SetLineStyle(2)
    xline2.SetLineStyle(2)
    xline1.Draw("same")
    xline2.Draw("same")
    angle = "%.3f"%alpha
    print "in Drawellipse a ",a," b ",b," alpha ",alpha," angle ", alpha*180.0/pi, " x0 ",x0, " y0 ",y0," PCut ",ddYDPhiCuts[0]," DCut ",ddYDPhiCuts[1]
    acep_p = float(nEvent_list[5])/float(nEvent_list[4])
    acep_d = float(nEvent_list[6])/float(nEvent_list[4])
    tex1 = ROOT.TLatex(0.15,.3,"%s"%(text))
    tex1.SetNDC()
    tex10 = TLatex(0.2,.9,"Signal entries %d"%(nEvent_list[4]))
    tex10.SetNDC()
    tex3 = TLatex(0.15, 0.7, "Acceptance %.3f(P) %.3f(D) %.3f(H)"%(acep_p, acep_d, eff1))
    tex3.SetTextSize(0.05)
    tex3.SetNDC()
    tex4 = TLatex(0.15, 0.8, "#splitline{HCut: a=%.2f,b=%.3f,angle=%.2f,center(%.1f,%.3f)}{P-Cut: %.2f, D-Cut: %.3f}"%(a, b, alpha*180/pi, x0, y0, ddYDPhiCuts[0],ddYDPhiCuts[1]))
    tex4.SetTextSize(0.05)
    tex4.SetNDC()
    tex4.Draw("same")
    tex3.Draw("same")
    tex1.Draw("same")
    tex10.Draw("same")
    c.cd(2)
    rej_p = 1-float(nEvent_list[2])/float(nEvent_list[1])
    rej_d = 1-float(nEvent_list[3])/float(nEvent_list[1])
    rej_h = 1-float(nrate)/float(nEvent_list[1])
    btest2 = TH2F("btest2","btest2",xBins/2,xmin/2.0,xmax/2.0,yBins/2,ymin/2.0,ymax/2.0)
    btest2.GetXaxis().SetTitle(hist.GetXaxis().GetTitle())
    btest2.GetYaxis().SetTitle(hist.GetYaxis().GetTitle())
    btest2.SetTitle("Rate sample")
    btest2.Draw()
    hist2.Draw("samecolz")
    #hist2.SetTitle(st_title[0])
    el2.Draw("same")
    xline1.Draw("same")
    xline2.Draw("same")
    print "Signal Acceptance: P ",acep_p, " D ",acep_d, " H ",eff1, " Rate nEvent ",nEvent_list[0]," this category ",nEvent_list[1]," Rejection: P ",rej_p," D ",rej_d," H ",rej_h
    tex2 = TLatex(0.15, 0.7, "Rejection %.3f(P), %.3f(D), %.3f(H)"%(rej_p, rej_d, rej_h))
    tex2.SetTextSize(0.05)
    tex2.SetNDC()
    #tex5 = TLatex(0.15, 0.9, "ellipse center(%.1f, %.3f)"%(x0, y0))
    tex5 = TLatex(0.15, 0.9, "Rate nEvent %d, this category %d"%(nEvent_list[0], nEvent_list[1]))
    tex5.SetTextSize(0.05)
    tex5.SetNDC()
    #print "text.split ",text.split(',')," 2nd split  ",(text.split(',')[2]).split('{')
    text_1 =(text.split(',')[2]).split('{')[1]
    tex5.Draw("same")
    #tex11 = ROOT.TLatex(0.15,.7,text_1+","+(st_title[0]))
    tex11 = ROOT.TLatex(0.15,.7,text_1)
    tex11.SetNDC()
    tex2.Draw("same")
    #tex4.Draw("same")
    #tex11.Draw("same")
    c.cd()

    
    c.SaveAs(picname+ "_ellipse.png")

def loopEllipse(chain, chain1, nEvent_list, ddYDPhiCuts, fraction, npar, astart, bstart, xaxis, yaxis,x_bins, y_bins,xtitle, ytitle,st_title, etamin, etamax, cuts,text,picname):

    gStyle.SetOptFit(0111)
    gStyle.SetOptStat(0)
    """
    xBins = b0.GetXaxis().GetNbins()
    yBins = b0.GetYaxis().GetNbins()
    xminBin = b0.GetXaxis().GetXmin()
    xmaxBin = b0.GetXaxis().GetXmax()
    yminBin = b0.GetYaxis().GetXmin()
    ymaxBin = b0.GetYaxis().GetXmax()
    """
    doTest = False
    xBins = int(x_bins[1:-1].split(',')[0])
    xminBin = float(x_bins[1:-1].split(',')[1])
    xmaxBin = float(x_bins[1:-1].split(',')[2])
    yBins = int(y_bins[1:-1].split(',')[0])
    yminBin = float(y_bins[1:-1].split(',')[1])
    ymaxBin = float(y_bins[1:-1].split(',')[2])
    xbinwidth = (xmaxBin-xminBin)/xBins
    ybinwidth = (ymaxBin-yminBin)/yBins
    b_step = ybinwidth

    todrawb0 = "%s"%yaxis[0]+":"+"%s>>b0"%xaxis[0]
    #todrawb01 = "(-1)*%s"%yaxis+":"+"(-1)*%s>>b01"%xaxis
    #todrawb1 = "%s*charge"%yaxis+":"+"%s*charge>>b1"%xaxis
    todrawb1 = "%s"%yaxis[1]+":"+"%s>>b1"%xaxis[1]
    #todrawb11 = "(-1)*%s"%yaxis+":"+"(-1)*%s>>b11"%xaxis
    b0 = TH2F("b0","b0",xBins,xminBin,xmaxBin,yBins,yminBin,ymaxBin)
    #b01 = TH2F("b01","b01",xBins,xminBin,xmaxBin,yBins,yminBin,ymaxBin)
    b0.GetXaxis().SetTitle("%s"%xtitle)
    b0.GetYaxis().SetTitle("%s"%ytitle)
    #b0.SetTitle("%s Vs %s,%s"%(ytitle, xtitle, st_title)) 
    #b0.SetTitleSize(0.05)
    b0.SetStats(1)
    chain.Draw(todrawb0,cuts[0])#background
    #chain.Draw(todrawb01,cuts[0]+"&& charge<0","colz")#background
    #b0.Add(b01)
    print "background todraw ",todrawb0, " cuts ", cuts[0]," b0.Getentries ",b0.GetEntries()," b0.Integral() ",b0.Integral()
    
    b1 = TH2F("b1","b1",xBins,xminBin,xmaxBin,yBins,yminBin,ymaxBin)
    #b11 = TH2F("b11","b11",xBins,xminBin,xmaxBin,yBins,yminBin,ymaxBin)
    b1.GetXaxis().SetTitle("%s"%xtitle)
    b1.GetYaxis().SetTitle("%s"%ytitle)
    #b1.SetTitle("%s Vs %s,%s"%(ytitle, xtitle, st_title)) 
    #b1.SetTitleFont(62)
    #b1.SetTitleSize(0.05)
    #b1.SetMaximum(30)
    b1.SetStats(1)
    chain1.Draw(todrawb1,cuts[1])#signal
    #chain1.Draw(todrawb11,cuts[1]+"&& charge<0","colz")#signal
    #b1.Add(b11)
    print "signal todraw ",todrawb1, " cuts ", cuts[1]," b1.Getentries ",b1.GetEntries()," b1.Integral() ",b1.Integral()

    totrate = b0.GetEntries()
    totsignal = b1.GetEntries()
    ddY_cut = ddYDPhiCuts[0]
    dphi_dir_cut =ddYDPhiCuts[1]
    
    #get events number by drawing tree???
    def getEvents(ch, cut):
	hist = TH2F("hist","hist", 1,xminBin,xmaxBin, 1,yminBin,ymaxBin)
	ch.Draw("1:1>>hist",cut)
	return hist.GetEntries()
    def getEffandRateFromEllipse(maxa, maxb, alpha, x0, y0):
	xaxis1 = "(%s*TMath::Cos(%f)+%s*TMath::Sin(%f)-%f)"%(xaxis[0], alpha, yaxis[0], alpha, x0)
	yaxis1 = "(%s*TMath::Sin(%f)-%s*TMath::Cos(%f)-%f)"%(xaxis[0], alpha, yaxis[0], alpha, y0)
	ellipse_b = "(%s*%s/(%f*%f)+%s*%s/(%f*%f))<=1.0"%(xaxis1, xaxis1, maxa, maxa, yaxis1, yaxis1, maxb, maxb)
	xaxis2 = "(%s*TMath::Cos(%f)+%s*TMath::Sin(%f)-%f)"%(xaxis[1], alpha, yaxis[1], alpha, x0)
	yaxis2 = "(%s*TMath::Sin(%f)-%s*TMath::Cos(%f)-%f)"%(xaxis[1], alpha, yaxis[1], alpha, y0)
	ellipse_s = "(%s*%s/(%f*%f)+%s*%s/(%f*%f))<=1.0"%(xaxis2, xaxis2, maxa, maxa, yaxis2, yaxis2, maxb, maxb)

	nsignal = getEvents(chain1, cuts[1]+"&&"+ellipse_s)
	nrate = getEvents(chain, cuts[0]+"&&"+ellipse_b)
	return float(nsignal)/float(totsignal),nrate

    nEvent_list.append(b0.GetEntries())
    nEvent_list.append(getEvents(chain, cuts[0]+"&& abs(%s)<=%f"%(xaxis[0], ddY_cut)))#rate, overflow and underflow are included
    nEvent_list.append(getEvents(chain, cuts[0]+"&& abs(%s)<=%f"%(yaxis[0], dphi_dir_cut)))
    nEvent_list.append(b1.GetEntries())
    nEvent_list.append(getEvents(chain1, cuts[1]+"&& abs(%s)<=%f"%(xaxis[1], ddY_cut)))#rate, overflow and underflow are included
    nEvent_list.append(getEvents(chain1, cuts[1]+"&& abs(%s)<=%f"%(yaxis[1], dphi_dir_cut)))


    acep_p = float(nEvent_list[5])/float(nEvent_list[4])
    acep_d = float(nEvent_list[6])/float(nEvent_list[4])
    rej_p = 1-float(nEvent_list[2])/float(nEvent_list[1])
    rej_d = 1-float(nEvent_list[3])/float(nEvent_list[1])
    print "nEvent_list ",nEvent_list," ddYDphiCut ", ddYDPhiCuts
    
    meanx_s = b1.GetMean(1)
    meany_s = b1.GetMean(2)
    #print "signal meanx ",meanx_s," meany ",meany_s," bg meanx ",b0.GetMean(1)," meany ",b0.GetMean(2)

    #GetEntries() incldues underflow and overflow, Integral() does not include them by default
    if (b1.GetEntries()<1 or b0.GetEntries() <1 ):
    	print "signal entries ",b1.GetEntries(), " bg entries ",b0.GetEntries() 
    #print "signal integral/entris ", b1.Integral() / b1.GetEntries(),"   Bg ", b0.Integral() / b0.GetEntries()
    preselected_axes_signalAcc_backRej = []
    fraction = fraction/100.0
    maxRej = 0
    maxAccept = 0
    max_a = ddY_cut*2.5
    max_b = dphi_dir_cut*2.5
    min_a = 0.0
    min_b = 0.0
    max_alpha = 0.
    max_centerx = 0.0
    max_centery = 0.0
    centerx = 0
    centery = 0
    signalAcceptanceFactor = 0.0
    background = 0.0
    AcceptanceThresh = fraction
    RejectionThresh = rej_p
    #if (npar==0 or npar==2):# bad resolution	
	#AcceptanceThresh = fraction - 0.05
	#RejectionThresh = 0.5 + rej_p/2.0
    #else:
	#AcceptanceThresh = fraction - 0.02
	#RejectionThresh = 0.5 + rej_p/2.0

    for factor in [1.3, 1.4, 1.5, 1.7, 1.8, 2.0, 2.2, 2.5, 3, 4, 5]:
	max_a = ddY_cut*factor
	max_b = dphi_dir_cut*factor
	print "find max a b, factor ", factor
	#signalAcceptanceFactor, background = getBackgroundRejectionEllipse(max_a, max_b, 0, centerx, centery, b1, b0)
    	signalAcceptanceFactor, background = getEffandRateFromEllipse(max_a, max_b, 0, centerx, centery)
        drawEllipse(b1, b0, nEvent_list, ddYDPhiCuts, max_a, max_b, 0, centerx, centery, signalAcceptanceFactor, background, xtitle, ytitle,st_title, text, picname+"_maxfactor%d"%(int(factor*10)))
    	if signalAcceptanceFactor > fraction+0.015:#make sure fraction<.97
		break
    for factor in [.85, .8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]:
	min_a = ddY_cut*factor
	min_b = dphi_dir_cut*factor
	print "find min a b, factor ", factor
	#signalAcceptanceFactor, background = getBackgroundRejectionEllipse(min_a, min_b, 0, centerx, centery, b1, b0)
    	signalAcceptanceFactor, background = getEffandRateFromEllipse(min_a, min_b, 0, centerx, centery)
        drawEllipse(b1, b0, nEvent_list, ddYDPhiCuts, min_a, min_b, 0, centerx, centery, signalAcceptanceFactor, background, xtitle, ytitle,st_title, text, picname+"_minfactor%d"%(int(factor*10)))
    	if signalAcceptanceFactor < fraction-0.05:
		break
    	
    #make b_range larger 
    if max_b < 2*dphi_dir_cut:
    	max_b = 2*dphi_dir_cut
    if min_b > 0.4*dphi_dir_cut:
    	min_b = 0.4*dphi_dir_cut
    if max_a>0.5*xmaxBin:
    	max_a = 0.5*xmaxBin
    if max_b>1.0:
    	max_b = 1.0
    a_range = frange(min_a, max_a, xbinwidth)
    b_range = frange(min_b, max_b, ybinwidth)
    max_b_lowedge = min_b
    max_b_highedge = max_b
    lena = len(a_range)
    lenb = len(b_range)
    #drawEllipse(b1, b0, nEvent_list, ddYDPhiCuts, max_a, max_b, 0, centerx, centery, signalAcceptanceFactor, background, xtitle, ytitle,st_title, text, picname+"_%d_initial"%(lena*lenb))
    #alpha_degrees = [0.0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    alpha_degrees =[0.0, 2, 4, 6, 8, 180-2, 180-4, 180-6, 180-8]
    #alpha_degrees = [0.0, 2, 4, 180-2, 180-4]
    #alpha_degrees = [0.0]
    nalpha = 0
    alpha = 0.0
    print "arange ",a_range," max_a ",max_a, " brange ", b_range, " max_b ",max_b," alpha_degrees ",alpha_degrees
    if doTest:
	a_range = frange(.2, 5.2, 1)
        b_step = 0.025
	alpha_degrees = [0.0, 2, 4, 180-2, 180-6]
    for xratio in [0.0]:
      for nalpha  in range(0,len(alpha_degrees)):
      #for nalpha  in range(0, 3):
    #for xratio in [-0.3, -0.2, -0.1, -0.05, 0.0, 0.05,0.1,0.2,0.3]:
    #for xratio in [-0.06,-0.03,0.0,0.03,0.06]:
    #  for yratio in [-0.06,-0.03,0.0,0.03,0.06]:
       yratio = xratio
       centerx = meanx_s*xratio
       centery = meany_s*yratio
       alpha = pi*alpha_degrees[nalpha]/180.0
       max_b_highedge = b_range[-1]
       max_b_lowedge = b_range[0]
       m =0
       print "alpha_degree ", alpha_degrees[nalpha], " alpha ",alpha," high dege ",max_b_highedge," x0 ",centerx," y0 ",centery
       for a_axis in a_range:
       #for a_axis in reversed(a_range):
	    #alpha = 0.0
	    m = m+1
	    b_axis = max_b_highedge
	    #signalAcceptanceFactor, background = getBackgroundRejectionEllipse(a_axis, b_axis, alpha, centerx, centery, b1, b0)
	    signalAcceptanceFactor, background = getEffandRateFromEllipse(a_axis, b_axis, alpha, centerx, centery)
	    print "new(a,b) a ", a_axis, " b ", b_axis, " alpha ",alpha, " x0 ",centerx," y0 ",centery," bhigh ",max_b_highedge, " blow ", max_b_lowedge, " signal ", signalAcceptanceFactor, " bg ",background," fraction ",fraction
	    if (m== int(len(a_range)/2.0) or doTest):
	       drawEllipse(b1, b0, nEvent_list, ddYDPhiCuts, a_axis, b_axis, alpha, meanx_s, meany_s, signalAcceptanceFactor, background, xtitle, ytitle,st_title, text, picname+"_nalpha%d_m%d_testplot"%(nalpha, m))
	    if signalAcceptanceFactor < AcceptanceThresh: 
		continue
	    step = max_b_highedge - max_b_lowedge
	    n =0
	    while (step > b_step):
	    #for b_axis in b_range:
		b_axis = (max_b_highedge+max_b_lowedge)/2.0
		n = n+1
		#signalAcceptanceFactor, background = getBackgroundRejectionEllipse(a_axis, b_axis, alpha, centerx, centery, b1, b0)
		signalAcceptanceFactor, background = getEffandRateFromEllipse(a_axis, b_axis, alpha, centerx, centery)
		print "m ",m," n ", n," bstep ",step, " a ", a_axis, " b ", b_axis," bhigh ",max_b_highedge, " blow ", max_b_lowedge, " signal ", signalAcceptanceFactor, " bg ",background
		if signalAcceptanceFactor >= AcceptanceThresh:
		#if (signalAcceptanceFactor > fraction or signalAcceptanceFactor > acep_p):
    		#if (background > RejectionThresh):
		    max_b_highedge = b_axis
		    #max_b_lowedge = b_axis
		    #print " n ", n," bstep ",step, " a ", a_axis, " b ", b_axis, " alpha ",alpha," x0 ", centerx, " y0 ", centery," signal ", signalAcceptanceFactor, " bg ",background, " as reference acep_p ",acep_p
		    if background < maxRej:
		    #if signalAcceptanceFactor > maxAccept:
			maxRej = background
			maxAccept = signalAcceptanceFactor
			max_a = a_axis
			max_b = b_axis
			max_alpha = alpha
			max_centerx = centerx
			max_centery = centery
			drawEllipse(b1, b0, nEvent_list, ddYDPhiCuts, a_axis, b_axis, max_alpha, max_centerx, max_centery, signalAcceptanceFactor, background, xtitle, ytitle,st_title, text, picname+"_nalpha%d_m%d_n%d"%(nalpha, m,n))
		    #preselected_axes_signalAcc_backRej.append([a_axis, b_axis, signalAcceptanceFactor, background])
		else:
		    max_b_lowedge = b_axis	     
		    #max_b_highedge = b_axis
		step = max_b_highedge - max_b_lowedge	
	    if doTest:
	    	print "after trying to better a and b,  a ",a_axis," b ",b_axis," max_b_lowedge ",max_b_lowedge," max_b_highedge ",max_b_highedge," signal ", signalAcceptanceFactor, " bg ",background
	    max_b_highedge = b_axis +  2*b_step
	    max_b_lowedge = b_range[0]
	    	
    nEvent_list.append(int(nEvent_list[1]*(1-maxRej)))
    nEvent_list.append(int(nEvent_list[4]*maxAccept))
    print "max_a ",max_a," max_b ",max_b, " alpha ",max_alpha, " x0 ",max_centerx," y0 ",max_centery ," signalAcceptanceFactor ",maxAccept," background ",maxRej
    return (max_a, max_b, max_alpha, max_centerx, max_centery)
            

def gethist1D(chain,den, todraw="pt"):
	
    	h1 = ROOT.TH1F("h1","h1",len(ptbins)-1, ptbins)
    	chain.Draw("fabs(%s) >> h1"%todraw,den)
	#print "gethist1D, den ",den
	#h1.Print("ALL")
	return h1

def getUpperlimit(h, fractionToKeep):

    ## just a safety to prevent it from crashing
    if h.GetEntries() == 0:
        return 0.0000
    
    ax = h.GetXaxis()
    total = h.Integral()
    bin = 1
    fractionToKeep = fractionToKeep/100.0
    for b in range(ax.GetNbins()):
        if (h.Integral(0,b)/total > fractionToKeep):
            bin = b - 1
            break

    ## interpolate
    x1 = ax.GetBinUpEdge(bin)
    x2 = ax.GetBinUpEdge(bin + 1)
    y1 = h.Integral(0, bin)/total
    y2 = h.Integral(0, bin + 1)/total
    x = x1 + (fractionToKeep - y1)/(y2-y1)*(x2-x1)
    return x

def getcuts(chain, den, num, pt, npar,etamin, etamax, fractionToKeep,x_bins, xtitle, txt, picname):
	
    xBins = int(x_bins[1:-1].split(',')[0])
    xminBin = float(x_bins[1:-1].split(',')[1])
    xmaxBin = float(x_bins[1:-1].split(',')[2])
    if (etamin<1.6):
	    ring = 2
    if (etamin>=1.6):
	    ring = 1
    evenodds = ["odd,even","odd,odd","even,even","even,odd","all pairs"]
    #hasnum = "&& fabs(%s)>0"%(num)
    hist = ROOT.TH1F("hist","hist",3000,0.0,xmaxBin*1.5)
    if pt>2 and pt<10:
	    deltapt=.5
    else:
	    deltapt=1.0	   
    #chain.Draw("TMath::Abs(%s)>>hist"%(num),den+"&& npar_L1==%d && pt>%f && pt<%f"%(npar,pt-deltapt, pt+deltapt))
    chain.Draw("TMath::Abs(%s)>>hist"%(num),den+"&& npar_L1==%d && pt>=%f"%(npar,pt))
    #hist.Print("ALL")
    upperlim = getUpperlimit(hist, fractionToKeep)
    #print "cuts ",den+"&& npar_L1==%d && pt>%f && pt<%f"%(npar,pt-1, pt+1)," upperlim ",upperlim
    print "cuts ",den+"&& npar_L1==%d && pt>=%f"%(npar,pt)," upperlim ",upperlim
    return upperlim
    """
    print "eta%dto%dnpar%d%spt%dfraction%d:%f"%(int(etamin*10), int(etamax*10), npar,num,pt,fractionToKeep,upperlim)
    c1 = ROOT.TCanvas()
    c1.SetGridx()
    c1.SetGridy()
    c1.SetTickx()
    c1.SetTicky()
    hist.Draw()
    hist.GetXaxis().SetTitle("%s"%xtitle)
    hist.GetYaxis().SetTitle("%s"%ytitle)
    hist.SetTitle("%s distribution "%xtitle)
    #tex = ROOT.TLatex(0.15,0.87,"%s"%txt)
    tex = ROOT.TLatex(0.4,0.6,"#splitline{%s}{p_{T}>%d GeV, cut:%.4f}"%(txt,pt, upperlim))
    tex.SetTextSize(0.05)
    tex.SetTextFont(62)
    tex.SetNDC()
    #tex.Draw("same")
    #return Teffs
    #c1.Update()
    #c1.SaveAs("%s_Plateau%d_binsimPt%d.png"%(picname, fractionToKeep,pt))
    #c1.SaveAs("%s_Plateau%d_binsimPt%d.pdf"%(picname, fractionToKeep,pt))

    """
#_____________________________________________________________
		
def makeEffplot_v2(chainlist,todraw, den, num, etamin, etamax, xtitle,ytitle,leg, legheader, txt,picname):
	
    b1 = ROOT.TH1F("b1","b1",len(ptbins)-1, ptbins)
    b1.GetYaxis().SetRangeUser(0.0,1.05)
    b1.GetYaxis().SetTitleOffset(1.1)
    b1.GetYaxis().SetNdivisions(520)
    b1.GetYaxis().SetTitle("Trigger efficiency")
    b1.GetXaxis().SetTitle("True muon p_{T} [GeV]")
    b1.GetXaxis().SetTitleSize(0.05)
    b1.GetXaxis().SetLabelSize(0.05)
    b1.GetYaxis().SetTitleSize(0.05)
    b1.GetYaxis().SetLabelSize(0.05)
    b1.SetTitle(" #scale[1.4]{#font[61]{CMS}} #font[52]{Simulation preliminary}"+"  "*10+" 14 TeV, 0 PU")
    
    
    Teffs = []
    hdens = []
    hnums = []
    npars = 4
    Upperlimits = [0 for x in range(npars)]
    color = [ROOT.kBlue, ROOT.kRed, ROOT.kMagenta+2, ROOT.kGreen+2,ROOT.kCyan+2]
    maker = [20,21,22,23,33]
    print "chainlist ",chainlist
    
    if (etamin<1.6):
	    ring = 2
    if (etamin>=1.6):
	    ring = 1
    #legend = ROOT.TLegend(0.45,0.15,0.9,0.5)
    legend = ROOT.TLegend(0.45,0.20,0.8,0.50)
    legend.SetFillColor(ROOT.kWhite)
    legend.SetTextFont(42)
    legend.SetTextSize(.05)
    legend.SetHeader("%s"%legheader)
    muons = ["Prompt Muons","Displaced Muons, 5<|d_{xy}|<50cm"]
    for n in range(len(chainlist)):
	print "n ",n
	hden = ROOT.TH1F("hden%d"%n,"hden%d"%n,len(ptbins)-1, ptbins)
	hnum = ROOT.TH1F("hnum%d"%n,"hnum%d"%n,len(ptbins)-1, ptbins)
	for i in range(len(ptbins)):
		hden.SetBinContent(i, 0)
		hnum.SetBinContent(i,.0)
	#Teffs.append(ROOT.TEfficiency(hnum, hden))
	hdens.append(hden)
	hnums.append(hnum)
	chain = chainlist[n]
	hdens[n].Add(gethist1D(chain, den[n],todraw))
	hnums[n].Add(gethist1D(chain, den[n]+" && %s"%(num[n]), todraw))
	print " den cut ",den[n]," num cut ", den[n]+" && %s"%(num[n])


    c1 = ROOT.TCanvas()
    c1.SetGridx()
    c1.SetGridy()
    c1.SetTickx()
    c1.SetTicky()

    b1.SetStats(0)
    b1.Draw()
    for n in range(len(chainlist)):
	Teffs.append(ROOT.TEfficiency(hnums[n],hdens[n]))	
	SetOwnership(Teffs[n], False)
	m = len(Teffs)-1
	Teffs[m].SetLineColor(color[n])
	Teffs[m].SetMarkerColor(color[n])
	Teffs[m].SetMarkerStyle(maker[n])
	Teffs[m].Draw("same")
	legend.AddEntry(Teffs[n],"%s"%leg[n],"pl")
    #print "Teffs ",Teffs
    #Teffs[0].Print("ALL")
    legend.Draw("same")

    tex = ROOT.TLatex(0.35,0.57,"%s"%txt)
    #tex = ROOT.TLatex(0.45,0.57,"#splitline{%s}{%d%% eff at %d [GeV]}"%(txt,fractionToKeep,pt))
    #tex = ROOT.TLatex(0.45,0.57,"#splitline{%s}{check the sign of #Delta Y_{12} and #Delta Y_{23}}"%(txt))
    tex.SetTextSize(0.05)
    tex.SetTextFont(62)
    tex.SetNDC()
    tex.Draw("same")
    #c1.Update()
    c1.SaveAs("%s.png"%(picname))
    c1.SaveAs("%s.pdf"%(picname))
    c1.SaveAs("%s.C"%(picname))
    return Teffs
	

def makeplots(Teffs, legs, text, picname):

    b1 = ROOT.TH1F("b1","b1",len(ptbins)-1, ptbins)
    b1.GetYaxis().SetRangeUser(0.0,1.05)
    b1.GetYaxis().SetTitleOffset(1.1)
    b1.GetYaxis().SetNdivisions(520)
    b1.GetYaxis().SetTitle("Trigger efficiency")
    b1.GetXaxis().SetTitle("True muon p_{T} [GeV]")
    b1.GetXaxis().SetTitleSize(0.05)
    b1.GetXaxis().SetLabelSize(0.05)
    b1.GetYaxis().SetTitleSize(0.05)
    b1.GetYaxis().SetLabelSize(0.05)
    b1.SetTitle(" #scale[1.4]{#font[61]{CMS}} #font[52]{Simulation preliminary}"+"  "*10+" 14 TeV, 0 PU")
    
    
    c1 = ROOT.TCanvas()
    c1.SetGridx()
    c1.SetGridy()
    c1.SetTickx()
    c1.SetTicky()

    color = [ROOT.kBlue, ROOT.kRed, ROOT.kGreen+2, ROOT.kMagenta+2,ROOT.kCyan+2]
    maker = [20,21,22,23,33]
    dy_leg = 0.1*len(Teffs)
    
    legend = ROOT.TLegend(0.45,0.2,0.9,0.2+dy_leg)
    legend.SetFillColor(ROOT.kWhite)
    legend.SetTextFont(42)
    legend.SetTextSize(.05)
    #legend.SetHeader("%"%legheader)
    b1.SetStats(0)
    b1.Draw()
    for n in range(len(Teffs)):
	Teffs[n].SetLineColor(color[n])
	Teffs[n].SetMarkerColor(color[n])
	Teffs[n].SetMarkerStyle(maker[n])
	Teffs[n].Draw("samep")
	legend.AddEntry(Teffs[n],"%s"%legs[n],"pl")
    legend.Draw("same")

    tex = ROOT.TLatex(0.4,0.7,"%s"%text)
    tex.SetTextSize(0.05)
    tex.SetTextFont(62)
    tex.SetNDC()
    tex.Draw("same")
    #c1.Update()
    c1.SaveAs("%s.png"%(picname))
    c1.SaveAs("%s.pdf"%(picname))
    c1.SaveAs("%s.C"%(picname))

##############################################################3


treename = "GEMCSCAnalyzer/trk_eff_CSC_ALL"
filedir16 = "/eos/uscms/store/user/tahuang/SLHC23_patch1_2023Muon_gen_sim_Pt2_50_1M/GEMCSCAna_ctau0_Pt2_50_20170131/170201_015620/0000/combined/out_ana_prompt.root"
#filedir46 = "/eos/uscms/store/user/tahuang/DarkSUSY_MH-125_MGammaD-20000_ctau100_14TeV_madgraph-pythia6-tauola/GEMCSCAna_DarkSUSY_ctau100_20170131/170201_015408/0000/combined/out_ana_displaced.root"
filedir46 = "/eos/uscms/store/user/tahuang/DispalcedMuonGun_1M_FlatPt1_50_FlatDxy0_50CM_GEN_SIM_CMSSW620SLHC_v3/GEMCSCAna_DisplacedMuonGun/170219_224752/0000/combined/out_ana_displaced.root"

binLow = [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,12.0,14.0,16.0,18.0,20.0,24.0,28.0,32.0,36.0,42.0,50.0]
ptbins = np.asarray(binLow)
evenodds = ["odd,even","odd,odd","even,even","even,odd","all pairs"]
netas = [1.2,1.4,1.6,1.8,2.0,2.2]
netas = [1.6,1.8,2.0,2.2]
allnpar = [0,1,2,3]
filedirs_v6 = [filedir16, filedir46]
ME21CSConly = False
if len(sys.argv)>=4:
    #take dir name from arguments, condor mode
    pt1 = int(sys.argv[1])
    fraction = int(sys.argv[2]) 
    outputdir1 = sys.argv[3]
    outputdir2 = sys.argv[4]
    #ME21CSConly = (sys.argv[5]=="True")
    #outputdir1 = "Profile_Ellipse_PT_0929_Pt%d_BGPt%d/"%(pt1,pt2)
    #outputdir2 = "Hybrid_Ellipse_PT_0929_Pt%d_BGPt%d/"%(pt1,pt2)
    filedirs_v6 = ["out_ana_prompt.root","out_ana_displaced.root"]
    #if outputdir1[-1] != "/":
    #	outputdir1 = outputdir1+"/"
    #if outputdir2[-1] != "/":
    #	outputdir2 = outputdir2+"/"
else:
    pt1 = 10
    fraction = 92
    outputdir1 = "Profile_Ellipse_PT_20170222_00_eta18to20_frac92_GE21_test/"
    outputdir2 = "Hybrid_Ellipse_PT_20170222_00_eta18to20_fract92_GE21_test/"
LUT = open("HybridLUT_Pt%d_fraction%d.log"%(pt1, fraction),"w+")
LUT_d = open("DirectionLUT_Pt%d_fraction%d.log"%(pt1, fraction),"w+")
LUT_p = open("PositionLUT_Pt%d_fraction%d.log"%(pt1, fraction),"w+")
LUT_nEvent = open("EventsNum_Pt_%d_fraction_%d.log"%(pt1, fraction),"w+")
#for npt in range(len(Pts)):	
def plotalleta(pt, pt1, netas, fraction1 = 90, fraction=95, fraction_d = 99, yaxis = "(csc_bending_angle12_xfactor_L1_2)",ME21CSConly=False):
    Teffs_0 = []
    Teffs_0_p = []
    Teffs_0_d = []
    Teffs_1 = []
    extrapic=""
    extratxt=""
    #fraction_d = 99
    GE21string= "withGE21"
    rate_y = "dphi_dir12_GE21"
    rate_x = "ddY123"
    xaxis = "(deltay123_test)"
    if ME21CSConly:
    	extrapic = "_ME21CSConly"
        extratxt = ", ME21 CSC only"
	GE21string = "NoGE21"
	rate_y = "dphi_dir12_noGE21"
    xaxislist = [rate_x, xaxis]
    yaxislist = [rate_y, yaxis]
    LUT.write("eta%dto%dfraction%d"%(int(netas[0]*10), int(netas[-1]*10), fraction)+extratxt+"\n")
    LUT_d.write("eta%dto%dfraction%d"%(int(netas[0]*10), int(netas[-1]*10), fraction)+extratxt+"\n")
    LUT_p.write("eta%dto%dfraction%d"%(int(netas[0]*10), int(netas[-1]*10), fraction)+extratxt+"\n")
    LUT_nEvent.write("eta%dto%dfraction%d"%(int(netas[0]*10), int(netas[-1]*10), fraction)+extratxt+"\n")

    legs3 = ["Position-based algorithm","Stub alignment algorithm","Hybrid algorithm"]

    ratesample = "RateTree.root"
    ratefile = TFile(ratesample)
    h_total = ratefile.Get("h_eventcount")

    rateEvents = h_total.GetEntries()
    L1MuTriggerRate = TChain("L1MuTriggerRate")
    addFilesToChain(L1MuTriggerRate, ratesample)
    ring = 1
    if (netas[0]<1.6):
	    ring = 2
    if (netas[0]==1.6):
	    ring = 1
    GEMCSCTrackCh0 = TChain("GEMCSCAnalyzer/trk_eff_CSC_ALL")
    GEMCSCME11Ch0 = TChain("GEMCSCAnalyzer/trk_eff_CSC_ME11")
    GEMCSCME21Ch0 = TChain("GEMCSCAnalyzer/trk_eff_CSC_ME21")
    GEMCSCTrackCh1 = TChain("GEMCSCAnalyzer/trk_eff_CSC_ALL")
    GEMCSCME11Ch1 = TChain("GEMCSCAnalyzer/trk_eff_CSC_ME11")
    GEMCSCME21Ch1 = TChain("GEMCSCAnalyzer/trk_eff_CSC_ME21")
    addFilesToChain(GEMCSCTrackCh0, filedirs_v6[0]) 
    addFilesToChain(GEMCSCME11Ch0, filedirs_v6[0]) 
    addFilesToChain(GEMCSCME21Ch0, filedirs_v6[0]) 
    addFilesToChain(GEMCSCTrackCh1, filedirs_v6[1]) 
    addFilesToChain(GEMCSCME11Ch1, filedirs_v6[1]) 
    addFilesToChain(GEMCSCME21Ch1, filedirs_v6[1]) 
    GEMCSCTrackCh0.AddFriend(GEMCSCME11Ch0)
    GEMCSCTrackCh0.AddFriend(GEMCSCME21Ch0)
    GEMCSCTrackCh1.AddFriend(GEMCSCME11Ch1)
    GEMCSCTrackCh1.AddFriend(GEMCSCME21Ch1)


    Teff_out = ROOT.TFile("Teffout_eff%d.root"%fraction,"RECREATE")
    for neta in range(len(netas)-1):
       if (netas[neta]<0 or netas[neta+1]<0):
	    continue
       Teffallnpars = []
       Teffallnpars_p = []
       Teffallnpars_d = []
       legs = ["Prompt muon", "#splitline{Displaced muon}{10<|d_{xy}|<50 cm}"]
       #pt = Pts[npt]
       #pt1 = Pts_1[npt]
       LUT.write("{\n")
       LUT_d.write("{")
       LUT_p.write("{")
       LUT_nEvent.write("{\n")
       for npar in allnpar:
		me11 = evenodds[npar].split(',')[0]
		me21 = evenodds[npar].split(',')[1]
		hasfitcut = "&& fabs(trk_eff_CSC_ME1%d.phi_layer3_fit_%s)<4 && fabs(trk_eff_CSC_ME2%d.phi_layer3_fit_%s)<4 && fabs(trk_eff_CSC_ME3%d.phi_layer3_fit_%s)<4"%(ring, me11, ring, me21, ring, me21)
		chambers = "ME1%d %s,ME2%d %s,ME3%d %s"%(ring, me11, ring, me21, ring, me21)
		st_title = ["Prompt muon, 2<p_{T}<%d"%pt1, "Displaced Muon, 10<|d_{xy}|<50, p_{T}>%d"%pt]
		etamin = netas[neta]
		etamax = netas[neta+1]
		x_bins = "(4000, -40, 40.0)"
		y_bins = "(800, -1.0, 1.0)"
		xtitle = "#Delta#Delta Y"
		ytitle = "#Delta#phi_{dir}"
		ratecut = "maxPositionPt && abs(L1Mu_eta)>%f && abs(L1Mu_eta)<%f && npar==%d"%(etamin, etamax, npar)
		etacuts ="&& meRing==%d"%ring+"&& fabs(trk_eff_CSC_ME2%d.eta_lct_%s)>%f && fabs(trk_eff_CSC_ME2%d.eta_lct_%s)<%f"%(ring,me21,netas[neta],ring,me21,netas[neta+1])
    		checkvalue = "&& fabs(deltay23_test)<50 && fabs(deltay12_test)<50 && fabs(%s)>0 && fabs(%s)>0 && meRing==%d"%(xaxis, yaxis,ring)
		checkx = "&& fabs(%s)<60 && fabs(%s)>0 "%(xaxis, xaxis)
		checky = "&& fabs(%s)<2.0 && fabs(%s)>0 "%(yaxis, yaxis)
		cutsbase =  ["meRing==%d && "%ring+"hasSt1St2St3 && fabs(eta_st2_L1)>%f && fabs(eta_st2_L1)<%f && npar_L1==%d"%(netas[neta],netas[neta+1], npar), "meRing==%d && "%ring+"hasSt1St2St3 && fabs(eta_st2_L1)>%f && fabs(eta_st2_L1)<%f && fabs(genGdMu_dxy)>10 && fabs(genGdMu_dxy)<50 && fabs(genGdMu_dR)<0.1 && npar_L1==%d"%(netas[neta],netas[neta+1], npar)]
		cuts = [cutsbase[0]+" && pt>=2 && pt<%f"%(pt1), cutsbase[1]+"&& pt>=%f"%(pt)]
		#cuts =  [cutsbase[0]+checkx+checky, cutsbase[1]+checkx+checky]
		cuts_p =  [cutsbase[0]+checkx, cutsbase[1]+checkx]
		cuts_d =  [cutsbase[0]+checky, cutsbase[1]+checky]
		#cuts_d =  ["meRing==%d && "%ring+"hasSt1St2St3 && fabs(deltay12_fit)<50 &&  fabs(deltay23_fit)<50 && fabs(eta_st2_sh)>%f && fabs(eta_st2_sh)<%f && npar==%d"%(netas[neta],netas[neta+1], npar)+checky, "meRing==%d && "%ring+" hasSt1St2St3 && fabs(deltay12_fit)<50 &&  fabs(deltay23_fit)<50 && fabs(eta_st2_sh)>%f && fabs(eta_st2_sh)<%f && fabs(genGdMu_dxy)>10 && fabs(genGdMu_dxy)<50 && fabs(genGdMu_dR)<0.1 && npar==%d"%(netas[neta],netas[neta+1], npar)+checky]

	        text = "#splitline{%s}{%.1f<|#eta|<%.2f, p_{T}^{L1}>%d GeV%s}"%(chambers, netas[neta],netas[neta+1],pt, extratxt)
		text_position = "#splitline{%s}{%.1f<|#eta|<%.2f, p_{T}^{L1}>%d GeV}"%(chambers,netas[neta],netas[neta+1],pt)
		ddY_cut = getcuts(GEMCSCTrackCh1, cuts_p[1], xaxis, pt, npar,netas[neta], netas[neta+1], fraction, "(4000,0,40.0)", xtitle,"",outputdir2+"GEMCSC_ctau0_positionOnly_getcuts_recopt_20170131_ptcut%d_st2eta%dto%d_npar%d%s"%(pt, int(netas[neta]*10), int(netas[neta+1]*10), npar,extrapic))
		dphi_dir_cut = getcuts(GEMCSCTrackCh1, cuts_d[1], yaxis, pt, npar,netas[neta], netas[neta+1], fraction, "(3000,0,1.0)", ytitle,"",outputdir2+"GEMCSC_ctau0_directionOnly_getcuts_recopt_20170131_ptcut%d_st2eta%dto%d_npar%d%s"%(pt, int(netas[neta]*10), int(netas[neta+1]*10), npar,extrapic))
		#LUT_d.write("eta%dto%dnpar%dpt%dfraction%d:%f"%(int(netas[neta]*10), int(netas[neta+1]*10), npar,pt,fraction1,dphi_dir_cut)+"\n")
		#LUT_p.write("eta%dto%dnpar%dpt%dfraction%d:%f"%(int(netas[neta]*10), int(netas[neta+1]*10), npar,pt,fraction1,ddY_cut)+"\n")
		ddYDPhiCuts = [ddY_cut, dphi_dir_cut]
		extra_comma = ","
		if npar==3:
			extra_comma = ""
		LUT_d.write("%f"%dphi_dir_cut+extra_comma)
		LUT_p.write("%f"%ddY_cut+extra_comma)

		nEvent_list = []
		nEvent_list.append(rateEvents)
    		
		Teffs_ddY = makeEffplot_v2([GEMCSCTrackCh0, GEMCSCTrackCh1], "pt", cuts_p, ["fabs(%s)<%f"%(xaxis, ddY_cut), "fabs(%s)<%f"%(xaxis, ddY_cut)], netas[neta], netas[neta+1],"true muon p_{T} GeV","Trigger efficiency",legs,"Position-based algo" ,text_position,outputdir2+"GEMCSC_ctau0andctau1000_position_eff_20170131_pt%d_fraction%d_st2eta%dto%d_npar%d%s"%(pt, fraction, int(netas[neta]*10),int(netas[neta+1]*10), npar, extrapic))
		Teffs_dphi_dir = makeEffplot_v2([GEMCSCTrackCh0, GEMCSCTrackCh1], "pt", cuts_d, ["fabs(%s)<%f"%(yaxis, dphi_dir_cut), "fabs(%s)<%f"%(yaxis, dphi_dir_cut)], netas[neta], netas[neta+1],"true muon p_{T} GeV","Trigger efficiency",legs,"Stub alignment algo",text,outputdir2+"GEMCSC_ctau0andctau1000_direction_eff_20170131_pt%d_fraction%d_st2eta%dto%d_npar%d%s"%(pt, fraction, int(netas[neta]*10),int(netas[neta+1]*10), npar, extrapic))
		astart = .1
		bstart = .0# not used 
		cut_list = [ratecut, cuts[1]+checkx+checky]
		(maxa, maxb, alpha, x0, y0) = loopEllipse(L1MuTriggerRate, GEMCSCTrackCh1, nEvent_list, ddYDPhiCuts, fraction, npar, astart, bstart, xaxislist, yaxislist,x_bins, y_bins,xtitle, ytitle,st_title, netas[neta], netas[neta+1], cut_list, text,outputdir1+"GEMCSC_ctau0andctau1000_hyrid_profile_20170131_pt%d_ptbg%d_fraction%d_st2eta%dto%d_npar%d%s"%(pt, pt1, fraction, int(netas[neta]*10),int(netas[neta+1]*10), npar, extrapic))
	        print "after ellipse , nEvent_list ",nEvent_list 
		#print "max_a ",maxa," maxb ",maxb," alpha ",alpha," x0 ",x0, " y0 ",y0
		#xaxis1 = "(%s*TMath::Cos(%f)*charge+%s*TMath::Sin(%f)*charge-%f)"%(xaxis, alpha, yaxis, alpha, x0)
		#yaxis1 = "(%s*TMath::Sin(%f)*charge-%s*TMath::Cos(%f)*charge-%f)"%(xaxis, alpha, yaxis, alpha, y0)
		xaxis1 = "(%s*TMath::Cos(%f)+%s*TMath::Sin(%f)-%f)"%(xaxis, alpha, yaxis, alpha, x0)
		yaxis1 = "(%s*TMath::Sin(%f)-%s*TMath::Cos(%f)-%f)"%(xaxis, alpha, yaxis, alpha, y0)
		ellipse = "(%s*%s/(%f*%f)+%s*%s/(%f*%f))<=1.0"%(xaxis1, xaxis1, maxa, maxa, yaxis1, yaxis1, maxb, maxb)
		Teffs = makeEffplot_v2([GEMCSCTrackCh0, GEMCSCTrackCh1], "pt", [cutsbase[0]+checkx+checky,cutsbase[1]+checkx+checky], [ellipse, ellipse], netas[neta], netas[neta+1],"true muon p_{T} GeV","Trigger efficiency",legs,"Hybrid algo",text,outputdir2+"GEMCSC_ctau0andctau1000_hybrid_eff_20170131_pt%d_ptbg%d_fraction%d_st2eta%dto%d_npar%d%s"%(pt, pt1, fraction, int(netas[neta]*10),int(netas[neta+1]*10), npar, extrapic))
		#Teffs = makeEffplot_v2(filedirs_v6, "pt", treename, cuts, [ellipse+"&& fabs(%s)<%f"%(xaxis, ddY_cut), ellipse+" && fabs(%s)<%f"%(xaxis, ddY_cut)], netas[neta], netas[neta+1],"true muon p_{T} GeV","Trigger efficiency",legs,"Hybrid algo",text,outputdir2+"GEMCSC_ctau0andctau1000_hybrid_eff_20170131_pt%d_ptbg%d_fraction%d_st2eta%dto%d_npar%d%s_addposition"%(pt, pt1, fraction, int(netas[neta]*10),int(netas[neta+1]*10), npar, extrapic))
		#Teffs = makeEffplot_v2(filedirs_v6, "pt", treename, cuts, [ellipse+"&& fabs(%s)<%f"%(xaxis, ddY_cut)+" && fabs(%s)<%f"%(yaxis, dphi_dir_cut), ellipse+" && fabs(%s)<%f"%(xaxis, ddY_cut)+"&& fabs(%s)<%f"%(yaxis, dphi_dir_cut)], netas[neta], netas[neta+1],"true muon p_{T} GeV","Trigger efficiency",legs,"Hybrid algo",text,outputdir2+"GEMCSC_ctau0andctau1000_hybrid_eff_20170131_pt%d_ptbg%d_fraction%d_st2eta%dto%d_npar%d%s_addpositionAnddirection"%(pt, pt1, fraction, int(netas[neta]*10),int(netas[neta+1]*10), npar, extrapic))
       		#makeplots([Teffs_h[0], Teffs_p[0], Teffs[0]], ["Hybrid Algo","Hybrid+Position-based Algo","Hybrid+Position+Direction"], text,outputdir2+"GEMCSC_ctau0andctau1000_combined3_eff_20170131_pt%d_ptbg%d_fraction%d_fractiond%d_St2eta%dto%d_npar%d_addall%s"%(pt, pt1, fraction, fraction_d, int(netas[neta]*10),int(netas[neta+1]*10), npar, extrapic)) 
		#LUT.write("eta%dto%dnpar%dfraction%d:(%f,%f,%f,%f,%f)\n"%(int(netas[neta]*10), int(netas[neta+1]*10), npar,fraction,maxa,maxb,alpha, x0, y0))
		LUT.write("{%f,%f,%f,%f,%f},\n"%(maxa,maxb,alpha, x0, y0))		
		#LUT_nEvent.write(nEvent_list)
    		#LUT_nEvent.write( ','.join( nEvent_list ))
		for item in nEvent_list:
		    LUT_nEvent.write("%f "%item)
		LUT_nEvent.write("\n")
		"""
		cuts_d = [cuts[0]+"&& "+ellipse+"&& pt<%f"%(pt-1), cuts[1]+"&& "+ellipse+" && pt>=%f"%(pt)]
		xaxis_d = "(dphi_dir_st1_st12_L1)"
		yaxis_d = "(dphi_dir_st2_st23_L1)"
		if ME21CSConly:
			xaxis_d = "(dphi_dir_st1_st12_L1_csc)"
			xaxis_d = "(dphi_dir_st2_st23_L1_csc)"
		xtitle_d = "#Delta#phi_{dir}(st1, st12)"
		ytitle_d = "#Delta#phi_{dir}(st2, st23)"
		astart_d = 1.2/120
		#### add one loop to cut on dphi_dir_st1_st12 and dphi_dir_st2_st23
		(maxa_d, maxb_d, alpha_d, x0_d, y0_d) = loopEllipse(filedirs_v6, treename, fraction_d, astart_d, bstart, xaxis_d, yaxis_d,y_bins, y_bins,xtitle_d, ytitle_d,st_title, netas[neta], netas[neta+1], cuts_d,text,outputdir1+"GEMCSC_ctau0andctau1000_hyrid_profile_20170131_pt%d_ptbg%d_fraction%d_fractiond%d_st2eta%dto%d_npar%d_dirinterstation%s"%(pt, pt1, fraction, fraction_d, int(netas[neta]*10),int(netas[neta+1]*10), npar, extrapic))
		#LUT.write("eta%dto%dnpar%dfraction%d:(%f,%f,%f,%f,%f,%f,%f,%f,%f,%f)\n"%(int(netas[neta]*10), int(netas[neta+1]*10), npar,fraction,maxa,maxb,alpha, x0, y0, maxa_d,maxb_d,alpha_d, x0_d, y0_d))		
		#LUT.write("{%f,%f,%f,%f,%f,%f,%f,%f,%f,%f}\n"%(maxa,maxb,alpha, x0, y0, maxa_d,maxb_d,alpha_d, x0_d, y0_d))		
		xaxis1_d = "(%s*TMath::Cos(%f)*charge-%s*TMath::Sin(%f)*charge-%f)"%(xaxis_d, alpha_d, yaxis_d, alpha_d, x0_d)
		yaxis1_d = "(%s*TMath::Sin(%f)*charge+%s*TMath::Cos(%f)*charge-%f)"%(xaxis_d, alpha_d, yaxis_d, alpha_d, y0_d)
		ellipse_d = "(%s*%s/(%f*%f)+%s*%s/(%f*%f))<=1.0"%(xaxis1_d, xaxis1_d, maxa_d, maxa_d, yaxis1_d, yaxis1_d, maxb_d, maxb_d)
		#Teffs = makeEffplot_v2(filedirs_v6, "pt", treename, cuts, [ellipse+"&&"+ellipse_d, ellipse+"&&"+ellipse_d], netas[neta], netas[neta+1],"true muon p_{T} GeV","Trigger efficiency",legs,"Hybrid algo",text,outputdir2+"GEMCSC_ctau0andctau1000_hybrid_eff_20170131_pt%d_ptbg%d_fraction%d_fractiond%d_st2eta%dto%d_npar%d_dirinterstation%s"%(pt, pt1, fraction, fraction_d, int(netas[neta]*10),int(netas[neta+1]*10), npar, extrapic))
		#Teffs = makeEffplot_v2(filedirs_v6, "pt", treename, cuts, [ellipse+"&&"+ellipse_d+" && fabs(%s)<%f"%(xaxis, ddY_cut), ellipse+"&&"+ellipse_d+"&& fabs(%s)<%f"%(xaxis, ddY_cut)], netas[neta], netas[neta+1],"true muon p_{T} GeV","Trigger efficiency",legs,"Hybrid algo",text,outputdir2+"GEMCSC_ctau0andctau1000_hybrid_eff_20170131_pt%d_ptbg%d_fraction%d_fractiond%d_st2eta%dto%d_npar%d_dirinterstation%s"%(pt, pt1, fraction, fraction_d, int(netas[neta]*10),int(netas[neta+1]*10), npar, extrapic))
		"""
       		makeplots([Teffs_ddY[0], Teffs_dphi_dir[0], Teffs[0]], legs3, text,outputdir2+"GEMCSC_ctau0andctau1000_combined3_eff_20170131_pt%d_ptbg%d_fraction%d_fractiond%d_St2eta%dto%d_npar%d_dirinterstation%s"%(pt, pt1, fraction, fraction_d, int(netas[neta]*10),int(netas[neta+1]*10), npar, extrapic)) 
		Teffallnpars.append(Teffs)
		Teffallnpars_p.append(Teffs_ddY)
		Teffallnpars_d.append(Teffs_dphi_dir)
	        Teffs[0].SetName("hybrideta%dto%dnpar%d"%(int(netas[neta]*10),int(netas[neta+1]*10), npar)+"promptmuonpt%dptbg%d"%(pt,pt1))
	        Teffs_ddY[0].SetName("poistioneta%dto%dnpar%d"%(int(netas[neta]*10),int(netas[neta+1]*10), npar)+"promptmuonpt%dptbg%d"%(pt,pt1))
	        Teffs_dphi_dir[0].SetName("directioneta%dto%dnpar%d"%(int(netas[neta]*10),int(netas[neta+1]*10), npar)+"promptmuonpt%dptbg%d"%(pt,pt1))
	        Teffs[1].SetName("hybrideta%dto%dnpar%d"%(int(netas[neta]*10),int(netas[neta+1]*10), npar)+"displacedmuonpt%dptbg%d"%(pt,pt1))
	        Teffs_ddY[1].SetName("poistioneta%dto%dnpar%d"%(int(netas[neta]*10),int(netas[neta+1]*10), npar)+"displacedmuonpt%dptbg%d"%(pt,pt1))
	        Teffs_dphi_dir[1].SetName("directioneta%dto%dnpar%d"%(int(netas[neta]*10),int(netas[neta+1]*10), npar)+"displacedmuonpt%dptbg%d"%(pt,pt1))
		Teffs[0].Write()
		Teffs_ddY[0].Write()
		Teffs_dphi_dir[0].Write()
		Teffs[1].Write()
		Teffs_ddY[1].Write()
		Teffs_dphi_dir[1].Write()
       LUT.write("},\n")
       LUT_p.write("},\n")
       LUT_d.write("},\n")
       LUT_nEvent.write("},\n")
       #print "Teffallnpars len ",len(Teffallnpars),Teffallnpars
       Teff0 = Teffallnpars[0][0]
       Teff1 = Teffallnpars[0][1]
       Teff0_d = Teffallnpars_d[0][0]
       Teff1_d = Teffallnpars_d[0][1]
       Teff0_p = Teffallnpars_p[0][0]
       Teff1_p = Teffallnpars_p[0][1]
       for xpar in range(len(Teffallnpars)-1):
   	Teff0.Add(Teffallnpars[xpar+1][0])		   
   	Teff1.Add(Teffallnpars[xpar+1][1])		   
   	Teff0_d.Add(Teffallnpars_d[xpar+1][0])		   
   	Teff1_d.Add(Teffallnpars_d[xpar+1][1])		   
   	Teff0_p.Add(Teffallnpars_p[xpar+1][0])		   
   	Teff1_p.Add(Teffallnpars_p[xpar+1][1])		   
       Teff0.SetName("hybrideta%dto%d"%(int(netas[neta]*10),int(netas[neta+1]*10))+"promptmuonpt%dptbg%d"%(pt,pt1))
       Teff1.SetName("hybrideta%dto%d"%(int(netas[neta]*10),int(netas[neta+1]*10))+"displacedmuonpt%dptbg%d"%(pt,pt1))
       Teff0_d.SetName("directioneta%dto%d"%(int(netas[neta]*10),int(netas[neta+1]*10))+"promptmuonpt%dptbg%d"%(pt,pt1))
       Teff1_d.SetName("directioneta%dto%d"%(int(netas[neta]*10),int(netas[neta+1]*10))+"displacedmuonpt%dptbg%d"%(pt,pt1))
       Teff0_p.SetName("positioneta%dto%d"%(int(netas[neta]*10),int(netas[neta+1]*10))+"promptmuonpt%dptbg%d"%(pt,pt1))
       Teff1_p.SetName("positioneta%dto%d"%(int(netas[neta]*10),int(netas[neta+1]*10))+"displacedmuonpt%dptbg%d"%(pt,pt1))
       text_h = "#splitline{Hybrid algorithm}{%.1f<|#eta|<%.2f, p_{T}^{L1}>%d GeV%s}"%(netas[neta],netas[neta+1], pt, extratxt)
       text_p = "#splitline{Position-based algorithm}{%.1f<|#eta|<%.2f, p_{T}^{L1}>%d GeV%s}"%(netas[neta],netas[neta+1], pt, extratxt)
       text_d = "#splitline{Stub alignment algorithm}{%.1f<|#eta|<%.2f, p_{T}^{L1}>%d GeV%s}"%(netas[neta],netas[neta+1], pt, extratxt)
       makeplots([Teff0, Teff1], legs, text_h,outputdir2+"GEMCSC_ctau0andctau1000_hybrid_eff_20170131_pt%d_ptbg%d_fraction%d_fractiond%d_St2eta%dto%d_allnpar_dirinterstation%s"%(pt, pt1, fraction, fraction_d, int(netas[neta]*10),int(netas[neta+1]*10), extrapic)) 
       makeplots([Teff0_d, Teff1_d], legs, text_d,outputdir2+"GEMCSC_ctau0andctau1000_direction_eff_20170131_pt%d_fraction%d_St2eta%dto%d_allnpar_dirinterstation%s"%(pt, fraction, int(netas[neta]*10),int(netas[neta+1]*10), extrapic)) 
       makeplots([Teff0_p, Teff1_p], legs, text_p,outputdir2+"GEMCSC_ctau0andctau1000_position_eff_20170131_pt%d_fraction%d_St2eta%dto%d_allnpar%s"%(pt, fraction, int(netas[neta]*10),int(netas[neta+1]*10), extrapic)) 
       text3 = "#splitline{%.1f<|#eta|<%.2f, p_{T}^{L1}>%d GeV%s}{Prompt muon}"%(netas[neta],netas[neta+1], pt, extratxt)
       makeplots([Teff0_p, Teff0_d, Teff0], legs3, text3,outputdir2+"GEMCSC_ctau0andctau1000_combined3_eff_20170131_pt%d_ptbg%d_fraction%d_fractiond%d_St2eta%dto%d_allnpar_dirinterstation%s"%(pt, pt1, fraction, fraction_d, int(netas[neta]*10),int(netas[neta+1]*10), extrapic)) 
       Teffs_0.append(Teff0)
       Teffs_0_p.append(Teff0_p)
       Teffs_0_d.append(Teff0_d)
       Teffs_1.append(Teff1)
    Teffs0_alleta = Teffs_0[0] 
    Teffs0_alleta_p = Teffs_0_p[0] 
    Teffs0_alleta_d = Teffs_0_d[0] 
    Teffs1_alleta = Teffs_1[0] 
    for xeta in range(len(Teffs_0)-1):
       Teffs0_alleta.Add(Teffs_0[xeta+1])	 
       Teffs0_alleta_p.Add(Teffs_0_p[xeta+1])	 
       Teffs0_alleta_d.Add(Teffs_0_d[xeta+1])	 
       Teffs1_alleta.Add(Teffs_1[xeta+1])	 
    Teffs0_alleta.SetName("hybrideta%dto%d"%(int(netas[0]*10),int(netas[-1]*10))+"promptmuonpt%dptbg%d"%(pt,pt1))
    Teffs0_alleta_p.SetName("positioneta%dto%d"%(int(netas[0]*10),int(netas[-1]*10))+"promptmuonpt%d"%(pt))
    Teffs0_alleta_d.SetName("directioneta%dto%d"%(int(netas[0]*10),int(netas[-1]*10))+"promptmuonpt%d"%(pt))
    Teffs1_alleta.SetName("hybrideta%dto%d"%(int(netas[0]*10),int(netas[-1]*10))+"displacedmuonpt%dptbg%d"%(pt,pt1))
    text_alleta = "#splitline{Hybrid algorithm}{%.1f<|#eta|<%.2f, p_{T}^{L1}>%d GeV%s}"%(netas[0],netas[-1], pt, extratxt)
    text_alleta_3 = "#splitline{%.1f<|#eta|<%.2f, p_{T}^{L1}>%d GeV%s}{Prompt muon}"%(netas[0],netas[-1], pt, extratxt)
    makeplots([Teffs0_alleta, Teffs1_alleta], legs, text_alleta,outputdir2+"GEMCSC_ctau0andctau1000_hybrid_eff_20170131_pt%d_ptbg%d_fraction%d_fractiond%d_St2eta%dto%d_allnpar_dirinterstation%s"%(pt, pt1, fraction,fraction_d, int(netas[0]*10),int(netas[-1]*10), extrapic)) 
    makeplots([Teffs0_alleta_p, Teffs0_alleta_d, Teffs0_alleta], legs3, text_alleta_3,outputdir2+"GEMCSC_ctau0andctau1000_combined3_eff_20170131_pt%d_ptbg%d_fraction%d_fractiond%d_St2eta%dto%d_allnpar_dirinterstation%s"%(pt, pt1, fraction,fraction_d, int(netas[0]*10),int(netas[-1]*10), extrapic)) 
    #Teff_out.Reopen("Update")
    Teff_out.Close()
print "outputdir1 ",outputdir1," outputdir2 ",outputdir2
if not os.path.exists(outputdir1):
        os.makedirs(outputdir1)
if not os.path.exists(outputdir2):
        os.makedirs(outputdir2)
pt2 = 0
#plotalleta(pt1,pt2, [1.6,1.8,2.0,2.2,2.4],90, 95, 99, "(dphi_dir_st1_st2_L1_csc)",True)
#plotalleta(pt1,pt2, [1.6,1.8,2.0,2.2],90, 95, 99, "(dphi_dir_st1_st2_L1)",False)
#plotalleta(pt1,pt2, [1.6, 1.8],90, 95, 99, "(dphi_dir_st1_st2_L1)",False)
#plotalleta(pt1,pt2, [1.8, 2.0, 2.15],90, fraction, 99, "(dphi_dir_st1_st2_L1)",False)
#plotalleta(pt1,pt2, [2.0,2.2],90, 95, 99, "(dphi_dir_st1_st2_L1)",False)
#plotalleta(pt1,pt2, [1.6, 1.8, 2.0, 2.2],90, 95, 99, "(dphi_dir_st1_st2_L1)",False)
#plotalleta(pt1,pt2, [1.6, 1.8],90, 95, 99, "(dphi_dir_st1_st2_L1_csc)", True)
plotalleta(pt1,pt2, [1.8,2.0,2.15],90, fraction, 99, "(dphi_dir_st1_st2_L1_csc)", True)