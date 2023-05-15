### Note for future improvement: 

Provide a better idea of authentication and identification 

Maybe say authentication is auth(id, token) matches with that of the id's stored pictures for genuine scores and matches with that of non-id folder to get
impostor scores

in contrast, identification(token) search for the id, basically the id would be the one which brings the highest match score
but remember the highest match score might not be the person that you are searching for and that would be false alarm. 


### Fingerprint-Recognition-SIFT

# CS379SP23-HW2

Biometric systems - fingerprint recognition via SIFT, performance evaluation on https://www.kaggle.com/datasets/ruizgara/socofing

Spring 2023, Bucknell University 

Due date: Due March 10th, 5 pm | submissions would be accepted through GitHub only unless stated otherwise.

Your full name:  

ime taken to complete:  

You can read the [general setup instructions](https://docs.google.com/document/d/1A1BGTjrnIgJXBYV0qg_ZrlOLL4x0hzlaSt6ryFXMbQE/edit?usp=sharing) before you start!

### Description: 

In HW1 we worked with hypothetical biometric recognition systems to compare. In this we will evaluate fingerprint recognition system on a publicly available dataset.

Face recognition consists of two functionalities, authentication (2 class problem, genuine and impostors) and identification (n class problem).
Once implemented successfully you will understand the difference between authentication and identification at implementation level. 
You are given a basic skeleton of the following in the FingerprintRec.py file: 

(1) How to read and show fingerprint from a dataset

(2) How to extract SIFT-based features (keypoints and descriptors)

(3) How to match two fingerprint and generate match scores using the extracted features

Your job is to understand the working of the given code (you can read the article referred in the implementation for deeper understanding)
and draw ideas to implement the Authentication and Identification functionalities in the dedicated files i.e. Authentication.py and Identification.py. 

Although FingerprintRec.py does not follow object-oriented design, I encourage you to follow OOD in your code. The design of code is left to your 
to you so make sure you comment and write a short description of design of code for both Authentication.py and Identification.py so its easier for me to understand during grading. 


The dataset folder provided with the code inside Dataset folder is just a sample set to work with the starter code and understand. 

Make sure you download the full dataset from the provided source and  

### Specific tasks: 

(1) Start a report document (I am a fan of Google doc), create a section "design" and illustrate what design you are following to implement both Authentication.py and Identification.py 

(2) Implement Authentication.py

(3) Implemented Identification.py

(4) Comment your code properly so anyone reading your code can understand what is going on

(5) plot_roc, plot_det, and report eer using the code you have already written in HW1 on the entire dataset beside the sample dataset

(6) Comment on the performance of both Authentication and Identification functionalities with reasoning  

(7) Expand the report document you created in step 1, outlining the process you followed, the results (roc, det, eer) you got, and what is your interpretation of the results. Upload the report in pdf format.

(8) Which functionality (identification or authentication) achieved the best EER rates and how would you explain that?

Each of the above tasks will be graded, so please complete all of them. 

Assume that the genuine and impostor scores represent the similarity measure

That means the higher the score is the better the match

Use any package you want but make sure you don't use the package that solves the part you have to implement that is Authentication and Identification functionalities. 

If needed use, np.random.seed(1846) so the results are reproducible

Any questions, please post on Piazza, try to keep your post public so other folks benefit. Don't post code please.

You may not be able to commit + push your repo with the large dataset, dont worry I will have the dataset to test your code. And here comes in the Report that helps me understand whether you actually completed the tasks with a proper understanding. 


