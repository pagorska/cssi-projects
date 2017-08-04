from google.appengine.ext import ndb
#from post import Post

class User(ndb.Model):
    username = ndb.StringProperty()
    bio = ndb.StringProperty()
    followers = ndb.KeyProperty('User', repeated = True)
    #posts = ndb.KeyProperty(Post, repeated = True)


from post import Post
from user import User
#
user1 = User(username='patrycjaa', bio='wut')
user2 = User(username='patrycjaa', bio='wut')
followsMe = [user1, user2]
userMe = User(username='patrycjaa', bio='wut',followers=followsMe.key)
userMe.put()
post1 = Post(description='no image oops', poster=userMe.key)
post2 = Post(description='also not an image', poster=userMe.key)
postList = [post1, post2]
print postList
print userMe
