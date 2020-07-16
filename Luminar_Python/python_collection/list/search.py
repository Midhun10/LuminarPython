lst=[]
line=0
num=int(input("Enter the length of the list"))
for item in range(0,num):
    line=line+1
    lst.append(line)
print(lst)

element=int(input("Enter element for searching"))
flag=0
for item in lst:
    if(item==element):
        flag=1
        break

if(flag==0):
    print("Em not f")
else:
    print("found at position")
