import re
import json

class Client:
    def __init__(self, nome, telefone, total_pedidos, valor_total_gasto):
        self.nome = nome
        self.telefone = telefone
        self.total_pedidos = total_pedidos
        self.valor_total_gasto = valor_total_gasto

    def __str__(self):
        return f"Nome: {self.nome}\nTelefone: {self.telefone}\nTotal de Pedidos: {self.total_pedidos}\nValor Total Gasto: R${self.valor_total_gasto:.2f}"

def load_clients():
    try:
        with open('clients.txt', 'r') as file:
            clients_data = json.load(file)
            clients = [Client(**data) for data in clients_data]
        return clients
    except FileNotFoundError:
        return []

def save_clients(clients):
    with open('clients.txt', 'w') as file:
        clients_data = [vars(client) for client in clients]
        json.dump(clients_data, file, indent=2)

clients = load_clients()

def create_client():
    numero_invalido = True
    while numero_invalido:
        telefone_cliente = input("Digite o telefone do cliente: ")
        padrao = re.compile(r'^\d{2}9\d{8}$')
        if padrao.match(telefone_cliente):
            numero_invalido = False
        else:
            print("Número digitado no formato incorreto, tente novamente.")
            numero_invalido = True

    cliente_novo = True
    if clients:
        for client in clients:
            if telefone_cliente == client.telefone:
                print("Cliente já cadastrado")
                cliente_novo = False
                break

    if cliente_novo:
        nome_cliente = input("Digite o nome do cliente: ").lower()
        
        for client in clients:
            if nome_cliente == client.nome.lower():
                print("Cliente já cadastrado pelo nome.")
                cliente_novo = False
                break

    if cliente_novo:
        fez_pedido = 0
        valor_total_gasto = 0

        cliente1 = Client(nome_cliente, telefone_cliente, fez_pedido, valor_total_gasto)

        clients.append(cliente1)
        save_clients(clients)


def busca_cliente(nome_cliente):
    encontrado = False
    for client in clients:
        if nome_cliente == client.nome:
            print(client)
            encontrado = True
    if not encontrado:
        print("Cliente não encontrado.")

    return encontrado

def read_client():
    opcao = input("\nDeseja visualizar todos os clientes(1) ou realizar uma pesquisa(2)? ")
    if opcao == "1":
        for client in clients:
            print(client)
    elif opcao == "2":
        nome_cliente = input("\nDigite o nome a ser pesquisado: ")
        busca_cliente(nome_cliente)
    else:
        print("\nOpção inválida.")

def update_client():
    nome_cliente = input("\nDigite o nome do cliente que deseja realizar a alteração: ")
    busca_cliente(nome_cliente)

    for client in clients:
        if nome_cliente == client.nome:
            opcao = input("\nQual dado deseja alterar? Digite 1 para nome, 2 para telefone, 3 para pedidos feitos e 4 para valor total gasto: ")
            if opcao == "1":
                client.nome = (input("\nDigite o novo nome: ")).lower()
            elif opcao == "2":
                numero_invalido = True
                while numero_invalido:
                    telefone_client = input("\nDigite o novo telefone do cliente: ")
                    padrao = re.compile(r'^\d{2}9\d{8}$')
                    if padrao.match(telefone_client):
                        numero_invalido = False
                        client.telefone = telefone_client
                    else:
                        print("\nNúmero digitado no formato incorreto, tente novamente.")
                        numero_invalido = True
            elif opcao == "3":
                client.total_pedidos = input("\nQuantos pedidos foram feitos? ")
            elif opcao == "4":
                client.valor_total_gasto = float(input("\nQual o valor total gasto?"))
            else: 
                print("\nOpção inválida.")
            
            save_clients(clients)

def update_pedidos_feitos(nome_cliente):
    for client in clients:
        if nome_cliente == client.nome:
            client.total_pedidos = client.total_pedidos + 1
        
        save_clients(clients)

def update_valor_gasto(nome_cliente, valor_gasto):
    for client in clients:
        if nome_cliente == client.nome:
            client.valor_total_gasto = client.valor_total_gasto + valor_gasto

            save_clients(clients)
