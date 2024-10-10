import psycopg2
from config import load_config

def users_query():

    config = load_config()

    users_query = "SELECT * FROM users;"

    with psycopg2.connect(**config) as conn:
        try:
            with conn.cursor() as cursor:
                try:
                    cursor.execute(users_query)
                    all_users = cursor.fetchall()
                    #for user in all_users:
                    #    print(user)
                    return all_users
                except (Exception, psycopg2.DatabaseError) as error:
                    print(error)
        except:
            print('error')

def user_query(user_id):

    config = load_config()

    users_query = "SELECT * FROM users WHERE id = %s;"

    with psycopg2.connect(**config) as conn:
        try:
            with conn.cursor() as cursor:
                try:
                    cursor.execute(users_query, (user_id,))
                    user = cursor.fetchone()
                    return user
                except (Exception, psycopg2.DatabaseError) as error:
                    print(error)
        except:
            print('error')
