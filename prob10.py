from math import sqrt
p=[2,3]

def prime(_list, num):
    for element in _list[:int(sqrt(num))]:
        if num%element==0:
            return False
    return True

for i in range(4,2000000):
    if prime(p, i):
        p.append(i)

#Even with the optimization of the square root value, it takes a while to compute...
        
print(sum(p))
