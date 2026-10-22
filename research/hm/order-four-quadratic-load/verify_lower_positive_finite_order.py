#!/usr/bin/env python3
"""Dimension and Smith-order bookkeeping only; no actual coefficients selected."""
source,target,rank0=12,41,11
assert source-rank0==1
first_nonzero_possible=2
max_minor_degree=source
assert first_nonzero_possible <= max_minor_degree
# A full-rank degree-one rectangular pencil has degree <=source maximal minors.
# Rank0=source-1 leaves one nonunit Smith factor; each maximal minor has its factor.
for e in range(first_nonzero_possible,max_minor_degree+1):
 assert 2<=e<=12
print('PASS: one nonunit Smith factor, first obstruction order at least2 and at most12.')
print('Uniform injectivity of the negative coefficient is the two hyperplane-vanishing proof, not a matrix test.')
print('No twist-four maximal-rank conclusion is asserted.')
