"""
THe root folder should contain LIDAR-->intensity_data-->images
                                                     -->labels
                                    -->range_data-->images
                                                 -->labels
LIDAR should be under the same parent directory of 'datasets'
Destination folder: 6_channel_data-->images
                                   -->labels
"""
import tifffile
import numpy as np
from PIL import Image
import os


root = "./LIDAR"
path_i = os.path.join(root, 'intensity_data', 'images')
path_r = os.path.join(root, 'range_data', 'images')
lis_i = os.listdir(path_i)
lis_r = os.listdir(path_r)


for file in lis_i:
    img_i = Image.open(os.path.join(path_i, file))
    img_r = Image.open(os.path.join(path_r, file.replace("_i", "_r")))
    combined_array = np.concatenate((img_i, img_r), axis=2)
    des = os.path.join("./Lidar_6_channel_data", "images", file.replace("_i.png", "_c.tif"))
    tifffile.imwrite(des, combined_array)


# Code for renaming the labels '_c' instead of '_i'
"""
root = "./LIDAR/intensity_data/labels"
lis_c = os.listdir(root)


for file in lis_c:
    label_path = os.path.join(root, file)
    new_file = os.path.join(root, file.replace("_i", "_c"))
    os.rename(label_path, new_file)
"""