import re

#predefined charcaters
x='\s' #chck for space
x='\d' #chck for digits
x='\D' #chck for non digits
x='\w' # chck for words
x='\W' #chck for except words


matcher=re.finditer(x,"ab9k _@72#")
count=0

for match in matcher:

    print(match.group())
    print(match.start())