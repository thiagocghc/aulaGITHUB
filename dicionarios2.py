empresa = {'razaosocial': 'P & P LTDA',
           'tipo':'Prog de Sites', 
           'CNPJ': 1231456464, 
           'cidade': 'São Paulo',
           'filial':'Tatuapé'
           }

# for key in empresa.keys():
#     print(key)

# print()
# for value in empresa.values():
#     print(value)

for key,value in empresa.items():
    print(key," : ",value)


del empresa['cidade']

empresa['telefone'] = '11 96666-6666'

print()

for key,value in empresa.items():
    print(key," : ",value)




