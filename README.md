# Flask Microservices Event Bus & Webhook Router

[![Flask CI](https://github.com/FelipeMadson/flask-microservices-event-bus/actions/workflows/ci.yml/badge.svg)](https://github.com/FelipeMadson/flask-microservices-event-bus/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Release](https://img.shields.io/badge/release-v1.0.0-green.svg)](https://github.com/FelipeMadson/flask-microservices-event-bus/releases)

High-throughput, decoupled event bus and webhook dispatching router built in Python 3.12 and Flask 3.

## Architecture

```mermaid
flowchart LR
    Ingress["HTTP Webhook Ingress"] --> Bus["Microservice Event Bus"]
    Bus --> BillingSub["Billing Consumer"]
    Bus --> AuditSub["Audit Trail Consumer"]
    Bus --> NotificationSub["Notification Worker"]
```

## Key Characteristics

- **Decoupled Pub/Sub Engine**: High-speed topic subscriptions with typed Pydantic payloads.
- **Audit & Replay History**: In-memory historical event journal for delivery verification and debugging.
- **Zero Heavy Brokers**: Lightweight, self-contained architecture suitable for serverless and containerized microservices.

## Testing

```bash
pip install -e ".[test]"
pytest -v
```

## Author

Developed by **[Felipe Madison](https://github.com/FelipeMadson)**.
