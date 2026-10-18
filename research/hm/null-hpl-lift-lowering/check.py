"""Static source and invented formal-word checks only. Never import production."""
import ast, hashlib, json
from pathlib import Path
from collections import defaultdict
ROOT=Path(__file__).resolve().parent

def need(ok,msg):
    if not ok: raise RuntimeError(msg)

def dump(s): return ast.dump(ast.parse(s),include_attributes=False)
def find(tree,cls,name):
    nodes=tree.body if cls is None else next(x for x in tree.body if isinstance(x,ast.ClassDef) and x.name==cls).body
    return next(x for x in nodes if isinstance(x,ast.FunctionDef) and x.name==name)
def contract(node,fragments):
    s=ast.unparse(node)
    for fragment in fragments:
        target=ast.dump(ast.parse(fragment).body[0],include_attributes=False)
        need(any(ast.dump(x,include_attributes=False)==target for x in ast.walk(node)), 'missing AST: '+fragment)

pins=json.loads((ROOT/'pins.json').read_text())
for p in pins:
    b=(ROOT/p['path']).read_bytes();need(hashlib.sha256(b).hexdigest()==p['sha256'],'pin '+p['path'])
C=ast.parse((ROOT/pins[0]['path']).read_text()); S=ast.parse((ROOT/pins[1]['path']).read_text()); R=ast.parse((ROOT/pins[2]['path']).read_text())
checks={
'at':["out = {(1, 1): c.mul(I, c.transpose(self.R(t)), P)}", "out = self.homotopy(self.delta(stage - 1, t), node['homotopy_input_degree'], t[0])", "out = {key: c.scale(n, node['coefficient']) for key, n in out.items()}"],
'delta':["face = t[:j] + t[j + 1:]", "self.merge(out, key, self.c.scale(node, (-1) ** j))"],
'homotopy':["need(v - u == r, 'End internal degree')", "if v > 0:\n self.merge(out, (u, v - 1), c.mul(self.H(v, owner), node))", "if v == 1 and u < 3:\n self.merge(out, (u + 1, v), c.scale(c.mul(EK, node, self.H(u + 1, owner)), (-1 if r % 2 else 1)))"]}
for name,fragments in checks.items(): contract(find(C,'Lift',name),fragments)
schema=find(S,None,'closed_lift_schema')
contract(schema,["for s, sign in ((1, 1), (2, -1), (3, 1)):\n nodes.append({'id': 'J'+str(s), 'cech_degree': 2+s, 'internal_degree': -s, 'coefficient': sign, 'op': 'end_homotopy', 'homotopy_input_degree': 1-s, 'input': {'op': 'cech', 'input': 'J'+str(s-1)}, 'leading_owner_rule': 'first vertex before any subsequent face deletion'})"])
raw=find(R,None,'source_and_lift');need(ast.literal_eval(raw.args.defaults[-1])==2,'stage2 default')
contract(raw,["return (source, lift.at(stage, tuple(owners)))"])
contract(find(R,'PhysicalModel','leaf'),["if name == 'I_phys':\n return self.M.mul(c['I'], self.Dframe(o))", "if name == 'P_phys':\n return self.M.mul(self.Dframe(o, True), c['P'])"])
# Reject concrete sign/transpose/block/owner-order mutations at the AST boundary.
mutations=[('at','c.transpose(self.R(t))','self.R(t)'),('at','t[0])','t[1])'),('delta','(-1) ** j','1'),('homotopy','v == 1','v == 2'),('homotopy','-1 if r % 2 else 1','1 if r % 2 else -1')]
for name,old,new in mutations:
    original=ast.unparse(find(C,'Lift',name));need(old in original,'mutation applicable')
    modified=ast.parse(original.replace(old,new)).body[0]
    try: contract(modified,checks[name])
    except RuntimeError: pass
    else: raise RuntimeError('mutation escaped '+old)
# Free noncommutative graded symbols; rewrite only declared contraction laws.
def reduce_word(w):
    for i in range(len(w)-1):
        p=w[i:i+2]
        if p in [('d','E'),('E','d'),('d','d')]:return {}
        if p==('d','h'):
            out=defaultdict(int)
            for mid,c in [((),1),(('E',),-1),(('h','d'),-1)]:
                for z,k in reduce_word(w[:i]+mid+w[i+2:]).items():out[z]+=c*k
            return {z:k for z,k in out.items() if k}
    return {w:1}
def simplify(terms):
    out=defaultdict(int)
    for c,w in terms:
        for z,k in reduce_word(w).items():out[z]+=c*k
    return {z:k for z,k in out.items() if k}
# d_End H_r(F)+H_(r+1)d_End(F), eight expanded ordered products.
for r in range(-3,4):
    e=(-1)**r
    terms=[(1,('d','h','F')),(e,('d','E','F','h')),(e,('h','F','d')),(1,('E','F','h','d')),(1,('h','d','F')),(-e,('h','F','d')),(-e,('E','d','F','h')),(1,('E','F','d','h'))]
    need(simplify(terms)=={('F',):1,('E','F','E'):-1},'graded identity')
    need(simplify(terms[:1]+terms[2:])==simplify(terms),'dE zero check')
# Independent word grammar records current first owner before each deletion.
def words(s,t,sign=1,hs=()):
    if s==0:return [(sign,hs,t)]
    out=[]
    for j in range(len(t)):
        out+=words(s-1,t[:j]+t[j+1:],sign*((-1)**(s+1))*((-1)**j),hs+((t[0],1-s),))
    return out
counts=[]
for s in range(4):
    w=words(s,tuple(range(s+3)));counts.append(len(w))
    for coefficient,hs,tail in w:
        need(len(tail)==3 and len(hs)==s,'arity')
        need(tuple(r for _,r in hs)==tuple(1-j for j in range(s,0,-1)),'input degrees')
        need(coefficient in (-1,1),'face sign')
need(counts==[1,4,20,120],'word counts')
need(any(hs[0][0] not in tail for _,hs,tail in words(2,tuple(range(5)))),'deleted prefix retained')
# Block support of both H terms, independently from pure type composition.
blocks={(1,1)};supports=[sorted(blocks)]
for s in range(1,4):
    out=set()
    for u,v in blocks:
        if v>0:out.add((u,v-1))
        if v==1 and u<3:out.add((u+1,v))
    need(all(v-u==-s for u,v in out),'output internal degree')
    blocks=out;supports.append(sorted(blocks))
need(supports==[[(1,1)],[(1,0),(2,1)],[(2,0),(3,1)],[(3,0)]],'four term support')
# Cech signs cancel pairwise: each two-deletion path has opposite parity.
for n in range(4,8):
    for a in range(n):
        for b in range(a+1,n): need((-1)**(a+b-1)+(-1)**(a+b)==0,'delta squared')
result={'status':'PASS','pins':len(pins),'AST_mutations_rejected':len(mutations),'graded_degrees_checked':7,'face_word_counts':counts,'block_supports':supports,'production_imports':False,'actual_products':False,'physical_execution_admission':False}
# Negative pin controls use inert bytes only; explicit exceptions survive -O.
def verify_bytes(data,expected):
    need(hashlib.sha256(data).hexdigest()==expected,'negative pin rejected')
for p in pins:
    original=(ROOT/p['path']).read_bytes()
    try: verify_bytes(original+b'\n# altered inert input\n',p['sha256'])
    except RuntimeError: pass
    else: raise RuntimeError('changed input escaped pin')
    try: verify_bytes(original,'0'*64)
    except RuntimeError: pass
    else: raise RuntimeError('changed expected digest escaped pin')
# Source files are data: their AST is inspected, never compiled or imported.
face=ast.parse((ROOT/pins[3]['path']).read_text())
contract(find(face,None,'_ordered_owners'),["need(all((owners[j].source_key < owners[j + 1].source_key for j in range(len(owners) - 1))), 'strict source-first common tuple')"])
contract(find(face,None,'lift_terms'),["out.extend(recurse(level - 1, current[:j] + current[j + 1:], prefix + (first,), sign * SIGNS[level] * (-1) ** j, word + [hom, {'op': 'signed_Cech_face', 'deleted_owner': current[j].data(), 'face_index': j}]))"])
# Transpose reverses factor order, so row g_ji occurs on the left.
column_word=('Gij','Rt','Gji')
transpose_names={'Gij':'gij','Gji':'gji','Rt':'R'}
need(tuple(transpose_names[x] for x in reversed(column_word))==('gji','R','gij'),'transpose reversal')
result.update({'negative_pin_controls_rejected':2*len(pins),'inputs_executed':False,'source_order_guard_in_face_program':True})
print(json.dumps(result,indent=2))
