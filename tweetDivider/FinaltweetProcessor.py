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
    
processfinally("/Users/sidhesh/Documents/workspace/process-tweet/sarcastic_temp.txt", "/Users/sidhesh/Documents/workspace/process-tweet/sarcastic_proc.txt")
processfinally("/Users/sidhesh/Documents/workspace/process-tweet/nonsarcastic_temp.txt", "/Users/sidhesh/Documents/workspace/process-tweet/nonsarcastic_proc.txt")

f=open("/Users/sidhesh/Documents/workspace/process-tweet/dev_temp.txt","r")
f1=open("/Users/sidhesh/Documents/workspace/process-tweet/dev_proc.txt","w")
f2=open("/Users/sidhesh/Documents/workspace/process-tweet/dev_tag.txt","w")
lines=f.readlines()
count=0
for line in lines:
    count+=1
    line = line.strip()
    if line!='':
        line+='\n'
        f1.write(line)
        if count<5000:
            f2.write("0\n") 
        else:
            f2.write("1\n")
print count
f.close()
f1.close()
os.remove("/Users/sidhesh/Documents/workspace/process-tweet/dev_temp.txt")