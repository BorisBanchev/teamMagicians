from config import db, app
from sqlalchemy import text

table = "reference_list"

def initialize_database():
    print(f"Checking if table {table} exists")
    sql = text("SELECT EXISTS(SELECT 1 FROM information_schema.tables WHERE table_name= :table)")
    result = db.session.execute(sql, {"table": table})
    if not result.scalar():
        print(f"Creating table {table}")
        sql = text(f"""CREATE TABLE {table}(
                   id SERIAL PRIMARY KEY, 
                   author TEXT,
                   title TEXT,
                   journal TEXT,
                   year INT)""")
        
        db.session.execute(sql)
        db.session.commit()
        print("Table created successfully")

def reset_db():
  print(f"Clearing contents from table {table}")
  sql = text(f"DELETE FROM {table}")
  db.session.execute(sql)
  db.session.commit()

if __name__ == "__main__":
    with app.app_context():
      initialize_database()