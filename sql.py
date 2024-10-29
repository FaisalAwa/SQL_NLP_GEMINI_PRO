import sqlite3

# Connect to sqlite
connection = sqlite3.connect("student.db")

# Create a cursor object to insert, record, create table, retrieve
cursor = connection.cursor()

# Create table
table_info = """
CREATE TABLE IF NOT EXISTS STUDENT (
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT
);
"""

cursor.execute(table_info)

# Insert some more records
cursor.execute('''INSERT INTO STUDENT VALUES ('Krish', 'Data Science', 'A', 100)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Shahid', 'HSO', 'B', 300)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Atif', 'Data Science', 'A', 250)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Aamir', 'Accounts', 'C', 30)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Hamid', 'PAF', 'B', 250)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Faisal', 'Analytics', 'B', 500)''')

# Display all the records
print("The inserted records are:")

data = cursor.execute('''SELECT * FROM STUDENT''')

for row in data:
    print(row)

# Close the connection
connection.commit()
connection.close()
