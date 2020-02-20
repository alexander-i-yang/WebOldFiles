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


class BlogData(db.Model):
    subject = db.StringProperty()
    content = db.TextProperty()
    created = db.DateTimeProperty(auto_now_add=True)


class MainPage(webapp2.RequestHandler):

    def get(self, bad=""):
        logging.info("********** MainPage GET **********")
        posts = db.GqlQuery("SELECT * FROM BlogData ORDER BY created DESC LIMIT 10")
        template_values = {"posts": posts}
        template = JINJA_ENVIRONMENT.get_template('templates/posts.html')
        self.response.write(template.render(template_values))  # write blank form


class BlogPost(webapp2.RequestHandler):

    def get(self, blog_post_id):
        logging.info("********** BlogPost GET **********")
        cur_id = int(blog_post_id)
        cur_post = BlogData.get_by_id(cur_id)
        template_values = {"subject": cur_post.subject, "created": cur_post.created, "content": cur_post.content}
        template = JINJA_ENVIRONMENT.get_template('templates/blogpost.html')
        self.response.write(template.render(template_values))  # write blank form


class NewPost(webapp2.RequestHandler):

    def get(self, bad=""):
        logging.info("********** NewPost GET **********")
        template_values = {"ph_subject": "", "ph_content": "", "ph_error": ""}
        template = JINJA_ENVIRONMENT.get_template('templates/newpost.html')
        self.response.write(template.render(template_values))  # write blank form

    def post(self, bad=""):
        logging.info("********** NewPost POST **********")
        logging.info(bad)
        subject = self.request.get("subject")
        content = self.request.get("content")
        error = ""
        if subject == "" or content == "":
            error = "Need both a title and some content!"
        else:
            new_post = BlogData()
            new_post.subject = subject
            new_post.content = content
            new_post.put()
            self.redirect("/blog/" + str(new_post.key().id()))
        template_values = {"ph_subject": subject, "ph_content": content, "ph_error": error}
        template = JINJA_ENVIRONMENT.get_template('templates/newpost.html')
        self.response.write(template.render(template_values))  # write blank form


application = webapp2.WSGIApplication([
    ('/', MainPage),
    (r'/blog(\/|)', MainPage),
    (r'/blog/(\d+)', BlogPost),
    (r'/newpost(\/|)', NewPost)
], debug=True)
