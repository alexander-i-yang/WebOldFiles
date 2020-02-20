import webapp2
import logging
import cgi


def escape_html(s):
    return cgi.escape(s, quote=True)


months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']

months_abrvs = dict((m[:3].lower(), m) for m in months)


def valid_month(month):
    return month in months or month in months_abrvs


def valid_year(year):
    if year.isdigit():
        year = int(year)
        if 1900 < year < 2020:
            return year


def valid_day(day):
    if day.isdigit():
        day = int(day)
        if 0 < day < 32:
            return day


form = """
<form method="post">
  What is your birthday?
  <br>
  <label> Month  <input type="text" name="month" value="%(month)s">  </label>
  <br>
  <label> Day  <input type="text" name="day" value="%(day)s">  </label>
  <br>
  <label> Year  <input type="text" name="year" value="%(year)s">  </label>
  <br>
  <input type="submit">
  <div style="color: red">%(error)s</div> 
</form>
"""


def write_form(self, month="", day="", year="", error=""):
    self.response.out.write(form % {
        "month": escape_html(month),
        "day": escape_html(day),
        "year": escape_html(year),
        "error": error
    })


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        write_form(self)
        logging.info("Mainpage get")

    def post(self):
        month = self.request.get("month")
        year = self.request.get("year")
        day = self.request.get("day")

        if valid_day(day) and valid_month(month) and valid_year(year):
            self.redirect("/success")
        else:
            write_form(self, month, day, year, "Invalid")


class SuccessPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write("Valid")


application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/success', SuccessPage)
], debug=True)
