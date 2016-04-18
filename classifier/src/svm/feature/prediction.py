from word_feature import createPredictionVector

from sklearn import svm
from sklearn.externals import joblib
from sklearn.feature_extraction import *

dev_corpus_sarcastic="../test.txt"
dev_corpus_nonsarcastic="../test.txt"

clf_word = joblib.load( '../predict/word_feature/word_feature.pkl')
feature_names = joblib.load( '../predict/word_feature/feature_names.pkl')

test_vector_sarcastic = createPredictionVector(feature_names, dev_corpus_sarcastic)
test_vector_nonsarcastic = createPredictionVector(feature_names, dev_corpus_nonsarcastic)
 
print clf_word.predict(test_vector_sarcastic)
print clf_word.predict(test_vector_nonsarcastic)


# clf_senti_cnt = joblib.load( '../predict/word_feature/word_feature.pkl')
# clf_senti_pos = joblib.load( '../predict/word_feature/word_feature.pkl')