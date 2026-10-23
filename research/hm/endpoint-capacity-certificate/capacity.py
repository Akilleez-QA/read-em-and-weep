"""Exact universal two-height capacity. No geometric instance is evaluated."""


def integer(x, name):
    if type(x) is not int:
        raise ValueError(name + ' must be an integer, not bool')
    return x


def parameters(n, l1, l2):
    for x, name in ((n, 'rank'), (l1, 'lambda1'), (l2, 'lambda2')):
        integer(x, name)
    if n < 1 or l1 < l2:
        raise ValueError('require rank >= 1 and lambda1 >= lambda2')
    return (n + 1) // 2, n, l1 - l2 + 2 * n, n * l2 - n * n - n


def value(n, l1, l2, h):
    lo, hi, b, c = parameters(n, l1, l2)
    integer(h, 'height')
    if not lo <= h <= hi:
        raise ValueError('inadmissible height')
    return -2 * h * h + b * h + c


def solve(n, l1, l2):
    lo, hi, b, c = parameters(n, l1, l2)
    clip = lambda h: max(lo, min(hi, h))
    candidates = sorted({clip(b // 4), clip(b // 4 + 1)})
    maximum = max(value(n, l1, l2, h) for h in candidates)
    heights = [h for h in candidates if value(n, l1, l2, h) == maximum]
    h = heights[0]
    return dict(rank=n, lambda1=l1, lambda2=l2, maximum=maximum,
                heights=heights, square_distance=(4*h-b)**2)


def verify(cert):
    """Check completeness via strict concavity, without calling solve/enumerating."""
    keys = {'rank', 'lambda1', 'lambda2', 'maximum', 'heights', 'square_distance'}
    if type(cert) is not dict or set(cert) != keys:
        raise ValueError('invalid certificate fields')
    n, l1, l2 = (cert[k] for k in ('rank', 'lambda1', 'lambda2'))
    lo, hi, b, c = parameters(n, l1, l2)
    m = integer(cert['maximum'], 'maximum')
    distance = integer(cert['square_distance'], 'square distance')
    hs = cert['heights']
    if type(hs) is not list or not 1 <= len(hs) <= 2:
        raise ValueError('one or two optimizers required')
    for h in hs:
        integer(h, 'height')
        if not lo <= h <= hi or value(n, l1, l2, h) != m:
            raise ValueError('invalid optimizer/value')
        if (4*h-b)**2 != distance or 8*m != b*b + 8*c - distance:
            raise ValueError('invalid completed-square identity')
    if hs != sorted(set(hs)) or (len(hs) == 2 and hs[1] != hs[0] + 1):
        raise ValueError('optimizers must be distinct consecutive ordered heights')
    # Strict outside differences ensure no omitted tie and no higher value.
    if hs[0] > lo and b - 4*(hs[0]-1) - 2 <= 0:
        raise ValueError('left optimality/completeness fails')
    if hs[-1] < hi and b - 4*hs[-1] - 2 >= 0:
        raise ValueError('right optimality/completeness fails')
    return True


def classify_degree(cert, degree):
    """Conclusions are conditional on the caller's geometric capacity bound."""
    verify(cert)
    integer(degree, 'degree')
    return ('excluded_above_capacity' if degree > cert['maximum'] else
            'attains_capacity' if degree == cert['maximum'] else 'below_capacity_no_exclusion')


def equality_filter(cert, degree, initial_top, *, actual_top_flags_proved=False):
    """Caller must supply geometric proof; this function cannot authenticate it.

    Only equality optimizers are filtered. This NEVER lowers global capacity.
    The hypothesis includes top(F_h)=lambda1-2h, even for equal heights.
    """
    verify(cert)
    integer(initial_top, 'initial top')
    if actual_top_flags_proved is not True:
        raise ValueError('separate proof of actual top flags is required')
    if classify_degree(cert, degree) != 'attains_capacity':
        raise ValueError('strict-top filtering is equality-only')
    lower = cert['lambda1'] - initial_top
    hs = [h for h in cert['heights'] if h >= lower]
    return dict(conditional_on_proved_actual_top_flags=True, threshold=lower,
                surviving_heights=hs, excluded_equality=not hs,
                unfiltered_capacity=cert['maximum'])
