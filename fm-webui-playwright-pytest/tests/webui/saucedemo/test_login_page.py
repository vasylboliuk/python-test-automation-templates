import pytest
from assertpy import assert_that

from core.webui.pages.login_page import LoginPage
from tests.webui.base_webui_test import BaseWebUiTest


class TestLoginPage(BaseWebUiTest):


    @pytest.mark.regression
    def test_success_login(self):
        LoginPage().navigate()
        LoginPage().login_to_site("standard_user", "secret_sauce")
        main_page = LoginPage().products_page()
        app_logo_label = main_page.app_logo_label().text_content()
        products_label = main_page.products_label().text_content()
        # Validation
        assert_that(app_logo_label).is_equal_to("Swag Labs")
        assert_that(products_label).is_equal_to("Products")

    @pytest.mark.regression
    def test_username_password_is_required(self):
        LoginPage().navigate()
        LoginPage().click_login()
        error_msg = LoginPage().error_msg()
        # Validation
        assert_that(error_msg).contains("Username is required")
        LoginPage().enter_user_name("standard_user")
        LoginPage().click_login()
        error_msg = LoginPage().error_msg()
        assert_that(error_msg).contains("Password is required")

    @pytest.mark.regression
    def test_locked_user(self):
        LoginPage().navigate()
        LoginPage().enter_user_name("locked_out_user")
        LoginPage().enter_password("secret_sauce")
        LoginPage().click_login()
        error_msg = LoginPage().error_msg()
        # Validation
        assert_that(error_msg).contains("Sorry, this user has been locked out.")

