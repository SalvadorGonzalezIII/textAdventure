import webapp2
import jinja2
import os

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
        result_template = jinja_env.get_template('templates/pageOne.html')
        self.response.write(result_template.render())

class deathPageHandler(webapp2.RequestHandler):
    def get(self):
        result_template = jinja_env.get_template('templates/deathPage.html')
        self.response.write(result_template.render())



app = webapp2.WSGIApplication([
    ('/',MainPage),
    ('/pageOne',pageOneHandler),
    ('/deathPage',deathPageHandler)
], debug=True)
