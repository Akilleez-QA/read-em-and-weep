# Linear spaces in a Grassmannian

Let S be a vector space and Z=P^s a projective linear space contained in the Plücker embedding of Gr(m,S), with s>=1. Then either all the represented m-planes contain a fixed (m-1)-plane, or they all lie in a fixed (m+1)-plane. Consequently their sum has dimension at most m+s.

Here is a proof. Two distinct m-planes whose entire Plücker line lies in the Grassmannian intersect in dimension m-1. To verify this standard line criterion directly, factor out their common intersection of dimension a. Their Plücker vectors become decomposable (m-a)-vectors on two disjoint spaces. If m-a>=2, the sum of those two vectors is not decomposable: the contraction span (the span of all contractions by (m-a-1)-forms) has dimension 2(m-a), whereas the contraction span of a nonzero decomposable (m-a)-vector has dimension m-a. Thus m-a=1.

Choose two distinct represented planes A,B, and put T=A intersect B and H=A+B. Every other represented plane C intersects both in codimension at most one. If C does not contain T, then C intersect A and C intersect B are distinct hyperplanes in C; their sum is C and lies in H. Thus each C either contains T or lies in H. If one C contains T but is not contained in H, then C intersect H=T. Any represented D contained in H but not containing T would meet C in dimension at most m-2, contradicting the line criterion. Therefore the family is entirely of one of the two asserted types.

For the family containing T, wedge with a fixed generator of det T identifies the Plücker linear space with a projective linear space of lines in S/T. Their span has dimension s+1, and the sum of the m-planes has dimension m+s. For the family contained in H, their sum has dimension at most m+1<=m+s.


For s=0 the family is a single m-plane, whose span has dimension m. This universal lemma requires no HM-instance computation.
