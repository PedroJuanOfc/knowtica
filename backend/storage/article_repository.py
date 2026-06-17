from models.article import Article
from storage.database import SessionLocal
from sqlalchemy import select

def save(data):
    article = Article(
        title=data["title"],
        url=data["url"],
        published_at=data["published_at"],
        source=data["source"],
        content=data["content"],
        summary_short=data["summary_short"],
        summary_medium=data["summary_medium"],
        summary_long=data["summary_long"]
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
        existing.summary_short = data.get("summary_short")
        existing.summary_medium = data.get("summary_medium")
        existing.summary_long = data.get("summary_long")
        session.commit()
        session.close()

