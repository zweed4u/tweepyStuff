#Goes through followers determines if the user is private
#...if the user is private, we block them, then unblock them.
#This is to say that we make all private followers unfollow us
import tweepy
from tweepy.auth import OAuthHandler

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = '';CONSUMER_SECRET = '';ACCESS_KEY = '';ACCESS_SECRET = '';
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

count=0
for user_id in api.followers_ids():
	user=api.get_user(id=user_id)
	if user.protected==True:
		#user is private - block 'em
		api.create_block(id=user_id)
		#block-unblock combo
		api.destroy_block(id=user_id)
		print 'Blocked @'+str(user.screen_name)
		count+=1
print 'Blocked '+str(count)+' users'

