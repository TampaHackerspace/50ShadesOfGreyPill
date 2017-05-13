import os
from urllib.parse import urlparse
from urllib.request import urlopen
import tweepy
import time
import sys
import csv
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
from posixpath import basename
 
searchTerm = 'isis'
class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open(searchTerm + '.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print('Error on_data: %s' % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
consumer_key = '2lMsg92vqrILMo4Ig1YwVMrMt'
consumer_secret = '1w7BZTh0yGTG28PIaA3LWSl0CwlItWEwVWj8bCCLunS6ZpM2Gw'
access_token = '16316561-YnUVRNIilfAdgrlSaVJ30zVhqCzqO3NFiQ0uSnd5E'
access_secret = 'HtJEzwDDF1OXrz7DxuKqtRugwJzW0kDElnQdgMlu1rCQP'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

picNum = 100
outputPath = "C:/Github/50ShadesOfGreyPill/DataSources/raw/twitter/"
	
def saveMedia(status):
    non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
    if 'media' in status.entities:
        for image in status.entities['media']:
            global picNum
            picNum += 1
            link = image['media_url']
            picName = basename(urlparse(link).path)
            f = open(os.path.join(outputPath+"images/",picName), 'wb')
            response = urlopen(link)
            f.write(response.read())
            f.close()            
            print(picName)

def getTweets(screenName):
    #Twitter only allows access to a users most recent 3240 tweets with this method
	
    #initialize a list to hold all the tweepy Tweets
    #alltweets = []	
	
    #make initial request for most recent tweets (200 is the maximum allowed count)
    newTweets = api.user_timeline(screen_name = screenName,count=200)
    print ("Found " + str(len(newTweets)) + " tweets.")

    for i in range(len(newTweets)):
        #print(alltweets[i])
        print("Tweet #" + str(i))
        saveMedia(newTweets[i])

    #transform the tweepy tweets into a 2D array that will populate the csv	
    outTweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in newTweets]

    #write the csv	
    with open(outputPath + '%s_tweets.csv' % screenName, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["id","created_at","text"])
        writer.writerows(outTweets)
                      
    pass

#twitter_stream = Stream(auth, MyListener())
#twitter_stream.filter(track=['#' + searchTerm])

screenName = 'deaddrop'
ids = []
for page in api.followers_ids(screen_name=screenName):
    i = api.get_user(page).screen_name
    ids.append(i)
    print("Getting tweets for " + i)
    getTweets(i)
    time.sleep(2)

print(ids)
