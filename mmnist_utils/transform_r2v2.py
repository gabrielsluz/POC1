'''
Transforms the Moving MNIST dataset from npy format to r2v2 directory format
How is the r2v2 format ?
    The file name of an image format ".jpg" denotes its source video and frame number:
    12_000001.jpg denotes video 12, frame 1.
Where will it be saved ?
    In a folder called mmnist_images
    with a bunch of jpg images inside.
'''

import numpy as np
from PIL import Image
import os


mmnist_dataset = np.load("mnist_test_seq.npy")
num_videos = mmnist_dataset.shape[1]
folder_path = "./mmnist_images/"
os.mkdir(folder_path)
for i in range(num_videos):
    num_frames = mmnist_dataset[:,i,:,:].shape[0]
    for j in range(num_frames):
        im = Image.fromarray(mmnist_dataset[j,i,:,:])
        im.save(folder_path + str(i) + "_" + str(j) + ".jpg")

