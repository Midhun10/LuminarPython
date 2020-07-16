import mysql.connector #importing package
db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="megha",

)#databse connection

cursor=db.cursor() #object creation
cursor.execute("SELECT VERSION()") #Sql code execution
data=cursor.fetchone() #
print("Database version:",data)
db.close