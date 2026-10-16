"""CO02: integer-only source dependency and conditional dense-cost adapter."""
from collections import Counter
from pathlib import Path
from math import prod
import hashlib
import json
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
BASE = HERE.parent
REVIEW = '82a8785d0a23e8d4e44e9ca4f52c8bb24fdadbdc'
HEAD = 'c44072e1d'
MAX_BYTES = 4_000_000
PINS_SHA256 = 'abcc7027eb3102a16ba047be95c856015a96fc7a9185a62f4639d0056421740e'


def need(ok, message):
    if not ok:
        raise ValueError(message)


def canonical(x):
    return json.dumps(x, sort_keys=True, separators=(',', ':'), allow_nan=False)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def read(path):
    need(path.stat().st_size <= MAX_BYTES, 'metadata byte cap')
    return json.loads(path.read_bytes())


def git_bytes(commit, path):
    raw = subprocess.check_output(['git', 'show', commit + ':' + path], cwd=ROOT, timeout=10)
    need(len(raw) <= MAX_BYTES, 'git byte cap')
    return raw


def authenticate():
    need(sha((HERE/'source-pins.json').read_bytes()) == PINS_SHA256, 'pin manifest drift')
    pins = read(HERE / 'source-pins.json')
    for p in pins['sources']:
        raw = git_bytes(p['commit'], p['path'])
        need(sha(raw) == p['sha256'], 'source pin drift: ' + p['path'])
        if p.get('same_at_head'):
            need(git_bytes(HEAD, p['path']) == raw, 'reviewed/HEAD mismatch')
            need((ROOT / p['path']).read_bytes() == raw, 'local drift: ' + p['path'])
    cert=json.loads(git_bytes('398bb5ea34893a2cac80092eb78d4c73dabebb85',
        'research/hm/null-source-integration/tracefree-currents/certificate.json'))
    need(cert['raw_projected_first_current_equivalence_proved'] is True
         and cert['baseline_equivalence_proved'] is False
         and cert['branch_count']==8 and cert['seed_scope']==[12,30], 'current theorem scope')
    return pins


def refs(n):
    op = n[0]
    if op in ('catalog_cleared_primitive', 'owned_polynomial_factor',
              'mask_times_x_squared_plus_one_over_two', 'binary_mask_q_numerator'):
        return []
    if op in ('ordered_product', 'sum'):
        return n[1:]
    if op == 'scale':
        return [n[3]]
    if op in ('transpose', 'trace', 'polynomial_diagonal', 'power',
              'polynomial_partial_after_elementary_substitution'):
        return [n[1]]
    raise ValueError('unknown finite source operation: ' + op)


def stats(nodes, roots, children, operation):
    sizes = []
    for i, n in enumerate(nodes):
        rs = children(n)
        need(all(type(r) is int and 0 <= r < i for r in rs), 'topological integer references')
        sizes.append(1 + sum(sizes[r] for r in rs))
    reached = set()
    stack = list(roots)
    while stack:
        r = stack.pop()
        need(type(r) is int and 0 <= r < len(nodes), 'root reference')
        if r not in reached:
            reached.add(r)
            stack.extend(children(nodes[r]))
    visits = sum(sizes[r] for r in roots)
    return {'root_references': len(roots), 'unique_nodes': len(reached),
            'tree_node_visits': visits, 'reuse_visits_avoided': visits-len(reached),
            'edge_references': sum(len(children(nodes[r])) for r in reached),
            'op_nodes': dict(sorted(Counter(operation(nodes[r]) for r in reached).items()))}


def dense_bound(nodes):
    """Rational coefficient operation bound, conditional on materialized leaf arrays.
    No source coefficients, floating point, polynomial operations or oracle calls.
    Degree boxes intentionally overestimate intermediate cancellation.
    """
    rows = []
    for i, n in enumerate(nodes):
        op = n[0]; rs = refs(n); xs = [rows[r] for r in rs]
        shape = [1, 1]; degree = [0]*4; cost = 0
        if op == 'catalog_cleared_primitive':
            shape = [2, 15] if n[2] == 'P' else [15, 2]
            degree = [12]*4  # raw degree <=7, each elementary generator multilinear, H <=5
        elif op == 'owned_polynomial_factor':
            degree = [5]*4 if n[1][1] == 'H' else [3 if j == n[1][2] else 0 for j in range(4)]
        elif op == 'mask_times_x_squared_plus_one_over_two':
            degree[n[2]] = 2
        elif op == 'binary_mask_q_numerator':
            degree[n[3]] = 2
        elif op in ('ordered_product', 'sum'):
            shape = xs[0]['shape'][:]; degree = xs[0]['degree'][:]
            for x in xs[1:]:
                a, b = shape, x['shape']; d = x['degree']
                if op == 'sum':
                    need(a == b, 'sum shape')
                    degree = [max(v,w) for v,w in zip(degree,d)]
                    cost += prod(shape)*prod(v+1 for v in degree)
                else:
                    sa, sb = prod(v+1 for v in degree), prod(v+1 for v in d)
                    if a == [1,1] or b == [1,1]:
                        shape = b[:] if a == [1,1] else a[:]
                        scalar_products = prod(shape)
                        inner_add = 0
                    else:
                        need(a[1] == b[0], 'product shape')
                        shape = [a[0],b[1]]
                        scalar_products = a[0]*a[1]*b[1]
                        inner_add = a[0]*b[1]*max(0,a[1]-1)
                    degree = [v+w for v,w in zip(degree,d)]
                    # Naive convolution: one multiply and at most one accumulation per pair.
                    cost += 2*scalar_products*sa*sb + inner_add*prod(v+1 for v in degree)
        elif op == 'power':
            x = xs[0]; need(x['shape'] == [1,1] and type(n[2]) is int and 1 <= n[2] <= 14, 'scalar power')
            degree = x['degree'][:]
            for _ in range(n[2]-1):
                cost += 2*prod(v+1 for v in degree)*prod(v+1 for v in x['degree'])
                degree = [v+w for v,w in zip(degree,x['degree'])]
        else:
            x = xs[0]; shape = x['shape'][:]; degree = x['degree'][:]
            cells = prod(shape)*prod(v+1 for v in degree)
            if op == 'transpose':
                shape.reverse()
            elif op == 'trace':
                need(shape[0] == shape[1], 'trace shape')
                cost = (shape[0]-1)*prod(v+1 for v in degree); shape = [1,1]
            elif op == 'polynomial_diagonal':
                need(shape == [1,1], 'diagonal scalar'); shape = [2,2]; cost = prod(v+1 for v in degree)
            elif op == 'scale':
                need(type(n[1]) is int and type(n[2]) is int and n[2] > 0, 'scale rational')
                cost = 2*cells
            elif op == 'polynomial_partial_after_elementary_substitution':
                need(type(n[2]) is int and n[2] in range(4), 'derivative coordinate')
                cost = cells; degree[n[2]] = max(0, degree[n[2]]-1)
            else:
                raise ValueError('unhandled bound operation')
        rows.append({'id':i, 'shape':shape, 'degree':degree, 'dense_cells':prod(shape)*prod(v+1 for v in degree), 'rational_operations_upper':cost})
    return {'conditional_on':'all source-leaf dense arrays supplied exactly in the common finite frame; naive dense rational arithmetic; leaf construction and oracle cost excluded',
            'nodes':rows, 'rational_operations_upper':sum(x['rational_operations_upper'] for x in rows),
            'retain_all_dense_cells_upper':sum(x['dense_cells'] for x in rows),
            'cleared_P_final_degree_box':[217,217,210,210],
            'cleared_P_final_dense_cells_upper':218**2*211**2,
            'physical_coefficient_height_bits':None,'bit_operations_upper':None,'physical_peak_bytes':None,
            'oracle_cost':None,'occupied_support':None}


def ast_graph(ast):
    """Intern exact matrix AST syntax inside ONE full branch/frame scope."""
    nodes = []; ids = {}
    def visit(x):
        need(isinstance(x,dict) and 'op' in x and 'args' in x, 'matrix AST')
        children = [visit(a) for a in x['args'] if isinstance(a,dict) and 'op' in a]
        key = canonical(x)
        if key not in ids:
            ids[key] = len(nodes)
            child_iter = iter(children)
            payload = {k:v for k,v in x.items() if k != 'args'}
            payload['args'] = [{'node':next(child_iter)} if isinstance(a,dict) and 'op' in a
                               else {'literal':a} for a in x['args']]
            nodes.append({'op':x['op'],'children':children,'payload':payload})
        return ids[key]
    root = visit(ast)
    return nodes, root


def combined_graph(edge, directions):
    """Exact padded N and one-derivative shell around pending complete programs.
    Indexed sums remain finite operators, never one arithmetic operation claims.
    """
    nodes = []
    def put(op, children=(), **payload):
        nodes.append({'op':op,'children':list(children),**payload})
        return len(nodes)-1
    B=put('pending_complete_B',program='R(Kcov Pi + A h S Pi)F12')
    ca=put('owned_C',binding=edge['C_output'][0])
    cb=put('owned_C',binding=edge['C_output'][1])
    z=put('owned_Z_ab',binding=edge['Z_output'])
    p1=put('finite_indexed_Qhat_times_whole_P_sum',call=edge['id']+':prism1',instances=96)
    p2=put('finite_indexed_Qhat_Qhat_times_whole_P_sum',call=edge['id']+':prism2',instances=9216)
    standard=put('ordered_product',[ca,cb,z,B])
    prism1=put('ordered_product',[z,p1])
    prism2=put('ordered_product',[ca,z,p2])
    negative=put('rational_scale',[prism2],coefficient=[-1,1])
    whole=put('whole_N_sum',[standard,prism1,negative])
    cancelled=put('pending_inserted_cancellation_witness',[whole],preserve_complete_sum=True)
    D=put('ordered_product',[ca,cb,z])
    factors=[]
    for C,Z in zip(edge['C_output'],edge['Z_output']):
        specs=[('H',-1,C['H_power'])]
        specs += [('ell',i,e) for i,e in enumerate(C['pair_ell_powers']) if e]
        specs += [('standard_x',i,e) for i,e in enumerate(Z['standard_powers']) if e]
        for kind,axis,power in specs:
            f=put('owned_denominator_factor',owner=C['owner'],kind=kind,axis=axis)
            factors.append((f,power))
    delta=put('ordered_product',[f for f,_ in factors])
    denominator=put('ordered_product',[D,delta])
    roots={}
    for d in sorted(set(directions)):
        dn=put('differentiate_complete_N',[cancelled],direction=d)
        left=put('ordered_product',[delta,dn])
        terms=[]
        for f,power in factors:
            df=put('differentiate_owned_factor',[f],direction=d)
            term=put('ordered_product',[df]+[g for g,_ in factors if g!=f])
            terms.append(put('rational_scale',[term],coefficient=[power,1]))
        right=put('ordered_product',[cancelled,put('sum',terms)])
        minus=put('rational_scale',[right],coefficient=[-1,1])
        numerator=put('sum',[left,minus])
        roots[str(d)]=put('pending_whole_quotient_coefficient',[numerator,denominator],direction=d,
                         boundary='complete N/D after inserted cancellation; not free quotient atoms')
    return {'nodes':nodes,'whole_N_root':whole,'derivative_roots':roots,
            'stats':stats(nodes,list(roots.values()),lambda n:n['children'],lambda n:n['op'])}


def build():
    pins = authenticate()
    source = read(BASE/'whole-source-clearing/source-integration.json')
    compiled = read(BASE/'scalar-compiler/compiled-template.json')
    finite = source['finite_actual_source_clearing']; nodes = finite['dag']
    need(len(nodes)==153 and finite['cleared_P']==152, 'actual F12 template')
    grammar = {'schema':'co02-scoped-adapter-v1','source_pins_sha256':sha((HERE/'source-pins.json').read_bytes()),
               'finite_F12_template':finite,'family_template':compiled,
               'scope_key_fields':['actual_map','Laurent_exponent','ordered_full_owners','source_branch','frame','source_order','standard_tags','legal_masks'],
               'scope_rule':'no cross-scope sharing; indexed domains preserve occurrence IDs; family symbolic owners are not fixed physical owners',
               'fixed_bindings':[r['v5_binding'] for r in source['requests']],
               'combined_edges':[], 'fixed_branches':[], 'actual_demands':[]}
    unresolved = []
    for j,n in enumerate(nodes):
        if not refs(n):
            unresolved.append({'id':'finite_F12:leaf:'+str(j),'operation':n[0],
                'scope':'ordered full-owner triple bound at each call site',
                'source_node':j,'required':'exact leaf array construction/oracle cost and coefficient height; finite dense bound starts after these arrays exist'})
    for req in source['requests']:
        v5=req['v5_binding']; seed=v5['request']['seed']
        unresolved.append({'id':'fixed:'+str(seed)+':selector_and_outer_weights',
            'scope':v5['request']['owners'],
            'required':'coefficient programs for full selector and every owned outer weight, including deleted prefixes; see fixed_bindings'})
        for edge in req['combined_edges']:
            eid = edge['id']; a,b = edge['output_edge']
            calls = []
            for branch, variables, slots in [('prism1',['u'],['u',a,b]),('prism2',['u','v'],['u','v',b])]:
                calls.append({'id':eid+':'+branch, 'branch':branch,'operation':'finite_indexed_whole_F12_call',
                    'variables':{v:edge['inserted_owner_maps'][v] for v in variables},
                    'slot_owners':slots, 'unpruned_instances':96**len(variables),
                    'body_template':'finite_F12_template', 'body_root':152,
                    'source_order':finite['source_triple_order'], 'sorting_sign':'source-first alternation; no nonlinear rebuilding',
                    'coefficient_program_status':'pending Qhat/frame lowering',
                    'sharing':'none between indexed assignments or prism branches'})
            directions=[b['source_branch']['coordinate'] for b in req['v5_binding']['branches'] if b['combined_numerator_reference']==eid]
            shell=combined_graph(edge,directions)
            grammar['combined_edges'].append({'id':eid,'binding':edge,'calls':calls,'combined_quotient_shell':shell,
                'dependency_sequence':['complete_B','padded_prism1','padded_prism2','whole_N_sum','cancel_inserted_factors','differentiate_whole_quotient'],
                'complete_B_boundary':{'id':eid+':complete_B','program':'R(Kcov Pi + A h S Pi)F12','split_into_free_leaves':False},
                'quotient_boundary':{'id':eid+':Qhat','definition':'null N14 exact quotient program; all owned factors and frame pullbacks retained'}})
            unresolved.extend([{'id':eid+':complete_B','scope':edge['output_edge'],'required':'executable complete standard B coefficient circuit and standard-target support witness'},
                               {'id':eid+':Qhat','scope':edge['inserted_owner_maps'],'required':'source-bound quotient coefficients and oracle support/cost for all indexed occurrences'}])
        for branch in req['v5_binding']['branches']:
            sb=branch['source_branch']; binding=sb['current_source_binding']
            ns, root=ast_graph(branch['demand_current']['input_ast'])
            ns.append({'op':'tracefree','children':[root],'shape':[2,2]})
            root=len(ns)-1
            all_owners=req['v5_binding']['request']['owners']
            scope={'ordered_full_owners':all_owners,'current_tail_owners':binding['owners'],'source_branch':branch['id'],
                   'frame':branch['demand_current']['frame'],'source_order':source['order_scope'],
                   'legal_masks':[o[3] for o in all_owners], 'standard_tags':[o[4] for o in all_owners]}
            grammar['fixed_branches'].append({'id':branch['id'],'scope':scope,'source_binding':branch,
                'current_AST_nodes':ns,'root':root,'N_reference':branch['combined_numerator_reference'],
                'current_stats':stats(ns,[root],lambda n:n['children'],lambda n:n['op']),
                'projection':'tracefree wrapper retained; equivalence resolved by authenticated tracefree-current theorem on these eight branches only'})
            unresolved.append({'id':branch['id']+':current_coefficients','scope':scope,'required':'rational current coefficient lowering, frame/selector contraction and support/cost schedule'})
    cn=compiled['nodes']; templates={(r['i'],r['b']):r['J2_scalar_circuit'] for r in compiled['scalar_templates']}
    groups={}
    for request in compiled['requests']:
        wr=request['weighted_request']; m=wr['scalar_map']
        for t in wr['terms']:
            key=(m['i'],m['b'],tuple(t['laurent_exponents']))
            groups.setdefault(key,[]).append({'request_id':wr['id'],'weight':t['coefficient']})
    for (i,b,e),uses in sorted(groups.items()):
        scalar=templates[i,b]
        roots=[j for j,n in enumerate(cn) if n['op']=='Laurent_coefficient' and tuple(n['exponent'])==e
               and cn[n['children'][0]]['op']=='finite_outer_cover_transport'
               and cn[n['children'][0]]['children']==[scalar]]
        need(len(roots)==1,'exact map/exponent source root')
        grammar['actual_demands'].append({'map':{'i':i,'b':b},'exponent':list(e),'uses':uses,'root':roots[0],
            'scope':{'owners':'five symbolic full occurrences a0..a4; retained deleted faces and inner owners',
                     'frame':'original fixed resolution; outer transport before scalar row',
                     'staircases':compiled['outer_transport']['staircases'],
                     'fibers':compiled['outer_transport']['fiber_per_standard_vertex'],
                     'source_branch':'all five corrected Rsharp terms, complete gerbe baseline and whole standard B'},
            'dependency_stats':stats(cn,roots,lambda n:n['children'],lambda n:n['op'])})
    for j,n in enumerate(cn):
        if n['op'] in ('leaf','matrix_inverse','physical_jet','N14_prism_first','N14_prism_second',
                       'N14_R_Kcov_Pi','N14_R_A_h_S_Pi','complete_inner_solver','differentiate_combined_solver','finite_outer_cover_transport'):
            unresolved.append({'id':'family:'+str(j),'operation':n['op'],'source_node':j,
                               'required':'physical coefficient program, support/domain and operation/storage schedule',
                               'scope':'exact family node payload in family_template; no fixed-seed substitution'})
    roots=[d['root'] for d in grammar['actual_demands']]
    bound=dense_bound(nodes)
    instances=sum(c['unpruned_instances'] for e in grammar['combined_edges'] for c in e['calls'])
    report={'schema':'co02-scoped-cost-report-v1','source_pins_sha256':grammar['source_pins_sha256'],
        'authentication':{'reviewed_commit':REVIEW,'same_bytes_HEAD':HEAD,'PR1_live_read':'unavailable: web cache miss and GitHub API connection failure; local published STATUS/README consumed',
                          'null_theorems':'pins authenticated; consume tracefree first-current projection resolution without reproving; other theorem hypotheses remain explicit'},
        'resolved_first_current_comparison':{
            'commit':'398bb5ea34893a2cac80092eb78d4c73dabebb85',
            'certificate_path':'research/hm/null-source-integration/tracefree-currents/certificate.json',
            'branch_ids':[b['id'] for b in grammar['fixed_branches']],
            'raw_projected_first_current_equivalence_proved':True,
            'baseline_equivalence_proved':False,
            'historical_v5_pending_flags_preserved_as_provenance':True,
            'proof_replayed_or_reproved_here':False},
        'finite_template_stats':stats(nodes,[152],refs,lambda n:n[0]),
        'finite_template_bound':bound,
        'fixed_E34':{'branches':len(grammar['fixed_branches']),'complete_N_edges':len(grammar['combined_edges']),
            'combined_quotient_shell_stats':{e['id']:e['combined_quotient_shell']['stats'] for e in grammar['combined_edges']},
            'current_stats_by_branch':{b['id']:b['current_stats'] for b in grammar['fixed_branches']},
            'indexed_P_call_sites':8,'unpruned_P_instances':sum(c['unpruned_instances'] for e in grammar['combined_edges'] for c in e['calls']),
            'unpruned_P_node_instances':sum(c['unpruned_instances'] for e in grammar['combined_edges'] for c in e['calls'])*153,
            'conditional_P_subprogram_rational_operations_upper':instances*bound['rational_operations_upper'],
            'conditional_P_subprogram_retain_all_cells_upper':instances*bound['retain_all_dense_cells_upper'],
            'instances_status':'finite no-sharing syntactic upper bound; sorting/repeated-label zero not pruned; excludes unresolved complete-B inner source calls and Qhat'},
        'family':{'source_template_nodes':len(cn),'weighted_tests':len(compiled['requests']),
            'weighted_occurrences':sum(len(d['uses']) for d in grammar['actual_demands']),
            'actual_map_exponent_demands':len(groups),'repeated_coefficient_references':sum(len(d['uses'])-1 for d in grammar['actual_demands']),
            'demand_union_stats':stats(cn,roots,lambda n:n['children'],lambda n:n['op']),
            'closure_J3_stats':stats(cn,[x['matrix'] for x in compiled['lift_components']['J3']],lambda n:n['children'],lambda n:n['op']),
            'outer_unpruned_assignments_per_demand':24*96**5,
            'outer_unpruned_assignments_all_demands':len(groups)*24*96**5,
            'counts_status':'exact symbolic stencil dependency counts; fiber occurrences are finite unpruned multiplicities, not physical operation counts; union sharing is source-template sharing only, not coefficient reuse across distinct scopes'},
        'unresolved_cost_leaves':unresolved,
        'remaining_global_inputs':['physical homogeneous/frame identification','all-row closure and standard-target extension','null-owned source-order comparison including F12/F34 relation',
            'physical coefficient height/representation and oracle cost/support','last-use allocation schedule and authoritative CURRENT reconciled global spending/live allocations/commitments'],
        'gates':{'physical_source_evaluated':False,'arithmetic_admission':False,'execution_release':False,'fresh_budget_granted':0},
        'physical_cost_upper':None,'physical_peak_bytes':None,'obstruction':'undecided'}
    return grammar,report


def validate(grammar, report):
    expected_grammar, expected_report = build()
    need(canonical(grammar) == canonical(expected_grammar), 'adapter grammar/source/scope drift')
    need(canonical(report) == canonical(expected_report), 'cost report/bound/gate drift')
    return True


if __name__ == '__main__':
    grammar,report=build()
    (HERE/'adapter-grammar.json').write_text(json.dumps(grammar,sort_keys=True,indent=2)+'\n')
    (HERE/'cost-report.json').write_text(json.dumps(report,sort_keys=True,indent=2)+'\n')
