from google.appengine.ext import ndb


    # name String
    # rating Integer
    # quantity Integer
    # calories Integer
    # expiration Date

class Snack(ndb.Model):
    name = ndb.StringProperty()
    rating = ndb.IntegerProperty(repeated = True)
    quantity = ndb.IntegerProperty()
    calories = ndb.IntegerProperty()
    expiration = ndb.DateTimeProperty()

class Food(ndb.Model):
    snacks = ndb.KeyProperty(Snack, repeated = True)
