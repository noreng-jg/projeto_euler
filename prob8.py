def product_of_sequence(_list, r=1):
    for i in _list:
        r*=i 
    return r

num_str=open('prob8.txt').read().replace('\n','')

_arrays=[]

for i in range(len(num_str)):
    temp_array=num_str[i:i+13]
    if len(temp_array)==13:
        _arrays.append(temp_array)

numerical=[]

for _array in _arrays:
    numerical.append([int(x) for x in list(_array)])

prods=[product_of_sequence(y) for y in numerical]

print(max(prods))
