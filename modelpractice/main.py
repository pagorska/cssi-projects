#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import jinja2
import os
from snack import Snack
from datetime import datetime

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')
class SnackHandler(webapp2.RequestHandler):
    def get(self):
        my_template = jinja_environment.get_template('templates/snackPage.html')
        self.response.write(my_template.render())
        name1 = self.request.get('snackName')
        if (name1 != ''):
            rating1 = self.request.get('snackRating')
            rL = rating1.strip().split(",")
            ratingList = []
            for item in rL:
                ratingList.append(int(item))
            quantity1 = int(self.request.get('snackQuantity'))
            calories1 = int(self.request.get('snackCalories'))
            expDate = self.request.get('snackExp')
            time1 = datetime.strptime(expDate, '%x')
            my_snack = Snack(name = name1, rating = ratingList, quantity = quantity1, calories = calories1, expiration = time1)
            #self.response.write(my_snack)
            my_snack.put()

class DisplaySnackHandler(webapp2.RequestHandler):
    def get(self):
        my_template = jinja_environment.get_template('templates/snackPage2.html')
        query = Snack.query()
        query1 = query.fetch()
        # self.response.write(query.fetch()[0].name)
        # for item in query1:
        #     self.response.write(item.name + "</br>")
        my_vars = {'query1': query1}
        self.response.write(my_template.render(my_vars))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/snack', SnackHandler),
    ('/snacklist', DisplaySnackHandler)
], debug=True)
