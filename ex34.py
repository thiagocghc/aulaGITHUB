lista = []
par = []
impar = []

i = 0
while i < 20:
    num = int(input("DIGITE UM NUMERO: "))
    lista.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    i = i + 1

print(lista)
print(par)
print(impar)