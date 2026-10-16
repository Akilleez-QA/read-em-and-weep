#!/usr/bin/env python3
"""Owner-aware formal map pruning; no physical matrix or polynomial input."""
import json
import hashlib
import sys
from dataclasses import dataclass, replace
import compile_refined_detector_metadata as spec

MAX_BYTES=49152
@dataclass(frozen=True)
class Term:
    coefficient:int
    left:tuple
    right:tuple
    tail:tuple
    source:int=1
    target:int=1
    legal_degree:bool=True


def h_branch(term,owner,r,branch):
    if branch=='L':
        return replace(term,left=(('H',owner),)+term.left,target=term.target-1,
                       legal_degree=term.legal_degree and term.target>0)
    if branch=='R':
        return replace(term,coefficient=term.coefficient*(-1 if r%2 else 1),
                       left=(('E',owner),)+term.left,
                       right=term.right+(('H',owner),),source=term.source+1,
                       legal_degree=term.legal_degree and term.target==1 and term.source<3)
    raise spec.ContractError('unknown homotopy branch')


def raw_lift(tuple_,depth):
    if depth==0:
        yield Term(1,(('I',tuple_[0]),),(('P',tuple_[0]),),tuple_)
        return
    sign=1 if depth==1 else -1
    for delete in range(len(tuple_)):
        face=tuple_[:delete]+tuple_[delete+1:]
        for term in raw_lift(face,depth-1):
            term=replace(term,coefficient=term.coefficient*sign*((-1)**delete))
            for branch in ('L','R'):
                yield h_branch(term,tuple_[0],-(depth-1),branch)


def zero_word(word):
    # Only SAME OWNER identities. Different owners cannot be merged.
    zeros={('H','H'),('H','E'),('E','H'),('H','I'),('P','H')}
    return any(a[1]==b[1] and (a[0],b[0]) in zeros for a,b in zip(word,word[1:]))


def reason(term,entry_block):
    if zero_word(term.left) or zero_word(term.right):
        return 'same_owner_split_identity'
    if not term.legal_degree:
        return 'graded_block_zero'
    if (term.source,term.target)!=entry_block:
        return 'terminal_block_mismatch'
    return None


def prefix_allowed(depth,vertices,frame='common-original-frame'):
    """Conditional label filter only; no tail-distinctness or mask merger."""
    spec.require(frame=='common-original-frame','uncertified frame for carrier equality')
    spec.require(depth in (0,1,2),'unsupported prefix depth')
    spec.require(len(vertices)==depth+3,'wrong common tuple length')
    spec.require(all(len(v)==3 and -1<=v[0]<=4 and 0<=v[1]<16 and 0<=v[2]<16
                     for v in vertices),'bad carrier/mask/standard label')
    spec.require(list(vertices)==sorted(vertices) and len(set(vertices))==len(vertices),
                 'common tuple must be source-first strictly ordered')
    carriers=[v[0] for v in vertices[:depth+1]]
    return all(a<b for a,b in zip(carriers,carriers[1:]))


def abstract_two_chart_sum(labels,partition_identity):
    spec.require(tuple(labels)==(0,1),'incomplete legal partition sum')
    spec.require(partition_identity=='w0+w1=1','missing legal partition identity')
    return '1'


def sum_prefix_masks(depth,strict_carriers=True,common_frame=True,tail_masks=False):
    spec.require(depth in (0,1,2),'prefix mask depth')
    spec.require(strict_carriers and common_frame,'prefix mask independence unproved')
    spec.require(not tail_masks,'tail mask merger not authorized')
    for _owner in range(depth):
        for _coordinate in range(4):
            spec.require(abstract_two_chart_sum((0,1),'w0+w1=1')=='1','partition rewrite')
    return {'prefix_owners':tuple(range(depth)),'legal_weight':'1',
            'raw_mask_combinations_removed':16**depth,
            'carrier_weights_retained':tuple(range(depth)),
            'standard_owners_retained':tuple(range(depth)),
            'tail_masks_summed':False,'inner_T_masks_summed':False}


def generate():
    seeds=spec.seed_records()
    counts={'raw':0,'same_owner_split_identity':0,'graded_block_zero':0,
            'terminal_block_mismatch':0,'surviving':0}
    paths=[]
    for seed_id,seed in enumerate(seeds):
        row=spec.ROWS[seed['row']]
        q,cell,exponents,block,entryrow,entrycol,coefficient=row
        labels=tuple(range(q+1))
        entry_block=(int(block[1]),int(block[2]))
        keep=[]
        for term in raw_lift(labels,q-2):
            counts['raw']+=1
            why=reason(term,entry_block)
            if why:
                counts[why]+=1
                continue
            counts['surviving']+=1
            # Every outer owner stays weighted, even if absent from residual tail.
            require_owners={o for _,o in term.left+term.right}
            spec.require(require_owners<=set(labels),'lost outer owner')
            keep.append({'seed':seed_id,'row':seed['row'],
                         'coefficient':int(term.coefficient*seed['coefficient']),
                         'tail':term.tail,'left':term.left,'right':term.right,
                         'entry':[entryrow,entrycol],
                         'weighted_owners':labels,
                         'deleted_prefix_owners':labels[:q-2],
                         'strict_carrier_prefix_length':q-1,
                         'prefix_mask_merger':sum_prefix_masks(q-2)})
        spec.require(len(keep)==1,'unproved one-path terminal reduction')
        spec.require(keep[0]['tail']==labels[q-2:],'unexpected residual tail')
        paths.extend(keep)
    spec.require(counts['raw']==4038 and counts['surviving']==78,'path count mismatch')
    return {'schema':'hm-refined-detector-pruned-v2',
            'base_schema':spec.SCHEMA,
            'base_certificate_sha256':hashlib.sha256(spec.encode_certificate(spec.build_certificate())).hexdigest(),
            'status':'formal_index_map_reduction_only','execution_release':False,
            'physical_source_evaluated':False,'old_four_tail_assumed':False,
            'counts':counts,'paths':paths,
            'identity_scope':'formal words use equal tuple owners; conditional label predicate also uses certified equal-carrier common-frame identities',
            'conditional_prefix_filter':{'frame':'common-original-frame',
                'J0':'none','J1':'carrier0<carrier1','J2':'carrier0<carrier1<carrier2',
                'tail_last_two':'may repeat carriers and physical labels with distinct standard tags',
                'prefix_mask_sum':'exact after strict carrier prefix; sum each four-coordinate legal partition to1; retain carrier and standard owners',
                'proof_blob':'7e12e8c7479427db87cd496763f5f003005af9c5'},
            'source_contraction':'row(left,entryrow) R_tail^t col(right,entrycol)',
            'labels':'positions in source-first sorted outer common tuple',
            'unresolved':['carrier/mask/standard label sums','source polynomial arithmetic DAG',
                          'coefficient extraction cost','peak live bytes'],
            'metadata_cap_bytes':MAX_BYTES}


def encode(certificate):
    spec.require(__debug__,'optimized Python rejected')
    data=(json.dumps(certificate,sort_keys=True,separators=(',',':'))+'\n').encode()
    canonical=(json.dumps(generate(),sort_keys=True,separators=(',',':'))+'\n').encode()
    spec.require(data==canonical,'mutated pruning certificate')
    spec.require(len(data)<=MAX_BYTES,'pruning metadata cap')
    return data

if __name__=='__main__':
    try:
        sys.stdout.buffer.write(encode(generate()))
    except spec.ContractError as exc:
        print('BLOCKED: '+str(exc),file=sys.stderr)
        sys.exit(2)
