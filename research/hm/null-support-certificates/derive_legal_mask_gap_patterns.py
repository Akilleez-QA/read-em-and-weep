"""Exact finite-domain check of closed gap formulas, not statistical fitting."""
import json
from pathlib import Path
from collections import Counter
ROOT=Path(__file__).parent

def gap_formula(masks,index):
    m=lambda o,i:(masks[o]>>i)&1
    if index<4:
        return 487-58*(m(0,2)+m(0,3))-57*sum(m(o,i) for o in (1,2) for i in (0,2,3))
    return (273 if index<6 else 272)-57*(m(0,3)+m(1,3))-58*m(2,3)

def build():
    a=json.loads((ROOT/'legal-mask-sector-support.json').read_text());rows=a['active_results']
    ranges=[]
    for j in range(8):
        gaps=[];worst=[]
        for row in rows:
            r=row['multipliers'][j];c=r['certificate'];expected=gap_formula(row['legal_masks'],j)
            if c is None or c['gap']!=expected:raise ValueError('gap formula failure')
            if c['normal']!=([1,0,1,1] if j<4 else [0,-1,0,1]):raise ValueError('normal changed')
            gaps.append(expected)
        minimum=min(gaps)
        worst=[r['legal_masks'] for r,g in zip(rows,gaps) if g==minimum]
        ranges.append({'multiplier_index':j,'min_gap':minimum,'max_gap':max(gaps),'minimizing_tuple_count':len(worst)})
    return {'schema':'legal-mask-gap-patterns-v1','domain_checked':512,'gap_formulas':['edge12:487-58*(m02+m03)-57*(m10+m12+m13+m20+m22+m23)','edge01 firstA/B:273-57*(m03+m13)-58*m23','edge01 secondA/B:272-57*(m03+m13)-58*m23'],'mask_notation':'moi is coordinate i low bit of owner o legal mask','ranges':ranges,'positive_coordinate_derivation':{'line_factor_upper_change':29,'homogenization_upper_change':-58,'legal_clearance_upper_change':87,'net_off_edge_upper_change':58,'edge_inverse_upper_change':-3,'net_on_edge_upper_change':55,'on_edge_degree_change':2,'net_on_edge_gap_change':-57},'negative_coordinate_derivation':{'line_factor_upper_change':-29,'homogenization_upper_change':58,'legal_clearance_upper_change':-29,'net_off_edge_upper_change':0,'note':'Only owner2 can vary coordinate1; that owner is off edge01. There is no negative-coordinate on-edge mask in this sector.'},'zero_support_not_cancellation':True,'physical_evaluation':False,'execution_release':False}
if __name__=='__main__':print(json.dumps(build(),sort_keys=True,indent=2))
