import psycopg2
import psycopg2.extras
import psycopg2.errors

conn = psycopg2.connect(
    database='psycopg2_test_db',
    user='jurgeon',
    password='69018',
    host='127.0.0.1',
    port=5432,
)
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)







# cur.execute('''
# create table users (id serial primary key, login varchar(64), password varchar(64))
# ''')
cur.execute("INSERT INTO users (login, password) VALUES (%s, %s)",
    ("afiskon", "123"))
cur.execute("INSERT INTO users (login, password) VALUES (%s, %s)",
    ("eax", "456"))
cur.execute(
    "UPDATE users SET password = %(password)s WHERE login = %(login)s", 
    {"login":"eax", "password":"789"}
)
cur.execute("DELETE FROM users WHERE id = %s", (2,))
cur.execute("PREPARE insuser AS " +
    "INSERT INTO users (login, password) VALUES ($1, $2)")
cur.execute("EXECUTE insuser(%s, %s)", ("afiskon", "123"))
cur.execute("EXECUTE insuser(%s, %s)", ("eax", "456"))
conn.commit()
cur.execute("SELECT version()")
cur.execute('SELECT * FROM users LIMIT 10')
print(cur.fetchone())
records = cur.fetchall()
# for record in records:
#     # print(dict(record.items()))
#     print(record['login'])



with conn:
    with conn.cursor() as cur:



cur.close()
conn.close()
'''
# створює юзера в БД. Вводити 1 раз перед початком розробки. 
sudo -u postgres psql -c "create user jurgeon with password '69018'; alter role jurgeon set client_encoding to 'utf8'; alter role jurgeon set default_transaction_isolation to 'read committed'; alter role jurgeon set timezone to 'UTC';"

# це не чіпай 
#####sudo -u postgres psql -c 'create database psycopg2_test_db;'
#####sudo -u postgres psql -c 'grant all privileges on database psycopg2_test_db to jurgeon;'


# видаляє БД
sudo -u postgres psql -c "drop database eleek; "

# створює БД 
sudo -u postgres psql -c "create database eleek owner jurgeon; "




'''