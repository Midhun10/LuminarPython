# 1. read this file and create employee objects
# 2.find out maximum salary from employee objects
# 3.write valid mails into a new file
# 4.create a mysql table and store this record and loads this data into table
# # 5.find desgination wise count from the table using mysql query.
# upload folder into git

import functools
class Employee:
    def __init__(self,eid,ename,edesig,mailid,salary):
        self.eid=eid
        self.ename=ename
        self.edesig=edesig
        self.mailid=mailid
        self.salary=salary
    def PrintEmployee(self):
        print(self.eid,":",self.ename,":",self.edesig,":",self.mailid,":",self.salary)

emplist=[]

f1=open("employee","r")
for lines in f1:
    employee=lines.rstrip("\n").split(",")
    # print(employee)
    eid=employee[0]
    ename=employee[1]
    edesig=employee[2]
    mailid=employee[3]
    salary=employee[4]

    ob=Employee(eid,ename,edesig,mailid,salary)
    ob.PrintEmployee()
    emplist.append(ob)

sal=functools.reduce(lambda o1,o2 : o1 if o1>o2 else o2,list(map(lambda o1:o1.salary,emplist)))
print(sal)


