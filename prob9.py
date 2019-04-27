from math import floor, sqrt

def is_perfect(n):
    return n-floor(n)==0

a=[x**2 for x in range(1,1000)]
b=[x**2 for x in range(1,1000)]

perfect_cs={}

for i in a:
    for j in b:
        c=sqrt(i+j)
        if is_perfect(c) and sqrt(i)<sqrt(j) and sqrt(j)<c:
            perfect_cs[(sqrt(i),sqrt(j))]=c


for key in perfect_cs.keys():
    if key[0]+key[1]+perfect_cs[key]==1000:
        print (key[0]*key[1]*perfect_cs[key])
