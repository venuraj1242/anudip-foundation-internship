import mysql.connector

# Establish the connection
con = mysql.connector.connect(
    host="localhost", user="root", password="root", database="abesit"
)

cr = con.cursor()
# id = int(input("enter your id"))
# name = input("enter your name ")
# age = int(input("enter your age "))
# city = input("enter your city ")
# data = [id, name, age, city]

# cr.execute("insert into student values(%s,%s,%s,%s)", data)
# cr.execute("update student set name='rajeev' where id =107")

# con.commit()

query = "SELECT * FROM student"

cr.execute(query)
results = cr.fetchall()

for row in results:
    print(row)

con.commit()
cr.close()
con.close()
