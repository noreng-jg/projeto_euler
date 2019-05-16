def odd(number):
    if number%2==0:
        return number / 2
    else:
        return 3 * number + 1

sequence=[]

def size_sequence(number):
    if number==1:
        return len(sequence) + 1 #dont miss the one
    else:
        sequence.append(number)
        return size_sequence(odd(number))

lista_de_comprimentos=[]

d={}

for i in range(2,1000001):
    d[i]=size_sequence(i)
    sequence=[]

max_value=max(d.values())

# it takes a while to compute
for _key, _value in d.items():
    if _value == max_value:
        print (_key)


