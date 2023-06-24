import numpy as np
from os import system

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


dict_nome_produtos = {"pão d'agua" : ["pão", 0.99, 100]}

dict_codigo_produtos = {}

dict_registro_vendas = {}

def alternativas_inicio():
    escolha = None
    while escolha not in [1, 2, 3, 4, 5]:
        escolha = int(input('Escolha uma das opções: \n1 - Cadastrar Produto \n2 - Realizar Venda \n3 - Alterar Produto \n4 - Relatórios  \n5 - Sair \n'))
    return escolha


resposta = alternativas_inicio()


if resposta == 5:
        print('Te vejo em breve!!!')



while(True):

    if resposta == 1:


        while(True):
            print('\nMuito bem, vamos começar o cadastro. ')

            lista_tipo_preço_estoque = []
            
            indentificador_do_produto = input('Qual o código você deseja colocar no produto? ')
            nome_produto = input('Qual o nome do produto? ')
            tipo_produto = input('Qual o tipo do produto? ')
            preço_produto = float(input('Qual o preço do produto? '))
            estoque_produto = int(input('Qual o estoque incial do produto? '))

            # Sobre o indentificador de produtos, não conseguimos integrar ele no codigo da maneira correta.

            
            lista_tipo_preço_estoque.append(tipo_produto)
            lista_tipo_preço_estoque.append(preço_produto)
            lista_tipo_preço_estoque.append(estoque_produto)
            
            dict_nome_produtos.update({nome_produto : lista_tipo_preço_estoque})

            dict_codigo_produtos.update({indentificador_do_produto : nome_produto})


            repitir = input('Deseja adicionar outro produto?(S/N) ')
            if repitir == 'S':
                pass
            elif repitir == 'N':
                break
        alternativas_inicio()




    elif resposta == 2:

        nome_venda = input('Qual produto você deseja realizar a venda?(Nome) ')
        confirmação_estoque = dict_nome_produtos.get(nome_venda)
        quant_estoque = confirmação_estoque[2]
        quant_venda = int(input('Quantos {} você deseja vender? '.format(nome_venda))) 
        

        
        if quant_venda > quant_estoque:
            print('Você tem {} {} em estoque'.format(quant_estoque, nome_venda))
            print('Não há estoque suficiente para esse produto...')
        
        
        else:
            dict_registro_vendas.update({nome_venda : quant_venda})
            quant_estoque = quant_estoque - quant_venda
            dict_nome_produtos.update({nome_venda : [confirmação_estoque[0], confirmação_estoque[1], quant_estoque]})
        print('Sobrou {} no estoque'.format(quant_estoque))
        print(dict_registro_vendas)   
        # o problema atual é que o registro de vendas está atualizando, porém, ele apaga os dados das ultimas transações

  

        repitir2 = input('Deseja vender outro produto?(S/N) ')
        if repitir2 == 'S':
            pass
        elif repitir2 == 'N':
            break
    alternativas_inicio()

    
            


print(dict_nome_produtos)
print(dict_codigo_produtos),