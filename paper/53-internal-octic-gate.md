# Internal fourth-through-seventh vanishing and the octic gate

**Craig Ward · 23 October 2026 · Update through PR995**

[PR995](https://github.com/Akilleez-QA/read-em-and-weep/blob/f9435fa37c78e86391fd1a773a039dd646a05e53/research/hm/source126-typeII-internal-octic-gate/PROOF.md) retains an actual source126 Type II occurrence with its entire two-dimensional radical Q-compatible. This hypothesis is not established. Under it, the internal fourth through seventh symbols are globally zero, and the actual eighth symbol lies in a canonical one-dimensional line with unselected scalar. **Four necessary catalogue pairs and three labels remain; the original repair is open.**

## 1. The internal problem is distinct from the original one

Let S be the full-radical annihilator complex. Its first symbol is multiplication A O(-1)→D O on A and zero on D; its cokernel E has rank two. Previous theorems establish its second and third symbols as zero. PR985 also bounds its generic rank by23, below target dimension24. After 19 constant pivots and three first-order pivots, the surviving five-to-two internal differential therefore has rank at most one.

The original complex already has all generic Bocksteins after the second zero. That is an imported result, not the new conclusion here. It does not by itself make every internal differential zero.

## 2. Globally defined higher symbols

A recursive normalization constructs each next internal symbol r_n:D O(-n)→E once the preceding ones vanish. At each step a zero residual in E factors uniquely through the injective first-image subbundle. This supplies a global polynomial kernel correction, not division by a selected coefficient. A shifted-lift comparison proves independence of choices.

The parameter space is the plane P(A), so its degree-m section representation is Sym^m A, not Sym^m W. The degree bookkeeping and equivariant character calculation retain that distinction.

## 3. Why orders four through seven vanish

A nonzero rank-one equivariant map must factor through a saturated line bundle O(k) in E. Character constraints show that no such map exists in degrees four or five. A nonzero r4 or r5 would consequently have generic rank two and make S onto, contradicting its rank bound. Both vanish globally.

Degrees six and seven do admit canonical one-dimensional rank-one possibilities. Their common source covector is the quadratic apolar pairing c_a(h)=⟨a²,h⟩. The quotient first-kernel inclusion κ has cκ nonzero, proved from the universal sextic subsystem at a general nonflex square. Multiplying it by either nonzero invariant target section cannot annihilate it on the integral parameter plane.

Actual radical naturality, applied only to liftable quotient first-kernel cycles, requires r_nκ=0. It therefore excludes each nonzero sixth- and seventh-order line, proving r6=r7=0 globally. The abstract lines remain valid representation-theoretic objects; their realization as these actual internal symbols is what is excluded.

## 4. A genuine one-dimensional eighth-order remainder

The actual r8 is now globally defined, has generic rank at most one and kills κ. Saturated-line analysis leaves two potential factor types. One again contains c and fails naturality. The other factors through O(-4), with a two-dimensional space of quartic source covectors and a unique invariant target section σ.

The covector Δc has nonzero κ restriction. Conversely, the unique cubic P-covariant paired with the quotient first symbol gives a nonzero quartic covector ψ4 killing κ. These establish exactly a one-dimensional restriction kernel. Thus

r8 ∈ C·(σψ4).

This line is canonical, nonzero and rank one generically, and all its members satisfy the tested naturality condition. Its actual scalar is **unselected**. This is the first degree in the bounded four-through-eight analysis admitting a nonzero map under both tested constraints. It does not show that the actual map is nonzero, rule out further actual constraints, or classify degree nine and above.

## 5. Verification and remaining boundaries

The full proof was read; the independent whole-proof review reports **185 exact checks** in ordinary and optimized Python. They authenticate inputs, compute the plane character multiplicities and saturated factors, and check symbolic recursive normalization. The actual-complex and geometric nonflex arguments remain written mathematics, not actual-instance evaluation or proof-assistant certification of the full chain.

This theorem is restricted to full-J Type II. PR992's single-line cubic remains unselected, and no full-J zero conclusion is silently transferred to it. The secondary scalar ν is also unselected. No pending secondary-octic test is incorporated. The through-PR993 archive in chapter52 is preserved exactly, with only its previously checked link relocation; current summaries record this new result separately.
