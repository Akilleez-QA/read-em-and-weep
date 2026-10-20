# Verified source inventory

Retrieved 2026-10-19. Public source URLs and reference checks follow. PROOF.md contains original deductions, not a reproduction of these papers.

1. Paola Bonacini, *On the plane section of an integral curve in positive characteristic*, arXiv:1009.4021v1 (2010).
   URL: https://arxiv.org/pdf/1009.4021
   SHA256: c4c4a957ca2ef8d70c70937538bc87610a2ef1c51e60faca4e3e73ee4f34a9e5
   Checked: Theorem 2.4, page 3, explicitly covers integral curves in P3 in characteristic zero. Reference [7] is J. Harris, *The genus of space curves*, Math. Ann. 249 (1980), 191–204; the theorem is attributed to its Section 2. Thus singular integral curves are included, not only smooth curves.

2. Rosa M. Miro-Roig, *Complete intersection liaison and Gorenstein liaison: new results and open problems*, Le Matematiche 55, fasc. II, 319–337.
   URL: https://lematematiche.dmi.unict.it/index.php/lematematiche/article/download/275/252/1043
   SHA256: c9b4e175d24f08dc97a7264b3f7b7a1cdc0ba6c8bdd024bd6785e48c328168c3
   Checked: Theorem/Definition 4.13 on printed page 331 explicitly bounds the arithmetic genus of integral nondegenerate curves. Formula gives pi(10,4)=9. The paragraph also states maximal-genus curves are ACM, but our proof does not use that stronger assertion.

3. Joe Harris, *Interpolation*, MSRI Publications 59 (2011), printed pages 165 ff.
   URL: https://library.slmath.org/books/Book59/files/60harris.pdf
   SHA256: 5110e37c297e6534690b91bae704e484e49462d2697446561a313ec1287e96b0
   Checked: Theorem 2.1, page 167, provides the elementary lower bound for the Hilbert function of points in linear general position. Page 168 explicitly states uniform position for general hyperplane sections of irreducible curves. This is corroboration by the original theorem's author. Our proof supplies the elementary bound and the genus summation directly.
   Caution: the intermediate displayed first-difference inequality on printed page 168 has its sign reversed. The correct direction is h_C(m)-h_C(m-1) >= h_Γ(m). Our coordinate-ring proof proves that direction explicitly and does not rely on the misprinted inequality.
