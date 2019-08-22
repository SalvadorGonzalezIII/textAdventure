import webapp2
import jinja2
import os

#from model import *

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        result_template = jinja_env.get_template('templates/index.html')
        self.response.write(result_template.render())

class pageOneHandler(webapp2.RequestHandler):
    def get(self):
#question = questions(question =  "you are on island what do you do now?", answer1 = "stay on the beach", answer2)
        result_template = jinja_env.get_template('templates/pageOne.html')
        self.response.write(result_template.render())

class deathPageOneHandler(webapp2.RequestHandler):
    def get(self):
        result_template = jinja_env.get_template('templates/deathPageOne.html')
        self.response.write(result_template.render())

class pageTwoHandler(webapp2.RequestHandler):
    def get(self):
        result_template = jinja_env.get_template('templates/pageTwo.html')
        self.response.write(result_template.render())

class pageThreeHandler(webapp2.RequestHandler):
    def get(self):
        result_template = jinja_env.get_template('templates/pageThree.html')
        self.response.write(result_template.render())

class pageFourHandler(webapp2.RequestHandler):
    def get(self):
        result_template = jinja_env.get_template('templates/pageFour.html')
        self.response.write(result_template.render())



app = webapp2.WSGIApplication([
    ('/',MainPage),
    ('/pageOne',pageOneHandler),
    ('/deathPageOne',deathPageOneHandler),
    ('/pageTwo',pageTwoHandler),
    ('/pageThree',pageThreeHandler),
    ('/pageFour',pageFourHandler)
], debug=True)
