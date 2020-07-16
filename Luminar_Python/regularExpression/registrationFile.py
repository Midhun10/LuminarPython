import re
f=open("vehiclereg.txt")
f2=open("rightreg.txt","w")
f3=open("wrongreg.txt","w")
reg=[]
for lines in f:
    line=lines.rstrip("\n")
    reg.append(line)
print(reg)

for data in reg:

    x="KL\d{2}[A-Z]*\d{4}"
    match=re.fullmatch(x,data)
    if(match!=None):
        f2.write(data+"\n")
    else:
        f3.write(data+"\n")
