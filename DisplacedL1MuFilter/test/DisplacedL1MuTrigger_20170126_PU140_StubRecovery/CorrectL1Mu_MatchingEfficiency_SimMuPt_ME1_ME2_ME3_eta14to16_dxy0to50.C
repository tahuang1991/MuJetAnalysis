void CorrectL1Mu_MatchingEfficiency_SimMuPt_ME1_ME2_ME3_eta14to16_dxy0to50()
{
//=========Macro generated from canvas: c/c
//=========  (Fri Jan 27 08:41:38 2017) by ROOT version6.06/09
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
   
   TH1F *b1__2 = new TH1F("b1__2","           #scale[1.4]{#font[61]{CMS}} #font[52]{Simulation preliminary}                                                         14 TeV, 0 PU",50,0,50);
   b1__2->SetMinimum(0);
   b1__2->SetMaximum(1.05);
   b1__2->SetStats(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   b1__2->SetLineColor(ci);
   b1__2->GetXaxis()->SetTitle("True muon p_{T} [GeV]");
   b1__2->GetXaxis()->SetLabelFont(42);
   b1__2->GetXaxis()->SetLabelSize(0.05);
   b1__2->GetXaxis()->SetTitleSize(0.05);
   b1__2->GetXaxis()->SetTitleOffset(1.2);
   b1__2->GetXaxis()->SetTitleFont(42);
   b1__2->GetYaxis()->SetTitle("Trigger efficiency");
   b1__2->GetYaxis()->SetNdivisions(520);
   b1__2->GetYaxis()->SetLabelFont(42);
   b1__2->GetYaxis()->SetLabelSize(0.05);
   b1__2->GetYaxis()->SetTitleSize(0.05);
   b1__2->GetYaxis()->SetTitleOffset(1.2);
   b1__2->GetYaxis()->SetTitleFont(42);
   b1__2->GetZaxis()->SetLabelFont(42);
   b1__2->GetZaxis()->SetLabelSize(0.035);
   b1__2->GetZaxis()->SetTitleSize(0.035);
   b1__2->GetZaxis()->SetTitleFont(42);
   b1__2->Draw("");
   Double_t xAxis3[22] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20, 24, 28, 32, 36, 42, 50}; 
   
   TEfficiency * den_clone3 = new TEfficiency("den_clone","",21,xAxis3);
   
   den_clone3->SetConfidenceLevel(0.6826895);
   den_clone3->SetBetaAlpha(1);
   den_clone3->SetBetaBeta(1);
   den_clone3->SetWeight(1);
   den_clone3->SetStatisticOption(0);
   den_clone3->SetPosteriorMode(0);
   den_clone3->SetShortestInterval(0);
   den_clone3->SetTotalEvents(0,0);
   den_clone3->SetPassedEvents(0,0);
   den_clone3->SetTotalEvents(1,0);
   den_clone3->SetPassedEvents(1,0);
   den_clone3->SetTotalEvents(2,0);
   den_clone3->SetPassedEvents(2,0);
   den_clone3->SetTotalEvents(3,141);
   den_clone3->SetPassedEvents(3,134);
   den_clone3->SetTotalEvents(4,552);
   den_clone3->SetPassedEvents(4,544);
   den_clone3->SetTotalEvents(5,640);
   den_clone3->SetPassedEvents(5,634);
   den_clone3->SetTotalEvents(6,759);
   den_clone3->SetPassedEvents(6,753);
   den_clone3->SetTotalEvents(7,815);
   den_clone3->SetPassedEvents(7,809);
   den_clone3->SetTotalEvents(8,783);
   den_clone3->SetPassedEvents(8,775);
   den_clone3->SetTotalEvents(9,863);
   den_clone3->SetPassedEvents(9,857);
   den_clone3->SetTotalEvents(10,908);
   den_clone3->SetPassedEvents(10,896);
   den_clone3->SetTotalEvents(11,1557);
   den_clone3->SetPassedEvents(11,1548);
   den_clone3->SetTotalEvents(12,1425);
   den_clone3->SetPassedEvents(12,1417);
   den_clone3->SetTotalEvents(13,1169);
   den_clone3->SetPassedEvents(13,1165);
   den_clone3->SetTotalEvents(14,1052);
   den_clone3->SetPassedEvents(14,1044);
   den_clone3->SetTotalEvents(15,874);
   den_clone3->SetPassedEvents(15,869);
   den_clone3->SetTotalEvents(16,1351);
   den_clone3->SetPassedEvents(16,1347);
   den_clone3->SetTotalEvents(17,939);
   den_clone3->SetPassedEvents(17,933);
   den_clone3->SetTotalEvents(18,568);
   den_clone3->SetPassedEvents(18,566);
   den_clone3->SetTotalEvents(19,411);
   den_clone3->SetPassedEvents(19,409);
   den_clone3->SetTotalEvents(20,315);
   den_clone3->SetPassedEvents(20,314);
   den_clone3->SetTotalEvents(21,142);
   den_clone3->SetPassedEvents(21,142);
   den_clone3->SetTotalEvents(22,45);
   den_clone3->SetPassedEvents(22,45);
   den_clone3->SetFillColor(19);

   ci = TColor::GetColor("#0000ff");
   den_clone3->SetLineColor(ci);

   ci = TColor::GetColor("#0000ff");
   den_clone3->SetMarkerColor(ci);
   den_clone3->SetMarkerStyle(20);
   den_clone3->Draw("samep");
   Double_t xAxis4[22] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20, 24, 28, 32, 36, 42, 50}; 
   
   TEfficiency * den_clone4 = new TEfficiency("den_clone","",21,xAxis4);
   
   den_clone4->SetConfidenceLevel(0.6826895);
   den_clone4->SetBetaAlpha(1);
   den_clone4->SetBetaBeta(1);
   den_clone4->SetWeight(1);
   den_clone4->SetStatisticOption(0);
   den_clone4->SetPosteriorMode(0);
   den_clone4->SetShortestInterval(0);
   den_clone4->SetTotalEvents(0,0);
   den_clone4->SetPassedEvents(0,0);
   den_clone4->SetTotalEvents(1,0);
   den_clone4->SetPassedEvents(1,0);
   den_clone4->SetTotalEvents(2,1);
   den_clone4->SetPassedEvents(2,1);
   den_clone4->SetTotalEvents(3,26);
   den_clone4->SetPassedEvents(3,26);
   den_clone4->SetTotalEvents(4,114);
   den_clone4->SetPassedEvents(4,110);
   den_clone4->SetTotalEvents(5,167);
   den_clone4->SetPassedEvents(5,163);
   den_clone4->SetTotalEvents(6,204);
   den_clone4->SetPassedEvents(6,202);
   den_clone4->SetTotalEvents(7,220);
   den_clone4->SetPassedEvents(7,219);
   den_clone4->SetTotalEvents(8,205);
   den_clone4->SetPassedEvents(8,202);
   den_clone4->SetTotalEvents(9,248);
   den_clone4->SetPassedEvents(9,244);
   den_clone4->SetTotalEvents(10,206);
   den_clone4->SetPassedEvents(10,203);
   den_clone4->SetTotalEvents(11,420);
   den_clone4->SetPassedEvents(11,416);
   den_clone4->SetTotalEvents(12,357);
   den_clone4->SetPassedEvents(12,354);
   den_clone4->SetTotalEvents(13,282);
   den_clone4->SetPassedEvents(13,280);
   den_clone4->SetTotalEvents(14,238);
   den_clone4->SetPassedEvents(14,235);
   den_clone4->SetTotalEvents(15,187);
   den_clone4->SetPassedEvents(15,186);
   den_clone4->SetTotalEvents(16,264);
   den_clone4->SetPassedEvents(16,262);
   den_clone4->SetTotalEvents(17,212);
   den_clone4->SetPassedEvents(17,210);
   den_clone4->SetTotalEvents(18,101);
   den_clone4->SetPassedEvents(18,99);
   den_clone4->SetTotalEvents(19,54);
   den_clone4->SetPassedEvents(19,53);
   den_clone4->SetTotalEvents(20,46);
   den_clone4->SetPassedEvents(20,46);
   den_clone4->SetTotalEvents(21,19);
   den_clone4->SetPassedEvents(21,18);
   den_clone4->SetTotalEvents(22,2);
   den_clone4->SetPassedEvents(22,2);
   den_clone4->SetFillColor(19);

   ci = TColor::GetColor("#ff0000");
   den_clone4->SetLineColor(ci);

   ci = TColor::GetColor("#ff0000");
   den_clone4->SetMarkerColor(ci);
   den_clone4->SetMarkerStyle(21);
   den_clone4->Draw("samep");
   TLatex *   tex = new TLatex(0.5,0.6,"");
tex->SetNDC();
   tex->SetLineWidth(2);
   tex->Draw();
      tex = new TLatex(0.5,0.5,"1.4<|#eta|<1.6");
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
