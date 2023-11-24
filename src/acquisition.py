from client import *
from products import *

def atualiza_dados_apos_compra(nome_cliente, id_produto):
    valor = update_storage(id_produto)
    update_pedidos_feitos(nome_cliente)
    update_valor_gasto(nome_cliente, valor)




