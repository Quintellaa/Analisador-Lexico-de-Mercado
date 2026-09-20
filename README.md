# Participantes

Victor Borges Quintella de Almeida - 2544963 <br> Kathleen Aquino - 2364196 

---

# Analisador Lexico | Rastreio de Encomendas - Mercado Livre

---

## 📋 Visão Geral

### Exemplos de Entrada
* Numero do Rastreio
* Status
* Saiu para entrega
* Horario

---

## ✨ Funcionalidades

- 🔐 **Login por CPF** — autenticação simples e direta
- 💬 **Chat em linguagem natural** — o sistema classifica a intenção do usuário automaticamente
- 📊 **Consulta de dados** — fatura, limite, bloqueio, parcelas e senha
- ✏️ **Atualização de dados** — alteração de fatura e limite via conversa
- 🗑️ **Exclusão de conta** — com confirmação explícita do usuário
- 🗄️ **Banco de dados SQLite** — leve, local e sem dependências externas

---

## 🛠️ Tecnologias Utilizadas

| Camada      | Tecnologia                        |
|-------------|-----------------------------------|
| Back-end    | Python 3, Flask, Flask-CORS       |
| Banco       | SQLite3                           |
| Front-end   | HTML5, CSS3, JavaScript (Vanilla) |
| Fonte       | Google Fonts — Inter              |

---

## 📁 Estrutura do Projeto

```
MonoIA/
├── app.py          # Servidor Flask — rotas e lógica de classificação de intenção
├── crud.py         # Funções de acesso ao banco (Create, Read, Update, Delete)
├── database.py     # Script de criação e seed do banco de dados
├── clientes.db     # Banco de dados SQLite (gerado pelo database.py)
├── index.html      # Interface do chatbot (front-end)
├── respostas.json  # Respostas padrão por categoria (referência)
└── perguntas.csv   # Base de perguntas para testes
