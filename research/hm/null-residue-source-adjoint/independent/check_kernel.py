"""Free differential symbols only: differentiate every complete-kernel factor."""
import sympy as S
import json
x=S.symbols('x')
labels=['test','frame','outer1','outer2','outer3','outer4','outer5','HPL','selector','current']
factors=[S.Function(label)(x) for label in labels]
s=S.Function('raw_leaf')(x)
kernel=S.prod(factors)
flux=kernel*s
remainder=-S.diff(kernel,x)*s
if S.expand(kernel*S.diff(s,x)-S.diff(flux,x)-remainder)!=0:raise ValueError('complete kernel')
for j,label in enumerate(labels):
    missing=-sum(S.diff(f,x)*S.prod(factors[:i]+factors[i+1:])*s for i,f in enumerate(factors) if i!=j)
    if S.expand(kernel*S.diff(s,x)-S.diff(flux,x)-missing)==0:raise ValueError('lost derivative '+label)
print(json.dumps({'status':'PASS','generic_product_identity':1,'dropped_factor_negative_controls':len(labels),'physical_evaluations':0},sort_keys=True))
