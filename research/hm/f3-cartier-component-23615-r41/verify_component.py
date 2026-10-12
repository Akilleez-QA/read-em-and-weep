"""Verify this fixed supplied F3 component; never recompute its source DAG."""
import hashlib,json,os,re,stat,sys

CATALOG="4df4f5af0f7688eff7f55c189ec1dd5a9d350b3e6e39efcdb24d2145fe841513"
SPEC="6d773fab0c9ffa021dc4de57cf6cf3cc3c495325652fee900f23ec7f6d3b3b7b"
ROWS="ab8a327f73a88c781f377925b54ad6496cc20825ef9b83808f50bc0af916b426"
CAPS={"README.md":3456,"ATTRIBUTION.md":4096,"SHA256SUMS":4736,
  "verify_component.py":8192,"test_verify_component.py":4096,
  "value-files.json":4901,"component-receipt.json":3842,
  "held-state-receipt.json":1112,"spec.json":839}

def need(ok,message):
 if not ok: raise ValueError(message)

def sha(raw):
 return hashlib.sha256(raw).hexdigest()

def canon(value):
 return json.dumps(value,sort_keys=True,separators=(",",":"),
      ensure_ascii=True,allow_nan=False).encode()

def same(a,b):
 if type(a) is not type(b): return False
 if type(a) is dict:
  return a.keys()==b.keys() and all(same(a[k],b[k]) for k in a)
 if type(a) in (list,tuple):
  return len(a)==len(b) and all(same(x,y) for x,y in zip(a,b))
 return a==b

def invalid(_):
 raise ValueError("invalid JSON number")

def unique(pairs):
 out={}
 for key,value in pairs:
  need(key not in out,"duplicate JSON key")
  out[key]=value
 return out

def integer(text):
 need(len(text.lstrip("-"))<=32,"integer bound")
 return int(text)

def parse_json(raw,newline=False):
 value=json.loads(raw,object_pairs_hook=unique,parse_int=integer,
      parse_float=invalid,parse_constant=invalid)
 need(raw==canon(value)+(b"\n" if newline else b""),"canonical JSON")
 return value

def parts(name):
 need(type(name) is str and bool(re.fullmatch(
  r"[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)*",name)),"relative path")
 out=name.split("/")
 need(all(p not in (".","..") for p in out),"path escape")
 return out

def directory(parent,name):
 return os.open(name,os.O_RDONLY|os.O_DIRECTORY|os.O_NOFOLLOW,
     dir_fd=parent)

def root_fd(path):
 fd=directory(None,"/")
 try:
  for name in os.path.abspath(path).split("/")[1:]:
   if name:
    child=directory(fd,name)
    os.close(fd)
    fd=child
  return fd
 except BaseException:
  os.close(fd)
  raise

def read(root,name,cap,pin=None):
 names=parts(name)
 fd=os.dup(root)
 try:
  for item in names[:-1]:
   child=directory(fd,item)
   os.close(fd)
   fd=child
  src=os.open(names[-1],os.O_RDONLY|os.O_NOFOLLOW|os.O_NONBLOCK,
       dir_fd=fd)
  try:
   st=os.fstat(src)
   need(stat.S_ISREG(st.st_mode) and 0<=st.st_size<=cap,
     "bounded regular file")
   chunks,left=[],st.st_size+1
   while left:
    chunk=os.read(src,left)
    if not chunk:
     break
    chunks.append(chunk)
    left-=len(chunk)
   raw=b"".join(chunks)
   end=os.fstat(src)
   stamp=lambda s: (s.st_dev,s.st_ino,s.st_size,s.st_mtime_ns,s.st_ctime_ns)
   need(len(raw)==st.st_size and not os.read(src,1)
     and stamp(st)==stamp(end),"immutable exact read")
  finally:
   os.close(src)
 finally:
  os.close(fd)
 need(pin is None or sha(raw)==pin,"file hash")
 return raw

def unpack(raw):
 need(raw[:9]==b"F3SLICE1\n" and len(raw)>=13,"frame magic")
 size=int.from_bytes(raw[9:13],"big")
 need(0<size<=2048 and len(raw)>=13+size,"header size")
 hd=parse_json(raw[13:13+size])
 need(type(hd) is dict,"header object")
 digits=hd.get("digits")
 size2=hd.get("payloadBytes")
 need(type(digits) is int and 0<digits<=23548 and
   type(size2) is int and size2==(digits+3)//4,"body dimensions")
 body=raw[13+size:]
 need(len(body)==size2,"body length")
 need(hd.get("payloadSHA256")==sha(body),"body SHA256")
 if digits%4:
  need(body[-1] >> (2*(digits%4))==0,"nonzero padding")
 return hd,body

def trits(body,digits):
 for j in range(digits):
  value=(body[j//4] >> (2*(j%4))) & 3
  need(value!=3,"invalid F3 trit")
  yield value

def logical(q):
 need(type(q) in (tuple,list) and len(q)==4 and
   all(type(v) is int for v in q),"native coordinates")
 need(all(0<=q[k]<=(27,27,28,28)[k] for k in range(4))
   and 47<=sum(q)<=85,"quotient keep")
 e=tuple(3*q[k]+(2,1,1,1)[k] for k in range(4))
 need(all(0<=e[k]<=(83,83,85,85)[k] for k in range(4))
   and 146<=sum(e)<=260
   and sum((e[k]%3)*3**k for k in range(4))==41,
   "logical keep")
 return e

def row(e,c):
 return ("[[%d,%d,%d,%d],%d]\n"%(*e,c)).encode()

def transaction(x,hashes):
 need(type(x) is int and 0<=x<28 and len(hashes)==28,"transaction index")
 first,count=(1,13) if x<13 else ((14,13) if x<26 else (27,2))
 return dict(transactionFirst=first,transactionCount=count,
    transactionOrdinal=x+1-first,
    transactionPreviousSHA256=hashes[first-2] if first>1 else "0"*64)

def check(path):
 root=root_fd(path)
 try:
  seen={}
  raw=read(root,"value-files.json",4901,CATALOG)
  seen["value-files.json"]=sha(raw)
  catalog=parse_json(raw,True)
  files={}
  for entry in catalog["files"]:
   need(type(entry) is list and len(entry)==3,"catalog row")
   name,size,digest=entry
   parts(name)
   need(name not in files and type(size) is int and 0<size<=8192
     and type(digest) is str and re.fullmatch("[0-9a-f]{64}",digest),
     "catalog entry")
   files[name]=(size,digest)
  frames={name for name in files if name.endswith(".f3s")}
  need(len(frames)==28 and len(files)==32 and set(files)==frames |
    {"frames/HEAD.json","component-receipt.json","held-state-receipt.json",
    "spec.json"},"value file set")
  need(set(os.listdir(root))==set(CAPS)|{"frames"},"exact root file set")
  folder=directory(root,"frames")
  try:
   need(set(os.listdir(folder))=={n.split("/")[1] for n in frames} |
     {"HEAD.json"},"exact frames file set")
  finally:
   os.close(folder)

  def get(name):
   cap,pin=files.get(name,(CAPS.get(name,0),None))
   data=read(root,name,cap,pin)
   need(name not in files or len(data)==cap,"catalog bytes")
   seen[name]=sha(data)
   return data

  receipt=parse_json(get("component-receipt.json"),True)
  parse_json(get("held-state-receipt.json"),True)
  spec=parse_json(get("spec.json"))
  store=receipt["store"]
  hashes=store["orderedFrameSHA256"]
  need(len(hashes)==len(set(hashes))==28 and
    frames=={"frames/"+h+".f3s" for h in hashes},"ordered frame set")
  need(seen["spec.json"]==SPEC==store["specSHA256"],"spec pin")
  head=parse_json(get("frames/HEAD.json"))
  need(seen["frames/HEAD.json"]==store["headSHA256"] and
    same(head,dict(schema=spec["schema"],contractSHA256=SPEC,
        count=28,lastSHA256=hashes[-1])),"HEAD")
  full,count=hashlib.sha256(),0
  for x,digest in enumerate(hashes):
   hd,body=unpack(get("frames/"+digest+".f3s"))
   sem,ones,twos=hashlib.sha256(),0,0
   for j,value in enumerate(trits(body,23548)):
    if value:
     q=(x,j//841,(j//29)%29,j%29)
     e=logical(q)
     sem.update(row(q,value))
     full.update(row(e,value))
     ones+=value==1
     twos+=value==2
   want=dict(schema=spec["schema"],sequence=x+1,
    previousSHA256=hashes[x-1] if x else "0"*64,contractSHA256=SPEC,
    sourcePinsSHA256=sha(canon(spec["sourcePins"])),sourceNode=133174,
    x0=x,origin=[x,0,0,0],shape=[28,29,29],
    keepBounds=spec["keepBounds"],keepMask=spec["keepMask"],
    digits=23548,payloadBytes=5887,complete=True,terms=ones+twos,
    ones=ones,twos=twos,semanticSHA256=sem.hexdigest(),
    payloadSHA256=sha(body),**transaction(x,hashes))
   need(same(hd,want),"frame metadata")
   count+=ones+twos
  need(count==95082 and full.hexdigest()==ROWS,"logical count/hash")
  for name in CAPS:
   if name not in seen and name!="SHA256SUMS":
    get(name)
  want="".join(seen[n]+"  "+n+"\n" for n in sorted(seen)).encode()
  need(len(seen)==37 and read(root,"SHA256SUMS",4736)==want,
    "SHA256SUMS")
  return dict(status="PASS_SUPPLIED_COMPONENT_VALUE",frames=28,
     denseTrits=659344,nonzeroTerms=count,logicalRowsSHA256=ROWS,
     sourceDAGRecomputed=False,heldStateReconstructed=False,
     fullDetectorEstablished=False,fullObstructionEstablished=False,
     wholeBlindPairingKnown=False)
 finally:
  os.close(root)

if __name__=="__main__":
 try:
  need(len(sys.argv)<=2,"usage: verify_component.py [package-directory]")
  out=check(sys.argv[1] if len(sys.argv)==2 else os.path.dirname(__file__))
  print(canon(out).decode())
 except Exception as error:
  print("FAIL_SUPPLIED_COMPONENT_VALUE: "+str(error),file=sys.stderr)
  sys.exit(1)
