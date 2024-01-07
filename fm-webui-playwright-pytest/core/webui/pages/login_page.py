from core.webui.pages.base_page import BasePage
from core.webui.pages.products_page import ProductsPage


class LoginPage(BasePage):

    def __init__(self) -> None:
        super().__init__()
        self.page = self.browser_factory.get_browser_page()

    def navigate(self):
        self.page.goto(self.base_url)

    def user_name_field(self):
        return self.page.locator('[data-test="username"]')

    def user_password_field(self):
        return self.page.locator('[data-test="password"]')

    def user_login_dtn(self):
        return self.page.locator('[data-test="login-button"]')

    def error_msg(self):
        return self.page.locator('[data-test="error"]').text_content(timeout=self.default_timeout)

    def products_page(self):
        return ProductsPage()

    def enter_user_name(self, user_name):
        self.user_name_field().click()
        self.user_name_field().fill(user_name)

    def enter_password(self, user_password):
        self.user_password_field().click()
        self.user_password_field().fill(user_password)

    def click_login(self):
        self.user_login_dtn().click()

    def login_to_site(self, user_name, user_password):
        self.enter_user_name(user_name)
        self.enter_password(user_password)
        self.click_login()
