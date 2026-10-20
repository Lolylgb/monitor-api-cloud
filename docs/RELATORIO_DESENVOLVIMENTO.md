# Relatório de Desenvolvimento — API Monitor Cloud

## 1. Introdução

O API Monitor Cloud é um projeto de desenvolvimento de software que tem como objetivo monitorar a disponibilidade de APIs externas, registrar resultados em um banco de dados MySQL e produzir informações úteis para análise de disponibilidade e desempenho.

O projeto é desenvolvido com Python e utiliza ferramentas de controle de versão para documentar sua evolução.

## 2. Objetivos

- Consumir APIs por meio de requisições HTTP.
- Identificar respostas HTTP e falhas de conexão.
- Medir tempos de resposta.
- Registrar resultados no MySQL.
- Consultar o histórico de verificações.
- Gerar relatórios.
- Implementar testes automatizados.
- Preparar a aplicação para uma futura implantação na AWS.

## 3. Ambiente de desenvolvimento

Registrar nesta seção:

- Sistema operacional.
- Versão do Python.
- Versão do IntelliJ IDEA.
- Versão do MySQL.
- Versão do Git.

## 4. Desenvolvimento

### 4.1 Preparação do ambiente

Descrever a criação do projeto no IntelliJ IDEA, a configuração do ambiente virtual e a instalação das dependências.

### 4.2 Integração com APIs

Documentar as requisições HTTP realizadas, os códigos de resposta observados e o tratamento de falhas.

### 4.3 Banco de dados

Descrever a criação do banco `api_monitor`, as tabelas utilizadas e o relacionamento entre APIs cadastradas e seus históricos de monitoramento.

### 4.4 Integração Python–MySQL

Registrar a configuração da conexão, o usuário utilizado pela aplicação e os testes realizados.

Não incluir senhas, tokens ou outras credenciais neste documento.

### 4.5 Monitoramento

Descrever como as APIs são consultadas, como os tempos de resposta são calculados e como os resultados são registrados.

### 4.6 Testes

Documentar os testes executados, seus resultados e eventuais correções realizadas.

### 4.7 Publicação no GitHub

Registrar a criação do repositório remoto, os commits relevantes e as instruções necessárias para executar o projeto.

## 5. Problemas encontrados e soluções

Utilizar esta seção para registrar problemas reais encontrados durante o desenvolvimento e explicar como foram solucionados.

## 6. Resultados

Apresentar resultados verificáveis, incluindo exemplos de consultas, registros produzidos e testes aprovados.

## 7. Evolução para Cloud

Documentar o planejamento de uma futura implantação na AWS, incluindo os serviços avaliados, as decisões arquiteturais e os cuidados com permissões e custos.

## 8. Conclusão

Apresentar os conhecimentos consolidados durante o desenvolvimento e as melhorias planejadas para versões futuras.