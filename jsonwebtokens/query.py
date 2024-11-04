import psycopg2
from config import load_config

def tokens_query():

    config = load_config()

    users_query = "SELECT * FROM tokens;"

    with psycopg2.connect(**config) as conn:
        try:
            with conn.cursor() as cursor:
                try:
                    cursor.execute(users_query)
                    all_users = cursor.fetchall()
                    for user in all_users:
                        print(user)
                    return all_users
                except (Exception, psycopg2.DatabaseError) as error:
                    print(error)
        except:
            print('error')

def users_query():

    config = load_config()

    users_query = "SELECT * FROM users;"

    with psycopg2.connect(**config) as conn:
        try:
            with conn.cursor() as cursor:
                try:
                    cursor.execute(users_query)
                    all_users = cursor.fetchall()
                    for user in all_users:
                        print(user)
                    return all_users
                except (Exception, psycopg2.DatabaseError) as error:
                    print(error)
        except:
            print('error')

def insert_user(username,password):
    config = load_config()

    query = "INSERT INTO users (username, password) VALUES (%s, %s);"

    with psycopg2.connect(**config) as conn:
        try:
            with conn.cursor() as cursor:
                try:
                    cursor.execute(query, (username, password,))
                except (Exception, psycopg2.DatabaseError) as error:
                    print(error)
        except:
            print('error')

def get_userid_by_username(username):
    config = load_config()

    query = "SELECT id from users WHERE username=%s;"

    with psycopg2.connect(**config) as conn:
        try:
            with conn.cursor() as cursor:
                try:
                    cursor.execute(query, (username,))
                    user = cursor.fetchone()
                    return user
                except (Exception, psycopg2.DatabaseError) as error:
                    print(error)
        except:
            print('error')

def insert_tokens(user_id, access, refresh):
    config = load_config()

    query = "INSERT INTO tokens (user_id, access_token, refresh_token) VALUES (%s, %s, %s);"
    
    with psycopg2.connect(**config) as conn:
        try:
            with conn.cursor() as cursor:
                try:
                    cursor.execute(query, (user_id, access, refresh,))
                except (Exception, psycopg2.DatabaseError) as error:
                    print(error)
        except:
            print('error')

def get_password(username):
    config = load_config()

    query = "SELECT password from users WHERE username=%s;"

    with psycopg2.connect(**config) as conn:
        try:
            with conn.cursor() as cursor:
                try:
                    cursor.execute(query, (username,))
                    user = cursor.fetchone()
                    '''
                    (I spend like 6 hours just to realize the correct way to solve it)
                    when you are using postgres and you use the password column
                    as bytea, it returns a memoryview object, if you want to 
                    get the actual hash you have to convert it to bytes, you
                    use bytes(user[0]) then you now have the hash and can use it
                    with bcrypt.checkpw(password encoded, variable with bytes data)
                    '''
                    '''
                    byte_data = bytes(user[0])
                    string_data = byte_data.decode('utf-8')
                    print("Byte Data:", byte_data)
                    print("String Data:", string_data)
                    print(user)
                    '''
                    return user
                except (Exception, psycopg2.DatabaseError) as error:
                    print(error)
        except:
            print('error')

def get_username(username):
    config = load_config()

    query = "SELECT username from users WHERE username=%s;"

    with psycopg2.connect(**config) as conn:
        try:
            with conn.cursor() as cursor:
                try:
                    cursor.execute(query, (username,))
                    user = cursor.fetchone()
                    return user
                except (Exception, psycopg2.DatabaseError) as error:
                    print(error)
        except:
            print('error')


#insert_user("???", "user123")
#validate_user("???", "user123")
#get_user("loor")
