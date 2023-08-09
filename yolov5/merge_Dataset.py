"""

 This script is for splitting the dataset into train and val set.
 Source directory structure: ./datasets/LIDAR_data1/intensity_data
                            ./datasets/LIDAR_data1/range_data
                            Both intensity_data and range_data folder consists of all images and labels
 IMPORTANT Note: While running the script make sure this file is outside the Yolov5 directory and under the same
                 parent directory of 'datasets' and 'Yolov5' folder.
"""

import os
import shutil
from sklearn.model_selection import train_test_split

sep = os.sep
root = '.'+os.sep + 'datasets' + os.sep + 'LIDAR_data1'
path_i = os.path.join(root, 'intensity_data', 'images')
label_i = os.path.join(root, 'intensity_data', 'labels')
path_r = os.path.join(root, 'range_data', 'images')
lis_i = os.listdir(path_i)
labels_i = os.listdir(label_i)

X_train, X_test, y_train, y_test = train_test_split(lis_i, labels_i, test_size=0.2, random_state=42)

des_i_train = '.' + sep + 'datasets' + sep + 'LIDAR_merge_data' + sep + 'images' + sep + 'train' + sep + 'intensity'
des_i_val = '.' + sep + 'datasets' + sep + 'LIDAR_merge_data' + sep + 'images' + sep + 'val' + sep + 'intensity'
des_r_train = des_i_train.replace('intensity', 'range')
des_r_val = des_i_val.replace('intensity', 'range')

des_label_train = os.path.join('.', 'datasets', 'LIDAR_merge_data', 'labels', 'train')
des_label_val = os.path.join('.', 'datasets', 'LIDAR_merge_data', 'labels', 'val')
os.makedirs(des_i_train)
os.makedirs(des_r_train)
os.makedirs(des_label_train)

os.makedirs(des_i_val)
os.makedirs(des_r_val)
os.makedirs(des_label_val)

for x, y in zip(X_train, y_train):
    img_path_i = os.path.join(path_i, x)
    img_path_r = img_path_i.replace('_i', '_r')
    img_path_r = img_path_r.replace('intensity_data', 'range_data')
    shutil.copy(img_path_i, des_i_train)
    shutil.copy(img_path_r, des_r_train)
    label_path = os.path.join(label_i, x.replace('.png', '.txt'))
    shutil.copy(label_path, des_label_train)

for x, y in zip(X_test, y_test):
    img_path_i = os.path.join(path_i, x)
    img_path_r = img_path_i.replace('_i', '_r')
    img_path_r = img_path_r.replace('intensity_data', 'range_data')
    shutil.copy(img_path_i, des_i_val)
    shutil.copy(img_path_r, des_r_val)
    label_path = os.path.join(label_i, x.replace('.png', '.txt'))
    shutil.copy(label_path, des_label_val)
