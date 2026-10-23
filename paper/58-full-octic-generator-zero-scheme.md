# The whole canonical octic generator has zero length 46

**Craig Ward · 23 October 2026 · Update through PR1005**

[PR1005](https://github.com/Akilleez-QA/read-em-and-weep/blob/4a50853a6b6a4f18f1a7aac06a90e33e78e7787e/research/hm/source126-typeII-octic-full-zero-scheme/PROOF.md) determines the zero scheme of the entire canonical nonzero octic generator g₈=σψ₄, not merely its target factor. There are **six triple fat points**, each of length six, and **ten simple points**, giving **6·6+10=46**. The generator is nowhere zero on the conic of square quadratics. The actual internal eighth symbol remains an unselected scalar multiple of this generator: a nonzero scalar gives this scheme; a zero scalar gives the identically zero map.

## 1. The source row has exactly six reduced zeros

The unique P-valued cubic covariant c_P has derivative proportional to the original quadratic symbol as a whole polynomial family: both lie in the same one-dimensional equivariant Hom space. Euler's identity puts any cubic basepoint in the already known six-axis rank-drop support. Conversely the order-five stabilizer has no fixed vector in P, forcing a zero at each axis. The known derivative rank two gives an injective projective tangent derivative. Thus the local component ideal is the full maximal ideal, and the six basepoints are reduced.

Where the quotient multiplication b_T is onto, its dual has a local left inverse. Consequently ψ₄=b_T* c_P has exactly the same component ideal as c_P. At the ten exceptional order-three axes, the parameter line carries the sign character of its S₃ stabilizer. The correctly twisted source is D⊗sign, and the rank-three image is sign plus the standard representation. The nonzero cubic value lies in that sign line, on which the invariant pairing is nondegenerate. Hence ψ₄ does not vanish at these ten points. Its zero scheme is precisely the six reduced order-five axes.

## 2. The product ideal distinguishes 46 from 34

In local frames the entries of g₈ are pairwise products of the components of σ and ψ₄, so their ideals multiply. At an order-five axis this gives

    I(g₈)=(u²,v²)(u,v)=(u,v)³.

The quotient has basis 1,u,v,u²,uv,v² and length six. At each order-three axis ψ₄ is nonzero, so the full generator retains the target factor's simple zero. There are no further points. In particular both factors, and therefore the whole generator, are nonzero everywhere on the square conic.

The earlier [target-section result](56-octic-target-zero-scheme.md) remains valid: σ alone has length34, with six length-four complete intersections and ten simple points. It was not a computation of g₈. The old original-second six-axis rank theorem is an input here, not a newly counted result.

## 3. Remaining boundary and evidence

This computes a universal canonical generator, not the actual eighth scalar or any actual HM instance. It does not contradict the original generic all-orders vanishing under full-J Type II compatibility, decide later internal orders, or exclude a source-dual pair. The necessary frontier stays four pairs across three labels.

The complete proof has independent review and 53 checks in both normal and optimized Python. The certificate covers authenticated inputs, representation multiplicities, the sign-twisted stabilizer calculation, and local product ideals. It supports the written proof rather than certifying the entire dependency chain in a proof assistant.
