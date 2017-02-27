import os

for i in range(0,15):
    ptCuts = [3,5,7,10,15,20,30,40]
    for ptCut in ptCuts:
        
        target = open("BatchFile_DT_Pt%d_Combo%d.sh"%(ptCut, i), 'w')
        target.write("#!/bin/bash\n")
        target.write("#BSUB -q 8nh\n")
        target.write("#BSUB -J Barrel\n")
        target.write("cd /afs/cern.ch/user/d/dildick/work/GEM/MuonPhaseIITDRStudies/CMSSW_6_2_0_SLHC28_patch1/src\n")
        target.write("eval `scramv1 runtime -sh`\n")
        target.write("python DisplacedMuon_Efficiency_DT_rate_v1.py %d %d\n"%(ptCut, i))
        target.close()
        #print "bsub < BatchFile_DT_Pt%d_Combo%d.sh"%(ptCut, i)
        os.system("bsub < BatchFile_DT_Pt%d_Combo%d.sh"%(ptCut, i))








