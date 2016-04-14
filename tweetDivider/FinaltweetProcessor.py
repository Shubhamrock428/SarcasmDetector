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
    os.remove(oldpath)
    
processfinally("/Users/sidhesh/Documents/workspace/process-tweet/sarcastic_temp.txt", "/Users/sidhesh/Documents/workspace/process-tweet/sarcastic_proc.txt")
processfinally("/Users/sidhesh/Documents/workspace/process-tweet/nonsarcastic_temp.txt", "/Users/sidhesh/Documents/workspace/process-tweet/nonsarcastic_proc.txt")
processfinally("/Users/sidhesh/Documents/workspace/process-tweet/dev_temp.txt", "/Users/sidhesh/Documents/workspace/process-tweet/dev_proc.txt")