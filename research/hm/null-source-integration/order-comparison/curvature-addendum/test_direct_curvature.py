"""Independent metadata replay via bounded-simplex vertices, not greedy support.
Run: python test_direct_curvature.py PATH_TO_PUBLIC_NULL_SUPPORT_CERTIFICATES
"""
import sys,json,itertools,functools,unittest,hashlib
from pathlib import Path
import probe_direct_curvature as probe
SUPPORT=Path(sys.argv.pop(1));ROOT=Path(__file__).parent

class VertexSupport:
    def __init__(self,nodes):self.nodes=nodes
    @functools.cache
    def bound(self,n,w):
        op,*args=self.nodes[n]
        if op=='rational':return (0,0) if args[0] else None
        if op=='coordinate':return (w[args[0]],)*2
        if op in ('add','multiply'):
            bs=[self.bound(i,w) for i in args]
            if op=='add':
                bs=[b for b in bs if b is not None]
                return (min(b[0] for b in bs),max(b[1] for b in bs)) if bs else None
            return None if None in bs else tuple(sum(b[j] for b in bs) for j in range(2))
        if op=='power':
            i,k=args;b=self.bound(i,w)
            assert k>=0 or self.nodes[i][0]=='coordinate'
            return (0,0) if k==0 else None if b is None else tuple(sorted(k*x for x in b))
        assert op=='bounded_composition_sum'
        d,body=args;N=d['dimension'];T=d['threshold'];total=d['total'];j=d['chosen']
        assert total==N*(T-1)+1 and d['earlier_upper']==T-1
        lo=[T if i==j else 0 for i in range(N)];hi=[T-1 if i<j else total for i in range(N)]
        for power in body['powers']:
            if self.bound(power['base'],w) is None:
                assert self.nodes[power['base']]==['rational',0,1]
                e=power['exponent'];assert e['constant']==0 and sorted(e['coefficients'])==[0]*(N-1)+[1]
                hi[e['coefficients'].index(1)]=0
        vertices=set()
        for free in range(N):
            other=[i for i in range(N) if i!=free]
            for bits in itertools.product((0,1),repeat=N-1):
                v=[0]*N
                for i,bit in zip(other,bits):v[i]=(lo,hi)[bit][i]
                v[free]=total-sum(v)
                if all(lo[i]<=v[i]<=hi[i] for i in range(N)):vertices.add(tuple(v))
        assert vertices
        values=[]
        for v in vertices:
            result=[0,0]
            for power in body['powers']:
                ex=power['exponent'];k=ex['constant']+sum(x*y for x,y in zip(v,ex['coefficients']));assert k>=0
                b=self.bound(power['base'],w)
                if b is None:assert k==0;continue
                for a in range(2):result[a]+=k*b[a]
            values.append(result)
        return min(x[0] for x in values),max(x[1] for x in values)

class Curvature(unittest.TestCase):
    def test_new_full_domain_and_all_512_associations(self):
        saved=json.loads((ROOT/'direct-curvature-support.json').read_text())
        domain=set(itertools.product((0,4,8,12),(1,5,9,13),range(16)))
        self.assertEqual({tuple(r['input_masks']) for r in saved['results']},domain)
        self.assertEqual(len(saved['results']),256)
        gaps=[]
        for row in saved['results']:
            actual=probe.build(*row['input_masks'],include_internal=True);inside=actual.pop('internal')
            self.assertEqual(json.loads(json.dumps(actual)),row)
            s=VertexSupport(inside['dag']);M=row['complete_F_numerator_degree']
            for record in row['results']:
                kind=record['kind'];w=(-1,-1,0,1);shift=[0,int(kind=='B'),0,0]
                b=s.bound(inside['roots'][kind]['root'],w)
                cert=record['certificate'];self.assertEqual(tuple(cert['normal']),w);self.assertEqual(tuple(cert['multiplier_bounds']),b)
                target=sum(w[i]*((-1,-2,-2,-2)[i]+shift[i]) for i in range(4))
                high=sum(w[i]*(M[i] if w[i]>=0 else shift[i]) for i in range(4))
                gap=target-b[1]-high;self.assertGreater(gap,0);self.assertEqual(gap,cert['gap']);gaps.append(gap)
                for ledger in record['denominator_ledger']:
                    self.assertLessEqual(ledger['carrier'],16)
                    self.assertLessEqual(max(ledger['legal']),3)
                    self.assertEqual(ledger['standard'],[0]*4)
            # Per-instance cache must not retain all factored DAGs across this loop.
            s.bound.cache_clear()
        self.assertEqual(min(gaps),30)
    def test_exact_selector_source_and_dependency_binding(self):
        for name,digest in json.loads((ROOT/'dependency-hashes.json').read_text()).items():
            self.assertEqual(hashlib.sha256((SUPPORT/name).read_bytes()).hexdigest(),digest)
        probe.core.outer.authenticate_public_sources();probe.core.contraction_certificate()
        chart=probe.core.source.authenticate()['charts'][1]
        self.assertEqual(dict(chart['I'][12][1]),{'4,0,0,0':-1,'2,2,1,0':-1})
        self.assertEqual(chart['P'][0][6],[])
        self.assertEqual(dict(chart['P'][1][6]),{'4,0,0,0':-1,'0,1,1,1':1})
        expected={'1,1,1,1':1,'5,0,0,0':-1}
        self.assertEqual(dict(chart['di']),expected);self.assertEqual(dict(chart['dp']),expected)
        # P[1,6]=1/v1 by the displayed factor identity, not polynomial arithmetic.

    def test_activity_reduction_without_full_assignment_rescan(self):
        # Sixteen standard bits with fixed high-bit decoding; active legal masks
        # are exactly subsets of infinity coordinates, independently of compiler.
        masks=lambda tag:[m for m in range(16) if all(not(m>>i&1) or (tag>>(3-i)&1) for i in range(4))]
        self.assertEqual(masks(3),[0,4,8,12]);self.assertEqual(masks(11),[0,1,4,5,8,9,12,13])
        self.assertEqual(len(masks(15)),16)
        # Full active primary carrier choices by original fixed standard owner.
        carrier_pairs=list(itertools.product(range(1,3),range(1,4)))
        self.assertEqual(sum(min(a,b)==1 for a,b in carrier_pairs),4)
        self.assertEqual(sum(min(a,b)==2 for a,b in carrier_pairs),2)
        same=[(a,b) for a,b in carrier_pairs if a==b and min(a,b)==1]
        self.assertEqual(same,[(1,1)])
        all_masks=list(itertools.product(masks(3),masks(11),masks(15)))
        self.assertEqual(len(all_masks),512)
        self.assertTrue(all(not(a&3) and not(b&2) for a,b,c in all_masks))
        self.assertEqual(sum(bool(b&1) for a,b,c in all_masks),256)
        self.assertEqual(622592+259072+1024+1536+256+256,884736)

if __name__=='__main__':unittest.main(verbosity=2)
