from core.webui.pages.LoginPage import LoginPage
from tests.webui.base_webui_test import BaseWebUiTest


class TestLoginPage(BaseWebUiTest):

    def test_success_login(self):
        LoginPage().navigate()
        LoginPage().login_to_site("problem_user", "secret_sauce")




