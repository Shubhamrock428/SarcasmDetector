import codecs
import os
count=0
f1 = codecs.open("/Users/sidhesh/Documents/Github/Team-MissionNLP/process-tweet/sarcastic_proc.txt", "w+", "utf-8")
f2 = codecs.open("/Users/sidhesh/Documents/Github/Team-MissionNLP/process-tweet/dev_sarcastic_proc.txt", "w+", "utf-8")
with codecs.open("/Users/sidhesh/Documents/Github/Team-MissionNLP/process-tweet/sarcastic_temp2.txt", "r","utf-8") as sourceFile:      
        lines=sourceFile.readlines()
        for line in lines:
            if count < 5661:
                f1.write(line)
                count+=1
            else:
                f2.write(line)
        f1.close()
        f2.close()               
sourceFile.close()
count=0
f1 = codecs.open("/Users/sidhesh/Documents/Github/Team-MissionNLP/process-tweet/nonsarcastic_proc.txt", "w+", "utf-8")
f2 = codecs.open("/Users/sidhesh/Documents/Github/Team-MissionNLP/process-tweet/dev_nonsarcastic_proc.txt", "w+", "utf-8")
with codecs.open("/Users/sidhesh/Documents/Github/Team-MissionNLP/process-tweet/nonsarcastic_temp2.txt", "r","utf-8") as sourceFile:      
        lines=sourceFile.readlines()
        for line in lines:
            if count < 5661:
                f1.write(line)
                count+=1
            else:
                f2.write(line)
        f1.close()
        f2.close()               
sourceFile.close()

os.remove("/Users/sidhesh/Documents/Github/Team-MissionNLP/process-tweet/sarcastic_temp2.txt")
os.remove("/Users/sidhesh/Documents/Github/Team-MissionNLP/process-tweet/nonsarcastic_temp2.txt")
