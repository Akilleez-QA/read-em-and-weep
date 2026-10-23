#!/usr/bin/env python3
"""Independent finite implication and arithmetic checks, not geometric verification.

No author verifier, historical enumerator, actual coefficient, actual point,
actual parameter, actual matrix, or actual-instance rank computation is used.
The W fusion graph is abstract group-representation input. All checks use
explicit exceptions, including under python -O.
"""
import copy
import hashlib
import itertools
import json
import math
import sys
from fractions import Fraction
from pathlib import Path

HERE=Path(__file__).resolve().parent
TARGET=Path(sys.argv[1]) if len(sys.argv)>1 else HERE.parent/'nine-profile-rank-bound'
class Failure(Exception): pass
CHECKS=0

def require(ok,why):
    global CHECKS
    CHECKS+=1
    if not ok: raise Failure(why)

def sha(b): return hashlib.sha256(b).hexdigest()
def exact(a,b): return json.dumps(a,sort_keys=True)==json.dumps(b,sort_keys=True)
def unit(name): return {name:1}
def combine(*terms):
    z={n:0 for n in NAMES}
    for scalar,rep in terms:
        for n,a in rep.items(): z[n]+=scalar*a
    return {n:a for n,a in z.items() if a}
NAMES=('1','W','A','S','D','T','V','P','Wp')
DIM=dict(zip(NAMES,(1,2,3,4,5,6,3,4,2)))
EDGES=(('1','W'),('W','A'),('A','S'),('S','D'),('D','T'),('T','V'),('T','P'),('P','Wp'))
def times_w(rep):
    z={n:0 for n in NAMES}
    for u,v in EDGES:
        z[u]+=rep.get(v,0);z[v]+=rep.get(u,0)
    return {n:a for n,a in z.items() if a}
def symmetric_action(n,rep):
    if n<0:return {}
    a,b=rep,times_w(rep)
    if n==0:return a
    for j in range(1,n):a,b=b,combine((1,times_w(b)),(-1,a))
    return b
def dimension(rep):return sum(DIM[n]*a for n,a in rep.items())

P22=[
'TWO-TWO-SYMMETRIC-QUOTIENT-DEFECT-IS-ZERO-OR-TWELVE.md',
'TWO-TWO-EXACT-NEGATIVE-KERNEL-SPLITTING-REFINEMENT.md',
'TWO-TWO-TOP-KERNEL-MULTIPLICITY-EXCLUDES-TEN-PAIRS.md',
'TWO-TWO-SECOND-INTERIOR-EULER-EXCLUDES-SEVENTEEN-PAIRS.md',
'TWO-TWO-ENDPOINT-TOP-SLOPE-LEAVES-THREE-PAIRS.md',
'TWO-TWO-ENDPOINT-RANK-DROP-EXCLUDES-LAST-THREE-PAIRS.md']
P31=['DUAL-CUBIC-IMAGE-HAS-RANK-AT-MOST-TWO','RANK-TWO-DUAL-IMAGE-FIVE-QUOTIENTS','FIVE-QUOTIENT-SECTION-ENVELOPES','SMALL-QUOTIENT-EXCLUSION','MIDDLE-QUOTIENT-EXCLUSION','LAST-LOW-QUOTIENT-EXCLUSION','FIRST-REMAINING-QUOTIENT-REDUCTION','FIRST-REMAINING-QUOTIENT-EXCLUSION','LAST-REMAINING-QUOTIENT-REDUCTION','DOUBLED-GAUSS-EXCLUSION','SINGLE-GAUSS-EXCLUSION','RANK-ONE-TEN-QUOTIENTS','RANK-ONE-DEGREE-ELEVEN-EXCLUSION','LAST-RANK-ONE-EXCLUSION']
P31=['EXTREMAL-31-'+s+'.md' for s in P31]
P32=['four-sources.md','SINGLE-D5-TYPE-EXCLUDED-BY-BACKWARD-GAUSS.md','THREE-P4-QUADRATIC-TYPES-EXCLUDED-BY-BACKWARD-GAUSS.md','P4-ZERO-PAIRING-EXCLUDED-BY-BACKWARD-PERSISTENCE.md','SINGLE-V-QUADRATIC-TYPE-EXCLUDED-BY-BACKWARD-EVALUATION.md','ZERO-QUADRATIC-TYPE-EXCLUDED-BY-BACKWARD-GAUSS.md']
SCOPES={(1,1):['profile11.md'],(1,2):['profile12.md'],(1,3):['EXTREMAL-13-FULL-SATURATION-EXCLUDES-THE-PROFILE.md','EXTREMAL-13-RANK-THREE-CUBIC-IMAGE-THREE-EXACT-QUOTIENTS.md','EXTREMAL-13-RANK-THREE-CUBIC-IMAGE-EXCLUSION.md','NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md'],(2,1):['profile21.md'],(2,2):P22,(2,3):['ADJACENT-RANK-THREE-GAUSS-EXCLUSION-AND-CONSTRAINTS.md'],(3,1):P31,(3,2):P32,(3,3):['EXCEPTIONAL-CUBIC-GAUSS-CORNER-EXCLUSION.md']}
LOWER={'0':'POSITIVE-DOUBLE-HYPERPLANE-GAUSS-GATE.md','1':'RANK-ONE-GAUSS-FLAG-DEGREE-EXCLUSION.md','2':'RANK-TWO-GAUSS-EXCLUSION-BY-ENDPOINT-FLAGS.md'}
SUPPORT=['RANK-TWO-GAUSS-PLATEAU-NECESSARY-BOUND.md','TWIST-ONE-ACTUAL-SECTION-KERNEL-VANISHING.md','GAUSS-DETERMINANT-ORBIT-RAMIFICATION.md']
SOURCES={'D':[1,1,1,0,0,1,0,0],'P':[1,1,1,0,1,0,0,0],'V':[1,1,2,0,0,0,0,0],'Z':[1,2,1,0,0,0,0,0]}
BR32={'D':['dual_cubic_rank1','dual_cubic_rank2'],'P':['pairing_zero','pairing_nonzero'],'V':['e2','e4'],'Z':['cubic_rank3','cubic_rank2_6_2','cubic_rank2_8_2','cubic_rank2_8_4']}

def authenticate():
    require(sha((HERE/'REVIEWED-INPUTS.json').read_bytes())=='b1f376130b3f6fe84e6d8e723b99751b90823c14604de4063e94b7b27b6c2cbc','reviewed immutable source list changed')
    manifest=json.loads((HERE/'REVIEWED-INPUTS.json').read_text())
    require(len(manifest)==52,'52 direct sources required')
    for line in (HERE/'TARGET-SHA256SUMS').read_text().splitlines():
        digest,name=line.split()
        require(sha((TARGET/name).read_bytes())==digest,'target hash: '+name)
    names=set()
    for r in manifest:
        b=(TARGET/r['file']).read_bytes()
        require(len(b)==r['bytes'],'source byte count')
        require(sha(b)==r['sha256'],'source digest: '+r['file'])
        require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==r['git_blob_sha1'],'source Git identity')
        require(r['url']=='https://github.com/Akilleez-QA/read-em-and-weep/blob/'+r['ref']+'/'+r['path'],'exact immutable URL')
        require(len(r['ref'])==40 and all(c in '0123456789abcdef' for c in r['ref']),'commit immutable')
        require(Path(r['file']).name not in names,'unique source basename')
        names.add(Path(r['file']).name)
    require(sha((TARGET/'inputs/profile11.md').read_bytes())=='a53c95281f491f09fffc3a3f8fcd542c2b2038d8306367f9c42c183b9e6e8c03','accepted full profile11 theorem')
    return manifest,names

def contract(c,available):
    g=c['geometry']
    require(exact([g[k] for k in ['ambient_dimension','coefficient_dimension','rank_E','degree_E','rank_Qdual','degree_Qdual']],[30,54,17,-54,13,-54]),'same actual rank/degree ambient')
    for key in ['actual','actual_images_retained','inherited_necessity_assumed','conditional_on_pinned_inputs']:
        require(g[key] is True,'actual/premise flag: '+key)
    require(g['physical_parameter']=='one_fixed_determinant_identification','physical marking')
    require(g['independent_rotation'] is False and g['horizontal_birkhoff'] is False,'forbidden identifications')
    p=c['plateau']
    for key in ['maximal','ordered','cubic_sections_E','cubic_sections_Qdual','saturated_sheaf_kernels']:
        require(p[key] is True,'plateau prerequisite: '+key)
    require(exact(p['k_range'],[1,2,3]) and exact(p['l_range'],[1,2,3]),'cubic lengths')
    require(type(p['endpoint_rank_at_most']) is int and p['endpoint_rank_at_most']==2,'endpoint rank cap')
    require(exact(c['lower_exclusions'],LOWER),'ranks zero one two all required')
    require(exact(c['lower_support'],SUPPORT),'lower exhaustion prerequisites')
    require(exact(c['four_sources'],SOURCES),'ordered four-source types')
    require(exact(c['branches32'],BR32),'32 complete source branches')
    rows=c['profiles']; seen=set()
    for row in rows:
        require(type(row['k']) is int and type(row['l']) is int,'integer profile indices')
        pair=(row['k'],row['l'])
        require(pair not in seen and pair in SCOPES,'ordered distinct profile')
        require(row['sources']==SCOPES[pair],'scope-matched complete proof chain')
        require(set(row['sources'])<=available,'source missing')
        seen.add(pair)
    require(seen==set(itertools.product(range(1,4),repeat=2)),'nine ordered alternatives')
    require(set(LOWER.values())|set(SUPPORT)<=available,'lower source missing')
    c22=c['coverage22']
    for key in ['necessity_chain_retained','original_positive_defect_retained','second_dual_defect12_retained']:
        require(c22[key] is True,'22 missing necessity/defect')
    require(c22['endpoint_rank3_assumed'] is False,'22 endpoint rank')
    c31=c['coverage31']
    require(exact(c31['cubic_ranks'],[1,2,3]),'nonzero cubic ranks exhaustive')
    require(exact(c31['rank2_quotients'],[[4,2],[6,2],[8,2],[6,4],[8,4]]),'five rank-two alternatives')
    require(c31['last_rank2_sectors']==['single11','doubled9'],'both last rank-two sectors')
    require(exact(c31['rank1_degrees'],[9,11]),'both rank-one degrees')
    require(c31['last_e9_shapes']==['two_O4','O4_plus_O6','W_O5'],'all final rank-one shapes')
    require(c31['endpoint_rank3_assumed'] is False,'31 endpoint rank')
    b=c['bridge']
    require(exact([b[k] for k in ['source_dimension','middle_dimension','target_dimension','rank_offset']],[41,54,37,24]),'actual square dimensions')
    require(b['first_map_injective'] is True and b['second_map_surjective'] is True,'actual linear map ranks')
    require(b['map_identity']=='actual_Koszul_derivative','map identity not dimension-only')
    possible=[r for r in range(min(g['rank_E'],g['rank_Qdual'])+1) if r not in {0,1,2,3}]
    smallest=min(possible)
    expected={'generic_SF_rank_lower':smallest,'generic_square_rank_lower':41-(17-smallest),'kernel_upper':17-smallest,'positive_double_hyperplane_sections_upper':17-smallest,'cokernel_upper':13-smallest}
    for key,value in expected.items():require(type(c['claim'][key]) is int and c['claim'][key]==value,'numerical conclusion: '+key)
    require(c['claim']['generic_only'] is True,'special-fiber promotion')
    for key in ['proof_assistant_verified','full_adjoint','original_repair','surjective','cone_rank36_improved']:
        require(c['claim'][key] is False,'unsupported promotion: '+key)
    return possible

def arithmetic():
    # Check the abstract W graph dimension relation at each irreducible.
    for name in NAMES:require(dimension(times_w(unit(name)))==2*DIM[name],'fusion dimensions')
    for n in range(31):
        v=symmetric_action(n,unit('1'))
        require(all(x>=0 for x in v.values()) and dimension(v)==n+1,'symmetric-power character')
    M2={'A':1,'V':2,'P':3,'D':4};M3={'Wp':3,'S':3,'T':6};M4={'V':2,'P':4,'D':3}
    require([dimension(x) for x in [M2,M3,M4]]==[41,54,37],'coefficient dimensions')
    require(combine((1,times_w(M3)),(-1,M2),(-1,M4))=={'A':2,'V':2,'P':2,'D':2},'actual plane ambient character')
    E1=combine((1,times_w(M4)),(-1,M3))
    E2=combine((1,symmetric_action(1,M3)),(-1,symmetric_action(2,M4)))
    E3=combine((1,symmetric_action(2,M3)),(-1,symmetric_action(3,M4)))
    Q3=combine((1,symmetric_action(2,M3)),(-1,symmetric_action(3,M2)))
    require(E1=={'Wp':1,'T':3} and E2=={'V':-1},'E lower Euler budgets')
    require(E3=={'Wp':1,'T':2} and Q3=={'T':1,'W':-2,'S':-1},'positive cubic Euler constituents')
    # Exhaust universal tuples, not selected actual bundles or source instances.
    all_types=[]; primary=[]
    for t in itertools.product(range(4),repeat=8):
        a,b,c,d,e,f,g,h=t
        if a+d+g+h!=1 or b+c+d+e+f+2*g+h!=3 or c+g+h<1:continue
        r2=3*(c+g+h-1)+4*(d+e+g+h)+5*(f+g)
        counts=[r2,2*a+6*b,3*c+4*d,2*e,f,2*g,h]
        require(sum(counts)==17 and sum(j*r for j,r in zip([2,3,4,5,8,9,10],counts))==54,'formal source rank/degree')
        all_types.append(t)
        if a>=1 and b>=1:primary.append(t)
    require(len(all_types)==28,'complete positive source equations')
    require(set(primary)==set(map(tuple,SOURCES.values())),'four-type exhaustion from both primary channels')
    # Pure integer rank constraints first yield 20 possibilities, then cubics give 9.
    numerical=[(k,l) for k in range(1,18) for l in range(1,14) if 17-3*k>=0 and 17+3*l<=30]
    bounded=[p for p in numerical if p[0]<=3 and p[1]<=3]
    require(len(numerical)==20 and set(bounded)==set(SCOPES),'actual maximal plateau rank bounds')
    ranks={str(k)+str(l):[17+3*(i-k) for i in range(k+l+1)] for k,l in bounded}
    for (k,l),seq in zip(bounded,ranks.values()):
        require(seq[k]==17 and all(b-a==3 for a,b in zip(seq,seq[1:])),'primal plateau orientation')
        dual=[30-x for x in seq[::-1]]
        require(dual[l]==13,'dual length exchange')
    # Universal complete-flag identity coefficients, not a selected ramification vector.
    for N in range(2,41):
        for r in range(1,N):
            require(r*(-N+1)+r*(r-1)==-r*(N-r),'unramified complete flag')
            for j in range(1,N):
                coefficient=-Fraction(r*(N-j),N)+max(r-j,0)
                expected=-Fraction((N-r)*j if j<r else r*(N-j),N)
                require(coefficient==expected and coefficient<0,'ramification coefficient sign')
    require(-17*13==-221 and -54>-221,'rank-one actual contradiction')
    # Original22 defect calculation preserves two different second-image defects.
    ab=[(a,b) for a in range(-2,19) for b in range(-10,7) if 0<=-6-a-b<=6]
    require(all((-6-a-b)==0 or -6-a-b<12 for a,b in ab),'original22 determinant gap')
    s2={a:[2*a+4,8-2*a] for a in [-2,0,2]}
    require(s2[-2]==[0,12] and s2[0]==[4,8] and s2[2]==[8,4],'second dual twelve retained exactly at a=-2')
    reachable={0}
    for value in range(105):
        if value in reachable:
            reachable.update(value+g for g in [96,160,240,60,100,150] if value+g<=104)
    require(104 not in reachable,'common32 endpoint semigroup obstruction')
    # Profile21 equality uses full Sym10, not an arbitrary 9-dimensional subspace.
    require(symmetric_action(10,unit('1'))=={'A':1,'V':1,'D':1},'degree-ten full system')
    require(max(sum(s) for m in range(3) for s in itertools.combinations([3,3,5],m))==8,'proper equivariant quotient capacity')
    caps={}
    for name,lam in {'2':[6,-4,-18],'5':[6,-6,-18],'9':[6,-8,-18],'10':[6,-11,-11]}.items():
        vals={(h,10-h):h*lam[0]-h*(h+1)+(10-h)*lam[1]-(10-h)*(11-h) for h in range(5,11)}
        caps[name]={'maximum':max(vals.values()),'maximizers':[list(k) for k,v in vals.items() if v==max(vals.values())]}
    require([caps[n]['maximum'] for n in ['2','5','9','10']]==[-38,-42,-46,-49],'profile21 capacities')
    require(caps['2']['maximizers']==[[7,3],[8,2]],'profile21 equality alternatives')
    # All admissible SF ranks obey the same exact sequence; no parameter is chosen.
    bridge=[]
    for r in range(14):
        ker=54-37-r;coker=54-41-r
        rank=41-ker
        require(rank==37-coker==24+r,'exact-square linear algebra')
        bridge.append({'SF':r,'square':rank,'kernel':ker,'cokernel':coker})
    return {'primal_types':len(all_types),'primary_types':[list(t) for t in primary],'numerical_plateaux':len(numerical),'ordered_cubic_plateaux':ranks,'Euler_E3':E3,'Euler_Qdual3':Q3,'profile21_capacities':caps,'second22_defect_caps':s2,'square_rank_table':bridge}

def controls(c,available):
    rejected=[]
    def bad(label,m,avail=available):
        try:contract(m,avail)
        except (Failure,KeyError,TypeError,ValueError):rejected.append(label);return
        raise Failure('accepted harmful mutation: '+label)
    for j,row in enumerate(c['profiles']):
        m=copy.deepcopy(c);del m['profiles'][j];bad('remove profile '+str((row['k'],row['l'])),m)
        for q,s in enumerate(row['sources']):
            m=copy.deepcopy(c);del m['profiles'][j]['sources'][q];bad('remove chain '+s,m)
    for n in ['0','1','2']:
        m=copy.deepcopy(c);del m['lower_exclusions'][n];bad('omit lower rank '+n,m)
    for key in ['generic_only','surjective','full_adjoint','proof_assistant_verified','original_repair','cone_rank36_improved']:
        m=copy.deepcopy(c);m['claim'][key]=not m['claim'][key];bad('promote '+key,m)
    for key in ['ambient_dimension','coefficient_dimension','rank_E','rank_Qdual','degree_E','degree_Qdual']:
        m=copy.deepcopy(c);m['geometry'][key]+=1;bad('change '+key,m)
    for key in ['maximal','ordered','cubic_sections_E','cubic_sections_Qdual','saturated_sheaf_kernels']:
        m=copy.deepcopy(c);m['plateau'][key]=False;bad('erase '+key,m)
    for group in ['D','P','V','Z']:
        for j in range(len(c['branches32'][group])):
            m=copy.deepcopy(c);del m['branches32'][group][j];bad('remove32 '+group+str(j),m)
    m=copy.deepcopy(c);m['geometry']['ambient_dimension']=54;bad('coefficient space substituted as constant ambient',m)
    m=copy.deepcopy(c);m['geometry']['independent_rotation']=True;bad('independent parameter rotation',m)
    m=copy.deepcopy(c);m['geometry']['horizontal_birkhoff']=True;bad('horizontal bundle splitting',m)
    m=copy.deepcopy(c);m['plateau']['endpoint_rank_at_most']=3;bad('rank-three endpoint',m)
    m=copy.deepcopy(c);m['coverage22']['second_dual_defect12_retained']=False;bad('erase second-dual12',m)
    m=copy.deepcopy(c);m['coverage31']['last_rank2_sectors']=['doubled9'];bad('omit single sector',m)
    m=copy.deepcopy(c);m['coverage31']['cubic_ranks']=[2,3];bad('omit cubic rank1',m)
    m=copy.deepcopy(c);m['coverage31']['rank2_quotients'].pop();bad('omit fifth quotient',m)
    m=copy.deepcopy(c);m['bridge']['map_identity']='dimension_matching';bad('dimension-only bridge',m)
    for field in ['first_map_injective','second_map_surjective']:
        m=copy.deepcopy(c);m['bridge'][field]=False;bad('erase '+field,m)
    m=copy.deepcopy(c);m['profiles'][1]['k'],m['profiles'][1]['l']=2,1;bad('replace12 by21',m)
    m=copy.deepcopy(c);m['profiles'][0]['k']=True;bad('boolean profile index',m)
    for n in sorted(set(sum(SCOPES.values(),[])+list(LOWER.values())+SUPPORT)):bad('missing actual proof '+n,c,available-{n})
    positives=0
    for order in [list(reversed(c['profiles'])),c['profiles'][4:]+c['profiles'][:4]]:
        m=copy.deepcopy(c);m['profiles']=order;require(contract(m,available)==list(range(4,14)),'irrelevant traversal order');positives+=1
    return {'rejected_count':len(rejected),'positive_order_controls':positives,'rejected':rejected}

def main():
    manifest,available=authenticate()
    c=json.loads((TARGET/'COVERAGE.json').read_text())
    allowed=contract(c,available)
    ar=arithmetic(); mut=controls(c,available)
    output={'status':'PASS','target_proof_sha256':sha((TARGET/'PROOF.md').read_bytes()),'scope':'conditional integration and abstract arithmetic; not independent reproof of all ancestor geometry','direct_inputs_authenticated':len(manifest),'allowed_generic_SF_ranks':allowed,'explicit_checks':CHECKS,'arithmetic':ar,'mutations':mut}
    print(json.dumps(output,indent=2,sort_keys=True))
if __name__=='__main__':main()
