
print('\n1 - Cadastrar Produto.')
print('2 - Realizar Venda.')
print('3 - Alterar Produto.')
print('4 - Relatórios.')
print('5 – Sair.')


resposta = int(input('\nOlá, o que você deseja fazer? '))

indentificador_do_produto = 0

dict_nome_produtos = {"pão d'agua" : ["pão", 0.99, 100]}

dict_codigo_produtos = {}

dict_registro_vendas = {}

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
        break




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
        


print(dict_nome_produtos)
print(dict_codigo_produtos)