#include "MuJetAnalysis/DataFormats/interface/MultiElectron.h"

#ifndef MULTILEPTONCANDIDATE_FOR_FWLITE
#include "TrackingTools/TransientTrack/interface/TransientTrackBuilder.h"
#include "TrackingTools/TransientTrack/interface/TransientTrack.h"
#include "RecoVertex/KalmanVertexFit/interface/KalmanVertexFitter.h"
#else
class TransientTrackBuilder {};
#endif // MULTILEPTONCANDIDATE_FOR_FWLITE

/// default constructor
pat::MultiElectron::MultiElectron( std::vector<const pat::Electron*> &electrons,
                          const TransientTrackBuilder    *transientTrackBuilder,
                          const reco::TrackCollection    *tracks,
                          const pat::ElectronCollection      *allelectrons,
                          const CaloTowerCollection      *caloTowers,
                          double centralTrackIsolationCone,
                          double unionTrackIsolationCone,
                          double centralTrackThresholdPt,
                          double unionTrackThresholdPt,
                          double centralCaloIsolationCone,
                          double unionCaloIsolationCone,
                          double centralNumberAboveThresholdCone,
                          double unionNumberAboveThresholdCone,
                          double centralNumberAboveThresholdPt,
                          double unionNumberAboveThresholdPt)
{
  pat::CompositeCandidate();

  int charge = 0;
  LorentzVector lorentzVector;
  
  for (std::vector<const pat::Electron*>::const_iterator electron = electrons.begin();  electron != electrons.end();  ++electron) {
    addDaughter(**electron);
    charge += (*electron)->charge();
    lorentzVector += (*electron)->p4();
  }
  
  setCharge(charge);
  setP4( PolarLorentzVector(lorentzVector.pt(),lorentzVector.eta(),lorentzVector.phi(),lorentzVector.mass()));

  std::map<const reco::Candidate*,unsigned int> ancestorCounter;
  for (std::vector<const pat::Electron*>::const_iterator electron = electrons.begin();  electron != electrons.end();  ++electron) {
    const reco::GenParticle *genParticle = (*electron)->genParticle();
    if (genParticle != NULL) {
      const reco::Candidate *mother = genParticle->mother();
      while (mother != NULL) {
	      if (ancestorCounter.find(mother) == ancestorCounter.end()) {
	        ancestorCounter[mother] = 0;
	      }
	      ancestorCounter[mother]++;
	      mother = mother->mother();
	    }
    }
  }

  const reco::Candidate *youngestCommonAncestor = NULL;
  unsigned int maxDepth = 0;
  for (std::map<const reco::Candidate*,unsigned int>::const_iterator ancestor = ancestorCounter.begin();  ancestor != ancestorCounter.end();  ++ancestor) {
    if (ancestor->second == numberOfDaughters()) {
      unsigned int depth = 0;
      for (const reco::Candidate *mother = ancestor->first;  mother != NULL;  mother = mother->mother()) {
        depth++;
      }
      if (depth > maxDepth) {
        maxDepth = depth;
	      youngestCommonAncestor = ancestor->first;
      }
    }
  }

  if (youngestCommonAncestor != NULL) {
    const reco::GenParticle *asGenParticle = dynamic_cast<const reco::GenParticle*>(youngestCommonAncestor);
    setGenParticle(*asGenParticle);
  }

// Fitted vertex
  m_vertexValid = false;
  m_chi2 = 0.;
  m_ndof = 0.;
  if (transientTrackBuilder != NULL) {
    calculateVertex(transientTrackBuilder);
  }

// Consistent vertex
  m_consistentVtxValid = false;
  
  m_centralTrackIsolationCone = 0.;
  m_unionTrackIsolationCone   = 0.;
  m_centralTrackThresholdPt   = 0.;
  m_unionTrackThresholdPt     = 0.;
  m_centralTrackIsolation     = 0.;
  m_unionTrackIsolation       = 0.;
  if (tracks != NULL) {
    calculateTrackIsolation(tracks, allelectrons, centralTrackIsolationCone, unionTrackIsolationCone, centralTrackThresholdPt, unionTrackThresholdPt);
  }

  m_centralCaloIsolationCone = 0.;
  m_unionCaloIsolationCone   = 0.;
  m_centralECALIsolation     = 0.;
  m_unionECALIsolation       = 0.;
  m_centralHCALIsolation     = 0.;
  m_unionHCALIsolation       = 0.;
  if (caloTowers != NULL) {
    calculateCaloIsolation(caloTowers, centralCaloIsolationCone, unionCaloIsolationCone);
  }

  m_centralNumberAboveThresholdCone = 0.;
  m_unionNumberAboveThresholdCone = 0.;
  m_centralNumberAboveThresholdPt = 0.;
  m_unionNumberAboveThresholdPt = 0.;
  m_centralNumberAboveThreshold = 0;
  m_unionNumberAboveThreshold = 0;
  if (tracks != NULL) {
    calculateNumberAboveThresholdIsolation(tracks, allelectrons, centralNumberAboveThresholdCone, unionNumberAboveThresholdCone,
					   centralNumberAboveThresholdPt, unionNumberAboveThresholdPt);
  }
}

/// constructor from MultiElectronType
pat::MultiElectron::MultiElectron(const pat::MultiElectron &aMultiElectron) : 
  pat::MultiLepton<Electron>(aMultiElectron) 
{
}

/// destructor
pat::MultiElectron::~MultiElectron() 
{
}

/// calculate the vertex from TransientTracks; return true if successful
bool pat::MultiElectron::calculateVertex(const TransientTrackBuilder *transientTrackBuilder) 
{
#ifdef MULTILEPTONCANDIDATE_FOR_FWLITE
  return false;
#endif // MULTILEPTONCANDIDATE_FOR_FWLITE
#ifndef MULTILEPTONCANDIDATE_FOR_FWLITE
  
  std::vector<reco::TransientTrack> tracksToVertex;
  for (unsigned int i = 0;  i < numberOfDaughters();  i++) {
    if (electron(i) == NULL) {
      throw cms::Exception("MultiElectron") << "MultiElectrons should only contain pat::Electrons";
    }
    if (electron(i)->closestTrack().isAvailable()) {
      tracksToVertex.push_back(transientTrackBuilder->build(electron(i)->closestTrack()));
    }
  }

  if (tracksToVertex.size() < 2) return false;

  KalmanVertexFitter vertexFitter;
  CachingVertex<5> fittedVertex = vertexFitter.vertex(tracksToVertex);

  if (!fittedVertex.isValid()  ||  fittedVertex.totalChiSquared() < 0.) return false;

  m_vertexValid = true;
  m_chi2 = fittedVertex.totalChiSquared();
  m_ndof = fittedVertex.degreesOfFreedom();

  setVertex(Point(fittedVertex.position().x(), fittedVertex.position().y(), fittedVertex.position().z()));

//   double covarianceMatrixArray[6] = {fittedVertex.error().cxx(), fittedVertex.error().cyy(), fittedVertex.error().czz(), fittedVertex.error().cyx(), fittedVertex.error().czx(), fittedVertex.error().czy()};
  double covarianceMatrixArray[6] = {fittedVertex.error().cxx(), fittedVertex.error().cyx(), fittedVertex.error().cyy(), fittedVertex.error().czx(), fittedVertex.error().czy(), fittedVertex.error().czz() }; // YP: FIXME! Check if this definition is correct
  m_covarianceMatrix = CovarianceMatrix(covarianceMatrixArray, 6);

  m_vertexPCA.clear();
  m_vertexPCACovarianceMatrix.clear();
  m_vertexP4.clear();
  for (unsigned int i = 0;  i < numberOfDaughters();  i++) {
    TrajectoryStateClosestToPoint TSCTP = tracksToVertex[i].trajectoryStateClosestToPoint(vertexPoint());

    m_vertexPCA.push_back(TSCTP.position());

    GlobalError error = TSCTP.theState().cartesianError().position();    
//    double covarianceMatrixArray2[6] = {error.cxx(), error.cyy(), error.czz(), error.cyx(), error.czx(), error.czy()};
    double covarianceMatrixArray2[6] = {error.cxx(), error.cyx(), error.cyy(), error.czx(), error.czy(), error.czz()}; // YP: FIXME! Check if this definition is correct
    CovarianceMatrix covarianceMatrix2 = CovarianceMatrix(covarianceMatrixArray2, 6);
    m_vertexPCACovarianceMatrix.push_back(covarianceMatrix2);

    GlobalVector momentum = TSCTP.momentum();
    m_vertexP4.push_back( LorentzVector( momentum.x(), momentum.y(), momentum.z(), sqrt( momentum.mag2() + daughter(i)->mass()*daughter(i)->mass() ) ) );
  }
  
   return true;
#endif // MULTILEPTONCANDIDATE_FOR_FWLITE
}


// Calorimeter Isolation
void pat::MultiElectron::calculateCaloIsolation(const CaloTowerCollection *caloTowers, double centralCone, double unionCone)
{
  m_centralCaloIsolationCone = centralCone;
  m_unionCaloIsolationCone   = unionCone;
  m_centralECALIsolation     = 0.;
  m_unionECALIsolation       = 0.;
  m_centralHCALIsolation     = 0.;
  m_unionHCALIsolation       = 0.;

  for (CaloTowerCollection::const_iterator caloTower = caloTowers->begin();  caloTower != caloTowers->end();  ++caloTower) {
    // what are the corresponding values for electrons???

    // just the "TowersBlock" and the "Towers" else block
    const double theThreshold_E  = 0.2;
    const double theThreshold_H  = 0.5;
    const double theThreshold_HO = 0.5;

    double ECALcontribution = 0.;
    double HCALcontribution = 0.;

    double etecal = caloTower->emEt();
    double eecal  = caloTower->emEnergy();
    if (etecal > theThreshold_E  &&  eecal > 3.*noiseEcal(*caloTower)) {
      ECALcontribution += etecal;
    }
    double ethcal = caloTower->hadEt();
    double ehcal  = caloTower->hadEnergy();
    if (ethcal > theThreshold_H  &&  ehcal > 3.*noiseHcal(*caloTower)) {
      HCALcontribution += ethcal;
    }
    double ethocal = caloTower->outerEt();
    double ehocal  = caloTower->outerEnergy();
    if (ethocal > theThreshold_HO  &&  ehocal > 3.*noiseHOcal(*caloTower)) {
      HCALcontribution += ethocal;
    }

    bool inUnionCone = false;
    for (unsigned int i = 0;  i < numberOfDaughters();  i++) {
      double dphi = daughter(i)->phi() - caloTower->phi();
      while (dphi > M_PI) dphi -= 2.*M_PI;
      while (dphi < -M_PI) dphi += 2.*M_PI;
      double deta = daughter(i)->eta() - caloTower->eta();
      double dR = sqrt(pow(dphi, 2) + pow(deta, 2));
      if (dR < unionCone) {
        inUnionCone = true;
        break;
      }
    }
    if (inUnionCone) {
      m_unionECALIsolation += ECALcontribution;
      m_unionHCALIsolation += HCALcontribution;
    }

    double dphi = phi() - caloTower->phi();
    while (dphi > M_PI) dphi -= 2.*M_PI;
    while (dphi < -M_PI) dphi += 2.*M_PI;
    double deta = eta() - caloTower->eta();
    double dR = sqrt(pow(dphi, 2) + pow(deta, 2));
    if (dR < centralCone) {
      m_centralECALIsolation += ECALcontribution;
      m_centralHCALIsolation += HCALcontribution;
    }
  }
}

// calculate isolation (performed by constructor if tracks, leptons, and caloTowers != NULL)
// Track Isolation
void pat::MultiElectron::calculateTrackIsolation(const reco::TrackCollection *tracks,
						 const pat::ElectronCollection   *allelectrons,
						 double centralCone,
						 double unionCone,
						 double centralThreshold,
						 double unionThreshold,
						 TTree   *diagnosticTTree,
						 Float_t *diagnosticdR,
						 Float_t *diagnosticpT) 
{
  m_centralTrackIsolationCone = centralCone;
  m_unionTrackIsolationCone   = unionCone;
  m_centralTrackThresholdPt   = centralThreshold;
  m_unionTrackThresholdPt     = unionThreshold;
  m_centralTrackIsolation     = 0.;
  m_unionTrackIsolation       = 0.;

  std::vector<const reco::Track*> nonElectrons;
  for (reco::TrackCollection::const_iterator track = tracks->begin();  track != tracks->end();  ++track) {
    bool matchesElectron = false;
    
    for (unsigned int i = 0;  i < numberOfDaughters();  i++) {
      const pat::Electron *electron = dynamic_cast<const pat::Electron*>(daughter(i));
      if (electron->closestTrack().isAvailable()  &&  sameTrack(&*track, &*(electron->closestTrack()))) {
        matchesElectron = true;
        break;
      }
    }
    
    for (pat::ElectronCollection::const_iterator electron = allelectrons->begin();  electron != allelectrons->end();  ++electron) {
      if (electron->closestTrack().isAvailable()  &&  sameTrack(&*track, &*(electron->closestTrack()))) {
        matchesElectron = true;
        break;
      }
    }
    
    if (!matchesElectron) nonElectrons.push_back(&*track);
  }

  for (std::vector<const reco::Track*>::const_iterator nonElectron = nonElectrons.begin();  nonElectron != nonElectrons.end();  ++nonElectron) {
    bool inUnionCone = false;
    
    for (unsigned int i = 0;  i < numberOfDaughters();  i++) {
      double dphi = daughter(i)->phi() - (*nonElectron)->phi();
      while (dphi > M_PI)  dphi -= 2.*M_PI;
      while (dphi < -M_PI) dphi += 2.*M_PI;
      double deta = daughter(i)->eta() - (*nonElectron)->eta();
      double dR = sqrt(pow(dphi, 2) + pow(deta, 2));
      if (dR < unionCone) {
        inUnionCone = true;
        break;
      }
    }
    
    if (inUnionCone  &&  (*nonElectron)->pt() > m_unionTrackThresholdPt) {
      m_unionTrackIsolation += (*nonElectron)->pt();
    }

    double dphi = phi() - (*nonElectron)->phi();
    while (dphi > M_PI) dphi -= 2.*M_PI;
    while (dphi < -M_PI) dphi += 2.*M_PI;
    double deta = eta() - (*nonElectron)->eta();
    double dR = sqrt(pow(dphi, 2) + pow(deta, 2));
    if (dR < centralCone  &&  (*nonElectron)->pt() > m_centralTrackThresholdPt) {
      m_centralTrackIsolation += (*nonElectron)->pt();
    }

    if (diagnosticTTree != NULL  &&  dR < 0.5) {
      *diagnosticdR = dR;
      *diagnosticpT = (*nonElectron)->pt();
      diagnosticTTree->Fill();
    }
  }
}

void pat::MultiElectron::calculateNumberAboveThresholdIsolation(const reco::TrackCollection *tracks,
								const pat::ElectronCollection *allelectrons,
								double centralCone,
								double unionCone,
								double centralThreshold,
								double unionThreshold,
								TTree *diagnosticTTree,
								Float_t *diagnosticdR,
								Float_t *diagnosticpT) 
{
  m_centralNumberAboveThresholdCone = centralCone;
  m_unionNumberAboveThresholdCone   = unionCone;
  m_centralNumberAboveThresholdPt   = centralThreshold;
  m_unionNumberAboveThresholdPt     = unionThreshold;
  m_centralNumberAboveThreshold     = 0;
  m_unionNumberAboveThreshold       = 0;

  std::vector<const reco::Track*> nonElectrons;
  for (reco::TrackCollection::const_iterator track = tracks->begin();  track != tracks->end();  ++track) {
    bool matchesElectron = false;
    
    for (unsigned int i = 0;  i < numberOfDaughters();  i++) {
      const pat::Electron *electron = dynamic_cast<const pat::Electron*>(daughter(i));
      if (electron->closestTrack().isAvailable()  &&  sameTrack(&*track, &*(electron->closestTrack()))) {
        matchesElectron = true;
        break;
      }
    }
    
    for (pat::ElectronCollection::const_iterator electron = allelectrons->begin();  electron != allelectrons->end();  ++electron) {
      if (electron->closestTrack().isAvailable()  &&  sameTrack(&*track, &*(electron->closestTrack()))) {
        matchesElectron = true;
        break;
      }
    }
    
    if (!matchesElectron) nonElectrons.push_back(&*track);
  }

  for (std::vector<const reco::Track*>::const_iterator nonElectron = nonElectrons.begin();  nonElectron != nonElectrons.end();  ++nonElectron) {
    if ((*nonElectron)->pt() > unionThreshold) {
      bool inUnionCone = false;
      for (unsigned int i = 0;  i < numberOfDaughters();  i++) {
        double dphi = daughter(i)->phi() - (*nonElectron)->phi();
        while (dphi > M_PI) dphi -= 2.*M_PI;
        while (dphi < -M_PI) dphi += 2.*M_PI;
        double deta = daughter(i)->eta() - (*nonElectron)->eta();
        double dR = sqrt(pow(dphi, 2) + pow(deta, 2));
        if (dR < unionCone) {
          inUnionCone = true;
          break;
        }
      }
      if (inUnionCone) {
        m_unionNumberAboveThreshold++;
      }
    }

    double dphi = phi() - (*nonElectron)->phi();
    while (dphi > M_PI) dphi -= 2.*M_PI;
    while (dphi < -M_PI) dphi += 2.*M_PI;
    double deta = eta() - (*nonElectron)->eta();
    double dR = sqrt(pow(dphi, 2) + pow(deta, 2));
    if (dR < centralCone  &&  (*nonElectron)->pt() > centralThreshold) {
      m_centralNumberAboveThreshold++;
    }

    if (diagnosticTTree != NULL  &&  dR < 0.5) {
      *diagnosticdR = dR;
      *diagnosticpT = (*nonElectron)->pt();
      diagnosticTTree->Fill();
    }
  }
}

pat::MultiElectron pat::MultiElectron::merge( const pat::MultiElectron &aMultiElectron,
                                      const TransientTrackBuilder *transientTrackBuilder,
                                      const reco::TrackCollection *tracks,
                                      const pat::ElectronCollection *allelectrons,
                                      const CaloTowerCollection *caloTowers,
                                      double centralTrackIsolationCone,
                                      double unionTrackIsolationCone,
                                      double centralTrackThresholdPt,
                                      double unionTrackThresholdPt,
                                      double centralCaloIsolationCone,
                                      double unionCaloIsolationCone,
                                      double centralNumberAboveThresholdCone,
                                      double unionNumberAboveThresholdCone,
                                      double centralNumberAboveThresholdPt,
                                      double unionNumberAboveThresholdPt) {
  
  std::vector<const pat::Electron*> electrons;
  for (unsigned int i = 0;  i < numberOfDaughters();  i++) {
    electrons.push_back(electron(i));
  }

  for (unsigned int j = 0;  j < aMultiElectron.numberOfDaughters();  j++) {
    const pat::Electron *daughter_j = aMultiElectron.electron(j);

    bool same = false;
    for (unsigned int i = 0;  i < numberOfDaughters();  i++) {
      const pat::Electron *daughter_i = electron(i);

      if (daughter_i->closestTrack().isAvailable()  &&  daughter_j->closestTrack().isAvailable()) {
        if (sameTrack(&*(daughter_i->closestTrack()), &*(daughter_j->closestTrack()))) {
          same = true;
          break;
        }
      }
    }

    if (!same) electrons.push_back(daughter_j);
  }
  return pat::MultiElectron(electrons, transientTrackBuilder, tracks, allelectrons, caloTowers, 
			    centralTrackIsolationCone, unionTrackIsolationCone, centralTrackThresholdPt, 
			    unionTrackThresholdPt, centralCaloIsolationCone, unionCaloIsolationCone, 
			    centralNumberAboveThresholdCone, unionNumberAboveThresholdCone, centralNumberAboveThresholdPt, unionNumberAboveThresholdPt);
}

double pat::MultiElectron::vertexDz(const Point& myBeamSpot) const
{
   if (vertexValid()) {
     GlobalPoint  v      = vertexPoint();
     GlobalVector p      = vertexMomentum();
     double      pt_mag = sqrt( p.x()*p.x() + p.y()*p.y() );
     return (v.z()-myBeamSpot.z()) - ((v.x()-myBeamSpot.x())*p.x()+(v.y()-myBeamSpot.y())*p.y())/pt_mag * p.z()/pt_mag;
   }
   else return electron(0)->closestTrack()->dz(myBeamSpot);
  return 0;
}


double pat::MultiElectron::noiseEcal(const CaloTower &tower) const {
  const double theNoiseTow_EB = 0.04;
  const double theNoiseTow_EE = 0.15;
  return (fabs(tower.eta()) > 1.479 ? theNoiseTow_EE : theNoiseTow_EB);
}

double pat::MultiElectron::noiseHcal(const CaloTower &tower) const {
  const double theNoise_HB = 0.2;
  const double theNoise_HE = 0.2;
  return (fabs(tower.eta()) > 1.479 ? theNoise_HE : theNoise_HB);
}

double pat::MultiElectron::noiseHOcal(const CaloTower &tower) const {
  const double theNoise_HO = 0.2;
  return theNoise_HO;
}

bool pat::MultiElectron::overlaps(const pat::MultiElectron &aMultiElectron) const 
{
  for (unsigned int i = 0;  i < numberOfDaughters();  i++) {
    const pat::Electron *daughter_i = electron(i);
	
    for (unsigned int j = 0;  j < aMultiElectron.numberOfDaughters();  j++) {
      const pat::Electron *daughter_j = aMultiElectron.electron(j);
      
      if (daughter_i->closestTrack().isAvailable()  &&  daughter_j->closestTrack().isAvailable()) {
	if (sameTrack(&*(daughter_i->closestTrack()), &*(daughter_j->closestTrack()))) return true;
      }
    }
  }
  return false;      
}

bool pat::MultiElectron::contains(const pat::Electron &aElectron) const 
{
  for (unsigned int i = 0;  i < numberOfDaughters();  i++) {
    const pat::Electron *daughter_i = electron(i);
    
    if (daughter_i->closestTrack().isAvailable()  &&  aElectron.closestTrack().isAvailable()) {
      if (sameTrack(&*(daughter_i->closestTrack()), &*(aElectron.closestTrack()))) return true;
    }
  }
  return false;
}
