import tweepy
from tweepy import OAuthHandler
import codecs
from string import punctuation

class tweetSearchAndAnalysis():
    ckey = 'MEOtoDBej43KqjgGMUYWrkchA'
    csecret = 'b93sewY8LQS6halYNfDCUkaDTJ70MCcAx8SWAJE099TizfPRHX'
    atoken = '810873594242863105-1eZZvK6k7SXNSPpjo71lLpG37TVQZ62'
    asecret = 'WgJFVWgouFepLwpDQKlCdb2vBy2ZnltHz83RQ692uCLKs'

    # OAuth Authentication
    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)

    # Twitter API wrapper
    api = tweepy.API(auth)

    # Load the list of positive and negative words
    # These will be used for analysing the tweets
    pos_sent = open("positive_words.txt").read()
    positive_words = pos_sent.split('\n')
    	
    neg_sent = open('negative_words.txt').read()
    negative_words = neg_sent.split('\n')

    # tweetSearch() searches for 100 tweets containing the "Celebrity name"
    # and saves them to "testTweets.txt" for sentiment analysis at
    # tweetSentimentAnalysis
    def tweetSearch(self, celebrityName):

        outFile = codecs.open("testTweets.txt", 'w', "utf-8")
        results = self.api.search(q=celebrityName, lang="en", locale="en", count=100)
	
        for result in results:
            outFile.write(result.text + '\n')
            
        outFile.close()

        # This is the core of the analysis logic
        # I've kept it really simple, i.e., count the total number
        # of positive and negative words cumulated across all the
        # tweets stored in "testTweets.txt" and decide the sentiment.
    def posNegCount(self, tweet):
        pos = 0
        neg = 0

        for p in list(punctuation):
            tweet = tweet.replace(p, '')

        tweet = tweet.lower() #.encode('utf8')
        words = tweet.split(' ')
        word_count = len(words)

        for word in words:
            if word in self.positive_words:
                pos = pos + 1
            elif word in self.negative_words:
                neg = neg + 1

        return pos, neg


    def tweetSentimentAnalysis(self):
        tweets = codecs.open("testTweets.txt", 'r', "utf-8").read()
        tweets_list = tweets.split('\n')
        positive_counter = 0
        negative_counter = 0
        for tweet in tweets_list:
            if(len(tweet)):
                p, n = self.posNegCount(tweet)
                positive_counter += p
                negative_counter += n
        if positive_counter > negative_counter:
            return "POSITIVE"

        elif positive_counter < negative_counter:
            return "NEGATIVE"

        else:
            return "NEUTRAL"