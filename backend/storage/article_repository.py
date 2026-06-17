from models.article import Article
from storage.database import SessionLocal
from sqlalchemy import select

def save(data):
    article = Article(
        title=data["title"],
        url=data["url"],
        published_at=data["published_at"],
        source=data["source"]
    )
    session = SessionLocal()
    stmt = select(Article).where(Article.url == data["url"])
    existing = session.scalars(stmt).first()

    if existing is None:
        session.add(article)
        session.commit()
        session.close()
    else:
        existing.content = data.get("content")
        session.commit()
        session.close()

