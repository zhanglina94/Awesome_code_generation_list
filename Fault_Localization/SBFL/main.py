import numpy as np
import pandas as pd
from sbfl.base import SBFL
from scipy.stats import rankdata

#   e1,e2,e3,e4,e5,e6
X = np.array([
    [1,1,0,0,1,1], # coverage of test t0
    [1,1,0,0,1,1], # coverage of test t1
    [0,1,1,0,1,0], # coverage of test t2
    [1,0,0,1,0,0],
    [0,1,0,1,1,0],
], dtype=bool)

y = np.array([1,1,0,0,0], dtype=bool)

print("X:",X,"y:",y)

"""
Calculate the suspiciousness scores
"""
sbfl = SBFL(formula='Ochiai')
sbfl.fit(X, y)
print(sbfl.ranks(method='max'))
