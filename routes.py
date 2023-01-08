from flask import Flask, render_template, url_for, request


app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/login", methods=['GET', "POST"])
def login_page():
    return render_template("login.html")

@app.route("/register", methods=['GET', 'POST'])
def register_page():
    return render_template("register.html")