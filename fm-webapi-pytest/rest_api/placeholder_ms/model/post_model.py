from typing import Optional

from pydantic import BaseModel, Field


class PostDto(BaseModel):
    id: Optional[int] = Field(alias='id')
    user_id: int = Field(alias='userId')
    title: str = Field(alias='title')
    body: str = Field(alias='body')

    class Config:
        fields = {
            'user_id': 'userId'
        }
        allow_population_by_field_name = True
