#constructor calls/invoked when the object is created.
#constructor duty is to invoke instance varibale.
#called using __init__
class Student:
    def __init__(self,name,rol,course):
        self.name=name
        self.rol=rol
        self.course=course
    def printValues(self):
        print(self.name,":",self.rol,":",self.course)

ob=Student("Midhun",1001,"DDMCA") # constructor calls automatically
ob.printValues()
