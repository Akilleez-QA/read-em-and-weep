"""Metadata-only support analysis of the audited single-sector Laurent DAG.

No polynomial arithmetic or coefficient extraction. Bounds are exact integers
for a cancellation-blind support envelope, NOT exact polynomial support.
"""
from pathlib import Path
from itertools import product
import hashlib,json

ROOT=Path(__file__).parent
PIN='d07117856027c371cc3dd7c3dca21fc95fd34c32d8b84dbb6fa9693f416f506f'
COMPILER='8c3bb290df33a2d17da477cd30a36cc581aeddc4cdb3e276fdfbf35973ced89d'

class Refused(ValueError):pass

def optimize(c,lo,hi,total,maximize=False):
    """Exact bounded-composition linear optimum by integral greedy allocation."""
    if any(a>b for a,b in zip(lo,hi)) or not sum(lo)<=total<=sum(hi):
        raise Refused('empty composition domain')
    n=list(lo);left=total-sum(n)
    for i in sorted(range(len(c)),key=lambda i:(-c[i] if maximize else c[i],i)):
        delta=min(left,hi[i]-n[i]);n[i]+=delta;left-=delta
    if left:raise Refused('infeasible composition')
    return sum(a*b for a,b in zip(c,n))

class Support:
    def __init__(self,nodes):self.nodes=nodes;self.cache={};self.domains={}
    def domain(self,node):
        _,d,body=node;s=d['dimension'];T=d['threshold'];L=d['total'];j=d['chosen']
        if not (1<=s<=5 and 0<=j<s and T>=1 and L==s*(T-1)+1 and d['earlier_upper']==T-1):raise Refused('bad composition domain')
        lo=[T if i==j else 0 for i in range(s)];hi=[T-1 if i<j else L for i in range(s)]
        expected=[{'top':{'constant':L,'coefficients':[-1 if h<i else 0 for h in range(s)]},'bottom':{'constant':0,'coefficients':[int(h==i) for h in range(s)]}} for i in range(s)]
        if body['coefficient']!={'op':'multiply_binomials','factors':expected}:raise Refused('unsupported coefficient template')
        for p in body['powers']:
            e=p['exponent'];c=e['coefficients']
            if len(c)!=s or any(type(v)!=int for v in c+[e['constant']]):raise Refused('noninteger affine power')
            if optimize(c,lo,hi,L)+e['constant']<0:raise Refused('negative composition power')
            base=self.nodes[p['base']]
            if base[0]=='rational' and base[1]==0:
                # Current audited AST uses zero^n_i only. Preserve 0^0=1.
                if e['constant']!=0 or c.count(1)!=1 or any(v not in (0,1) for v in c):raise Refused('unsupported zero-base constraint')
                hi[c.index(1)]=0
        optimize([0]*s,lo,hi,L)
        return lo,hi,L
    def bound(self,index,w):
        key=(index,tuple(w))
        if key in self.cache:return self.cache[key]
        n=self.nodes[index];op=n[0]
        if op=='rational':r=None if n[1]==0 else (0,0)
        elif op=='coordinate':r=(w[n[1]],w[n[1]])
        elif op in ('add','multiply'):
            bs=[self.bound(k,w) for k in n[1:]]
            if op=='add':
                bs=[b for b in bs if b is not None]
                r=(min(b[0] for b in bs),max(b[1] for b in bs)) if bs else None
            else:r=None if None in bs else (sum(b[0] for b in bs),sum(b[1] for b in bs))
        elif op=='power':
            _,b,e=n
            if type(e)!=int:raise Refused('noninteger power')
            if e<0 and self.nodes[b][0]!='coordinate':raise Refused('noncoordinate inverse')
            q=self.bound(b,w)
            r=(0,0) if e==0 else None if q is None else tuple(sorted((e*q[0],e*q[1])))
        elif op=='bounded_composition_sum':
            lo,hi,L=self.domain(n);self.domains[index]={'lower':lo,'upper':hi,'total':L}
            constants=[0,0];coeffs=[[0]*len(lo) for _ in range(2)]
            for p in n[2]['powers']:
                b=self.bound(p['base'],w)
                if b is None:continue # domain already forces zero-base exponent=0
                e=p['exponent']
                for k in (0,1):
                    constants[k]+=b[k]*e['constant']
                    for i,c in enumerate(e['coefficients']):coeffs[k][i]+=b[k]*c
            r=tuple(constants[k]+optimize(coeffs[k],lo,hi,L,bool(k)) for k in (0,1))
        else:raise Refused('unknown AST operation')
        self.cache[key]=r;return r

def literal_unit_sum(s,index):
    """Prove singleton domain and body=1 using only literal zero/one bases."""
    node=s.nodes[index];lo,hi,L=s.domain(node)
    mins=[optimize([int(i==j) for i in range(len(lo))],lo,hi,L) for j in range(len(lo))]
    maxs=[optimize([int(i==j) for i in range(len(lo))],lo,hi,L,True) for j in range(len(lo))]
    if mins!=maxs:raise Refused('not a singleton composition')
    for p in node[2]['powers']:
        e=p['exponent'];power=e['constant']+sum(x*y for x,y in zip(e['coefficients'],mins))
        base=s.nodes[p['base']]
        if power!=0 and not (base[0]=='rational' and base[1]==base[2]):raise Refused('body not literal unit')
    # With one nonzero composition entry, every chained binomial is choose(N,0)
    # or choose(N,N). Domain validation authenticates that exact chain.
    if sum(x!=0 for x in mins)!=1:raise Refused('multinomial not syntactically one')
    return {'node':index,'unique_index':mins,'value':'1','zero_power_convention':'0^0=1 in the finite polynomial power template','coefficient_proof':'each chained binomial has bottom0 or bottom=top'}

def build():
    raw=(ROOT/'selected-full-owner-kernel-lowering.json').read_bytes()
    if hashlib.sha256(raw).hexdigest()!=PIN:raise Refused('audited artifact changed')
    if hashlib.sha256((ROOT/'lower_selected_kernel_denominators.py').read_bytes()).hexdigest()!=COMPILER:raise Refused('audited compiler changed')
    a=json.loads(raw);m=json.loads((ROOT/'refined-detector-metadata.json').read_text())
    if m['seeds'][4]!={'coefficient':-2,'lift_depth':0,'orientation':1,'row':2,'standard':[3,11,15]}:raise Refused('seed mismatch')
    row=m['terminal_rows'][2]
    if row!={'cell':'CCBB','coefficient':-2,'entry':['M11',12,6],'exponent':[-1,-2,-2,-2],'q':2}:raise Refused('terminal mismatch')
    kappa=row['exponent'];s=Support(a['dag']);directions=[list(w) for w in product((-1,0,1),repeat=4) if any(w)]
    # Homogeneous degrees: primary h has multidegree(5,5,5,5),
    # each standard section has degree5250 even on its finite chart.
    degrees=[[5250+14*5+(3 if (v[3]>>i)&1 else 1) for i in range(4)] for v in a['owners']]
    char=[0,0,-2,-2];out=[]
    for t in a['terms']:
        M=[char[i]+sum(degrees[v][i] for v in t['edge']) for i in range(4)]
        for kind in ('A','B'):
            delta=[int(kind=='B' and i==t['coordinate']) for i in range(4)]
            bounds=[s.bound(t[kind]['root'],[int(i==j) for i in range(4)]) for j in range(4)]
            candidates=[[max(int(kind=='B' and i==t['coordinate']),kappa[i]+delta[i]-bounds[i][1]),min(M[i],kappa[i]+delta[i]-bounds[i][0])] for i in range(4)]
            inequalities=[]
            for w in directions:
                low,high=s.bound(t[kind]['root'],w);target=sum(w[i]*(kappa[i]+delta[i]) for i in range(4))
                inequalities.append({'normal':w,'lower':target-high,'upper':target-low})
            domain=[[int(kind=='B' and i==t['coordinate']),M[i]] for i in range(4)]
            separators=[]
            for q in inequalities:
                w=q['normal']
                low=sum(v*domain[i][0 if v>=0 else 1] for i,v in enumerate(w))
                high=sum(v*domain[i][1 if v>=0 else 0] for i,v in enumerate(w))
                if high<q['lower'] or low>q['upper']:
                    separators.append({**q,'full_domain_projection':[low,high]})
            out.append({'edge':t['edge'],'kind':kind,'derivative':t['coordinate'] if kind=='B' else None,'root':t[kind]['root'],'target_shift':delta,'multiplier_coordinate_envelope':bounds,'complete_numerator_degree':M,'candidate_numerator_box':candidates,'candidate_linear_constraints':inequalities,'full_domain_separator':separators[0] if separators else None,'support_prunes_entire_multiplier':bool(separators),'box_prunes_entire_multiplier':any(l>h for l,h in candidates)})
    return {'schema':'selected-coefficient-support-preflight-v1','scope':'seed4 row2 standard(3,11,15) carrier(1,2,4) legal(12,13,15) only','audited_ast_sha256':PIN,'terminal_target':kappa,'input_character':char,'vertex_degrees':degrees,'formula':'w(edge,a)=sum_terms ([x^(kappa-a)]A + a_i [x^(kappa-a+e_i)]B)','composition_domains_after_literal_zero_constraints':s.domains,'literal_composition_collapse':literal_unit_sum(s,1301),'multipliers':out,'support_semantics':'sound cancellation-blind envelopes; membership does not assert nonzero','selected_sector_row_identically_zero_by_support':all(t['support_prunes_entire_multiplier'] for t in out),'remaining_scope':'No coefficient extraction is needed for this selected tuple on the complete numerator domain. Other full-owner tuples and sectors remain unproved. No global factorization or arithmetic admission follows.','actual_factorization_accepted':False,'execution_release':False,'physical_polynomial_evaluation':False,'physical_polynomial_expansion':False}

if __name__=='__main__':print(json.dumps(build(),sort_keys=True,indent=2))
