import unittest
from spacemenu.branch import Branch

class TestBranch(unittest.TestCase):
    def test_content_nrows_calculates_rows_by_maxcolumns(self):
        options = {
            'column_spacing': 1,
            'row_spacing': 1,
            'max_columns': 2
        }
        b1r1c = Branch('b1r1c', [],[
            {'name': 'l1'},
            {'name': 'l2'}
        ]).get_content(options)
        b1r2c = Branch('b1r2c', [],[
            {'name': 'l1'},
            {'name': 'l2'}
        ]).get_content(options)
        b2r1c = Branch('b2r2c', [],[
            {'name': 'l1'},
            {'name': 'l2'},
            {'name': 'l3'}
        ]).get_content(options)
        b2r2c = Branch('b2r2c', [],[
            {'name': 'l1'},
            {'name': 'l2'},
            {'name': 'l3'},
            {'name': 'l4'}
        ]).get_content(options)
        b3r1c = Branch('b2r2c', [],[
            {'name': 'l1'},
            {'name': 'l2'},
            {'name': 'l3'},
            {'name': 'l4'},
            {'name': 'l5'}
        ]).get_content(options)

        self.assertEqual(b1r1c[0],1)
        self.assertEqual(b1r2c[0],1)
        self.assertEqual(b2r1c[0],2)
        self.assertEqual(b2r2c[0],2)
        self.assertEqual(b3r1c[0],3)
