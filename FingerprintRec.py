# Editor: Rajesh Kumar (rajeshjnu2006@gmail.com)
# There is a direct way of reading dataset from Kaggle https://www.kaggle.com/general/74235 
# You can try doing that the link is https://www.kaggle.com/datasets/ruizgara/socofing
# Alternatively, you can download the dataset from Kaggle and put it into your IDE
# Following code is adapted from https://sesamedisk.com/authentication-in-python-biometric-fingerprint-matching/

import os
# setting the path for the folder containing the data
datapath = os.path.join(os.getcwd(),"Dataset")
# os.listdir returns a list of items residing in the input folder location
folder_list = os.listdir(datapath)

# creating a dictionary of the foldernames, not necessary just a preference
dfolders = {'Template':'Real', 'Probe-Hard':'Altered-Hard', 'Probe-Medium': 'Altered-Medium', 'Probe-Easy':'Altered-Easy'}
template_filenames = os.listdir(os.path.join(datapath, dfolders['Template']))
probe_hard_filenames = os.listdir(os.path.join(datapath, 'Altered', dfolders['Probe-Hard']))
probe_medium_filenames = os.listdir(os.path.join(datapath, 'Altered', dfolders['Probe-Medium']))
probe_easy_filenames = os.listdir(os.path.join(datapath, 'Altered', dfolders['Probe-Easy']))
howmuchtowait = 5000 # in milliseconds

# Now that we are able to read the file names, we can start reading the images 
# There is an opencv library that we can use to read and show the images
# The imshow of opencv library does not work in Google colab, so Google colab has a path for that
# The following code is taken from 
# https://github.com/Sesame-Disk/fingerprint-matching/blob/main/fingerprint_match.py
# Follows the article https://sesamedisk.com/authentication-in-python-biometric-fingerprint-matching/
import os
from aiohttp import Fingerprint
import cv2
import random
import numpy as np

# The following experiment design is about picking a random probe image from one of the altered
# data folders and trying to find its match in the template (real fingerprints) folder. 
# Now pick a probe image randomly from the altered folder of your choice
probe_image_name = random.choice(probe_hard_filenames)
print(f'The picked probe image is: {probe_image_name}')


# One of the probe images that worked for demo is as follows:
# A fixed image that i have already tested has some positive scores
# probe_image_name = "9__M_Left_little_finger_CR.BMP"

probe_file_parentdir = os.path.join(datapath, 'Altered', dfolders['Probe-Hard'])
probe_image = cv2.imread(os.path.join(probe_file_parentdir, probe_image_name))
print(f'following is how the probe image looks like visually:')
final_image = cv2.resize(probe_image, (400, 300))
cv2.imshow("probe_and_template_images", final_image)
cv2.waitKey(5)

# Now to compare we need to extract features from the probe image
# Extracting the keypoints and descriptors from the probe image.
sift = cv2.SIFT_create() # creating an SIFT object
probe_keypoints, prob_des = sift.detectAndCompute(probe_image, None)

# Assuming that the best score is 0, as we have to find the best (max) score
best_score = 0
counter = 0
best_match_filename = "No match found!"
best_match_image = kp1 = kp2 = mp = None
template_file_parentdir = os.path.join(datapath, dfolders['Template'])

# Comparing the prob images with the images inside the real (template) folder
# one by one
for image_name in template_filenames:

    # reading the current template image
    template_image = cv2.imread(os.path.join(template_file_parentdir,image_name))
    # before we compare we need to extract the keypoints and descriptors from the template image.
    template_keypoints, template_des = sift.detectAndCompute(template_image, None)
    
    # fast library for approx best match KNN
    # Flann Based Matcher performs a fast local approximate nearest neighbors (FLANN) calculation between two
    # sets of feature vectors. The result is two NumPy arrays. The first is a list of indexes of the matches,
    # while the second contains the values of match distances.
    matches = cv2.FlannBasedMatcher({"algorithm": 1, "trees": 10}, {}).knnMatch(prob_des, template_des, k=2)


    # No idea what is going on here
    match_points = []
    for p, q in matches:
        if p.distance < 0.1 * q.distance:
            match_points.append(p)

    # The number of keypoints won't be necessarily same for both template and probe image
    # Comparing the minimum number of keypoints, the min of the two
    if len(probe_keypoints) <= len(template_keypoints):
        total_keypoints = len(probe_keypoints)
    else:
        total_keypoints = len(template_keypoints)

    # calculating the match score as percentage
    match_score = len(match_points) / total_keypoints * 100
    
    
    # Saving template image with highest match score
    if  match_score > best_score:
        best_score = match_score
        best_match_filename = image_name
        best_match_image = template_image
        kp1, kp2, mp = probe_keypoints, template_keypoints, match_points
    
    if match_score > 0: # majority of the match scores were zero, showing only the scores that are > 0
      print(f'({probe_image_name}, {image_name}) ==>: {match_score}')
      print(f'following is how the images look like visually:')
      # display images side by side -- concatenate image Horizontally
      # https://www.geeksforgeeks.org/how-to-display-multiple-images-in-one-window-using-opencv-python/
      horizontal = np.concatenate((probe_image, template_image), axis=1)
      horizontal = np.concatenate((probe_image, best_match_image), axis=1)
      final_image = cv2.resize(horizontal, (400, 300))
      cv2.imshow("probe_and_template_images", final_image)
      cv2.waitKey(howmuchtowait) # wait for specified milliseconds


print(f'best match template: {best_match_filename}')
print(f'best score: {best_score}')
horizontal = np.concatenate((probe_image, best_match_image), axis=1)
final_image = cv2.resize(horizontal, (400, 300))
cv2.imshow("probe_and_template_images", final_image)
cv2.waitKey(howmuchtowait) # wait for specified milliseconds


# Drawing the matches
if len(mp) > 0:
    print('I came here to draw the matched points, did you see that?')
    result = cv2.drawMatches(probe_image, kp1, best_match_image, kp2, mp, None)
    result = cv2.resize(result, (400, 300))
    cv2.imshow("Result", result)
    cv2.waitKey(howmuchtowait**2) # Stop for more time than usual
    cv2.destroyAllWindows()

