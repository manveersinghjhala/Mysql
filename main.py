import mysql.connector

db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="*******",
        database="testdatabase"
    )

mycursor = db.cursor()
#mycursor.execute("CREATE DATABASE testdatabase")
#mycursor.execute("CREATE TABLE Employee(emp_id INTEGER PRIMARY KEY AUTO_INCREMENT, first_name VARCHAR(20), last_name VARCHAR(20), Age INTEGER, Salary INTEGER)")

#mycursor.execute("INSERT INTO Employee(emp_id, first_name, last_name, Age, Salary) VALUES(%s,%s,%s,%s,%s)",(1,"Michael","Scott",40,150000))
mycursor.execute("INSERT INTO Employee(first_name, last_name, Age, Salary) VALUES(%s,%s,%s,%s)",("Stanley","Hudson",51,100000))

db.commit()

mycursor.execute("SELECT * from Employee")
for x in mycursor:
    print(x)
