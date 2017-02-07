void CorrectStubMatching_CorrectME1_SimMuPt_ME1_ME2_ME3_eta12to14_dxy0to50()
{
//=========Macro generated from canvas: c/c
//=========  (Fri Jan 27 08:41:41 2017) by ROOT version6.06/09
   TCanvas *c = new TCanvas("c", "c",0,0,800,600);
   gStyle->SetOptStat(0);
   c->SetHighLightColor(2);
   c->Range(-7.553957,-0.1685185,52.39808,1.127778);
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
   
   TH1F *b1__7 = new TH1F("b1__7","           #scale[1.4]{#font[61]{CMS}} #font[52]{Simulation preliminary}                                                         14 TeV, 0 PU",50,0,50);
   b1__7->SetMinimum(0);
   b1__7->SetMaximum(1.05);
   b1__7->SetStats(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   b1__7->SetLineColor(ci);
   b1__7->GetXaxis()->SetTitle("True muon p_{T} [GeV]");
   b1__7->GetXaxis()->SetLabelFont(42);
   b1__7->GetXaxis()->SetLabelSize(0.05);
   b1__7->GetXaxis()->SetTitleSize(0.05);
   b1__7->GetXaxis()->SetTitleOffset(1.2);
   b1__7->GetXaxis()->SetTitleFont(42);
   b1__7->GetYaxis()->SetTitle("Trigger efficiency");
   b1__7->GetYaxis()->SetNdivisions(520);
   b1__7->GetYaxis()->SetLabelFont(42);
   b1__7->GetYaxis()->SetLabelSize(0.05);
   b1__7->GetYaxis()->SetTitleSize(0.05);
   b1__7->GetYaxis()->SetTitleOffset(1.2);
   b1__7->GetYaxis()->SetTitleFont(42);
   b1__7->GetZaxis()->SetLabelFont(42);
   b1__7->GetZaxis()->SetLabelSize(0.035);
   b1__7->GetZaxis()->SetTitleSize(0.035);
   b1__7->GetZaxis()->SetTitleFont(42);
   b1__7->Draw("");
   Double_t xAxis13[22] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20, 24, 28, 32, 36, 42, 50}; 
   
   TEfficiency * den_clone13 = new TEfficiency("den_clone","",21,xAxis13);
   
   den_clone13->SetConfidenceLevel(0.6826895);
   den_clone13->SetBetaAlpha(1);
   den_clone13->SetBetaBeta(1);
   den_clone13->SetWeight(1);
   den_clone13->SetStatisticOption(0);
   den_clone13->SetPosteriorMode(0);
   den_clone13->SetShortestInterval(0);
   den_clone13->SetTotalEvents(0,0);
   den_clone13->SetPassedEvents(0,0);
   den_clone13->SetTotalEvents(1,0);
   den_clone13->SetPassedEvents(1,0);
   den_clone13->SetTotalEvents(2,0);
   den_clone13->SetPassedEvents(2,0);
   den_clone13->SetTotalEvents(3,0);
   den_clone13->SetPassedEvents(3,0);
   den_clone13->SetTotalEvents(4,0);
   den_clone13->SetPassedEvents(4,0);
   den_clone13->SetTotalEvents(5,0);
   den_clone13->SetPassedEvents(5,0);
   den_clone13->SetTotalEvents(6,0);
   den_clone13->SetPassedEvents(6,0);
   den_clone13->SetTotalEvents(7,0);
   den_clone13->SetPassedEvents(7,0);
   den_clone13->SetTotalEvents(8,0);
   den_clone13->SetPassedEvents(8,0);
   den_clone13->SetTotalEvents(9,0);
   den_clone13->SetPassedEvents(9,0);
   den_clone13->SetTotalEvents(10,0);
   den_clone13->SetPassedEvents(10,0);
   den_clone13->SetTotalEvents(11,0);
   den_clone13->SetPassedEvents(11,0);
   den_clone13->SetTotalEvents(12,0);
   den_clone13->SetPassedEvents(12,0);
   den_clone13->SetTotalEvents(13,0);
   den_clone13->SetPassedEvents(13,0);
   den_clone13->SetTotalEvents(14,0);
   den_clone13->SetPassedEvents(14,0);
   den_clone13->SetTotalEvents(15,0);
   den_clone13->SetPassedEvents(15,0);
   den_clone13->SetTotalEvents(16,0);
   den_clone13->SetPassedEvents(16,0);
   den_clone13->SetTotalEvents(17,0);
   den_clone13->SetPassedEvents(17,0);
   den_clone13->SetTotalEvents(18,0);
   den_clone13->SetPassedEvents(18,0);
   den_clone13->SetTotalEvents(19,0);
   den_clone13->SetPassedEvents(19,0);
   den_clone13->SetTotalEvents(20,0);
   den_clone13->SetPassedEvents(20,0);
   den_clone13->SetTotalEvents(21,0);
   den_clone13->SetPassedEvents(21,0);
   den_clone13->SetTotalEvents(22,0);
   den_clone13->SetPassedEvents(22,0);
   den_clone13->SetFillColor(19);

   ci = TColor::GetColor("#0000ff");
   den_clone13->SetLineColor(ci);

   ci = TColor::GetColor("#0000ff");
   den_clone13->SetMarkerColor(ci);
   den_clone13->SetMarkerStyle(20);
   den_clone13->Draw("samep");
   Double_t xAxis14[22] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20, 24, 28, 32, 36, 42, 50}; 
   
   TEfficiency * den_clone14 = new TEfficiency("den_clone","",21,xAxis14);
   
   den_clone14->SetConfidenceLevel(0.6826895);
   den_clone14->SetBetaAlpha(1);
   den_clone14->SetBetaBeta(1);
   den_clone14->SetWeight(1);
   den_clone14->SetStatisticOption(0);
   den_clone14->SetPosteriorMode(0);
   den_clone14->SetShortestInterval(0);
   den_clone14->SetTotalEvents(0,0);
   den_clone14->SetPassedEvents(0,0);
   den_clone14->SetTotalEvents(1,0);
   den_clone14->SetPassedEvents(1,0);
   den_clone14->SetTotalEvents(2,0);
   den_clone14->SetPassedEvents(2,0);
   den_clone14->SetTotalEvents(3,0);
   den_clone14->SetPassedEvents(3,0);
   den_clone14->SetTotalEvents(4,0);
   den_clone14->SetPassedEvents(4,0);
   den_clone14->SetTotalEvents(5,0);
   den_clone14->SetPassedEvents(5,0);
   den_clone14->SetTotalEvents(6,0);
   den_clone14->SetPassedEvents(6,0);
   den_clone14->SetTotalEvents(7,0);
   den_clone14->SetPassedEvents(7,0);
   den_clone14->SetTotalEvents(8,0);
   den_clone14->SetPassedEvents(8,0);
   den_clone14->SetTotalEvents(9,0);
   den_clone14->SetPassedEvents(9,0);
   den_clone14->SetTotalEvents(10,0);
   den_clone14->SetPassedEvents(10,0);
   den_clone14->SetTotalEvents(11,0);
   den_clone14->SetPassedEvents(11,0);
   den_clone14->SetTotalEvents(12,0);
   den_clone14->SetPassedEvents(12,0);
   den_clone14->SetTotalEvents(13,0);
   den_clone14->SetPassedEvents(13,0);
   den_clone14->SetTotalEvents(14,0);
   den_clone14->SetPassedEvents(14,0);
   den_clone14->SetTotalEvents(15,0);
   den_clone14->SetPassedEvents(15,0);
   den_clone14->SetTotalEvents(16,0);
   den_clone14->SetPassedEvents(16,0);
   den_clone14->SetTotalEvents(17,0);
   den_clone14->SetPassedEvents(17,0);
   den_clone14->SetTotalEvents(18,0);
   den_clone14->SetPassedEvents(18,0);
   den_clone14->SetTotalEvents(19,0);
   den_clone14->SetPassedEvents(19,0);
   den_clone14->SetTotalEvents(20,0);
   den_clone14->SetPassedEvents(20,0);
   den_clone14->SetTotalEvents(21,0);
   den_clone14->SetPassedEvents(21,0);
   den_clone14->SetTotalEvents(22,0);
   den_clone14->SetPassedEvents(22,0);
   den_clone14->SetFillColor(19);

   ci = TColor::GetColor("#ff0000");
   den_clone14->SetLineColor(ci);

   ci = TColor::GetColor("#ff0000");
   den_clone14->SetMarkerColor(ci);
   den_clone14->SetMarkerStyle(21);
   den_clone14->Draw("samep");
   TLatex *   tex = new TLatex(0.5,0.6,"");
tex->SetNDC();
   tex->SetLineWidth(2);
   tex->Draw();
      tex = new TLatex(0.5,0.5,"1.2<|#eta|<1.4");
tex->SetNDC();
   tex->SetLineWidth(2);
   tex->Draw();
   
   TLegend *leg = new TLegend(0.5,0.2,0.9,0.45,NULL,"brNDC");
   leg->SetBorderSize(1);
   leg->SetTextSize(0.05);
   leg->SetLineColor(1);
   leg->SetLineStyle(1);
   leg->SetLineWidth(1);
   leg->SetFillColor(0);
   leg->SetFillStyle(1001);
   TLegendEntry *entry=leg->AddEntry("den_clone","|d_{xy}|<5 cm","lp");

   ci = TColor::GetColor("#0000ff");
   entry->SetLineColor(ci);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);

   ci = TColor::GetColor("#0000ff");
   entry->SetMarkerColor(ci);
   entry->SetMarkerStyle(20);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("den_clone","10<|d_{xy}|<50 cm","lp");

   ci = TColor::GetColor("#ff0000");
   entry->SetLineColor(ci);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);

   ci = TColor::GetColor("#ff0000");
   entry->SetMarkerColor(ci);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   leg->Draw();
   
   TPaveText *pt = new TPaveText(0,0.942,1,1,"blNDC");
   pt->SetName("title");
   pt->SetBorderSize(0);
   pt->SetFillColor(0);
   pt->SetFillStyle(0);
   pt->SetTextFont(42);
   AText = pt->AddText("           #scale[1.4]{#font[61]{CMS}} #font[52]{Simulation preliminary}                                                         14 TeV, 0 PU");
   pt->Draw();
   c->Modified();
   c->cd();
   c->SetSelected(c);
}
