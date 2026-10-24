#!/usr/bin/env python3
"""Independent fixed-character/degree and retained-source review checks.

This is not a proof-assistant certification of the actual differential geometry.
It imports neither the author's verifier nor characters.py, uses no assertions,
and evaluates no selected actual source coefficients, points, jets, or ranks.
"""
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PROOF_SHA256 = "145a8b2607ac5d888de52aa75ce4271fb8426a63f5123841f356a4025354fc6b"
SOURCE_BASELINES = [
 ("zero-defect.md", "e4708738bb38e39293957982d3af53be265c13ec", "research/hm/rankfour-profile11-triplet-zero-defect/PROOF.md", 5934, "0b62e7739d3ff5ef52c5e8c76e50931f99f882015c037132370707f341c425c5", "99217242681519a6a3884227d90447a8b96e13cc"),
 ("five-kernels.md", "7d71f0e2a3963cff64a069198f4415c5cfd0fe9b", "research/hm/rankfour-profile11-triplet-kernels/PROOF.md", 8501, "4d06da768074a6e813ed295a088d862ce328a4cd33b739e88e20ac1f315de36a", "163ba2126b6130befcc2351db7f6910d85fac2ec"),
 ("deep-images.md", "95af2c0fa1e3cce92496a44ef9023708735e1ec7", "research/hm/rankfour-profile11-triplet-deep-images/PROOF.md", 12085, "09424f92b56ce3b907968ccae3c065ececbfbc800fb4db0f79a04a3863f74e26", "9cf95f42505f37900f5a24c25cff07acca1b499f"),
 ("pair-defect.md", "0156405384eefb3efe08d724e682b4a839157bfc", "research/hm/rankfour-profile11-pair-defect/PROOF.md", 15519, "95cc7824898dd0bffe13f86ab1ede2947451eb3d4632e189baa608ad0de3fdec", "f409e036c549d15dc0ad03443325922575107b4d"),
 ("actual.md", "db51525015bb7c5e825833d550d08dedf6f6ea96", "research/hm/order-four-quadratic-load/ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md", 9672, "a52685fc9e7c89abf26171a15989cedeaf3bd101a2edde790a24f9cfe0179256", "b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3"),
 ("low-top.md", "236e0a3723c3d73ea7fb9e549376540a8e70508b", "research/hm/rankfour-profile11-low-top/PROOF.md", 11259, "c3d21cb63ffac4c69247e8deba8ef352f673ac3a7b2f91507bc54fbecae943af", "6565110a12173fb6ff27838d294489ec1ad53941"),
 ("top-four.md", "e4de44641a53b0b3424102cd5fbaf3cf5821996d", "research/hm/rankfour-profile11-top-four/PROOF.md", 22067, "56bb8a0aa5ada0f550e0967ef9e535838e9162c2ff2e5ced039a3f6ddb2aacf0", "51d43f891d940ff1dd250747ac450db28057ac54"),
]
CHECKS = []

def require(ok, label):
    if not ok:
        raise RuntimeError("FAIL CLOSED: " + label)
    CHECKS.append(label)

def sha(data):
    return hashlib.sha256(data).hexdigest()

def authenticate():
    require(sha((ROOT / "PROOF.md").read_bytes()) == PROOF_SHA256, "exact reviewed proof bytes")
    manifest = json.loads((ROOT / "INPUTS.json").read_text())
    require(len(manifest) == len(SOURCE_BASELINES) == 7, "complete source set")
    require(len({e["file"] for e in manifest}) == 7, "no duplicate author source")
    by_path = {e["file"]: e for e in manifest}
    for name, commit, path, length, expected_sha, expected_git in SOURCE_BASELINES:
        file = "inputs/" + name
        e = by_path[file]
        url = "https://github.com/Akilleez-QA/read-em-and-weep/blob/" + commit + "/" + path
        expected = dict(file=file, ref=commit, path=path, url=url, bytes=length,
                        sha256=expected_sha, git_blob_sha1=expected_git)
        require(e == expected, name + " full author manifest matches independent baseline")
        data = (ROOT / file).read_bytes()
        require(len(data) == length and sha(data) == expected_sha, name + " exact local bytes")
        git = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        require(git == expected_git, name + " Git blob hash")

# A second arithmetic implementation: exact conjugacy-class character inner
# products over Q(sqrt(5)), not the author's McKay recurrence implementation.
def q(a, b=0):
    return F(a), F(b)

def add(x, y):
    return x[0] + y[0], x[1] + y[1]

def neg(x):
    return -x[0], -x[1]

def mul(x, y):
    return x[0]*y[0] + 5*x[1]*y[1], x[0]*y[1] + x[1]*y[0]

def scale(c, x):
    return c*x[0], c*x[1]

TRACES = [q(2), q(-2), q(0), q(1), q(-1),
          q(F(1,2), F(1,2)), q(F(-1,2), F(-1,2)),
          q(F(-1,2), F(1,2)), q(F(1,2), F(-1,2))]
SIZES = [1, 1, 30, 20, 20, 12, 12, 12, 12]

def sym(n):
    if n < 0:
        return [q(0) for _ in TRACES]
    previous = [q(0) for _ in TRACES]
    current = [q(1) for _ in TRACES]
    for _ in range(n):
        previous, current = current, [add(mul(t,c), neg(p)) for t,c,p in zip(TRACES,current,previous)]
    return current

CHARS = {name: sym(n) for n, name in enumerate(("1", "W", "A", "S4", "D", "T6"))}
CHARS["P"] = [q(x) for x in [4,4,0,1,1,-1,-1,-1,-1]]
# The other A5 three-character is the Galois conjugate of A.
CHARS["V"] = [(x[0], -x[1]) for x in CHARS["A"]]
CHARS["Wp"] = [add(mul(t,p),neg(s)) for t,p,s in zip(TRACES,CHARS["P"],CHARS["T6"])]

def char_sum(*terms):
    return [tuple(map(sum,zip(*row))) for row in zip(*terms)]

def char_product(x,y):
    return [mul(a,b) for a,b in zip(x,y)]

def representation(**multiplicities):
    return char_sum(*[[scale(v,c) for c in CHARS[k]] for k,v in multiplicities.items()])

def inner(x,y):
    total=q(0)
    for s,a,b in zip(SIZES,x,y):
        total=add(total,scale(F(s,120),mul(a,b)))
    return total

def eqchar(actual, expected, label):
    require(actual == expected, label)

def representation_checks():
    require(sum(SIZES) == 120, "binary icosahedral conjugacy-class mass")
    require(sum(c[0][0]**2 for c in CHARS.values()) == 120, "complete irreducible dimension-square mass")
    for r,c in CHARS.items():
        for s,d in CHARS.items():
            require(inner(c,d) == q(int(r==s)), "orthogonality " + r + "/" + s)
    for degree in range(27):
        c=sym(degree)
        require(c[0] == q(degree+1), "universal symmetric dimension " + str(degree))
        multiplicities=[inner(c,d) for d in CHARS.values()]
        require(all(b==0 and a.denominator==1 and a>=0 for a,b in multiplicities),
                "genuine symmetric character " + str(degree))
    eqchar(sym(6), representation(V=1,P=1), "Sym6")
    eqchar(sym(7), representation(Wp=1,T6=1), "Sym7")
    eqchar(sym(8), representation(P=1,D=1), "complete octic coefficient representation")
    eqchar(sym(10), representation(A=1,V=1,D=1), "degree-ten coefficient domain")
    eqchar(sym(16), representation(V=1,P=1,D=2), "degree-eighteen H1 character")
    eqchar(sym(18), representation(A=1,V=1,P=2,D=1), "degree-eighteen coefficient domain")
    a4=char_product(CHARS["A"],sym(4))
    eqchar(a4,representation(A=1,V=1,P=1,D=1), "triplet H0 gate and H1 B0")
    eqchar(char_product(CHARS["A"],sym(5)),representation(Wp=1,S4=1,T6=2), "triplet twist-one section gate")
    m2=representation(A=1,V=2,P=3,D=4)
    endpoint=representation(V=1,P=2,D=3)
    eqchar(char_sum(a4,endpoint),m2,"exact endpoint cohomology difference")
    eqchar(char_sum(sym(8),sym(16)),endpoint,"unique scalar endpoint H1")
    exclusions={2:"1",4:"A",6:"1",8:"A",12:"A",14:"1"}
    for j,bad in exclusions.items():
        count=inner(char_sum(sym(j-2),sym(26-j)),CHARS[bad])
        require(count[1]==0 and count[0]>0,"forbidden constituent at scalar partition " + str(j))
    require(set(exclusions)|{10} == set(range(2,15,2)), "complete seven scalar partitions")
    require((-28 // 2)%2 == 0, "doublet average degree has forbidden even parity")
    require(inner(CHARS["A"],sym(2))==q(1), "unique equivariant U derivative row")
    require(inner(sym(6),CHARS["1"])==q(0), "T cannot differentiate internally to U(-2)")
    require(inner(sym(8),CHARS["1"])==q(0), "T cannot factor through saturated U derivative image")
    require(inner(CHARS["A"],CHARS["1"])==q(0), "saturation equality forbids determinant")
    # For determinant-one orthogonal A, wedge^2 A = A. Verify independently
    # using t(g^2)=t(g)^2-2 and the exterior-square character formula.
    exterior=[]
    for t,a in zip(TRACES,CHARS["A"]):
        t2=add(mul(t,t),q(-2))
        a2=add(mul(t2,t2),q(-1))
        exterior.append(scale(F(1,2),add(mul(a,a),neg(a2))))
    eqchar(exterior,CHARS["A"],"exterior-square determinant obstruction")
    h0estar=char_sum(char_product(CHARS["D"],sym(2)),
                    char_product(CHARS["Wp"],sym(3)),
                    char_product(CHARS["T6"],sym(3)),
                    char_product(CHARS["V"],sym(4)),sym(8))
    hstar=representation(A=2,V=2,P=2,D=2)
    eqchar(h0estar,char_sum(hstar,m2),"original H* from exact dual sequence")
    small=representation(A=2,V=2,P=1,D=1)
    eqchar(hstar,char_sum(small,sym(8)),"C* after genuine constant octic complement")
    eqchar(char_sum(sym(10),sym(18)),char_sum(small,representation(P=1,D=1)),
           "joint coefficient kernel P+D")
    for name in ("A","V"):
        require(inner(sym(10),CHARS[name])==q(1) and inner(sym(18),CHARS[name])==q(1)
                and inner(small,CHARS[name])==q(2), "both independent coefficient copies " + name)
    require(inner(sym(10),CHARS["P"])==q(0) and inner(sym(18),CHARS["P"])==q(2)
            and inner(small,CHARS["P"])==q(1), "only degree-eighteen contributes P")
    require(inner(sym(10),CHARS["D"])==q(1) and inner(sym(18),CHARS["D"])==q(1)
            and inner(small,CHARS["D"])==q(1), "exactly one retained total D")

def degree_checks():
    require(5+2+6+3==16 and -2*5-3*(2+6)-4*3==-46,"E0 rank and degree")
    require(30-(8+1)==21,"minimal-span lower bound")
    # Identity in n,q1, recorded as coefficients (constant,n,q1).
    require((0,-10,-8+10)==(0,-10,2),"coherent capacity -8q1-10(n-q1)")
    require(-10*4+2*3==-34 and -34 < -28,"n>=4 contradicts endpoint degree lower bound")
    require({0,4,5,9}.intersection({8,9})=={9},"semisimple octic quotient dimension")
    require(21-16==5 and 5-3==2,"small annihilator and endpoint ranks")
    require(3*(-6)==-18 and -46-(-18)==-28,"zero-defect B0 and L0 degrees")
    require(-10-18==-28 and (10-1)+(18-1)==26,"scalar endpoint degree and H1 dimension")
    require(-20 < -10,"U to O(-20) Hom vanishes by degree")
    require(-28+12==-16,"rank-two saturation defect bound and equality determinant line")
    require(min(60//d for d in [1,2,3,5])==12,"minimum projective A5 orbit size")
    require(3*(-8)-(-28)==4,"actual saturated derivative cokernel degree")
    require(-28+2*2==-24,"twisted rank-two derivative image degree")
    require(-28-24==-52 and -46-(-52)==6,"actual forward transform and positive quotient degree")
    require(2*(-9)+2*(-17)==-52 and 2+2==4,"universal first-jet rank and degree")
    require((10-1,18-1)==(9,17),"dual principal-parts twists")
    require(-6 < 0,"Hom(O(6),O)=0 degree obstruction")
    require(2*3+2*3+4+5==21 and 11+19-21==4+5,"joint coefficient dimension and kernel")

def main():
    authenticate()
    representation_checks()
    degree_checks()
    result={
        "status":"PASS",
        "proof_sha256":PROOF_SHA256,
        "checks":len(CHECKS),
        "checker_sha256":sha(Path(__file__).read_bytes()),
        "source_files_checked":len(SOURCE_BASELINES),
        "implementation":"independent exact conjugacy-class arithmetic plus degree identities; no author-module imports",
        "geometry":"reviewed in REVIEW-INDEPENDENT.md; not mechanically certified",
        "scope":"full-positive triplet branch only; no existence, whole-branch exclusion, higher-order or algebraicity conclusion",
        "actual_instance_evaluation":False,
        "github_writes":False,
    }
    print(json.dumps(result,sort_keys=True,indent=2))

if __name__ == "__main__":
    main()
