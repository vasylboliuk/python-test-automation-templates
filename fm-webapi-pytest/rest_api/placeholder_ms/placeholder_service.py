from rest_api.common.base_client import BaseApiClient
from rest_api.placeholder_ms.endpoints.post_endpoint import PostEndpoint
from rest_api.placeholder_ms.endpoints.user_endpoint import UserEndpoint


class PlaceholderService(BaseApiClient):

    _v2 = "v2"

    def __init__(self):
        super().__init__('PlaceholderService')
        # self._user_endpoint = UserEndpoint(f"{self.url}/{self.api_base_path}/{self._v2}")
        self._user_endpoint = UserEndpoint(f"{self.url}")
        self._post_endpoint = PostEndpoint(f"{self.url}")

    def user(self):
        return self._user_endpoint

    def post(self):
        return self._post_endpoint
