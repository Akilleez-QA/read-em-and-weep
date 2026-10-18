"""Independent QB01 review: metadata only for actual inputs; artificial N1/N2 arithmetic."""
import hashlib,json,unittest,os
from pathlib import Path
from unittest.mock import patch
import q_binding as B
ZERO=(0,0,0,0)
PINROOT=Path(os.environ['QB_REVIEW_PIN_ROOT']) if 'QB_REVIEW_PIN_ROOT' in os.environ else None
ORIGINAL_GIT=B.QH.subprocess.check_output
def pinned_git(args,**kwargs):
    if PINROOT is None:return ORIGINAL_GIT(args,**kwargs)
    if args[:2]!=['git','show']:raise AssertionError('unexpected transport')
    commit,path=args[2].split(':',1)
    if commit!='10810ee877fdaf291399198ad60d7dd0c316a42d':raise AssertionError('unexpected pin')
    return (PINROOT/('/'.join(path.split('/')[-2:]))).read_bytes()
def prohibited(*args,**kwargs):raise AssertionError('physical coefficient operation attempted')
class Independent(unittest.TestCase):
    def test_canonical_repository_guard(self):
        canonical=Path(B.__file__).resolve().parents[3]
        with patch.object(B,'authenticate',return_value={'review_spy':True}) as auth:
            for alternate in [canonical.parent/'different-repository',canonical/'child']:
                with self.assertRaisesRegex(ValueError,'only canonical workspace'):
                    B.ActualQBinding(alternate)
            auth.assert_not_called()
            for accepted in [None,canonical,str(canonical),canonical/'child'/'..']:
                self.assertEqual(B.ActualQBinding(accepted).pins,{'review_spy':True})
            self.assertEqual(auth.call_count,4)
    def test_metadata_all_charts_pairs_full_owners(self):
        with patch.object(B.QH.subprocess,'check_output',pinned_git),patch.object(B.QH.FiniteRing,'coefficient',prohibited),patch.object(B.QH.FiniteRing,'_coefficient',prohibited):
            api=B.ActualQBinding()
            for tag in range(16):
                for pair in [(0,1),(2,3)]:
                    owner=B.I.FullOwner(30,('audit',tag,pair),tag%6,(tag*7)%16,tag)
                    d=api.describe(owner,pair)
                    degree=tuple(14*(4 if owner.carrier==5 else 5)+(1+2*((owner.legal_mask>>i)&1)if i in pair else 0)for i in range(4))
                    bits=tuple((tag>>(3-i))&1 for i in range(4))
                    self.assertEqual(d['owned_degree'],degree)
                    self.assertEqual(d['finite_frame_shift'],tuple(-degree[i]if bits[i]else 0 for i in range(4)))
                    self.assertEqual(d['owner'],owner.data())
                    self.assertEqual(d['parameters'],{'N':14,'M':27,'T':135,'L':134*(sum(bits)+1)+1,'s':sum(bits),'legal_power':1})
                    self.assertEqual(d['C_ledger'],({'owner':owner.data(),'kind':'H','axis':None,'power':14},)+tuple({'owner':owner.data(),'kind':'ell','axis':i,'power':1}for i in pair))
                    self.assertFalse(d['actual_coefficient_execution']);self.assertFalse(d['physical_admission'])
                    json.dumps(d)
    def test_unconditional_actual_refusal(self):
        owner=B.I.FullOwner(12,'zero',4,1,0)
        with patch.object(B.QH.subprocess,'check_output',pinned_git):
            api=B.ActualQBinding();bound=B.ActualQuotientBinding(owner);C=B.OwnedClearing(owner,(0,1))
        for obj in [api,bound,C]:obj.mode='synthetic';obj.support_box=prohibited
        calls=[lambda:api.coefficient(owner,None),lambda:api.factor_terms(owner),lambda:bound.coefficient(None),lambda:bound.factor_terms(owner),lambda:C.coefficient(None)]
        for call in calls:
            with self.assertRaises(B.I.PhysicalAdmissionMissing):call()
    def test_artificial_partition_identity(self):
        # Artificial constants obey -v0+v1=1 and hj+v2*a=vj^5.
        C=lambda x:{ZERO:x}
        vs=[2,3,2,1,1];a=3
        cat=B.QH.ArtificialCatalog([C(v)for v in vs],[C(v**5-vs[2]*a)for v in vs],C(a),[C(1),C(1),C(0),C(0),C(0)])
        for N in [1,2]:
            for pair in [(0,1),(2,3)]:
                total=0
                for carrier in [0,1,5]:
                    owner=B.I.FullOwner(12,('toy',carrier),carrier,0,8)
                    p=B.ArtificialBinding(owner,cat,N=N,p=pair)
                    # Axis0 pair factor t or complementary raw t^2, then one frame shift.
                    exp=-N*(4 if carrier==5 else 5)-(2 if 0 in pair else 2)
                    coeff=p.coefficient((exp,0,0,0))
                    self.assertEqual(dict(p.factor_terms(owner,pair)),{(exp,0,0,0):coeff})
                    total+=(a if carrier==5 else vs[carrier]**5-vs[2]*a)**N*coeff
                self.assertEqual(total,1)
    def test_pin_drift_rejected(self):
        original=Path.read_bytes
        def changed(path):
            data=original(path)
            return data+b' 'if str(path).endswith('/inner-quotient/quotient.py')else data
        with patch.object(Path,'read_bytes',changed):
            with self.assertRaisesRegex(ValueError,'pin drift'):B.ActualQBinding()
if __name__=='__main__':unittest.main()
