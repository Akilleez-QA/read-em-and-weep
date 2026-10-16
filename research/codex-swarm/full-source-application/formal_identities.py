"""Small exact free-word identities; no physical polynomial operations."""
from fractions import Fraction as Q


def atom(name):
    return {(name,): Q(1)}


def add(*ps):
    out={}
    for p in ps:
        for w,c in p.items():out[w]=out.get(w,Q(0))+c
    return {w:c for w,c in out.items()if c}


def scale(p,c):return {w:c*v for w,v in p.items()if c*v}


def mul(*ps):
    out={():Q(1)}
    for p in ps:
        nxt={}
        for a,c in out.items():
            for b,d in p.items():
                w=a+b
                if len(w)>12:raise ValueError('abstract word length guard')
                nxt[w]=nxt.get(w,Q(0))+c*d
        out={w:c for w,c in nxt.items()if c}
        if len(out)>128:raise ValueError('abstract word count guard')
    return out


def defect_syzygy(signs=(1,1,-1,-1)):
    """Ambient notation in PROOF: X A=A V and A B=C D.

    Eikl=V W-B H, Eijk=Y Z-A W, Eijl=T Z-D H,
    Fij(Ejkl)=X Y-C T. Return expansion and its two coherence remainders.
    """
    A,B,C,D,H,V,W,X,Y,Z,T=map(atom,['A','B','C','D','H','V','W','X','Y','Z','T'])
    eikl=add(mul(V,W),scale(mul(B,H),-1))
    eijk=add(mul(Y,Z),scale(mul(A,W),-1))
    eijl=add(mul(T,Z),scale(mul(D,H),-1))
    fij_ejkl=add(mul(X,Y),scale(mul(C,T),-1))
    terms=[mul(A,eikl),mul(X,eijk),mul(C,eijl),mul(fij_ejkl,Z)]
    actual=add(*(scale(v,s)for v,s in zip(terms,signs)))
    remainder=add(mul(add(mul(A,V),scale(mul(X,A),-1)),W),
                  mul(add(mul(C,D),scale(mul(A,B),-1)),H))
    return actual,remainder


def reduction_identity(boundary_sign=1):
    """s-terms of tf M minus baseline = -delta(s*k)+F*k_out."""
    sjk,sij,sik,kb,ki,ko=map(atom,['s_jk','s_ij','s_ik','kbar','k_ij','k_ik'])
    C0=add(scale(kb,-1),ko,scale(ki,-1))
    lhs=add(mul(sjk,ki),mul(sij,kb),mul(add(sjk,sij),C0))
    deltaW=add(mul(sjk,kb),scale(mul(sik,ko),-1),mul(sij,ki))
    F=add(sjk,scale(sik,-1),sij)
    # The accepted source identity is lhs+deltaW-F*k_out=0.
    return add(lhs,scale(deltaW,boundary_sign),scale(mul(F,ko),-1))
