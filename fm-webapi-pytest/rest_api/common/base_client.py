from core.config.model.environment_config import EnvironmentConfigDto
from core.utils.environment_loader import EnvLoader


class BaseApiClient:

    def __init__(self, config_name: str):
        self.config: EnvironmentConfigDto = EnvLoader().get_config_value(config_name)
        self.main_url = self.config.api_url
        self.api_port = self.config.api_port
        self.api_base_path = self.config.api_base_path
        final_url = self.url = f'{self.main_url}'
        if self.api_port is not None:
            final_url = f'{self.main_url}:{self.api_port}'
        self.url = final_url
