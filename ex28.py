cont = 1
numerador = 1
denominador = 1
s = 0
while cont <= 50:
    s += numerador / denominador
    numerador += 2
    denominador += 1
    cont = cont + 1
    print(s)

print(f"RESULTADO FINAL: {s:.2f}")