import numpy as np ### usamos para criar o gerador de codigos
import json   ### vamos usar para registrar os dados
from os import system ### usamos para limpar a tela nas trocas de ações

dict_produtos = {2814: ['Pão Francês', 'Pão', 2.5, 50],
                  3940: ['Bolo de Chocolate', 'Bolo', 25.0, 10],
                  6528: ['Croissant', 'Salgado', 3.0, 20],
                  4015: ['Rosquinha', 'Doce', 1.5, 30],
                  1778: ['Pão de Queijo', 'Salgado', 2.0, 40],
                  2641: ['Torta de Morango', 'Torta', 30.0, 5],
                  5388: ['Cookie', 'Doce', 1.0, 15],
                  1516: ['Pão Integral', 'Pão', 3.0, 25],
                  3709: ['Pastel de Carne', 'Salgado', 2.5, 10],
                  1978: ['Bolo de Cenoura', 'Bolo', 20.0, 8],
                  9487: ['Sonho de Creme', 'Doce', 2.0, 12],
                  6067: ['Pão de Alho', 'Salgado', 2.5, 18], 
                  2474: ['Biscoito de Aveia', 'Doce', 1.5, 20], 
                  1993: ['Pão Australiano', 'Pão', 3.5, 15], 
                  5414: ['Coxinha', 'Salgado', 2.0, 25], 
                  8635: ['Água', 'Ingrediente', 1.0, 100],
                  5629: ['Farinha de Trigo', 'Ingrediente', 3.0, 50], 
                  1898: ['Fermento', 'Ingrediente', 2.5, 30],
                  9985: ['Açúcar', 'Ingrediente', 2.0, 40], 
                  9858: ['Leite', 'Ingrediente', 2.0, 35], 
                  2882: ['Ovos', 'Ingrediente', 1.5, 60], 
                  8007: ['Manteiga', 'Ingrediente', 3.0, 25], 
                  990: ['Sal', 'Ingrediente', 1.0, 75], 
                  3760: ['Chocolate em Pó', 'Ingrediente', 4.0, 15],
                  742: ['Fermento Biológico', 'Ingrediente', 2.0, 20],
                  7193: ['farinha', 'po', 10.87, 1000]}

with open("dict_produtos.json", "w") as arquivo:
    json.dump(dict_produtos, arquivo)

with open("dict_produtos.json", "r") as arquivo:
    dicionario_carregado = json.load(arquivo)


mudança = int(input('oq vc quer mudar? '))

if mudança == 2:
    novo_nome = input("qual o nova idade? ")
    dict_produtos.update({ 2814 : novo_nome})




with open("dict_produtos.json", "w") as arquivo:
    json.dump(dict_produtos, arquivo)

with open("dict_produtos.json", "r") as arquivo:
    dicionario_carregado = json.load(arquivo)


print(dicionario_carregado)

