from storage.database import Base, engine
from models.article import Article

Base.metadata.create_all(engine)
