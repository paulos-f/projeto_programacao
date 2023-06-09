
print('\n1 - Cadastrar Produto.')
print('2 - Alterar Produto.')
print('3 - Realizar Venda.')
print('4 - Relatórios.')
print('5 – Sair.')


resposta = int(input('\nOlá, o que você deseja fazer? '))

indentificador_do_produto = 0

dict_nome_produtos = {"pão d'agua" : ["pão", 0.99, 100]}

dict_codigo_produtos = {}

while(True):


    if resposta == 5:
        print('Te vejo em breve!!!')
        break


    elif resposta == 1:


        while(True):
            print('\nMuito bem, vamos começar o cadastro. ')

            lista_tipo_preço_estoque = []
            
            indentificador_do_produto = input('Qual o código você deseja colocar no produto? ')
            nome_produto = input('Qual o nome do produto? ')
            tipo_produto = input('Qual o tipo do produto? ')
            preço_produto = float(input('Qual o preço do produto? '))
            estoque_produto = int(input('Qual o estoque incial do produto? '))

            
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
        break
    elif resposta == 2:
        nome_venda = input('Qual produto você deseja realizar a venda?(Nome) ')
        z = dict_nome_produtos.get(nome_venda)
        print(z)























print(dict_nome_produtos)
print(dict_codigo_produtos)