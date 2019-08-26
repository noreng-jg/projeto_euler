names_list=open('prob22').read().split(',')
nomes=[nome.replace('\"','') for nome in names_list]
nomes.sort()
alfa=['A','B','C',"D","E","F",'G','H','I','J','K','L','M',"N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numeric=[i+1 for i in range(26)]
dici=dict(zip(alfa,numeric))

def number_name(_string,s=0):
    for char in _string:
        s+=dici[char]
    return s

soma_total=0

for nome in nomes:
    soma_total+=number_name(nome)*(1+nomes.index(nome))

print(soma_total)
