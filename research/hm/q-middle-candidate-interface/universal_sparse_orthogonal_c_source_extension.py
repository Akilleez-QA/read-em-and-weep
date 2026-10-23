"""Sparse additive C-source port for the new orthogonal-leg family.

Imports the frozen sparse tensor API but never calls its supported-middle
source_map on a new T0. Every old error sector, including exact zeros,
is retained. No coefficient filter, solve, rank or specialization occurs.
"""
from universal_unconditional216_source_map import *

class OrthogonalSourceMap(SourceMap):
    def source_map_new(self,D3,G5):
        t=time.time()
        assert len(D3)==3 and len(G5)==6 and len(G5[0])==3
        schemas=json.loads((ROOT/'unconditional216-source-map-cache/joint_error_rows_summary.json').read_text())['error_schemas']
        assert len(schemas)==26
        errors={name:{**schema,'entries':{}} for name,schema in schemas.items()}
        candidates={};checks={};scaled_residual={}
        def em(name,A):errors[name]=pack_matrix(A)
        def ef(name,F):errors[name]=pack_forms(F)
        def cm(name,A):candidates[name]=pack_matrix(A)
        def cf(name,F):candidates[name]=pack_forms(F)
        def scaled(terms):
            out={}
            for powers,F in terms:out[powers]=vadd(out.get(powers,[{},{}]),F)
            return {m:F for m,F in out.items() if not vzero(F)}
        def pack_scaled(record):return {'scale_variables':['kAt','am','bm','cm'],'entries':{m:pack_forms(F) for m,F in record.items()}}
        H=G5
        ycolumns=[]
        Pc=matscale(s.Rational(1,3),matmul(matmul(self.cliff,self.low),H))
        LC=matmul(matmul(self.extract,self.low),H);em('LC',LC)
        assert matzero(matadd(H,matscale(-1,matmul(self.YL,Pc)),matscale(-1,matmul(matmul(self.up,self.Kinc),LC))))
        for j in range(2):
            scaled_residual['U%d'%j]=pack_scaled({})
            cf('raw_B_U%d'%j,[{},{}]);cm('reverse_U%d'%j,zeros(3,1))
        for j in range(3):
            rawC=D3[j]
            assert vzero(vcontract(rawC)) and all((3,4) not in ff for ff in rawC)
            low_output=vcontract(putY(col(G5,j),(3,4)))
            low_literal=vadd(low_output,vscale(-1,self.B(col(Pc,j))))
            ef('low_literal_C%d'%j,low_literal)
            R=vadd(rawC,vscale(-1,self.A(col(Pc,j))));E=getp(R)
            # This is the general ordered full-U/C coupling, not a C5 screen.
            WW=[[ff.get((3,4),{})] for ff in low_literal]
            assert matzero(matadd(matmul(self.cliff,E),matscale(-1,WW)))
            assert matzero(matmul(self.cliff,getp(low_literal)))
            em('high_spin_C%d'%j,matmul(self.cliff,E))
            Ebin=binary_row(matmul(matmul(self.finv,self.extract),E))[0][0]
            sigma=diagonal(Ebin)
            rq=scale(s.Rational(1,6),lap(sigma));sigmah=add(sigma,scale(-1,mul(self.q,rq)))
            assert not lap(sigmah)
            em('sigma_harmonic_C%d'%j,[[sigmah]])
            e0bin=scale(s.Rational(1,120),delta(delta(delta(rq))))
            E0=matmul(matmul(self.Kinc,self.fmat),[[e] for e in binary_coeff(e0bin,3)])
            p1bin=binary_row(matmul(matmul(self.finv,self.extract),matadd(E,matscale(-1,matpoly(self.q,E0)))))[0][0]
            yy,polar=ell_split(p1bin,3);ycol=[[e] for e in binary_coeff(yy,2)];ycolumns.append(ycol)
            R1=vadd(R,self.C(ycol))
            cweight=(1,0,0,1);lcweight=(1,-1,1,1)
            literal=scaled([(cweight,rawC),(lcweight,low_output),(cweight,vscale(-1,self.A(col(Pc,j)))),(lcweight,vscale(-1,self.B(col(Pc,j)))),(cweight,self.C(ycol))])
            expected=scaled([(cweight,R1),(lcweight,low_literal)])
            assert literal==expected
            scaled_residual['C%d'%j]=pack_scaled(literal)
            V0=vcontract(vadd(putp(matscale(s.Rational(1,3),matdiff(E0,3)),(3,)),putp(matscale(s.Rational(1,3),matdiff(E0,4)),(4,))))
            Hhigh=vadd(R1,vscale(-1,vmul(self.q,V0)))
            Lhigh=matscale(s.Rational(1,3),matadd(matdiff(getY(Hhigh,(4,)),3),matscale(-1,matdiff(getY(Hhigh,(3,)),4))))
            Lwedge=[wedge(ff,self.j) for ff in putY(Lhigh,())]
            ef('high_full_remainder_C%d'%j,vadd(Hhigh,vscale(-1,Lwedge)))
            expected=matadd(matmul(matmul(self.spin,self.cliff),E),matmul(matmul(self.Kinc,self.fmat),[[e] for e in binary_coeff(scale(s.Rational(1,120),delta(delta(delta(sigmah)))),3)]))
            assert matzero(matadd(getp(Hhigh),matscale(-1,expected)))
            Lquot=matfun(Lhigh,lambda e:scale(s.Rational(1,10),lap(e)))
            Lharm=matadd(Lhigh,matscale(-1,matpoly(self.q,Lquot)))
            assert all(not lap(e) for e in flat(Lharm))
            for e,eq,eh in zip(flat(Lhigh),flat(Lquot),flat(Lharm)):
                fq,fh=positive_cubic_fischer(public(e),self.variables[:17],*self.variables[:3],self.variables[16])
                assert fq==public(eq) and fh==public(eh)
            em('Lharm_C%d'%j,Lharm)
            Vnorm=vscale(-1,vadd(V0,[wedge(ff,self.j) for ff in putY(Lquot,())]))
            assert vzero(vadd(R1,vmul(self.q,Vnorm),vscale(-1,vadd(Hhigh,vscale(-1,Lwedge))),vscale(-1,[wedge(ff,self.j) for ff in putY(Lharm,())])))
            for name,A in [('Pc',col(Pc,j)),('E0',E0),('y',ycol),('Lhigh',Lhigh),('Lquot',Lquot),('sigma',[[sigma]]),('rq',[[rq]])]:cm(name+'_C%d'%j,A)
            for name,F in [('raw_C',rawC),('R',R),('R1',R1),('V0',V0),('Vnorm',Vnorm),('new_C5',low_output)]:cf(name+'_C%d'%j,F)
        for name,A in [('P',zeros(2,2)),('K0',zeros(6,6)),('K',zeros(6,6)),('Kker',zeros(6,6)),('Qmat',zeros(3,6)),('Paa',zeros(3,3)),('Pc',Pc),('H',H),('y',columns(ycolumns))]:cm(name,A)
        allp=[p for group in (errors,candidates) for item in group.values() for p in item['entries'].values()]
        for pp in allp:
            assert all(all(m[i]>=0 for i in range(13)) for m in pp)
            assert not lapD({m+(0,0):c for m,c in pp.items()})
        zero_sectors=['principal_spin','cartan_error','low_polar','Ylow']+[prefix+'_U%d'%j for prefix in ('K0_Berror','Uerror','Berror') for j in range(2)]
        assert len(zero_sectors)==10 and all(not errors[n]['entries'] for n in zero_sectors)
        assert set(errors)==set(schemas) and all({k:v for k,v in errors[n].items() if k!='entries'}==schemas[n] for n in schemas)
        den={NAMES[i]:max((max(-m[i],0) for pp in allp for m in pp),default=0) for i in range(13,17)}
        checks.update(all26_error_sectors_retained=True,ten_old_U_and_VV_sectors_exact_zero=True,complete_C3_C5_source_scale_identity=True,both_upper_source_companions_retained=True,full_U_C_ordered_coupling_before_vanishing=True,positive_cubic_fischer_all_C=True,literal_high_remainder_reconstruction_all_C=True,whole_external_harmonicity_all_outputs=True,no_isolated_C5_filter=True)
        return dict(schema='orthogonal18-additive-source-map-v1',variables=list(NAMES[:17]),errors=errors,candidates=candidates,scaled_left_residual=scaled_residual,checks=checks,denominator_unit_max_powers=den,elapsed_seconds=time.time()-t,zero_sectors=zero_sectors,source_columns=['U0','U1','C0','C1','C2'],affine_target=False,coordinate_divisions=[],filters=[],source_solve='not run',rank_tests='not run',physical_scales={'middle':'kAt*(am/bm)*sum_ij K_ij L_i L_j_star','leg':'L_i=Y_i-(bm/am)Z_i','C_output':'kAt*cm*(D3+(bm/am)*p(G5))','source':'kAt*[[0,(cm/am)*Pc],[0,-y]]','right_endpoint':'negative determinant dual','divided_arrow':'existing Vnorm convention; no division claimed until every joint error vanishes'},scope='Exact additive new columns only; no source solution or enlarged-family independence asserted.')
