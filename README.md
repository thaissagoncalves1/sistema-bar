# Sistema de Comandas para Bar/Restaurante

Sistema de gerenciamento de pedidos para bar/restaurante, onde garçons e balconistas registram pedidos em comandas identificadas por número ou nome do cliente, e o caixa consulta e fecha essas comandas na hora do pagamento.

## Funcionalidades

- Cadastro de produtos organizados por categoria (Bebidas, Petiscos, Pratos Individuais, Pratos para Compartilhar)
- Abertura de comandas identificadas por número ou nome
- Adição e remoção de itens na comanda em tempo real
- Cálculo automático do total da comanda
- Fechamento de comanda com registro da forma de pagamento (Pix, Cartão, Dinheiro)

## Tecnologias utilizadas

- **Backend:** Python + FastAPI
- **Banco de dados:** PostgreSQL
- **Driver de conexão:** psycopg

## Como rodar o projeto localmente

### Pré-requisitos

- Python instalado
- PostgreSQL instalado e rodando

### Passos

1. Clone o repositório:
```bash
git clone https://github.com/thaissagoncalves1/sistema-bar.git
cd sistema-bar
```

2. Crie um ambiente virtual e instale as dependências:
```bash
pip install fastapi uvicorn "psycopg[binary]" python-dotenv
```

3. Crie um banco de dados PostgreSQL chamado `bar_sistema` e rode o script `schema.sql` para criar as tabelas.

4. Copie o arquivo `.env.example` para `.env` e preencha com suas credenciais do banco:
```bash
cp .env.example .env
```

5. Rode o servidor:
```bash
uvicorn bar_sistema_backend:app --reload

6. Acesse a documentação interativa da API em:
http://127.0.0.1:8000/docs

## Endpoints da API

| Método | Rota                                                    | Descrição                                  |
|--------|---------------------------------------------------------|--------------------------------------------|
| GET    | `/produtos`                                             | Lista todos os produtos                    |
| GET    | `/categorias`                                           | Lista todas as categorias                  |
| GET    | `/comandas`                                             | Lista todas as comandas                    |
| POST   | `/comandas`                                             | Abre uma nova comanda                      |
| POST   | `/comandas/{id}/itens`                                  | Adiciona um item à comanda                 |
| GET    | `/comandas/{id}/itens`                                  | Lista os itens de uma comanda              |
| PATCH  | `/comandas/{comanda_id}/produtos/{produto_id}/diminuir` | Reduz a quantidade de um item              |
| DELETE | `/comandas/{comanda_id}/produtos/{produto_id}`          | Remove um item da comanda                  |
| GET    | `/comandas/{id}/total`                                  | Calcula o total da comanda                 |
| PUT    | `/comandas/{id}/fechar`                                 | Fecha a comanda e registra o pagamento     |

## Status do projeto

backend completo, frontend em construção.
```

