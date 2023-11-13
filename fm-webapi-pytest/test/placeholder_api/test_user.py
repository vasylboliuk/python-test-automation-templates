from assertpy import assert_that

from rest_api.common.enum.http_status import HttpStatus
from rest_api.placeholder_ms.model.user_model import UserDto
from rest_api.placeholder_ms.placeholder_service import PlaceholderService
from test.base_service_test import BaseApiTest


class TestUserEndpoint(BaseApiTest):

    def test_get_users_list(self):
        users = PlaceholderService().user().get_users()
        assert_that(users).is_not_empty()
        assert_that(len(users)).is_greater_than(5)

    def test_get_users_list_failed(self):
        users = PlaceholderService().user().get_users()
        assert_that(len(users)).is_greater_than(10)

    def test_get_users_list_failed_status_code(self):
        users = PlaceholderService().user().get_users(status_code=HttpStatus.BAD_REQUEST.code)

    def test_get_user_by_id(self):
        users = PlaceholderService().user().get_users()
        first_user = users[0]
        user_id = first_user.id
        user = PlaceholderService().user().get_user(user_id)
        assert_that(user.name).is_equal_to("Leanne Graham")
        assert_that(user.username).is_equal_to("Bret")

    def test_create_user(self):
        user_data = UserDto(
            name="Vasyl",
            username="vbol"
        )
        user_response = PlaceholderService().user().create_user(user_data)
        assert_that(user_response.name).is_equal_to(user_data.name)
        assert_that(user_response.username).is_equal_to(user_data.username)
        assert_that(user_response.id).is_equal_to(11)  # new created user get 11 ID

