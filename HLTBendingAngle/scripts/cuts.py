from ROOT import *
import math
import array
from math import log10, floor
from simpleCuts import *

#_______________________________________________________________________________
def cand_rpcb_st(n):
    return TCut("cand_rpcb_st_%d>0"%(n))

#_______________________________________________________________________________
def cand_rpcf_st(n):
    return TCut("cand_rpcf_st_%d>0"%(n))

#_______________________________________________________________________________
def cand_csc_st(n):
    return TCut("cand_csc_st_%d>0"%(n))

#_______________________________________________________________________________
def cand_dt_st(n):
    return TCut("cand_dt_st_%d>0"%(n))

#_______________________________________________________________________________
def cand_seg_st(n):
    return OR(cand_dt_st(n), cand_csc_st(n))

#_______________________________________________________________________________
def cand_rpcgem_st(n):
    return OR(cand_rpcf_st(n), cand_rpcb_st(n), cand_gem_st(n))

#_______________________________________________________________________________
def cand_rpcgem_e_st(n):
    return OR(cand_rpcf_st(n), cand_gem_st(n))

#_______________________________________________________________________________
def cand_gem_st(n):
    if n==3 or n==4:
        return nocut()
    return TCut("cand_gem_st_%d>0"%(n))

#_______________________________________________________________________________
def cand_gem_n_st(n):
    if n==2:
        return AND(cand_gem_st(1), cand_gem_st(2))
    elif n==1:
        return OR(cand_gem_st(1), cand_gem_st(2))          

#_______________________________________________________________________________
def cand_barrel_st(n):
    return OR(cand_dt_st(n), cand_rpcb_st(n))

#_______________________________________________________________________________
def cand_endcap_st(n):
    return OR(cand_csc_st(n), cand_rpcf_st(n), cand_gem_st(n))

#_______________________________________________________________________________
def cand_overlap_st(n):
    return OR(cand_dt_st(n), cand_rpcb_st(n), cand_csc_st(n), cand_rpcf_st(n))

#_______________________________________________________________________________
def cand_3_st_2_segments_barrel():
    return OR(
        AND(cand_dt_st(1), cand_dt_st(2)),
        AND(cand_dt_st(1), cand_dt_st(3)),
        AND(cand_dt_st(1), cand_dt_st(4)),
        AND(cand_dt_st(2), cand_dt_st(3)),
        AND(cand_dt_st(2), cand_dt_st(4)),
        AND(cand_dt_st(3), cand_dt_st(4)) )

#_______________________________________________________________________________
def cand_3_st_3_segments_barrel():
    return OR(
        AND(cand_dt_st(1), cand_dt_st(2), cand_dt_st(3)),
        AND(cand_dt_st(1), cand_dt_st(2), cand_dt_st(4)),
        AND(cand_dt_st(1), cand_dt_st(3), cand_dt_st(4)),
        AND(cand_dt_st(2), cand_dt_st(3), cand_dt_st(4)) )

#_______________________________________________________________________________
def cand_3_st_3_segments_endcap():
    return OR(
        AND(cand_csc_st(1), cand_csc_st(2), cand_csc_st(3)),
        AND(cand_csc_st(1), cand_csc_st(2), cand_csc_st(4)),
        AND(cand_csc_st(1), cand_csc_st(3), cand_csc_st(4)),
        AND(cand_csc_st(2), cand_csc_st(3), cand_csc_st(4)) )

#_______________________________________________________________________________
def cand_3_st_3_segments_nocscst2_endcap():
    return AND(cand_csc_st(1), cand_csc_st(3), cand_csc_st(4))

#_______________________________________________________________________________
def cand_3_st_3_segments_overlap():
    return OR(
        AND(cand_dt_st(1), cand_dt_st(2), cand_csc_st(1)),
        AND(cand_dt_st(1), cand_dt_st(2), cand_csc_st(2)),
        AND(cand_dt_st(1), cand_dt_st(2), cand_csc_st(3)),
        AND(cand_dt_st(1), cand_dt_st(2), cand_csc_st(4)),
        
        AND(cand_dt_st(1), cand_dt_st(3), cand_csc_st(1)),
        AND(cand_dt_st(2), cand_dt_st(3), cand_csc_st(1)),
        
        AND(cand_dt_st(1), cand_csc_st(1), cand_csc_st(2)),
        AND(cand_dt_st(1), cand_csc_st(1), cand_csc_st(3)),
        AND(cand_dt_st(1), cand_csc_st(1), cand_csc_st(4)),
        
        AND(cand_dt_st(1), cand_csc_st(2), cand_csc_st(3)),
        AND(cand_dt_st(1), cand_csc_st(2), cand_csc_st(4)),
        
        AND(cand_dt_st(1), cand_csc_st(3), cand_csc_st(4)),
        
        AND(cand_dt_st(2), cand_csc_st(1), cand_csc_st(2)),
        AND(cand_dt_st(2), cand_csc_st(1), cand_csc_st(3)) )

#_______________________________________________________________________________
def cand_3_st_2_segments_1_rechit_barrel():
    return OR( 
        AND(cand_dt_st(1), cand_dt_st(2), cand_rpcb_st(3)), 
        AND(cand_dt_st(1), cand_dt_st(2), cand_rpcb_st(4)),
        
        AND(cand_dt_st(1), cand_dt_st(3), cand_rpcb_st(2)),
        AND(cand_dt_st(1), cand_dt_st(3), cand_rpcb_st(4)),
        
        AND(cand_dt_st(1), cand_dt_st(4), cand_rpcb_st(2)),
        AND(cand_dt_st(1), cand_dt_st(4), cand_rpcb_st(3)),
        
        AND(cand_dt_st(2), cand_dt_st(3), cand_rpcb_st(1)),
        AND(cand_dt_st(2), cand_dt_st(3), cand_rpcb_st(4)),
        
        AND(cand_dt_st(2), cand_dt_st(4), cand_rpcb_st(1)),
        AND(cand_dt_st(2), cand_dt_st(4), cand_rpcb_st(3)),
        
        AND(cand_dt_st(3), cand_dt_st(4), cand_rpcb_st(1)),
        AND(cand_dt_st(3), cand_dt_st(4), cand_rpcb_st(2)) )

#_______________________________________________________________________________
def cand_3_st_2_segments_1_rechit_overlap():
    return OR(
        AND(cand_dt_st(1), cand_dt_st(2), cand_rpcf_st(1)), 
        AND(cand_dt_st(1), cand_dt_st(2), cand_rpcf_st(2)), 
        
        AND(cand_dt_st(1), cand_csc_st(1), cand_rpcf_st(2)), 
        AND(cand_dt_st(1), cand_csc_st(1), cand_rpcf_st(3)), 
        AND(cand_dt_st(1), cand_csc_st(1), cand_rpcf_st(4)), 
        
        AND(cand_dt_st(1), cand_csc_st(2), cand_rpcf_st(1)), 
        AND(cand_dt_st(1), cand_csc_st(2), cand_rpcf_st(3)), 
        AND(cand_dt_st(1), cand_csc_st(2), cand_rpcf_st(4)), 
        
        AND(cand_dt_st(1), cand_csc_st(3), cand_rpcf_st(1)), 
        AND(cand_dt_st(1), cand_csc_st(3), cand_rpcf_st(2)), 
        AND(cand_dt_st(1), cand_csc_st(3), cand_rpcf_st(4)), 
        
        AND(cand_dt_st(1), cand_csc_st(4), cand_rpcf_st(1)), 
        AND(cand_dt_st(1), cand_csc_st(4), cand_rpcf_st(2)), 
        AND(cand_dt_st(1), cand_csc_st(4), cand_rpcf_st(3)), 
        
        AND(cand_rpcb_st(1), cand_dt_st(2), cand_csc_st(1)), 
        AND(cand_rpcb_st(1), cand_dt_st(2), cand_csc_st(2)), 
        AND(cand_rpcb_st(1), cand_dt_st(2), cand_csc_st(3)), 
        AND(cand_rpcb_st(1), cand_dt_st(2), cand_csc_st(4)), 
        
        AND(cand_rpcb_st(2), cand_dt_st(1), cand_csc_st(1)), 
        AND(cand_rpcb_st(2), cand_dt_st(1), cand_csc_st(2)), 
        AND(cand_rpcb_st(2), cand_dt_st(1), cand_csc_st(3)), 
        AND(cand_rpcb_st(2), cand_dt_st(1), cand_csc_st(4)), 
        
        AND(cand_rpcb_st(1), cand_csc_st(1), cand_csc_st(2)), 
        AND(cand_rpcb_st(1), cand_csc_st(1), cand_csc_st(3)), 
        AND(cand_rpcb_st(1), cand_csc_st(1), cand_csc_st(4)), 
        AND(cand_rpcb_st(1), cand_csc_st(2), cand_csc_st(3)), 
        AND(cand_rpcb_st(1), cand_csc_st(2), cand_csc_st(4)), 
        AND(cand_rpcb_st(1), cand_csc_st(3), cand_csc_st(4)) )
        
#_______________________________________________________________________________
def cand_3_st_2_segments_1_rechit_endcap():
    return OR(
        AND(cand_csc_st(1), cand_csc_st(3), cand_rpcgem_e_st(2)),
        AND(cand_csc_st(1), cand_csc_st(4), cand_rpcgem_e_st(2)),
        AND(cand_csc_st(3), cand_csc_st(4), cand_rpcgem_e_st(2)),

        AND(cand_csc_st(1), cand_csc_st(2), cand_rpcgem_e_st(3)),
        AND(cand_csc_st(1), cand_csc_st(4), cand_rpcgem_e_st(3)),
        AND(cand_csc_st(2), cand_csc_st(4), cand_rpcgem_e_st(3)),

        AND(cand_csc_st(1), cand_csc_st(2), cand_rpcgem_e_st(4)),
        AND(cand_csc_st(1), cand_csc_st(3), cand_rpcgem_e_st(4)),
        AND(cand_csc_st(2), cand_csc_st(3), cand_rpcgem_e_st(4)),
        
        AND(cand_csc_st(2), cand_csc_st(3), cand_rpcgem_e_st(1)),
        AND(cand_csc_st(2), cand_csc_st(4), cand_rpcgem_e_st(1)),
        AND(cand_csc_st(3), cand_csc_st(4), cand_rpcgem_e_st(1)) )
        
#_______________________________________________________________________________
def cand_3_st_2_segments_1_rechit_gem_endcap():
    return OR(
        AND(cand_csc_st(1), cand_csc_st(3), cand_gem_st(2)),
        AND(cand_csc_st(1), cand_csc_st(4), cand_gem_st(2)),
        AND(cand_csc_st(3), cand_csc_st(4), cand_gem_st(2)),        
        AND(cand_csc_st(2), cand_csc_st(3), cand_gem_st(1)),
        AND(cand_csc_st(3), cand_csc_st(4), cand_gem_st(1)),
        AND(cand_csc_st(2), cand_csc_st(4), cand_gem_st(1)) )

#_______________________________________________________________________________
def cand_3_st_2_segments_1_rechit_GE21_endcap():
    return OR(
        AND(cand_csc_st(1), cand_csc_st(3), cand_gem_st(2)),
        AND(cand_csc_st(1), cand_csc_st(4), cand_gem_st(2)),
        AND(cand_csc_st(3), cand_csc_st(4), cand_gem_st(2)) )

#_______________________________________________________________________________
def cand_3_st_2_segments_1_rechit_GE21_nocscst2_endcap():
    return OR(
        AND(cand_csc_st(1), cand_csc_st(3), cand_gem_st(2), NOT(cand_csc_st(2))),
        AND(cand_csc_st(1), cand_csc_st(4), cand_gem_st(2), NOT(cand_csc_st(2))),
        AND(cand_csc_st(3), cand_csc_st(4), cand_gem_st(2), NOT(cand_csc_st(2))) )

#_______________________________________________________________________________
def cand_3_st_2_segments_1_rechit_nocscst2_endcap():
    return OR(
        AND(cand_csc_st(1), cand_csc_st(3), cand_rpcgem_e_st(2)),
        AND(cand_csc_st(1), cand_csc_st(4), cand_rpcgem_e_st(2)),
        AND(cand_csc_st(3), cand_csc_st(4), cand_rpcgem_e_st(2)),
        AND(cand_csc_st(1), cand_csc_st(4), cand_rpcgem_e_st(3)),
        AND(cand_csc_st(1), cand_csc_st(3), cand_rpcgem_e_st(4)),
        AND(cand_csc_st(3), cand_csc_st(4), cand_rpcgem_e_st(1)) )

#_______________________________________________________________________________
def cand_3_st_2_segments_1_rechit():
    return OR(cand_3_st_2_segments_1_rechit_barrel(),
              cand_3_st_2_segments_1_rechit_endcap(),
              cand_3_st_2_segments_1_rechit_overlap()
              )

#_______________________________________________________________________________
def cand_3_st_3_segments():
    return OR(cand_3_st_3_segments_barrel(),
              cand_3_st_3_segments_endcap(),
              cand_3_st_3_segments_overlap())

#_______________________________________________________________________________
def cand_3_st():
    ## 3 segments 
    TFormula.SetMaxima(100000,1000,1000000)
    return OR(cand_3_st_3_segments(), cand_3_st_2_segments_1_rechit())

#_______________________________________________________________________________
def cand_3_st_tree_3_segments_barrel(tree):
    return ( 
        (ord(tree.cand_dt_st_1)>0 and ord(tree.cand_dt_st_2)>0 and ord(tree.cand_dt_st_3)>0) or
        (ord(tree.cand_dt_st_1)>0 and ord(tree.cand_dt_st_2)>0 and ord(tree.cand_dt_st_4)>0) or
        (ord(tree.cand_dt_st_1)>0 and ord(tree.cand_dt_st_3)>0 and ord(tree.cand_dt_st_4)>0) or
        (ord(tree.cand_dt_st_2)>0 and ord(tree.cand_dt_st_3)>0 and ord(tree.cand_dt_st_4)>0) )

#_______________________________________________________________________________
def cand_3_st_tree_3_segments_endcap(tree):
    return ( 
        (ord(tree.cand_csc_st_1)>0 and ord(tree.cand_csc_st_2)>0 and ord(tree.cand_csc_st_3)>0) or
        (ord(tree.cand_csc_st_1)>0 and ord(tree.cand_csc_st_2)>0 and ord(tree.cand_csc_st_4)>0) or
        (ord(tree.cand_csc_st_1)>0 and ord(tree.cand_csc_st_3)>0 and ord(tree.cand_csc_st_4)>0) or
        (ord(tree.cand_csc_st_2)>0 and ord(tree.cand_csc_st_3)>0 and ord(tree.cand_csc_st_4)>0) )

#_______________________________________________________________________________
def cand_3_st_tree_2_segments_endcap(tree):
    return ( 
        (ord(tree.cand_csc_st_1)>0 and ord(tree.cand_csc_st_2)>0) or
        (ord(tree.cand_csc_st_1)>0 and ord(tree.cand_csc_st_3)>0) or
        (ord(tree.cand_csc_st_1)>0 and ord(tree.cand_csc_st_4)>0) or
        (ord(tree.cand_csc_st_2)>0 and ord(tree.cand_csc_st_3)>0) or
        (ord(tree.cand_csc_st_2)>0 and ord(tree.cand_csc_st_4)>0) or
        (ord(tree.cand_csc_st_3)>0 and ord(tree.cand_csc_st_4)>0) )

#_______________________________________________________________________________
def cand_3_st_tree_3_segments_overlap(tree):
    return (
        (ord(tree.cand_dt_st_1)>0 and ord(tree.cand_dt_st_2)>0 and ord(tree.cand_csc_st_1)>0) or
        (ord(tree.cand_dt_st_1)>0 and ord(tree.cand_dt_st_2)>0 and ord(tree.cand_csc_st_2)>0) or
        (ord(tree.cand_dt_st_1)>0 and ord(tree.cand_dt_st_2)>0 and ord(tree.cand_csc_st_3)>0) or
        (ord(tree.cand_dt_st_1)>0 and ord(tree.cand_dt_st_2)>0 and ord(tree.cand_csc_st_4)>0) or
        
        (ord(tree.cand_dt_st_1)>0 and ord(tree.cand_dt_st_3)>0 and ord(tree.cand_csc_st_1)>0) or
        (ord(tree.cand_dt_st_2)>0 and ord(tree.cand_dt_st_3)>0 and ord(tree.cand_csc_st_1)>0) or
        
        (ord(tree.cand_dt_st_1)>0 and ord(tree.cand_csc_st_1)>0 and ord(tree.cand_csc_st_2)>0) or
        (ord(tree.cand_dt_st_1)>0 and ord(tree.cand_csc_st_1)>0 and ord(tree.cand_csc_st_3)>0) or
        (ord(tree.cand_dt_st_1)>0 and ord(tree.cand_csc_st_1)>0 and ord(tree.cand_csc_st_4)>0) or
        
        (ord(tree.cand_dt_st_1)>0 and ord(tree.cand_csc_st_2)>0 and ord(tree.cand_csc_st_3)>0) or
        (ord(tree.cand_dt_st_1)>0 and ord(tree.cand_csc_st_2)>0 and ord(tree.cand_csc_st_4)>0) or
        
        (ord(tree.cand_dt_st_1)>0 and ord(tree.cand_csc_st_3)>0 and ord(tree.cand_csc_st_4)>0) or
        
        (ord(tree.cand_dt_st_2)>0 and ord(tree.cand_csc_st_1)>0 and ord(tree.cand_csc_st_2)>0) or
        (ord(tree.cand_dt_st_2)>0 and ord(tree.cand_csc_st_1)>0 and ord(tree.cand_csc_st_3)>0) )

#_______________________________________________________________________________
def cand_3_st_tree_2_segments_1_rechit_barrel(tree):
    return ( 
        (ord(tree.cand_dt_st_1)>0 and ord(tree.cand_dt_st_2)>0 and ord(tree.cand_rpcb_st_3)>0) or 
        (ord(tree.cand_dt_st_1)>0 and ord(tree.cand_dt_st_2)>0 and ord(tree.cand_rpcb_st_4)>0) or
        
        (ord(tree.cand_dt_st_1)>0 and ord(tree.cand_dt_st_3)>0 and ord(tree.cand_rpcb_st_2)>0) or
        (ord(tree.cand_dt_st_1)>0 and ord(tree.cand_dt_st_3)>0 and ord(tree.cand_rpcb_st_4)>0) or
        
        (ord(tree.cand_dt_st_1)>0 and ord(tree.cand_dt_st_4)>0 and ord(tree.cand_rpcb_st_2)>0) or
        (ord(tree.cand_dt_st_1)>0 and ord(tree.cand_dt_st_4)>0 and ord(tree.cand_rpcb_st_3)>0) or
        
        (ord(tree.cand_dt_st_2)>0 and ord(tree.cand_dt_st_3)>0 and ord(tree.cand_rpcb_st_1)>0) or
        (ord(tree.cand_dt_st_2)>0 and ord(tree.cand_dt_st_3)>0 and ord(tree.cand_rpcb_st_4)>0) or
        
        (ord(tree.cand_dt_st_2)>0 and ord(tree.cand_dt_st_4)>0 and ord(tree.cand_rpcb_st_1)>0) or
        (ord(tree.cand_dt_st_2)>0 and ord(tree.cand_dt_st_4)>0 and ord(tree.cand_rpcb_st_3)>0) or
        
        (ord(tree.cand_dt_st_3)>0 and ord(tree.cand_dt_st_4)>0 and ord(tree.cand_rpcb_st_1)>0) or
        (ord(tree.cand_dt_st_3)>0 and ord(tree.cand_dt_st_4)>0 and ord(tree.cand_rpcb_st_2)>0) )

#_______________________________________________________________________________
def cand_3_st_tree_2_segments_1_rechit_endcap(tree):
    return (
        (ord(tree.cand_csc_st_1)>0 and ord(tree.cand_csc_st_2)>0 and ord(tree.cand_rpcf_st_3)>0) or
        (ord(tree.cand_csc_st_1)>0 and ord(tree.cand_csc_st_4)>0 and ord(tree.cand_rpcf_st_3)>0) or
        (ord(tree.cand_csc_st_2)>0 and ord(tree.cand_csc_st_4)>0 and ord(tree.cand_rpcf_st_3)>0) or

        (ord(tree.cand_csc_st_1)>0 and ord(tree.cand_csc_st_2)>0 and ord(tree.cand_rpcf_st_4)>0) or
        (ord(tree.cand_csc_st_1)>0 and ord(tree.cand_csc_st_3)>0 and ord(tree.cand_rpcf_st_4)>0) or
        (ord(tree.cand_csc_st_2)>0 and ord(tree.cand_csc_st_3)>0 and ord(tree.cand_rpcf_st_4)>0) or
        
        (ord(tree.cand_csc_st_1)>0 and ord(tree.cand_csc_st_3)>0 and ord(tree.cand_gem_st_2)>0) or
        (ord(tree.cand_csc_st_1)>0 and ord(tree.cand_csc_st_4)>0 and ord(tree.cand_gem_st_2)>0) or
        (ord(tree.cand_csc_st_3)>0 and ord(tree.cand_csc_st_4)>0 and ord(tree.cand_gem_st_2)>0) or

        (ord(tree.cand_csc_st_2)>0 and ord(tree.cand_csc_st_3)>0 and ord(tree.cand_gem_st_1)>0) or
        (ord(tree.cand_csc_st_3)>0 and ord(tree.cand_csc_st_4)>0 and ord(tree.cand_gem_st_1)>0) or
        (ord(tree.cand_csc_st_2)>0 and ord(tree.cand_csc_st_4)>0 and ord(tree.cand_gem_st_1)>0) )

#_______________________________________________________________________________
def cand_3_st_tree_2_segments_1_rechit_gem_endcap(tree):
    return (
        (ord(tree.cand_csc_st_1)>0 and ord(tree.cand_csc_st_3)>0 and ord(tree.cand_gem_st_2)>0) or
        (ord(tree.cand_csc_st_1)>0 and ord(tree.cand_csc_st_4)>0 and ord(tree.cand_gem_st_2)>0) or
        (ord(tree.cand_csc_st_3)>0 and ord(tree.cand_csc_st_4)>0 and ord(tree.cand_gem_st_2)>0) or

        (ord(tree.cand_csc_st_2)>0 and ord(tree.cand_csc_st_3)>0 and ord(tree.cand_gem_st_1)>0) or
        (ord(tree.cand_csc_st_3)>0 and ord(tree.cand_csc_st_4)>0 and ord(tree.cand_gem_st_1)>0) or
        (ord(tree.cand_csc_st_2)>0 and ord(tree.cand_csc_st_4)>0 and ord(tree.cand_gem_st_1)>0) )

#_______________________________________________________________________________
def cand_3_st_tree_2_segments_1_rechit_GE21_endcap(tree):
    return (
        (ord(tree.cand_csc_st_1)>0 and ord(tree.cand_csc_st_3)>0 and ord(tree.cand_gem_st_2)>0) or
        (ord(tree.cand_csc_st_1)>0 and ord(tree.cand_csc_st_4)>0 and ord(tree.cand_gem_st_2)>0) or
        (ord(tree.cand_csc_st_3)>0 and ord(tree.cand_csc_st_4)>0 and ord(tree.cand_gem_st_2)>0) )

#_______________________________________________________________________________
def cand_3_st_tree_2_segments_1_rechit_GE21_nocscst2_endcap(tree):
    return (
        (ord(tree.cand_csc_st_1)>0 and ord(tree.cand_csc_st_3)>0 and ord(tree.cand_gem_st_2)>0 and ord(tree.cand_csc_st_2)<1) or
        (ord(tree.cand_csc_st_1)>0 and ord(tree.cand_csc_st_4)>0 and ord(tree.cand_gem_st_2)>0 and ord(tree.cand_csc_st_2)<1) or
        (ord(tree.cand_csc_st_3)>0 and ord(tree.cand_csc_st_4)>0 and ord(tree.cand_gem_st_2)>0 and ord(tree.cand_csc_st_2)<1) )

#_______________________________________________________________________________
def cand_3_st_tree_2_segments_1_rechit_overlap(tree):
    return ( 
        (ord(tree.cand_dt_st_1)>0 and ord(tree.cand_dt_st_2)>0 and ord(tree.cand_rpcf_st_1)>0) or 
        (ord(tree.cand_dt_st_1)>0 and ord(tree.cand_dt_st_2)>0 and ord(tree.cand_rpcf_st_2)>0) or 
        
        (ord(tree.cand_dt_st_1)>0 and ord(tree.cand_csc_st_1)>0 and ord(tree.cand_rpcf_st_2)>0) or 
        (ord(tree.cand_dt_st_1)>0 and ord(tree.cand_csc_st_1)>0 and ord(tree.cand_rpcf_st_3)>0) or 
        (ord(tree.cand_dt_st_1)>0 and ord(tree.cand_csc_st_1)>0 and ord(tree.cand_rpcf_st_4)>0) or 
        
        (ord(tree.cand_dt_st_1)>0 and ord(tree.cand_csc_st_2)>0 and ord(tree.cand_rpcf_st_1)>0) or 
        (ord(tree.cand_dt_st_1)>0 and ord(tree.cand_csc_st_2)>0 and ord(tree.cand_rpcf_st_3)>0) or 
        (ord(tree.cand_dt_st_1)>0 and ord(tree.cand_csc_st_2)>0 and ord(tree.cand_rpcf_st_4)>0) or 
        
        (ord(tree.cand_dt_st_1)>0 and ord(tree.cand_csc_st_3)>0 and ord(tree.cand_rpcf_st_1)>0) or 
        (ord(tree.cand_dt_st_1)>0 and ord(tree.cand_csc_st_3)>0 and ord(tree.cand_rpcf_st_2)>0) or 
        (ord(tree.cand_dt_st_1)>0 and ord(tree.cand_csc_st_3)>0 and ord(tree.cand_rpcf_st_4)>0) or 
        
        (ord(tree.cand_dt_st_1)>0 and ord(tree.cand_csc_st_4)>0 and ord(tree.cand_rpcf_st_1)>0) or 
        (ord(tree.cand_dt_st_1)>0 and ord(tree.cand_csc_st_4)>0 and ord(tree.cand_rpcf_st_2)>0) or 
        (ord(tree.cand_dt_st_1)>0 and ord(tree.cand_csc_st_4)>0 and ord(tree.cand_rpcf_st_3)>0) or 
        
        (ord(tree.cand_rpcb_st_1)>0 and ord(tree.cand_dt_st_2)>0 and ord(tree.cand_csc_st_1)>0) or 
        (ord(tree.cand_rpcb_st_1)>0 and ord(tree.cand_dt_st_2)>0 and ord(tree.cand_csc_st_2)>0) or 
        (ord(tree.cand_rpcb_st_1)>0 and ord(tree.cand_dt_st_2)>0 and ord(tree.cand_csc_st_3)>0) or 
        (ord(tree.cand_rpcb_st_1)>0 and ord(tree.cand_dt_st_2)>0 and ord(tree.cand_csc_st_4)>0) or 
        
        (ord(tree.cand_rpcb_st_2)>0 and ord(tree.cand_dt_st_1)>0 and ord(tree.cand_csc_st_1)>0) or 
        (ord(tree.cand_rpcb_st_2)>0 and ord(tree.cand_dt_st_1)>0 and ord(tree.cand_csc_st_2)>0) or 
        (ord(tree.cand_rpcb_st_2)>0 and ord(tree.cand_dt_st_1)>0 and ord(tree.cand_csc_st_3)>0) or 
        (ord(tree.cand_rpcb_st_2)>0 and ord(tree.cand_dt_st_1)>0 and ord(tree.cand_csc_st_4)>0) or 
        
        (ord(tree.cand_rpcb_st_1)>0 and ord(tree.cand_csc_st_1)>0 and ord(tree.cand_csc_st_2)>0) or 
        (ord(tree.cand_rpcb_st_1)>0 and ord(tree.cand_csc_st_1)>0 and ord(tree.cand_csc_st_3)>0) or 
        (ord(tree.cand_rpcb_st_1)>0 and ord(tree.cand_csc_st_1)>0 and ord(tree.cand_csc_st_4)>0) or 
        (ord(tree.cand_rpcb_st_1)>0 and ord(tree.cand_csc_st_2)>0 and ord(tree.cand_csc_st_3)>0) or 
        (ord(tree.cand_rpcb_st_1)>0 and ord(tree.cand_csc_st_2)>0 and ord(tree.cand_csc_st_4)>0) or 
        (ord(tree.cand_rpcb_st_1)>0 and ord(tree.cand_csc_st_3)>0 and ord(tree.cand_csc_st_4)>0) )

#_______________________________________________________________________________
def cand_3_st_tree(tree):
    ## 3 segments     
    return ( 
        cand_3_st_tree_3_segments_barrel(tree) or
        cand_3_st_tree_3_segments_endcap(tree) or
        cand_3_st_tree_3_segments_overlap(tree) or 
        cand_3_st_tree_2_segments_1_rechit_barrel(tree) or
        cand_3_st_tree_2_segments_1_rechit_endcap(tree) or
        cand_3_st_tree_2_segments_1_rechit_overlap(tree) )

#_______________________________________________________________________________
def cand_3_st_tree_3_segments_barrel_int(tree):
    return ( 
        (tree.cand_dt_st_1>0 and tree.cand_dt_st_2>0 and tree.cand_dt_st_3>0) or
        (tree.cand_dt_st_1>0 and tree.cand_dt_st_2>0 and tree.cand_dt_st_4>0) or
        (tree.cand_dt_st_1>0 and tree.cand_dt_st_3>0 and tree.cand_dt_st_4>0) or
        (tree.cand_dt_st_2>0 and tree.cand_dt_st_3>0 and tree.cand_dt_st_4>0) )

#_______________________________________________________________________________
def cand_3_st_tree_3_segments_endcap_int(tree):
    return ( 
        (tree.cand_csc_st_1>0 and tree.cand_csc_st_2>0 and tree.cand_csc_st_3>0) or
        (tree.cand_csc_st_1>0 and tree.cand_csc_st_2>0 and tree.cand_csc_st_4>0) or
        (tree.cand_csc_st_1>0 and tree.cand_csc_st_3>0 and tree.cand_csc_st_4>0) or
        (tree.cand_csc_st_2>0 and tree.cand_csc_st_3>0 and tree.cand_csc_st_4>0) )

#_______________________________________________________________________________
def cand_3_st_tree_2_segments_endcap_int(tree):
    return ( 
        (tree.cand_csc_st_1>0 and tree.cand_csc_st_2>0) or
        (tree.cand_csc_st_1>0 and tree.cand_csc_st_3>0) or
        (tree.cand_csc_st_1>0 and tree.cand_csc_st_4>0) or
        (tree.cand_csc_st_2>0 and tree.cand_csc_st_3>0) or
        (tree.cand_csc_st_2>0 and tree.cand_csc_st_4>0) or
        (tree.cand_csc_st_3>0 and tree.cand_csc_st_4>0) )

#_______________________________________________________________________________
def cand_3_st_tree_3_segments_overlap_int(tree):
    return (
        (tree.cand_dt_st_1>0 and tree.cand_dt_st_2>0 and tree.cand_csc_st_1>0) or
        (tree.cand_dt_st_1>0 and tree.cand_dt_st_2>0 and tree.cand_csc_st_2>0) or
        (tree.cand_dt_st_1>0 and tree.cand_dt_st_2>0 and tree.cand_csc_st_3>0) or
        (tree.cand_dt_st_1>0 and tree.cand_dt_st_2>0 and tree.cand_csc_st_4>0) or
        
        (tree.cand_dt_st_1>0 and tree.cand_dt_st_3>0 and tree.cand_csc_st_1>0) or
        (tree.cand_dt_st_2>0 and tree.cand_dt_st_3>0 and tree.cand_csc_st_1>0) or
        
        (tree.cand_dt_st_1>0 and tree.cand_csc_st_1>0 and tree.cand_csc_st_2>0) or
        (tree.cand_dt_st_1>0 and tree.cand_csc_st_1>0 and tree.cand_csc_st_3>0) or
        (tree.cand_dt_st_1>0 and tree.cand_csc_st_1>0 and tree.cand_csc_st_4>0) or
        
        (tree.cand_dt_st_1>0 and tree.cand_csc_st_2>0 and tree.cand_csc_st_3>0) or
        (tree.cand_dt_st_1>0 and tree.cand_csc_st_2>0 and tree.cand_csc_st_4>0) or
        
        (tree.cand_dt_st_1>0 and tree.cand_csc_st_3>0 and tree.cand_csc_st_4>0) or
        
        (tree.cand_dt_st_2>0 and tree.cand_csc_st_1>0 and tree.cand_csc_st_2>0) or
        (tree.cand_dt_st_2>0 and tree.cand_csc_st_1>0 and tree.cand_csc_st_3>0) )

#_______________________________________________________________________________
def cand_3_st_tree_2_segments_1_rechit_barrel_int(tree):
    return ( 
        (tree.cand_dt_st_1>0 and tree.cand_dt_st_2>0 and tree.cand_rpcb_st_3>0) or 
        (tree.cand_dt_st_1>0 and tree.cand_dt_st_2>0 and tree.cand_rpcb_st_4>0) or
        
        (tree.cand_dt_st_1>0 and tree.cand_dt_st_3>0 and tree.cand_rpcb_st_2>0) or
        (tree.cand_dt_st_1>0 and tree.cand_dt_st_3>0 and tree.cand_rpcb_st_4>0) or
        
        (tree.cand_dt_st_1>0 and tree.cand_dt_st_4>0 and tree.cand_rpcb_st_2>0) or
        (tree.cand_dt_st_1>0 and tree.cand_dt_st_4>0 and tree.cand_rpcb_st_3>0) or
        
        (tree.cand_dt_st_2>0 and tree.cand_dt_st_3>0 and tree.cand_rpcb_st_1>0) or
        (tree.cand_dt_st_2>0 and tree.cand_dt_st_3>0 and tree.cand_rpcb_st_4>0) or
        
        (tree.cand_dt_st_2>0 and tree.cand_dt_st_4>0 and tree.cand_rpcb_st_1>0) or
        (tree.cand_dt_st_2>0 and tree.cand_dt_st_4>0 and tree.cand_rpcb_st_3>0) or
        
        (tree.cand_dt_st_3>0 and tree.cand_dt_st_4>0 and tree.cand_rpcb_st_1>0) or
        (tree.cand_dt_st_3>0 and tree.cand_dt_st_4>0 and tree.cand_rpcb_st_2>0) )

#_______________________________________________________________________________
def cand_3_st_tree_2_segments_1_rechit_endcap_int(tree):
    return (
        (tree.cand_csc_st_1>0 and tree.cand_csc_st_2>0 and tree.cand_rpcf_st_3>0) or
        (tree.cand_csc_st_1>0 and tree.cand_csc_st_4>0 and tree.cand_rpcf_st_3>0) or
        (tree.cand_csc_st_2>0 and tree.cand_csc_st_4>0 and tree.cand_rpcf_st_3>0) or

        (tree.cand_csc_st_1>0 and tree.cand_csc_st_2>0 and tree.cand_rpcf_st_4>0) or
        (tree.cand_csc_st_1>0 and tree.cand_csc_st_3>0 and tree.cand_rpcf_st_4>0) or
        (tree.cand_csc_st_2>0 and tree.cand_csc_st_3>0 and tree.cand_rpcf_st_4>0) or
        
        (tree.cand_csc_st_1>0 and tree.cand_csc_st_3>0 and (tree.cand_gem_st_2>0 or tree.cand_rpcf_st_2>0)) or
        (tree.cand_csc_st_1>0 and tree.cand_csc_st_4>0 and (tree.cand_gem_st_2>0 or tree.cand_rpcf_st_2>0)) or
        (tree.cand_csc_st_3>0 and tree.cand_csc_st_4>0 and (tree.cand_gem_st_2>0 or tree.cand_rpcf_st_2>0)) or

        (tree.cand_csc_st_2>0 and tree.cand_csc_st_3>0 and (tree.cand_gem_st_1>0 or tree.cand_rpcf_st_1>0)) or
        (tree.cand_csc_st_3>0 and tree.cand_csc_st_4>0 and (tree.cand_gem_st_1>0 or tree.cand_rpcf_st_1>0)) or
        (tree.cand_csc_st_2>0 and tree.cand_csc_st_4>0 and (tree.cand_gem_st_1>0 or tree.cand_rpcf_st_1>0)) )

#_______________________________________________________________________________
def cand_3_st_tree_2_segments_1_rechit_gem_endcap_int(tree):
    return (
        (tree.cand_csc_st_1>0 and tree.cand_csc_st_3>0 and tree.cand_gem_st_2>0) or
        (tree.cand_csc_st_1>0 and tree.cand_csc_st_4>0 and tree.cand_gem_st_2>0) or
        (tree.cand_csc_st_3>0 and tree.cand_csc_st_4>0 and tree.cand_gem_st_2>0) or

        (tree.cand_csc_st_2>0 and tree.cand_csc_st_3>0 and tree.cand_gem_st_1>0) or
        (tree.cand_csc_st_3>0 and tree.cand_csc_st_4>0 and tree.cand_gem_st_1>0) or
        (tree.cand_csc_st_2>0 and tree.cand_csc_st_4>0 and tree.cand_gem_st_1>0) )

#_______________________________________________________________________________
def cand_3_st_tree_2_segments_1_rechit_GE21_endcap_int(tree):
    return (
        (tree.cand_csc_st_1>0 and tree.cand_csc_st_3>0 and tree.cand_gem_st_2>0) or
        (tree.cand_csc_st_1>0 and tree.cand_csc_st_4>0 and tree.cand_gem_st_2>0) or
        (tree.cand_csc_st_3>0 and tree.cand_csc_st_4>0 and tree.cand_gem_st_2>0) )

#_______________________________________________________________________________
def cand_3_st_tree_2_segments_1_rechit_GE21_nocscst2_endcap_int(tree):
    return (
        (tree.cand_csc_st_1>0 and tree.cand_csc_st_3>0 and tree.cand_gem_st_2>0 and tree.cand_csc_st_2<1) or
        (tree.cand_csc_st_1>0 and tree.cand_csc_st_4>0 and tree.cand_gem_st_2>0 and tree.cand_csc_st_2<1) or
        (tree.cand_csc_st_3>0 and tree.cand_csc_st_4>0 and tree.cand_gem_st_2>0 and tree.cand_csc_st_2<1) )

#_______________________________________________________________________________
def cand_3_st_tree_2_segments_1_rechit_overlap_int(tree):
    return ( 
        (tree.cand_dt_st_1>0 and tree.cand_dt_st_2>0 and tree.cand_rpcf_st_1>0) or 
        (tree.cand_dt_st_1>0 and tree.cand_dt_st_2>0 and tree.cand_rpcf_st_2>0) or 
        
        (tree.cand_dt_st_1>0 and tree.cand_csc_st_1>0 and tree.cand_rpcf_st_2>0) or 
        (tree.cand_dt_st_1>0 and tree.cand_csc_st_1>0 and tree.cand_rpcf_st_3>0) or 
        (tree.cand_dt_st_1>0 and tree.cand_csc_st_1>0 and tree.cand_rpcf_st_4>0) or 
        
        (tree.cand_dt_st_1>0 and tree.cand_csc_st_2>0 and tree.cand_rpcf_st_1>0) or 
        (tree.cand_dt_st_1>0 and tree.cand_csc_st_2>0 and tree.cand_rpcf_st_3>0) or 
        (tree.cand_dt_st_1>0 and tree.cand_csc_st_2>0 and tree.cand_rpcf_st_4>0) or 
        
        (tree.cand_dt_st_1>0 and tree.cand_csc_st_3>0 and tree.cand_rpcf_st_1>0) or 
        (tree.cand_dt_st_1>0 and tree.cand_csc_st_3>0 and tree.cand_rpcf_st_2>0) or 
        (tree.cand_dt_st_1>0 and tree.cand_csc_st_3>0 and tree.cand_rpcf_st_4>0) or 
        
        (tree.cand_dt_st_1>0 and tree.cand_csc_st_4>0 and tree.cand_rpcf_st_1>0) or 
        (tree.cand_dt_st_1>0 and tree.cand_csc_st_4>0 and tree.cand_rpcf_st_2>0) or 
        (tree.cand_dt_st_1>0 and tree.cand_csc_st_4>0 and tree.cand_rpcf_st_3>0) or 
        
        (tree.cand_rpcb_st_1>0 and tree.cand_dt_st_2>0 and tree.cand_csc_st_1>0) or 
        (tree.cand_rpcb_st_1>0 and tree.cand_dt_st_2>0 and tree.cand_csc_st_2>0) or 
        (tree.cand_rpcb_st_1>0 and tree.cand_dt_st_2>0 and tree.cand_csc_st_3>0) or 
        (tree.cand_rpcb_st_1>0 and tree.cand_dt_st_2>0 and tree.cand_csc_st_4>0) or 
        
        (tree.cand_rpcb_st_2>0 and tree.cand_dt_st_1>0 and tree.cand_csc_st_1>0) or 
        (tree.cand_rpcb_st_2>0 and tree.cand_dt_st_1>0 and tree.cand_csc_st_2>0) or 
        (tree.cand_rpcb_st_2>0 and tree.cand_dt_st_1>0 and tree.cand_csc_st_3>0) or 
        (tree.cand_rpcb_st_2>0 and tree.cand_dt_st_1>0 and tree.cand_csc_st_4>0) or 
        
        (tree.cand_rpcb_st_1>0 and tree.cand_csc_st_1>0 and tree.cand_csc_st_2>0) or 
        (tree.cand_rpcb_st_1>0 and tree.cand_csc_st_1>0 and tree.cand_csc_st_3>0) or 
        (tree.cand_rpcb_st_1>0 and tree.cand_csc_st_1>0 and tree.cand_csc_st_4>0) or 
        (tree.cand_rpcb_st_1>0 and tree.cand_csc_st_2>0 and tree.cand_csc_st_3>0) or 
        (tree.cand_rpcb_st_1>0 and tree.cand_csc_st_2>0 and tree.cand_csc_st_4>0) or 
        (tree.cand_rpcb_st_1>0 and tree.cand_csc_st_3>0 and tree.cand_csc_st_4>0) or

        (tree.cand_dt_st_2>0 and tree.cand_csc_st_1>0 and tree.cand_rpcf_st_2>0) or
        (tree.cand_dt_st_2>0 and tree.cand_csc_st_2>0 and tree.cand_rpcf_st_1>0) or 
        (tree.cand_dt_st_2>0 and tree.cand_csc_st_1>0 and tree.cand_rpcb_st_3>0) )

#_______________________________________________________________________________
def cand_3_st_tree_int(tree):
    ## 3 segments     
    return (cand_3_st_tree_3_segments_barrel_int(tree)
            or cand_3_st_tree_3_segments_endcap_int(tree)
            or cand_3_st_tree_3_segments_overlap_int(tree)
            or cand_3_st_tree_2_segments_1_rechit_barrel_int(tree)
            or cand_3_st_tree_2_segments_1_rechit_endcap_int(tree)
            or cand_3_st_tree_2_segments_1_rechit_overlap_int(tree) 
            )
