from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from storage.database import SessionLocal
from models.article import Article
from api.schemas import ArticleResponse

app = FastAPI()

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

@app.get("/articles", response_model=list[ArticleResponse])
def list_articles(session: Session = Depends(get_session)):
    articles = session.query(Article).all()
    return articles


@app.get("/articles/{article_id}", response_model=ArticleResponse)
def get_article(article_id: int, session: Session = Depends(get_session)):
    article = session.query(Article).filter(Article.id == article_id).first()
    if article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    return article