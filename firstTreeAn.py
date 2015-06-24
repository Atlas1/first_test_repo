# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>
from sklearn.datasets import load_iris
iris = load_iris()
iris
iris.target
iris.data
iris.data.shape
x = iris.data[:,2]
x = iris.data[:,:2]
iris.data
x
y=iris.target
x_train = x[:90]
x_train.shape
y_train = y[:90]
y_train
from sklearn import cross_validation

x_train, x_test, y_train, y_test = cross_validation.train_test_split(x,y, test_size=0.2)
x_test
y_test
y_train
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier()
clf_fitted=clf.fit(x_train,y_train)
clf
clf.fitted
clf_fitted
clf_fitted.score(x_test,y_test)
from sklearn import svm
clf=svm.linearSVC(C=1)
clf=svm.linearSVC(C=1)
clf=svm.LinearSVC(C=1)
clf_fitted = clf.fit(x_train, y_train)
clf_fitted
clf_fitted.score(x_test,y_test)
cross_validation.cross_val_score(clf, x, y, cv=5)
print( "Accuracy: %.2f (+/- %.2f " % (scores.mean(), scores.std()*2))
scores = cross_validation.cross_val_score(clf, x, y, cv=5)
print( "Accuracy: %.2f (+/- %.2f " % (scores.mean(), scores.std()*2))
print( "\nAccuracy: %.2f (+/- %.2f) " % (scores.mean(), scores.std()*2))
print( "Accuracy: %.2f (+/- %.2f) " % (scores.mean(), scores.std()*2))
clf=svm.LinearSVC(C=10)
clf_fitted = clf.fit(x_train, y_train)
cross_validation.cross_val_score(clf, x, y, cv=5)
print( "Accuracy: %.2f (+/- %.2f) " % (scores.mean(), scores.std()*2))
Clist = [ 10**i for i in range(-5,5) ]
Clist
for C il Clist:
    clf = svm.LinearSVC(C=C)
    cross_validation.cross_val_score(clf, x, y, cv=5)
    print( "Accuracy: %.2f (+/- %.2f) " % (scores.mean(), scores.std()*2))
for C in Clist:
    clf = svm.LinearSVC(C=C)
    cross_validation.cross_val_score(clf, x, y, cv=5)
    print( "Accuracy: %.2f (+/- %.2f) " % (scores.mean(), scores.std()*2))
Clist
C
for C in Clist:
    clf = svm.LinearSVC(C=C)
    scores = cross_validation.cross_val_score(clf, x, y, cv=5)
    print( "Accuracy: %.2f (+/- %.2f) " % (scores.mean(), scores.std()*2))
for f in Clist:
    clf = svm.LinearSVC(C=f)
    scores = cross_validation.cross_val_score(clf, x, y, cv=5)
    print( "Accuracy: %.2f (+/- %.2f) " % (scores.mean(), scores.std()*2))

