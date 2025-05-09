from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()


def analyze_sentiment(texto: str) -> str:
    """
    Classifica o sentimento de um texto como 'positiva', 'negativa' ou 'neutra' utilizando VADER.

    A análise é baseada no score compound retornado pelo VADER, com os seguintes limiares:
    - >= 0.1: sentimento positivo
    - <= -0.1: sentimento negativo
    - entre -0.1 e 0.1: sentimento neutro

    Args:
        texto (str): Texto da avaliação a ser analisado.

    Returns:
        str: A classificação do sentimento ('positiva', 'negativa' ou 'neutra').
    """
    scores = analyzer.polarity_scores(texto)
    compound = scores["compound"]

    if compound >= 0.1:
        return "positiva"
    elif compound <= -0.1:
        return "negativa"
    else:
        return "neutra"
