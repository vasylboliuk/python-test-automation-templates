from core.utils.web_ui_config_loader import WebUiConfigLoader
from core.webui.webexecutor.browser_factory import BrowserFactory

class BasePage:

    def __init__(self):
        self.web_ui_config = WebUiConfigLoader().get_config()
        self.base_url = self.web_ui_config.base_url
        self.browser_factory = BrowserFactory()

    def navigate_to(self, url: str):

        pass
