import tweepy

auth = tweepy.OAuthHandler("kXU34Ed346zm0YtUTWGLOJ9zj", "C9bdfFcCXvbCWIBdvwOvYFdTY9gYRjfnf87IKc9Apsh6wMwEqt")

# Redirect user to Twitter to authorize
#redirect_user(auth.get_authorization_url())

# Get access token
auth.set_access_token('751073154303393792-LiItR3rIgJu4lC6b5HDx1TxnDELn1pF','DKdxX4BebK2Sitz15plyCoF0hMz7wEcrzg19G5nsSXEYx')

# Construct the API instance
api = tweepy.API(auth)

result = api.search(q="titli")
#print(result[0])
#print(len(result))
pics = set()
for tweets in result:
    media = tweets.entities.get('media',[])
    
    if(hasattr(tweets, 'extended_entities')):
        media_ext = tweets.extended_entities.get('media',[])
    
    if(len(media)>0):
        pics.add(media[0]['media_url_https'])
        pics.add(media[0]['media_url'])
    if(len(media_ext)>0):    
        pics.add(media_ext[0]['media_url'])
        pics.add(media_ext[0]['media_url_https'])

print(pics)