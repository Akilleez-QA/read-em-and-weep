"""PH-R: exact source-free frame controls and read-only source metadata audit.

Stored physical coefficients are never used in arithmetic. Artificial Laurent
matrices below are deliberately unrelated to the pinned primitive matrices.
"""
import copy
import hashlib
import json
from fractions import Fraction as Q
from itertools import combinations, product
from pathlib import Path
import subprocess
import unittest
import frames as producer

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
ZERO = (0, 0, 0, 0)

# A tiny exact Laurent ring; fractional exponents represent formal line frames.
def scalar(c):
    return {ZERO: Q(c)} if c else {}
def add(*polys):
    out = {}
    for p in polys:
        for e, c in p.items():
            out[e] = out.get(e, Q(0)) + c
    return {e: c for e, c in out.items() if c}
def scale(p, c):
    return {e: c*v for e, v in p.items() if c*v}
def mul(a, b):
    out = {}
    for e, c in a.items():
        for f, d in b.items():
            k = tuple(x+y for x, y in zip(e, f))
            out[k] = out.get(k, Q(0)) + c*d
    return {e: c for e, c in out.items() if c}
def mon(axis, exponent, c=1):
    e = [0]*4
    e[axis] = exponent
    return {tuple(e): Q(c)} if c else {}
def shift(p, e):
    return mul(p, {tuple(e): Q(1)})
def deriv(p, i):
    out = {}
    for e, c in p.items():
        if e[i]:
            f = list(e)
            f[i] -= 1
            out[tuple(f)] = c*e[i]
    return out
def pull(p, bits):
    return {tuple(-a if b else a for a, b in zip(e, bits)): c for e, c in p.items()}
def mm(a, b):
    return [[add(*(mul(a[r][k], b[k][s]) for k in range(2))) for s in range(2)] for r in range(2)]
def madd(a, b, sign=1):
    return [[add(a[r][s], scale(b[r][s], sign)) for s in range(2)] for r in range(2)]
def mscale(a, c):
    return [[scale(p, c) for p in row] for row in a]
def tr(a):
    return add(a[0][0], a[1][1])
def toy(edge):
    return [[add(scalar(1+edge+2*r+s), mon((edge+r+s)%4, 1+r, 2+s),
                     mon((edge+s+1)%4, -1, 1+r)) for s in range(2)] for r in range(2)]
def tangent(k, i, ma, mb, inverted=False, omit=None):
    # Artificial nu_v = product x_i^(mask_i/2), unrelated to HM coefficients.
    qa = (Q(1,2)-Q(ma[i],2)) if inverted else Q(ma[i],2)
    qb = (Q(1,2)-Q(mb[i],2)) if inverted else Q(mb[i],2)
    if omit == 'a': qa = 0
    if omit == 'b': qb = 0
    return [[add(deriv(k[r][s], i), mul(k[r][s], mon(i, -1,
                (1-2*r)*qb-(1-2*s)*qa))) for s in range(2)] for r in range(2)]
def local_core(k, bits):
    return [[shift(pull(k[r][s], bits), [(r-s)*b for b in bits]) for s in range(2)] for r in range(2)]
def trace_term(k20, a, b, c, d):
    return tr(mm(k20, madd(mm(a,b), mm(c,d), -1)))

class Independent(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.marker_bytes = (HERE/'producer-ready.json').read_bytes()
        cls.marker = json.loads(cls.marker_bytes)
        cls.before = {n: hashlib.sha256((HERE/n).read_bytes()).hexdigest() for n in cls.marker['files_sha256']}

    @classmethod
    def tearDownClass(cls):
        after = {n: hashlib.sha256((HERE/n).read_bytes()).hexdigest() for n in cls.before}
        if after != cls.before or (HERE/'producer-ready.json').read_bytes() != cls.marker_bytes:
            raise RuntimeError('producer or marker changed during independent audit')

    def test_01_pins_and_entire_certificate(self):
        self.assertEqual(self.before, self.marker['files_sha256'])
        certificate = json.loads((HERE/'physical-source-certificate.json').read_bytes())
        self.assertEqual(certificate, producer.build(REPO))
        self.assertTrue(all(v is False for v in certificate['global_gates'].values()))
        self.assertFalse(self.marker['global_arithmetic_admission'])
        # Authenticate bytes only; never import or execute pinned physical source.
        for rev, path, expected in producer.PINS:
            raw = subprocess.check_output(['git','show',rev+':'+path], cwd=REPO)
            self.assertEqual(hashlib.sha256(raw).hexdigest(), expected)

    def test_02_elementary_lift_as_independent_subset_polynomials(self):
        for bits in product((0,1), repeat=4):
            for degree in range(5):
                finite = {tuple(int(i in s) for i in range(4)): Q(1)
                          for s in combinations(range(4), degree)}
                # Local product uses X=1,Y=t at infinity and X=x,Y=1 finite.
                local = {}
                for s in combinations(range(4), degree):
                    term = scalar(1)
                    for i in range(4):
                        term = mul(term, mon(i, int((i not in s) if bits[i] else (i in s))))
                    local = add(local, term)
                self.assertEqual(local, shift(pull(finite,bits),bits))

    def test_03_literal_primitive_exponents_and_padding(self):
        raw = producer.read(REPO, producer.V5_REV, 'research/hm/null-operator-compiler/hm-pinned-model.json')
        model = json.loads(raw)
        self.assertEqual(len(model['charts']), 6)
        count = 0
        for carrier, chart in enumerate(model['charts']):
            D = 4 if carrier in (0,5) else 5
            for name in ('di','dp'):
                support = {tuple(map(int,e.split(','))) for e, _ in chart[name]}
                expected = ({(2,0,1,1)} if carrier == 5 else
                            {(1,1,1,1), (0,0,0,0)} if carrier == 0 else
                            {(1,1,1,1), tuple(5 if i == carrier-1 else 0 for i in range(4))})
                self.assertEqual(support, expected)
                self.assertEqual(max(map(sum,support)), D)
            for name in ('I','P'):
                rows = chart[name]
                self.assertEqual((len(rows),len(rows[0])), (15,2) if name=='I' else (2,15))
                for r,row in enumerate(rows):
                    for s,entry in enumerate(row):
                        if not entry: continue
                        count += 1
                        w = s if name=='I' else -r
                        pdegree = max(sum(map(int,e.split(','))) for e,_ in entry)
                        e = max(0,pdegree-D-w)
                        padding = (2-e) if carrier==5 else (1-e) if carrier==0 else -e
                        self.assertGreaterEqual(padding,0)
                        self.assertEqual(D+e+w+padding,(6 if carrier==5 else 5)+w)
        self.assertEqual(count,161)
        # Aux denominator hom_4 = -v1^2 v3 v4, while raw -v1*a has degree5.
        aux_D, raw_D, max_e = 4, 5, 2
        self.assertEqual(2-max_e,0)
        self.assertEqual(aux_D+max_e,6)
        self.assertNotEqual(raw_D+max_e,6)
        # H=a=v0*v1*v3*v4. H²/(v0^e hom_4(d)) has v0^(2-e).
        for e in range(3):
            quotient = tuple(a-b for a,b in zip((2,2,0,2,2),(e,2,0,1,1)))
            self.assertEqual(quotient,(2-e,0,0,1,1))

    def test_04_actual_rf_connection_cross_multiplied(self):
        # rf(1/t)=t(1+t²)/(2(1-t²)); common denominator 2t(1-t²).
        den = add(mon(0,1,2), mon(0,3,-2))
        for mask in (0,1):
            numerator = add(scalar(1-mask),mon(0,2,-1-mask))
            target = mul(den,mon(0,-1,Q(1,2))) if mask==0 else mon(0,2,-2)
            self.assertEqual(numerator,target)
            omitted_common = scale(add(scalar(1),mon(0,2)), -mask)
            self.assertNotEqual(numerator,omitted_common)
        # Independent K,K_x,rf symbols: check every coefficient for both endpoints.
        for r,s,ma,mb in product((0,1),repeat=4):
            w=r-s
            self.assertEqual(w+Q((1-2*r)-(1-2*s),2),0)
            self.assertEqual(-(1-2*r)*mb+(1-2*s)*ma,
                             -((1-2*r)*mb-(1-2*s)*ma))

    def test_actual_rf_tangent_on_artificial_Laurent_entries(self):
        # Cross multiply by L=2t(1-t²), so no rational simplifier is needed.
        L=add(mon(0,1,2),mon(0,3,-2))
        for r,s,ma,mb in product((0,1),repeat=4):
            w=r-s
            sig_r,sig_s=1-2*r,1-2*s
            for finite in (mon(0,-2),add(scalar(2),mon(0,3,5)),
                           add(mon(0,-1,3),mon(0,2,7))):
                pulled=pull(finite,(1,0,0,0))
                local=mul(mon(0,w),pulled)
                qa=add(scalar(1-ma),mon(0,2,-1-ma))
                qb=add(scalar(1-mb),mon(0,2,-1-mb))
                lhs=add(mul(L,deriv(local,0)),
                        mul(local,add(scale(qb,sig_r),scale(qa,-sig_s))))
                # L*rf(1/t)=t²(1+t²), independently from finite rf.
                Lrf=add(mon(0,2),mon(0,4))
                rhs=mul(mon(0,w-2,-1),add(
                    mul(L,pull(deriv(finite,0),(1,0,0,0))),
                    scale(mul(Lrf,pulled),sig_r*mb-sig_s*ma)))
                self.assertEqual(lhs,rhs)
                if r!=s:
                    missing_common=add(lhs,scale(mul(add(scalar(1),mon(0,2,-1)),local),2*w))
                    self.assertNotEqual(missing_common,rhs)

    def test_05_artificial_matrices_all_charts_both_pairs(self):
        masks = ((0,1,0,1),(1,0,1,0),(1,1,1,1))
        a,b,c = masks
        cores = [toy(i) for i in range(3)] # 01,12,20, in fixed positions
        for bits in product((0,1),repeat=4):
            local = [local_core(k,bits) for k in cores]
            for pair in ((0,1),(2,3)):
                i,j=pair
                finiteT = [tangent(cores[1],i,b,c),tangent(cores[0],j,a,b),
                           tangent(cores[1],j,b,c),tangent(cores[0],i,a,b)]
                localT = [tangent(local[1],i,b,c,bits[i]),tangent(local[0],j,a,b,bits[j]),
                          tangent(local[1],j,b,c,bits[j]),tangent(local[0],i,a,b,bits[i])]
                # Ordinary chain Jacobian before invariant-vector signs.
                for k,axis,finite in zip(localT,(i,j,j,i),finiteT):
                    for r,s in product((0,1),repeat=2):
                        exps=[(r-s)*e for e in bits]
                        exps[axis]-=2*bits[axis]
                        expected=scale(shift(pull(finite[r][s],bits),exps),-1 if bits[axis] else 1)
                        self.assertEqual(k[r][s],expected)
                ordinary=trace_term(local[2],*localT)
                finite=trace_term(cores[2],*finiteT)
                power=[-2*bits[k] if k in pair else 0 for k in range(4)]
                invariant=scale(ordinary,(-1)**(bits[i]+bits[j]))
                self.assertEqual(invariant,shift(pull(finite,bits),power))
                # Transported gerbe has the identical positive character factor.
                qfinite=mul(mon(i,-1,b[i]-a[i]),mon(j,-1,c[j]-b[j]))
                qlocal=mul(mon(i,-1,b[i]-a[i]),mon(j,-1,c[j]-b[j]))
                self.assertEqual(qlocal,shift(pull(qfinite,bits),power))
                Ffinite=add(scale(qfinite,Q(15,4)),scale(finite,Q(-1,4)))
                Flocal=add(scale(qlocal,Q(15,4)),scale(invariant,Q(-1,4)))
                self.assertEqual(Flocal,shift(pull(Ffinite,bits),power))

    def test_06_negative_endpoint_sign_order_controls(self):
        k=toy(1);a=(0,0,1,0);b=(0,1,0,1)
        right=tangent(k,0,a,b,True)
        self.assertNotEqual(right,tangent(k,0,a,b,True,'a'))
        self.assertNotEqual(right,tangent(k,0,a,b,True,'b'))
        bits=(1,0,0,0)
        ordinary=scale(shift(pull(k[0][1],bits),(-3,0,0,0)),-1)
        self.assertNotEqual(ordinary,scale(ordinary,-1))
        A,B,C=toy(0),toy(1),toy(2)
        self.assertNotEqual(tr(mm(C,mm(A,B))),tr(mm(C,mm(B,A))))
        self.assertNotEqual(mon(0,-1),mon(0,-1,-1)) # lost dlog or V sign
        self.assertNotEqual(scale(mon(0,-1),Q(15,4)),scale(mon(0,-1),Q(15,8)))

    def test_07_D_half_weight_and_chain_balance(self):
        for bits in product((0,1),repeat=4):
            k=toy(0);loc=local_core(k,bits)
            for r,s in product((0,1),repeat=2):
                d=[Q((1-2*r)-(1-2*s),2)*b for b in bits]
                self.assertEqual(shift(loc[r][s],d),pull(k[r][s],bits))
            for r in (0,1):
                self.assertEqual(Q(r)+Q(1-2*r,2),Q(1,2))
                self.assertEqual(-Q(r)-Q(1-2*r,2),Q(-1,2))
        expected=[(1,-2),(0,0),(1,-2),(-1,2),(0,0),(-1,2),(-1,2),(0,0),(-1,2),(1,-2),(0,0),(1,-2)]
        balance=producer.chain_splitting_balance()
        self.assertEqual([(x['homogeneous_degree'],x['nu_power']) for x in balance],expected)
        self.assertTrue(all(2*d+p==0 for d,p in expected))

    def test_08_C_legal_sections_owner_tags_and_reversal(self):
        owners=[[97,0,5,0,0],[97,1,0,5,8],[97,2,4,15,15]]
        for tag in range(16):
            bits=[(tag>>(3-i))&1 for i in range(4)]
            for pair in ((0,1),(2,3)):
                result=producer.bind_triple(owners,tag,pair)
                degrees=[0]*4
                for owner,record in zip(owners,result['C_owner_records']):
                    self.assertEqual(record['owner'],owner)
                    d=4 if owner[2]==5 else 5
                    for i in range(4):
                        m=(owner[3]>>i)&1
                        ellfinite=add(mon(i,3),mon(i,1,-1)) if m else scalar(1)
                        elllocal=add(scalar(1),mon(i,2,-1)) if m and bits[i] else mon(i,1) if bits[i] else ellfinite
                        self.assertEqual(elllocal,shift(pull(ellfinite,bits),[(1+2*m)*bits[i] if j==i else 0 for j in range(4)]))
                        degrees[i]+=14*d+(1+2*m if i in pair else 0)
                        orig=(owner[4]>>(3-i))&1
                        unit=('1' if orig else 't') if bits[i] else ('x' if orig else '1')
                        self.assertEqual(record['original_standard_units'][i],unit)
                target=[degrees[i]-(2 if i in pair else 0) for i in range(4)]
                self.assertEqual(result['P_target_multidegree'],target)
                self.assertEqual(result['owners'],owners)
                # Arbitrary formal bounded polynomial, including the top monomial.
                p=add(scalar(3),{tuple(target):Q(7)},mon(0,1,2))
                reversed_p=shift(pull(p,bits),[bits[i]*target[i] for i in range(4)])
                self.assertTrue(all(all(a>=0 for a in e) for e in reversed_p))
                if pair==(2,3):
                    ref=result['finite_candidate_reference']
                    self.assertTrue(ref['ordered_slot_positions_preserved'])
                    self.assertFalse(ref['direct_F12_root_on_target_owners'])
        self.assertEqual(producer.bind_triple(owners,15)['C_owner_records'][0]['original_standard_units'],['t']*4)

    def test_09_order_boundary_and_mutation_rejection(self):
        rotate=lambda m: ((m&3)<<2)|(m>>2)
        self.assertEqual([rotate(m) for m in (1,2,4)],[4,8,1])
        self.assertNotEqual([4,8,1],sorted([4,8,1]))
        owners=[[97,0,5,0,0],[97,1,0,5,8],[97,2,4,15,15]]
        result=producer.bind_triple(owners,8,(2,3))
        for mutate in ('Q','D','degree','order','tag','F'):
            bad=copy.deepcopy(result)
            if mutate=='Q': bad['frame']['coordinates'][0]['Q_local_cases']['mask0']='0'
            elif mutate=='D': bad['frame']['entries'][1]['physical_D_conjugation_tau_weight']=99
            elif mutate=='degree': bad['C_owner_records'][0]['carrier_equation_degree']=3
            elif mutate=='order': bad['source_finite_slot_map']['0']=owners[1]
            elif mutate=='tag': bad['C_owner_records'][0]['owner'][4]=8
            else: bad['frame']['F_transition']['character']=[-4]*4
            with self.assertRaises(ValueError): producer.validate_instance(bad)
        with self.assertRaises(ValueError): producer.bind_triple(list(reversed(owners)),8)

if __name__=='__main__':
    unittest.main()
