{
//=========Macro generated from canvas: c/c
//=========  (Tue Jan 24 14:47:04 2017) by ROOT version5.34/07
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
   Double_t xAxis77[51] = {0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1.05, 1.1, 1.15, 1.2, 1.25, 1.3, 1.35, 1.4, 1.45, 1.5, 1.55, 1.6, 1.65, 1.7, 1.75, 1.8, 1.85, 1.9, 1.95, 2, 2.05, 2.1, 2.15, 2.2, 2.25, 2.3, 2.35, 2.4, 2.45, 2.5}; 
   
   TH1F *b1 = new TH1F("b1","           #scale[1.4]{#font[61]{CMS}} #font[52]{Simulation preliminary}                                                           14 TeV, 140 PU",50, xAxis77);
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
   Double_t xAxis78[51] = {0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1.05, 1.1, 1.15, 1.2, 1.25, 1.3, 1.35, 1.4, 1.45, 1.5, 1.55, 1.6, 1.65, 1.7, 1.75, 1.8, 1.85, 1.9, 1.95, 2, 2.05, 2.1, 2.15, 2.2, 2.25, 2.3, 2.35, 2.4, 2.45, 2.5}; 
   
   TH1F *_clone = new TH1F("_clone","",50, xAxis78);

   ci = TColor::GetColor("#ff0000");
   _clone->SetLineColor(ci);

   ci = TColor::GetColor("#ff0000");
   _clone->SetMarkerColor(ci);
   _clone->SetMarkerStyle(20);
   _clone->GetXaxis()->SetLabelFont(42);
   _clone->GetXaxis()->SetLabelSize(0.035);
   _clone->GetXaxis()->SetTitleSize(0.035);
   _clone->GetXaxis()->SetTitleFont(42);
   _clone->GetYaxis()->SetLabelFont(42);
   _clone->GetYaxis()->SetLabelSize(0.035);
   _clone->GetYaxis()->SetTitleSize(0.035);
   _clone->GetYaxis()->SetTitleFont(42);
   _clone->GetZaxis()->SetLabelFont(42);
   _clone->GetZaxis()->SetLabelSize(0.035);
   _clone->GetZaxis()->SetTitleSize(0.035);
   _clone->GetZaxis()->SetTitleFont(42);
   _clone->Draw("E1X0 same");
   Double_t xAxis79[51] = {0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1.05, 1.1, 1.15, 1.2, 1.25, 1.3, 1.35, 1.4, 1.45, 1.5, 1.55, 1.6, 1.65, 1.7, 1.75, 1.8, 1.85, 1.9, 1.95, 2, 2.05, 2.1, 2.15, 2.2, 2.25, 2.3, 2.35, 2.4, 2.45, 2.5}; 
   
   TH1F *_clone = new TH1F("_clone","",50, xAxis79);

   ci = TColor::GetColor("#cc00ff");
   _clone->SetLineColor(ci);

   ci = TColor::GetColor("#cc00ff");
   _clone->SetMarkerColor(ci);
   _clone->SetMarkerStyle(21);
   _clone->GetXaxis()->SetLabelFont(42);
   _clone->GetXaxis()->SetLabelSize(0.035);
   _clone->GetXaxis()->SetTitleSize(0.035);
   _clone->GetXaxis()->SetTitleFont(42);
   _clone->GetYaxis()->SetLabelFont(42);
   _clone->GetYaxis()->SetLabelSize(0.035);
   _clone->GetYaxis()->SetTitleSize(0.035);
   _clone->GetYaxis()->SetTitleFont(42);
   _clone->GetZaxis()->SetLabelFont(42);
   _clone->GetZaxis()->SetLabelSize(0.035);
   _clone->GetZaxis()->SetTitleSize(0.035);
   _clone->GetZaxis()->SetTitleFont(42);
   _clone->Draw("E1X0 same");
   Double_t xAxis80[51] = {0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1.05, 1.1, 1.15, 1.2, 1.25, 1.3, 1.35, 1.4, 1.45, 1.5, 1.55, 1.6, 1.65, 1.7, 1.75, 1.8, 1.85, 1.9, 1.95, 2, 2.05, 2.1, 2.15, 2.2, 2.25, 2.3, 2.35, 2.4, 2.45, 2.5}; 
   
   TH1F *_clone = new TH1F("_clone","",50, xAxis80);

   ci = TColor::GetColor("#0000ff");
   _clone->SetLineColor(ci);

   ci = TColor::GetColor("#0000ff");
   _clone->SetMarkerColor(ci);
   _clone->SetMarkerStyle(22);
   _clone->GetXaxis()->SetLabelFont(42);
   _clone->GetXaxis()->SetLabelSize(0.035);
   _clone->GetXaxis()->SetTitleSize(0.035);
   _clone->GetXaxis()->SetTitleFont(42);
   _clone->GetYaxis()->SetLabelFont(42);
   _clone->GetYaxis()->SetLabelSize(0.035);
   _clone->GetYaxis()->SetTitleSize(0.035);
   _clone->GetYaxis()->SetTitleFont(42);
   _clone->GetZaxis()->SetLabelFont(42);
   _clone->GetZaxis()->SetLabelSize(0.035);
   _clone->GetZaxis()->SetTitleSize(0.035);
   _clone->GetZaxis()->SetTitleFont(42);
   _clone->Draw("E1X0 same");
   
   TLegend *leg = new TLegend(0.15,0.2,0.5,0.35,NULL,"brNDC");
   leg->SetBorderSize(0);
   leg->SetTextSize(0.03);
   leg->SetLineColor(1);
   leg->SetLineStyle(1);
   leg->SetLineWidth(1);
   leg->SetFillColor(0);
   leg->SetFillStyle(0);
   TLegendEntry *entry=leg->AddEntry("NULL","1.6<|#eta|<2.2","h");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("_clone","Prompt L1Mu","p");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);

   ci = TColor::GetColor("#ff0000");
   entry->SetMarkerColor(ci);
   entry->SetMarkerStyle(20);
   entry->SetMarkerSize(1);
   entry=leg->AddEntry("_clone","Prompt L1Mu, 3 CSC stubs, ME11","p");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);

   ci = TColor::GetColor("#cc00ff");
   entry->SetMarkerColor(ci);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry=leg->AddEntry("_clone","Prompt L1Mu, 3 CSC stubs, ME11, GE11","p");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);

   ci = TColor::GetColor("#0000ff");
   entry->SetMarkerColor(ci);
   entry->SetMarkerStyle(22);
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
