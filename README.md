# newsType
NewsType is a desktop application that helps users classify news articles into five categories: business, entertainment, politics, sport, and tech. In NewsType, the user can submit either news articles by way of a text file or by copying and pasting the text directly into the application.  Once the user provides a news article, the application processes it by first preparing the text for the classification algorithm. The application parses the data by removing all special characters, punctuation, possessives from nouns, and words that are not needed. Then the text is converted into a vector representation using term frequency-inverse document frequency (TF-IDF) and then feeding the text through a classification algorithm. Finally, the application will display the resulting classification category. Since NewsType is developed in Python, it can run on both OS X and Windows.

# Installation Guide

NewsType uses Python version 3.7. Other versions of Python have not been tested and might not work correctly. For users that do not have Python 3.7 installed already, I have included the install executables for Windows 64-bit and macOS obtained from https://python.org/ 

Additionally, NewsType has several dependencies that are outlined in the “requirements.txt” file. Here are steps to install all of the specified dependencies:
1.	Once you have python 3.7 installed, you can use the following command in Terminal to install the required pip packages: “python -m pip install --requirement [PATH TO requirements.txt]”
2.	Now that all of the requirements are installed, you can run NewsType by typing “python [PATH TO newsType.py].”

This guide is not meant to be a verbatim step by step instruction manual but rather a general guide to give the basic steps to “install” NewsType. The reason for this is that every computer system is different, and it would be impossible to account for every environmental specific scenario.
