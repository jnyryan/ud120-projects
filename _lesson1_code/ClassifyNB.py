

def classify(features_train, labels_train, features_test, labels_test):
    ### import the sklearn module for GaussianNB
    ### create classifier
    ### fit the classifier on the training features and labels
    ### return the fit classifier


    ### your code goes here!

    from sklearn.naive_bayes import GaussianNB

    # Create the classifier
    clf = GaussianNB()
    # fit is using our training features and training labels
    clf.fit(features_train, labels_train)
    # create a vector of predictions from the trained classifier
    pred = clf.predict(features_test)

    accuracy = clf.score(features_test, labels_test)
    print "Accuracy is ", accuracy

    return clf
