import re
f=open("email.txt")
f2=open("rightemail.txt","w")
f3=open("wrongemail.txt","w")

email=[]

for lines in f:
    line=lines.rstrip("\n")
    # print(line)
    email.append(line)
print(email)

for data in email:
    pattern='[a-zA-Z]\w.*[_]*\w*[.]*@[a-z]*[.][a-z]{3}'
    match=re.fullmatch(pattern,data)

    if(match!=None):
        f2.write(data+"\n")
    else:
        f3.write(data+"\n")
