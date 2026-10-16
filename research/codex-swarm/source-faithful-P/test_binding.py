"""PB01 bounded artificial and metadata controls; no physical coefficients."""
import copy
import importlib
import unittest
from fractions import Fraction as F
import p_binding as pb

Z=(0,0)
ONE={Z:F(1)}
X={(1,0):F(1)}
Y={(0,1):F(1)}

def add(*ps):
    out={}
    for p in ps:
        for e,c in p.items():out[e]=out.get(e,F(0))+c
    return {e:c for e,c in out.items()if c}
def scale(p,c):return {e:v*c for e,v in p.items()if v*c}
def mul(p,q):
    out={}
    for a,c in p.items():
        for b,d in q.items():
            e=tuple(x+y for x,y in zip(a,b));out[e]=out.get(e,F(0))+c*d
    return {e:c for e,c in out.items()if c}
def derivative(p,i):
    out={}
    for e,c in p.items():
        if e[i]:
            k=list(e);k[i]-=1;out[tuple(k)]=c*e[i]
    return out
def transpose(m):return [list(r)for r in zip(*m)]
def mm(a,b):return [[add(*(mul(a[i][k],b[k][j])for k in range(2)))for j in range(2)]for i in range(2)]
def md(a,i):return [[derivative(p,i)for p in r]for r in a]
def ma(a,b):return [[add(a[i][j],scale(b[i][j],-1))for j in range(2)]for i in range(2)]
def mat(entries):return [[entries[2*i+j]for j in range(2)]for i in range(2)]
def owners():
    return tuple(pb.FullOwner(12,('source',i),i,0,i)for i in range(3))

def toy_catalog():
    # Source entries are small artificial polynomials in formal e1/e2.
    # All remaining 13 rows/columns are zero, so direct matrices are 2x2.
    v1=add(X,Y);v2=mul(X,Y)
    primitives=[(mat([ONE,v1,{},ONE]),mat([ONE,{},v2,ONE])),
                (mat([ONE,{},v2,ONE]),mat([ONE,v1,{},ONE])),
                (mat([v1,ONE,{},ONE]),mat([ONE,v2,ONE,{}]))]
    def literal(p):
        if p=={}:return []
        if p==ONE:return [['0,0,0,0',1]]
        if p==v1:return [['1,0,0,0',1]]
        if p==v2:return [['0,1,0,0',1]]
        raise AssertionError('toy literal')
    charts=[]
    for I,P in primitives:
        i=[[literal(I[r][s])if r<2 else []for s in range(2)]for r in range(15)]
        p=[[literal(P[r][s])if s<2 else []for s in range(15)]for r in range(2)]
        charts.append({'I':i,'P':p})
    return charts,primitives


class BindingControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.binding=pb.ActualPBinding()

    def test_both_pairs_exact_owner_degree_and_source_order(self):
        oo=owners()
        for pair in [(0,1),(2,3)]:
            c=self.binding.describe(oo,pair)
            self.assertEqual(c['P_homogeneous_multidegree'],[211 if i in pair else 210 for i in range(4)])
            self.assertEqual(c['program']['cleared_P'],152)
            self.assertEqual(len(c['ordered_operation_induction']),153)
            self.assertFalse(c['source_order']['matrix_product_reordered'])
            self.assertFalse(c['physical_source_evaluated'])
        aux=(pb.FullOwner(30,'aux',5,15,15),pb.FullOwner(30,'a',1,9,9),pb.FullOwner(30,'b',2,11,13))
        self.assertEqual(self.binding.degree_upper(aux),(203,201,196,196))
        bridge=self.binding.describe(aux)['primitive_bridges'][5]
        self.assertEqual(bridge['assigned_H_degree'],4)
        self.assertIn('v0',bridge['homogeneous_H'])
        self.assertEqual(bridge['homogeneous_H_squared_primitive'],'-v3*v4*hom_(6+w)(stored_num)')

    def test_strict_owner_pair_and_constructor_inputs(self):
        oo=owners()
        for bad in [oo[::-1],(oo[0],oo[0],oo[2]),
                    (oo[0],pb.FullOwner(30,'bad',1,0,1),oo[2]),
                    (oo[0],pb.FullOwner(12,oo[0].occurrence,1,0,1),oo[2]),[o.data()for o in oo]]:
            with self.assertRaises(ValueError):self.binding.describe(bad)
        for pair in [(1,0),(True,1),(0,2)]:
            with self.assertRaises(ValueError):self.binding.describe(oo,pair)
        with self.assertRaises(TypeError):pb.ActualPBinding(catalog=lambda:True)

    def test_shape_order_and_elementary_derivative_guards(self):
        p=self.binding.symbolic_program_definition()
        a=copy.deepcopy(p['dag']);a[0]=['ordered_product',0]
        with self.assertRaises(ValueError):pb.audit_shapes(a,152)
        a=copy.deepcopy(p['dag']);a[0]=['catalog_cleared_primitive',True,'P']
        with self.assertRaises(ValueError):pb.audit_shapes(a,152)
        a=copy.deepcopy(p['dag']);a[0]=['unknown_physical_leaf']
        with self.assertRaises(ValueError):pb.audit_shapes(a,152)
        self.assertTrue(any('AFTER' in r['denotation_rule']for r in pb.audit_shapes(p['dag'],152)))

    def test_exact_INS_pair_rename_no_owner_permutation(self):
        mod=importlib.import_module('source_program')
        a=self.binding.symbolic_program_definition()['dag']
        b=self.binding.symbolic_program_definition((2,3))['dag']
        self.assertEqual(b,mod.pair_nodes(a,(2,3)))
        self.assertEqual(pb.rename_pair(b,(2,3)),a)
        for x,y in zip(a,b):
            if x[0]=='catalog_cleared_primitive':self.assertEqual(x,y)

    def test_artificial153_node_lowering_against_direct_matrices(self):
        pc=importlib.import_module('polynomial_coefficients')
        charts,prim=toy_catalog()
        cat=pc.Catalog('synthetic',charts,synthetic_H=[{(0,0,0,0):1}for _ in range(6)])
        # P/I primitive signs occur in pairs in K and cancel.
        K=lambda a,b:transpose(mm(prim[a][1],prim[b][0]))
        A=K(0,1);B=K(1,2)
        mixed=ma(mm(md(B,0),md(A,1)),mm(md(B,1),md(A,0)))
        tr=mm(K(2,0),mixed)
        expected=scale(add(tr[0][0],tr[1][1]),F(-1,4))
        self.assertTrue(expected)
        definition=self.binding.symbolic_program_definition()
        prog=pc.ClearedSourceProgram(definition['dag'],152,cat,owners())
        # Compare independent rational bivariate coefficients, including zero.
        selected=sorted(expected)[:6]+[(0,0),(6,6)]
        for i,j in selected:
            self.assertEqual(prog.coefficient((i,j,0,0)),expected.get((i,j),F(0)))

    def test_metadata_copies_do_not_mutate_source_and_physical_always_refuses(self):
        p=self.binding.describe(owners());p['program']['dag'][0]=['fake']
        p['physical_execution_admitted']=True
        self.assertNotEqual(self.binding.describe(owners())['program']['dag'][0],['fake'])
        for method in [self.binding.coefficient,self.binding.alternating_coefficient]:
            for args in [(),(owners(),(-10**9,0,0,0)),('garbage',)]:
                with self.assertRaises(pb.PhysicalAdmissionMissing):method(*args)

    def test_malformed_source_bytes_reject_before_catalog(self):
        pins,raw=pb._authenticate(pb.HERE.parents[2])
        def bad(rev,path):
            b=raw[(rev,path)]
            return b+b' ' if path==pb.MODEL else b
        with self.assertRaisesRegex(ValueError,'source bytes drift'):
            pb._authenticate(pb.HERE.parents[2],reader=bad)
        # Authenticated references are returned by copy, never caller authority.
        pins=self.binding.source_pins();pins['sources'][0]['sha256']='0'*64
        self.assertNotEqual(self.binding.source_pins()['sources'][0]['sha256'],'0'*64)


if __name__=='__main__':unittest.main()
