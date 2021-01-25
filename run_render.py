"""this module execute render operation 

author baiyu
"""


import os
import subprocess
import pickle
import numpy as np

from render_helper import *
from settings import *

OBJ_NUM = 5
VP_NUM = 5


if __name__ == '__main__':

    # you could also just comment these 4 lines after run it once
    # if you want to use the same models and vps instead of generate
    # again randomly every time you run the program

    # change the numbers to what you want to generate
    # 2 number of objects
    # 3 vps for each model(each vp will be used for only once)
    print("sampling data.....")
    result_dict = random_sample_objs_and_vps(OBJ_NUM, VP_NUM)
    if not os.path.exists(g_temp):
        os.mkdir(g_temp)

    with open(os.path.join(g_temp, g_result_dict), 'wb') as f:
        pickle.dump(result_dict, f)

    # render rgb
    command = [g_blender_excutable_path,
            '--background','--python', 'render_rgb.py']
    subprocess.run(command)

    # #render depth
    command = [g_blender_excutable_path, '--background', '--python', 'render_depth.py']
    subprocess.run(command)

    # write pose
    command = [g_blender_excutable_path,
               '--background', '--python', 'render_pose.py']
    subprocess.run(command)
