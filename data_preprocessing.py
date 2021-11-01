# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 01:21:59 2021

@author: user
"""
import os
import glob
import cv2
import math
from PIL import Image
from imaging_interview import preprocess_image_change_detection

path = os.path.dirname(__file__)
data_path = os.path.join(path, r'c23', '*g')

def dim(img):
    scale_percent = 30
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    return dim

def gaussian_blur_radius():
    radius_list = []
    for sigma in range(0, 8):
        kernel_radius = 1 + (2*math.sqrt((-2)*(sigma**2)*(math.log(0.005))))
        if (int(kernel_radius) % 2) == 0:
            kernel_radius += 1
            
        radius_list.append(kernel_radius)
        
    return radius_list
            
def preprocess_images(data_path):
    color_list = []
    file_index = []
    i = 0
    radius_list = gaussian_blur_radius()
    
    if not os.path.exists(os.path.join(path, r'gray_images')):
            os.makedirs(os.path.join(path, r'gray_images'))
            
    for image in glob.glob(data_path):
        img = cv2.imread(image)
        color_list.append(os.path.basename(glob.glob(data_path)[i]))
        file_index.append(i)
        gray_image = preprocess_image_change_detection(img, radius_list)
        
        cv2.imwrite(os.path.join(path, r'gray_images', 'image_{}.png').format(i+1), gray_image)
        i+=1
        
    return color_list, file_index
        
def resize_prepro_images():
    color_list, file_index = preprocess_images(data_path)
    gray_list = []
    
    gray_img_path = os.path.join(path, r'gray_images', '*g')
    
    for image in glob.glob(gray_img_path):
        img = cv2.imread(image, 0)
        r_img= cv2.resize(img, dim(img), interpolation = cv2.INTER_AREA) 
        gray_list.append(r_img)
   
    return color_list, file_index, gray_list

def folder_unique_images(non_duplicate_list, color_list):
    i=0
    if not os.path.exists(os.path.join(path, r'unique_images')):
        os.makedirs(os.path.join(path, r'unique_images'))
    
    for image_path in non_duplicate_list:
        if os.path.basename(image_path) in color_list:
           im_path = os.path.join(path, r'c23', os.path.basename(image_path))
           img = cv2.imread(im_path)
           im = Image.fromarray(img)
           im.save(os.path.join(path, r'unique_images', 'image_{}.png').format(i+1))
           i+=1

    



        



