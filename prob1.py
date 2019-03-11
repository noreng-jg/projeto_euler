#Soma de multiplos de 3 ou 5 ate 1000

def eh_multiplo(valor):
    return valor%3==0 or valor%5==0

def acha_soma(n):
    i=0
    soma=0
    while i<n:
        if eh_multiplo(i):
            soma+=i
        i+=1
    return soma

print (acha_soma(1000))