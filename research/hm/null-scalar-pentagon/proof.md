# The next scalar unit defect, and only that defect

Source read in full before calculation: Akilleez-QA/read-em-and-weep,
`research/hm/second-order-algebroid.md`, commit
`c8aec970fd65a105f39f4e8aeb8a17f0f0053f89` (blob
`a58834ab61e18a5dedd8a7bf20bec7121bfa9165`). The pinned source is linked rather than copied: https://github.com/Akilleez-QA/read-em-and-weep/blob/c8aec970fd65a105f39f4e8aeb8a17f0f0053f89/research/hm/second-order-algebroid.md .

This is an independent formal scalar calculation. It does not evaluate any physical q, bundle matrices, owner data, finite-model coordinates, jets, or experiments. It does not claim an order-three algebroid or module extension.

## 1. Conventions and order two

Take a unital star product with μ₁(f,g)={f,g}/2 and normalized higher bidifferential coefficients (they vanish when an argument is 1). All b and c below are scalar functions on intersections. Use the ordinary Čech differential

(δb)ijkl = bjkl − bikl + bijl − bijk.

The source has Fij=id+h²Tij modulo h³, Aijk=exp(hbijk) modulo h³, where exp is the ordinary exponential, δb=0, and δT={b,−}. T is an ordinary derivation. Therefore F is an algebra map modulo h³; the inner-gluing equation at h² is precisely δT={b,−}. The unit equation through h² follows from bijk+bikl=bjkl+bijl. These statements agree with Section 3 of the pinned source.

## 2. Expansion through h³ of the unit equation

Write Fij=id+h²Tij+h³Sij+O(h⁴) and
Aijk=1+hbijk+h²bijk²/2+h³(bijk³/6+cijk)+O(h⁴).
The maps are unital: T(1)=S(1)=0. Set a=bijk, d=bikl, e=bjkl, f=bijl. Then the coefficients of h³ on the two sides of

Aijk ⋆ Aikl = Fij(Ajkl) ⋆ Aijl

are, respectively,

(a+d)³/6 + cijk+cikl + μ₁(a,d),
(e+f)³/6 + cjkl+cijl + Tij(e) + μ₁(e,f).

Indeed h μ₁(ha,hd) first contributes at h³; μ₂ and higher coefficients cannot contribute at h³ because their first possible nonconstant inputs each cost h, and their unit inputs vanish. The unknown S contributes nothing: S(1)=0, while h³S(h e) has order h⁴. This exclusion of S requires unitality, not merely an arbitrary linear-map expansion.

Since a+d=e+f, the cubic terms cancel. Thus the exact sign is

δc = Ψ,
Ψijkl = ½{bijk,bikl} − ½{bjkl,bijl} − Tij(bjkl).

No unknown F₃ or star-product μ₃ enters this particular scalar unit equation. Algebra preservation and inner-gluing through h³ are distinct equations which this calculation does not solve. In particular an arbitrary ordinary derivation T need not preserve the Poisson bracket, so order-two preservation cannot simply be promoted to order three.

## 3. Ψ is closed from the stated identities alone

Put Cijkl=½({bijk,bikl}−{bjkl,bijl}) and Dijkl=Tij(bjkl), so Ψ=C−D. Standard Čech cup signs give

δD = (δT)∪b − T∪δb,
(δD)01234 = {b012,b234}.

For an explicit independent check of the bracket term, set
x=b012, y=b013, z=b014, u=b023, v=b024, w=b034.
The cocycle relation expresses the remaining four entries as

b123=u−y+x, b124=v−z+x,
b134=w−z+y, b234=w−v+u.

Substitution into C1234−C0234+C0134−C0124+C0123, using only bilinearity and antisymmetry, gives

δC = {x,u}−{x,v}+{x,w} = {b012,b234}.

Hence δΨ=0. This proof needs no Jacobi identity, no assumption that T is Poisson, and no higher descent equation. The accompanying standard-library script checks the identity in the free antisymmetric bracket on six independent symbols, rather than at a numerical specialization.

Closedness is not exactness on a general cover/space. The class [Ψ] in scalar H³ is the obstruction for this unit equation with the displayed lower-order data. Even exactness does not solve the other order-three descent equations.

## 4. Conditional deck-character statement

Assume the actual scalar Čech entries decompose b=bP+bQ with characters P=χ₁χ₂ and Q=χ₃χ₄; μ₁=μ₁,P+μ₁,Q has those respective bivector characters; T has character zero; and restrictions/deck actions respect the cochain model. Every bracket term has weight R+S+U with R,S,U in {P,Q}; in the exponent-two character group that sum is always P or Q. T(b) also lies in P/Q. Thus Ψ has no full-sign P+Q component, and no invariant component.

If in addition bP and bQ genuinely depend only on their disjoint factor pairs, all mixed pair brackets vanish and C is the sum of its separate pair contributions. This support assumption is stronger than character purity and is not needed just to exclude full-sign weight. These are assertions about actual scalar cochains: they are not inferred from arbitrary matrix normalization or labels on a finite-model output.

Optional unit-only consequence: on C⁴, Künneth gives H³(O)=⊕|S|=3 χS. Thus if the cochains above are regular in an equivariant acyclic Čech model, [Ψ] vanishes in scalar H³ and a c solving this unit equation exists (and may be chosen in P/Q by averaging). The formal calculation does not instantiate that regular model or construct c. This conditional consequence is not an order-three algebroid existence claim.

## 5. Reproduction and boundaries

The preserved checker is `verify.py`; its existing output is `test-output.txt`. It was not rerun for publication.
The bounded test uses only Python's standard library, six free scalar symbols represented linearly, an antisymmetric formal bracket, a three-variable polynomial-ring check of cubic exponential cancellation, and XOR character arithmetic. It performs no network access, production imports, model matrix products, or geometric evaluations.
