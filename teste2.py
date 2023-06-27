def alternativas_alteração(): ### alterar alguma informação de um produto
    escolha_alterar = None
    while escolha_alterar not in [1,2,3,4,5] and escolha_alterar != '':
        try:
            escolha_alterar = int(input('Você deseja alterar o que? \n 1-Codigo \n 2-Nome \n 3-tipo \n 4-valor \n  5-estoque\n'))
            assert escolha_alterar in [1,2,3,4,5]    
        except(ValueError, AssertionError):
            print("Campo digitado errado!!!")
    return escolha_alterar

x = alternativas_alteração()

print(x)
print(type(x))