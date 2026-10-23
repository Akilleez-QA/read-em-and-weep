# Independent mathematical and reproducibility review

Verdict: PASS for the stated conditional actual-candidate specialization. Source126 E10 has only Q129 or Q157 among its four retained actual quotient candidates. Q231 and Q249 are excluded; no stable label or actual-HM realization is settled.

## Exact reviewed artifacts

- PROOF.md SHA256: 4530b934749d8702571df45a30aaa3eb7a8fea3a2e5c07fdefe00bf551fa33fa
- verify.py SHA256: 941aaee568ca108539d74fddf6726858c9b2c969061af4bbd41b66c2831dfb8c
- RESULT.json SHA256: 72f7eb59a8d16582a151f230198db634389086b2315138437cdc6689871d54a5
- INPUTS.json SHA256: a49e7b2915b5dc28dcd428db808900720e6a8d9683591d14d42b5a0d3dac1aa3
- README.md SHA256: c948b2a4970cfd21065aa7ef7900cd106ca76b24a3f6eb1a01154e7c36e65a1e

## Source authentication and scope

Independent immutable GitHub file retrieval returned Git blobs 8a5522965ac861b5c4e149724782a489c5afb7cd (856), 54207bb4a1d2ff7cce3ce365f81bb5b146a61c81 (858), e18035dcceb1c7e0d0d4356ee578937d3172390b (862), 050610e5144820c5e323e092dcc7c8417fb52828 (869), and e411417c9a61677df55e07f0aff15fbea4c9ec69 (original quotient catalogue). Local Git-blob and SHA256 checks match the recorded inputs. The relevant separation, template and abstract-family proof sections were read; this review does not re-prove their entire ancestry or the historical retained-list completeness.

## Mathematical checks

1. The degree-eight P projection is w tensor a7 by the pinned Euler contraction. Its saturated Euler filtration gives 0 -> O(6) -> Q_P -> Wp O(1) -> 0. H1(O(5)) vanishes, so Q_P splits equivariantly as claimed. The degree signs and quotient versus annihilator orientation agree.
2. For Type II, dividing by the full first-polar Y leaves P O plus B, with B=(P+D)O(2). Quotienting the graph of X over its saturated P projection gives 0 -> B -> Q_R -> Q_P -> 0. This is the correct extension orientation. Its O(1) term has zero ordinary Ext; its O(6) term has invariant Ext Hom_G(A,P+D)=0. Finite-group averaging in characteristic zero is legitimate. No constant shear is inferred from this bundle splitting.
3. The complete osculating quotient identity has the correct rank, twist and apolar convention. It yields (Wp+T)O(1) for the complete degree-eight line and (P+D)O(2) for the complete degree-ten first polar.
4. The first-polar linear-annihilator lemma is valid. Euler gives ell f=0 from ell partial_u f=ell partial_v f=0; differentiation gives both constant partial derivatives of ell annihilating the full coefficient span. They vanish, and homogeneous linear ell is zero. Characteristic zero and full span are essential and supplied here.
5. Type III therefore has H0(Q*(1))=Wp+T. The four exact catalogue profiles have respectively Wp, Wp+T, 2Wp and 2Wp+T at this twist. Only157 survives Type III, while Types I/II give129 directly.
6. Independent weaker cross-check: all three templates allow at most one Wp in H0(Q*(1)). In Types I/II the complete-Y annihilator has no twist-one sections and the projected-P contribution lies in P tensor W=Wp+T. In Type III the other constant span contributes a subrepresentation of (A+V) tensor W=W+S+T, containing no Wp. This separately excludes231 and249 without the stronger exact Type III lemma.

## Reproduction

Executed python verify.py and python -O verify.py independently after final-byte freeze. Both passed288 explicit checks, returned identical output and reproduced the pinned RESULT.json. The verifier uses explicit exceptions rather than optimized-away assertions. Its universal coefficient identities are bounded supporting algebra tests, not proof-assistant verification of the geometric argument and not an actual-instance evaluation.

During review, the abstract-family language was narrowed: Type III's full-profile selection is explicitly conditional on the retained actual catalogue. No claim that its completeness automatically transfers to every abstract family member remains. A test comment was corrected from dimensions to multiplicity counts. No blocking issue remains for the stated two-pair exclusion.
