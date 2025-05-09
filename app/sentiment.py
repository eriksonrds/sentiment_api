from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()


def analyze_sentiment(texto: str) -> str:
    """
    Realiza análise de sentimento usando VADER.

    Args:
        texto (str): Texto da avaliação.

    Returns:
        str: Classificação 'positiva', 'negativa' ou 'neutra'.
    """
    scores = analyzer.polarity_scores(texto)
    compound = scores["compound"]

    if compound >= 0.1:
        return "positiva"
    elif compound <= -0.1:
        return "negativa"
    else:
        return "neutra"
