{
//=========Macro generated from canvas: c/c
//=========  (Tue Feb  7 16:48:43 2017) by ROOT version5.34/07
   TCanvas *c = new TCanvas("c", "c",0,0,800,600);
   gStyle->SetOptStat(0);
   c->SetHighLightColor(2);
   c->Range(-0.06510791,-0.06604938,0.05479616,0.05740741);
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
   
   TH2F *h_dphi_ME11_ME21_charge_Pt30to140 = new TH2F("h_dphi_ME11_ME21_charge_Pt30to140","           #scale[1.4]{#font[61]{CMS}} #font[52]{Simulation preliminary}                                                           14 TeV, 140 PU",100,-0.05,0.05,100,-0.05,0.05);
   h_dphi_ME11_ME21_charge_Pt30to140->SetBinContent(5152,1);
   h_dphi_ME11_ME21_charge_Pt30to140->SetBinContent(5182,1);
   h_dphi_ME11_ME21_charge_Pt30to140->SetBinContent(10353,1);
   h_dphi_ME11_ME21_charge_Pt30to140->SetBinContent(10403,2);
   h_dphi_ME11_ME21_charge_Pt30to140->SetEntries(5);
   h_dphi_ME11_ME21_charge_Pt30to140->SetStats(0);
   h_dphi_ME11_ME21_charge_Pt30to140->SetContour(20);
   h_dphi_ME11_ME21_charge_Pt30to140->SetContourLevel(0,0);
   h_dphi_ME11_ME21_charge_Pt30to140->SetContourLevel(1,0.05);
   h_dphi_ME11_ME21_charge_Pt30to140->SetContourLevel(2,0.1);
   h_dphi_ME11_ME21_charge_Pt30to140->SetContourLevel(3,0.15);
   h_dphi_ME11_ME21_charge_Pt30to140->SetContourLevel(4,0.2);
   h_dphi_ME11_ME21_charge_Pt30to140->SetContourLevel(5,0.25);
   h_dphi_ME11_ME21_charge_Pt30to140->SetContourLevel(6,0.3);
   h_dphi_ME11_ME21_charge_Pt30to140->SetContourLevel(7,0.35);
   h_dphi_ME11_ME21_charge_Pt30to140->SetContourLevel(8,0.4);
   h_dphi_ME11_ME21_charge_Pt30to140->SetContourLevel(9,0.45);
   h_dphi_ME11_ME21_charge_Pt30to140->SetContourLevel(10,0.5);
   h_dphi_ME11_ME21_charge_Pt30to140->SetContourLevel(11,0.55);
   h_dphi_ME11_ME21_charge_Pt30to140->SetContourLevel(12,0.6);
   h_dphi_ME11_ME21_charge_Pt30to140->SetContourLevel(13,0.65);
   h_dphi_ME11_ME21_charge_Pt30to140->SetContourLevel(14,0.7);
   h_dphi_ME11_ME21_charge_Pt30to140->SetContourLevel(15,0.75);
   h_dphi_ME11_ME21_charge_Pt30to140->SetContourLevel(16,0.8);
   h_dphi_ME11_ME21_charge_Pt30to140->SetContourLevel(17,0.85);
   h_dphi_ME11_ME21_charge_Pt30to140->SetContourLevel(18,0.9);
   h_dphi_ME11_ME21_charge_Pt30to140->SetContourLevel(19,0.95);
   
   TPaletteAxis *palette = new TPaletteAxis(0.05059952,-0.05,0.05473621,0.05,h_dphi_ME11_ME21_charge_Pt30to140);
palette->SetLabelColor(1);
palette->SetLabelFont(42);
palette->SetLabelOffset(0.005);
palette->SetLabelSize(0.035);
palette->SetTitleOffset(1);
palette->SetTitleSize(0.035);
   palette->SetFillColor(100);
   palette->SetFillStyle(1001);
   h_dphi_ME11_ME21_charge_Pt30to140->GetListOfFunctions()->Add(palette,"br");

   Int_t ci;   // for color index setting
   ci = TColor::GetColor("#000099");
   h_dphi_ME11_ME21_charge_Pt30to140->SetLineColor(ci);
   h_dphi_ME11_ME21_charge_Pt30to140->GetXaxis()->SetTitle("charge*#Delta#Phi(GE2/1-ME2/1)");
   h_dphi_ME11_ME21_charge_Pt30to140->GetXaxis()->SetLabelFont(42);
   h_dphi_ME11_ME21_charge_Pt30to140->GetXaxis()->SetLabelSize(0.05);
   h_dphi_ME11_ME21_charge_Pt30to140->GetXaxis()->SetTitleSize(0.05);
   h_dphi_ME11_ME21_charge_Pt30to140->GetXaxis()->SetTitleFont(42);
   h_dphi_ME11_ME21_charge_Pt30to140->GetYaxis()->SetTitle("charge*#Delta#Phi(GE1/1-ME1/1)");
   h_dphi_ME11_ME21_charge_Pt30to140->GetYaxis()->SetLabelFont(42);
   h_dphi_ME11_ME21_charge_Pt30to140->GetYaxis()->SetLabelSize(0.05);
   h_dphi_ME11_ME21_charge_Pt30to140->GetYaxis()->SetTitleSize(0.05);
   h_dphi_ME11_ME21_charge_Pt30to140->GetYaxis()->SetTitleFont(42);
   h_dphi_ME11_ME21_charge_Pt30to140->GetZaxis()->SetLabelFont(42);
   h_dphi_ME11_ME21_charge_Pt30to140->GetZaxis()->SetLabelSize(0.035);
   h_dphi_ME11_ME21_charge_Pt30to140->GetZaxis()->SetTitleSize(0.035);
   h_dphi_ME11_ME21_charge_Pt30to140->GetZaxis()->SetTitleFont(42);
   h_dphi_ME11_ME21_charge_Pt30to140->Draw("COLZ");
   
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
