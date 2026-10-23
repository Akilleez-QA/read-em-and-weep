#!/usr/bin/env python3
"""Two additional complete source cuts; empty index113 relation is not a label gate."""
import argparse,hashlib,json
import verify_source_frontier_through877 as previous
ROOT=previous.ROOT;require=previous.require;accounting=previous.accounting
PREVIOUS_SHA256='972d7674776a804568371ca20962ab90517e8ab06997a2f1c2a6e6a835652c96'
def load_inputs():
 s,c,p=previous.load_inputs();snapshot=previous.build(s,c,p)
 raw=(ROOT/'frontier-source-through877.json').read_bytes();require(hashlib.sha256(raw).hexdigest()==PREVIOUS_SHA256 and json.loads(raw)==snapshot,'Through877 predecessor changed')
 return snapshot,c,p

def build(snapshot,catalog,pins):
 result=previous.make(snapshot,catalog,pins,previous.LATER,'source-through882','frontier-source-through877.json',PREVIOUS_SHA256,377,351)
 require(result['nonempty_relation_label_count']==4,'Expected one empty necessary relation')
 require([r['id'] for r in result['records'] if r['relation_empty']]==[previous.LABELS[113]],'Wrong empty relation')
 return result

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();result=build(*load_inputs());p=ROOT/'frontier-source-through882.json'
 if args.write:p.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
 require(json.loads(p.read_text())==result,'Artifact differs from replay');print('PASS through882: 5 registered labels, 4 nonempty relations, 351 necessary pairs, 26 new pair cuts; label gate closed')
if __name__=='__main__':main()
