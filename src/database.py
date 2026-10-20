import mysql.connector
from src.config import DB_CONFIG


def conectar():
    return mysql.connector.connect(**DB_CONFIG, use_pure=True)


def testar_conexao():
    conexao = None

    try:
        conexao = conectar()

        if conexao.is_connected():
            print("Conexão com MySQL realizada com sucesso.")

    except mysql.connector.Error as erro:
        print("Erro ao conectar ao MySQL:", erro)
    except Exception as erro:
        print("Erro inesperado:", type(erro).__name__, erro)

    finally:
        if conexao is not None and conexao.is_connected():
            conexao.close()


if __name__ == "__main__":
    testar_conexao()