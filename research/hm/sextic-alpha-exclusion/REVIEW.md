# Independent review

## Verdict

The alpha-exclusion argument proposed by Mr. Slop passes independent mathematical review under the explicitly pinned PR543 inputs. The proof excludes alpha/line on a dense open set of hyperplanes, not all special hyperplanes. It leaves the beta-plane case open. No formal proof-assistant check is claimed.

## Checks completed

1. Read the exact SEXTIC-PLUCKER-FLAGS.md at a82e9aeaad55a4e58a0fea12581bab1dcf42e4b0. The image bundle is locally free both at the DVR points of Z and at singular points away from Z. Its determinant has degree five.
2. Verified duality for a possibly non-Gorenstein integral genus-three curve: the degree-minus-one rank-one torsion-free sheaf has no sections. Thus h^0(L)=3. The line/plane-quintic dichotomy and the finite-birational quotient length three follow as stated.
3. Verified the Grassmannian flags and their interpretation for actual sections, including across Z.
4. Checked the vanishing lemma H^0(I_C tensor E)=0 using N-equivariance, irreducibility of U, and nonzero evaluation on the smooth reduced degeneracy curve. The original Horrocks–Mumford paper pins U to chi_4 in equation (4.12), printed p.74, and its irreducible character in the appendix, printed p.81.
5. Checked the rational kernel-line construction on an open stratum, positive-dimensional fiber, fixed component, degree bound, Heisenberg orbit argument, and fixed-intersection-point contradiction.
6. Checked that the argument uses only generic symbolic geometry. It neither requires nor performs a selected actual HM/source-instance evaluation.

The main note records precise dependency links and the remaining beta-plane boundary. The root author also independently checked the incidence, degree, and orbit steps before preparation of this slice.
