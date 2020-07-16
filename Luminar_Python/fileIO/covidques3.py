#total number of cured cases
fin=open("complete.csv","r")
dict={}
for lines in fin:
    report=lines.rstrip("\n").split(",")
    state=report[1]
    cured=int(report[6])
    if(state not in dict):
        dict[state]=cured
    else:
        dict[state]+=cured
print("Dic",dict)
# curedlist=[]
# for k,v in dict.items():
#     curedlist.append((v,k))
#     d=max(curedlist)
# print("Curedlist",curedlist)
# sortedlist=sorted(curedlist)
# print("Sorted List",sortedlist)
# print("highest cured rate",d)