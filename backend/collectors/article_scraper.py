import requests
from bs4 import BeautifulSoup

def scrape(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()

    html = response.text

    soup = BeautifulSoup(html, "html.parser")

    title_tag = soup.find("h1", class_="article-hero__title")
    if title_tag is None:
        return None
    title = title_tag.get_text(strip=True)

    entry_tag = soup.find("div", class_="entry-content")
    if entry_tag is None:
        return None
    paragraphs = entry_tag.find_all("p", class_="wp-block-paragraph")
    content = " ".join([p.get_text(strip=True) for p in paragraphs])

    return {
        "title": title,
        "content": content
    }