#!/usr/bin/env python3
"""Finite oriented-chain and coefficient-map controls; no source polynomials."""
import sys
if not __debug__:
    print('ERROR: assertions disabled',file=sys.stderr);raise SystemExit(2)
from itertools import product, combinations
from fractions import Fraction
from collections import Counter
import json
from test_scalar_homotopy_adjoint import hom
counts=Counter()

def canon(vertices):
    if len(set(vertices)) != len(vertices):return (),0
    sign=(-1)**sum(vertices[i]>vertices[j] for i in range(len(vertices)) for j in range(i+1,len(vertices)))
    return tuple(sorted(vertices)),sign

def add(out,vertices,c):
    v,s=canon(tuple(vertices));c*=s
    if c:
        out[v]=out.get(v,0)+c
        if not out[v]:del out[v]

def boundary(chain):
    out={}
    for vertices,c in chain.items():
        for i in range(len(vertices)):add(out,vertices[:i]+vertices[i+1:],c*(-1)**i)
    return out

def aw_edge(e0,e1):
    out=[]
    for d in range(4):
        if e0[d]==e1[d]:continue
        states=tuple(('B' if e0[i] else 'A') if i<d else 'C' if i==d else ('B' if e1[i] else 'A') for i in range(4))
        out.append((states,1 if e0[d]<e1[d] else -1))
    return out

def g_aw(e0,e1):
    out={}
    for states,c in aw_edge(e0,e1):
        active=states.index('C')
        a=tuple(0 if s in ('A','C') else 1 for s in states)
        b=list(a);b[active]=1
        add(out,(a,tuple(b)),c)
    return out

def g_path(e0,e1):
    out={};a=e0
    for d in (3,2,1,0):
        if a[d]==e1[d]:continue
        b=list(a);b[d]=e1[d];b=tuple(b)
        add(out,(a,b),1);a=b
    return out

def cone(vertex,chain):
    out={}
    for key,c in chain.items():add(out,(vertex,)+key,c)
    return out

vertices=list(product((0,1),repeat=4))
maxima={'k_nonzero_triangles':0,'pair12_raw_paths':0,'pair34_raw_paths':0}
witness={}
for e0,e1 in combinations(vertices,2):
    g=g_aw(e0,e1);assert g==g_path(e0,e1);counts['AW_reverse_path_edges']+=1
    b=tuple(min(x,y) for x,y in zip(e0,e1))
    diff={(e0,e1):1}
    for key,c in g.items():add(diff,key,-c)
    k=cone(b,diff)
    assert boundary(k)==diff;counts['rectangle_cone_boundary_edges']+=1
    assert len(k)<=5;counts['five_triangle_bounds']+=1
    maxima['k_nonzero_triangles']=max(maxima['k_nonzero_triangles'],len(k))
    for exponents in product((-3,-2,-1,0,1),repeat=4):
        for ns,name,limit in [((-2,-2,0,0),'pair12_raw_paths',16),((0,0,-2,-2),'pair34_raw_paths',32)]:
            branches=sum(len(hom(ns,tuple(zip(states,exponents)),True)) for states,_ in aw_edge(e0,e1))
            paths=2*branches
            assert paths<=limit;counts['raw_request_bound_checks']+=1
            if paths>maxima[name]:maxima[name]=paths;witness[name]={'edge':[e0,e1],'exponents':exponents}
# Weighted prism on a toy common refinement, ordered SOURCE FIRST (alpha,e).
common=list(product(range(2),repeat=2))
def r(a):return a[1]
def rho(e,alpha):return Fraction((1,2)[alpha],3) if e==0 else Fraction((3,2)[alpha],5)
def evaluate(c,vs):
    key,sign=canon(tuple(vs));return sign*c.get(key,0)
def dc(c,degree):
    out={}
    for vs in combinations(common,degree+2):
        val=sum((-1)**i*evaluate(c,vs[:i]+vs[i+1:]) for i in range(len(vs)))
        if val:out[vs]=val
    return out

def H(c,degree):
    if degree==0:return {}
    out={}
    for vs in combinations(common,degree):
        value=0
        for pivot in range(degree):
            for labels in product(range(2),repeat=pivot+1):
                inserted=tuple((alpha,r(vs[i])) for i,alpha in enumerate(labels))
                weight=Fraction((-1)**pivot)
                for i,alpha in enumerate(labels):weight*=rho(r(vs[i]),alpha)
                value+=weight*evaluate(c,inserted+vs[pivot:])
        if value:out[vs]=value
    return out

def RPi(c,degree):
    out={}
    for vs in combinations(common,degree+1):
        es=tuple(r(a) for a in vs)
        # Pi is first defined on sorted target tuples then alternated.
        ordered,orientation=canon(es)
        if not orientation:continue
        value=0
        for labels in product(range(2),repeat=degree+1):
            weight=Fraction(orientation)
            for e,alpha in zip(ordered,labels):weight*=rho(e,alpha)
            value+=weight*evaluate(c,tuple((alpha,e) for e,alpha in zip(ordered,labels)))
        if value:out[vs]=value
    return out
for degree in range(4):
    for basis in combinations(common,degree+1):
        c={basis:Fraction(1)}
        dh=dc(H(c,degree),degree-1) if degree else {}
        hd=H(dc(c,degree),degree+1)
        projected=RPi(c,degree)
        for output in combinations(common,degree+1):
            assert dh.get(output,0)+hd.get(output,0)==c.get(output,0)-projected.get(output,0),(degree,basis,output)
            counts['weighted_prism_identity_entries']+=1
# q=2 explicit +first branch -second branch is the generic H formula.
for source in combinations(common,3):
    c={source:Fraction(1)}
    for a0,a1 in combinations(common,2):
        value=sum(rho(r(a0),b0)*evaluate(c,((b0,r(a0)),a0,a1)) for b0 in range(2))
        value-=sum(rho(r(a0),b0)*rho(r(a1),b1)*evaluate(c,((b0,r(a0)),(b1,r(a1)),a1)) for b0,b1 in product(range(2),repeat=2))
        assert value==H(c,2).get((a0,a1),0)
        counts['two_branch_prism_entries']+=1
print(json.dumps({'status':'PASS','scope':'formal finite chains and coefficient indices only','counts':dict(counts),'maxima_on_test_domain':maxima,'witnesses':witness,'total_checks':sum(counts.values())},indent=2))
