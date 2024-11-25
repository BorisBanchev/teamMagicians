from sqlalchemy import text
from config import db

from entities.reference import Reference


def get_references():
    sql = text("SELECT * FROM reference_list")
    result = db.session.execute(sql)
    field_names = result.keys()

    # make dictionaries with field-value pairs corresponding to each reference
    rows = [dict(zip(field_names, row)) for row in result.fetchall()]
    references = []
    for dictionary in rows:
        reference_id = dictionary["id"]
        # filtering out empty or None fields
        non_empty_fields = {key: value for key, value in dictionary.items(
        ) if value not in ("", None) and key != "id"}

        # create reference instance
        reference_instance = Reference(reference_id, non_empty_fields)
        references.append(reference_instance)

    return references


def create_reference(fields):
    columns = ", ".join(fields.keys())  # Field names
    # Parameter placeholders
    values = ", ".join(f":{key}" for key in fields.keys())

    sql = text(f"INSERT INTO reference_list ({columns}) VALUES ({values})")
    db.session.execute(sql, fields)
    db.session.commit()


def delete_reference(reference_id):
    sql = text("DELETE FROM reference_list WHERE id = :id")
    db.session.execute(sql, {"id": reference_id})
    db.session.commit()


def check_valid_keyword(keyword):
    sql = text("SELECT keyword FROM reference_list")
    keywords = db.session.execute(sql).fetchall()
    list_keywords = [keyword[0] for keyword in keywords]
    return keyword in list_keywords and len(keyword) > 0
