# Atividade de Aula: Integração com Banco de Dados

Uma aplicação Python desenvolvida como atividade didática para demonstrar a integração com banco de dados.

## Objetivo

Esta atividade tem como principal objetivo demonstrar como realizar a integração de uma aplicação Python com um banco de dados, utilizando boas práticas de programação e arquitetura MVC.

## Estrutura do Projeto

```
├── _pycache_
├── controllers
│   ├── _pycache_
│   └── user_controller.py
├── database
│   ├── _pycache_
│   └── db.py
├── models
├── routes
├── templates
├── venv
├── .env
├── .env.example
├── .gitignore
├── banco.db
├── main.py
├── readme.md
├── requirements.txt
└── tarefa.txt
```

## Descrição

Esta é uma aplicação web Python que lida com operações de banco de dados como parte de um exercício de aula. A aplicação segue a arquitetura MVC com pastas organizadas para controllers, models, routes e templates.

## Configuração do Banco de Dados

A conexão com o banco de dados é configurada através de variáveis de ambiente:

```
DB_USER=exemplo_usuario
DB_PASSWORD=exemplo_senha
DB_DSN=example.com:1521/meuservico
```

Certifique-se de criar um arquivo `.env` baseado no `.env.example` fornecido com suas credenciais reais de banco de dados.

## Dependências

A aplicação requer vários pacotes Python, incluindo:

- FastAPI (0.115.12)
- Pydantic (2.10.6)
- Uvicorn (0.34.0)
- Python-dotenv (1.1.0)
- Cryptography (44.0.2)
- Jinja2 (3.1.6)
- E outros listados no arquivo requirements.txt

## Instalação

1. Clone o repositório
2. Crie um ambiente virtual:
   ```
   python -m venv venv
   ```
3. Ative o ambiente virtual:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
4. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```
5. Configure sua conexão com o banco de dados no arquivo `.env`
6. Execute a aplicação:
   ```
   python main.py
   ```

## Uso

A aplicação fornece um sistema de gerenciamento de usuários com integração de banco de dados. Consulte a documentação específica para detalhes sobre endpoints de API e funcionalidades.

## Avaliação

Este projeto faz parte da avaliação da disciplina e demonstra a capacidade de:
- Implementar conexões com banco de dados em Python
- Aplicar o padrão MVC
- Gerenciar configurações sensíveis com variáveis de ambiente
- Estruturar um projeto web com organização adequada

## Contato

[Adicione informações de contato aqui]
