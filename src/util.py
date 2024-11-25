from sqlalchemy import text
from config import db

class UserInputError(Exception):
    pass

def validate_reference(reference_type, fields):
    reference_fields = {
        "article": {"mandatory": ["author", "title", "journal", "year"],
                    "optional": ["volume", "number", "pages", "month", "note"],},
        "book": {"mandatory": ["author", "title", "publisher", "year"],
                 "optional": ["editor", "volume", "number", "series", "edition", "isbn"]},
        "misc": {"mandatory": [],
                 "optional": ["author", "title", "howpublished", "month", "year", "note"]},
    }

    if not fields["keyword"]:
        raise ValueError("Keyword is a mandatory field")

    fields_for_type = reference_fields[reference_type]

    # Check mandatory fields
    missing_fields = [
        field for field in fields_for_type["mandatory"] if not fields.get(field)
    ]

    if missing_fields:
        raise ValueError(f"Missing mandatory fields: {', '.join(missing_fields)}")

    #Check that at least one field is maintained (case misc)
    all_valid_fields = fields_for_type["mandatory"] + fields_for_type["optional"]
    provided_fields = [
        field for field in all_valid_fields if fields.get(field)
    ]

    if not provided_fields:
        raise ValueError("At least one field needs to be maintained.")

    if "author" in fields and check_input_length(fields["author"]):
        raise ValueError("Reference author length must be greater than 2")

    if "title" in fields and check_input_length(fields["title"]) or len(fields["title"]) > 100:
        raise ValueError("Reference title length must be smaller than 100 and greater than 2")

    if "journal" in fields and check_input_length(fields["journal"]):
        raise ValueError("Reference journal length must be greater than 2")

    if "year" in fields:  # Check if year exists and is not empty
        if fields["year"] == "":
            pass
        elif int(fields["year"]) < 0 or int(fields["year"]) > 2025:  # Check range
            raise ValueError("Reference year must be positive and smaller than 2026")

    if "publisher" in fields and check_input_length(fields["publisher"]):
        raise ValueError("Reference publisher length must be greater than 2")

def check_input_length(field):
    if len(field) > 0 and len(field) < 3:
        return True
    return False

def check_valid_keyword(keyword):
    sql = text("SELECT keyword FROM reference_list")
    keywords = db.session.execute(sql).fetchall()
    list_keywords = [keyword[0] for keyword in keywords]
    if keyword in list_keywords:
        raise  ValueError("Reference keyword must be unique")
    if len(keyword) > 20:
        raise ValueError("Reference keyword length can't be greater than 20")
    if len(keyword) == 0:
        raise ValueError("Reference keyword length can't be empty")

def raise_error(message):
    raise ValueError(message)
