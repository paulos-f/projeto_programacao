import copy

import numpy as np
import pandas as pd


def get_answer_alternatives(): # menu das opções, apenas possível escolher entre 1,2,3,4,5
    resposta = None
    while resposta not in [1,2,3,4,5]:
        try:
            resposta = int(input('Escolha uma das opções: \n \
                                1 - Cadastrar Produto \n \
                                2 - Realizar Venda \n \
                                3 - Alterar Produto \n \
                                4 - Relatórios \n \
                                5 - Sair'))
            assert resposta in [1,2,3,4,5]
        except (ValueError, AssertionError):
            print('Opção não existente, digite novamente.')
    return resposta

def get_answer_continue(type_answer): # função para repetir sem ter que voltar pro menu ou sair da opção(opção me refiro ao 1,2,3,4,5)
    decision = None
    while decision not in ['s','n']:
        if decision != None:
            print('Opção não existente, digite novamente.')
        
        if type_answer == 'cadastro':
            decision = input('Deseja adicionar outro produto?(S/N)').lower()
        elif type_answer == 'venda':
            decision = input('Deseja vender outro produto?(S/N)').lower()
        elif type_answer == 'alterar':
            decision = input('Deseja alterar outro produto?(S/N)').lower()
        elif type_answer == 'relatorio':
            decision = input('Deseja gerar outro relatório?(S/N)').lower()
    return decision

def generate_identifier(): # gera automaticamente um id entre 1 e 10000 único
    ident = None
    while ident in list(dict_products.keys()) or ident == None:
        ident = np.random.choice(np.arange(0,10_000))
    return ident

# garante que as respostas para todas as perguntas que você venha a fazer para o usuário retorne no tipo de dado que você deseja
# exemplo: se eu digitar um nome no campo "preço" irá retornar um erro
def assert_type_answer(phrase, data_type):
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

def check_product_name(name): # verifica se existe produto com o nome no banco de dados
    for i in list(dict_products.keys()):
        if name == dict_products[i][0]:
            return i
    return False

def check_indet(cod): # verifica se existe produto com o id no banco de dados
    for i in list(dict_products.keys()):
        if cod == i:
            return i
    return False
        

def check_quant_product(ident,quant): # verifica a quantidade existente do produto especificado no parametro da função
    available_quant = dict_products[ident][3]
    if quant > available_quant:
        return False
    else:
        return True

resposta = get_answer_alternatives()

#dict_products = dict()
dict_products = {2814: ['pao frances', 'pao', 2.5, 50], 
                 3940: ['bolo de chocolate', 'bolo', 25.0, 10],
                 6528: ['croissant', 'salgado', 3.0, 20], 
                 4015: ['rosquinha', 'doce', 1.5, 30],
                 1778: ['pao de queijo', 'salgado', 2.0, 40], 
                 2641: ['torta de morango', 'torta', 30.0, 5],
                 5388: ['cookie', 'doce', 1.0, 15], 
                 1516: ['pao integral', 'pao', 3.0, 25],
                 3709: ['pastel de carne', 'salgado', 2.5, 10], 
                 1978: ['bolo de cenoura', 'bolo', 20.0, 8], 
                 9487: ['sonho de creme', 'doce', 2.0, 12], 
                 6067: ['pao de alho', 'salgado', 2.5, 18],
                 2474: ['biscoito de aveia', 'doce', 1.5, 20],
                 1993: ['pao australiano', 'pao', 3.5, 15],
                 5414: ['coxinha', 'salgado', 2.0, 25], 
                 8635: ['agua', 'ingrediente', 1.0, 100],
                 5629: ['farinha de trigo', 'ingrediente', 3.0, 50],
                 1898: ['fermento', 'ingrediente', 2.5, 30], 
                 9985: ['acucar', 'ingrediente', 2.0, 40], 
                 9858: ['leite', 'ingrediente', 2.0, 35], 
                 2882: ['ovos', 'ingrediente', 1.5, 60], 
                 8007: ['manteiga', 'ingrediente', 3.0, 25],
                 990: ['sal', 'ingrediente', 1.0, 75], 
                 3760: ['chocolate em po', 'ingrediente', 4.0, 15], 
                 742: ['fermento biologico', 'ingrediente', 2.0, 20], 
                 7193: ['farinha', 'po', 10.87, 1000]}

dict_rel_products = copy.deepcopy(dict_products)
dict_rel_sales = dict()

count_sales = 1

while resposta != 5:

    if resposta == 1:
        repetir = 's'
        while repetir == 's':
            print('\n Cadastro')
            lista_tipo_preço_estoque = []
            indentificador_do_produto = generate_identifier()
            
            print(f'O código do produto será {indentificador_do_produto}')
            nome_produto = assert_type_answer('Qual o nome do produto?','string')
            tipo_produto = assert_type_answer('Qual o tipo do produto?','string')
            preço_produto = assert_type_answer('Qual o preço do produto?','float')
            estoque_produto = assert_type_answer('Qual o estoque inicial do produto?','int')

            dict_products[indentificador_do_produto] = [nome_produto,tipo_produto,preço_produto,estoque_produto]
            dict_rel_products[indentificador_do_produto] = [nome_produto,tipo_produto,preço_produto,estoque_produto]
            
            repetir = get_answer_continue('cadastro')
            if repetir == 's':
                pass
            elif repetir == 'n':
                break
                

    elif resposta == 2:
        repetir = 's'
        while repetir == 's':
            nome_venda = assert_type_answer('Qual produto você deseja realizar a venda?(Nome)','string').lower()
            if check_product_name(nome_venda) == False:
                print('Produto não encontrado no banco de dados')
            else:
                ident = check_product_name(nome_venda)
                quant_venda = assert_type_answer('Quantas unidades deseja vender? ', 'int')
                
                if check_quant_product(ident, quant_venda) == False:
                    number = dict_products[ident][3]
                    print(f'O seu estoque {number} é menor que a quantidade {quant_venda} pedida')
                else:
                    dict_products[ident][3] = dict_products[ident][3] - quant_venda

                    dict_rel_sales[count_sales] = copy.deepcopy(dict_products[ident])
                    dict_rel_sales[count_sales][3] = quant_venda
                    count_sales += 1
                    
                    print('Venda realizada com sucesso!')
            
            repetir = get_answer_continue('venda')
            if repetir == 's':
                pass
            elif repetir == 'n':
                break
                
                
    elif resposta == 3:
        repetir = 's'
        while repetir == 's':
            cond = assert_type_answer('Procurar por código ou nome? (C/N)', 'string').lower()
            if cond == 'c':
                answer = assert_type_answer('Digite o código: ','int')
                if check_indet(answer) != False:
                    cadastro = assert_type_answer('Qual tipo de informação deseja trocar? \n\tNome -> n  \
                                                  \n\tTipo -> t \n\tPreço -> p \n\tEstoque -> e\n\t','string')
                    if cadastro == 'n':
                        alteracao = assert_type_answer('Digite o novo nome: ','string')
                        index_dict = 0
                    elif cadastro == 't':
                        alteracao = assert_type_answer('Digite o novo tipo: ','string')
                        index_dict = 1
                    elif cadastro == 'p':
                        alteracao = assert_type_answer('Digite o novo preço: ','float')
                        index_dict = 2
                    elif cadastro == 'e':
                        alteracao = assert_type_answer('Digite o novo estoque: ','int')
                        index_dict = 3
                        
                    answer = assert_type_answer('Tem certeza que deseja alterar? (S/N)','string').lower()
                    
                    if answer == 's':
                        dict_products[ident][index_dict] = alteracao
                        print('Alteração feita com sucesso!')
                    elif answer not in ['s','n']:
                        print('Opção não existente') 
                else:
                    print('Código não existente no banco de dados')
            
            elif cond == 'n':
                nome = assert_type_answer('Digite o nome do produto: ', 'string')
                if check_product_name(nome) != False:
                    ident = check_product_name(nome)
                    cadastro = assert_type_answer('Qual tipo de informação deseja trocar? \n\tNome -> n  \
                                                  \n\tTipo -> t \n\tPreço -> p \n\tEstoque -> e\n\t','string')
                    if cadastro == 'n':
                        alteracao = assert_type_answer('Digite o novo nome: ','string')
                        index_dict = 0
                    elif cadastro == 't':
                        alteracao = assert_type_answer('Digite o novo tipo: ','string')
                        index_dict = 1
                    elif cadastro == 'p':
                        alteracao = assert_type_answer('Digite o novo preço: ','float')
                        index_dict = 2
                    elif cadastro == 'e':
                        alteracao = assert_type_answer('Digite o novo estoque: ','int')
                        index_dict = 3
                    
                    answer = assert_type_answer('Tem certeza que deseja alterar? (S/N)','string').lower()
                    
                    if answer == 's':
                        dict_products[ident][index_dict] = alteracao
                        print('Alteração feita com sucesso!')
                    elif answer not in ['s','n']:
                        print('Opção não existente')    
                    
                else:
                    print('Nome não existente no banco de dados')
                
                    
            repetir = get_answer_continue('alterar')
            if repetir == 's':
                pass
            elif repetir == 'n':
                break
                
    elif resposta == 4:
        repetir = 's'
        while repetir == 's':
            answer = assert_type_answer('Deseja gerar qual tipo de relatório? [Produtos(P) / Vendas(V)]','string').lower()
            if answer == 'p':
                print(' ')
                dict_rel_products = copy.deepcopy(dict_products)
                df = pd.DataFrame(dict_rel_products).T
                df.columns = ['Nome', 'Tipo', 'Preço', 'Quantidade']
                df.index.name = 'id'
                print(df)
                print(' ')
            elif answer == 'v':
                print(' ')
                df = pd.DataFrame(dict_rel_sales).T
                df.columns = ['Nome', 'Tipo', 'Preço', 'Quantidade']
                df['Preço Total'] = df['Preço'] * df['Quantidade']
                print(df)
                print(' ')
            else:
                print('Opção não existente.')
            
            repetir = get_answer_continue('relatorio')
            if repetir == 's':
                pass
            elif repetir == 'n':
                break
                    
                    
        
    resposta = get_answer_alternatives()
        
print('Te vejo em breve!!!')
