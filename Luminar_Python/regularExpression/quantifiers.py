import re

x="a+"
x="a*" #counts a but also takes the place of non a okay.
x="a?" #counts indivudally  but matchs the other positions as well.
x="a{2,3}"
matcher=re.finditer(x,"aaaabbbaaaaababbaaaaa")
count=0

for match in matcher:

    print(match.group())
    print(match.start())

