# #Anonymous function=nameless
#
# # def add(num1,num2):
# #     return (num1+num2)
#
# f=lambda num1,num2:(num1+num2)
# print(f(10,12))
#
# f2=lambda num1,num2:(num2-num1)
#
# f3=lambda num1,num2:(num1/num2)
#
# f4=lambda num1,num2:(num1%num2)
#
# f5=lambda num1,num2:(num1**num2)
#
# print(f5(10,2))
# print(f2(10,12))
# print(f3(12,10))
# print(f4(10,12))

#map,filter
lst=[10,20,30,40,5]

sqlist=list(map(lambda num1:num1**3,lst))
print(sqlist)

even=list(filter(lambda num1:(num1%2==0),lst))
print(even)