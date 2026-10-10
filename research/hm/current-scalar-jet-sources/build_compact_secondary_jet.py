#!/usr/bin/env python3
"""Exact finite reverse-jet circuit, without expanding coefficient-ring products."""
import json,hashlib,time
from fractions import Fraction
from pathlib import Path

def build(D,axis=1,K=6,output=1,first=0,remove=48,target=164):
    root=D['outputs'][output]; need=set()
    def visit(s):
        if s<16 or s in need:return
        need.add(s)
        for c,f in D['sumNodes'][s-16]:
            for j,e in f:visit(j)
    for j,e in root['factors']:visit(j)
    rem=[i for i in range(4) if i not in (first,axis)]
    Z=(0,0,0,0,0,0)
    def union(A,B):
        if A is None:return B
        if B is None:return A
        return tuple(min(A[i],B[i]) if i%2==0 else max(A[i],B[i]) for i in range(6))
    def product(A,B):
        if A is None or B is None:return None
        return tuple(x+y for x,y in zip(A,B))
    def times(A,B):
        C=[None]*K
        for r in range(K):
            for s in range(r+1):C[r]=union(C[r],product(A[s],B[r-s]))
        return C
    one=[Z]+[None]*(K-1)
    counts={'symbolicCoefficientRingProducts':0,'symbolicCoefficientRingAdditions':0,'powerCalls':0,'formalFrobeniusLeadingPowers':0}
    def mult(A,B):
        counts['symbolicCoefficientRingProducts']+=sum(A[s] is not None and B[r-s] is not None for r in range(K) for s in range(r+1))
        counts['symbolicCoefficientRingAdditions']+=sum(max(0,sum(A[s] is not None and B[r-s] is not None for s in range(r+1))-1) for r in range(K))
        return times(A,B)
    def power(A,e):
        counts['powerCalls']+=1
        if not e:return one
        if e==1:return A
        if all(v is None for v in A[1:]):return [None if A[0] is None else tuple(e*v for v in A[0])]+[None]*(K-1)
        B=one
        while e:
            if e%2:B=mult(B,A)
            e//=2
            if e:A=mult(A,A)
        return B
    deg={};totaldeg={};bounds={};cache={}
    for j in range(4):
        deg[j]=int(j==axis)
        totaldeg[j]=1
        b=list(Z)
        if j in rem:b[2*rem.index(j)]=b[2*rem.index(j)+1]=b[4]=b[5]=1
        bounds[j]=[tuple(b)]+[None]*(K-1)
    def factor(j,e):
        assert not (4<=j<16),('Noncoordinate factor',j)
        assert j!=first,('Eliminated axis leaked',j)
        if e==1:return bounds[j]
        key=(j,e)
        if key not in cache:cache[key]=power(bounds[j],e)
        return cache[key]
    nodes=[];dropped=0;retained=0;slots=0
    for s in sorted(need):
        terms=D['sumNodes'][s-16]
        degree=max((sum(e*deg[j] for j,e in f) for c,f in terms),default=0);deg[s]=degree
        totaldeg[s]=max((sum(e*totaldeg[j] for j,e in f) for c,f in terms),default=0)
        C=[None]*K;kept=[]
        for c,f in terms:
            shift=degree-sum(e*deg[j] for j,e in f)
            if shift>=K:dropped+=1;continue
            # Preserve exact rational coefficients; no characteristic identities.
            cv=Fraction(int(c[0]),int(c[1]))
            if not cv:continue
            T=one
            for j,e in f:T=mult(T,factor(j,e))
            for r in range(shift,K):
                if C[r] is not None and T[r-shift] is not None:counts['symbolicCoefficientRingAdditions']+=1
                C[r]=union(C[r],T[r-shift])
            kept.append([[str(cv.numerator),str(cv.denominator)],shift,f]);retained+=1;slots+=len(f)
        nodes.append({'sourceSymbol':s,'degree':degree,'totalDegreeBound':totaldeg[s],'terms':kept,'layerSupport':C})
        bounds[s]=C
    factors=[];removed=[]
    for j,e in root['factors']:
        if remove and j<4 and j!=first:
            assert e==remove
            removed.append(j);e-=remove
        if e:factors.append([j,e])
    assert not remove or len(removed)==3
    rd=sum(deg[j]*e for j,e in factors);assert rd<=target,(rd,target)
    C=one
    for j,e in factors:C=mult(C,factor(j,e))
    shift=target-rd;C=[None if r<shift else C[r-shift] for r in range(K)]
    coef=[str(int(root['coefficient'][0])),str(int(root['coefficient'][1]))]
    return {'schema':'hm-exact-compact-reverse-jet-factor-sum-v1','coefficientField':'Q','characteristic':0,'truncationLength':K,'firstEliminatedAxis':first,'secondEliminatedAxis':axis,'remainingAxes':rem,'sourceOutputIndex':output,'sourceDegreeBound':target,'normalizedSyntaxDegree':rd,'normalizedFactoredTotalDegreeBound':sum(totaldeg[j]*e for j,e in factors),'nodeBoundMethod':'Coordinate degree and total degree use sum for products and maximum for sums, retaining conservative bounds through cancellations.','removedCoordinateFactor':remove,'semantics':{'leaf':'J_j(s)=1 for the eliminated u coordinate; other coordinate leaves retain their formal polynomial variable.','symbol':'J_id(s)=sum_[c,shift,f] c*s^shift*product_(j,e in f) J_j(s)^e modulo s^K. Its declared degree is the source polynomial degree bound, even when leading terms cancel.','power':'Formal polynomial power in Q[remaining variables][s]/(s^K); no Frobenius or exponent reduction is used.','droppedTermRule':'A term with reverseShift >= K is exactly zero in this quotient, before any further multiplication; all later shifts and polynomial degrees are nonnegative.','homogeneousProjection':'Each output selects a reverse coefficient first, then applies its explicit homogeneous-degree projector in the two remaining variables. No variable is set to1 before that projection.'},'sumNodes':nodes,'root':{'coefficient':coef,'reverseShift':shift,'factors':factors},'outputs':[{'reverseCoefficient':r,'layerSupport':C[r]} for r in range(K)],'representationCounts':{'sumSymbols':len(nodes),'weightedProductTerms':retained,'factorSlots':slots,'termsDiscardedByCertifiedReverseShift':dropped},'symbolicEvaluationCostUpperEstimate':counts,'coefficientEvaluationPerformed':False,'homogeneousProjectionEvaluated':False,'dehomogenizationApplied':False}

