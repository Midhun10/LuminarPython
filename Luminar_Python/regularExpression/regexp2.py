import re

x='kl[0-9]{2}[a-z]{2}[0-9]{4}'
# x='kl\d{2}[a-z]*\d{4}'
x='kl\d{2}[a-z]{2}\d{4}'
x='\d{10}' #phone number
x='[a-zA-z]\w*@gmail[.]com'
vname=input("Enter the variable")

match=re.fullmatch(x,vname)

if(match!=None):
    print("valid")
else:
    print("invalid")