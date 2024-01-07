from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config


@dataclass_json
@dataclass
class WebDriverConfigDto:
    default_explicit_wait: int = field(metadata=config(field_name="DefaultExplicitWait"))
    headless_mode: bool = field(metadata=config(field_name="HeadlessMode"))
    window_size: str = field(metadata=config(field_name="WindowSize"))


@dataclass_json
@dataclass
class WebUiConfigDto:
    base_url: str = field(metadata=config(field_name="BaseURL"))
    web_driver_config: WebDriverConfigDto = field(metadata=config(field_name="WebDriverConfig"))

