from flask import Flask, render_template, flash, request
import requests

app = Flask(__name__)
app.secret_key = "password"
user = "Dave"

@app.route("/")
def index():
    flash("Welcome!")
    return render_template("my_index.html", user=user)

@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Hello, " + str(request.form["name_input"]) + "! " 
          + str(request.form["game_name"]).title() 
          + " is a great game!"" Please take a look around!")
    return render_template("greet_index.html", user=user)

app.run(host="0.0.0.0", port=80)