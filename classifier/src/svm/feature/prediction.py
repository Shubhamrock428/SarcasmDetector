from word_feature import createPredictionVector
from sentiment_feature_with_count import getSVMVectorSentiCnt
from sentiment_feature_position import getSVMVectorSentiPos

from sklearn import svm
from sklearn.externals import joblib
from sklearn.feature_extraction import *

dev_corpus_sarcastic="../../../../process-tweet/dev_sarcastic_proc.txt"
dev_corpus_nonsarcastic="../../../../process-tweet/dev_nonsarcastic_proc.txt"


# BAG OF WORDS
clf_word = joblib.load( '../predict/word_feature/word_feature.pkl')
feature_names = joblib.load( '../predict/word_feature/feature_names.pkl')
 
test_vector_sarcastic = createPredictionVector(feature_names, dev_corpus_sarcastic)
test_vector_nonsarcastic = createPredictionVector(feature_names, dev_corpus_nonsarcastic)
  
v1 = clf_word.predict(test_vector_sarcastic)
v2 = clf_word.predict(test_vector_nonsarcastic)
print "writing tags_sarcastic_word, tags_nonsarcastic_word"
f = open("../../../../process-tweet/tags_sarcastic_word.txt","w")
for vect in v1:
    v=str(vect)
    f.write(v)
    f.write("\n")
f.close()
f = open("../../../../process-tweet/tags_nonsarcastic_word.txt","w")
for vect in v2:
    v=str(vect)
    f.write(v)
    f.write("\n")
f.close()


# SENTI CNT
# clf_senti_cnt = joblib.load( '../predict/senti_feature_cnt/senti_feature_cnt.pkl')
# print "predicting using SENTI CNT feature"
# test_vector_sarcastic = getSVMVectorSentiCnt( dev_corpus_sarcastic)
# test_vector_nonsarcastic = getSVMVectorSentiCnt( dev_corpus_nonsarcastic)
# 
# v1 = clf_senti_cnt.predict(test_vector_sarcastic)
# v2 = clf_senti_cnt.predict(test_vector_nonsarcastic)
# print "writing tags_sarcastic_senti_cnt, tags_nonsarcastic_senti_cnt"
# f = open("../../../../process-tweet/tags_sarcastic_senti_cnt.txt","w")
# for vect in v1:
#     v=str(vect)
#     f.write(v)
#     f.write("\n")
# f.close()
# f = open("../../../../process-tweet/tags_nonsarcastic_senti_cnt.txt","w")
# for vect in v2:
#     v=str(vect)
#     f.write(v)
#     f.write("\n")
# f.close()

# SENTI POS
# clf_senti_pos = joblib.load( '../predict/senti_feature_pos/senti_feature_pos.pkl')
# print "predicting using SENTI POS feature"
# test_vector_sarcastic = getSVMVectorSentiPos(dev_corpus_sarcastic)
# test_vector_nonsarcastic = getSVMVectorSentiPos( dev_corpus_nonsarcastic)
# 
# v1 = clf_senti_pos.predict(test_vector_sarcastic)
# v2 = clf_senti_pos.predict(test_vector_nonsarcastic)
# 
# print "writing tags_sarcastic_senti_pos, tags_nonsarcastic_senti_pos"
# 
# f = open("../../../../process-tweet/tags_sarcastic_senti_pos.txt","w")
# for vect in v1:
#     v=str(vect)
#     f.write(v)
#     f.write("\n")
# f.close()
# f = open("../../../../process-tweet/tags_nonsarcastic_senti_pos.txt","w")
# for vect in v2:
#     v=str(vect)
#     f.write(v)
#     f.write("\n")
# f.close()
