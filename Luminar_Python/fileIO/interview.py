f1=open("person.txt","r")
emp = {}
emp2 = {}
for items in f1:
    report=items.rstrip("\n").split(",")
    #print(report)
    id=report[0]
    name=report[1]
    age=report[2]
    designation=report[3]
    experience=report[4]
    salary=report[5]
    if(items not in emp):
        emp={"ID":id,"Name":name,"Age":age,"Designation":designation,"Experience":experience,"Salary":salary}
    else:
        pass
    emp2[id]=emp
for k,v in emp2.items():
    print(k,":",v)


def printEmployee(**kwargs):
        for k, v in kwargs.items():
            id = v
            prop = kwargs["property"]
            if (id in emp2):
                print("Name : ", emp2[id]["Name"])
                print(prop, ":", emp2[id][prop])
                break
            else:
                print("Employee not found with ", id)


printEmployee(id="1001")









