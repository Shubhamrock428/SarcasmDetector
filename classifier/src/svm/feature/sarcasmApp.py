# coding=utf-8

import os, string, json, math, sys
from nbclassify import NBSentence
from sentiment_feature_position import getSVMVectorSentiPosAPP
from sentiment_feature_with_count import getSVMVectorSentiCntAPP
from word_feature import getSVMVectorBagWordsAPP 


JAVA_CLI_PREPROCESS = "java -cp ../../../../process-tweet/target/process-tweet-0.0.1-SNAPSHOT-jar-with-dependencies.jar InputPreprocessTweet '{0}' "


def run_all_features(input_line): 
    output = []
    output.append("Input provided - " + input_line)
    
    stemmed_op = os.popen(JAVA_CLI_PREPROCESS.format(input_line)).read()
    if(stemmed_op):
        input_line = stemmed_op
        
    output.append("Stemmed it to - {0}".format(stemmed_op))
    
    output.append(NBSentence(input_line))
    
    output.append(getSVMVectorBagWordsAPP(input_line))
    output.append(getSVMVectorSentiCntAPP(input_line))
    output.append(getSVMVectorSentiPosAPP(input_line))
    
    return output


if __name__ == "__main__":
    # stuff only to run when not called via 'import' here
    print "\n".join( run_all_features(sys.argv[1]) ) 
