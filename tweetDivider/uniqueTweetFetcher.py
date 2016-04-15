import os,string,json,codecs

def fileRead(file):
        
    filename=file
    with open(filename) as f:
    	content = f.readlines()
    return content

content=fileRead('/home/swanand/nlpProject/remove repet/nonsarcastic_proc.txt')
checkList=[]
output= codecs.open('/home/swanand/nlpProject/remove repet/OP_nonsarcastic_proc.txt','w',encoding='utf8')
for s in content:
	s=unicode(s,"utf-8")
	if s not in checkList:
		output.write(s)	
		checkList.append(s)
output.close()
