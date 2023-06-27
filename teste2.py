import json

mdict = {"nome" : "paulo", 
         "idade" : 30,
         "cidade" : "criciuma",
         "Bomba" : "deca"
         }

with open("mdict.json", "w") as arquivo:
    json.dump(mdict, arquivo)

with open("mdict.json", "r") as arquivo:
    dicionario_carregado = json.load(arquivo)




mudança = int(input('oq vc quer mudar? '))

if mudança == 2:
    novo_nome = input("qual o nova idade? ")
    mdict.update({"idade" : novo_nome})






with open("mdict.json", "w") as arquivo:
    json.dump(mdict, arquivo)

with open("mdict.json", "r") as arquivo:
    dicionario_carregado = json.load(arquivo)


print(dicionario_carregado)