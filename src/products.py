import re
import json

class Product:
    def __init__(self, id, nome, valor, quantidade_disponivel):
        self.id = id
        self.nome = nome
        self.valor = valor
        self.quantidade_disponivel = quantidade_disponivel

    def __str__(self):
        return f"Id: {self.id}\nNome: {self.nome}\nValor: R${self.valor:.2f}\nQuantidade disponível: {self.quantidade_disponivel}"

def load_products():
    try:
        with open('products.txt', 'r') as file:
            products_data = json.load(file)
            products = [Product(**data) for data in products_data]
        return products
    except FileNotFoundError:
        return []

def save_products(products):
    with open('products.txt', 'w') as file:
        products_data = [vars(product) for product in products]
        json.dump(products_data, file, indent=2)

products = load_products()

def create_product():
    id_product = input("Digite o ID do produto: ")

    produto_novo = True
    if products:
        for product in products:
            if id_product == product.id:
                print("Produto já cadastrado")
                produto_novo = False

    if produto_novo:
        nome_produto = input("Digite o nome do produto: ")
        valor = float(input("Digite o valor do produto: "))
        quantidade_disponivel = int(input("Digite a quantidade disponível no estoque: "))

        produto1 = Product(id_product, nome_produto, valor, quantidade_disponivel)

        products.append(produto1)
        save_products(products)

def busca(id_product):
    encontrado = False
    for product in products:
        if id_product == product.id:
            print(product)
            encontrado = True
    if not encontrado:
        print("Produto não encontrado.")

def read_product():
    opcao = input("Deseja visualizar todos os produtos(1) ou realizar uma pesquisa(2)? ")
    if opcao == "1":
        for product in products:
            print(product)
    elif opcao == "2":
        id_product = input("Digite o ID do produto a ser pesquisado: ")
        busca(id_product)
    else:
        print("Opção inválida.")

def update_product():
    id_product = input("Digite o ID do produto que deseja realizar a alteração: ")
    busca(id_product)

    for product in products:
        if id_product == product.id:
            opcao = input("Qual dado deseja alterar? Digite 1 para nome, 2 para valor e 3 para quantidade disponível: ")
            if opcao == "1":
                product.nome = input("Digite o novo nome: ")
            elif opcao == "2":
                product.valor = float(input("Digite o novo valor: "))
            elif opcao == "3":
                product.quantidade_disponivel = int(input("Qual a quantidade disponível? "))
            else: 
                print("Opção inválida.")
            
            save_products(products)


def update_storage(id_product):
    for product in products:
        if id_product == product.id:
            product.quantidade_disponivel = product.quantidade_disponivel - 1

        save_products(products)



read_product()
update_storage("123")
read_product()
