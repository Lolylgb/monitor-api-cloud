# API Monitor Cloud

**Monitoramento automatizado de APIs com Python, MySQL e evolução planejada para AWS.**

## Sobre o projeto

O API Monitor Cloud é um projeto de portfólio que demonstra o desenvolvimento de uma solução para monitorar a disponibilidade de APIs externas.

A aplicação consulta serviços HTTP, identifica respostas bem-sucedidas e respostas com erro, mede tempos de resposta e registra o histórico das verificações em um banco de dados MySQL.

O desenvolvimento é incremental: começa com uma aplicação Python executada localmente e evolui para testes automatizados, geração de relatórios e integração com serviços de computação em nuvem.

## Objetivos

- Automatizar verificações de disponibilidade.
- Consumir APIs REST.
- Medir tempos de resposta.
- Tratar erros HTTP, falhas de conexão e timeouts.
- Persistir resultados em um banco de dados relacional.
- Consultar o histórico de monitoramento.
- Gerar relatórios.
- Implementar testes automatizados.
- Explorar a implantação e a observabilidade na AWS.

## Tecnologias

| Tecnologia | Finalidade |
|---|---|
| Python | Desenvolvimento da aplicação |
| Requests | Consumo de APIs |
| MySQL | Persistência de dados |
| MySQL Connector/Python | Integração Python–MySQL |
| Python-dotenv | Gerenciamento de configurações |
| Git | Controle de versão |
| GitHub | Hospedagem e documentação |
| Pytest | Testes automatizados |
| FastAPI | API própria, em etapa futura |
| AWS Lambda | Execução em nuvem, em etapa futura |
| Amazon EventBridge | Agendamento, em etapa futura |
| Amazon CloudWatch | Logs e monitoramento, em etapa futura |

## Funcionamento

O fluxo principal da aplicação é:

1. Recuperar as APIs cadastradas no MySQL.
2. Consultar cada API por meio de uma requisição HTTP.
3. Medir o tempo de resposta.
4. Identificar o resultado da requisição.
5. Registrar o resultado no banco de dados.
6. Disponibilizar os registros para consulta e geração de relatórios.

## Estrutura do projeto

```text
api-monitor-cloud/
├── src/
├── sql/
├── tests/
├── docs/
├── reports/
├── requirements.txt
├── README.md
└── .gitignore
```

A estrutura será ampliada conforme novas funcionalidades forem implementadas.

## Pré-requisitos

- Python 3.
- Servidor MySQL.
- Git.
- IntelliJ IDEA com suporte a Python.
- Conexão com a internet para consultar APIs externas.

## Instalação

Clone o repositório:

```bash
git clone <URL_DO_REPOSITORIO>
```

Acesse a pasta:

```bash
cd api-monitor-cloud
```

Crie um ambiente virtual:

```bash
python -m venv .venv
```

No Windows PowerShell, ative-o:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Configure as variáveis de ambiente com base no arquivo `.env.example`.

Crie o banco de dados e as tabelas utilizando os scripts disponibilizados no diretório `sql/`.

## Execução

A execução do monitor requer que o servidor MySQL esteja acessível e que as variáveis de ambiente estejam configuradas corretamente.

O comando de execução será documentado e validado durante o desenvolvimento.

## Banco de dados

O MySQL armazena as APIs cadastradas e o histórico das verificações.

Os registros incluem o resultado do monitoramento, o código HTTP, o tempo de resposta e eventuais mensagens de erro.

## Testes

Os testes automatizados serão implementados com Pytest.

O objetivo é validar tanto os cenários de sucesso quanto as situações de falha, incluindo timeouts e respostas HTTP com erro.

## Segurança

- Credenciais não devem ser armazenadas no código-fonte.
- O arquivo `.env` não deve ser publicado.
- A aplicação deve utilizar permissões mínimas necessárias.
- Configurações de produção devem ser gerenciadas separadamente das configurações locais.

## Documentação

A documentação técnica está sendo organizada no diretório `docs/`, incluindo o relatório de desenvolvimento e a descrição da arquitetura.

## Status do projeto

**Desenvolvimento incremental.**

As funcionalidades serão consideradas concluídas após implementação e validação.

## Próximas etapas

- [ ] Preparar o ambiente Python.
- [ ] Configurar o MySQL.
- [ ] Implementar o monitoramento.
- [ ] Registrar os resultados no banco.
- [ ] Criar relatórios.
- [ ] Implementar testes automatizados.
- [ ] Publicar a primeira versão no GitHub.
- [ ] Desenvolver uma API própria.
- [ ] Avaliar a implantação na AWS.

## Licença

A licença será definida antes da publicação da versão inicial.

---

Projeto de estudo e portfólio em Python, integração de APIs, bancos de dados relacionais e computação em nuvem.