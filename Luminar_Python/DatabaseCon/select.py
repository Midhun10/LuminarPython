import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="megha",
    database="Luminar"
)

cursor=db.cursor()

sql="""select * from employee where age>=23"""
try:
    cursor.execute(sql)
    data=cursor.fetchall()
    for lines in data:
        print(lines)
except Exception as e:
    print(e.args)

db.close()
