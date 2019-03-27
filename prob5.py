from numpy import prod

until_20=list(range(1,21))
products=[]

for i in until_20:
    for j in products:
        if(i%j==0):
            i=i/j
    products.append(i)

result=prod(products)

print(int(result))
