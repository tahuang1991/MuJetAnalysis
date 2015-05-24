void DarkSusy_mH_125_mGammaD_2000_cT_100_LHE_gammaD_Sorted_cT()
{
//=========Macro generated from canvas: cnv/cnv
//=========  (Sun May 24 15:18:25 2015) by ROOT version6.02/05
   TCanvas *cnv = new TCanvas("cnv", "cnv",1,1,904,904);
   gStyle->SetOptFit(1);
   gStyle->SetOptStat(0);
   gStyle->SetOptTitle(0);
   cnv->SetHighLightColor(2);
   cnv->Range(-106.25,-0.001860965,518.75,0.01245415);
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
   
   TH1F *h_gammaD_1_cT_dummy59 = new TH1F("h_gammaD_1_cT_dummy59","h_gammaD_1_cT_dummy",5,0,500);
   h_gammaD_1_cT_dummy59->SetMaximum(0.01145209);
   h_gammaD_1_cT_dummy59->SetLineStyle(0);
   h_gammaD_1_cT_dummy59->SetMarkerStyle(20);
   h_gammaD_1_cT_dummy59->GetXaxis()->SetTitle("c#tau of #gamma_{D} [mm]");
   h_gammaD_1_cT_dummy59->GetXaxis()->SetLabelFont(42);
   h_gammaD_1_cT_dummy59->GetXaxis()->SetLabelOffset(0.007);
   h_gammaD_1_cT_dummy59->GetXaxis()->SetTitleSize(0.06);
   h_gammaD_1_cT_dummy59->GetXaxis()->SetTitleOffset(0.95);
   h_gammaD_1_cT_dummy59->GetXaxis()->SetTitleFont(42);
   h_gammaD_1_cT_dummy59->GetYaxis()->SetTitle("Normalized Fraction of events / 100.0 mm");
   h_gammaD_1_cT_dummy59->GetYaxis()->SetLabelFont(42);
   h_gammaD_1_cT_dummy59->GetYaxis()->SetLabelOffset(0.007);
   h_gammaD_1_cT_dummy59->GetYaxis()->SetTitleSize(0.05);
   h_gammaD_1_cT_dummy59->GetYaxis()->SetTitleOffset(1.3);
   h_gammaD_1_cT_dummy59->GetYaxis()->SetTitleFont(42);
   h_gammaD_1_cT_dummy59->GetZaxis()->SetLabelFont(42);
   h_gammaD_1_cT_dummy59->GetZaxis()->SetLabelOffset(0.007);
   h_gammaD_1_cT_dummy59->GetZaxis()->SetTitleSize(0.06);
   h_gammaD_1_cT_dummy59->GetZaxis()->SetTitleFont(42);
   h_gammaD_1_cT_dummy59->Draw("");
   
   TH1F *h_gammaD_1_cT60 = new TH1F("h_gammaD_1_cT60","h_gammaD_1_cT",5,0,500);
   h_gammaD_1_cT60->SetBinContent(1,0.006365398);
   h_gammaD_1_cT60->SetBinContent(2,0.002343073);
   h_gammaD_1_cT60->SetBinContent(3,0.0008620256);
   h_gammaD_1_cT60->SetBinContent(4,0.0003122168);
   h_gammaD_1_cT60->SetBinContent(5,0.0001172858);
   h_gammaD_1_cT60->SetBinContent(6,6.732609e-05);
   h_gammaD_1_cT60->SetEntries(79999);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#0000ff");
   h_gammaD_1_cT60->SetLineColor(ci);
   h_gammaD_1_cT60->SetLineWidth(2);
   h_gammaD_1_cT60->SetMarkerStyle(20);
   h_gammaD_1_cT60->GetXaxis()->SetLabelFont(42);
   h_gammaD_1_cT60->GetXaxis()->SetLabelOffset(0.007);
   h_gammaD_1_cT60->GetXaxis()->SetTitleSize(0.06);
   h_gammaD_1_cT60->GetXaxis()->SetTitleOffset(0.95);
   h_gammaD_1_cT60->GetXaxis()->SetTitleFont(42);
   h_gammaD_1_cT60->GetYaxis()->SetLabelFont(42);
   h_gammaD_1_cT60->GetYaxis()->SetLabelOffset(0.007);
   h_gammaD_1_cT60->GetYaxis()->SetTitleSize(0.06);
   h_gammaD_1_cT60->GetYaxis()->SetTitleOffset(1.3);
   h_gammaD_1_cT60->GetYaxis()->SetTitleFont(42);
   h_gammaD_1_cT60->GetZaxis()->SetLabelFont(42);
   h_gammaD_1_cT60->GetZaxis()->SetLabelOffset(0.007);
   h_gammaD_1_cT60->GetZaxis()->SetTitleSize(0.06);
   h_gammaD_1_cT60->GetZaxis()->SetTitleFont(42);
   h_gammaD_1_cT60->Draw("same");
   
   TH1F *h_gammaD_2_cT61 = new TH1F("h_gammaD_2_cT61","h_gammaD_2_cT",5,0,500);
   h_gammaD_2_cT61->SetBinContent(1,0.006362274);
   h_gammaD_2_cT61->SetBinContent(2,0.002352704);
   h_gammaD_2_cT61->SetBinContent(3,0.000847447);
   h_gammaD_2_cT61->SetBinContent(4,0.0003198388);
   h_gammaD_2_cT61->SetBinContent(5,0.0001177359);
   h_gammaD_2_cT61->SetBinContent(6,7.353775e-05);
   h_gammaD_2_cT61->SetEntries(79999);

   ci = TColor::GetColor("#ff0000");
   h_gammaD_2_cT61->SetLineColor(ci);
   h_gammaD_2_cT61->SetLineWidth(2);
   h_gammaD_2_cT61->SetMarkerStyle(20);
   h_gammaD_2_cT61->GetXaxis()->SetLabelFont(42);
   h_gammaD_2_cT61->GetXaxis()->SetLabelOffset(0.007);
   h_gammaD_2_cT61->GetXaxis()->SetTitleSize(0.06);
   h_gammaD_2_cT61->GetXaxis()->SetTitleOffset(0.95);
   h_gammaD_2_cT61->GetXaxis()->SetTitleFont(42);
   h_gammaD_2_cT61->GetYaxis()->SetLabelFont(42);
   h_gammaD_2_cT61->GetYaxis()->SetLabelOffset(0.007);
   h_gammaD_2_cT61->GetYaxis()->SetTitleSize(0.06);
   h_gammaD_2_cT61->GetYaxis()->SetTitleOffset(1.3);
   h_gammaD_2_cT61->GetYaxis()->SetTitleFont(42);
   h_gammaD_2_cT61->GetZaxis()->SetLabelFont(42);
   h_gammaD_2_cT61->GetZaxis()->SetLabelOffset(0.007);
   h_gammaD_2_cT61->GetZaxis()->SetTitleSize(0.06);
   h_gammaD_2_cT61->GetZaxis()->SetTitleFont(42);
   h_gammaD_2_cT61->Draw("same");
   
   TLegend *leg = new TLegend(0.46,0.6744444,0.6955556,0.7644444,NULL,"brNDC");
   leg->SetBorderSize(0);
   leg->SetTextSize(0.02777778);
   leg->SetLineColor(1);
   leg->SetLineStyle(1);
   leg->SetLineWidth(1);
   leg->SetFillColor(0);
   leg->SetFillStyle(0);
   TLegendEntry *entry=leg->AddEntry("h_gammaD_1_cT","1st dark photon (leading p_{T})","L");

   ci = TColor::GetColor("#0000ff");
   entry->SetLineColor(ci);
   entry->SetLineStyle(1);
   entry->SetLineWidth(2);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("h_gammaD_2_cT","2nd dark photon","L");

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
   entry=leg->AddEntry("NULL","#splitline{pp #rightarrow h #rightarrow 2n_{1} #rightarrow 2n_{D} + 2 #gamma_{D} #rightarrow 2n_{D} + 4#mu}{#splitline{m_{h} = 125 GeV, m_{n_{1}} = 50 GeV, m_{n_{D}} = 1 GeV}{m_{#gamma_{D}} = 20 GeV, c#tau_{#gamma_{D}} = 100 mm}}","h");
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
