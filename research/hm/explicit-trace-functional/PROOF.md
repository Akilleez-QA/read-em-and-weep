# The descended trace functional has an explicit first-ideal formula

## Assumptions and pinned inputs

Let k=C(L), S=k[X,Y], f∈S3, g∈S5 a regular pair, and u∈k×. Put n=u[[fg,−f²],[g²,−fg]]. Fix the canonical first-normal lift

    T=[[u τ2(f,g)/112, −u Hess(f)/20],
       [u Hess(g)/144, −u τ2(f,g)/112]].

Here Hess(p)=p_XX p_YY−p_XY² and τ2(p,r)=p_XX r_YY−2p_XY r_XY+p_YY r_XX. All claims are universal identities for arbitrary such forms, not evaluations of actual coefficients or selected models.

Pinned dependencies:
- [PR718, 2411fcd92acd738d0d8af7bebc79ee9191b276ef](https://github.com/Akilleez-QA/read-em-and-weep/blob/2411fcd92acd738d0d8af7bebc79ee9191b276ef/research/hm/trace-obstruction-target-reduction/PROOF.md): B1(p_d,r_e)=τ2(p,r)/(2(d−1)(e−1)(d+e−1)), and Ψ kills the trace kernel modulo f.
- [PR724, 2061379fe77ec4c82b5f05c7a11d3b7454b97a04](https://github.com/Akilleez-QA/read-em-and-weep/blob/2061379fe77ec4c82b5f05c7a11d3b7454b97a04/research/hm/canonical-trace-isomorphism/PROOF.md): the displayed canonical T is first-normal nilpotent.
- [PR725, 397c7473691a08a839ccf7e9abeed06002b48bab](https://github.com/Akilleez-QA/read-em-and-weep/blob/397c7473691a08a839ccf7e9abeed06002b48bab/research/hm/modular-vertex-elimination/PROOF.md): τ:M4→S12 is surjective with kernel {ell[[f/2,0],[g,−f/2]]:ell∈S1}.
- [PR729, c384ae419983a5031af19c37674df020de1aa5da](https://github.com/Akilleez-QA/read-em-and-weep/blob/c384ae419983a5031af19c37674df020de1aa5da/research/hm/firstnormal-scalar-slope/PROOF.md), equation (10): exact cubic factorization.
- [PR747, 0a0ee30a5142477e54245b7c6f22d561abb4f5f1](https://github.com/Akilleez-QA/read-em-and-weep/blob/0a0ee30a5142477e54245b7c6f22d561abb4f5f1/research/hm/source-family-fourth-square-exclusion/PROOF.md): source linearity and fixed-frame interpretation.

For D=[[x,y],[z,−x]] with entries of degrees 4,2,6 define

    τ(D)=u(2fgx+g²y−f²z),
    Ψ(D)=sc(TD+DT+B1(n,D)+B1(D,n)),
    V=(S/(f))8.

The first and third inputs imply a unique k-linear map ℒ:S12→V such that ℒ(τ(D))=[Ψ(D)]. This quotient-space descent is an input reduction, not the new theorem.

## 1. New first-ideal formula

For every r∈S9,

    ℒ(f r)=[τ2(f,r)]/352.                              (1)

In particular this restriction is independent of g and u, despite the definition of ℒ involving both.

Proof. A trace solution for e=f r has y=0: reducing τ(D)=fr modulo f and using regularity forces f|y, whence y=0 by degree. Therefore choose x∈S4,z∈S6 with

    2u g x−u f z=r.                                    (2)

Existence follows from trace surjectivity. For this D, entrywise scalar extraction gives

    Ψ(D)=2Tdiag x+2u B1(fg,x)+Tupper z−u B1(f²,z).       (3)

For a purely formal verification choose an SL2 coordinate chart with X coprime to f, put t=Y/X, and write F,G,x,z,r for dehomogenizations. This is an abstract frame choice to prove a polynomial congruence, not an actual-point evaluation. Use

    τ2(p_d,r_e)(1,t)=d(d−1)P R″−2(d−1)(e−1)P′R′+e(e−1)P″R.

The diagonal contribution in (3), modulo F, is

    u((9/22)F″Gx−(2/11)F′G′x−(2/11)F′Gx′).

Indeed the T term contributes u((5/14)F″G−(2/7)F′G′)x and the B1 term contributes u((4/77)F″Gx+(8/77)F′G′x−(2/11)F′Gx′). The lower contribution is

    u F′² z/11,

because Tupper≡uF′²/5 and τ2(f²,z)≡60F′²z while B1(f²,z)=τ2(f²,z)/550.

Differentiate (2) formally and reduce modulo F:

    uF′z=2uG′x+2uGx′−r′.

Substitution in (3) cancels both terms involving G′x and Gx′. Reducing (2) itself gives uGx=r/2, so

    Ψ(D)≡(9F″r−4F′r′)/44 mod F.

On the other hand τ2(f,r)≡72F″r−32F′r′ mod F because the degrees are 3 and 9. This proves (1) in the affine quotient. Both original sides have homogeneous degree eight. Since X is coprime to f, homogenization and cancellation of powers of X prove the global congruence. No square-free assumption was used. QED.

## 2. One modular division computes the entire functional

For any e∈S12 let t_e∈S2 be the unique solution of

    [g²t_e]=[e] in (S/(f))12.

Existence and uniqueness are exactly the graded isomorphism in PR725. Set r_e=(e−g²t_e)/f∈S9. Then

    ℒ(e)=[Hess(g)t_e/144+τ2(g²,t_e)/198+τ2(f,r_e)/352]. (4)

Proof. For e0=g²t_e use the upper-triangular matrix D0 with y=t_e/u and x=z=0. Its trace is e0 and

    Ψ(D0)=Hess(g)t_e/144+B1(g²,t_e).

The B1 denominator for degrees 10 and 2 is 198. Add (1) for the remaining e−e0=f r_e. QED.

Thus the old two-stage trace representative is unnecessary for this descended functional: the second modular division and the degree-four representative disappear. Formula (4) is a universal construction, not an execution of a coefficient calculation on the actual pair.

## 3. Second-ideal symbol and finite thickening

For every z∈S6,

    ℒ(f²z)=[Hess(f)z]/44.                              (5)

This follows from (1): τ2(f,fz)≡−32F′²z mod F, whereas Hess(f)≡−4F′² mod F. Consequently

    ℒ(f³S3)=0,

so ℒ factors through S12/f³S3. Its restriction to the last filtration piece

    f²S6/f³S3 ≅ (S/(f))6

is multiplication by Hess(f)/44 into V. The source quotient S12/f³S3 has dimension 13−4=9.

After extending scalars to an algebraic closure, the rank of this last restriction is 3,1,0 according as the cubic divisor has multiplicity type (1,1,1), (2,1), or (3). To see this without a selected model, work in a chart avoiding the cubic divisor at infinity and use Hess(f)≡−4F′² mod F. At each root of multiplicity m, F′ has order m−1 in characteristic zero. The common divisor of F and F′² has degree sum min(m,2m−2). The rank of multiplication on k[t]/(F) is three minus this degree, giving the stated alternatives. Rank is unchanged by field extension. In particular square-free f implies ℒ itself is surjective. These are conditional universal ranks, not evaluation of which multiplicity type or rank the actual f has.

## 4. Lift transport and the unresolved actual source map

The full operator above uses T_can. This must not silently be identified with an actual fixed-frame T. By [PR717, 7362df9da60a3b87b3200078a0145a376cc3056b](https://github.com/Akilleez-QA/read-em-and-weep/blob/7362df9da60a3b87b3200078a0145a376cc3056b/research/hm/nilpotent-trace-lift-invariance/PROOF.md), any other first-normal nilpotent lift has the form

    T'=T_can+ell A0,     A0=[[f/2,0],[g,−f/2]], ell∈S1.

For D=[[x,y],[z,−x]], its change in Ψ is ell(fx+gy). Since e=τ(D)≡u g²y modulo f, the exact transport law is

    ℒ_T'(e)=ℒ_can(e)+[ell e/(u g)].                    (6)

Division by g here means the inverse of multiplication by g in the graded quotient S/(f), legitimate by regularity; the total degree is 1+12−5=8. In particular the first-ideal formula (1), second-ideal symbol (5), and f³-annihilation hold for every such T'. The full formula (4) requires the additional term in (6).

Use consistent data N'=n+qT', N'*N'=q²d2' Id+q³d3' Id+O(q4), and V_h'=[q³](h*N'). PR729/747 give

    K_T'(h)=[h d3'+B1(h,d2')−tr(nV_h')]
             −ℒ_can(h d2')−[ell h d2'/(u g)].         (7)

There is also a degree-based simplification: V_h' has weight zero, so its upper entry has degree −2 and vanishes. The other terms of tr(nV_h') have factors fg or f². Hence tr(nV_h') is divisible by f, and this term may be dropped from (7). This argument uses polynomial harmonic coefficients, not a localized rational matrix substitute.

Formula (4) explicitly resolves the previously implicit ℒ_can term using just the unique degree-two residue representative of h d2'/g² modulo f, and (6) supplies the exact lift correction. Formula (1) supplies the entire first-ideal restriction, and (5) its second-ideal symbol. These are new operator identities, not a conclusion from nonzero d=[d2']. No coefficient ell of the actual lift has been evaluated.

No inference that image(K_T') is or is not contained in k d follows: the remaining terms of (7) can still cancel ℒ_can(hd2') and its correction, and h d2' is not an arbitrary element of S12. Nor does surjectivity of ℒ imply surjectivity of K. The common-direction certificate in PR761, values at selected actual source pairs, beta4, and algebraicity remain undecided by this note. No actual f,g,h, source point, derivative, matrix, or rank was selected or evaluated; the proof consists only of bounded formal differential identities and graded linear algebra.
