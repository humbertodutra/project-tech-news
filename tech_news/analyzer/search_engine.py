from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    newByTitle = search_news({"title": {"$regex": title, "$options": "i"}})
    return [(news["title"], news["url"]) for news in newByTitle]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        format_date = datetime.fromisoformat(date).strftime("%d/%m/%Y")
        q = {"timestamp": {"$eq": format_date}}
        newsMatch = search_news(q)
        return [(news["title"], news["url"]) for news in newsMatch]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""
    newsList = []
    newsByTAG = search_news({"tags": {"$regex": tag, "$options": "i"}})
    for new in newsByTAG:
        newsList.append((new["title"], new["url"]))
    return newsList


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    newsList = []
    newsByCategory = search_news({
        "category": {"$regex": category, "$options": "i"}})
    for new in newsByCategory:
        newsList.append((new["title"], new["url"]))
    return newsList
