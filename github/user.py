from pydantic import BaseModel, Field


class User(BaseModel):
    id_: int = Field(alias="id")
    bio: str | None = None
    repos_url: str
    html_url: str
    login: str
    url: str
