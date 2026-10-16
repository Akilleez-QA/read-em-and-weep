"""Only tiny artificial exact complexes/cochains; no actual HM matrices."""
from fractions import Fraction as Q
import itertools
import unittest
import lift as L

GRADES=(0,1,1,1,1,2,2,3)

def matrix(rows,cols,entries):
    return tuple(tuple(Q(entries.get((i,j),0))for j in range(cols))for i in range(rows))

def fixtures():
    d=matrix(8,8,{(1,0):1,(5,4):1,(7,6):1});h=L.transpose(d)
    inc=matrix(8,2,{(2,0):1,(3,1):1});proj=L.transpose(inc);result={}
    for v in range(7):
        n=matrix(8,8,{(i,j):((v+1)*(i+2)+(j+1))%3 for i in range(8)for j in range(8)if GRADES[i]==GRADES[j]-1})
        C=L.add(L.identity(8),L.add(L.times(d,n),L.times(n,d)));Ci=L.inverse(C)
        result[v]=L.TinyContraction(d,L.times(C,inc),L.times(proj,Ci),L.times(L.times(C,h),Ci),GRADES)
    def edge(a,b):return matrix(2,2,{(0,0):a+b,(0,1):a*b+1,(1,0):a-b,(1,1):a+2*b})
    def residual(v):
        a,b,c=v
        return L.add(L.add(edge(b,c),L.scale(-1,edge(a,c))),edge(a,b))
    return result,residual

def owners(n):
    return tuple(L.I.FullOwner(12,('toy-outer',j),c,0,t)for j,(c,t)in enumerate(zip((5,0,1,2,3,4)[:n],(0,1,3,7,11,15)[:n])))

class Controls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.local,residual=fixtures();cls.R=staticmethod(residual);cls.P=L.TinyLift(cls.local,residual)
    def test_local_End_contraction_identity_all_tiny_matrix_units(self):
        c=self.local[3]
        for i in range(8):
            for j in range(8):
                f=matrix(8,8,{(i,j):1});r=GRADES[i]-GRADES[j]
                left=L.add(c.differential(c.homotopy(f,r),r-1),c.homotopy(c.differential(f,r),r+1))
                self.assertEqual(left,L.add(f,L.scale(-1,L.times(L.times(c.E,f),c.E))))
    def test_source_closed_and_same_induced_cohomology_frames(self):
        for a,b in itertools.product(range(7),repeat=2):self.assertEqual(L.times(self.local[a].proj,self.local[b].inc),L.identity(2))
        for v in itertools.combinations(range(7),4):
            out=L.zero(2)
            for j in range(4):out=L.add(out,L.scale((-1)**j,self.R(v[:j]+v[j+1:])))
            self.assertEqual(out,L.zero(2))
    def test_full_signed_lift_all_five_equations_and_nonzero_J3(self):
        nonzero=[False]*4
        for s in range(4):
            for v in itertools.combinations(range(7),3+s):
                F=self.P.component(s,v);nonzero[s]|=F!=L.zero(8)
                d=self.local[v[0]].differential(F,-s)
                self.assertEqual(d,L.zero(8)if s==0 else L.scale(L.SIGNS[s],self.P.delta(s-1,v)))
        self.assertEqual(self.P.delta(3,tuple(range(7))),L.zero(8))
        self.assertTrue(all(nonzero),nonzero)
    def test_wrong_middle_sign_fails_and_bottom_d_is_injective(self):
        found=False
        for v in itertools.combinations(range(7),5):
            f=self.P.component(2,v);delta=self.P.delta(1,v)
            if delta!=L.zero(8):
                self.assertNotEqual(self.local[v[0]].differential(L.scale(-1,f),-2),L.scale(-1,delta));found=True;break
        self.assertTrue(found)
        bottom=matrix(8,8,{(0,7):1})
        self.assertNotEqual(self.local[0].differential(bottom,-3),L.zero(8))
        self.assertEqual(self.local[0].homotopy(bottom,-3),L.zero(8))
    def test_face_words_and_deleted_prefix_ownership_retained(self):
        for s,count in enumerate((1,4,20,120)):
            p=L.lift_terms(s,owners(3+s));self.assertEqual(len(p['terms']),count)
            self.assertEqual(p['bidegree'],(2+s,-s))
        p=L.lift_terms(3,owners(6));first=p['terms'][0]
        self.assertEqual(len(first['retained_prefix_owners']),3)
        self.assertEqual(first['retained_prefix_owners'][0],owners(6)[0].data())
        self.assertNotIn(owners(6)[0].data(),first['Rsharp_owners'])
        self.assertIn(owners(6)[0].data(),first['all_factor_owners'])
        self.assertFalse(p['physical_execution_authorized'])
    def test_ledger_is_not_a_standard_extension_certificate(self):
        x=L.domain_ledger();self.assertEqual([(r['carrier'],r['legal'])for r in x['components']],list(L.BOUNDS))
        self.assertFalse(x['whole_standard_extension_from_ledger_alone'])
    def test_strict_owner_and_physical_gates(self):
        with self.assertRaises(ValueError):L.lift_terms(True,owners(4))
        with self.assertRaises(ValueError):L.lift_terms(1,tuple(reversed(owners(4))))
        a=owners(4)
        with self.assertRaises(ValueError):L.lift_terms(1,(a[0],L.I.FullOwner(13,'bad',0,0,1),*a[2:]))
        with self.assertRaises(L.I.PhysicalAdmissionMissing):L.actual_coefficient(a,(0,0,0,0))
    def test_original_frame_deck_conversion_precedes_scalar(self):
        for s in range(4):
            f=L.original_frame(s);self.assertEqual(f['tau_power'],-s-2)
            self.assertEqual(f['full_sign_deck_product_removed_count'],1)
            self.assertEqual(f['scalar_L_applied_after_this_conversion'],s==2)
        self.assertEqual(L.original_frame(2)['tau_power'],-4)
    def test_outer_degree_owner_units_and_no_unowned_tag(self):
        a=owners(5);d=L.outer_owner_contract(a,2,[o.standard_tag for o in a])
        independent=tuple(sum(54*(4 if o.carrier==5 else 5)+29*(1+2*((o.legal_mask>>i)&1))+5251 for o in a)-4 for i in range(4))
        self.assertEqual(d['whole_numerator_homogeneous_degree'],independent)
        with self.assertRaises(ValueError):L.outer_owner_contract(a,2,[o.standard_tag for o in a[1:]])
        with self.assertRaises(ValueError):L.outer_owner_contract(a,2,[False,*[o.standard_tag for o in a[1:]]])
    def test_canonical_actual_factory_does_not_accept_closure_strings(self):
        app=L.ActualFullLiftApplication()
        for f in(app.coefficient,app.factor_terms,app.owners):
            with self.assertRaises(L.I.PhysicalAdmissionMissing):f('closed',True)
        with self.assertRaises(TypeError):L.ActualFullLiftApplication(closure=True)
        with self.assertRaises(ValueError):L.ActualFullLiftApplication('/tmp/arbitrary-model')
    def test_top_boundary_seven_owner_domain_is_not_a_six_owner_box(self):
        a=owners(6)+(L.I.FullOwner(12,'seventh-toy-owner',4,1,15),)
        d=L.outer_boundary_contract(a,3,[o.standard_tag for o in a])
        self.assertEqual(len(d['factors']),7);self.assertEqual(d['cech_degree'],6)
        self.assertEqual(d['internal_degree'],-3);self.assertEqual(d['source_bundle_degree'],[-5]*4)
        with self.assertRaises(ValueError):L.lift_terms(3,a)

if __name__=='__main__':unittest.main()
