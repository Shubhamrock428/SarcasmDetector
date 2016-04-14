import json,string,codecs
model={}

with codecs.open("sentiment_json.txt","r","utf-8") as f:
	model = json.load(f)

def fileRead(file):
        
    filename=file
    with open(filename) as f:
    	content = f.readlines()
    return content

def check(s):
	score=[]
	words=s.split()
	for word in words:
		word = unicode(word, "utf-8")		
		if word in model:
			scores=model[word]
			pscore=scores[0]
			nscore=scores[1]
			check=abs(pscore-nscore)
			if check>=0.1:	#can change
				if pscore>nscore:
					word=word+'/pos'
				else:
					word=word+'/neg'
				print word	
			else:
				word=word+'/neu'		
				print word		    
	return s

content=fileRead('test.txt')

#print content
for s in content:
	check(s)
	
	
