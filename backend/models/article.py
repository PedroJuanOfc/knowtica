from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from storage.database import Base


class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    relevance_score = Column(Float, nullable=True)
    published_at = Column(DateTime, nullable=False)
    source = Column(String(255), nullable=False)
    url = Column(String(255), nullable=False)
    category = Column(String(255), nullable=False)
    tag = Column(String(255), nullable=False)
