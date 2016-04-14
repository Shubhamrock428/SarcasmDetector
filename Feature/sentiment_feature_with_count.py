import json,string,codecs
model={}

with codecs.open("sentiment_model.txt","r") as f:
	model = json.load(f)

def fileRead(file):
        
    filename=file
    with open(filename) as f:
    	content = f.readlines()
    return content


def tag(s):
	score=[]
	seq=''
	posCount=0
	negCount=0
	neuCount=0
	words=s.split()
	length=len(words)	
	for word in words:
		word = unicode(word, "utf-8")		
		if word in model:
			if model[word] == 1:
				posCount+=1
			elif model[word] == 0:
				neuCount+=1
			else:
				negCount+=1
		else:
			neuCount+=1
	score.append(float(posCount/length)*100)
	score.append(float(neuCount/length)*100)
	score.append(float(negCount/length)*100)		
	return score

content=fileRead('test.txt')
file = open("sentiment_feature_with_count", "w")
for s in content:
	score=tag(s)
	file.write(str(score)+'\n')
file.close()
	
	
	
