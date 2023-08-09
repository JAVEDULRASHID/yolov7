import os
import shutil
from sklearn.model_selection import train_test_split
import cv2
'''
First place the entire dataset folder in the root directory named as custom_dataset
custom_dataset > images
                labels
'''


root_dir = '../6_channel_data'
images = os.listdir(r"../6_channel_data/images")
labels = os.listdir(r"../6_channel_data/labels")

X_train, X_test, y_train, y_test = train_test_split(images, labels, test_size=0.2, random_state=42)
directory = '../datasets/Lidar_6_channel_data'

if os.path.exists(directory):
    print(f"The directory '{directory}' exists.")
else:
    print(f"The directory '{directory}' does not exist.")
    os.mkdir(directory)
    os.makedirs(directory+'/images/train')
    os.makedirs(directory+'/images/val')
    os.makedirs(directory+'/labels/train')
    os.makedirs(directory+'/labels/val')
    print(f"The directory '{directory}' does now exist.")
    for file in X_train:
        img_path = os.path.join(root_dir, 'images', file)
        des_path = directory+'/images/train'
        shutil.copy(img_path, des_path)
    for file in X_test:
        img_path = os.path.join(root_dir, 'images', file)
        des_path = directory+'/images/val'
        shutil.copy(img_path, des_path)
    for file in y_train:
        img_path = os.path.join(root_dir, 'labels', file)
        des_path = directory+'/labels/train'
        shutil.copy(img_path, des_path)
    for file in y_test:
        img_path = os.path.join(root_dir, 'labels', file)
        des_path = directory+'/labels/val'
        shutil.copy(img_path, des_path)
