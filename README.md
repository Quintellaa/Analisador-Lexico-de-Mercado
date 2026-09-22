# Participantes

Victor Borges Quintella de Almeida - 2544963 <br> Kathleen Aquino Lima - 2364196 <br> João Victor Brandão - 2359197 <br> Lucas Costa - 2361186


---
# 📦 Analisador Léxico de Mercado — Simulador de Rastreio

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Gradio](https://img.shields.io/badge/Gradio-Interface-orange?logo=gradio)
![Pandas](https://img.shields.io/badge/Pandas-Dataframe-green?logo=pandas)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)

---

## 📋 Visão Geral

Este projeto implementa um **analisador léxico** para entradas relacionadas a rastreamento de encomendas e simula o processo de entrega.  
A interface é construída com **Gradio**, permitindo interação em abas para análise de tokens, rastreamento, pós‑processamento e execução de casos de teste.

### Exemplos de Entrada
- Número do Rastreio  
- Status  
- Saiu para entrega  
- Horário  

---

## ✨ Funcionalidades

- 🔎 **Tabela de Tokens** — identifica palavras reservadas, códigos de rastreio, datas, horas, CEPs e strings entre aspas  
- 📦 **Rastreamento de Encomenda** — simula eventos de entrega com linha do tempo  
- 📊 **Pós‑Processamento** — gera resumo da entrega, progresso e alertas  
- 🧪 **Casos de Teste** — valida entradas válidas e inválidas  
- 📖 **Diário de Ambiguidade** — documenta decisões sobre conflitos de tokens  

---

## 🛠️ Tecnologias Utilizadas

| Camada      | Tecnologia                        |
|-------------|-----------------------------------|
| Back-end    | Python 3, Regex, Pandas           |
| Interface   | Gradio                            |
| Fonte       | Google Fonts — Inter              |

---

## 📁 Estrutura do Projeto

Analisador-Rastreio/
├── app.py          # Código principal com definição de tokens, funções e interface Gradio
├── lexer()         # Função de análise léxica
├── rastrear()      # Simulação de rastreamento de encomenda
├── pos_processamento() # Pós-processamento e resumo da entrega
├── testes()        # Casos de teste válidos e inválidos
└── README.md       # Documentação do projeto
