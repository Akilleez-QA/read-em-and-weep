"""AST/byte checks only; no candidate import, compilation or execution."""
from pathlib import Path
import argparse, ast, copy, hashlib, json
HERE=Path(__file__).resolve().parent
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--source-root', type=Path, required=True, help='Directory containing the pinned codex-swarm source subdirectories')
BASE=parser.parse_args().source_root.resolve()
manifest=json.loads((HERE/'public-pins.json').read_text())
def need(ok, msg):
    if not ok: raise ValueError(msg)
def dump(x): return ast.dump(x,include_attributes=False)
def named(tree): return {n.name:n for n in tree.body if isinstance(n,(ast.FunctionDef,ast.ClassDef))}
def checks(oldfield,newfield,oldprogram,newprogram):
    of,nf,op,np=map(ast.parse,(oldfield,newfield,oldprogram,newprogram))
    on,nn=named(op),named(np)
    for name,node in on.items(): need(dump(node)==dump(nn[name]),'old program changed: '+name)
    need(newprogram.startswith(oldprogram),'old program bytes changed')
    need(set(nn)-set(on)=={'actual_id0'},'secondary top-level construction path')
    entry=nn['actual_id0']
    need(isinstance(entry.body[0],ast.Raise),'first operation not direct raise')
    need(dump(entry.body[0])==dump(ast.parse('raise RuntimeError("ID0 physical execution is unconditionally held")').body[0]),'refusal changed')
    need(not any(isinstance(n,(ast.Yield,ast.YieldFrom,ast.Await)) for n in entry.body if not isinstance(n,ast.FunctionDef)),'deferred public refusal')
    own=entry.body[1];need(isinstance(own,ast.FunctionDef) and own.name=='potential_owners_id0','owner helper not unreachable nested')
    expected=copy.deepcopy(on['potential_owners']);expected.name='potential_owners_id0'
    for n in ast.walk(expected):
        if isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute) and n.func.attr=='FullOwner':n.args[0]=ast.Constant(0)
    need(dump(own)==dump(expected),'owner delta exceeds seed/name')
    original=on['_actual_body'].body[:-1]
    actual=copy.deepcopy(entry.body[2:2+len(original)])
    for n in ast.walk(ast.Module(body=actual,type_ignores=[])):
        if isinstance(n,ast.Name) and n.id=='potential_owners_id0':n.id='potential_owners'
    need([dump(x) for x in original]==[dump(x) for x in actual],'preterminal delta')
    tail=entry.body[2+len(original):]
    need(len(tail)==3 and isinstance(tail[-1],ast.Return),'terminal structure')
    call=tail[-1].value
    need(isinstance(call,ast.Call) and call.func.attr=='weighted_coefficients','weighted terminal')
    terms=ast.literal_eval(call.args[2])
    need(terms==(((-3,-3,-1,-1),1),((-2,-2,-2,-2),2),((-1,-1,-3,-3),1)),'ID0 terms')
    need(dump(tail[1])==dump(ast.parse('certificate=stripped.certify_laurent(context)').body[0]),'single shared certificate')
    frame=ast.literal_eval(tail[0].value.args[1])
    need(frame==('original-resolution-frame','degree-minus2-tau-minus4','finite-tau1','full-deck-mask15','ID0-L5,0-Q2'),'frame labels')
    oldnodes,newnodes=named(of),named(nf)
    for name,node in oldnodes.items():
        candidate=copy.deepcopy(newnodes[name])
        if name=='Rational':candidate.body=[n for n in candidate.body if not isinstance(n,ast.FunctionDef) or n.name!='certify_laurent']
        need(dump(node)==dump(candidate),'old field API changed: '+name)
    need(set(newnodes)-set(oldnodes)=={'LaurentContext','LaurentCertificate'},'unexpected field entry')
    method=named(newnodes['Rational'])['certify_laurent']
    divisions=[n for n in ast.walk(method) if isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute) and n.func.attr=='divide']
    need(len(divisions)==1,'not one complete division')
    certmethods=named(newnodes['LaurentCertificate'])
    for name in ('coefficient','weighted_coefficients'):
        b=certmethods[name].body
        check=ast.parse('self._check(rational, context)').body[0]
        need(dump(b[0])==dump(check) and dump(b[-2])==dump(check) and isinstance(b[-1],ast.Return),'missing failure checks')
    return True
for row in manifest['frozen_sources']:
    need(hashlib.sha256((BASE/row['path']).read_bytes()).hexdigest()==row['sha256'],'frozen source changed')
need(hashlib.sha256((HERE/'candidate.patch').read_bytes()).hexdigest()==manifest['patch_sha256'],'patch digest')
texts=[]
for row in manifest['changed_files']:
    old=(BASE/row['path']).read_text();new=(HERE/row['candidate_text']).read_text()
    need(hashlib.sha256(new.encode()).hexdigest()==row['candidate_sha256'],'candidate digest')
    texts.extend([old,new])
checks(*texts)
mutations=[
 ('entry refusal',3,'raise RuntimeError("ID0 physical execution is unconditionally held")','require_aggregate_admission()'),
 ('owner seed',3,'I.FullOwner(0,','I.FullOwner(1,'),
 ('weight two',3,'((-2,-2,-2,-2),2)','((-2,-2,-2,-2),1)'),
 ('old route',3,'def actual_route30(*args,**kwargs):','def actual_route30_changed(*args,**kwargs):'),
 ('terminal exponent',3,'((-3,-3,-1,-1),1)','((-4,-3,-1,-1),1)'),
 ('field failure check',1,'        self._check(rational, context)\n        return answer','        return answer'),
]
for label,idx,old,new in mutations:
    candidate=texts.copy();need(old in candidate[idx],'mutation target absent');candidate[idx]=candidate[idx].replace(old,new)
    try:checks(*candidate)
    except (ValueError,KeyError):pass
    else:raise ValueError('mutation accepted: '+label)
# Static dependency inventory. Absence is reported, never silently authenticated.
pins=json.loads((BASE/'detector-realization/source-pins.json').read_text())
closure={'local_receipt_dependencies':[], 'historical_git_objects_not_refetched':pins['git_objects'], 'static_imports':{}}
for row in pins['local_dependencies']:
    p=BASE/row['path'];present=p.is_file()
    match=present and hashlib.sha256(p.read_bytes()).hexdigest()==row['sha256']
    record=dict(row,present_in_frozen_snapshot=present,byte_match=match)
    closure['local_receipt_dependencies'].append(record)
for p in sorted(BASE/row['path'] for row in manifest['frozen_sources'] if row['path'].endswith('.py')):
    tree=ast.parse(p.read_text())
    closure['static_imports'][str(p.relative_to(BASE))]=[ast.unparse(n) for n in ast.walk(tree) if isinstance(n,(ast.Import,ast.ImportFrom))]
(HERE/'dependency-inventory.json').write_text(json.dumps(closure,indent=2)+'\n')
print('PASS: all 23 frozen hashes unchanged; candidate/patch hashes match.')
print('PASS: old program prefix byte-identical; all old field definitions AST-identical.')
print('PASS: public direct raise; no new top-level secondary body; owner helper only below raise.')
print('PASS: preterminal AST identical modulo nested owner helper name; helper differs only seed30->0.')
print('PASS: exact three terminals, weights1:2:1, one shared division, failure checks before reads/returns.')
print('PASS: six in-memory negative AST mutations rejected.')
print('LIMIT: no candidate/production code executed; no physical or synthetic numeric result claimed.')
