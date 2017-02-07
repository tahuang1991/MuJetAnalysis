void CorrectStubMatching_CorrectME2_SimMuPt_ME1_ME2_ME3_eta12to14_dxy0to50()
{
//=========Macro generated from canvas: c/c
//=========  (Fri Jan 27 08:41:44 2017) by ROOT version6.06/09
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
   
   TH1F *b1__13 = new TH1F("b1__13","           #scale[1.4]{#font[61]{CMS}} #font[52]{Simulation preliminary}                                                         14 TeV, 0 PU",50,0,50);
   b1__13->SetMinimum(0);
   b1__13->SetMaximum(1.05);
   b1__13->SetStats(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   b1__13->SetLineColor(ci);
   b1__13->GetXaxis()->SetTitle("True muon p_{T} [GeV]");
   b1__13->GetXaxis()->SetLabelFont(42);
   b1__13->GetXaxis()->SetLabelSize(0.05);
   b1__13->GetXaxis()->SetTitleSize(0.05);
   b1__13->GetXaxis()->SetTitleOffset(1.2);
   b1__13->GetXaxis()->SetTitleFont(42);
   b1__13->GetYaxis()->SetTitle("Trigger efficiency");
   b1__13->GetYaxis()->SetNdivisions(520);
   b1__13->GetYaxis()->SetLabelFont(42);
   b1__13->GetYaxis()->SetLabelSize(0.05);
   b1__13->GetYaxis()->SetTitleSize(0.05);
   b1__13->GetYaxis()->SetTitleOffset(1.2);
   b1__13->GetYaxis()->SetTitleFont(42);
   b1__13->GetZaxis()->SetLabelFont(42);
   b1__13->GetZaxis()->SetLabelSize(0.035);
   b1__13->GetZaxis()->SetTitleSize(0.035);
   b1__13->GetZaxis()->SetTitleFont(42);
   b1__13->Draw("");
   Double_t xAxis25[22] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20, 24, 28, 32, 36, 42, 50}; 
   
   TEfficiency * den_clone25 = new TEfficiency("den_clone","",21,xAxis25);
   
   den_clone25->SetConfidenceLevel(0.6826895);
   den_clone25->SetBetaAlpha(1);
   den_clone25->SetBetaBeta(1);
   den_clone25->SetWeight(1);
   den_clone25->SetStatisticOption(0);
   den_clone25->SetPosteriorMode(0);
   den_clone25->SetShortestInterval(0);
   den_clone25->SetTotalEvents(0,0);
   den_clone25->SetPassedEvents(0,0);
   den_clone25->SetTotalEvents(1,0);
   den_clone25->SetPassedEvents(1,0);
   den_clone25->SetTotalEvents(2,0);
   den_clone25->SetPassedEvents(2,0);
   den_clone25->SetTotalEvents(3,0);
   den_clone25->SetPassedEvents(3,0);
   den_clone25->SetTotalEvents(4,0);
   den_clone25->SetPassedEvents(4,0);
   den_clone25->SetTotalEvents(5,0);
   den_clone25->SetPassedEvents(5,0);
   den_clone25->SetTotalEvents(6,0);
   den_clone25->SetPassedEvents(6,0);
   den_clone25->SetTotalEvents(7,0);
   den_clone25->SetPassedEvents(7,0);
   den_clone25->SetTotalEvents(8,0);
   den_clone25->SetPassedEvents(8,0);
   den_clone25->SetTotalEvents(9,0);
   den_clone25->SetPassedEvents(9,0);
   den_clone25->SetTotalEvents(10,0);
   den_clone25->SetPassedEvents(10,0);
   den_clone25->SetTotalEvents(11,0);
   den_clone25->SetPassedEvents(11,0);
   den_clone25->SetTotalEvents(12,0);
   den_clone25->SetPassedEvents(12,0);
   den_clone25->SetTotalEvents(13,0);
   den_clone25->SetPassedEvents(13,0);
   den_clone25->SetTotalEvents(14,0);
   den_clone25->SetPassedEvents(14,0);
   den_clone25->SetTotalEvents(15,0);
   den_clone25->SetPassedEvents(15,0);
   den_clone25->SetTotalEvents(16,0);
   den_clone25->SetPassedEvents(16,0);
   den_clone25->SetTotalEvents(17,0);
   den_clone25->SetPassedEvents(17,0);
   den_clone25->SetTotalEvents(18,0);
   den_clone25->SetPassedEvents(18,0);
   den_clone25->SetTotalEvents(19,0);
   den_clone25->SetPassedEvents(19,0);
   den_clone25->SetTotalEvents(20,0);
   den_clone25->SetPassedEvents(20,0);
   den_clone25->SetTotalEvents(21,0);
   den_clone25->SetPassedEvents(21,0);
   den_clone25->SetTotalEvents(22,0);
   den_clone25->SetPassedEvents(22,0);
   den_clone25->SetFillColor(19);

   ci = TColor::GetColor("#0000ff");
   den_clone25->SetLineColor(ci);

   ci = TColor::GetColor("#0000ff");
   den_clone25->SetMarkerColor(ci);
   den_clone25->SetMarkerStyle(20);
   den_clone25->Draw("samep");
   Double_t xAxis26[22] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20, 24, 28, 32, 36, 42, 50}; 
   
   TEfficiency * den_clone26 = new TEfficiency("den_clone","",21,xAxis26);
   
   den_clone26->SetConfidenceLevel(0.6826895);
   den_clone26->SetBetaAlpha(1);
   den_clone26->SetBetaBeta(1);
   den_clone26->SetWeight(1);
   den_clone26->SetStatisticOption(0);
   den_clone26->SetPosteriorMode(0);
   den_clone26->SetShortestInterval(0);
   den_clone26->SetTotalEvents(0,0);
   den_clone26->SetPassedEvents(0,0);
   den_clone26->SetTotalEvents(1,0);
   den_clone26->SetPassedEvents(1,0);
   den_clone26->SetTotalEvents(2,0);
   den_clone26->SetPassedEvents(2,0);
   den_clone26->SetTotalEvents(3,0);
   den_clone26->SetPassedEvents(3,0);
   den_clone26->SetTotalEvents(4,0);
   den_clone26->SetPassedEvents(4,0);
   den_clone26->SetTotalEvents(5,0);
   den_clone26->SetPassedEvents(5,0);
   den_clone26->SetTotalEvents(6,0);
   den_clone26->SetPassedEvents(6,0);
   den_clone26->SetTotalEvents(7,0);
   den_clone26->SetPassedEvents(7,0);
   den_clone26->SetTotalEvents(8,0);
   den_clone26->SetPassedEvents(8,0);
   den_clone26->SetTotalEvents(9,0);
   den_clone26->SetPassedEvents(9,0);
   den_clone26->SetTotalEvents(10,0);
   den_clone26->SetPassedEvents(10,0);
   den_clone26->SetTotalEvents(11,0);
   den_clone26->SetPassedEvents(11,0);
   den_clone26->SetTotalEvents(12,0);
   den_clone26->SetPassedEvents(12,0);
   den_clone26->SetTotalEvents(13,0);
   den_clone26->SetPassedEvents(13,0);
   den_clone26->SetTotalEvents(14,0);
   den_clone26->SetPassedEvents(14,0);
   den_clone26->SetTotalEvents(15,0);
   den_clone26->SetPassedEvents(15,0);
   den_clone26->SetTotalEvents(16,0);
   den_clone26->SetPassedEvents(16,0);
   den_clone26->SetTotalEvents(17,0);
   den_clone26->SetPassedEvents(17,0);
   den_clone26->SetTotalEvents(18,0);
   den_clone26->SetPassedEvents(18,0);
   den_clone26->SetTotalEvents(19,0);
   den_clone26->SetPassedEvents(19,0);
   den_clone26->SetTotalEvents(20,0);
   den_clone26->SetPassedEvents(20,0);
   den_clone26->SetTotalEvents(21,0);
   den_clone26->SetPassedEvents(21,0);
   den_clone26->SetTotalEvents(22,0);
   den_clone26->SetPassedEvents(22,0);
   den_clone26->SetFillColor(19);

   ci = TColor::GetColor("#ff0000");
   den_clone26->SetLineColor(ci);

   ci = TColor::GetColor("#ff0000");
   den_clone26->SetMarkerColor(ci);
   den_clone26->SetMarkerStyle(21);
   den_clone26->Draw("samep");
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
