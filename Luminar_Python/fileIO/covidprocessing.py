fin=open("complete.csv","r")
i=0
dict={}
for lines in fin:
    # 2020 - 01 - 30, Kerala, 10.8505, 76.2711, 1, 0, 0, 0, 0, 0
    report=lines.rstrip("\n").split(",")
    state=report[1]
    cases=int(report[4])
    print(report)
    if(state not in dict):
        dict[state]=cases
    else:
        dict[state]=cases
    # print("State",state)
    # print("Confirmed cases",cases)
    # i=i+1
    # if(i==50):
    #     break
print(dict)