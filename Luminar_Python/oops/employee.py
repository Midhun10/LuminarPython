class Employee:
    def __init__(self,eid,name,desig,sal,exp):
        self.eid=eid
        self.name=name
        self.desig=desig
        self.sal=sal
        self.exp=exp
    def printEmployee(self):
        print(self.eid,":",self.name,":",self.desig,":",self.sal,":",self.exp)
emp=[]
f=open("emp.txt")
for data in  f:
    #print(data)
    employee=data.rstrip("\n").split(",")
    eid=employee[0]
    name=employee[1]
    desig=employee[2]
    sal=int(employee[3])
    exp=employee[4]
    # if(sal>75000):
    #     ob=Employee(eid,name,desig,sal,exp)
    #     ob.printEmployee()
    # else:
    #     pass
    ob = Employee(eid, name, desig, sal, exp)
    ob.printEmployee()
    emp.append(ob)

for employee in emp:
    if(employee.sal>75000):
        nam=employee.name.upper()
        print("Name of employee having salary >75.",nam)
