import feedparser


def collect(url):
    feed = feedparser.parse(url)
    articles = []
    for entry in feed.entries:
        articles.append(
            {
                "title": entry.title,
                "url": entry.link,
                "published_at": entry.published,
                "source": feed.feed.title,
            }
        )
    return articles
