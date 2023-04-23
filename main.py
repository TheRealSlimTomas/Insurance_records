import sqlite3

class Person:
    def __init__(self,id_number=-1, first="", last="", age=-1, phone=-1):
        self.id_number = id_number
        self.first = first
        self.last = last
        self.age = age
        self.phone = phone
        # linking python and database
        self.connection = sqlite3.connect('Evidence_pojištění')
        self.cursor = self.connection.cursor()

    def load_person(self, id_number):
        self.cursor.execute("""
        SELECT * FROM persons
        WHERE id = {}
        """.format(id_number))

        results = self.cursor.fetchone()
        self.id_number = id_number
        self.first = results[1]
        self.last = results[2]
        self.age = results[3]
        self.phone = results[4]

    def insert_person(self):
        self.cursor.execute("""
            INSERT OR REPLACE INTO persons VALUES (NULL, ?, ?, ?, ?)
            """, (self.first, self.last, self.age, self.phone))

        self.connection.commit()
        self.connection.close()






