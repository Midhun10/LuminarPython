f1=open("complete.csv","r")
coviddata={}
for lines in f1:
    report=lines.rstrip("\n").split(",")
    # Date,Name of state ,Latitude, Longitude ,Total Confirmed cases ,Death,Cured / Discharged / Migrated ,New cases, New deaths ,New recovered
    # print(report)
    date=report[0]
    state=report[1]
    lati=report[2]
    long=report[3]
    confirmed=report[4]
    death=report[5]
    cured=report[6]
    newcases=report[7]
    newdeath=report[8]
    newrecovered=report[9]
    if(lines not in coviddata):
        coviddata[state]={"Date":date,"State":state,"Latitude":lati,"Longitude":long,"Confirmed":confirmed,"Death":death,"Cured":cured,"NewCases":newcases,"NewDeaths":newdeath,"NewRecovered":newrecovered}
    else:
        pass
print(coviddata)
for k,v in coviddata.items():
    print(k,":",v,"\n")


def getValues(**kwargs):

    if "State" in kwargs:
        State = kwargs["State"]
        if (State in coviddata):
            print("State : ", coviddata[State]["State"])
            # break
        else:
            print("No Covid data / No State found for  ", State)
    if "property" in kwargs:
        prop = kwargs["property"]
        print(prop, ":", coviddata[State][prop])

getValues(State="State",property="Death")





