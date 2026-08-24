# Sistema de Comandas para Bar/Restaurante

Sistema de gerenciamento de pedidos para bar/restaurante, onde garçons e balconistas registram pedidos em comandas identificadas por número ou nome do cliente, e fecham essas comandas na hora do pagamento.

## Funcionalidades

- Cadastro de produtos organizados por categoria (Bebidas, Petiscos, Pratos Individuais, Pratos para Compartilhar)
- Bebidas organizadas por alcoólicas e não alcoólicas
- Abertura de comandas identificadas por número ou nome
- Possibilidade de reabrir uma comanda existente para continuar editando
- Adição e remoção de itens na comanda em tempo real
- Cálculo automático do total da comanda
- Fechamento de comanda com registro da forma de pagamento (Pix, Cartão de Crédito, Cartão de Débito, Dinheiro, Vale Refeição)
- Cancelamento de comandas abertas
- Histórico de comandas abertas, fechadas e canceladas, ordenado por data

## Tecnologias utilizadas

- **Backend:** Python + FastAPI
- **Frontend:** HTML, CSS e JavaScript puro
- **Banco de dados:** PostgreSQL (Neon em produção)
- **Driver de conexão:** psycopg

## Telas do sistema

- **index.html** — tela inicial de navegação
- **atendimento.html** — onde o garçom/balconista monta os pedidos
- **caixa.html** — onde é feito o fechamento e cancelamento de comandas

## Como rodar o projeto localmente

### Pré-requisitos

- Python instalado
- PostgreSQL instalado e rodando (ou uma conta no Neon)

### Passos

1. Clone o repositório:

```bash
git clone https://github.com/thaissagoncalves1/sistema-bar.git
cd sistema-bar
```

2. Crie e ative um ambiente virtual:

```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Crie um banco de dados PostgreSQL chamado `bar_sistema` e rode o script `schema.sql` para criar as tabelas e os dados iniciais.

5. Copie o arquivo `.env.example` para `.env` e preencha com suas credenciais do banco:

```bash
cp .env.example .env
```

6. Rode o servidor:

```bash
uvicorn bar_sistema_backend:app --reload
```

7. Acesse a documentação interativa da API em: http://127.0.0.1:8000/docs

8. Abra o arquivo `index.html` no navegador para acessar as telas do sistema.

## Endpoints da API

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/produtos` | Lista todos os produtos |
| GET | `/categorias` | Lista todas as categorias |
| GET | `/comandas` | Lista todas as comandas |
| POST | `/comandas` | Abre uma nova comanda |
| POST | `/comandas/{id}/itens` | Adiciona um item à comanda |
| GET | `/comandas/{id}/itens` | Lista os itens de uma comanda |
| PATCH | `/comandas/{comanda_id}/produtos/{produto_id}/diminuir` | Reduz a quantidade de um item |
| DELETE | `/comandas/{comanda_id}/produtos/{produto_id}` | Remove um item da comanda |
| GET | `/comandas/{id}/total` | Calcula o total da comanda |
| PUT | `/comandas/{id}/fechar` | Fecha a comanda e registra o pagamento |
| PUT | `/comandas/{id}/cancelar` | Cancela uma comanda aberta |

## Status do projeto

✅ Backend completo · ✅ Frontend completo (Atendimento, Fechar Comanda, tela inicial) · 🚧 Deploy em andamento (banco de dados já migrado para Neon)