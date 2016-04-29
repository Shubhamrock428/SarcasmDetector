import os,string,json,math,sys

stopwords=[]
vocab=set()

    
def readModel():
    with open('nbmodel.txt', 'rb') as handle:
        data = json.loads(handle.read())
    return data

def fileRead(file):
        
    filename=file
    with open(filename) as f:
    	content = f.readlines()
    return content

def NBtest(content,f1):
    output= open(f1,"w")
    score1=math.log(0.44)
    score2=math.log(0.56)
    for s in content:
        score1=math.log(0.44)
        score2=math.log(0.56)
        tweet=s.split()
        for word in tweet:
            word = unicode(word, "utf-8")		
            if word in model:
                score1+=math.log(model[word][0])
                score2+=math.log(model[word][1])
            else:
                score1+=math.log(1.0/sarcasm_count)
                score2+=math.log(1.0/nonsarcasm_count)
        if score1> score2:
            output.write('1')
        else:
            output.write('0')
        output.write('\n')
    output.close()
    return 

data=readModel()
model=data['MODEL']
sarcasm_count=data['SARCASM_LENGTH']
nonsarcasm_count=data['NONSARCASM_LENGTH']
# print sarcasm_count
# print nonsarcasm_count

def main_fn(): 
    content=fileRead("../../../../process-tweet/dev_sarcastic_proc.txt")
    f1="../../../../process-tweet/tags_sarcastic_nb.txt"
    NBtest(content,f1)
    content=fileRead("../../../../process-tweet/dev_nonsarcastic_proc.txt")
    f1="../../../../process-tweet/tags_nonsarcastic_nb.txt"
    NBtest(content,f1)
    

def NBSentence(sentence):
	score1=math.log(0.44)
	score2=math.log(0.56)
    	tweet=sentence.split()
	c=0
	for word in tweet:
		word = unicode(word, "utf-8")		
		if word in model:
			score1+=math.log(model[word][0])
                        score2+=math.log(model[word][1])
		else:
			score1+=math.log(1.0/sarcasm_count)
			score2+=math.log(1.0/nonsarcasm_count)
        if score1> score2:
		return 'Naive Bayes says: Sarcastic'
        else:
		return 'Naive Bayes says: Non Sarcastic'

	
if __name__ == "__main__":
    # stuff only to run when not called via 'import' here
    main_fn() 
