from storage.database import Base, engine
from models.article import Article
from collectors.rss_collector import collect
from collectors.article_scraper import scrape
from storage.article_repository import save

Base.metadata.create_all(engine)

articles = collect("https://techcrunch.com/feed/")

for article in articles:
    scraped = scrape(article["url"])
    if scraped is None:
        continue
    article["content"] = scraped["content"]
    save(article)
