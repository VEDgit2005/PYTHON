price= (29.95,4.5,15.5,4.5)
print(len(price))
print(price.count(4.5))
print(4.5 in price)
#print(1.4 in price)
for x in price:
    print(x)
#price.add(20) , we cant add or update or even sort because tiple is immutable....  
print(price)