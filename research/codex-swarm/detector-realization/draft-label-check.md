# Draft metadata-label boundary receipt

Before the helper guard fix, this unpublished draft test executed twice:

```python
self.assertEqual([len(tuple(P.potential_owners(t,('t',t))))for t in(0,8,12,14,15)],[2,6,16,40,32])
```

SHA256 of the UTF-8 snippet above, excluding newline: `1f08de897620166310c98f22bb5e8c1a584ee0af3d2331328b5f4a95c63ef438`.
This is snippet provenance, not an archived whole-file hash or Git commit.
The first execution had8 tests and the second10 tests. Each constructed96
FullOwner metadata labels across tags0,8,12,14,15 (counts2,6,16,40,32), hence192
object instances representing the same96 label combinations. This crossed the
no-physical-owner-iteration boundary. No physical model, field value, source,
coefficient or joint five-owner fiber was evaluated on those labels.

The fix guards potential_owners before its first yield. The structural test now
uses only alphabet_count(tag), with the FullOwner constructor patched to fail.
The physical refusal test likewise patches both field and owner constructors to
fail, and requires PhysicalAdmissionMissing instead. Further physical label
iteration is held. Artificial fixture labels are separate explicit toy inputs.
