# pylint:disable=C0111,C0103
import sqlite3
conn = sqlite3.connect('data/school.sqlite')

def students_from_city(db, city):
    """return a list of students from a specific city"""
    db = conn.cursor()
    query = """SELECT s.first_name, s.last_name
    FROM students s
    WHERE s.birth_city LIKE ?"""
    db.execute(query, (f"%{city}%",))
    result = db.fetchall()
    return [list(i) for i in result]

# To test your code, you can **run it** before running `make`
#   => Uncomment the following lines + run:
#$ python school.py

# print(students_from_city(db, 'Paris'))
