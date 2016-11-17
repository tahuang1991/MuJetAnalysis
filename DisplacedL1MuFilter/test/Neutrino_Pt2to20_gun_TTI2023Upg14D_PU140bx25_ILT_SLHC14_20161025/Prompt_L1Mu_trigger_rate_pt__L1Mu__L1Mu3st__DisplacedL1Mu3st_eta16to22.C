{
//=========Macro generated from canvas: c/c
//=========  (Tue Oct 25 23:12:07 2016) by ROOT version5.34/07
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
   Double_t xAxis61[29] = {2, 2.5, 3, 3.5, 4, 4.5, 5, 6, 7, 8, 10, 12, 14, 16, 18, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100, 120, 140}; 
   
   TH1F *b1 = new TH1F("b1","                                                                                        14TeV, PU140",28, xAxis61);
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
   Double_t xAxis62[29] = {2, 2.5, 3, 3.5, 4, 4.5, 5, 6, 7, 8, 10, 12, 14, 16, 18, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100, 120, 140}; 
   
   TH1F *htemp__31 = new TH1F("htemp__31"," ",28, xAxis62);
   htemp__31->SetEntries(30);
   htemp__31->SetDirectory(0);
   htemp__31->SetStats(0);

   ci = TColor::GetColor("#ff0000");
   htemp__31->SetFillColor(ci);

   ci = TColor::GetColor("#000099");
   htemp__31->SetLineColor(ci);
   htemp__31->GetXaxis()->SetLabelFont(42);
   htemp__31->GetXaxis()->SetLabelSize(0.035);
   htemp__31->GetXaxis()->SetTitleSize(0.035);
   htemp__31->GetXaxis()->SetTitleFont(42);
   htemp__31->GetYaxis()->SetLabelFont(42);
   htemp__31->GetYaxis()->SetLabelSize(0.035);
   htemp__31->GetYaxis()->SetTitleSize(0.035);
   htemp__31->GetYaxis()->SetTitleFont(42);
   htemp__31->GetZaxis()->SetLabelFont(42);
   htemp__31->GetZaxis()->SetLabelSize(0.035);
   htemp__31->GetZaxis()->SetTitleSize(0.035);
   htemp__31->GetZaxis()->SetTitleFont(42);
   htemp__31->Draw("e3 same");
   Double_t xAxis63[29] = {2, 2.5, 3, 3.5, 4, 4.5, 5, 6, 7, 8, 10, 12, 14, 16, 18, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100, 120, 140}; 
   
   TH1F *htemp__32 = new TH1F("htemp__32"," ",28, xAxis63);
   htemp__32->SetEntries(30);
   htemp__32->SetDirectory(0);
   htemp__32->SetStats(0);

   ci = TColor::GetColor("#cc00ff");
   htemp__32->SetFillColor(ci);

   ci = TColor::GetColor("#000099");
   htemp__32->SetLineColor(ci);
   htemp__32->GetXaxis()->SetLabelFont(42);
   htemp__32->GetXaxis()->SetLabelSize(0.035);
   htemp__32->GetXaxis()->SetTitleSize(0.035);
   htemp__32->GetXaxis()->SetTitleFont(42);
   htemp__32->GetYaxis()->SetLabelFont(42);
   htemp__32->GetYaxis()->SetLabelSize(0.035);
   htemp__32->GetYaxis()->SetTitleSize(0.035);
   htemp__32->GetYaxis()->SetTitleFont(42);
   htemp__32->GetZaxis()->SetLabelFont(42);
   htemp__32->GetZaxis()->SetLabelSize(0.035);
   htemp__32->GetZaxis()->SetTitleSize(0.035);
   htemp__32->GetZaxis()->SetTitleFont(42);
   htemp__32->Draw("e3 same");
   Double_t xAxis64[29] = {2, 2.5, 3, 3.5, 4, 4.5, 5, 6, 7, 8, 10, 12, 14, 16, 18, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100, 120, 140}; 
   
   TH1F *htemp = new TH1F("htemp"," ",28, xAxis64);
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
   entry=leg->AddEntry("htemp","Displaced L1Mu, hit in ME1, ME2, ME3, position based","f");

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
