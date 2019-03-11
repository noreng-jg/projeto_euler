def find_greatest_prime(n):
    p=2
    acum=1
    list=[]
    while acum!=n:
        if n%p==0:
            acum*=p
            list.append(p)
        p+=1
    return max(list)		
                        
print(find_greatest_prime(600851475143))
