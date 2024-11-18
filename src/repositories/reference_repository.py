from config import db
from sqlalchemy import text

from entities.reference import Reference

def get_references():
    sql = text("SELECT id, author, title, journal, year FROM reference_list")
    result = db.session.execute(sql)
    references = result.fetchall()
    return [Reference(reference[0], reference[1], reference[2], reference[3], reference[4]) for reference in references]

def create_reference(author, title, journal, year):
    sql = text("INSERT INTO reference_list (author, title, journal, year) VALUES (:author, :title, :journal, :year)")
    db.session.execute(sql,{"author":author, "title":title, "journal":journal, "year":year})
    db.session.commit()
