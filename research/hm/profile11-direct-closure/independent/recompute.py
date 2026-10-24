#!/usr/bin/env python3
"""Independent fixed-159 certificate calculation from nine class characters.

No imports/execution of ../characters.py, ../verify.py, or the historical
verifier. No candidate enumeration. Symmetric characters use a closed binomial
polynomial, not a McKay recurrence or the reference's recurrence.
"""
from pathlib import Path
from fractions import Fraction
from math import comb
from functools import lru_cache
from collections import Counter
import ast
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parent.parent
OUT = Path(__file__).resolve().parent
CHECKS = 0

def require(condition, detail):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise RuntimeError(detail)

def sha256(data):
    return hashlib.sha256(data).hexdigest()

def git_blob(data):
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()

manifest_bytes = (ROOT/'INPUTS.json').read_bytes()
manifest = json.loads(manifest_bytes)
require(len(manifest) == 14, 'Fourteen pinned inputs required')
require(len({m['file'] for m in manifest}) == 14, 'Distinct input paths')
authenticated = []
for m in manifest:
    require(re.fullmatch(r'[0-9a-f]{40}',m['ref']) is not None, 'Immutable full commit')
    require(m['url'] == 'https://github.com/Akilleez-QA/read-em-and-weep/blob/'+m['ref']+'/'+m['path'], 'URL, ref and path agree')
    data = (ROOT/m['file']).read_bytes()
    observed = {'file':m['file'], 'url':m['url'], 'ref':m['ref'], 'path':m['path'],
                'bytes':len(data), 'sha256':sha256(data), 'git_blob_sha1':git_blob(data)}
    require(observed == m, 'Byte authentication: '+m['file'])
    authenticated.append(observed)

# Exact arithmetic in Q(sqrt(5)), using independent operations.
def q(a, b=0):
    return (Fraction(a), Fraction(b))
def qadd(x,y):
    return (x[0]+y[0],x[1]+y[1])
def qneg(x):
    return (-x[0],-x[1])
def qmul(x,y):
    return (x[0]*y[0]+5*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def qscale(c,x):
    return (c*x[0],c*x[1])
def qpow(x,n):
    ans=q(1)
    for _ in range(n):
        ans=qmul(ans,x)
    return ans

def qsum(values):
    ans=q(0)
    for x in values:
        ans=qadd(ans,x)
    return ans

# Read only the reference's class-defining assignments. The evaluator has no
# filesystem, Python execution, imports, attribute access or arbitrary calls.
reference=(ROOT/'inputs/character-reference.py').read_text()
tree=ast.parse(reference)
assignments={target.id: node.value for node in tree.body if isinstance(node,ast.Assign)
             for target in node.targets if isinstance(target,ast.Name)}
env={}
def eval_table(node):
    if isinstance(node, ast.Constant) and isinstance(node.value,int):
        return node.value
    if isinstance(node, ast.List):
        return [eval_table(x) for x in node.elts]
    if isinstance(node, ast.Name):
        return env[node.id]
    if isinstance(node, ast.UnaryOp) and isinstance(node.op,ast.USub):
        return -eval_table(node.operand)
    if isinstance(node,ast.Call) and isinstance(node.func,ast.Name):
        args=[eval_table(x) for x in node.args]
        return {'F':Fraction, 'z':q, 'neg':qneg}[node.func.id](*args)
    raise RuntimeError('Unexpected reference table expression: '+ast.dump(node))
for name in ('phi','phip','tr','sizes'):
    env[name]=eval_table(assignments[name])
traces=env['tr']; sizes=env['sizes']
# P is exactly list(map(z, [the nine recorded class values])).
pnode=assignments['P']
require(isinstance(pnode,ast.Call) and isinstance(pnode.func,ast.Name) and pnode.func.id=='list', 'P list expression')
mapnode=pnode.args[0]
require(isinstance(mapnode,ast.Call) and isinstance(mapnode.func,ast.Name) and mapnode.func.id=='map' and isinstance(mapnode.args[0],ast.Name) and mapnode.args[0].id=='z', 'P map expression')
p_values=eval_table(mapnode.args[1])
require(len(traces)==len(sizes)==len(p_values)==9 and sum(sizes)==120, 'Nine classes, group order120')

# Closed formula for the complete symmetric character of eigenvalues alpha,
# alpha^-1 with x=alpha+alpha^-1. It is a polynomial, valid at x=+/-2 too.
@lru_cache(None)
def symmetric_class(n,x):
    if n < 0:
        return q(0)
    return qsum(qscale((-1)**k*comb(n-k,k), qpow(x,n-2*k))
                for k in range(n//2+1))
@lru_cache(None)
def sym_values(n):
    return tuple(symmetric_class(n,x) for x in traces)

def class_add(*cs):
    return tuple(qsum(c[j] for c in cs) for j in range(9))
def class_product(a,b):
    return tuple(qmul(x,y) for x,y in zip(a,b))
def class_negative(a):
    return tuple(qneg(x) for x in a)

names=('one','W','Wp','A','V','P','S','D','T')
chars={'one':sym_values(0), 'W':tuple(traces), 'A':sym_values(2),
       'S':sym_values(3), 'D':sym_values(4), 'T':sym_values(5),
       'P':tuple(q(x) for x in p_values)}
chars['V']=class_add(sym_values(6),class_negative(chars['P']))
chars['Wp']=class_add(class_product(chars['W'],chars['P']),class_negative(chars['T']))

def scalar_product(a,b):
    return qscale(Fraction(1,120),qsum(qscale(size,qmul(x,y)) for size,x,y in zip(sizes,a,b)))
for x in names:
    for y in names:
        require(scalar_product(chars[x],chars[y])==q(int(x==y)), 'Irreducible orthonormality '+x+','+y)
dims={x:int(chars[x][0][0]) for x in names}
require(dims==dict(zip(names,(1,2,2,3,3,4,4,5,6))), 'Physical dimensions')
require(sum(v*v for v in dims.values())==120, 'All irreducibles accounted for')

def decompose(class_values):
    ans={}
    for name in names:
        a,b=scalar_product(class_values,chars[name])
        require(b==0 and a.denominator==1, 'Exact integral decomposition '+name)
        ans[name]=int(a)
    reconstructed=tuple(qsum(qscale(ans[name],chars[name][j]) for name in names) for j in range(9))
    require(reconstructed==class_values, 'Character reconstructed on all nine classes')
    return ans

@lru_cache(None)
def symmetric(n):
    return decompose(sym_values(n))

def h0(bundle,twist):
    terms=[class_product(chars[name],sym_values(e+twist)) for e,name in bundle if e+twist>=0]
    return decompose(class_add(*terms))

def euler(bundle,twist):
    terms=[]
    for e,name in bundle:
        d=e+twist
        if d>=0:
            terms.append(class_product(chars[name],sym_values(d)))
        elif d<=-2:
            terms.append(class_negative(class_product(chars[name],sym_values(-d-2))))
    return decompose(class_add(*terms))

def sum_char(*cs):
    return {name:sum(c[name] for c in cs) for name in names}
def difference(a,b):
    return {name:a[name]-b[name] for name in names}
def ordinary(bundle):
    return sorted((e for e,name in bundle for _ in range(dims[name])), reverse=True)

def endpoint(bundle,n):
    degrees=ordinary(bundle)
    require(len(degrees)==3,'Rank-three quotient for endpoint')
    heights=[]
    for first in range((n+1)//2,n+1):
        second=n-first
        ranks=[int(j<=first)+int(j<=second) for j in range(1,first+1)]
        require(sum(ranks)==n and all(x in (1,2) for x in ranks), 'Height partition ranks')
        # Independently sum the exterior-degree bounds stage by stage.
        value=sum(sum(degrees[:r])-2*j*r for j,r in enumerate(ranks,1))
        closed=first*degrees[0]-first*(first+1)+second*degrees[1]-second*(second+1)
        require(value==closed, 'Independent stage sum agrees with stated closed capacity')
        heights.append({'h1':first,'h2':second,'value':value})
    maximum=max(x['value'] for x in heights)
    return {'n':n,'ordinary_degrees':degrees,'height_values':heights,
            'capacity':maximum,'optimizers':[[x['h1'],x['h2']] for x in heights if x['value']==maximum]}

original=json.loads((ROOT/'inputs/profile11-pairs.json').read_bytes())
require(len(original)==159,'Exactly159 imported fixed records')
partition={k:[] for k in ('source_degree_or_rank','cubic_visibility','dual_capacity','primal_capacity','six_shapes')}
records=[]
for index,raw in enumerate(original):
    a_degrees=ordinary(raw['A']); b_degrees=ordinary(raw['B'])
    require(sum(a_degrees)==raw['a'] and sum(b_degrees)==raw['b'],'Original degree labels '+str(index))
    require(raw['defect']==-6-raw['a']-raw['b'],'Original determinant defect '+str(index))
    require(raw['defect'] in (0,12,20,24),'Original defect window '+str(index))
    for bundle in (raw['A'],raw['B']):
        for e,name in bundle:
            require(chars[name][1]==qscale(-1 if e%2 else 1,chars[name][0]),'Physical parity '+str(index))
    primal=endpoint(raw['A'],14)
    dual=endpoint(raw['B'],10)
    cubic=h0(raw['A'],3)
    if min(a_degrees)<-8 or a_degrees.count(-8)>1:
        reason='source_degree_or_rank'
    elif cubic['Wp']<1 or cubic['T']<2:
        reason='cubic_visibility'
    elif -54-raw['b']>dual['capacity']:
        reason='dual_capacity'
    elif -54-raw['a']>primal['capacity']:
        reason='primal_capacity'
    else:
        reason='six_shapes'
    partition[reason].append(index)
    records.append({'original_index':index,'A':raw['A'],'B':raw['B'],'a':raw['a'],'b':raw['b'],
        'original_defect':raw['defect'],'cubic_character':cubic,
        'primal_endpoint_degree':-54-raw['a'],'dual_endpoint_degree':-54-raw['b'],
        'primal':primal,'dual':dual,'first_reason':reason})
require([len(x) for x in partition.values()]==[56,32,62,3,6],'First-obstruction partition sizes')
require(partition['primal_capacity']==[32,50,52],'Three primal-only first obstructions')
require(partition['six_shapes']==[94,95,100,106,109,127],'Six exact original residual indices')
require(Counter(r['defect'] for r in original)=={0:80,12:61,20:5,24:13},'Imported original defect distribution')
for index,theorem in {94:'PR1135',95:'PR1135',100:'PR1142',106:'PR1142',109:'Section5',127:'PR1145'}.items():
    records[index]['closing_theorem']=theorem

sources={
 'D':[[-2,'D'],[-3,'Wp'],[-3,'T'],[-4,'V'],[-8,'one']],
 'P':[[-2,'P'],[-3,'Wp'],[-3,'T'],[-4,'V'],[-5,'Wp']],
 'V':[[-2,'V'],[-3,'Wp'],[-3,'T'],[-4,'V'],[-4,'V']],
 'Z':[[-3,'Wp'],[-3,'T'],[-3,'T'],[-4,'V']]}
source_facts={}
for label,bundle in sources.items():
    ds=ordinary(bundle)
    require(len(ds)==17 and sum(ds)==-54,'Actual source numerical type '+label)
    source_facts[label]={'bundle':bundle,'ordinary_degrees':ds,'cubic_sections':h0(bundle,3),
                         'quartic_euler':euler(bundle,4)}
    # Hom_G(E, Wp(-5)) from all blocks of the SAME displayed source.
    hom_terms=[(e,name, decompose(class_product(class_product(chars[name],chars['Wp']),sym_values(-5-e)))['one'])
               for e,name in bundle if e<=-5]
    source_facts[label]['hom_to_Wp_minus5_terms']=hom_terms
    source_facts[label]['hom_to_Wp_minus5']=sum(v for e,name,v in hom_terms)
require({label:x['hom_to_Wp_minus5'] for label,x in source_facts.items()}=={'D':0,'P':1,'V':0,'Z':0},'Only actual P-source can supply Wp(-5)')

# Independent whole-character telescope, including the individual invariant terms.
residual=original[109]
source10=h0(sources['P'],10)
target_terms=[{'i':i,'twist':10-2*i,'character':h0(residual['A'],10-2*i)} for i in range(9)]
target10=sum_char(*(x['character'] for x in target_terms))
scalar_degrees=list(range(26,9,-2))
scalar_invariants=[symmetric(n)['one'] for n in scalar_degrees]
negative_invariants=[decompose(class_product(chars['Wp'],sym_values(n)))['one'] for n in (5,3,1)]
source_invariant_terms=[h0([block],10)['one'] for block in sources['P']]
require(source_invariant_terms==[1,1,1,1,0],'Four source invariant contributors')
require(scalar_invariants==[0,1,0,1,0,0,0,1,0],'Nine scalar invariant terms')
require(negative_invariants==[0,0,0],'Negative-doublet terms contribute no invariant')
require([source10['one'],target10['one']]==[4,3],'Independent invariant contradiction4>3')
section5={'source':source10,'target':target10,'invariant_multiplicities':[4,3],'scalar_degrees':scalar_degrees}

# Fixed auxiliary identities used by the imported full proofs; no historical
# candidate enumeration is performed. Preserve negative tails in Euler values.
aux={}
for idx in (94,95,100,106,127):
    A=original[idx]['A']
    aux[str(idx)]={'h0_twist2':h0(A,2),'euler_twist4':euler(A,4),'hom_O2_A':h0(A,-2)['one']}
    if idx in (100,106):
        env=difference(sum_char(h0(A,2),euler(A,4)),euler(sources['D'],4))
        require(aux[str(idx)]['hom_O2_A']==0 and env['V']==-1,'PR1142 quartic obstruction '+str(idx))
        aux[str(idx)]['quartic_envelope']=env
for idx in (94,95):
    K4=difference(euler(sources['D'],4),euler(original[idx]['A'],4))
    require(K4==dict(zip(names,(0,0,0,0,2,2,0,0,0))), 'PR1135 kernel character '+str(idx))
    require(h0(original[idx]['A'],2)['V']==1,'PR1135 target has one V '+str(idx))
    aux[str(idx)]['kernel_twist4']=K4
require(records[119]['dual']['capacity']==-50 and records[119]['dual_endpoint_degree']==-26,'PR1145 positive defect capacity')
require(records[127]['dual']['optimizers']==[[7,3],[8,2]],'PR1145 two genuine equality heights')
require(records[127]['dual']['capacity']==records[127]['dual_endpoint_degree']==-38,'PR1145 zero defect equality')
aux['apolar']={'positive_defect_row':119,'zero_defect_row':127,
              'sextic_kernel_splits':[[a,6-a] for a in range(1,6)],
              'max_proper_Sym10_quotient_dimension':8,'max_proper_Sym8_quotient_dimension':5}
for a,b in aux['apolar']['sextic_kernel_splits']:
    require(4-a>=-1 and 4-b>=-1,'Basepoint-free sextic-net H1 vanishings')
for n,want in {6:{'V':1,'P':1},7:{'Wp':1,'T':1},8:{'P':1,'D':1},9:{'S':1,'T':1},10:{'A':1,'V':1,'D':1}}.items():
    require(symmetric(n)=={name:want.get(name,0) for name in names},'Physical symmetric identity '+str(n))

# Finish the independent certificate BEFORE opening either production result.
independent={'scope':'Conditional maximal-profile(1,1) closure only; no global profile exhaustion.',
 'proof_sha256':sha256((ROOT/'PROOF.md').read_bytes()),'manifest_sha256':sha256(manifest_bytes),
 'method':'Nine conjugacy classes; closed binomial symmetric characters; exact Fraction arithmetic; stagewise exterior-degree sums.',
 'input_authentication':authenticated,'original_record_count':len(records),'partition_indices':partition,
 'section5':section5,'records':records,'source_facts':source_facts,
 'twist10_detail':{'target_terms':target_terms,'source_invariant_terms':source_invariant_terms,
                  'scalar_invariants':scalar_invariants,'Wp_invariants':negative_invariants},
 'auxiliary_shape_checks':aux,
 'class_table':{name:[[str(a),str(b)] for a,b in chars[name]] for name in names},
 'symmetric_characters_0_through_31':{str(n):symmetric(n) for n in range(32)}}
(OUT/'CERTIFICATES.json').write_text(json.dumps(independent,indent=2)+'\n')

comparisons=[]
for filename in ('RESULT.json',):
    production=json.loads((ROOT/filename).read_bytes())
    require(production['records']==records,'All159 complete row certificates match '+filename)
    require(production['partition_indices']==partition,'Exact partition labels match '+filename)
    require(production['section5']==section5,'Whole twist10 characters match '+filename)
    require(production['input_count']==14 and production['original_record_count']==159,'Input/record counts match '+filename)
    comparisons.append({'file':filename,'sha256':sha256((ROOT/filename).read_bytes()),
                        'all159_complete_row_certificates_equal':True,
                        'all2226_height_values_equal':True,'section5_whole_characters_equal':True})
summary={'status':'PASS','proof_sha256':independent['proof_sha256'],
         'manifest_sha256':independent['manifest_sha256'],'checks':CHECKS,'inputs_authenticated':14,
         'fixed_records':159,'height_values':159*14,
         'partition_counts':{k:len(v) for k,v in partition.items()},'residual_indices':partition['six_shapes'],
         'invariant_deficit':[4,3],'certificate_sha256':sha256((OUT/'CERTIFICATES.json').read_bytes()),
         'comparisons':comparisons,
         'restrictions':'No historical enumeration; no actual-instance data; no production code imported or executed; no public writes.'}
(OUT/'SUMMARY.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
