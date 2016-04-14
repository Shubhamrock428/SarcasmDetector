import json,string,io,codecs
model={}

with io.open("HSWN_WN.txt",encoding="utf-8") as f:
	content = f.readlines()

for line in content:
	words = line.split()
	pscore=float(words[2])
	nscore=float(words[3])
	synonyms=words[4].split(',')
	#print synonyms
	for eachWord in synonyms:
		if eachWord not in model:
			model[eachWord]=[pscore,nscore]

with codecs.open("sentiment_json.txt","w","utf-8") as f:
	json.dump(model,f)


