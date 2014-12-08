from ROOT import *

def analyzeHLT():
    f = TFile.Open("/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctauExp_0_8TeV_madgraph452_bridge224_LHE_pythia6_RAW/DarkSUSY_mH_125_mGammaD_0400_ctauExp_0_8TeV_madgraph452_bridge224_LHE_pythia6_ANA/d37f287c329e62f6cda917e97d6b627b/out_cutana_1_2_1Aa.root")
    f.cd("cutFlowAnalyzer")      
    f.ls()

    t = f.Get("cutFlowAnalyzer/Events");
    
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
    
    m_eventsMassDiMuonsOKnoHLT = 0
    m_eventsIsoDiMuonsOKnoHLT = 0
    m_eventsVertexOKnoHLT = 0
    
    m_eventsDiMuonsHLTFired = 0
    
    m_eventsMassDiMuonsOK = 0
    m_eventsIsoDiMuonsOK = 0
    m_eventsVertexOK = 0

    for k in range(0,nentries):
        t.GetEntry(k)    
        m_events += 1
            
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
                ## use consistent vtx fit for dz cut
                if (t.is2DiMuonsDzOK_ConsistentVtx):                    
                    m_events2DiMuonsDzOK_ConsistentVtx += 1
                    ## without HLT
                    if (t.isMassDiMuonsOK):
                        m_eventsMassDiMuonsOKnoHLT += 1
                        if (t.isIsoDiMuonsOK):
                            m_eventsIsoDiMuonsOKnoHLT += 1
                            if (t.isVertexOK):
                                m_eventsVertexOKnoHLT += 1
                    ## with HLT
                    if (t.isDiMuonsHLTFired):
                        m_eventsDiMuonsHLTFired += 1
                        if (t.isMassDiMuonsOK):
                            m_eventsMassDiMuonsOK += 1
                            if (t.isIsoDiMuonsOK):
                                m_eventsIsoDiMuonsOK += 1
                                if (t.isVertexOK):
                                    m_eventsVertexOK  += 1
            
    print "m_events", m_events
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
    
    print "m_eventsDz2DiMuonsOK_FittedVtx", m_events2DiMuonsDzOK_FittedVtx
    print "m_eventsDz2DiMuonsOK_ConsistentVtx", m_events2DiMuonsDzOK_ConsistentVtx

    print "m_eventsMassDiMuonsOKnoHLT", m_eventsMassDiMuonsOKnoHLT
    print "m_eventsIsoDiMuonsOKnoHLT", m_eventsIsoDiMuonsOKnoHLT
    print "m_eventsVertexOKnoHLT", m_eventsVertexOKnoHLT
    
    print "m_eventsDiMuonsHLTFired", m_eventsDiMuonsHLTFired

    print "m_eventsMassDiMuonsOK", m_eventsMassDiMuonsOK
    print "m_eventsIsoDiMuonsOK", m_eventsIsoDiMuonsOK
    print "m_eventsVertexOK", m_eventsVertexOK
    
if __name__ == "__main__":
    analyzeHLT()
