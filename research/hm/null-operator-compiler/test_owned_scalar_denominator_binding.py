#!/usr/bin/env python3
"""Syntactic actual-definition checks and abstract local identity tests, no physical evaluation."""
import sys
if not __debug__:raise SystemExit(2)
import unittest
import sympy as s
import owned_scalar_denominator_binding as b
import compile_actual_scalar_differential_kernel as c

def walk(t):
    yield t
    for arg in t.args:
        if isinstance(arg,b.Factor):yield from walk(arg)
        elif isinstance(arg,tuple):
            for a in arg:
                if isinstance(a,b.Factor):yield from walk(a)

class BindingTests(unittest.TestCase):
    def test_complete_labels_and_denominator_shape(self):
        label=b.label(7,2);D=b.denominator(label)
        choices=[n for n in walk(D) if n.op=='choice']
        self.assertEqual(len(choices),9)
        self.assertTrue(all(n.args[0][1]==label.data() for n in choices))
        carrier=choices[0]
        self.assertEqual(carrier.args[0][2],(5,0,1,2,3,4))
        self.assertEqual(len(carrier.args[1]),6)
        self.assertEqual([n.args[1] for n in walk(D) if n.op=='power'].count(5250),4)
        self.assertEqual([n.args[1] for n in walk(D) if n.op=='power'].count(14),1)
        self.assertEqual([n.args[0][2] for n in choices if n.args[0][0]=='legal_bit'],list(range(4)))
        self.assertEqual([n.args[0][2] for n in choices if n.args[0][0]=='standard_bit'],list(range(4)))
    def test_product_power_derivative_abstract(self):
        # This deliberately uses abstract monomials, never the actual D AST.
        x,y=s.symbols('x y');xs=(x,y)
        def ev(n):
            op=n.op;a=n.args
            if op=='integer':return s.Integer(a[0])
            if op=='coordinate':return xs[a[0]]
            if op=='add':return ev(a[0])+ev(a[1])
            if op=='multiply':return ev(a[0])*ev(a[1])
            if op=='power':return ev(a[0])**a[1]
            raise ValueError('physical choice evaluation forbidden')
        X=b.Factor('coordinate',(0,));Y=b.Factor('coordinate',(1,))
        for N in (0,1,2,14,5250):
            abstract=(X+Y).power(N)*(X*Y+b.integer(1))
            for i in range(2):self.assertEqual(s.simplify(ev(b.derivative(abstract,i))-s.diff(ev(abstract),xs[i])),0)
    def test_choice_derivative_keeps_full_discrete_owner(self):
        X=b.Factor('coordinate',(0,));key=('legal_bit',b.label(9,4).data(),2)
        choice=b.Factor('choice',(key,(b.integer(1),X.power(3))))
        d=b.derivative(choice,0)
        self.assertEqual(d.args[0],key)
        self.assertEqual(d.args[1],tuple(b.derivative(t,0) for t in choice.args[1]))
    def test_character_conversion_rejects_noncomplementary(self):
        for pair,other in (((0,1),(2,3)),((2,3),(0,1))):
            for i in pair:
                conv=b.character_conversion(pair,other,i)
                self.assertEqual((conv['c'],conv['alpha'],conv['beta']),(1,1,0))
                self.assertEqual(conv['input_character'][i],0)
        with self.assertRaises(ValueError):b.character_conversion((0,1),(0,1),0)
        with self.assertRaises(ValueError):b.character_conversion((0,1),(2,3),2)
    def test_inventory_is_bound_for_every_branch(self):
        data=c.build()
        self.assertEqual(len(data['unresolved_leaves']),78)
        self.assertEqual({t['type'] for t in data['unresolved_leaves']},{'regularization_laurent'})
        for seed in data['seeds']:
            for branch in seed['derivative_terms']:
                binding=branch['owned_edge_definition']
                self.assertEqual(binding['vertices'],[b.label(seed['seed'],o).data() for o in branch['edge']])
                self.assertEqual(binding['frame_conversion'],{'c':1,'alpha':1,'beta':0})
    def test_asymmetric_mask_and_standard_decoders(self):
        self.assertEqual(b.decode_legal_mask(1),(1,0,0,0))
        self.assertEqual(b.decode_standard_tag(1),(0,0,0,1))
        self.assertEqual(b.decode_legal_mask(8),(0,0,0,1))
        self.assertEqual(b.decode_standard_tag(8),(1,0,0,0))
        v=b.VertexLabel(4,0,1,1,8)
        for i in range(4):
            self.assertEqual(b.choice_index(('legal_bit',v.data(),i)),int(i==0))
            self.assertEqual(b.choice_index(('standard_bit',v.data(),i)),int(i==0))
        self.assertEqual(b.choice_index(('carrier',v.data(),(5,0,1,2,3,4))),2)
    def test_canonical_star_carrier_is_five_not_sort_key(self):
        star=b.VertexLabel(0,0,5,0,0);primary=b.VertexLabel(0,0,0,0,0)
        self.assertEqual(b.choice_index(('carrier',star.data(),(5,0,1,2,3,4))),0)
        self.assertEqual(b.choice_index(('carrier',primary.data(),(5,0,1,2,3,4))),1)
        with self.assertRaises(ValueError):b.VertexLabel(0,0,-1,0,0)
        self.assertEqual(b.definition()['carrier_domain'],[5,0,1,2,3,4])
    def test_elementary_structure_without_expansion(self):
        xs=tuple(b.Factor('coordinate',(i,)) for i in range(4))
        # Count the explicitly listed elementary symmetric summands, not source coefficients.
        for k,n in ((1,4),(2,6),(3,4),(4,1)):
            expr=b.elementary(xs,k)
            self.assertEqual(sum(t.op=='add' for t in walk(expr)),n)
        with self.assertRaises(ValueError):b.denominator((0,1))

if __name__=='__main__':unittest.main(verbosity=2)
