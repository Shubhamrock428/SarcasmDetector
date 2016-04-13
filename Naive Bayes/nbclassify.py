import os,string,json,math,sys

stopwords=[]
vocab=set()
'''
def createStopwords():
    with open("stopwords.txt","r") as stopfile:
        stopwords= stopfile.readlines(1)
    stopwords=[x.strip('\n') for x in stopwords]
    return stopwords

def readFile(root,file):
        
    filename=root+'\\'+file
    inp=open(filename,"r")
    s=inp.readline()
    exclude=set(string.punctuation)
    s = ''.join(ch for ch in s if ch not in exclude)
    s = s.lower()
    s = ''.join(i for i in s if not i.isdigit()) 
    stopwords=createStopwords()
    s = ' '.join([word for word in s.split() if word not in stopwords])
    inp.close()
    return s.split()


'''
def readModel():
    with open('nbmodel.txt', 'rb') as handle:
        data = json.loads(handle.read())
    return data

def fileRead(file):
        
    filename=file
    with open(filename) as f:
    	content = f.readlines()
    return content

def NBtest(content):
    output= open("nboutput.txt","w")
    score1=score2=0
    for s in content:
	output.write(s)
	tweet=s.split()
	for word in tweet:
		word = unicode(word, "utf-8")		
		if word in model:
			print 'found: ',word
        		score1+=math.log(model[word][0])
                        score2+=math.log(model[word][1])
        if score1> score2:
		print s,'SARCASTIC'
        	output.write('/SARCASTIC')
        else:
		print 'NON_SARCASTIC'
    		output.write('/NON_SARCASTIC')
        output.write('\n')
    output.close()
    return 

content=fileRead('/home/swanand/nlpProject/test.txt')
data=readModel()
model=data['MODEL']
NBtest(content)
