#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "3067475153-gdXzF6K0UnyDtETPS3GzCBiN3LQ9SRsTEb3PZR1"
access_token_secret = "nSFhHSjLIPVT0WTiJW7KgShcORAz0jL88MR2URcYktR8q"
consumer_key = "DRrDmC3wIzjRn1mTXloeYfMRI"
consumer_secret = "wSXQKoNnjnj7tDSaVh6wEjuvQqwJLXbvLQrvW3jVERmIif8o2p"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['Trump'])