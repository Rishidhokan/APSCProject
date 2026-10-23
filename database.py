
import sqlite3

conn = sqlite3.connect('')
cursor = conn.cursor()

cursor.execute('CREATE TABLE register (role TEXT, adhar_no TEXT, full_name TEXT, gender TEXT, mobile_no TEXT, address TEXT, dob TEXT)')
conn.commit()


result = cursor.fetchone()
