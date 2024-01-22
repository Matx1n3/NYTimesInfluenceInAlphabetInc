import re
import requests
from relevant_words import relevant_words
from bs4 import BeautifulSoup


def get_wordbag_and_date(url):
    """
    Extrae información relevante de un artículo web, incluyendo un conjunto de palabras y la fecha de publicación.

    Parámetros:
        url (str): La URL del artículo web del cual extraer la información.

    Devoluciones:
        tuple: Una tupla que contiene un diccionario de palabras y la fecha de publicación.

    Uso:
        wordbag, published_date = get_wordbag_and_date('https://example.com/article')
    """

    headers = {
        'user-agent': 'curl/7.81.0',
        'accept': '*/*',
    }

    response = requests.get(url, headers=headers)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    published_date = '?'
    published_time = soup.find('meta', {'property': 'article:published_time'})
    if published_time:
        published_date = published_time['content'][0:10]

    matches = re.findall(r'"text":\s*"([^"]+)"', html)

    words = {word: 0 for word in relevant_words}

    for match in matches:
        for word in relevant_words:
            if word in match.lower():
                words[word] += 1

    return words, published_date
