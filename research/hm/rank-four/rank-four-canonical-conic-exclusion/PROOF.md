# The canonical conic cannot have residual rank four everywhere

## Theorem and imported inputs

Retain the hypotheses of `../rank-four-conic-component-classification/PROOF.md`, together with the actual operation's linear image dimension twenty, as established in `../cubic-massey-module-reduction/PROOF.md` and `../full-hm-image-symmetry/PROOF.md`. Then the rank-four curve has no irreducible conic component.

More generally the contradiction below needs only image dimension greater than sixteen. It does not evaluate the actual operation, its coefficients, or a selected source input.

Write G=SL2(F5), with central involution z, and V=T⊕W with dimensions three and two, where z acts positively on T and negatively on W. We import the following audited consequences from the conic classification and its independent audit. If a conic component exists, it is a translate of the unique G-invariant smooth conic C⊂P(T); on C the even and odd middle blocks have constant ranks five and three; the pure-T coefficient image lies in one fixed H≅P5 of dimension five; and all coefficients f(w1,t,w2), with w1,w2∈W and t∈T, lie in that same H.

We also use the audited irreducibility of E=W⊗T of dimension six from `../canonical-line-parity-exclusion/PROOF.md`, Section 2. Outer symmetry and cyclic zero hold throughout. We replace J by the span of all operation values, with the induced honest G-action, and denote its parity eigenspaces J+ and J−.

## 1. The odd image fibers span at most six dimensions

Identify C with P1. The odd middle block on C is the constant-rank-three morphism

    O_C(-2)⊗E → J−⊗O_C.

Its image I is a rank-three equivariant vector subbundle of the trivial target and a quotient of O_C(-2)⊗E. Thus I(2) and I* are globally generated. Birkhoff–Grothendieck gives

    I ≅ O(-d1)⊕O(-d2)⊕O(-d3),    0≤di≤2.

The nonzero equivariant source map induces a nonzero map E→H⁰(I(2)). As E is irreducible of dimension six, this map is injective. Therefore

    6 ≤ h⁰(I(2)) = 9-(d1+d2+d3),

so d1+d2+d3≤3. Consequently

    h⁰(I*) = 3+(d1+d2+d3) ≤ 6.

The fixed vector space spanned by the fibers of I inside J− has dimension at most h⁰(I*), hence at most six. Indeed, the restriction map J−*→H⁰(I*) has kernel precisely the annihilator of that fiber span. Its rank is the span's dimension.

This argument needs no equivariant splitting classification, no identification of the summand representations, and no determinant-character argument.

## 2. All odd coefficients span at most eight dimensions

Let M⊂J− be this span. It contains f(w,t,t') for all w∈W, t'∈T, and nonzero t representing points of C. Since C spans T and the operation is linear in t, it follows that

    f(W,T,T) ⊂ M,    dim M≤6.

Outer symmetry and cyclic zero put every permutation of these mixed coefficients in M. Explicitly,

    f(t1,w,t2) = -f(w,t2,t1)-f(w,t1,t2).

The only other odd coefficients are those of f|W³. The universal outer-symmetric cyclic-zero quotient in dimension two is S_(2,1)W, of dimension two. Hence their span has dimension at most two. Therefore

    dim J− ≤ 6+2 = 8.

## 3. All even coefficients span at most eight dimensions

The pure-T coefficients and f(W,T,W) already lie in H, of dimension five. For the remaining placement define

    h(w1,w2,t)=f(w1,w2,t).

Outer symmetry and cyclic zero give

    h(w1,w2,t)+h(w2,w1,t) = -f(w1,t,w2) ∈ H.

Thus modulo H the map h is alternating in its W inputs. Its quotient coefficient image factors through Λ²W⊗T, of dimension three. Every even coefficient is either pure T or has two W inputs and one T input. We have now covered every placement, so

    dim J+ ≤ 5+3 = 8.

## 4. Contradiction and conclusion

Together Sections 2 and 3 show that the linear span of all values of f has dimension at most sixteen. For the actual operation, nonzero repeated-input injectivity makes f nonzero, and irreducibility of its twenty-dimensional normalizer target makes its linear image all twenty dimensions. This is a contradiction.

The canonical conic is therefore not contained in Z4. The earlier classification shows every possible conic component under the degree budget is one of its twenty-five translates. None occurs. Together with the already audited no-line theorem, every irreducible component of the reduced rank-four curve has degree at least three.

The proof does not exclude higher-degree components, determine isolated Z4 points, or assert a new bound on their ranks. No source tensor, source coefficient, selected source input, or actual-operation matrix was evaluated.
