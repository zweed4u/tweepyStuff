#Find all users that you have blocked and unblocks them
import tweepy
from tweepy.auth import OAuthHandler

'''@anon121792 application'''
#enter the corresponding information from your Twitter application:
CONSUMER_KEY = '';CONSUMER_SECRET = '';ACCESS_KEY = '';ACCESS_SECRET = '';
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

for blockedUsers in api.blocks():
	api.destroy_block(id=blockedUsers.id)
	print 'Unblocked @'+str(blockedUsers.screen_name)
	
