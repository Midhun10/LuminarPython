f=open("students.txt","r")
p=open("passed.txt","r")

fw=open("failed.txt","w")
# lst=[]
# lst1=[]
# st3=set()
# for data in f:
#    lst=[data]
#    print(lst)
# for item in p:
#     lst1=[item]
#     print(lst1)
#     st1=set(lst)
#     st2=set(lst1)
#     st3=st1-st2
#     print("diff",st3)
st1=set()
st2=set()
def readDataFromFile(fref): # Func to check for
    st=set()
    for data in fref:
        data=data.rstrip("\n")
        st.add(data)
    return st
st1=readDataFromFile(f)
st2=readDataFromFile(p)
print(st1)
print(st2)
fail=st1-st2
print(fail)
for data in fail:
    fw.write(data+"\n")





