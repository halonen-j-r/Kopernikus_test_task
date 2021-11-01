import os
import sys
from itertools import combinations

sys.path.append(os.path.dirname(__file__))
path = os.path.dirname(__file__)

from data_preprocessing import resize_prepro_images, folder_unique_images
from imaging_interview import compare_frames_change_detection

if __name__ == "__main__": 
    
    print("Preprocessing images.....")
    color_list, file_index, gray_list = resize_prepro_images()
    duplicates = []
    non_duplicates = []
    uniques_images = []
    
    #compare every pair of images in the list without repetition
    img_comb = combinations(gray_list, 2)
    index_comb = combinations(file_index, 2)
    image_comb_list = list(img_comb)
    index_comb_list = list(index_comb) 
    
    print("Finding duplicate pairs of images......")
    for i, j in zip(image_comb_list, index_comb_list):
        img_1, img_2 = i
        ix_1, ix_2 = j
        min_contour_area = 1250  #selected based on the generated contours for the given sigma and dilate iterations
        score, res_cnts, thresh = compare_frames_change_detection(img_1, img_2, min_contour_area)
        # print("score: {}".format(score))
        
        if ix_1 == 0 and ix_2 == 1:
           non_duplicates.append(os.path.abspath(color_list[ix_1]))  #The very first original image is never a second image of a pair
           
        if score == 0:
           duplicates.append(os.path.abspath(color_list[ix_2])) #every second image in duplicate pairs is considered a duplicate
           
    # print("Duplicate pairs appended : {}".format(len(duplicates)))
    
    #sort paths of unique images
    for item in duplicates:
        if not item in non_duplicates:
            non_duplicates.append(item)
           
    print("Unique images : {}".format(len(non_duplicates))) 
    
    #create folder of unique images     
    folder_unique_images(non_duplicates, color_list)
    
    
    
    
    
    
    

        
    
       