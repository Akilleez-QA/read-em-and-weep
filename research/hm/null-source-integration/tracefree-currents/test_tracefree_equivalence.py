#!/usr/bin/env python3
"""Abstract exact 2x2 controls only. No physical model imports or evaluation."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json
import unittest

if not __debug__:
    raise SystemExit('Optimized Python refused')

def mat(a,b,c,d):return ((F(a),F(b)),(F(c),F(d)))
def add(*xs):return tuple(tuple(sum(x[i][j] for x in xs) for j in range(2)) for i in range(2))
def scale(a,s):return tuple(tuple(s*x for x in row) for row in a)
def mul(a,b):return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def tr(a):return a[0][0]+a[1][1]
def det(a):return a[0][0]*a[1][1]-a[0][1]*a[1][0]
def inv(a):return scale(mat(a[1][1],-a[0][1],-a[1][0],a[0][0]),1/det(a))
def tf(a):return add(a,scale(I,-tr(a)/2))
def transpose(a):return tuple(zip(*a))
def tangent(a,da,qa,qb):return add(da,mul(qb,a),scale(mul(a,qa),-1))
I=mat(1,0,0,1)
H=mat(1,0,0,-1)
E=mat(0,1,0,0)
FF=mat(0,0,1,0)
SL=(I,mat(1,2,0,1),mat(1,0,-3,1),mat(2,1,1,1))
BASIS=(H,E,FF)
FULL=(I,H,E,FF)

class Controls(unittest.TestCase):
    def test_pinned_source_bytes_and_determinant_dependency(self):
        root=Path(__file__).parent
        pins=json.loads((root/'source-pins.json').read_text())
        for pin in pins:
            raw=(root/'sources'/pin['file']).read_bytes()
            self.assertEqual(hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest(),pin['git_blob'])
        receipt=json.loads((root/'sources/determinant-verification.json').read_text())['checks']['determinants']
        self.assertEqual(receipt['status'],'PASS')
        self.assertEqual(receipt['orderedPairs'],[list(p) for p in product(range(6),repeat=2)])
        self.assertEqual(receipt['modelSHA256'],'635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926')
        current=(root/'sources/physical_current_source_binding.py').read_text()
        self.assertIn(receipt['modelSHA256'],current)
        self.assertFalse(receipt['pointSamplesUsedAsProof'])

    def test_missing_term_general_basis(self):
        for k,r in product(FULL,repeat=2):
            self.assertEqual(tr(mul(k,r))-tr(mul(k,tf(r))),tr(k)*tr(r)/2)

    def test_moving_frame_L_and_transported_U(self):
        # dA=A X and dB=B Y are exact determinant-one tangent jets.
        # They are realized by A exp(tX), B exp(tY), respectively.
        qa,qb,qc=scale(H,F(2,3)),scale(H,F(-5,7)),scale(H,F(11,13))
        daframe=mat(F(3,2),0,0,F(2,3))
        dbframe=mat(F(5,3),0,0,F(3,5))
        dcframe=mat(F(7,4),0,0,F(4,7))
        for a,b,x,y in product(SL,SL,BASIS,BASIS):
            ta=tangent(a,mul(a,x),qa,qb)
            tb=tangent(b,mul(b,y),qb,qc)
            l=mul(inv(a),ta)
            u=mul(mul(mul(inv(a),inv(b)),tb),a)
            ga=mul(mul(dbframe,a),inv(daframe))
            gb=mul(mul(dcframe,b),inv(dbframe))
            dga=mul(mul(dbframe,ta),inv(daframe))
            dgb=mul(mul(dcframe,tb),inv(dbframe))
            lp=mul(inv(ga),dga)
            up=mul(mul(mul(inv(ga),inv(gb)),dgb),ga)
            self.assertEqual(lp,mul(mul(daframe,l),inv(daframe)))
            self.assertEqual(up,mul(mul(daframe,u),inv(daframe)))
            for r in (l,u,lp,up):
                self.assertEqual(tr(r),0)
                self.assertEqual(tf(r),r)
                for k in FULL+(mat(3,2,-7,5),):
                    for weight in (F(0),F(1),F(-11,7)):
                        self.assertEqual(weight*tr(mul(k,r)),weight*tr(mul(k,tf(r))))

    def test_selector_transpose_and_physical_adapter(self):
        l=(F(2),F(-3));r=(F(5),F(7));k=mat(r[0]*l[0],r[1]*l[0],r[0]*l[1],r[1]*l[1])
        self.assertNotEqual(tr(k),0)
        d=mat(3,0,0,F(1,3))
        for residual in FULL:
            direct=sum(l[i]*residual[j][i]*r[j] for i,j in product(range(2),repeat=2))
            self.assertEqual(direct,tr(mul(k,residual)))
            rp=mul(mul(d,residual),inv(d))
            self.assertEqual(mul(mul(d,transpose(rp)),inv(d)),transpose(residual))

    def test_nonSL2_negative_controls(self):
        # A(0)=I but A'(0)=diag(1,0): determinant value alone is insufficient.
        r=mat(1,0,0,0)
        self.assertEqual(det(I),1)
        self.assertNotEqual(tr(mul(inv(I),r)),0)
        # An endpoint scalar connection spoils the conclusion as well.
        self.assertEqual(tr(tangent(I,mat(0,0,0,0),mat(0,0,0,0),I)),2)

    def test_raw_baseline_and_second_jet_negative_controls(self):
        k=mat(1,0,0,0)
        self.assertEqual(mul(H,H),I)
        self.assertEqual(tr(mul(k,I)),1)
        self.assertEqual(tr(mul(k,tf(I))),0)
        # At t=0, diag(exp(t),exp(-t)) has A=I, A'=H, A''=I.
        self.assertEqual(tr(mul(inv(I),I)),2)

    def test_weighted_normal_order_is_linear_in_C(self):
        # Arbitrary scalar derivative jets, including nonconstant conversion/D.
        conversion,dc,D,dD,alpha,beta=map(F,(3,5,7,11,13,17))
        for k,r in product(FULL,BASIS):
            raw=F(-19,23)*tr(mul(k,r)); projected=F(-19,23)*tr(mul(k,tf(r)))
            def coeff(c):return (c*(alpha*(dc/D-conversion*dD/D**2)+beta*conversion/D),c*alpha*conversion/D)
            self.assertEqual(coeff(raw),coeff(projected))

if __name__=='__main__':unittest.main(verbosity=2)
