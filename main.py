import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-type'] = 'text/plain'
        self.response.write('hellow,world')

class QuestionPage(webapp2.RequestHandler):
    def get(self:)
        self.response.headers['content-type'] = 'text/plain'
        self.response.write('questions here')

app = webapp2.WSGIApplication([
    ('/',MainPage),
    ('questions',QuestionPage),
], debug=True)
