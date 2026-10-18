"""Only one-variable rational identities; no physical imports or evaluation."""
import argparse
import sympy as S
x,t=S.symbols('x t')
s=1-t*t
rf=(x*x+1)/(2*x*(x*x-1))
ga=1/(x*(x*x-1))
checks={
 'square_root_identification': (x**3-x)/x**2-(1-x**-2)*x,
 'frame_log_derivative': (3*x*x-1)/(2*(x**3-x))-1/x-rf,
 'half_old_connection': S.diff(1-x**-2,x)/(2*(1-x**-2))-ga,
 'transported_old_difference': ga-rf+1/(2*x),
 'infinity_connection': ga.subs(x,1/t)*(-1/t**2)+t/s,
 'infinity_dlogx': (1/x).subs(x,1/t)*(-1/t**2)+1/t,
 'infinity_log_refined_frame': rf.subs(x,1/t)*(-1/t**2)+(1+t*t)/(2*t*s),
 'infinity_normalized_bit1_log': rf.subs(x,1/t)*(-1/t**2)+1/(2*t)+t/s,
 'infinity_bit1_square': t*((x**3-x)/x**2).subs(x,1/t)-s,
 'alpha_after_y_equals_z_over_t2': ga.subs(x,1/t)/t**2-t/s,
 'q_after_y_equals_z_over_t2': (1/x).subs(x,1/t)/t**2-1/t,
 'connection_difference_after_contraction': t/s-(1+t*t)/(2*t*s)+1/(2*t),
}

# All expressions are coefficients of one-curve formal rational identities.
checks.update({
 'infinity_tangent_derivation': 2*((3*t*t-1)/2)+(1-3*t*t),
 'infinity_vector_from_finite': ((3*x*x-1)/(2*x*x)-2*(x**3-x)/x**3).subs(x,1/t)-(3*t*t-1)/2,
 'infinity_connection_in_n_frame': -t/s-S.diff(s,t)/s-t/s,
 'bit0_normalized_ratio': S.diff(t,t)/(2*t)-1/(2*t),
})
negative={
 'reversed_A_sign': ga-rf-1/(2*x),
 'omit_common_frame_subtraction': ga+1/(2*x),
 'replace_q_by_dlog_nu': ga-rf+rf/2,
 'reset_gamma1_to_zero': -rf+1/(2*x),
 'reverse_squared_transition': (x**3-x)/x**2-(1-x**-2)/x,
 'reverse_infinity_V_sign': -t/s+(1+t*t)/(2*t*s)+1/(2*t),
 'reset_infinity_connection': t/s,
 'use_zero_n_infinity_connection': t/s,
 'omit_V_z_component': 1-3*t*t,
}
def require_zero(name,value):
    if S.cancel(value)!=0:
        raise RuntimeError('Identity failed: '+name)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--inject-wrong-sign',action='store_true',help='Must fail even under python -O.')
    args=parser.parse_args()
    for name,value in checks.items():
        require_zero(name,value)
    for name,value in negative.items():
        try:
            require_zero(name,value)
        except RuntimeError:
            pass
        else:
            raise RuntimeError('Negative control was accepted: '+name)
    if args.inject_wrong_sign:
        require_zero('injected_reversed_A_sign',negative['reversed_A_sign'])
    print('PASS:',len(checks),'one-curve rational identities;',len(negative),'wrong variants rejected.')
    print('No physical model, source owner, jet, residual, production import, or product matrix evaluated.')
if __name__=='__main__':
    main()
