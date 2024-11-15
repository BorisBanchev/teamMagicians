from flask import redirect, render_template, request, jsonify, flash
from config import app, test_env
from entities.add_reference import add__reference

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/add_reference", methods = ["POST", "GET"])
def add_reference():
    if request.method == "GET":
        return render_template("add_reference.html")
    
    if request.method == "POST":
        author = request.form["author"]
        title = request.form["title"]
        journal = request.form["journal"]
        year = request.form["year"]
        message = add__reference(author, title, journal, year)
        return render_template("/add_reference.html",message = message)
