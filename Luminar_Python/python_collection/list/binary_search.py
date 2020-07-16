lst=[10,40,30,2,5,60,23,56]
# line=0
# num=int(input("Enter the length of the list"))
# for item in range(0,num):
#     line=line+1
#     lst.append(line)
print(lst)
lst.sort()
print(lst)
low=0
upper=len(lst)-1
element=int(input("Enter the element to be searched"))
while(low<upper):
    mid=(low+upper)//2
    print(lst[mid])
    if(element<lst[mid]):
        upper=mid-1
    elif(element==lst[mid]):
        print("Element Found")
        break
    elif(element>lst[mid]):
        low=mid+1
