{
//=========Macro generated from canvas: c/c
//=========  (Tue Jan 24 14:47:07 2017) by ROOT version5.34/07
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
   Double_t xAxis176[30] = {1, 2, 2.5, 3, 3.5, 4, 4.5, 5, 6, 7, 8, 10, 12, 14, 16, 18, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100, 120, 140}; 
   
   TH1F *b1 = new TH1F("b1","           #scale[1.4]{#font[61]{CMS}} #font[52]{Simulation preliminary}                                                           14 TeV, 140 PU",29, xAxis176);
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
   Double_t xAxis177[29] = {2, 2.5, 3, 3.5, 4, 4.5, 5, 6, 7, 8, 10, 12, 14, 16, 18, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100, 120, 140}; 
   
   TH1F *htemp__49 = new TH1F("htemp__49"," ",28, xAxis177);
   htemp__49->SetEntries(30);
   htemp__49->SetDirectory(0);
   htemp__49->SetStats(0);

   ci = TColor::GetColor("#ff0000");
   htemp__49->SetLineColor(ci);

   ci = TColor::GetColor("#ff0000");
   htemp__49->SetMarkerColor(ci);
   htemp__49->SetMarkerStyle(20);
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
   Double_t xAxis178[29] = {2, 2.5, 3, 3.5, 4, 4.5, 5, 6, 7, 8, 10, 12, 14, 16, 18, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100, 120, 140}; 
   
   TH1F *htemp__50 = new TH1F("htemp__50"," ",28, xAxis178);
   htemp__50->SetEntries(41);
   htemp__50->SetDirectory(0);
   htemp__50->SetStats(0);

   ci = TColor::GetColor("#cc00ff");
   htemp__50->SetLineColor(ci);

   ci = TColor::GetColor("#cc00ff");
   htemp__50->SetMarkerColor(ci);
   htemp__50->SetMarkerStyle(21);
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
   TLatex *   tex = new TLatex(0.6,0.8,"#font[41]{Note: p_{T,min}^{hybrid} = 5 GeV}");
tex->SetNDC();
   tex->SetLineWidth(2);
   tex->Draw();
   Double_t xAxis179[29] = {2, 2.5, 3, 3.5, 4, 4.5, 5, 6, 7, 8, 10, 12, 14, 16, 18, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100, 120, 140}; 
   
   TH1F *htemp = new TH1F("htemp"," ",28, xAxis179);
   htemp->SetEntries(41);
   htemp->SetStats(0);

   ci = TColor::GetColor("#0000ff");
   htemp->SetLineColor(ci);

   ci = TColor::GetColor("#0000ff");
   htemp->SetMarkerColor(ci);
   htemp->SetMarkerStyle(22);
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
   TLegendEntry *entry=leg->AddEntry("NULL","1.6<|#eta|<2.2","h");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("htemp","Prompt L1Mu, hit in ME1, ME2, ME3","p");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);

   ci = TColor::GetColor("#ff0000");
   entry->SetMarkerColor(ci);
   entry->SetMarkerStyle(20);
   entry->SetMarkerSize(1);
   entry=leg->AddEntry("htemp","Displaced L1Mu, hit in ME1, ME2, ME3 hybrid based","p");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);

   ci = TColor::GetColor("#cc00ff");
   entry->SetMarkerColor(ci);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry=leg->AddEntry("htemp","Displaced L1Mu, hit in ME1, ME2, ME3 hybrid based, loose veto","p");
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
   text = pt->AddText("           #scale[1.4]{#font[61]{CMS}} #font[52]{Simulation preliminary}                                                           14 TeV, 140 PU");
   pt->Draw();
   c->Modified();
   c->cd();
   c->SetSelected(c);
}
