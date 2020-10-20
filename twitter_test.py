import tweepy
from config import Config
auth = tweepy.AppAuthHandler(Config.CONSUMER_KEY, Config.CONSUMER_SECRET)



#Construct the API instance
api = tweepy.API(auth, wait_on_rate_limit=True) # create an API object


def main():
    # Change this
    handle = "MontellFish"
    timeline = api.user_timeline(handle, count=50)
    for tweet in timeline:
        print("---- tweet ----\n")
        print(tweet.text, "\n")
    print(f"total tweets = {len(timeline)}")

if __name__ == '__main__':
    main()
