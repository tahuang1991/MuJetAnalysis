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

    m_events2DiMuonsMassOK_FittedVtx_noHLT = 0
    m_events2DiMuonsMassOK_ConsistentVtx_noHLT = 0
    
    m_events2DiMuonsIsoTkOK_FittedVtx_noHLT = 0
    m_events2DiMuonsIsoTkOK_ConsistentVtx_noHLT = 0

    m_eventsVertexOK_FittedVtx_noHLT = 0
    m_eventsVertexOK_ConsistentVtx_noHLT = 0

    m_eventsDiMuonHLTFired_FittedVtx = 0
    m_eventsDiMuonHLTFired_ConsistentVtx = 0
    
    m_events2DiMuonsDzOK_FittedVtx = 0
    m_events2DiMuonsDzOK_ConsistentVtx = 0

    m_events2DiMuonsMassOK_FittedVtx = 0
    m_events2DiMuonsMassOK_ConsistentVtx = 0
    
    m_events2DiMuonsIsoTkOK_FittedVtx = 0
    m_events2DiMuonsIsoTkOK_ConsistentVtx = 0

    m_eventsVertexOK_FittedVtx = 0
    m_eventsVertexOK_ConsistentVtx = 0

    """
    m_eventsVertexOK_FittedVtx = 0
    m_eventsVertexOK_ConsistentVtx = 0
    
    m_events2DiMuonsLxyOK_FittedVtx = 0
    m_events2DiMuonsLxyOK_ConsistentVtx = 0
    
    b_is2DiMuonsMassOK_FittedVtx = 0  
    b_is2DiMuonsMassOK_ConsistentVtx = 0
    
    b_is2DiMuonsIsoTkOK_FittedVtx = 0   
    b_is2DiMuonsIsoTkOK_ConsistentVtx = 0
    """
    
    b_isVertexOK   
   
    
    
    m_events2DiMuonMassOk_FittedVtx_noHLT = 0
    m_events2DiMuonMassOk_ConsistentVtx_noHLT = 0
    m_events2DiMuonIsoTkOk_FittedVtx_noHLT = 0
    m_events2DiMuonIsoTkOk_ConsistentVtx_noHLT = 0

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
                    if (t.is2DiMuonsMassOK_FittedVtx_noHLT):
                        m_events2DiMuonsMassOK_FittedVtx_noHLT += 1
                        if (t.is2DiMuonsIsoTkOK_FittedVtx_noHLT):
                            m_events2DiMuonsIsoTkOK_FittedVtx_noHLT += 1
                            if (t.isVertexOK_noHLT):
                                m_eventsVertexOK_FittedVtx_noHLT += 1
                    if (t.isDiMuonHLTFired_FittedVtx):
                        m_eventsDiMuonHLTFired_FittedVtx += 1
                        if (t.is2DiMuonsMassOK_FittedVtx):
                            m_events2DiMuonsMassOK_FittedVtx += 1
                            if (t.is2DiMuonsIsoTkOK_FittedVtx):
                                m_events2DiMuonsIsoTkOK_FittedVtx += 1
                                if (t.isVertexOK):
                                    m_eventsVertexOK_FittedVtx += 1
                                    
                if (t.is2DiMuonsDzOK_ConsistentVtx):
                    m_events2DiMuonsDzOK_ConsistentVtx += 1
                    if (t.is2DiMuonsMassOK_ConsistentVtx_noHLT):
                        m_events2DiMuonsMassOK_ConsistentVtx_noHLT += 1
                        if (t.is2DiMuonsIsoTkOK_ConsistentVtx_noHLT):
                            m_events2DiMuonsIsoTkOK_ConsistentVtx_noHLT += 1
                            if (t.isVertexOK_noHLT):
                                m_eventsVertexOK_ConsistentVtx_noHLT += 1
                    if (t.isDiMuonHLTFired_ConsistentVtx):
                        m_eventsDiMuonHLTFired_ConsistentVtx += 1
                        if (t.is2DiMuonsMassOK_ConsistentVtx):
                            m_events2DiMuonsMassOK_ConsistentVtx += 1
                            if (t.is2DiMuonsIsoTkOK_ConsistentVtx):
                                m_events2DiMuonsIsoTkOK_ConsistentVtx += 1
                                if (t.isVertexOK):
                                    m_eventsVertexOK_ConsistentVtx += 1
                                    
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

    print "m_events2DiMuonsDzOK_FittedVtx_noHLT", m_events2DiMuonsDzOK_FittedVtx_noHLT
    print "m_events2DiMuonsMassOK_FittedVtx_noHLT", m_events2DiMuonsMassOK_FittedVtx_noHLT
    print "m_events2DiMuonsIsoTkOK_FittedVtx_noHLT", m_events2DiMuonsIsoTkOK_FittedVtx_noHLT
    print "m_eventsVertexOK_FittedVtx_noHLT", m_eventsVertexOK_FittedVtx_noHLT
    
    print "m_events2DiMuonsDzOK_FittedVtx", m_events2DiMuonsDzOK_FittedVtx
    print "m_events2DiMuonsMassOK_FittedVtx", m_events2DiMuonsMassOK_FittedVtx
    print "m_events2DiMuonsIsoTkOK_FittedVtx", m_events2DiMuonsIsoTkOK_FittedVtx
    print "m_eventsVertexOK_FittedVtx", m_eventsVertexOK_FittedVtx

    print "m_events2DiMuonsDzOK_ConsistentVtx_noHLT", m_events2DiMuonsDzOK_ConsistentVtx_noHLT
    print "m_events2DiMuonsMassOK_ConsistentVtx_noHLT", m_events2DiMuonsMassOK_ConsistentVtx_noHLT
    print "m_events2DiMuonsIsoTkOK_ConsistentVtx_noHLT", m_events2DiMuonsIsoTkOK_ConsistentVtx_noHLT
    print "m_eventsVertexOK_ConsistentVtx_noHLT", m_eventsVertexOK_ConsistentVtx_noHLT
    
    print "m_events2DiMuonsDzOK_ConsistentVtx", m_events2DiMuonsDzOK_ConsistentVtx
    print "m_events2DiMuonsMassOK_ConsistentVtx", m_events2DiMuonsMassOK_ConsistentVtx
    print "m_events2DiMuonsIsoTkOK_ConsistentVtx", m_events2DiMuonsIsoTkOK_ConsistentVtx
    print "m_eventsVertexOK_ConsistentVtx", m_eventsVertexOK_ConsistentVtx
    
if __name__ == "__main__":
    analyzeHLT()
