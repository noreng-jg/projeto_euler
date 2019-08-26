def divisor_int(number):
    divisors_list=[]
    half=number/2 if number%2==0 else (number-1)/2
    while number!=1:
        try:
            if number%half==0:
                divisors_list.append(half)
            half-=1
        except ZeroDivisionError:
            break
    return divisors_list

def amicable(number, check=False, _tuple=(None, None)):
    var=sum(divisor_int(number))
    if number==sum(divisor_int(var)) and number!=var:
        check=True
        _tuple=number, var 
    else:
        check=False
    return {'check':check, 'amicables':_tuple}

_list=[]

for index in range(1,10000):
    if not index in _list: 
        if amicable(index)['check']:
            _list.append(amicable(index)['amicables'][0])
            _list.append(amicable(index)['amicables'][1])

print (sum(_list))