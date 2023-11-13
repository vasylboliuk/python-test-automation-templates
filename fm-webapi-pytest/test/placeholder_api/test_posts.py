from assertpy import assert_that

from core.utils.generator import Faker
from rest_api.common.enum.http_status import HttpStatus
from rest_api.placeholder_ms.model.post_model import PostDto
from rest_api.placeholder_ms.placeholder_service import PlaceholderService
from test.base_service_test import BaseApiTest


class TestPostEndpoint(BaseApiTest):

    def test_get_posts_list(self):
        posts = PlaceholderService().post().get_posts()
        assert_that(posts).is_not_empty()
        assert_that(len(posts)).is_greater_than(20)

    def test_get_posts_list_failed_status_code(self):
        posts = PlaceholderService().post().get_posts(status_code=HttpStatus.BAD_REQUEST.code)

    def test_get_post_by_id(self):
        hardcoded_post_id = 1
        post = PlaceholderService().post().get_post(hardcoded_post_id)
        assert_that(post.title).contains("sunt aut facere")
        assert_that(post.body).contains("quia et suscipit\nsuscipit")

    def test_create_post(self):
        post_data = PostDto(
            user_id=1,
            title=f"Automation Test Post Title {Faker.get_random_string_len(10)}",
            body=f"Automation Test Post Body {Faker.get_random_string_len(20)}"
        )
        post_response = PlaceholderService().post().create_post(post_data)
        assert_that(post_response.title).is_equal_to(post_data.title)
        assert_that(post_response.body).is_equal_to(post_data.body)
        assert_that(post_response.user_id).is_equal_to(post_data.user_id)
