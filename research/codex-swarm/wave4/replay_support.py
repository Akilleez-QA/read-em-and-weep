"""Authenticate and replay only the published abstract source-integration controls."""
import argparse, hashlib, json, os, re, resource, subprocess, sys, tempfile
from pathlib import Path
PIN='10810ee877fdaf291399198ad60d7dd0c316a42d'
PREFIX='research/hm/null-source-integration/'
PACKAGES=(('complementary-pair','02d0e727ffb95dfd9281906cc284c56e8bffd018'),)
def git(*args):return subprocess.check_output(['git',*args])
def limits():resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,512*1024**2))
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--replay',action='store_true');a=p.parse_args()
 result={'schema':'codex-wave4-source-support-replay-v1','source_commits':sorted(set(pin for _,pin in PACKAGES)),'packages':{},'physical_source_evaluated':False,'arithmetic_admission':False}
 with tempfile.TemporaryDirectory(prefix='codex-wave4-support-') as tmp:
  for name,pin in PACKAGES:
   prefix=PREFIX+name+'/'
   files=git('ls-tree','-r','--name-only',pin,prefix).decode().splitlines()
   target=Path(tmp)/name;target.mkdir();blobs={}
   for path in files:
    if '..' in Path(path[len(prefix):]).parts:raise ValueError('unexpected source path')
    raw=git('show',pin+':'+path);base=path[len(prefix):]
    (target/base).parent.mkdir(parents=True,exist_ok=True)
    (target/base).write_bytes(raw)
    blobs[base]={'sha256':hashlib.sha256(raw).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()}
   manifest=(target/'SHA256SUMS').read_text().splitlines()
   for line in manifest:
    sha,filename=line.split(None,1)
    filename=filename.removeprefix('./')
    if Path(filename).is_absolute() or '..' in Path(filename).parts:raise ValueError('unsafe manifest path')
    if filename not in blobs or blobs[filename]['sha256']!=sha:raise ValueError('source integrity: '+filename)
   entry={'source_commit':pin,'files':blobs,'manifest_entries_checked':len(manifest),'replay':'not_requested'}
   if a.replay:
    run=subprocess.run([sys.executable,'-B','-m','unittest','discover','-s',str(target),'-v'],capture_output=True,text=True,timeout=45,preexec_fn=limits)
    text=run.stdout+run.stderr
    count=re.search(r'Ran (\d+) tests?',text)
    if run.returncode or not count or not text.rstrip().endswith('OK'):raise RuntimeError(text)
    entry.update(replay='pass',unittest_cases=int(count[1]),log_sha256=hashlib.sha256(text.encode()).hexdigest(),timeout_seconds=45,address_space_cap_bytes=512*1024**2)
   result['packages'][name]=entry
 result['runtime']={'python':sys.version.split()[0]}
 print(json.dumps(result,indent=2,sort_keys=True))
if __name__=='__main__':main()
