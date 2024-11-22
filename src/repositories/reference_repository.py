from config import db
from sqlalchemy import text

from entities.reference import Reference

def get_references():
    sql = text("SELECT id, author, title, journal, year FROM reference_list")
    result = db.session.execute(sql)
    references = result.fetchall()
    return [Reference(reference[0], reference[1], reference[2], reference[3], reference[4]) for reference in references]

def create_reference(fields):
    columns = ", ".join(fields.keys())  # Field names
    values = ", ".join(f":{key}" for key in fields.keys())  # Parameter placeholders

    sql = text(f"INSERT INTO reference_list ({columns}) VALUES ({values})")
    db.session.execute(sql, fields) 
    db.session.commit()

def delete_reference(id):
    sql = text("DELETE FROM reference_list WHERE id= :id")
    db.session.execute(sql, {"id":id})
    db.session.commit()