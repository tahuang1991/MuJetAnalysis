void CorrectL1Mu_MatchingEfficiency_SimMuPt_ME1_ME2_ME3_eta20to22_dxy0to50()
{
//=========Macro generated from canvas: c/c
//=========  (Fri Jan 27 08:41:40 2017) by ROOT version6.06/09
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
   
   TH1F *b1__5 = new TH1F("b1__5","           #scale[1.4]{#font[61]{CMS}} #font[52]{Simulation preliminary}                                                         14 TeV, 0 PU",50,0,50);
   b1__5->SetMinimum(0);
   b1__5->SetMaximum(1.05);
   b1__5->SetStats(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   b1__5->SetLineColor(ci);
   b1__5->GetXaxis()->SetTitle("True muon p_{T} [GeV]");
   b1__5->GetXaxis()->SetLabelFont(42);
   b1__5->GetXaxis()->SetLabelSize(0.05);
   b1__5->GetXaxis()->SetTitleSize(0.05);
   b1__5->GetXaxis()->SetTitleOffset(1.2);
   b1__5->GetXaxis()->SetTitleFont(42);
   b1__5->GetYaxis()->SetTitle("Trigger efficiency");
   b1__5->GetYaxis()->SetNdivisions(520);
   b1__5->GetYaxis()->SetLabelFont(42);
   b1__5->GetYaxis()->SetLabelSize(0.05);
   b1__5->GetYaxis()->SetTitleSize(0.05);
   b1__5->GetYaxis()->SetTitleOffset(1.2);
   b1__5->GetYaxis()->SetTitleFont(42);
   b1__5->GetZaxis()->SetLabelFont(42);
   b1__5->GetZaxis()->SetLabelSize(0.035);
   b1__5->GetZaxis()->SetTitleSize(0.035);
   b1__5->GetZaxis()->SetTitleFont(42);
   b1__5->Draw("");
   Double_t xAxis9[22] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20, 24, 28, 32, 36, 42, 50}; 
   
   TEfficiency * den_clone9 = new TEfficiency("den_clone","",21,xAxis9);
   
   den_clone9->SetConfidenceLevel(0.6826895);
   den_clone9->SetBetaAlpha(1);
   den_clone9->SetBetaBeta(1);
   den_clone9->SetWeight(1);
   den_clone9->SetStatisticOption(0);
   den_clone9->SetPosteriorMode(0);
   den_clone9->SetShortestInterval(0);
   den_clone9->SetTotalEvents(0,0);
   den_clone9->SetPassedEvents(0,0);
   den_clone9->SetTotalEvents(1,0);
   den_clone9->SetPassedEvents(1,0);
   den_clone9->SetTotalEvents(2,38);
   den_clone9->SetPassedEvents(2,35);
   den_clone9->SetTotalEvents(3,295);
   den_clone9->SetPassedEvents(3,292);
   den_clone9->SetTotalEvents(4,482);
   den_clone9->SetPassedEvents(4,477);
   den_clone9->SetTotalEvents(5,584);
   den_clone9->SetPassedEvents(5,581);
   den_clone9->SetTotalEvents(6,668);
   den_clone9->SetPassedEvents(6,661);
   den_clone9->SetTotalEvents(7,666);
   den_clone9->SetPassedEvents(7,662);
   den_clone9->SetTotalEvents(8,749);
   den_clone9->SetPassedEvents(8,745);
   den_clone9->SetTotalEvents(9,789);
   den_clone9->SetPassedEvents(9,785);
   den_clone9->SetTotalEvents(10,767);
   den_clone9->SetPassedEvents(10,762);
   den_clone9->SetTotalEvents(11,1412);
   den_clone9->SetPassedEvents(11,1407);
   den_clone9->SetTotalEvents(12,1279);
   den_clone9->SetPassedEvents(12,1271);
   den_clone9->SetTotalEvents(13,1076);
   den_clone9->SetPassedEvents(13,1074);
   den_clone9->SetTotalEvents(14,887);
   den_clone9->SetPassedEvents(14,883);
   den_clone9->SetTotalEvents(15,765);
   den_clone9->SetPassedEvents(15,759);
   den_clone9->SetTotalEvents(16,1238);
   den_clone9->SetPassedEvents(16,1236);
   den_clone9->SetTotalEvents(17,785);
   den_clone9->SetPassedEvents(17,781);
   den_clone9->SetTotalEvents(18,541);
   den_clone9->SetPassedEvents(18,541);
   den_clone9->SetTotalEvents(19,372);
   den_clone9->SetPassedEvents(19,372);
   den_clone9->SetTotalEvents(20,261);
   den_clone9->SetPassedEvents(20,259);
   den_clone9->SetTotalEvents(21,110);
   den_clone9->SetPassedEvents(21,110);
   den_clone9->SetTotalEvents(22,42);
   den_clone9->SetPassedEvents(22,42);
   den_clone9->SetFillColor(19);

   ci = TColor::GetColor("#0000ff");
   den_clone9->SetLineColor(ci);

   ci = TColor::GetColor("#0000ff");
   den_clone9->SetMarkerColor(ci);
   den_clone9->SetMarkerStyle(20);
   den_clone9->Draw("samep");
   Double_t xAxis10[22] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20, 24, 28, 32, 36, 42, 50}; 
   
   TEfficiency * den_clone10 = new TEfficiency("den_clone","",21,xAxis10);
   
   den_clone10->SetConfidenceLevel(0.6826895);
   den_clone10->SetBetaAlpha(1);
   den_clone10->SetBetaBeta(1);
   den_clone10->SetWeight(1);
   den_clone10->SetStatisticOption(0);
   den_clone10->SetPosteriorMode(0);
   den_clone10->SetShortestInterval(0);
   den_clone10->SetTotalEvents(0,0);
   den_clone10->SetPassedEvents(0,0);
   den_clone10->SetTotalEvents(1,0);
   den_clone10->SetPassedEvents(1,0);
   den_clone10->SetTotalEvents(2,17);
   den_clone10->SetPassedEvents(2,16);
   den_clone10->SetTotalEvents(3,65);
   den_clone10->SetPassedEvents(3,64);
   den_clone10->SetTotalEvents(4,104);
   den_clone10->SetPassedEvents(4,103);
   den_clone10->SetTotalEvents(5,124);
   den_clone10->SetPassedEvents(5,122);
   den_clone10->SetTotalEvents(6,146);
   den_clone10->SetPassedEvents(6,141);
   den_clone10->SetTotalEvents(7,171);
   den_clone10->SetPassedEvents(7,170);
   den_clone10->SetTotalEvents(8,169);
   den_clone10->SetPassedEvents(8,166);
   den_clone10->SetTotalEvents(9,168);
   den_clone10->SetPassedEvents(9,165);
   den_clone10->SetTotalEvents(10,164);
   den_clone10->SetPassedEvents(10,161);
   den_clone10->SetTotalEvents(11,306);
   den_clone10->SetPassedEvents(11,299);
   den_clone10->SetTotalEvents(12,253);
   den_clone10->SetPassedEvents(12,251);
   den_clone10->SetTotalEvents(13,215);
   den_clone10->SetPassedEvents(13,210);
   den_clone10->SetTotalEvents(14,195);
   den_clone10->SetPassedEvents(14,191);
   den_clone10->SetTotalEvents(15,147);
   den_clone10->SetPassedEvents(15,147);
   den_clone10->SetTotalEvents(16,218);
   den_clone10->SetPassedEvents(16,214);
   den_clone10->SetTotalEvents(17,113);
   den_clone10->SetPassedEvents(17,111);
   den_clone10->SetTotalEvents(18,57);
   den_clone10->SetPassedEvents(18,54);
   den_clone10->SetTotalEvents(19,39);
   den_clone10->SetPassedEvents(19,37);
   den_clone10->SetTotalEvents(20,22);
   den_clone10->SetPassedEvents(20,22);
   den_clone10->SetTotalEvents(21,13);
   den_clone10->SetPassedEvents(21,13);
   den_clone10->SetTotalEvents(22,0);
   den_clone10->SetPassedEvents(22,0);
   den_clone10->SetFillColor(19);

   ci = TColor::GetColor("#ff0000");
   den_clone10->SetLineColor(ci);

   ci = TColor::GetColor("#ff0000");
   den_clone10->SetMarkerColor(ci);
   den_clone10->SetMarkerStyle(21);
   den_clone10->Draw("samep");
   TLatex *   tex = new TLatex(0.5,0.6,"");
tex->SetNDC();
   tex->SetLineWidth(2);
   tex->Draw();
      tex = new TLatex(0.5,0.5,"2.0<|#eta|<2.2");
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
