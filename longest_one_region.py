# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 13:44:43 2016

@author: A30123
"""

import itertools

import numpy as np

data = [0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1,1,0,0,0,0]
data = [0,0,0,0,0,0,0,0,0]


def longest_one_region(one_zero_list):
    '''
    obtains the beginning and ending indices of the overall longest one region over a list of zeros and ones
    
    Parameters
    ----------
    one_zero_list: list, a list of zeros and ones
    
    Returns
    -------
    start_idx : the beginning index of the longest one region in one_zero_list. 
                If list consists of all zeros, then zero is returned
    
    end_idx: the ending index of the longest one region in one_zero_list. 
            If list consists of all zeros, then zero is returned
    '''    
    if sum(one_zero_list)==0:
        print("no ones in vector")
        return 0, 0
    else:
        group_lengths = []
        group_keys = []
        for k, g in itertools.groupby(one_zero_list):
            cnst_len = len(list(g))
            key = k
            if int(key)==0:
                group_lengths .append([0, cnst_len])
            else:
                group_lengths .append([cnst_len, cnst_len])
            group_keys.append(key)   
                
        
        max_interval_idx = np.argmax(np.asarray(group_lengths), axis=0)[0]
        start_idx = np.cumsum(np.asarray(group_lengths), axis=0)[max_interval_idx - 1, 1]
        end_idx = np.cumsum(np.asarray(group_lengths), axis=0)[max_interval_idx, 1] - 1

        return start_idx, end_idx

longest_one_region(data)

