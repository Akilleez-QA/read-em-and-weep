# Exact abstract rank-interface freedom

Companion to GENERIC-PRIMARY-TOP-SURJECTIVITY.md at d4bda2be129a9536e9e0a50aac0f5eb39c4911c8 and AMBIENT-BETA-SECONDARY-MAP.md at4697da676f49f13eb74c2cc73d09db1406b71b37 in PR543.

Exact abstract certificate: the remaining mu rank is not fixed by these interfaces

The accompanying standard-library script check_rank_interface_freedom.py constructs exact rational diagrams with P=C20, R=C10, T=C2, an injective tau:C6->P plus R and surjective Psi:P plus R->T. It checks Psi tau=0 and lets mu be projection_P tau and ell=Psi restricted to R. For every s=0,...,6 and r=0,1,2, it constructs rank(mu)=s and rank(ell)=r. All 21 checks pass. The generic primary-generation theorem above removes r=0,1 in the actual HM situation; the seven r=2 models still permit every s.

Explicit construction: put s basis vectors of the domain into the first s coordinates of P and the remaining 6-s into coordinates r through r+5-s of R (indices start at zero). Let ell project the first r coordinates of R onto the first r output coordinates. Let the cubic component of Psi take P coordinates s through s+1-r onto the other output coordinates. These supports are disjoint from the tau image. Thus tau is injective, Psi is onto, and their composition is zero. The script also checks all relevant cokernel and image dimensions, including the exact sequence (*) when r=2.

These are abstract vector-space models, NOT selected HM coefficients, and NOT asserted realizable by any HM bundle, commutative graded module, Hilbert--Burch matrix, sextic, or beta extension. Their precise logical use is limited: ranks tau=6, Psi=2, ell=2 and the displayed exact vector-space interfaces cannot alone force any particular mu rank. Further information about actual multiplication or geometry is required. They do not show such further information is absent or cannot close the branch.

The projection relation used by the models also agrees, up to the choice of connecting-map sign, with the ambient/hyperplane presentation: for a Cech 2-cocycle v in 3F(-2), an acyclic lift (a,b) in 3F(-1) plus 4F(-1) satisfies da=-ell v and db=Mv. Its image in Q has first component Ma+ell b. Reduction modulo ell gives M(a mod ell), exactly hyperplane multiplication on the connecting-class representative of v. This explains why retaining the projection relation still does not remove the linear-algebra freedom.

