{
//=========Macro generated from canvas: c/c
//=========  (Thu Sep 29 00:31:12 2016) by ROOT version5.34/07
   TCanvas *c = new TCanvas("c", "c",0,0,800,600);
   c->SetHighLightColor(2);
   c->Range(0,0,1,1);
   c->SetFillColor(0);
   c->SetBorderMode(0);
   c->SetBorderSize(2);
   c->SetTickx(1);
   c->SetTicky(1);
   c->SetLeftMargin(0.126);
   c->SetRightMargin(0.04);
   c->SetTopMargin(0.06);
   c->SetBottomMargin(0.13);
   c->SetFrameBorderMode(0);
   
   TH1F *GenMuEta_leading_MS2_random_pt10 = new TH1F("GenMuEta_leading_MS2_random_pt10","",100,-5,5);
   
   TPaveStats *ptstats = new TPaveStats(0.78,0.615,0.98,0.935,"brNDC");
   ptstats->SetName("stats");
   ptstats->SetBorderSize(1);
   ptstats->SetFillColor(0);
   ptstats->SetFillStyle(0);
   ptstats->SetTextAlign(12);
   ptstats->SetTextFont(42);
   TText *text = ptstats->AddText("GenMuEta_leading_MS2_random_pt10");
   text->SetTextSize(0.0368);
   text = ptstats->AddText("Entries = 0      ");
   text = ptstats->AddText("Mean  =      0");
   text = ptstats->AddText("RMS   =      0");
   text = ptstats->AddText("Underflow =      0");
   text = ptstats->AddText("Overflow  =      0");
   text = ptstats->AddText("Integral =      0");
   text = ptstats->AddText("Skewness =   -nan");
   ptstats->SetOptStat(11111111);
   ptstats->SetOptFit(0);
   ptstats->Draw();
   GenMuEta_leading_MS2_random_pt10->GetListOfFunctions()->Add(ptstats);
   ptstats->SetParent(GenMuEta_leading_MS2_random_pt10);

   Int_t ci;   // for color index setting
   ci = TColor::GetColor("#000099");
   GenMuEta_leading_MS2_random_pt10->SetLineColor(ci);
   GenMuEta_leading_MS2_random_pt10->GetXaxis()->SetTitle("Muon #eta at 2nd muon station");
   GenMuEta_leading_MS2_random_pt10->GetXaxis()->SetLabelFont(42);
   GenMuEta_leading_MS2_random_pt10->GetXaxis()->SetLabelSize(0.035);
   GenMuEta_leading_MS2_random_pt10->GetXaxis()->SetTitleSize(0.035);
   GenMuEta_leading_MS2_random_pt10->GetXaxis()->SetTitleFont(42);
   GenMuEta_leading_MS2_random_pt10->GetYaxis()->SetTitle(" Entries");
   GenMuEta_leading_MS2_random_pt10->GetYaxis()->SetLabelFont(42);
   GenMuEta_leading_MS2_random_pt10->GetYaxis()->SetLabelSize(0.035);
   GenMuEta_leading_MS2_random_pt10->GetYaxis()->SetTitleSize(0.035);
   GenMuEta_leading_MS2_random_pt10->GetYaxis()->SetTitleFont(42);
   GenMuEta_leading_MS2_random_pt10->GetZaxis()->SetLabelFont(42);
   GenMuEta_leading_MS2_random_pt10->GetZaxis()->SetLabelSize(0.035);
   GenMuEta_leading_MS2_random_pt10->GetZaxis()->SetTitleSize(0.035);
   GenMuEta_leading_MS2_random_pt10->GetZaxis()->SetTitleFont(42);
   GenMuEta_leading_MS2_random_pt10->Draw("");
   c->Modified();
   c->cd();
   c->SetSelected(c);
}
