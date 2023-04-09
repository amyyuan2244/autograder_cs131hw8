import unittest
from gradescope_utils.autograder_utils.decorators import weight, visibility, number
from parse import cyk, cnf, parse


class TestComplex(unittest.TestCase):
    def setUp(self):
        self.cnf = cnf()

    @weight(2)
    @visibility('after_due_date')
    @number("2.1")
    def test_eval_parens(self):
        """cyk(R1, "S", "01", {})"""
        val = self.cnf.eval("cyk(R1, "S", "01", {})")
        self.assertEqual(val, "(True, (’S’, (’A’, ’0’), (’B’, ’1’)))")

    @weight(2)
    @visibility('after_due_date')
    @number("2.2")
    def test_eval_precedence(self):
        """cyk(R1, "S", "0011", {})"""
        val = self.calc.eval("cyk(R1, "S", "0011", {})")
        self.assertEqual(val, "(True, (’S’, (’C’, (’A’, ’0’), (’S’, (’A’, ’0’), (’B’, ’1’))), (’B’, ’1’)))")

 
