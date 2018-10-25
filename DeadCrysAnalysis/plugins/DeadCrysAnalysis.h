#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Utilities/interface/EDGetToken.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/EcalRecHit/interface/EcalRecHitCollections.h"
#include "DataFormats/EgammaCandidates/interface/GsfElectron.h"
#include "DataFormats/EgammaCandidates/interface/GsfElectronFwd.h"
#include "DataFormats/EgammaCandidates/interface/Photon.h"
#include "DataFormats/EgammaCandidates/interface/PhotonFwd.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"


#include <vector>
#include <string>
#include <iostream>
#include <TH1I.h>
#include <TFile.h>
#include <TTree.h>
#include <TH2F.h>
#include <TH1F.h>

//
// class declaration
//


class DeadCrysAnalysis : public edm::one::EDAnalyzer<> {
   public:

  explicit DeadCrysAnalysis(const edm::ParameterSet&);
  ~DeadCrysAnalysis();


  virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
  virtual void endJob();
   private:
  float recHitEnergy(DetId id, const EcalRecHitCollection *recHits);

  int nEvents_;
  

  TFile *histfile_;
  TFile *histWeightFile_;
  TTree *tree_;
  TH1F *h_etrue_;
  TH1F *h_inverse_etrue_;

  edm::EDGetTokenT<reco::GsfElectronCollection> gsfElectrons_;
  edm::EDGetTokenT<reco::PhotonCollection> gedPhotons_;
  edm::EDGetTokenT<EcalRecHitCollection> rechits_EB_;

  bool storeLogE_;
  bool recHits_;
  double e3x3Cut_;
  double rhECut_;
  bool analyzeElectrons_;
  bool debug_;
  bool fillTreeForTraining_;
  bool usePhotons_;
  bool do5x5_;
  bool largestCentralCrystal_;
  int nPhotons_;
  std::string outputFileName_; 
  std::string inputHistoFileName_; 

  std::vector<float> E_;
  std::vector<float> eta_;
  std::vector<float> phi_;
  std::vector<float> iEta_;
  std::vector<float> iPhi_;
  float target_;
  float target_w_;
  int deadFlag_;

  int lumi; 
  int run;
  long evt;



};
