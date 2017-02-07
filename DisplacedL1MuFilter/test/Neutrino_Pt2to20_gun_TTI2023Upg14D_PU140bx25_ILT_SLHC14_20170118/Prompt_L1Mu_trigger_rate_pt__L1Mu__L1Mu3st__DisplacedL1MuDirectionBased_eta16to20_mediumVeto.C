{
//=========Macro generated from canvas: c/c
//=========  (Wed Jan 18 15:36:37 2017) by ROOT version5.34/07
   TCanvas *c = new TCanvas("c", "c",0,0,800,600);
   gStyle->SetOptStat(0);
   c->SetHighLightColor(2);
   c->Range(0.02227417,-1.453126,2.234622,4.348072);
   c->SetFillColor(0);
   c->SetBorderMode(0);
   c->SetBorderSize(2);
   c->SetLogx();
   c->SetLogy();
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
   Double_t xAxis116[30] = {1, 2, 2.5, 3, 3.5, 4, 4.5, 5, 6, 7, 8, 10, 12, 14, 16, 18, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100, 120, 140}; 
   
   TH1F *b1 = new TH1F("b1","           #scale[1.4]{#font[61]{CMS}} #font[52]{Simulation preliminary}                                                           14 TeV, 140 PU",29, xAxis116);
   b1->SetMinimum(0.2);
   b1->SetMaximum(10000);
   b1->SetStats(0);

   Int_t ci;   // for color index setting
   ci = TColor::GetColor("#000099");
   b1->SetLineColor(ci);
   b1->GetXaxis()->SetTitle("Muon trigger p_{T} threshold [GeV]");
   b1->GetXaxis()->SetRange(2,29);
   b1->GetXaxis()->SetLabelFont(42);
   b1->GetXaxis()->SetLabelSize(0.05);
   b1->GetXaxis()->SetTitleSize(0.05);
   b1->GetXaxis()->SetTitleFont(42);
   b1->GetYaxis()->SetTitle("Trigger rate [kHz]");
   b1->GetYaxis()->SetNdivisions(520);
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
   Double_t xAxis117[29] = {2, 2.5, 3, 3.5, 4, 4.5, 5, 6, 7, 8, 10, 12, 14, 16, 18, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100, 120, 140}; 
   
   TH1F *htemp__49 = new TH1F("htemp__49"," ",28, xAxis117);
   htemp__49->SetBinContent(1,750);
   htemp__49->SetBinContent(2,750);
   htemp__49->SetBinContent(3,654);
   htemp__49->SetBinContent(4,516);
   htemp__49->SetBinContent(5,420);
   htemp__49->SetBinContent(6,315);
   htemp__49->SetBinContent(7,219);
   htemp__49->SetBinContent(8,123);
   htemp__49->SetBinContent(9,63);
   htemp__49->SetBinContent(10,45);
   htemp__49->SetBinContent(11,12);
   htemp__49->SetBinContent(12,9);
   htemp__49->SetBinContent(13,9);
   htemp__49->SetBinContent(14,9);
   htemp__49->SetBinContent(15,6);
   htemp__49->SetBinContent(16,6);
   htemp__49->SetBinContent(17,6);
   htemp__49->SetBinContent(18,6);
   htemp__49->SetBinContent(19,3);
   htemp__49->SetBinContent(20,3);
   htemp__49->SetBinError(1,47.43416);
   htemp__49->SetBinError(2,47.43416);
   htemp__49->SetBinError(3,44.29447);
   htemp__49->SetBinError(4,39.34463);
   htemp__49->SetBinError(5,35.49648);
   htemp__49->SetBinError(6,30.74085);
   htemp__49->SetBinError(7,25.63201);
   htemp__49->SetBinError(8,19.20937);
   htemp__49->SetBinError(9,13.74773);
   htemp__49->SetBinError(10,11.61895);
   htemp__49->SetBinError(11,6);
   htemp__49->SetBinError(12,5.196152);
   htemp__49->SetBinError(13,5.196152);
   htemp__49->SetBinError(14,5.196152);
   htemp__49->SetBinError(15,4.242641);
   htemp__49->SetBinError(16,4.242641);
   htemp__49->SetBinError(17,4.242641);
   htemp__49->SetBinError(18,4.242641);
   htemp__49->SetBinError(19,3);
   htemp__49->SetBinError(20,3);
   htemp__49->SetEntries(30);
   htemp__49->SetDirectory(0);
   htemp__49->SetStats(0);

   ci = TColor::GetColor("#ff0000");
   htemp__49->SetFillColor(ci);

   ci = TColor::GetColor("#ff0000");
   htemp__49->SetLineColor(ci);

   ci = TColor::GetColor("#ff0000");
   htemp__49->SetMarkerColor(ci);
   htemp__49->GetXaxis()->SetLabelFont(42);
   htemp__49->GetXaxis()->SetLabelSize(0.035);
   htemp__49->GetXaxis()->SetTitleSize(0.035);
   htemp__49->GetXaxis()->SetTitleFont(42);
   htemp__49->GetYaxis()->SetLabelFont(42);
   htemp__49->GetYaxis()->SetLabelSize(0.035);
   htemp__49->GetYaxis()->SetTitleSize(0.035);
   htemp__49->GetYaxis()->SetTitleFont(42);
   htemp__49->GetZaxis()->SetLabelFont(42);
   htemp__49->GetZaxis()->SetLabelSize(0.035);
   htemp__49->GetZaxis()->SetTitleSize(0.035);
   htemp__49->GetZaxis()->SetTitleFont(42);
   htemp__49->Draw("E1X0 same");
   Double_t xAxis118[29] = {2, 2.5, 3, 3.5, 4, 4.5, 5, 6, 7, 8, 10, 12, 14, 16, 18, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100, 120, 140}; 
   
   TH1F *htemp__50 = new TH1F("htemp__50"," ",28, xAxis118);
   htemp__50->SetEntries(30);
   htemp__50->SetDirectory(0);
   htemp__50->SetStats(0);

   ci = TColor::GetColor("#cc00ff");
   htemp__50->SetFillColor(ci);

   ci = TColor::GetColor("#cc00ff");
   htemp__50->SetLineColor(ci);

   ci = TColor::GetColor("#cc00ff");
   htemp__50->SetMarkerColor(ci);
   htemp__50->GetXaxis()->SetLabelFont(42);
   htemp__50->GetXaxis()->SetLabelSize(0.035);
   htemp__50->GetXaxis()->SetTitleSize(0.035);
   htemp__50->GetXaxis()->SetTitleFont(42);
   htemp__50->GetYaxis()->SetLabelFont(42);
   htemp__50->GetYaxis()->SetLabelSize(0.035);
   htemp__50->GetYaxis()->SetTitleSize(0.035);
   htemp__50->GetYaxis()->SetTitleFont(42);
   htemp__50->GetZaxis()->SetLabelFont(42);
   htemp__50->GetZaxis()->SetLabelSize(0.035);
   htemp__50->GetZaxis()->SetTitleSize(0.035);
   htemp__50->GetZaxis()->SetTitleFont(42);
   htemp__50->Draw("E1X0 same");
   Double_t xAxis119[29] = {2, 2.5, 3, 3.5, 4, 4.5, 5, 6, 7, 8, 10, 12, 14, 16, 18, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100, 120, 140}; 
   
   TH1F *htemp = new TH1F("htemp"," ",28, xAxis119);
   htemp->SetEntries(30);
   htemp->SetStats(0);

   ci = TColor::GetColor("#0000ff");
   htemp->SetFillColor(ci);

   ci = TColor::GetColor("#0000ff");
   htemp->SetLineColor(ci);

   ci = TColor::GetColor("#0000ff");
   htemp->SetMarkerColor(ci);
   htemp->GetXaxis()->SetLabelFont(42);
   htemp->GetXaxis()->SetLabelSize(0.035);
   htemp->GetXaxis()->SetTitleSize(0.035);
   htemp->GetXaxis()->SetTitleFont(42);
   htemp->GetYaxis()->SetLabelFont(42);
   htemp->GetYaxis()->SetLabelSize(0.035);
   htemp->GetYaxis()->SetTitleSize(0.035);
   htemp->GetYaxis()->SetTitleFont(42);
   htemp->GetZaxis()->SetLabelFont(42);
   htemp->GetZaxis()->SetLabelSize(0.035);
   htemp->GetZaxis()->SetTitleSize(0.035);
   htemp->GetZaxis()->SetTitleFont(42);
   htemp->Draw("E1X0 same");
   
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
   entry=leg->AddEntry("htemp","Prompt L1Mu, hit in GE11, ME11, GE21, ME21","f");

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
   entry=leg->AddEntry("htemp","Displaced L1Mu, hit in GE11, ME11, GE21, ME21 direction based","f");

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
   entry=leg->AddEntry("htemp","Displaced L1Mu, hit in GE11, ME11, GE21, ME21 direction based, medium veto","f");

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
