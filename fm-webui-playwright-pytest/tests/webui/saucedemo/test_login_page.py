from core.webui.pages.LoginPage import LoginPage
from core.webui.webexecutor.browser_factory import BrowserFactory
from tests.webui.base_webui_test import BaseWebUiTest


class TestLoginPage(BaseWebUiTest):

    def test_success_login(self):
        LoginPage().navigate()
        LoginPage().login_to_site("problem_user", "secret_sauce")




