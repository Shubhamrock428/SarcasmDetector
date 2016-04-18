from word_feature import createPredictionVector
from sentiment_feature_with_count import getSVMVectorSentiCnt

from sklearn import svm
from sklearn.externals import joblib
from sklearn.feature_extraction import *

dev_corpus_sarcastic="/Users/sidhesh/Documents/Github/Team-MissionNLP/process-tweet/dev_sarcastic_proc.txt"
dev_corpus_nonsarcastic="/Users/sidhesh/Documents/Github/Team-MissionNLP/process-tweet/dev_nonsarcastic_proc.txt"


# BAG OF WORDS
# clf_word = joblib.load( '../predict/word_feature/word_feature.pkl')
# feature_names = joblib.load( '../predict/word_feature/feature_names.pkl')
# 
# test_vector_sarcastic = createPredictionVector(feature_names, dev_corpus_sarcastic)
# test_vector_nonsarcastic = createPredictionVector(feature_names, dev_corpus_nonsarcastic)
#  
# print clf_word.predict(test_vector_sarcastic)
# print clf_word.predict(test_vector_nonsarcastic)


# SENTI CNT
clf_senti_cnt = joblib.load( '../predict/senti_feature_cnt/senti_feature_cnt.pkl')
test_vector_sarcastic = getSVMVectorSentiCnt( dev_corpus_sarcastic)
test_vector_nonsarcastic = getSVMVectorSentiCnt( dev_corpus_nonsarcastic)
f = open("/Users/sidhesh/Documents/Github/Team-MissionNLP/process-tweet/tags_sarcastic.txt","w")

v1= clf_senti_cnt.predict(test_vector_sarcastic)
v2= clf_senti_cnt.predict(test_vector_nonsarcastic)

for vect in v1:
    v=str(vect)
    f.write(v)
    f.write("\n")
f.close()
f = open("/Users/sidhesh/Documents/Github/Team-MissionNLP/process-tweet/tags_nonsarcastic.txt","w")
for vect in v2:
    v=str(vect)
    f.write(v)
    f.write("\n")
f.close()
# SENTI POS
# clf_senti_pos = joblib.load( '../predict/word_feature/word_feature.pkl')

