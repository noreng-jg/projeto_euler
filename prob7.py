def is_new_prime(l,t):
    for i in range(len(l)):
        if t%l[i]==0:
            return False
    return True

def core():
    l=[2,3]
    for i in range(9999):
        temp=l[len(l)-1]
        temp+=2
        while(True):
            if is_new_prime(l,temp):
                l.append(temp)
                break
            else:
                temp+=2
    return l[-1]


print(core())

