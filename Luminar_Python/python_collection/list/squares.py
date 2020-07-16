lst=[]
line=0
num=int(input("Enter the length of the list"))
for i in range(0,num):
    line=line+1
    lst.append(line)

even=[]
odd=[]

for i in lst: # this could also be writen as even=[i for i in lst if i %2 ==0]
    if (i%2==0):
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)

def squa(even):
    squares=[]
    for item in even:
        squares.append(item**2)
    return squares

evensquares=squa(even)
oddsquares=squa(odd)
print("EvenSqu",evensquares)
print("Odd Squa",oddsquares)