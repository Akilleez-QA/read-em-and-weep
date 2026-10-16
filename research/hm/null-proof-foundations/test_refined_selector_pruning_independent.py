#!/usr/bin/env python3
"""Independent closed-form selector audit; indices only, no physical arithmetic."""
import sys
if not __debug__:raise SystemExit(2)
import copy
import subprocess
import unittest
import prune_refined_selector_paths as p
import compile_refined_detector_metadata as s

class IndependentSelectorAudit(unittest.TestCase):
    def test_all78_against_closed_form_words(self):
        out=p.generate();seeds=s.seed_records()
        self.assertEqual(out['counts'],{'raw':4038,'same_owner_split_identity':3792,'graded_block_zero':96,'terminal_block_mismatch':72,'surviving':78})
        for item in out['paths']:
            seed=seeds[item['seed']];row=s.ROWS[item['row']];q,block=row[0],row[3]
            with self.subTest(seed=item['seed']):
                if q==2:L=(('I',0),);R=(('P',0),);coefficient=seed['coefficient']
                elif q==3 and block=='M10':L=(('H',0),('I',1));R=(('P',1),);coefficient=seed['coefficient']
                elif q==3 and block=='M21':L=(('E',0),('I',1));R=(('P',1),('H',0));coefficient=seed['coefficient']
                elif q==4 and block=='M20':L=(('H',0),('E',1),('I',2));R=(('P',2),('H',1));coefficient=seed['orientation']
                elif q==4 and block=='M31':L=(('E',0),('E',1),('I',2));R=(('P',2),('H',1),('H',0));coefficient=seed['orientation']
                else:self.fail('unexpected terminal block')
                self.assertEqual(item['left'],L);self.assertEqual(item['right'],R)
                self.assertEqual(item['coefficient'],coefficient)
                self.assertEqual(item['tail'],tuple(range(q-2,q+1)))
                self.assertEqual(item['weighted_owners'],tuple(range(q+1)))

    def test_carrier_prefix_not_tail_distinctness(self):
        self.assertFalse(p.prefix_allowed(1,[(1,0,0),(1,1,0),(2,0,0),(3,0,0)]))
        self.assertFalse(p.prefix_allowed(2,[(0,0,0),(1,0,0),(1,1,0),(2,0,0),(3,0,0)]))
        self.assertTrue(p.prefix_allowed(2,[(0,0,0),(1,0,0),(2,0,0),(2,0,1),(2,0,2)]))
        self.assertTrue(p.prefix_allowed(0,[(1,0,0),(1,0,1),(1,0,2)]))
        with self.assertRaises(s.ContractError):p.prefix_allowed(0,[(1,0,0),(1,0,1),(1,0,2)],frame='unconverted')

    def test_word_identities_only_same_owner(self):
        for a,b in [('H','H'),('H','E'),('E','H'),('H','I'),('P','H')]:
            self.assertTrue(p.zero_word(((a,0),(b,0))))
            self.assertFalse(p.zero_word(((a,0),(b,1))))
        self.assertFalse(p.zero_word((('E',0),('E',0))))

    def test_mutation_fails_closed(self):
        for name in ('coefficient','left','weighted_owners','tail'):
            c=p.generate()
            c['paths'][0][name]=99 if name=='coefficient' else ()
            with self.subTest(field=name),self.assertRaises(s.ContractError):p.encode(c)
        for flag in ('execution_release','physical_source_evaluated','old_four_tail_assumed'):
            c=p.generate();c[flag]=True
            with self.subTest(flag=flag),self.assertRaises(s.ContractError):p.encode(c)

    def test_optimized_cli_fails_before_output(self):
        for opt in ('-O','-OO'):
            run=subprocess.run([sys.executable,opt,p.__file__],capture_output=True)
            self.assertEqual(run.returncode,2);self.assertEqual(run.stdout,b'')

if __name__=='__main__':unittest.main(verbosity=2)
