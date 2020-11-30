"""
This type stub file was generated by pyright.
"""

import numpy as np

mat = np.array
_default_table_fmt = dict(empty_cell='', colsep='  ', row_pre='', row_post='', table_dec_above='=', table_dec_below='=', header_dec_below='-', header_fmt='%s', stub_fmt='%s', title_align='c', header_align='r', data_aligns='r', stubs_align='l', fmt='txt')
class VARSummary(object):
    default_fmt = ...
    part1_fmt = ...
    part2_fmt = ...
    def __init__(self, estimator) -> None:
        ...
    
    def __repr__(self):
        ...
    
    def make(self, endog_names=..., exog_names=...):
        """
        Summary of VAR model
        """
        ...
    


def normality_summary(results):
    ...

def hypothesis_test_table(results, title, null_hyp):
    ...

def pprint_matrix(values, rlabels, clabels, col_space=...):
    ...
