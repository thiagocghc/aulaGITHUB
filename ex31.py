salario = 4000 #SALARIO INICIAL
ano = 2021     #CONTADOR 
aumento = 0.015 #PERCENTUAL

while ano <= 2024:
    print(f"PERCENTUAL {aumento} ANO: {ano}")
    salario += salario * aumento
    aumento *= 2  ####VALOR ATUAL x2
    print("NOVO SALARIO: ",salario)
    ano = ano + 1