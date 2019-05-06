import numpy as np

def is_there_spaces(_list):
    for _string in _list:
        if ' ' in _string:
            return True
    return False

def clean_and_write(_list):
    with open('prob13.txt','w') as myfile:
        for line in _list:
            myfile.write(' '.join(list(line)))
    
def separated_numbers():
    with open('prob13.txt','r+') as myfile:
        lines=myfile.readlines()
        if not is_there_spaces(lines):#if there aren't spaces
            clean_and_write(lines)        

separated_numbers()
array=np.loadtxt('prob13.txt',dtype=int)
#print (array.shape)

restante=0
ultimos_digitos=[]
 
for elemento_v in range(50):
    tot=restante  
    tot+= sum(array[:,-(elemento_v+1)])
    l_d=(str(tot)[-1])
    restante=int(str(tot)[:-1])
    ultimos_digitos.append(l_d)

ultimos_digitos=reversed(ultimos_digitos)
most_sign=str(restante)
rest=''.join(ultimos_digitos)

print((most_sign+rest)[:10])
