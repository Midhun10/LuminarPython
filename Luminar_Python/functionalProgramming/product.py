class Product:
    def __init__(self,id,name,category,price):
        self.id=id
        self.name=name
        self.category=category
        self.price=price
    def __str__(self):
        return self.name
lst=[]
ob=lst.append(Product(1001,"Galaxy","Chocolate",210))
ob=lst.append(Product(1002,"Lux","Soap",45))
ob=lst.append(Product(1003,"Milma","Milk",23))
ob=lst.append(Product(1004,"666Rice","Rice",310))

for item in lst:
    print(item)
# def con(name):
#     return name.upper()
# print(con("midhun"))

up=list(map(lambda Product:(Product.name.upper()),lst))
print(up)
price=list(filter(lambda Product:Product.price>50,lst))
for value in price:
    print(value.price)


# above=list(filter(lambda ,lst))
# print(above)

