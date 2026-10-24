# Reproduce the fixed positive-pair checks

From this directory:

    python verify.py > RESULT.replay.json
    python -O verify.py > RESULT.optimized.replay.json
    cmp RESULT.json RESULT.replay.json
    cmp RESULT.replay.json RESULT.optimized.replay.json
    python review_verify.py > REVIEW-RESULT.replay.json
    python -O review_verify.py > REVIEW-RESULT.optimized.replay.json
    cmp REVIEW-RESULT.json REVIEW-RESULT.replay.json
    cmp REVIEW-RESULT.replay.json REVIEW-RESULT.optimized.replay.json

The author checker uses the physical McKay recurrence, itself authenticated against exact characters in characters.py. It checks only the two specified quotients, seven individual irreducible tail atoms under the proved eight-dimensional H1 budget, six written tail partitions, fixed Hom spaces and rank/degree consequences. Its semantic controls change the orbit-size bound, sextic representation, target V multiplicity, endpoint rank cap, cotangent twist and scalar-tail H1 contribution. No global bundle candidate domain, actual map instance or historical enumeration is used.

The independent checker uses closed binary-icosahedral class characters over Q(sqrt(5)), not the author's recurrence. It binds the exact reviewed proof hash and independently checks the displayed representation facts, source identities and rank/degree arithmetic. REVIEW-AUTHENTICITY.json records its fresh full-byte authentication of all five immutable GitHub source originals. REVIEW-INDEPENDENT.md reviews the actual sheaf maps, saturation and connection arguments mathematically; neither checker is a proof-assistant certification of the imported geometric premises.

The conclusion concerns exactly the two decomposable positive quotient parts. It forces the common K and the actual sheaf image F(-2), with zero negative component, identifies K^-, K^+=E0 and E0^-=K, and proves the adjacent graded derivative isomorphism. It does not exclude either quotient, assert its realization, treat the triplet-positive form, set the original determinant defect to zero, or transfer a rank-seventeen rank-three theorem to the rank-sixteen E0.
