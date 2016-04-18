tagged_file = "hindioutput.txt"

with open(tagged_file,"r") as f:
    content = f.readlines()


def getSVMVectorPOS():
    tags = ['NN','PSP','VM','SYM','JJ','VAUX','NNP','XC','PRP','CC','RP','QC','NST','DEM','QF','NEG','RB','INTF','RDP','QO','WQ','INJ']
    vector=[]
    v = [0]*len(tags)
    print v
    for line in content:

        words = line.split()
        if len(words) < 2:
            if words[0]=='</s>':
                vector.append(v)
                v = [0]*len(tags)
            continue
        actual_word = words[0]
        pos_tag = words[2]

        if pos_tag in tags:
            index = tags.index(pos_tag)
            v[index]+=1
    vector.append(v)
    return vector

print getSVMVectorPOS()




