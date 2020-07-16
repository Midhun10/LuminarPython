# convert all employee name into upper case
# print employee salary greater than 1500
# provide increment of 5000 for all employee who have experience greater than or equal to 2
# list all employee designation equal to developer

class Employees:

    def __init__(self, id, name, desig, sal, exp):
        self.id = id
        self.name = name
        self.desig = desig
        self.sal = sal
        self.exp = exp

    def printEmp(self):
        print(self.id, ":", self.name, ":", self.desig, ":", self.sal, ":", self.exp)

    def __str__(self):
        return self.name

emp = []
f = open("emp.txt")
for data in f:
    employee = data.rstrip("\n").split(",")
    id=employee[0]
    name=employee[1]
    desig=employee[2]
    sal=int(employee[3])
    exp=int(employee[4])
    ob = Employees(id,name,desig,sal,exp)
    ob.printEmp()
    emp.append(ob)

print("\n")

#name to upper case
name=list(map(lambda Employees:Employees.name.upper(),emp))
print(name)

print("\n")

#salary greater than 59000
salary=list(filter(lambda Employees:Employees.sal>59000,emp))
for value in salary:
    print(value)

print("\n")

#incremnt of 5000 if exp>=2
incr=list(filter(lambda Employees:Employees.exp>=2,emp))
for value in incr:
    print(value,":",value.sal)
    sal=value.sal+5000
    print("Updated : ",sal)

print("\n")

#name if desig=developer
des=list(filter(lambda Employees:Employees.desig=="developer",emp))
for value in des:
    print("Developer:",value)
