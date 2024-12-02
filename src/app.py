import json
import re
from flask import redirect, render_template, request, jsonify, flash
from config import app, test_env
from db_helper import reset_db
from repositories.reference_repository import create_reference, get_references, delete_reference
from util import validate_reference, check_valid_keyword
from api import fetch_work


@app.route("/")
def index():
    references = get_references()
    all_fields = [
        'reference_type', 'keyword', 'author', 'title', 'booktitle', 'publisher',
        'journal', 'year', 'editor', 'volume', 'number', 'series', 'type', 'chapter',
        'pages', 'address', 'edition', 'month', 'note', 'howpublished', 'organization'
    ]

    return render_template("index.html", references=references, all_fields=all_fields)


@app.route("/add_reference", methods=["POST", "GET"])
def add_reference():
    if request.method == "GET":
        return render_template("add_reference.html")

    if request.method == "POST":
        all_fields = request.form.to_dict()

    # Retrieve all fields submitted by the user
        try:
            check_valid_keyword(all_fields["keyword"])
            # Dynamic validation
            validate_reference(all_fields["reference_type"], all_fields)

            create_reference(all_fields)
            return redirect("/")
        except ValueError as error:
            flash(str(error))
            return redirect("/add_reference")
    return None

@app.route("/fetch_reference", methods=["POST"])
def fetch_reference():
    doi_input = request.form.to_dict()["doi_fetch"]
    doi = re.search(r'10\.\d{4}\/.*$', doi_input).group()
    print(doi)
    data = fetch_work(doi)
    jsondata = re.escape(json.dumps(data))
    return render_template("add_reference.html", fetch_data=jsondata)


@app.route("/delete_reference/<int:reference_id>", methods=["POST"])
def delete_reference_route(reference_id):
    try:
        delete_reference(reference_id)
        flash("Reference deleted")
    except ValueError as error_message:
        flash(f"Error deleting reference: {error_message}")
    return redirect("/")


# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({'message': "db reset"})
