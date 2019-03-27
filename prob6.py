def dif_sqr(_max, sum_of_squares=0, _sum=0):
    for i in range(1,_max+1):
        sum_of_squares+=i**2
        _sum+=i
    return _sum**2 - sum_of_squares

print(dif_sqr(100))
