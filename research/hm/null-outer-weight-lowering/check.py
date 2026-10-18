"""Static source wiring plus independent tiny formal/index controls; no production execution."""
import ast, hashlib, json, math
from pathlib import Path
ROOT=Path(__file__).resolve().parent
def need(x,msg):
    if not x: raise ValueError(msg)
manifest=(ROOT/'pins.json').read_bytes()
need(hashlib.sha256(manifest).hexdigest()=='164eb23618f9ebe9938d845f0705c6f73a96d28375a9eb7cdba5152a1adeffca', 'immutable manifest pin')
pins=json.loads(manifest)
for name,pin in pins.items():
    raw=(ROOT/'sources'/(name+'.txt')).read_bytes()
    need(hashlib.sha256(raw).hexdigest()==pin['sha256'], 'pin '+name)
    need(len(raw)==pin['bytes'],'length '+name)
    need(hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==pin['git_blob'],'Git blob '+name)
need(pins['program.py']['git_blob']=='745beade7f111b4648d5da36a962c787f1a29d72','remote immutable program blob')
need(pins['pinned-program.py']==pins['program.py'],'frozen snapshot equals remote')
need(pins['outer_partition_source_binding.py']['sha256']=='e99e4a8c8a3736a7ef583d66f8de21680fae7dca5fe253bff7483426c513fa00','TR formula source pin')
need(pins['regular-cover-transport.md']['sha256']=='98a10d3da934ef5b6dfe1e2cf6af4ac46fcf6347e0e6081a8c0cbd58b2f7f02d','TR theorem source pin')
def tree(name): return ast.parse((ROOT/'sources'/(name+'.txt')).read_text())
P=tree('program.py'); functions={x.name:x for x in P.body if isinstance(x,ast.FunctionDef)}
def canon(x):return ast.dump(x,include_attributes=False)
checks=[]
def contains(fn,s):
    node=ast.parse(s).body[0]
    if isinstance(node,ast.Expr): node=node.value
    need(any(canon(x)==canon(node) for x in ast.walk(functions[fn])),fn+': '+s)
    checks.append(fn+': '+s)
for fn,s in [
 ('binomial','out=out*(n-j+1)//j'),
 ('binomial','range(1,min(k,n-k)+1)'),
 ('compositions','range(n+1)'),
 ('compositions','compositions(n-a,k-1)'),
 ('first_hit','compositions(L,len(vs))'),
 ('first_hit','ns[j]<T or any(ns[i]>=T for i in range(j))'),
 ('first_hit','co*=binomial(left,n)'),
 ('first_hit','left-=n'),
 ('first_hit','term=term*power(cs[i],n)*power(vs[i],n-(T if i==j else 0))'),
 ('first_hit','out=out+ex.scalar(co)*term'),
 ('outer_weight','bits=[(owner.standard_tag>>(3-i))&1 for i in range(4)]'),
 ('outer_weight','z=[x[i].inverse() if bits[i] else x[i] for i in range(4)]'),
 ('outer_weight','(i in A and not bits[i]) or(i not in A and bits[i])'),
 ('outer_weight','h=[power(a,5)-prod for a in v]'),
 ('outer_weight','aux=v[0]*v[1]*v[3]*v[4]'),
 ('outer_weight','compositions(k,len(finite)) if finite else ([()]if k==0 else [])'),
 ('outer_weight','M=2*N-1'),('outer_weight','T=5*M'),('outer_weight','L=(s+1)*(T-1)+1'),
 ('outer_weight','cs=[ex.scalar((-1)**(s-j))*H[s-j]for j in range(s+1)]'),
 ('outer_weight','range(s+1)if b==5 else [b]if b<=s else []'),
 ('outer_weight','B=first_hit(ex,cs,v[:s+1],j,T,L)'),
 ('outer_weight','range(N)if b==5 else range(N,M+1)'),
 ('outer_weight','term=term*power(h[j],k if b==5 else k-N)*power(v[2],M-k)*power(aux,M-k-N if b==5 else M-k)'),
 ('outer_weight','root=root+B*split'),
 ('outer_weight','root=root*power(aux if b==5 else h[b],N)'),
 ('outer_weight','ml=2*n-1'),('outer_weight','mask=(owner.legal_mask>>i)&1'),
 ('outer_weight','range(n)if mask else range(n,ml+1)'),
 ('outer_weight','line=line+ex.scalar(binomial(ml,k))*power(t,2*k if mask else 2*k-n)*power(ex.scalar(1)-t*t,ml-k-n if mask else ml-k)'),
 ('outer_weight','ell=ex.scalar(1)-t*t if mask else t'),
 ('outer_weight','root=root*power(ell,n)*line'),
 ('potential_owners','carriers=[4,5]if s==4 else list(range(s+1))+[5]'),
 ('potential_owners','any(((m>>i)&1)and not bits[i]for i in range(4))'),
 ('potential_owners','I.FullOwner(30,occurrence,c,m,tag)'),
 ('weighted_assignment','canonical,parity=I.sorted_source(owners)'),
 ('weighted_assignment','source,blocks=source_and_lift(model,canonical,2)'),
 ('weighted_assignment','scalar=X13[5][0]+X02[1][3]+X02[4][2]'),
 ('weighted_assignment','weighted=scalar*ex.scalar(parity)'),
 ('weighted_assignment','for owner in owners:weighted=weighted*outer_weight(ex,owner)'),
 ('_actual_body',"fibers=[tuple(potential_owners(t,('outer',si,j)))for j,t in enumerate(stair['standard_tags'])]"),
 ('_actual_body',"total=total+weighted_assignment(ex,model_data,owners)*ex.scalar(stair['orientation'])"),
 ('_actual_body','stripped=dict(total.terms).get(15,ex.rational(0))'),
 ('_actual_body','return stripped.laurent_coefficient(EXPONENT)'),
]:contains(fn,s)
need([x.value for x in functions['outer_weight'].args.defaults]==[54,29],'fixed powers')
body=functions['_actual_body'].body
need(isinstance(body[-3],ast.For) and isinstance(body[-2],ast.Assign) and isinstance(body[-1],ast.Return),'mask extraction outside all sums')
need(not any(isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute) and n.func.attr=='laurent_coefficient' for n in ast.walk(body[-3])),'no per-term coefficient extraction')
# Independent finite-index checks, no owners or geometric variables instantiated.
for N in [1,2,54]:
    M=2*N-1
    low=list(range(N));high=list(range(N,M+1))
    need(low+high==list(range(M+1)),'split exhaustive and disjoint')
    need(all(M-k-N>=0 for k in low),'auxiliary exponent')
    need(all(k-N>=0 and M-k>=0 for k in high),'primary exponents')
for n in [1,2,29]:
    m=2*n-1
    need(all(m-k-n>=0 for k in range(n)),'mask1 exponent')
    need(all(2*k-n>=0 and m-k>=0 for k in range(n,m+1)),'mask0 exponents')
# Tiny invented first-hit monomials in two independent formal letters g,h.
# Dictionary keys are exponent pairs, not physical polynomial/owner products.
E=[{},{}]
for a in range(4):
    ns=(a,3-a);eligible=[i for i,v in enumerate(ns) if v>=2]
    need(bool(eligible),'pigeonhole')
    j=min(eligible);left=3;co=1
    for v in ns: co*=math.comb(left,v);left-=v
    E[j][ns]=co
need(E[0]=={(2,1):3,(3,0):1} and E[1]=={(0,3):1,(1,2):3},'tiny first-hit split')
need({**E[0],**E[1]}=={(a,3-a):math.comb(3,a) for a in range(4)},'tiny binomial identity')
# Independent universal-form exponent recombination at tiny and fixed powers.
for N in [1,2,54]:
    M=2*N-1
    for k in range(M+1):
        quotient=(k-N,M-k,M-k) if k>=N else (k,M-k,M-k-N)
        restored=tuple(v+(N if i==(0 if k>=N else 2) else 0) for i,v in enumerate(quotient))
        need(restored==(k,M-k,M-k),'Cbar/Dbar restoration')
# Semantic AST negative controls. These mutate only an in-memory source string.
source=(ROOT/'sources/program.py.txt').read_text()
mutations=[('range(N,M+1)','range(N,M)'),('range(N)if b==5','range(N+1)if b==5'),('M-k-N if b==5','M-k if b==5'),('2*k-n','2*k'),('ml-k-n if mask','ml-k if mask'),('for owner in owners:weighted','for owner in canonical:weighted'),('get(15,','get(7,'),('ns[j]<T','ns[j]<=T')]
for old,new in mutations:
    need(old in source,'mutation present')
    altered=ast.parse(source.replace(old,new,1))
    need(canon(altered)!=canon(P),'mutation changes AST')
    af={x.name:x for x in altered.body if isinstance(x,ast.FunctionDef)}
    need(any(not any(canon(n)==canon((lambda t:t.value if isinstance(t,ast.Expr) else t)(ast.parse(s.split(': ',1)[1]).body[0])) for n in ast.walk(af[s.split(': ',1)[0]])) for s in checks),'mutation rejected by expected fragment')

# Pin failures remain active under optimization, including jointly altered metadata.
for name,pin in pins.items():
    raw=(ROOT/'sources'/(name+'.txt')).read_bytes()
    need(hashlib.sha256(raw+b'\n').hexdigest()!=pin['sha256'],'negative source pin')
changed=dict(pins);changed['program.py']=dict(changed['program.py'],sha256='0'*64)
need(hashlib.sha256(json.dumps(changed,indent=2,sort_keys=True).encode()).hexdigest()!=hashlib.sha256(manifest).hexdigest(),'negative manifest pin')
I=tree('interfaces.py'); C=tree('compiler.py')
def has(t,s):
    n=ast.parse(s).body[0]; n=n.value if isinstance(n,ast.Expr) else n
    return any(canon(x)==canon(n) for x in ast.walk(t))
for t,s in [(I,'return (-1 if self.carrier==5 else self.carrier,self.legal_mask,self.standard_tag)'),(I,'p=sorted(range(len(owners)),key=lambda j:owners[j].source_key)'),(I,'sign=(-1)**sum(p[i]>p[j]for i in range(len(p))for j in range(i+1,len(p)))'),(C,'for d in perm:tag|=1<<(3-d);tags.append(tag)'),(C,'sign=(-1)**sum(perm[i]>perm[j]for i in range(4)for j in range(i+1,4))')]:
    need(has(t,s),'ordering/staircase AST')
# Only 24 coordinate permutations and five integer tags; no owner alphabet enumeration.
import itertools
seen=set();signs=[]
for perm in itertools.permutations(range(4)):
    tags=[0]
    for d in perm:tags.append(tags[-1]|(1<<(3-d)))
    need(len(set(tags))==5 and tags==sorted(tags) and tags[-1]==15,'distinct increasing tags')
    need([t.bit_count() for t in tags]==list(range(5)),'rank profile')
    seen.add(tuple(tags));signs.append((-1)**sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4)))
need(len(seen)==24 and sum(signs)==0,'24 signed staircases')
counts=[(2 if s==4 else s+2)*2**s for s in range(5)]
need(counts==[2,6,16,40,32] and math.prod(counts)==245760 and 24*math.prod(counts)==5898240,'formal alphabet counts')
# Toy chart/mask convention distinction, without instantiating a physical owner.
need([(8>>(3-i))&1 for i in range(4)]==[1,0,0,0],'standard big-endian')
need([(1>>i)&1 for i in range(4)]==[1,0,0,0],'mask little-endian')

result={'status':'PASS','static_formula_checks':len(checks),'negative_controls':len(mutations),'negative_pin_controls':len(pins)+1,'formal_staircases':24,'physical_execution':False,'owner_enumeration':False,'actual_pole_bounds_proved':False,'scope':'static wiring and finite-index algebra; read PROOF.md for universal identities and geometric premises'}
print(json.dumps(result,indent=2))
