# Independent mathematical review

Reviewed PROOF.md with SHA256 6069a0228a58827a57bfd3aec0a28462e9d3fbe3fd6685af6a37dd204f9459f8. The proof is mathematically valid conditional on its pinned PR488 inputs. This is an independent mathematical review, not formal proof-assistant verification.

## Quartic generators and linear syzygies

Horrocks–Mumford Lemma 3.3(vii) dualizes to Sym^4 T=V tensor (T_4+Q_4+U+U'). The quotient labels are self-dual, while the five-dimensional factor changes from V* to V. The distinction between ordinary T_4 and spin Q_4 is respected throughout.

The displayed tensor identities give T tensor I_3=V tensor (W'+Q_4+T_4). Irreducibility, inequivalence and multiplicity one imply that the multiplication image dimension is zero, twenty or forty. This does not assume a nonzero scalar on either eligible summand.

The Macaulay calculation is correct: 25=binom(6,3)+binom(3,2)+binom(2,1), whose degree-three successor is 35+4+3=42. Applying the growth bound to S/(I_3), not to a guessed higher truncation, forces dim(T I_3)>=28. Both twenty-dimensional channels therefore occur. The kernel is V tensor W', dimension ten.

Because PR488 gives R_4=V tensor U', the unique remaining summand of I_4/(T I_3) is V tensor U, dimension fifteen. These are precisely minimal quartic generators because I vanishes below degree three. The multiplication kernel describes all linear syzygies on the cubic generators. Adding minimal quartic generators does not change that space: any putative degree-four syzygy with constants on quartic generators would contradict independence of their classes modulo T I_3.

## Degree-six exclusion

Section 4 is also valid. The reversed dual N_j=R_(5-j)* is generated in degree zero because the only socle of R is R_5. Hence T tensor N_0 -> N_1 is surjective; both sides have dimension fifteen, so it is an isomorphism.

In total degree four, the fourth Koszul differential on N then identifies with exterior comultiplication tensored with N_0. Its composition with the exterior product is plus or minus four times the identity, so it is injective over C. This proves Tor_4(N,C)_4=0 without needing information on later differentials or higher relations of N.

The stated determinant convention is correct: (Lambda^i T)* tensor det(T) identifies with Lambda^(5-i) T. Dualizing R_(d-i) gives N_(5-d+i), which is the module degree at position 5-i and total degree 10-d. Therefore Tor_i(R,C)_d* tensor det(T)=Tor_(5-i)(N,C)_(10-d), and the case i=1,d=6 excludes minimal degree-six generators. For d>6, the first Koszul term T tensor R_(d-1) vanishes directly.

Thus section 4 proves that every minimal generator of I has degree three, four or five. Sections 5 and 6 then exclude the last possible degree, as checked below.

## Quintic reduction and Euler elimination

The second Macaulay bound is correct: 15=binom(6,4) has successor binom(7,5)=21. For J=(I_3,I_4), the exact quotient sequence gives dim(I_5/J_5)<=21-3=18.

The Heisenberg center acts trivially in degree five, so restriction to Gamma factors through the order-twenty-five abelian quotient. Normalizer conjugation permutes its nontrivial characters transitively, so any nonzero nontrivial-character contribution has dimension at least twenty-four. The eighteen-dimensional bound excludes it. Gamma therefore acts trivially on the minimal quintic generator quotient. The notation Gamma now distinguishes the finite group from the cohomology module H and its graded pieces.

Exactness of invariants in characteristic zero makes the remaining quotient a quotient of I_5^Gamma. Theorem 3.5 gives S_5^Gamma=U+U', and the pinned quotient R_5=U' forces I_5^Gamma=U. Thus only the irreducible U channel could survive.

Directional differentiation is an equivariant map T* tensor U=V tensor U -> S_4. Its image lies in the unique V tensor U summand of S_4, contained in I_4. The map is nonzero because homogeneous quintics cannot have every first derivative vanish over C. Hence every first derivative of every element of the invariant U space lies in I_4. Euler's identity 5q=sum_i x_i partial_i q then places all of U in T I_4. The surjection from this U space to the quintic generator quotient is consequently zero, so that quotient vanishes.

The complete conclusion is therefore exact: I has ten cubic minimal generators A tensor W' and fifteen quartic minimal generators V tensor U, and no generators of any other degree. No explicit quintic polynomial or selected instance is used.

## Scope

The proof uses universal representation theory, Hilbert-function growth, level duality and Koszul complexes. It does not evaluate selected HM instances or numerical multiplication matrices, and it does not resolve the separate parameters r or s for H, selected-form membership, higher-order lifting or algebraicity.
