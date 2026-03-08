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

