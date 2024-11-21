from flask import Flask
from random import randint

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1> Witaj świecie</h1><a> href='/druga'>Przejdż do drugiej strony</a>"

@app.route("/druga")
def druga():
    return "<p>Jakaś podstrona. Losowa liczba: {randint(1,100)}</p><a href='/'>Wróć do storny głównej</a>"

app.run(debug=True)