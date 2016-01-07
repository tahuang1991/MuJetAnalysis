import ROOT
from DataFormats.FWLite import Events, Handle


events = Events ('/eos/uscms/store/user/slava77/Neutrino_Pt2to20_gun/TTI2023Upg14D-PU140bx25-ILT_SLHC14/6a6577f18a9b70d924bea399af3ff625//2023TTIUpg14D_1000_1_IFv.root')

k = 0
handle  = Handle ('L1MuGMTReadoutCollection')
label = ("simGmtDigis")

for event in events:    
    k += 1
    event.getByLabel (label, handle)
    tttracks = handle.product()
    print tttracks
    for tttrack in tttracks:
        print tttrack.getMomentum().perp(), tttrack.getMomentum().eta(), tttrack.getMomentum().phi()

    print event
    if k>10:
        break
