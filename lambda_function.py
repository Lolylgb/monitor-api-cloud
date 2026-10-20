from src.monitor import executar_monitoramento


def lambda_handler(event, context):
    executar_monitoramento()

    return {
        "statusCode": 200,
        "body": "Monitoramento das APIs concluído."
    }