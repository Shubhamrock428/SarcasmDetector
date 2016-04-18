import string,pickle,math,sys
content_test=[]
content_op=[]

def readFile(file):
        
    filename=file
    with open(filename) as f:
    	content = f.readlines()
    return content


content_sarcastic=readFile("../../../process-tweet/tags_sarcastic_word.txt")
content_nonsarcastic=readFile("../../../process-tweet/tags_nonsarcastic_word.txt")
tp=0
tn=0
fp=0
fn=0
def calculateF1(content,flag):
	global tp
	global tn
	global fp
	global fn
	count=0 
	while count!=len(content):
		if flag==1:
			if content_sarcastic[count]=='0\n':
				fp+=1
			else:
				tp+=1
		else:
			if content_nonsarcastic[count]=='0\n':
				tn+=1
			else:
				fn+=1
		count+=1			
	return
calculateF1(content_sarcastic,1)
calculateF1(content_nonsarcastic,0)
p=1.0*tp/(tp+fp)
r=1.0*tp/(tp+tn)
f=2.0*p*r/(p+r)
print 'Precision: '+str(p)+' Recall: '+str(r)
print 'F1: ',str(f)



