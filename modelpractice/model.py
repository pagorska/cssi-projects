from google.appengine.ext import ndb

class DirectMessage(ndb.Model):
    sender = ndb.StringProperty()
    receiver = ndb.StringProperty()
    content = ndb.StringProperty()
    messageID = ndb.IntegerProperty()
    #timestamp = ndb.DateProperty()



# from model import DirectMessage
# from random import randint
# import urllib2
# import json
#
# DM = DirectMessage(sender="Ivana", receiver= "Patrycja", content = "look at these corgis", messageID = randint(1,1045632))
#
# DM.put()
#
# for i in range(10):
#     response1 = urllib2.urlopen("https://uinames.com/api/")
#
#     content1 = response1.read()
#     content_dict1 = json.loads(content1)
#
#     name1 = content_dict1['name']
#     response2 = urllib2.urlopen("https://uinames.com/api/")
#
#     content2 = response2.read()
#     content_dict2 = json.loads(content2)
#
#     name2 = content_dict2['name']
#     DM = DirectMessage(sender= name1, receiver= name2, content = str(i), messageID = randint(1,1045632))
#     DM.put()
