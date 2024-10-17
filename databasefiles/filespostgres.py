import json
import psycopg2

json_file_path = 'data.json'

conn = psycopg2.connect(database="magic", user="postgre", password="liQuid?sql2", host="localhost", port="5432")
cursor = conn.cursor()

with open(json_file_path, 'r') as f:
    data = json.load(f)

insert_query = """
    INSERT INTO files (id, uri, type, name, description, download_uri, updated_at, size, content_type, content_encoding)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

for record in data:
    cursor.execute(insert_query, (
        record.get('id'),                            # Use .get() to avoid KeyError
        record.get('uri'),                           # Use .get() for safety
        record.get('type', 'unknown'),               # Set default value if 'type' is missing
        record.get('name'),                          # Use .get() for safety
        record.get('description'),                   # Use .get() for safety
        record.get('download_uri'),                  # Use .get() for safety
        record.get('updated_at'),                    # Use .get() for safety
        record.get('size', 0),                       # Default to 0 if 'size' is missing
        record.get('content_type', 'unknown'),       # Default value if 'content_type' is missing
        record.get('content_encoding', 'none')       # Default value if 'content_encoding' is missing
    ))

conn.commit()

cursor.close()
conn.close()

print("Data inserted successfully into PostgreSQL table.")
