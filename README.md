# monetary-control

[![Python](https://img.shields.io/badge/python-3.12-blue)](https://www.python.org/)  
[![Django](https://img.shields.io/badge/django-4.x-green)](https://www.djangoproject.com/)  
[![Pytest](https://img.shields.io/badge/tests-pytest-orange)](https://docs.pytest.org/)  
[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)](https://github.com/seu-usuario/monetary-control/actions)  
[![License](https://img.shields.io/badge/license-MIT-lightgrey)](LICENSE)  

Um projeto Django de estudo para **controle financeiro pessoal**, utilizando **DDD soft**, **Clean Code** e **Clean Architecture**, com APIs REST e autenticação JWT.  

O objetivo é criar um **sistema simples de gestão financeira**, permitindo criar transações (receitas e despesas), categorizar, gerar relatórios e praticar boas práticas de arquitetura de software.  

---

## Tecnologias

- Python 3.12  
- Django 4.x  
- Django REST Framework  
- SQLite (para estudo; pode ser substituído por PostgreSQL)  
- JWT (via `djangorestframework-simplejwt`)  

---

## Arquitetura

- **DDD soft:** separação de **models**, **services**, **repositories** e **use cases** mantendo o Django funcional.  
- **Clean Architecture:** cada camada com responsabilidade única.  
- **Clean Code:** nomes claros, consistência, DTOs e validações centralizadas.  

Estrutura do projeto:

```text
monetary-control/
├─ finance/
│  ├─ models/               # Modelos (transaction, account, category)
│  ├─ repositories/         # Acesso a dados
│  ├─ services/             # Lógica de negócio
│  ├─ api/
│  │  ├─ serializers/       # Serializers Django REST
│  │  ├─ views.py           # Endpoints
│  │  └─ urls.py            # Rotas da API
│  └─ tests/                # Testes unitários e de API
└─ manage.py
```

Este projeto possui uma **API REST** construída com **Django REST Framework** e protegida por **autenticação JWT**.  

---

## 🔑 Autenticação JWT

| Endpoint           | Método | Descrição                          | Autenticação |
|------------------|--------|-----------------------------------|--------------|
| `/api/token/`     | POST   | Obter tokens JWT (access e refresh) | Não          |
| `/api/token/refresh/` | POST | Renovar token access usando refresh | Não          |

**Exemplo de request para obter JWT:**

```json
{
  "username": "usuario1",
  "password": "senha123"
}

Exemplo de resposta:

{
  "refresh": "<refresh_token>",
  "access": "<access_token>"
}

Exemplo de resposta:

{
  "refresh": "<refresh_token>",
  "access": "<access_token>"
}

💰 Criar Transação
Endpoint	Método	Descrição	Autenticação
/api/transactions/	POST	Criar transação (expense ou income)	Sim

Payload para despesa (expense):

{
  "account": 1,
  "category": 1,
  "amount": "50.00",
  "type": "EXPENSE",
  "description": "Mercado"
}

Payload para receita (income):

{
  "account": 1,
  "category": 2,
  "amount": "1000.00",
  "type": "INCOME",
  "description": "Salário"
}

Resposta esperada:

{
  "id": 1
}
📊 Relatório de Transações
Endpoint	Método	Descrição	Autenticação
/api/transactions/report/	GET	Listar todas as transações do usuário	Sim

Parâmetros opcionais:

type → EXPENSE ou INCOME (filtra por tipo de transação)

Exemplo de requisição filtrada:

GET /api/transactions/report/?type=EXPENSE
Authorization: Bearer <access_token>

Exemplo de resposta:

[
  {
    "id": 1,
    "account": 1,
    "category": 1,
    "amount": "50.00",
    "type": "EXPENSE",
    "description": "Mercado",
    "created_at": "2026-03-07T18:45:00Z"
  },
  {
    "id": 2,
    "account": 1,
    "category": 2,
    "amount": "1000.00",
    "type": "INCOME",
    "description": "Salário",
    "created_at": "2026-03-07T18:50:00Z"
  }
]
⚙️ Notas técnicas

Todos os endpoints protegidos exigem Bearer JWT no header.

account e category devem existir no banco antes de criar transações.

Tipos válidos para type:

EXPENSE → despesa

INCOME → receita

O sistema gera automaticamente a data de criação (created_at).

As transações são vinculadas ao usuário autenticado (request.user).

🔄 Fluxo de uso sugerido

Obter token JWT via /api/token/.

Criar transações usando POST /api/transactions/ com token no header.

Consultar relatório usando GET /api/transactions/report/.

Filtrar relatório por tipo: /api/transactions/report/?type=EXPENSE ou ?type=INCOME.

💡 Exemplo completo do fluxo

Obter token:

curl -X POST http://127.0.0.1:8000/api/token/ \
-H "Content-Type: application/json" \
-d '{"username": "usuario1", "password": "senha123"}'

Criar despesa:

curl -X POST http://127.0.0.1:8000/api/transactions/ \
-H "Authorization: Bearer <access_token>" \
-H "Content-Type: application/json" \
-d '{"account":1,"category":1,"amount":"50.00","type":"EXPENSE","description":"Mercado"}'

Criar receita:

curl -X POST http://127.0.0.1:8000/api/transactions/ \
-H "Authorization: Bearer <access_token>" \
-H "Content-Type: application/json" \
-d '{"account":1,"category":2,"amount":"1000.00","type":"INCOME","description":"Salário"}'

Consultar relatório:

curl -X GET http://127.0.0.1:8000/api/transactions/report/ \
-H "Authorization: Bearer <access_token>"

Consultar relatório filtrado por tipo:

curl -X GET http://127.0.0.1:8000/api/transactions/report/?type=EXPENSE \
-H "Authorization: Bearer <access_token>"