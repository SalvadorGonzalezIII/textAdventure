import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-type'] = 'text/plain'
        self.response.write('hellow,world')

app = webapp2.WSGIApplicaion([
    ('/',MainPage),
], debug=True)
