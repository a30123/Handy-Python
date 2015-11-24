# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 14:43:33 2015

@author: Mary
"""

u,indices=np.unique(testDataCycle,return_index=True)
u,counts=np.unique(testDataCycle,return_counts=True) 
#u,indices=np.unique(['c','b','a','b'],return_index=True)
sorting_index=sorted(range(len(indices)),key=lambda x:indices[x])
counts[sorting_index]
testDataCycle[indices]