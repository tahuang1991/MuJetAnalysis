void CorrectL1Mu_MatchingEfficiency_SimMuPt_ME1_ME2_ME3_eta22to24_dxy0to50()
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
   
   TH1F *b1__6 = new TH1F("b1__6","           #scale[1.4]{#font[61]{CMS}} #font[52]{Simulation preliminary}                                                         14 TeV, 0 PU",50,0,50);
   b1__6->SetMinimum(0);
   b1__6->SetMaximum(1.05);
   b1__6->SetStats(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   b1__6->SetLineColor(ci);
   b1__6->GetXaxis()->SetTitle("True muon p_{T} [GeV]");
   b1__6->GetXaxis()->SetLabelFont(42);
   b1__6->GetXaxis()->SetLabelSize(0.05);
   b1__6->GetXaxis()->SetTitleSize(0.05);
   b1__6->GetXaxis()->SetTitleOffset(1.2);
   b1__6->GetXaxis()->SetTitleFont(42);
   b1__6->GetYaxis()->SetTitle("Trigger efficiency");
   b1__6->GetYaxis()->SetNdivisions(520);
   b1__6->GetYaxis()->SetLabelFont(42);
   b1__6->GetYaxis()->SetLabelSize(0.05);
   b1__6->GetYaxis()->SetTitleSize(0.05);
   b1__6->GetYaxis()->SetTitleOffset(1.2);
   b1__6->GetYaxis()->SetTitleFont(42);
   b1__6->GetZaxis()->SetLabelFont(42);
   b1__6->GetZaxis()->SetLabelSize(0.035);
   b1__6->GetZaxis()->SetTitleSize(0.035);
   b1__6->GetZaxis()->SetTitleFont(42);
   b1__6->Draw("");
   Double_t xAxis11[22] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20, 24, 28, 32, 36, 42, 50}; 
   
   TEfficiency * den_clone11 = new TEfficiency("den_clone","",21,xAxis11);
   
   den_clone11->SetConfidenceLevel(0.6826895);
   den_clone11->SetBetaAlpha(1);
   den_clone11->SetBetaBeta(1);
   den_clone11->SetWeight(1);
   den_clone11->SetStatisticOption(0);
   den_clone11->SetPosteriorMode(0);
   den_clone11->SetShortestInterval(0);
   den_clone11->SetTotalEvents(0,0);
   den_clone11->SetPassedEvents(0,0);
   den_clone11->SetTotalEvents(1,0);
   den_clone11->SetPassedEvents(1,0);
   den_clone11->SetTotalEvents(2,73);
   den_clone11->SetPassedEvents(2,71);
   den_clone11->SetTotalEvents(3,310);
   den_clone11->SetPassedEvents(3,307);
   den_clone11->SetTotalEvents(4,426);
   den_clone11->SetPassedEvents(4,422);
   den_clone11->SetTotalEvents(5,512);
   den_clone11->SetPassedEvents(5,510);
   den_clone11->SetTotalEvents(6,613);
   den_clone11->SetPassedEvents(6,610);
   den_clone11->SetTotalEvents(7,674);
   den_clone11->SetPassedEvents(7,671);
   den_clone11->SetTotalEvents(8,694);
   den_clone11->SetPassedEvents(8,692);
   den_clone11->SetTotalEvents(9,638);
   den_clone11->SetPassedEvents(9,633);
   den_clone11->SetTotalEvents(10,678);
   den_clone11->SetPassedEvents(10,674);
   den_clone11->SetTotalEvents(11,1306);
   den_clone11->SetPassedEvents(11,1301);
   den_clone11->SetTotalEvents(12,1047);
   den_clone11->SetPassedEvents(12,1045);
   den_clone11->SetTotalEvents(13,903);
   den_clone11->SetPassedEvents(13,902);
   den_clone11->SetTotalEvents(14,783);
   den_clone11->SetPassedEvents(14,781);
   den_clone11->SetTotalEvents(15,721);
   den_clone11->SetPassedEvents(15,716);
   den_clone11->SetTotalEvents(16,1018);
   den_clone11->SetPassedEvents(16,1014);
   den_clone11->SetTotalEvents(17,700);
   den_clone11->SetPassedEvents(17,697);
   den_clone11->SetTotalEvents(18,419);
   den_clone11->SetPassedEvents(18,417);
   den_clone11->SetTotalEvents(19,335);
   den_clone11->SetPassedEvents(19,334);
   den_clone11->SetTotalEvents(20,229);
   den_clone11->SetPassedEvents(20,228);
   den_clone11->SetTotalEvents(21,113);
   den_clone11->SetPassedEvents(21,112);
   den_clone11->SetTotalEvents(22,47);
   den_clone11->SetPassedEvents(22,47);
   den_clone11->SetFillColor(19);

   ci = TColor::GetColor("#0000ff");
   den_clone11->SetLineColor(ci);

   ci = TColor::GetColor("#0000ff");
   den_clone11->SetMarkerColor(ci);
   den_clone11->SetMarkerStyle(20);
   den_clone11->Draw("samep");
   Double_t xAxis12[22] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20, 24, 28, 32, 36, 42, 50}; 
   
   TEfficiency * den_clone12 = new TEfficiency("den_clone","",21,xAxis12);
   
   den_clone12->SetConfidenceLevel(0.6826895);
   den_clone12->SetBetaAlpha(1);
   den_clone12->SetBetaBeta(1);
   den_clone12->SetWeight(1);
   den_clone12->SetStatisticOption(0);
   den_clone12->SetPosteriorMode(0);
   den_clone12->SetShortestInterval(0);
   den_clone12->SetTotalEvents(0,0);
   den_clone12->SetPassedEvents(0,0);
   den_clone12->SetTotalEvents(1,0);
   den_clone12->SetPassedEvents(1,0);
   den_clone12->SetTotalEvents(2,13);
   den_clone12->SetPassedEvents(2,12);
   den_clone12->SetTotalEvents(3,51);
   den_clone12->SetPassedEvents(3,51);
   den_clone12->SetTotalEvents(4,90);
   den_clone12->SetPassedEvents(4,89);
   den_clone12->SetTotalEvents(5,108);
   den_clone12->SetPassedEvents(5,106);
   den_clone12->SetTotalEvents(6,119);
   den_clone12->SetPassedEvents(6,118);
   den_clone12->SetTotalEvents(7,140);
   den_clone12->SetPassedEvents(7,138);
   den_clone12->SetTotalEvents(8,132);
   den_clone12->SetPassedEvents(8,130);
   den_clone12->SetTotalEvents(9,125);
   den_clone12->SetPassedEvents(9,123);
   den_clone12->SetTotalEvents(10,135);
   den_clone12->SetPassedEvents(10,132);
   den_clone12->SetTotalEvents(11,245);
   den_clone12->SetPassedEvents(11,241);
   den_clone12->SetTotalEvents(12,206);
   den_clone12->SetPassedEvents(12,205);
   den_clone12->SetTotalEvents(13,173);
   den_clone12->SetPassedEvents(13,171);
   den_clone12->SetTotalEvents(14,162);
   den_clone12->SetPassedEvents(14,162);
   den_clone12->SetTotalEvents(15,122);
   den_clone12->SetPassedEvents(15,122);
   den_clone12->SetTotalEvents(16,168);
   den_clone12->SetPassedEvents(16,164);
   den_clone12->SetTotalEvents(17,93);
   den_clone12->SetPassedEvents(17,90);
   den_clone12->SetTotalEvents(18,55);
   den_clone12->SetPassedEvents(18,54);
   den_clone12->SetTotalEvents(19,15);
   den_clone12->SetPassedEvents(19,15);
   den_clone12->SetTotalEvents(20,11);
   den_clone12->SetPassedEvents(20,10);
   den_clone12->SetTotalEvents(21,4);
   den_clone12->SetPassedEvents(21,3);
   den_clone12->SetTotalEvents(22,0);
   den_clone12->SetPassedEvents(22,0);
   den_clone12->SetFillColor(19);

   ci = TColor::GetColor("#ff0000");
   den_clone12->SetLineColor(ci);

   ci = TColor::GetColor("#ff0000");
   den_clone12->SetMarkerColor(ci);
   den_clone12->SetMarkerStyle(21);
   den_clone12->Draw("samep");
   TLatex *   tex = new TLatex(0.5,0.6,"");
tex->SetNDC();
   tex->SetLineWidth(2);
   tex->Draw();
      tex = new TLatex(0.5,0.5,"2.2<|#eta|<2.4");
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
