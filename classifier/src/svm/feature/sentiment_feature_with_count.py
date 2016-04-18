import json,string,codecs

from sklearn import svm
from sklearn.externals import joblib
from sklearn.feature_extraction import *

model={}

with codecs.open("sentiment_model.txt","r") as f:
	model = json.load(f)

def fileRead(file):
        
    filename=file
    with open(filename) as f:
    	content = f.readlines()
    return content


def tag(s):
	score=[]
	seq=''
	posCount=0
	negCount=0
	neuCount=0
	words=s.split()
	length=len(words)	
	for word in words:
		word = unicode(word, "utf-8")		
		if word in model:
			if model[word] == 1:
				#print 'inside: ',word
				posCount+=1
			elif model[word] == 0:
				neuCount+=1
			else:
				negCount+=1
		else:
			neuCount+=1
	score.append(float(1.0*posCount/length)*100)
	score.append(float(1.0*neuCount/length)*100)
	score.append(float(1.0*negCount/length)*100)		
	return score

def getSVMVectorSentiCnt(fileName):
	#content=fileRead('/home/swanand/nlpProject/Feature/data/nonsarcastic_proc.txt')
	content=fileRead(fileName)	
	#file = open('/home/swanand/nlpProject/Feature/data/outputs/vector_nonsarcastic_proc.txt', "w")
	featureVecor=[]
	for s in content:
		score=tag(s)
		featureVecor.append(score)
	return featureVecor

def main_fn():
	sarcastic_corpus="../../../../process-tweet/sarcastic_proc.txt"
	non_sarcastic_corpus="../../../../process-tweet/nonsarcastic_proc.txt"
	test_corpus_sarcastic="../test.txt"
	test_corpus_nonsarcastic="../test.txt"
	
	sar_features_arr = getSVMVectorSentiCnt(sarcastic_corpus)
	print len(sar_features_arr)
	observations = [1] * len(sar_features_arr)
	
	non_features_arr = getSVMVectorSentiCnt(non_sarcastic_corpus)
	observations += [0] * len(non_features_arr)
	
	print len(sar_features_arr) + len(non_features_arr) 
	print len(observations)
	
	
	
	clf = svm.SVC()
	# clf = SGDClassifier(loss="hinge", penalty="l2")
	
	 
	clf.fit(sar_features_arr + non_features_arr, observations)
	
	joblib.dump(clf, '../predict/senti_feature_cnt/senti_feature_cnt.pkl')
	
	# print s
	# This list of features is needed to create a vector for prediction  
	# print vectorize.get_feature_names()
	
	# test createPredictionVector 
	test_vector_sarcastic = getSVMVectorSentiCnt(test_corpus_sarcastic)
	test_vector_nonsarcastic= getSVMVectorSentiCnt(test_corpus_nonsarcastic)
	print clf.predict(test_vector_sarcastic)
	print clf.predict(test_vector_nonsarcastic)
	
	#print vectors in files for F1
	
		
print __name__
if __name__ == "__main__":
    # stuff only to run when not called via 'import' here
    main_fn() 