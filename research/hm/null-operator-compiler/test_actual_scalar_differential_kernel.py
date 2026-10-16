#!/usr/bin/env python3
"""Independent abstract identities only. No physical polynomial inputs."""
import sys
if not __debug__:raise SystemExit(2)
import unittest
import sympy as s
import compile_actual_scalar_differential_kernel as c
from check_rectangular_jet_factorization import Term,Operator,polynomial,derive_row,admit_current_actual_metadata,Refused
x=s.symbols('x0:4')

def evaluate(expr,env):
    op=expr.op;a=expr.args
    if op=='constant':return s.Integer(a[0])
    if op=='owned_denominator_partial':return s.diff(s.Function('owned_den_'+str(a[0][0])+'_'+str(a[0][1]))(*x),x[a[1]])
    if op=='owned_denominator':return s.Function('owned_den_'+str(a[0][0])+'_'+str(a[0][1]))(*x)
    if op=='leaf':return env[a]
    if op=='add':return evaluate(a[0],env)+evaluate(a[1],env)
    if op=='multiply':return evaluate(a[0],env)*evaluate(a[1],env)
    if op=='inverse':return 1/evaluate(a[0],env)
    if op=='partial':return s.diff(evaluate(a[0],env),x[a[1]])
    raise ValueError(op)

class KernelTests(unittest.TestCase):
    def test_normal_order_arbitrary_functions(self):
        # Independent direct differentiation includes nonconstant c, alpha, beta, D.
        names=('C','D','c','alpha','beta');L={n:c.leaf(n,0) for n in names}
        env={L[n].args:s.Function(n)(*x) for n in names}
        P=s.Function('P')(*x)
        for d in range(4):
            t=c.normal_order((0,1),d,*(L[n] for n in names),(0,1),(0,))
            C,D,conv,alpha,beta=(env[L[n].args] for n in names)
            direct=C*(alpha*s.diff(conv*P/D,x[d])+beta*conv*P/D)
            lowered=evaluate(t.zero,env)*P+evaluate(t.first,env)*s.diff(P,x[d])
            self.assertEqual(s.expand(direct-lowered),0)
    def test_denominator_term_cannot_be_dropped(self):
        C,D,conv,alpha,beta=(c.leaf(n) for n in ('C','D','c','a','b'))
        t=c.normal_order((0,1),0,C,D,conv,alpha,beta,(0,1),())
        env={C.args:1,D.args:1+x[0],conv.args:1,alpha.args:1,beta.args:0}
        self.assertEqual(s.simplify(evaluate(t.zero,env)), -1/(x[0]+1)**2)
    def test_physical_frame_conjugation_and_four_terms(self):
        # Arbitrary symbols, all four E terms, and nontrivial nu. No source values.
        nu,h,*v=s.symbols('nu h v0:5',nonzero=True)
        mats=[s.Matrix([[s.Symbol(f'z{i}'),s.Symbol(f'u{i}')],
                        [s.Symbol(f'l{i}'),-s.Symbol(f'z{i}')]]) for i in range(4)]
        derivatives=s.symbols('pjka pjkb pijb pija')
        E=sum((sign*M*d/2 for sign,M,d in zip((1,-1,1,-1),mats,derivatives)),s.zeros(2))
        gauge=s.diag(nu,1/nu);bare=gauge.inv()*E*gauge
        a=2*v[1]*(v[1]**2*v[4]+v[0]*v[3]**2)/h
        b=2*v[0]*v[1]*(v[0]*v[1]**2+v[2]**2*v[3])/h
        expected=a*bare[1,0]+b*bare[0,0]
        compiled=sum(sign*(a*nu**2*M[1,0]+b*M[0,0])*d/2
                     for sign,M,d in zip((1,-1,1,-1),mats,derivatives))
        self.assertEqual(s.expand(expected-compiled),0)
    def test_all_seed_owner_sign_coverage(self):
        data=c.build();self.assertEqual(data['seed_count'],78);self.assertEqual(data['edge_branch_count'],624)
        self.assertEqual(len(data['unresolved_leaves']),78)
        self.assertEqual(data['resolved_edge_frame_instances'],624)
        self.assertEqual(data['schema'],'hm-actual-scalar-rational-kernel-v5')
        self.assertEqual(data['bound_outer_weight_source_definition_groups'],78)
        self.assertEqual(data['unresolved_regularization_Laurent_groups'],78)
        self.assertFalse(data['outer_weight_source_definition_is_executable_AST'])
        self.assertEqual({leaf['type'] for leaf in data['unresolved_leaves']},{'regularization_laurent'})
        for rec in data['seeds']:
            self.assertEqual([ref['owner'][1] for ref in rec['outer_weight_source_bindings']],list(rec['weighted_owners']))
            self.assertTrue(all('chart_cases' not in ref for ref in rec['outer_weight_source_bindings']))
            for branch in rec['derivative_terms']:
                typed=c.compile_term(rec,branch)
                self.assertEqual(typed.edge,tuple(branch['edge']))
            self.assertTrue(set(rec['kernel_owners'])<=set(rec['weighted_owners']))
            self.assertTrue(set(rec['deleted_prefix_owners'])<=set(rec['weighted_owners']))
            i,j,k=rec['tail']
            for offset,pair in ((0,(0,1)),(4,(2,3))):
                a,b=pair;ts=rec['derivative_terms'][offset:offset+4]
                self.assertEqual([t['edge'] for t in ts],[(j,k),(j,k),(i,j),(i,j)])
                self.assertEqual([t['coordinate'] for t in ts],[a,b,b,a])
                self.assertEqual([t['coefficient'][0] for t in ts],[1,-1,1,-1])
    def test_scalar_types_fail_closed(self):
        with self.assertRaises(ValueError):c.Scalar('leaf',('D',()),'infinity-unconverted')
        with self.assertRaises(ValueError):c.const(0.5)
        with self.assertRaises(ValueError):c.FirstOrder((0,1),0,c.const(0),c.const(1),(0,1),(2,))
    def test_full_formal_branch_four_terms(self):
        branch=c.selected_branch();self.assertEqual(len(branch['terms']),4)
        for t in branch['terms']:self.assertEqual(t['weighted_owners'],(0,1,2))
    def test_abstract_laurent_lowering_matches_independent_coefficients(self):
        # Abstract scalar C=x^4,D=x^2 => C*d(P/D)=x^2 P'-2xP.
        # kappa=3 selects a=2, where its coefficient cancels exactly.
        op=Operator(((4,), (4,)),(0,),(
            Term((0,1),(3,),(2,),0,polynomial([((),1)])),
            Term((0,1),(3,),(1,),None,polynomial([((),-2)]))))
        self.assertEqual(derive_row(op),{})
        for a in range(9):
            direct=s.expand(x[0]**4*s.diff(x[0]**a/x[0]**2,x[0]))
            self.assertEqual(direct.coeff(x[0],3),0)
    def test_selected_serialized_ast_against_direct_E(self):
        def decode(a):
            if a[0]=='leaf':return c.leaf(a[1],*a[2])
            if a[0]=='constant':return c.const(a[1])
            if a[0]=='owned_denominator_partial':return c.Scalar('owned_denominator_partial',(tuple(a[1]),a[2]))
            if a[0]=='owned_denominator':return c.Scalar('owned_denominator',(tuple(a[1]),))
            if a[0]=='partial':return decode(a[1]).diff(a[2])
            return c.Scalar(a[0],tuple(decode(b) for b in a[1:]))
        for index,t in enumerate(c.selected_branch()['terms']):
            A=decode(t['A']);B=decode(t['B']);env={}
            def visit(node):
                if node.op=='leaf':
                    name,owners=node.args
                    env[node.args]=s.Function('den'+str(owners))(*x) if name=='denominator' else s.Symbol(name+str(owners))
                for arg in node.args:
                    if isinstance(arg,c.Scalar):visit(arg)
            visit(A);visit(B)
            val=lambda name,*owners:env[(name,tuple(owners))]
            v=[val('v'+str(i),'a') for i in range(5)]
            h=val('h1','a');nu=val('nu','a')
            s10=2*v[1]*(v[1]**2*v[4]+v[0]*v[3]**2)/h*nu**2
            s00=2*v[0]*v[1]*(v[0]*v[1]**2+v[2]**2*v[3])/h
            edge,d,kind,coord,sign=c.branches((0,1,2))[index]
            kernel=sign*s.prod(val('outer_weight',i) for i in range(3))/2*(
                s10*val(kind+str(coord)+'_10_physical',0,1,2)+s00*val(kind+str(coord)+'_00_physical',0,1,2))
            P=s.Function('arbitrary_edge_numerator')(*x)
            D=s.prod(s.Function('owned_den_4_'+str(owner))(*x) for owner in edge)
            direct=kernel*s.diff(P/D,x[d])
            self.assertEqual(s.expand(direct-evaluate(A,env)*P-evaluate(B,env)*s.diff(P,x[d])),0)
    def test_actual_admission_stays_closed(self):
        data=c.build();data['actual_detector_authenticated']=True;data['unresolved_leaves']=[]
        with self.assertRaises(Refused):admit_current_actual_metadata(data,{})

if __name__=='__main__':unittest.main(verbosity=2)
