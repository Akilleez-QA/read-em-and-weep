#!/usr/bin/env python3
"""Exact ten-row source coverage, not a new source or frontier enumeration."""
from pathlib import Path
import json,hashlib
from characters import *
p=Path(__file__).resolve().parent
expected=[('ff',[0,0,0,0,0,2,0,1]),('ef',[0,0,0,0,1,1,0,1]),
 ('ee',[0,0,0,0,2,0,0,1]),('cf',[0,0,1,0,0,1,0,1]),
 ('ce',[0,0,1,0,1,0,0,1]),('cc',[0,0,2,0,0,0,0,1]),
 ('bf',[0,1,0,0,0,1,0,1]),('be',[0,1,0,0,1,0,0,1]),
 ('bc',[0,1,1,0,0,0,0,1]),('bb',[0,2,0,0,0,0,0,1])]
for name,sha in [('one-one-endpoint-necessary-pairs.json','fe0afa410d89340d3082dc814277f89fbb582c19'),('rank-three-quotient-frontier-144.json','8b5971092f9ef762584912609fd5e9301c4e271d')]:
 b=(p/'audit-inputs'/name).read_bytes();assert hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()==sha
catalog=json.loads((p/'audit-inputs/one-one-endpoint-necessary-pairs.json').read_text())[113]
assert catalog['A']==[[-10,'one'],[2,'one'],[16,'one']]
assert catalog['B']==[[-18,'one'],[-4,'one'],[8,'one']] and catalog['defect']==0
assert catalog['compatible_E_types']==[row for _,row in expected]
rows=json.loads((p/'audit-inputs/rank-three-quotient-frontier-144.json').read_text())['cases']
assert [r['source_index'] for r in rows if r['id']=='G3.11.ad509d55173f']==[113]
manifest=json.loads((p/'coverage.json').read_text())
assert manifest['original_commit']=='db51525015bb7c5e825833d550d08dedf6f6ea96'
assert manifest['source_index']==113 and manifest['stable_label']=='G3.11.ad509d55173f'
assert [(r['name'],r['tuple']) for r in manifest['coverage']]==expected
assert len({tuple(r['tuple']) for r in manifest['coverage']})==10
for r in manifest['coverage']:
 a,b,c,d,e,f,g,h=r['tuple']
 top=va(va(vk(c+g+h-1,chars['V']),vk(d+e+g+h,chars['P'])),vk(f+g,chars['D']))
 if r['kind']=='strict_top':
  assert r['name'] in ('ee','cc')
  target=va(sym(4),sym(18))
  assert target==rep('A+V+2P+2D')
  assert top==rep('3P' if r['name']=='ee' else '2V+P')
  assert any(a>b for a,b in zip(dec(top),dec(target)))
 else:
  assert r['kind']=='whole_source'
  assert isinstance(r['pr'],int) and r['pr']>0
  assert len(r['commit'])==40 and all(x in'0123456789abcdef' for x in r['commit'])
  assert r['path'].startswith('research/hm/') and r['path'].endswith('.md')
  assert r['url']==f"https://github.com/Akilleez-QA/read-em-and-weep/blob/{r['commit']}/{r['path']}"
pins=json.loads((p/'source-proof-pins.json').read_text())
expected_urls={r['url'] for r in manifest['coverage'] if r['kind']=='whole_source'}
expected_urls.add('https://github.com/Akilleez-QA/read-em-and-weep/blob/7b5b3371a82cb92f46ea60895e45617d0891a5b0/research/hm/profile11-source113-cf-reduction/PROOF.md')
assert len(pins)==7 and {r['url'] for r in pins.values()}==expected_urls
for r in pins.values():
 for field,length in [('git_blob',40),('sha256',64)]:
  assert len(r[field])==length and all(c in '0123456789abcdef' for c in r[field])
print('PASS: original stable label and endpoints; exact ordered ten-tuple set with no duplicates or omissions; ee/cc direct strict-top contradictions; eight immutable whole-source records; seven exact theorem-byte pin records.')
print('This fixed coverage audit does not re-prove source theorems or establish a current global frontier count.')
