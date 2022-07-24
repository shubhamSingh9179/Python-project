import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="collage"
)
mycursor = mydb.cursor()

mycursor.execute("select * from t1")

myresult = mycursor.fetchall()

for x in myresult:
    print (x)