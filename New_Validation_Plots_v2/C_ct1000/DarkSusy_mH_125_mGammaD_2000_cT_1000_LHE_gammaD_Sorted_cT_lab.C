void DarkSusy_mH_125_mGammaD_2000_cT_1000_LHE_gammaD_Sorted_cT_lab()
{
//=========Macro generated from canvas: cnv/cnv
//=========  (Sun May 24 15:19:01 2015) by ROOT version6.02/05
   TCanvas *cnv = new TCanvas("cnv", "cnv",1,1,904,904);
   gStyle->SetOptFit(1);
   gStyle->SetOptStat(0);
   gStyle->SetOptTitle(0);
   cnv->SetHighLightColor(2);
   cnv->Range(-1062.5,-0.000125593,5187.5,0.0008405072);
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
   
   TH1F *h_gammaD_1_cT_lab_dummy62 = new TH1F("h_gammaD_1_cT_lab_dummy62","h_gammaD_1_cT_lab_dummy",5,0,5000);
   h_gammaD_1_cT_lab_dummy62->SetMaximum(0.0007728802);
   h_gammaD_1_cT_lab_dummy62->SetLineStyle(0);
   h_gammaD_1_cT_lab_dummy62->SetMarkerStyle(20);
   h_gammaD_1_cT_lab_dummy62->GetXaxis()->SetTitle("L of #gamma_{D} [mm]");
   h_gammaD_1_cT_lab_dummy62->GetXaxis()->SetLabelFont(42);
   h_gammaD_1_cT_lab_dummy62->GetXaxis()->SetLabelOffset(0.007);
   h_gammaD_1_cT_lab_dummy62->GetXaxis()->SetTitleSize(0.06);
   h_gammaD_1_cT_lab_dummy62->GetXaxis()->SetTitleOffset(0.95);
   h_gammaD_1_cT_lab_dummy62->GetXaxis()->SetTitleFont(42);
   h_gammaD_1_cT_lab_dummy62->GetYaxis()->SetTitle("Normalized Fraction of events / 1000.0 mm");
   h_gammaD_1_cT_lab_dummy62->GetYaxis()->SetLabelFont(42);
   h_gammaD_1_cT_lab_dummy62->GetYaxis()->SetLabelOffset(0.007);
   h_gammaD_1_cT_lab_dummy62->GetYaxis()->SetTitleSize(0.05);
   h_gammaD_1_cT_lab_dummy62->GetYaxis()->SetTitleOffset(1.3);
   h_gammaD_1_cT_lab_dummy62->GetYaxis()->SetTitleFont(42);
   h_gammaD_1_cT_lab_dummy62->GetZaxis()->SetLabelFont(42);
   h_gammaD_1_cT_lab_dummy62->GetZaxis()->SetLabelOffset(0.007);
   h_gammaD_1_cT_lab_dummy62->GetZaxis()->SetTitleSize(0.06);
   h_gammaD_1_cT_lab_dummy62->GetZaxis()->SetTitleFont(42);
   h_gammaD_1_cT_lab_dummy62->Draw("");
   
   TH1F *h_gammaD_1_cT_lab63 = new TH1F("h_gammaD_1_cT_lab63","h_gammaD_1_cT_lab",5,0,5000);
   h_gammaD_1_cT_lab63->SetBinContent(1,0.0003772487);
   h_gammaD_1_cT_lab63->SetBinContent(2,0.0002436332);
   h_gammaD_1_cT_lab63->SetBinContent(3,0.000171164);
   h_gammaD_1_cT_lab63->SetBinContent(4,0.0001209524);
   h_gammaD_1_cT_lab63->SetBinContent(5,8.700176e-05);
   h_gammaD_1_cT_lab63->SetBinContent(6,0.0004109171);
   h_gammaD_1_cT_lab63->SetEntries(79999);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#0000ff");
   h_gammaD_1_cT_lab63->SetLineColor(ci);
   h_gammaD_1_cT_lab63->SetLineWidth(2);
   h_gammaD_1_cT_lab63->SetMarkerStyle(20);
   h_gammaD_1_cT_lab63->GetXaxis()->SetLabelFont(42);
   h_gammaD_1_cT_lab63->GetXaxis()->SetLabelOffset(0.007);
   h_gammaD_1_cT_lab63->GetXaxis()->SetTitleSize(0.06);
   h_gammaD_1_cT_lab63->GetXaxis()->SetTitleOffset(0.95);
   h_gammaD_1_cT_lab63->GetXaxis()->SetTitleFont(42);
   h_gammaD_1_cT_lab63->GetYaxis()->SetLabelFont(42);
   h_gammaD_1_cT_lab63->GetYaxis()->SetLabelOffset(0.007);
   h_gammaD_1_cT_lab63->GetYaxis()->SetTitleSize(0.06);
   h_gammaD_1_cT_lab63->GetYaxis()->SetTitleOffset(1.3);
   h_gammaD_1_cT_lab63->GetYaxis()->SetTitleFont(42);
   h_gammaD_1_cT_lab63->GetZaxis()->SetLabelFont(42);
   h_gammaD_1_cT_lab63->GetZaxis()->SetLabelOffset(0.007);
   h_gammaD_1_cT_lab63->GetZaxis()->SetTitleSize(0.06);
   h_gammaD_1_cT_lab63->GetZaxis()->SetTitleFont(42);
   h_gammaD_1_cT_lab63->Draw("same");
   
   TH1F *h_gammaD_2_cT_lab64 = new TH1F("h_gammaD_2_cT_lab64","h_gammaD_2_cT_lab",5,0,5000);
   h_gammaD_2_cT_lab64->SetBinContent(1,0.0004293779);
   h_gammaD_2_cT_lab64->SetBinContent(2,0.0002456491);
   h_gammaD_2_cT_lab64->SetBinContent(3,0.0001533734);
   h_gammaD_2_cT_lab64->SetBinContent(4,0.0001032597);
   h_gammaD_2_cT_lab64->SetBinContent(5,6.833981e-05);
   h_gammaD_2_cT_lab64->SetBinContent(6,0.0002903273);
   h_gammaD_2_cT_lab64->SetEntries(79999);

   ci = TColor::GetColor("#ff0000");
   h_gammaD_2_cT_lab64->SetLineColor(ci);
   h_gammaD_2_cT_lab64->SetLineWidth(2);
   h_gammaD_2_cT_lab64->SetMarkerStyle(20);
   h_gammaD_2_cT_lab64->GetXaxis()->SetLabelFont(42);
   h_gammaD_2_cT_lab64->GetXaxis()->SetLabelOffset(0.007);
   h_gammaD_2_cT_lab64->GetXaxis()->SetTitleSize(0.06);
   h_gammaD_2_cT_lab64->GetXaxis()->SetTitleOffset(0.95);
   h_gammaD_2_cT_lab64->GetXaxis()->SetTitleFont(42);
   h_gammaD_2_cT_lab64->GetYaxis()->SetLabelFont(42);
   h_gammaD_2_cT_lab64->GetYaxis()->SetLabelOffset(0.007);
   h_gammaD_2_cT_lab64->GetYaxis()->SetTitleSize(0.06);
   h_gammaD_2_cT_lab64->GetYaxis()->SetTitleOffset(1.3);
   h_gammaD_2_cT_lab64->GetYaxis()->SetTitleFont(42);
   h_gammaD_2_cT_lab64->GetZaxis()->SetLabelFont(42);
   h_gammaD_2_cT_lab64->GetZaxis()->SetLabelOffset(0.007);
   h_gammaD_2_cT_lab64->GetZaxis()->SetTitleSize(0.06);
   h_gammaD_2_cT_lab64->GetZaxis()->SetTitleFont(42);
   h_gammaD_2_cT_lab64->Draw("same");
   
   TLegend *leg = new TLegend(0.46,0.6744444,0.6955556,0.7644444,NULL,"brNDC");
   leg->SetBorderSize(0);
   leg->SetTextSize(0.02777778);
   leg->SetLineColor(1);
   leg->SetLineStyle(1);
   leg->SetLineWidth(1);
   leg->SetFillColor(0);
   leg->SetFillStyle(0);
   TLegendEntry *entry=leg->AddEntry("h_gammaD_1_cT_lab","1st dark photon (leading p_{T})","L");

   ci = TColor::GetColor("#0000ff");
   entry->SetLineColor(ci);
   entry->SetLineStyle(1);
   entry->SetLineWidth(2);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("h_gammaD_2_cT_lab","2nd dark photon","L");

   ci = TColor::GetColor("#ff0000");
   entry->SetLineColor(ci);
   entry->SetLineStyle(1);
   entry->SetLineWidth(2);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   leg->Draw();
   
   leg = new TLegend(0.4566667,0.82,0.7822222,0.9066667,NULL,"brNDC");
   leg->SetBorderSize(0);
   leg->SetTextSize(0.02777778);
   leg->SetLineColor(1);
   leg->SetLineStyle(1);
   leg->SetLineWidth(1);
   leg->SetFillColor(0);
   leg->SetFillStyle(0);
   entry=leg->AddEntry("NULL","#splitline{pp #rightarrow h #rightarrow 2n_{1} #rightarrow 2n_{D} + 2 #gamma_{D} #rightarrow 2n_{D} + 4#mu}{#splitline{m_{h} = 125 GeV, m_{n_{1}} = 50 GeV, m_{n_{D}} = 1 GeV}{m_{#gamma_{D}} = 20 GeV, c#tau_{#gamma_{D}} = 1000 mm}}","h");
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
