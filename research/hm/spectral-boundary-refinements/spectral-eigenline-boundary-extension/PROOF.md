# Eigenlines across the nilpotent boundary and exact determinant degeneration

## Statement and imports

Use the reduced projective spectral incidence X from https://github.com/Akilleez-QA/read-em-and-weep/blob/264b18521dd174e3e4ae185b8be51f9f6c303d87/research/hm/relative-models/spectral-nef-boundary-bound/PROOF.md. Write G=Gr(3,V), dim V=5, S its tautological bundle, E=sl(S)⊗det S, R=O_P(E)(−1), and M=R*⊗det S. The universal twisted endomorphism A:S→S⊗M has determinant zero and q=tr(A²)∈H⁰(M²). Every geometric point has rank two: rank one is excluded by the imported two-plane theorem, and the universal tensor is nonzero. Points where q=0 are regular nilpotents.

Let Y be any integral component of X not contained in the nilpotent incidence. On the finite flat eigenvalue cover π:Y'→Y defined by λ²=q/2, the three eigenline bundles extend across the entire nilpotent boundary. Their sum maps to S with local cokernel

    O/(λ) ⊕ O/(λ²).

Its determinant vanishes to exactly three times the Cartier divisor of λ. Consequently, writing r=c1(R*) and H=c1(det S*), the class 3r−2H is nef on all of reduced X.

These are universal bundle identities and scheme-theoretic boundary statements. No actual source matrix, input, product, operation rank, selected jet or residue is evaluated.

## 1. The finite cover and extended eigenlines

Construct Y' as Spec_Y(O_Y⊕M⁻¹), with multiplication on the second summand determined by q/2. This is finite flat of degree two, and λ is its tautological section of π*M. Since q is nonzero on the integral Y, the generic algebra is a separable quadratic algebra over the characteristic-zero function field. The finite locally free algebra injects into that reduced generic algebra, so Y' is reduced, even if reducible. Multiplication by λ is injective because λ²=q/2 is a nonzerodivisor. Thus its zero scheme D_λ is an effective Cartier divisor, possibly empty, with O(D_λ)=π*M.

All bundles below are pulled back to Y'. The three maps A, A−λI and A+λI from S to S⊗M have constant geometric rank two. For λ≠0 the eigenvalues are 0,λ,−λ and are distinct, by the traceless characteristic identity A³=(q/2)A. For λ=0 the endomorphism is regular nilpotent of rank two. On a reduced scheme the rank-two minor charts therefore give line subbundles

    L0=ker A, L+=ker(A−λI), L−=ker(A+λI).

Each is a subbundle of V⊗O. Their duals are globally generated and nef. No normalization, smoothness or unramified-boundary assumption is required.

## 2. A cyclic local presentation

Locally trivialize M. At every point A is a regular three-dimensional endomorphism: either it has three distinct eigenvalues or a single length-three nilpotent Jordan block. A cyclic vector exists on each fiber. Lift such a vector v to a local section and shrink so v,Av,A²v is a basis. The characteristic identity in this basis is

    A³v=λ²Av.

The sections

    e−=(A²−λA)v,
    e0=(A²−λ²I)v,
    e+=(A²+λA)v

generate L−, L0 and L+, respectively. Each has third cyclic coordinate one, so it is primitive even at λ=0. They satisfy the indicated eigenvalue equations directly from A³=λ²A.

In the basis v,Av,A²v, the natural inclusion Φ:L−⊕L0⊕L+→S has matrix

    [ 0    −λ²   0 ]
    [−λ     0    λ ]
    [ 1     1    1 ].

This is a universal companion calculation, independent of any actual operation value. Subtract the first column from the other two. Eliminate the unit in the third row and first column. The remaining two-by-two matrix is

    [−λ²  0]
    [ λ  2λ].

Subtract one half of its second column from the first and interchange rows and columns as needed. Since two is invertible, this gives diagonal entries λ and λ² up to units. Thus Φ is locally equivalent by invertible row and column operations to diag(1,λ,λ²). This is an explicit equivalence over the local base ring, not an appeal to a principal-ideal-domain normal form.

In particular Φ is injective because λ is a nonzerodivisor, and its cokernel C has local description

    C ≅ O/(λ) ⊕ O/(λ²).

Its Fitting ideals are

    Fitt_0(C)=(λ³), Fitt_1(C)=(λ), Fitt_2(C)=O.

This resolves the exact module thickness of the eigenline collision; it does not assign multiplicity three to the rank-one component of the original cubic zero scheme.

## 3. The determinant line and a new nef class

Taking determinants, the map L−⊗L0⊗L+→det S has divisor exactly 3D_λ. Hence there is an isomorphism of line bundles

    det S ≅ (L−⊗L0⊗L+)⊗M³.

The assertion is global: the determinant map itself is global, its local zero ideal is (λ³), and O(3D_λ)=M³. Twists introduced by choosing a local trivialization or cyclic vector do not alter that divisor.

Let x_i=c1(L_i*). Since c1(M)=r−H, this identity gives

    x−+x0+x+ = H+3c1(M)=3r−2H.

The left side is nef on Y', so the right side descends as a nef class on Y under the finite surjective map π. Equivalently every complete integral curve C⊂Y satisfies

    3 deg(R*|C) >= 2 deg(det S*|C).

On any integral component of X contained in N, the previously established flag formulas r=h+2t and H=3t give 3r−2H=3h, which is nef. Nefness can be tested on integral curves, each lying in some component, so 3r−2H is nef on all reduced X.

## Scope and next dependency

The eigenvalue cover compactifies the earlier eigenline construction on the spectral open. The extended eigenlines cease to form a frame precisely at λ=0, with invariant factors 1,λ,λ² and determinant divisor 3D_λ. This supplies a controlled boundary model and an additional global nef constraint for studying the remaining spectral components.

It does not prove that the cover is smooth or normal, that the nilpotent boundary is reduced, that any spectral component attains dimension four, or that the physical retained obstruction vanishes. The generic rank-one algebra and its multiplicity are separate objects; none of their currently unresolved numerical values is computed here.
