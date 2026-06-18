from storage.database import Base, engine
from models.article import Article
from collectors.rss_collector import collect
from collectors.article_scraper import scrape, scrape_venturebeat
from storage.article_repository import save
from agents.ai_generator import generate

Base.metadata.create_all(engine)

articles = collect("https://venturebeat.com/feed") + collect(
    "https://techcrunch.com/feed/"
)

for article in articles:
    if "venturebeat.com" in article["url"]:
        scraped = scrape_venturebeat(article["url"])
    else:
        scraped = scrape(article["url"])
    if scraped is None:
        continue
    article["content"] = scraped["content"]
    summary = generate(article["content"])
    article["summary_short"] = summary["short"]
    article["summary_medium"] = summary["medium"]
    article["summary_long"] = summary["long"]

    save(article)
