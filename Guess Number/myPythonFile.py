import webapp2
import logging
import datetime
from random import seed
from random import random
from random import randint

form = """
<form method="post" action="/testform">
Enter Guess: <input name="q">
<input type="submit">
</form>
"""

numbers = []

class MainPage(webapp2.RequestHandler):
    
    def get(self):
        logging.info("****** MainPage GET ******")
        logging.info(numbers)
        seed(datetime.datetime.now().time())
        number = randint(1, 100)
        numbers.append(number)
        self.response.write("Good luck!")
        self.response.write(form)
        self.response.write("Random Number: " + str(numbers[-1]))

    def post(self):
        logging.info("****** MainPage GET ******")
        logging.info(numbers)
        seed(datetime.datetime.now().time())
        number = randint(1, 100)
        correct = False
        if len(numbers) == 0:
            numbers.append(number)
            self.response.write("Good luck!")
        else:
            guess = self.request.get("q")
            self.response.write("Guess: " + str(guess))
            status = "\nYour guess is too high"
            try:
                if int(guess) > 100 or int(guess) < 1:
                    status = "Guess must be a number between 1 and 100!"
                elif int(numbers[-1]) == int(guess):
                    status = "\nCorrect!"
                    correct = True
                elif int(numbers[-1]) > int(guess):
                    status = "\nYour guess is too low"
            except ValueError:
                status = "Guess must be a number between 1 and 100!"
            self.response.write("<div>" + status + "</div>")
        self.response.headers['Content-Type'] = 'text/html'
        if not correct:
            self.response.write(form)  # write blank form
        self.response.write("Random Number: " + str(numbers[-1]))

application = webapp2.WSGIApplication([
    ('/', MainPage),   # maps the URL '/' to MainPage
    ('/testform', MainPage),
], debug=True)

