# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 13:20:16 2015

@author: A30123
"""
import pandas as pd


All_temp=pd.read_csv(single_file_path)
 
All_temp=All_temp.convert_objects(convert_numeric=True)
All_temp[sensor_list]=All_temp[sensor_list].astype('float32')