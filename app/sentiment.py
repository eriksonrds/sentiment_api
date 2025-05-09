from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import requests
from urllib.parse import quote
import urllib3

# Silencia os avisos de verificação SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

analyzer = SentimentIntensityAnalyzer()


def traduzir_pt_en(texto: str) -> str:
    """
    Realiza a tradução de um texto do português para o inglês
    utilizando a versão mobile do Google Translate via requisição HTTP.
    A verificação SSL é desativada para evitar erros em ambientes com certificados não confiáveis.

    Args:
        texto (str): Texto em português a ser traduzido.

    Returns:
        str: Texto traduzido para o inglês. Em caso de erro, retorna o texto original.
    """
    try:
        url = f"https://translate.google.com/m?tl=en&sl=pt&q={quote(texto)}"
        headers = {"User-Agent": "Mozilla/5.0"}

        response = requests.get(url, headers=headers, verify=False)
        response.raise_for_status()

        inicio = response.text.find('class="result-container">') + len(
            'class="result-container">'
        )
        fim = response.text.find("</div>", inicio)
        traducao = response.text[inicio:fim].strip()
        return traducao
    except Exception as e:
        print(f"[ERRO DE TRADUÇÃO] {e}")
        return texto


def analyze_sentiment(texto: str) -> str:
    """
    Traduz um texto em português para inglês e classifica seu sentimento
    como 'positiva', 'negativa' ou 'neutra', utilizando VADER.

    O threshold é definido como:
    - >= 0.4: positiva
    - <= -0.4: negativa
    - Entre -0.4 e 0.4: neutra

    Args:
        texto (str): Texto em português.

    Returns:
        str: Classificação de sentimento ('positiva', 'negativa' ou 'neutra').
    """
    texto_en = traduzir_pt_en(texto)
    scores = analyzer.polarity_scores(texto_en)
    compound = scores["compound"]

    if compound >= 0.3:
        return "positiva"
    elif compound <= -0.3:
        return "negativa"
    else:
        return "neutra"
