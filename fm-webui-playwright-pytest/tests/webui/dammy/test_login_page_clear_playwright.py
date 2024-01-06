from playwright.async_api import Playwright

from tests.webui.base_webui_test import BaseWebUiTest


class TestLoginPage(BaseWebUiTest):

    def test_success_login(self, playwright: Playwright):
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.saucedemo.com/")
        page.locator("[data-test=\"username\"]").click()
        page.locator("[data-test=\"username\"]").fill("problem_user")
        page.locator("[data-test=\"password\"]").click()
        page.locator("[data-test=\"password\"]").click()
        page.locator("[data-test=\"password\"]").fill("secret_sauce")
        page.locator("[data-test=\"login-button\"]").click()

        # ---------------------
        context.close()
        browser.close()



