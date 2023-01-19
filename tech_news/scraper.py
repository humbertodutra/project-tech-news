import requests
import time

# Requisito 1


def fetch(url):
    """Seu código deve vir aqui"""
    headers = {"user-agent": "Fake user-agent"}
    time.sleep(1)  # garante um intervalo de 1 segundo entre cada requisição
    try:
        response = requests.get(
            url, headers=headers, timeout=3
        )  # especifica um timeout de 3 segundos
        if response.status_code == 200:
            print(response.text)
            return response.text
        else:
            return None
    except requests.exceptions.RequestException:
        return None


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


