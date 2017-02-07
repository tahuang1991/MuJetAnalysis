{
//=========Macro generated from canvas: c/c
//=========  (Thu Jan  5 14:03:48 2017) by ROOT version5.34/07
   TCanvas *c = new TCanvas("c", "c",0,0,800,600);
   gStyle->SetOptStat(0);
   c->SetHighLightColor(2);
   c->Range(-0.3776979,-8.024691,2.619904,53.7037);
   c->SetFillColor(0);
   c->SetBorderMode(0);
   c->SetBorderSize(2);
   c->SetGridx();
   c->SetGridy();
   c->SetTickx(1);
   c->SetTicky(1);
   c->SetLeftMargin(0.126);
   c->SetRightMargin(0.04);
   c->SetTopMargin(0.06);
   c->SetBottomMargin(0.13);
   c->SetFrameBorderMode(0);
   c->SetFrameBorderMode(0);
   Double_t xAxis157[51] = {0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1.05, 1.1, 1.15, 1.2, 1.25, 1.3, 1.35, 1.4, 1.45, 1.5, 1.55, 1.6, 1.65, 1.7, 1.75, 1.8, 1.85, 1.9, 1.95, 2, 2.05, 2.1, 2.15, 2.2, 2.25, 2.3, 2.35, 2.4, 2.45, 2.5}; 
   
   TH1F *b1 = new TH1F("b1","           #scale[1.4]{#font[61]{CMS}} #font[52]{Simulation preliminary}                                                           14 TeV, 140 PU",50, xAxis157);
   b1->SetMinimum(0);
   b1->SetMaximum(50);
   b1->SetStats(0);

   Int_t ci;   // for color index setting
   ci = TColor::GetColor("#000099");
   b1->SetLineColor(ci);
   b1->GetXaxis()->SetTitle("Muon trigger #eta");
   b1->GetXaxis()->SetRange(1,50);
   b1->GetXaxis()->SetLabelFont(42);
   b1->GetXaxis()->SetLabelSize(0.05);
   b1->GetXaxis()->SetTitleSize(0.05);
   b1->GetXaxis()->SetTitleFont(42);
   b1->GetYaxis()->SetTitle("Trigger rate [kHz]");
   b1->GetYaxis()->SetLabelFont(42);
   b1->GetYaxis()->SetLabelSize(0.05);
   b1->GetYaxis()->SetTitleSize(0.05);
   b1->GetYaxis()->SetTitleOffset(1.2);
   b1->GetYaxis()->SetTitleFont(42);
   b1->GetZaxis()->SetLabelFont(42);
   b1->GetZaxis()->SetLabelSize(0.035);
   b1->GetZaxis()->SetTitleSize(0.035);
   b1->GetZaxis()->SetTitleFont(42);
   b1->Draw("");
   Double_t xAxis158[51] = {0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1.05, 1.1, 1.15, 1.2, 1.25, 1.3, 1.35, 1.4, 1.45, 1.5, 1.55, 1.6, 1.65, 1.7, 1.75, 1.8, 1.85, 1.9, 1.95, 2, 2.05, 2.1, 2.15, 2.2, 2.25, 2.3, 2.35, 2.4, 2.45, 2.5}; 
   
   TH1F *h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20 = new TH1F("h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20","",50, xAxis158);
   h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20->SetBinContent(35,0.1803605);
   h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20->SetBinContent(38,0.1803605);
   h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20->SetBinContent(40,0.2705408);
   h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20->SetBinError(35,0.1275342);
   h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20->SetBinError(38,0.1275342);
   h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20->SetBinError(40,0.1561968);
   h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20->SetEntries(7);

   ci = TColor::GetColor("#ff0000");
   h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20->SetFillColor(ci);

   ci = TColor::GetColor("#ff0000");
   h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20->SetLineColor(ci);
   h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20->GetXaxis()->SetLabelFont(42);
   h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20->GetXaxis()->SetLabelSize(0.035);
   h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20->GetXaxis()->SetTitleSize(0.035);
   h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20->GetXaxis()->SetTitleFont(42);
   h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20->GetYaxis()->SetLabelFont(42);
   h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20->GetYaxis()->SetLabelSize(0.035);
   h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20->GetYaxis()->SetTitleSize(0.035);
   h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20->GetYaxis()->SetTitleFont(42);
   h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20->GetZaxis()->SetLabelFont(42);
   h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20->GetZaxis()->SetLabelSize(0.035);
   h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20->GetZaxis()->SetTitleSize(0.035);
   h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20->GetZaxis()->SetTitleFont(42);
   h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20->Draw("P same");
   Double_t xAxis159[51] = {0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1.05, 1.1, 1.15, 1.2, 1.25, 1.3, 1.35, 1.4, 1.45, 1.5, 1.55, 1.6, 1.65, 1.7, 1.75, 1.8, 1.85, 1.9, 1.95, 2, 2.05, 2.1, 2.15, 2.2, 2.25, 2.3, 2.35, 2.4, 2.45, 2.5}; 
   
   TH1F *h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20 = new TH1F("h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20","",50, xAxis159);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20->SetBinContent(33,0.6312619);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20->SetBinContent(34,0.5410816);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20->SetBinContent(35,1.082163);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20->SetBinContent(36,2.795588);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20->SetBinContent(37,3.877752);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20->SetBinContent(38,7.394782);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20->SetBinContent(39,7.845683);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20->SetBinContent(40,8.747486);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20->SetBinContent(41,0.4509014);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20->SetBinError(33,0.2385946);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20->SetBinError(34,0.2208956);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20->SetBinError(35,0.3123936);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20->SetBinError(36,0.5021025);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20->SetBinError(37,0.5913516);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20->SetBinError(38,0.8166171);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20->SetBinError(39,0.8411456);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20->SetBinError(40,0.8881727);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20->SetBinError(41,0.2016492);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20->SetEntries(370);

   ci = TColor::GetColor("#cc00ff");
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20->SetFillColor(ci);

   ci = TColor::GetColor("#cc00ff");
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20->SetLineColor(ci);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20->GetXaxis()->SetLabelFont(42);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20->GetXaxis()->SetLabelSize(0.035);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20->GetXaxis()->SetTitleSize(0.035);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20->GetXaxis()->SetTitleFont(42);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20->GetYaxis()->SetLabelFont(42);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20->GetYaxis()->SetLabelSize(0.035);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20->GetYaxis()->SetTitleSize(0.035);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20->GetYaxis()->SetTitleFont(42);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20->GetZaxis()->SetLabelFont(42);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20->GetZaxis()->SetLabelSize(0.035);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20->GetZaxis()->SetTitleSize(0.035);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20->GetZaxis()->SetTitleFont(42);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20->Draw("P same");
   Double_t xAxis160[51] = {0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1.05, 1.1, 1.15, 1.2, 1.25, 1.3, 1.35, 1.4, 1.45, 1.5, 1.55, 1.6, 1.65, 1.7, 1.75, 1.8, 1.85, 1.9, 1.95, 2, 2.05, 2.1, 2.15, 2.2, 2.25, 2.3, 2.35, 2.4, 2.45, 2.5}; 
   
   TH1F *h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20_looseIso = new TH1F("h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20_looseIso","",50, xAxis160);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20_looseIso->SetBinContent(33,0.9009009);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20_looseIso->SetBinContent(34,0.6006006);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20_looseIso->SetBinContent(35,0.6006006);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20_looseIso->SetBinContent(36,3.603604);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20_looseIso->SetBinContent(37,3.903904);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20_looseIso->SetBinContent(38,10.81081);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20_looseIso->SetBinContent(39,17.11712);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20_looseIso->SetBinContent(40,16.21622);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20_looseIso->SetBinContent(41,1.501502);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20_looseIso->SetBinError(33,0.5201354);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20_looseIso->SetBinError(34,0.4246888);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20_looseIso->SetBinError(35,0.4246888);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20_looseIso->SetBinError(36,1.040271);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20_looseIso->SetBinError(37,1.082748);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20_looseIso->SetBinError(38,1.801802);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20_looseIso->SetBinError(39,2.267218);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20_looseIso->SetBinError(40,2.206748);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20_looseIso->SetBinError(41,0.6714919);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20_looseIso->SetEntries(184);

   ci = TColor::GetColor("#0000ff");
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20_looseIso->SetFillColor(ci);

   ci = TColor::GetColor("#0000ff");
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20_looseIso->SetLineColor(ci);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20_looseIso->GetXaxis()->SetLabelFont(42);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20_looseIso->GetXaxis()->SetLabelSize(0.035);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20_looseIso->GetXaxis()->SetTitleSize(0.035);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20_looseIso->GetXaxis()->SetTitleFont(42);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20_looseIso->GetYaxis()->SetLabelFont(42);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20_looseIso->GetYaxis()->SetLabelSize(0.035);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20_looseIso->GetYaxis()->SetTitleSize(0.035);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20_looseIso->GetYaxis()->SetTitleFont(42);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20_looseIso->GetZaxis()->SetLabelFont(42);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20_looseIso->GetZaxis()->SetLabelSize(0.035);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20_looseIso->GetZaxis()->SetTitleSize(0.035);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20_looseIso->GetZaxis()->SetTitleFont(42);
   h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20_looseIso->Draw("P same");
   
   TLegend *leg = new TLegend(0.15,0.2,0.5,0.35,NULL,"brNDC");
   leg->SetBorderSize(0);
   leg->SetTextSize(0.03);
   leg->SetLineColor(1);
   leg->SetLineStyle(1);
   leg->SetLineWidth(1);
   leg->SetFillColor(0);
   leg->SetFillStyle(0);
   TLegendEntry *entry=leg->AddEntry("NULL","1.6<|#eta|<2.0","h");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("h_single_prompt_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20","Prompt L1Mu, hit in GE11, ME11, GE21, ME21","f");

   ci = TColor::GetColor("#ff0000");
   entry->SetFillColor(ci);
   entry->SetFillStyle(1001);

   ci = TColor::GetColor("#ff0000");
   entry->SetLineColor(ci);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry=leg->AddEntry("h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20","Displaced L1Mu, hit in GE11, ME11, GE21, ME21 direction based","f");

   ci = TColor::GetColor("#cc00ff");
   entry->SetFillColor(ci);
   entry->SetFillStyle(1001);

   ci = TColor::GetColor("#cc00ff");
   entry->SetLineColor(ci);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry=leg->AddEntry("h_single_displaced_L1Mu_rate_eta_GE11_ME11_GE21_ME21_eta16to20_looseIso","Displaced L1Mu, hit in GE11, ME11, GE21, ME21 direction based, loose Iso","f");

   ci = TColor::GetColor("#0000ff");
   entry->SetFillColor(ci);
   entry->SetFillStyle(1001);

   ci = TColor::GetColor("#0000ff");
   entry->SetLineColor(ci);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   leg->Draw();
   
   TPaveText *pt = new TPaveText(0,0.942,1,1,"blNDC");
   pt->SetName("title");
   pt->SetBorderSize(0);
   pt->SetFillColor(0);
   pt->SetFillStyle(0);
   pt->SetTextFont(42);
   TText *text = pt->AddText("           #scale[1.4]{#font[61]{CMS}} #font[52]{Simulation preliminary}                                                           14 TeV, 140 PU");
   pt->Draw();
   c->Modified();
   c->cd();
   c->SetSelected(c);
}
