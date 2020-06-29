#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 02:23:47 2019

@author: johncotton
"""
import dataUtil as du
import string
import re
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

from sklearn.model_selection import train_test_split
from sklearn.feature_selection import chi2
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.data.path = ['nltk/nltk_data']

def preprocess(data, trainingData=True):
    if trainingData:
        # Convert the article_org Column to lowercase and store it in column article_lowercase.
        data.loc[:, 'article_lowercase'] = data.loc[:,'article_org'].str.lower()
        # Removes all non-ascii characters from the text.
        data.loc[:, 'article_ascii'] = data.loc[:,'article_lowercase'].map(lambda s: removeNonASCII(s))
        
        data.loc[:, 'article_rmMan'] = data.loc[:,'article_ascii'].map(lambda s: removeMan(s, ['¬','£']))
        # Removes all possessives from the text.
        data.loc[:, 'article_rmpossessives'] = data.loc[:,'article_rmMan'].map(lambda s: removePosessives(s))
        # Removes all escape characters from articles
        data.loc[:, 'article_rmEscapeChar'] = data.loc[:, 'article_rmpossessives'].map(lambda s: removeEscapeCharacters(s))
        # Removes duplicate spaces.
        data.loc[:, 'article_rmSpace'] = data.loc[:, 'article_rmEscapeChar'].map(lambda s: removeDuplicateSpaces(s))
        # Romoves all punctuation.
        data.loc[:, 'article_rmPunctuation'] = data.loc[:,'article_rmSpace'].map(lambda s: removePunctuation(s))
        # Romoves all stop-words.
        data.loc[:, 'article_rmStopWords'] = data.loc[:, 'article_rmPunctuation'].map(lambda s: removeStopWords(s))
        
        
        # lemmatizes article
        data.loc[:, 'article_lemmatized'] = data.loc[:,'article_rmStopWords'].map(lambda s: lemmatize(s))
        
        # Updates article_len column
        data.loc[:, 'article_len'] = data.loc[:,'article_lemmatized'].map(lambda s: len(s))
    
        data.loc[:, 'article_preprossed'] = data.loc[:,'article_lemmatized']
    
    
        data.loc[:, 'category_num'] = data.loc[:,'category'].map(lambda c: 0 if c == 'business' else 1 if c == 'entertainment' else 2 if c == 'politics' else 3 if c == 'sport' else 4 if c == 'tech' else -1)
    
        du.exportDF(data, data=1)
        return data
    
    if not(trainingData):
        # Converts to lowercase.
        data = data.lower()
        # Removes all non-ascii characters from the text.
        data = removeNonASCII(data)
        # Manual removal.
        data = removeMan(data, ['¬', '£'])
        # Removes all possessives from the text.
        data = removePosessives(data)
        # Removes all escape characters from articles
        data = removeEscapeCharacters(data)
        # Removes duplicate spaces.
        data = removeDuplicateSpaces(data)
        # Romoves all punctuation.
        data = removePunctuation(data)
        # Romoves all stop-words.
        data = removeStopWords(data)
        # lemmatizes article
        data = lemmatize(data)
        
        return data


    # This function removes punctuation from a string.
    # @param stringData  - type str.
    # @return a new string with all of the punctuation removed.
def removePunctuation(stringData):
    stringData = ''.join(char for char in stringData if char not in string.punctuation)
    stringData = stringData.replace('¬', '')
    return stringData

    # This function removes sucessive duplicate spaces from a string.
    # @param stringData  - type str.
    # @return a new string with all of the sucessive duplicate spaces removed.
def removeDuplicateSpaces(stringData):
    stringData = re.sub(' +', ' ',stringData)
    return stringData

    # This function removes possessives from a string.
    # @param stringData  - type str.
    # @return a new string with all of the possessives removed.
def removePosessives(stringData):
    stringData = stringData.replace("'s", "")
    stringData = stringData.replace("s'", "s")
    stringData = stringData.replace("\'s", "")
    stringData = stringData.replace("s\'", "s")
    stringData = stringData.replace('"', '')
    return stringData

    # This function removes escape character from a string.
    # @param stringData  - type str.
    # @return a new string with all of the escape character removed.
def removeEscapeCharacters(stringData):
    stringData = stringData.replace("\newline", " ")
    stringData = stringData.replace("\\", " ")
    stringData = stringData.replace("\'", "")
    stringData = stringData.replace('\"', "")
    stringData = stringData.replace("\a", " ")
    stringData = stringData.replace("\b", " ")
    stringData = stringData.replace("\f", " ")
    stringData = stringData.replace("\n", " ")
    stringData = stringData.replace("\r", " ")
    stringData = stringData.replace("\t", " ")
    stringData = stringData.replace("\v", " ")
    return stringData

    # This function removes stop-words from a string.
    # @param stringData  - type str.
    # @return a new string with all of the stop-words removed.
def removeStopWords(stringData):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(stringData)
    wordsFiltered = []
    for w in words:
        if w not in stop_words:
            wordsFiltered.append(w)
    return ' '.join(wordsFiltered)

def removeNonASCII(stringData):
    asci = set(string.printable)
    filter(lambda s: s in asci, stringData)
    return stringData
    
def removeMan(stringData, rmList):
    for s in rmList:
        stringData = stringData.replace(s, "")
    return stringData
    

    # This function lemmatizes a string using WordNetLemmatizer.
    # @param stringData  - type str.
    # @return a new string that is lemmatized.
def lemmatize(stringData):
    
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = []
    words = stringData.split(" ")
    
    for word in words:
        lemmatized_words.append(lemmatizer.lemmatize(word, pos="v"))
    
    lemmatized_words = " ".join(lemmatized_words)
    #print(lemmatized_words)
    return lemmatized_words


def vectorize(df, s_test, series = False):
    if series == False:
        x_train, x_test, y_train, y_test = train_test_split(df.loc[:, 'article_preprossed'], df.loc[:,'category_num'], test_size=0.15, random_state=8)

        tfidf = TfidfVectorizer(encoding='utf-8', ngram_range=(1,2), stop_words=None, lowercase=False, max_df=1., min_df=10, max_features=300, norm="l2", sublinear_tf=True)

        features_train = tfidf.fit_transform(x_train).toarray()
        labels_train = y_train
        #print(features_train.shape)
        #print(type(x_test), x_test)
        features_test = tfidf.transform(x_test).toarray()
        labels_test = y_test
        #print(features_test.shape)
    if series == True:
        x_train, x_test, y_train, y_test = train_test_split(df.loc[:, 'article_preprossed'], df.loc[:,'category_num'], test_size=0.15, random_state=8)

        tfidf = TfidfVectorizer(encoding='utf-8', ngram_range=(1,2), stop_words=None, lowercase=False, max_df=1., min_df=10, max_features=300, norm="l2", sublinear_tf=True)

        features_train = tfidf.fit_transform(x_train).toarray()
        labels_train = y_train
        #print(features_train.shape)

        features_test = tfidf.transform(s_test).toarray()

        labels_test = -1
 

    category_codes = {'business': 0,'entertainment': 1,'politics': 2,'sport': 3,'tech': 4}

    for Product, category_id in sorted(category_codes.items()):
        
        features_chi2 = chi2(features_train, labels_train == category_id)
        
        indices = np.argsort(features_chi2[0])
        feature_names = np.array(tfidf.get_feature_names())[indices]
        
        unigrams = [v for v in feature_names if len(v.split(' ')) == 1]
        bigrams = [v for v in feature_names if len(v.split(' ')) == 2]
        '''
        print("# '"+ Product + "' category:")
        print("  . Most correlated unigrams:\n. {}".format('\n. '.join(unigrams[-5:])))
        print("  . Most correlated bigrams:\n. {}".format('\n. '.join(bigrams[-2:])))
        print("")
        '''
    return features_train, labels_train, features_test, labels_test

    # This function downloads all of the NLTK required packages.
def nltkDependancies():
    nltk.download('wordnet')
    nltk.download('stopwords')
    nltk.download('punkt')