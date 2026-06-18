from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime


class ArticleResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    source: str
    url: str
    summary_short: Optional[str]
    summary_medium: Optional[str]
    summary_long: Optional[str]
    published_at: datetime
