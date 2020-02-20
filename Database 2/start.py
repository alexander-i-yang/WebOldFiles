import webapp2
import logging
import jinja2
import os
from google.appengine.ext import db
import time
import cgi

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])


class Art(db.Model):
    title = db.StringProperty()
    art = db.TextProperty()
    created = db.DateTimeProperty(auto_now_add=True)


def get_arts():
    art_str = ""
    arts = db.GqlQuery("SELECT * FROM Art ORDER BY created DESC")
    art_list = arts.fetch(5)
    if len(art_list) == 0:
        return "no vals!"
    else:
        for x in art_list:
            art_str += "<h3>"
            art_str += cgi.escape(str(x.title))
            art_str += "</h3>"
            art_str += cgi.escape(str(x.art))
    return art_str


class MainPage(webapp2.RequestHandler):

    def get(self):
        logging.info("********** MainPage GET **********")
        template_values = {"error": "", "art": get_arts()}
        template = JINJA_ENVIRONMENT.get_template('templates/hello.html')
        self.response.write(template.render(template_values))  # write blank form

    def post(self):
        title = self.request.get("title")
        art = self.request.get("art")
        error = ""
        if title == "" or art == "":
            error = "Need both a title and some artwork!"
        else:
            art_instance = Art()
            art_instance.title = title
            art_instance.art = art
            art_instance.put()
            time.sleep(0.2)
        template_values = {"error": error, "art": get_arts()}
        template = JINJA_ENVIRONMENT.get_template('templates/hello.html')
        self.response.write(template.render(template_values))  # write blank form


application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
