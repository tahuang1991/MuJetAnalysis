class Plotter:
    def __init__(self):
        self.inputDir = inputDir
        self.inputFile = lowMassInput[index]
        self.outputDir = lowMassOutput[index]
        self.ext = lowMassExt[index] + ext
        self.analyzer = "HLTBendingAngle"
        self.events = "Events"
        self.file = TFile.Open(self.inputFile)
        self.dirAna = (self.file).Get(self.analyzer)
        self.tree = (self.dirAna).Get(self.events)            
        self.symb = "#gamma_{D}"
        self.ctau = "c#tau(" + self.symb + ") = %d mm"%(lowMassCtau[index])
        self.mass = 'm(' + self.symb + ') = 0.4 GeV'
        self.boson = "photon"
        self.pu = lowMassPU[index]
        self.debug = False
        
