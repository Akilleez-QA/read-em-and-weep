"""Pin texts and emit exact analytic source recipes; no actual HM arithmetic."""
import hashlib
import json
from pathlib import Path
import subprocess
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
BASE=HERE.parent
def write(name,value):(HERE/name).write_text(json.dumps(value,indent=2)+'\n')
def sha(raw):return hashlib.sha256(raw).hexdigest()

def main():
    old='08b73637d4136f91606aad332c46cafd064417f8';null='10810ee877fdaf291399198ad60d7dd0c316a42d'
    source_rev='ce8b3eeae7159e2dcb146638789533360a3e32be'
    items=[(old,'research/hm/current-scalar-residual-attribution/first-order-source.md'),
        (old,'research/hm/current-scalar-geometric-dependencies/data/source-formulas.js'),
        (old,'research/hm/current-scalar-geometric-dependencies/frames-and-poles.md'),
        (old,'research/hm/current-scalar-proof/map-and-comparison.md'),
        (null,'research/hm/null-proof-foundations/direct-scalar-free-pairing-reduction.md'),
        (null,'research/hm/null-proof-foundations/hm-transition-only-first-lift-alternative.md'),
        (null,'research/hm/null-proof-foundations/hm-regular-cover-transport.md'),
        (null,'research/hm/null-proof-foundations/refined-tracefree-pole-domain.md'),
        (null,'research/hm/null-proof-foundations/m0-second-jet-survivor.md'),
        ('5df68750f766b18a746e50bff662b09829225ab1','research/hm/null-support-certificates/source-second-jet-degeneracy-certificate.md'),
        ('43193bc8badf3f29a1363132135d956cc12d46ad','research/hm/null-source-integration/scalar-family-transport/PROOF.md'),
        (source_rev,'research/codex-swarm/full-source-application/PROOF.md'),
        (source_rev,'research/codex-swarm/full-source-application/r_binding.py'),
        (source_rev,'research/codex-swarm/full-source-application/review-independent.md'),
        (source_rev,'research/codex-swarm/source-domain-application/PROOF.md')]
    pins=[]
    for commit,path in items:
        ref=commit+':'+path;raw=subprocess.check_output(['git','show',ref],cwd=ROOT)
        blob=subprocess.check_output(['git','rev-parse',ref],cwd=ROOT,text=True).strip()
        pins.append({'commit':commit,'path':path,'git_blob':blob,'sha256':sha(raw),'bytes':len(raw)})
    workspace=[]
    for name in('full-lift-domain/lift.py','full-lift-domain/test_lift.py','full-lift-domain/PROOF.md'):
        p=BASE/name;raw=p.read_bytes();workspace.append({'path':str(p.relative_to(ROOT)),
            'sha256':sha(raw),'bytes':len(raw),'scope':'toy engine/fixture reuse and corrected Pi-vs-cleared-prism theorem; no actual source factory executed'})
    write('source-pins.json',{'schema':'BI01-source-manifest-v1','immutable_dependencies':pins,
        'workspace_dependencies':workspace,'actual_source_evaluated':False,'physical_execution_authorized':False})
    write('actual-raw-s-denotation.json',{'schema':'BI01-fresh-raw-s-source-recipe-v1',
        'source_pin':{'commit':old,'path':'research/hm/current-scalar-residual-attribution/first-order-source.md','sections':[1,2,3,4]},
        'cover_order':'auxiliary5-first; primary0..4; numeric legal mask; standard tag; evaluate new increasing tuples THEN alternate',
        'pairs':[[0,1],[2,3]],'block_ranks':[5,15,10,2],'supertrace_signs':[-1,1,-1,1],
        'line_weights':[-1,1,3,5],
        'raw_split_bases':{'K0':'identity5','K1':'U0=(gamma,I,H1 W)','K2':'U1=(W,eta)','K3':'identity2',
            'inverses':'Q0=(H0;P;L delta_K), Q1=(L;ev)',
            'W':'8 nonpivot columns of ker(ev); e_k-(v_k/v_j)e_j in each five-coordinate block',
            'L':'selector of the eight nonpivot coordinates','eta':'pivot entries1/v_j',
            'pivots_by_carrier0_to5':[0,1,2,3,4,0]},
        'physical_refined_line_frames':{'nu':'product_i (y_i/x_i)^mask_i; coherent common base line frame',
            'U0_column_scalings':'(nu^-2 I5,1,nu^-2,nu^2 I8)',
            'U1_column_scalings':'(I8,nu^2 I2)','inverse_rows':'reciprocal scalings',
            'gamma_mask0':'0','gamma_mask1':'dx/[x(x^2-1)]','gamma_mask1_infinity':'-t dt/(1-t^2)',
            'moving_frames_differentiated':True,'nu_is_not_differentiated_as_constant1':True},
        'connection_blocks':'B_i=-(d U_i)U_i^-1-diag(k gamma_i); every physical derivative and frame term retained',
        'theta_pair':'theta_a=q_a,ij/2, theta_b=q_b,ij/2',
        'wedge':'tr(B_i,a B_j,b-B_i,b B_j,a)',
        'linear':'k*(theta_a tr(B_i,b+B_j,b)-theta_b tr(B_i,a+B_j,a))',
        'scalar':'sum_blocks(supertrace_sign*(wedge+linear))/4-15*q_a,ij*q_b,ij/8',
        'identity':'delta s_raw=(15/4)q_a cup q_b-tr(C_p)/2=F_p',
        'whole_Rraw_components':['complete M0 tracefree','F_q k_p,ik','F_p k_q,ik','E_p(s_raw,q)','E_q(s_raw,p)'],
        'M0_kinetic_term_count':7,'M0_negative_gerbe_term_count':3,
        'raw_source_owner_scope':'each scalar edge uses its two actual owners; full Rraw uses the same three source owners, no inner inserted labels',
        'source_specific_JTSH_symmetry_proved':False,'historical_source_value_identified':False,
        'future_required_implementation':'source-faithful complete cleared raw-s / complementary-derivative coefficient program in physical homogeneous frame',
        'physical_source_evaluated':False,'physical_execution_authorized':False})
    def box(m,r):
        D=357*m+r-2
        return {'owners':m,'internal_degree':r,'whole_numerator_degree_upper':D,
            'finite_exponent_rectangle':[-m*(2006+357),D+m*6677]}
    write('analytic-reduction.json',{'schema':'BI01-global-representative-replacement-v1',
        'explicit_boundary':'E_p(delta f)=delta B_p(f); B_p(f)_ij=((V_b f_i+V_b f_j)L_a-(V_a f_i+V_a f_j)L_b)/2',
        'full_source_comparison':'R_T-R_raw=delta(B_p(f_q)+B_q(f_p)); s_T-s_raw=delta f by pair H1=0',
        'global_comparison':'both admitted lifts separately represent their global class; acyclic standard/common cover pullback is quasiisomorphism; no cutoff bound asserted for comparison primitive',
        'all32_weighted_tests_equal':True,'common_values_computed':False,
        'additional_standard_boundary_power_for_raw_route':0,
        'std0_premise':'actual homogeneous raw-s carrier14/legal1 and derivative15/2 source theorem, with moving physical frames and all restrictions; not an affine-only bound',
        'raw_source_orders':{'carrier':32,'legal':18},'raw_full_lift_orders':{'carrier':54,'legal':29},
        'imported_outer_quotient_local_degree_bounds':{'finite':6677,'infinity':2006,
            'proof_commit':'43193bc8badf3f29a1363132135d956cc12d46ad','proof_path':'research/hm/null-source-integration/scalar-family-transport/PROOF.md','section':6},
        'J2':box(5,-2),'full_lift_max6_owners':box(6,-3),
        'rectangles_are_occupied_support':False,'six_owner_box_applies_to_seven_owner_deltaJ3':False,
        'nonconstant_product_or_memory_bound_proved':False,'new_execution_budget_issued':False,
        'physical_source_evaluated':False,'physical_execution_authorized':False,'obstruction_decided':False})

if __name__=='__main__':main()
