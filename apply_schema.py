import os
import psycopg2
from dotenv import load_dotenv

load_dotenv(dotenv_path="backend/.env")

def apply_schema():
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        print("Error: DATABASE_URL not found in backend/.env")
        return

    schema_path = "db/schema.sql"
    if not os.path.exists(schema_path):
        print(f"Error: Schema file not found at {schema_path}")
        return

    try:
        conn = psycopg2.connect(database_url)
        cur = conn.cursor()
        
        with open(schema_path, "r") as f:
            schema_sql = f.read()
        
        print(f"Applying schema from {schema_path}...")
        cur.execute(schema_sql)
        conn.commit()
        print("Schema applied successfully!")
        
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error applying schema: {e}")

if __name__ == "__main__":
    apply_schema()
