# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 15:47:18 2015

@author: A30123
"""
import os

current_directory=os.getcwd()

files_in_current_directory=os.listdir(path=current_directory)

reg_search_list=[re.search('(^\w+\.)csv',k) for k in files_in_current_directory]
csv_file=[l.group(0) for l in reg_search_list if l!=None]