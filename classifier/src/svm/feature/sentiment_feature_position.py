import json

from sklearn import svm
from sklearn.externals import joblib
from sklearn.feature_extraction import *


def flattenListOfLists(lst):
    result = []
    for sublist in lst:
        result.extend(sublist)
    return result
def chunkify(lst,n):
    return [ lst[i::n] for i in xrange(n) ]

def fillSameValue(lst,val):
    lst = [val for i in range(0,len(lst))]
    return lst

#sentiment Tagged File
classifier = {}
with open("sentiment_model.txt","r") as f:
    classifier = json.load(f)

#getSVMVectorSentiPos
def getSVMVectorSentiPos(filename):
    global classifier
    #Input File
    with open(filename,"r") as f:
        content = f.readlines()
    vector=[]
    for line in content:
        words = line.split()
        list = chunkify(range(100),len(words))
        for i in range(0,len(words)):
            s=unicode(words[i],"utf-8")
            if s in classifier:
                value = classifier[s]
            else :
                value = 0
            list[i]=fillSameValue(list[i],value)
        vector.append(flattenListOfLists(list))
    return vector

def getSVMVectorSentiPosAPP(line):
    global classifier
    print line
    vector=[]
    words = line.split()
    list = chunkify(range(100),len(words))
    for i in range(0,len(words)):
    	s=unicode(words[i],"utf-8")
    	if s in classifier:
   		value = classifier[s]
    	else :
    		value = 0
        list[i]=fillSameValue(list[i],value)
    vector.append(flattenListOfLists(list))
    clf_senti_pos = joblib.load( '../predict/senti_feature_pos/senti_feature_pos.pkl')
    v1 = clf_senti_pos.predict(vector)
    for vect in v1:
     v=str(vect)
     if v=='0':
	print 'SVM Feature sentiment with position says: Non Sarcastic' 
     else:
	print 'SVM Feature sentiment with position says: Sarcastic' 
	

def main_fn() :
    sarcastic_corpus="../../../../process-tweet/sarcastic_proc.txt"
    non_sarcastic_corpus="../../../../process-tweet/nonsarcastic_proc.txt"
    test_corpus_sarcastic="../test.txt"
    test_corpus_nonsarcastic="../test.txt"
    
    sar_features_arr = getSVMVectorSentiPos(sarcastic_corpus)
    print sar_features_arr
    observations = [1] * len(sar_features_arr)
    
    non_features_arr = getSVMVectorSentiPos(non_sarcastic_corpus)
    observations += [0] * len(non_features_arr)
    
    print len(sar_features_arr) + len(non_features_arr) 
    print len(observations)
    
    clf = svm.SVC()
    # clf = SGDClassifier(loss="hinge", penalty="l2")
     
    clf.fit(sar_features_arr + non_features_arr, observations)
    
    print joblib.dump(clf, '../predict/senti_feature_pos/senti_feature_pos.pkl')
    
    print "dumped senti_feature_pos model"
    # print s
    # This list of features is needed to create a vector for prediction  
    # print vectorize.get_feature_names()
    
    # test createPredictionVector 
    test_vector_sarcastic = getSVMVectorSentiPos(test_corpus_sarcastic)
    test_vector_nonsarcastic= getSVMVectorSentiPos(test_corpus_nonsarcastic)
    print clf.predict(test_vector_sarcastic)
    print clf.predict(test_vector_nonsarcastic)
    
    #print vectors in files for F1

print __name__
if __name__ == "__main__":
    # stuff only to run when not called via 'import' here
    main_fn() 
