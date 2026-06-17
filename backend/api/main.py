from fastapi import FastAPI, Depends
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