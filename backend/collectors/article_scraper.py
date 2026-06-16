import requests
from bs4 import BeautifulSoup

def scrape(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()

    html = response.text

    soup = BeautifulSoup(html, "html.parser")

    title = soup.find("h1", class_="article-hero__title").get_text(strip=True)
    entry_div = soup.find("div", class_="entry-content")
    paragraphs = entry_div.find_all("p", class_="wp-block-paragraph")
    content = " ".join([p.get_text(strip=True) for p in paragraphs])

    return {
        "title": title,
        "content": content
    }