import requests
import time
import re
from parsel import Selector
from tech_news.database import create_news

# Requisito 1


def fetch(url):
    """Seu código deve vir aqui"""
    headers = {"user-agent": "Fake user-agent"}
    time.sleep(1)
    try:
        response = requests.get(url, headers=headers, timeout=3)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.exceptions.RequestException:
        return None


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)
    links = selector.css("h2.entry-title a::attr(href)").getall()
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)
    next_page = selector.css("a.next.page-numbers::attr(href)").get()
    return next_page


def clear_html(text):
    clean = re.compile("<.*?>")
    return re.sub(clean, "", text)


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)
    return {
        "url": selector.css("link[rel='canonical']::attr(href)").get(),
        "title": selector.css("h1.entry-title::text").get().strip(),
        "timestamp": selector.css(".meta-date::text").get(),
        "writer": selector.css(".author a::text").get(),
        "comments_count": len(selector.css("comment-list li").getall()) or 0,
        "summary": clear_html(selector.css(".entry-content p").get()).strip(),
        "tags": selector.css(".post-tags li a::text").getall(),
        "category": selector.css(".meta-category .label::text").get(),
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    URL = "https://blog.betrybe.com/"

    links = []
    news = []

    while len(links) <= amount:
        html = fetch(URL)
        links.extend(scrape_updates(html))
        URL = scrape_next_page_link(html)

    for link in links[:amount]:
        page = fetch(link)
        news.append(scrape_news(page))

    create_news(news)
    return news
