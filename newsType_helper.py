#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 7 11:55:10 2019

@author: johncotton
"""
import preprocess as pp
import dataUtil as du
import predict as pred
import pandas as pd

def main():
    print("Starting import:")
    data = du.importData()
    print("-------------------------------------------")
    print("-------------------------------------------")    
    print("Starting preprocessing on " + du.getLatestDataFile() +":")
    print()
    pp.preprocess(pd.read_csv(du.getLatestDataFile()))
    print()
    print("Data has finished importing.")

def classify(text):
    text = pp.preprocess(text, trainingData=False)
    textSeries = pd.Series([text])
    features_train, labels_train, features_test, labels_test = pp.vectorize(pd.read_csv(du.getLatestDataFile(False)), textSeries, series=True)
    cat = pred.predictSeries(features_train, labels_train, features_test, labels_test)
    return cat

def classify2(text, alg):
    text = pp.preprocess(text, trainingData=False)
    textSeries = pd.Series([text])
    features_train, labels_train, features_test, labels_test = pp.vectorize(pd.read_csv('2019102925652-prepocessed.csv'), textSeries, series=True)
    cat = pred.predict(features_train, labels_train, features_test, labels_test, algSelect=alg)
    return cat

def test():
    print("" + du.getLatestDataFile(False) +":")
    print()
    s = pd.Series()
    features_train, labels_train, features_test, labels_test = pp.vectorize(pd.read_csv(du.getLatestDataFile(False)),s)
    pred.predict(features_train, labels_train, features_test, labels_test)
    print()
    


    
