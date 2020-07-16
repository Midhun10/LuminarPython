f1 = open("person.txt", "r")
emp = {}
for items in f1:
    report = items.rstrip("\n").split(",")
    # print(report)
    id = report[0]
    name = report[1]
    age = report[2]
    designation = report[3]
    experience = report[4]
    salary = report[5]
    if (items not in emp):
        emp[id] = {"ID": id, "Name": name, "Age": age, "Designation": designation, "Experience": experience,
                   "Salary": salary}
    else:
        pass
for k, v in emp.items():
    print(k, "\t", v)


def printEmployee(**kwargs):
    # for k, v in kwargs.items():
    if "id" in kwargs:
        id = kwargs["id"]
        if (id in emp):
            print("Name : ", emp[id]["Name"])
            # break
        else:
            print("Employee not found with ",id)
    if "property" in kwargs:
        prop = kwargs["property"]
        print(prop, ":", emp[id][prop])

printEmployee(id="1001",property="Salary")

#covid dataset

# {kerala:{state:kerala,confirmedcases:3000,cured:2500,death:15}}
# getValues(name="Kerala",property="death")

