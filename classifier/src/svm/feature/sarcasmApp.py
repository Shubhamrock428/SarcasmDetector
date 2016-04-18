import os,string,json,math,sys
from nbclassify import NBSentence
from sentiment_feature_position import getSVMVectorSentiPosAPP
from sentiment_feature_with_count import getSVMVectorSentiCntAPP
from word_feature import getSVMVectorBagWordsAPP 



NBSentence(sys.argv[1])

# getSVMVectorBagWordsAPP(sys.argv[1])
getSVMVectorSentiCntAPP(sys.argv[1])
getSVMVectorSentiPosAPP(sys.argv[1])


