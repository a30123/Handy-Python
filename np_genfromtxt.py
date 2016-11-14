# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 14:36:14 2016

@author: A30123
"""

C = np.genfromtxt(config_file_path_name,dtype = [('Name','S20'),('Switch','S100')],delimiter = ",",skip_header = 1)    
no_of_sensors = len(C['Name'])    
C1 = C['Name'].astype(str)  
C2 = (np.asarray([(C['Switch'].astype(str))]).flatten()).reshape((no_of_sensors,-1))
