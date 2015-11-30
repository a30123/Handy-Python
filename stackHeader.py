# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 09:39:47 2015

@author: A30123
"""


unreal_event=np.column_stack((sensor_variables,unreal_event))
unreal_event=np.vstack((np.array(run_list),unreal_event))
ensure_dir(output_folder)
write_array_to_csv(os.path.join(output_folder,output_filename),unreal_event)