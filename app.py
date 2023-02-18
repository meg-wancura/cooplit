from flask import Flask, render_template, request, flash
#import json

app = Flask(__name__, template_folder="templates")
app.secret_key = "password"


if __name__ == '__main__':
    app.run(debug=True)

@app.route("/")
@app.route("/index")
def index():
    return render_template("/index.html")

@app.route("/contact", methods=["GET"])
def contact():
    return render_template("/contact.html")

@app.route("/mock", methods=["GET"])
def mock():
    return render_template("/mock.html")

@app.route("/function", methods=["GET"])
def function():
    req = request.args.get('https://api.openalex.org/authors/https://orcid.org/0000-0002-1298-3089')
    print(req)