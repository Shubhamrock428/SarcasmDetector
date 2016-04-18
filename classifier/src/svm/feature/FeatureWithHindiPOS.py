from sklearn import svm
from sklearn.externals import joblib
from sklearn.feature_extraction import *

def getSVMVector(tagged_file):
    with open(tagged_file,"r") as f:
        content = f.readlines()
    count = 0
    tags = ['NN','PSP','VM','SYM','JJ','VAUX','NNP','XC','PRP','CC','RP','QC','NST','DEM','QF','NEG','RB','INTF','RDP','QO','WQ','INJ']
    vector=[]
    v = [0]*len(tags)
    print v
    for line in content:
        words = line.split()
        if len(words) < 2:
            if words[0]=='</s>':
                for i in range(0,len(tags)):
                    v[i]/=(count*1.0)
                    v[i]*=100
                vector.append(v)
                v = [0]*len(tags)
                count = 0
            continue
        actual_word = words[0]
        pos_tag = words[2]

        if pos_tag in tags:
            index = tags.index(pos_tag)
            v[index]+=1
        count+=1
    vector.append(v)

    return vector
print getSVMVector()

def main_fn() :
    sarcastic_corpus="../../../../process-tweet/sarcastic_proc.txt"
    non_sarcastic_corpus="../../../../process-tweet/nonsarcastic_proc.txt"
    test_corpus_sarcastic="../test.txt"
    test_corpus_nonsarcastic="../test.txt"

    sarcastic_corpus_output=""
    non_sarcastic_corpus_output=""
    test_corpus_sarcastic_output=""
    test_corpus_nonsarcastic_output=""

    sar_features_arr = getSVMVector(sarcastic_corpus_output)
    print sar_features_arr
    observations = [1] * len(sar_features_arr)

    non_features_arr = getSVMVector(non_sarcastic_corpus_output)
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
    test_vector_sarcastic = getSVMVector(test_corpus_sarcastic_output)
    test_vector_nonsarcastic= getSVMVector(test_corpus_nonsarcastic_output)
    print clf.predict(test_vector_sarcastic)
    print clf.predict(test_vector_nonsarcastic)

    #print vectors in files for F1

print __name__
if __name__ == "__main__":
    # stuff only to run when not called via 'import' here
    main_fn()
