num = int(input("DIGITE UM NUMERO: "))
i = num
cont = 0
while i >= 1:
    if num % i == 0:
        cont = cont + 1
        print(i)
    i = i - 1

print(cont)
if cont == 2:
    print(f"{num} é primo!!")
else:
    print(f"{num} não é primo!!")

