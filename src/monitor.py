import time
import requests

from src.database import conectar


def verificar_api(nome, url):
    inicio = time.perf_counter()

    try:
        resposta = requests.get(url, timeout=10)

        tempo_resposta = round(
            (time.perf_counter() - inicio) * 1000,
            2
        )

        if resposta.ok:
            status = "ONLINE"
        else:
            status = "ERRO_HTTP"

        return {
            "nome": nome,
            "status": status,
            "codigo_http": resposta.status_code,
            "tempo_resposta_ms": tempo_resposta,
            "erro": None
        }

    except requests.RequestException as erro:
        tempo_resposta = round(
            (time.perf_counter() - inicio) * 1000,
            2
        )

        return {
            "nome": nome,
            "status": "INDISPONIVEL",
            "codigo_http": None,
            "tempo_resposta_ms": tempo_resposta,
            "erro": str(erro)
        }


def listar_apis(conexao):
    cursor = conexao.cursor(dictionary=True)

    try:
        cursor.execute(
            "SELECT id, nome, url FROM apis WHERE ativo = TRUE"
        )

        return cursor.fetchall()

    finally:
        cursor.close()


def salvar_monitoramento(conexao, api_id, resultado):
    cursor = conexao.cursor()

    try:
        sql = """
              INSERT INTO monitoramentos
              (
                  api_id,
                  status,
                  codigo_http,
                  tempo_resposta_ms,
                  erro
              )
              VALUES (%s, %s, %s, %s, %s) \
              """

        valores = (
            api_id,
            resultado["status"],
            resultado["codigo_http"],
            resultado["tempo_resposta_ms"],
            resultado["erro"]
        )

        cursor.execute(sql, valores)
        conexao.commit()

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()


def executar_monitoramento():
    conexao = conectar()

    try:
        apis = listar_apis(conexao)

        for api in apis:
            resultado = verificar_api(
                api["nome"],
                api["url"]
            )

            salvar_monitoramento(
                conexao,
                api["id"],
                resultado
            )

            print(resultado)

    finally:
        conexao.close()


if __name__ == "__main__":
    executar_monitoramento()