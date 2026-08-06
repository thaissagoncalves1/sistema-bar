from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import psycopg
import os

load_dotenv()

app = FastAPI()


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
    cursor.execute("SELECT id, nome, preco, categoria_id FROM produtos ORDER BY nome;")
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado


class NovaComanda(BaseModel):
    identificador_comanda: str


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