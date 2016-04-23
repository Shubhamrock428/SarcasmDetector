import os,string,json,codecs

vocab=set()
sarcasmDict={}
nonSarcasmDict={}
content=[]

vocabB=set()
sarcasmDictB={}
nonSarcasmDictB={}

vocabT=set()
sarcasmDictT={}
nonSarcasmDictT={}

def fileRead(file):
        
    filename=file
    with open(filename) as f:
    	content = f.readlines()
    return content
sarcasm=0
nonSarcasm=0
sarcasmB=0
nonSarcasmB=0
sarcasmT=0
nonSarcasmT=0
    
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

def trainBigramNB(content,classFlag):
    global sarcasmB
    global nonSarcasmB
    exclude=set(string.punctuation)
    for s in content:	
	s = ''.join(ch for ch in s if ch not in exclude)
    	tweet=s.split()
	for index in range (0,len(tweet)):
		if index==0:
			word='q0,'+tweet[index]
		else:
			word=tweet[index-1]+','+tweet[index]
		vocabB.add(word)
                if classFlag==1:
                	sarcasmB+=1
                        if word in sarcasmDictB:
                                sarcasmDictB[word]=sarcasmDictB[word]+1
                        else:
                                sarcasmDictB[word]=1
                else:
                        nonSarcasmB+=1
                        if word in nonSarcasmDictB:
                                 nonSarcasmDictB[word]=nonSarcasmDictB[word]+1
                        else:
                                 nonSarcasmDictB[word]=1
    return

def trainTrigramNB(content,classFlag):
    global sarcasmT
    global nonSarcasmT
    exclude=set(string.punctuation)
    for s in content:	
	s = ''.join(ch for ch in s if ch not in exclude)
    	tweet=s.split()
	for index in range (2,len(tweet)):
		word=tweet[index-2]+','+tweet[index-1]+','+tweet[index]
		vocabT.add(word)
                if classFlag==1:
                	sarcasmT+=1
                        if word in sarcasmDictT:
                                sarcasmDictT[word]=sarcasmDictT[word]+1
                        else:
                                sarcasmDictT[word]=1
                else:
                        nonSarcasmT+=1
                        if word in nonSarcasmDictT:
                                 nonSarcasmDictT[word]=nonSarcasmDictT[word]+1
                        else:
                                 nonSarcasmDictT[word]=1
    return
    
def writeModel(sarcasm,nonSarcasm,vocab,sarcasmDict,nonSarcasmDict,flag):
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
    #print model
    if flag==1:
	fwrite='nbmodel.txt'
    elif flag==0:
	fwrite='nbmodelBigram.txt'
    else:
	fwrite='nbmodelTrigram.txt'    
    with codecs.open(fwrite,'w',encoding='utf8') as handle:
	s1=len(sarcasmDict)
	s2=len(nonSarcasmDict)
	data={'MODEL':model,'SARCASM_LENGTH':s1,'NONSARCASM_LENGTH':s2}
	json.dump(data, handle)

    return

content=fileRead('/home/swanand/nlpProject/Naive Bayes/data/nonsarcastic_proc.txt')
trainNB(content,0)
trainBigramNB(content,0)
trainTrigramNB(content,0)
content=fileRead('/home/swanand/nlpProject/Naive Bayes/data/sarcastic_proc.txt')
trainNB(content,1)
trainBigramNB(content,1)
trainTrigramNB(content,1)
print 'Vocab Length:'+ str(len(vocab))
print 'Sarcasm Vocab Length:' +str(len(sarcasmDict))
print 'Non Sarcasm Length:' +str(len(nonSarcasmDict))
print str(sarcasm)
print str(nonSarcasm)
print 'Bigram Vocab Length:'+ str(len(vocabB))
print 'Bigram Sarcasm Vocab Length:' +str(len(sarcasmDictB))
print 'Bigram Non Sarcasm Length:' +str(len(nonSarcasmDictB))
print str(sarcasmB)
print str(nonSarcasmB)

print 'Trigram Vocab Length:'+ str(len(vocabT))
print 'Trigram Sarcasm Vocab Length:' +str(len(sarcasmDictT))
print 'Trigram Non Sarcasm Length:' +str(len(nonSarcasmDictT))
print str(sarcasmT)
print str(nonSarcasmT)

writeModel(sarcasm,nonSarcasm,vocab,sarcasmDict,nonSarcasmDict,1)
writeModel(sarcasmB,nonSarcasmB,vocabB,sarcasmDictB,nonSarcasmDictB,0)
writeModel(sarcasmT,nonSarcasmT,vocabT,sarcasmDictT,nonSarcasmDictT,2)
