def fibo(n,i=1):
    l=[1]
    l.append(1)
    while(True):
        if l[i]>n:
            break
        else:
            l.append(l[i]+l[i-1])
            i+=1
    return l[:-1]
    
#bool for even function            
def even(n):
    return n%2==0

#retrieve the sum of the even values of a given list
def sum_even_list(l,the_sum=0):
    for i in range(len(l)):
        if even(l[i]):
            the_sum+=l[i]   
    return the_sum

print(sum_even_list(fibo(4000000)))

    
