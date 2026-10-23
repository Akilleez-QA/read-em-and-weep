"""Additive raw-eight-leg q-source adapter, without a source solve.

The frozen supported SourceMap.source_map is NEVER used. The existing
OrthogonalSourceMap.source_map_new constructs only the reduced D3/G5
increment. All q0 N terms, physical scales, five columns, both endpoints,
and off-image exterior/d-squared defects are restored literally here.
"""
from copy import deepcopy
import universal_q_orthogonal_leg_completion as reference
from universal_sparse_orthogonal_c_source_extension import *

SCALE_NAMES = ('kAt','am','bm','cm')
S0 = (0,0,0,0)
CW = (1,0,0,1)
LOW = (1,-1,1,1)
INV = (1,1,-1,1)
COLUMNS = ('U0','U1','C0','C1','C2')


def unpack_poly(p):
    return {m+(0,0):c for m,c in p.items()}


def unpack_matrix(record):
    A=zeros(*record['shape'])
    for (i,j),p in record['entries'].items():A[i][j]=unpack_poly(p)
    return A


def unpack_forms(record):
    F=[{},{}]
    for (j,I),p in record['entries'].items():F[j][I]=unpack_poly(p)
    return F


def pack_form(F):
    return {'kind':'form','entries':{I:public(p) for I,p in F.items() if p}}


def pairing(F,G):
    return fadd(wedge(F[0],G[1]),fscale(-1,wedge(F[1],G[0])))


def clean_scaled(terms,kind='spinor_form'):
    result={}
    zero=(lambda:[{},{}]) if kind=='spinor_form' else (lambda:{})
    plus=vadd if kind=='spinor_form' else fadd
    for powers,value in terms:result[powers]=plus(result.get(powers,zero()),value)
    return {p:v for p,v in result.items() if (not vzero(v) if kind=='spinor_form' else bool(v))}


def pack_scaled(values,kind='spinor_form'):
    pack={'spinor_form':pack_forms,'form':pack_form,'matrix':pack_matrix}[kind]
    return {'scale_variables':list(SCALE_NAMES),'entries':{p:pack(v) for p,v in values.items()}}


def shift_scales(values,powers):
    return {tuple(a+b for a,b in zip(p,powers)):v for p,v in values.items()}


def tensor_polys(value):
    """Every public coefficient, including all restored cochain/defect data."""
    if isinstance(value,dict):
        if value.get('kind') in ('matrix','spinor_form','form'):
            yield from value['entries'].values()
        else:
            for v in value.values():yield from tensor_polys(v)
    elif isinstance(value,(tuple,list)):
        for v in value:yield from tensor_polys(v)


def transform_tensors(value,operation):
    """Coefficientwise transformation, never a partial middle-only projection."""
    if isinstance(value,dict):
        if value.get('kind') in ('matrix','spinor_form','form'):
            out={k:deepcopy(v) for k,v in value.items() if k!='entries'}
            out['entries']={k:q for k,p in value['entries'].items() if (q:=public(operation(unpack_poly(p))))}
            return out
        return {k:transform_tensors(v,operation) for k,v in value.items()}
    if isinstance(value,list):return [transform_tensors(v,operation) for v in value]
    if isinstance(value,tuple):return tuple(transform_tensors(v,operation) for v in value)
    return deepcopy(value)


def merge_tensor_records(records):
    """Linear sum of identically shaped packed coefficient records."""
    out=deepcopy(records[0])
    def add_into(a,b):
        if isinstance(a,dict) and a.get('kind') in ('matrix','spinor_form','form'):
            assert a['kind']==b['kind'] and a.get('shape')==b.get('shape')
            a['entries']={k:p for k in a['entries'].keys()|b['entries'].keys()
                          if (p:=add(a['entries'].get(k,{}),b['entries'].get(k,{})))}
        elif isinstance(a,dict):
            for k,v in b.items():
                if k in a:add_into(a[k],v)
                else:a[k]=deepcopy(v)
        elif isinstance(a,list):
            for aa,bb in zip(a,b):add_into(aa,bb)
    for record in records[1:]:add_into(out,record)
    return out


class QOrthogonalSourceMap(OrthogonalSourceMap):
    def __init__(self):
        super().__init__()
        self.reference_rename={v:self.ns[n] for v,n in (
            (reference.x,'x'),(reference.y,'y'),(reference.z,'z'),
            (reference.u,'u'),(reference.w,'w'),(reference.S,'S'),(reference.T,'T'),
            (reference.FB,'FB'),(reference.FC,'FC'),(reference.FD,'FD'),(reference.theta,'theta'))}
        self.reference_matrix=lambda A:self.lmat(A.xreplace(self.reference_rename))
        self.reference_forms=lambda F:self.lforms([{I:s.expand(p.xreplace(self.reference_rename)) for I,p in f.items()} for f in F])
        legs=reference.q_orthogonal_legs()
        self.q_Y=[self.reference_matrix(s.Matrix.hstack(*(leg['Y'][r] for leg in legs))) for r in range(2)]
        self.q_Z=self.reference_matrix(s.Matrix.hstack(*(leg['Z'] for leg in legs)))
        self.q_RC=self.reference_matrix(s.Matrix.vstack(*(leg['rC'] for leg in legs)))
        self.q_R0=self.reference_matrix(s.Matrix.vstack(*(leg['R0'] for leg in legs)))

    def mixed_q(self,V0,V1):
        return vcontract(vadd(putp(V0,(3,)),putp(V1,(4,))))

    def vww_q(self,G):return vcontract(putY(G,(3,4)))

    def interface_q(self,K):
        """Raw symmetric8x8 tensor over the fixed sparse Laurent ring."""
        assert len(K)==8 and all(len(r)==8 for r in K)
        assert matzero(matadd(K,matscale(-1,trans(K))))
        assert all(sum(m[:3])==1 for p in flat(K) for m in p), 'Positive-linear K required.'
        assert all(not m[3] and not m[4] and not m[17] and not m[18] for p in flat(K) for m in p)
        T=matmul(K,self.q_RC);T0=matmul(K,self.q_R0)
        return dict(D3=[vscale(-1,self.mixed_q(matmul(self.q_Y[0],col(T,j)),matmul(self.q_Y[1],col(T,j)))) for j in range(3)],
                    G5=matmul(self.q_Z,T),
                    quotient_Y=[self.mixed_q(matmul(self.q_Y[0],col(T0,j)),matmul(self.q_Y[1],col(T0,j))) for j in range(3)],
                    quotient_Z=matmul(self.q_Z,T0))

    def _reduced(self,D3,G5):
        """Retain trace input too: strip/reinsert external h,k,l coefficients.

        The frozen adapter asserts harmonicity. For nonharmonic input only,
        apply it coefficientwise in h,k,l, then restore ALL coefficients.
        No harmonic projection is performed and no trace term is discarded.
        """
        ps=flat(G5)+[p for F in D3 for ff in F for p in ff.values()]
        if all(not lapD(p) for p in ps):return self.source_map_new(D3,G5)
        degrees=sorted({m[10:13] for p in ps for m in p})
        results=[];base=None
        for degrees3 in degrees:
            def strip(p):
                out={}
                for m,c in p.items():
                    if m[10:13]==degrees3:
                        n=m[:10]+(0,0,0)+m[13:];out[n]=c
                return out
            dd=[[{I:q for I,p in ff.items() if (q:=strip(p))} for ff in F] for F in D3]
            gg=matfun(G5,strip)
            result=self.source_map_new(dd,gg)
            if base is None:base=result
            monomial=list(ZERO);monomial[10:13]=degrees3;monomial={tuple(monomial):s.S.One}
            results.append(transform_tensors({k:result[k] for k in ('errors','candidates','scaled_left_residual')},lambda p:mul(monomial,p)))
        out={**base,**merge_tensor_records(results)}
        out['checks']={**base['checks'],'whole_external_harmonicity_all_outputs':False,'external_trace_retained_coefficientwise':True}
        return out

    def source_map_q(self,K):
        interface=self.interface_q(K)
        return self.source_map_q_reduced(**interface,coefficient=K)

    def source_map_q_reduced(self,D3,G5,quotient_Y,quotient_Z,coefficient=None):
        """Restore q cochains. Input must arise from the symmetric raw8 map.

        Exact closure/d-squared checks below reject incompatible free data.
        This adapter does not decide whether any of the26 errors vanishes.
        """
        start=time.time();ex=self._reduced(D3,G5)
        cand=ex['candidates'];err=ex['errors']
        Pc=unpack_matrix(cand['Pc']);yy=unpack_matrix(cand['y'])
        upper=zeros(5,5);lower=zeros(5,5)
        for i in range(2):
            for j in range(3):upper[i][j+2]=Pc[i][j]
        for i in range(3):
            for j in range(3):lower[i+2][j+2]=scale(-1,yy[i][j])
        source={(1,-1,0,1):upper,(1,0,0,0):lower}
        right={p:matscale(-1,trans(A)) for p,A in source.items()}
        raw={c:{} for c in COLUMNS};residual={c:{} for c in COLUMNS};divided={c:{} for c in COLUMNS};errors={c:{} for c in COLUMNS}
        normalized={c:{} for c in COLUMNS}
        for j in range(3):
            c='C%d'%j;Y=quotient_Y[j];Z=self.vww_q(col(quotient_Z,j))
            V=unpack_forms(cand['Vnorm_'+c]);R1=unpack_forms(cand['R1_'+c])
            low=unpack_forms(err['low_literal_'+c])
            high=unpack_forms(err['high_full_remainder_'+c])
            Lharm=unpack_matrix(err['Lharm_'+c])
            high=vadd(high,[wedge(ff,self.j) for ff in putY(Lharm,())])
            normalized[c]=clean_scaled([(S0,vadd(V,Z)),((0,1,-1,0),vscale(-1,Y))])
            divided[c]=shift_scales(normalized[c],CW)
            raw[c]=clean_scaled([(CW,D3[j]),(LOW,self.vww_q(col(G5,j))),(INV,vmul(self.q,Y)),(CW,vmul(self.q,vscale(-1,Z)))])
            residual[c]=clean_scaled([(CW,R1),(LOW,low),(INV,vmul(self.q,Y)),(CW,vmul(self.q,vscale(-1,Z)))])
            errors[c]=clean_scaled([(CW,high),(LOW,low)])
            identity=clean_scaled(list(residual[c].items())+[(p,vmul(self.q,F)) for p,F in divided[c].items()]+[(p,vscale(-1,F)) for p,F in errors[c].items()])
            assert not identity, ('literal q restoration',c)
        exterior={c:{p:vcontract(F) for p,F in divided[c].items()} for c in COLUMNS}
        error_exterior={c:{p:vcontract(F) for p,F in errors[c].items()} for c in COLUMNS}
        for c in COLUMNS:
            assert not clean_scaled([(p,vmul(self.q,F)) for p,F in exterior[c].items()]+[(p,vscale(-1,F)) for p,F in error_exterior[c].items()]), ('exterior defect',c)
        alpha=[{(0,1,0,0):self.As[j],(0,0,1,0):self.Bs[j]} for j in range(2)]+[{(0,0,0,1):self.Cs[j]} for j in range(3)]
        def d2(forms):
            answer={}
            for i in range(5):
                for j in range(i+1,5):
                    terms=[]
                    for a,b,sign in ((i,j,1),(j,i,-1)):
                        for p,A in alpha[a].items():
                            for r,F in forms[COLUMNS[b]].items():terms.append((tuple(x+y for x,y in zip(p,r)),fscale(sign,pairing(A,F))))
                    answer[COLUMNS[i]+':'+COLUMNS[j]]=clean_scaled(terms,'form')
            return answer
        defect=d2(divided);error_defect=d2(errors)
        for label in defect:
            assert not clean_scaled([(p,fmul(self.q,F)) for p,F in defect[label].items()]+[(p,fscale(-1,F)) for p,F in error_defect[label].items()],'form'), ('d-squared defect',label)
        out={**ex,'schema':'q-orthogonal8-additive-sparse-source-adapter-v1',
             'source_left':pack_scaled(source,'matrix'),'source_right':pack_scaled(right,'matrix'),
             'normalized_divided_left':{c:pack_scaled(v) for c,v in normalized.items()},
             'divided_left':{c:pack_scaled(v) for c,v in divided.items()},
             'actual_raw_left':{c:pack_scaled(v) for c,v in raw.items()},
             'actual_corrected_left_residual':{c:pack_scaled(v) for c,v in residual.items()},
             'actual_error_left':{c:pack_scaled(v) for c,v in errors.items()},
             'exterior_defect_left':{c:pack_scaled(v) for c,v in exterior.items()},
             'exterior_defect_error':{c:pack_scaled(v) for c,v in error_exterior.items()},
             'd_squared_defect':{c:pack_scaled(v,'form') for c,v in defect.items()},
             'd_squared_error_defect':{c:pack_scaled(v,'form') for c,v in error_defect.items()},
             'q_quotient_Y':[pack_forms(F) for F in quotient_Y],
             'q_quotient_Z':pack_matrix(quotient_Z),'raw8_coefficient':pack_matrix(coefficient) if coefficient is not None else None}
        ps=list(tensor_polys(out))
        out['checks']={**ex['checks'],'literal_q_restoration':True,'all_five_physical_columns':True,
            'fixed_negative_dual_source_endpoint':True,'off_image_exterior_defects_retained':True,
            'off_image_d_squared_defects_retained':True,'q_times_exterior_equals_error_defect':True,
            'q_times_d_squared_equals_error_defect':True,'whole_external_harmonicity_all_outputs':all(not lapD(unpack_poly(p)) for p in ps),
            'whole_external_trace_never_projected_away':True}
        out['denominator_unit_max_powers']={NAMES[i]:max((max(-m[i],0) for p in ps for m in p),default=0) for i in range(13,17)}
        out['physical_scales']={**ex['physical_scales'],'C_output':'kAt*cm*(D3+kappa*p(G5)+q0*(kappa^-1*YKR0-ZKR0))',
            'normalized_actual_divided':'Vnorm-kappa^-1*YKR0+ZKR0','divided_left':'kAt*cm*normalized_actual_divided',
            'right_endpoint':'source_right=-source_left.T; divided right is the full alternating four-form pairing until closure'}
        out['scope']='Exact universal raw8 additive translation only. No enlarged family columns, source solve, rank, specialization, independence or descent asserted.'
        out['elapsed_seconds']=time.time()-start
        return out

    def divided_right_pairing(self,record,eta):
        """Always defined off-image; no illegal determinant division."""
        answer={}
        for c in COLUMNS:
            answer[c]=pack_scaled({p:pairing(unpack_forms(F),eta) for p,F in record['divided_left'][c]['entries'].items()},'form')
        return answer

    def tensor_payload(self,record):
        """Only mathematical data, for whole-cochain differential comparison."""
        keys=('errors','candidates','scaled_left_residual','source_left','source_right','normalized_divided_left','divided_left','actual_raw_left','actual_corrected_left_residual','actual_error_left','exterior_defect_left','exterior_defect_error','d_squared_defect','d_squared_error_defect','q_quotient_Y','q_quotient_Z','raw8_coefficient')
        return {k:record[k] for k in keys}
