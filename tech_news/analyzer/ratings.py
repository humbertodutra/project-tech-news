from tech_news.database import find_news


# Requisito 10
def top_5_news():
    """Seu código deve vir aqui"""
    news = find_news()
    sorted_news = sorted(
        news, key=lambda x: (x["comments_count"], x["title"]), reverse=True
    )

    five_news = [(new['title'], new['url']) for new in sorted_news[:5]]

    return five_news


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""


top_5_news()
