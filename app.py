from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "password"


@app.route("/")
@app.route("/index")
def index():
    return render_template("templates/index.html")

@app.route("/about")
def about():
    return render_template("templates/about.html")

@app.route("/contact")
def contact():
    return render_template("templates/contact.html")

if __name__ == '__main__':
    app.run(debug=True)