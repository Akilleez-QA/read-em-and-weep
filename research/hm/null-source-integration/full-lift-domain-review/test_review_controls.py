"""Independent abstract controls; no physical source, jets, or fibers.

Reviewed producer pin: 92b2a88edb6a199056bdee0225df98071a734d33.
Put the repository's research/codex-swarm/full-lift-domain on PYTHONPATH.
This file deliberately imports no staging directory or unpublished source.
"""
from collections import Counter,defaultdict
from fractions import Fraction as Q
import unittest
import lift as L

def artificial_owners(n):
    labels=((5,0,0),(0,0,1),(1,1,3),(2,2,7),(3,4,11),(4,8,15),(4,9,15))
    return tuple(L.I.FullOwner(99,('independent',j),*labels[j])for j in range(n))

class Independent(unittest.TestCase):
    def test_every_face_word_sign_and_prefix_occurrence(self):
        for s in range(4):
            os=artificial_owners(s+3);words=L.lift_terms(s,os)['terms']
            self.assertEqual(len(words),(1,4,20,120)[s])
            for word in words:
                current=list(os);expected=1;prefix=[];level=s
                ops=word['operator_word']
                for k in range(0,2*s,2):
                    hom,face=ops[k:k+2];owner=current[0]
                    self.assertEqual(hom['owner'],owner.data())
                    self.assertEqual(hom['input_internal_degree'],1-level)
                    expected*=(-1 if level==2 else 1)*(-1)**face['face_index']
                    prefix.append(owner.data())
                    removed=current.pop(face['face_index']);self.assertEqual(face['deleted_owner'],removed.data());level-=1
                self.assertEqual(word['coefficient'],expected)
                self.assertEqual(word['Rsharp_owners'],[o.data()for o in current])
                self.assertEqual(word['all_factor_owners'],prefix+[o.data()for o in current])
                self.assertEqual(ops[-1]['owner'],current[0].data())
                self.assertTrue(ops[-1]['transpose_row_input_once'])

    def test_seven_owner_top_boundary_clearance_and_tags(self):
        os=artificial_owners(7);tags=[o.standard_tag for o in os]
        out=L.outer_boundary_contract(os,3,tags)
        expected=tuple(sum(54*(4 if o.carrier==5 else 5)+29*(1+2*((o.legal_mask>>i)&1))+5251 for o in os)-5 for i in range(4))
        self.assertEqual(out['whole_numerator_homogeneous_degree'],expected)
        self.assertEqual(out['cech_degree'],6);self.assertEqual(out['internal_degree'],-3)
        self.assertTrue(out['standard_factors_are_target_units_not_partition_divisors'])
        self.assertTrue(out['index_checks_are_not_source_clearing_proof'])
        with self.assertRaises(ValueError):L.outer_boundary_contract(os,3,[t for t in tags if t!=7])
        with self.assertRaises(ValueError):L.lift_terms(3,os)

    def test_abstract_bottom_injectivity_and_constant_scalar_map(self):
        # Artificial gamma=(v0,v1)^T, ev=(v0,v1); W is a scalar.
        # Coefficients are keyed by formal monomial tuples, never physical data.
        w=Q(7,5);gamma=((Q(1),Q(2)),(Q(3),Q(-1)))
        ev=(Q(1),Q(1));x02=({(1,0):w},{(0,1):w})
        for row in gamma:
            x13={(1,0):row[0]*w,(0,1):row[1]*w}
            ans=defaultdict(Q)
            for e,c in x13.items():ans[e]+=c
            for k in range(2):
                for e,c in x02[k].items():ans[e]-=row[k]*c
            self.assertTrue(all(c==0 for c in ans.values()))
        # d_End W is not zero for W!=0: ev has a nonzero coefficient.
        self.assertNotEqual(x02[0][(1,0)],0)
        # The bad polynomial selector adds an extra v_k and fails.
        bad=defaultdict(Q,{(1,0):gamma[0][0]*w,(0,1):gamma[0][1]*w})
        bad[(2,0)]-=gamma[0][0]*w;bad[(0,2)]-=gamma[0][1]*w
        self.assertTrue(any(c for c in bad.values()))

    def test_original_frame_and_common_ledger_are_not_admission(self):
        for s in range(4):
            f=L.original_frame(s)
            self.assertEqual(f['tau_power'],-s-2);self.assertEqual(f['full_sign_deck_product_removed_count'],1)
            self.assertEqual(f['scalar_L_applied_after_this_conversion'],s==2)
        ledger=L.domain_ledger();self.assertFalse(ledger['whole_standard_extension_from_ledger_alone'])
        self.assertEqual(ledger['common_outer_partition'],{'carrier':54,'legal':29,'standard_unit_order':5251})
        app=L.ActualFullLiftApplication()
        for method in (app.coefficient,app.factor_terms,app.owners):
            with self.assertRaises(L.I.PhysicalAdmissionMissing):method(None)

    def test_prism_weights_cancel_inserted_not_suffix_divisors(self):
        # An abstract term 1/(H_insert H_suffix), with weight H_insert,
        # still has a suffix pole. This is a formal owned-factor control.
        denominator=Counter({'H_insert':1,'H_suffix':1})
        weight=Counter({'H_insert':1})
        remaining=denominator-weight
        self.assertEqual(remaining,Counter({'H_suffix':1}))
        self.assertNotEqual(remaining,Counter())
        suffix_clearing=Counter({'H_suffix':1})
        self.assertEqual(remaining-suffix_clearing,Counter())
        # Projection differs: all sampled owners have their matching weight.
        self.assertEqual(denominator-Counter({'H_insert':1,'H_suffix':1}),Counter())

    def test_current_projection_and_prism_scope_metadata(self):
        for n,s,boundary in ((5,2,False),(7,3,True)):
            os=artificial_owners(n)
            callback=L.outer_boundary_contract if boundary else L.outer_owner_contract
            out=callback(os,s,[o.standard_tag for o in os])
            self.assertTrue(out['fully_weighted_Pi_out_value_extends_full_standard_target'])
            self.assertFalse(out['uncleared_prism_full_standard_extension_claimed'])
            self.assertEqual(out['prism_full_standard_extension_scope'],'appropriately cleared WHOLE coefficient with retained owned suffix divisors')
            self.assertTrue(out['index_checks_are_not_source_clearing_proof'])
            self.assertFalse(out['physical_execution_authorized'])

if __name__=='__main__':unittest.main()
