import os

from core.config.common_paths import CommonPaths
from core.config.model.webui_config_model import WebUiConfigDto
from core.utils.file_util import FileUtil


class LoaderSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class WebUiConfigLoader(metaclass=LoaderSingleton):

    def __init__(self, env='qa'):
        self.env = env
        print(f"\nAutomation Tests started on Environment: [{self.env.upper()}]")
        self._web_ui_config = self.__load_config_yaml("webui_config.yaml")

    def __load_config_yaml(self, config_file):
        config_path = os.path.join(CommonPaths.environment_path, self.env, config_file)
        return FileUtil.read_yaml_file(config_path)

    def get_config(self) -> WebUiConfigDto:
        return WebUiConfigDto.from_dict(self._web_ui_config)

    def get_env(self):
        return self.env