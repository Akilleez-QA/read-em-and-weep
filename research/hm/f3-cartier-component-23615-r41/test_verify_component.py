"""Small rejection tests and full supplied-package verification (POSIX)."""
import errno
import os
import shutil
import sys
import tempfile
import unittest

sys.dont_write_bytecode=True
ROOT=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,ROOT)
import verify_component as v

def frame(body=b"\x24",digits=3,**changes):
 hd=dict(digits=digits,payloadBytes=len(body),payloadSHA256=v.sha(body))
 hd.update(changes)
 raw=v.canon(hd)
 return b"F3SLICE1\n"+len(raw).to_bytes(4,"big")+raw+body

class VerifyTests(unittest.TestCase):
 def reject(self,function,*args):
  with self.assertRaises((ValueError,OSError)):
   function(*args)

 def test_json_and_native_types(self):
  for raw in (b'{"a":1,"a":2}',b'{"a":1 }',b'NaN',b'1.0',
     b'1e0',b'01',b'1'*33,b'{}\n',b'{}x'):
   self.reject(v.parse_json,raw)
  self.assertEqual(v.parse_json(b'{"a":1}'),{"a": 1})
  self.assertFalse(v.same({"n": [1]},{"n": [True]}))
  self.assertFalse(v.same({"complete": True},{"complete": 1}))
  self.assertFalse(v.same([0],[0.0]))
  self.reject(v.unpack,frame(digits=True))
  self.reject(v.unpack,frame(payloadBytes=True))

 def test_payload_and_envelope(self):
  raw=frame()
  hd,body=v.unpack(raw)
  self.assertEqual(list(v.trits(body,hd["digits"])),[0,1,2])
  for bad in (b"",raw[:8],raw[:-1],raw+b"x",
     raw[:-1]+bytes([raw[-1] ^ 1]),
     b"X"+raw[1:],raw[:9]+b"\xff"*4+raw[13:]):
   self.reject(v.unpack,bad)
  self.reject(v.unpack,frame(body=b"\x04",digits=1))
  self.reject(v.unpack,frame(body=b"",digits=1))
  hd,body=v.unpack(frame(body=b"\x03",digits=1))
  self.reject(lambda: list(v.trits(body,hd["digits"])))

 def test_quotient_vs_logical(self):
  q=(0,0,19,28)
  e=v.logical(q)
  self.assertEqual(e,(2,1,58,85))
  self.assertEqual(v.row(e,2),b"[[2,1,58,85],2]\n")
  self.assertNotEqual(v.sha(v.row(q,2)),v.sha(v.row(e,2)))
  for bad in ((0,0,0,0),(28,0,19,28),(27,27,28,28),
     (False,0,19,28),(0,0,19)):
   self.reject(v.logical,bad)

 def test_transactions(self):
  hashes=["%064x" % n for n in range(28)]
  for x,first,count in ((0,1,13),(12,1,13),(13,14,13),
         (25,14,13),(26,27,2),(27,27,2)):
   want=dict(transactionFirst=first,transactionCount=count,
      transactionOrdinal=x+1-first,
      transactionPreviousSHA256=hashes[first-2]
      if first > 1 else "0"*64)
   self.assertTrue(v.same(v.transaction(x,hashes),want))
  wrong=dict(v.transaction(13,hashes),transactionFirst=1)
  self.reject(v.need,v.same(wrong,v.transaction(13,hashes)),"boundary")
  self.reject(v.transaction,True,hashes)
  self.reject(v.transaction,28,hashes)

 def test_paths_and_nofollow(self):
  # Four synthetic bytes total, counting the three one-byte link targets.
  folder=tempfile.mkdtemp(prefix="f3-check-",dir=os.path.dirname(ROOT))
  passed,fd=False,None
  try:
   with open(folder+"/a","xb") as out:
    out.write(b"x")
   os.mkdir(folder+"/d")
   for name,target in (("link","a"),("alias","d"),("root",".")):
    os.symlink(target,folder+"/"+name)
   fd=v.root_fd(folder)
   self.assertEqual(v.read(fd,"a",1,v.sha(b"x")),b"x")
   self.reject(v.read,fd,"a",0)
   self.reject(v.read,fd,"a",1,"0"*64)
   for name in ("../a","/a","d/../a","",".","d//a","d\\a"):
    self.reject(v.read,fd,name,1)
   for function,args in ((v.read,(fd,"link",1)),
         (v.read,(fd,"alias/a",1)),
         (v.root_fd,(folder+"/root",))):
    with self.assertRaises(OSError) as caught:
     function(*args)
    self.assertIn(caught.exception.errno,(errno.ELOOP,errno.ENOTDIR))
   passed=True
  finally:
   if fd is not None:
    os.close(fd)
   if passed:
    shutil.rmtree(folder)
   else:
    print("Retained failed synthetic fixture:",folder,file=sys.stderr)

 def test_package(self):
  result=v.check(ROOT)
  self.assertEqual(result["status"],"PASS_SUPPLIED_COMPONENT_VALUE")
  self.assertFalse(result["sourceDAGRecomputed"])

if __name__ == "__main__":
 unittest.main()
