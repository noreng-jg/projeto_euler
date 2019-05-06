primes_list=[2,3]

def isprime_number(number):
    for prime in primes_list:
        if number%prime==0:#not prime
            return False
    primes_list.append(number)
    return True
            
for i in range(5,100000): #very long prime_range generation
    isprime_number(i)

def tn(posicao, soma=0):# triangular number
    for number in range(1, posicao+1):
        soma+=number
    return soma

def factorize(number, prod=1):#Divisor function 
    factors_sequence=[]
    iterator=iter(primes_list)
    primo_atual=next(iterator)
    while number !=1:
        if number%primo_atual==0:  
            number/=primo_atual
            factors_sequence.append(primo_atual)
        else:
            primo_atual=next(iterator)
    dict_divisor={factor:factors_sequence.count(factor)+1 for factor in set(factors_sequence)}
    
    for value in dict_divisor.values():
        prod*=value
        
    return prod #return quantity of divisors

def itsover500(n=1):
    while True:
        if factorize(tn(n))>500:
            print (tn(n))
            break
        n+=1

itsover500()


