"""RS01: actual fresh five-term representative and coefficient-free closure.

This authenticates definitions and composes the fresh first-lift theorem.
Physical coefficients, jets and full fibers are never evaluated here.
"""
from pathlib import Path
import copy
import hashlib
import importlib.util
import json
import subprocess
import sys

HERE=Path(__file__).resolve().parent
BASE=HERE.parent
REV='e011d7c2e0b79f1b885e001c9b0e39b97618a424'
PINS_SHA='80de123d734a20c27de405cbef32282aedb6b9487cc0738f57c270e6d0f16c44'
SC='research/codex-swarm/scalar-compiler/'
FD='research/codex-swarm/source-domain-application/'


def need(ok,msg):
    if not ok:raise ValueError(msg)


def sha(raw):return hashlib.sha256(raw).hexdigest()


def authenticate(repo,reader=None):
    pinraw=(HERE/'source-pins.json').read_bytes()
    need(sha(pinraw)==PINS_SHA,'RS immutable pin manifest drift')
    pins=json.loads(pinraw);raws={}
    reader=reader or(lambda r,p:subprocess.check_output(['git','show',r+':'+p],cwd=repo,timeout=15))
    for row in pins['sources']:
        raw=reader(row['commit'],row['path'])
        need(type(raw)is bytes and sha(raw)==row['sha256'],'source bytes drift: '+row['path'])
        need(hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==row['git_blob'],'source blob drift')
        raws[row['commit'],row['path']]=raw
        if row['commit']==REV and row['path'].endswith(('.py','source-pins.json')):
            path=BASE.parents[1]/row['path']
            need(path.read_bytes()==raw,'local canonical dependency drift: '+row['path'])
    return pins,raws


def _load_domain():
    name='rs01_canonical_domain'
    if name in sys.modules:return sys.modules[name]
    path=BASE/'source-domain-application/domain.py'
    spec=importlib.util.spec_from_file_location(name,path);module=importlib.util.module_from_spec(spec)
    sys.modules[name]=module;spec.loader.exec_module(module);return module


def compiler_source_contract(template):
    """Bind every one of the existing20 universal source triples; no rebuild."""
    need(template['schema']=='complete-constant-scalar-compiler-v1','SC source schema')
    nodes=template['nodes'];need(len(nodes)==4270,'exact reviewed SC4270 graph')
    expected=['baseline','Fk12','Fk34','E12','E34']
    need(template['Rsharp_components']==expected,'all five source branches required')
    out=[]
    for rec in template['source_residual_components']:
        base=rec['baseline'];parts=rec['components']
        need(len(base['kinetic_terms'])==7 and len(base['gerbe_terms'])==3 and not base['legacy_scalar_correction'],'full M0 at u0=gk required')
        need(set(parts)==set(expected),'source component omissions')
        component_ids=[parts[k]for k in expected]
        root=[i for i,n in enumerate(nodes)if n['op']=='add'and n['shape']==[2,2]and n['children']==component_ids]
        need(len(root)==1,'exact five-term source sum')
        m0=nodes[base['M0']]
        need(m0['op']=='matrix_product'and len(m0['children'])==2,'left-normalized baseline')
        baseline_sum=nodes[m0['children'][1]]
        need(baseline_sum['op']=='add'and baseline_sum['children']==base['kinetic_terms']+base['gerbe_terms'],'seven kinetic plus three gerbe terms retained')
        out.append({'compiler_owner_slots':rec['owners'],'Rsharp_root':root[0],
                    'M0_root':base['M0'],'component_roots':copy.deepcopy(parts),
                    'kinetic_roots':base['kinetic_terms'][:],'gerbe_roots':base['gerbe_terms'][:]})
    need(len(out)==20,'all20 source triples')
    jets=[n for n in nodes if n['op']=='physical_jet']
    need(all(n['frames_differentiated']is True and len(n['directions'])<=2 and len(set(n['directions']))==len(n['directions'])for n in jets),'actual moving-frame distinct-axis twojets')
    return out


class ActualFullSourceApplication:
    def __init__(self,repo=None):
        repo=Path(repo)if repo is not None else HERE.parents[2]
        self._pins,raw=authenticate(repo)
        self._template=json.loads(raw[REV,SC+'compiled-template.json'])
        self._source=compiler_source_contract(self._template)
        self._domain=_load_domain();self._FD=self._domain.ActualDomainApplication(repo)

    @property
    def mode(self):return 'physical'

    def source_pins(self):return copy.deepcopy(self._pins)

    def describe(self,ordered_owners):
        owners=self._domain.whole_owners(ordered_owners)
        keys=[o.source_key for o in owners]
        need(keys[0]<keys[1]<keys[2],'strict increasing target source triple required')
        inner=[self._FD.describe(owners,p)for p in ((0,1),(2,3))]
        return {'schema':'actual-fresh-full-source-application-v1','ordered_owners':[list(o.data())for o in owners],
          'source_kind':'five-term Rsharp for SAME freshly defined first lift; not projected E-only source',
          'SC_source_reference':{'commit':REV,'path':SC+'compiled-template.json','node_count':4270,
              'universal_source_triples':copy.deepcopy(self._source),'bound_triple_record':copy.deepcopy(self._source[0]),
              'slot_binding':{str(i):list(o.data())for i,o in enumerate(owners)}},
          'actual_physical_leaf_dictionary':{
              'g_phys':'D_b*(P_a*I_b)^transpose*D_a^-1; actual pinned carrier primitives',
              'D':'diag(nu,nu^-1), actual coherent physical moving line frame; endpoint constants retained',
              'physical_jet':'actual distinct-axis invariant V derivatives of the moving matrix before common deck-factor removal; no frozen-frame derivative',
              'q':'(mask_b,i-mask_a,i)*y_i/x_i before deck stripping',
              'normalization':'form nonlinear row source, left multiply g_ik^-1, then strip full y product; transpose only for later column resolution inclusion'},
          'fresh_first_lift':{'pairs':[[0,1],[2,3]],'s':'s_pair=T_N14,pair F_pair',
              'T':'Hrho+R(Kcov Pi+A h S Pi), every branch retained',
              'k':'-mu_pair(g^-1,g)/2','u':'g*(s I+k)',
              'equation':'delta s=F; delta k=-C^0; hence delta(s I+k)=b I-C',
              'FD_actual_definitions':inner,'gauge_choice':'This exact fresh scalar homotopy solution; second-order transition coefficient set to zero to define its residual. No historical-order value/gauge identification is assumed.'},
          'ambient':{'base':'X=(y^2=x^3-x)^4; characteristic zero; h^3=0',
              'V':'V_i=y_i partial_xi+(3x_i^2-1)/2 partial_yi, commuting',
              'pi':'V0 wedge V1+V2 wedge V3','star':'fg+h mu1+h^2 mu2; mu1=pi/2, mu2=pi*pi/8',
              'Fij':'1+h^2 T_ij','Aijk':'1+h b_ijk+h^2 b_ijk^2/2',
              'coherence':['Fij Fjk=Ad_star(Aijk) Fik','Aijk star Aikl=Fij(Ajkl) star Aijl'],
              'b':'15/4*(q0 cup q1+q2 cup q3)',
              'T':'15/4*[(a0 cup q1)V1+(q0 cup a1)V0+(a2 cup q3)V3+(q2 cup a3)V2]',
              'a_mask':'a0=-x/2, a1=1/(2*x); V(q)=delta a',
              'coherence_status':'Published coefficient-free ambient theorem, not an unfilled source oracle; exact proof premises imported.'},
          'same_representative_identity':{
              'M':'g_ik^-1*(full ambient order-two defect for u_fresh, v=0), full-sign character component',
              'M0':'SAME globalCross with u_pair^0=g*k_pair; seven kinetic terms and all three negative gerbe terms',
              'W':'s_q*k_p+s_p*k_q, full End edge cochain',
              'identity':'Rsharp=M^0+delta W',
              'Rsharp':'M0^0+F_q*k_p,ik+F_p*k_q,ik+E_p(s_q)+E_q(s_p)',
              'boundary_sign':1,'pointwise_Rsharp_equals_M':False,
              'E':'1/2[(Va t_jk)Lb-(Vb t_jk)La+(Vb t_ij)Ua-(Va t_ij)Ub]',
              'L':'g_ij^-1 V(g_ij)','U':'g_ij^-1 g_jk^-1 V(g_jk) g_ij'},
          'closure_derivation':{
              'exact_defect':'Eijk=Fij(Gjk) star Gij-Aijk star Gik',
              'identity':'Aijk star Eikl+FijFjk(Gkl) star Eijk-Fij(Ajkl) star Eijl-Fij(Ejkl) star Gij=0',
              'h2':'Rikl+gkl Rijk-Rijl-Rjkl gij=0 after defects of order0 and1 vanish',
              'row_End':'delta(g_ik^-1 Rijk)=0',
              'Rsharp':'delta Rsharp=delta M^0+delta^2 W=0',
              'cohomology':'full-sign scalar H2=0 for O(-2,-2,-2,-2); therefore tf M has same class as M, and adding delta W preserves it',
              'identity_scope':'Published ambient coherence+actual source/model contraction premises and accepted FD fresh first-lift equation; no historic recomputation identity.'},
          'source_homogeneity':{'deck_character':[1,1,1,1],
              'scalar_character_eigensheaf':'O(-2,-2,-2,-2)',
              'matrix_frame':'actual physical row-End; conjugation/line frames retained',
              'tau_minus4_scope':'completed scalar after resolution/physical frame conversion, not a blanket twist assigned to every row matrix entry'},
          'source_pins':self.source_pins(),'historical_order_comparison_established':False,
          'physical_coefficients_evaluated':False,'actual_fibers_enumerated':False,
          'physical_execution_admitted':False,'outer_full54_29_5251_domain_discharged':False,
          'J0_J3_lift_extension_discharged':False,'obstruction_decided':False}

    def coefficient(self,*args,**kwargs):raise self._domain.I.PhysicalAdmissionMissing('RS01 is a source identity/closure application, not physical coefficient admission')
    def factor_terms(self,*args,**kwargs):return self.coefficient()
    def owners(self,*args,**kwargs):return self.coefficient()
