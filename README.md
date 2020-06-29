# newsType
NewsType is a desktop application that helps users classify news articles into five categories: business, entertainment, politics, sport, and tech. In NewsType, the user can submit either news articles by way of a text file or by copying and pasting the text directly into the application.  Once the user provides a news article, the application processes it by first preparing the text for the classification algorithm. The application parses the data by removing all special characters, punctuation, possessives from nouns, and words that are not needed. Then the text is converted into a vector representation using term frequency-inverse document frequency (TF-IDF) and then feeding the text through a classification algorithm. Finally, the application will display the resulting classification category. Since NewsType is developed in Python, it can run on both OS X and Windows.
