from dotenv import load_dotenv
import os

load_dotenv()

print("Host:", os.getenv("DB_HOST"))
print("Banco:", os.getenv("DB_NAME"))
print("Usuário:", os.getenv("DB_USER"))