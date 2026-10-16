"""Replay bounded artificial controls in isolated processes, never physical sources."""
import argparse,hashlib,json,os,pathlib,resource,subprocess,sys,time
HERE=pathlib.Path(__file__).resolve().parent
ROOT=HERE.parents[2]
LANES=('source-faithful-P','source-faithful-Q','source-domain-application','wave5')
def limits():
 resource.setrlimit(resource.RLIMIT_AS,(768*1024**2,768*1024**2))
 resource.setrlimit(resource.RLIMIT_CPU,(59,59))
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output');args=ap.parse_args()
 out={'schema':'bounded-wave5-replay-v1','physical_source_evaluated':False,'execution_release':False,'lanes':[]}
 for lane in LANES:
  p=HERE.parent/lane
  if lane=='wave5':
   hashes={'test_bundle_metadata.py':hashlib.sha256((p/'test_bundle_metadata.py').read_bytes()).hexdigest()}
  else:
   if not(p/'producer-ready.json').is_file():raise ValueError('producer not ready: '+lane)
   marker=json.loads((p/'producer-ready.json').read_text())
   hashes=marker.get('files_sha256',marker.get('producer_files_sha256',marker.get('files')))
   if hashes is None:raise ValueError('unknown producer marker: '+lane)
  for name,digest in hashes.items():
   if hashlib.sha256((p/name).read_bytes()).hexdigest()!=digest:raise ValueError('producer hash mismatch: '+lane+'/'+name)
  for testfile in sorted(p.glob('test*.py')):
   for optimized in(False,True):
    cmd=[sys.executable,'-B']+(['-O']if optimized else[])+[testfile.name,'-v']
    t=time.monotonic();r=subprocess.run(cmd,cwd=p,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'},text=True,capture_output=True,timeout=60,preexec_fn=limits)
    log=lane+'-'+testfile.stem+('-optimized.log'if optimized else'-normal.log');(HERE/log).write_text(r.stdout+r.stderr)
    row={'lane':lane,'testfile':testfile.name,'optimized':optimized,'returncode':r.returncode,'seconds':round(time.monotonic()-t,3),'log':log,'log_sha256':hashlib.sha256((r.stdout+r.stderr).encode()).hexdigest()};out['lanes'].append(row)
    if r.returncode:raise RuntimeError('control failure: '+lane+' see '+log)
 if args.output:(HERE/args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 print(json.dumps(out,indent=2))
if __name__=='__main__':main()
