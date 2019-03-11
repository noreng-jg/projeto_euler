#sum of multiple 3 or 5 until 1000

def is_multiple(value):
    return value%3==0 or value%5==0

def find_sum(n):
    i=0
    _sum=0
    while i<n:
        if is_multiple(i):
            _sum+=i
        i+=1
    return _sum

print (find_sum(1000))
