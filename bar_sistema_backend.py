from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from enum import Enum
import psycopg
import os

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


def conectar_banco():
    return psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )


@app.get("/")
def home():
    return {"mensagem": "Sistema do bar funcionando!"}


@app.get("/produtos")
def listar_produtos():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT id, nome, preco, categoria_id FROM produtos ORDER BY nome;"
    )

    resultado = cursor.fetchall()

    cursor.close()
    conexao.close()

    return resultado


class NovaComanda(BaseModel):
    identificador_comanda: str


class NovoItem(BaseModel):
    produto_id: int
    quantidade: int


class FormaPagamento(str, Enum):
    pix = "Pix"
    credito = "Cartão de Crédito"
    debito = "Cartão de Débito"
    dinheiro = "Dinheiro"
    vale_refeicao = "Vale Refeição"

class FecharComanda(BaseModel):
    forma_pagamento: FormaPagamento


@app.get("/comandas")
def listar_comandas():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute(
        """
        SELECT id, identificador_comanda, status, forma_pagamento, criado_em, pago_em
        FROM comandas
        ORDER BY id;
        """
    )

    comandas = cursor.fetchall()

    cursor.close()
    conexao.close()

    resultado = []

    for comanda in comandas:
        resultado.append({
            "id": comanda[0],
            "identificador_comanda": comanda[1],
            "status": comanda[2],
            "forma_pagamento": comanda[3],
            "criado_em": comanda[4],
            "pago_em": comanda[5]
        })

    return resultado


@app.post("/comandas")
def abrir_comanda(dados: NovaComanda):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO comandas (identificador_comanda) VALUES (%s) RETURNING id;",
        (dados.identificador_comanda,)
    )

    nova_comanda_id = cursor.fetchone()[0]

    conexao.commit()

    cursor.close()
    conexao.close()

    return {
        "id": nova_comanda_id,
        "identificador_comanda": dados.identificador_comanda,
        "status": "aberta"
    }


@app.post("/comandas/{comanda_id}/itens")
def adicionar_item(comanda_id: int, dados: NovoItem):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT preco FROM produtos WHERE id = %s;",
        (dados.produto_id,)
    )
    resultado = cursor.fetchone()
    preco_atual = resultado[0]

    cursor.execute(
        "SELECT id, quantidade FROM itens_comanda WHERE comanda_id = %s AND produto_id = %s;",
        (comanda_id, dados.produto_id)
    )
    item_existente = cursor.fetchone()

    if item_existente:
        item_id, quantidade_atual = item_existente
        cursor.execute(
            "UPDATE itens_comanda SET quantidade = quantidade + %s WHERE id = %s;",
            (dados.quantidade, item_id)
        )
    else:
        cursor.execute(
            """
            INSERT INTO itens_comanda
            (comanda_id, produto_id, quantidade, preco_unitario)
            VALUES (%s, %s, %s, %s);
            """,
            (comanda_id, dados.produto_id, dados.quantidade, preco_atual)
        )

    conexao.commit()

    cursor.close()
    conexao.close()

    return {"mensagem": "Item adicionado com sucesso"}


@app.get("/comandas/{comanda_id}/total")
def calcular_total(comanda_id: int):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute(
        """
        SELECT SUM(quantidade * preco_unitario)
        FROM itens_comanda
        WHERE comanda_id = %s;
        """,
        (comanda_id,)
    )

    resultado = cursor.fetchone()

    cursor.close()
    conexao.close()

    total = resultado[0] if resultado[0] is not None else 0

    return {
        "comanda_id": comanda_id,
        "total": float(total)
    }


@app.put("/comandas/{comanda_id}/fechar")
def fechar_comanda(comanda_id: int, dados: FecharComanda):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT id, status FROM comandas WHERE id = %s;",
        (comanda_id,)
    )

    comanda = cursor.fetchone()

    if not comanda:
        cursor.close()
        conexao.close()
        return {"erro": "Comanda não encontrada."}

    if comanda[1] != "aberta":
        cursor.close()
        conexao.close()
        return {"erro": f"Esta comanda não pode ser fechada (status atual: {comanda[1]})."}

    cursor.execute(
        """
        UPDATE comandas
        SET
            status = 'fechada',
            forma_pagamento = %s,
            pago_em = NOW()
        WHERE id = %s;
        """,
        (
            dados.forma_pagamento.value,
            comanda_id
        )
    )

    conexao.commit()

    cursor.close()
    conexao.close()

    return {
        "mensagem": "Comanda fechada com sucesso.",
        "comanda_id": comanda_id,
        "forma_pagamento": dados.forma_pagamento.value,
        "status": "fechada"
    }


@app.get("/comandas/{comanda_id}/itens")
def listar_itens_comanda(comanda_id: int):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute(
        """
        SELECT itens_comanda.id, produtos.id, produtos.nome, itens_comanda.quantidade, itens_comanda.preco_unitario
        FROM itens_comanda
        JOIN produtos ON itens_comanda.produto_id = produtos.id
        WHERE itens_comanda.comanda_id = %s;
        """,
        (comanda_id,)
    )

    itens = cursor.fetchall()
    cursor.close()
    conexao.close()

    resultado = []
    for item in itens:
        resultado.append({
            "item_id": item[0],
            "produto_id": item[1],
            "produto_nome": item[2],
            "quantidade": item[3],
            "preco_unitario": float(item[4])
        })

    return resultado


@app.delete("/comandas/{comanda_id}/produtos/{produto_id}")
def remover_item(comanda_id: int, produto_id: int):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute(
        "DELETE FROM itens_comanda WHERE comanda_id = %s AND produto_id = %s;",
        (comanda_id, produto_id)
    )

    conexao.commit()
    cursor.close()
    conexao.close()

    return {"mensagem": "Item removido com sucesso"}


@app.patch("/comandas/{comanda_id}/produtos/{produto_id}/diminuir")
def diminuir_item(comanda_id: int, produto_id: int):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT id, quantidade FROM itens_comanda WHERE comanda_id = %s AND produto_id = %s;",
        (comanda_id, produto_id)
    )
    resultado = cursor.fetchone()

    if not resultado:
        cursor.close()
        conexao.close()
        return {"erro": "Item não encontrado nessa comanda."}

    item_id, quantidade_atual = resultado

    if quantidade_atual > 1:
        cursor.execute(
            "UPDATE itens_comanda SET quantidade = quantidade - 1 WHERE id = %s;",
            (item_id,)
        )
        mensagem = "Quantidade reduzida em 1."
    else:
        cursor.execute(
            "DELETE FROM itens_comanda WHERE id = %s;",
            (item_id,)
        )
        mensagem = "Item removido (quantidade chegou a zero)."

    conexao.commit()
    cursor.close()
    conexao.close()

    return {"mensagem": mensagem}


@app.get("/categorias")
def listar_categorias():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("SELECT id, nome FROM categorias ORDER BY nome;")
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado

@app.put("/comandas/{comanda_id}/cancelar")
def cancelar_comanda(comanda_id: int):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute("SELECT status FROM comandas WHERE id = %s;", (comanda_id,))
    comanda = cursor.fetchone()

    if not comanda:
        cursor.close()
        conexao.close()
        return {"erro": "Comanda não encontrada."}

    if comanda[0] != "aberta":
        cursor.close()
        conexao.close()
        return {"erro": "Só é possível cancelar comandas que estão abertas."}

    cursor.execute(
        "UPDATE comandas SET status = 'cancelada' WHERE id = %s;",
        (comanda_id,)
    )

    conexao.commit()
    cursor.close()
    conexao.close()

    return {
        "mensagem": "Comanda cancelada com sucesso.",
        "comanda_id": comanda_id,
        "status": "cancelada"
    }