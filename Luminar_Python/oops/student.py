class Students:
    def __init__(self,sid,name,course,total):
        self.sid=sid
        self.name=name
        self.course=course
        self.total=total

    def printStudent(self):
        print(self.sid,":",self.name,":",self.course,":",self.total)
stud=[]
f=open("students.txt")
for data in f:
    print(data)
    student=data.rstrip("\n").split(",")
    sid=student[0]
    name=student[1]
    course=student[2]
    total=int(student[3])
    ob = Students(sid,name,course,total)
    ob.printStudent()
    stud.append(ob)
for studs in stud:
    if(studs.course=="MCA"):
        print(studs.name)