#!/usr/bin/env python3
"""Typed rational normal ordering of actual selector/E combinatorics. No physical evaluation.

This is deliberately NOT a Laurent compiler or an actual stencil admission path.
Opaque physical leaves are inventoried, never passed to a zero oracle.
"""
from dataclasses import dataclass
from pathlib import Path
import hashlib
import json
import sys
import compile_refined_detector_metadata as metadata
import prune_refined_selector_paths as pruning
import owned_scalar_denominator_binding as owned
import physical_current_source_binding as currents
import resolution_selector_source_binding as selectors
import outer_partition_source_binding as outer

FRAME='global-finite-product-frame'
@dataclass(frozen=True)
class Scalar:
    op: str
    args: tuple
    frame: str=FRAME
    def __post_init__(self):
        if self.frame != FRAME: raise ValueError('unconverted scalar frame')
        arities={'constant':1,'leaf':2,'add':2,'multiply':2,'inverse':1,'partial':2,'owned_denominator':1,'owned_denominator_partial':2}
        if self.op not in arities or len(self.args)!=arities[self.op]:raise ValueError('bad scalar node')
        if self.op=='constant' and type(self.args[0]) is not int:raise ValueError('exact integers only')
        if self.op in ('add','multiply','inverse') and not all(isinstance(x,Scalar) for x in self.args):raise ValueError('scalar type')
        if self.op=='owned_denominator_partial' and (not isinstance(self.args[0],tuple) or len(self.args[0])!=5 or type(self.args[1]) is not int or not 0<=self.args[1]<4):raise ValueError('denominator partial')
        if self.op=='owned_denominator' and (not isinstance(self.args[0],tuple) or len(self.args[0])!=5):raise ValueError('complete denominator label required')
        if self.op=='partial' and (not isinstance(self.args[0],Scalar) or type(self.args[1]) is not int or not 0<=self.args[1]<4):raise ValueError('partial type')
    def __add__(self,b): return Scalar('add',(self,b))
    def __mul__(self,b): return Scalar('multiply',(self,b))
    def inv(self): return Scalar('inverse',(self,))
    def diff(self,i):
        if type(i) is not int or not 0<=i<4:raise ValueError('derivative coordinate')
        if self.op=='constant':return const(0)
        if self.op=='owned_denominator':return Scalar('owned_denominator_partial',(self.args[0],i))
        if self.op=='multiply':
            a,b=self.args;return a.diff(i)*b+a*b.diff(i)
        if self.op=='add':return self.args[0].diff(i)+self.args[1].diff(i)
        if self.op=='inverse':return const(-1)*self.args[0].diff(i)*self*self
        return Scalar('partial',(self,i))
    def data(self):return [self.op,*[x.data() if isinstance(x,Scalar) else x for x in self.args]]

def const(n):return Scalar('constant',(n,))
def leaf(name,*owners):return Scalar('leaf',(name,tuple(owners)))
def resolve_owned_definition(node):
    if node.op not in ('owned_denominator','owned_denominator_partial'):raise ValueError('not an owned definition')
    base=owned.denominator(owned.VertexLabel(*node.args[0]))
    return base if node.op=='owned_denominator' else owned.derivative(base,node.args[1])

def owned_D(seed,edge):
    return Scalar('owned_denominator',(owned.label(seed,edge[0]).data(),))*Scalar('owned_denominator',(owned.label(seed,edge[1]).data(),))

@dataclass(frozen=True)
class FirstOrder:
    edge: tuple
    coordinate: int
    zero: Scalar
    first: Scalar
    weighted_owners: tuple
    kernel_owners: tuple
    def __post_init__(self):
        if len(self.edge)!=2 or self.edge[0]>=self.edge[1]:raise ValueError('edge order')
        if not set(self.edge+self.kernel_owners)<=set(self.weighted_owners):raise ValueError('lost owner')
        if type(self.coordinate) is not int or not 0<=self.coordinate<4:raise ValueError('coordinate')
        if not isinstance(self.zero,Scalar) or not isinstance(self.first,Scalar):raise ValueError('multiplier type')

def normal_order(edge,i,C,D,conversion,alpha,beta,weighted,kernel):
    """C (alpha partial_i + beta)(conversion P / D) = zero P + first partial_i P.
    C stays OUTSIDE the derivative. Derivatives of conversion and D stay inside.
    alpha/beta describe the physical-character operator after frame conversion.
    """
    inv=D.inv()
    A=C*(alpha*(conversion.diff(i)*inv+const(-1)*conversion*D.diff(i)*inv*inv)+beta*conversion*inv)
    B=C*alpha*conversion*inv
    return FirstOrder(tuple(edge),i,A,B,tuple(weighted),tuple(kernel))

def branches(tail,pair=(0,1)):
    i,j,k=tail;a,b=pair
    return (((j,k),a,'L',b,1),((j,k),b,'L',a,-1),
            ((i,j),b,'U',a,1),((i,j),a,'U',b,-1))

def compile_term(seed, branch):
    """Instantiate the typed operator for one emitted seed/edge branch.
    C contracts the factored selector against a physical current and ALL weights.
    Physical realization of these exact leaf arguments remains an obligation.
    """
    sid=seed['seed'];edge=tuple(branch['edge']);d=branch['coordinate']
    C=const(seed['coefficient'])*const(branch['coefficient'][0])*const(2).inv()
    for owner in seed['weighted_owners']:C=C*leaf('outer_weight',sid,owner)
    C=C*leaf('selector_current_contraction',sid,branch['id'])
    pair=tuple(branch['derivative_pair']);input_pair=tuple(i for i in range(4) if i not in pair)
    conv=owned.character_conversion(pair,input_pair,d)
    return normal_order(edge,d,C,owned_D(sid,edge),const(conv['c']),const(conv['alpha']),const(conv['beta']),
        seed['weighted_owners'],seed['kernel_owners'])

def selected_branch():
    """Complete four-term formal E12 branch of the pinned selected row2 sector.
    Selector polynomials are written as factor ASTs, never expanded/evaluated.
    All physical currents remain arbitrary physical-frame traceless matrices.
    """
    v=[leaf('v'+str(i),'a') for i in range(5)];h=leaf('h1','a');nu=leaf('nu','a')
    s10=const(2)*v[1]*(v[1]*v[1]*v[4]+v[0]*v[3]*v[3])*h.inv()*nu*nu
    s00=const(2)*v[0]*v[1]*(v[0]*v[1]*v[1]+v[2]*v[2]*v[3])*h.inv()
    omega=leaf('outer_weight',0)*leaf('outer_weight',1)*leaf('outer_weight',2)
    out=[]
    for edge,d,kind,c,sign in branches((0,1,2)):
        contraction=s10*leaf(kind+str(c)+'_10_physical',0,1,2)+s00*leaf(kind+str(c)+'_00_physical',0,1,2)
        C=const(sign)*const(2).inv()*omega*contraction
        D=owned_D(4,edge)
        # Complementary E12 on pair34 has zero character in coordinates 0,1.
        # In global finite frame, stripping the output y_d gives alpha=1,beta=0.
        out.append(normal_order(edge,d,C,D,const(1),const(1),const(0),(0,1,2),(0,)))
    return {'scope':'row2 staircase (3,11,15); source-first sector; carrier(first)=1; E12 on pair34 scalar edges',
            'selector_frame':'Rbar10=nu(a)^2 Rphysical10; Rbar00=Rphysical00',
            'character_conversion':'V_d=y_d partial_xd; strip newly introduced y_d; input twist d=0; finite chart only',
            'status':'complete formal rational branch; physical leaf realization and Laurent lowering unresolved',
            'terms':[{'edge':t.edge,'coordinate':t.coordinate,'A':t.zero.data(),'B':t.first.data(),
                      'weighted_owners':t.weighted_owners,'kernel_owners':t.kernel_owners} for t in out]}

def build():
    paths=pruning.generate()['paths'];seeds=metadata.seed_records();out=[];leaves=[];obligations={}
    def unresolved(id,kind,args,uses,obligation):
        obligations[kind]=obligation
        leaves.append({'id':id,'type':kind,'arguments':args,'uses':uses})
    for path in paths:
        sid=path['seed']; tail=path['tail']; weighted=path['weighted_owners']
        kernel=sorted(set(o for _,o in path['left']+path['right']))
        rec={k:path[k] for k in ('seed','row','coefficient','tail','left','right','entry','weighted_owners','deleted_prefix_owners')}
        rec.update({'standard':seeds[sid]['standard'],'kappa':metadata.ROWS[path['row']][2],
                    'kernel_owners':kernel,'derivative_terms':[]})
        for pair in ((0,1),(2,3)):
            for n,(edge,d,kind,c,sign) in enumerate(branches(tail,pair)):
                uid=f's{sid}:p{pair[0]}:b{n}'
                rec['derivative_terms'].append({'id':uid,'edge':edge,'coordinate':d,'current':[kind,c,tail],
                    'coefficient':[sign,2],'derivative_pair':pair,'normal_order_template':'quotient-and-frame-v1'})
                current_binding=currents.bind_instance(sid,rec['derivative_terms'][-1])
                rec['derivative_terms'][-1]['current_source_binding']={
                    'id':current_binding['id'],'definition':current_binding['definition'],
                    'owners':current_binding['owners'],'kind':kind,'coordinate':c,
                    'normalized_source_ast':current_binding['normalized_source_ast'],
                    'contraction_frame_witness':'Iphysical Rphysical^t Pphysical=I Rnormalized^t P; same first owner; cancel diagonal frames once',
                    'physical_matrix_identified_with_normalized':False,
                    'moving_frame_log_terms_retained':True}
                if path['left'][-1]!=('I',tail[0]) or path['right'][0]!=('P',tail[0]):
                    raise ValueError('current selector first-owner frame mismatch')
                rec['derivative_terms'][-1]['owned_edge_definition']={'vertices':[owned.label(sid,o).data() for o in edge],
                    'definition':'owned-scalar-denominator-factored-v1','frame_conversion':{'c':1,'alpha':1,'beta':0},
                    'input_pair':tuple(i for i in range(4) if i not in pair)}
        rec['selector_source_binding']=selectors.bind_seed(sid)
        rec['outer_weight_source_bindings']=[outer.bind_reference(owned.label(sid,o)) for o in weighted]
        unresolved(f's{sid}:regularization','regularization_laurent',[weighted,seeds[sid]['standard']],
                   [x['id'] for x in rec['derivative_terms']],
                   'source-definition weight formulas are bound; prove actual source pole domain, source-first orientation, owned regularized cancellation and executable finite Laurent A/B lowering')
        for branch in rec['derivative_terms']:compile_term(rec,branch)
        out.append(rec)
    selected=json.loads(Path(__file__).with_name('selected-scalar-demand-dag.json').read_text())
    return {'schema':'hm-actual-scalar-rational-kernel-v5','status':'rational_normal_order_only',
        'actual_factorization_accepted':False,'actual_detector_authenticated':False,'execution_release':False,
        'physical_source_evaluated':False,
        'seed_count':len(out),'edge_branch_count':sum(len(x['derivative_terms']) for x in out),
        'label_domain':'all common labels over staircase; source-first sorting and its sign required; no tail merger',
        'operator_scope':'both E12*Phi and E34*Phi; edge numerators arbitrary, not T(F)-restricted',
        'selected_source_dag_sha256':hashlib.sha256(Path(__file__).with_name('selected-scalar-demand-dag.json').read_bytes()).hexdigest(),
        'selected_source_dag_not_full_domain_evidence':True,
        'selected_source_dag_unresolved':selected['unresolved'],
        'owned_denominator_definition':owned.definition(),'resolved_edge_frame_instances':624,
        'physical_current_source_definition':currents.definition(),'resolved_parameterized_current_instances':624,
        'resolution_selector_source_definition':selectors.definition(),'resolved_parameterized_selector_instances':78,
        'outer_partition_source_definition':outer.shared_definition(),
        'bound_outer_weight_source_definition_groups':len(out),
        'bound_outer_weight_owner_references':sum(len(rec['outer_weight_source_bindings']) for rec in out),
        'unresolved_regularization_Laurent_groups':len(leaves),
        'outer_weight_source_definition_is_executable_AST':False,
        'current_binding_scope':'normalized physical current inside proved matching selector contraction, not absolute physical matrix values',
        'normal_order_templates':{'quotient-and-frame-v1':'C*(alpha*(dc/D-c*dD/D^2)+beta*c/D) P + C*alpha*c/D partial(P)'},
        'unresolved_obligations':obligations,'seeds':out,'unresolved_leaves':leaves,'selected_complete_formal_branch':selected_branch(),
        'lowering_obligations':['lower bound source-definition formulas to executable arithmetic in the same frame; source binding alone is not lowering',
           'regularize grouped multipliers before Laurent coefficient extraction',
           'derive finite exact monomial A/B then call existing stencil checker',
           'prove complete equality before allowing actual admission; no flag or hash substitutes']}

if __name__=='__main__':
    if not __debug__:raise SystemExit('optimized Python refused')
    print(json.dumps(build(),sort_keys=True,separators=(',',':')))
