#!/usr/bin/python

"""
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project.

    Use a Naive Bayes Classifier to identify emails by their authors

    authors and labels:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from class_vis import prettyPicture, output_image

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#########################################################
### your code goes here ###
from sklearn.naive_bayes import GaussianNB

### your code goes here!

t0 = time()
# Create the classifier
clf = GaussianNB()
# fit is using our training features and training labels
clf.fit(features_train, labels_train)
# create a vector of predictions from the trained classifier
#pred = clf.predict(features_test)

print "training time:", round(time()-t0, 3), "s"
t0 = time()
accuracy = clf.score(features_test, labels_test)
print "prediction time:", round(time()-t0, 3), "s"

print "Accuracy is ", accuracy

### draw the decision boundary with the text points overlaid
prettyPicture(clf, features_test, labels_test)
#output_image("test.png", "png", open("test.png", "rb").read())

#########################################################
