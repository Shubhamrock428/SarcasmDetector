from sklearn import svm
from sklearn.feature_extraction import *
from collections import Counter
word_counts = []

with open("ProcessedtextTweets.txt", "r") as o:
    line = o.readline()
    
    while (line):
        line.strip()
        word_count = Counter()
        words = line.split(" ")
        for word in words:
            print word
            word_count.update(word)
            
        print word_count
        line = o.readline()
    
    o.close()

word_counts = [{'word1': 1,'word2': 1,},{'word1': 2,'word2': 2,},{'word3': 2,'word4': 2,},{'word3': 3,'word4': 3,}, ]

vectorize = DictVectorizer()

feature_vectorized = vectorize.fit_transform(word_counts)

# # vector array  
features_arr = feature_vectorized.toarray()

# # 1 = sarcastic , 0 = non-sarcastic
observations = [1, 1, 0, 0]

clf = svm.SVC()

clf.fit(features_arr, observations)  

print clf.predict([[ 0, 1, 2, 2]])

