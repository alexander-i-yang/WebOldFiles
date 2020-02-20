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


class Fav(db.Model):
    fav_id = db.StringProperty()
    created = db.DateTimeProperty(auto_now_add=True)


def concat_art(art_obj):
    art_str = ""
    art_str += "<h3>"
    art_str += cgi.escape(str(art_obj.title))
    art_str += "</h3>"
    art_str += cgi.escape(str(art_obj.art))
    return art_str


def get_arts():
    art_str = ""
    arts = db.GqlQuery("SELECT * FROM Art ORDER BY created DESC")
    art_list = arts.fetch(5)
    if len(art_list) == 0:
        return "no vals!"
    else:
        for x in art_list:
            art_str += concat_art(x)
    return art_str


def get_fav():
    favs = db.GqlQuery("SELECT * FROM Fav ORDER BY created DESC")
    if favs == "": return "No favorites!"
    fav_id = int(favs.fetch(1)[0].fav_id)
    return concat_art(Art.get_by_id(fav_id))


class MainPage(webapp2.RequestHandler):

    def get(self):
        logging.info("********** MainPage GET **********")
        template_values = {"error": "", "art": get_arts()}
        template = JINJA_ENVIRONMENT.get_template('templates/hello.html')
        self.response.write(template.render(template_values))  # write blank form

    def post(self):
        title = self.request.get("title")
        art = self.request.get("art")
        favorite = self.request.get("favorite")
        error = ""
        if title == "" or art == "":
            error = "Need both a title and some artwork!"
        else:
            art_instance = Art()
            art_instance.title = title
            art_instance.art = art
            art_instance.put()
            if favorite == "on":
                new_fav = Fav()
                new_fav.fav_id = str(art_instance.key().id())
                new_fav.put()
        time.sleep(0.2)
        template_values = {"error": error, "art": get_arts()}
        template = JINJA_ENVIRONMENT.get_template('templates/hello.html')
        self.response.write(template.render(template_values))  # write blank form


class Favorite(webapp2.RequestHandler):

    def get(self):
        template_values = {"art": get_fav()}
        template = JINJA_ENVIRONMENT.get_template('templates/favorite.html')
        self.response.write(template.render(template_values))  # write blank form


application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/favorite', Favorite)
], debug=True)
