#!/usr/bin/env python3
"""Sparse F_101 independence certificate for CONSTANT P4 matrices only.

A modular nonzero minor proves a rational lower bound. Rational boundary
upper ranks 240/848 are separately pinned premises, not specialization claims.
No physical source, source-polynomial DAG or full finite oracle is used.
"""
import hashlib
import json
from pathlib import Path
import subprocess
import sys

PRIME=101
UPDATE_CAP=20_000_000
OUTPUT_CAP=2_000_000
HERE=Path(__file__).resolve().parent
updates=0

def need(ok,message):
    if not ok: raise ValueError(message)

def digest(value):
    return hashlib.sha256(json.dumps(value,separators=(',',':'),sort_keys=True).encode()).hexdigest()

class Space:
    def __init__(self,n): self.n=n;self.pivots={};self.pivot_log=[]
    def add(self,entries,label):
        global updates
        v={int(i):int(x)%PRIME for i,x in entries if x%PRIME}
        need(len(v)==len([1 for _,x in entries if x%PRIME]),'duplicate column row')
        need(all(0<=i<self.n for i in v),'row bounds')
        while v:
            row=min(v)
            if row not in self.pivots:
                pivot=v[row]; inv=pow(pivot,-1,PRIME)
                v={i:x*inv%PRIME for i,x in v.items()}
                self.pivots[row]=v
                self.pivot_log.append({'label':label,'row':row,'pre_normalization_pivot':pivot})
                return True
            factor=v[row]
            for i,x in self.pivots[row].items():
                updates+=1
                need(updates<=UPDATE_CAP,'coefficient-update cap')
                z=(v.get(i,0)-factor*x)%PRIME
                if z:v[i]=z
                elif i in v:del v[i]
        return False


def image(matrix,vector):
    result={}
    for col,a in vector:
        for row,b in matrix['data'][col]:result[row]=result.get(row,0)+a*b
    return sorted((i,x)for i,x in result.items()if x)


def main():
    extracted=subprocess.run(['node','--max-old-space-size=64',str(HERE/'extract_constants.js')],check=True,capture_output=True,timeout=10)
    need(len(extracted.stdout)<500000,'constant output cap')
    source=json.loads(extracted.stdout)
    matrices=source['matrices'];bases=source['bases'];gamma=source['gamma']
    expected={'E':(50,80),'B1':(400,245),'C1':(150,400),'B0':(1200,1225),'C0':(350,1200)}
    for name,(rows,cols)in expected.items():
        m=matrices[name];need((m['rows'],m['columns'],len(m['data']))==(rows,cols,cols),'matrix dimensions')
    I20=[(i,0)for i in range(5,11)]+[(i,1)for i in range(15)if i!=5]
    c=[]
    for i,b in I20:
        # c=-K_(15*b+i): M13[target b,source i]=-1;
        # M02[target 5*b+k,source a]=-gamma[i,a,k].
        entries={50+15*b+i:-1}
        for a in range(5):
            for k in range(5):
                z=-gamma[i][a][k]
                if z:entries[5*(5*b+k)+a]=z
        column=sorted(entries.items())
        need(not image(matrices['E'],column),'constant scalar-dual not a cycle')
        c.append(column)
    selection={}
    for key,degree,target,number,boundary_rank in [('minus1',1,10,100,240),('zero',2,2,300,848)]:
        suffix='1'if degree==1 else'0';B=matrices['B'+suffix];C=matrices['C'+suffix]
        need(all(not image(C,col)for col in B['data']),'ordinary differential square')
        lookup={tuple(k):j for j,k in enumerate(bases[key])}
        need(len(lookup)==B['rows'],'basis uniqueness')
        monomials=[(k,)for k in range(5)]if degree==1 else[(k,l)for k in range(5)for l in range(k,5)]
        space=Space(B['rows'])
        for j,col in enumerate(B['data']):space.add(col,{'boundary_column':j})
        need(len(space.pivots)==boundary_rank,'boundary rank differs from pinned value')
        picks=[];candidate_checks=0
        for (i,b),constant in zip(I20,c):
            for monomial in monomials:
                entries={}
                for idx,z in constant:
                    base=list(bases['minus2'][idx])
                    for k in monomial:base[4+k]+=1
                    j=lookup[tuple(base)];entries[j]=entries.get(j,0)+z
                column=sorted((j,z)for j,z in entries.items()if z)
                need(not image(C,column),'multiplication candidate not a cycle')
                candidate_checks+=1
                label={'i':i,'b':b,'base_monomial':list(monomial)}
                if len(picks)<target and space.add(column,{'candidate':label}):
                    picks.append(label)
        need(candidate_checks==number,'candidate coverage')
        need(len(picks)==target and len(space.pivots)==boundary_rank+target,'incomplete selection')
        selection[key]={'labels':picks,'candidate_cycles_checked':candidate_checks,'boundary_rank_mod101':boundary_rank,'augmented_rank_mod101':len(space.pivots),'matrix_digest':digest(B),'outgoing_digest':digest(C),'pivot_log':space.pivot_log}
    cert={'version':1,'status':'selected_output_labels_only','field_lower_bound':'F_101','rational_conclusion':'32 independent dual classes conditional on pinned rational boundary ranks and established P4/Serre source identifications','source':source['source'],'rational_boundary_upper_receipt':source['rank_receipt'],'candidate_order':'I20 as listed, then k=0..4 or (k,l) with k ascending and l=k..4','I20':I20,'supertrace_orientation':'c_(i,b)=-K_(15*b+i)','twist_minus2_cycle_checks':20,'d5_regenerated':False,'d5_relations_premise':{'commit':'e6e8d272e760a432dbbc1053b88c8eae03a47304','path':'research/hsd/twist-minus2-d5/NOTE.md','blob':'0a1d5d00a85e13bcf535a2001577eb0eafc77f43'},'selected':selection,'coefficient_updates':updates,'physical_source_evaluated':False,'obstruction':'undecided'}
    encoded=json.dumps(cert,indent=2,sort_keys=True)+'\n';need(len(encoded.encode())<=OUTPUT_CAP,'certificate output cap')
    sys.stdout.write(encoded)

if __name__=='__main__':main()
