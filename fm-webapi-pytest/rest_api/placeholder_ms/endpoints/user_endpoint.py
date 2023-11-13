from typing import List

from rest_api.common.base_endpoint import BaseEndpoint
from rest_api.placeholder_ms.model.user_model import UserDto


class UserEndpoint(BaseEndpoint):
    def __init__(self, base_url):
        super().__init__(base_url)

    def get_users(self, **kwargs) -> List[UserDto]:
        response_data = self.get('/users', **kwargs)
        return self.dataclass_deserialize(response_data.json(), UserDto)

    def get_user(self, user_id, **kwargs) -> UserDto:
        response_data = self.get(f'/users/{user_id}', **kwargs)
        return self.dataclass_deserialize(response_data.json(), UserDto)

    def get_user_as_dict(self, **kwargs) -> dict:
        response_data = self.get(f'/users', **kwargs)
        return response_data

    def create_user(self, payload: UserDto, **kwargs) -> UserDto:
        response_data = self.post(
            '/users',
            json=payload.as_dict(exclude_none=True),
            **kwargs)
        return self.dataclass_deserialize(response_data.json(), UserDto)
