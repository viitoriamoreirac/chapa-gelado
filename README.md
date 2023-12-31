# Projeto para funcionamento de uma sorveteria, feito para fins avaliativos.

### Como Rodar?

1. Copie e cole o código abaixo em seu terminal dentro de um diretório local de sua preferência: <br>
`git clone https://github.com/viitoriamoreirac/chapa-gelado.git` <br>
2. Execute o arquivo `main.py` contido na pasta `src`

### Demandas do Projeto

A demanda principal identificada para o estabelecimento se trata da necessidade de registrar as vendas realizadas, de forma a controlar a quantidade de itens ainda disponíveis e ter um controle da base de clientes. O sistema deve permitir a manipulação dos produtos e suas respectivas quantidades, e o registro da quantidade e valor dos pedidos feitos por cada cliente.

### Objetivos do Projeto

O projeto tem como objetivo fornecer ao funcionário, ou proprietário do estabelecimento, o controle dos produtos e clientes do estabelecimento, podendo cadastrar, visualizar e atualizar dados sobre os mesmos.

### Atendimento pelo Projeto

O projeto atendeu às demandas estabelecidas ao fornecer uma aplicação que permite o cadastro de clientes e produtos, a realização de uma venda e o controle do estoque e valor vendido.

### Utilização de Estruturas no Código

#### If/Elif/Else
Utilizado em várias funções, principalmente nas funções de menu de opções, no arquivo `main.py` -> `main()`, `crud_cliente()`, `crud_produto()`

#### While
Utilizado na função `main()`, contida no arquivo `main.py` para repetir o menu inicial, enquanto solicitado.

#### Subprogramas
Utilizado no projeto  inteiro.

#### Matrizes/listas
Um dos exemplos está contido no arquivo `client.py` na função `load_clients()`

#### String
Foi utilizada string no projeto inteiro, um dos exemplos está na função `busca_cliente(nome_cliente)` contida no arquivo `client.py`

#### Estruturas
Foi usada estruturas nos arquivos `clients.txt` e `products.txt`

#### Arquivos
Foi usada interação entre arquivos no projeto inteiro, um exemplo está na função `atualiza_dados_apos_compra(nome_cliente, id_produto)` no arquivo `aquisition.py`


### Requisitos Funcionais

Clientes:
- [x] Cadastro de um novo cliente.
- [x] Listar todos os clientes cadastrados.
- [x] Realizar a pesquisa de determinado cliente a partir de seu nome.
- [x] Atualização de dados de clientes.
- [x] Exclusão de cliente.

Produtos:
- [x] Cadastro de um novo produto.
- [x] Listar todos os produtos cadastrados.
- [x] Realizar a pesquisa de determinado produto a partir de seu ID.
- [x] Atualização de nome, valor ou quantidade disponível de um produto.
- [x] Exclusão de produto.

Venda:
- [x] Realizar venda a partir de busca de produto e cliente.
- [x] Verificação se produto e cliente já existem cadastrados em sistema.
- [x] Atualização de estoque e valor gasto pelo cliente a partir da venda feita.

Inicial
- [x] Escolher entre opções de cliente, produto, venda ou encerrar sessão.

### Requisitos Não Funcionais

- [x] Usabilidade: o sistema deve ser fácil de usar, apresentando uma interface intuitiva.
- [x] Confiabilidade: o sistema deve ser confiável, apresentando tolerância a falhas ou a erros.
- [x] Velocidade: o sistema deve ser rápido, apresentando respostas rápidas às ações do usuário.

### História de Usuário

- [x] Como comerciante eu gostaria de registrar cada venda feita;
- [x] Como comerciante eu gostaria de cadastrar meus produtos, visualizar, alterar ou exclui-los;
- [x] Como comerciante eu gostaria de visualizar meu estoque disponível para cada produto.
- [x] Como comerciante eu gostaria que o estoque fosse atualizado a cada venda que faço.
- [x] Como comerciante eu gostaria de cadastrar meus clientes, fazer alterações em seus dados ou exclusão, caso necessário;
- [x] Como comerciante eu gostaria de visualizar os clientes mais assíduos e ter um controle do quanto ($) ele consumiu;
- [x] Como comerciante eu gostaria de ter a opção de sair do sistema.

### Diagrama de casos de uso:

Confira clicando [aqui](https://www.figma.com/file/IRkJKptev8TBG13IBWkR7b/Welcome-to-FigJam?type=whiteboard&node-id=0%3A1&t=CcqO2YNxkf4eiji9-1)
