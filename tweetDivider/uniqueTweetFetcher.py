import os,string,json,codecs

def fileprocess(path,outputpath):     
    with open(path) as f:
        content = f.readlines()
        checkList=[]
        output= codecs.open(outputpath,'w',encoding='utf8')
        for s in content:
            s=unicode(s,"utf-8")
            if s not in checkList:
                output.write(s)    
                checkList.append(s)
        output.close()
    f.close()
#fileprocess("/Users/sidhesh/Documents/Github/Team-MissionNLP/process-tweet/sarcastic_temp1.txt","/Users/sidhesh/Documents/Github/Team-MissionNLP/process-tweet/sarcastic_temp2.txt")
#fileprocess("/Users/sidhesh/Documents/Github/Team-MissionNLP/process-tweet/nonsarcastic_temp1.txt","/Users/sidhesh/Documents/Github/Team-MissionNLP/process-tweet/nonsarcastic_temp2.txt")
fileprocess("/Users/sidhesh/Documents/Github/Team-MissionNLP/process-tweet/newenglishsarcastic_temp.txt","/Users/sidhesh/Documents/Github/Team-MissionNLP/process-tweet/newenglishsarcastic1.txt")
#os.remove("/Users/sidhesh/Documents/Github/Team-MissionNLP/process-tweet/sarcastic_temp1.txt")
#os.remove("/Users/sidhesh/Documents/Github/Team-MissionNLP/process-tweet/nonsarcastic_temp1.txt")