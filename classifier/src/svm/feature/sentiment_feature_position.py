import json, io, itertools
def flattenListOfLists(lst):
    result = []
    for sublist in lst:
        result.extend(sublist)
    return result
def chunkify(lst,n):
    return [ lst[i::n] for i in xrange(n) ]

def fillSameValue(lst,val):
    lst = [1 for i in range(0,len(lst))]

#sentiment Tagged File
with open("sentiment_model.txt","r") as f:
    classifier = json.load(f)



#getSVMVector
def getSVMVector(filename,classifier):
    #Input File
    with open(filename,"r") as f:
        content = f.readlines()
    vector={}
    for line in content:
        words = line.split()
        list = chunkify(range(100),len(words))
        for i in range(0,len(words)):
            if words[i] in classifier:
                value = int(classifier[words[i]])
            else :
                value = int(0)
            fillSameValue(list[i],value)
        vector.add(flattenListOfLists(list))
    return vector

filename=""
vector = getSVMVector(filename,classifier)



