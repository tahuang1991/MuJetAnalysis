from ROOT import *

from Helpers import *
from ROOT import SetOwnership

def l1ExtraTrackEfficiency(p):

    etaBinning = "(50,-2.5,2.5)"

    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(5)), n_dt_st_sh(1)), "eff_sim_eta_pt5_dt_st_1", ">=1 DT station")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(5)), n_dt_st_sh(2)), "eff_sim_eta_pt5_dt_st_2", ">=2 DT station")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(5)), n_dt_st_sh(3)), "eff_sim_eta_pt5_dt_st_3", ">=3 DT station")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(5)), n_dt_st_sh(4)), "eff_sim_eta_pt5_dt_st_4", ">=4 DT station")

    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(5)), n_csc_st_sh(1)), "eff_sim_eta_pt5_csc_st_1", ">=1 CSC station")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(5)), n_csc_st_sh(2)), "eff_sim_eta_pt5_csc_st_2", ">=2 CSC station")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(5)), n_csc_st_sh(3)), "eff_sim_eta_pt5_csc_st_3", ">=3 CSC station")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(5)), n_csc_st_sh(4)), "eff_sim_eta_pt5_csc_st_4", ">=4 CSC station")

    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(5)), n_gem_st_sh(1)), "eff_sim_eta_pt5_gem_st_1", ">=1 GEM station")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(5)), n_gem_st_sh(2)), "eff_sim_eta_pt5_gem_st_2", ">=2 GEM station")

    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(5)), has_L1Extra()), "eff_sim_eta_pt5_L1Extra_pt0", "L1Extra")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(20)), has_L1Extra(17)), "eff_sim_eta_pt20_L1Extra_pt17", "L1Extra")
    makeEtaEffPlot(p, getEffObject(p, "abs(sim_eta)", etaBinning, AND(sim_pt(20), sim_dxy(0, 5)), has_L1Extra(17)), "eff_sim_eta_pt20_dxy0dto5_L1Extra_pt17", "L1Extra")
