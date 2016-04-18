# coding=utf-8

import os,string,json,math,sys
from nbclassify import NBSentence
from sentiment_feature_position import getSVMVectorSentiPosAPP
from sentiment_feature_with_count import getSVMVectorSentiCntAPP
from word_feature import getSVMVectorBagWordsAPP 


JAVA_CLI = "java -cp ../../../../process-tweet/target/process-tweet-0.0.1-SNAPSHOT-jar-with-dependencies.jar InputPreprocessTweet '{0}' "

input_line = sys.argv[1]

print "Input provided - ", input_line

stemmed_op = os.popen(JAVA_CLI.format(input_line)).read()
if(stemmed_op):
    input_line = stemmed_op
    
print "Stemmed it to - ", stemmed_op

NBSentence(input_line)

# getSVMVectorBagWordsAPP(input_line)
getSVMVectorSentiCntAPP(input_line)
getSVMVectorSentiPosAPP(input_line)


