lst=[]
line=0
num=int(input("Enter the length of the list"))
for item in range(0,num):
    line=line+1
    lst.append(line)
print(lst)
value=int(input("Enter the resultant value"))
for item in lst:
    for item2 in lst:
        if(item+item2==value):
            print(item,"+",item2,"=",value)
