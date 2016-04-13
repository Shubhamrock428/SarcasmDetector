import os,string,json,codecs

vocab=set()
sarcasmDict={}
nonSarcasmDict={}
content=[]


'''def createStopwords():
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

def fileRead(file):
        
    filename=file
    with open(filename) as f:
    	content = f.readlines()
    return content
sarcasm=0
nonSarcasm=0
    
def trainNB(content,classFlag):
    global sarcasm
    global nonSarcasm
    exclude=set(string.punctuation)
    for s in content:	
	s = ''.join(ch for ch in s if ch not in exclude)
    	tweet=s.split()
	for word in tweet:
		vocab.add(word)
                if classFlag==1:
                	sarcasm+=1
                        if word in sarcasmDict:
                                sarcasmDict[word]=sarcasmDict[word]+1
                        else:
                                sarcasmDict[word]=1
                else:
                        nonSarcasm+=1
                        if word in nonSarcasmDict:
                                 nonSarcasmDict[word]=nonSarcasmDict[word]+1
                        else:
                                 nonSarcasmDict[word]=1
    return
    
def writeModel():
    global sarcasm
    global nonSarcasm
    vocabList=list(vocab)
    model={}
    for word in vocab:
        classList=[]
        if word in sarcasmDict:
            prob=1.0*(sarcasmDict[word]+1)/(sarcasm+len(vocab))
        else:
            prob=1.0/(sarcasm+len(vocab))
        classList.append(prob)
        if word in nonSarcasmDict:
            prob=1.0*(nonSarcasmDict[word]+1)/(nonSarcasm+len(vocab))
	else:
            prob=1.0/(nonSarcasm+len(vocab))
	classList.append(prob)        
	model[word]=classList
    print model    
    with codecs.open('nbmodel.txt','w',encoding='utf8') as handle:
      	data={'MODEL':model}
	json.dump(data, handle)

    return

content=fileRead('/home/swanand/nlpProject/train1.txt')
trainNB(content,1)
fileName='/home/swanand/nlpProject/nonSarcasticTrain.txt'
content=fileRead(fileName)
print str(len(vocab))
print str(sarcasm)
trainNB(content,0)
print str(nonSarcasm)
writeModel()

