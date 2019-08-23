import webapp2
import jinja2
import os

#from model import *

user = ""
Nombre = {
"userN": user
}
pageNumber = 0
message = ""
die={
"page":pageNumber,
"deathMessage": message
}

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
    def post(self):
        die["page"] = 1
        user=self.request.get("user")
        Nombre["userN"] = user
        result_template = jinja_env.get_template('templates/pageOne.html')
        self.response.write(result_template.render(Nombre))

class deathPageOneHandler(webapp2.RequestHandler):
    def get(self):
        if die["page"] == 1:
            die["deathMessage"]="you were attacked by a monster :( "

        elif die["page"] == 2:
            die["deathMessage"]="you were to slow buddy :( "

        elif die["page"] == 3:
            die["deathMessage"]="you fell into quicksand and well...oops :( "

        elif die["page"] == 4:
            die["deathMessage"]="you used fuel instead of water -.- "

        elif die["page"] == 5:
            die["deathMessage"]="turns out you have never been much of a climber XD "

        elif die["page"] == 6:
            die["deathMessage"]="lets be honest you arent a athlete "

        result_template = jinja_env.get_template('templates/deathPageOne.html')
        self.response.write(result_template.render(die))


class pageTwoHandler(webapp2.RequestHandler):
    def get(self):
        result_template = jinja_env.get_template('templates/pageTwo.html')
        self.response.write(result_template.render(Nombre))

class pageThreeHandler(webapp2.RequestHandler):
    def get(self):
        die["page"] = 2
        result_template = jinja_env.get_template('templates/pageThree.html')
        self.response.write(result_template.render(Nombre))

class pageFourHandler(webapp2.RequestHandler):
    def get(self):
        die["page"] = 5
        result_template = jinja_env.get_template('templates/pageFour.html')
        self.response.write(result_template.render(Nombre))

class pageFiveHandler(webapp2.RequestHandler):
    def get(self):
        die["page"] = 3
        result_template = jinja_env.get_template('templates/pageFive.html')
        self.response.write(result_template.render(Nombre))

class pageSixHandler(webapp2.RequestHandler):
    def get(self):
        result_template = jinja_env.get_template('templates/pageSix.html')
        self.response.write(result_template.render(Nombre))

class pageSevenHandler(webapp2.RequestHandler):
    def get(self):
        die["page"] = 4
        result_template = jinja_env.get_template('templates/pageSeven.html')
        self.response.write(result_template.render(Nombre))

class pageEightHandler(webapp2.RequestHandler):
    def get(self):
        result_template = jinja_env.get_template('templates/pageEight.html')
        self.response.write(result_template.render(Nombre))

class pageNineHandler(webapp2.RequestHandler):
    def get(self):
        result_template = jinja_env.get_template('templates/pageNine.html')
        self.response.write(result_template.render(Nombre))

class pageTenHandler(webapp2.RequestHandler):
    def get(self):
        die["page"] = 6
        result_template = jinja_env.get_template('templates/pageTen.html')
        self.response.write(result_template.render(Nombre))

class pageElevenHandler(webapp2.RequestHandler):
    def get(self):
        result_template = jinja_env.get_template('templates/pageEleven.html')
        self.response.write(result_template.render(Nombre))

class pageTwelveHandler(webapp2.RequestHandler):
    def get(self):
        result_template = jinja_env.get_template('templates/pageTwelve.html')
        self.response.write(result_template.render(Nombre))

class tutorialHandler(webapp2.RequestHandler):
    def get(self):
        result_template = jinja_env.get_template('templates/tutorial.html')
        self.response.write(result_template.render(Nombre))


app = webapp2.WSGIApplication([
    ('/',MainPage),
    ('/pageOne',pageOneHandler),
    ('/deathPageOne',deathPageOneHandler),
    ('/pageTwo',pageTwoHandler),
    ('/pageThree',pageThreeHandler),
    ('/pageFour',pageFourHandler),
    ('/pageFive',pageFiveHandler),
    ('/pageSix',pageSixHandler),
    ('/pageSeven',pageSevenHandler),
    ('/pageEight',pageEightHandler),
    ('/pageNine',pageNineHandler),
    ('/pageTen',pageTenHandler),
    ('/pageEleven',pageElevenHandler),
    ('/pageTwelve',pageTwelveHandler),
    ('/tutorial',tutorialHandler)
], debug=True)
