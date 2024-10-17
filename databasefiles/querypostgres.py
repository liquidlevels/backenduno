import psycopg2

def connect_and_query():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="magic",
            user="postgres",
            password="liQuid?sql2",
            port="5432"
        )

        cursor = conn.cursor()

        query = "SELECT * FROM files"
        value = ("some_value",)

        cursor.execute(query, value)

        rows = cursor.fetchall()

        for row in rows:
            print(row)

        cursor.close()
        conn.close()

    except Exception as e:
        print(f"Error: {e}")

connect_and_query()

