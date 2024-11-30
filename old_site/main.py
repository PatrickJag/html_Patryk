from flask import Flask, render_template
from random import randint

app = Flask(__name__)


@app.route("/")
def hello():
    losowa = randint(1,100)
    napis
    return "<h1>Witaj świecie!</h1><a href='/druga'>Przejdź do drugiej strony</a>"


@app.route("/druga")
def druga():
    return f"<p>Jakaś podstrona. Losowa liczba: {randint(1, 100)}</p><a href='/'>Wróć do strony głównej</a>"

@app.route("/druga")

app.run(debug=True)