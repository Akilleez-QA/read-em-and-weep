"""Producer controls using exact abstract split complexes, never physical data."""
import copy
from fractions import Fraction as Q
import itertools
import json
from pathlib import Path
import unittest
import compiler as C


def zero(r,c):return [[Q(0)for _ in range(c)]for _ in range(r)]
def eye(n):return [[Q(i==j)for j in range(n)]for i in range(n)]
def add(A,B):return [[x+y for x,y in zip(a,b)]for a,b in zip(A,B)]
def scale(A,c):return [[x*c for x in row]for row in A]
def mul(A,B):return [[sum(a[k]*B[k][j]for k in range(len(B)))for j in range(len(B[0]))]for a in A]
def transpose(A):return list(map(list,zip(*A)))


def toy_leaf(node):
    if node['name']=='toy_R':return [[Q(2),Q(3)],[Q(5),Q(7)]]
    t=Q(node['owner']+1);s=t*t
    table={'I_phys':[[t,0],[1,0],[0,1],[0,0]],
           'P_phys':[[0,1,0,-s],[0,0,1,0]],'H0':[[1,-t,0,0]],
           'H1':[[t*s,0],[s,0],[0,0],[1,0]],'eta':[[0],[1]]}
    return [[Q(x)for x in row]for row in table[node['name']]]


def evaluate(c,n,leaf=toy_leaf,cache=None):
    cache={}if cache is None else cache
    if n in cache:return cache[n]
    rec=c.nodes[n];op=rec['op'];r,s=rec['shape']
    if op=='zero':out=zero(r,s)
    elif op=='identity':out=eye(r)
    elif op=='leaf':out=leaf(rec)
    else:
        kids=[evaluate(c,k,leaf,cache)for k in rec['children']]
        if op=='add':
            out=zero(r,s)
            for v in kids:out=add(out,v)
        elif op=='rational_scale':out=scale(kids[0],Q(*rec['coefficient']))
        elif op=='matrix_product':
            out=kids[0]
            for v in kids[1:]:out=mul(out,v)
        elif op=='transpose':out=transpose(kids[0])
        elif op=='trace':out=[[sum(kids[0][j][j]for j in range(len(kids[0])))]]
        elif op=='scalar_times_matrix':out=scale(kids[1],kids[0][0][0])
        elif op=='entry':a,b=rec['entry'];out=[[kids[0][a][b]]]
        else:raise ValueError('no physical/solver/cover/coefficient evaluator')
    if(len(out),len(out[0]))!=(r,s):raise ValueError('toy evaluator shape')
    cache[n]=out;return out


def eval_blocks(c,blocks):return {key:evaluate(c,n)for key,n in blocks.items()}
def merge(out,key,value):out[key]=add(out[key],value)if key in out else value

def end_d(F,r):
    d=[[[1],[0],[0],[0]],[[0,0,0,1],[0,0,0,0]],[[0,1]]]
    out={}
    for(u,v),matrix in F.items():
        if v<3:merge(out,(u,v+1),mul(d[v],matrix))
        if u>0:merge(out,(u-1,v),scale(mul(matrix,d[u-1]),-(-1 if r%2 else 1)))
    return out


def sum_blocks(*items):
    out={}
    for sign,F in items:
        for key,v in F.items():merge(out,key,scale(v,sign))
    return out


def iszero(F):return not any(x for matrix in F.values()for row in matrix for x in row)


class Controls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.template=C.compile_template();_,cls.model,cls.shared,_=C.authenticate();cls.g=C.gamma_coefficients(cls.model)
    def test_all_constant_chain_rows_and_wrong_sign(self):
        self.assertEqual(C.check_chain_rows(self.g),1500)
        terms=C.scalar_terms(self.g,5,0);terms[0]['coefficient']=-1
        self.assertTrue(C.row_bottom_coefficients(self.g,terms))
    def test_staircases_all24_with_correct_bits(self):
        records=C.staircase_records();self.assertEqual(len(records),24)
        self.assertEqual(records[0]['standard_tags'],[0,8,12,14,15])
        self.assertEqual(sum(r['orientation']for r in records),0)
        self.assertEqual(len({tuple(r['standard_tags'])for r in records}),24)
    def test_full_source_terms_gerbe_and_top(self):
        t=self.template
        self.assertEqual(t['Rsharp_components'],['baseline','Fk12','Fk34','E12','E34'])
        for rec in t['source_residual_components']:
            self.assertEqual(set(rec['components']),set(t['Rsharp_components']))
            self.assertEqual(len(rec['baseline']['gerbe_terms']),3)
            self.assertEqual(len(rec['baseline']['kinetic_terms']),7)
            self.assertFalse(rec['baseline']['legacy_scalar_correction'])
        self.assertEqual([b['block']for b in t['lift_components']['J2']],[[2,0],[3,1]])
        self.assertEqual([b['block']for b in t['lift_components']['J3']],[[3,0]])
    def test_compiled_weighted_tests_not_old_selectors(self):
        t=self.template
        self.assertEqual(t['counts']['weighted_tests'],32);self.assertEqual(len(t['scalar_templates']),20)
        self.assertEqual(sum(len(r['weighted_request']['terms'])for r in t['requests']),127)
        self.assertEqual(len({(r['weighted_request']['scalar_map']['i'],r['weighted_request']['scalar_map']['b'],tuple(x['laurent_exponents']))for r in t['requests']for x in r['weighted_request']['terms']}),121)
        self.assertFalse(t['outer_transport']['legacy_78_seed_table_used'])
        self.assertFalse(t['outer_transport']['scalar_merger_used'])
        for n in t['nodes']:
            if n['op']=='differentiate_combined_solver':self.assertFalse(n['actual_source_clearing_witness'])
    def test_noncommutative_product_derivative(self):
        c=C.Circuit();a=c.leaf('A',(2,2));b=c.leaf('B',(2,2));out=c.D(c.mul(a,b),0)
        rec=c.nodes[out];self.assertEqual(rec['op'],'add')
        terms=[c.nodes[x]for x in rec['children']]
        self.assertEqual([x['op']for x in terms],['matrix_product','matrix_product'])
        self.assertEqual(terms[0]['children'][1],b);self.assertEqual(terms[1]['children'][0],a)
    def test_source_derivatives_keep_moving_frames(self):
        jets=[n for n in self.template['nodes']if n['op']=='physical_jet']
        self.assertTrue(jets);self.assertTrue(all(n['frames_differentiated']for n in jets))
        self.assertTrue(all(n['directions']==sorted(n['directions'])for n in jets))
    def test_complete_solver_derivative_rejects_pair_direction(self):
        c=C.Circuit();s=C.Source(c).T((0,1),0,1)
        with self.assertRaises(ValueError):c.D(s,0)
        node=c.nodes[c.D(s,2)];self.assertEqual(node['op'],'differentiate_combined_solver')
        self.assertIn('whole combined',node['rule'])
        rec=c.nodes[s];self.assertEqual([c.nodes[n]['op']for n in rec['children']],['N14_Hrho','N14_R_Kcov_Pi','N14_R_A_h_S_Pi'])
        prism=c.nodes[rec['children'][0]];self.assertEqual([c.nodes[n]['sign']for n in prism['children']],[1,-1])
    def test_owner_sort_keeps_all_occurrences(self):
        tags=[0,8,12,14,15];owners=[[0,j,1,0,t]for j,t in enumerate(tags)]
        out=C.bind_outer_assignment(tags,owners);self.assertFalse(out['zero'])
        self.assertEqual(out['partition_owners'],owners);self.assertFalse(out['rebuild_ordered_source'])
        bad=copy.deepcopy(owners);bad[1][1]=0
        with self.assertRaises(ValueError):C.bind_outer_assignment(tags,bad)
    def test_common_repetition_not_carrier_repetition(self):
        tags=[0,8,12,14,15];owners=[[0,j,1,0,t]for j,t in enumerate(tags)]
        self.assertFalse(C.bind_outer_assignment(tags,owners)['zero'])
        tags=[0,0,12,14,15];owners[1][4]=0
        self.assertTrue(C.bind_outer_assignment(tags,owners)['zero'])
    def test_shape_and_internal_degree_controls(self):
        c=C.Circuit();a=c.leaf('A',(2,3));b=c.leaf('B',(2,2))
        with self.assertRaises(ValueError):c.mul(a,b)
        with self.assertRaises(ValueError):c.entry(a,2,0)
        L=C.Lift(c,lambda t:b,self.shared.closed_lift_schema())
        with self.assertRaises(ValueError):L.homotopy({(0,1):a},0,0)
    def test_exact_abstract_split_lift_closure_and_J2_sign(self):
        c=C.Circuit();R=lambda t:c.leaf('toy_R',(2,2),owners=list(t))
        lift=C.Lift(c,R,self.shared.closed_lift_schema(),dims=(1,4,2,1))
        F=lambda stage,t:eval_blocks(c,lift.at(stage,t))
        self.assertTrue(iszero(end_d(F(0,(0,1,2)),0)))
        nonzero_J2=False
        for stage in range(4):
            t=tuple(range(stage+4));delta={}
            for j in range(len(t)):
                for key,v in F(stage,t[:j]+t[j+1:]).items():merge(delta,key,scale(v,(-1)**j))
            if stage<3:
                nextF=F(stage+1,t)
                self.assertTrue(iszero(sum_blocks((1,delta),((-1 if stage%2==0 else 1),end_d(nextF,-stage-1)))))
                if stage==1:
                    nonzero_J2=not iszero(nextF)
                    self.assertFalse(iszero(sum_blocks((1,delta),(-1,end_d(nextF,-2)))))
            else:self.assertTrue(iszero(delta))
        self.assertTrue(nonzero_J2)
    def test_boolean_standard_tags_and_selectors_rejected(self):
        tags=[0,8,12,14,15];owners=[[0,j,1,0,t]for j,t in enumerate(tags)]
        tags[0]=False
        with self.assertRaises(ValueError):C.bind_outer_assignment(tags,owners)
        for field,position in [('entry',0),('block',0),('coefficient',None)]:
            terms=C.scalar_terms(self.g,5,0)
            if position is None:terms[0][field]=True
            else:terms[0][field][position]=False
            with self.assertRaises(ValueError):C.row_bottom_coefficients(self.g,terms)
    def test_no_realization_gate_can_be_forged(self):
        bad=copy.deepcopy(self.template);bad['gates']['physical_source_evaluated']=True
        with self.assertRaises(ValueError):C.validate_template(bad)
        bad=copy.deepcopy(self.template);bad['lift_components'].pop('J3')
        with self.assertRaises(ValueError):C.validate_template(bad)

if __name__=='__main__':unittest.main()
