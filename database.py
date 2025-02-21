import mysql.connector as mysql
import creds

db = mysql.connect(
    user=creds.user,
    passwd=creds.passwd,
    host=creds.host,
    port=creds.port,
    database=creds.database
)

cursor = db.cursor()

select_query = '''
SELECT *
FROM students
WHERE first_name = "Viktor"
AND last_name = "Metelkin"
'''

cursor.execute(select_query)
print(cursor.fetchall())

db.close()