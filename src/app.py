from flask import redirect, render_template, request, jsonify, flash
from config import app, test_env
from db_helper import reset_db
from repositories.reference_repository import create_reference
from util import validate_reference

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
        year = int(request.form["year"])
        try:
            validate_reference(author, title, journal, year)
            create_reference(author, title, journal, year)
            return redirect("/")
        except Exception as error:
            flash(str(error))
            return redirect("/add_reference")


# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })