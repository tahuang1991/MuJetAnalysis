from __future__ import division ## floating point division
from ROOT import *

def passedHltPath(t,trigger):
    return (trigger in t.hltPaths)

def analyzeHLT():
    files = {}
    files['DarkSUSY_mH_125_mGammaD_0400_ctauExp_0_8TeV'] = "/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctauExp_0_8TeV_madgraph452_bridge224_LHE_pythia6_RAW/DarkSUSY_mH_125_mGammaD_0400_ctauExp_0_8TeV_madgraph452_bridge224_LHE_pythia6_ANA/d37f287c329e62f6cda917e97d6b627b/out_cutana_1_2_1Aa.root"
    files['DarkSUSY_mH_125_mGammaD_0400_ctauExp_02_8TeV'] = "/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctauExp_02_8TeV_madgraph452_bridge224_LHE_pythia6_RAW/DarkSUSY_mH_125_mGammaD_0400_ctauExp_02_8TeV_madgraph452_bridge224_LHE_pythia6_ANA/d37f287c329e62f6cda917e97d6b627b/out_cutana_1_1_t1W.root"
    files['DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV'] = "/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV_madgraph452_bridge224_LHE_pythia6_RAW/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV_madgraph452_bridge224_LHE_pythia6_ANA/d37f287c329e62f6cda917e97d6b627b/out_cutana_1_2_mjw.root"
    files['DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV'] = "/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_RAW/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_ANA/d37f287c329e62f6cda917e97d6b627b/out_cutana_1_1_Y38.root"
#    f = TFile.Open(files['DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV'])
#files['DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_newHLT']
    #file = "file:/eos/uscms/store/user/lpcgem/dildick/CMSSW_73/dildick/DarkSUSY_mH_125_mGammaD_0400_ctauExp_0_8TeV_madgraph452_bridge224_LHE_pythia6_RAW/DarkSUSY_mH_125_mGammaD_0400_ctauExp_0_8TeV_madgraph452_bridge224_LHE_pythia6_ANA_3/c2a1d8d9d4e09ccfe856b56c4a74ff8c/out_ana.root"
    #file = "file:/eos/uscms/store/user/lpcgem/dildick/CMSSW_73/dildick/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_RAW/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_ANA_5/c2a1d8d9d4e09ccfe856b56c4a74ff8c/out_ana.root"
    file = "file:/eos/uscms/store/user/lpcgem/dildick/CMSSW_73/dildick/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_RAW/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_ANA_5/b97cadbec7ab990f85182de4f25716c7/out_ana.root"    
    file = "file:/eos/uscms/store/user/lpcgem/dildick/CMSSW_73/dildick/DarkSUSY_mH_125_mGammaD_0400_ctauExp_0_8TeV_madgraph452_bridge224_LHE_pythia6_RAW/DarkSUSY_mH_125_mGammaD_0400_ctauExp_0_8TeV_madgraph452_bridge224_LHE_pythia6_ANA/b97cadbec7ab990f85182de4f25716c7/out_ana.root"

    f = TFile.Open(file)
    ana = "cutFlowAnalyzer"
    dir = f.Get(ana)      
    print "Opening directory", dir.GetName()
    t = dir.Get("Events");
    print "Loading tree", t.GetName()
    
    nentries = t.GetEntries();
    m_events = 0
    m_events4GenMu = 0
    m_events1GenMu17 = 0
    m_events2GenMu8 = 0      
    m_events3GenMu8 = 0
    m_events4GenMu8 = 0
    m_events1SelMu17 = 0
    m_events2SelMu8 = 0
    m_events3SelMu8 = 0
    m_events4SelMu8 = 0
    m_events2MuJets = 0
    m_events2DiMuons = 0
    
    m_events2DiMuonsDzOK_FittedVtx = 0
    m_events2DiMuonsDzOK_ConsistentVtx = 0

    m_events2DiMuonsMassOK_FittedVtx_noHLT = 0
    m_events2DiMuonsMassOK_ConsistentVtx_noHLT = 0
    m_events2DiMuonsIsoTkOK_FittedVtx_noHLT = 0
    m_events2DiMuonsIsoTkOK_ConsistentVtx_noHLT = 0
    m_eventsVertexOK_FittedVtx_noHLT = 0
    m_eventsVertexOK_ConsistentVtx_noHLT = 0

    m_eventsDiMuonHLTFired_FittedVtx = 0
    m_eventsDiMuonHLTFired_ConsistentVtx = 0
    m_events2DiMuonsMassOK_FittedVtx = 0
    m_events2DiMuonsMassOK_ConsistentVtx = 0
    m_events2DiMuonsIsoTkOK_FittedVtx = 0
    m_events2DiMuonsIsoTkOK_ConsistentVtx = 0

    m_eventsVertexOK_FittedVtx = 0
    m_eventsVertexOK_ConsistentVtx = 0

    m_eventsGoodFailingHLT = 0
    m_eventsGoodPassingHLT = 0
    m_isDiMuonHLTFired = 0

    ## make a dictionary to count the triggers
    hltPaths = ['HLT_Mu17_Mu8_DZ_v1',
                'HLT_Mu17_Mu8_DZ_v1_NoDz',
                'HLT_Mu30_TkMu11_v1',
                'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v1',
                'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v1_NoIso',
                'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v1',
                'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v1_NoIso',
                'HLT_TripleMu_12_10_5_v1',
                'HLT_TrkMu15_DoubleTrkMu5_v1']
    hltPathPass = {}
    hltPathFail = {}
    for p in hltPaths:
        hltPathPass[p] = 0 ## intialization
        hltPathFail[p] = 0 ## intialization

    for k in range(0,nentries):
        t.GetEntry(k)    
        m_events += 1
        ## print "Processing Event", k

        if (t.is4GenMu):
            m_events4GenMu += 1            
        if (t.is1GenMu17):
            m_events1GenMu17 += 1
            if (t.is2GenMu8):
                m_events2GenMu8 += 1      
            if (t.is3GenMu8):
                m_events3GenMu8 += 1
            if (t.is4GenMu8):
                m_events4GenMu8 += 1
        if (t.is1SelMu17):
            m_events1SelMu17 += 1
            if (t.is2SelMu8):
                m_events2SelMu8 += 1
            if (t.is3SelMu8):
                m_events3SelMu8 += 1
            if (t.is4SelMu8):
                m_events4SelMu8 += 1
                
        if (t.is2MuJets):
            m_events2MuJets += 1
            if (t.is2DiMuons):
                m_events2DiMuons += 1
                
                if (t.is2DiMuonsDzOK_FittedVtx):
                    m_events2DiMuonsDzOK_FittedVtx += 1
                    if (t.is2DiMuonsMassOK_FittedVtx):
                        m_events2DiMuonsMassOK_FittedVtx_noHLT += 1
                        if (t.is2DiMuonsIsoTkOK_FittedVtx):
                            m_events2DiMuonsIsoTkOK_FittedVtx_noHLT += 1
                            if (t.isVertexOK):
                                m_eventsVertexOK_FittedVtx_noHLT += 1
                                for p in hltPaths:
                                    if passedHltPath(t,p):
                                        hltPathPass[p] += 1
                                    else:
                                        hltPathFail[p] += 1
                                """
                                text_file.write("'%s:%s:%s',"%(t.run, t.lumi, t.event))
                                if (not t.isDiMuonHLTFired):                                    
                                    m_eventsGoodFailingHLT += 1
                                    text_file2.write("%s\t%s\n"%(t.genA0_Lxy, t.genA1_Lxy))
                                    #                                    text_file2.write("%s\n"%(t.genA1_Lxy))
                                    #print t.genA0_Lxy
                                    #                                    print "genA0_Lxy", t.genA0_Lxy, "genA1_Lxy", t.genA1_Lxy
                                else:
                                    m_eventsGoodPassingHLT += 1
                                """

                    if (t.isDiMuonHLTFired):
                        m_eventsDiMuonHLTFired_FittedVtx += 1
                        if (t.is2DiMuonsMassOK_FittedVtx):
                            m_events2DiMuonsMassOK_FittedVtx += 1
                            if (t.is2DiMuonsIsoTkOK_FittedVtx):
                                m_events2DiMuonsIsoTkOK_FittedVtx += 1
                                if (t.isVertexOK):
                                    m_eventsVertexOK_FittedVtx += 1
                                    
                if (t.is2DiMuonsDzOK_ConsistentVtx):
                    m_events2DiMuonsDzOK_ConsistentVtx += 1
                    if (t.is2DiMuonsMassOK_ConsistentVtx):
                        m_events2DiMuonsMassOK_ConsistentVtx_noHLT += 1
                        if (t.is2DiMuonsIsoTkOK_ConsistentVtx):
                            m_events2DiMuonsIsoTkOK_ConsistentVtx_noHLT += 1
                            if (t.isVertexOK):
                                m_eventsVertexOK_ConsistentVtx_noHLT += 1
                    if (t.isDiMuonHLTFired):
                        m_eventsDiMuonHLTFired_ConsistentVtx += 1
                        if (t.is2DiMuonsMassOK_ConsistentVtx):
                            m_events2DiMuonsMassOK_ConsistentVtx += 1
                            if (t.is2DiMuonsIsoTkOK_ConsistentVtx):
                                m_events2DiMuonsIsoTkOK_ConsistentVtx += 1
                                if (t.isVertexOK):
                                    m_eventsVertexOK_ConsistentVtx += 1
                                    
    print "m_events", m_events
    print "m_isDiMuonHLTFired", m_isDiMuonHLTFired
    print "m_events4GenMu", m_events4GenMu
    print "m_events1GenMu17", m_events1GenMu17
    print "m_events2GenMu8", m_events2GenMu8
    print "m_events3GenMu8", m_events3GenMu8
    print "m_events4GenMu8", m_events4GenMu8
    print "m_events1SelMu17", m_events1SelMu17
    print "m_events2SelMu8", m_events2SelMu8
    print "m_events3SelMu8", m_events3SelMu8
    print "m_events4SelMu8", m_events4SelMu8

    print "m_events2MuJets", m_events2MuJets
    print "m_events2DiMuons", m_events2DiMuons

    print "m_events2DiMuonsDzOK_FittedVtx", m_events2DiMuonsDzOK_FittedVtx
#    print "m_events2DiMuonsDzOK_ConsistentVtx", m_events2DiMuonsDzOK_ConsistentVtx
    
    print "m_events2DiMuonsMassOK_FittedVtx_noHLT", m_events2DiMuonsMassOK_FittedVtx_noHLT
    print "m_events2DiMuonsIsoTkOK_FittedVtx_noHLT", m_events2DiMuonsIsoTkOK_FittedVtx_noHLT
    print "m_eventsVertexOK_FittedVtx_noHLT", m_eventsVertexOK_FittedVtx_noHLT
    print
    print "m_events2DiMuonsMassOK_FittedVtx", m_events2DiMuonsMassOK_FittedVtx
    print "m_events2DiMuonsIsoTkOK_FittedVtx", m_events2DiMuonsIsoTkOK_FittedVtx
    print "m_eventsVertexOK_FittedVtx", m_eventsVertexOK_FittedVtx
    print
##     print "m_events2DiMuonsMassOK_ConsistentVtx_noHLT", m_events2DiMuonsMassOK_ConsistentVtx_noHLT
##     print "m_events2DiMuonsIsoTkOK_ConsistentVtx_noHLT", m_events2DiMuonsIsoTkOK_ConsistentVtx_noHLT
##     print "m_eventsVertexOK_ConsistentVtx_noHLT", m_eventsVertexOK_ConsistentVtx_noHLT
##     print
##     print "m_events2DiMuonsMassOK_ConsistentVtx", m_events2DiMuonsMassOK_ConsistentVtx
##     print "m_events2DiMuonsIsoTkOK_ConsistentVtx", m_events2DiMuonsIsoTkOK_ConsistentVtx
##     print "m_eventsVertexOK_ConsistentVtx", m_eventsVertexOK_ConsistentVtx
    print
    print "Trigger efficiencies:"
    for p in hltPaths:
        print "\t", p, "Pass", hltPathPass[p], "Fail", hltPathFail[p], "Efficiency", hltPathPass[p]/m_eventsVertexOK_FittedVtx_noHLT
    
if __name__ == "__main__":
    analyzeHLT()
