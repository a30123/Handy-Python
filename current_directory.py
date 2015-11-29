# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 17:14:19 2015

@author: Mary
"""

import os

current_directory=os.getcwd()
train_data_folder=os.path.join(current_directory,"train_test_data//train_data")
test_data_folder=os.path.join(current_directory,"train_test_data//test_data")
train_filenames=os.listdir(train_data_folder)
test_filenames=os.listdir(test_data_folder)
