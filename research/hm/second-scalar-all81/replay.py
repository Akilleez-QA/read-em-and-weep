#!/usr/bin/env python3
"""Finite supplied-quotient replay for all 81 L_minus coordinates; no source jobs."""
import hashlib
import itertools
import json
from fractions import Fraction as F
from math import comb
from pathlib import Path
HERE = Path(__file__).resolve().parent
MAP = 'X02[0,5]-X13[10,1]'
SHAPE = [9,44,23]
ROLES = tuple(itertools.permutations(range(4)))
FILES = {'README.md','SOURCES.md','DUPLICATE-ARRAYS.md','quotients.json','expected.json',
         'duplicate-binding.json','provenance.json','replay.py','test_replay.py'}
STATS = {'quotients':24,'targets':81,'computed_targets':65,'empty_boundary_targets':16,
         'requests':648,'rows':114048,'distinct_exponents':32472,'nonzero_rows':10504,
         'distinct_nonzero_coefficients':3152,'nonzero_signed_selections':552}

def require(condition, message):
    if not condition:
        raise ValueError(message)


def integer(value):
    require(type(value) is str, 'Integers must be canonical decimal strings')
    result = int(value)
    require(str(result) == value, 'Noncanonical integer')
    return result


def enc(value):
    return [str(value.numerator), str(value.denominator)]


def rat(value):
    require(type(value) is list and len(value) == 2, 'Invalid rational pair')
    n, d = map(integer, value)
    require(d > 0, 'Nonpositive denominator')
    result = F(n, d)
    require(enc(result) == value, 'Unreduced rational')
    return result


def unique(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, 'Duplicate JSON key')
        result[key] = value
    return result


def load(path):
    return json.loads(Path(path).read_text(), object_pairs_hook=unique)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def kernel():
    """Exact binomial expansion of G(T,z)^(-70) modulo (T^9,z^23)."""
    h = {(0, 1): 1, (1, 0): 1, (1, 1): 3, (1, 2): 1, (2, 1): 1, (2, 2): 1}
    answer = {(0, 0): 1}
    power = {(0, 0): 1}
    for n in range(1, 32):
        following = {}
        for (a, b), c in power.items():
            for (i, j), d in h.items():
                if a + i < 9 and b + j < 23:
                    key = (a + i, b + j)
                    following[key] = following.get(key, 0) + c * d
        power = following
        factor = (-1) ** n * comb(69 + n, n)
        for key, c in power.items():
            answer[key] = answer.get(key, 0) + factor * c
    require(not power, 'Nilpotence bound failed')
    return answer


def digest(value):
    return hashlib.sha256(json.dumps(value,separators=(',',':')).encode()).hexdigest()


def verify_manifest(directory):
    directory=Path(directory)
    manifest=load(directory/'manifest.json')
    require(manifest['schema']=='Lminus-all81-manifest-v1','Manifest schema')
    require(set(manifest['files'])==FILES,'Manifest file set')
    require({p.name for p in directory.iterdir()}-{'__pycache__'}==FILES|{'manifest.json'},'Unexpected package file')
    for name,record in manifest['files'].items():
        p=directory/name
        require(p.is_file() and not p.is_symlink(),'Invalid package file')
        require(record=={'sha256':sha(p),'bytes':p.stat().st_size},'Package digest mismatch')


def read_quotients(data):
    require(data['schema']=='Lminus-all81-quotients-v1' and data['field']=='Q' and data['scalar_map']==MAP,'Wrong map/field')
    require(len(data['quotients'])==24,'Missing quotient')
    result={}
    for q in data['quotients']:
        roles=tuple(q['roles'])
        require(all(type(x)is int for x in roles) and roles in ROLES and roles not in result,'Invalid/duplicate roles')
        require(q['shape']==SHAPE and all(type(x)is int for x in q['shape']),'Wrong shape')
        require(q['denominator']=='64','Wrong denominator')
        require(q['homogeneous_degrees_separated']is True and q['pairing_aggregated']is False,'Lost grading')
        terms=q['coefficients'];require(digest(terms)==q['array_sha256'],'Array digest mismatch')
        require(len(terms) in (203,233),'Wrong full quotient size')
        values={};slots=[]
        for row in terms:
            require(type(row)is list and len(row)==4,'Malformed coefficient')
            slot=tuple(row[:3]);require(all(type(v)is int and 0<=v<b for v,b in zip(slot,SHAPE)),'Invalid slot')
            c=integer(row[3]);require(c and slot not in values,'Zero/duplicate term')
            values[slot]=F(c,64);slots.append(slot)
        require(slots==sorted(slots),'Unsorted quotient')
        for key in ('original_quotient_sha256','completion_receipt_sha256','configuration_sha256',
                    'normalized_source_sha256','compact_source_sha256','checkpoint_sha256'):
            value=q[key];require(type(value)is str and len(value)==64 and all(c in '0123456789abcdef'for c in value),'Invalid historical pin')
        result[roles]=values
    require(set(result)==set(ROLES),'Incomplete quotient coverage')
    return result


def selection(roles,m,values,weights):
    i,j,k,l=roles;require(m[i]==2,'Inactive orientation selected')
    S=sum(m);d,L,w=6+m[j],22-m[l],35+S
    rows=[];unsigned=F(0)
    for r in range(d+1):
        for ell in range(L+1):
            ex=[0]*4;ex[i],ex[j],ex[k],ex[l]=272,215-r,157-S+r-ell,47+ell
            require(sum(ex)==691-S,'Wrong physical degree')
            coefficient=values.get((r,w,ell),F(0));weight=weights[d-r,L-ell]
            weighted=coefficient*weight;unsigned+=weighted
            rows.append([[r,w,ell],ex,str(weight),enc(coefficient),enc(weighted)])
    sign=(-1)**sum(roles[a]>roles[b]for a in range(4)for b in range(a+1,4))
    return rows,sign,sign*unsigned


def verify(data,expected):
    quotients=read_quotients(data)
    require(expected['schema']=='Lminus-all81-expected-v1' and expected['statistics']==STATS,'Wrong expected metadata')
    require(expected['source_regeneration_reproduced']is False and expected['full_obstruction_computed']is False,'Overbroad evidence scope')
    require(len(expected['targets'])==81,'Missing target')
    weights=kernel();distinct={};row_count=nonzero_rows=requests=nonzero_selections=empty_count=0;coordinates=[]
    for index,m0 in enumerate(itertools.product((2,1,0),repeat=4)):
        m=list(m0);target=expected['targets'][index];empty=max(m)<=1
        require(type(target['index'])is int and target['index']==index,'Wrong target index')
        require(target['m']==m and all(type(x)is int for x in target['m']),'Wrong monomial')
        require(target['laurent']==[-v-1 for v in m] and all(type(x)is int for x in target['laurent']),'Wrong Laurent exponents')
        require(target['empty_boundary']is empty,'Wrong empty-boundary classification')
        active=[r for r in ROLES if m[r[0]]==2]
        require(len(target['edges'])==len(active),'Wrong target edge coverage')
        total=F(0)
        for roles,record in zip(active,target['edges']):
            rows,sign,value=selection(roles,m,quotients[roles],weights)
            actual={'roles':list(roles),'sign':sign,'signed':enc(value),'rows':len(rows),
                    'nonzero_rows':sum(row[3][0]!='0'for row in rows),'rows_sha256':digest(rows)}
            require(record==actual,'Oriented contraction/row digest mismatch')
            require(type(record['sign'])is int and type(record['rows'])is int and type(record['nonzero_rows'])is int,'Invalid record integer')
            require(all(type(x)is int for x in record['roles']),'Invalid record roles')
            rat(record['signed']);total+=value;requests+=1;nonzero_selections+=bool(value)
            for row in rows:
                ex=tuple(row[1]);c=rat(row[3]);row_count+=1;nonzero_rows+=bool(c)
                require(ex not in distinct or distinct[ex]==c,'Inconsistent repeated physical coefficient')
                distinct[ex]=c
        require(total==rat(target['value'])==0,'Nonzero or incorrect scalar coordinate')
        empty_count+=empty;coordinates.append(enc(total))
    counts={'quotients':len(quotients),'targets':len(coordinates),'computed_targets':81-empty_count,
        'empty_boundary_targets':empty_count,'requests':requests,'rows':row_count,
        'distinct_exponents':len(distinct),'nonzero_rows':nonzero_rows,
        'distinct_nonzero_coefficients':sum(bool(c)for c in distinct.values()),
        'nonzero_signed_selections':nonzero_selections}
    require(counts==STATS,'Global counts mismatch')
    return {'status':'PASS_ALL81_SUPPLIED_QUOTIENT_REPLAY','field':'Q','scalar_map':MAP,
        'coordinates':coordinates,'statistics':counts,'source_regeneration_reproduced':False,
        'full_obstruction_computed':False}


def verify_duplicates(data,report):
    require(report['sourceSymmetryProved']is False and report['actualSourceNodesReevaluated']==0,'Overbroad duplicate scope')
    require(report['uniqueArraysAmong18']==12 and len(report['duplicatePairs'])==6,'Wrong duplicate scope')
    require({tuple(p['roles']) for p in report['duplicatePairs']}=={('0123','2301'),('0132','2310'),('0213','2031'),('0231','2013'),('0312','2130'),('0321','2103')},'Wrong duplicate pair coverage')
    arrays={''.join(map(str,q['roles'])):q for q in data['quotients']};values=read_quotients(data);weights=kernel()
    original=[q for q in data['quotients']if q['roles'][0]<3]
    require(len({q['array_sha256']for q in original})==12,'Wrong observed duplicate count')
    permutation=[2,3,0,1];m=[2,2,2,0];mapped=[0]*4
    for axis in range(4):mapped[permutation[axis]]=m[axis]
    count=0
    for pair in report['duplicatePairs']:
        a,b=pair['roles'];left,right=arrays[a],arrays[b];ra=tuple(left['roles']);rb=tuple(right['roles'])
        require(tuple(permutation[x]for x in ra)==rb,'Wrong physical permutation')
        require(left['coefficients']==right['coefficients'],'Unequal duplicate arrays')
        for role,q in ((a,left),(b,right)):
            historical=report['roles'][role]
            for public,original in {'configuration_sha256':'configurationSHA256',
                'normalized_source_sha256':'normalizedSourceSHA256','compact_source_sha256':'compactSourceSHA256',
                'checkpoint_sha256':'checkpointSHA256','original_quotient_sha256':'quotientSHA256',
                'array_sha256':'coefficientArraySHA256','completion_receipt_sha256':'independentCompletionReceiptSHA256'}.items():
                require(q[public]==historical[original],'Duplicate receipt binding mismatch')
        for key in ('configuration_sha256','normalized_source_sha256','compact_source_sha256','checkpoint_sha256'):
            require(left[key]!=right[key],'Reused source/checkpoint binding')
        lrows,ls,lv=selection(ra,m,values[ra],weights);rrows,rs,rv=selection(rb,mapped,values[rb],weights)
        require(ls==rs and lv==rv and enc(lv)==pair['originalSignedValue']==pair['permutedTargetSignedValue'],'Selector covariance value/sign')
        require(pair['originalTarget']==m and pair['permutedTarget']==mapped,'Wrong mapped target')
        for lrow,rrow in zip(lrows,rrows):
            ex=[0]*4
            for axis in range(4):ex[permutation[axis]]=lrow[1][axis]
            require(rrow==[lrow[0],ex,*lrow[2:]],'Selector row covariance')
        require(len(lrows)==len(rrows)==pair['mappedRowCount'],'Covariance row count')
        require(enc(selection(rb,m,values[rb],weights)[2])==pair['sameFixedM2220TargetOnSecondRole'],'Wrong fixed-target comparison')
        count+=len(lrows)
    require(count==report['exactMappedSelectorRowsCompared']==1086,'Wrong total mapped rows')
    return {'duplicate_pairs':6,'mapped_rows':count,'physical_permutation':permutation,
            'symbolic_source_symmetry_proved':False,'historical_terminal_reconstruction_repeated':False}


def replay(directory=HERE):
    directory=Path(directory);verify_manifest(directory)
    data=load(directory/'quotients.json');result=verify(data,load(directory/'expected.json'))
    provenance=load(directory/'provenance.json')
    require(provenance['historical_archives_distributed'] is False and provenance['symbolic_source_symmetry_proved'] is False and provenance['source_DAG_nodes_reevaluated_by_seal']==0,'Historical evidence scope changed')
    result['duplicate_array_checks']=verify_duplicates(data,load(directory/'duplicate-binding.json'))
    return result


if __name__=='__main__':
    print(json.dumps(replay(),indent=2))
