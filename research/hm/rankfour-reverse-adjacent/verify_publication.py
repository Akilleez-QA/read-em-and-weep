#!/usr/bin/env python3
"""Authenticate and replay this mathematical publication without network access."""
from pathlib import Path
import hashlib,json,subprocess,sys,tempfile
ROOT=Path(__file__).resolve().parent

def require(ok,message):
    if not ok:raise RuntimeError(message)

def authenticate(folder):
    entries=json.loads((folder/'MANIFEST.json').read_text())['files']
    for name,expected in entries.items():
        raw=(folder/name).read_bytes()
        require(len(raw)==expected['bytes'],'byte length: '+name)
        require(hashlib.sha256(raw).hexdigest()==expected['sha256'],'SHA256: '+name)
        require(hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==expected['git_blob_sha1'],'Git blob: '+name)

def shape(items):
    return tuple(sorted((x['degree'],x.get('coefficient',x.get('irrep')))for x in items))

def rows(result):
    out={}
    for case in result['cases']:
        endpoints=tuple(case.get('endpoint_degrees',case.get('endpoints')))
        for x in case['Euler_survivors']:
            key=(endpoints,shape(x['F0']),shape(x['D0']))
            require(key not in out,'duplicate survivor')
            out[key]=(x['minus_chi_F2_2'],x['minus_chi_D1_3'])
    return out

def main():
    authenticate(ROOT);authenticate(ROOT/'independent')
    author=json.loads((ROOT/'RESULT.json').read_text())
    independent=json.loads((ROOT/'independent/RESULT.json').read_text())
    require(author['checks']==10951 and author['mutation_rejections']==54,'frozen author counts')
    require(independent['checks']==470,'frozen independent count')
    require(rows(author)==rows(independent) and len(rows(author))==14,'all fourteen pairs and both characters agree')
    endpoints=json.loads((ROOT/'independent/ENDPOINTS.json').read_text())
    require({d:sorted(map(shape,ss))for d,ss in endpoints.items()}==
            {d:sorted(map(shape,ss))for d,ss in author['derived_endpoint_splittings'].items()},'all endpoint domains agree')
    snapshots=['PROOF.md','verify.py','RESULT.json','INPUTS.json']+[
        x.relative_to(ROOT).as_posix()for x in sorted((ROOT/'inputs').glob('*.md'))]
    for name in snapshots:
        require((ROOT/name).read_bytes()==(ROOT/'independent/author'/name).read_bytes(),'reviewed snapshot differs: '+name)
    replays=[]
    with tempfile.TemporaryDirectory() as temp:
        for program,result in [('verify.py','RESULT.json'),('independent/verify.py','independent/RESULT.json'),
                               ('independent/author/verify.py','independent/author/RESULT.json')]:
            for optimized in (False,True):
                command=[sys.executable]+(['-O']if optimized else [])+[str(ROOT/program)]
                run=subprocess.run(command,capture_output=True,cwd=temp if optimized else ROOT)
                require(run.returncode==0,run.stderr.decode())
                require(run.stdout==(ROOT/result).read_bytes(),'replay differs: '+program)
                replays.append({'program':program,'optimized':optimized,'alternate_directory':optimized,'status':'PASS'})
        control=subprocess.run([sys.executable,str(ROOT/'independent/test_controls.py')],capture_output=True,cwd=temp)
        require(control.returncode==0,control.stderr.decode())
        require(control.stdout==(ROOT/'independent/CONTROLS.json').read_bytes(),'mutation-control replay differs')
    return {'status':'PASS','scope':'Conditional ordered maximal rank-four (3,2) exclusion only.',
            'author_checks':10951,'author_contract_mutations':54,'independent_checks':470,
            'executed_independent_mutations':9,'all_endpoint_domains_match':True,
            'all14_pairs_and_both_characters_match':True,'reviewed_author_snapshots_match':True,
            'normal_optimized_portable_replays':replays}
if __name__=='__main__':print(json.dumps(main(),indent=2,sort_keys=True))
