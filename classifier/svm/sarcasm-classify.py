from collections import Counter

from sklearn import svm
from sklearn.feature_extraction import *

test_data = ""

def createPredictionVector(feature_names, test_data):
    print test_data
    vec_arr = [0] * len(feature_names)
    for word in test_data.split(" "):
        if word in feature_names:
            vec_arr[feature_names.index(word)]=1
    
    print vec_arr
    print Counter(vec_arr)
    return vec_arr
    

def getTrainingVectors (sarcastic_corpus="sarcastic.txt", non_sarcastic_corpus="non_sarcastic.txt"):
    global test_data
    # Array of dicts. dicts have count of words
    word_counts = []
    # 1 = sarcastic , 0 = non-sarcastic
    observations = []
    
    # Read sarcastic 
    with open(sarcastic_corpus, "r") as o:
        line = o.readline()
        while (line):
            line = line.strip()
            test_data = line.strip()
            word_count = Counter(filter(None,line.split(" ")))
            word_counts.append(dict(word_count) )
            # 1 for sarcastic
            observations.append(1)
            line = o.readline()
        
        o.close()
    
    # Read non sarcastic
    with open(non_sarcastic_corpus, "r") as o:
        line = o.readline()
        
        while (line):
            line = line.strip()
            word_count = Counter(filter(None,line.split(" ")))
            word_counts.append(dict(word_count) )
            # 0 for non sarcastic
            observations.append(0)
            line = o.readline()
        
        o.close()
    
    # word_counts = [{'word4': 1,'word2': 1,},{'word1': 2,'word2': 2,},{'word3': 2,'word4': 2,},{'word3': 3,'word4': 3,} ]
    # observations = [1,1,1,0]
    # print word_counts
    # print observations
    vectorize = DictVectorizer()
    
    feature_vectorized = vectorize.fit_transform(word_counts)
    
    # # vector array  
    features_arr = feature_vectorized.toarray()
    # print features_arr[0]
    
    return features_arr, observations,vectorize.get_feature_names()




clf = svm.SVC()
# clf = SGDClassifier(loss="hinge", penalty="l2")

features_arr, observations, feature_names = getTrainingVectors() 
print clf.fit(features_arr, observations)

# This list of features is needed to create a vector for prediction  
# print vectorize.get_feature_names()

# test createPredictionVector 
test_vector = createPredictionVector(feature_names, test_data)

print clf.predict([test_vector])


    
    
    
    
