#!/usr/bin/env python3
"""Universal terminal-pencil coefficient morphisms; no actual HM data."""
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

CHECKS = 0

def check(ok, message):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise RuntimeError(message)


def nullspace(rows, ncols):
    a = [[F(x) for x in row] for row in rows]
    if any(len(row) != ncols for row in a):
        raise ValueError('wrong row length')
    pivots = []
    i = 0
    for j in range(ncols):
        pivot = next((k for k in range(i, len(a)) if a[k][j]), None)
        if pivot is None:
            continue
        a[i], a[pivot] = a[pivot], a[i]
        scale = a[i][j]
        a[i] = [x / scale for x in a[i]]
        for k in range(len(a)):
            if k != i and a[k][j]:
                scale = a[k][j]
                a[k] = [x-scale*y for x, y in zip(a[k], a[i])]
        pivots.append(j)
        i += 1
        if i == len(a):
            break
    free = [j for j in range(ncols) if j not in pivots]
    basis = []
    for j in free:
        v = [F(0)] * ncols
        v[j] = F(1)
        for k, p in enumerate(pivots):
            v[p] = -a[k][j]
        basis.append(v)
    return basis


def equations(m, r):
    """E2^r source columns (x-copy0,y-copy0,...), target E_m.
    Variables row-major F: m x 2r, then G: (m-1) x r.
    Impose B_x F=G A_x and B_y F=G A_y, coefficientwise.
    """
    if not (1 <= m <= 16 and 1 <= r <= 8):
        raise ValueError('bounded universal inputs required')
    nf = m * 2*r
    n = nf + (m-1)*r
    rows = []
    for direction in (0, 1):
        for i in range(m-1):
            for c in range(2*r):
                row = [0]*n
                row[(i+direction)*2*r+c] = 1
                if c % 2 == direction:
                    row[nf+i*r+c//2] -= 1
                rows.append(row)
    return rows, n, nf


def general_equations(n, m):
    """Full x/y equations for one standard E_n -> E_m."""
    nf=m*n
    count=nf+(m-1)*(n-1)
    rows=[]
    for direction in (0,1):
        for i in range(m-1):
            for c in range(n):
                row=[0]*count
                row[(i+direction)*n+c]=1
                j=c-direction
                if 0 <= j < n-1:
                    row[nf+i*(n-1)+j]-=1
                rows.append(row)
    return rows,count


def mixed_equations(ms,r):
    src=sum(ms); dst=sum(m-1 for m in ms); nf=src*2*r
    n=nf+dst*r; rows=[]; so=to=0
    for m in ms:
        for direction in (0,1):
            for i in range(m-1):
                for c in range(2*r):
                    row=[0]*n
                    row[(so+i+direction)*2*r+c]=1
                    if c%2==direction:
                        row[nf+(to+i)*r+c//2]-=1
                    rows.append(row)
        so+=m; to+=m-1
    return rows,n,nf,dst


def expected_basis(m, r, n, nf):
    ans = []
    if m == 1:
        for j in range(2*r):
            v = [F(0)]*n; v[j]=F(1); ans.append(v)
    elif m == 2:
        for j in range(r):
            v = [F(0)]*n
            v[2*j] = v[2*r+2*j+1] = v[nf+j] = F(1)
            ans.append(v)
    return ans


def solve(m, r):
    rows, n, nf = equations(m, r)
    basis = nullspace(rows, n)
    expected = expected_basis(m, r, n, nf)
    check(basis == expected, f'exact basis m={m},r={r}')
    check(len(basis) == r*max(0,3-m), f'dimension m={m},r={r}')
    check(all(sum(x*y for x,y in zip(row,v)) == 0
              for row in rows for v in basis), f'full coefficient identity m={m},r={r}')
    return {'m':m, 'r':r, 'variables':n, 'equations':len(rows),
            'hom_dimension':len(basis),
            'basis':[[str(x) for x in v] for v in basis]}


def matrix_rank(a, ncols):
    return ncols - len(nullspace(a,ncols))


def split_terminal_matrix(ms, r, coefficients):
    """Construct every terminal map: E1 contributes zero, E2 arbitrary row.
    Coefficients contains one length-r row per E2 summand.
    """
    if len(coefficients) != ms.count(2) or any(len(v)!=r for v in coefficients):
        raise ValueError('one coefficient row per E2 summand required')
    out=[]; j=0
    for m in ms:
        if m < 1: raise ValueError('m must be positive')
        if m == 2:
            out.append(coefficients[j]); j+=1
        else:
            out.extend([[0]*r for _ in range(m-1)])
    return out


def main():
    here=Path(__file__).resolve().parent
    manifest=json.loads((here/'INPUTS.json').read_text())
    for entry in manifest:
        b=(here/entry['file']).read_bytes()
        check(hashlib.sha256(b).hexdigest()==entry['sha256'],'input SHA256')
        check(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==entry['git_blob'],'input Git blob')
    results=[solve(m,r) for r in (1,2,3) for m in range(1,11)]
    general=[]
    for n in range(1,7):
        for m in range(1,11):
            rows,count=general_equations(n,m)
            basis=nullspace(rows,count)
            check(len(basis)==max(0,n-m+1),'general kernel restriction dimension')
            check(all(sum(x*y for x,y in zip(row,v))==0 for row in rows for v in basis),'general full coefficient identities')
            general.append({'source':n,'target':m,'dimension':len(basis),'basis':[[str(x) for x in v] for v in basis]})
    mixed=[]
    for ms in ([1,2,3,8],[3,1,2,2],[1,1,8],[2,2,2],[1,3,10]):
        for r in (1,2,3):
            rows,n,nf,dst=mixed_equations(ms,r)
            basis=nullspace(rows,n)
            check(len(basis)==r*(2*ms.count(1)+ms.count(2)),'mixed rectangular Hom dimension')
            check(all(sum(x*y for x,y in zip(row,v))==0 for row in rows for v in basis),'mixed all coefficients')
            tails=[v[nf:] for v in basis]
            check(matrix_rank(tails,dst*r)==r*ms.count(2),'mixed terminal map-space capacity')
            offset=0
            for m in ms:
                if m>=3:
                    check(all(not any(v[nf+offset*r:nf+(offset+m-1)*r]) for v in basis),'mixed long terminal block vanishes')
                offset+=m-1
            mixed.append({'blocks':ms,'r':r,'hom_dimension':len(basis),'terminal_map_space_dimension':r*ms.count(2),'basis':[[str(x) for x in v] for v in basis]})
    # E2^8 can inject terminal coefficients into exactly eight E2 slots;
    # seven slots cannot do so. Long slots and E1 slots add no capacity.
    capacities=[]
    for r in (1,2,3,8):
        for k in (0,1,2,7,8,9):
            ms=[1]+[2]*k+[3,8,10]
            coeff=[[int(i==j) for j in range(r)] for i in range(k)]
            mat=split_terminal_matrix(ms,r,coeff)
            rank=matrix_rank(mat,r)
            check(rank==min(k,r),'sharp terminal capacity')
            check(all(not any(row) for row in mat[k:]),'long blocks carry zero terminal image')
            capacities.append({'source_multiplicity':r,'E2_slots':k,'rank':rank})
    # A tempting one-direction-only diagonal mimic for m=3 is rejected
    # by the y coefficient even though its x equation vanishes.
    rows,n,nf=equations(3,1)
    wrong=[F(0)]*n; wrong[0]=wrong[nf]=1
    half=len(rows)//2
    check(all(sum(x*y for x,y in zip(row,wrong))==0 for row in rows[:half]),'one-direction false positive control')
    check(any(sum(x*y for x,y in zip(row,wrong))!=0 for row in rows[half:]),'second coefficient rejects false map')
    check(matrix_rank([[1,0],[0,1]],2)==2,'rank full control')
    check(matrix_rank([[1,2],[2,4]],2)==1,'rank dependent control')
    print(json.dumps({'checks':CHECKS,'scope':'universal rational coefficient pencils only; no actual HM data',
                      'hom_tests':results,'general_hom_tests':general,'mixed_hom_tests':mixed,'capacity_tests':capacities},indent=2,sort_keys=True))

if __name__=='__main__':
    main()
