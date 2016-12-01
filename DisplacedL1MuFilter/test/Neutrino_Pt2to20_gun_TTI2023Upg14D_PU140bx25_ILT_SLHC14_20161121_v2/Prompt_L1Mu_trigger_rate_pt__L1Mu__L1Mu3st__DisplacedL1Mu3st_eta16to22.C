{
//=========Macro generated from canvas: c/c
//=========  (Mon Nov 21 19:57:35 2016) by ROOT version5.34/07
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
   Double_t xAxis73[30] = {1, 2, 2.5, 3, 3.5, 4, 4.5, 5, 6, 7, 8, 10, 12, 14, 16, 18, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100, 120, 140}; 
   
   TH1F *b1 = new TH1F("b1","           #scale[1.4]{#font[61]{CMS}} #font[52]{Simulation preliminary}                                                           14 TeV, 140 PU",29, xAxis73);
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
   Double_t xAxis74[29] = {2, 2.5, 3, 3.5, 4, 4.5, 5, 6, 7, 8, 10, 12, 14, 16, 18, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100, 120, 140}; 
   
   TH1F *htemp__37 = new TH1F("htemp__37"," ",28, xAxis74);
   htemp__37->SetBinContent(1,2490);
   htemp__37->SetBinContent(2,2490);
   htemp__37->SetBinContent(3,1872);
   htemp__37->SetBinContent(4,1500);
   htemp__37->SetBinContent(5,1263);
   htemp__37->SetBinContent(6,999);
   htemp__37->SetBinContent(7,762);
   htemp__37->SetBinContent(8,399);
   htemp__37->SetBinContent(9,249);
   htemp__37->SetBinContent(10,180);
   htemp__37->SetBinContent(11,90);
   htemp__37->SetBinContent(12,66);
   htemp__37->SetBinContent(13,45);
   htemp__37->SetBinContent(14,33);
   htemp__37->SetBinContent(15,27);
   htemp__37->SetBinContent(16,24);
   htemp__37->SetBinContent(17,15);
   htemp__37->SetBinContent(18,6);
   htemp__37->SetBinContent(19,3);
   htemp__37->SetBinContent(20,3);
   htemp__37->SetBinError(1,86.42916);
   htemp__37->SetBinError(2,86.42916);
   htemp__37->SetBinError(3,74.93998);
   htemp__37->SetBinError(4,67.08204);
   htemp__37->SetBinError(5,61.55485);
   htemp__37->SetBinError(6,54.74486);
   htemp__37->SetBinError(7,47.81213);
   htemp__37->SetBinError(8,34.59769);
   htemp__37->SetBinError(9,27.3313);
   htemp__37->SetBinError(10,23.2379);
   htemp__37->SetBinError(11,16.43168);
   htemp__37->SetBinError(12,14.07125);
   htemp__37->SetBinError(13,11.61895);
   htemp__37->SetBinError(14,9.949874);
   htemp__37->SetBinError(15,9);
   htemp__37->SetBinError(16,8.485281);
   htemp__37->SetBinError(17,6.708204);
   htemp__37->SetBinError(18,4.242641);
   htemp__37->SetBinError(19,3);
   htemp__37->SetBinError(20,3);
   htemp__37->SetEntries(30);
   htemp__37->SetDirectory(0);
   htemp__37->SetStats(0);

   ci = TColor::GetColor("#ff0000");
   htemp__37->SetFillColor(ci);

   ci = TColor::GetColor("#000099");
   htemp__37->SetLineColor(ci);
   htemp__37->GetXaxis()->SetLabelFont(42);
   htemp__37->GetXaxis()->SetLabelSize(0.035);
   htemp__37->GetXaxis()->SetTitleSize(0.035);
   htemp__37->GetXaxis()->SetTitleFont(42);
   htemp__37->GetYaxis()->SetLabelFont(42);
   htemp__37->GetYaxis()->SetLabelSize(0.035);
   htemp__37->GetYaxis()->SetTitleSize(0.035);
   htemp__37->GetYaxis()->SetTitleFont(42);
   htemp__37->GetZaxis()->SetLabelFont(42);
   htemp__37->GetZaxis()->SetLabelSize(0.035);
   htemp__37->GetZaxis()->SetTitleSize(0.035);
   htemp__37->GetZaxis()->SetTitleFont(42);
   htemp__37->Draw("e3 same");
   Double_t xAxis75[29] = {2, 2.5, 3, 3.5, 4, 4.5, 5, 6, 7, 8, 10, 12, 14, 16, 18, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100, 120, 140}; 
   
   TH1F *htemp__38 = new TH1F("htemp__38"," ",28, xAxis75);
   htemp__38->SetEntries(30);
   htemp__38->SetDirectory(0);
   htemp__38->SetStats(0);

   ci = TColor::GetColor("#cc00ff");
   htemp__38->SetFillColor(ci);

   ci = TColor::GetColor("#000099");
   htemp__38->SetLineColor(ci);
   htemp__38->GetXaxis()->SetLabelFont(42);
   htemp__38->GetXaxis()->SetLabelSize(0.035);
   htemp__38->GetXaxis()->SetTitleSize(0.035);
   htemp__38->GetXaxis()->SetTitleFont(42);
   htemp__38->GetYaxis()->SetLabelFont(42);
   htemp__38->GetYaxis()->SetLabelSize(0.035);
   htemp__38->GetYaxis()->SetTitleSize(0.035);
   htemp__38->GetYaxis()->SetTitleFont(42);
   htemp__38->GetZaxis()->SetLabelFont(42);
   htemp__38->GetZaxis()->SetLabelSize(0.035);
   htemp__38->GetZaxis()->SetTitleSize(0.035);
   htemp__38->GetZaxis()->SetTitleFont(42);
   htemp__38->Draw("e3 same");
   Double_t xAxis76[29] = {2, 2.5, 3, 3.5, 4, 4.5, 5, 6, 7, 8, 10, 12, 14, 16, 18, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100, 120, 140}; 
   
   TH1F *htemp = new TH1F("htemp"," ",28, xAxis76);
   htemp->SetEntries(30);
   htemp->SetStats(0);

   ci = TColor::GetColor("#0000ff");
   htemp->SetFillColor(ci);

   ci = TColor::GetColor("#000099");
   htemp->SetLineColor(ci);
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
   htemp->Draw("e3 same");
   
   TLegend *leg = new TLegend(0.15,0.2,0.5,0.35,NULL,"brNDC");
   leg->SetBorderSize(0);
   leg->SetTextSize(0.04);
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
   entry=leg->AddEntry("htemp","Prompt L1Mu","f");

   ci = TColor::GetColor("#ff0000");
   entry->SetFillColor(ci);
   entry->SetFillStyle(1001);

   ci = TColor::GetColor("#000099");
   entry->SetLineColor(ci);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry=leg->AddEntry("htemp","Prompt L1Mu, hit in ME1, ME2, ME3","f");

   ci = TColor::GetColor("#cc00ff");
   entry->SetFillColor(ci);
   entry->SetFillStyle(1001);

   ci = TColor::GetColor("#000099");
   entry->SetLineColor(ci);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry=leg->AddEntry("htemp","Displaced L1Mu, hit in ME1, ME2, ME3 position based","f");

   ci = TColor::GetColor("#0000ff");
   entry->SetFillColor(ci);
   entry->SetFillStyle(1001);

   ci = TColor::GetColor("#000099");
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
