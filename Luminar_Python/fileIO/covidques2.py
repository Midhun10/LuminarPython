#total number of cases high state
fin=open("complete.csv","r")
i=0
dict={}
for lines in fin:
# 2020 - 01 - 30, Kerala, 10.8505, 76.2711, 1, 0, 0, 0, 0, 0
    report = lines.rstrip("\n").split(",")
    #print(report)
    state = report[1]
    cases = int(report[4])
    if (state not in dict):
        dict[state] = cases
    else:
        dict[state] = cases
print(dict)

# caseslist=[]
# srtlist=[]
# for k,v in dict.items():
#     caseslist.append(v)
#     d=max(caseslist)
#     if (d == v):
#         f=[k,v]
#     srtlist.append((v,k))
# print(srtlist)
# sorteddate=sorted(srtlist) #or sorteddate=sorted(srtlist,reverse=True)
# print(sorteddate[-3:])  # or print(sorteddate[3])
# print("The largest confirmed cases state",f)


