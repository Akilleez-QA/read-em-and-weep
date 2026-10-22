# Explicit Hessian constants in the canonical harmonic splitting

## Universal correction

Use the harmonic lift L and first-order product B from UNIVERSAL-FIRST-NORMAL-HARMONIC-PRODUCT-AND-OPERATOR-RESIDUE.md. For arbitrary binary f,g of degrees3,5 put

    n=[[fg,-f²],[g²,-fg]],
    T_can=[[mix(Hf,Hg)/112, -det(Hf)/20],
           [det(Hg)/144, -mix(Hf,Hg)/112]].

Then

    (L(n)+q L(T_can))²=0 mod q².                    (1)

These are the explicit constants needed to convert the Euler-Gram Hessian lift to the harmonic splitting. This does not remove the quintic-generator cochain correction or the actual midpoint matching requirements.

## Proof of the splitting conversion

For odd degrees p,r, form the Euler-Gram pairing

    Gram(f,g)=(grad f/p)^t C (grad g/r),

using harmonic lifts of its even gradient entries. Its restriction to q=0 is fg. Its first normal difference is the universal identity

    Gram(f,g)=L(fg)+q L((f,g)_2/[2pr(p+r-1)]) mod q². (2)

Apply the Laplacian and restrict to the cone. By SL2 equivariance the resulting bilinear map is a scalar multiple of the unique second-transvectant channel. Testing f=u^p, g=v^r gives scalar 1/(4pr) before dividing by the factor (p+r-1)/2 from the q-times-harmonic term. This proves (2) in all odd degrees greater than one.

For (p,r)=(3,5), the three conversion constants for f², fg, g² are1/90,1/210,1/450. Since (f,f)_2=2detHf and (g,g)_2=2detHg, adding the Euler-Gram correction to the earlier Hessian correction gives

    1/240+1/210=1/112,
    -1/36-2/90=-1/20,
    1/400+2/450=1/144.

This proves (1). Equivalently, its scalar first-normal square is the universal zero polynomial

    B(fg,fg)-B(f²,g²)
      +2fg mix(Hf,Hg)/112
      -f² detHg/144-g² detHf/20=0.                  (3)

## What to retain in an actual calculation

If q0=nu q, the correction relative to q0 is T_can/nu. The corrected actual symbol also includes the unique primitive of the previously computed quintic-generator residue, expressed in the same splitting. Neither nu nor that primitive may be dropped. The local operator formula must still be taken through the global connecting map modulo H0(G(4)); a nonzero local degree-eight expression alone is not a nonzero third Bockstein.

## Reproduction

Run verify_harmonic_hessian_nilpotent.py. It expands (3) with all four cubic and all six quintic coefficients independent indeterminates. This is a universal polynomial identity, not a selected source instance or rank evaluation.
