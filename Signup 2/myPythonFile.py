import webapp2
import logging
import re
import jinja2
import os

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])

success = """
    <!DOCTYPE HTML>
<html>
  <head>
    <meta charset="utf-8">
    <title>Welcome</title>
  </head>
  <body>
    <h1>Welcome, ${username}</h1>
  </body>
</html>
"""

img = """<img src="https://www.w3schools.com/w3css/img_lights.jpg"/>"""


def valid_user(user):
    try:
        ret = re.search("^[a-zA-z0-9-]{3,20}$", user).group(0) == user
    except AttributeError:
        ret = False
    return ret


def valid_pass(password):
    try:
        ret = re.search("^[\S]{3,20}$", password).group(0) == password
    except AttributeError:
        ret = False
    return ret


def valid_email(email):
    try:
        ret = re.search("^[\S]+@[\S]+\.[\S]+$", email).group(0) == email
    except AttributeError:
        ret = False
    return ret


class MainPage(webapp2.RequestHandler):
    def get(self):
        logging.info("****** MainPage GET ******")
        template_values = {"userError": "", "passError": "", "verifError": "", "emailError": ""}
        template = JINJA_ENVIRONMENT.get_template('templates/signup.html')
        self.response.write(template.render(template_values))  # write blank form


class TestHandler(webapp2.RequestHandler):
    def post(self):
        logging.info("****** TestHandler POST ******")
        username = self.request.get("username")  # get 'q' from request
        password = self.request.get("password")
        verif = self.request.get("verify")
        email = self.request.get("email")
        logging.info("*** user=" + str(username) + " type=" + str(type(username)))
        welcome = True
        user_msg = ""
        password_msg = ""
        verif_msg = ""
        email_msg = ""
        if not valid_user(username):
            welcome = False
            user_msg = "The username is invalid"
        if not valid_pass(password):
            welcome = False
            password_msg = "The password is invalid"
        if password != verif:
            welcome = False
            verif_msg = "Passwords do not match"
        if len(email) != 0 and not valid_email(email):
            welcome = False
            email_msg = "Invalid email"

        if welcome:
            self.response.write(success.replace("${username}", username))
            self.response.write(img)
        else:
            template_values = {"userError": user_msg, "passError": password_msg, "verifError": verif_msg, "emailError": email_msg};
            template = JINJA_ENVIRONMENT.get_template('templates/signup.html')
            self.response.write(template.render(template_values))  # write blank form


application = webapp2.WSGIApplication([
    ('/', MainPage),   # maps the URL '/' to MainPage
    ('/welcome', TestHandler),
], debug=True)

