from unittest.mock import Mock, patch
import requests

from src.monitor import verificar_api


@patch("src.monitor.requests.get")
def test_api_disponivel(mock_get):
    resposta = Mock()
    resposta.status_code = 200
    resposta.ok = True

    mock_get.return_value = resposta

    resultado = verificar_api("GitHub", "https://api.github.com")

    assert resultado["nome"] == "GitHub"
    assert resultado["status"] == "ONLINE"
    assert resultado["codigo_http"] == 200
    assert resultado["erro"] is None


@patch("src.monitor.requests.get")
def test_api_com_erro_http(mock_get):
    resposta = Mock()
    resposta.status_code = 500
    resposta.ok = False

    mock_get.return_value = resposta

    resultado = verificar_api("GitHub", "https://api.github.com")

    assert resultado["status"] == "ERRO_HTTP"
    assert resultado["codigo_http"] == 500


@patch("src.monitor.requests.get")
def test_falha_de_conexao(mock_get):
    mock_get.side_effect = requests.ConnectionError(
        "Falha simulada de conexão"
    )

    resultado = verificar_api("GitHub", "https://api.github.com")

    assert resultado["status"] == "INDISPONIVEL"
    assert resultado["codigo_http"] is None
    assert "Falha simulada de conexão" in resultado["erro"]


@patch("src.monitor.requests.get")
def test_tempo_limite_excedido(mock_get):
    mock_get.side_effect = requests.Timeout(
        "Tempo limite excedido"
    )

    resultado = verificar_api("GitHub", "https://api.github.com")

    assert resultado["status"] == "INDISPONIVEL"
    assert resultado["codigo_http"] is None
    assert "Tempo limite excedido" in resultado["erro"]