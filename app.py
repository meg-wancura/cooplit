from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "password"


@app.route("/")
def index():
    return render_template("index.html")

@app.route("../html/about")
def about():
    return render_template("../html/about.html")

@app.route("../html/contact")
def contact():
    return render_template("../html/contact.html")

@app.route("../html/mock")
def contact():
    return render_template("../html/mock.html")
