import numpy as np

def product_list(_list, p=1):
    for num in _list:
        p*=num
    return  p

n=20

adjacent=4

a1=np.loadtxt('prob11.txt').reshape([n,n])
#reverse matrix
a2=a1[::-1]

main,horizontal, vertical, list_diagonals, inverse_diagonals=[],[],[],[],[]

for line in range(0,n-adjacent+1):
    for column in range(0,n-adjacent+1):
        horizontal.append(list(a1[line,column:column+adjacent]))
        vertical.append(list(a1[line:line+adjacent,column]))

main.extend(horizontal)
main.extend(vertical)

for i in range(0, n-adjacent+1):
    for j in range(0, n-adjacent+1):
        list_diagonals.append(list(a1[i:i+adjacent, j:j+adjacent].diagonal()))
        inverse_diagonals.append(list(a2[i:i+adjacent, j:j+adjacent].diagonal()))

main.extend(list_diagonals)
main.extend(inverse_diagonals)
#size 4 only
main=[x for x in main if len(x)==4]

products=[]
for each in main:
    products.append(product_list(each))

print(max(products))


