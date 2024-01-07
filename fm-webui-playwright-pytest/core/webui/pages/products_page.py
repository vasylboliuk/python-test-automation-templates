from playwright.sync_api import Locator

from core.webui.pages.base_page import BasePage


class ProductsPage(BasePage):

    def __init__(self):
        super().__init__()
        self.page = self.browser_factory.get_browser_page()

    def app_logo_label(self) -> Locator:
        return self.page.locator('.app_logo')

    def products_label(self):
        return self.page.locator('.title')

