void DarkSusy_mH_125_mGammaD_2000_cT_1000_LHE_gammaD_L_XY()
{
//=========Macro generated from canvas: cnv/cnv
//=========  (Sun May 24 15:19:01 2015) by ROOT version6.02/05
   TCanvas *cnv = new TCanvas("cnv", "cnv",1,1,904,904);
   gStyle->SetOptFit(1);
   gStyle->SetOptStat(0);
   gStyle->SetOptTitle(0);
   cnv->SetHighLightColor(2);
   cnv->Range(-1062.5,-0.000148977,5187.5,0.0009969997);
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
   
   TH1F *h_gammaD_cT_XY_lab_dummy55 = new TH1F("h_gammaD_cT_XY_lab_dummy55","h_gammaD_cT_XY_lab_dummy",5,0,5000);
   h_gammaD_cT_XY_lab_dummy55->SetMaximum(0.0009167813);
   h_gammaD_cT_XY_lab_dummy55->SetLineStyle(0);
   h_gammaD_cT_XY_lab_dummy55->SetMarkerStyle(20);
   h_gammaD_cT_XY_lab_dummy55->GetXaxis()->SetTitle("L_{XY} of #gamma_{D} [mm]");
   h_gammaD_cT_XY_lab_dummy55->GetXaxis()->SetLabelFont(42);
   h_gammaD_cT_XY_lab_dummy55->GetXaxis()->SetLabelOffset(0.007);
   h_gammaD_cT_XY_lab_dummy55->GetXaxis()->SetTitleSize(0.06);
   h_gammaD_cT_XY_lab_dummy55->GetXaxis()->SetTitleOffset(0.95);
   h_gammaD_cT_XY_lab_dummy55->GetXaxis()->SetTitleFont(42);
   h_gammaD_cT_XY_lab_dummy55->GetYaxis()->SetTitle("Normalized Fraction of Events / 1000.0 mm");
   h_gammaD_cT_XY_lab_dummy55->GetYaxis()->SetLabelFont(42);
   h_gammaD_cT_XY_lab_dummy55->GetYaxis()->SetLabelOffset(0.007);
   h_gammaD_cT_XY_lab_dummy55->GetYaxis()->SetTitleSize(0.05);
   h_gammaD_cT_XY_lab_dummy55->GetYaxis()->SetTitleOffset(1.3);
   h_gammaD_cT_XY_lab_dummy55->GetYaxis()->SetTitleFont(42);
   h_gammaD_cT_XY_lab_dummy55->GetZaxis()->SetLabelFont(42);
   h_gammaD_cT_XY_lab_dummy55->GetZaxis()->SetLabelOffset(0.007);
   h_gammaD_cT_XY_lab_dummy55->GetZaxis()->SetTitleSize(0.06);
   h_gammaD_cT_XY_lab_dummy55->GetZaxis()->SetTitleFont(42);
   h_gammaD_cT_XY_lab_dummy55->Draw("");
   
   TH1F *h_gammaD_cT_XY_lab56 = new TH1F("h_gammaD_cT_XY_lab56","h_gammaD_cT_XY_lab",5,0,5000);
   h_gammaD_cT_XY_lab56->SetBinContent(1,0.000509323);
   h_gammaD_cT_XY_lab56->SetBinContent(2,0.000253035);
   h_gammaD_cT_XY_lab56->SetBinContent(3,0.0001309937);
   h_gammaD_cT_XY_lab56->SetBinContent(4,6.952706e-05);
   h_gammaD_cT_XY_lab56->SetBinContent(5,3.712133e-05);
   h_gammaD_cT_XY_lab56->SetBinContent(6,4.9353e-05);
   h_gammaD_cT_XY_lab56->SetEntries(159998);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#0000ff");
   h_gammaD_cT_XY_lab56->SetLineColor(ci);
   h_gammaD_cT_XY_lab56->SetLineWidth(2);
   h_gammaD_cT_XY_lab56->SetMarkerStyle(20);
   h_gammaD_cT_XY_lab56->GetXaxis()->SetTitle("L_{xy} of #gamma_{D} [mm]");
   h_gammaD_cT_XY_lab56->GetXaxis()->SetLabelFont(42);
   h_gammaD_cT_XY_lab56->GetXaxis()->SetLabelOffset(0.007);
   h_gammaD_cT_XY_lab56->GetXaxis()->SetTitleSize(0.06);
   h_gammaD_cT_XY_lab56->GetXaxis()->SetTitleOffset(0.95);
   h_gammaD_cT_XY_lab56->GetXaxis()->SetTitleFont(42);
   h_gammaD_cT_XY_lab56->GetYaxis()->SetTitle("Events");
   h_gammaD_cT_XY_lab56->GetYaxis()->SetLabelFont(42);
   h_gammaD_cT_XY_lab56->GetYaxis()->SetLabelOffset(0.007);
   h_gammaD_cT_XY_lab56->GetYaxis()->SetTitleSize(0.06);
   h_gammaD_cT_XY_lab56->GetYaxis()->SetTitleOffset(1.5);
   h_gammaD_cT_XY_lab56->GetYaxis()->SetTitleFont(42);
   h_gammaD_cT_XY_lab56->GetZaxis()->SetLabelFont(42);
   h_gammaD_cT_XY_lab56->GetZaxis()->SetLabelOffset(0.007);
   h_gammaD_cT_XY_lab56->GetZaxis()->SetTitleSize(0.06);
   h_gammaD_cT_XY_lab56->GetZaxis()->SetTitleFont(42);
   h_gammaD_cT_XY_lab56->Draw("same");
   
   TLegend *leg = new TLegend(0.4566667,0.82,0.7822222,0.9066667,NULL,"brNDC");
   leg->SetBorderSize(0);
   leg->SetTextSize(0.02777778);
   leg->SetLineColor(1);
   leg->SetLineStyle(1);
   leg->SetLineWidth(1);
   leg->SetFillColor(0);
   leg->SetFillStyle(0);
   TLegendEntry *entry=leg->AddEntry("NULL","#splitline{pp #rightarrow h #rightarrow 2n_{1} #rightarrow 2n_{D} + 2 #gamma_{D} #rightarrow 2n_{D} + 4#mu}{#splitline{m_{h} = 125 GeV, m_{n_{1}} = 50 GeV, m_{n_{D}} = 1 GeV}{m_{#gamma_{D}} = 20 GeV, c#tau_{#gamma_{D}} = 1000 mm}}","h");
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
