# 💰 Monetary Control

![Python](https://img.shields.io/badge/python-3.12-blue)
![Django](https://img.shields.io/badge/django-4.x-green)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)
![Build](https://img.shields.io/badge/build-passing-brightgreen)

Sistema de controle financeiro desenvolvido em **Django** com foco em **DDD soft**, Clean Code e Clean Architecture.  
Projeto de estudo com APIs REST e autenticação JWT.

---

## 🛠 Tecnologias

- Python 3.12  
- Django 4.x  
- Django REST Framework  
- JWT para autenticação  
- SQLite (desenvolvimento)  
- Factory Boy + Pytest para testes  

---

## 📁 Estrutura do projeto


monetary-control/
│
├── finance/ # Core do domínio
│ ├── models/ # Models DDD soft
│ │ ├── account.py
│ │ ├── category.py
│ │ └── transaction.py
│ ├── repositories/
│ └── services/
│
├── finance/api/ # API REST
│ ├── serializers/
│ │ ├── transaction_serializer.py
│ ├── views.py
│ └── urls.py
│
├── finance/tests/ # Testes unitários e de integração
│
├── manage.py
├── requirements.txt
└── README.md


---

## ⚙️ Setup do projeto

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/monetary-control.git
cd monetary-control

Crie e ative um virtualenv:

python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows

Instale as dependências:

pip install -r requirements.txt

Rode migrações:

python manage.py migrate

Crie superusuário:

python manage.py createsuperuser

Inicie o servidor:

python manage.py runserver
✅ Rodando testes
pytest

Testes usam Factory Boy para dados fictícios

Cobrem services, usecases e APIs

📌 API Reference

Todos os endpoints protegidos requerem Bearer JWT.

🔑 Autenticação
Endpoint	Método	Descrição
/api/token/	POST	Obter access e refresh tokens
/api/token/refresh/	POST	Renovar access token

Request exemplo:

{
  "username": "usuario1",
  "password": "senha123"
}

Resposta:

{
  "refresh": "<refresh_token>",
  "access": "<access_token>"
}

Use o access no header Authorization: Bearer <access_token>.

💰 Criar transação
Endpoint	Método	Descrição
/api/transactions/	POST	Criar transação (EXPENSE ou INCOME)

Payload - Expense:

{
  "account": 1,
  "category": 1,
  "amount": "50.00",
  "type": "EXPENSE",
  "description": "Mercado"
}

Payload - Income:

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
📊 Relatório de transações
Endpoint	Método	Descrição
/api/transactions/report/	GET	Listar todas as transações do usuário

Parâmetros opcionais:

type → EXPENSE ou INCOME (filtra por tipo)

Exemplo de requisição:

GET /api/transactions/report/?type=EXPENSE
Authorization: Bearer <access_token>

Resposta exemplo:

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
🔄 Fluxo completo de uso

Obter token JWT via /api/token/.

Criar transações (POST /api/transactions/) usando token no header.

Consultar relatório (GET /api/transactions/report/) com ou sem filtro de tipo.

⚡ Notas técnicas

account e category devem existir antes de criar transações.

Tipos válidos: EXPENSE (despesa), INCOME (receita)

created_at gerado automaticamente

Transações vinculadas ao usuário autenticado (request.user)