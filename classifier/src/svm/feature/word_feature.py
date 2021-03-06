from collections import Counter

from sklearn import svm
from sklearn.feature_extraction import *
from sklearn.linear_model import *
from sklearn.externals import joblib
from nlputility import ngrams
import time 
  
GRAM_SIZE = 1

def createPredictionVector(feature_names, test_file):
    print "Reading from " , test_file
    vector_arr = []
    with open(test_file, "r") as f:
        test_data = f.readline()
        while test_data:
            test_data = test_data.strip()
            vector = [0] * len(feature_names)
            for word in ngrams(test_data, GRAM_SIZE):
                if word in feature_names:
                    vector[feature_names.index(word)]+=1
            vector_arr.append(vector)
            test_data = f.readline()
#         print vector_arr
        return vector_arr
try:
    clf_word = joblib.load( '../predict/word_feature/word_feature.pkl')
    feature_names = joblib.load( '../predict/word_feature/feature_names.pkl')
except:
    pass
        
def getSVMVectorBagWordsAPP(line):
    global clf_word,feature_names
    if not (clf_word and feature_names):
        clf_word = joblib.load( '../predict/word_feature/word_feature.pkl')
        feature_names = joblib.load( '../predict/word_feature/feature_names.pkl')

    vector = [0] * len(feature_names)
    for word in ngrams(line, GRAM_SIZE):
        if word in feature_names:
            vector[feature_names.index(word)]+=1

    v1 = clf_word.predict([vector])
    for vect in v1:
        v=str(vect)
        if v=='0':
            return 'SVM Bag of words says: Non Sarcastic' 
        else:
            return 'SVM Bag of words says: Sarcastic'


def getTrainingVectors (sarcastic_corpus="../sarcastic.txt", non_sarcastic_corpus="../non_sarcastic.txt"):
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
            word_count = Counter(filter(None,ngrams(line, GRAM_SIZE)))
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
            word_count = Counter(filter(None,ngrams(line, GRAM_SIZE)))
            word_counts.append(dict(word_count) )
            # 0 for non sarcastic
            observations.append(0)
            line = o.readline()
        
        o.close()
    
    # word_counts = [{'word4': 1,'word2': 1,},{'word1': 2,'word2': 2,},{'word3': 2,'word4': 2,},{'word3': 3,'word4': 3,} ]
    # observations = [1,1,1,0]
    # print word_counts
    #print observations
    vectorize = DictVectorizer()
    
    feature_vectorized = vectorize.fit_transform(word_counts)
    
    # # vector array  
    features_arr = feature_vectorized.toarray()
    #feature_arr=features_arr.tolist()
    #print features_arr[0]
    
    return features_arr, observations,vectorize.get_feature_names()


def main_fn():
    start =  time.time()
#     clf = svm.SVC()
    clf = SGDClassifier(loss="hinge", penalty="l1")
    
    features_arr, observations, feature_names = getTrainingVectors(
      "../../../../process-tweet/sarcastic_proc.txt",
      "../../../../process-tweet/nonsarcastic_proc.txt")

    print "Created feature vectors length observations {0} length of one vector {1}".format(len(observations),len(features_arr[0])),  
    clf.fit(features_arr, observations)
    
    print joblib.dump(clf, '../predict/word_feature/word_feature.pkl')
    print joblib.dump(feature_names, '../predict/word_feature/feature_names.pkl')
    
    print "Dumped model. Time taken {0} secs".format((time.time() -start))
    
    # print s
    # This list of features is needed to create a vector for prediction  
    # print vectorize.get_feature_names()
    
    # test createPredictionVector 
#     test_vector_sarcastic = createPredictionVector(feature_names, test_data_sarcastic)
#     test_vector_nonsarcastic = createPredictionVector(feature_names, test_data_nonsarcastic)
#     
#     print clf.predict([test_vector_sarcastic])
#     print clf.predict([test_vector_nonsarcastic])
    
    #print these vectors in files for F1
        
    
if __name__ == "__main__":
    # stuff only to run when not called via 'import' here
    main_fn() 
