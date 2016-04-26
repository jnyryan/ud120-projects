#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

from sklearn.svm import SVC
#clf = SVC(kernel="linear")
#clf = SVC(kernel="rbf")
#clf = SVC(kernel="rbf", C=10 )
#clf = SVC(kernel="rbf", C=100 )
#clf = SVC(kernel="rbf", C=1000 )
clf = SVC(kernel="rbf", C=10000 )

# Training

# reduce size of test data
#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]

t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

# Prediction
t0 = time()
pred = clf.predict(features_test)
print "prediction time:", round(time()-t0, 3), "s"

# results of test predictions to actual test results
from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)
print "Accuracy : ", acc

# What class does your SVM (0 or 1, corresponding to Sara and Chris respectively) predict for element 10 of the test set? The 26th? The 50th?

print "Prediction for index 10", pred[10]
print "Prediction for index 26", pred[26]
print "Prediction for index 50", pred[50]

count = 0
for n in pred:
    if n == 1:
        count = count + 1

print "how many are predicted to be in the Chris: ", count


#########################################################
