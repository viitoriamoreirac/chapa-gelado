from client import *
from products import *
from acquisition import *

def main():
    opcao = 0
    while opcao != 4:
        opcao = int(input("\nDigite o numeral correspondente a opção que deseja: \n1 - Realizar compra. \n2 - Criar, editar ou visualizar clientes. \n3 - Criar, editar ou visualizar produtos. \n4 - Sair.\nOpção: "))

        if opcao == 1:
            realiza_compra()
        elif opcao == 2:
            crud_cliente()
        elif opcao == 3:
            crud_produto()
        elif opcao == 4:
            print("\nAté a próxima!")
        else:
            print("\nOpção inválida, tente novamente.")




def realiza_compra():
    nome_cliente = input("\nDigite o nome do cliente: ")
    cliente_encontrado = busca_cliente(nome_cliente)
    if cliente_encontrado:
        id_produto = input("\nDigite o ID do produto a ser vendido: ")
        produto_encontrado = busca_produto(id_produto)
        if produto_encontrado:
            atualiza_dados_apos_compra(nome_cliente, id_produto)
        
            print("\nPedido feito!")




def crud_cliente():
    opcao = int(input("\nDigite o numeral correspondente a opção que deseja: \n1 - Cadastrar um novo cliente. \n2 - Visualizar clientes existentes. \n3 - Atualizar dados de algum cliente. \n4 - Deletar cliente existente. \n5 - Voltar ao menu principal.\nOpção: "))
    if opcao == 1:
        create_client()
    elif opcao == 2:
        read_client()
    elif opcao == 3:
        update_client()
    elif opcao == 4:
        nome_client = input("\nDigite o nome do cliente que deseja deletar: ")
        delete_client(nome_client)
    elif opcao == 5:
        print("\nRetornando ao menu principal.")
    else:
        print("\nOpção inválida, tente novamente.")
        crud_cliente()


def crud_produto():
    opcao = int(input("\nDigite o numeral correspondente a opção que deseja: \n1 - Cadastrar um novo produto. \n2 - Visualizar produtos existentes. \n3 - Atualizar dados de algum produto. \n4 - Deletar produto existente. \n5 - Voltar ao menu principal.\nOpção: "))
    if opcao == 1:
        create_product()
    elif opcao == 2:
        read_product()
    elif opcao == 3:
        update_product()
    elif opcao == 4:
        id_product = input("Digite o ID do produto que deseja deletar: ")
        delete_product(id_product)
    elif opcao == 5:
        print("\nRetornando ao menu principal.")
    else:
        print("\nOpção inválida, tente novamente.")
        crud_produto()



main()