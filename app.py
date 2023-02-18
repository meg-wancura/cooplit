from flask import Flask, render_template, request, flash
import requests
import json

app = Flask(__name__)
app.secret_key = "password"


if __name__ == '__main__':
    app.run(debug=True)


@app.route("/")
@app.route("/index")
def index():
    return render_template("/index.html")

@app.route("/contact")
def contact():
    return render_template("/contact.html")

@app.route("/mock")
def contact():
    return render_template("/mock.html")

@app.route("/function")
def function():
    req = requests.get('https://api.openalex.org/authors/https://orcid.org/0000-0002-1298-3089')
    data = req.content
    json_data = json.loads(data)
    return render_template('function.html', data=jason_data)
