import json

filename="/Users/sidhesh/Documents/Github/Team-MissionNLP/process-tweet/sarcastic_proc.txt"
with open(filename,"r") as f:
    content= f.readlines()
total_tweets = 0
total_tweets_words = 0
for line in content:
    total_tweets+=1
    total_tweets_words += len(line.split())

average_len_tweet = total_tweets_words/(total_tweets*1.0)

#filename_output=""
#with open(filename_output,"w+") as f:
    #dumpdata = {'TotalTweet':total_tweets,'AverageTweetLength':average_len_tweet}
    #json.dump(dumpdata)

print total_tweets,average_len_tweet