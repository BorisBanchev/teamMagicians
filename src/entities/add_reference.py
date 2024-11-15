from config import db, app
from sqlalchemy import text

def add__reference(author: str, title: str, journal: str, year: int):
    if author != "" and title != "" and journal != "" and year != "":
        if len(title) <= 100:
            sql = text("INSERT INTO reference_list (author, title, journal, year) VALUES (:author, :title, :journal, :year)")
            db.session.execute(sql,{"author":author, "title":title, "journal":journal, "year":year})
            db.session.commit()
            return "Article reference added successfully!"
        else:
            return "title is too long!"
    return "Reference fields can not be empty!"
