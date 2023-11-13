from typing import List

from rest_api.common.base_endpoint import BaseEndpoint
from rest_api.placeholder_ms.model.post_model import PostDto


class PostEndpoint(BaseEndpoint):
    def __init__(self, base_url):
        super().__init__(base_url)

    def get_posts(self, **kwargs) -> List[PostDto]:
        response_data = self.get('/posts', **kwargs)
        return self.pydentic_deserialize(response_data.json(), PostDto)

    def get_post(self, post_id, **kwargs) -> PostDto:
        response_data = self.get(f'/posts/{post_id}', **kwargs)
        return self.pydentic_deserialize(response_data.json(), PostDto)

    def create_post(self, payload: PostDto, **kwargs) -> PostDto:
        response_data = self.post(
            '/posts',
            json=payload.dict(
                by_alias=True,
                exclude_none=True),
            **kwargs)
        return self.pydentic_deserialize(response_data.json(), PostDto)
