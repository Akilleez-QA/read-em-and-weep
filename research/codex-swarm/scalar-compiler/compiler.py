"""Typed complete-source scalar operator compiler; never a physical evaluator.

Cech faces and graded End homotopies are executable finite matrix circuits.
Outer regularization remains an explicit finite, owned sum, NOT a realization
of its rational coefficient payload. All source-admission gates stay false.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import importlib.util
import itertools
import json
import subprocess

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
PIN='10810ee877fdaf291399198ad60d7dd0c316a42d'
SHARED_SHA='3de33f88790e46bb62d4c400143ef62dea8b0b15d51bd18a4fb70689e3261f31'
WEIGHT_SHA='f256746fbfd0897fd4a5241e13715198004d277fec700b7ba5c4b3ace9bfe5e0'
MODEL_PATH='research/hm/null-operator-compiler/hm-pinned-model.json'
PINS={MODEL_PATH:'fcd48a9a22d40d55ce7a08b8aefcb4eaa2fdf761',
 'research/hm/null-operator-compiler/hm-pinned-source-formulas.js':'3dfed53a28b53b3c912a097971d89fc547330a5f',
 'research/hm/null-source-integration/combined-pole/PROOF.md':'9d7a5a400b48d9b8b46008fbd9fb3d79be601920',
 'research/hm/null-source-integration/order-comparison/source-order-curvature-comparison.md':'2be2660f33f791af9ce6ceda87be7693a41b7dfb'}


def need(ok,message):
    if not ok:raise ValueError(message)

def canonical(x):return json.dumps(x,sort_keys=True,separators=(',',':'),allow_nan=False)
def sha(x):return hashlib.sha256(x).hexdigest()

def authenticate():
    records=[];model=None
    for path,blob in PINS.items():
        raw=subprocess.check_output(['git','show',PIN+':'+path],cwd=ROOT,timeout=10)
        need(hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==blob,'source blob changed')
        records.append({'commit':PIN,'path':path,'git_blob':blob,'bytes':len(raw),'sha256':sha(raw)})
        if path==MODEL_PATH:model=json.loads(raw)
    extra_commit='43193bc8badf3f29a1363132135d956cc12d46ad'
    extra_path='research/hm/null-source-integration/scalar-family-transport/PROOF.md'
    raw=subprocess.check_output(['git','show',extra_commit+':'+extra_path],cwd=ROOT,timeout=10)
    need(hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()=='fc8befcc863efd073d4a66dc6eec12c722504447','uniform scalar transport pin changed')
    records.append({'commit':extra_commit,'path':extra_path,'git_blob':'fc8befcc863efd073d4a66dc6eec12c722504447','bytes':len(raw),'sha256':sha(raw)})
    shared=HERE.parent/'transport-binding/lift_schema.py';raw=shared.read_bytes()
    need(sha(raw)==SHARED_SHA,'shared lift schema changed')
    spec=importlib.util.spec_from_file_location('sc01_shared_lift',shared);module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    weights_raw=(HERE.parent/'detector-selection/weighted-requests.json').read_bytes()
    need(sha(weights_raw)==WEIGHT_SHA,'weighted request binding changed')
    return records,model,module,json.loads(weights_raw)


def gamma_coefficients(model):
    g=[[[0]*5 for _ in range(5)]for _ in range(15)]
    for i,row in enumerate(model['gamma']):
        for a,poly in enumerate(row):
            for key,z in poly:
                e=tuple(map(int,key.split(',')))
                need(len(e)==4 and sum(e)<=1 and min(e)>=0,'nonlinear homogeneous gamma')
                k=0 if sum(e)==0 else 1+e.index(1)
                g[i][a][k]+=z
    return g


def scalar_terms(g,i,b):
    need(type(i)is int and 0<=i<15 and type(b)is int and 0<=b<2,'scalar index')
    terms=[{'block':[3,1],'entry':[i,b],'coefficient':1}]
    for a in range(5):
        for k in range(5):
            if g[i][a][k]:terms.append({'block':[2,0],'entry':[a,5*b+k],'coefficient':-g[i][a][k]})
    return terms


def row_bottom_coefficients(g,terms):
    residual={}
    def put(a,b,k,z):
        key=(a,b,k);residual[key]=residual.get(key,0)+z
        if not residual[key]:del residual[key]
    for t in terms:
        block=t['block'];a,b=t['entry'];z=t['coefficient']
        if block==[2,0]:
            need(0<=a<5 and 0<=b<10,'X02 selector bounds');put(a,b//5,b%5,z)
        elif block==[3,1]:
            need(0<=a<15 and 0<=b<2,'X13 selector bounds')
            for u in range(5):
                for k in range(5):put(u,b,k,z*g[a][u][k])
        else:raise ValueError('wrong scalar block')
    return residual


def check_chain_rows(g):
    checks=0
    for i in range(15):
        for b in range(2):
            need(not row_bottom_coefficients(g,scalar_terms(g,i,b)),'scalar chain-map equation')
            checks+=50
    return checks


class Circuit:
    def __init__(self):self.nodes=[];self.cache={};self.derivatives={}
    def node(self,op,shape,children=(),**data):
        shape=tuple(shape);need(len(shape)==2 and all(type(x)is int and x>0 for x in shape),'matrix shape')
        record={'op':op,'shape':list(shape),'children':list(children),**data}
        key=canonical(record)
        if key in self.cache:return self.cache[key]
        need(len(self.nodes)<25000,'formal circuit node cap')
        n=len(self.nodes);self.nodes.append(record);self.cache[key]=n;return n
    def shape(self,n):return tuple(self.nodes[n]['shape'])
    def zero(self,shape):return self.node('zero',shape)
    def eye(self,n):return self.node('identity',(n,n))
    def leaf(self,name,shape,**data):return self.node('leaf',shape,name=name,**data)
    def scale(self,n,c):
        c=Q(c)
        if not c:return self.zero(self.shape(n))
        if c==1:return n
        return self.node('rational_scale',self.shape(n),(n,),coefficient=[c.numerator,c.denominator])
    def add(self,*nodes):
        need(bool(nodes),'empty sum');shape=self.shape(nodes[0]);need(all(self.shape(n)==shape for n in nodes),'sum shapes')
        use=[n for n in nodes if self.nodes[n]['op']!='zero']
        if not use:return self.zero(shape)
        if len(use)==1:return use[0]
        return self.node('add',shape,use)
    def mul(self,*nodes):
        need(bool(nodes),'empty product');rows,cols=self.shape(nodes[0])
        for n in nodes[1:]:
            r,c=self.shape(n);need(cols==r,'product shapes');cols=c
        return self.node('matrix_product',(rows,cols),nodes)
    def smul(self,s,m):
        need(self.shape(s)==(1,1),'scalar multiplier shape')
        return self.node('scalar_times_matrix',self.shape(m),(s,m))
    def transpose(self,n):return self.node('transpose',self.shape(n)[::-1],(n,))
    def trace(self,n):
        r,c=self.shape(n);need(r==c,'trace square');return self.node('trace',(1,1),(n,))
    def tf(self,n):
        r,c=self.shape(n);need(r==c==2,'tracefree rank two')
        return self.add(n,self.smul(self.scale(self.trace(n),Q(-1,2)),self.eye(2)))
    def inverse(self,n):
        r,c=self.shape(n);need(r==c==2,'only physical two-by-two inverse')
        return self.node('matrix_inverse',(2,2),(n,),source_determinant='one, source theorem required')
    def entry(self,n,a,b):
        r,c=self.shape(n);need(type(a)is int and type(b)is int and 0<=a<r and 0<=b<c,'entry index')
        return self.node('entry',(1,1),(n,),entry=[a,b])
    def D(self,n,d):
        need(type(d)is int and 0<=d<4,'physical derivative direction')
        if(n,d)in self.derivatives:return self.derivatives[n,d]
        rec=self.nodes[n];op=rec['op'];kids=rec['children'];shape=self.shape(n)
        if op in('zero','identity'):out=self.zero(shape)
        elif op=='add':out=self.add(*(self.D(k,d)for k in kids))
        elif op=='rational_scale':out=self.scale(self.D(kids[0],d),Q(*rec['coefficient']))
        elif op=='matrix_product':out=self.add(*(self.mul(*(kids[:j]+[self.D(k,d)]+kids[j+1:]))for j,k in enumerate(kids)))
        elif op=='scalar_times_matrix':out=self.add(self.smul(self.D(kids[0],d),kids[1]),self.smul(kids[0],self.D(kids[1],d)))
        elif op=='transpose':out=self.transpose(self.D(kids[0],d))
        elif op=='trace':out=self.trace(self.D(kids[0],d))
        elif op=='matrix_inverse':out=self.scale(self.mul(n,self.D(kids[0],d),n),-1)
        elif op=='complete_inner_solver':
            need(d not in rec['pair'],'only complementary solver derivative admitted')
            out=self.node('differentiate_combined_solver',shape,(n,),direction=d,
                 rule='first realize whole combined regular numerator; then differentiate including weights and physical frames',
                 combined_pole_pin=PINS['research/hm/null-source-integration/combined-pole/PROOF.md'],actual_source_clearing_witness=False)
        elif op in('leaf','physical_jet'):
            base=n if op=='leaf'else kids[0];ds=[]if op=='leaf'else rec['directions']
            out=self.node('physical_jet',shape,(base,),directions=sorted(ds+[d]),frames_differentiated=True)
        else:raise ValueError('unimplemented formal derivative: '+op)
        self.derivatives[n,d]=out;return out


class Source:
    def __init__(self,c):self.c=c;self.memo={};self.baselines={};self.components={}
    def g(self,a,b):return self.c.leaf('g_phys',(2,2),owners=[a,b],frame='physical row-End, complete moving frame')
    def gi(self,a,b):return self.c.inverse(self.g(a,b))
    def k(self,p,a,b):
        c=self.c;u,v=p;G=self.g(a,b);Ginv=self.gi(a,b)
        return c.scale(c.add(c.mul(c.D(Ginv,u),c.D(G,v)),c.scale(c.mul(c.D(Ginv,v),c.D(G,u)),-1)),Q(-1,4))
    def mu(self,p,B,A):
        c=self.c;a,b=p
        return c.scale(c.add(c.mul(c.D(B,a),c.D(A,b)),c.scale(c.mul(c.D(B,b),c.D(A,a)),-1)),Q(1,2))
    def mu2(self,B,A):
        c=self.c;terms=[]
        for a,b,e,f,z in[(0,2,1,3,1),(0,3,1,2,-1),(1,2,0,3,-1),(1,3,0,2,1)]:
            terms.append(c.scale(c.mul(c.D(c.D(B,a),b),c.D(c.D(A,e),f)),z))
        return c.scale(c.add(*terms),Q(1,4))
    def b(self,p,t):
        c=self.c;i,j,k=t;a,b=p
        qa=c.leaf('physical_q',(1,1),owners=[i,j],coordinate=a)
        qb=c.leaf('physical_q',(1,1),owners=[j,k],coordinate=b)
        return c.scale(c.mul(qa,qb),Q(15,4))
    def F(self,p,t):
        c=self.c;i,j,k=t
        curvature=c.mul(self.gi(i,k),self.mu(p,self.g(j,k),self.g(i,j)))
        return c.add(self.b(p,t),c.scale(c.trace(curvature),Q(-1,2)))
    def T(self,p,a,b):
        # Input is an actual universal F cochain circuit, not an untyped string.
        F=self.F(p,('inner_u','inner_v','inner_w'))
        c=self.c
        prism1=c.node('N14_prism_first',(1,1),(F,),output_owners=[a,b],sign=1,
            sum='sum_u rho_u F_[u,a,b]',inserted_standard_tag='r(u)=r(a)',full_occurrence_ownership=True)
        prism2=c.node('N14_prism_second',(1,1),(F,),output_owners=[a,b],sign=-1,
            sum='-sum_(u,v) rho_u rho_v F_[u,v,b]',inserted_standard_tags=['r(u)=r(a)','r(v)=r(b)'],full_occurrence_ownership=True)
        prism=c.node('N14_Hrho',(1,1),(prism1,prism2),whole_sum=True)
        standardK=c.node('N14_R_Kcov_Pi',(1,1),(F,),output_owners=[a,b],all_oriented_faces=True)
        standardh=c.node('N14_R_A_h_S_Pi',(1,1),(F,),output_owners=[a,b],full_h_branch_predicates=True)
        return c.node('complete_inner_solver',(1,1),(prism,standardK,standardh),pair=list(p),owners=[a,b],input_variables=['inner_u','inner_v','inner_w'],
            partition={'carrier':14,'legal':1,'pair_specific':True},standard_unit_order=5250,source_order='fresh consistent carrier/star-first, numeric legal mask, standard tag',
            combined_numerator_recipe='N_ab=C_a C_b Z_ab B_ab+Z_ab sum_u Qhat_u P_[u,a,b]-C_a Z_ab sum_(u,v) Qhat_u Qhat_v P_[u,v,b]',
            actual_source_clearing_witness=False)

    def E(self,p,solver_pair,t):
        c=self.c;i,j,k=t;a,b=p;sij=self.T(solver_pair,i,j);sjk=self.T(solver_pair,j,k)
        la=c.mul(self.gi(i,j),c.D(self.g(i,j),a));lb=c.mul(self.gi(i,j),c.D(self.g(i,j),b))
        ta=c.mul(self.gi(i,j),self.gi(j,k),c.D(self.g(j,k),a),self.g(i,j))
        tb=c.mul(self.gi(i,j),self.gi(j,k),c.D(self.g(j,k),b),self.g(i,j))
        return c.scale(c.add(c.smul(c.D(sjk,a),lb),c.scale(c.smul(c.D(sjk,b),la),-1),c.smul(c.D(sij,b),ta),c.scale(c.smul(c.D(sij,a),tb),-1)),Q(1,2))
    def residual(self,t):
        t=tuple(t)
        if t in self.memo:return self.memo[t]
        c=self.c;i,j,k=t;p=(0,1);q=(2,3);A=self.g(i,j);B=self.g(j,k);G=self.g(i,k)
        u=lambda pair,a,b:c.mul(self.g(a,b),self.k(pair,a,b))
        kin=[c.mul(u(p,j,k),u(q,i,j)),c.mul(u(q,j,k),u(p,i,j)),
             self.mu(p,u(q,j,k),A),self.mu(q,u(p,j,k),A),self.mu(p,B,u(q,i,j)),self.mu(q,B,u(p,i,j)),self.mu2(B,A)]
        bp=self.b(p,t);bq=self.b(q,t)
        gerbe=[c.scale(c.smul(bp,u(q,i,k)),-1),c.scale(c.smul(bq,u(p,i,k)),-1),c.scale(c.smul(c.mul(bp,bq),G),-1)]
        M0=c.mul(self.gi(i,k),c.add(*(kin+gerbe)));self.baselines[t]={'M0':M0,'kinetic_terms':kin,'gerbe_terms':gerbe,'legacy_scalar_correction':False}
        parts={'baseline':c.tf(M0),'Fk12':c.smul(self.F(q,t),self.k(p,i,k)),
               'Fk34':c.smul(self.F(p,t),self.k(q,i,k)),'E12':self.E(p,q,t),'E34':self.E(q,p,t)}
        self.components[t]=parts;out=c.add(*parts.values());self.memo[t]=out;return out


class Lift:
    def __init__(self,c,residual,schema,dims=(5,15,10,2)):
        self.c=c;self.R=residual;self.schema=schema;self.dims=dims;self.cache={}
        need([n['coefficient']for n in schema['nodes']]==[1,1,-1,1],'shared lift signs')
        need(schema['scalar_test_component']=='J2'and schema['top_component_required']=='J3','shared lift top component')
    def leaf(self,name,owner,shape):return self.c.leaf(name,shape,owner=owner,frame='original fixed resolution')
    def IP(self,owner):return self.leaf('I_phys',owner,(self.dims[1],2)),self.leaf('P_phys',owner,(2,self.dims[1]))
    def H(self,source,owner):
        need(1<=source<=3,'HK degree')
        return self.leaf(('H0','H1','eta')[source-1],owner,(self.dims[source-1],self.dims[source]))
    def merge(self,out,key,node):out[key]=self.c.add(out[key],node)if key in out else node
    def homotopy(self,F,r,owner):
        c=self.c;out={};I,P=self.IP(owner);EK=c.mul(I,P)
        for(u,v),node in F.items():
            need(v-u==r,'End internal degree')
            if v>0:self.merge(out,(u,v-1),c.mul(self.H(v,owner),node))
            if v==1 and u<3:self.merge(out,(u+1,v),c.scale(c.mul(EK,node,self.H(u+1,owner)),(-1 if r%2 else 1)))
        return out
    def delta(self,stage,t):
        out={}
        for j in range(len(t)):
            face=t[:j]+t[j+1:]
            for key,node in self.at(stage,face).items():self.merge(out,key,self.c.scale(node,(-1)**j))
        return out
    def at(self,stage,t):
        t=tuple(t);need(len(t)==stage+3 and len(set(t))==len(t),'ordered full common tuple')
        if(stage,t)in self.cache:return self.cache[stage,t]
        c=self.c
        if stage==0:
            I,P=self.IP(t[0]);out={(1,1):c.mul(I,c.transpose(self.R(t)),P)}
        else:
            node=self.schema['nodes'][stage]
            out=self.homotopy(self.delta(stage-1,t),node['homotopy_input_degree'],t[0])
            out={key:c.scale(n,node['coefficient'])for key,n in out.items()}
        self.cache[stage,t]=out;return out


def staircase_records():
    records=[]
    for perm in itertools.permutations(range(4)):
        tags=[0];tag=0
        for d in perm:tag|=1<<(3-d);tags.append(tag)
        sign=(-1)**sum(perm[i]>perm[j]for i in range(4)for j in range(i+1,4))
        records.append({'coordinate_order':list(perm),'standard_tags':tags,'orientation':sign})
    return records


def bind_outer_assignment(standard_tags,owners):
    """Instantiate a single whole outer summand; no source payload evaluated.

    Each owner=(test,occurrence,carrier,legal_mask,standard_tag). Prefix owners
    survive every subsequent face deletion. Sorting reindexes the pre-existing
    alternating cochain, never rebuilds a nonlinear directional prescription.
    """
    need(len(standard_tags)==len(owners)==5,'five outer owners')
    for t,o in zip(standard_tags,owners):
        need(len(o)==5 and all(type(x)is int for x in o),'integer full owner')
        need(0<=o[0]<32 and o[1]>=0 and o[4]==t and 0<=t<16 and 0<=o[2]<6 and 0<=o[3]<16,'owner request/occurrence/standard/carrier/mask')
    need(len({(o[0],o[1])for o in owners})==5,'occurrence identity merged')
    keys=[(-1 if o[2]==5 else o[2],o[3],o[4])for o in owners]
    order=sorted(range(5),key=lambda j:keys[j]);zero=len(set(keys))<5
    return {'zero':zero,'source_sorted_owners':[list(owners[j])for j in order],
        'sorting_sign':0 if zero else(-1)**sum(order[a]>order[b]for a in range(5)for b in range(a+1,5)),
        'partition_owners':[list(o)for o in owners],'rebuild_ordered_source':False}


def compile_template():
    pins,model,shared,weights=authenticate();g=gamma_coefficients(model);checks=check_chain_rows(g)
    schema=shared.closed_lift_schema();c=Circuit();source=Source(c);lift=Lift(c,source.residual,schema)
    components={}
    for stage in range(4):
        F=lift.at(stage,tuple(range(stage+3)))
        components['J'+str(stage)]=[{'block':list(key),'matrix':n}for key,n in sorted(F.items())]
    J2=lift.at(2,tuple(range(5)));scalar=[]
    I20=[(i,0)for i in range(5,11)]+[(i,1)for i in range(15)if i!=5]
    for i,b in I20:
        terms=scalar_terms(g,i,b)
        expr=c.add(*(c.scale(c.entry(J2[tuple(t['block'])],*t['entry']),t['coefficient'])for t in terms))
        scalar.append({'i':i,'b':b,'constant_terms':terms,'J2_scalar_circuit':expr})
    scalar_by_key={(r['i'],r['b']):r['J2_scalar_circuit']for r in scalar}
    transported={}
    for key,expr in scalar_by_key.items():
        transported[key]=c.node('finite_outer_cover_transport',(1,1),(expr,),staircases=staircase_records(),
           common_fibers=[{'variable':'a'+str(j),'standard_tag':'staircase['+str(j)+']','carrier_values':list(range(6)),'legal_mask_values':list(range(16))}for j in range(5)],
           summand='orientation * product_j rho(a_j) * same-source-alternating-stencil(sorted a)',partition={'carrier':54,'legal':29},standard_unit_order=5251,
           owner_policy='every full input occurrence and every deleted prefix retained; fixed r(a_j)=staircase[j]',
           source_extension='reindex existing alternating cochain; NEVER rebuild directional E after a permutation',
           uniform_transport_pin='fc8befcc863efd073d4a66dc6eec12c722504447',actual_domain_witness=False)
    requests=[]
    for r in weights['requests']:
        # Retain exact root-generated polynomial coefficient rows unchanged.
        key=tuple(r['scalar_map'])if isinstance(r['scalar_map'],list)else None
        if key is None:key=(r['scalar_map']['i'],r['scalar_map']['b'])
        coefficient_nodes=[c.scale(c.node('Laurent_coefficient',(1,1),(transported[key],),exponent=t['laurent_exponents'],output_index=t['output_index']),t['coefficient'])for t in r['terms']]
        requests.append({'weighted_request':r,'scalar_template':scalar_by_key[key],'compiled_output':c.add(*coefficient_nodes),
             'operation':'coefficient_of_complete_regularized_S_Pi_outer_sum',
             'transport_order':['complete closed total lift','Pi_outer on full EndK J2','signed S at CCCC','constant scalar row','weighted Laurent extraction']})
    return {'schema':'complete-constant-scalar-compiler-v1','source_pin':PIN,'source_bindings':pins,
      'shared_lift_schema_sha256':SHARED_SHA,'shared_lift_schema':schema,'shared_source_components':shared.source_components(),
      'weighted_requests_sha256':WEIGHT_SHA,'constant_chainmap_coefficient_checks':checks,
      'source_order':'fresh consistent: star first, numeric legal-mask integer, standard tag; historical equality NOT inferred',
      'Rsharp_components':['baseline','Fk12','Fk34','E12','E34'],'baseline_rule':'M0 at u0=gk retains all three gerbe terms; tracefree M0 before inclusion; never legacy scalar-inclusive residual',
      'source_residual_components':[{'owners':list(t),'components':source.components[t],'baseline':source.baselines[t]}for t in sorted(source.memo)],
      'lift_components':components,'scalar_templates':scalar,'requests':requests,
      'outer_transport':{'staircases':staircase_records(),'cover_cell':'CCCC','partition':{'carrier':54,'legal':29},
          'fiber_per_standard_vertex':{'carrier_values':list(range(6)),'legal_mask_values':list(range(16)),'count':96},
          'joint_fiber_count_before_alternation':96**5,'finite_sum':'sum over five full-owner fibers; product of their OWN weights; alternating extension of the SAME already-defined source cochain',
          'prefix_owners_retained':True,'standard_tag_is_target_unit':True,'scalar_merger_used':False,'legacy_78_seed_table_used':False},
      'closure':{'conditional_on':['delta Rsharp=0 from complete source','local graded contraction identities','regular full-cover comparison'],
          'equations':schema['closure_equations'],'scalar_identity':'delta L(J2)=L(d_End J3)=0 by all polynomial chain-map coefficients',
          'top_J3_discarded':False,'source_geometry_instantiated':False},
      'nodes':c.nodes,'counts':{'nodes':len(c.nodes),'scalar_maps':20,'weighted_tests':len(requests),'staircases':24,'weighted_coefficient_occurrences':127,'distinct_map_exponent_pairs':121,'staircase_occurrences_before_selector_and_outer_fibers':127*24},
      'gates':{'formal_circuit_compiled':True,'pinned_bytes_authenticated':True,'constant_chainmap_checked':True,'uniform_transport_theorem_available':True,
          'physical_matrix_leaf_lowering':False,'actual_F_source_clearing_witness':False,'all_twenty_row_transport_domain':False,
          'outer_fiber_coefficient_realization':False,'historical_order_identification':False,'physical_source_evaluated':False,'execution_release':False},
      'obstruction':'undecided'}


def validate_template(candidate):
    expected=compile_template()
    need(canonical(candidate)==canonical(expected),'compiled circuit/binding/owner/sign/gate mismatch')
    return True

if __name__=='__main__':
    out=compile_template();encoded=json.dumps(out,sort_keys=True,indent=2)+'\n'
    need(len(encoded.encode())<=4_000_000,'formal circuit output cap')
    print(encoded,end='')
