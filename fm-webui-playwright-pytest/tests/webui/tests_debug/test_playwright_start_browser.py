import playwright
from playwright.async_api import Playwright

from tests.webui.base_webui_test import BaseWebUiTest
from playwright.sync_api import sync_playwright
from playwright.sync_api import Page, expect
import re


class TestLoginPage(BaseWebUiTest):

    def test_playwright_1(self):
        with sync_playwright() as p:
            for browser_type in [p.chromium, p.firefox, p.webkit]:
                browser = browser_type.launch()
                page = browser.new_page()
                page.goto('http://playwright.dev')
                page.screenshot(path=f'example-{browser_type.name}.png')
                browser.close()

    def test_playwright_2(self, page: Page):
        page.goto("https://playwright.dev/")
        # Expect a title "to contain" a substring.
        expect(page).to_have_title(re.compile("Playwright"))

    def test_playwright_recorded_steps(self, playwright: Playwright):
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



