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
        opcao = 1
        while opcao == 1:
            fez_pedido = input("Esse cliente já fez algum pedido? 1 para sim e 2 para não: ")
            if fez_pedido == "1":
                fez_pedido = input("Quantos pedidos foram feitos? ")
                valor_total_gasto = float(input("Qual o valor total já gasto? "))
                opcao = 0
            elif fez_pedido == "2":
                fez_pedido = 0
                valor_total_gasto = 0
                opcao = 0
            else:
                print("Opção inválida, tente novamente:")

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


def main():
    createClient()
    createClient()
    read_client()
    read_client()

if __name__ == "__main__":
    main()



