#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 02:33:22 2019

@author: johncotton
"""
import os
import glob
import pandas as pd
from datetime import datetime

def timeStamp(): 
    today = datetime.today()
    time = (str(today.year) + str(today.month) + str(today.day) + str(today.hour) + str(today.minute) + str(today.second))
    return str(time)



    # This function exports a Pandas DataFrame to a CSV file.
    # @param df - the Dataframe that will be exported.
    # @param data - 0 = training data; 1 = prepocessed data; 2 = other data.
    # @return a new string with all of the stop-words removed.
def exportDF(df, data=0):
    if data == 0:
        filename = 'Training_Data_CSV/' + timeStamp() + '-trainingData.csv'
        print("Creating " + filename)
        df.to_csv(filename, sep=',', encoding='utf-8')
    if data == 1:
        filename = 'Saved_CSV/' + timeStamp() + '-prepocessed.csv'
        print("Creating " + filename)
        df.to_csv(filename, sep=',', encoding='utf-8')
    if data == 2:
        filename = 'Saved_CSV/' + timeStamp() + '-data.csv'
        print("Creating " + filename)
        df.to_csv(filename, sep=',', encoding='utf-8')

def importData(data = 0):
    if data == 0:
        articleCategory = ['business', 'entertainment', 'politics', 'sport', 'tech']
        filesDF = pd.DataFrame(columns=['fileName', 'category', 'article_len','article_org' ])

        for cat in articleCategory:
            fileDir = os.listdir('bbc/' + cat + '/')
            try:
                fileDir.remove('.DS_Store')
                print()
            except:
                print()
                #print('NO .DS_Store FOUND')
                
            for fileName in fileDir:
               
                fileOpen = open('bbc/' + cat + '/' + fileName, 'r')
                fileContent = str(fileOpen.read())
                fileOpen.close()
                file = pd.Series({'fileName': fileName, 'category': cat, 'article_len': len(fileContent),'article_org': fileContent})
                filesDF = filesDF.append(file, ignore_index=True)
                
            print(cat + ' is done importing.')
            #print("Dataframe Contens ", filesDF, sep='\n')

        print()
        exportDF(filesDF,data=0)
        print()        
        print("Data has finished importing.")
        return filesDF
    elif data == 1:
        pass



    
def getLatestDataFile(training=True):
    if training:
        list_of_files = glob.glob('Training_Data_CSV/*-trainingData.csv') # * means all if need specific format then *.csv
        latest_file = max(list_of_files, key=os.path.getctime)
        return latest_file
    if not(training):
        list_of_files = glob.glob('Saved_CSV/*-prepocessed.csv') # * means all if need specific format then *.csv
        latest_file = max(list_of_files, key=os.path.getctime)
        return latest_file