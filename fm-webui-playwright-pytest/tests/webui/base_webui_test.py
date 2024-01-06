from core.webui.webexecutor.browser_factory import BrowserFactory


class BaseWebUiTest:

    BROWSER = "Chrome"

    @classmethod
    def setup_class(self):
        BrowserFactory().init_web_browser(self.BROWSER)

    @classmethod
    def teardown_class(self):
        BrowserFactory().close_browser()

