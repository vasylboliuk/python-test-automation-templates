from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config


@dataclass_json
@dataclass
class WebDriverConfigDto:
    default_implicit_wait: int = field(metadata=config(field_name="DefaultImplicitWait"))
    default_explicit_wait: int = field(metadata=config(field_name="DefaultExplicitWait"))
    window_size: str = field(metadata=config(field_name="WindowSize"))


@dataclass_json
@dataclass
class WebUiConfigDto:
    base_url: str = field(metadata=config(field_name="BaseURL"))
    web_driver_config: WebDriverConfigDto = field(metadata=config(field_name="WebDriverConfig"))

