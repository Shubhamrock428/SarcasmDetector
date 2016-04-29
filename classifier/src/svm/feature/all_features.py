import sys,string,time
from collections import Counter
from word_feature import createPredictionVector,getTrainingVectors
from sentiment_feature_with_count import getSVMVectorSentiCnt
from sentiment_feature_position import getSVMVectorSentiPos
from sklearn import svm
from sklearn.feature_extraction import *
from sklearn.linear_model import *
from sklearn.externals import joblib
from nlputility import ngrams

'''l1=[[1,2,3],[4,5,6]]
l2=[[7,8],[9,10]]
l3=[[0],[0]]
l4=[[4],[5]]
for x in range(0,len(l1)):
	l1[x].extend(l2[x])
	l1[x].extend(l3[x])
	l3[x].extend(l4[x])
print l3
'''
corpus_sarcastic="../../../../process-tweet/sarcastic_proc.txt"
corpus_nonsarcastic="../../../../process-tweet/nonsarcastic_proc.txt"
dev_corpus_sarcastic="../../../../process-tweet/dev_sarcastic_proc.txt"
dev_corpus_nonsarcastic="../../../../process-tweet/dev_nonsarcastic_proc.txt"

start =  time.time()
clf = SGDClassifier(loss="hinge", penalty="l1")

#BAG OF WORDS
features_arr, observations, feature_names = getTrainingVectors(
  "../../../../process-tweet/sarcastic_proc.txt",
  "../../../../process-tweet/nonsarcastic_proc.txt")

print 'part1 done'

feature_arr=[]
#SENTIMENT COUNT len(senti_cnt_vector_sarcastic)
senti_cnt_vector_sarcastic = getSVMVectorSentiCnt(corpus_sarcastic)
senti_cnt_vector_nonsarcastic = getSVMVectorSentiCnt(corpus_nonsarcastic)
print 'part2 done'
#SENTIMENT POS
senti_pos_vector_sarcastic = getSVMVectorSentiPos(corpus_sarcastic)
senti_pos_vector_nonsarcastic = getSVMVectorSentiPos(corpus_nonsarcastic)
print 'part3 done'
#ADDING THEM TOGETHER
count=0
for x in range(0,len(senti_cnt_vector_sarcastic)):
	senti_cnt_vector_sarcastic[x].extend(senti_pos_vector_sarcastic[x])
	
for x in range(0,len(senti_cnt_vector_nonsarcastic)):
	senti_cnt_vector_nonsarcastic[x].extend(senti_pos_vector_nonsarcastic[x])
print 'part4 done'

print "Created feature vectors length observations {0} length of one vector {1}".format(len(observations),len(features_arr[0])),  


clf.fit(feature_arr, observations)
joblib.dump(clf, '../predict/all_features/all_feature.pkl')
joblib.dump(feature_names, '../predict/all_features/feature_names.pkl')
print "Dumped model. Time taken {0} secs".format((time.time() -start))
    