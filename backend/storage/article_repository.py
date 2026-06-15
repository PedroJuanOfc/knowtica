from models.article import Article
from storage.database import SessionLocal

def save(data):
    article = Article(
        title=data["title"],
        url=data["url"],
        published_at=data["published_at"],
        source=data["source"]
    )
    session = SessionLocal()
    session.add(article)
    session.commit()
    session.close()