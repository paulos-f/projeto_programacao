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
numero = 0
dict_registro_vendas = { numero : ['NOME DO PRODUTO', 'QUANTIDADE VENDIDA']}


with open("dict_produtos.json", "r") as arquivo:
    dicionario_produtos_carregado = json.load(arquivo)

dict_produtos = dicionario_produtos_carregado


with open("dict_registro_vendas.json", "r") as arquivo:
    dicionario_vendas_carregado = json.load(arquivo)

dict_registro_vendas = dicionario_vendas_carregado



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


def alternativas_alteração(): ### alterar alguma informação de um produto
    escolha_alterar = None
    while escolha_alterar not in [1,2,3,4,5]:
        try:
            escolha_alterar = int(input('Você deseja alterar o que? \n 1-Codigo \n 2-Nome \n 3-tipo \n 4-valor \n 5-estoque\n'))
            assert escolha_alterar in [1,2,3,4,5]    
        except(ValueError, AssertionError):
            print("Campo digitado errado!!!")
    return escolha_alterar


def alternativas_inicio(): ### gerar a tela inicial
    escolha = None
    while escolha not in [1, 2, 3, 4, 5]:
        try:
            escolha = int(input('Escolha uma das opções: \n1 - Cadastrar Produto \n2 - Realizar Venda \n3 - Alterar Produto \n4 - Relatórios  \n5 - Sair \n'))
            assert escolha in [1,2,3,4,5]    
        except(ValueError, AssertionError):
            print("Campo digitado errado!!!\n")
    return escolha





def gerando_codigo(): # gera automaticamente um id entre 1 e 10000 único
    codigo = None
    while codigo in list(dict_produtos.keys()) or codigo == None:
        codigo = np.random.choice(np.arange(0,10_000))
        codigo = int(codigo)
    return codigo


def checando_produto_dicionario(nome): # verifica se existe produto com o nome no banco de dados e coleta o codigo do produto caso seja colocado o nome dele
    for i in list(dict_produtos.keys()):
        if nome == dict_produtos[i][0]:
            return i
    return False


def numero_sequencia():
        numero = 0
        ultimo_valor_lista = list(dict_registro_vendas.keys())[-1]
        numero = int(ultimo_valor_lista) + 1
        return numero


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
                
            

            dict_produtos.update({indentificador_do_produto : lista_tipo_preço_estoque})


            print('Cadastro Realizado com sucesso!!!!')
           

            repitir = input('Deseja adicionar outro produto?(S/N) ')
            if repitir.upper() == 'S':
                pass
            elif repitir.upper() == 'N':
                break     
        



    elif resposta == 2:  ### codigo para realizar a venda de um produto
        
        system("cls") ### limpa o terminal
        

        while (True):
            nome_venda = escrita_campo_correta('Qual produto você deseja realizar a venda?(nome) ', 'string')
            
            if checando_produto_dicionario(nome_venda) == False: ###Verifica se o produto está no dicionario
                print('Produto não encontrado!!!')

            else:

                lista_codigo_produto = dict_produtos.get(checando_produto_dicionario(nome_venda)) ### transforma a variavel na lista correspondente ao codigo do produto
                quant_estoque = lista_codigo_produto[3]
                quant_venda = int(input('Quantos {} você deseja vender? '.format(nome_venda)))
                
                
                if quant_venda > quant_estoque: ### verifica se o pedido não excede o estoque
                    print('Você tem {} {} em estoque'.format(quant_estoque, nome_venda))
                    print('Não há estoque suficiente para esse produto...')
                
                
                else: #### realisa a venda do produto 
                    conjunto_vendas = [nome_venda, quant_venda]
                    dict_registro_vendas.update({numero_sequencia() : conjunto_vendas})
                    quant_estoque = quant_estoque - quant_venda
                    dict_produtos.update({checando_produto_dicionario(nome_venda) : [lista_codigo_produto[0], lista_codigo_produto[1], lista_codigo_produto[2], int(quant_estoque)]})
                    print('Sobrou {} no estoque'.format(quant_estoque))
                    print('Venda realizada com sucesso!!!')
                     
                
            repitir2 = input('Deseja vender outro produto?(S/N) ')
            if repitir2.upper() == 'S':
                pass
            elif repitir2.upper() == 'N':
                break

    
    elif resposta == 3: ### altera alguma caracteristica do produto
       
        system("cls")

        while (True):
            decidir_modo_alterção = escrita_campo_correta('Você quer pesquisar o produto pelo código ou pelo nome?(C / N) ', 'string') ### solicitando para o usuario se ele deseja pesquisar via nome ou codigo

            if decidir_modo_alterção.upper() == 'C': ### alterações feitas via codigo

                codigo_produto_alteração = escrita_campo_correta('Qual produto você deseja realizar a alteração? ', 'int') ## pegando o codigo do produto

                if codigo_produto_alteração not in dict_produtos.keys(): ### certificando que ele está no dicionario
                    print('Codigo inexistente!!!')


                else:
                    escolha_alteração = alternativas_alteração() ### chamando a função que é menu de alterações

                    if escolha_alteração == 1: ### mudando o codigo
                        lista_codigo_produto = dict_produtos.get(codigo_produto_alteração)  ### usando o codigo dado para receber a lista com as informações
                        novo_codigo = escrita_campo_correta('qual o numero do novo codigo? ', 'int')
                        dict_produtos.update({novo_codigo : [lista_codigo_produto[0], lista_codigo_produto[1], lista_codigo_produto[2], lista_codigo_produto[3]]}) ### quando "mudamos" o codigo, na verdade, criamos outro produto. Sendo assim, copiamos os dados do antigo produto para o novo e após isso apagamos o produto antigo.
                        dict_produtos.pop(codigo_produto_alteração) ### apagando o produto antigo

                        ### nos seguintes casos não precisamos fazer isso, devido ao codigo permanecer o mesmo.

                    elif escolha_alteração == 2: ### alterando o nome via codigo
                        lista_nome_produto = dict_produtos.get(codigo_produto_alteração)
                        novo_nome = escrita_campo_correta('qual o nome do novo produto? ', 'string')
                        dict_produtos.update({codigo_produto_alteração : [novo_nome, lista_nome_produto[1], lista_nome_produto[2], lista_nome_produto[3]]})
                        
                    elif escolha_alteração == 3: ### alterando o tipo via codigo
                        lista_tipo_produto = dict_produtos.get(codigo_produto_alteração)
                        novo_tipo = escrita_campo_correta('qual o novo tipo do produto? ', 'string')
                        dict_produtos.update({codigo_produto_alteração : [lista_tipo_produto[0], novo_tipo, lista_tipo_produto[2], lista_tipo_produto[3]]})

                    elif escolha_alteração == 4: ### alterando o preço via codigo
                        lista_preço_produto = dict_produtos.get(codigo_produto_alteração)
                        novo_preço = escrita_campo_correta('qual o novo preço do produto? ', 'string')
                        dict_produtos.update({codigo_produto_alteração : [lista_preço_produto[0], lista_preço_produto[1], novo_preço, lista_preço_produto[3]]})

                    elif escolha_alteração ==5: ### alterando o estoque via codigo
                        lista_estoque_produto = dict_produtos.get(codigo_produto_alteração)
                        novo_estoque = escrita_campo_correta('Qual é o novo estoque do produto? ', 'string')
                        dict_produtos.update({codigo_produto_alteração : [lista_estoque_produto[0], lista_estoque_produto[1], lista_estoque_produto[2], int(novo_estoque)]})


                repitir3 = input('Deseja fazer outra alteração?(S/N) ') ### confirmando se o usuario deseja fazer mais alguma alteração
                if repitir3.upper() == 'S':
                    pass
                elif repitir3.upper() == 'N':
                    break







            elif decidir_modo_alterção.upper() == 'N': ### alterações feitas via nome

                produto_nome_alteração = escrita_campo_correta('Qual produto você deseja realizar alteração? ', 'string')
                
                if checando_produto_dicionario(produto_nome_alteração) == False: ### usando a função para pegar o codigo do produto e em seguida verificando se ele está no estoque
                    print('Produto não encontrado!!!')
                
                else:
                    escolha_alteração = alternativas_alteração()
                    
                    if escolha_alteração == 1:
                        lista_codigo_produto = dict_produtos.get(checando_produto_dicionario(produto_nome_alteração))
                        novo_codigo = escrita_campo_correta('qual o numero do novo codigo? ', 'int')
                        dict_produtos.update({novo_codigo : [lista_codigo_produto[0], lista_codigo_produto[1], lista_codigo_produto[2], lista_codigo_produto[3]]})
                        dict_produtos.pop(checando_produto_dicionario(produto_nome_alteração))
                        print(dict_produtos)

                    elif escolha_alteração == 2:
                        lista_nome_produto = dict_produtos.get(checando_produto_dicionario(produto_nome_alteração))
                        novo_nome = escrita_campo_correta('qual o nome do novo produto? ', 'string')
                        dict_produtos.update({checando_produto_dicionario(produto_nome_alteração) : [novo_nome, lista_nome_produto[1], lista_nome_produto[2], lista_nome_produto[3]]})
                        
                    elif escolha_alteração == 3:
                        lista_tipo_produto = dict_produtos.get(checando_produto_dicionario(produto_nome_alteração))
                        novo_tipo = escrita_campo_correta('qual o novo tipo do produto? ', 'string')
                        dict_produtos.update({checando_produto_dicionario(produto_nome_alteração) : [lista_tipo_produto[0], novo_tipo, lista_tipo_produto[2], lista_tipo_produto[3]]})

                    elif escolha_alteração == 4:
                        lista_preço_produto = dict_produtos.get(checando_produto_dicionario(produto_nome_alteração))
                        novo_preço = escrita_campo_correta('qual o novo preço do produto? ', 'string')
                        dict_produtos.update({checando_produto_dicionario(produto_nome_alteração) : [lista_preço_produto[0], lista_preço_produto[1], novo_preço, lista_preço_produto[3]]})

                    elif escolha_alteração ==5:
                        lista_estoque_produto = dict_produtos.get(checando_produto_dicionario(produto_nome_alteração))
                        novo_estoque = escrita_campo_correta('Qual é o novo estoque do produto? ', 'string')
                        dict_produtos.update({checando_produto_dicionario(produto_nome_alteração) : [lista_estoque_produto[0], lista_estoque_produto[1], lista_estoque_produto[2], int(novo_estoque)]}) ### Tivemos que colocar a variavel "novo_estoque" como int, pois quando faziamos as alteraçoes ela salvava como uma string

                
                repitir4 = input('Deseja fazer outra alteração?(S/N) ')
                if repitir4.upper() == 'S':
                    pass
                elif repitir4.upper() == 'N':
                    break

    elif resposta == 4:
        escolha_relatorio = escrita_campo_correta("Você deseja ver:\n1 - Relatório de todos os produtos.\n2 - Relatório de vendas realizadas.\n", "int")
        if escolha_relatorio == 1:
            print(dict_produtos)
        elif escolha_relatorio == 2:
            print(dict_registro_vendas)


with open("dict_produtos.json", "w") as arquivo:
    json.dump(dict_produtos, arquivo)

with open("dict_produtos.json", "r") as arquivo:
    dicionario_produtos_carregado = json.load(arquivo)



with open("dict_registro_vendas.json", "w") as arquivo:
    json.dump(dict_registro_vendas, arquivo)

with open("dict_registro_vendas.json", "r") as arquivo:
    dicionario_vendas_carregado = json.load(arquivo)
