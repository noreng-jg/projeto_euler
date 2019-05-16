"""combinational problem c_(20x2,20)=(40x39x38x...x20!)/20!x20!
"""
initial=1
size=20

for i in range(2*size,size,-1):
    initial*=i
    initial/=(i-size)

print (round(initial))
