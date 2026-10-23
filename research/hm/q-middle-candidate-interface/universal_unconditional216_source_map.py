"""Sparse LINEAR full-source reconstruction, with every off-image error retained.

No solve, rank, point test, coefficient specialization, old140 restriction, or
coordinate division occurs. Dictionary coefficients are exact QQ Laurent data.
Public outputs use the fixed17-variable order; S,T are internal only.
"""
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
import hashlib,pickle,json,time
import sympy as s
from universal_laurent_lex_module import sparse_laurent,sparse_expression
from universal_sparse_positive_cubic_fischer import positive_cubic_fischer
ROOT=Path(__file__).resolve().parent
NAMES=('x','y','z','u','w','ha','hb','hc','hd','hf','h','k','l','FB','FC','FD','theta','S','T')
N=len(NAMES); ZERO=(0,)*N

def add(*ps):
    d={}
    for p in ps:
        for m,c in p.items():
            v=d.get(m,0)+c
            if v:d[m]=v
            elif m in d:del d[m]
    return d

def scale(c,p):return {m:c*v for m,v in p.items() if c*v}
def mul(p,q):
    if not p or not q:return {}
    d={}
    for m,c in p.items():
        for n,e in q.items():
            k=tuple(a+b for a,b in zip(m,n));v=d.get(k,0)+c*e
            if v:d[k]=v
            elif k in d:del d[k]
    return d

def const(c):return {ZERO:s.Rational(c)} if c else {}
def var(i):
    m=list(ZERO);m[i]=1;return {tuple(m):s.S.One}
def power(p,n):
    out=const(1)
    for _ in range(n):out=mul(out,p)
    return out

def deriv(p,i,n=1):
    for _ in range(n):
        d={}
        for m,c in p.items():
            if m[i]:
                k=list(m);k[i]-=1;d[tuple(k)]=c*m[i]
        p=d
    return p

def coeff(p,i,n=1):
    d={}
    for m,c in p.items():
        if m[i]==n:
            k=list(m);k[i]=0;d[tuple(k)]=c
    return d

def binary_coeff(p,degree):
    out=[]
    for j in range(degree+1):
        out.append(coeff(coeff(p,17,degree-j),18,j))
    assert p==add(*(mul(out[j],mul(power(var(17),degree-j),power(var(18),j))) for j in range(degree+1)))
    return out

def diagonal(p):
    d={}
    for m,c in p.items():
        n=list(m);n[3]+=n[17];n[4]+=n[18];n[17]=n[18]=0;n=tuple(n)
        d[n]=d.get(n,0)+c
    return {m:c for m,c in d.items() if c}
def delta(p):return add(mul(var(17),deriv(p,3)),mul(var(18),deriv(p,4)))
def epsilon(p):return add(mul(var(3),deriv(p,17)),mul(var(4),deriv(p,18)))
def omega(p):return add(deriv(deriv(p,3),18),scale(-1,deriv(deriv(p,4),17)))
def ell_split(p,m):
    n=m+3;el=add(mul(var(3),var(18)),scale(-1,mul(var(4),var(17))))
    polar=scale(s.Rational(1,n*(n-1)*(n-2)),delta(delta(delta(diagonal(p)))))
    w1=omega(p);w2=omega(w1);w3=omega(w2)
    q=add(scale(s.Rational(1,n),w1),scale(-s.Rational(1,2*n*(n-1)),mul(el,w2)),scale(s.Rational(1,6*n*(n-1)*(n-2)),mul(power(el,2),w3)))
    assert add(p,scale(-1,mul(el,q)),scale(-1,polar))=={}
    return q,polar

def lap(p):return mul(var(16),add(scale(4,deriv(deriv(p,0),1)),deriv(p,2,2)))
def lapD(p):return add(deriv(p,10,2),scale(4,deriv(deriv(p,11),12)))
def projectD(p):return add(p,scale(-s.Rational(1,6),mul(add(power(var(10),2),mul(var(11),var(12))),lapD(p))))
def zeros(r,c):return [[{} for _ in range(c)] for _ in range(r)]
def eye(n):return [[const(i==j) for j in range(n)] for i in range(n)]
def matadd(*As):return [[add(*(A[i][j] for A in As)) for j in range(len(As[0][0]))] for i in range(len(As[0]))]
def matscale(c,A):return [[scale(c,e) for e in row] for row in A]
def matpoly(p,A):return [[mul(p,e) for e in row] for row in A]
def matmul(A,B):return [[add(*(mul(a,b) for a,b in zip(row,col))) for col in zip(*B)] for row in A]
def trans(A):return [list(col) for col in zip(*A)]
def col(A,j):return [[row[j]] for row in A]
def columns(cs):return [list(row) for row in zip(*(tuple(r[0] for r in c) for c in cs))]
def matdiff(A,i):return [[deriv(e,i) for e in row] for row in A]
def matfun(A,f):return [[f(e) for e in row] for row in A]
def flat(A):return [e for row in A for e in row]
def matzero(A):return not any(flat(A))
def fadd(*fs):
    out={}
    for f in fs:
        for I,p in f.items():
            q=add(out.get(I,{}),p)
            if q:out[I]=q
            elif I in out:del out[I]
    return out

def fscale(c,f):return {I:scale(c,p) for I,p in f.items() if c and p}
def fmul(p,f):return {I:q for I,c in f.items() if (q:=mul(p,c))}
def wedge(f,g):
    out={}
    for I,a in f.items():
        for J,b in g.items():
            if set(I)&set(J):continue
            K=tuple(sorted(I+J));c=scale((-1)**sum(i>j for i in I for j in J),mul(a,b))
            out=fadd(out,{K:c})
    return out

def contract(f):
    out={}
    for I,a in f.items():
        for j,i in enumerate(I):out=fadd(out,{I[:j]+I[j+1:]:scale((-1)**j,mul(var(i),a))})
    return out

def vadd(*fs):return [fadd(*(f[j] for f in fs)) for j in range(2)]
def vscale(c,f):return [fscale(c,q) for q in f]
def vmul(p,f):return [fmul(p,q) for q in f]
def vdiff(f,i):return [{I:deriv(p,i) for I,p in q.items() if deriv(p,i)} for q in f]
def vcontract(f):return [contract(q) for q in f]
def vzero(f):return not any(f)
def getp(F,extra=()):
    return [[scale(sign,F[j].get(tuple(sorted(I+extra)),{}))] for I,sign in [((1,2),1),((0,2),-1),((0,1),1)] for j in range(2)]
def putp(p,extra=()):
    return [{tuple(sorted(I+extra)):scale(sign,p[2*i+j][0]) for i,(I,sign) in enumerate([((1,2),1),((0,2),-1),((0,1),1)]) if p[2*i+j][0]} for j in range(2)]
def getY(F,extra):return [[F[j].get((i,)+extra,{})] for i in range(3) for j in range(2)]
def putY(Y,extra):return [{(i,)+extra:Y[2*i+j][0] for i in range(3) if Y[2*i+j][0]} for j in range(2)]
def binary_row(A):return [[add(*(mul(A[j][i],mul(power(var(17),3-j),power(var(18),j))) for j in range(4))) for i in range(len(A[0]))]]

def public(poly):
    assert all(not m[17] and not m[18] for m in poly)
    return {m[:17]:c for m,c in poly.items()}
def pack_matrix(A):return {'kind':'matrix','shape':[len(A),len(A[0])],'entries':{(i,j):public(e) for i,row in enumerate(A) for j,e in enumerate(row) if e}}
def pack_forms(F):return {'kind':'spinor_form','entries':{(j,I):public(e) for j,f in enumerate(F) for I,e in f.items() if e}}

class SourceMap:
    def __init__(self):
        ns={'__file__':str(ROOT/'derive_c_only140_unfiltered_principal_quotient.py')}
        with redirect_stdout(StringIO()):exec((ROOT/'derive_c_only140_unfiltered_principal_quotient.py').read_text().split("rq_symbols,rh_symbols,Theta=ns['build_symbols']")[0],ns)
        self.ns=ns;self.variables=[ns[name] for name in NAMES]
        self.units=self.variables[13:17]
        self.load=lambda e:sparse_laurent(e,self.variables,self.units)
        self.lmat=lambda A:[[self.load(A[i,j]) for j in range(A.cols)] for i in range(A.rows)]
        self.lforms=lambda F:[{I:self.load(e) for I,e in ff.items() if e!=0} for ff in F]
        for name in ('cliff','spin','Kinc','extract','fmat','finv','up','low','J6','M','M2','J','B6','B6inv'):
            setattr(self,name,self.lmat(ns[name]))
        self.J6inv=self.lmat(ns['J6'].inv());self.Jinv=self.lmat(ns['J'].inv())
        self.As=[self.lforms(ns['A'](s.eye(2)[:,i])) for i in range(2)]
        self.Bs=[self.lforms(ns['B'](s.eye(2)[:,i])) for i in range(2)]
        Cp3=ns['Kinc']*ns['fmat']*s.Matrix([[0,0,0],[-1,0,0],[0,-1,0],[0,0,-1]])
        Cp4=ns['Kinc']*ns['fmat']*s.Matrix([[1,0,0],[0,1,0],[0,0,1],[0,0,0]])
        self.Cp3=self.lmat(Cp3);self.Cp4=self.lmat(Cp4)
        self.Cs=[vcontract(vadd(putp(col(self.Cp3,i),(3,)),putp(col(self.Cp4,i),(4,)))) for i in range(3)]
        self.pC=matadd(matpoly(var(3),self.Cp3),matpoly(var(4),self.Cp4))
        aa=s.Matrix.hstack(*[ns['getp'](ns['A'](ns['p'])).diff(v).diff(pp) for v in [ns['x'],ns['y'],ns['z']] for pp in ns['p']])
        self.AAinv=self.lmat(aa.inv())
        self.ellmat=self.lmat(s.Matrix([[-ns['w'],0,0],[ns['u'],-ns['w'],0],[0,ns['u'],-ns['w']],[0,0,ns['u']]]))
        self.cv=columns([getY(vcontract(putp(col(eye(6),i))),()) for i in range(6)])
        self.YL=self.lmat(s.Matrix.vstack(ns['M0'],ns['M1'],ns['M2']))
        self.q=self.load((ns['x']*ns['y']+ns['z']**2)/ns['theta'])
        self.j={(3,):scale(-1,var(4)),(4,):var(3)}
        hp=s.expand((s.Matrix(1,5,ns['coords'])*ns['rh'])[0]);dd=s.Matrix([[ns['h'],ns['k']],[ns['l'],-ns['h']]])
        cpp=[Cp3,Cp4]
        target=[(ns['abase']*hp*sum((dd[j,i]*cpp[i] for i in range(2)),s.zeros(6,3))).applyfunc(s.expand) for j in range(2)]
        tp=[matfun(self.lmat(A),projectD) for A in target]
        self.targets=[vcontract(vadd(putp(col(tp[0],i),(3,)),putp(col(tp[1],i),(4,)))) for i in range(3)]
        assert all(not lapD(p) for F in self.targets for f in F for p in f.values())
    def adj6(self,K):return matmul(matmul(self.J6inv,trans(K)),self.J6)
    def combine(self,Fs,v):return vadd(*(vmul(v[i][0],F) for i,F in enumerate(Fs)))
    def A(self,v):return self.combine(self.As,v)
    def B(self,v):return self.combine(self.Bs,v)
    def C(self,v):return self.combine(self.Cs,v)
    def fullE(self,K,F):
        adj=matmul(matmul(self.up,self.adj6(K)),self.low)
        return vadd(putp(matmul(K,getp(F))),*(putY(matscale(-1,matmul(adj,getY(F,(i,)))),(i,)) for i in (3,4)))
    def fullT(self,K,F):
        return vadd(*[vcontract([wedge({(i,):const(1)},ff) for ff in self.fullE(matscale(s.Rational(1,4),matdiff(K,i)),F)]) for i in (3,4)])
    def apply(self,M,F):
        yy=getY(F,(3,))+getY(F,(4,));out=matmul(M,yy)
        return vcontract(vadd(putp(out[:6],(3,)),putp(out[6:],(4,))))
    def source_map(self,M=None,affine=False):
        t=time.time()
        if not affine:assert all(vzero(self.apply(M,F)) for F in self.As)
        rawB=[[{},{}] for _ in range(2)] if affine else [self.apply(M,F) for F in self.Bs]
        rawC=[[{},{}] for _ in range(3)] if affine else [self.apply(M,F) for F in self.Cs]
        errors={};candidates={};checks={};scaled_residual={}
        def scaled(terms):
            out={}
            for powers,F in terms:out[powers]=vadd(out.get(powers,[{},{}]),F)
            return {m:F for m,F in out.items() if not vzero(F)}
        def pack_scaled(record):return {'scale_variables':['kAt','am','bm','cm'],'entries':{m:pack_forms(F) for m,F in record.items()}}
        def em(name,A):errors[name]=pack_matrix(A)
        def ef(name,F):errors[name]=pack_forms(F)
        def cm(name,A):candidates[name]=pack_matrix(A)
        def cf(name,F):candidates[name]=pack_forms(F)
        Y=columns([getp(F) for F in rawB]);Ys=matmul(self.cliff,Y)
        P=[[scale(s.Rational(1,2),coeff(Ys[1][0],1)),scale(s.Rational(1,2),coeff(Ys[0][1],2))],
           [scale(-s.Rational(1,2),coeff(Ys[1][0],2)),scale(s.Rational(1,2),coeff(Ys[0][1],0))]]
        Ycoef=columns([matfun(col(Y,j),lambda e:coeff(e,v)) for v in range(3) for j in range(2)])
        Ymat=matmul(Ycoef,self.AAinv)
        diag=zeros(6,6)
        for r in range(3):
            for i in range(2):
                for j in range(2):diag[2*r+i][2*r+j]=P[i][j]
        K0=matadd(diag,matscale(-1,Ymat))
        Padj=matmul(matmul(self.Jinv,trans(P)),self.J)
        em('principal_spin',matadd(Ys,matscale(-1,matmul(self.M,P)),matscale(-1,matmul(Padj,self.M))))
        Ls=[]
        for j in range(2):
            assert matzero(matadd(getp(rawB[j]),matmul(K0,getp(self.As[j])),matscale(-1,getp(self.A(col(P,j))))))
            ef('K0_Berror_U%d'%j,vadd(self.fullT(K0,self.Bs[j]),vscale(-1,self.B(col(P,j)))))
            D=vadd(rawB[j],self.fullT(K0,self.As[j]),vscale(-1,self.A(col(P,j))))
            assert matzero(getp(D)) and all(all(sum(i<3 for i in I)==1 for I in ff) for ff in D)
            assert vzero(vcontract(D))
            B0=[fadd(*[wedge({(i,):const(1)},fscale(s.Rational(1,3),{I:deriv(p,i) for I,p in ff.items()})) for i in range(3)]) for ff in D]
            L0=matscale(s.Rational(1,4),matadd(matdiff(getp(B0,(4,)),3),matscale(-1,matdiff(getp(B0,(3,)),4))))
            assert vzero(vadd(B0,vscale(-1,vadd(putp(matpoly(scale(-1,var(4)),L0),(3,)),putp(matpoly(var(3),L0),(4,))))))
            Ls.append(L0)
        L0=columns(Ls);T0=matscale(-1,matmul(self.M2,matfun(matmul(self.cliff,L0),lambda e:coeff(e,2))))
        L=matadd(L0,columns([getp(self.A(col(T0,j))) for j in range(2)]));em('cartan_error',matmul(self.cliff,L))
        Lmap=matmul(columns([matfun(col(L,j),lambda e:coeff(e,v)) for v in range(3) for j in range(2)]),self.AAinv)
        Lbin=binary_row(matmul(matmul(self.finv,self.extract),Lmap))[0]
        assert all(m[3]+m[4]==2 and m[17]+m[18]==3 for pp in Lbin for m in pp)
        Qbin=[scale(-4,add(epsilon(e),scale(-s.Rational(1,4),epsilon(epsilon(delta(e)))),scale(s.Rational(1,36),epsilon(epsilon(epsilon(delta(delta(e)))))))) for e in Lbin]
        assert all(add(delta(q),scale(4,Lb))=={} for q,Lb in zip(Qbin,Lbin))
        Qmat=trans([binary_coeff(e,2) for e in Qbin]);Kker=matmul(matmul(matmul(self.Kinc,self.fmat),self.ellmat),Qmat);K=matadd(K0,Kker)
        for j in range(2):
            reverse=matmul(Qmat,getp(self.As[j]));cm('reverse_U%d'%j,reverse)
            ef('Uerror_U%d'%j,vadd(rawB[j],self.fullT(K,self.As[j]),vscale(-1,self.A(col(P,j))),self.C(reverse)))
            ef('Berror_U%d'%j,vadd(self.fullT(K,self.Bs[j]),vscale(-1,self.B(col(P,j)))))
            cf('raw_B_U%d'%j,rawB[j])
            uweight=(1,0,1,0);bweight=(1,-1,2,0)
            literal=scaled([(uweight,rawB[j]),(uweight,self.fullT(K,self.As[j])),(bweight,self.fullT(K,self.Bs[j])),(uweight,vscale(-1,self.A(col(P,j)))),(bweight,vscale(-1,self.B(col(P,j)))),(uweight,self.C(reverse))])
            expected=scaled([(uweight,vadd(rawB[j],self.fullT(K,self.As[j]),vscale(-1,self.A(col(P,j))),self.C(reverse))),(bweight,vadd(self.fullT(K,self.Bs[j]),vscale(-1,self.B(col(P,j)))))])
            assert literal==expected
            scaled_residual['U%d'%j]=pack_scaled(literal)
        Z=matmul(matmul(matmul(matmul(matmul(self.finv,self.extract),K),self.Kinc),self.fmat),self.ellmat)
        zz=binary_row(Z)[0];spl=[ell_split(e,5) for e in zz];Paa=trans([binary_coeff(q,2) for q,polar in spl])
        em('low_polar',trans([binary_coeff(polar,3) for q,polar in spl]))
        Ylow=matadd(matmul(K,self.pC),matscale(-1,matmul(self.pC,Paa)));em('Ylow',Ylow)
        Ku=matdiff(K,3);Kw=matdiff(K,4);C3=matmul(self.cv,self.Cp3);C4=matmul(self.cv,self.Cp4)
        H=matadd(matscale(s.Rational(1,4),matmul(self.up,matadd(matmul(matmul(self.adj6(Ku),self.low),C4),matscale(-1,matmul(matmul(self.adj6(Kw),self.low),C3))))),matscale(s.Rational(1,20),matmul(self.cv,matadd(matmul(Ku,self.Cp4),matscale(-1,matmul(Kw,self.Cp3))))),matscale(s.Rational(1,5),matadd(matmul(C4,matdiff(Paa,3)),matscale(-1,matmul(C3,matdiff(Paa,4))))))
        Pc=matscale(s.Rational(1,3),matmul(matmul(self.cliff,self.low),H));LC=matmul(matmul(self.extract,self.low),H);em('LC',LC)
        assert matzero(matadd(H,matscale(-1,matmul(self.YL,Pc)),matscale(-1,matmul(matmul(self.up,self.Kinc),LC))))
        for j in range(3):
            lhs=vadd(self.fullT(K,self.Cs[j]),vscale(-1,self.C(col(Paa,j))))
            primitive=vadd(putp(matscale(s.Rational(1,5),matdiff(col(Ylow,j),3)),(3,)),putp(matscale(s.Rational(1,5),matdiff(col(Ylow,j),4)),(4,)),putY(col(H,j),(3,4)))
            assert vzero(vadd(lhs,vscale(-1,vcontract(primitive))))
            ef('low_literal_C%d'%j,vadd(lhs,vscale(-1,self.B(col(Pc,j)))))
            R=vadd(rawC[j],vscale(-1,self.A(col(Pc,j))),vscale(-1,self.targets[j]) if affine else [{},{}]);E=getp(R)
            em('high_spin_C%d'%j,matmul(self.cliff,E));Ebin=binary_row(matmul(matmul(self.finv,self.extract),E))[0][0];sigma=diagonal(Ebin)
            rq=scale(s.Rational(1,6),lap(sigma));sigmah=add(sigma,scale(-1,mul(self.q,rq)));assert not lap(sigmah)
            em('sigma_harmonic_C%d'%j,[[sigmah]])
            e0bin=scale(s.Rational(1,120),delta(delta(delta(rq))));E0=matmul(matmul(self.Kinc,self.fmat),[[e] for e in binary_coeff(e0bin,3)])
            p1bin=binary_row(matmul(matmul(self.finv,self.extract),matadd(E,matscale(-1,matpoly(self.q,E0)))))[0][0]
            yy,pol=ell_split(p1bin,3);ycol=[[e] for e in binary_coeff(yy,2)]
            R1=vadd(R,self.C(ycol))
            cweight=(1,0,0,1);lcweight=(1,-1,1,1)
            literal=scaled([(cweight,rawC[j]),(lcweight,self.fullT(K,self.Cs[j])),(cweight,vscale(-1,self.A(col(Pc,j)))),(lcweight,vscale(-1,self.B(col(Pc,j)))),(lcweight,vscale(-1,self.C(col(Paa,j)))),(cweight,self.C(ycol))]+([(cweight,vscale(-1,self.targets[j]))] if affine else []))
            expected=scaled([(cweight,R1),(lcweight,vadd(lhs,vscale(-1,self.B(col(Pc,j)))))])
            assert literal==expected
            scaled_residual['C%d'%j]=pack_scaled(literal)
            V0=vcontract(vadd(putp(matscale(s.Rational(1,3),matdiff(E0,3)),(3,)),putp(matscale(s.Rational(1,3),matdiff(E0,4)),(4,))))
            Hhigh=vadd(R1,vscale(-1,vmul(self.q,V0)))
            Lhigh=matscale(s.Rational(1,3),matadd(matdiff(getY(Hhigh,(4,)),3),matscale(-1,matdiff(getY(Hhigh,(3,)),4))))
            Lform=putY(Lhigh,());Lwedge=[wedge(ff,self.j) for ff in Lform]
            ef('high_full_remainder_C%d'%j,vadd(Hhigh,vscale(-1,Lwedge)))
            expected=matadd(matmul(matmul(self.spin,self.cliff),E),matmul(matmul(self.Kinc,self.fmat),[[e] for e in binary_coeff(scale(s.Rational(1,120),delta(delta(delta(sigmah)))),3)]))
            assert matzero(matadd(getp(Hhigh),matscale(-1,expected)))
            Lquot=matfun(Lhigh,lambda e:scale(s.Rational(1,10),lap(e)));Lharm=matadd(Lhigh,matscale(-1,matpoly(self.q,Lquot)))
            assert all(not lap(e) for e in flat(Lharm))
            for e,eq,eh in zip(flat(Lhigh),flat(Lquot),flat(Lharm)):
                fq,fh=positive_cubic_fischer(public(e),self.variables[:17],*self.variables[:3],self.variables[16])
                assert fq==public(eq) and fh==public(eh)
            em('Lharm_C%d'%j,Lharm)
            Vnorm=vscale(-1,vadd(V0,[wedge(ff,self.j) for ff in putY(Lquot,())]))
            assert vzero(vadd(R1,vmul(self.q,Vnorm),vscale(-1,vadd(Hhigh,vscale(-1,Lwedge))),vscale(-1,[wedge(ff,self.j) for ff in putY(Lharm,())])))
            for name,A in [('Pc',col(Pc,j)),('E0',E0),('y',ycol),('Lhigh',Lhigh),('Lquot',Lquot),('sigma',[[sigma]]),('rq',[[rq]])]:cm(name+'_C%d'%j,A)
            for name,F in [('raw_C',rawC[j]),('R',R),('R1',R1),('V0',V0),('Vnorm',Vnorm)]:cf(name+'_C%d'%j,F)
        for name,A in [('P',P),('K0',K0),('K',K),('Kker',Kker),('Qmat',Qmat),('Paa',Paa),('Pc',Pc),('H',H)]:cm(name,A)
        allp=[p for group in (errors,candidates) for item in group.values() for p in item['entries'].values()]
        for pp in allp:
            assert all(all(m[i]>=0 for i in range(13)) for m in pp)
            lifted={m+(0,0):c for m,c in pp.items()}
            assert not lapD(lifted)
        checks.update(principal_identity_all_U=True,closed_mixed_D_all_U=True,cartan_delta_Q_identity=True,regular_low_split=True,unconditional_low_derivative_identity_all_C=True,unconditional_high_VV_identity_all_C=True,positive_cubic_fischer_all_C=True,literal_high_remainder_reconstruction_all_C=True,whole_external_D_harmonicity_all_outputs=True,ordered_actual_scaled_left_residual_all_five_sources=True)
        den={NAMES[i]:max((max(-m[i],0) for pp in allp for m in pp),default=0) for i in range(13,17)}
        return {'schema':'unconditional216-source-map-v1','variables':list(NAMES[:17]),'errors':errors,'candidates':candidates,'scaled_left_residual':scaled_residual,'checks':checks,'denominator_unit_max_powers':den,'elapsed_seconds':time.time()-t,'scope':'Sufficient joint linear error map only; no converse or source solution asserted.','source_columns':['U0','U1','C0','C1','C2'],'affine_target':affine,'coordinate_divisions':[],'filters':[],'source_solve':'not run','rank_tests':'not run','physical_scales':{'middle':'kAt*(Traw+(bm/am)*T4(K))+T_trace','source':'kAt*[[(bm/am)*P,(cm/am)*Pc],[-(bm/cm)*Qmat*A,(bm/am)*Paa-y]]','trace':'-kAt*(h^2+k*l)*hp*rho^2(N_W)/6','c_residual_and_divided_arrow':'kAt*cm','right_arrow':'fixed determinant adjoint'}}
