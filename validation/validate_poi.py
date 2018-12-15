#!/usr/bin/env python3


"""
    Starter code for the validation mini-project.
    The first step toward building your POI identifier!

    Start by loading/formatting the data

    After that, it's not our code anymore--it's yours!
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "rb") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list, sort_keys='../tools/python2_lesson14_keys.pkl')
labels, features = targetFeatureSplit(data)



### it's all yours from here forward!  
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    features, labels, random_state=42, test_size=0.3)

from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf.fit(X_train, y_train)
y_predict = clf.predict(X_test)
clf.score(X_test, y_test)
num_people = 0
num_poi = 0
for i in y_test:
    if i == 1.0:
        num_poi += 1
    num_people += 1
print("Number of POI: %d" %num_poi)
print("Number of people: %d" %num_people)

true_pos = 0
for true, pred in zip(y_test, y_predict):
    if true == 1 and pred == 1:
        true_pos += 1
print("Number of true positives: %d" %true_pos)

from sklearn.metrics import precision_score, recall_score
precision = precision_score(y_test, y_predict)
recall = recall_score(y_test, y_predict)
print("Precision score: %.4f" %precision)
print("Recall score: %.4f" %recall)



