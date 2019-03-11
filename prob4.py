from numpy import prod
a=100
b=100
l=[]

def palindrome_pair_finder(a,b,l):
    while(a<1000):
        while(b<1000):
            if str(a*b)==str(a*b)[::-1]:
                 l.append([a,b])
            b+=1
        b=100
        a+=1
        
def greater_list_of_the_list(l):
    list2=[]
    
    #making a list of the sums
    for i in range(len(l)):
        temp_sum=0
        for j in range(len(l[i])):
            temp_sum+=l[i][j]
        list2.append(temp_sum)
        temp_sum=0

    return l[list2.index(max(list2))]


    
palindrome_pair_finder(a,b,l)
print(prod(greater_list_of_the_list(l)))

