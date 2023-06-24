import numpy as np
import json
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

dict_codigo_produtos = {}

dict_registro_vendas = {}




def escrita_campo_correta(phrase, data_type): ### assegura que as variaveis estão corretas.
    answer = None
    case_condition = False
    while answer == None or case_condition != True or answer == '':
        try:
            answer = input(phrase)
            if data_type == 'int':
                answer = int(answer)
                case_condition = True
            elif data_type == 'float':
                answer = float(answer)
                case_condition = True
            elif data_type == 'string':
                case_condition = True
            assert answer != ''
        except (ValueError, AssertionError):
            print('Digite de acordo com tipo de unidade.')
    return answer


def alternativas_alteração(): ### alterar alguma coisa
    escolha_alterar = None
    while escolha_alterar not in [1, 2, 3, 4, 5]:
        escolha_alterar = int(input('Você deseja alterar o que? \n 1-Codigo \n 2-Nome \n 3-tipo \n 4-valor \n 5-estoque '))
    return escolha_alterar


def alternativas_inicio(): ### gerar a tela inicial
    escolha = None
    while escolha not in [1, 2, 3, 4, 5]:
        escolha = int(input('Escolha uma das opções: \n1 - Cadastrar Produto \n2 - Realizar Venda \n3 - Alterar Produto \n4 - Relatórios  \n5 - Sair \n'))
    return escolha





def gerando_codigo(): # gera automaticamente um id entre 1 e 10000 único
    codigo = None
    while codigo in list(dict_produtos.keys()) or codigo == None:
        codigo = np.random.choice(np.arange(0,10_000))
    return codigo


def checando_produto_dicionario(nome): # verifica se existe produto com o nome no banco de dados
    for i in list(dict_produtos.keys()):
        if nome == dict_produtos[i][0]:
            return i
    return False



while (True):

    resposta = alternativas_inicio() ### variavel resposta para o menu inicial



    if resposta == 5: ### codigo para encerramento
        print('Te vejo em breve!!!')
        break






    elif resposta == 1: ### codigo para cadastrar produto
        
        system("cls") ### limpa o terminal

        while(True): ### loop para recadastro
            print('\nMuito bem, vamos começar o cadastro. ')

            lista_tipo_preço_estoque = []
                
            indentificador_do_produto = gerando_codigo()
            
            print(indentificador_do_produto)
            
            nome_produto = escrita_campo_correta('Qual o nome do produto? ', 'string')
            tipo_produto = escrita_campo_correta('Qual o tipo do produto? ', 'string')
            preço_produto = escrita_campo_correta('Qual o preço do produto? ', 'float')
            estoque_produto = escrita_campo_correta('Qual o estoque incial do produto? ', 'int')


            lista_tipo_preço_estoque.append(nome_produto) 
            lista_tipo_preço_estoque.append(tipo_produto)
            lista_tipo_preço_estoque.append(preço_produto)
            lista_tipo_preço_estoque.append(estoque_produto)
                
            dict_produtos[indentificador_do_produto] = lista_tipo_preço_estoque

            dict_codigo_produtos.update({indentificador_do_produto : nome_produto})

            print('Cadastro Realizado com sucesso!!!!')

            repitir = input('Deseja adicionar outro produto?(S/N) ')
            if repitir.upper() == 'S':
                pass
            elif repitir.upper() == 'N':
                break     
        



    elif resposta == 2:
        
        system("cls") ### limpa o terminal
        

        while (True):
            nome_venda = escrita_campo_correta('Qual produto você deseja realizar a venda?(nome) ', 'string')
            
            if checando_produto_dicionario(nome_venda) == False:
                print('Produto não encontrado!!!')
            else:

                lista_codigo_produto = dict_produtos.get(checando_produto_dicionario(nome_venda))
                quant_estoque = lista_codigo_produto[3]
                quant_venda = int(input('Quantos {} você deseja vender? '.format(nome_venda)))
                

                
                if quant_venda > quant_estoque:
                    print('Você tem {} {} em estoque'.format(quant_estoque, nome_venda))
                    print('Não há estoque suficiente para esse produto...')
                
                
                else:
                    dict_registro_vendas.update({nome_venda : quant_venda})
                    quant_estoque = quant_estoque - quant_venda
                    dict_produtos.update({checando_produto_dicionario(nome_venda) : [lista_codigo_produto[0], lista_codigo_produto[1], lista_codigo_produto[2], quant_estoque]})
                print('Sobrou {} no estoque'.format(quant_estoque))
                print(dict_registro_vendas)  
                print('Venda realizada com sucesso!!!')
                # o problema atual é que o registro de vendas está atualizando, porém, ele apaga os dados das ultimas transações
            
            repitir2 = input('Deseja vender outro produto?(S/N) ')
            if repitir2.upper() == 'S':
                pass
            elif repitir2.upper() == 'N':
                break

    
    elif resposta == 3:
       
       
        while (True):
            decidir_modo_alterção = escrita_campo_correta('Você quer pesquisar o produto pelo código ou pelo nome?(C / N) ', 'string')

            if decidir_modo_alterção.upper() == 'C':

                produto_codigo_alteração = escrita_campo_correta('Qual produto você deseja realizar a alteração? ', 'int')

                if produto_codigo_alteração not in dict_produtos.keys():
                    print('Codigo invalido!!!')


                else:
                    escolha_alteração = alternativas_alteração()

                    if escolha_alteração == 1:
                        lista_codigo_produto = dict_produtos.get(produto_codigo_alteração)
                        novo_codigo = escrita_campo_correta('qual o numero do novo codigo? ', 'int')
                        dict_produtos.update({novo_codigo : [lista_codigo_produto[0], lista_codigo_produto[1], lista_codigo_produto[2], lista_codigo_produto[3]]})
                        dict_produtos.pop(produto_codigo_alteração)
                        print(dict_produtos)


                repitir2 = input('Deseja fazer outra alteração?(S/N) ')
                if repitir2.upper() == 'S':
                    pass
                elif repitir2.upper() == 'N':
                    break







            elif decidir_modo_alterção.upper() == 'N':

                produto_nome_alteração = escrita_campo_correta('Qual produto você deseja realizar alteração? ', 'string')
                
                if checando_produto_dicionario(produto_nome_alteração) == False:
                    print('Produto não encontrado!!!')
                
                else:
                    escolha_alteração = alternativas_alteração()
                    
                    if escolha_alteração == 1:
                        lista_nome_produto = dict_produtos.get(checando_produto_dicionario(produto_nome_alteração))
                        novo_codigo = escrita_campo_correta('qual o numero do novo codigo? ', 'int')
                        dict_produtos.update({novo_codigo : [lista_nome_produto[0], lista_nome_produto[1], lista_nome_produto[2], lista_nome_produto[3]]})
                        dict_produtos.pop(checando_produto_dicionario(produto_nome_alteração))
                        print(dict_produtos)

                
                repitir3 = input('Deseja fazer outra alteração?(S/N) ')
                if repitir3.upper() == 'S':
                    pass
                elif repitir3.upper() == 'N':
                    break

print(dict_produtos)


    