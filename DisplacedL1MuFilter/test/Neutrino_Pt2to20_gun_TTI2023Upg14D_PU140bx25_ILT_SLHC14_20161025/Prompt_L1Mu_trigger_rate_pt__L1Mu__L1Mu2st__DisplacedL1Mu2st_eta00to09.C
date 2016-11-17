{
//=========Macro generated from canvas: c/c
//=========  (Tue Oct 25 23:12:08 2016) by ROOT version5.34/07
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
   Double_t xAxis69[29] = {2, 2.5, 3, 3.5, 4, 4.5, 5, 6, 7, 8, 10, 12, 14, 16, 18, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100, 120, 140}; 
   
   TH1F *b1 = new TH1F("b1","                                                                                        14TeV, PU140",28, xAxis69);
   b1->SetMinimum(0.2);
   b1->SetMaximum(10000);
   b1->SetStats(0);

   Int_t ci;   // for color index setting
   ci = TColor::GetColor("#000099");
   b1->SetLineColor(ci);
   b1->GetXaxis()->SetTitle("L1 trigger p_{T} threshold [GeV]");
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
   Double_t xAxis70[29] = {2, 2.5, 3, 3.5, 4, 4.5, 5, 6, 7, 8, 10, 12, 14, 16, 18, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100, 120, 140}; 
   
   TH1F *htemp__35 = new TH1F("htemp__35"," ",28, xAxis70);
   htemp__35->SetEntries(30);
   htemp__35->SetDirectory(0);
   htemp__35->SetStats(0);

   ci = TColor::GetColor("#ff0000");
   htemp__35->SetFillColor(ci);

   ci = TColor::GetColor("#000099");
   htemp__35->SetLineColor(ci);
   htemp__35->GetXaxis()->SetLabelFont(42);
   htemp__35->GetXaxis()->SetLabelSize(0.035);
   htemp__35->GetXaxis()->SetTitleSize(0.035);
   htemp__35->GetXaxis()->SetTitleFont(42);
   htemp__35->GetYaxis()->SetLabelFont(42);
   htemp__35->GetYaxis()->SetLabelSize(0.035);
   htemp__35->GetYaxis()->SetTitleSize(0.035);
   htemp__35->GetYaxis()->SetTitleFont(42);
   htemp__35->GetZaxis()->SetLabelFont(42);
   htemp__35->GetZaxis()->SetLabelSize(0.035);
   htemp__35->GetZaxis()->SetTitleSize(0.035);
   htemp__35->GetZaxis()->SetTitleFont(42);
   htemp__35->Draw("e3 same");
   Double_t xAxis71[29] = {2, 2.5, 3, 3.5, 4, 4.5, 5, 6, 7, 8, 10, 12, 14, 16, 18, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100, 120, 140}; 
   
   TH1F *htemp__36 = new TH1F("htemp__36"," ",28, xAxis71);
   htemp__36->SetEntries(30);
   htemp__36->SetDirectory(0);
   htemp__36->SetStats(0);

   ci = TColor::GetColor("#cc00ff");
   htemp__36->SetFillColor(ci);

   ci = TColor::GetColor("#000099");
   htemp__36->SetLineColor(ci);
   htemp__36->GetXaxis()->SetLabelFont(42);
   htemp__36->GetXaxis()->SetLabelSize(0.035);
   htemp__36->GetXaxis()->SetTitleSize(0.035);
   htemp__36->GetXaxis()->SetTitleFont(42);
   htemp__36->GetYaxis()->SetLabelFont(42);
   htemp__36->GetYaxis()->SetLabelSize(0.035);
   htemp__36->GetYaxis()->SetTitleSize(0.035);
   htemp__36->GetYaxis()->SetTitleFont(42);
   htemp__36->GetZaxis()->SetLabelFont(42);
   htemp__36->GetZaxis()->SetLabelSize(0.035);
   htemp__36->GetZaxis()->SetTitleSize(0.035);
   htemp__36->GetZaxis()->SetTitleFont(42);
   htemp__36->Draw("e3 same");
   Double_t xAxis72[29] = {2, 2.5, 3, 3.5, 4, 4.5, 5, 6, 7, 8, 10, 12, 14, 16, 18, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100, 120, 140}; 
   
   TH1F *htemp = new TH1F("htemp"," ",28, xAxis72);
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
   TLatex *   tex = new TLatex(0.52,0.87,"CMS PhaseII Simulation");
tex->SetNDC();
   tex->SetLineWidth(2);
   tex->Draw();
   
   TLegend *leg = new TLegend(0.15,0.2,0.5,0.35,NULL,"brNDC");
   leg->SetBorderSize(0);
   leg->SetTextSize(0.04);
   leg->SetLineColor(1);
   leg->SetLineStyle(1);
   leg->SetLineWidth(1);
   leg->SetFillColor(0);
   leg->SetFillStyle(0);
   TLegendEntry *entry=leg->AddEntry("NULL","0.0<|#eta|<0.9","h");
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
   entry=leg->AddEntry("htemp","Prompt L1Mu, hit in MB1, MB4","f");

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
   entry=leg->AddEntry("htemp","Displaced L1Mu, hit in MB1, MB4, direction based","f");

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
   text = pt->AddText("                                                                                        14TeV, PU140");
   pt->Draw();
   c->Modified();
   c->cd();
   c->SetSelected(c);
}
