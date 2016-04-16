import os

def processfinally(oldpath,newpath):
    f=open(oldpath,"r")
    f1=open(newpath,"w")
    lines=f.readlines()
    for line in lines:
        line = line.strip()
        if line!='':
            line+='\n'
            f1.write(line) 
    f.close()
    f1.close()
    os.remove(oldpath)
    
processfinally("/Users/sidhesh/Documents/workspace/process-tweet/sarcastic_temp.txt", "/Users/sidhesh/Documents/workspace/process-tweet/sarcastic_temp1.txt")
processfinally("/Users/sidhesh/Documents/workspace/process-tweet/nonsarcastic_temp.txt", "/Users/sidhesh/Documents/workspace/process-tweet/nonsarcastic_temp1.txt")


