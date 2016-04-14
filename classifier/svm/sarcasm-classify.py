from sklearn import svm
from sklearn.feature_extraction import *
from collections import Counter

# Array of dicts. dicts have count of words
word_counts = []
# 1 = sarcastic , 0 = non-sarcastic
observations = []

# Read sarcastic 
with open("sarcastic.txt", "r") as o:
    line = o.readline()
    
    while (line):
        line = line.strip()
        word_count = Counter(filter(None,line.split(" ")))
        word_counts.append(dict(word_count) )
        # 1 for sarcastic
        observations.append(1)
        line = o.readline()
    
    o.close()

# Read non sarcastic
with open("non_sarcastic.txt", "r") as o:
    line = o.readline()
    
    while (line):
        line = line.strip()
        word_count = Counter(filter(None,line.split(" ")))
        word_counts.append(dict(word_count) )
        # 0 for non sarcastic
        observations.append(0)
        line = o.readline()
    
    o.close()

# word_counts = [{'word1': 1,'word2': 1,},{'word1': 2,'word2': 2,},{'word3': 2,'word4': 2,},{'word3': 3,'word4': 3,} ]

vectorize = DictVectorizer()

feature_vectorized = vectorize.fit_transform(word_counts)

# # vector array  
features_arr = feature_vectorized.toarray()

clf = svm.SVC()
# clf = SGDClassifier(loss="hinge", penalty="l2")

clf.fit(features_arr, observations)  
print vectorize.get_feature_names()
# print clf.predict([[ 0, 1, 2, 2]])

