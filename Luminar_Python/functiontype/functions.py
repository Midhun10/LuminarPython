# def add(num1,num2):
#     print(num1+num2)
# add(10,20)

#we have varible length argument
# kwargs takes in as dictonary hence more understnding of the values

# def add(**kwargs):
#     print(kwargs)
#     total=0
#     for k,v in kwargs.items():
#         total+=v
#     print(total)
# add(num1=10,num2=20,num3=30,num4=40)
#
# def employee(*args): # here single * means it will read us tuple hence we won't be able to understand the values.
#     for data in args:
#         print(data)
# employee("Kochi","thrissur",33,25000)