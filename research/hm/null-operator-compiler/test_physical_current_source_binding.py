#!/usr/bin/env python3
"""Abstract matrix identities and source-reference metadata only."""
import sys
if not __debug__:raise SystemExit(2)
import unittest
import tempfile
from pathlib import Path
import sympy as s
import physical_current_source_binding as b
import owned_scalar_denominator_binding as o
import compile_actual_scalar_differential_kernel as compiler

class Tests(unittest.TestCase):
    def test_hash_and_mutation(self):
        self.assertEqual(len(b.authenticate()['charts']),6)
        with tempfile.TemporaryDirectory() as t:
            p=Path(t)/'bad.json';p.write_text('{}')
            with self.assertRaises(ValueError):b.authenticate(p)
    def test_all_624_instances(self):
        out=compiler.build();count=0
        for seed in out['seeds']:
            for branch in seed['derivative_terms']:
                v=b.bind_instance(seed['seed'],branch);count+=1
                self.assertEqual(v['source_ast']['shape'],[2,2])
                self.assertEqual([z[1] for z in v['owners']],list(branch['current'][2]))
                self.assertEqual(v['id'],branch['id']+':current')
        self.assertEqual(count,624)
    def test_carrier_masks_tags(self):
        with self.assertRaises(ValueError):o.VertexLabel(0,0,-1,0,0)
        star=o.VertexLabel(0,0,5,1,8)
        self.assertEqual(b.block(star,'I').args[1],star.data())
        self.assertEqual(o.decode_legal_mask(1),(1,0,0,0))
        self.assertEqual(o.decode_standard_tag(1),(0,0,0,1))
        self.assertEqual(o.decode_standard_tag(8),(1,0,0,0))
    def test_repeated_carrier_distinct_owners(self):
        vs=tuple(o.VertexLabel(2,i,1,m,t) for i,(m,t) in enumerate(((0,3),(0,11),(1,15))))
        data=str(b.current('U',0,vs).data())
        for v in vs:self.assertIn(str(list(v.data())),data)
        with self.assertRaises(ValueError):b.current('L',0,(vs[0],vs[0],vs[2]))
    def test_moving_frame_and_transport(self):
        # Abstract polynomial matrices and integer-exponent frame controls ONLY.
        x=s.symbols('x',nonzero=True)
        A=s.Matrix([[1,x],[x,1+x*x]])
        B=s.Matrix([[1,x*x],[x+1,1+x*x*(x+1)]])
        for powers in ((1,2,3),(0,1,-1),(-2,0,1)):
            Da,Db,Dc=[s.diag(x**n,x**(-n)) for n in powers]
            Qa,Qb,Qc=[D.inv()*D.diff(x) for D in (Da,Db,Dc)]
            ga=Db*A*Da.inv();gb=Dc*B*Db.inv()
            Ta=A.diff(x)+Qb*A-A*Qa
            Tb=B.diff(x)+Qc*B-B*Qb
            expectedL=Da*A.inv()*Ta*Da.inv()
            expectedU=Da*A.inv()*B.inv()*Tb*A*Da.inv()
            for actual,expected in ((ga.inv()*ga.diff(x),expectedL),(ga.inv()*gb.inv()*gb.diff(x)*ga,expectedU)):
                self.assertEqual((actual-expected).applyfunc(s.simplify),s.zeros(2))
            if powers==(1,2,3):
                wrong=Da*A.inv()*A.diff(x)*Da.inv()
                self.assertNotEqual((expectedL-wrong).applyfunc(s.simplify),s.zeros(2))
    def test_emitted_ast_against_direct_derivative(self):
        x=s.symbols('x',nonzero=True)
        vs=tuple(o.VertexLabel(3,i,i,0,0) for i in range(3))
        H=[s.Matrix([[1,(i+1)*x],[0,1]]) for i in range(3)]
        G=[s.Matrix([[1,0],[(i+2)*x,1]]) for i in range(3)]
        D=[s.diag(x**(i+1),x**(-i-1)) for i in range(3)]
        def ev(n):
            op=n.op;a=n.args
            if op=='pinned_rational_block':
                owner=a[1][1]
                return H[owner].T.row_join(s.zeros(2,13)) if a[2]=='P' else G[owner].T.col_join(s.zeros(13,2))
            if op=='physical_diagonal_frame':return D[a[0][1]]
            if op=='logarithmic_diagonal_frame':
                d=D[a[0][1]];return d.inv()*d.diff(x)
            if op=='transpose':return ev(a[0]).T
            if op=='multiply':return ev(a[0])*ev(a[1])
            if op=='add':return ev(a[0])+ev(a[1])
            if op=='negate':return -ev(a[0])
            if op=='partial':return ev(a[0]).diff(x)
            if op=='adjugate_over_determinant':return ev(a[0]).inv()
            raise ValueError(op)
        A=D[1]*(G[1]*H[0])*D[0].inv()
        B=D[2]*(G[2]*H[1])*D[1].inv()
        expected={'L':A.inv()*A.diff(x),'U':A.inv()*B.inv()*B.diff(x)*A}
        for kind in ('L','U'):
            self.assertEqual((ev(b.current(kind,0,vs))-expected[kind]).applyfunc(s.simplify),s.zeros(2))
            self.assertEqual((D[0]*ev(b.normalized_current(kind,0,vs))*D[0].inv()-expected[kind]).applyfunc(s.simplify),s.zeros(2))
    def test_parity_and_single_adapter(self):
        n,a,z,c=s.symbols('n a z c',nonzero=True)
        D=s.diag(n,1/n);M=s.Matrix([[a,z],[c,-a]])
        P=D*M*D.inv()
        self.assertEqual(P[1,0],c/n**2)
        self.assertEqual(s.simplify(n**2*P[1,0]),c)
        self.assertEqual(P[0,1],n**2*z)
        self.assertEqual(P[0,0],a)
    def test_log_primitive(self):
        x=s.symbols('x',nonzero=True)
        rho=(x*x-1)/x
        ell=(x*x+1)/(2*x*(x*x-1))
        self.assertEqual(s.simplify(s.diff(rho,x)/(2*rho)-ell),0)
    def test_bad_shapes_and_indices(self):
        v=o.label(1,0)
        with self.assertRaises(ValueError):b.mul(b.block(v,'I'),b.block(v,'I'))
        with self.assertRaises(ValueError):b.partial(b.core(v,o.label(1,1)),True)
        with self.assertRaises(ValueError):b.block(v,'H')

if __name__=='__main__':unittest.main()
