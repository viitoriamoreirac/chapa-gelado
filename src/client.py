import re


class Client:
    def __init__(self, nome, telefone, total_pedidos, valor_total_gasto):
        self.nome = nome
        self.telefone = telefone
        self.total_pedidos = total_pedidos
        self.valor_total_gasto = valor_total_gasto

    def __str__(self):
        return f"Nome: {self.nome}\nTelefone: {self.telefone}\nTotal de Pedidos: {self.total_pedidos}\nValor Total Gasto: R${self.valor_total_gasto:.2f}"

clients = []

def createClient():
    numero_invalido = True
    while numero_invalido:
        telefone_cliente = (input("Digite o telefone do cliente: "))
        padrao = re.compile(r'^\d{2}9\d{8}$')
        if padrao.match(telefone_cliente):
            numero_invalido = False
        else:
            print("Número digitado no formato incorreto, tente novamente.")
            numero_invalido = True

    cliente_novo = True
    if clients != []:
        for client in clients:
            if telefone_cliente == client.telefone:
                print("Cliente já cadastrado")
                cliente_novo = False
    if cliente_novo:
        nome_cliente = input("Digite o nome do cliente: ")
        fez_pedido = 0
        valor_total_gasto = 0

        cliente1 = Client(nome_cliente, telefone_cliente, fez_pedido, valor_total_gasto)

        clients.append(cliente1)

def busca(telefone_client):
    encontrado = False
    for client in clients:
        if telefone_client == client.telefone:
            print(client)
            encontrado = True
    if not encontrado:
        print("Cliente não encontrado.")

def read_client():
    opcao = input("Deseja visualizar todos os clientes(1) ou realizar uma pesquisa(2)? ")
    if opcao == "1":
        for client in clients:
            print(client)
    elif opcao == "2":
        telefone_client = input("Digite o numero de telefone a ser pesquisado: ")
        busca(telefone_client)
    else:
        print("Opção inválida.")

def update_client():
    telefone_client = input("Digite o telefone do cliente que deseja realizar a alteração: ")
    busca(telefone_client)

    for client in clients:
        if telefone_client == client.telefone:
            opcao = input("Qual dado deseja alterar? Digite 1 para nome, 2 para telefone, 3 para pedidos feitos e 4 para valor total gasto: ")
            if opcao == "1":
                client.nome = input("Digite o novo nome: ")
            elif opcao == "2":
                numero_invalido = True
                while numero_invalido:
                    telefone_client = (input("Digite o novo telefone do cliente: "))
                    padrao = re.compile(r'^\d{2}9\d{8}$')
                    if padrao.match(telefone_client):
                        numero_invalido = False
                        client.telefone = telefone_client
                    else:
                        print("Número digitado no formato incorreto, tente novamente.")
                        numero_invalido = True
            elif opcao == "3":
                client.total_pedidos = input("Quantos pedidos foram feitos? ")
            elif opcao == "4":
                client.valor_total_gasto = float(input("Qual o valor total gasto?"))
            else: 
                print("Opção inválida.")
            
def delete_client():
    telefone_client = input("Digite o telefone do cliente que deseja deletar: ")
    busca(telefone_client)
    deletar = input("Deseja deletar o cliente acima? Digite 1. ")
    if deletar == "1":
        for client in clients:
            if telefone_client == client.telefone:
                clients.remove(client)
    else:
        print("Opção inválida.")



