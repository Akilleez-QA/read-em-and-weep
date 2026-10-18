"""Portable read-only source excerpt and formal word checks. No source execution."""
import argparse, ast, hashlib, json, textwrap
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def need(ok,message):
    if not ok: raise RuntimeError(message)
def digest(b): return hashlib.sha256(b).hexdigest()
def check_bindings(records):
    def f(file,name): return ast.unparse(ast.parse(textwrap.dedent(records[file]['excerpts'][name]['text'])))
    raw='raw_engine.py.txt'; comp='compiler.py.txt'; prog='program.py.txt'
    need('self.M.mul(self.Dframe(b), self.M.transpose(self.M.mul(pa, ib)), self.Dframe(a, True))' in f(raw,'PhysicalModel.g'),'transition order')
    need("pa = self.primitive(a.carrier)['P']" in f(raw,'PhysicalModel.g'),'P ancestor')
    need("ib = self.primitive(b.carrier)['I']" in f(raw,'PhysicalModel.g'),'I ancestor')
    need('self.c.model.s_raw(tuple(p), a, b)' in f(raw,'RawSource.T'),'raw scalar override')
    need('source = RawSource(M)' in f(raw,'source_and_lift'),'actual source class')
    need('c.mul(I, c.transpose(self.R(t)), P)' in f(comp,'Lift.at'),'residual transpose')
    need("self.homotopy(self.delta(stage - 1, t), node['homotopy_input_degree'], t[0])" in f(comp,'Lift.at'),'face owner recursion')
    need('c.mul(EK, node, self.H(u + 1, owner)), -1 if r % 2 else 1' in f(comp,'Lift.homotopy'),'second signed homotopy term')
    need("[1, 1, -1, 1]" in f(comp,'Lift.__init__'),'HPL stage signs')
    w=f(prog,'weighted_assignment')
    need('X13 = blocks[3, 1]' in w and 'X02 = blocks[2, 0]' in w,'selected blocks')
    need('scalar = X13[5][0] + X02[1][3] + X02[4][2]' in w,'selector entries')
    need('weighted = scalar * ex.scalar(parity)' in w and 'for owner in owners:' in w and 'outer_weight(ex, owner)' in w,'parity and original owner weights')

p=argparse.ArgumentParser(); p.add_argument('--source-dir',type=Path); args=p.parse_args()
records=json.loads((ROOT/'SOURCE_EXCERPTS.json').read_text())
n=0
for file,record in records.items():
    original=None
    if args.source_dir:
        original=(args.source_dir/file).read_bytes(); need(digest(original)==record['original_file_sha256'],'complete source pin '+file)
    for key,e in record['excerpts'].items():
        need(digest(e['text'].encode())==e['sha256'],'excerpt pin '+key)
        tree=ast.parse(textwrap.dedent(e['text']))
        need(digest(ast.dump(tree,include_attributes=False).encode())==e['ast_sha256'],'AST pin '+key)
        if original:
            actual=''.join(original.decode().splitlines(keepends=True)[e['start_line']-1:e['end_line']])
            need(actual==e['text'],'original range '+key)
        n+=1
check_bindings(records)
# Negative controls for the literal binding checks, independent of hash checks.
for file,key,old,new in [
 ('raw_engine.py.txt','PhysicalModel.g','self.Dframe(b),','self.Dframe(a),'),
 ('raw_engine.py.txt','RawSource.T','model.s_raw','model.other'),
 ('compiler.py.txt','Lift.at','c.transpose(self.R(t))','self.R(t)'),
 ('program.py.txt','weighted_assignment','X13[5][0]','X13[0][5]')]:
    changed=json.loads(json.dumps(records)); entry=changed[file]['excerpts'][key]
    need(old in entry['text'],'mutation target'); entry['text']=entry['text'].replace(old,new)
    try: check_bindings(changed)
    except RuntimeError: pass
    else: raise RuntimeError('negative control accepted: '+key)
# Formal noncommutative factor words: derivative slots never reorder factors.
def placements(count):
    words=[]
    for i in range(count):
        for j in range(count):
            slots=[[] for _ in range(count)]; slots[i].append(2); slots[j].append(4)
            words.append(tuple(tuple(sorted(s)) for s in slots))
    return words
expected3={((2,4),(),()),((),(2,4),()),((),(),(2,4)),((2,),(4,),()),((4,),(2,),()),((2,),(),(4,)),((4,),(),(2,)),((),(2,),(4,)),((),(4,),(2,))}
need(set(placements(3))==expected3 and len(placements(3))==9,'three-factor mixed derivative')
need(set(placements(2))=={((2,4),()),((),(2,4)),((2,),(4,)),((4,),(2,))},'two-factor mixed derivative')
need(set(placements(3)[:-1])!=expected3,'omitted-placement control')
print(json.dumps({'status':'pass','excerpt_count':n,'literal_negative_controls':4,'formal_derivative_placements':[9,4],'full_source_provenance_checked':bool(args.source_dir),'scope':'Static excerpts and formal derivative words only; no mathematical cancellation or nonzero variation test'},sort_keys=True))
