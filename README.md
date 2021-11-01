# Kopernikus_test_task
1) Parameters chosen:
a) Standard Deviation (sigma)
b) Number of dilate iterations
c) Minimum contour area

2) 
a) Based on some research papers related to Computer Vision, I decided to use sigma values in the range 0 to 15. A standard deviation of 8 was blurring the grayscale images without losing the information of edges.
b) The number of dilate iterations were varied with values 1,2, and 3 (since 2 was the given value) to check the variation of contours on dilated threshold image. One dilate iteration together with a sigma of value 8, was able to capture the regions of interest precisely.
c) Inorder to reduce the remaining noise i.e., very small contours, the approximate minimum contour area was calculated based on the values on axes of the image.

3) Out of the 484 images in the original data folder, 32 images are found to be duplicate, for the considered parameter values. 

4) A maximum number of edge cases should be considered and the necessary scenarios should be created during the recording of images, inorder to collect many unique cases and consequently to train the algorithms better. 

5) I observed that there is some flaw in the condition related to min_contour_area in the provided "imaging_interview.py" file. I modified it logically and used it for my project.





