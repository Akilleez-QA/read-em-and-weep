#!/usr/bin/env python3
"""Authenticate the public packet and replay its exact mathematical certificates."""
from pathlib import Path
import hashlib,json,subprocess,sys,tempfile
ROOT=Path(__file__).resolve().parent

def require(ok,message):
    if not ok:raise RuntimeError(message)

def authenticate(folder):
    entries=json.loads((folder/'MANIFEST.json').read_text())['files']
    if isinstance(entries,list):entries={x['file']:x for x in entries}
    for name,want in entries.items():
        raw=(folder/name).read_bytes()
        require(len(raw)==want['bytes'],'byte length: '+name)
        require(hashlib.sha256(raw).hexdigest()==want['sha256'],'SHA256: '+name)
        require(hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==want['git_blob_sha1'],'Git blob: '+name)

def main():
    for folder in [ROOT,ROOT/'independent',ROOT/'independent/author']:authenticate(folder)
    author=json.loads((ROOT/'RESULT.json').read_text())
    independent=json.loads((ROOT/'independent/RESULT.json').read_text())
    require(author['checks']==12643 and independent['checks']==603,'frozen arithmetic check counts')
    require(independent['intertwiner_multiplicity']==1,'reported intertwiner multiplicity is the computed value one')
    require(author['ledger_rows']==31 and author['positive_defect_rows']==24,'general positive defects retained')
    require(independent['coarse_profile_eliminations']==0,'no profile exclusion')
    require(json.loads((ROOT/'LEDGER.json').read_text())==author['ledger'],'ledger projection')
    require(json.loads((ROOT/'ENDPOINTS.json').read_text())==author['endpoint_shapes'],'endpoint projection')
    snapshot=json.loads((ROOT/'independent/author/MANIFEST.json').read_text())['files']
    for item in snapshot:
        name=item['file']
        require((ROOT/name).read_bytes()==(ROOT/'independent/author'/name).read_bytes(),'reviewed author bytes: '+name)
    for name in ['RESULT-O.json','RESULT-OTHER-CWD.json']:
        require((ROOT/name).read_bytes()==(ROOT/'RESULT.json').read_bytes(),'retained author replay: '+name)
    for name in ['AUTHOR-RUN.json','AUTHOR-RUN-O.json']:
        require((ROOT/'independent'/name).read_bytes()==(ROOT/'RESULT.json').read_bytes(),'reviewer author replay: '+name)
    replays=[]
    with tempfile.TemporaryDirectory()as temp:
        for program,result in [('verify.py','RESULT.json'),('independent/verify.py','independent/RESULT.json'),('independent/author/verify.py','independent/author/RESULT.json')]:
            for optimized in(False,True):
                run=subprocess.run([sys.executable]+(['-O']if optimized else [])+[str(ROOT/program)],cwd=temp if optimized else ROOT,capture_output=True)
                require(run.returncode==0,run.stderr.decode())
                require(run.stdout==(ROOT/result).read_bytes(),'portable replay: '+program)
                replays.append({'program':program,'optimized':optimized,'alternate_directory':optimized,'status':'PASS'})
        for program,result in [('independent/test_controls.py','independent/CONTROLS.json'),('independent/check_package.py','independent/PACKAGE-CHECK.json')]:
            run=subprocess.run([sys.executable,str(ROOT/program)],cwd=temp,capture_output=True)
            require(run.returncode==0,run.stderr.decode())
            require(run.stdout==(ROOT/result).read_bytes(),'portable review replay: '+program)
    return {'status':'PASS','scope':'Restricted dual-cubic image ranks 1..3 only; whole ordered rank-four (3,1) remains open.',
            'author_checks':12643,'independent_checks':603,'executed_independent_mutations':13,
            'reported_intertwiner_multiplicity':1,'complete_domains_match':True,'reviewed_author_snapshots_match':True,
            'general_ledger_rows':31,'positive_defect_rows':24,'coarse_profile_eliminations':0,
            'normal_optimized_portable_replays':replays}
if __name__=='__main__':print(json.dumps(main(),indent=2,sort_keys=True))
