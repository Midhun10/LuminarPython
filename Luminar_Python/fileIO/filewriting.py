f=open("abc.txt","r")
# f.write("Hello world")
#
# lst=["helo","hai","how"]
# for i in lst:#for getting datas from list
#     f.write("\n"+i+"\n")
fw=open("out.txt","w") # w for write mode A new file will be created automatically

for data in f:
    num=int(data)
    if(num%2==0):
        fw.write(str(num)+"\n") # for converting values into string and also for new line


