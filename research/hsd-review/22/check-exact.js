"use strict";

/**
 * Independent exact checker for the numerical inputs in
 * research/carriers/rank-two-ext-bound.md at
 * 9be62063a9b922f9d31042403dd70bf57f9f40e3.
 *
 * Dependency-free. Rational arithmetic is BigInt. This file does not read,
 * import, or execute any other repository code.
 *
 * Two separate derivations are required to agree:
 *   Newton–Girard power sums from Chern classes, and
 *   the splitting principle (truncated exponential of Chern roots).
 * The principal-polarization identities are expanded in the exterior algebra
 * on a symplectic integral basis, not taken from the note's displayed counts.
 */

function gcd(a, b) {
  a = a < 0n ? -a : a;
  b = b < 0n ? -b : b;
  while (b !== 0n) {
    const t = a % b;
    a = b;
    b = t;
  }
  return a;
}

function rat(n, d = 1n) {
  if (d === 0n) throw new Error("zero denominator");
  if (d < 0n) {
    n = -n;
    d = -d;
  }
  const g = gcd(n, d);
  return { n: n / g, d: d / g };
}

function radd(a, b) {
  return rat(a.n * b.d + b.n * a.d, a.d * b.d);
}
function rsub(a, b) {
  return rat(a.n * b.d - b.n * a.d, a.d * b.d);
}
function rmul(a, b) {
  return rat(a.n * b.n, a.d * b.d);
}
function rdiv(a, b) {
  return rat(a.n * b.d, a.d * b.n);
}
function req(a, b) {
  return a.n === b.n && a.d === b.d;
}
function rstr(a) {
  return a.d === 1n ? a.n.toString() : `${a.n}/${a.d}`;
}
function rint(a) {
  if (a.d !== 1n) throw new Error(`not an integer: ${rstr(a)}`);
  return a.n;
}

const Z = (n) => rat(BigInt(n), 1n);
const ZERO = Z(0);
const ONE = Z(1);

function assert(cond, msg) {
  if (!cond) throw new Error(msg);
}

// Polynomials in u, where u stands for the codimension-2 class c2.
// Coefficient arrays are low degree first. Codimension of u^k is 2k,
// so degree 2 is the top class on a fourfold.

function polyTrim(p) {
  const q = p.slice();
  while (q.length > 1 && req(q[q.length - 1], ZERO)) q.pop();
  return q;
}
function polyAdd(a, b) {
  const n = Math.max(a.length, b.length);
  const o = [];
  for (let i = 0; i < n; i++) o.push(radd(a[i] || ZERO, b[i] || ZERO));
  return polyTrim(o);
}
function polyMul(a, b) {
  const o = Array.from({ length: a.length + b.length - 1 }, () => ZERO);
  for (let i = 0; i < a.length; i++) {
    for (let j = 0; j < b.length; j++) o[i + j] = radd(o[i + j], rmul(a[i], b[j]));
  }
  return polyTrim(o);
}
function polyScale(a, s) {
  return polyTrim(a.map((c) => rmul(c, s)));
}
function polyEq(a, b) {
  const n = Math.max(a.length, b.length);
  for (let i = 0; i < n; i++) if (!req(a[i] || ZERO, b[i] || ZERO)) return false;
  return true;
}
function polyStr(p) {
  return p.map(rstr).join(" + ") + "·u^k";
}

// --- Newton–Girard ---
// k c_k = sum_{i=1}^k (-1)^{i-1} e_{k-i} p_i, with e_0 = 1 and e_j = c_j.
// Rank two, c1 = 0, c3 = c4 = 0, c2 = u. Power sums are returned as
// polynomials in u. Chern character ch_k = p_k / k!.

function factorial(k) {
  let f = 1n;
  for (let i = 2; i <= k; i++) f *= BigInt(i);
  return f;
}

function newtonRankTwo() {
  // e[k] is c_k as a polynomial in u=c2. Only k<=4 is needed.
  const e = [
    [ONE],
    [ZERO], // c1
    [ZERO, ONE], // c2 = u
    [ZERO], // c3
    [ZERO], // c4
  ];
  const p = [null];
  for (let k = 1; k <= 4; k++) {
    // p_k = (-1)^{k-1} * ( k c_k - sum_{i=1}^{k-1} (-1)^{i-1} e_{k-i} p_i )
    // Rearranged from k e_k = sum_{i=1}^k (-1)^{i-1} e_{k-i} p_i
    // so (-1)^{k-1} p_k = k e_k - sum_{i=1}^{k-1} (-1)^{i-1} e_{k-i} p_i
    let right = polyScale(e[k], Z(k));
    for (let i = 1; i < k; i++) {
      const term = polyMul(e[k - i], p[i]);
      if (i % 2 === 1) right = polyAdd(right, polyScale(term, Z(-1)));
      else right = polyAdd(right, term);
    }
    // right = (-1)^{k-1} p_k
    const sign = k % 2 === 1 ? ONE : Z(-1);
    p[k] = polyScale(right, sign);
  }
  const ch = p.map((pk, k) => (k === 0 ? [ONE] : polyScale(pk, rat(1n, factorial(k)))));
  return { p, ch };
}

// --- Splitting principle ---
// Chern roots r, -r with r^2 = -c2 = -u, so r^{2m} = (-u)^m and odd powers cancel.
// ch = exp(r)+exp(-r) = 2 sum_{m>=0} r^{2m} / (2m)!.

function splittingRankTwo() {
  // ch = 2 sum_{m>=0} r^{2m}/(2m)! with r^{2m} = (-1)^m u^m.
  // Index m is the coefficient of u^m, which is the codimension-2m component.
  const parts = [Z(2)];
  for (let m = 1; m <= 2; m++) {
    const sign = m % 2 === 0 ? 1n : -1n;
    parts.push(rat(2n * sign, factorial(2 * m)));
  }
  return parts;
}

function splittingEnd() {
  // Eigenvalues of End(E) are the differences of {r,-r} with itself:
  // 0, 0, 2r, -2r. Thus ch = 2 + 2 sum_{m>=0} (2r)^{2m}/(2m)!,
  // and (2r)^{2m} = 2^{2m} (-u)^m.
  const out = [];
  for (let m = 0; m <= 2; m++) {
    const sign = m % 2 === 0 ? 1n : -1n;
    const pow2 = 1n << BigInt(2 * m);
    const coeff = m === 0 ? Z(4) : rat(2n * pow2 * sign, factorial(2 * m));
    out.push(coeff);
  }
  return out;
}

// --- Exterior algebra on 8 generators ---
// Basis order: x0,x1,x2,x3,y0,y1,y2,y3 as bits 0..7.
// A form is a Map from bitmask to Rational.

function popcount(mask) {
  let c = 0;
  let m = mask;
  while (m) {
    c += m & 1;
    m >>= 1;
  }
  return c;
}

function emptyForm() {
  return new Map();
}

function addTerm(form, mask, coeff) {
  if (req(coeff, ZERO)) return;
  const prev = form.get(mask) || ZERO;
  const next = radd(prev, coeff);
  if (req(next, ZERO)) form.delete(mask);
  else form.set(mask, next);
}

function bit(i) {
  return 1 << i;
}

function wedgeAtoms(i, j) {
  // e_i ∧ e_j as a canonical form
  const form = emptyForm();
  if (i === j) return form;
  if (i < j) addTerm(form, bit(i) | bit(j), ONE);
  else addTerm(form, bit(i) | bit(j), Z(-1));
  return form;
}

function shuffleSign(a, b) {
  // Sign of concatenating increasing(a) with increasing(b): inversions are
  // pairs (bit in a, bit in b) with the a-bit larger.
  let negative = false;
  for (let i = 0; i < 8; i++) {
    if ((b & bit(i)) === 0) continue;
    if (popcount(a >>> (i + 1)) % 2 === 1) negative = !negative;
  }
  return negative ? -1n : 1n;
}

function wedge(a, b) {
  const out = emptyForm();
  for (const [ma, ca] of a) {
    for (const [mb, cb] of b) {
      if (ma & mb) continue;
      const sign = shuffleSign(ma, mb);
      addTerm(out, ma | mb, rmul(rmul(ca, cb), rat(sign, 1n)));
    }
  }
  return out;
}

function scaleForm(form, s) {
  const out = emptyForm();
  for (const [m, c] of form) addTerm(out, m, rmul(c, s));
  return out;
}

function addForm(a, b) {
  const out = emptyForm();
  for (const [m, c] of a) addTerm(out, m, c);
  for (const [m, c] of b) addTerm(out, m, c);
  return out;
}

function subForm(a, b) {
  return addForm(a, scaleForm(b, Z(-1)));
}

function formEq(a, b) {
  if (a.size !== b.size) return false;
  for (const [m, c] of a) {
    if (!b.has(m) || !req(b.get(m), c)) return false;
  }
  return true;
}

function contract(form, k) {
  // Interior product by the dual basis vector of generator k.
  const out = emptyForm();
  const bk = bit(k);
  for (const [mask, coeff] of form) {
    if ((mask & bk) === 0) continue;
    const sign = popcount(mask & (bk - 1)) % 2 === 0 ? 1n : -1n;
    addTerm(out, mask ^ bk, rmul(coeff, rat(sign, 1n)));
  }
  return out;
}

function alpha(i) {
  // x_i ∧ y_i
  return wedgeAtoms(i, 4 + i);
}

function principalPolarization() {
  let theta = emptyForm();
  for (let i = 0; i < 4; i++) theta = addForm(theta, alpha(i));
  const theta2 = wedge(theta, theta);
  const halfTheta2 = scaleForm(theta2, rat(1n, 2n));
  let sumPairs = emptyForm();
  for (let i = 0; i < 4; i++) {
    for (let j = i + 1; j < 4; j++) sumPairs = addForm(sumPairs, wedge(alpha(i), alpha(j)));
  }
  let omega = alpha(0);
  omega = wedge(omega, alpha(1));
  omega = wedge(omega, alpha(2));
  omega = wedge(omega, alpha(3));
  const theta4 = wedge(theta2, theta2);
  return { theta, theta2, halfTheta2, sumPairs, omega, theta4 };
}

function binom(n, k) {
  if (k < 0 || k > n) return 0n;
  let c = 1n;
  for (let i = 1; i <= k; i++) {
    c = (c * BigInt(n - k + i)) / BigInt(i);
  }
  return c;
}

function hodge(p, q) {
  return binom(4, p) * binom(4, q);
}

function main() {
  const report = {};

  // Unit anchor for the shuffle: (x0∧y0)∧(x1∧y1) sorts to x0∧x1∧y0∧y1 with sign -1.
  const anchor = wedge(alpha(0), alpha(1));
  const anchorMask = bit(0) | bit(1) | bit(4) | bit(5);
  assert(anchor.size === 1 && anchor.has(anchorMask), "anchor mask");
  assert(req(anchor.get(anchorMask), Z(-1)), "anchor sign is -1");

  const newt = newtonRankTwo();
  const split = splittingRankTwo();
  // ch graded by codimension, stored per power of u: index m ↔ codimension 2m.
  // Newton ch[k] is the codimension-k component as a polynomial in u.
  // For k=0,2,4 those polynomials are pure of u-degree k/2.
  // ch0 is the rank. Newton–Girard determines the positive-degree components.
  const chNewton = [
    Z(2),
    newt.ch[2][1], // coefficient of u in ch2
    newt.ch[4][2], // coefficient of u^2 in ch4
  ];
  assert(req(newt.p[1][0], ZERO), "p1 = c1 = 0");
  assert(req(chNewton[1], Z(-1)), "newton ch2 = -c2");
  assert(req(chNewton[2], rat(1n, 12n)), "newton ch4 = c2^2/12");
  assert(req(split[0], Z(2)) && req(split[1], Z(-1)) && req(split[2], rat(1n, 12n)), "splitting ch");
  assert(req(chNewton[0], split[0]) && req(chNewton[1], split[1]) && req(chNewton[2], split[2]), "ch paths agree");
  // Odd components vanish.
  assert(newt.ch[1].every((c) => req(c, ZERO)) && newt.ch[3].every((c) => req(c, ZERO)), "odd ch vanishes");

  const chE = [Z(2), Z(-1), rat(1n, 12n)];
  const chEndFull = polyMul(chE, chE);
  // On a fourfold, components past codimension 4 (u-degree > 2) are zero.
  const chEndFromProduct = chEndFull.slice(0, 3);
  const chEndSplit = splittingEnd();
  const chEndExpected = [Z(4), Z(-4), rat(4n, 3n)];
  assert(polyEq(chEndFromProduct, chEndExpected), `product ch(End)=${polyStr(chEndFromProduct)}`);
  assert(req(chEndFull[3], rat(-1n, 6n)) && req(chEndFull[4], rat(1n, 144n)), "higher components identified before truncation");
  assert(chEndSplit.length === 3, "end length");
  for (let i = 0; i < 3; i++) assert(req(chEndSplit[i], chEndExpected[i]), `end split ${i}: ${rstr(chEndSplit[i])}`);

  // χ(E) = ∫ c2^2 / 12, so ∫ c2^2 = 12 χ.
  // χ(End) = ∫ (4/3) c2^2 = (4/3)*12 χ = 16 χ.
  const sixteen = rmul(rat(4n, 3n), Z(12));
  assert(req(sixteen, Z(16)), "16 chi factor");

  // Euler characteristic of End: ext2 = 16χ - 2 + 2 ext1, using ext0=ext4=1, ext3=ext1.
  function ext2From(chi, ext1) {
    return 16n * chi - 2n + 2n * ext1;
  }
  const corner = ext2From(2n, 8n);
  assert(corner === 46n, `corner ${corner}`);
  // Same corner from the Euler relation written as ext2 = χ(End) + 2 ext1 - 2.
  assert(16n * 2n + 2n * 8n - 2n === 46n, "euler rearrangement");
  // Picard-only predecessor, ext1>=4: 32 - 2 + 8 = 38.
  assert(ext2From(2n, 4n) === 38n, "superseded 38");

  // Odd-dimensional alternating forms are degenerate over ℚ.
  // det(A) = det(A^T) = det(-A) = (-1)^n det(A). For n odd, det(A) = -det(A).
  // Concrete 3×3 skew integer matrix, determinant by cofactor expansion.
  function det3(m) {
    return (
      m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) -
      m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0]) +
      m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
    );
  }
  const skew3 = [
    [0n, 1n, 2n],
    [-1n, 0n, 3n],
    [-2n, -3n, 0n],
  ];
  assert(det3(skew3) === 0n, "odd skew determinant");
  // Standard symplectic 2×2 block [[0,1],[-1,0]] has det 1, so even dimension can be perfect.
  assert(0n * 0n - 1n * -1n === 1n, "even symplectic det");

  // Hodge numbers of an abelian fourfold and the two comparison spaces.
  const h02 = hodge(0, 2);
  const h13 = hodge(1, 3);
  const h24 = hodge(2, 4);
  assert(h02 === 6n && h13 === 16n && h24 === 6n, "hodge summands");
  const semi = h02 + h13 + h24;
  assert(semi === 28n, "semiregularity dimension");
  // HKR: ⊕_{p+q=2} H^q(∧^p T). T trivial of rank 4, so dim = C(4,p) * C(4,q).
  const hh =
    binom(4, 0) * binom(4, 2) + // p=0,q=2
    binom(4, 1) * binom(4, 1) + // p=1,q=1
    binom(4, 2) * binom(4, 0); // p=2,q=0
  assert(hh === 28n, `HH2 ${hh}`);
  assert(binom(4, 0) * binom(4, 2) === 6n, "H2(O)");
  assert(binom(4, 1) * binom(4, 1) === 16n, "H1(T)");
  assert(binom(4, 2) * binom(4, 0) === 6n, "H0(wedge2 T)");
  assert(46n > semi, "46 exceeds 28");

  // Principal polarization.
  const pol = principalPolarization();
  assert(formEq(pol.halfTheta2, pol.sumPairs), "theta^2/2 equals the six-term sum");
  assert(pol.sumPairs.size === 6, `six monomials, got ${pol.sumPairs.size}`);
  let gcdCoeff = 0n;
  for (const [, c] of pol.sumPairs) {
    assert(c.d === 1n, "integral coefficients");
    assert(c.n === 1n || c.n === -1n, `coeff ±1, got ${rstr(c)}`);
    gcdCoeff = gcd(gcdCoeff, c.n);
  }
  assert(gcdCoeff === 1n, "primitive");
  // The unsorted written monomials are exactly the sum, so each written
  // coefficient is +1. Anchor one sorted coefficient: mask of x0∧x1∧y0∧y1 is -1.
  assert(req(pol.halfTheta2.get(anchorMask), Z(-1)), "sorted coefficient -1");
  assert(formEq(pol.theta4, scaleForm(pol.omega, Z(24))), "theta^4 = 24 Ω");
  assert(pol.omega.size === 1, "omega is a single monomial");

  // k=2d integral and χ=k^2/2 integral forces k even, hence d integral.
  function kSquaredOver2IsInteger(k) {
    return (k * k) % 2n === 0n;
  }
  for (let k = -31n; k <= 31n; k++) {
    const even = k % 2n === 0n;
    assert(kSquaredOver2IsInteger(k) === even, `parity of k=${k}`);
    if (even) assert((k * k) / 2n === (k / 2n) * (k / 2n) * 2n, "k^2/2 = 2 d^2");
  }
  // Integrality of k from primitivity: if (a/b) ξ is an integral class and
  // gcd(a,b)=1, then b divides every coefficient of ξ, hence b|gcd=1.
  function lowestTermsMultiplierIsIntegral(a, b) {
    let g = gcd(a, b);
    a /= g;
    b /= g;
    if (b < 0n) b = -b;
    // b must divide gcd of the coefficients, which is 1.
    return b === 1n;
  }
  assert(lowestTermsMultiplierIsIntegral(2n, 2n) === true, "2/2");
  assert(lowestTermsMultiplierIsIntegral(1n, 2n) === false, "1/2 not integral");
  assert(lowestTermsMultiplierIsIntegral(3n, 2n) === false, "3/2 not integral");
  assert(lowestTermsMultiplierIsIntegral(15n, 1n) === true, "15");
  assert(lowestTermsMultiplierIsIntegral(-8n, 1n) === true, "-8");
  assert(lowestTermsMultiplierIsIntegral(30n, 2n) === true, "30/2 reduces");

  function chiFromD(d) {
    return 2n * d * d;
  }
  function ext2Lower(d) {
    return 32n * d * d + 14n;
  }
  assert(chiFromD(15n) === 450n, "HM chi");
  assert(chiFromD(8n) === 128n, "Lange chi");
  assert(16n * 450n === 7200n, "HM chi(End)");
  assert(16n * 128n === 2048n, "Lange chi(End)");
  assert(32n * 225n === 7200n, "32 d^2 at d=15");
  const ext2hm = 32n * 225n - 2n + 2n * 87n;
  assert(ext2hm === 7372n, `7372 got ${ext2hm}`);
  assert(ext2From(450n, 87n) === 7372n, "7372 via 16 chi");
  assert(ext2Lower(8n) === 2062n, `2062 got ${ext2Lower(8n)}`);
  assert(ext2From(128n, 8n) === 2062n, "2062 via euler at ext1=8");
  assert(450n / 2n === 225n && 128n / 2n === 64n, "halves");
  // g | χ/2 because χ(E)=g χ(G) and χ(G)=2t.
  function descentQuotient(chiE, g, t) {
    const chiG = 2n * t;
    assert(g * chiG === chiE, "degree scaling");
    const half = chiE / 2n;
    assert(chiE % 2n === 0n, "chi even");
    assert(half % g === 0n, "g divides chi/2");
    assert(half / g === t, "quotient is chi(G)/2");
    return half / g;
  }
  assert(descentQuotient(450n, 225n, 1n) === 1n, "maximal HM degree");
  assert(descentQuotient(450n, 15n, 15n) === 15n, "g=15");
  assert(descentQuotient(450n, 9n, 25n) === 25n, "g=9");
  assert(descentQuotient(128n, 64n, 1n) === 1n, "maximal Lange degree");
  assert(descentQuotient(128n, 8n, 8n) === 8n, "g=8");
  assert(225n % 7n !== 0n, "7 does not divide 225");
  assert(64n % 3n !== 0n, "3 does not divide 64");

  function positiveDivisors(n) {
    const small = [];
    const large = [];
    for (let i = 1n; i * i <= n; i++) {
      if (n % i === 0n) {
        small.push(i);
        if (i * i !== n) large.push(n / i);
      }
    }
    return small.concat(large.reverse());
  }
  const div225 = positiveDivisors(225n);
  const div64 = positiveDivisors(64n);
  assert(div225.join(",") === "1,3,5,9,15,25,45,75,225", div225.join(","));
  assert(div64.join(",") === "1,2,4,8,16,32,64", div64.join(","));

  // Holomorphic contraction on the complex volume form.
  // Generators z0,z1,z2,z3,zb0,zb1,zb2,zb3.
  const volMask = (1 << 8) - 1;
  const vol = emptyForm();
  addTerm(vol, volMask, ONE);
  const images = [];
  for (let k = 0; k < 4; k++) {
    const img = contract(vol, k);
    assert(img.size === 1, "one term");
    const mask = volMask ^ bit(k);
    assert(img.has(mask), "expected mask");
    const sign = popcount(volMask & (bit(k) - 1)) % 2 === 0 ? 1n : -1n;
    assert(req(img.get(mask), rat(sign, 1n)), "contraction sign");
    images.push(img);
  }
  // The four image masks are distinct, so the images are linearly independent.
  const masks = images.map((img) => [...img.keys()][0]);
  assert(new Set(masks).size === 4, "independent contractions");
  // A general vector Σ a_k ∂_k kills vol iff every a_k is 0.
  function contractVector(coeffs) {
    let out = emptyForm();
    for (let k = 0; k < 4; k++) out = addForm(out, scaleForm(images[k], coeffs[k]));
    return out;
  }
  assert(contractVector([ONE, ZERO, ZERO, ZERO]).size === 1, "e0");
  assert(contractVector([Z(3), Z(-2), Z(5), Z(7)]).size === 4, "generic nonzero");
  assert(contractVector([ZERO, ZERO, ZERO, ZERO]).size === 0, "zero vector");

  // Leibniz on a degree-4 class with nonzero square. The two summands are
  // complementary, so α∧α is a nonzero multiple of the volume form.
  const mA = wedge(wedgeAtoms(0, 1), wedgeAtoms(4, 5));
  const mB = wedge(wedgeAtoms(2, 3), wedgeAtoms(6, 7));
  const sample = addForm(mA, mB);
  const square = wedge(sample, sample);
  assert(square.size === 1, "sample square is a volume monomial");
  const v0 = 0;
  const left = contract(square, v0);
  const right = scaleForm(wedge(contract(sample, v0), sample), Z(2));
  assert(contract(sample, v0).size > 0, "sample is not killed by ∂0");
  assert(left.size > 0, "contraction of the square is nonzero");
  assert(formEq(left, right), "Leibniz on an even class");
  // A class missing z0 is killed by ∂0, and then so is its square.
  const missed = addForm(
    wedge(wedgeAtoms(1, 2), wedgeAtoms(5, 6)),
    wedge(wedgeAtoms(1, 3), wedgeAtoms(4, 7))
  );
  assert(contract(missed, v0).size === 0, "∂0 kills a class with no z0");
  assert(contract(wedge(missed, missed), v0).size === 0, "hence kills the square");

  // Top class multiple: c≠0 implies ι_v(c·vol)=0 iff v=0, already from independence.
  const multiple = scaleForm(vol, Z(12));
  assert(contract(multiple, 0).size === 1, "nonzero multiple still contracts");

  report.pin = "9be62063a9b922f9d31042403dd70bf57f9f40e3";
  report.chE = ["2", "-c2", "c2^2/12"];
  report.chEnd = ["4", "-4 c2", "(4/3) c2^2"];
  report.chiEndFactor = "16";
  report.ext2Corner = "46";
  report.ext2PicardOnly = "38";
  report.comparisonDimension = "28";
  report.theta4 = "24";
  const sortedCoeffs = [...pol.halfTheta2.entries()]
    .sort((a, b) => a[0] - b[0])
    .map(([mask, c]) => ({ mask, coeff: rstr(c) }));
  report.halfTheta2 = {
    terms: String(pol.sumPairs.size),
    gcd: gcdCoeff.toString(),
    equalsUnsortedSum: true,
    sortedCoefficients: sortedCoeffs,
  };
  report.hm = { d: "15", chi: "450", ext1: "87", ext2: "7372", halfChi: "225" };
  report.lange = { d: "8", chi: "128", ext2Lower: "2062", halfChi: "64", chiEnd: "2048" };
  report.divisors = { 225: div225.map(String), 64: div64.map(String) };
  report.volumeContractionRank = 4;
  report.result = "agreement";

  process.stdout.write(`${JSON.stringify(report, null, 2)}\n`);
}

main();
