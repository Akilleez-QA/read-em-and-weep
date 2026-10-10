import tempfile
from pathlib import Path
import unittest
import inspect_sources as check


class StaticChecks(unittest.TestCase):
    def test_vendored_example(self):
        result = check.inspect_package()
        self.assertFalse(result['lean_kernel_validation_performed'])
        self.assertFalse(result['upstream_source_inspected'])

    def test_nested_comments(self):
        self.assertEqual(check.code_only('a/- x /- sorry -/ y -/b'), 'a' + ' ' * len('/- x /- sorry -/ y -/') + 'b')

    def test_line_comment_and_string(self):
        self.assertNotIn('sorry', check.code_only('"sorry\\\"" -- sorry\n'))

    def test_unterminated_comment(self):
        with self.assertRaises(ValueError): check.code_only('/-')

    def test_unterminated_string(self):
        with self.assertRaises(ValueError): check.code_only('"')

    def test_placeholder_rejected(self):
        for word in ('sorry', 'admit', 'axiom', 'native_decide'):
            with self.subTest(word=word), self.assertRaises(ValueError):
                check.inspect_text('import Mathlib\ntheorem x : True := ' + word, full_target=False)

    def test_comment_word_allowed(self):
        check.inspect_text('import Mathlib\n/- admit -/\n', full_target=False)

    def test_wrong_import_rejected(self):
        with self.assertRaises(ValueError): check.inspect_text('import Foo\n', full_target=False)

    def test_target_guard(self):
        text = 'import Mathlib\n' + check.TARGET + '\ntheorem P5 : ProblemP5 := by\n trivial\n'
        self.assertTrue(check.inspect_text(text, full_target=True)['target_statement_text_checked'])
        for old, new in [('PureOrderIdeal 3', 'PureOrderIdeal 4'), ('typePO P = 2', 'typePO P = 1'), ('theorem P5', 'theorem Q5')]:
            with self.subTest(old=old), self.assertRaises(ValueError):
                check.inspect_text(text.replace(old, new), full_target=True)
        with self.assertRaises(ValueError):
            check.inspect_text(text.replace('theorem P5', '∧ True\ntheorem P5'), full_target=True)

    def test_unpinned_upstream_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'proof.lean'
            path.write_text('import Mathlib\n')
            with self.assertRaises(ValueError): check.inspect_package(upstream=path)


if __name__ == '__main__':
    unittest.main()
