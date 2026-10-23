"""Universal234-coefficient sparse/SymPy qB comparison, no source solve.

Distinct ha powers label every coefficient of Sym²(mixed12) tensor V; this
is a free-module coefficient embedding, not an actual-instance value.
Independent hb powers label all six external quadratic coefficients.
Every marking, source coordinate and physical channel scale stays free.
"""
from pathlib import Path
import hashlib,json,time
import sympy as s
import universal_q_middle_C_interface as ref
import universal_sparse_q_middle_source_adapter as sp
ROOT=Path(__file__).resolve().parent

def log(message):print('PASS:',message,flush=True)
def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
def same(a,b,label):
    if a!=b:raise AssertionError(label)

def main():
    started=time.time()
    pins={'Q-CUBIC-KERNEL-LIFT-AND-FULL-COMPLETION.sha256':'8a51729d04e922910d8b5e61e7651fbc7b006ae2a0f6a5597335660e3636e2d2',
          'SPARSE-Q-ORTHOGONAL8-ADDITIVE-SOURCE-ADAPTER.sha256':'b82f4a53c708ae106b98f516882b473d67b7c8ed3d4a1ac8bbfd5eaa4c76354d',
          'audit-q-middle-full-source-independent/INDEPENDENT-AUDIT.sha256':'7368cbcd8ecb9134dbd3f448ab2343ba3e508c41175106879bce8f5e61cb5bd7'}
    for p,h in pins.items():same(sha(p),h,('frozen input',p))
    # A tripwire catches any route through the unsupported old middle map.
    def forbidden(*a,**kw):raise AssertionError('Old supported source_map must not receive new qB middle data.')
    sp.SourceMap.source_map=forbidden
    b=sp.QMiddleSourceMap();lm=b.reference_matrix;lf=b.reference_forms;ns=b.ns
    t=ns['ha'];K=s.zeros(12);count=0
    for i in range(12):
        for j in range(i,12):
            entry=0
            for v in (ref.x,ref.y,ref.z):count+=1;entry+=t**count*v
            K[i,j]=K[j,i]=entry
    same(count,234,'all234 formal coefficient tags')
    # The reference q interface is independent of the sparse adapter.
    exact=ref.extend_q_middle_C_source(K)
    log('independent SymPy qB reconstruction completed on all234 free coefficient tags, with all marking/source parameters symbolic')
    data=b.interface_q_middle(lm(K));got=b.source_map_q_middle(lm(K));ex=exact['source_extension']
    for key in ('G5','quotient_Z','D3coeff','quotient_Y_coeff','D3_mixed_raw','D3_vww_raw','ZB','ZQ','RC_B','RC_Q','E','quotient_Z_C','C_C_anomaly_factor'):same(data[key],lm(exact[key]),key)
    for key in ('D3','quotient_Y'):same(data[key],[lf(F) for F in exact[key]],key)
    for key in ('Pc','H','y'):same(got['candidates'][key],sp.pack_matrix(lm(ex[key])),key)
    same(got['errors']['LC'],sp.pack_matrix(lm(ex['LC'])),'LC')
    for j,hg in enumerate(ex['high']):
        c='C%d'%j
        for key in ('high_spin','sigma_harmonic','Lharm'):
            val=hg[key] if isinstance(hg[key],s.MatrixBase) else s.Matrix([[hg[key]]])
            same(got['errors'][key+'_'+c],sp.pack_matrix(lm(val)),(key,j))
        same(got['errors']['high_full_remainder_'+c],sp.pack_forms(lf(hg['high_full_remainder'])),('full remainder',j))
        same(got['errors']['low_literal_'+c],sp.pack_forms(lf(ex['low_literal'][j])),('low literal',j))
        for key in ('E0','y','Lhigh','Lquot','sigma','rq'):
            val=hg[key] if isinstance(hg[key],s.MatrixBase) else s.Matrix([[hg[key]]])
            same(got['candidates'][key+'_'+c],sp.pack_matrix(lm(val)),(key,j))
        for key in ('R','R1','V0','Vnorm'):
            same(got['candidates'][key+'_'+c],sp.pack_forms(lf(hg[key])),(key,j))
        same(got['candidates']['raw_C_'+c],sp.pack_forms(lf(exact['D3'][j])),('raw C',j))
        same(got['candidates']['new_C5_'+c],sp.pack_forms(lf(ref.vww_leg(exact['G5'][:,j]))),('C5',j))
    same(len(got['errors']),26,'26 error sectors')
    for name in ('LC','low_literal','high_spin','sigma_harmonic','high_full_remainder','Lharm'):
        assert any(v['entries'] for k,v in got['errors'].items() if k==name or k.startswith(name+'_')),(name,'was filtered')
    log('every reduced sparse candidate and all26 error sectors agree with the independent full SymPy interface; all off-image C sectors remain nonzero')

    am,bm,cm,kAt=s.symbols('sparse_q_am sparse_q_bm sparse_q_cm sparse_q_kAt',nonzero=True)
    scales=(kAt,am,bm,cm);kap=bm/am
    restore=ref.restore_q_middle_companion(exact,am,bm,cm,kAt)
    def scaled_expected(value,kind):
        # Split literal Laurent channel scales independently with SymPy.
        if kind=='matrix':items=[((i,j),value[i,j]) for i in range(value.rows) for j in range(value.cols)]
        elif kind=='spinor_form':items=[((a,I),p) for a,f in enumerate(value) for I,p in f.items()]
        else:items=list(value.items())
        groups={}
        for index,poly in items:
            for term in s.Add.make_args(s.expand(poly)):
                if term==0:continue
                powers=tuple(int(term.as_powers_dict().get(v,0)) for v in scales)
                coeff=s.cancel(term/s.prod(v**p for v,p in zip(scales,powers)))
                group=groups.setdefault(powers,{})
                group[index]=group.get(index,0)+coeff
        packed={}
        for powers,entries in groups.items():
            entries={i:sp.public(b.load(s.expand(p.xreplace(b.reference_rename)))) for i,p in entries.items() if s.expand(p)!=0}
            if entries:
                packed[powers]={'kind':kind,'entries':entries}
                if kind=='matrix':packed[powers]['shape']=[value.rows,value.cols]
        return {'scale_variables':list(sp.SCALE_NAMES),'entries':packed}
    # Permit structural exact-zero scale terms in the public representation.
    def canonical(value):
        if isinstance(value,dict):
            if 'scale_variables' in value:return {**value,'entries':{k:canonical(v) for k,v in value['entries'].items() if v['entries']}}
            return {k:canonical(v) for k,v in value.items()}
        if isinstance(value,list):return [canonical(v) for v in value]
        return value
    def compare_scaled(actual,value,kind,label):same(canonical(actual),scaled_expected(value,kind),label)
    compare_scaled(got['source_left'],restore['source_left'],'matrix','all5 source left')
    compare_scaled(got['source_right'],restore['source_right'],'matrix','fixed negative-dual source right')
    alpha=[ref.adds(ref.sc(am,ref.A(s.eye(2)[:,i])),ref.sc(bm,ref.B(s.eye(2)[:,i]))) for i in range(2)]+[ref.sc(cm,ref.C_column(p)[0]) for p in ref.mon(2)]
    def alpha_action(v):return ref.adds(*(ref.sc(v[i],alpha[i]) for i in range(5)))
    residuals=[];errors=[]
    for i,c in enumerate(sp.COLUMNS):
        V=restore['divided_left'][i]
        compare_scaled(got['divided_left'][c],V,'spinor_form',('actual divided',c))
        raw=ref.sc(kAt/kap,exact['action'](alpha[i],am,bm))
        residual=ref.adds(raw,ref.sc(-1,alpha_action(restore['source_left'][:,i])))
        if i<2:E=[{},{}]
        else:
            j=i-2;h=ex['high'][j]
            harmonic=[ref.wedge({(k,):h['Lharm'][2*k+a] for k in range(3)},{(3,):-ref.w,(4,):ref.u}) for a in range(2)]
            E=ref.sc(kAt*cm,ref.adds(h['high_full_remainder'],harmonic,ref.sc(kap,ex['low_literal'][j])))
        compare_scaled(got['actual_raw_left'][c],raw,'spinor_form',('literal actual middle source',c))
        compare_scaled(got['actual_corrected_left_residual'][c],residual,'spinor_form',('literal corrected residual',c))
        compare_scaled(got['actual_error_left'][c],E,'spinor_form',('combined actual errors',c))
        ref.eqvec(ref.adds(residual,ref.sc(exact['q'],V)),E)
        compare_scaled(got['exterior_defect_left'][c],[ref.contract(ref.coords,f) for f in V],'spinor_form',('exterior defect',c))
        compare_scaled(got['exterior_defect_error'][c],[ref.contract(ref.coords,f) for f in E],'spinor_form',('error exterior defect',c))
        residuals.append(residual);errors.append(E)
    log('literal middle action on all5 sources agrees at every physical scale, with both q0 terms, Pc/y companions and actual lower divided quotient restored')
    for i in range(5):
        for j in range(i+1,5):
            label=sp.COLUMNS[i]+':'+sp.COLUMNS[j]
            dv=ref.add(ref.pair(alpha[i],restore['divided_left'][j]),ref.scale(-1,ref.pair(alpha[j],restore['divided_left'][i])))
            de=ref.add(ref.pair(alpha[i],errors[j]),ref.scale(-1,ref.pair(alpha[j],errors[i])))
            compare_scaled(got['d_squared_defect'][label],dv,'form',('d-squared',label))
            compare_scaled(got['d_squared_error_defect'][label],de,'form',('error d-squared',label))
            ref.eq(ref.scale(exact['q'],dv),de)
    assert any(F['entries'] for record in got['exterior_defect_left'].values() for F in record['entries'].values()),'Off-image closure defect must not be screened.'
    assert any(F['entries'] for record in got['d_squared_defect'].values() for F in record['entries'].values()),'Off-image d-squared defect must not be screened.'
    # Literal function-object bridge to the immutable unrestricted200 theorem.
    from universal_sparse_q_orthogonal_c_source_adapter import QOrthogonalSourceMap
    assert sp.QMiddleSourceMap.divided_right_pairing is QOrthogonalSourceMap.divided_right_pairing
    assert sp.QMiddleSourceMap.source_map_q_reduced is QOrthogonalSourceMap.source_map_q_reduced
    assert sp.QMiddleSourceMap._reduced is QOrthogonalSourceMap._reduced
    assert all(set(v['entries']).issubset({sp.CW,sp.INV}) for v in got['divided_left'].values())
    assert set(got['divided_left'])==set(sp.COLUMNS)
    for record in got['divided_left'].values():
        for F in record['entries'].values():
            assert F['kind']=='spinor_form'
            assert all(a in (0,1) and len(I)==2 and set(I).issubset(range(5)) for a,I in F['entries'])
    log('unchanged production right-pairing method and exact domain inclusion into the frozen200-free-cochain duality theorem; no scalar division or duplicated expensive test')

    # All six external quadratic coefficients, not selected harmonic inputs.
    ext=(ns['h']**2,ns['h']*ns['k'],ns['h']*ns['l'],ns['k']**2,ns['k']*ns['l'],ns['l']**2)
    external=sum(ns['hb']**(j+1)*p for j,p in enumerate(ext))
    ek=b.load(external);trace=sp.lapD(ek)
    full=b.source_map_q_middle(sp.matpoly(ek,lm(K)))
    baseline=b.tensor_payload(got);full_payload=b.tensor_payload(full)
    expected=sp.transform_tensors(baseline,lambda p:sp.mul(ek,p))
    same(canonical(full_payload),canonical(expected),'whole-cochain coefficientwise tensor product identity')
    same(canonical(sp.transform_tensors(full_payload,sp.lapD)),canonical(sp.transform_tensors(baseline,lambda p:sp.mul(trace,p))),'whole-cochain Laplacian commutes')
    projected=sp.transform_tensors(full_payload,sp.projectD)
    assert all(not sp.lapD(sp.unpack_poly(p)) for p in sp.tensor_polys(projected))
    assert not full['checks']['whole_external_harmonicity_all_outputs']
    assert any(sp.lapD(sp.unpack_poly(p)) for p in sp.tensor_polys(full_payload))
    assert all(all(m[i]>=0 for i in range(13)) for p in sp.tensor_polys(full) for m in p)
    log('all234 raw coefficients × all6 external quadratic coefficients commute with full-cochain Laplacian/Fischer projection; trace retained, not discarded, including both endpoints and every defect')
    for p,h in pins.items():same(sha(p),h,('frozen input unchanged',p))
    receipt={'schema':'universal-sparse-qB-source-adapter-verification-v1','raw_symmetric_positive_linear_coefficients':234,
        'external_quadratic_coefficients':6,'physical_source_columns':5,'error_sectors':26,'d_squared_components':10,
        'free_right_pairing_coefficients':20,'unrestricted_duality_domain_free_coefficients':200,'unrestricted_duality_exact_helper_reused':True,'all_marking_and_source_parameters_free':True,
        'sparse_equals_independent_SymPy_q_interface':True,'literal_actual_middle_action_all_sources':True,
        'off_image_exterior_and_d_squared_defects_retained':True,'whole_cochain_external_trace_and_harmonicity_checked':True,
        'old_supported_source_map_call_forbidden':True,'new_source_solve':'not run','new_family_column_generation':'not run','rank_tests':'not run',
        'point_or_actual_coefficient_tests':'not run','coordinate_divisions':[],
        'sources':{p:sha(p) for p in [*pins,'universal_sparse_q_middle_source_adapter.py','universal_sparse_q_orthogonal_c_source_adapter.py','universal_sparse_orthogonal_c_source_extension.py','verify_sparse_q_full_cochain_external_duality.py','verify_sparse_q_full_cochain_external_duality.log','verify_sparse_q_middle_source_adapter.py']},
        'elapsed_seconds':time.time()-started}
    (ROOT/'verify-sparse-q-middle-source-adapter-receipt.json').write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n')
    log('frozen q manifest unchanged; no solve, 55/65-family columns, source values, points or ranks; complete adapter certificate written')
if __name__=='__main__':main()
