num1=int(input("Enter num1"))
num2=int(input("Enter num2"))
# res=num1/num2#exception can be raised in this code.
# print(res)
try:
    res=num1/num2
    print(res)
except Exception as e:#Exception is a class in the
    # print("exception occured")
    print("Error:",e.args)

finally:
    print("Printing finally")

# if(age<18):
#     raise Exception("invalid Age") used for raiseing custom exception or userdefined
# else:
#     print("U can vote")