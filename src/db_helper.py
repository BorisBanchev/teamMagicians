from sqlalchemy import text
from config import db, app

table = "reference_list"  # pylint: disable=invalid-name


def initialize_database():
    print(f"Checking if table {table} exists")
    sql = text(
        "SELECT EXISTS(SELECT 1 FROM information_schema.tables WHERE table_name= :table)")
    result = db.session.execute(sql, {"table": table})
    if not result.scalar():
        print(f"Creating table {table}")
        sql = text(f"""CREATE TABLE {table}(
                   id SERIAL PRIMARY KEY,
                   reference_type TEXT,
                   keyword TEXT,
                   author TEXT,
                   title TEXT,
                   booktitle TEXT,
                   publisher TEXT,
                   journal TEXT,
                   year INT,
                   editor TEXT,
                   volume TEXT,
                   number TEXT,
                   series TEXT,
                   type TEXT,
                   chapter TEXT,
                   pages TEXT,
                   address TEXT,
                   edition TEXT,
                   month TEXT,
                   note TEXT,
                   howpublished TEXT,
                   organization TEXT)""")

        db.session.execute(sql)
        db.session.commit()
        print("Table created successfully")


def reset_db():
    print(f"Clearing contents from table {table}")
    sql = text(f"DELETE FROM {table}")
    db.session.execute(sql)
    db.session.commit()


def delete_table():
    print(f"delete table {table}")
    sql = text(f"DROP TABLE IF EXISTS {table}")
    db.session.execute(sql)
    db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        delete_table()
        initialize_database()
