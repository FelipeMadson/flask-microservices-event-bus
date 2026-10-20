# Barramento de Eventos e Roteador de Webhooks com Flask 3

[![Flask CI](https://github.com/FelipeMadson/flask-microservices-event-bus/actions/workflows/ci.yml/badge.svg)](https://github.com/FelipeMadson/flask-microservices-event-bus/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Release](https://img.shields.io/badge/release-v1.0.0-green.svg)](https://github.com/FelipeMadson/flask-microservices-event-bus/releases)

Barramento de eventos desacoplado e roteador de webhooks de alta performance em Python 3.12 e Flask 3.

## Arquitetura de Microsserviços

```mermaid
flowchart LR
    Origem["Ingresso de Webhooks"] --> Barramento["Microservice Event Bus"]
    Barramento --> Faturamento["Consumidor de Faturamento"]
    Barramento --> Auditoria["Consumidor de Auditoria"]
    Barramento --> Notificacao["Trabalhador de Notificações"]
```

## Destaques de Engenharia

- **Padrão Pub/Sub Tipado**: Inscrição por tópicos com validação estrita de esquemas via Pydantic v2.
- **Histórico Auditável**: Registro em memória de todos os eventos recebidos para inspeção e depuração.
- **Leve e Hermético**: Zero necessidade de brokers externos pesados para ambientes isolados.

## Execução e Testes

```bash
pip install -e ".[test]"
pytest -v
```

## Autor

Desenvolvido por **[Felipe Madison](https://github.com/FelipeMadson)**.
