import os
from dotenv import load_dotenv
import tweepy

# Load API keys from .env file
load_dotenv()

API_KEY = os.getenv("TWITTER_API_KEY")
API_SECRET = os.getenv("TWITTER_API_SECRET")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")

# Authenticate with Tweepy
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# Verify credentials
try:
    api.verify_credentials()
    print("✅ Twitter Authentication Successful!")
except tweepy.TweepyException as e:
    print("❌ Twitter Authentication Failed!", e)
