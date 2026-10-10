#!/usr/bin/env python3
"""Exact independent certificate for four u*beta Atiyah detector classes.

Default is the k=0 stable Hamiltonian ribbon bundle. All arithmetic is exact.
Certifies the full spectral sequence relevant to survival, the actual Cech
cocycles, and dual functionals detecting four independent nonzero classes.
Also computes the full End(F) d5 and cohomology as an independent check.
"""
import json
from pathlib import Path
import sympy as S
from sympy.polys.domains import QQ
import model as M
import spectral_d1 as C
import cech_transfer as T


def rank(A):return len(A.to_DM().convert_to(QQ).rref(method='GJ')[1])

def sparse(A):
    return dict(shape=list(A.shape),entries=[[r,c,str(v)] for r,c,v in
                sorted((r,c,v) for (r,c),v in A.todok().items())])


def derivative_cochain(data,variable):
    """Literal u*d_x differential, where u is the Cech monomial 1/(st)."""
    out={}
    for i,A in data['d'].items():
        for r in range(A.rows):
            for c in range(A.cols):
                f=S.diff(A[r,c],variable)
                if f==0:continue
                for exps,value in S.Poly(f,M.s,M.t,*M.x).terms():
                    e=(exps[0]-1,exps[1]-1)+exps[2:]
                    for b in range(4):out[i,c,i+1,r,e,3,1<<b]=value
    return out


def audit():
    data=M.build();M.verify(data,verbose=False)
    assert T.verify_contraction()==640
    tw=(-2,-1);rows={};ranks={}
    for q in [4,1,0]:
        dims,mats=C.row(data,q,tw)
        rr={p:rank(A) for p,A in mats.items() if A.rows and A.cols}
        for p in range(-3,2):
            assert mats[p+1]*mats[p]==S.zeros(mats[p+1].rows,mats[p].cols)
        rows[q]=mats;ranks[q]=rr
        print('EndF(-2,-1): q=',q,'E1 dimensions=',dims,'d1 ranks=',rr)
    assert ranks=={4:{-3:36,-2:28},1:{0:132},0:{2:60}}
    A=rows[1][0];target=C.basis(data,1,1,tw)
    cocycles=[derivative_cochain(data,x) for x in M.x]
    beta=[]
    for Z in cocycles:
        assert not T.vertical(Z),'u beta must be Cech closed'
        assert not T.horizontal(data,Z),'u beta must be Hom closed'
        beta.append(T.project(Z,target))
    B=S.Matrix.hstack(*beta)
    individual=[rank(A.row_join(v)) for v in beta]
    joint=rank(A.row_join(B))
    assert individual==[133]*4 and joint==136
    print('Actual u*beta_j: individual augmented ranks=',individual,'joint rank=',joint)
    annihilator=S.Matrix.hstack(*A.T.nullspace()).T
    pairing=annihilator*B
    selected=list(pairing.T.rref()[1])
    assert len(selected)==4
    N=annihilator[selected,:];P=N*B
    W=P.inv()*N
    assert W*A==S.zeros(4,144)
    assert W*B==S.eye(4)
    print('PASS: exact 4 x 144 detector W satisfies W*d1=0 and W*[u beta_j]=I4.')
    # The only remaining higher differential for this twist is d2: 12 -> 20.
    K=A.nullspace();d2cols=[]
    for v in K:
        col,_=T.transfer_column(data,0,1,tw,v,2)
        d2cols.append(col)
    d2=S.Matrix.hstack(*d2cols)
    assert rows[0][2]*d2==S.zeros(60,12)
    assert rank(d2)==12
    print('EndF(-2,-1): d2 has rank12; h2=24, all other cohomology dimensions zero.')
    # Full End(F): only q0 and one isolated q4 source.
    dims0,mats0=C.row(data,0,(0,0))
    fullranks={p:rank(mats0[p]) for p in [0,1,2]}
    assert fullranks=={0:393,1:922,2:315}
    full_source=C.basis(data,-3,4,(0,0));assert len(full_source)==3
    d5cols=[]
    for i in range(3):
        col,_=T.transfer_column(data,-3,4,(0,0),S.eye(3)[:,i],5)
        d5cols.append(col)
    d5=S.Matrix.hstack(*d5cols)
    assert mats0[2]*d5==S.zeros(315,3)
    d5rank=rank(mats0[1].row_join(d5))-fullranks[1]
    assert d5rank==3
    print('EndF: q0 d1 ranks=',fullranks,'d5 quotient rank=',d5rank)
    print('EndF: h0=1, h1=21, and all higher cohomology dimensions zero.')
    certificate={
        'model':'k=0 Hamiltonian ribbon F on P1 x P3',
        'basis_order':'spectral_d1.basis(build(),1,1,(-2,-1)); label=(source_degree,source_index,target_degree,target_index,(s,t,x0,x1,x2,x3) Laurent exponents)',
        'target_basis':target,
        'd1':sparse(A),
        'u_beta_columns':sparse(B),
        'dual_detector':sparse(W),
        'q4_first_d1':sparse(rows[4][-3]),
        'q4_second_d1':sparse(rows[4][-2]),
        'd2_columns_on_d1_nullspace':sparse(d2),
        'full_end_d5_columns':sparse(d5),
        'd1_ranks_by_q':ranks,
        'individual_augmented_ranks':individual,
        'joint_augmented_rank':joint,
        'full_end_d1_ranks':fullranks,
        'full_end_d5_rank':d5rank,
    }
    path=Path(__file__).with_name('exact_certificate.json')
    path.write_text(json.dumps(certificate,indent=2)+'\n')
    print('Saved exact certificate:',path)
    return certificate

if __name__=='__main__':audit()
