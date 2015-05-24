void DarkSusy_mH_125_mGammaD_2000_cT_10_LHE_Higgs_pT()
{
//=========Macro generated from canvas: cnv/cnv
//=========  (Sun May 24 15:17:46 2015) by ROOT version6.02/05
   TCanvas *cnv = new TCanvas("cnv", "cnv",1,1,904,904);
   gStyle->SetOptFit(1);
   gStyle->SetOptStat(0);
   gStyle->SetOptTitle(0);
   cnv->SetHighLightColor(2);
   cnv->Range(-2.125,-0.17875,10.375,1.19625);
   cnv->SetFillColor(0);
   cnv->SetBorderMode(0);
   cnv->SetBorderSize(2);
   cnv->SetTickx(1);
   cnv->SetTicky(1);
   cnv->SetLeftMargin(0.17);
   cnv->SetRightMargin(0.03);
   cnv->SetTopMargin(0.07);
   cnv->SetBottomMargin(0.13);
   cnv->SetFrameFillStyle(0);
   cnv->SetFrameBorderMode(0);
   cnv->SetFrameFillStyle(0);
   cnv->SetFrameBorderMode(0);
   
   TH1F *h_higgs_pT_dummy3 = new TH1F("h_higgs_pT_dummy3","h_higgs_pT_dummy",10,0,10);
   h_higgs_pT_dummy3->SetMaximum(1.1);
   h_higgs_pT_dummy3->SetLineStyle(0);
   h_higgs_pT_dummy3->SetMarkerStyle(20);
   h_higgs_pT_dummy3->GetXaxis()->SetTitle("p_{T} of h [GeV]");
   h_higgs_pT_dummy3->GetXaxis()->SetLabelFont(42);
   h_higgs_pT_dummy3->GetXaxis()->SetLabelOffset(0.007);
   h_higgs_pT_dummy3->GetXaxis()->SetTitleSize(0.06);
   h_higgs_pT_dummy3->GetXaxis()->SetTitleOffset(0.95);
   h_higgs_pT_dummy3->GetXaxis()->SetTitleFont(42);
   h_higgs_pT_dummy3->GetYaxis()->SetTitle("Fraction of events / 1 GeV");
   h_higgs_pT_dummy3->GetYaxis()->SetLabelFont(42);
   h_higgs_pT_dummy3->GetYaxis()->SetLabelOffset(0.007);
   h_higgs_pT_dummy3->GetYaxis()->SetTitleSize(0.06);
   h_higgs_pT_dummy3->GetYaxis()->SetTitleOffset(1.35);
   h_higgs_pT_dummy3->GetYaxis()->SetTitleFont(42);
   h_higgs_pT_dummy3->GetZaxis()->SetLabelFont(42);
   h_higgs_pT_dummy3->GetZaxis()->SetLabelOffset(0.007);
   h_higgs_pT_dummy3->GetZaxis()->SetTitleSize(0.06);
   h_higgs_pT_dummy3->GetZaxis()->SetTitleFont(42);
   h_higgs_pT_dummy3->Draw("");
   
   TH1F *h_higgs_pT4 = new TH1F("h_higgs_pT4","h_higgs_pT",10,0,10);
   h_higgs_pT4->SetBinContent(1,1);
   h_higgs_pT4->SetBinError(1,0.003535556);
   h_higgs_pT4->SetEntries(79999);
   h_higgs_pT4->SetDirectory(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#0000ff");
   h_higgs_pT4->SetLineColor(ci);
   h_higgs_pT4->SetLineWidth(2);
   h_higgs_pT4->SetMarkerStyle(20);
   h_higgs_pT4->GetXaxis()->SetLabelFont(42);
   h_higgs_pT4->GetXaxis()->SetLabelOffset(0.007);
   h_higgs_pT4->GetXaxis()->SetTitleSize(0.06);
   h_higgs_pT4->GetXaxis()->SetTitleOffset(0.95);
   h_higgs_pT4->GetXaxis()->SetTitleFont(42);
   h_higgs_pT4->GetYaxis()->SetLabelFont(42);
   h_higgs_pT4->GetYaxis()->SetLabelOffset(0.007);
   h_higgs_pT4->GetYaxis()->SetTitleSize(0.06);
   h_higgs_pT4->GetYaxis()->SetTitleOffset(1.3);
   h_higgs_pT4->GetYaxis()->SetTitleFont(42);
   h_higgs_pT4->GetZaxis()->SetLabelFont(42);
   h_higgs_pT4->GetZaxis()->SetLabelOffset(0.007);
   h_higgs_pT4->GetZaxis()->SetTitleSize(0.06);
   h_higgs_pT4->GetZaxis()->SetTitleFont(42);
   h_higgs_pT4->Draw("SAMEHIST");
   
   TLegend *leg = new TLegend(0.4566667,0.82,0.7822222,0.9066667,NULL,"brNDC");
   leg->SetBorderSize(0);
   leg->SetTextSize(0.02777778);
   leg->SetLineColor(1);
   leg->SetLineStyle(1);
   leg->SetLineWidth(1);
   leg->SetFillColor(0);
   leg->SetFillStyle(0);
   TLegendEntry *entry=leg->AddEntry("NULL","#splitline{pp #rightarrow h #rightarrow 2n_{1} #rightarrow 2n_{D} + 2 #gamma_{D} #rightarrow 2n_{D} + 4#mu}{#splitline{m_{h} = 125 GeV, m_{n_{1}} = 50 GeV, m_{n_{D}} = 1 GeV}{m_{#gamma_{D}} = 20 GeV, c#tau_{#gamma_{D}} = 10 mm}}","h");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   leg->Draw();
   
   leg = new TLegend(0.17,0.935,0.97,1,NULL,"brNDC");
   leg->SetBorderSize(0);
   leg->SetTextAlign(22);
   leg->SetTextSize(0.045);
   leg->SetLineColor(1);
   leg->SetLineStyle(1);
   leg->SetLineWidth(1);
   leg->SetFillColor(0);
   leg->SetFillStyle(0);
   entry=leg->AddEntry("NULL","CMS Simulation (LHE) 14 TeV","h");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   leg->Draw();
   cnv->Modified();
   cnv->cd();
   cnv->SetSelected(cnv);
}
