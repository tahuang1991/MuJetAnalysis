import array, os, re, math, random, string
from math import *

ctau_mean_mm = 50.0

#filename = "../2013-01-23_DarkSUSY_MC_8TeV/Samples_With_Different_mGammaD/DarkSUSY_mH_125_mGammaD_0400_8TeV-madgraph452_bridge224_events80k.lhe"
filename = "DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_events80k.lhe"

f = open(filename, 'r')

event_begin = False
event_end = True

for line in f:
	if line == '<event>\n':
		event_begin = True
		event_end = False
	if line == '</event>\n':
		event_begin = False
		event_end = True
	new_line = ''
	if event_begin == True and event_end == False:
		word_n = 0
		for word in line.split():
			if word == '3000022' or word_n > 0:
				word_n = word_n + 1
				if word_n < 13:
					if word_n == 12:
					  ctau_mm = '%E' % random.expovariate(1.0/ctau_mean_mm) # exponential distribution
#					  print "ctau (mm) mean: ", ctau_mean_mm, " actual: ", ctau_mm
					  new_line = new_line + ctau_mm + '   '
					else:
						new_line = new_line + word + '   '
				else:
					new_line = new_line + word + '\n'
					word_n = 0
	if new_line == '':
		print line.rstrip('\n')
	else:
		print new_line.rstrip('\n')

f.close()
