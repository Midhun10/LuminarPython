#total cases in the country
fin=open("complete.csv","r")
i=0
total=0
dict={}
for lines in fin:
    # 2020 - 01 - 30, Kerala, 10.8505, 76.2711, 1, 0, 0, 0, 0, 0
    report = lines.rstrip("\n").split(",")
    print(report)
    state = report[1]
    cases = int(report[4])
    if(state not in dict):
        dict[state]=cases
    else:
        dict[state]=cases
        #total+=cases

print(dict)

caseslist=[]

for k,v in dict.items():
    caseslist.append(v)
    total+=v #other method usual one
print(sum(caseslist))
print("total cases",total)