"""Regular linear split of arbitrary bidegree-(5,3) binary c-source data.

The coefficient variables are u,w, binary variables S,T and ell=-w*S+u*T.
All coefficients remain arbitrary; no geometric point or marking is chosen.
"""
import sympy as s

def regular_cubic_ell_split_degree(Z,u,w,S,T,coefficient_degree):
    """Regular split of bidegree-(m,3) data, m>=0, with no image assumption.

    Return (Q,polar) satisfying Z=ell*Q+polar.  The denominator is purely
    numerical; no coefficient or geometric coordinate is inverted.
    """
    m=coefficient_degree
    if not isinstance(m,int) or m<0:raise ValueError('Expected an integer degree m>=0.')
    n=m+3
    delta=lambda e:s.expand(S*s.diff(e,u)+T*s.diff(e,w))
    omega=lambda e:s.expand(s.diff(e,u,T)-s.diff(e,w,S))
    ell=-w*S+u*T
    z=s.expand(Z.subs({S:u,T:w},simultaneous=True))
    polar=s.expand(delta(delta(delta(z)))/(n*(n-1)*(n-2)))
    # [omega,delta]=0, so omega annihilates this polar.  No subtraction
    # or failed image condition is hidden in the regular inverse.
    W1=omega(Z);W2=omega(W1);W3=omega(W2)
    Q=s.expand(W1/n-ell*W2/(2*n*(n-1))+ell**2*W3/(6*n*(n-1)*(n-2)))
    return Q,polar

def regular_cubic_ell_split(Z,u,w,S,T):
    """Backward-compatible coefficient-degree-five source split."""
    return regular_cubic_ell_split_degree(Z,u,w,S,T,5)

if __name__=='__main__':
    u,w,S,T=s.symbols('u w S T');c=s.symbols('z0:24')
    Z=sum(c[4*i+j]*u**(5-i)*w**i*S**(3-j)*T**j for i in range(6) for j in range(4))
    Q,polar=regular_cubic_ell_split(Z,u,w,S,T)
    ell=-w*S+u*T
    assert s.expand(Z-ell*Q-polar)==0
    assert s.expand((Z-polar).subs({S:u,T:w},simultaneous=True))==0
    assert s.expand(u*s.diff(Q,u)+w*s.diff(Q,w)-4*Q)==0
    assert s.expand(S*s.diff(Q,S)+T*s.diff(Q,T)-2*Q)==0
    # The restriction to the complete ell image is a genuine left inverse.
    b=s.symbols('b0:15')
    original=sum(b[3*i+j]*u**(4-i)*w**i*S**(2-j)*T**j for i in range(5) for j in range(3))
    recovered,remainder=regular_cubic_ell_split(ell*original,u,w,S,T)
    assert s.expand(recovered-original)==0 and remainder==0
    for m in range(6):
        cc=s.symbols('c0:'+str(4*(m+1)))
        Zm=sum(cc[4*i+j]*u**(m-i)*w**i*S**(3-j)*T**j for i in range(m+1) for j in range(4))
        Qm,Pm=regular_cubic_ell_split_degree(Zm,u,w,S,T,m)
        assert s.expand(Zm-ell*Qm-Pm)==0
        assert s.expand(s.diff(Pm,u,T)-s.diff(Pm,w,S))==0
        assert s.expand((Zm-Pm).subs({S:u,T:w},simultaneous=True))==0
    print('PASS arbitrary coefficient degrees0 through5 and exact polar annihilation; all24 free cubic-source coefficients: regular exact split, bidegrees, diagonal restriction and full15-coefficient ell-image inverse.')
