# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 17:19:52 2015

@author: Mary
"""

import numpy as np




input_filename="input//distancepairs.csv"

ii=np.loadtxt(input_filename, delimiter=',')


def fetch_data_and_header(file_path_name):
    table_values = np.loadtxt(file_path_name, delimiter=",", skiprows=1)

    with open(file_path_name,'rU') as csvfile:
        contents = csv.reader(csvfile)
        header_list = np.asarray(next(contents))
    
    return table_values, header_list  