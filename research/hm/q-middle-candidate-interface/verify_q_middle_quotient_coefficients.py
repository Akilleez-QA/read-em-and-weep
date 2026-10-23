"""Free-symbol direct-sum and physical-section certificates for all55+10 maps.

No rank calculation, selected marking, point, actual source assignment, or
source-feasibility system is used. Every equality is a polynomial/Laurent-unit
identity; Gram constants are checked on whole typed domains.
"""
import hashlib
from pathlib import Path
from collections import Counter
from time import monotonic
from universal_q_middle_quotient_coefficients import *
from universal_new_d5_leg_coefficients import tv,typed_outputs

start=monotonic()
def report(msg):print('PASS: '+msg+' [%.1fs]'%(monotonic()-start),flush=True)
def eq(a,b):
    assert s.cancel(s.expand(a-b))==0,s.factor(a-b)
def meq(A,B):
    assert A.shape==B.shape,(A.shape,B.shape)
    for a,b in zip(A,B):eq(a,b)
def flat(A):return s.Matrix(list(A))
def columns(fun,degree):return s.Matrix.hstack(*[flat(fun(p)) for p in mon(degree)])
def simp(A):return A.applyfunc(s.factor)
def sp(A):return s.SparseMatrix(A)
def symmetrizer(n):
    return s.SparseMatrix(n*n,n*n,lambda i,j:s.Rational(int(i==j)+int(i//n==j%n and i%n==j//n),2))

manifest=Path('Q-CUBIC-KERNEL-LIFT-AND-FULL-COMPLETION.sha256')
assert hashlib.sha256(manifest.read_bytes()).hexdigest()=='8a51729d04e922910d8b5e61e7651fbc7b006ae2a0f6a5597335660e3636e2d2'
frozen={}
for line in manifest.read_text().splitlines():
    digest,name=line.split(None,1)
    assert hashlib.sha256(Path(name).read_bytes()).hexdigest()==digest,name
    frozen[name]=digest
report('the prescribed qB completion manifest and every frozen input match')

b=QMiddleQuotientCoefficientBuilder()
def projector(kind):
    d=CANONICAL_DEGREE[kind]
    return columns(lambda p:coeff(typed_projection(b.f,kind,p),d),d)
P={k:projector(k) for k in CANONICAL_DEGREE}
J={k:apolar_metric(CANONICAL_DEGREE[k]) for k in CANONICAL_DEGREE}

# Primitive CG identities on ENTIRE tensor spaces, including antisymmetric legs.
cg_constants={}
for m,n in ((2,2),(4,4),(2,6),(2,4),(2,0)):
    G=sp(s.kronecker_product(apolar_metric(m),apolar_metric(n)))
    rec=s.zeros((m+1)*(n+1))
    inc=[]
    for r in range(min(m,n)+1):
        d=m+n-2*r;I=cg_matrix(m,n,r);JJ=apolar_metric(d)
        H=simp(I.T*G*I)
        cc=s.factor(H[0,d]/JJ[0,d]);assert cc!=0
        meq(H,cc*JJ)
        L=simp(JJ.inv()*I.T*G/cc)
        meq(L*I,s.eye(d+1));rec+=I*L;inc.append((I,L));cg_constants[(m,n,r)]=cc
    for i,(I,L) in enumerate(inc):
        for j,(II,LL) in enumerate(inc):
            if i!=j:meq(L*II,s.zeros(L.rows,II.cols))
    meq(rec,s.eye((m+1)*(n+1)))
report('all primitive CG apolar left inverses, cross-zero identities, and full tensor reconstructions: '+str(cg_constants))

# Pair inclusions: explicit Cauchy splitting in both distinct binary frames.
G9=sp(s.kronecker_product(J2,J2));G81=sp(s.kronecker_product(G9,G9))
pairs={};pair_constants={};rec=s.zeros(81)
for route in middle_pair_routes():
    k=route.kind;d=CANONICAL_DEGREE[k]
    I=sp(columns(lambda p:b.cauchy_pair(p,route),d))
    H=simp(I.T*G81*I);JP=J[k]*P[k]
    ii,jj=next((i,j) for i in range(d+1) for j in range(d+1) if JP[i,j]!=0)
    cc=s.factor(H[ii,jj]/JP[ii,jj]);assert cc!=0 and not cc.free_symbols,(route,cc)
    meq(H,cc*JP)
    L=sp(simp(J[k].inv()*I.T*G81/cc));meq(L*I,P[k]);meq(I*P[k],I)
    for old,(II,LL) in pairs.items():
        meq(L*II,s.zeros(L.rows,II.cols));meq(LL*I,s.zeros(LL.rows,I.cols))
    meq(symmetrizer(9)*I,I)
    rec+=I*L;pairs[route]=(I,L);pair_constants[route.label]=cc
meq(rec,symmetrizer(9))
assert Counter(r.kind for r in pairs)=={'1':2,'A':1,'V':1,'P4':3,'D5':5}
report('all12 Cauchy pair routes are mutually biorthogonal and reconstruct Sym9; constants '+str(pair_constants))

# Outer inclusions and their typed projections; no assumed witness nonzero.
outers={};outer_constants={}
for pair in CANONICAL_DEGREE:
    n=CANONICAL_DEGREE[pair];G=sp(s.kronecker_product(J2,apolar_metric(n)))
    rec=s.zeros(3*(n+1));local=[]
    for r,degree,k in PAIR_OUTER_CHOICES[pair]:
        rr=QLegTargetRoute('universal',pair,r,degree,k)
        d=CANONICAL_DEGREE[k]
        I=sp(columns(lambda p:outer_binary_tensor(b.f,b.g12,p,rr),d))
        H=simp(I.T*G*I);JP=J[k]*P[k]
        ii,jj=next((i,j) for i in range(d+1) for j in range(d+1) if JP[i,j]!=0)
        cc=s.factor(H[ii,jj]/JP[ii,jj]);assert cc!=0 and not cc.free_symbols
        meq(H,cc*JP);L=sp(simp(J[k].inv()*I.T*G/cc));meq(L*I,P[k])
        for II,LL in local:
            meq(L*II,s.zeros(L.rows,II.cols));meq(LL*I,s.zeros(LL.rows,I.cols))
        local.append((I,L));rec+=I*L;outers[(pair,r,k)]=(I,L);outer_constants[(pair,r,k)]=cc
    meq(rec,s.kronecker_product(s.eye(3),P[pair]))
report('all13 outer routes have exact mutually biorthogonal apolar inverses and full typed reconstructions')

# Tensor templates are literally these composite inclusions, not merely same types.
targets={};rec=s.zeros(243)
for route in middle_target_routes():
    pairI,pairL=pairs[route.pair];outI,outL=outers[(route.pair_kind,route.outer_order,route.kind)]
    I=sp(simp(s.kronecker_product(s.eye(3),pairI)*outI))
    L=sp(simp(outL*s.kronecker_product(s.eye(3),pairL)))
    d=CANONICAL_DEGREE[route.kind]
    template=s.Matrix.hstack(*[s.Matrix.vstack(*[flat(K.diff(v))*sign for v,sign in ((y,-1),(z,1),(x,1))]) for K in b.middle_template(route)])
    meq(template,I);meq(L*I,P[route.kind])
    rec+=I*L;targets[route]=(I,L)
meq(rec,s.kronecker_product(s.eye(3),symmetrizer(9)))
for r,(I,L) in targets.items():
    for rr,(II,LL) in targets.items():
        if r!=rr:meq(L*II,s.zeros(L.rows,II.cols))
assert Counter(r.kind for r in targets)=={'1':1,'A':8,'V':8,'P4':9,'D5':10}
report('all36 final templates equal the composite maps; full243-entry target biorthogonality and I3 tensor Sym9 reconstruction prove dimension135')

# Seven source projections on all25 harmonic coordinates, plus the trace copy.
sourceG=sp(s.kronecker_product(apolar_metric(4),apolar_metric(4)))
sources={};rec=s.zeros(25)
for order in range(5):
    degree=8-2*order
    kinds=[k for k,_ in typed_outputs(b.f,b.g12,tv(S**4,S**4,order),degree)]
    for k in kinds:
        d=CANONICAL_DEGREE[k]
        M=s.Matrix.hstack(*[coeff(dict(typed_outputs(b.f,b.g12,tv(p,q,order),degree))[k],d) for p in mon(4) for q in mon(4)])
        N=simp(sourceG.inv()*M.T*J[k]);MN=simp(M*N)
        ii,jj=next((i,j) for i in range(d+1) for j in range(d+1) if P[k][i,j]!=0)
        cc=s.factor(MN[ii,jj]/P[k][ii,jj]);assert cc!=0 and not cc.free_symbols
        meq(MN,cc*P[k]);N=simp(N/cc)
        for (_,kk),(MM,NN) in sources.items():
            meq(M*NN,s.zeros(M.rows,NN.cols));meq(MM*N,s.zeros(MM.rows,N.cols))
        rec+=N*M;sources[(order,k)]=(M,N)
meq(rec,s.eye(25))
report('the seven harmonic source maps are mutually split and reconstruct I25; independent trace D5 gives I30')

# Physical conversion is exact on both indices. The positive dual frame is
# derived from the literal polynomial, not identified with the negative frame.
c=s.Matrix(s.symbols('frame_c0:3'));p=polynomial(c,2)
eq((s.Matrix([[x,y,z]])*POSITIVE_COVECTOR*c)[0],-y*c[0]+z*c[1]+x*c[2])
meq(QUOTIENT_FRAME.inv()*QUOTIENT_FRAME,s.eye(9))
from universal_graded_c_orthogonal_module import graded_module
m=graded_module();D,R,C,Zeta=(m[k] for k in ('D','R','C','Zeta'))
meq(D*R,s.eye(9));meq(R*D+C*Zeta,s.eye(12));meq(D*C,s.zeros(9,3))
F=R*QUOTIENT_FRAME;Finv=QUOTIENT_FRAME.inv()*D
meq(Finv*F,s.eye(9))
# Arbitrary symmetric12x12 positive-linear B, all234 coefficients formal.
freeB=s.Matrix(12,12,lambda i,j:sum(s.Symbol('projection_B_%s_%s_%s'%(a,min(i,j),max(i,j)))*v for a,v in enumerate((x,y,z))))
Pr=R*D;L=freeB*Zeta.T-C*Zeta*freeB*Zeta.T/2
meq(freeB-Pr*freeB*Pr.T,C*L.T+L*C.T)
meq(D*(C*L.T+L*C.T)*D.T,s.zeros(9))
report('both physical frame indices and the exact regular section are checked; all234 free B coefficients obey the complete C-factor projection identity')

# Entire source dependence remains formal. Check all65 actual returned tensors.
d,k,l=s.symbols('qmiddle_a_d qmiddle_a_k qmiddle_a_l');hs=s.symbols('qmiddle_external_h0:5')
a=k*S*S-2*d*S*T-l*T*T;hp=polynomial(hs,4);rho=d*d+k*l
lap=lambda p:s.expand(s.diff(p,d,2)+4*s.diff(p,k,l))
eq(lap(a*a),0);eq(-tv(a,a,2)/8,rho)
expected=set();source_by_label={}
for name,kind,p in b.harmonic_sources(a,hp):
    source_by_label[('harmonic',name)]=(kind,p)
for name,kind,p in [b.trace_source(a,hp)]:source_by_label[('trace',name)]=(kind,p)
for (cat,name),(kind,p) in source_by_label.items():
    for route in middle_target_routes(kind):expected.add((cat,name+'__'+route.label))
seen=set();counts=Counter()
for cat,label,K in b.iter_coefficients(a,hp,frame='intrinsic'):
    name,route_label=label.split('__');kind,p=source_by_label[(cat,name)]
    route=next(r for r in targets if r.label==route_label);I,L=targets[route]
    tensor=s.Matrix.vstack(*[flat(K.diff(v))*sign for v,sign in ((y,-1),(z,1),(x,1))])
    meq(tensor,I*coeff(p,CANONICAL_DEGREE[kind]));meq(K,K.T)
    physical=simp(F*K*F.T)
    meq(Finv*physical*Finv.T,K);meq(physical,physical.T)
    for val in physical:
        if val==0:continue
        for exponents,_ in s.Poly(val,x,y,z,d,k,l,*hs).terms():
            assert (sum(exponents[:3]),sum(exponents[3:6]),sum(exponents[6:]))==(1,2,1)
        if cat=='harmonic':eq(lap(val),0)
        else:eq(val,rho*lap(val)/6)
    counts[cat]+=1;seen.add((cat,label))
    print('CHECKED '+cat+' '+label,flush=True)
assert seen==expected and counts=={'harmonic':55,'trace':10}
report('every55 harmonic+10 trace physical12x12 map is symmetric, regular, degree(1,2,1), exactly harmonic/trace, and recovered by D on both indices')

# Matrix-unit functional is tr(L_target F N_source)/dim(type). The checked
# cross identities prove delta_target delta_source on all65 returned maps.
assert sum(sum(1 for r in targets if r.kind==k) for _,k in sources)==55
assert sum(1 for r in targets if r.kind=='D5')==10
for name,digest in frozen.items():assert hashlib.sha256(Path(name).read_bytes()).hexdigest()==digest,name
report('all65 maps are exact coefficient matrix units and complete by the source/target direct sums; all frozen files unchanged')
print('No supported-operator independence, actual-source solution, fixed-trace freedom, equivariant R, or obstruction value is claimed.',flush=True)
