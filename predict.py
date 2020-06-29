#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 02:40:16 2019

@author: johncotton
"""
import sys
import pandas as pd

def predictSeries(features_train, labels_train, features_test, labels_test):
    #print("# -------------------------------------------------------------")
    #print("# -------------------------------------------------------------")
    #print("Making a model using svm.SVC()")
    from sklearn import svm
    model = svm.SVC(gamma='scale')

    #print("Training model...")
    model = model.fit(features_train, labels_train)

    #print("Predicting testing data classification...")
    predicted_labels = model.predict(features_test)
    #print(model.score(features_test, labels_test))
    category_codes = {0: 'Business', 1: 'Entertainment', 2: 'Politics', 3: 'Sport', 4: 'Tech'}
    cat = int(predicted_labels.item(0))
    print('RESULTS:', cat)
    return str(category_codes[cat])

    print("# -------------------------------------------------------------")

def predict(features_train, labels_train, features_test, labels_test, algSelect = "SVM"):
    if algSelect == "SVM" or algSelect == "None":
        print("in", algSelect)
        print("# -------------------------------------------------------------")
        print("# -------------------------------------------------------------")
        print("Making a model using svm.SVC()")
        from sklearn import svm
        model = svm.SVC(gamma='scale')

        # print("Training model...")
        model = model.fit(features_train, labels_train)

        # print("Predicting testing data classification...")
        predicted_labels = model.predict(features_test)
        # print(model.score(features_test, labels_test))
        category_codes = {0: 'Business', 1: 'Entertainment', 2: 'Politics', 3: 'Sport', 4: 'Tech'}
        cat = int(predicted_labels.item(0))
        print('RESULTS:', cat)
        return str(category_codes[cat])
    print("# -------------------------------------------------------------")
    if algSelect == "GBC1":
        print("in", algSelect)
        print("# -------------------------------------------------------------")
        #print("Making a model using GradientBoostingClassifier()")
        from sklearn.ensemble import GradientBoostingClassifier

        model2 = GradientBoostingClassifier()

        model2 = model2.fit(features_train, labels_train)
        #print(features_test)
        predicted_labels = model2.predict(features_test)
        category_codes = {0: 'Business', 1: 'Entertainment', 2: 'Politics', 3: 'Sport', 4: 'Tech'}
        cat = int(predicted_labels.item(0))
        print('RESULTS:', cat)
        return str(category_codes[cat])
        print("# -------------------------------------------------------------")

    if algSelect == "XGB":
        print("in", algSelect)
        print("# -------------------------------------------------------------")

        #print("Making a model using XGBClassifier()")
        from xgboost import XGBClassifier

        model3 = XGBClassifier()

        model3 = model3.fit(features_train, labels_train)

        predicted_labels = model3.predict(features_test)
        print(predicted_labels)
        predictions = [round(value) for value in predicted_labels]
        print(predictions)
        category_codes = {0: 'Business', 1: 'Entertainment', 2: 'Politics', 3: 'Sport', 4: 'Tech'}
        cat = int(predictions[0])
        print('RESULTS:', cat)
        return str(category_codes[cat])
        print("# -------------------------------------------------------------")
    if algSelect == "RFC":
        print("in", algSelect)
        print("# -------------------------------------------------------------")

        #print("Making a model using RandomForestClassifier()")
        from sklearn.ensemble import RandomForestClassifier

        model4 = RandomForestClassifier(n_jobs=2, random_state=0)

        model4 = model4.fit(features_train, labels_train)

        predicted_labels = model4.predict(features_test)
        predictions = predicted_labels

        category_codes = {0: 'Business', 1: 'Entertainment', 2: 'Politics', 3: 'Sport', 4: 'Tech'}
        cat = int(predictions.item(0))
        print('RESULTS:', cat)
        return str(category_codes[cat])
        print("# -------------------------------------------------------------")
