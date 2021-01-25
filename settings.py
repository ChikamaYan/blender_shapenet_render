"""settings.py contains all configuration parameters the blender needs


author baiyu
"""
import os


g_shapenet_path = os.path.join('.','objs','02958343')
g_blender_excutable_path = os.path.join('C:/Program Files','Blender Foundation','Blender','blender.exe')


workspace_path = os.path.join('C:/nonsys','ucl','summer-intern','blender_shapenet_render')

#change this path to your background image folder
g_background_image_path = os.path.join(workspace_path,'background_image')

#folders to store synthetic data
g_syn_rgb_folder = os.path.join(workspace_path,'out','syn_rgb')
g_syn_depth_folder = os.path.join(workspace_path,'out','syn_depth')
g_syn_pose_folder = os.path.join(workspace_path,'out','syn_pose')
g_temp = os.path.join(workspace_path,'out','tmp_data')
g_result_dict = 'result.p'

#background image composite
#enum in [‘RELATIVE’, ‘ABSOLUTE’, ‘SCENE_SIZE’, ‘RENDER_SIZE’], default ‘RELATIVE’
g_scale_space = 'RENDER_SIZE'
g_use_film_transparent = True

#camera:
#enum in [‘QUATERNION’, ‘XYZ’, ‘XZY’, ‘YXZ’, ‘YZX’, ‘ZXY’, ‘ZYX’, ‘AXIS_ANGLE’]
g_rotation_mode = 'XYZ'
g_depth_clip_start = 0
g_depth_clip_end = 3

#output:

#enum in [‘BW’, ‘RGB’, ‘RGBA’], default ‘BW’
g_rgb_color_mode = 'RGB'
#enum in [‘8’, ‘10’, ‘12’, ‘16’, ‘32’], default ‘8’
g_rgb_color_depth = '8'
g_rgb_file_format = 'PNG'

g_depth_color_mode = 'BW'
g_depth_color_depth = '8'
g_depth_file_format = 'PNG'

g_depth_use_overwrite = True
g_depth_use_file_extension = True

#dimension:

#engine type [CYCLES, BLENDER_RENDER]
g_engine_type = 'BLENDER_RENDER'

#output image size =  (g_resolution_x * resolution_percentage%, g_resolution_y * resolution_percentage%)
g_resolution_x = 128
g_resolution_y = 128
g_resolution_percentage = 100


#performance:
g_gpu_render_enable = False

#if you are using gpu render, recommand to set hilbert spiral to 256 or 512
#default value for cpu render is fine
g_hilbert_spiral = 512 


