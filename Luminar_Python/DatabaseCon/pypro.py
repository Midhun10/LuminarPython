import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="megha",
    database="Luminar"
)

cursor=db.cursor()

sql="""INSERT INTO employee values("Midhun","Benny",22,'M')"""
try:
    cursor.execute(sql)
    db.commit()
except Exception as e:
    #print(e.args)
    db.rollback() # partial changes are undone
finally:
    db.close()