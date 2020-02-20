import webapp2
import logging
import re

form = """
<!DOCTYPE HTML>
<html>
  <head>
    <meta charset="utf-8">
    <title>Signup Page</title>
    <link rel="stylesheet" type="text/css" href="stylesheets/style.css">
  </head>
  <body>
    <h1>Signup</h1>
    <form method="post" action="/welcome">
      <table>
        <tr>
          <td class="label">Username</td>
          <td><input type="text" name="username" value=""></td>
          <td class="error">${user-error}</td>
        </tr>

        <tr>
          <td class="label">Password</td>
          <td><input type="password" name="password" value=""></td>
          <td class="error">${pass-error}</td>
        </tr>

        <tr>
          <td class="label">Verify Password</td>
          <td><input type="password" name="verify" value=""></td>
          <td class="error">${verif-error}</td>
        </tr>

        <tr>
          <td class="label">Email (optional)</td>
          <td><input type="text" name="email" value=""></td>
          <td class="error">${email-error}</td>
        </tr>
      </table>

      <input type="submit">

    </form>
  </body>
</html>
"""

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
        self.response.headers['Content-Type'] = 'text/html'
        new_form = form.replace("${user-error}", "")
        new_form = new_form.replace("${pass-error}", "")
        new_form = new_form.replace("${verif-error}", "")
        new_form = new_form.replace("${email-error}", "")
        self.response.write(new_form)  # write blank form


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
            new_form = form.replace("${user-error}", user_msg)
            new_form = new_form.replace("${pass-error}", password_msg)
            new_form = new_form.replace("${verif-error}", verif_msg)
            new_form = new_form.replace("${email-error}", email_msg)
            self.response.write(new_form)


application = webapp2.WSGIApplication([
    ('/', MainPage),   # maps the URL '/' to MainPage
    ('/welcome', TestHandler),
], debug=True)

