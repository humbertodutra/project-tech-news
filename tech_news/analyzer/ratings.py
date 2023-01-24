from tech_news.database import find_news
from collections import Counter


# Requisito 10
def top_5_news():
    """Seu código deve vir aqui"""
    news = find_news()
    sorted_news = sorted(
        news, key=lambda x: (x["comments_count"], x["title"]), reverse=True
    )

    five_news = [(new["title"], new["url"]) for new in sorted_news[:5]]

    return five_news


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
    news = find_news()
    categories = [new["category"] for new in news]
    sorted_categories = sorted(categories)
    categories_count = Counter(sorted_categories).most_common()
    topFive = [category[0] for category in categories_count[:5]]

    return topFive
