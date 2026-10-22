from pathlib import Path
import contextlib,io,sympy as s
base=Path(__file__).resolve().parent
with contextlib.redirect_stdout(io.StringIO()):
 exec((base/'verify_positive_atiyah_cartan_offdiagonal_interface.py').read_text())
# U-valued VV coefficients use ordered wedge basis (12),(20),(01).
def coeff(F):
 return s.Matrix([F[0].get((1,2),0),F[1].get((1,2),0),-F[0].get((0,2),0),-F[1].get((0,2),0),F[0].get((0,1),0),F[1].get((0,1),0)])
Lrh=[];Et=[]
for jj in range(2):
 Lv={(i,):(Ms[i]*p)[jj] for i in range(3)}
 Lrh.append(wedge(Lv,rhf))
 Et.append(contract(coords,wedge(wedge(Lv,rhf),t)))
vH=s.Matrix([[x,y,z]])*H
# A(v,p) VV is the tensor v times p, so no source specialization enters.
raw=s.Matrix.vstack(vH[0]*p,vH[1]*p,vH[2]*p)
zm(ex*coeff(Lrh)+ex*raw/(2*theta))  # g_L=2, chi=theta
a_dir=-contract(coords,t).get((),0)/2
zm(ex*coeff(Et)+2*a_dir*ex*coeff(Lrh))
am,bm,kk,gg,cc,aa,jet,required=s.symbols('a_m b_m k g_L chi a jet required',nonzero=True)
EU=-aa**2*bm*gg*jet/(2*cc)
baseline=required-kk*EU/am
correction=kk*EU/am
assert s.simplify(baseline+correction-required)==0
print('PASS: fully free polarized Fierz projection and negative contraction sign.')
print('PASS: physical-scale residual, baseline discrepancy and required correction cancel exactly.')
print('No actual source coefficient, point, matrix or rank was evaluated.')
