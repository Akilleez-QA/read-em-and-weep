"""Separate parameterized metadata lowering. Audited original is never changed.

The returned legacy schema is retained for original-byte equivalence; caller
certificates must state the parameterized scope explicitly. No polynomial evaluation.
"""
from lower_selected_kernel_denominators import *

def build(masks=(12,13,15)):
    if len(masks)!=3 or any(type(m) is not int or not 0<=m<16 for m in masks):raise ValueError('three legal masks required')
    outer.authenticate_public_sources()
    inverse_certificate=contraction_certificate()
    vs=tuple(owned.VertexLabel(4,o,b,m,t) for o,(b,m,t) in enumerate(((1,masks[0],3),(2,masks[1],11),(4,masks[2],15))))
    lo=Lower(vs);g=lo.g;v=lo.v
    terms=[]
    for edge,d,kind,c,sign in (((1,2),0,'L',1,1),((1,2),1,'L',0,-1),((0,1),1,'U',0,1),((0,1),0,'U',1,-1)):
        R=lo.tracefree(lo.current(kind,c))
        # Use the full pinned selected entry, avoiding an additional unproved
        # trace-free shortcut for each isolated current summand.
        I=lo.block(vs[0],'I');P=lo.block(vs[0],'P')
        contraction=lo.rat(g.c(0))
        for u in range(2):
            for w in range(2):contraction=lo.add(contraction,lo.mul(lo.mul(I[12][u],R[w][u]),P[w][6]))
        C=lo.mul(lo.rat(g.c(-2*sign,2)),contraction)
        inv=lo.edge_inverse(edge)
        terms.append({'edge':edge,'coordinate':d,'current':[kind,c],'E_sign':sign,'A':lo.cancel(lo.mul(C,lo.diff(inv,d))),'B':lo.cancel(lo.mul(C,inv))})
    return {'schema':'selected-full-owner-kernel-lowering-v1','scope':'one concrete structurally active candidate source-first full-owner tuple, all four E12 terms; not the entire symbolic label sum','owners':[v.data() for v in vs],'sorting_sign':1,'staircase':[3,11,15],'selector_terminal_coefficient_included_once':-2,'selector_rule':'full pinned -2*(I_a transpose(tf(R)) P_a)[12,6]; tf(R)=R-tr(R)/2 Id explicitly; no assumption tr(R)=0','frame':'global finite; normalized current after matching physical conjugation cancellation; outer scalar weights pulled back once; no section twist on scalar rho','transition_inverse_rewrite':{'rule':'inverse(C_ab)=C_ba','C_ab':'transpose(P_a I_b)','proof':'P_a I_a=Id; d I_a=0; P_a d=0; I_b P_b=Id-dH_b-H_bd imply (P_a I_b)(P_b I_a)=Id and reverse. Transposition gives C_ba C_ab=Id and C_ab C_ba=Id.','source_certificate':inverse_certificate},'dag':g.nodes,'terms':terms,'unresolved':['Independently verify the bounded-composition-sum lowering and full-owner pullback certificate.','Extend to every remaining full-owner label in the selected symbolic sector and then other kernel sectors.','Supply arithmetic schedule and peak-byte certificate before admission.'],'actual_factorization_accepted':False,'execution_release':False,'physical_polynomial_expansion':False,'physical_polynomial_evaluation':False,'held_limits':{'private_resource_configuration_omitted':True},'pinned_model_sha256':source.MODEL_SHA256}

