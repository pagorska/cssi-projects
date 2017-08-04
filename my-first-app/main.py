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
from PIL import Image
import webapp2
import urllib
import cStringIO
import os
import jinja2
from random import randint


#set up environment for Jinja
#this sets jinja's relative directory to match the directory name(dirname) of
#the current __file__, in this case, main.py
jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

def listitem(listo):
    return listo[randint(0, len(listo)-1)]

class MainHandler(webapp2.RequestHandler):

    # def randList(self):
    #     hello_world = ['Hej varlden', 'Hello Byd','Hallo warld', 'Hallo Wereld','Salam dunya','Czesc swiat', 'Hello world', 'Bonjour le monde', 'Hola mundo', 'Hola mon', 'Salom Dunyo']
    #     return hello_world[randint(0, len(hello_world)-1)]

    def get(self):
        num = int(self.request.get("num"))
        hello_world = ['Hej varlden', 'Hello Byd','Hallo warld', 'Hallo Wereld','Salam dunya','Czesc swiat', 'Hello world', 'Bonjour le monde', 'Hola mundo', 'Hola mon', 'Salom Dunyo']
        hello_list = []
        for i in range(num):
            matches = 0
            hello = listitem(hello_world)
            for index in range(len(hello_list)):
                if hello == hello_list[index]:
                    matches += 1

            if matches == 0:
                hello_list.append(hello)
                self.response.write(hello + '<br>')

class MilkHandler(webapp2.RequestHandler):
    def steve(self):
        return 'Steve hates milk'

    def get(self):
        yay = self.steve()
        self.response.write(yay)

class FoodHandler(webapp2.RequestHandler):
    def get(self):
        froot = self.request.get("froot")
        num = int(self.request.get("numTimes"))
        render_data = {
            'froot' : froot,
            'numTimes' : num
        }
        my_template = jinja_environment.get_template("templates/fruit.html")
        self.response.write(my_template.render(render_data))


class NameHandler(webapp2.RequestHandler):
    def get(self):
        name = self.request.get("name")
        self.response.write('Hello ' + name)
        self.response.write(my_template.render)

class ImageHandler(webapp2.RequestHandler):
    def get(self):
        hellos = ['Hej ', 'Hello ','Hallo ','Czesc ', 'Bonjour ', 'Hola ']
        hello = hellos[randint(0,len(hellos)-1)]
        name = ''
        name = self.request.get("name")
        if (name == ''):
            name = 'person!'
        my_template = jinja_environment.get_template("templates/hello-world.html")
        #self.response.write('something')
        mycolor = self.request.get("mycolor")
        render_data = { 'greeting' : hello,
                'name' : name,
                'mycolor' : mycolor
            }
        self.response.write(my_template.render(render_data))
        # self.response.write('<link rel="stylesheet" href="/resources/blue.css">')
        # self.response.write('<h1>please work</h1>')
        # self.response.write('<img width="50%" src="/resources/cupcake.png">')

class Instagram(webapp2.RequestHandler):
    def getRed(pixel):
        return pixel[0]

    def getGreen(pixel):
        return pixel[1]

    def getBlue(pixel):
        return pixel[2]

    def purple(image):
        new_pixels = []
        for pixel in image.getdata():
            new_pixel = (getGreen(pixel),getBlue(pixel),getRed(pixel))
            new_pixels.append(new_pixel)
        return new_pixels

    def gray(image):
        new_pixels = []
        for pixel in image.getdata():
            new_pixel = (getAverage(pixel),getAverage(pixel),getAverage(pixel))
            new_pixels.append(new_pixel)
        return new_pixels

    def cyan(image):
        new_pixels = []
        for pixel in image.getdata():
            new_pixel = (getBlue(pixel),getRed(pixel),getGreen(pixel))
            new_pixels.append(new_pixel)
        return new_pixels

    def pink(image):
        new_pixels = []
        for pixel in image.getdata():
            new_pixel = (getRed(pixel),getBlue(pixel),getGreen(pixel))
            new_pixels.append(new_pixel)
        return new_pixels

    def get(self):
        my_template = jinja_environment.get_template("templates/imageProcessor.html")
        image = self.request.get('image')
        if (image != ''):
            file = cStringIO.StringIO(urllib.urlopen(image).read())
            image = Image.open(file)
            color = self.request.get('color')
            if (color == 'cyan'):
                new_image = Image.new("RGB", image.size)
                new_image.putdata(cyan(image))
                new_image.show()
            elif (color == 'gray'):
                new_image = Image.new("RGB", image.size)
                new_image.putdata(gray(image))
                new_image.show()
            elif (color == 'pink'):
                new_image = Image.new("RGB", image.size)
                new_image.putdata(pink(image))
                new_image.show()
            elif (color == 'purple'):
                new_image = Image.new("RGB", image.size)
                new_image.putdata(purple(image))
                new_image.show()
            else:
                print 'No filter selected'
                new_image = Image.new("RGB", image.size)
                new_image.putdata(new_pixels)
                new_image.show()
        render_data = {
            'image' : image
        }
        self.response.write(my_template.render(render_data))



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/milk', MilkHandler),
    ('/hello', NameHandler),
    ('/image', ImageHandler),
    ('/fruit', FoodHandler),
    ('/instagram', Instagram)
], debug=True)
