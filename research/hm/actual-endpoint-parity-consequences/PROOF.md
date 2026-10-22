# The actual normal-variation line has both parities and a canonical reconstruction

## 1. Precisely pinned interface

Work over C with G=SL2(F5), W its fixed binary representation, A=Sym²W, D=Sym⁴W, and P the LOWER endpoint four-dimensional module. Assume the canonical source identification and invariant forms of PR661 (1325647fd916bf2daa71b11efeae6d52cfefa2cd), PR662 (f75a18fd411350adda35dedf18751eee002a39bc), and PR663 (ad3ab59f6fbbbb3e5bde1da58b3b92a1f49c6889). Their quadratic family space is

Q=Hom_G(D_source,P⊗Sym²A*)=Q_+⊕Q_−,

with one-dimensional symmetric and alternating lines. Parity interchanges the parameter D and source D slots after the fixed source identification. The invariant form identifies the primal/dual A convention in null's theorem with this convention.

Use as an additional input ACTUAL-ENDPOINT-NORMAL-VARIATION-IS-NONZERO.md at fb574c01207099eeb63960da5cb23ad2f2498a84. It supplies a linear map n:T→Q from a one-dimensional invariant normal space T, and, at the specified C5 square a=t², the already public statements

I_f(X⁴) is a nonzero multiple of st³,  n(eta)(a,X⁴)=0;
I_f(XY³) is a nonzero multiple of t⁴,  n(eta)(a,XY³)≠0

for every eta≠0. Here s is the other C5 eigenline, not an arbitrary complementary vector. No new actual coefficient evaluation is made below. Write q_eta for the family transported by I_f, so its source arguments below are binary quartics. Thus q_eta(a,st³)=0 and q_eta(a,t⁴)≠0. These properties alone are the actual input.

## 2. A universal missing nonvanishing

At b=t⁴ the symmetric channel is represented, up to a nonzero scalar, by B_+(b,h)=π_P^(8)(bh); the alternating one by B_−(b,h)=π_P^(6)((b,h)_1).

Both channels have nonzero value on h=t³s. For the alternating one, (t⁴,t³s)_1 is a nonzero multiple of t⁶ and PR661 proves π_P^(6)(t⁶)≠0. For the symmetric one the required assertion is π_P^(8)(t⁷s)≠0. If it vanished, t⁷s would belong to the complementary five-dimensional D⊂Sym⁸W. PR663's Wronskian lemma, with k=5,n=8,m=7 and root orbit size N≥12, would give

12(7−5+1)=36 ≤ 5(8−5+1)=20,

an impossibility. This is a universal representation-theoretic argument, not an actual endpoint calculation.

On the pure input t⁴, B_−(t⁴,t⁴)=0, whereas B_+(t⁴,t⁴)=π_P^(8)(t⁸)≠0 by PR661.

## 3. Both actual parity components are nonzero

Decompose q_eta=q_eta,+ + q_eta,−. Its nonzero pure-input value, where every alternating channel vanishes, forces q_eta,+≠0. Since the symmetric channel has a nonzero mixed-input value, the equality q_eta(a,t³s)=0 then forces q_eta,−≠0 as well. In particular the mixed zero is a cancellation of two nonzero terms, not a vanishing parity channel.

This holds for every eta≠0. Therefore each projection T→Q_+ and T→Q_− is an isomorphism of lines. The actual normal-variation image is a line transverse to both parity axes.

## 4. Intrinsic ratio and reconstruction without numerical coefficients

Fix the projective C5 square [a] just used. Let U⊂W be its root eigenline and Z the other eigenline of its C5 stabilizer. Let L_0=U⁴ and L_1=U³Z. These are canonical distinct stabilizer eigenlines in K_a=L_0⊕L_1. No generator of U, Z, or either channel line is chosen.

Retain the natural quadratic twist. Define

H_i=Hom_{C5}(L_i,P⊗O(2)_[a]),  i=0,1.

Both are one-dimensional by the C5 weight calculation of PR661; this incorporates the parameter-line character rather than choosing a trivialization of O(2). Let r_i:Q→H_i be restriction. Section 2 proves that r_1 restricts to isomorphisms r_1,+ :Q_+→H_1 and r_1,− :Q_−→H_1. Consequently

C_a=ker r_1={x−(r_1,−)^{-1}r_1,+(x): x∈Q_+}

is a canonical mixed line. Section 1 and n≠0 prove im n=C_a. This is the intrinsic parity ratio: the canonical isomorphism −(r_1,−)^{-1}r_1,+ between the parity lines. A scalar ratio only exists after generators are chosen and transforms under their rescaling.

The map r_0,+ :Q_+→H_0 is an isomorphism and r_0 vanishes on Q_−. Thus r_0 restricts to an isomorphism C_a→H_0. For any actual pure-line datum y_eta=r_0(q_eta), the entire family is reconstructed intrinsically by

x_eta=(r_0,+)^{-1}(y_eta),
q_eta=x_eta−(r_1,−)^{-1}r_1,+(x_eta).

This determines the projective family from the mixed zero alone, and the actual family from that zero plus its pure-line value. It does not choose a generator of T or remove the unknown actual normal-coordinate scale. The construction is unchanged on transporting [a] around its G-orbit: equivariance implies r_1(q)=0 at one such square if and only if it does at any translate, so C_a is the same subspace of Q throughout that orbit.

## 5. Uniform consequence and an exact orbit certificate

For eta≠0 and every nonzero a'∈A, the full map q_eta(a',−):D_source→P is nonzero. Indeed PR662 applies to the nonzero family q_eta. Explicitly q_eta(a',−)=T_q((a'⊗a')_0), where T_q:D→Hom(D_source,P) is a nonzero equivariant map from an irreducible module, hence injective. The trace-free tensor (a'⊗a')_0 cannot be zero: a nonzero rank-one tensor cannot equal a scalar multiple of a rank-three metric. This argument also covers isotropic a'.

There is a sharper statement at the twelve C5 square directions: the map q_eta(a',−)|K_a' has rank exactly one, with kernel precisely the transported mixed eigenline L_1. This follows at the fixed square because its two-dimensional kernel input space is L_0⊕L_1, the map kills L_1 and is nonzero on L_0. Equivariance transports the conclusion to all twelve directions. This is a rank statement about the already supplied two-input normal-variation restriction, not a new selected-instance evaluation.

## 6. Scope and contribution

The result determines the projective position of the actual lower endpoint NORMAL-VARIATION line in the two-channel space, proves both its parity projections nonzero, and promotes its known one-direction nonzero to full-map nonzero in every parameter direction. The intrinsic reconstruction retains all line twists and actual normal scale.

It does NOT identify the whole original-source endpoint family, assign a numerical channel ratio, determine the rank of the full D→P map, determine its nonsquare secant restriction, prove a fourth Bockstein nonzero, evaluate the next ambient division, or resolve higher lifting or complete repair. The lower P here is not the third-Bockstein P. No comparison with PR663's two axis kernel lines, nor equality/inequality of those lines with C_a, is inferred merely from their mixed parity.

## Sources

- https://github.com/Akilleez-QA/read-em-and-weep/pull/1
- https://github.com/Akilleez-QA/read-em-and-weep/pull/543
- https://github.com/Akilleez-QA/read-em-and-weep/blob/fb574c01207099eeb63960da5cb23ad2f2498a84/research/hm/order-four-quadratic-load/ACTUAL-ENDPOINT-NORMAL-VARIATION-IS-NONZERO.md
- https://github.com/Akilleez-QA/read-em-and-weep/blob/1325647fd916bf2daa71b11efeae6d52cfefa2cd/research/hm/endpoint-square-reconstruction/PROOF.md
- https://github.com/Akilleez-QA/read-em-and-weep/blob/f75a18fd411350adda35dedf18751eee002a39bc/research/hm/endpoint-base-locus-exclusion/PROOF.md
- https://github.com/Akilleez-QA/read-em-and-weep/blob/ad3ab59f6fbbbb3e5bde1da58b3b92a1f49c6889/research/hm/secant-detection-exceptions/PROOF.md
