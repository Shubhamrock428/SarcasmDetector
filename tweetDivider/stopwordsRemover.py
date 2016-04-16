import os
import codecs
from __builtin__ import str

stopwords=[]
with codecs.open("/Users/sidhesh/Documents/Github/Team-MissionNLP/process-tweet/stopwords_hi.txt", "r","utf-8") as sourceFile:      
    stopwords=sourceFile.readlines()
sourceFile.close()

stopwords=[]
with codecs.open("/Users/sidhesh/Documents/Github/Team-MissionNLP/process-tweet/ranknl.txt", "r","utf-8") as sourceFile:      
    lines=sourceFile.readlines()
    for line in lines:
        words = line.split()
        for word in words:
            if word not in stopwords:
                stopwords.append(word)
sourceFile.close()

f1 = codecs.open("/Users/sidhesh/Documents/Github/Team-MissionNLP/process-tweet/sarcastic_proc1.txt", "w+", "utf-8")
with codecs.open("/Users/sidhesh/Documents/Github/Team-MissionNLP/process-tweet/sarcastic_proc.txt", "r","utf-8") as sourceFile:      
    lines=sourceFile.readlines()
    for line in lines:
        str=''
        words = line.split()
        for word in words:
            if word not in stopwords:
                str+= word + " "
            else:
                print word
        f1.write(str+'\n')
sourceFile.close()
f1.close()
    

            


        