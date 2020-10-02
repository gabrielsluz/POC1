'''
Transforms the Moving MNIST dataset from npy format to r2v2 directory format
How is the r2v2 format ?
    The file name of an image format ".jpg" denotes its source video and frame number:
    12_000001.jpg denotes video 12, frame 1.
    The dataset must be inside a folder divided into two other folders: train and val
    Train and val are also composed of folders with underline followed by
    letter prefixes, each containing several images. The folder name is used as a prefix
    for the image files. The images must be RGB
Where will it be saved ?
    In a folder called mmnist_images with folders train and val inside. 
    Inside each one there will be a single folder 
    with a bunch of jpg images inside.
'''

import numpy as np
from PIL import Image
import os
import sys

NAME_EXAMPLE = '__2j5sXjpp0_001379.jpg'
PREFIX_LEN = len('__') #Used as prefix for files and is the folder name
VIDEO_NAME_LEN = len('2j5sXjpp0') #Used after the prefix
FRAME_NUM_LEN = len('001379') #Indicates the frame

def gen_file_name(folder_path, prefix, video_num, frame_num):
    file_name = ''
    file_name += folder_path
    file_name += prefix + "/"
    file_name += prefix + "%09d" % video_num #VIDEO_NAME_LEN
    file_name += "_%06d.jpg" % frame_num #FRAME_NUM_LEN
    return file_name


base_dataset_path = sys.argv[1]
print("Store dataset in: "  + base_dataset_path + '/mmnist_images/')
mnist_npy_file = sys.argv[2]
print("npy file location: " + mnist_npy_file)

mmnist_dataset = np.load(mnist_npy_file)
num_videos = mmnist_dataset.shape[1]
num_videos_train = int(num_videos * 0.8) #Uses 80 percent as training

folder_path = base_dataset_path + "/mmnist_images/train/"
os.mkdir(base_dataset_path + '/mmnist_images/')
os.mkdir(folder_path)
os.mkdir(folder_path + '__/')
for i in range(num_videos_train):
    num_frames = mmnist_dataset[:,i,:,:].shape[0]
    for j in range(num_frames):
        im = Image.fromarray(mmnist_dataset[j,i,:,:])
        file_name = gen_file_name(folder_path, '__', i, j)
        rgbimg = Image.new("RGB", im.size)
        rgbimg.paste(im)
        rgbimg.save(file_name)

folder_path = "./mmnist_images/val/"
os.mkdir(folder_path)
os.mkdir(folder_path + '__/')
for i in range(num_videos_train, num_videos):
    num_frames = mmnist_dataset[:,i,:,:].shape[0]
    for j in range(num_frames):
        im = Image.fromarray(mmnist_dataset[j,i,:,:])
        file_name = gen_file_name(folder_path, '__', i, j)
        rgbimg = Image.new("RGB", im.size)
        rgbimg.paste(im)
        rgbimg.save(file_name)
