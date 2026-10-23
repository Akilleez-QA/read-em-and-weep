"""Sparse arbitrary-qB full source adapter; no source solve or family columns.

B is arbitrary symmetric12x12, positive-linear, with all remaining Laurent
coefficients free. The physical q is (xy+z²)/theta. Literal derivatives of B
are retained in Euler partners. The immutable q8 restoration, full external
coefficient extension and unrestricted negative-dual pairing are reused as
functions on (D3,G5,N1,ZN), not as a raw8 restriction on B.
"""
import universal_q_middle_C_interface as qreference
from universal_sparse_q_orthogonal_c_source_adapter import *


class QMiddleSourceMap(QOrthogonalSourceMap):
    def __init__(self):
        # Do not construct or generate raw8,55,65 or any family coefficients.
        OrthogonalSourceMap.__init__(self)
        self.reference_rename={getattr(qreference,n):self.ns[n] for n in
                               ('x','y','z','u','w','S','T','FB','FC','FD')}
        self.reference_rename[s.Symbol('mixed_theta',nonzero=True)]=self.ns['theta']
        self.reference_matrix=lambda A:self.lmat(A.xreplace(self.reference_rename))
        self.reference_forms=lambda F:self.lforms([{I:s.expand(p.xreplace(self.reference_rename)) for I,p in f.items()} for f in F])
        const_mixed=[qreference.mixed(s.eye(12)[:6,j],s.eye(12)[6:,j]) for j in range(12)]
        const_vww=[qreference.vww_leg(s.eye(6)[:,j]) for j in range(6)]
        cc=[qreference.C_column(m)[0] for m in qreference.mon(2)]
        # These fixed physical tensors have no external h,k,l dependence.
        self.qm_E=self.reference_matrix(s.Matrix([[qreference.scalar_pairing(g,c) for g in const_mixed] for c in cc]))
        self.qm_RB=self.reference_matrix(s.Matrix([[qreference.scalar_pairing(g,qreference.B(s.eye(2)[:,j])) for j in range(2)] for g in const_mixed]))
        self.qm_ZC=self.reference_matrix(s.Matrix([[qreference.scalar_pairing(g,c) for c in cc] for g in const_vww]))
        self.qm_ZQ=self.homogeneous_partner_qm(matpoly(self.q,eye(12)),2)
        self.qm_RC_Q=matmul(trans(self.qm_ZQ),self.qm_ZC)
        assert all(not m[i] for A in self.physical_operator_matrices() for p in flat(A) for m in p for i in (10,11,12))
        assert all(not m[i] for F in self.As+self.Bs+self.Cs for f in F for p in f.values() for m in p for i in (10,11,12))

    def physical_operator_matrices(self):
        names=('cliff','spin','Kinc','extract','fmat','finv','up','low','J','YL',
               'qm_E','qm_RB','qm_ZC','qm_ZQ','qm_RC_Q')
        return [getattr(self,n) for n in names]

    def homogeneous_partner_qm(self,coefficients,degree):
        """Z_d(C)=stack_i J partial_i(C^t RB)^t/d, all product rules.

        Derivatives are only x,y,z; there are no external direction-variable
        derivatives, evaluations, truncations, or coordinate divisions.
        """
        assert len(coefficients)==12 and degree>0
        assert all(sum(m[:3])==degree for p in flat(coefficients) for m in p)
        row=matmul(trans(coefficients),self.qm_RB)
        return [r for i in range(3) for r in matscale(s.Rational(1,degree),matmul(self.J,trans(matdiff(row,i))))]

    def vww_zero_WW_to_mixed_qm(self,G,degree):
        assert len(G)==6 and len(G[0])==1
        assert all(sum(m[:3])==degree for p in flat(G) for m in p)
        h=zeros(6,1)
        for a in range(2):
            g=[G[2*i+a][0] for i in range(3)]
            assert not add(*(mul(var(i),g[i]) for i in range(3)))
            curl=[add(deriv(g[2],1),scale(-1,deriv(g[1],2))),
                  add(deriv(g[0],2),scale(-1,deriv(g[2],0))),
                  add(deriv(g[1],0),scale(-1,deriv(g[0],1)))]
            for i in range(3):h[2*i+a][0]=scale(-s.Rational(1,degree+1),curl[i])
        converted=matpoly(scale(-1,var(4)),h)+matpoly(var(3),h)
        assert vzero(vadd(self.vww_q(G),vscale(-1,self.mixed_q(converted[:6],converted[6:]))))
        return converted

    def interface_q_middle(self,B):
        assert len(B)==12 and all(len(r)==12 for r in B)
        assert matzero(matadd(B,matscale(-1,trans(B))))
        assert all(sum(m[:3])==1 for p in flat(B) for m in p), 'Positive-linear B required.'
        assert all(not m[3] and not m[4] and not m[17] and not m[18] for p in flat(B) for m in p)
        ZB=self.homogeneous_partner_qm(B,1);ZQ=self.qm_ZQ
        RC_B=matmul(trans(ZB),self.qm_ZC);RC_Q=self.qm_RC_Q
        N1=matmul(B,trans(self.qm_E));ZN=self.homogeneous_partner_qm(N1,2)
        D3mixed=matscale(-s.Rational(1,2),matadd(matmul(B,RC_Q),matpoly(self.q,RC_B)))
        D3vww=matadd(matscale(-s.Rational(1,2),matadd(matmul(ZQ,N1),matpoly(self.q,matmul(ZB,trans(self.qm_E))))),matpoly(self.q,ZN))
        converted=columns([self.vww_zero_WW_to_mixed_qm(col(D3vww,j),3) for j in range(3)])
        D3coeff=matadd(D3mixed,converted)
        G5=matscale(s.Rational(1,2),matadd(matmul(ZB,RC_Q),matmul(ZQ,RC_B)))
        ZNC=matmul(trans(ZN),self.qm_ZC)
        return dict(D3=[self.mixed_q(col(D3coeff,j)[:6],col(D3coeff,j)[6:]) for j in range(3)],
                    G5=G5,quotient_Y=[self.mixed_q(col(N1,j)[:6],col(N1,j)[6:]) for j in range(3)],
                    quotient_Z=ZN,D3coeff=D3coeff,quotient_Y_coeff=N1,D3_mixed_raw=D3mixed,
                    D3_vww_raw=D3vww,ZB=ZB,ZQ=ZQ,RC_B=RC_B,RC_Q=RC_Q,E=self.qm_E,
                    quotient_Z_C=ZNC,C_C_anomaly_factor=matadd(ZNC,matscale(-1,trans(ZNC))))

    def source_map_q_middle(self,B):
        """All26 joint-error candidates with actual qN restored, unconditionally."""
        interface=self.interface_q_middle(B)
        out=QOrthogonalSourceMap.source_map_q_reduced(self,**{k:interface[k] for k in ('D3','G5','quotient_Y','quotient_Z')})
        del out['raw8_coefficient']
        out.update(schema='arbitrary-q-middle234-additive-sparse-source-adapter-v1',
                   q_middle_coefficient=pack_matrix(B),
                   q_middle_interface={k:pack_matrix(v) for k,v in interface.items() if k not in ('D3','quotient_Y')})
        out['checks'].update(all234_raw_coefficients_allowed=True,literal_positive_derivatives_retained=True,
                             physical_operators_external_direction_independent=True,
                             canonical_qN_C_C_anomaly_retained=True)
        out['checks']['whole_external_harmonicity_all_outputs']=all(not lapD(unpack_poly(p)) for p in tensor_polys(out))
        out['physical_scales'].update(middle='kAt*kappa^-1*T_qB; paired degree1(B) and degree2(q0*I) full-U completion',
                                     C_output='kAt*cm*(D3+kappa*p(G5)+q0*(kappa^-1*N1-p(ZN)))',
                                     normalized_actual_divided='Vnorm-kappa^-1*N1+p(ZN)')
        ps=list(tensor_polys(out))
        out['denominator_unit_max_powers']={NAMES[i]:max((max(-m[i],0) for p in ps for m in p),default=0) for i in range(13,17)}
        out['scope']='Exact arbitrary symmetric-positive-linear12x12 qB additive translation. No55/65 family columns, solve, rank, specialization, independence or obstruction value.'
        return out

    def tensor_payload(self,record):
        old=QOrthogonalSourceMap.tensor_payload(self,{**record,'raw8_coefficient':None})
        del old['raw8_coefficient']
        # Fixed E,ZQ,RC_Q are constructor constants, not linear outputs.
        linear={k:v for k,v in record['q_middle_interface'].items() if k not in ('E','ZQ','RC_Q')}
        return {**old,'q_middle_coefficient':record['q_middle_coefficient'],'q_middle_interface':linear}
