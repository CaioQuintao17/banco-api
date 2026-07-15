# Banco API

Projeto de sistema bancário desenvolvido com FastAPI no backend e HTML, CSS e JavaScript no frontend.

---

#  Funcionalidades

Criar conta  
Consultar saldo  
Depositar dinheiro  
Sacar dinheiro  
Transferir entre contas  

---

#  Tecnologias utilizadas

## Backend
- Python
- FastAPI
- SQLAlchemy
- SQLite
- Uvicorn

## Frontend
- HTML
- CSS
- JavaScript

---

# 📂 Estrutura do Projeto

```bash
banco_api/
│
├── back_end/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│
├── front_end/
│   ├── index.html
│   ├── style.css
│   ├── script.js
│
└── README.md
```

---

# ⚙️ Como executar o projeto

## 1️⃣ Clonar repositório

```bash
git clone https://github.com/CaioQuintao17/banco-api.git
```

---

## 2️⃣ Entrar na pasta

```bash
cd banco-api
```

---

#  Backend

## Entrar na pasta backend

```bash
cd back_end
```

---

## Instalar dependências

```bash
pip install fastapi uvicorn sqlalchemy aiosqlite
```

---

## Rodar servidor

```bash
uvicorn main:app --reload
```

Servidor:
```bash
http://127.0.0.1:8000
```

Swagger:
```bash
http://127.0.0.1:8000/docs
```

---

#  Frontend

Abra:

```bash
front_end/index.html
```

Ou utilize:
- Live Server no VS Code

---

#  Objetivo do Projeto

Projeto criado para estudos de:
- APIs REST
- FastAPI
- Backend Python
- Integração frontend/backend
- Banco de dados
- Git e GitHub

---


Desenvolvido por Caio Quintão 🚀
