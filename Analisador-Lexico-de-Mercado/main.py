import gradio as gr
import pandas as pd
import re

# -------------------------------
# Definição dos Tokens
# -------------------------------
tokens = [
    ("RASTREIO", r"\bRASTREIO\b", "Palavra reservada"),
    ("STATUS", r"\bSTATUS\b", "Palavra reservada"),
    ("CEP", r"\bCEP\b", "Palavra reservada"),
    ("EM", r"\bEM\b", "Palavra reservada"),
    ("CODIGO_OBJ", r"[A-Z]{2}[0-9]{9}[A-Z]{2}", "Código de rastreio"),
    ("DATA", r"\d{2}/\d{2}/\d{4}", "Data"),
    ("HORA", r"\d{2}:\d{2}", "Hora"),
    ("CEP_VALOR", r"\d{5}-\d{3}", "CEP"),
    ("STRING", r"\"[^\"]*\"", "Texto entre aspas"),
    ("NUMERO", r"\d+", "Número"),
    ("COMENTARIO", r"#.*", "Comentário"),
    ("ESPACO", r"\s+", "Espaço"),
]

# -------------------------------
# Analisador Léxico
# -------------------------------


def lexer(texto):
    tabela = []
    for nome, regex, desc in tokens:
        for match in re.finditer(regex, texto, flags=re.IGNORECASE):
            tabela.append({
                "Token": nome,
                "Lexema": match.group(),
                "Posição": match.start(),
                "Descrição": desc
            })
    if not tabela:
        return pd.DataFrame([{
            "Token": "ERRO",
            "Lexema": "Nenhum token reconhecido",
            "Posição": "-",
            "Descrição": "Verifique o formato da entrada"
        }])
    return pd.DataFrame(tabela)

# -------------------------------
# Rastreador visual
# -------------------------------


def rastrear(codigo):
    if not re.match(r"[A-Z]{2}[0-9]{9}[A-Z]{2}", codigo):
        return "❌ Erro léxico na linha 1, coluna 1.\nDicas:\n1. Código deve ter 2 letras + 9 dígitos + 2 letras.\n2. Exemplo válido: BR123456789BR", None

    eventos = [
        ["10/09/2026 08:15", "Centro de Postagem - São Paulo/SP", "📦 Objeto postado"],
        ["11/09/2026 14:30", "Centro de Distribuição - Campinas/SP",
            "🟡 Objeto em trânsito"],
        ["12/09/2026 09:00", "Unidade de Entrega - São Paulo/SP", "🔵 Saiu para entrega"],
        ["12/09/2026 13:45", "São Paulo/SP", "🟢 Entregue"]
    ]
    df = pd.DataFrame(eventos, columns=["Data/Hora", "Local", "Status"])
    return f"🔍 Rastreamento de {codigo}", df

# -------------------------------
# Pós-processamento
# -------------------------------


def pos_processamento(codigo):
    try:
        # Validação do formato do código
        if not re.match(r"[A-Z]{2}[0-9]{9}[A-Z]{2}", codigo):
            df_vazio = pd.DataFrame(
                [{"Item": "Erro", "Valor": "Código inválido"}])
            texto_erro = "⚠️ Nenhum dado gerado — formato incorreto."
            return "❌ Código inválido.", df_vazio, texto_erro

        # Simulação de análise
        resumo = [
            ["Total de eventos", "4"],
            ["Tempo total", "3 dias"],
            ["Status final", "🟢 Entregue"]
        ]
        df = pd.DataFrame(resumo, columns=["Item", "Valor"])

        progresso = "🟩🟩🟩🟩 100% concluído"
        alertas = "✅ Nenhum problema detectado. Entrega concluída com sucesso!"
        texto_final = f"{progresso}\n\n{alertas}"

        # Retorno correto: texto, DataFrame, texto
        return f"📊 Análise da entrega de {codigo}", df, texto_final

    except Exception as e:
        # Captura qualquer erro inesperado
        df_erro = pd.DataFrame([{"Item": "Erro interno", "Valor": str(e)}])
        texto_erro = "⚠️ Ocorreu um erro inesperado. Tente novamente."
        return "❌ Erro no processamento.", df_erro, texto_erro


# -------------------------------
# Casos de testeS
# -------------------------------
def testes():
    casos_validos = [
        'RASTREIO BR123456789BR STATUS "saiu para entrega" CEP 01310-100 EM 10/09/2026 08:15',
        'RASTREIO BR987654321BR STATUS "aguardando retirada" CEP 04567-890 EM 01/01/2025 14:30',
        'RASTREIO BR111222333BR STATUS "entregue" CEP 22040-001 EM 25/12/2024 09:00'
    ]
    casos_invalidos = [
        'RASTREIO BR123 STATUS "ok" CEP 99999-999 EM 99/99/9999 99:99',
        'RASTREIO BR123456789BR STATUS saiu_para_entrega CEP 01310-100 EM 10-09-2026 08:15'
    ]

    resultados = []
    for caso in casos_validos:
        resultados.append(f"✅ Válido: {caso}")
    for caso in casos_invalidos:
        resultados.append(f"❌ Inválido: {caso}")
    return "\n".join(resultados)


# -------------------------------
# Interface Gradio
# -------------------------------
with gr.Blocks() as app:
    gr.Markdown("## 📦 Analisador Léxico de Mercado — Simulador de Rastreio")

    with gr.Tab("Tabela de Tokens"):
        entrada = gr.Textbox(lines=5, label="Entrada")
        tabela = gr.Dataframe(label="Tabela de Tokens")
        botao = gr.Button("Analisar")
        botao.click(lexer, entrada, tabela)

    with gr.Tab("Rastreamento"):
        codigo = gr.Textbox(
            label="Digite o código de rastreio (ex: BR123456789BR)", value="BR123456789BR")
        resultado = gr.Textbox(label="Resultado")
        tabela = gr.Dataframe(label="Linha do Tempo da Encomenda")
        botao = gr.Button("Rastrear Encomenda")
        botao.click(rastrear, codigo, [resultado, tabela])

    with gr.Tab("Pós‑Processamento"):
        codigo2 = gr.Textbox(label="Digite novamente o código de rastreio", value="BR123456789BR")
        titulo = gr.Textbox(label="Título")  # NOVO
        resumo = gr.Dataframe(label="Resumo da Entrega")
        alertas = gr.Textbox(label="Alertas e Progresso", lines=5)
        botao2 = gr.Button("Gerar Análise")
        botao2.click(pos_processamento, codigo2, [titulo, resumo, alertas])

    with gr.Tab("Casos de Teste"):
        resultados = gr.Textbox(label="Resultados dos Testes", lines=10)
        botao3 = gr.Button("Executar Testes")
        botao3.click(testes, None, resultados)

    with gr.Tab("Diário de Ambiguidade"):
        gr.Markdown("""
### Diário de Ambiguidade
Durante o desenvolvimento, houve conflito entre o token **STRING** (`"texto"`) e as palavras reservadas (ex.: `"STATUS"`).
**Decisão:** priorizar **STRING** quando delimitada por aspas, pois no domínio de rastreio o status sempre vem entre aspas.
Assim, `"STATUS"` é tratado como texto literal, não como palavra reservada.
        """)

app.launch()
