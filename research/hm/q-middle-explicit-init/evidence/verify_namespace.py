"""Guarded universal namespace equivalence only; no family or sparse execution."""
import ast
import argparse
import builtins
import dis
import hashlib
import importlib.util
import inspect
import json
import platform
import sys
from pathlib import Path
from types import CodeType, FunctionType, ModuleType

if not __debug__:
    raise RuntimeError("Run without -O; comparison and provenance checks require assertions.")
HERE=Path(__file__).resolve().parent
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--package',type=Path,default=HERE.parent,help='Directory containing initializer.py (default: parent of this evidence directory).')
parser.add_argument('--payload',type=Path,help='Frozen PR810 payload directory (default: sibling q-middle-candidate-interface).')
parser.add_argument('--check-layout',action='store_true',help='Verify file hashes only, then exit before symbolic imports.')
args=parser.parse_args()
PACKAGE=args.package.resolve()
PAYLOAD=(args.payload or PACKAGE.parent/'q-middle-candidate-interface').resolve()
EXPLICIT=PACKAGE/'initializer.py'
PINS=json.loads((HERE/'pins.json').read_text())
ROOTS={'package':PACKAGE,'payload':PAYLOAD,'reference':HERE}

def verify_pins():
    for item in PINS['inputs']:
        path=ROOTS[item['role']]/item['path']
        assert hashlib.sha256(path.read_bytes()).hexdigest()==item['sha256'], (item['role'],item['path'])

verify_pins()
if args.check_layout:
    print(json.dumps({'status':'metadata_layout_pass','input_count':len(PINS['inputs']),'symbolic_imports':False,'mathematical_verification':False},sort_keys=True))
    raise SystemExit(0)
assert sys.version_info[:2]==(3,12), 'The authenticated AST metadata requires Python 3.12.'
assert __debug__
import sympy as s
import mpmath
assert s.__version__=='1.14.0' and mpmath.__version__=='1.3.0', 'Use the reviewed dependency versions.'

FORBIDDEN={'build_symbols','source_map','iter_coefficients','middle_apply','graded_module','build_module'}
def profile(frame,event,arg):
    if event=='call' and frame.f_code.co_name in FORBIDDEN:
        raise AssertionError('Forbidden family/job call: '+frame.f_code.co_name)
sys.setprofile(profile)

def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

candidate_module=load('candidate_explicit_namespace',EXPLICIT)
candidate=candidate_module.build_namespace(PAYLOAD)
reference_module=load('review_reference_namespace',HERE/'reference_namespace.py')
reference=vars(reference_module)

# Compare the exact authenticated statements against both explicit and global
# reference harness ASTs before accepting any runtime agreement.
def adigest(nodes):
    return hashlib.sha256('\n'.join(ast.dump(n,include_attributes=False) for n in nodes).encode()).hexdigest()
explicit_ast=ast.parse(EXPLICIT.read_text())
functions={n.name:n for n in explicit_ast.body if isinstance(n,ast.FunctionDef)}
reference_ast=ast.parse((HERE/'reference_namespace.py').read_text()).body
offset=4; candidate_offset=5
for segment in PINS['reference_segments']:
    name=segment['path']
    source=ast.parse((PAYLOAD/name).read_text()).body[segment['start']:segment['stop']]
    assert adigest(source)==segment['ast_sha256']
    if name=='universal_complete_w_action_symbols.py':
        assert adigest(ast.parse((HERE/'reference_complete.py').read_text()).body[2:])==adigest(source)
        assert adigest(functions['_complete_symbols'].body[1:-1])==adigest(source)
        continue
    if name.startswith('derive_'):
        offset+=2; candidate_offset+=1
    count=len(source)
    assert adigest(reference_ast[offset:offset+count])==adigest(source)
    assert adigest(functions['build_namespace'].body[candidate_offset:candidate_offset+count])==adigest(source)
    offset+=count; candidate_offset+=count

PLUMBING={'root','__name__','__doc__','__package__','__loader__','__spec__','__file__','__cached__','__builtins__','_review_complete'}
stats={'scalar_comparisons':0,'matrix_comparisons':0,'container_comparisons':0,'function_binding_checks':0,'probes':0,'algebraic_fallbacks':0}
inventories={};bindings={};differences=[]

def filtered(namespace):
    return {k:v for k,v in namespace.items() if k not in PLUMBING}

def same(a,b,path):
    if isinstance(a,FunctionType) or isinstance(b,FunctionType):
        assert isinstance(a,FunctionType) and isinstance(b,FunctionType), path
        assert a.__name__==b.__name__, path
        return
    if isinstance(a,ModuleType) or isinstance(b,ModuleType):
        assert a is b, path
        return
    assert type(a) is type(b), (path,type(a).__name__,type(b).__name__)
    if isinstance(a,dict):
        stats['container_comparisons']+=1
        assert set(a)==set(b),(path,'dictionary keys')
        for k in a: same(a[k],b[k],path+'.'+str(k))
    elif isinstance(a,(tuple,list)):
        stats['container_comparisons']+=1
        assert len(a)==len(b),(path,'length')
        for i,(x,y) in enumerate(zip(a,b)):same(x,y,path+'[%d]'%i)
    elif isinstance(a,s.MatrixBase):
        stats['matrix_comparisons']+=1
        assert a.shape==b.shape,(path,'shape')
        for i,(x,y) in enumerate(zip(a,b)):same(x,y,path+'[%d]'%i)
    elif callable(a):
        assert a is b,path  # Shared imported math/itertools callables.
    else:
        stats['scalar_comparisons']+=1
        if isinstance(a,s.Symbol):
            assert a.name==b.name and a.assumptions0==b.assumptions0,path
        if a!=b:
            assert isinstance(a,s.Basic) and isinstance(b,s.Basic),(path,a,b)
            stats['algebraic_fallbacks']+=1
            assert s.cancel(s.expand(a-b))==0,path

def describe(value):
    if isinstance(value,FunctionType):return {'type':'function','name':value.__name__}
    if isinstance(value,ModuleType):return {'type':'module','name':value.__name__}
    if isinstance(value,s.MatrixBase):return {'type':type(value).__name__,'shape':list(value.shape),'entries_sha256':hashlib.sha256(s.srepr(value).encode()).hexdigest()}
    if isinstance(value,dict):return {'type':'dict','length':len(value)}
    if isinstance(value,(tuple,list)):return {'type':type(value).__name__,'length':len(value)}
    if isinstance(value,s.Symbol):return {'type':'Symbol','name':value.name,'assumptions':value.assumptions0}
    if callable(value):return {'type':type(value).__name__,'name':value.__name__}
    return {'type':type(value).__name__,'repr_sha256':hashlib.sha256(repr(value).encode()).hexdigest()}

def dependencies(fn):
    # New lexical functions can capture a name solely to pass it into a nested
    # lambda; frozen globals appear only in that lambda's code. Walk both.
    cells={name:cell.cell_contents for name,cell in zip(fn.__code__.co_freevars,fn.__closure__ or ())}
    out={}
    def walk(code):
        for ins in dis.get_instructions(code):
            name=ins.argval
            if ins.opname in ('LOAD_GLOBAL','LOAD_NAME'):
                if name in fn.__globals__:out[name]=fn.__globals__[name]
                elif hasattr(builtins,name):out[name]=getattr(builtins,name)
                else:raise AssertionError(('unbound global',fn.__name__,name))
            elif ins.opname=='LOAD_DEREF' and name in cells:
                out[name]=cells[name]
        for value in code.co_consts:
            if isinstance(value,CodeType):walk(value)
    walk(fn.__code__)
    return out

def compare_namespace(a,b,label):
    aa,bb=filtered(a),filtered(b)
    assert set(aa)==set(bb),(label,'namespace keys',sorted(set(aa)-set(bb)),sorted(set(bb)-set(aa)))
    inventories[label]={k:describe(v) for k,v in sorted(aa.items())}
    for k in aa:
        if k=='ns':
            compare_namespace(aa[k],bb[k],label+'.ns')
        else:same(aa[k],bb[k],label+'.'+k)
    for k,fn in aa.items():
        if not isinstance(fn,FunctionType):continue
        af=inspect.getclosurevars(fn);bf=inspect.getclosurevars(bb[k])
        adeps=dependencies(fn)
        bdeps=dependencies(bb[k])
        assert set(adeps)==set(bdeps),(label,k,'dependency names',sorted(adeps),sorted(bdeps))
        for dep in adeps:same(adeps[dep],bdeps[dep],label+'.'+k+'->'+dep)
        bindings[label+'.'+k]={'dependencies':sorted(adeps),'candidate_nonlocals':sorted(af.nonlocals),'reference_globals':sorted(bf.globals)}
        stats['function_binding_checks']+=1

compare_namespace(candidate,reference,'outer')
for missing in ('rq_symbols','rh_symbols','Theta','sol','pars','Q6','spsol'):
    assert missing not in candidate and missing not in reference

def probe(label,fun):
    same(fun(candidate),fun(reference),'probe.'+label)
    stats['probes']+=1

for j in range(2):
    for name in ('A','B','Bcoef'):
        probe('%s_basis%d'%(name,j),lambda n,name=name,j=j:n[name](s.eye(2)[:,j]))
for name in ('A','B','Bcoef'):
    probe(name+'_free_spinor',lambda n,name=name:n[name](n['p']))
for j in range(6):
    probe('p_roundtrip%d'%j,lambda n,j=j:n['getp'](n['putp'](s.eye(6)[:,j])))
    probe('Y_roundtrip%d'%j,lambda n,j=j:n['getY'](n['putY'](s.eye(6)[:,j],(3,)),(3,)))
u0,u1=s.symbols('review_form_u0 review_form_u1')
f={(0,):u0,(3,):u1};g={(1,2):u1,(2,4):u0}
probe('exterior_add',lambda n:n['add'](f,n['scale'](u0,f)))
probe('exterior_wedge',lambda n:n['wedge'](f,g))
probe('exterior_contract',lambda n:n['contract'](n['coords'],g))
probe('exterior_pair',lambda n:n['pair']([f,f],[g,n['scale'](u0,g)]))
for i in range(4):
    for name in ('DD','NN'):
        probe('%s_cubic%d'%(name,i),lambda n,name=name,i=i:n[name](n['mons'][i]))
for name in ('DD','NN'):
    probe('rep_'+name,lambda n,name=name:n['rep'](n[name]))
g0=s.symbols('review_quartic0:5')
def quartic(n):
    nn=n['ns'];return sum(c*m for c,m in zip(g0,nn['mon'](4)))
probe('complete_coeff',lambda n:n['ns']['coeff'](quartic(n),4))
probe('complete_tv',lambda n:n['ns']['tv'](quartic(n),quartic(n),2))
probe('complete_op4',lambda n:n['ns']['op4'](quartic(n)))
probe('complete_quartic',lambda n:n['ns']['quartic'](n['ns']['op4'](quartic(n))))
probe('complete_monomials',lambda n:[n['ns']['mon'](i) for i in range(5)])

# Negative checks prove value and lexical-dependency comparisons are sensitive.
bad=dict(reference);bad['theta']=s.Symbol('theta')
try:compare_namespace(candidate,bad,'negative_symbol')
except AssertionError:pass
else:raise AssertionError('Symbol-assumption mutation was not rejected')
rf=reference['A'];old=rf.__globals__['tau']
rf.__globals__['tau']={(0,1,2):2}
try:
    try:same(candidate['A'](s.eye(2)[:,0]),rf(s.eye(2)[:,0]),'negative_binding')
    except AssertionError:pass
    else:raise AssertionError('Global tensor mutation was not rejected')
finally:rf.__globals__['tau']=old

assert len(candidate_module.error_schemas(PAYLOAD))==26
assert not any(name.startswith(('verify_','derive_','universal_')) for name in sys.modules)
verify_pins()
sys.setprofile(None)
output={'status':'namespace_behavioral_equivalence_pass','scope':'universal namespace values/bindings/safe probes only; no sparse or q65 verification',
        'python':sys.version,'executable':Path(sys.executable).name,'platform':platform.platform(),'sympy':s.__version__,'mpmath':mpmath.__version__,
        'stats':stats,'inventories':inventories,'bindings':bindings,'negative_fixtures':['symbol_assumption_rejected','global_tau_change_rejected'],
        'payload_modules_imported':False,'family_functions_called':False,'input_hashes_unchanged':True}
print(json.dumps(output,sort_keys=True))
print('PASS: independent universal namespace behavioral equivalence; sparse/q65 integration remains unverified.')
